#!/usr/bin/env python3
"""mcb-3p-c10: miniature circuit breaker, 3-pole C10, DIN 43880 module. Brief: references/measure.md (maker's datasheet and 2-D drawing:
17.7 per pole, 105 high, 73 deep, toggle 16.6 x 3.7 proud, terminal spacing 66, rail datum 45). Maker and part number only in
references/source.txt (OPERATING.md 6, DOC-006).
1.4 (elec-r30): every terminal screw is a port node t-<pole>-line / t-<pole>-load (the core's pin-nodes note of 2026-11-11, request
panel-4 item 1): the pivot at the wire entry's mouth on the end face, axis the way the wire goes in, kind port, unit screw, gender
none (PIN-002). Nodes added, none moved: a minor. The node names say pole and side, not the printed mark (the marks are an
Assumption (A) in behaviour.csv), so EM's ruling on the marks changes no node name.
1.5 (elec-r37; review mcb-3p-c10-1.4 findings 1, 2, 3, 5): text only. The 73.0 depth's planes and the shoulder line are one
"Assumption (B)" each with its reason, the rail clip cites its contract (EN 60715 TH35-7.5) and says what of the brief is not
modelled, the toggle swing's class is in the code. Geometry as 1.4."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "mcb-3p-c10", "1.5", "device"
TITLE = "miniature circuit breaker, 3-pole 10 A C-curve, 35 mm rail"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet and 2-D drawing (references/measure.md, references/source.txt: 53.1 x 105.0 x 73.0, pole pitch 17.7, terminals 66.0; sheet p. 1 / p. 13)"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face of pole 1 x = 0, body toward -y"
COMMAND = "MCB3"
PARAMS = dict(poles=3, rating="C10")
PITCH, H, D, DT = 17.7, 105.0, 73.0, 3.7        # module pitch, height, depth overall from the mounting plane (the clip region's back, y +7.5) to the toggle face (y -65.5): the planes Assumption (B), spec.md Dimensions; toggle proud
CLIP = 7.5
FRONT = D - CLIP - DT                            # raised front face at -61.8 (toggle face at -65.5)
SHOULDER = 45.0 - CLIP                           # terminal shoulders 45 from the rail mounting plane = 37.5 from the crown: Assumption (B), the drawing's 45.0 read as this line (spec.md Dimensions)
TERM = 66.0                                      # terminal screw spacing

def build(poles=3, rating="C10"):
    P = Prims(); W = PITCH * poles
    P.box("M-GREY-PA", 0, -SHOULDER, -H / 2, W, SHOULDER, H)                                      # base to the shoulder line
    P.box("M-GREY-PA", 0, -FRONT, -22.5, W, FRONT - SHOULDER, 45.0)                               # raised 45 mm front
    din.rail_clip(P, 0, W)                                                                         # the library's contract for the 35 x 7.5 rail (EN 60715 TH35-7.5, din-rail-35)
    for i in range(poles):
        x0 = i * PITCH; cx = x0 + PITCH / 2
        for sz, side in ((1, "line"), (-1, "load")):                                              # captive screw terminal per pole, line top, load bottom
            n = f"t-{i + 1}-{side}"                                                               # the port node (1.4): the screw head carries it
            P.cyl(f"node:{n}|M-ZINC", (cx, -SHOULDER, sz * TERM / 2), (cx, -SHOULDER - 1.2, sz * TERM / 2), 2.6)
            P.box("M-GASKET", cx - 2.3, -SHOULDER + 3, sz * H / 2 - (0.4 if sz > 0 else 0.1), 4.6, 10, 0.5)   # wire entry 0.1 proud: flush it flickers in glTF (1.2)
            P.pivot(n, "port", (cx, -SHOULDER + 8.0, sz * H / 2), axis=(0, 0, -sz), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp; at the entry's mouth on the end face, axis in
        din.indicator(P, f"indicator-{i + 1}", x0, PITCH, -FRONT, 14.0)
        P.box("M-WHITE-PA", x0 + 2, -FRONT - 0.2, -20, PITCH - 4, 0.2, 8)                         # rating label field (decal: rating)
    din.toggle(P, "toggle", 0, W, -FRONT, 0.0)                                                     # one common handle; swing +/-25: Assumption (C), a handle swing (spec.md Named nodes)
    P.collider("env", 0, -(D - CLIP), -H / 2, W, D, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="terminals and rail clip", az=60, el=25), dict(name="toggle close-up", az=255, el=10, center=(26.5, -70, 0), height=70)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
