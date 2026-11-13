#!/usr/bin/env python3
"""control-valve: a pneumatically operated two-way control valve for a liquid loop (a heat-exchanger loop's cooling water, a process
skid's line): a brass in-line globe body with two female NPT 3/8 ports, a bonnet, and a single-acting spring-return piston actuator
on top. Normally closed: the spring holds the plug on its seat; control air into `port-12` (female NPT 1/8 on the actuator's top,
ISO 11727 number 12: the signal that joins 1 to 2) lifts it open. The `stem`, a position indicator on the actuator's top, rises with
the plug by the stroke; it is the one moving part. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of
ETIM 10.0 EC010171 "Pneumatic controlled two-way control valve"; lib/inventory.csv row `control-valve`, own_design generic. The
class values it is designed to are in spec.md "## Class values"; every size is a design choice. Threads ASME B1.20.1
(toolkit/pneu.py THREADS, D1); each port's bore as regulator 1.0's: Ø (E1 + h) × (L2 + 2) deep, blind in its boss, role in
features.csv (HOLE-010). The liquid ports carry no pneumatic role, as coolant-pump's `port-out`. The plug, seat, piston and spring
are inside and not modelled. No vendor file was opened (the reference file in the folder is the core's, reference only)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "control-valve", "1.0", "device"
TITLE = "generic pneumatic two-way control valve, normally closed, spring return, NPT 3/8 female body ports, NPT 1/8 control port"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic pneumatic controlled two-way control valve (ETIM 10.0 EC010171), an in-line globe body with "
            "a single-acting spring-return piston actuator, normally closed (inventory own_design generic); ports female NPT "
            "(ASME B1.20.1, toolkit/pneu.py THREADS, D1), the liquid ports as coolant-pump's, the control port numbered 12 to ISO "
            "11727; body, bonnet, actuator and indicator are design choices; no vendor file opened")
ORIGIN = ("in line: the inlet boss's face centre (`port-in`); the port axis is the x axis, flow along +x, the actuator toward +z, the "
          "label face toward -y")
COMMAND = "CONTROL-VALVE"
PARAMS = dict()

PORT = "NPT3/8"                       # from pneu.THREADS (D1): the liquid ports, as coolant-pump's and chiller's (NPT 3/8 female)
PILOT = "NPT1/8"                      # from pneu.THREADS (D1): the control air port, the smallest of the series (a signal line)
BOSS_D, BOSS_L = 26.0, 16.0           # design choice: each liquid port's round boss on the body's end faces
BODY = (56.0, 40.0, 44.0)             # design choice: the globe body x (along the flow), y, z; centred on the port axis in y and z
BONNET_D, BONNET_H = 30.0, 24.0       # design choice: the bonnet between the body's top and the actuator
ACT_D, ACT_H = 80.0, 60.0             # design choice: the actuator's cylinder (piston and spring inside, not modelled)
PBOSS_D, PBOSS_L, PBOSS_DX = 18.0, 10.0, 24.0   # design choice: the control port's boss on the actuator's top, 24 off the axis (+x)
STEM_D, STEM_H = 12.0, 10.0           # design choice: the position indicator on the actuator's top, on the axis
STROKE = 10.0                         # design choice: the plug's lift, closed (0) to open, shown by the indicator
LABEL = (40.0, 14.0)                  # complexes.org generic field and flow arrow on the body's label face (x by z)
FIELD_T = 0.2                         # the label field stands 0.2 proud (GEO-050)
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_BON, MAT_ACT, MAT_STEM, FIELDM = "M-BRASS", "M-STEEL-7035", "M-ALU-ANOD", "M-YELLOW-PA", "M-WHITE-PA"

_T, _P = pneu.NPT[PORT]["table"], pneu.NPT[PILOT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 17.055 for NPT 3/8: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 + 2 = 12.36: design choice, a run-out past the male's effective thread (tank 2.0)
PBORE_D = (_P["E1"] + _P["h"]) * 25.4     # 10.242 for NPT 1/8
PBORE_L = pneu.NPT[PILOT]["length"] + 2.0  # L2 + 2 = 8.702
assert PORT in pneu.THREADS and PILOT in pneu.THREADS
assert BOSS_D >= _T["D"] * 25.4 + 2 * WALL and PBOSS_D >= _P["D"] * 25.4 + 2 * WALL     # 3 mm round each port's pipe OD
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < BOSS_L                     # deeper than a male's make-up, blind in its boss
assert PBORE_L >= pneu.NPT[PILOT]["engagement"] and PBORE_L < PBOSS_L
assert BOSS_D - BORE_D >= 2 * WALL and PBOSS_D - PBORE_D >= 2 * WALL                   # 3 mm of boss wall round each bore
assert BOSS_D < min(BODY[1], BODY[2]) and BONNET_D < min(BODY[0], BODY[1])             # the bosses and the bonnet sit inside the faces they meet
assert PBOSS_DX + PBOSS_D / 2 + 2.0 <= ACT_D / 2 and PBOSS_DX - PBOSS_D / 2 >= STEM_D / 2 + 6.0   # the control boss on the top, clear of the stem


def frame():
    """the main levels: the outlet face, the body's x span and top, the bonnet's top, the actuator's bottom and top, the axis"""
    bx, by, bz = BODY
    xb0 = BOSS_L                          # the body's inlet end face
    xb1 = xb0 + bx                        # its outlet end face
    xo = xb1 + BOSS_L                     # the outlet boss's face (`port-out`)
    xc = (xb0 + xb1) / 2.0                # the actuator's axis
    zt = bz / 2.0                         # the body's top
    zn = zt + BONNET_H                    # the bonnet's top
    za0, za1 = zn - IN, zn - IN + ACT_H   # the actuator's bottom (0.5 into the bonnet) and top
    return xb0, xb1, xo, xc, zt, zn, za0, za1


