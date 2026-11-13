#!/usr/bin/env python3
"""hose-reel-single-npt: a hand-crank hose reel for one hose: a galvanised drum with two flanges turning on axle stubs in the two
side frames of a floor (or wall) base, a crank on the drum's +x end, and on its -x end a fixed brass swivel boss with a female NPT 3/8
inlet on the drum's axis, where the supply line comes in while the drum turns. Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC010439 "Hose reel, single hose" (synonyms "Hose car", "Hose wagon"), the next class of the Hoses
group (EG015510) in generic.next_classes' order after EC010745 (pneu-r119, lib/rounds/pneu/next.md); the class values it is designed
to are in spec.md "## Class values". No dimensional standard shapes a hose reel: its base, frames, drum and crank are design choices.
Its four mounting holes are M10 clearance, medium (ISO 273, lib/standards/holes.csv); the screws are the host's (not built, so not
placed). The inlet is pneu.py D1's NPT, bored at E1 + h from pneu.NPT (ASME B1.20.1 by its formulas), through a round land 0.2 proud
of the boss's end face (cap-hex-npt's port), the pivot on the land's outer face. The hose wound on the drum is not drawn (it is its own
element, hose-flex-npt or tube-pneu) and its inner end's joint inside the hub is not modelled. One moving part: the drum with its
flanges, stubs and crank (`drum`, rotate about +x). No vendor file was opened (pneu-r120)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "hose-reel-single-npt", "1.0", "device"
TITLE = "generic hose reel, single hose, hand crank, galvanised drum on a red steel stand, female NPT 3/8 swivel inlet, four M10 holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hose reel, single hose (ETIM 10.0 EC010439), a hand-crank drum between two side frames on a "
            "base; inlet NPT 3/8 female (toolkit/pneu.py D1) bored at E1 + h from pneu.NPT (calculated from ASME B1.20.1's "
            "formulas); mounting holes M10 clearance medium (ISO 273, lib/standards/holes.csv); base, frames, drum and crank are "
            "design choices")
ORIGIN = ("the centre of the base's underside (the mounting face, z = 0); the drum's axis along x at z = 176, the crank on +x, the "
          "inlet on -x; the hose pays out along y")
COMMAND = "HOSE-REEL-SINGLE-NPT"
PARAMS = dict()

PORT = "NPT3/8"                    # design choice within pneu.THREADS (D1): the inlet, the largest of the series
BASE = (220.0, 280.0, 6.0)         # design choice: the base plate, x by y by thickness, centred on the origin in plan
HOLE_D, HOLE_XY = 11.0, (90.0, 120.0)   # M10 clearance, medium (ISO 273 H13: 11.0 to 11.27; holes.csv), at (±90, ±120)
FRAME_T, FRAME_IN = 6.0, 67.0      # design choice: the two side frames, 6 thick, inner faces at x = ±67
FRAME_D, FRAME_TOP = 120.0, 216.0  # design choice: the frames 120 deep (y) and standing to z = 216
AXIS_Z = 176.0                     # design choice: the drum's axis height above the mounting face
HUB_D, HUB_L = 150.0, 120.0        # design choice: the drum's hub (the hose's core) Ø150, 120 long between the flanges
FLANGE_D, FLANGE_T = 320.0, 4.0    # design choice: the drum's two flanges Ø320, 4 thick
STUB_D = 25.0                      # design choice: the axle stubs Ø25, turning in Ø25 plain bores in the frames, face to face
CRANK_HUB = (40.0, 10.0)           # design choice: the crank's hub Ø40, 10 long, on the +x stub's end
ARM = (8.0, 24.0, 134.0)           # design choice: the crank arm, x thick, y wide, z long from the axis (at rest pointing up)
HANDLE = (25.0, 80.0, 120.0)       # design choice: the crank handle Ø25, 80 long along +x, its axis 120 from the drum's axis
BOSS_D, BOSS_L = 40.0, 30.0        # design choice: the swivel boss on the -x frame's outer face, on the drum's axis
LAND_D, LAND_T = 26.0, 0.2         # the round land round the inlet bore (the port node), 0.2 proud of the boss's end (GEO-050)
HOSE_OD = 16.0                     # class value: the hose the drum is sized for: 3/8 in air hose, 16 outside diameter
MAT_FRAME, MAT_DRUM, MAT_AXLE = "M-RED", "M-GALV", "M-SILVER"
MAT_BOSS, MAT_HANDLE = "M-BRASS", "M-GREY-PA"
assert PORT in pneu.THREADS
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 + 2, the 2 a run-out past the male's effective thread (tank 2.0)

_X1 = HUB_L / 2                    # 60: hub to flange
_X2 = _X1 + FLANGE_T               # 64: flange's outer face
_GAP = FRAME_IN - _X2              # 3: running clearance between each flange and its frame
_X3 = FRAME_IN + FRAME_T           # 73: the frame's outer face, where each stub ends flush
_X4 = _X3 + CRANK_HUB[1]           # 83: the crank hub's outer face, where the arm starts
_X5 = _X4 + ARM[0]                 # 91: the arm's outer face, where the handle starts
_XB = _X3 + BOSS_L                 # 103: the boss's end face (at x = -103)


def layers():
    """whole layers of hose the drum holds between the hub and 10 below the flanges' rim"""
    return int(((FLANGE_D - 20.0) - HUB_D) / 2 // HOSE_OD)


def capacity():
    """the hose length the drum holds, m: turns per layer x the layers' mean circumferences (a plain count, no squash)"""
    turns = int(HUB_L // HOSE_OD)
    return turns * sum(math.pi * (HUB_D + HOSE_OD * (2 * k + 1)) for k in range(layers())) / 1000.0


assert _GAP >= 2.0                                                   # the flanges never rub the frames
assert AXIS_Z - FLANGE_D / 2 - BASE[2] >= 10.0                       # 10 between the flanges and the base plate
assert FRAME_TOP - AXIS_Z - STUB_D / 2 >= 3 * FRAME_T / 2            # 27.5 of steel above each frame's bore
assert FRAME_D / 2 - STUB_D / 2 >= 3 * FRAME_T / 2                   # 47.5 beside it
assert BASE[0] / 2 - HOLE_XY[0] - HOLE_D / 2 >= 5.0                  # 14.5 of plate between each hole and the base's end
assert BASE[1] / 2 - HOLE_XY[1] - HOLE_D / 2 >= 5.0                  # and its side
assert HOLE_XY[0] - HOLE_D / 2 - _X3 >= 10.0                         # 11.5 between each hole and the frame (room for an M10 head)
assert HOLE_XY[1] - HOLE_D / 2 >= FRAME_D / 2 + 10.0                 # the holes stand clear of the frames' feet in y too
assert ARM[2] >= HANDLE[2] + HANDLE[0] / 2                           # the handle sits on the arm
assert AXIS_Z + ARM[2] < AXIS_Z + FLANGE_D / 2                       # the crank stays below the flanges' top at rest
assert BOSS_L >= BORE_L + 3.0 * 2                                    # the bore stays well inside the boss, its floor clear of the frame
assert BORE_L >= pneu.NPT[PORT]["engagement"]                        # deeper than a male's make-up (L1 + L3)
assert BORE_D + 2.0 < LAND_D < BOSS_D                                # the land rings its bore, inside the boss's end face
assert (BOSS_D - BORE_D) / 2 >= 3.0                                  # brass round the bore
assert layers() >= 4 and capacity() >= 15.0                          # class value: 15 m of 3/8 in hose fits (4 layers, 18.8 m)
assert min(BASE[2], FRAME_T, FLANGE_T, ARM[0]) >= 2.5 * 0.5          # every edge passes the AutoCAD gate's fillet pre-flight


def height(): return AXIS_Z + FLANGE_D / 2                          # 336: the mounting face to the flanges' top


def build():
    P = Prims()
    bx, by, bt = BASE
    base = P.box(MAT_FRAME, -bx / 2, -by / 2, 0, bx, by, bt)                                          # base plate
    for x in (-HOLE_XY[0], HOLE_XY[0]):
        for y in (-HOLE_XY[1], HOLE_XY[1]):
            P.hole(MAT_FRAME, (x, y, -1.0), (x, y, bt + 1.0), HOLE_D / 2, base)                       # M10 clearance, through
    for s in (-1, 1):
        x0 = FRAME_IN if s > 0 else -_X3
        fr = P.box(MAT_FRAME, x0, -FRAME_D / 2, bt, FRAME_T, FRAME_D, FRAME_TOP - bt)                 # side frame, on the base
        P.hole(MAT_FRAME, (s * (FRAME_IN - 1.0), 0, AXIS_Z), (s * (_X3 + 1.0), 0, AXIS_Z), STUB_D / 2, fr)   # axle bore, through
    a = lambda x: (x, 0, AXIS_Z)
    P.cyl(f"node:drum|{MAT_DRUM}", a(-_X1), a(_X1), HUB_D / 2)                                         # hub: the hose's core
    for s in (-1, 1):
        P.cyl(f"node:drum|{MAT_DRUM}", a(s * _X1), a(s * _X2), FLANGE_D / 2)                         # flange, face to face on the hub
        P.cyl(f"node:drum|{MAT_AXLE}", a(s * _X2), a(s * _X3), STUB_D / 2)                           # axle stub, through the frame's bore
    P.cyl(f"node:drum|{MAT_DRUM}", a(_X3), a(_X4), CRANK_HUB[0] / 2)                                 # crank hub on the +x stub's end
    t, w, l = ARM
    P.box(f"node:drum|{MAT_DRUM}", _X4, -w / 2, AXIS_Z - w / 2, t, w, l + w / 2)                      # crank arm, pointing up at rest
    hz = AXIS_Z + HANDLE[2]
    P.cyl(f"node:drum|{MAT_HANDLE}", (_X5, 0, hz), (_X5 + HANDLE[1], 0, hz), HANDLE[0] / 2)          # crank handle
    P.pivot("drum", "rotate", a(0), axis=(1, 0, 0), range=(0, 360), unit="deg")
    boss = P.cyl(MAT_BOSS, a(-_X3), a(-_XB), BOSS_D / 2)                                              # swivel boss, fixed to the -x frame
    P.hole("M-GASKET", a(-_XB - 1.0), a(-_XB + BORE_L), BORE_D / 2, boss)                             # inlet bore, NPT 3/8 at E1 + h
    land = P.cyl(f"node:{pneu.NODES['supply']}|{MAT_BOSS}", a(-_XB), a(-_XB - LAND_T), LAND_D / 2)  # the land (the port node)
    P.hole("M-GASKET", a(-_XB - LAND_T - 1.0), a(-_XB + 1.0), BORE_D / 2, land)                       # the bore through the land
    P.pivot(pneu.NODES["supply"], "port", a(-_XB - LAND_T), axis=(-1, 0, 0), range=(0, 0), unit=PORT, gender="female",
            role="supply")
    x0 = min(-bx / 2, -_XB - LAND_T)                                                                  # the base's -x end (-110)
    P.collider("env", x0, -FLANGE_D / 2, 0, _X5 + HANDLE[1] - x0, FLANGE_D, height())
    return P


PREVIEWS = [dict(name="three-quarter", az=250, el=25), dict(name="crank", az=0, el=10), dict(name="inlet", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
