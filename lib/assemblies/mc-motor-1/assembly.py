#!/usr/bin/env python3
"""mc-motor-1: the machine side of the motor-starter cell: bench, motor, field I/O block, operator station. Plugs into pm-motor-starter."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, cadout, preview
from toolkit.prims import Prims
ID = "mc-motor-1"; VERSION = "1.0"; HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
def build(report=True, override=None):
    P = Prims(); P.assembly = True; placed, planned = [], []
    for row in library.read_bom(os.path.join(HERE, "bom.csv")):
        if row["version"].strip() in ("", "-") or not os.path.isdir(os.path.join(library.ELEMENTS, row["element"])): planned.append(row); continue
        library.place(P, row); placed.append(row)
    if report: print(f"{ID}: placed {len(placed)}; planned {len(planned)}: " + ", ".join(f"{r['tag']}={r['element']}" for r in planned))
    return P
if __name__ == "__main__":
    P = build(); cadout.write_lsp(os.path.join(OUT, ID + ".lsp"), "MACHINE", P, ID); cadout.write_glb(os.path.join(OUT, ID + ".glb"), P, ID)
    preview.render(preview.mesh(P), f"{ID} field devices (bench and motor planned)", az=250, el=20, fname="preview-front.png", out=OUT)
