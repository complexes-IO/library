"""Run by .github/workflows/wanted.yml only (GitHub's machine, its own token): keeps one issue per wanted element in step with main,
handles /claim and /unclaim, releases stale claims, and writes claims.csv for the branch wanted-claims (toolkit/wanted.py).
Standard library only (urllib), so the workflow installs nothing. Reads GITHUB_TOKEN, GITHUB_REPOSITORY, GITHUB_EVENT_NAME and
GITHUB_EVENT_PATH from the workflow. Never runs text from an issue or a comment: a comment is matched against /claim or /unclaim
and nothing else.

python lib/toolkit/wanted_sync.py sync|comment <claims.csv out path>
"""
import datetime as dt, json, os, sys, time, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from toolkit import wanted as W

API = "https://api.github.com"
REPO = os.environ.get("GITHUB_REPOSITORY", W.REPO)
TOKEN = os.environ.get("GITHUB_TOKEN", "")
MAX_NEW = 40                                                                 # a run opens at most this many (GitHub limits content creation)


def gh(method, path, data=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
                                          "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "complexes-wanted"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: return json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        print(f"  {method} {path}: HTTP {e.code} {e.read()[:200]!r}"); return None


def wanted_issues():
    out, page = [], 1
    while True:
        got = gh("GET", f"/repos/{REPO}/issues?labels=wanted&state=all&per_page=100&page={page}") or []
        out += [i for i in got if "pull_request" not in i]
        if len(got) < 100: return out
        page += 1


def key(issue):
    import re
    m = re.search(r"<!-- wanted:([a-z0-9][a-z0-9.\-]*) -->", issue.get("body") or "")
    return m.group(1) if m else None


def sync():
    specs = {s["id"]: s for s in W.specs()}
    have = set(W.library.element_ids())
    issues = wanted_issues(); by = {}
    for i in issues: by.setdefault(key(i), i)
    made = 0
    for eid, s in specs.items():
        i = by.get(eid)
        if i is None:
            if made >= MAX_NEW: continue
            if gh("POST", f"/repos/{REPO}/issues", {"title": s["title"], "body": s["body"], "labels": s["labels"]}): made += 1; time.sleep(3)
        elif i["state"] == "open" and (i.get("body") or "").strip() != s["body"].strip():
            gh("PATCH", f"/repos/{REPO}/issues/{i['number']}", {"title": s["title"], "body": s["body"]}); time.sleep(1)
    now = dt.datetime.now(dt.timezone.utc)
    for i in issues:
        eid = key(i)
        if not eid or i["state"] != "open": continue
        if eid in have:                                                       # the element folder is on main: built
            gh("POST", f"/repos/{REPO}/issues/{i['number']}/comments", {"body": f"`lib/elements/{eid}/` is on main: built. It is released when it passes its stations (`python lib/build.py station {eid}`)."})
            gh("PATCH", f"/repos/{REPO}/issues/{i['number']}", {"state": "closed", "state_reason": "completed"})
        elif i.get("assignees"):
            last = dt.datetime.fromisoformat(i["updated_at"].replace("Z", "+00:00"))
            if (now - last).days >= W.STALE_DAYS:
                who = i["assignees"][0]["login"]
                gh("DELETE", f"/repos/{REPO}/issues/{i['number']}/assignees", {"assignees": [who]})
                gh("POST", f"/repos/{REPO}/issues/{i['number']}/comments", {"body": f"No activity for {W.STALE_DAYS} days, so the claim is released and the element is open again. @{who}, comment `/claim` to take it back."})
    print(f"wanted: {len(specs)} wanted, {made} issue(s) opened this run, {len(issues)} on file")


def comment():
    ev = json.load(open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8"))
    issue, c = ev.get("issue") or {}, ev.get("comment") or {}
    if "wanted" not in [l["name"] for l in issue.get("labels", [])] or issue.get("state") != "open": return
    word = (c.get("body") or "").strip().split()[:1]
    who = (c.get("user") or {}).get("login", ""); n = issue["number"]; owners = [a["login"] for a in issue.get("assignees") or []]
    if word == ["/claim"]:
        if owners and who not in owners:
            gh("POST", f"/repos/{REPO}/issues/{n}/comments", {"body": f"@{who}, this one is claimed by @{owners[0]}. Pick another from the wanted list, or ask here if they would share it."})
        elif not owners:
            gh("POST", f"/repos/{REPO}/issues/{n}/assignees", {"assignees": [who]})
            gh("POST", f"/repos/{REPO}/issues/{n}/comments", {"body": f"Claimed by @{who}. Nobody else, person or lane, starts it now. `/unclaim` gives it back; {W.STALE_DAYS} days with no activity releases it."})
    elif word == ["/unclaim"] and who in owners:
        gh("DELETE", f"/repos/{REPO}/issues/{n}/assignees", {"assignees": [who]})
        gh("POST", f"/repos/{REPO}/issues/{n}/comments", {"body": "Released: the element is open again."})


if __name__ == "__main__":
    if not TOKEN: sys.exit("GITHUB_TOKEN is not set: this runs in the workflow only")
    {"sync": sync, "comment": comment}[sys.argv[1]]()
    if len(sys.argv) > 2: open(sys.argv[2], "w", encoding="utf-8").write(W.claims_csv(wanted_issues()))
