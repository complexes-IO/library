#!/usr/bin/env python3
"""vacuum: a vacuum gripper for pick and place, a compact inline ejector (venturi) body with a flat round suction cup below it.
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC004675 "Vacuum suction cup", the class
lib/standards/etim/classes.csv maps inventory row `vacuum` to ("vacuum ejector and suction cup", made of fitting-pushin x2 and
silencer; cobot-bench, pneumatic-pick-and-place, pneumatic-trainer, servo-pick-and-place). No vendor file was opened or measured;
the product figures in this folder's metadata.json are not used. Supply air enters `port-1` (female NPT 1/8 on the left end face,
ISO 11727 number 1 as pneu.NODES), passes the nozzle and leaves through `port-3` (female NPT 1/8 on the right end face, number 3,
role exhaust), where the silencer goes; the cup below holds while it flows. `port-blow` (female NPT 1/8 on the top face, over the
cup) takes the blow-off air that releases the part. fitting-pushin 2.0 (tube 1/4 to NPT 1/8, its default) fits `port-1` and
`port-blow`, silencer 1.0 (NPT1/8) fits `port-3`: the assembly places them (regulator 1.0's gauge-p pattern), never redrawn.
Threads ASME B1.20.1 (toolkit/pneu.py THREADS, D1); each port's bore as tank 2.0's: Ø E1 + h (the male stub's own diameter),
L2 + 2 deep, blind, role in features.csv (HOLE-010). Body, cup and stem sizes are design choices. The nozzle, the diffuser, the
check valve and the vacuum channel to the cup are inside and not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "vacuum", "2.0", "device"
TITLE = "generic vacuum gripper: inline ejector with a flat round suction cup Ø32, NPT 1/8 female supply, blow-off and exhaust ports"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic vacuum suction cup (ETIM 10.0 EC004675) on an inline ejector body (inventory own_design generic, "
            "\"vacuum ejector and suction cup\"); ports female NPT (ASME B1.20.1, toolkit/pneu.py THREADS, D1), supply and exhaust "
            "numbered to ISO 11727 (pneu.NODES); body, stem and cup are design choices")
ORIGIN = ("the centre of the body's left end face, on port-1's axis (port-1's joint plane, its number field's outer face, is 0.2 "
          "to -x); the air flows in along +x, z up, the cup below")
COMMAND = "VACUUM"
PARAMS = dict()

PORT = "NPT1/8"                       # from pneu.THREADS (D1): fitting-pushin 2.0's default thread, silencer 1.0's NPT1/8 size
BODY = (64.0, 20.0, 28.0)             # design choice: the ejector body x (along the flow), y, z; centred on the port axis in y and z
XB = 40.0                             # design choice: the blow-off port and the cup's centre line along x (the vacuum chamber)
STEM_D, STEM_L = 12.0, 8.0            # design choice: the cup's stem below the body (it carries the vacuum channel)
CUP_D, CUP_H = 20.0, 4.5              # design choice: the cup's back under the stem
LIP_D, LIP_H = 32.0, 3.5              # design choice: the flat sealing lip, Ø32 (class value 1, EF014871 Suction disc diameter)
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD
FIELD, FIELD_T = 16.0, 0.2            # port-number field (decal), centred on each bore, 0.2 proud of its face (GEO-050)
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_CUP, MAT_FIELD = "M-ALU-ANOD", "M-GASKET", "M-WHITE-PA"   # anodised body and stem; black nitrile cup; white fields

assert PORT in pneu.THREADS
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # E1 + h: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"]                          # deeper than a male's make-up (L1 + L3)
assert min(BODY[1], BODY[2]) >= _T["D"] * 25.4 + 2 * WALL               # 3 mm round the pipe OD on each end face
assert BODY[1] >= _T["D"] * 25.4 + 2 * WALL                             # and across the top face, round port-blow
assert min(BODY[1], BODY[2]) - BORE_D >= 2 * WALL                       # 3 mm of wall round each bore
assert XB - BORE_D / 2 >= BORE_L + WALL and XB + BORE_D / 2 <= BODY[0] - BORE_L - WALL   # port-blow's bore clear of both end bores
assert STEM_D < BODY[1] and CUP_D > STEM_D and LIP_D > CUP_D            # the stem under the body, the cup wider, the lip wider still
assert BORE_D + 2.0 < FIELD < min(BODY[1], BODY[2])                     # each field rings its bore, inside the face it sits on


def frame():
    """the main levels: the body's half height, the exhaust face, the cup's lip face"""
    bx, by, bz = BODY
    z0 = -bz / 2.0                                         # body underside
    zs = z0 - STEM_L                                       # stem's lower end
    zc = zs - CUP_H + IN                                   # cup back's lower face
    zl = zc - LIP_H + IN                                   # lip face (the suction face)
    return bz / 2.0, bx, z0, zs, zc, zl


def height(): h, _, _, _, _, zl = frame(); return h - zl   # top face to the lip face


def build():
    P = Prims(); bx, by, bz = BODY
    zt, x3, z0, zs, zc, zl = frame()
    body = P.box(MAT_BODY, 0.0, -by / 2, -bz / 2, bx, by, bz)                                            # ejector body
    P.cyl(MAT_BODY, (XB, 0, z0 + IN), (XB, 0, zs), STEM_D / 2.0)                                          # cup stem, 0.5 into the body
    P.cyl(MAT_CUP, (XB, 0, zs + IN), (XB, 0, zc), CUP_D / 2.0)                                            # cup back
    P.cyl(MAT_CUP, (XB, 0, zc + IN), (XB, 0, zl), LIP_D / 2.0)                                            # sealing lip, its face at zl
    _port(P, body, pneu.NODES["supply"], (0.0, 0.0, 0.0), (-1, 0, 0), "supply")                         # port-1, inlet (ISO 11727: 1)
    _port(P, body, pneu.NODES["exhaust"][0], (x3, 0.0, 0.0), (1, 0, 0), "exhaust")                      # port-3, exhaust (ISO 11727: 3)
    _port(P, body, "port-blow", (XB, 0.0, zt), (0, 0, 1), "supply")                                     # blow-off air, over the cup
    r = LIP_D / 2.0
    P.collider("env", -FIELD_T, -r, zl, bx + 2 * FIELD_T, 2 * r, zt + FIELD_T - zl)
    return P


def _port(P, body, name, at, out, role):
    """a female NPT 1/8 port on a face of the body: the bore (1 outside the face, L2 + 2 into the body), its number field (the node,
    FIELD square, FIELD_T proud, the bore through it) and the pivot on the field's outer face (2.0, vacuum-1.0.md finding 1), its axis out toward the counterpart
    (pneu.py port frame; valve-air-shutoff and filter-air 2.0's pattern)"""
    a = tuple(at); o = tuple(out); k = [i for i in range(3) if o[i]][0]
    pt = lambda d: tuple(a[i] + o[i] * d for i in range(3))
    P.hole(MAT_BODY, pt(1.0), pt(-BORE_L), BORE_D / 2.0, body)
    lo = [a[i] - FIELD / 2.0 for i in range(3)]; size = [FIELD, FIELD, FIELD]
    lo[k] = a[k] if o[k] > 0 else a[k] - FIELD_T; size[k] = FIELD_T
    f = P.box(f"node:{name}|{MAT_FIELD}", lo[0], lo[1], lo[2], size[0], size[1], size[2])
    P.hole(MAT_BODY, pt(FIELD_T + 1.0), pt(-1.0), BORE_D / 2.0, f)
    P.pivot(name, "port", pt(FIELD_T), axis=o, range=(0, 0), unit=PORT, gender="female", role=role)   # 2.0: on the field's outer face


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="cup", az=300, el=-30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
