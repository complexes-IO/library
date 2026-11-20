"""The validation suite (VALIDATION in toolkit/__init__.py): PASS / REVIEW / FAIL for everything check.py and qa.py do not cover.
Every finding carries a rule id from toolkit/rules.py, the scope it belongs to, where, the message and the standard it rests on.
  documentation   docs(): spec version and history, baseline, brief on file, open figures (DOC-0xx)
  interfaces      mates() lib/mates.csv (MATE-010) · pinout() per connections.csv (PIN-001) · v_features.stacks() (STK-010)
  geometry        v_geometry: interference on true solids (GEO-0xx), motion sweep with followers (MOT-010)
  features        v_features: holes (HOLE-010), GD&T fastener fit (GDT-010), sheet-metal DFM (DFM-010)
  electrical      v_electrical: pins (PIN-010/020), electrical rule check (ERC-0xx), ratings on circuits.csv (ELR-0xx)
Status rules: FAIL = a stated requirement is violated; REVIEW = engineering judgement or a missing figure is needed; PASS otherwise.
lib/waivers.csv (rule, scope, match, by, date, reason) turns a named finding into PASS with the waiver recorded; a spec line
'REVIEW accepted: <who, date, why>' signs off open figures. An element is releasable when check, qa and every finding on it are PASS.
Reports: lib/out/validation.json (the run) and out/validate.json in every element and assembly folder."""
import csv, math, fnmatch, importlib.util, json, os, re, time
from . import library, outfile, rules, VERSION as TOOLKIT, VALIDATION

ROOT = library.ROOT
SECTIONS = {   # section name -> port units allowed at both ends of a cable in it
    "480 VAC & 120 VAC power": {"480V-3P+E", "120V-1P+E"},
    "control & 24 VDC supply": {"A", "L", "screw"},
    "Ethernet & communication": {"D", "X"},
    "ground": {"PE", "cable"},
}
CABLES = {     # cable element -> rule on the two port units
    "cordset-m12": lambda a, b: a == b and a in {"A", "D", "L"},
    "cable-pwr-480": lambda a, b: a == b == "480V-3P+E",
    "cable-pe": lambda a, b: {a, b} <= {"PE", "cable"},
}

def worst(statuses):
    return "FAIL" if "FAIL" in statuses else "REVIEW" if "REVIEW" in statuses else "PASS"

# ------------------------------------------------------------------ docs
def docs(eid):
    """[(status, rule, message)]"""
    m = library.load(eid); here = os.path.join(library.ELEMENTS, eid); out = []
    spec = os.path.join(here, "spec.md")
    if not os.path.isfile(spec): return [("FAIL", "DOC-001", "spec.md missing")]
    s = open(spec, encoding="utf-8").read(); first = s.splitlines()[0]
    out.append(("PASS", "DOC-001", "spec header carries the version") if f"v{m.VERSION}" in first else ("FAIL", "DOC-001", f"spec header '{first}' lacks v{m.VERSION}"))
    out.append(("PASS", "DOC-002", "history row for this version") if re.search(rf"^\|\s*{re.escape(m.VERSION)}\s*\|", s, re.M) else ("FAIL", "DOC-002", f"no history row for {m.VERSION}"))
    out.append(("PASS", "DOC-003", "baseline stated") if getattr(m, "BASELINE", "").strip() else ("FAIL", "DOC-003", "BASELINE empty"))
    own = own_design(m.BASELINE, inventory_own(eid))
    refs = os.path.join(here, "references")
    has_brief = any(os.path.isfile(os.path.join(refs, f)) for f in ("measure.md", "interior.md"))
    if not own and not has_brief: out.append(("REVIEW", "DOC-004", "no Stage 0 brief (references/measure.md) on file"))
    rp = os.path.join(here, "ratings.csv")
    rrows = list(csv.DictReader(open(rp, encoding="utf-8"))) if os.path.isfile(rp) else []
    brief = "".join(open(os.path.join(refs, f), encoding="utf-8", errors="replace").read() for f in ("measure.md", "interior.md") if os.path.isfile(os.path.join(refs, f)))
    bp_ = os.path.join(here, "behaviour.csv")                                  # escape mech-r68:4: its open figures count too
    beh = open(bp_, encoding="utf-8", errors="replace").read() if os.path.isfile(bp_) else ""
    from . import approvals                                                   # EM's page decisions (lib/approvals.csv)
    r = doc005(s, ratings=rrows, brief=brief, em=approvals.counts(eid, s, brief, rrows, behaviour=beh), behaviour=beh)
    if r: out.append(r)
    out += [("REVIEW", "DOC-008", f"spec.md gives '{row[:70]}' for the brief's NOT ON FILE '{f}': mark it 'Assumption (A|B|C)' with its reason, "
             "or cite the document (or EM's dated ruling) in the brief and the spec") for f, row in unmarked_nof(s, brief)]
    _fam = getattr(m, "FAMILY", None); _fp = os.path.join(library.ELEMENTS, _fam, "behaviour.csv") if isinstance(_fam, str) else ""
    out += [("REVIEW", "DOC-009", msg) for msg in unruled_design(s, beh) + meets_unruled(s) + leans_on_open(eid) + current_derivable(s, rrows)
            + behaviour_unruled(beh, open(_fp, encoding="utf-8", errors="replace").read() if _fp and os.path.isfile(_fp) else "")]   # escapes 28 to 32
    out += [("REVIEW", "SRC-010", msg) for msg in silent_defaults(os.path.join(here, "element.py"))]
    from . import generic                                                      # generic elements (EM 2026-11-07)
    out += [("REVIEW", "GEN-010", msg) for msg in generic.check(getattr(m, "BASELINE", ""), s)]
    out += [("REVIEW", "GEN-010", msg) for msg in generic.rating_rows(getattr(m, "BASELINE", ""), rrows)]   # escape, pneu-r52
    src = os.path.join(refs, "source.txt")
    bp = os.path.join(here, "bom.csv")
    bom = "\n".join(r_.get("note", "") or "" for r_ in csv.DictReader(open(bp, encoding="utf-8"))) if os.path.isfile(bp) else ""
    out += [("REVIEW", "DOC-006", msg) for msg in vendor_hits(dict(spec=s, BASELINE=getattr(m, "BASELINE", ""), TITLE=getattr(m, "TITLE", ""),
            COMMAND=str(getattr(m, "COMMAND", "") or ""), ratings="\n".join(r_.get("source", "") or "" for r_ in rrows), bom=bom),
            open(src, encoding="utf-8", errors="replace").read() if os.path.isfile(src) else "", others=library_part_numbers(eid))]
    from . import owner                                                        # every element is the Institute's (EM 2026-11-10)
    out += [("REVIEW", "DOC-007", msg) for msg in owner.check(eid, m=m)]
    return out

SILENT = re.compile(r"\b([A-Z][A-Z0-9_]*)\.get\(((?:[^()]|\([^()]*\))*?),\s*(-?\d+(?:\.\d+)?)\s*\)")

def silent_defaults(path, text=None):
    """SRC-010 (EM 2026-11-06: "this info should be from the National Electrical Code; how are we guessing?"): a figure table looked
    up with a number to fall back on, TABLE.get(key, 0.8), builds any key the table lacks with a figure from nowhere. One message per
    lookup; the fix is TABLE[key], or a NOT ON FILE error naming the table and its source."""
    try: text = open(path, encoding="utf-8").read() if text is None else text
    except OSError: return []
    return [f"element.py:{i} {m.group(1)}.get({m.group(2).strip()}, {m.group(3)}): a key not in {m.group(1)} gets {m.group(3)} with no "
            f"source; look it up as {m.group(1)}[...] and stop with NOT ON FILE when it is missing"
            for i, ln in enumerate(text.splitlines(), 1) if not ln.lstrip().startswith("#") for m in SILENT.finditer(ln)]

def vendors():
    """[(kind, name, compiled pattern)] from lib/standards/vendors.csv"""
    p = os.path.join(ROOT, "standards", "vendors.csv"); out = []
    for r in (csv.DictReader(open(p, encoding="utf-8")) if os.path.isfile(p) else []):
        if not r.get("kind") or r["kind"].startswith("#"): continue
        out.append((r["kind"], r["name"], re.compile(r.get("pattern") or re.escape(r["name"]))))
    return out

