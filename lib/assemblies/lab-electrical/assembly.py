#!/usr/bin/env python3
"""lab-electrical: the Electrical / motor control lab, bay 2 of the campus Labs building (lib/labs.csv; toolkit/rooms.py).
The room's shell comes from the campus model's own files; the machines are placed by bom.csv (an assembly or an element a row).
Outputs: out/lab-electrical.glb (with its shell: walk the room on its own), out/lab-electrical-campus.glb (contents only: the
campus Labs building brings the walls) and out/lab-electrical-campus.json (where the campus places it, metres)."""
import csv, json, os, sys, importlib.util
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, cadout, preview, rooms
from toolkit.prims import Prims, transform, extents
ID = "lab-electrical"; VERSION = "0.1"; HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
ASM = os.path.dirname(HERE)
ROOM = {r["key"]: r["value"] for r in csv.DictReader(open(os.path.join(HERE, "room.csv"), encoding="utf-8"))}
def sub(aid):
    spec = importlib.util.spec_from_file_location(f"asm_{aid.replace('-', '_')}", os.path.join(ASM, aid, "assembly.py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def build(report=True, override=None, shell=True):
    b = rooms.bay(int(ROOM["bay"])); P = Prims(); P.assembly = True
    if shell: rooms.shell(P, b)
    placed = []
    for row in library.read_bom(os.path.join(HERE, "bom.csv")):
        if os.path.isdir(os.path.join(ASM, row["element"])):                       # a machine (an assembly)
            body = sub(row["element"]).build(report=False, override=(override or {}).get(row["tag"])); tag = row["tag"]
            tp = transform(body, (row["x"], row["y"], row["z"]), row["yaw"], lambda n: f"{tag}.{n}", len(P)); b0 = len(P); P.extend(tp); P.pivots.update(tp.pivots)
            P.owners.extend(tp.owners); P.owners.append((b0, len(P), tag, row["element"]))
            P.hosts.update(tp.hosts); P.parents.update(tp.parents); P.parents[tag] = row["parent"]; P.params.update(tp.params)
        else: library.place(P, row)
        placed.append(row)
    if report: print(f"{ID}: bay {b['n']} of the Labs building, clear {b['dx']:.0f} x {b['dy']:.0f} mm, {b['h']:.0f} mm to the eaves; door {b['door_w']:.0f} x {b['door_h']:.0f} "
                     f"at x {b['door_x']:.0f}; placed {len(placed)}: " + ", ".join(f"{r['tag']}={r['element']}" for r in placed))
    return P
if __name__ == "__main__":
    P = build(); cadout.write_lsp(os.path.join(OUT, ID + ".lsp"), "ROOM", P, ID); print(" ", cadout.write_glb(os.path.join(OUT, ID + ".glb"), P, ID)["triangles"], "triangles")
    for st, rule, where, msg in rooms.check(ID, P, rooms.bay(int(ROOM["bay"])), float(ROOM["volts_to_ground"])): print(f"  {st:6} {rule} {where}: {msg}")
    C = build(report=False, shell=False); cadout.write_glb(os.path.join(OUT, ID + "-campus.glb"), C, ID)
    b = rooms.bay(int(ROOM["bay"]))
    json.dump(dict(id=ID, version=VERSION, bay=b["n"], lab=rooms.labs()[b["n"]]["name"], glb=ID + "-campus.glb", units="mm in the glb; metres here",
                   campus_origin_m=b["campus_origin"], scale_to_campus=0.001, yaw_deg=0,
                   note="the room frame's origin is the bay's inner south-west corner (wall faces); +x east, +y north, +z up"),
              open(os.path.join(OUT, ID + "-campus.json"), "w", encoding="utf-8"), indent=1)
    preview.render(preview.mesh(C), f"{ID}: the Electrical lab, bay 2 (contents)", az=220, el=28, fname="preview-iso.png", out=OUT)
