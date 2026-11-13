"""Every element is the Institute's (EM 2026-11-10: "remove vendor name. all elements are owned by complexes. open to the public via
MIT"). Two things follow, both checked as DOC-007 at station 5 (validate.py):

  1. An element id names the class, never a maker or a product (the first two held, round 27, named a product family and a
     part-number prefix of the reference parts they were measured from). A rename is the library terminal's, on main: `python lib/build.py rename <old> <new>` moves the folder and every
     live reference (OWNERS.csv, inventory, machines lists, assemblies, scenes, coverage), keeps the old id in metadata.json
     aliases, and leaves history (lib/rounds, lib/reviews, lib/metrics, the batch reports, lessons) as it was.
  2. metadata.json is the owner's record: id, domain, category, envelope, brief, owner, licence, aliases. The reference part's
     record (maker, part number, product page, licence review of the reference files, verification notes) is vendor material and
     lives in references/source.txt (the provenance file, tracked; the rest of references/ is ignored), as a block at its end.
     `python lib/build.py own <lane|id>` moves it, verbatim; the lane commits what it moved (autopilot.md 2.a0).
  3. An own design's envelope is its own build's (request mech-10 3, review mech-r86 finding 3; core watch 2026-11-11): own designs and
     generics built in a folder that came with a catalogue record kept that part's width, height, depth and datasheet_dims (KEEP), so
     the record named another part's size (hardware-cabinet 152.4 x 1.27 x 50.8 against a build of 600 x 347 x 700). For an element
     whose baseline is our own design (validate.own_design), `own` moves a differing envelope and datasheet_dims verbatim into the
     source.txt block and writes the build's extents: width = x, depth = y, height = z (catalogue.csv size_mm's x x y x z), units mm,
     datasheet_dims null. DOC-007 holds an own design whose record differs from its build by more than ENV_TOL mm (envelope_drift).
"""
import os, re, json, csv, subprocess
from . import library

ROOT = library.ROOT
OWNER = "Complexes Institute of Technology"
LICENCE = "MIT"
KEEP = ("element_id", "domain", "category", "width", "height", "depth", "units", "datasheet_dims", "aliases", "brief", "owner", "licence", "references")
ACQ = "references/source.txt"
ENV = ("width", "height", "depth", "datasheet_dims")
ENV_TOL = 0.5                                                              # mm: the record is written to 0.1 mm
BLOCK = "## Record moved from metadata.json"
HISTORY = ("rounds/", "reviews/", "metrics/", "milestone-1/", "lessons.md", "kaizen.md", "GATE-REPORT", "REPORT.md",
           "line-history.csv", "reference-download-list.txt", "-prompt.txt",
           "requests/", "needs-em/")   # left as written at the time; requests and needs-em are records too (round 28's return 1 and 3).
                                       # The core's behaviour proposal under requests/ is moved by name (rename), its rows name no id
REVIEW_NAME = re.compile(r"-\d+\.\d+(?![0-9])")    # <old>-<version>: a review file's name (lib/reviews/elements/<id>-<version>.md), history
RECORD_PATH = re.compile(r"(?:^|[^\w])(?:requests|reviews|needs-em|rounds|metrics)/[\w./-]*$")   # a match inside a path to a record
# regions a rename leaves as written: (file, first line's text, last line's text). OPERATING.md 6's id convention names classes and
# forms that are also old ids ("relay-safety / relay-aux-2no2nc" is a form's example, not the element; round 27's return 1)
KEEP_REGIONS = (("OPERATING.md", "The id convention", "Built elements whose id lacks the function"),)
TEXT = (".csv", ".md", ".txt", ".json", ".py", ".lsp", ".gd", ".tscn", ".cfg", ".yml", ".yaml", ".toml", ".rs", ".scr")


def _meta(eid):
    p = os.path.join(library.ELEMENTS, eid, "metadata.json")
    try: return json.load(open(p, encoding="utf-8")), p
    except (OSError, ValueError): return None, p


def _vendor_patterns():
    from .validate import vendors
    return [(n, re.compile(rx.pattern, re.I)) for k, n, rx in vendors() if k == "vendor"]


def id_hits(eid, source=""):
    """why <eid> names a product: vendor names (lib/standards/vendors.csv, case-blind) and the element's own part-number family
    prefixes (validate.pn_prefix) found inside the id. [] when the id names a class."""
    from .validate import part_numbers, pn_prefix
    out = [n for n, rx in _vendor_patterns() if rx.search(eid.replace("-", " ")) or rx.search(eid)]
    low = eid.lower()
    for pn in part_numbers(source):
        p = pn_prefix(pn)
        if p and re.search(rf"(?<![a-z0-9]){re.escape(p.lower())}(?![a-z0-9])", low): out.append(f"part-number family {p}")
    return sorted(set(out))


