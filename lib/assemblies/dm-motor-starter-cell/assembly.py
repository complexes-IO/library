#!/usr/bin/env python3
"""dm-motor-starter-cell = pm-motor-starter (the panel) + mc-motor-1 (the machine) + connections.csv (the cables between them).
Sub-assemblies are placed like elements; cables are routed port to port by section (toolkit 1.3 does the routing; until then they are listed)."""
import csv, os, sys, importlib.util
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, cadout, preview
from toolkit.prims import Prims, transform, nodes
ID = "dm-motor-starter-cell"; HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
ASM = os.path.dirname(HERE)
def sub(aid):
    spec = importlib.util.spec_from_file_location(f"asm_{aid}", os.path.join(ASM, aid, "assembly.py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def build(report=True, override=None):
    P = Prims(); P.assembly = True
    for row in library.read_bom(os.path.join(HERE, "bom.csv")):
        if row["parent"] == "connections": continue
        if os.path.isdir(os.path.join(ASM, row["element"])):
            m = sub(row["element"]); body = m.build(report=False, override=(override or {}).get(row["tag"]))
            tag = row["tag"]; tp = transform(body, (row["x"], row["y"], row["z"]), row["yaw"], lambda n: f"{tag}.{n}", len(P)); b0 = len(P); P.extend(tp); P.pivots.update(tp.pivots)
            P.owners.extend(tp.owners); P.owners.append((b0, len(P), tag, row["element"])); P.hosts.update(tp.hosts); P.parents.update(tp.parents); P.parents[tag] = row["parent"]; P.params.update(tp.params)
        else: library.place(P, row)
    conns = list(csv.DictReader(open(os.path.join(HERE, "connections.csv"), encoding="utf-8")))
    if report:
        print(f"{ID}: {len(nodes(P))} nodes from the two sub-assemblies; {len(conns)} connections by section:")
        for sec in sorted({c["section"] for c in conns}): print(f"   {sec}: " + ", ".join(c["from"] + " -> " + c["to"] for c in conns if c["section"] == sec))
        missing = [c for c in conns if not any(c["from"].split(".", 1)[1] == n or c["from"] == n for n in nodes(P))]
        print(f"   ports not yet in the model: {len(missing)}" + (f" ({', '.join(c['from'] for c in missing)})" if missing else ""))
    return P
if __name__ == "__main__":
    P = build(); cadout.write_lsp(os.path.join(OUT, ID + ".lsp"), "CELL", P, ID); print(" ", cadout.write_glb(os.path.join(OUT, ID + ".glb"), P, ID)["triangles"], "triangles")
    preview.render(preview.mesh(P), f"{ID} panel and machine", az=250, el=18, fname="preview-front.png", out=OUT)
    Fo = preview.mesh(build(report=False, override={"panel-1": {"enc-1": dict(swing_l=110, swing_r=110)}}))
    preview.render(Fo, f"{ID} panel open, machine side", az=262, el=14, fname="preview-open.png", out=OUT)
