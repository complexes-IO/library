#!/usr/bin/env python3
"""drain-auto: an automatic condensate drain (float drain) for compressed air, hung below the drain point of a receiver, filter
bowl or dryer. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC004031 "Condensate separator
(compressed air)", synonym "Condensate trap (compressed air)"; lib/inventory.csv row `drain-auto`, own_design generic
(compressor-station, compressors-plant, dryers-air). Its sizes are design choices. Condensate runs in through `port-1` (female NPT
1/4 on the head's top face, ISO 11727 number 1 as pneu.NODES: the side under supply pressure) and collects in the bowl; a float
inside opens the drain valve when the bowl fills and closes it before air escapes. `port-drain` (female NPT 1/8 on the bottom
boss) discharges the condensate to a collector; it is named, not numbered, as tank's `port-drain`: ISO 11727's numbers
(pneu.NODES) name air ports, and this one carries water and oil. Threads ASME B1.20.1 (toolkit/pneu.py THREADS, D1). 2.0 cuts
each port's bore as tank 2.0 and check-valve 2.0 do (review drain-auto-1.0.md finding 1): Ø E1 + h (the male stub's own
diameter, fitting-pushin 2.0 and gauge-p), L2 + 2 deep, blind, role in features.csv (HOLE-010). The fit to the vessel the drain
hangs from (a nipple, no element on file) is an open class B figure in spec.md (finding 2). The float and valve inside are not
modelled (nothing moves outside the body)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "drain-auto", "2.0", "device"
TITLE = "generic automatic condensate drain, float type, NPT 1/4 female inlet on top, NPT 1/8 female drain below"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic condensate separator (compressed air) (ETIM 10.0 EC004031), an automatic float drain "
            "(inventory own_design generic); ports female NPT (ASME B1.20.1, toolkit/pneu.py THREADS, D1), the inlet numbered to "
            "ISO 11727 (pneu.NODES); head, bowl and drain boss are design choices")
ORIGIN = "the centre of the head's top face (port-1's joint plane, where the drain hangs from its vessel); z up, the body below z = 0"
COMMAND = "DRAIN-AUTO"
PARAMS = dict()

INLET, DRAIN = "NPT1/4", "NPT1/8"     # from pneu.THREADS (D1): the inlet as the bench's FRL ports (pneu.py D3), the drain one size down
HEAD, HEAD_H = 50.0, 30.0             # design choices: square head (x, y) and its height (z), holding the float valve
BOWL_D, BOWL_H = 46.0, 90.0           # design choices: the bowl under the head (about 0.11 l inside with 3 mm walls), inside the head's square
BOSS_D, BOSS_H = 20.0, 10.0           # design choice: the drain boss under the bowl
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD
IN = 0.5                              # each part runs 0.5 into the one above it (one solid joint)
MAT_HEAD, MAT_BOWL, MAT_BOSS = "M-ALU-ANOD", "M-ALU-ANOD", "M-BRASS"
P_MAX_BAR = 10.0                      # class value 3 (EF025498 Operating pressure, upper end): ratings.csv p_max
P_MIN_BAR = 0.5                       # class value 3, lower end: the float valve seals from 0.5 bar (design value, not checked)

assert {INLET, DRAIN} <= set(pneu.THREADS)
assert HEAD >= pneu.NPT[INLET]["table"]["D"] * 25.4 + 2 * WALL        # 3 mm round the inlet's pipe OD
assert HEAD_H >= pneu.NPT[INLET]["length"] + 2.0                       # a male's effective thread L2 fits in the head
assert HEAD_H >= pneu.NPT[INLET]["engagement"] + 2.0                   # and its make-up depth L1 + L3
assert BOSS_D >= pneu.NPT[DRAIN]["table"]["D"] * 25.4 + 2 * WALL       # 3 mm round the drain's pipe OD
assert BOSS_H >= pneu.NPT[DRAIN]["engagement"] + 2.0                   # the drain's make-up depth fits in the boss alone (finding 3)
assert BOWL_D < HEAD and BOSS_D < BOWL_D                               # each part sits inside the one above it


def bore(thread):
    """the port bore (diameter, depth): Ø E1 + h, the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas), and L2 + 2,
    a design choice: a run-out past the male's effective thread (tank 2.0, check-valve 2.0)"""
    t = pneu.NPT[thread]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[thread]["length"] + 2.0


for _t, _part_h, _part_w in ((INLET, HEAD_H, HEAD), (DRAIN, BOSS_H, BOSS_D)):
    _d, _l = bore(_t)
    assert _l >= pneu.NPT[_t]["engagement"] and _l < _part_h          # deeper than make-up, blind inside its head or boss
    assert _part_w - _d >= 2 * WALL                                     # 3 mm of metal round each bore


def height(): return HEAD_H + BOWL_H + BOSS_H


def build():
    P = Prims()
    zb = -HEAD_H; zd = -HEAD_H - BOWL_H; z0 = -height()
    head = P.box(f"node:port-1|{MAT_HEAD}", -HEAD / 2, -HEAD / 2, zb, HEAD, HEAD, HEAD_H)   # head, inlet on its top face
    P.cyl(MAT_BOWL, (0, 0, zd), (0, 0, zb + IN), BOWL_D / 2.0)                               # bowl, 0.5 into the head
    boss = P.cyl(f"node:port-drain|{MAT_BOSS}", (0, 0, z0), (0, 0, zd + IN), BOSS_D / 2.0)    # drain boss, 0.5 into the bowl
    d1, l1 = bore(INLET); d2, l2 = bore(DRAIN)
    P.hole(MAT_HEAD, (0, 0, 1.0), (0, 0, -l1), d1 / 2.0, head)                               # bores: 1 outside each face,
    P.hole(MAT_BOSS, (0, 0, z0 - 1.0), (0, 0, z0 + l2), d2 / 2.0, boss)                      # L2 + 2 into its head or boss
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, 1), range=(0, 0), unit=INLET, gender="female", role="supply")
    P.pivot("port-drain", "port", (0, 0, z0), axis=(0, 0, -1), range=(0, 0), unit=DRAIN, gender="female")
    P.collider("env", -HEAD / 2, -HEAD / 2, z0, HEAD, HEAD, height())
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