def part_numbers(source):
    """the element's own part numbers, from its references/source.txt 'Part number:' line (tokens with a digit, 5 characters or more)"""
    out = []
    for ln in source.splitlines():
        if ln.lower().startswith(("part number:", "manufacturer part number:")):
            out += [t for t in re.findall(r"[A-Z0-9][A-Z0-9.\-/]{4,}", ln.split(":", 1)[1].split("(")[0]) if re.search(r"\d", t) and re.search(r"[A-Z]|-", t)]
    return out

def pn_prefix(pn):
    """a part number's family prefix (escape 21, mech r15:1: '440R' of 440R-S13R2 passed in a host's spec): the part before the first
    '-', 4 characters or more of capitals and digits, with at least one of each (so '1200' of 'IRB 1200-7' or a plain word is no
    prefix; the match is case-sensitive, so an element id such as relay-safety-2ch-2no1nc is not one either)."""
    head = pn.split("-", 1)[0] if "-" in pn else ""
    return head if len(head) >= 4 and re.fullmatch(r"[A-Z0-9]+", head) and re.search(r"\d", head) and re.search(r"[A-Z]", head) else ""

_LIB_PN = {}
def library_part_numbers(eid=None):
    """{part number or prefix: element} of every element's references/source.txt but eid's own (escape 21: DOC-006 read only the
    element's own part numbers, so a carried or wired element's number or family prefix passed in a host's spec and bom.csv notes)."""
    if ROOT not in _LIB_PN:
        d = {}
        for e in sorted(os.listdir(library.ELEMENTS)) if os.path.isdir(library.ELEMENTS) else []:
            f = os.path.join(library.ELEMENTS, e, "references", "source.txt")
            if not os.path.isfile(f): continue
            for x in part_numbers(open(f, encoding="utf-8", errors="replace").read()):
                d.setdefault(x, e); p = pn_prefix(x)
                if p: d.setdefault(p, e)
        _LIB_PN[ROOT] = d
    return {k: v for k, v in _LIB_PN[ROOT].items() if v != eid}

def vendor_hits(texts, source="", others=None):
    """DOC-006 (EM 2026-11-05, OPERATING.md 6): vendor and product names, part numbers and approval marks appear only in references/.
    texts: {where: text} of what leaves the brief (spec.md, BASELINE, TITLE, ratings.csv sources, bom.csv notes). One message per
    place and kind. source: the element's own source.txt (its part numbers and their prefixes); others: {part number or prefix:
    element} of the rest of the library (escape 21), matched as whole tokens."""
    V = vendors(); pn = part_numbers(source); out = []
    own = {x: None for x in pn}; own.update({pn_prefix(x): None for x in pn if pn_prefix(x)})
    allpn = dict(others or {}); allpn.update(own)
    tok = lambda x, t: re.search(rf"(?<![A-Za-z0-9]){re.escape(x)}(?![A-Za-z0-9])", t)
    for where, t in texts.items():
        if not t: continue
        names = sorted({n for k, n, rx in V if k == "vendor" and rx.search(t)}); marks = sorted({n for k, n, rx in V if k == "mark" and rx.search(t)})
        found = {x for x in pn if x in t} | {x for x in allpn if x not in pn and tok(x, t)}
        found = {x for x in found if not any(x != y and x in y for y in found)}       # a prefix inside a number found whole is that number
        nums = sorted(x + (f" ({allpn[x]}'s)" if allpn.get(x) else "") for x in found)
        bits = ([f"vendor names {', '.join(names)}"] if names else []) + ([f"part numbers {', '.join(nums)}"] if nums else []) + ([f"approval marks {', '.join(marks)}"] if marks else [])
        if bits: out.append(f"{where}: {'; '.join(bits)}: these live only in references/ with file and page; here say \"maker's datasheet\" and point to the brief")
    return out

def inventory_own(eid, path=None):
    """lib/inventory.csv's own_design for <eid>: True ('yes'), False (a row that isn't marked: a product class with products to match),
    None (no row: common parts and own designs outside the inventory, OPERATING.md 12, are judged by their baseline alone)"""
    try: rows = csv.DictReader(open(path or os.path.join(os.path.dirname(library.ELEMENTS), "inventory.csv"), encoding="utf-8"))
    except OSError: return None
    for r in rows:
        if (r.get("id") or "").strip() == eid: return (r.get("own_design") or "").strip().lower() in ("yes", "generic")   # generic: EM 2026-11-07
    return None

def inventory_unmarked(path=None):
    """request elec-13 (core watch 2026-11-13; elec-10 before it): rows the core added from a request answer (note "request ...")
    with an empty own_design cell. An empty cell reads as a product class with a product to match, so an unattended lane may not
    build the row (autopilot.md 2b2) and skips it: the core's answer states the route in the row, generic, yes or no."""
    try: rows = list(csv.DictReader(open(path or os.path.join(os.path.dirname(library.ELEMENTS), "inventory.csv"), encoding="utf-8")))
    except OSError: return []
    return [r["id"].strip() for r in rows if (r.get("note") or "").strip().lower().startswith("request ")
            and not (r.get("own_design") or "").strip() and not r["id"].startswith("#")]

def own_design(baseline, inventory=None):
    """DOC-004's exemption (OPERATING.md 12: 'Its BASELINE says "our own design"'): only a baseline that STARTS by saying so ('own',
    'our own'). The reviewer's escapes (gl-xr-1 1.2 finding 3, cable-pwr-480 1.1 finding 2): 'own design' or 'our own' anywhere
    exempted baselines that take their figures from a datasheet or spec sheet and say 'own' only of one part.
    Escape group 19 (elec r6:1, core watch 2026-11-07): the words alone exempted thermostat-enc, a product class lib/inventory.csv does not
    mark own_design. An element whose inventory row is not own_design=yes (inventory False) is never exempt; no row (None): the words."""
    if inventory is False: return False
    b = re.sub(r"^[\s*_`\"'(]+", "", baseline or "").lower()
    return bool(re.match(r"(?:our\s+)?own\b", b))   # "own design: ...", "own (EM 2026-11-03): ...", "Our own design ..."

ACCEPT = re.compile(r"REVIEW accepted:\s*(?P<what>.*?)\s*(?:·\s*EM\s+(?P<date>\d{4}-\d{2}-\d{2}))?\s*$")

def _signoffs(s):
    """(EM's approvals, proposals) among a spec's 'REVIEW accepted:' lines (round 10 e). An approval ends '· EM <date>' and names the
    figure it accepts (text before the '·'); a line without EM's mark is a terminal's proposal and accepts nothing (OPERATING.md 8.c)."""
    ok, prop = [], []
    for ln in s.splitlines():
        i = ln.find("REVIEW accepted:")
        if i < 0: continue
        m = ACCEPT.search(ln[i:])
        what = re.sub(r"[\s*`|_-]+$", "", (m.group("what") if m else "")).strip()
        (ok if m and m.group("date") and what else prop).append(what or ln.strip())
    return ok, prop

def open_figures(s, classes=False):
    """(Assumptions, NOT ON FILE) a spec.md marks. Assumption counts in any case (request elec-1: relay-safety-2ch-2no1nc's '**assumption**' went
    uncounted) above '## History', except in headings ('## Notes and assumptions' names a section, not a figure); in the History
    table and after it only the capitalised marking counts, so a closed note ('then an assumption: the drawing gives it') does not.
    A 'REVIEW accepted:' line is a sign-off, not a figure, and is not counted. classes=True: (dict A/B/C/None -> count, NOT ON FILE),
    the class written 'Assumption (A|B|C)' (round 10 b), None for an Assumption with no class."""
    body = re.sub(r"(Figures|Every figure) marked \*\*Assumption\*\*[^.]*\.", "", s)             # boilerplate sentences do not count
    body = "\n".join(ln for ln in body.splitlines() if "REVIEW accepted:" not in ln)
    top, rest = (re.split(r"^(?=## History)", body, maxsplit=1, flags=re.M) + [""])[:2]
    pat_any, pat_cap = re.compile(r"assumption(?:\W{0,3}\(\s*([ABC])\s*\))?", re.I), re.compile(r"Assumption(?:\W{0,3}\(\s*([ABC])\s*\))?")
    hits = []
    for ln in top.splitlines(): hits += (pat_cap if ln.lstrip().startswith("#") else pat_any).findall(ln)
    hits += pat_cap.findall(rest)
    nofs = re.findall(r"NOT ON FILE(?:\W{0,3}\(\s*([ABC])\s*\))?", body); nof = len(nofs)
    if not classes: return len(hits), nof
    c = {"A": 0, "B": 0, "C": 0, None: 0}
    for h in hits: c[h.upper() if h else None] += 1
    n = {"A": 0, "B": 0, "C": 0, None: 0}                                    # EM 2026-11-05: a NOT ON FILE figure takes a class too
    for h in nofs: n[h or None] += 1
    return c, n

