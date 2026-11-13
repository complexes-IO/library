"""draw.io diagrams of the work, generated from what is on file (EM 2026-11-09: "start with a draw.io diagram of the machine we are
building ... list the stations / machines we could be fixing while the code elements are being built"). Nothing here is drawn by
hand: the machine's BOM is lib/machines-factory.txt or lib/machines-from-elements.txt, the status of each element is the board
(toolkit/line.py), the lane is lib/inventory.csv. Open the file in draw.io (app.diagrams.net or the desktop app); regenerate it
any time, it is a build output (lib/toolkit/diagrams/, not committed).
    python lib/build.py drawio <machine>        -> lib/toolkit/diagrams/<machine>.drawio: page 1 the machine (its elements by lane, coloured
                                                   by station), page 2 the line (every station with the lane counts), page 3 the
                                                   factory (every machine, coloured by how much of it is built)
    python lib/build.py drawio                  -> the factory and line pages only
Colours: green released (station 8) · yellow at station 7 (sign-off: EM or the reviewer) · orange in build (stations 1-6) ·
grey in the inventory, not started · red not in the inventory (a (new) id of the factory list).
"""
import csv, html, os, re

from . import library, line as LN

LIB = os.path.dirname(library.ELEMENTS)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams")           # a build output, not committed (its .gitignore)
QTY = re.compile(r"\(x(\d+)\)")
FILL = {"released": ("#d5e8d4", "#82b366"), "signoff": ("#fff2cc", "#d6b656"), "build": ("#ffe6cc", "#d79b00"), "todo": ("#f5f5f5", "#999999"), "missing": ("#f8cecc", "#b85450")}
LANE_ORDER = ["mech", "pneu", "elec", "panel", "core", "?"]
LANE_TITLE = {"mech": "mechanical (mech)", "pneu": "fluid power (pneu)", "elec": "electrical (elec)", "panel": "control panels (panel)", "core": "core", "?": "lane not set"}


def machines():
    """{machine: (department, [(id, qty, marks)])} from both machine lists"""
    out = {}
    for fn in ("machines-factory.txt", "machines-from-elements.txt"):
        dept = ""
        for line in open(os.path.join(LIB, fn), encoding="utf-8"):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith(("MACHINES", "One line", "(tool)", "control (", "elements are", "pins first", "its 13", "structure (", "element this", "`python")): continue
            if re.match(r"^\d+\.\s", line) or (line.isupper() and "," not in line): dept = re.sub(r"^\d+\.\s*", "", line).strip().title(); continue
            m = re.match(r"^([a-z0-9][a-z0-9\-]*)\s{2,}(.*)$", line)
            if not m: continue
            items = []
            for tok in m.group(2).split(", "):
                tok = tok.strip()
                if not tok: continue
                q = QTY.search(tok); qty = int(q.group(1)) if q else 1
                eid = tok.split(" ")[0].split("(")[0]
                marks = [x for x in ("own", "new", "tool") if f"({x})" in tok]
                items.append((eid, qty, marks))
            out.setdefault(m.group(1), (dept or fn, items))
    return out


