"""The audit card (EM 2026-11-12: "I'll be the auditor of the lines. since people will be contributing a lot of elements I'll need a
way to verify those elements fast"). One card per element, everything EM needs to decide in about two minutes, and nothing a machine
has already checked:

  tier        how much EM audits, from what the element is: safety (every figure, every version), device (the class A figures:
              ratings, safety and behaviour the twin reports), structure (furniture, plates, rails: the reviewer's pass releases it;
              EM spot-checks)
  model       the element's glb, to turn
  figures     every line that holds the element for EM (approvals.open_lines, the rule DOC-005 counts by), each with the brief line
              it cites when it cites one ("measure.md:18"), and its class
  behaviour   what the element does at its terminals, state by state (behaviour.csv: which contacts close in which state)
  reviewer    the independent reviewer's verdict at this version and its findings' headings
  history     who changed the element (the lane, the commits), and whether a version of it was released before

`python lib/build.py audit <id> [<id> ...]` prints the cards' data (JSON); the core chat publishes the page (the
artifact "Audit card") and merges EM's decisions with `python lib/build.py approvals merge` (toolkit/approvals.py), as before.
"""
import csv, hashlib, json, os, re, subprocess

from . import library, approvals as AP

GH = "https://github.com/complexes-IO/CAD-Assets/blob/main/lib/elements"
STRUCTURE = ("furniture", "plate", "rail", "run", "prop", "tube")


def _read(p):
    try: return open(p, encoding="utf-8", errors="replace").read()
    except OSError: return ""


def _csv(p):
    return list(csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#"))) if os.path.isfile(p) else []


def tier(eid, cls):
    """'safety' | 'device' | 'structure'"""
    inv = {r.get("id"): r for r in _csv(os.path.join(library.ROOT, "inventory.csv"))}
    if (inv.get(eid, {}).get("safety") or "").strip().lower() == "yes": return "safety"
    return "structure" if cls in STRUCTURE else "device"


def fid(eid, file, text):
    """a stable record id for one figure line (the page's db key; approvals.merge keeps it as `record`)"""
    return f"{eid}--{hashlib.sha1((file + '|' + text.strip()).encode('utf-8')).hexdigest()[:12]}"


def cited(text, briefs):
    """the brief lines a figure cites as 'measure.md:18' or 'interior.md:7': [(ref, line text)]"""
    out = []
    for name, n in re.findall(r"\b(measure|interior)\.md:(\d+)", text):
        lines = briefs.get(f"{name}.md", "").splitlines()
        i = int(n)
        if 1 <= i <= len(lines): out.append((f"{name}.md:{i}", lines[i - 1].strip()))
    return out


def behaviour_table(beh_text):
    """{'states': [names], 'contacts': [(a, b, part, when)], 'pins': [marks]} from behaviour.csv"""
    rows = list(csv.DictReader(l for l in beh_text.splitlines() if l.strip() and not l.startswith("#")))
    states = []
    for r in rows:
        s = (r.get("a") or "").strip()
        if r.get("kind") == "state" and s and s not in states: states.append(s)
    contacts = [(r["a"], r["b"], r.get("part", ""), (r.get("when") or "").strip()) for r in rows if r.get("kind") == "contact"]
    pins = [r["a"] for r in rows if r.get("kind") == "pin"]
    return dict(states=states, contacts=contacts, pins=pins)


def review(eid, version):
    """(verdict line, [finding headings], file) of the newest review of eid at this version"""
    d = os.path.join(library.ROOT, "reviews", "elements")
    names = sorted(f for f in (os.listdir(d) if os.path.isdir(d) else []) if re.match(rf"{re.escape(eid)}-{re.escape(version)}(-.*)?\.md$", f))
    if not names: return ("no review at this version yet", [], "")
    f = names[-1]; text = _read(os.path.join(d, f)); first = text.splitlines()[0].strip() if text else ""
    sec = re.search(r"^## Findings[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    heads = [re.sub(r"\s+", " ", m).strip()[:160] for m in re.findall(r"^\d+\.\s+(.*(?:\n(?!\d+\.|\n).*){0,1})", sec.group(1), re.M)][:8] if sec else []
    return (first, heads, f"https://github.com/complexes-IO/CAD-Assets/blob/main/lib/reviews/elements/{f}")


def history(eid, n=5):
    """[(date, author, subject)] of the newest commits that touched the element's hand files, and its release tags"""
    root = os.path.dirname(library.ROOT)
    g = lambda *a: subprocess.run(["git", *a], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    paths = [f"lib/elements/{eid}/{f}" for f in ("spec.md", "element.py", "ratings.csv", "behaviour.csv", "parts.csv", "references/measure.md")]
    log = [ln.split("\t", 2) for ln in g("log", f"-{n}", "--format=%ad\t%an\t%s", "--date=short", "--", *paths).splitlines() if ln.count("\t") >= 2]
    tags = sorted(t for t in g("tag", "--list", f"{eid}/*").split() if t)
    return [(a, b, c[:140]) for a, b, c in log], tags


def card(eid):
    m = library.load(eid); d = os.path.join(library.ELEMENTS, eid)
    spec = _read(os.path.join(d, "spec.md"))
    briefs = {n: _read(os.path.join(d, "references", n)) for n in ("measure.md", "interior.md") if os.path.isfile(os.path.join(d, "references", n))}
    rat = _csv(os.path.join(d, "ratings.csv")); beh = _read(os.path.join(d, "behaviour.csv"))
    t = tier(eid, getattr(m, "CLASS", ""))
    classes = ("A", "B", None) if t == "safety" else AP.NEED                          # a safety element: every figure, B too
    rows = []
    for L in AP.open_lines(spec, list(briefs.items()), rat, beh, classes=classes):
        cls = sorted({(k or "A*") for _, k in L["hits"]}); kinds = sorted({k for k, _ in L["hits"]})
        text = re.sub(r"\*\*|`", "", L["text"]).strip("|- ").replace(" | ", " · ")
        anchor = f"#L{L['line']}" if L["line"] else ""
        rows.append(dict(fid=fid(eid, L["file"], L["text"]), file=L["file"], line=L["line"], cls=cls, kinds=kinds, n=len(L["hits"]),
                         raw=L["text"], text=text, cites=cited(L["text"], briefs), url=f"{GH}/{eid}/{L['file']}{anchor}"))
    verdict, findings, rurl = review(eid, m.VERSION)
    log, tags = history(eid)
    lane = next((r["owner"] for r in _csv(os.path.join(library.ROOT, "OWNERS.csv")) if r.get("path") == f"lib/elements/{eid}/*"), "?")
    return dict(id=eid, version=m.VERSION, title=getattr(m, "TITLE", ""), cls=getattr(m, "CLASS", ""), tier=t, lane=lane,
                spec=f"{GH}/{eid}/spec.md", glb=f"{eid}.glb", rows=rows, behaviour=behaviour_table(beh),
                review=dict(verdict=verdict, findings=findings, url=rurl), history=log, released=tags)


def cards(ids):
    import datetime as dt
    root = os.path.dirname(library.ROOT)
    sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True, text=True).stdout.strip()
    return dict(asof=f"{sha} · {dt.datetime.now():%Y-%m-%d %H:%M}", elements=[card(e) for e in ids])