def _extra_figures(ratings=(), brief=""):
    """(Assumptions, NOT ON FILE) by class outside spec.md (EM 2026-11-05; reviewer plc0-1.1 finding 2): ratings.csv rows whose status
    is an assumption (ratings are class A unless the status names another class) and the brief's NOT ON FILE table rows (unclassed:
    counted as A; 'NOT ON FILE (C)' is the reviewer's)."""
    c = {"A": 0, "B": 0, "C": 0, None: 0}; n = {"A": 0, "B": 0, "C": 0, None: 0}
    for r in ratings or ():
        st = (r.get("status") or "")
        m = re.match(r"\s*assumption(?:\W{0,3}\(\s*([ABC])\s*\))?", st, re.I)
        if m: c[(m.group(1) or "A").upper()] += 1
    for ln in (brief or "").splitlines():
        if ln.lstrip().startswith("|") and "NOT ON FILE" in ln:
            m = re.search(r"NOT ON FILE(?:\W{0,3}\(\s*([ABC])\s*\))?", ln); n[m.group(1) or None] += 1
    return c, n

_BEH_MARK = re.compile(r"(Assumption|NOT ON FILE)(?:\W{0,3}\(\s*([ABC])\s*\))?", re.I)

def behaviour_open(text):
    """the open figures of a behaviour.csv (escape mech-r68:4, the DOC-005 half; core watch 2026-11-09): gland-m20 1.3 took a
    behaviour.csv whose torque reads NOT ON FILE, with no class, and DOC-005 read only spec.md, ratings.csv and the brief, so the
    open figure (unclassed: counted as A, OPERATING.md 6) needed no line of EM's. One figure per data row whose value cell reads
    'NOT ON FILE' or an assumption, or whose source cell states an 'Assumption' (capitalised: the row's figure is assumed here). A
    source's 'NOT ON FILE' beside a value on file names a side fact the row does not use (psu-24v-2a4's 60 W 'input current ...
    NOT ON FILE'), a lower-case 'status assumption' points to a ratings.csv row DOC-005 counts already (plc0), and the note cell is
    prose (hyd-gauge's 'thread NOT ON FILE; spec.md Open figures'): none of them is a figure of the row. Its class is the first
    '(A|B|C)' written after a mark in the value or source cell, else none (counted as A). '#' lines are the file's header. Returns [(line number, the line as written, kind,
    class)], kind 'Assumption' or 'NOT ON FILE' (the value cell's mark first)."""
    out = []
    lines = (text or "").splitlines()
    for i, ln in enumerate(lines):
        if not ln.strip() or ln.lstrip().startswith("#"): continue
        try: head = next(csv.reader([ln]))
        except Exception: continue
        if [h.strip() for h in head[:2]] == ["kind", "a"]: cols = [h.strip() for h in head]; break
    else: return out
    for i, ln in enumerate(lines):
        if not ln.strip() or ln.lstrip().startswith("#"): continue
        try: row = dict(zip(cols, next(csv.reader([ln]))))
        except Exception: continue
        if [str(row.get(c, "")).strip() for c in cols[:2]] == cols[:2]: continue
        v_, s_ = row.get("value") or "", row.get("source") or ""
        hits = list(_BEH_MARK.finditer(v_)) + [m for m in _BEH_MARK.finditer(s_) if m.group(1) == "Assumption" or _BEH_MARK.search(v_)]
        if not _BEH_MARK.search(v_) and not any(m.group(1) == "Assumption" for m in hits): continue
        kind = "Assumption" if hits[0].group(1).lower() == "assumption" else "NOT ON FILE"
        k = next((m.group(2).upper() for m in hits if m.group(2)), None)
        out.append((i + 1, ln.strip(), kind, k))
    return out

_NOF_STOP = set("a an and as at by for from in into of on or per the to with w h t x d l mm size sizes dimension dimensions figure figures value values".split())
_NOF_MARK = re.compile(r"assumption|not on file|EM \d{4}-\d{2}-\d{2}", re.I)

def _nof_words(text):
    return {w for w in re.findall(r"[a-z][a-z0-9]*", text.lower()) if w not in _NOF_STOP}

def _table_rows(text):
    for ln in text.splitlines():
        s_ = ln.strip()
        if not s_.startswith("|") or re.match(r"^\|[\s:|-]+\|?$", s_): continue
        yield ln, [c.strip() for c in s_.strip("|").split("|")]

# DOC-009 (core watch 2026-11-11; escapes 28 mech/r94:1, 29 mech/r95:1, 30 pneu/r87:1): a figure that leans on another is no better
# sourced than what it leans on. A rule or a standard is named by one of these words; an element on file by its id.
RULE_WORD = re.compile(r"\b(ISO|IEC|EN|DIN|NFPA|NEC|UL|ASME|SAE|VDI|JIS|GB|ANSI|IEEE|CGA|NEMA|EIA|ETIM|NOT ON FILE|OPERATING\.md)\b|"
                       r"lib/standards|derive\.|holes\.csv|\bEM \d{4}-\d{2}-\d{2}")
_DESIGN = re.compile(r"design: ([^()]{0,120}?)\(((?:[^()]|\([^()]*\))*)\)")
_THIS_DESIGN = re.compile(r"this design's (figure|choice)", re.I)

def unruled_design(s, behaviour=""):
    """DOC-009 a (escape 29, mech/r95:1, enc-wm 1.3): a derived figure is only as good as its inputs. On a line of spec.md or
    behaviour.csv that gives a 'derived:' figure, every 'design: <value> (<reason>)' input names the rule it meets (OPERATING.md 6:
    "design: <value> (<the rule it meets>)"): a standard, a table or derive call on file, EM's dated ruling, or NOT ON FILE. enc-wm's
    earth-stud torque 22.3 N·m was derived at 'design: property class 8.8 (the stud's steel, this design's choice)', on studs the
    spec calls welded (ISO 13918's product). An input whose reason calls it "this design's choice" (or figure) and names none of
    those is unruled; an input that points to the element's own build (d_w: "the element's bearing face") is that build's figure.
    Returns one message per unruled input."""
    out = []
    for ln in (s + "\n" + (behaviour or "")).splitlines():
        if "derived:" not in ln: continue
        for m in _DESIGN.finditer(ln):
            if _THIS_DESIGN.search(m.group(2)) and not RULE_WORD.search(m.group(2)):   # the element's own face (d_w) is its build's
                out.append(f"a derived figure takes 'design: {m.group(1).strip()} ({m.group(2).strip()[:60]})' as an input with no rule it meets: "
                           "name the rule (OPERATING.md 6, 'design: <value> (<the rule it meets>)'), or the standard that fixes it as "
                           "'NOT ON FILE (B): <standard>' and the figure waits for it")
    return list(dict.fromkeys(out))

BEH_DECIDES = ("state", "limit", "contact")          # rows whose figure decides what the twin reports (class A when assumed)
_DESIGN_LEAD = re.compile(r"^\s*[\"']?\s*design(?: choice\b|:)", re.I)

def behaviour_unruled(behaviour, family=""):
    """DOC-009 d (escape 31, reviews/elements/mcb-2p-1.0.md finding 1): a behaviour.csv state, limit or contact row decides what the
    twin reports (OPERATING.md 6, class A). One whose source starts "design choice" or "design:" and names no rule it meets (RULE_WORD:
    a standard, a table on file, EM's dated ruling, NOT ON FILE) passed DOC-005, which counts only Assumption and NOT ON FILE markers:
    mcb-2p's reset row read "design choice: trip-free ..." while its family mcb-3p-c10 writes the same row "Assumption (A)". A source
    that only adds "a design choice" after its spec line (a knob's 0° named shut) is a node's pose, class C, and passes. family: the
    behaviour.csv of the element's FAMILY, named in the message when its row of the same kind and name is an Assumption."""
    def rows(text):
        try: return list(csv.DictReader([l for l in (text or "").splitlines() if l.strip() and not l.lstrip().startswith("#")]))
        except csv.Error: return []
    fam = {((r.get("kind") or "").strip(), (r.get("a") or "").strip()): r.get("source") or "" for r in rows(family)}
    out = []
    for r in rows(behaviour):
        k, a, src = (r.get("kind") or "").strip(), (r.get("a") or "").strip(), (r.get("source") or "")
        if k not in BEH_DECIDES or not _DESIGN_LEAD.search(src) or RULE_WORD.search(src): continue
        f = fam.get((k, a), ""); also = " (its family writes this row 'Assumption', as DOC-005 counts it)" if re.search(r"\bAssumption\b", f) else ""
        out.append(f"behaviour.csv {k} '{a}' is sourced '{src.strip()[:60]}' with no rule it meets{also}: a behaviour the twin reports is "
                   "class A; write 'Assumption (A): <value> (<reason>)' for EM, or 'design: <value> (<the rule it meets>)' (OPERATING.md 6)")
    return out

