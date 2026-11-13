#!/usr/bin/env python3
"""tag-plate: the institute's plates: panel nameplate, device tag, operator legend plate. Own element; sizes per the 2026-11-03 ruling."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "tag-plate", "1.0", "plate"
TITLE = "nameplate / device tag / legend plate, engraved or printed, our own"
TOOLKIT = "1.3"
BASELINE = "own: panel nameplate 120 x 60 x 1.5 anodised aluminium (2 x Ø3.5 at 100 x 40), device tag 30 x 12 x 1 adhesive, legend plate 30 x 50 x 1 (pbs-6h-22 spec)"
ORIGIN = "panel device: back face on the panel y = 0, lower-left corner x = 0, z = 0, plate toward -y"
COMMAND = "TAG"
PARAMS = dict(kind="tag", text="")
KINDS = dict(tag=(120.0, 60.0, 1.5, "M-ALU-ANOD"), device=(30.0, 12.0, 1.0, "M-BLACK-PA"), legend=(30.0, 50.0, 1.0, "M-BLACK-PA"))

def build(kind="tag", text=""):
    P = Prims(); w, h, t, mat = KINDS[kind]
    pl = P.box(mat, 0, -t, 0, w, t, h)
    if kind == "tag":
        for cx in (10.0, 110.0): P.hole("M-GASKET", (cx, -t - 1, 10.0), (cx, 1, 10.0), 1.75, pl); P.hole("M-GASKET", (cx, -t - 1, 50.0), (cx, 1, 50.0), 1.75, pl)
        for cx in (10.0, 110.0):
            for cz in (10.0, 50.0): P.cyl("M-ZINC", (cx, -t, cz), (cx, -t - 0.8, cz), 2.6)
        P.box("M-BLACK-PA", 8, -t - 0.1, 18, w - 16, 0.1, 26)                                       # engraved text field (decal: three lines)
    elif kind == "legend":
        P.hole("M-GASKET", (w / 2, -t - 1, h * 0.65), (w / 2, 1, h * 0.65), 11.15, pl)              # Ø22.3 cut-out, centre at 0.65 h
        P.box("M-WHITE-PA", 4, -t - 0.1, 4, w - 8, 0.1, 8)                                           # text field
    else:
        P.box("M-WHITE-PA", 2, -t - 0.1, 2, w - 4, 0.1, h - 4)
    P.collider("env", 0, -t - 1, 0, w, t + 1, h)
    return P

PREVIEWS = [dict(name="panel nameplate", az=262, el=15), dict(name="device tag", az=262, el=15, params=dict(kind="device")), dict(name="legend plate", az=262, el=15, params=dict(kind="legend"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
