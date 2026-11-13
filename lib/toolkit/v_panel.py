"""Panel wiring checkers of the validation suite (request panel-4 item 4, core watch 2026-11-11). They read an assembly's wire list
and terminal plan and run on any assembly that has a wires.csv (the core's test wiring and the panel shop's panels alike):
  assemblies/<aid>/wires.csv       wire,from,to,...   one row a wire (or a join: a plug-in, a bridge); an end is <tag>.<mark>
  assemblies/<aid>/terminals.csv   strip,terminal,tag,side1,side2,bridge,point,wire,status,note   (the panel shop's terminal plan;
                                   wire = "<side 1's wire>/<side 2's wire>", side 1 the block's pin 1, side 2 its pin 2; a number in
                                   brackets is kept for a wire whose other end is not on file and is not checked)
PNL-010  every end of a numbered wire names an element of the assembly (placed, or a row of its bom.csv: held or planned) and a
         mark that element's behaviour.csv has as a pin. FAIL on a tag or mark that does not exist; REVIEW when the element has no
         behaviour.csv to read its marks from. (pm-motor-starter's plc-1.L+ / .M / .TD+ ...: the solver joins any two names, so a
         wrong mark left the controller's load on no net and nothing failed.)
PNL-030  the terminal plan and the wire list agree: every wire a terminal row names is a row of wires.csv with that block's pin as
         one end, and every wire with an end on a planned block is named on that block's row, on that side.
BOM-010  every bom.csv row of any assembly names an element on file or a lib/inventory.csv row (planned, not built yet). FAIL on a
         row that names a renamed element's old id (an alias in its metadata.json): the assembly drops it as "planned" and nothing
         else says so; REVIEW on a row that pins a version to an id that is neither (a wrong name: a planned row with no
         element yet writes "-" for its version, as the panel shop's placeholder rows do, request panel-6's answer). Reviewer
         panel/r6.md finding 1, an ESCAPE (core watch 2026-11-11): core round 28 renamed contactor-9a and op-estop-22 on main while
         the panels waited in the queue, the merge brought the old ids back, and both panels built without K1 and the door e-stop.
Not checked here: how many conductors one clamp takes (PNL-020 waits on term-4mm's brief, request panel-3 item 4)."""
import csv, os, re

def _rows(path):
    if not os.path.isfile(path): return []
    return [{k: (v or "").strip() for k, v in r.items() if k} for r in csv.DictReader(l for l in open(path, encoding="utf-8") if not l.startswith("#"))
            if r and any((v or "").strip() for v in r.values() if isinstance(v, str))]

def split_end(end, tags):
    """'<tag>.<mark>' -> (tag, mark): the longest tag of the assembly that the end starts with (tags hold dots: enc-1.lamp-power);
    (None, end) when no tag matches"""
    best = None
    for t in tags:
        if end.startswith(t + ".") and (best is None or len(t) > len(best)): best = t
    return (best, end[len(best) + 1:]) if best else (None, end)

def ends(W, tags, element_of, pins_of):
    """PNL-010 on a wire list W ([{wire, from, to}]); tags: every tag of the assembly; element_of(tag) -> element id or None;
    pins_of(eid) -> set of pin marks, or None when the element has no behaviour.csv"""
    out = []; bad = 0; n = 0
    for i, w in enumerate(W, 1):
        num = (w.get("wire") or "").strip()
        if not num: continue                                                    # a join that is not a wire (a plug-in row, a bridge)
        for side in ("from", "to"):
            e = (w.get(side) or "").strip()
            if not e: continue
            n += 1; tag, mark = split_end(e, tags)
            if tag is None:
                out.append(("FAIL", "PNL-010", f"wire {num} {side} {e}", "no element of the assembly has this tag (placed, or a row of bom.csv)")); bad += 1; continue
            eid = element_of(tag); pins = pins_of(eid) if eid else None
            if pins is None:
                out.append(("REVIEW", "PNL-010", f"wire {num} {side} {e}", f"{tag} ({eid or 'no element'}) has no behaviour.csv: its marks cannot be read")); continue
            if mark not in pins:
                out.append(("FAIL", "PNL-010", f"wire {num} {side} {e}", f"{tag} ({eid}) has no pin '{mark}'; its pins: {' '.join(sorted(pins)) or 'none'}")); bad += 1
    if n and not bad: out.append(("PASS", "PNL-010", "wires.csv", f"{n} wire ends name a tag of the assembly and a pin of its element"))
    return out

def _nums(cell):
    """terminals.csv wire cell '20/42' -> (['20'], ['42']); '(31)/' -> ([], []): bracketed numbers are kept, not checked"""
    a, _, b = (cell or "").partition("/")
    clean = lambda s: [x for x in re.split(r"[\s,;]+", s.strip()) if x and not x.startswith("(")]
    return clean(a), clean(b)