def vendor_fields(meta):
    """metadata.json keys that are the reference part's record, not the element's"""
    return [k for k in meta if k not in KEEP]


def built_envelope(m):
    """the build's own envelope as metadata.json writes it: width x, depth y, height z (catalogue.csv size_mm's order x, y, z), mm"""
    from .prims import extents
    lo, hi = extents(m.build(**getattr(m, "PARAMS", {})))
    return dict(width=round(hi[0] - lo[0], 1), height=round(hi[2] - lo[2], 1), depth=round(hi[1] - lo[1], 1))


def envelope_drift(meta, built):
    """the record's envelope fields that are not the build's, [(key, recorded)]: width, height or depth more than ENV_TOL mm from
    built (a field the record leaves out or null is not a drift), and a datasheet_dims that is not null (a catalogue part's figure)"""
    out = []
    for k in ("width", "height", "depth"):
        v = meta.get(k)
        if v is None: continue
        try: off = abs(float(v) - float(built[k])) > ENV_TOL
        except (TypeError, ValueError): off = True
        if off: out.append((k, v))
    if meta.get("datasheet_dims") not in (None, [], ""): out.append(("datasheet_dims", meta["datasheet_dims"]))
    return out


def _own_built(eid, m=None):
    """the build's envelope when <eid> is our own design (validate.own_design, its inventory row first), else None"""
    from .validate import own_design, inventory_own
    try:
        m = m or library.load(eid)
        if not own_design(getattr(m, "BASELINE", ""), inventory_own(eid)): return None
        return built_envelope(m)
    except Exception:
        return None


def check(eid, m=None, built=None):
    """DOC-007 messages for <eid>: a product name in the id; vendor fields in metadata.json; no owner; an own design's record that
    keeps another part's envelope (built: the build's envelope, computed for an own design when not given)"""
    out = []
    src = os.path.join(library.ELEMENTS, eid, "references", "source.txt")
    source = open(src, encoding="utf-8", errors="replace").read() if os.path.isfile(src) else ""
    hits = id_hits(eid, source)
    if hits: out.append(f"id {eid} names a product ({', '.join(hits)}): an id names the class; the library terminal renames it (build.py rename)")
    meta, p = _meta(eid)
    if meta is None: return out                                                # no record: nothing of a vendor's in it (own designs, generics)
    vf = vendor_fields(meta)
    if vf: out.append(f"metadata.json carries the reference part's record ({', '.join(vf[:6])}{'…' if len(vf) > 6 else ''}): "
                      f"`python lib/build.py own {eid}` moves it to {ACQ}")
    elif meta.get("owner") != OWNER: out.append(f"metadata.json names no owner: every element is {OWNER}'s, {LICENCE} (build.py own)")
    if any(meta.get(k) not in (None, [], "") for k in ENV):
        built = built or _own_built(eid, m)
        drift = envelope_drift(meta, built) if built else []
        if drift: out.append(f"metadata.json keeps another part's envelope ({', '.join(f'{k} {json.dumps(v)}' for k, v in drift)}; the build: "
                             f"width {built['width']:g}, height {built['height']:g}, depth {built['depth']:g}): an own design's record is its own build's; "
                             f"`python lib/build.py own {eid} --write` writes it and moves the old figures to {ACQ}")
    return out


