#!/usr/bin/env python3
"""contactor-18a-1no: power contactor, 3 main N.O. poles, AC-3 18 A at 400 V, 24 V DC coil, one auxiliary N.O. 13-14, on the 35 mm
rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000066 "Power
contactor, AC switching", built to the class values in spec.md "## Class values"; no maker's datasheet. Inventory row pinned 6
(request panel-6 1a, the HPU motor's contactor in pnl-press-hydraulic). What it meets comes from the files on hand: the rail clip
from toolkit/din.py (rail_clip, the 35 x 7.5 rail of din-rail-35 / EN 60715 TH35-7.5) and the overload relay below it from
overload-9a-1no1nc 1.1 (its pin row, pin and sleeve sizes and width read from that element, its rear hooks from its build), so the
overload mounts on this contactor as it does on contactor-9a-1no1nc; every other size is a design choice, said so in spec.md.
Modelled from the outside in, as relay-aux-2no2nc: base with the terminal shoulders, a box-clamp entry per main terminal (the
overload's pins enter the lower three), front housing with the coil and auxiliary terminals on its end faces, and the contact
carrier's front tab in its window (the state the twin shows); the magnet system and the contacts inside are not modelled in this
version. 1.1 (elec-r46): text only (review elec-r35 findings 1 to 3), the geometry is 1.0's."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "contactor-18a-1no", "1.1", "device"
TITLE = "power contactor 3-pole, AC-3 18 A, 24 V DC coil, 1 NO auxiliary, screw terminals, 35 mm rail, overload direct mount (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Power contactor, AC switching (ETIM 10.0 EC000066); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); lower terminals at overload-9a-1no1nc 1.1's pin row (read from that "
            "element; its pin row depth and hook form are that element's own open figures, followed here by library.load); sizes are "
            "design choices; the terminals' conductor range is open (spec.md)")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "CT18"
PARAMS = dict(operated=False)

# ---- what it meets: the overload relay below it (overload-9a-1no1nc 1.1; one figure, one home)
OV = library.load("overload-9a-1no1nc", "1.1")
RAIL_IN = 7.5                        # rail crown to the mounting plane (din.rail_clip depth; din-rail-35's 7.5)
W = OV.W                             # 45.0: the overload's width, so the stack is flush on both sides (overload x = this x)
PITCH = OV.PIN_PITCH                 # 14.0: main pole pitch = the overload's pin pitch
XP = OV.PIN_X                        # pole centres x 5.3, 19.3, 33.3 (the overload's pin row, 3.2 left of the body's centre)
CLAMP_Y = RAIL_IN + OV.PIN_Y         # -34.5: the overload's pin row depth (its back face on the mounting plane, y = +7.5 here)
ENTRY = 2.4                          # box-clamp entry half-width: takes the overload's sleeve (r 2.2) and pin (r 1.25); design choice
ENTRY_D = 16.0                       # entry depth from the end face: the overload's pin reaches OV.PIN_TOP = 14.1 in; design choice
HOOK_X = (8.0, OV.W - 8.0)           # the overload's two rear hooks (overload-9a-1no1nc 1.1 build(): x 8.0 and W - 8.0, y -2.75 from
HOOK_Y, HOOK_R = RAIL_IN - 2.75, 2.0  # the mounting plane, r 2.0, up to HOOK_TOP 9.7 above its top): their slots in the lower lugs
HOOK_SLOT, HOOK_SLOT_D = 2.2, 11.0   # slot half-width and depth (0.2 clear of the hook, 1.3 above its top); design choice
LUG = (10.0, 12.0)                   # lower lug width (x) and height (z) behind the base, each round a hook slot; design choice

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
H = 85.0                             # height: z -42.5 ... 42.5, centred on the rail; the overload's top meets the bottom face
D_BASE = 42.0                        # base and terminal shoulders: front face at y -42
D = 84.0                             # front housing face at y -84; 91.5 overall with the 7.5 behind the crown
FH_X, FH_Z = (2.0, 43.0), (-30.0, 30.0)   # front housing (coil and contact carrier cover)
HEAD_R, HEAD_T, HEAD_DZ = 2.2, 1.2, 6.5   # main terminal screw heads on the shoulders: radius, height, centre 6.5 in from the end face
CTL = (("A1", "A2", 10.0), ("13", "14", 35.0))   # coil and auxiliary terminals: top mark, bottom mark, x; on the front housing's end faces
CTL_Y = -D + 8.0                     # their screws 8 behind the front face
WIN = (16.5, 28.5, -18.0, -8.0, 18.0)     # carrier window x0, x1, z0, z1, pocket depth behind the face
TAB = (17.5, 27.5, -17.0, -9.0, 1.0, 9.0)  # carrier tab x0, x1, z0, z1, set back from the face, length (y)
TRAVEL = 4.0                         # carrier travel toward the mounting plane (+y) when the coil pulls in; design choice

def build(operated=False):
    P = Prims(); G = "M-GREY-PA"
    base = P.box(G, 0, -D_BASE, -H / 2, W, D_BASE, H)                                        # base with the terminal shoulders
    fh = P.box(G, FH_X[0], -D, FH_Z[0], FH_X[1] - FH_X[0], D - D_BASE, FH_Z[1] - FH_Z[0])   # front housing
    din.rail_clip(P, 0, W)                                                                   # the rail latch (toolkit contract)
    # ---------------- main terminals: 1 3 5 (line, top) and 2 4 6 (load, bottom); a screw head per terminal on the shoulder, its
    # box-clamp entry cut up into the end face at the overload's pin row (the lower three take the overload's pins)
    for i, x in enumerate(XP):
        for up, n in ((True, 2 * i + 1), (False, 2 * i + 2)):
            s = 1 if up else -1; ze = s * H / 2; zc = ze - s * HEAD_DZ; t = f"t-{n}"
            P.cyl(f"node:{t}|M-ZINC", (x, -D_BASE, zc), (x, -D_BASE - HEAD_T, zc), HEAD_R)
            P.pivot(t, "port", (x, -D_BASE - HEAD_T, zc), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
            z0 = (ze - ENTRY_D) if up else (ze - 1.0)
            P.cutbox("M-GASKET", x - ENTRY, CLAMP_Y - ENTRY, z0, 2 * ENTRY, 2 * ENTRY, ENTRY_D + 1.0, base)                # out past the end face
    # ---------------- lower lugs behind the base, down to the mounting plane, each with the slot an overload hook enters
    for hx in HOOK_X:
        lug = P.box(G, hx - LUG[0] / 2, 0, -H / 2, LUG[0], RAIL_IN, LUG[1])
        P.cutbox("M-GASKET", hx - HOOK_SLOT, HOOK_Y - HOOK_SLOT, -H / 2 - 1.0, 2 * HOOK_SLOT, 2 * HOOK_SLOT, HOOK_SLOT_D + 1.0, lug)
    # ---------------- coil A1 / A2 and auxiliary 13 / 14 on the front housing's end faces
    for top, bot, x in CTL:
        for s, mk in ((1, top), (-1, bot)):
            ze = FH_Z[1] if s > 0 else FH_Z[0]; t = f"t-{mk}"
            P.cyl(f"node:{t}|M-ZINC", (x, CTL_Y, ze), (x, CTL_Y, ze + s * HEAD_T), HEAD_R)
            P.pivot(t, "port", (x, CTL_Y, ze + s * HEAD_T), axis=(0, 0, s), range=(0, 0), unit="screw", gender="none")
    # ---------------- front: the contact carrier's tab in its window, legend field
    x0, x1, z0, z1, pd = WIN
    P.cutbox("M-GASKET", x0, -D - 0.5, z0, x1 - x0, pd + 0.5, z1 - z0, fh)                   # carrier window and its pocket
    tx0, tx1, tz0, tz1, back, ln = TAB; ty = -D + back + (TRAVEL if operated else 0.0)
    P.box("node:carrier|M-YELLOW-PA", tx0, ty, tz0, tx1 - tx0, ln, tz1 - tz0)                 # carrier front tab: the contact state shown
    P.pivot("carrier", "translate", ((tx0 + tx1) / 2, -D + back, (tz0 + tz1) / 2), axis=(0, 1, 0), range=(0, TRAVEL))
    P.box("M-WHITE-PA", 6.0, -D - 0.1, 2.0, 33.0, 0.1, 22.0)                                  # legend field (decal: marks, 24 V DC, generic label)
    P.collider("env", 0, -D - 0.1, -H / 2, W, D + 0.1 + RAIL_IN, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip and hook lugs", az=60, el=25),
            dict(name="top clamp entries", az=230, el=55, center=(22.5, -30, 42.5), height=40),
            dict(name="operated carrier pulled in", az=255, el=10, center=(22.5, -84, -13), height=20, params=dict(operated=True))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