_CURRENT = re.compile(r"\b(full[- ]load|rated|running|nameplate)\b[^.;]{0,30}\bcurrent\b|\bmotor'?s?\b[^.;]{0,40}\bcurrent\b|\bFLA\b", re.I)
_OPEN_A = re.compile(r"NOT ON FILE(?!\s*\((?:B|C)\))|Assumption(?!\s*\((?:B|C)\))")
_CUR_PROP = re.compile(r"^(fla|flc|i_?rated|rated_?current|current|i_?fl|i)$", re.I)

def current_derivable(s, ratings=()):
    """DOC-009 e (escape 32, reviews/elements/hpu-large-1.2.md finding 1, hpu-7.5kw-1.2.md finding 1): a motor's full-load current
    is derived from its rated power and supply (OPERATING.md 6, derive before you ask: "a motor's current from its power"), and
    DOC-005 counted hpu-7.5kw's "NOT ON FILE (A): the drive motor's full-load current at 460 V" for EM while ratings.csv held 7.5 kW
    and 460 V. When ratings.csv gives a power (kW or W) and a voltage (V) and toolkit/derive.motor_current gives the current from
    them (an IE3 efficiency on file for that rating), a spec.md paragraph marked NOT ON FILE or Assumption with no class B or C that
    names the motor's current, or a ratings.csv current row whose status is "assumption", is derivable. The table current NEC
    430.6(A)(1) sizes conductors by (NFPA 70 Table 430.250) is a separate figure, tabulated: a class B line, not caught here.
    0.37 kW has no IE3 efficiency on file, so hpu-0.37kw's 'fla' assumption is not derivable and passes. Returns one message each."""
    from . import derive
    val = {}
    for r in ratings or ():
        p, u = (r.get("property") or "").strip().lower(), (r.get("unit") or "").strip()
        try: v = float((r.get("value") or "").strip())
        except ValueError: continue
        if p in ("power", "p", "rated_power", "power_kw", "p_kw", "output") and u in ("kW", "W"): val["P"] = v / 1000 if u == "W" else v
        elif p in ("voltage", "v", "rated_voltage", "u", "un") and u == "V": val["V"] = v
        elif p == "phases": val["ph"] = int(v)
    if "P" not in val or "V" not in val: return []
    try: d = derive.motor_current(val["P"], val["V"], phases=val.get("ph", 3))
    except (ValueError, ZeroDivisionError): return []
    call = f"`python lib/build.py derive motor {val['P']:g} {val['V']:g}` gives {d['I']} A ({d['source']})"
    out = []
    top = re.split(r"^(?=## History)", s or "", maxsplit=1, flags=re.M)[0]
    for p in _paras(top):
        if "derived:" in p or "Table 430.250" in p and re.search(r"NOT ON FILE\s*\(B\)", p): continue
        if not _OPEN_A.search(p) or not _CURRENT.search(p) or not re.search(r"\bmotor|\bdrive\b|FLA", p, re.I): continue
        out.append(f"spec.md holds the motor's current open for EM ('{p.strip()[:70]}'), but it is derived: {call}; write it with that "
                   "source (OPERATING.md 6), and the table current (NFPA 70 Table 430.250) as its own 'NOT ON FILE (B)' line")
    for r in ratings or ():
        if _CUR_PROP.match((r.get("property") or "").strip()) and (r.get("status") or "").strip().lower() == "assumption" and (r.get("unit") or "").strip() == "A":
            out.append(f"ratings.csv '{r.get('property')}' is an assumption, but the motor's current is derived: {call}; status 'derived' "
                       "with that source (OPERATING.md 6)")
    return out

def meets_unruled(s):
    """DOC-009 b (escape 28, mech/r94:1, stand-magnetic 1.0): a figure in '## What it meets' is another part's interface. A row whose
    source calls it "this design's figure" (or choice) names the standard that tabulates it ('NOT ON FILE (B): <standard>'), the
    standard that leaves it free, or the element on file it meets; stand-magnetic's Ø8 bore for a dial indicator's stem (ISO 463's)
    passed as its own size. A check can't tell a design hole from an interface hole; the table is the lane's word that it is one."""
    m = re.search(r"^## What it meets\s*$(.*?)(?=^## |\Z)", s, re.M | re.S)
    if not m: return []
    ids = set(os.listdir(library.ELEMENTS)) if os.path.isdir(library.ELEMENTS) else set()
    out = []
    for ln, c in _table_rows(m.group(1)):
        if len(c) < 3 or c[0].lower() in ("figure", "what", "item"): continue
        src = c[-1]
        if not _THIS_DESIGN.search(src) or RULE_WORD.search(src): continue
        if any(re.search(rf"(?<![\w-]){re.escape(i)}(?![\w-])", src) for i in ids): continue
        out.append(f"What it meets: '{c[0][:40]}' is another part's interface sourced \"this design's figure\" with no standard named: write "
                   "'NOT ON FILE (B): <the standard that tabulates it>' (OPERATING.md 6, source wanted), or name the standard that leaves it free")
    return out

def leans_on_open(eid):
    """DOC-009 c (escape 30, pneu/r87:1, head-rivet-c-hyd 1.0): DOC-005 counts only an element's own lines, so a host that places a part whose
    spec says its mounting is NOT ON FILE showed nothing open: head-rivet-c-hyd seats hyd-cylinder-da-40 on a face and a bore while the
    cylinder's spec reads 'NOT ON FILE (B): the mounting interface (ISO 6020-2 ...) ... a host can't place the cylinder until it is on
    file'. For each element the host's bom.csv places, a NOT ON FILE paragraph of its spec.md about its mounting needs a NOT ON FILE
    line in the host's spec.md that names the placed element (then DOC-005 counts it: source wanted)."""
    here = os.path.join(library.ELEMENTS, eid); bp = os.path.join(here, "bom.csv"); sp = os.path.join(here, "spec.md")
    if not (os.path.isfile(bp) and os.path.isfile(sp)): return []
    host = _paras(open(sp, encoding="utf-8").read()); out = []
    rows = csv.DictReader(l for l in open(bp, encoding="utf-8") if not l.startswith("#"))
    for e in dict.fromkeys((r.get("element") or "").strip() for r in rows):
        ps = os.path.join(library.ELEMENTS, e, "spec.md")
        if not e or e == eid or not os.path.isfile(ps): continue
        if not mount_open(open(ps, encoding="utf-8").read()): continue
        if any("NOT ON FILE" in p and re.search(rf"(?<![\w-]){re.escape(e)}(?![\w-])", p) for p in host): continue
        out.append(f"places {e}, whose spec has its mounting NOT ON FILE, with no NOT ON FILE line of its own naming {e}: write "
                   f"'NOT ON FILE (B): <what holds {e} here> (<the standard>; {e}'s open figure)' so it waits with it (source wanted)")
    return out

def _paras(t):
    return re.split(r"\n(?=\s*- |\s*\* |\| |\s*\n)", t)

def mount_open(spec):
    """the NOT ON FILE paragraphs of a spec.md that leave its mounting open (a host can't place it as it stands)"""
    return [p for p in _paras(spec) if "NOT ON FILE" in p and re.search(r"mounting|host can.?t place", p, re.I)]