def own(eid, write=False, built=None):
    """move the reference part's record out of metadata.json into references/source.txt; set owner and licence; for an own design,
    write the build's envelope and move a differing one (and datasheet_dims) with the record (built: the build's envelope, computed
    for an own design when not given). Returns (moved keys, note). write=False only reports."""
    meta, p = _meta(eid)
    if meta is None: return [], "metadata.json missing or not JSON"
    vf = vendor_fields(meta)
    built = built or (_own_built(eid) if any(meta.get(k) not in (None, [], "") for k in ENV) else None)
    drift = envelope_drift(meta, built) if built else []
    if not vf and not drift and meta.get("owner") == OWNER: return [], "already the owner's record"
    acq_p = os.path.join(library.ELEMENTS, eid, *ACQ.split("/"))
    moved = {k: meta[k] for k in vf}
    if drift:                                                                  # request mech-10 3: the catalogue part's envelope goes with its record
        moved.update({f"catalogue {k}": v for k, v in drift})
        meta = dict(meta, **built, units="mm", datasheet_dims=None)
    block = "\n".join([f"{BLOCK} (build.py own, EM 2026-11-10: every element is {OWNER}'s; vendor material lives in references/ only)"]
                      + [f"{k}: {v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)}" for k, v in moved.items()]) + "\n"
    new = {k: meta[k] for k in KEEP if k in meta}
    new["element_id"] = eid; new["owner"] = OWNER; new["licence"] = LICENCE
    new["references"] = f"{ACQ} (the reference part: maker, part number, source files, their licence review)" if moved or os.path.isfile(acq_p) else "none"
    order = ["element_id", "domain", "category", "owner", "licence", "aliases", "width", "height", "depth", "units", "datasheet_dims", "brief", "references"]
    new = {k: new[k] for k in order if k in new}
    if write:
        if moved:
            os.makedirs(os.path.dirname(acq_p), exist_ok=True)
            old = open(acq_p, encoding="utf-8", errors="replace").read() if os.path.isfile(acq_p) else ""
            open(acq_p, "w", encoding="utf-8", newline="\n").write(old + ("" if not old or old.endswith("\n") else "\n") + ("\n" if old else "") + block)
        open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(new, indent=2, ensure_ascii=False) + "\n")
    return sorted(moved), ("moved" if write else "would move") + f" {len(moved)} field(s) to {ACQ}"


def lane_of(eid):
    """the lane OWNERS.csv gives lib/elements/<eid>/* (None when no row)"""
    p = os.path.join(ROOT, "OWNERS.csv")
    for r in csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#")):
        if (r.get("path") or "").strip() == f"lib/elements/{eid}/*": return (r.get("owner") or "").strip()
    return None


def scan(lane=None):
    """[(lane, eid, messages)] of every element DOC-007 would hold, one lane's when given"""
    out = []
    for e in library.element_ids():
        ln = lane_of(e)
        if lane and ln != lane: continue
        msgs = check(e)
        if msgs: out.append((ln or "?", e, msgs))
    return out


def _text_files(keep=None):
    """live text files under lib/: not history, not generated out/, and other elements' gate and qa logs (a run's record, which
    names every file AutoCAD trusted) only for the element being renamed (keep)"""
    for dp, dn, fn in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT).replace("\\", "/"); parts = rel.split("/")
        if any(x in ("__pycache__", ".git", "out", "thumbs", "target") for x in parts): dn[:] = []; continue
        if len(parts) >= 3 and parts[0] == "elements" and parts[2] in ("gate", "qa") and parts[1] != keep: dn[:] = []; continue
        for f in fn:
            path = os.path.join(dp, f); r = os.path.relpath(path, ROOT).replace("\\", "/")
            if any(h in r for h in HISTORY) or r.startswith("elements/BATCH-") or r.startswith("elements/_vendor"): continue
            if f.lower().endswith(TEXT): yield path


_TOK = r"[A-Za-z0-9_]"
_START = rf"(?:(?<!{_TOK})|(?<=\\[nrt]))"     # a token starts after a non-word character, or after a string's \n, \r, \t escape ("...signed\nrelay-safety-2ch-2no1nc,1.0")


def keep_lines(rel, text):
    """line numbers (1-based) of text in rel that a rename leaves: KEEP_REGIONS"""
    out, lines = set(), text.split("\n")
    for f, a, b in KEEP_REGIONS:
        if rel != f: continue
        on = False
        for i, ln in enumerate(lines, 1):
            if a in ln: on = True
            if on: out.add(i)
            if on and b in ln: on = False
    return out