def height(): return BODY[2] / 2.0 + frame()[7] + max(STEM_H, PBOSS_L)     # class value 32: body underside to the stem's top, closed


def build():
    P = Prims(); bx, by, bz = BODY
    xb0, xb1, xo, xc, zt, zn, za0, za1 = frame()
    body = P.box(MAT_BODY, xb0, -by / 2, -bz / 2, bx, by, bz)                                               # globe body
    bi = P.cyl(f"node:port-in|{MAT_BODY}", (0, 0, 0), (xb0 + IN, 0, 0), BOSS_D / 2.0)                       # inlet boss
    bo = P.cyl(f"node:port-out|{MAT_BODY}", (xb1 - IN, 0, 0), (xo, 0, 0), BOSS_D / 2.0)                     # outlet boss
    P.hole(MAT_BODY, (-1.0, 0, 0), (BORE_L, 0, 0), BORE_D / 2.0, bi)                                       # bores: 1 outside each face,
    P.hole(MAT_BODY, (xo + 1.0, 0, 0), (xo - BORE_L, 0, 0), BORE_D / 2.0, bo)                              # L2 + 2 into its boss
    P.cyl(MAT_BON, (xc, 0, zt - IN), (xc, 0, zn), BONNET_D / 2.0)                                           # bonnet, 0.5 into the body
    P.cyl(MAT_ACT, (xc, 0, za0), (xc, 0, za1), ACT_D / 2.0)                                                 # actuator, 0.5 into the bonnet
    px = xc + PBOSS_DX
    bp = P.cyl(f"node:port-12|{MAT_ACT}", (px, 0, za1 - IN), (px, 0, za1 + PBOSS_L), PBOSS_D / 2.0)         # control port boss, top
    P.hole(MAT_ACT, (px, 0, za1 + PBOSS_L + 1.0), (px, 0, za1 + PBOSS_L - PBORE_L), PBORE_D / 2.0, bp)
    P.cyl(f"node:stem|{MAT_STEM}", (xc, 0, za1), (xc, 0, za1 + STEM_H), STEM_D / 2.0)                       # indicator, seated face to face
    P.box(FIELDM, xc - LABEL[0] / 2, -by / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])        # complexes.org generic, arrow 1 -> 2
    P.pivot("port-in", "port", (0, 0, 0), axis=(-1, 0, 0), range=(0, 0), unit=PORT, gender="female")
    P.pivot("port-out", "port", (xo, 0, 0), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female")
    P.pivot("port-12", "port", (px, 0, za1 + PBOSS_L), axis=(0, 0, 1), range=(0, 0), unit=PILOT, gender="female", role="pilot")
    P.pivot("stem", "translate", (xc, 0, za1), axis=(0, 0, 1), range=(0, STROKE), unit="mm")               # rises as the valve opens
    ztop = za1 + max(STEM_H, PBOSS_L)
    P.collider("env", min(0.0, xc - ACT_D / 2), -ACT_D / 2, -bz / 2, max(xo, xc + ACT_D / 2) - min(0.0, xc - ACT_D / 2), ACT_D, ztop + bz / 2)
    return P


PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="inlet port-in", az=200, el=10),
            dict(name="top control port", az=250, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