def unmarked_nof(s, brief=""):
    """DOC-008 (escape group 4, tag-plate-1.0:1; core watch 2026-11-08): a figure the brief marks NOT ON FILE is not built as if it were
    on file. A brief table row whose figure cell reads NOT ON FILE names a feature; a row of spec.md's tables above '## History' whose
    label names the same feature (its words all among the feature's, or the feature's all among its) and that gives a number with no
    'Assumption', 'NOT ON FILE' or dated EM ruling ('EM <yyyy-mm-dd>') on its line is an unmarked guess. EM accepting the brief's
    NOT ON FILE line accepts the figure as missing, not the number the spec put in its place: tag-plate's '| tag | 120 × 60 × 1.5 |'
    passed DOC-005 under the brief's 'institute tag plate W x H x T | NOT ON FILE'. A brief row that lists parts ('coil turns, wire
    gauge, inductance, bobbin size') is matched by a spec row naming one part fully, not by every row that shares a word (relay-ice-
    cube's '| coil | 24 V DC, 640 Ω |' is on file). Returns [(feature, spec row)]."""
    feats = []
    for ln, c in _table_rows(brief or ""):
        if len(c) > 1 and re.match(r"[*_\s]*NOT ON FILE", c[1]) and "NOT ON FILE" not in c[0]:
            items = [_nof_words(x) for x in re.split(r",|;| / ", c[0])]; items = [x for x in items if x]
            if items: feats.append((c[0], _nof_words(c[0]), items if len(items) > 1 else None))
    top = re.split(r"^(?=## History)", s, maxsplit=1, flags=re.M)[0]
    hits = []
    for ln, c in _table_rows(top):
        if len(c) < 2: continue
        lab = _nof_words(c[0])
        if not lab or not re.search(r"\d", " ".join(c[1:])) or _NOF_MARK.search(ln): continue
        for f, w, items in feats:                                             # a list of parts (relay-ice-cube-2co's 'coil turns, wire gauge,
            if items: ok = any(it <= lab for it in items)                       # inductance, bobbin size'): the spec row names one part fully
            else: ok = lab <= w or w <= lab                                     # one feature: the words of one name all among the other's
            if ok: hits.append((f, ln.strip())); break
    return hits

def doc005(s, ratings=(), brief="", em=(0, 0), behaviour=""):
    """DOC-005 on a spec.md's text, the element's ratings.csv rows and its brief's text: None when it has no open figure. Round 10 (b, e)
    and EM 2026-11-05: an Assumption, and a NOT ON FILE figure, carries its class. C (appearance, and motion or internal mechanism the
    twin doesn't read: handle and toggle swing, pot angle, legend and decal positions, housing walls, springs, armatures) is accepted
    with the reviewer's PASS, which station 7 asks for anyway; A (ratings, safety, behaviour), B (fits and envelope: it needs a
    source) and an Assumption with no class (counted as A: behaviour the twin reports), and every NOT ON FILE not marked (C), each
    need one line of EM's: 'REVIEW accepted: <the figure> · EM
    <date>'. A 'REVIEW accepted:' without '· EM <date>' is a proposal and clears nothing. em: (figures EM accepted, figures he
    refused) on the station 7 sign-off page (toolkit/approvals.py, lib/approvals.csv; EM 2026-11-06); a refusal is named first, so
    the line board (which cuts a hold at 110 characters) sees it is the lane's to change."""
    c, n = open_figures(s, classes=True)
    (cr, _), (_, nb) = _extra_figures(ratings, ""), _extra_figures((), brief)
    for k in c: c[k] += cr[k]; n[k] += nb[k]
    bo = behaviour_open(behaviour)                                              # escape mech-r68:4: behaviour.csv's open figures
    for _, _, kind, k in bo: (c if kind == "Assumption" else n)[k] += 1
    # EM 2026-11-09 ("all engineering is mathematics made visible ... let's make sure we are not stopping for data that is derived from
    # known formulas or based in standards"): class B (a fit or envelope whose figure a standard tabulates) is no longer a line of EM's
    # per figure: it is a document wanted once (lib/standards/wanted.md, build.py wanted) and holds the element as "source wanted", not
    # as EM's. A figure a formula or a table on file gives is written derived, not NOT ON FILE (OPERATING.md 6), and is not counted.
    nof = n["A"] + n[None]; cc = c["C"] + n["C"]; wanted = c["B"] + n["B"]        # class C is the reviewer's; B wants a source
    need = c["A"] + c[None] + nof
    if not need and not cc and not wanted: return None
    ok, prop = _signoffs(s)
    yes, no = em
    ok = ok + ["(lib/approvals.csv)"] * yes
    where = "spec.md" + (", ratings.csv" if any(cr.values()) else "") + (", the brief" if any(nb.values()) else "") + (", behaviour.csv" if bo else "")
    parts = [f"{c[k]} Assumption ({k})" for k in "ABC" if c[k]] + ([f"{c[None]} Assumption with no class (counted as A)"] if c[None] else []) + ([f"{nof} NOT ON FILE"] if nof else []) + ([f"{n['B']} NOT ON FILE (B)"] if n["B"] else []) + ([f"{n['C']} NOT ON FILE (C)"] if n["C"] else [])
    src = f"; {wanted} class B want a source (lib/standards/wanted.md), not EM's line" if wanted else ""
    if need <= len(ok):
        if wanted and wanted > max(0, len(ok) - need):                            # B figures EM has not accepted: held for the document
            return ("REVIEW", "DOC-005", f"source wanted: {wanted} class B figure(s) in {where} ({', '.join(parts)}); the document is asked for once in lib/standards/wanted.md; EM may still accept a figure ('REVIEW accepted: <figure> · EM <date>'); {len(ok)} approved")
        return ("PASS", "DOC-005", f"open figures in {where}: {', '.join(parts)}; {len(ok)} approved by EM" + (f"; class C accepted with the reviewer's PASS" if cc else ""))
    return ("REVIEW", "DOC-005", (f"{no} refused by EM (lib/approvals.csv), the lane's to change; " if no else "") + f"open figures in {where}: {', '.join(parts)}; {need} need EM, {len(ok)} approved ('REVIEW accepted: <figure> · EM <date>', one line each)"
            + (f"; {len(prop)} proposal(s) without '· EM <date>' clear nothing" if prop else "") + src)

# ------------------------------------------------------------------ mates
def mates(path=None):
    path = path or os.path.join(ROOT, "mates.csv"); res = []
    if not os.path.isfile(path): return res
    for r in csv.DictReader(open(path, encoding="utf-8")):
        if not r.get("a_element") or r["a_element"].startswith("#"): continue
        from .v_features import resolve
        try:
            a = resolve(r["a_element"], r["a_attr"]); b = resolve(r["b_element"], r["b_attr"])
        except Exception as e:
            res.append(("REVIEW", r, f"cannot read: {e}")); continue
        kind = (r.get("kind") or "equal").strip(); tol = float(r.get("tol") or 0.1); miss = "FAIL" if r.get("required", "yes") == "yes" else "REVIEW"
        A, B = f"{r['a_element']}.{r['a_attr']} = {a}", f"{r['b_element']}.{r['b_attr']} = {b}"
        if kind == "within":
            lo, hi = (float(x) for x in b); ok = lo - tol <= float(a) <= hi + tol; res.append(("PASS" if ok else miss, r, f"{A} {'within' if ok else 'outside'} {B}"))
        elif kind in ("le", "ge"):
            ok = float(a) <= float(b) + tol if kind == "le" else float(a) + tol >= float(b); res.append(("PASS" if ok else miss, r, f"{A} {'≤' if kind == 'le' else '≥'} {B}: {'yes' if ok else 'no'}"))
        else:
            d = abs(float(a) - float(b)); res.append(("PASS" if d <= tol else miss, r, f"{A} vs {B}: diff {d:.2f} (tol {tol})"))
    return res

def mate_elements(r):
    """the elements a MATE-010 finding holds (station 2). A row that names an element not in the library yet holds neither side
    (request elec-12, core watch 2026-11-12: the guard rows for contactor-18a-1no went on core before elec's round reached main, and
    the REVIEW 'not in the library yet' would have taken overload-9a-1no1nc, which did nothing wrong, back below station 2). The
    REVIEW still shows in validate -v until the element arrives; once it does, a figure that disagrees holds both, as before."""
    ids = (r["a_element"], r["b_element"])
    return () if any(not os.path.isfile(os.path.join(ROOT, "elements", e, "element.py")) for e in ids) else ids

