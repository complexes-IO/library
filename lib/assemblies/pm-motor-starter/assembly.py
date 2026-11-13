#!/usr/bin/env python3
"""pm-motor-starter: the control panel as a portable unit: cabinet, rails, ducts, devices, and the ports on its right wall.
Nothing of the machine lives here; the machine plugs in through the ports."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, cadout, preview
from toolkit.prims import Prims, nodes
ID = "pm-motor-starter"; VERSION = "1.0"; HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
def build(report=True, override=None):
    P = Prims(); P.assembly = True; placed, planned = [], []
    for row in library.read_bom(os.path.join(HERE, "bom.csv")):
        if override and row["tag"] in override: row = {**row, "params": {**row["params"], **override[row["tag"]]}}
        if row["version"].strip() in ("", "-") or not os.path.isdir(os.path.join(library.ELEMENTS, row["element"])): planned.append(row); continue
        library.place_on_hosts(P, row); placed.append(row)                 # a row on enc-1.door-r / wall-r / gland-plate is mounted: the host gets its cut-out
    if report: print(f"{ID}: placed {len(placed)}; planned {len(planned)}: " + ", ".join(f"{r['tag']}={r['element']}" for r in planned))
    return P
if __name__ == "__main__":
    P = build(); cadout.write_lsp(os.path.join(OUT, ID + ".lsp"), "PANEL", P, ID); print(" ", cadout.write_glb(os.path.join(OUT, ID + ".glb"), P, ID)["nodes"][:6], "...")
    Fo = preview.mesh(build(report=False, override={"enc-1": dict(swing_l=110, swing_r=110)}))
    preview.render(Fo, f"{ID} doors open", az=265, el=12, center=(762, 240, 1400), height=1500, fname="preview-open.png", out=OUT)
