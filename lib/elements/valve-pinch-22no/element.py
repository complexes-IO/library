#!/usr/bin/env python3
"""valve-pinch-22no: a pneumatic hose (pinch) valve, a 2/2 valve open at rest: an elastomer sleeve runs straight through a closed
housing from `port-in` to `port-out`; control air let into the housing through `port-10` squeezes the sleeve flat and shuts the line,
air off, the sleeve's own stiffness and the medium open it again. Nothing in the flow path but the sleeve, so it shuts on slurries,
powders and abrasive grit (a blast cabinet's feed, a process skid's line) where a seat would wear.
Generic (OPERATING.md 12, EM 2026-11-07; autopilot.md 2.b2: the next ETIM class `inventory pneu` lists after EC010102): our own
vendor-neutral design of ETIM 10.0 EC010401 "Hose valve" (synonyms "Pinch valve", "Pneumatic hose valve"); the class values it is
designed to are in spec.md "## Class values". Threaded connections, no coupling and no flange (class values 5, 6 and 9), so nothing in
its shape waits on a dimensional standard. Ports from toolkit/pneu.py (D1 threads): the process ports NPT 3/8 female with no
pneumatic role, as control-valve's liquid ports; the control port NPT 1/8 female, role pilot, numbered 10 (ISO 11727: the signal that
shuts 1 from 2, the normally open valve's pilot). Each bore as control-valve 1.0's: Ø (E1 + h) × (L2 + 2), blind in its boss (tank
2.0's rule). The sleeve inside is not modelled. Every other size is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "valve-pinch-22no", "1.1", "device"
TITLE = "pneumatic hose (pinch) valve, generic, 2/2 normally open, NPT 3/8 female process ports, NPT 1/8 control port"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hose valve (ETIM 10.0 EC010401), a pneumatic pinch valve, 2/2 normally open: control air into "
            "the housing shuts the sleeve; class values in spec.md; process ports female NPT 3/8 and the control port female NPT 1/8 "
            "(ASME B1.20.1 by its formulas, toolkit/pneu.py THREADS, D1), bored at E1 + h from pneu.NPT; the control port numbered 10 "
            "to ISO 11727; housing and bosses are design choices; no vendor file opened")
ORIGIN = ("in line: the inlet boss's face centre (`port-in`); the port axis is the x axis, flow along +x, the control port toward +z, "
          "the label face toward -y")
COMMAND = "VALVE-PINCH-22NO"
PARAMS = dict()

PORT = "NPT3/8"                       # from pneu.THREADS (D1): the process ports, as control-valve's liquid ports (class value 5)
PILOT = "NPT1/8"                      # from pneu.THREADS (D1): the control air port, the smallest of the series (a signal line)
BOSS_D, BOSS_L = 26.0, 16.0           # design choice: each process port's round boss on the housing's end faces (control-valve's)
BODY = (80.0, 56.0, 56.0)             # design choice: the housing x (along the flow), y, z; centred on the port axis in y and z
PBOSS_D, PBOSS_L = 18.0, 10.0         # design choice: the control port's boss on the housing's top, on the housing's centre in x
LABEL = (40.0, 20.0)                  # complexes.org generic field, the 2/2 symbol and the flow arrow on the label face (x by z)
FIELD_T = 0.2                         # the label field stands 0.2 proud (GEO-050)
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD and each bore
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_BOSS, FIELDM = "M-ALU-ANOD", "M-BRASS", "M-WHITE-PA"
P_CONTROL_BAR = 8.0                   # class value 12 (EF020305 Max. control pressure): ratings.csv p_max, port-10's rating only
P_MEDIUM_BAR = 4.0                    # class value 11 (EF020449 Max. operating pressure): the process ports' rating; no check reads it yet
CLOSE_MARGIN_BAR = 2.5                # design choice: control air above the medium's pressure that flattens the sleeve

_T, _P = pneu.NPT[PORT]["table"], pneu.NPT[PILOT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 17.055 for NPT 3/8: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 + 2 = 12.36: design choice, a run-out past the male's effective thread (tank 2.0)
PBORE_D = (_P["E1"] + _P["h"]) * 25.4     # 10.242 for NPT 1/8
PBORE_L = pneu.NPT[PILOT]["length"] + 2.0  # L2 + 2 = 8.702
assert PORT in pneu.THREADS and PILOT in pneu.THREADS
assert BOSS_D >= _T["D"] * 25.4 + 2 * WALL and PBOSS_D >= _P["D"] * 25.4 + 2 * WALL     # 3 mm round each port's pipe OD
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < BOSS_L                     # deeper than a male's make-up, blind in its boss
assert PBORE_L >= pneu.NPT[PILOT]["engagement"] and PBORE_L < PBOSS_L                 # blind in the control boss, above the housing's top
assert BOSS_D - BORE_D >= 2 * WALL and PBOSS_D - PBORE_D >= 2 * WALL                   # 3 mm of boss wall round each bore
assert BOSS_D < min(BODY[1], BODY[2]) and PBOSS_D < min(BODY[0], BODY[1])              # the bosses sit inside the faces they meet
assert LABEL[0] < BODY[0] and LABEL[1] < BODY[2]                                       # the label field stays on the front face
assert P_CONTROL_BAR * 100.0 >= pneu.P_SUPPLY                                          # control air (kPa): 800 above the bench drop's 689.5
assert P_MEDIUM_BAR + CLOSE_MARGIN_BAR <= pneu.P_SUPPLY / 100.0                        # bench air (6.89 bar) shuts a 4 bar line


def frame():
    """the main levels: the housing's end faces, the outlet face, the housing's centre in x and its top"""
    bx, by, bz = BODY
    xb0 = BOSS_L                          # the housing's inlet end face
    xb1 = xb0 + bx                        # its outlet end face
    xo = xb1 + BOSS_L                     # the outlet boss's face (`port-out`)
    xc = (xb0 + xb1) / 2.0                # the control port's axis
    zt = bz / 2.0                         # the housing's top
    return xb0, xb1, xo, xc, zt


def height(): return BODY[2] / 2.0 + frame()[4] + PBOSS_L        # class value 18: the housing's underside to the control boss's top: 66


def build():
    P = Prims(); bx, by, bz = BODY
    xb0, xb1, xo, xc, zt = frame()
    body = P.box(MAT_BODY, xb0, -by / 2, -bz / 2, bx, by, bz)                                               # housing (sleeve inside)
    bi = P.cyl(f"node:port-in|{MAT_BOSS}", (0, 0, 0), (xb0 + IN, 0, 0), BOSS_D / 2.0)                       # inlet boss
    bo = P.cyl(f"node:port-out|{MAT_BOSS}", (xb1 - IN, 0, 0), (xo, 0, 0), BOSS_D / 2.0)                     # outlet boss
    P.hole(MAT_BOSS, (-1.0, 0, 0), (BORE_L, 0, 0), BORE_D / 2.0, bi)                                       # bores: 1 outside each face,
    P.hole(MAT_BOSS, (xo + 1.0, 0, 0), (xo - BORE_L, 0, 0), BORE_D / 2.0, bo)                              # L2 + 2 into its boss
    ztop = zt + PBOSS_L
    bp = P.cyl(f"node:port-10|{MAT_BODY}", (xc, 0, zt - IN), (xc, 0, ztop), PBOSS_D / 2.0)                 # control port boss, top
    P.hole(MAT_BODY, (xc, 0, ztop + 1.0), (xc, 0, ztop - PBORE_L), PBORE_D / 2.0, bp)
    P.box(FIELDM, xc - LABEL[0] / 2, -by / 2 - FIELD_T, -LABEL[1] / 2, LABEL[0], FIELD_T, LABEL[1])        # complexes.org generic, 2/2
    P.pivot("port-in", "port", (0, 0, 0), axis=(-1, 0, 0), range=(0, 0), unit=PORT, gender="female")
    P.pivot("port-out", "port", (xo, 0, 0), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female")
    P.pivot("port-10", "port", (xc, 0, ztop), axis=(0, 0, 1), range=(0, 0), unit=PILOT, gender="female", role="pilot")
    P.collider("env", 0.0, -by / 2 - FIELD_T, -bz / 2, xo, by + FIELD_T, ztop + bz / 2)
    return P


PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="inlet port-in", az=200, el=10),
            dict(name="top control port", az=250, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
