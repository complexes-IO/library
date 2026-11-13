#!/usr/bin/env python3
"""capacitor-run: motor-run capacitor, 10 uF, 450 V AC, a cylindrical can Ø45 x 95 with two screw terminals on its cap, held to the
back panel by a strap bracket with two panel-screw holes. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral
design of the ETIM 10.0 class EC001516 "Capacitor", built to the class values in spec.md "## Class values"; no maker's datasheet.
What it meets comes from the standards on file: the two panel-screw holes are ISO 273 medium clearance for M5
(lib/standards/holes.csv); their pattern, and every other size, is a design choice, said so in spec.md. Modelled from the outside in:
the can standing on its axis (z), the strap round it and the strap's foot on the panel, the terminal cap with two screw-clamp blocks
and the barrier between them; the film winding, its discharge resistor and its pressure disconnector are not modelled in 1.0."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "capacitor-run", "1.1", "device"
TITLE = "motor-run capacitor 10 uF 450 V AC, cylindrical can 45 x 95, two screw terminals, strap bracket for two M5 panel screws (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Capacitor (ETIM 10.0 EC001516); class values in spec.md; panel-screw holes ISO 273 medium for M5 "
            "(lib/standards/holes.csv); sizes and the hole pattern are design choices; the terminals' conductor range is open (spec.md)")
ORIGIN = "surface-mount device: back face (the strap's foot) y = 0, left mounting hole x = 0, z = 0, body toward -y"
COMMAND = "CAPRUN"
PARAMS = {}

# ---- can and strap (design choices; Class values 6 to 9 in spec.md)
CAN_R, CAN_H = 22.5, 95.0              # can Ø45.0 x 95.0, centred on the strap in z (z -47.5 ... 47.5)
STRAP_T, STRAP_H = 1.5, 16.0           # strap ring round the can: sheet thickness, height (z -8 ... 8)
FOOT_L, FOOT_T = 80.0, 2.0             # the strap's foot on the panel: length (x), sheet thickness (y); its height is the strap's
PITCH = 64.0                           # panel-screw hole pattern (x); the can's axis at its middle
HOLE_D = 5.5                           # Ø5.5 = ISO 273 medium for M5 (holes.csv)
AXIS = (PITCH / 2, -FOOT_T - CAN_R - STRAP_T)   # can axis x, y: the strap touches the foot's face along one line
# ---- terminal end (design choices); the conductor range is open (spec.md)
CAP_R, CAP_T = 20.5, 3.0               # terminal cap Ø41.0 x 3.0 on the can's top
TB = (12.0, 12.0, 9.0, 10.0)           # terminal block: width (x), depth (y), height (z), its centre this far either side of the axis (x)
BARRIER = (2.0, 16.0, 11.5)            # insulating barrier between the blocks: x, y, z (2.5 above the blocks)
HEAD_R, HEAD_T = 2.2, 1.2              # terminal screw head
ENTRY = (5.0, 4.0, 0.5, 4.0)           # wire entry slot: width (y), height (z), cut into the outer side face, centre 4.0 below the block's top

def build():
    P = Prims(); G = "M-GALV"; B = "M-BLACK-PA"; ax, ay = AXIS
    z0, z1 = -CAN_H / 2, CAN_H / 2
    P.cyl("M-GREY-PA", (ax, ay, z0), (ax, ay, z1), CAN_R)                                      # the can
    # ---------------- strap bracket: ring round the can, foot on the panel with two M5 holes
    ring = P.cyl(G, (ax, ay, -STRAP_H / 2), (ax, ay, STRAP_H / 2), CAN_R + STRAP_T)
    P.hole("M-GASKET", (ax, ay, -STRAP_H / 2 - 1), (ax, ay, STRAP_H / 2 + 1), CAN_R, ring)      # the strap's bore on the can (features.csv)
    xl = ax - FOOT_L / 2
    foot = P.box(G, xl, -FOOT_T, -STRAP_H / 2, FOOT_L, FOOT_T, STRAP_H)
    for x in (0.0, PITCH):
        P.hole("M-GASKET", (x, 0.5, 0), (x, -FOOT_T - 0.5, 0), HOLE_D / 2, foot)               # M5 panel screw, ISO 273 medium
    # ---------------- terminal end: cap, two screw-clamp blocks and the barrier between them
    P.cyl(B, (ax, ay, z1), (ax, ay, z1 + CAP_T), CAP_R)
    zc = z1 + CAP_T; w, d, h, off = TB; ew, eh, ed, ein = ENTRY
    for side, mk in ((-1, "1"), (1, "2")):
        cx = ax + side * off
        blk = P.box(B, cx - w / 2, ay - d / 2, zc, w, d, h)
        n = f"t-{mk}"
        P.cyl(f"node:{n}|M-ZINC", (cx, ay, zc + h), (cx, ay, zc + h + HEAD_T), HEAD_R)
        P.pivot(n, "port", (cx, ay, zc + h + HEAD_T), axis=(0, 0, 1), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        xf = cx + side * w / 2; ze = zc + h - ein
        P.cutbox("M-GASKET", xf - (ed if side > 0 else 1.0), ay - ew / 2, ze - eh / 2, ed + 1.0, ew, eh, blk)   # out past the outer face
        P.box("M-GASKET", xf - (ed if side > 0 else 0.0), ay - ew / 2, ze - eh / 2, ed, ew, eh)                 # the dark slot in its cut
    bx, by, bz = BARRIER
    P.box(B, ax - bx / 2, ay - by / 2, zc, bx, by, bz)
    P.collider("env", xl, ay - CAN_R - STRAP_T, z0, FOOT_L, CAN_R + STRAP_T - ay, CAN_H / 2 + CAP_T + bz - z0)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear strap foot and panel holes", az=60, el=20),
            dict(name="plan strap and can", az=270, el=89),
            dict(name="terminal end", az=230, el=40, center=(32, -26, 56), height=34)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