def retoken(text, old, new, others=(), keep=(), code=False):
    """text with every whole-token <old> made <new>, and the lines changed [(line no., before, after)]. A token boundary allows "-"
    and "." after the id (its files: <old>-acad.json), so three places are left as written (round 27's return, 1 and 2):
      · a match that is already <new> or another id that holds <old> ("contactor-9a-1no1nc" when old is contactor-9a; the
        rename never doubles a suffix, and a second run changes nothing; a hydraulic twin "hyd-<old>" holds the pneumatic "<old>",
        round 29's return 2.a.8: a token may start after "-", so the old id matched as another id's tail);
      · a line that already names <new> (it is written about the new id: OPERATING.md 6's examples, a note made before the run);
      · a line that records a rename from <old> ("<old> -> ...", "<old> → ...": ROADMAP's record of what was renamed);
      · the lines numbered in keep (keep_lines: OPERATING.md 6's id convention);
      · a match followed by -<version> ("relay-ice-cube-1.3", "sr-440r-1.1.md", "relay-ice-cube-1.3:1"): the name of a review written
        under the old id, which keeps its name (round 28's return 1);
      · a match inside a path to a record (lib/requests/core/behaviour/<old>.csv in a "taken in from" line, lib/reviews/...): the
        record keeps its name. History folders themselves (HISTORY, now with requests/ and needs-em/) are never read.
      · code (a .py file) and an id with no "-": only a match that opens a string or a path ("<id>", 'elements/<id>/...') is the id; a
        bare name is code (request pneu-13 2: `hx` is a half-width in 20 elements' element.py, 49 lines the dry run would have changed)."""
    tok = re.compile(rf"{_START}{re.escape(old)}(?!{_TOK})")
    newtok = re.compile(rf"{_START}{re.escape(new)}(?!{_TOK})")
    record = re.compile(rf"{_START}{re.escape(old)}\s*(?:->|→)")
    longer = sorted({o for o in others if o != old and old in o} | ({new} if old in new else set()), key=len, reverse=True)
    def sub_line(line):
        if newtok.search(line) or record.search(line): return line
        def rep(m):
            if REVIEW_NAME.match(line, m.end()) or RECORD_PATH.search(line[:m.start()]): return m.group(0)
            if code and "-" not in old and (m.start() == 0 or line[m.start() - 1] not in "\"'/"): return m.group(0)
            for o in longer:                     # another id that holds <old> anywhere (round 29's return 2.a.8: hyd-<old> holds <old>)
                for k in [i for i in range(len(o)) if o.startswith(old, i)]:
                    s = m.start() - k
                    if s >= 0 and line.startswith(o, s) and not re.match(_TOK, line[s + len(o):s + len(o) + 1] or " "): return m.group(0)
            return new
        return tok.sub(rep, line)
    lines = text.split("\n"); out, diff = [], []
    for i, ln in enumerate(lines, 1):
        n = sub_line(ln) if i not in keep and tok.search(ln) else ln
        if n != ln: diff.append((i, ln, n))
        out.append(n)
    return "\n".join(out), diff


def rename(old, new, git=True, write=False, diff=None):
    """lib/elements/<old> -> <new>, files named after the id with it, and every live reference under lib/ (whole tokens, by
    retoken; history folders untouched); the old id joins metadata.json aliases. Returns (paths moved, files changed, notes);
    the dry run lists the same moves it would make. diff: a list that receives (file, line no., before, after) per changed line."""
    src, dst = os.path.join(library.ELEMENTS, old), os.path.join(library.ELEMENTS, new)
    notes = []
    if not os.path.isdir(src): return [], [], [f"{old}: no such element"]
    if os.path.exists(dst): return [], [], [f"{new}: exists already"]
    if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9.]+)*", new): return [], [], [f"{new}: an id is lower-case words and figures joined by '-'"]
    if id_hits(new, open(os.path.join(src, "references", "source.txt"), encoding="utf-8", errors="replace").read() if os.path.isfile(os.path.join(src, "references", "source.txt")) else ""):
        return [], [], [f"{new}: still names a product ({', '.join(id_hits(new))})"]
    others = set(library.element_ids()) - {old}
    def mv(a, b):
        """git mv for what git tracks; a plain rename for the rest (out/, thumbs/: ignored or untracked)"""
        if not write: return
        if git and subprocess.run(["git", "mv", a, b], cwd=os.path.dirname(ROOT), capture_output=True).returncode == 0: return
        if os.path.exists(a) and not os.path.exists(b): os.replace(a, b)
    moved, changed = [], []
    inner = [(dp, f) for dp, dn, fn in os.walk(src) for f in fn if old in f]                  # files named after the id, before the move
    mv(src, dst); moved.append(f"elements/{old} -> elements/{new}")
    prop = os.path.join(ROOT, "requests", "core", "behaviour", old + ".csv")                  # the core's behaviour proposal, named after the id
    if os.path.isfile(prop): mv(prop, prop[:-len(old + ".csv")] + new + ".csv"); moved.append(f"requests/core/behaviour/{old}.csv -> {new}.csv")
    for dp, f in inner:
        d = dst + dp[len(src):] if write else dp
        nf = retoken(f, old, new, others)[0] if old in f else f
        if nf == f: continue
        mv(os.path.join(d, f), os.path.join(d, nf))
        moved.append(os.path.relpath(os.path.join(dst + dp[len(src):], nf), ROOT).replace("\\", "/"))
    for path in list(_text_files(keep=new if write else old)):
        try: t = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError): continue
        if old not in t: continue
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        nt, d = retoken(t, old, new, others, keep_lines(rel, t), code=rel.endswith(".py"))
        if not d: continue
        changed.append(rel)
        if diff is not None: diff.extend((rel, i, a, b) for i, a, b in d)
        if write: open(path, "w", encoding="utf-8", newline="\n").write(nt)
    if write:
        keep_alias(new, old)
        notes.append(f"{old} kept in metadata.json aliases; rebuild ({new}'s out/ and gate files carry the new id); the lane's next gate run is at the same version")
    return moved, changed, notes


