"""The catalogue of what is not in store (EM 2026-11-12: "how do they know which elements needs to be made? and how does that not
conflict with other contributors? we almost need a catalog of what's not in store").

One GitHub issue per element the inventory wants and the library has not built: what it is, its ETIM class and the features
that define the class, the machines waiting for it, how to start, and how to claim it. .github/workflows/wanted.yml keeps the
issues in step with main (toolkit/wanted_sync.py): opens the new ones, closes an issue when its element folder lands on main, and
handles claims (a comment "/claim" assigns the commenter; "/unclaim" releases; a claim with no activity for 14 days is released).
The claims are published to the branch wanted-claims (claims.csv), and the lanes skip a claimed element (build.py inventory), so a
person and a lane never build the same thing.

`python lib/build.py store` lists the wanted elements and their labels (`-v`: the issues as the workflow would open them).
(`python lib/build.py wanted` is the other list: the standards' documents the figures wait for.)
"""
import csv, hashlib, json, os, re

from . import library

REPO = "complexes-IO/CAD-Assets"
FIRST = "motor-starter-cell"                                           # the first machine (EM 2026-11-10: public when it is released)
STALE_DAYS = 14


def _csv(p):
    return [r for r in csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#"))] if os.path.isfile(p) else []


def first_machine():
    """the element ids the first machine is made of (lib/machines-from-elements.txt)"""
    p = os.path.join(library.ROOT, "machines-from-elements.txt")
    for ln in (open(p, encoding="utf-8").read().splitlines() if os.path.isfile(p) else []):
        if ln.startswith(FIRST + " "): return {x.strip().split(" ")[0] for x in ln[len(FIRST):].split(",") if x.strip()}
    return set()


def etim():
    E = os.path.join(library.ROOT, "standards", "etim")
    classes = {r["class"]: r for r in _csv(os.path.join(E, "classes.csv"))}
    feats = {}
    for r in _csv(os.path.join(E, "class-features.csv")): feats.setdefault(r["class"], []).append(r)
    return classes, feats


def specs(root=None):
    """[{id, title, labels, body, digest}] for every inventory row with no element folder, highest priority first"""
    rows = [r for r in _csv(os.path.join(library.ROOT, "inventory.csv")) if r.get("id")]
    have = set(library.element_ids())
    classes, feats = etim(); first = first_machine()
    parts = lambda r: [m.group(1) for m in re.finditer(r"([a-z0-9][a-z0-9.\-]*)(?:\s*x\d+)?", r.get("made_of") or "")]
    demand = {}
    for r in rows:
        for c in set(parts(r)): demand[c] = demand.get(c, 0) + int(r.get("systems") or 0)
    rank = lambda r: max(int(r.get("systems") or 0), demand.get(r["id"], 0))
    todo = sorted((r for r in rows if r["id"] not in have), key=lambda r: (r["id"] not in first, -rank(r), r["id"]))
    out = []
    for r in todo:
        eid = r["id"]; safety = (r.get("safety") or "").strip().lower() == "yes"; own = (r.get("own_design") or "").strip().lower()
        c = classes.get((r.get("etim") or "").strip())
        labels = ["wanted", f"lane: {r['lane']}"]
        if eid in first: labels.append("first machine")
        if safety: labels.append("safety")
        elif r["lane"] == "mech" and own in ("yes", "generic") and not r.get("made_of") and rank(r) <= 2: labels.append("good first issue")   # a part with no terminals, made of nothing else
        title = f"Wanted: {eid}" + (f" ({c['description']})" if c else (f" ({r['type']})" if r.get("type") else ""))
        lines = [f"<!-- wanted:{eid} -->",
                 f"**{eid}** is in the library's inventory and not built yet." + (" It is part of the **first machine** (the motor starter cell)." if eid in first else ""),
                 "", "| | |", "|---|---|",
                 f"| needed by | {', '.join((r.get('used_by') or '').split()) or 'the inventory'} ({rank(r)} systems) |",
                 f"| lane | {r['lane']} (the AI lane that builds it if nobody claims it) |",
                 f"| design | {'our own design' if own == 'yes' else 'generic: built to its class and standards' if own == 'generic' else 'measured from a real product, then made our own'} |"]
        if r.get("made_of"): lines.append(f"| made of | {r['made_of']} |")
        if r.get("note"): lines.append(f"| note | {r['note'].replace('|', '/')} |")
        if safety: lines.append("| safety | yes: a safety function (ISO 13849-1 / IEC 62061). EM audits every figure at every version. |")
        if c:
            lines += ["", f"**ETIM class {c['class']}, {c['description']}** ({c['group_description']}). The features that define the class:", ""]
            fs = feats.get(c["class"], [])
            lines += [f"- {f['description']}" + (f" ({f['unit']})" if f.get("unit") else "") for f in fs[:25]]
            if len(fs) > 25: lines.append(f"- ... and {len(fs) - 25} more (lib/standards/etim/class-features.csv)")
        lines += ["", "**How to build it**",
                  "1. Comment `/claim` on this issue: it is assigned to you and nobody else, person or lane, starts it. `/unclaim` gives it back; a claim with no activity for 14 days is released.",
                  f"2. Make `lib/elements/{eid}/` with `element.py` (the geometry, from `toolkit`), `spec.md` (every figure with its source: a standard's clause, a datasheet page, or *our own design* with the reason), `ratings.csv` and `behaviour.csv` where it has ratings and terminals. Copy the shape of a released element of the same kind.",
                  "3. Every figure is sourced or marked `NOT ON FILE`: never guessed. No maker's name, part number or CAD file goes in the library (references only, in `references/`, never committed).",
                  f"4. Run `python lib/build.py {eid}`, `python lib/build.py guard main` and `python lib/build.py selftest`, then open a pull request with `Closes #<this issue>` and a DCO sign-off (`git commit -s`).",
                  "5. The checks run on the pull request; the reviewer and EM audit it; the library builds the AutoCAD, Blender and Godot files itself.",
                  "", "The id follows the naming convention `class[-form][-size][-function]` (lib/OPERATING.md 6); propose a better one in the pull request if this one does not say what the element is."]
        body = "\n".join(lines)
        out.append(dict(id=eid, title=title[:240], labels=labels, body=body, digest=hashlib.sha1(body.encode("utf-8")).hexdigest()[:12]))
    return out


def claims_csv(issues):
    """claims.csv for the branch wanted-claims: id,login,since,issue (from the open wanted issues that are assigned)"""
    rows = ["id,login,since,issue"]
    for i in issues:
        m = re.search(r"<!-- wanted:([a-z0-9][a-z0-9.\-]*) -->", i.get("body") or "")
        if m and i.get("state") == "open" and i.get("assignees"):
            rows.append(f"{m.group(1)},{i['assignees'][0]['login']},{(i.get('updated_at') or '')[:10]},{i['number']}")
    return "\n".join(rows) + "\n"


def claimed(text):
    """{element id: login} from a claims.csv text"""
    return {r["id"]: r["login"] for r in csv.DictReader(text.splitlines()) if r.get("id")}