# ------------------------------------------------------------------ pinout
def _assembly_prims(aid):
    p = os.path.join(ROOT, "assemblies", aid, "assembly.py")
    spec = importlib.util.spec_from_file_location(f"asm_{aid.replace('-', '_')}", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.build(report=False)

def pinout(aid, P=None):
    path = os.path.join(ROOT, "assemblies", aid, "connections.csv")
    if not os.path.isfile(path): return []
    P = P or _assembly_prims(aid); piv = P.pivots; res = []; used = {}
    for i, c in enumerate(csv.DictReader(open(path, encoding="utf-8")), 1):
        tag = f"row {i} {c['from']} -> {c['to']}"; ends = []
        if c["section"] not in SECTIONS: res.append(("FAIL", tag, f"unknown section '{c['section']}'")); continue
        for end in (c["from"], c["to"]):
            pv = piv.get(end)
            if pv is None: res.append(("REVIEW", tag, f"{end}: not in the model (planned element or wrong name)")); ends.append(None); continue
            if pv["kind"] != "port": res.append(("FAIL", tag, f"{end}: is a {pv['kind']} node, not a port (cables land on ports)")); ends.append(None); continue
            ends.append(pv["unit"]); used.setdefault(end, []).append(i)
        a, b = ends
        if a is None or b is None: continue
        for u in (a, b):
            if u not in SECTIONS[c["section"]]: res.append(("FAIL", tag, f"unit {u} does not belong in section '{c['section']}'"))
        rule = CABLES.get(c["cable"])
        if rule is None: res.append(("REVIEW", tag, f"cable '{c['cable']}' has no compatibility rule yet"))
        elif not rule(a, b): res.append(("FAIL", tag, f"{c['cable']} cannot join {a} to {b}"))
        else: res.append(("PASS", tag, f"{c['cable']}: {a} to {b}"))
    for end, rows in used.items():
        if len(rows) > 1: res.append(("FAIL", end, f"port used by {len(rows)} cables (rows {rows})"))
    return res

GENDERS = ("male", "female", "none")

def port_genders(eid, P):
    """PIN-002 (EM 2026-11-05; reviewer plc0-1.1 finding 3): every kind-port pivot declares its gender: male, female, or none (a screw
    clamp, a stud, a cable gland). Without it PIN-030 cannot see a live socket that should be pins."""
    bad = [n for n, p in sorted(P.pivots.items()) if p.get("kind") == "port" and p.get("gender") not in GENDERS]
    if not bad: return [("PASS", "PIN-002", eid, f"every port declares its gender")] if any(p.get("kind") == "port" for p in P.pivots.values()) else []
    return [("REVIEW", "PIN-002", f"{eid} {' '.join(bad)}", f"{len(bad)} port(s) without a gender ({', '.join(bad[:6])}{' ...' if len(bad) > 6 else ''}): declare gender=male, female or none on the pivot")]

def core_assumptions(eid, P):
    """CORE-010: every contact the element carries meets what the Rust core's Kani proofs assume (lib/core/src/proofs.rs
    any_contact): a contact zone that runs forward from the origin and ends within 20 mm, a wipe above 0 and at most 2 mm, a socket
    face 0 to 2 mm in front of its mouth, an axis along the mating axis (within 3°) unless the pin is bent, and a bent pin never
    along it. The proofs hold for every element that passes this, so a new element needs no new proof."""
    from . import contact as C
    import numpy as np
    out = []; n = 0
    for node, pv in C.contacts(P).items():
        if pv.get("gender") not in ("pin", "socket"): continue
        n += 1; bad = []
        s0, s1 = (float(v) for v in pv["range"]); w = float(pv.get("wipe", 0.5)); f = float(pv.get("face", 0.0))
        ref = np.array([0.0, 1.0, 0.0]); parts = node.split(".")
        for k in range(len(parts) - 1, -1, -1):                       # the mating axis of the port this contact belongs to
            port = ".".join(parts[:k]) or "self"
            if port in P.pivots and P.pivots[port]["kind"] == "port": ref = np.array(P.pivots[port]["axis"], float); ref /= np.linalg.norm(ref); break
        a = np.array(pv["axis"], float); a /= np.linalg.norm(a); along = abs(float(a @ ref)) >= math.cos(math.radians(3))
        if not (0 <= s0 < s1 <= 20.0): bad.append(f"zone {s0:g} to {s1:g} mm")
        if not (0 < w <= 2.0): bad.append(f"wipe {w:g}")
        if not (0 <= f <= 2.0): bad.append(f"face {f:g}")
        if (pv.get("condition") == "bent") == along: bad.append("a bent pin along the axis" if along else f"axis {np.round(a, 3).tolist()} off the mating axis")
        if bad: out.append(("FAIL", "CORE-010", node, "outside what the core's proofs assume: " + ", ".join(bad)))
    if n and not out: out.append(("PASS", "CORE-010", eid, f"{n} contact(s) meet the Rust core's proof assumptions"))
    return out

def joints(aid, P=None, path=None):
    """PIN-030: every cable end mates with the port it lands on, as the parts are built: opposite genders, the same coding (the key
    fits), and every pole its wiring map uses made at the seat (toolkit/contact.py: nut fully turned, torque at its minimum).
    Also reports the engagement window: the gap at which the pins first touch and at which they are made."""
    from . import contact as C
    path = path or os.path.join(ROOT, "assemblies", aid, "connections.csv")
    if not os.path.isfile(path): return []
    P = P or _assembly_prims(aid); out = []
    maps = {}
    sp = os.path.join(ROOT, "standards", "cables.csv")
    if os.path.isfile(sp):
        for r in csv.DictReader(open(sp, encoding="utf-8")):
            if r.get("cable") and not r["cable"].startswith("#"): maps[(r["cable"], r["unit"])] = [tuple(x.split("-", 1)) for x in r["map"].split()]
    for i, c in enumerate(csv.DictReader(open(path, encoding="utf-8")), 1):
        try: mod = library.load(c["cable"])
        except Exception: continue
        if "genders" not in getattr(mod, "PARAMS", {}): continue                       # not a cable built from mating halves (yet)
        ends = [(c["from"], "port-a"), (c["to"], "port-b")]
        if any(e not in P.pivots or P.pivots[e]["kind"] != "port" for e, _ in ends): continue   # PIN-001 reports a missing port
        unit = P.pivots[c["from"]].get("unit")
        prm = {**getattr(mod, "PARAMS", {}), "coding": unit, **library.parse_params(c.get("params", ""))}
        try: cable = mod.build(**prm)
        except Exception as e: out.append(("FAIL", "PIN-030", f"row {i} {c['cable']}", f"cannot build with {c.get('params', '')}: {e}")); continue
        mp = maps.get((c["cable"], prm["coding"]), [])
        for k, (port, end) in enumerate(ends):
            used = sorted({(a if k == 0 else b) for a, b in mp}) if mp else None
            seat = C.mate(P, port, cable, end, turns=99, torque=None)
            pg, cg = P.pivots[port].get("gender"), cable.pivots[end].get("gender")
            where = f"row {i} {c['cable']} {end} ({cg or '?'} {prm['coding']}) -> {port} ({pg or '?'} {P.pivots[port].get('unit')})"
            if pg is None: out.append(("REVIEW", "PIN-030", where, "the port carries no mating data (gender, key, thread): rebuild it from receptacle-m12")); continue
            if not seat["gender"]: out.append(("FAIL", "PIN-030", where, f"both {pg}: this cable end cannot go on this port (order the cable with genders to suit, params column)")); continue
            if not seat["key"]: out.append(("FAIL", "PIN-030", where, "; ".join(seat["notes"]))); continue
            bad = [p_ for p_ in (used or seat["poles"]) if seat["poles"].get(p_, {}).get("state") not in ("made", "high-r")]
            if bad: out.append(("FAIL", "PIN-030", where, f"at the seat pole(s) {', '.join(bad)} not made: " + ", ".join(f"{p_} {seat['poles'].get(p_, {}).get('state', 'missing')}" for p_ in bad) + ("; " + "; ".join(seat["notes"]) if seat["notes"] else "")))
            else:
                w = C.window(P, port, cable, end)
                ft = max((v["first_touch"] or 0) for v in w.values()) if w else 0; ma = min((v["made_at"] or 0) for v in w.values()) if w else 0
                pitch = float(P.pivots[port].get("pitch", 1.0)); tg = float(seat["thread_catch"])
                when = (f"made {ma:.2f} mm out, before the nut catches the thread at {tg:g}: pushed on by hand it works, held by friction only"
                        if ma > tg + 1e-6 else f"made by {ma:.2f} mm out ({(tg - ma) / pitch:.1f} of {tg / pitch:g} turns)")
                out.append(("PASS", "PIN-030", where, f"{len(used or seat['poles'])} pole(s) made at the seat; pins touch {ft:.2f} mm out, {when}; thread engaged {seat['thread_engaged']:g} mm at the seat"))
    return out

# ------------------------------------------------------------------ the suite
def waivers():
    p = os.path.join(ROOT, "waivers.csv")
    return [r for r in csv.DictReader(open(p, encoding="utf-8")) if r.get("rule") and not r["rule"].startswith("#")] if os.path.isfile(p) else []

JUDGED = ("ERC-", "ELR-", "PIN-030", "GEO-020", "PNE-", "HYD-")      # assembly findings that name the elements they judged (round 10 d)

def judged(P, where, extra=()):
    """the element ids an assembly finding judged (round 10 d: a failure in an assembly held no element). Each token of `where` that
    is an instance tag, or a node under one, maps to the outermost ELEMENT placed on that path (panel-1.k1 -> contactor-9a-1no1nc; a port
    machine-1.io-1.port-x03 -> io-block-m12-8di8do, the device whose port it is): the device placed in the assembly, never a sub-assembly and
    never a part inside the device. `extra`: element ids the checker names itself (a cable)."""
    ids = set(library.element_ids()); tags = {}
    for _, _, t, e in getattr(P, "owners", []): tags.setdefault(t, e)
    out = [e for e in extra if e in ids]
    for tok in re.split(r"[\s,;()×↔>]+", where or ""):
        tok = tok.strip(".:-")
        chain = sorted((t for t in tags if tok == t or tok.startswith(t + ".")), key=len)
        e = next((tags[t] for t in chain if tags[t] in ids), None)
        if e and e not in out: out.append(e)
    return out

def assembly_findings(aid, P, rows):
    """[(status, rule, where, message)] of one assembly -> findings, those of JUDGED rules naming their elements"""
    F = []
    for st, rule, where, msg in rows:
        extra = where.split()[2:3] if rule == "PIN-030" and where.startswith("row ") else ()          # the cable: "row <n> <cable> ..."
        F.append(_F(st, rule, aid, where, msg, judged(P, where, extra) if rule.startswith(JUDGED) else ()))
    return F

def _F(status, rule, scope, where, message, elements=()):
    return dict(status=status, rule=rule, scope=scope, where=where, message=message, elements=list(elements), title=rules.title(rule), basis=rules.basis(rule))

M12_PAIRS = [("A", "device", "cordset"), ("A", "cordset", "cordset"), ("A", "cordset", "device"), ("D", "device", "cordset"),
             ("L", "device", "cordset"), ("L", "cordset", "device"), ("L", "cordset", "cordset")]   # (coding, female kind, male kind)

def m12_fits(step=0.1, pairs=None):
    """M12-010: each M12 joint on file seated: the female insert and the male insert (turned to face it) share no material. Sampled
    on a 0.1 mm grid over the key region (r 4.45, 0.05 to 8.6 into the female); the seal's squeeze is not in the inserts. Round 7: the
    cordset L female's keyway as read did not fit its own male (0.302 over the ledge)."""
    import numpy as np
    from .prims import transform
    from .solid import Scene, inside
    ins = library.load("insert-m12"); out = []
    g = np.arange(-4.45, 4.45 + 1e-9, step); y = np.arange(0.05, 8.6, 2 * step)
    xx, zz = np.meshgrid(g, g); keep = xx ** 2 + zz ** 2 < 4.45 ** 2
    X = np.array([(x, yy, z) for x, z in zip(xx[keep], zz[keep]) for yy in y])
    def mat(P):
        S = Scene(P); m = np.zeros(len(X), bool)
        for i in S.idx:
            k, q, H = S.geom(i); lo, hi = S.bounds(i); sel = np.all((X >= lo - 1e-6) & (X <= hi + 1e-6), axis=1)
            if not sel.any(): continue
            mi = inside(k, q, X[sel])
            for hk, hq in H: mi &= ~inside(hk, hq, X[sel])
            m[np.nonzero(sel)[0][mi]] = True
        return m
    for coding, fk, mk in (pairs or M12_PAIRS):
        F_ = ins.build(**{**ins.PARAMS, "gender": "female", "coding": coding, "kind": fk})
        M_ = transform(ins.build(**{**ins.PARAMS, "gender": "male", "coding": coding, "kind": mk}), (0, 0, 0), 180.0)
        both = mat(F_) & mat(M_); vol = both.sum() * step * step * 2 * step; name = f"{coding} {fk} female + {mk} male"
        if both.any():
            c = X[both]; out.append(("FAIL", name, f"the inserts share about {vol:.2f} mm³ when seated, round x {c[:, 0].min():.2f} to {c[:, 0].max():.2f}, z {c[:, 2].min():.2f} to {c[:, 2].max():.2f}"))
        else: out.append(("PASS", name, "the inserts mate without overlapping (0.1 mm grid)"))
    return out

def run(element_ids, assembly_ids, geometry=True, log=None):
    """every checker on every element and assembly: a list of findings (dicts), waivers applied"""
    from . import v_geometry as G, v_electrical as E, v_features as V
    F = []; t0 = time.time()
    for eid in element_ids:
        m = library.load(eid); P = m.build(**getattr(m, "PARAMS", {}))
        for st, rule, msg in docs(eid): F.append(_F(st, rule, eid, eid, msg))
        if geometry:
            for st, rule, where, msg in G.interference(P, eid) + G.motion(P, eid, G.element_parents(m)) + G.follow_contact(P, eid) + G.screw_stroke(P, eid) + G.zfight(P, eid) + G.openings(P, eid) + G.bodies(P, eid): F.append(_F(st, rule, eid, where, msg))
        for st, rule, where, msg in core_assumptions(eid, P) + port_genders(eid, P): F.append(_F(st, rule, eid, where, msg))
        from . import behaviour as BH                                                 # the behaviour spec (EM 2026-11-09)
        for st, rule, where, msg in BH.check(eid, P): F.append(_F(st, rule, eid, where, msg))
        h, groups = V.holes(eid, P)
        for st, rule, where, msg in h + V.gdt(eid, P, groups) + V.dfm(eid, P) + V.breakout(eid, P): F.append(_F(st, rule, eid, where, msg))
        if geometry:
            from . import fillet as FIL
            c = FIL.summary(P, cls=getattr(m, "CLASS", ""))
            F.append(_F("PASS", "FIL-010", eid, eid, f"the AutoCAD gate will pick {c.get('pick', 0)} edges; skipped {c.get('buried', 0)} buried, {c.get('short', 0)} short, {c.get('thin', 0)} on thin parts, {c.get('shared', 0)} shared, {c.get('hidden', 0)} hidden; {c.get('child', 0)} on placed elements, left to their own gates; {c.get('batches', 0)} FILLETEDGE batches"))
        if log: log(f"  {eid:24} {time.time() - t0:5.1f} s")
    for st, r, msg in mates(): F.append(_F(st, "MATE-010", "library", r["feature"], msg, mate_elements(r)))
    for st, rule, where, msg in V.stacks(): F.append(_F(st, rule, "library", where, msg))
    if geometry:
        for st, where, msg in m12_fits(): F.append(_F(st, "M12-010", "library", where, msg))
    for aid in assembly_ids:
        F += assembly_run(aid, geometry, waive=False)
        if log: log(f"  {aid:24} {time.time() - t0:5.1f} s")
    return apply_waivers(F)

def assembly_run(aid, geometry=True, waive=True, P=None):
    """every assembly rule on one assembly (scope "assembly"): its findings. `python lib/build.py assembly <id>` (request panel-5 2a:
    a placement or wiring change had only the full build to answer it)"""
    from . import v_geometry as G, v_electrical as E
    F = []; P = P if P is not None else _assembly_prims(aid)
    if geometry:
        F += assembly_findings(aid, P, G.interference(P, aid) + G.motion(P, aid, G.assembly_parents(aid), level="assembly"))
    res = pinout(aid, P)
    for st, tag, msg in res: F.append(_F(st, "PIN-001", aid, tag, msg))
    if res:
        erc, spare = E.erc(aid, P)
        F += assembly_findings(aid, P, erc)
        for sp in spare: F.append(_F("PASS", "ERC-000", aid, "spare", sp))
    F += assembly_findings(aid, P, E.ratings(aid, P))
    F += assembly_findings(aid, P, joints(aid, P))
    from . import v_pneu as PNV
    F += assembly_findings(aid, P, PNV.run(aid, P, ROOT))                    # an air circuit on file (request pneu-1)
    from . import v_hyd as HYV
    F += assembly_findings(aid, P, HYV.run(aid, P, ROOT))                    # a hydraulic circuit on file (request pneu-8)
    from . import v_panel as PLV
    F += assembly_findings(aid, P, PLV.run(aid, P, ROOT))                    # a wire list on file (request panel-4 4)
    from . import rooms as RMV
    F += assembly_findings(aid, P, RMV.run(aid, P, ROOT))                    # a lab room (room.csv; EM 2026-11-12: the campus becomes a virtual school)
    F += assembly_findings(aid, P, PLV.bom_run(aid, ROOT))                   # every BOM row an element or a planned row (panel/r6 ESCAPE)
    F += assembly_findings(aid, P, PLV.bom_station_run(aid, ROOT))           # what it places past station 6, as drawn (panel/r18 ESCAPE)
    F += assembly_findings(aid, P, assembly_gate(aid))                       # the gate ran the LISP on file (panel/r15 ESCAPE)
    return apply_waivers(F) if waive else F

GATE_SOLID = re.compile(r'^\s*(?:\(setq e\d+ )?\((?:BX|CY|UB) "([A-Za-z0-9_:.-]+)"', re.M)   # acad-gate.py's census of a LISP, as it counts

def lisp_census(src):
    """{layer: solids} a LISP will build, counted as acad-gate.py counts it (its 'lisp_per_layer')"""
    out = {}
    for m in GATE_SOLID.finditer(src): out[m.group(1)] = out.get(m.group(1), 0) + 1
    return out

def assembly_gate(aid, root=None):
    """GATE-010 (ESCAPE panel/r15 2, core watch 2026-11-12): an assembly's AutoCAD gate on file ran the LISP on file. The first gate of
    pnl-press-hydraulic ran out/<id>.lsp as a merge had left it (v0.4's, no q1 solids) while assembly.py said 0.5, and the result read
    PASS: an assembly's LISP had no version line and gate/<id>-acad.json no version or fingerprint. The census the gate recorded
    (lisp_per_layer) is compared with the census of out/<id>.lsp as the build wrote it; a version the result or the LISP's first line
    names is compared with assembly.py's VERSION. [(status, rule, where, message)]"""
    d = os.path.join(root or ROOT, "assemblies", aid)
    try: g = json.load(open(os.path.join(d, "gate", f"{aid}-acad.json"), encoding="utf-8"))
    except (OSError, ValueError): return []
    if not g.get("pass"): return []
    try: src = open(os.path.join(d, "out", f"{aid}.lsp"), encoding="utf-8", errors="replace").read()
    except OSError: return [("REVIEW", "GATE-010", "gate", f"the AutoCAD gate of {g.get('date', '?')} passed, and no out/{aid}.lsp is on file to say what it ran")]
    m = re.search(r'(?<![\w.])VERSION\s*=\s*["\']([^"\']+)', open(os.path.join(d, "assembly.py"), encoding="utf-8", errors="replace").read()) \
        if os.path.isfile(os.path.join(d, "assembly.py")) else None
    ver = m.group(1) if m else None; why = []
    hv = re.search(rf"{re.escape(aid)} v([\d.]+)", src.split("\n", 1)[0])
    if ver and hv and hv.group(1) != ver: why.append(f"out/{aid}.lsp says v{hv.group(1)}, assembly.py {ver}: rebuild")
    if ver and g.get("version") and str(g["version"]) != ver: why.append(f"the gate ran v{g['version']}, assembly.py is {ver}")
    lp = g.get("lisp_per_layer")
    if isinstance(lp, dict):
        now = lisp_census(src); diff = sorted(k for k in set(lp) | set(now) if lp.get(k) != now.get(k))
        if diff: why.append(f"the gate's census ({sum(lp.values())} solids) is not the LISP on file's ({sum(now.values())}); "
                            f"{len(diff)} layer(s) differ, first {diff[0]} {lp.get(diff[0], 0)} -> {now.get(diff[0], 0)}")
    if why: return [("REVIEW", "GATE-010", "gate", f"the AutoCAD gate of {g.get('date', '?')} passed on another LISP than the one on file: "
                     + "; ".join(why) + f". Build the assembly, then gate the LISP the build wrote again (acad-gate.py --assembly {aid})")]
    return [("PASS", "GATE-010", "gate", f"the AutoCAD gate of {g.get('date', '?')} ran the LISP on file ({sum(lp.values()) if isinstance(lp, dict) else '?'} solids)")]

def apply_waivers(F):
    W = waivers()
    for f in F:
        if f["status"] == "PASS": continue
        for w in W:
            if w["rule"] == f["rule"] and fnmatch.fnmatch(f["scope"], w["scope"]) and w.get("match", "") in (f["where"] + " " + f["message"]):
                f["waived"] = f"{w['by']}, {w['date']}: {w['reason']}"; f["status_before_waiver"] = f["status"]; f["status"] = "PASS"; break
    return F

def statuses(F, element_ids, assembly_ids):
    per = {e: [] for e in list(element_ids) + list(assembly_ids)}
    for f in F:
        if f["scope"] in per: per[f["scope"]].append(f["status"])
        for e in f["elements"]:
            if e in per: per[e].append(f["status"])
    return {k: worst(v) if v else "PASS" for k, v in per.items()}

def write_reports(F, st, element_ids, assembly_ids):
    stamp = time.strftime("%Y-%m-%dT%H:%M:%S"); out = os.path.join(ROOT, "out"); os.makedirs(out, exist_ok=True)
    head = dict(generated=stamp, toolkit=TOOLKIT, validation=VALIDATION, rules=len(rules.RULES))
    vp = os.path.join(out, "validation.json")                                     # the time stamp alone is no change (round 10 h)
    try: old = json.load(open(vp, encoding="utf-8")); old.pop("generated", None)
    except (OSError, ValueError): old = None
    new = json.loads(json.dumps(dict({h: v for h, v in head.items() if h != "generated"}, status=st, findings=F), default=str))
    if new != old: outfile.write(vp, json.dumps(dict(head, status=st, findings=F), indent=1, default=str))
    for k in st:
        base = os.path.join(library.ELEMENTS, k) if k in element_ids else os.path.join(ROOT, "assemblies", k)
        d = os.path.join(base, "out"); os.makedirs(d, exist_ok=True)
        mine = [f for f in F if f["scope"] == k or k in f["elements"]]
        # no time stamp per element: four worktrees rebuild these, and a stamp alone would mark every element changed (OPERATING.md 5)
        outfile.write(os.path.join(d, "validate.json"), json.dumps(dict({h: v for h, v in head.items() if h != "generated"}, id=k, status=st[k], findings=mine), indent=1, default=str))

def report(element_ids, assembly_ids, geometry=True, verbose=False, part=None):
    """run the suite, print it, write lib/out/validation.json and out/validate.json per element and assembly; return {id: status}.
    part (toolkit/incremental.py, `build.py changed`): (elements, assemblies, old findings): run those and the library-wide rules
    only, and take every other scope's findings from the old list (a full build's, at the base)."""
    if part:
        from . import incremental as INC
        pe, pa, old = part
        F = INC.merge(old, run(pe, pa, geometry), set(pe) | set(pa) | {"library"}, element_ids, assembly_ids)
    else: F = run(element_ids, assembly_ids, geometry)
    st = statuses(F, element_ids, assembly_ids); write_reports(F, st, element_ids, assembly_ids)
    print(f"validation {VALIDATION} (PASS / REVIEW / FAIL): {len(F)} findings from {len({f['rule'] for f in F})} rules")
    by = {}
    for f in F: by.setdefault(f["rule"].split("-")[0], []).append(f["status"])
    names = dict(DOC="documentation", MATE="mates and fits", STK="stack-ups", GEO="interference", MOT="motion", HOLE="holes", GDT="GD&T fastener fit",
                 DFM="sheet-metal DFM", PIN="pinout and pins", ERC="electrical rule check", ELR="electrical ratings", FIL="fillet pre-flight", M12="M12 mated pairs")
    for k, v in by.items():
        print(f"  {names.get(k, k):24} {v.count('PASS'):4} pass {v.count('REVIEW'):4} review {v.count('FAIL'):4} fail")
    for f in sorted(F, key=lambda f: ({"FAIL": 0, "REVIEW": 1, "PASS": 2}[f["status"]], f["scope"], f["rule"])):
        if f["status"] == "FAIL" or (verbose and f["status"] == "REVIEW"):
            print(f"  {f['status']:6} {f['rule']:8} {f['scope']}: {f['where']}: {f['message']}")
    waived = [f for f in F if f.get("waived")]
    for f in waived: print(f"  WAIVED {f['rule']:8} {f['scope']}: {f['where']} ({f['waived']})")
    E = [e for e in element_ids]; A = [a for a in assembly_ids]
    print(f"elements: {sum(st[e] == 'PASS' for e in E)} releasable, {sum(st[e] == 'REVIEW' for e in E)} review, {sum(st[e] == 'FAIL' for e in E)} fail · "
          f"assemblies: {sum(st[a] == 'PASS' for a in A)} pass, {sum(st[a] == 'REVIEW' for a in A)} review, {sum(st[a] == 'FAIL' for a in A)} fail  (lib/out/validation.json)")
    return st