def inventory():
    p = os.path.join(LIB, "inventory.csv")
    return {r["id"].strip(): r for r in csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#")) if r.get("id")}


def status():
    """{element id: (station reached, 'released'|'signoff'|'build', version, what holds it)} from the board"""
    out = {}
    for lane, items in LN.board().items():
        for eid, ver, r, nxt in items:
            kind = "released" if r >= 8 else ("signoff" if r == 7 or (nxt and nxt[0] == 7) else "build")
            hold = (nxt[4][0][:70] if nxt and nxt[4] else "")
            out[eid] = (r, kind, ver, hold)
    return out


def _cell(cid, parent, label, x, y, w, h, style):
    return (f'<mxCell id="{cid}" value="{html.escape(label, quote=True)}" style="{style}" vertex="1" parent="{parent}">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')


def _page(name, cells):
    body = "".join(cells)
    return (f'<diagram name="{html.escape(name, quote=True)}" id="{re.sub(r"[^a-z0-9]", "-", name.lower())}"><mxGraphModel grid="1" gridSize="10" page="1" '
            f'pageWidth="1600" pageHeight="1000"><root><mxCell id="0"/><mxCell id="1" parent="0"/>{body}</root></mxGraphModel></diagram>')


def machine_page(mid, dept, items, inv, st):
    """the machine: a swimlane per lane, an element box per BOM item, coloured by its station"""
    cells = []; n = [0]
    def nid(): n[0] += 1; return f"{mid}-{n[0]}"
    by_lane = {}
    for eid, qty, marks in items:
        lane = inv.get(eid, {}).get("lane", "").strip() or ("core" if eid in st and LN.owners().get(eid) == "core" else "?")
        by_lane.setdefault(lane, []).append((eid, qty, marks))
    cells.append(_cell(nid(), "1", f"{mid} · {dept}  —  {len(items)} element kinds, {sum(q for _, q, _ in items)} parts", 20, 20, 1200, 40,
                       "text;html=1;fontSize=18;fontStyle=1;align=left;verticalAlign=middle;"))
    cells.append(_cell(nid(), "1", "released · at station 7 (sign-off) · in build (stations 1–6) · in the inventory, not started · not in the inventory (new)", 20, 60, 1200, 24,
                       "text;html=1;fontSize=11;align=left;verticalAlign=middle;fontColor=#666666;"))
    x = 20; y = 100; W = 230; BH = 60; cols = 2
    counts = dict(released=0, signoff=0, build=0, todo=0, missing=0)
    for lane in [l for l in LANE_ORDER if l in by_lane]:
        rows = by_lane[lane]; h = 40 + ((len(rows) + cols - 1) // cols) * (BH + 10) + 10
        lid = nid()
        cells.append(_cell(lid, "1", f"{LANE_TITLE.get(lane, lane)} · {len(rows)}", x, y, cols * (W + 10) + 10, h, "swimlane;html=1;fontStyle=1;startSize=30;fillColor=#f9f9f9;strokeColor=#666666;"))
        for i, (eid, qty, marks) in enumerate(sorted(rows, key=lambda r: (-(st.get(r[0], (0,))[0]), r[0]))):
            if eid in st: r, kind, ver, hold = st[eid]; sub = f"v{ver} · station {r}" + (f"\n{hold}" if kind != "released" and hold else "")
            elif eid in inv: kind = "todo"; sub = "in the inventory, not started" + (f" · pin {inv[eid]['pin']}" if inv[eid].get("pin", "").strip() else "")
            else: kind = "missing"; sub = "not in the inventory yet"
            counts[kind] += 1
            fill, stroke = FILL[kind]
            label = eid + (f"  ×{qty}" if qty > 1 else "") + (f"  ({', '.join(marks)})" if marks else "") + "\n" + sub
            cells.append(_cell(nid(), lid, label, 10 + (i % cols) * (W + 10), 40 + (i // cols) * (BH + 10), W, BH,
                               f"rounded=1;whiteSpace=wrap;html=1;fontSize=10;align=left;spacingLeft=6;fillColor={fill};strokeColor={stroke};"))
        x += cols * (W + 10) + 30
        if x > 1300: x = 20; y += h + 30
    total = sum(counts.values())
    cells.append(_cell(nid(), "1", f"built: {counts['released']} released, {counts['signoff']} at sign-off, {counts['build']} in build, {counts['todo']} not started, {counts['missing']} not in the inventory  ·  {round(100 * (counts['released'] + counts['signoff']) / total) if total else 0} % through station 6",
                       20, 84, 1200, 16, "text;html=1;fontSize=11;align=left;verticalAlign=middle;"))
    return cells, counts


def line_page(st):
    cells = []; n = [0]
    def nid(): n[0] += 1; return f"line-{n[0]}"
    cells.append(_cell(nid(), "1", "The element line · eight stations (OPERATING.md 13) · every element at the station it has reached", 20, 20, 1400, 40, "text;html=1;fontSize=18;fontStyle=1;align=left;verticalAlign=middle;"))
    per = {}
    for lane, items in LN.board().items():
        for eid, ver, r, nxt in items: per.setdefault((lane, r), []).append(eid)
    lanes = [l for l in LANE_ORDER if any(k[0] == l for k in per)]
    x0 = 160; W = 150
    for i, (num, name, title) in enumerate(LN.STATIONS):
        cells.append(_cell(nid(), "1", f"{num} · {title}", x0 + i * (W + 10), 70, W, 50, "rounded=1;whiteSpace=wrap;html=1;fontStyle=1;fontSize=11;fillColor=#dae8fc;strokeColor=#6c8ebf;"))
    cells.append(_cell(nid(), "1", "0 · not yet on the line", x0 - 150, 70, 130, 50, "rounded=1;whiteSpace=wrap;html=1;fontStyle=1;fontSize=11;fillColor=#f5f5f5;strokeColor=#999999;"))
    for j, lane in enumerate(lanes):
        y = 140 + j * 150
        cells.append(_cell(nid(), "1", LANE_TITLE.get(lane, lane), 20, y, 120, 130, "text;html=1;fontStyle=1;fontSize=12;align=left;verticalAlign=top;"))
        for i in range(0, 9):
            ids = sorted(per.get((lane, i), []))
            if not ids: continue
            kind = "released" if i == 8 else ("signoff" if i == 7 else "build"); fill, stroke = FILL[kind]
            xx = x0 + (i - 1) * (W + 10) if i >= 1 else x0 - 150; ww = W if i >= 1 else 130
            cells.append(_cell(nid(), "1", f"{len(ids)}\n" + "\n".join(ids[:7]) + (f"\n… +{len(ids) - 7}" if len(ids) > 7 else ""), xx, y, ww, 130,
                               f"rounded=1;whiteSpace=wrap;html=1;fontSize=9;align=left;spacingLeft=4;verticalAlign=top;fillColor={fill};strokeColor={stroke};"))
    return cells


def factory_page(M, inv, st):
    cells = []; n = [0]
    def nid(): n[0] += 1; return f"fac-{n[0]}"
    cells.append(_cell(nid(), "1", f"The machines · {len(M)} · coloured by how much of each is through station 6 (released or at sign-off)", 20, 20, 1400, 40, "text;html=1;fontSize=18;fontStyle=1;align=left;verticalAlign=middle;"))
    depts = {}
    for mid, (dept, items) in M.items(): depts.setdefault(dept, []).append((mid, items))
    x = 20; y = 70; W = 200; BH = 46; cols = 2
    for dept, ms in depts.items():
        h = 40 + ((len(ms) + cols - 1) // cols) * (BH + 8) + 8
        did = nid()
        cells.append(_cell(did, "1", f"{dept} · {len(ms)}", x, y, cols * (W + 8) + 8, h, "swimlane;html=1;fontStyle=1;startSize=30;fillColor=#f9f9f9;strokeColor=#666666;"))
        scored = []
        for mid, items in ms:
            done = sum(1 for e, _, _ in items if st.get(e, (0, ""))[1] in ("released", "signoff")); miss = sum(1 for e, _, _ in items if e not in inv and e not in st)
            scored.append((round(100 * done / len(items)) if items else 0, mid, len(items), miss))
        for i, (pct, mid, k, miss) in enumerate(sorted(scored, reverse=True)):
            fill = "#d5e8d4" if pct >= 80 else "#fff2cc" if pct >= 50 else "#ffe6cc" if pct >= 20 else "#f5f5f5"
            cells.append(_cell(nid(), did, f"{mid}\n{pct} % of {k}" + (f" · {miss} not in the inventory" if miss else ""), 8 + (i % cols) * (W + 8), 36 + (i // cols) * (BH + 8), W, BH,
                               f"rounded=1;whiteSpace=wrap;html=1;fontSize=9;align=left;spacingLeft=4;fillColor={fill};strokeColor=#999999;"))
        x += cols * (W + 8) + 30
        if x > 1300: x = 20; y += h + 30
    return cells


def write(machine=None):
    M = machines(); inv = inventory(); st = status(); pages = []
    if machine:
        if machine not in M: return None, f"{machine}: not a machine of lib/machines-factory.txt or lib/machines-from-elements.txt ({len(M)} known)"
        dept, items = M[machine]; cells, counts = machine_page(machine, dept, items, inv, st); pages.append(_page(machine, cells))
    pages.append(_page("the line", line_page(st))); pages.append(_page("the machines", factory_page(M, inv, st)))
    os.makedirs(OUT, exist_ok=True); path = os.path.join(OUT, (machine or "factory") + ".drawio")
    open(path, "w", encoding="utf-8").write('<mxfile host="complexes.org" type="device">' + "".join(pages) + "</mxfile>")
    return path, (f"{machine}: {counts}" if machine else f"{len(M)} machines")