def plan(T, W):
    """PNL-030 between a terminal plan T and a wire list W"""
    out = []; bad = 0
    by_num = {}
    for w in W:
        if (w.get("wire") or "").strip(): by_num.setdefault(w["wire"].strip(), []).append(w)
    blocks = {r["tag"]: r for r in T if r.get("tag")}
    for tag, r in blocks.items():
        for pin, nums in zip(("1", "2"), _nums(r.get("wire"))):
            for num in nums:
                ws = by_num.get(num)
                if not ws:
                    out.append(("FAIL", "PNL-030", f"{r.get('strip')}:{r.get('terminal')} {tag} side {pin}", f"wire {num}: no such wire in wires.csv")); bad += 1
                elif not any(f"{tag}.{pin}" in (w.get("from"), w.get("to")) for w in ws):
                    out.append(("FAIL", "PNL-030", f"{r.get('strip')}:{r.get('terminal')} {tag} side {pin}", f"wire {num} does not end at {tag}.{pin} (it runs {ws[0].get('from')} to {ws[0].get('to')})")); bad += 1
    for num, ws in by_num.items():
        for w in ws:
            for e in (w.get("from"), w.get("to")):
                tag, _, pin = (e or "").rpartition(".")
                if tag in blocks and pin in ("1", "2"):
                    listed = _nums(blocks[tag].get("wire"))[int(pin) - 1]
                    if num not in listed:
                        out.append(("FAIL", "PNL-030", f"wire {num} {e}", f"ends on {tag} side {pin}, and the terminal plan's row for {tag} does not name it")); bad += 1
    if T and not bad: out.append(("PASS", "PNL-030", "terminals.csv", f"{len(blocks)} terminal rows and the wire list agree"))
    return out

def aliases(root):
    """{old id: new id} from every element's metadata.json aliases (build.py rename writes the old id there)"""
    import json
    out = {}; d = os.path.join(root, "elements")
    for e in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        try: m = json.load(open(os.path.join(d, e, "metadata.json"), encoding="utf-8"))
        except (OSError, ValueError): continue
        for a in (m.get("aliases") or []) if isinstance(m, dict) else []:
            if isinstance(a, str) and a and a != e: out.setdefault(a, e)
    return out

def bom_ids(rows, on_file, planned, renamed):
    """BOM-010 on bom.csv rows: [(status, rule, where, message)]. on_file: element ids with a folder; planned: lib/inventory.csv ids;
    renamed: {old id: new id}"""
    out = []
    for i, r in enumerate(rows, 1):
        e = (r.get("element") or "").strip(); tag = (r.get("tag") or "").strip() or f"row {i}"
        if not e or e.startswith("#") or e in on_file: continue
        if e in renamed:
            out.append(("FAIL", "BOM-010", tag, f"{e} was renamed {renamed[e]} (its metadata.json aliases): the row still names the old id, "
                        f"so the assembly builds without it; write {renamed[e]} and its version"))
        elif e not in planned and (r.get("version") or "").strip() not in ("", "-"):
            out.append(("REVIEW", "BOM-010", tag, f"{e} {r['version'].strip()} is no element on file and no lib/inventory.csv row: a wrong "
                        f"name (a planned row with no element yet pins no version: '-')"))
    return out

def bom_run(aid, root):
    """BOM-010 on assembly aid's bom.csv (nothing when it has none)"""
    rows = _rows(os.path.join(root, "assemblies", aid, "bom.csv"))
    if not rows: return []
    d = os.path.join(root, "elements")
    on_file = {e for e in os.listdir(d) if os.path.isdir(os.path.join(d, e))} if os.path.isdir(d) else set()
    a = os.path.join(root, "assemblies")                                       # a cell places assemblies too (dm-motor-starter-cell)
    on_file |= {x for x in os.listdir(a) if os.path.isdir(os.path.join(a, x))} if os.path.isdir(a) else set()
    planned = {r.get("id", "") for r in _rows(os.path.join(root, "inventory.csv"))}
    return bom_ids(rows, on_file, planned, aliases(root))

def run(aid, P, root):
    """PNL-010 and PNL-030 on assembly aid (P: its built prims, for the placed tags); nothing when it has no wires.csv"""
    d = os.path.join(root, "assemblies", aid)
    W = _rows(os.path.join(d, "wires.csv"))
    if not W: return []
    from . import behaviour as BH
    placed = {}
    for _, _, t, e in getattr(P, "owners", []): placed.setdefault(t, e)
    for r in _rows(os.path.join(d, "bom.csv")):                                  # held or planned rows: in the BOM, not built
        if r.get("tag") and r.get("element") and not r["element"].startswith("#"): placed.setdefault(r["tag"], r["element"])
    cache = {}
    def pins_of(eid):
        if eid not in cache:
            S = BH.spec(eid) if os.path.isdir(os.path.join(root, "elements", eid)) else None
            cache[eid] = (set(S["pins"]) | set(S.get("counts") or {})) if S else None      # a count pin (behaviour.md) is a mark a wire may end on
        return cache[eid]
    return ends(W, list(placed), placed.get, pins_of) + plan(_rows(os.path.join(d, "terminals.csv")), W)