def keep_alias(new, old):
    """the old id joins <new>'s metadata.json aliases. request pneu-14 item 3 (core watch 2026-11-12): an element with no metadata.json
    (hpu-7.5kw, hyd-filter-return and some 110 others: own designs and generics) kept its old id nowhere, so a reader that finds an
    element by its aliases (line.waits_on_reading, BOM-010) could not; the rename now starts the owner's record: element_id, owner,
    licence, aliases (OPERATING.md 6). Returns the path written."""
    meta, p = _meta(new)
    if meta is None: meta = {"element_id": new, "owner": OWNER, "licence": LICENCE, "aliases": []}
    al = meta.get("aliases") or []
    if old not in al: al.append(old)
    meta["aliases"] = al; meta["element_id"] = new
    open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
    return p


def holders(old, new=None):
    """the other element ids that hold <old> as a part of theirs (hyd-<old> holds <old>): retoken leaves each of them;
    the dry run names them so the reader checks it (round 29's return, 4). <new> is the element itself after --write (round 30's
    return 2.c: flow-control-inline holds flow-control and was listed as another id)"""
    return sorted(o for o in library.element_ids() if o not in (old, new) and old in o)


def risky(diff, old, new=None):
    """the dry run's own summary (round 28's return, "how the core writes rounds"): the changed lines outside the element's folder,
    counted by kind of file (its name, or its folder for a doc), so a reader of a 100 kB --diff knows where to look. After --write
    the folder is elements/<new>/ and is the element's too (round 30's return 2.c: the write's count took its gate and qa files as outside)"""
    out = {}
    for f, i, a, b in diff:
        if f.startswith(f"elements/{old}/") or (new and f.startswith(f"elements/{new}/")): continue
        parts = f.split("/"); kind = parts[-1] if parts[0] == "elements" else ("/".join(parts[:2]) if len(parts) > 2 else f)
        out[kind] = out.get(kind, 0) + 1
    return sorted(out.items(), key=lambda kv: (-kv[1], kv[0]))


def describe(args):
    """build.py own [lane|id] [--write]; build.py rename <old> <new> [--write] [--diff]"""
    write = "--write" in args; a = [x for x in args if not x.startswith("-")]
    if a and a[0] == "rename":
        if len(a) < 3: return "rename <old> <new> [--write] [--diff]"
        d = []; show = "--diff" in args
        moved, changed, notes = rename(a[1], a[2], write=write, diff=d)
        rk = risky(d, a[1], a[2])
        return "\n".join([f"{'moved' if write else 'would move'} {len(moved)} path(s); {'changed' if write else 'would change'} {len(changed)} file(s):"]
                         + [f"  mv {x}" for x in moved] + [f"  {x}" for x in changed]
                         + [f"lines outside elements/{a[1]}/: {sum(n for _, n in rk)}" + ("; by kind: " + ", ".join(f"{k} {n}" for k, n in rk) if rk else "")]
                         + [f"other ids that hold {a[1]} (left as they are): " + (", ".join(holders(a[1], a[2])) or "none")]
                         + ([f"  {f}:{i}\n    - {b0.strip()[:200]}\n    + {b1.strip()[:200]}" for f, i, b0, b1 in d] if show else [])
                         + notes + ([] if write else ["(--diff prints each changed line; --write does it: the library terminal's, on main)"]))
    ids = [a[0]] if a and a[0] in library.element_ids() else None
    lane = a[0] if a and not ids else None
    rows = []
    for e in ids or [e for _, e, _ in scan(lane)]:
        moved, note = own(e, write=write); rows.append(f"  {lane_of(e) or '?':5} {e:28} {note}{': ' + ', '.join(moved) if moved else ''}")
    held = scan(lane)
    head = f"{len(held)} element(s) DOC-007 holds{' in ' + lane if lane else ''}; {sum(1 for _, e, m in held if any(x.startswith('id ') for x in m))} with a product name in the id"
    return "\n".join([head] + rows + ([] if write else ["(--write moves the fields; the lane commits its own elements)"]))
