#!/usr/bin/env python3
"""separator-oil-water: a static oil-water separator for compressor condensate. The condensate the drains blow out (drain-auto,
the receiver's and the dryer's drains) comes in through two inlets on top of a steel expansion chamber, where its pressure is let
off to atmosphere; it settles in the vented plastic tank below, where free oil rises and runs over into the oil container hung on
the tank's front, and the water passes the adsorption filters (two cartridges, their screw caps on the lid) to the clean-water
outlet low on the right end, which goes to the sewer. lib/inventory.csv row `separator-oil-water` (own_design generic, "oil-water
separator (condensate)"; 2 systems: compressor-station, compressors-plant). Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC012068 "Oil-/water separator static" (group EG015140 Filters/separators, tier 2), the class
lib/standards/etim/classes.csv gives for it; the row names no class. Its five features are not in class-features.csv (tier 2, on no
inventory row: request pneu-4's case, lib/requests/core/pneu-4-answer.md), so spec.md's Class values gives the design values under
plain names, as tube-pneu 1.0 and pump-hand-hyd 1.0. No vendor file was opened. Its ports are female NPT (ASME B1.20.1; the lane's
thread series, toolkit/pneu.py THREADS and D1), each bored at the male stub's own diameter E1 + h, L2 + 2 deep (tank 2.0's rule):
`port-in-1`, `port-in-2` NPT 1/4 on the chamber's top, `port-out` NPT 3/8 on the right end (the liquid ports' size, as tank's).
The max. inlet pressure is not on file (class A, spec.md Open figures): no ratings.csv. The filters, the oil and the water inside are
not modelled; nothing moves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "separator-oil-water", "1.1", "device"
TITLE = "oil-water separator for compressor condensate, generic, static (gravity and adsorption), vented tank, two NPT 1/4 inlets, NPT 3/8 water outlet"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic oil-/water separator static (ETIM 10.0 EC012068), for compressor condensate (inventory own_design "
            "generic); design values in spec.md; ports NPT 1/4 and 3/8 female (ASME B1.20.1, toolkit/pneu.py THREADS), bored at E1 + h "
            "from pneu.NPT; max. inlet pressure not on file (class A, spec.md Open figures); tank, lid, expansion chamber, filter caps "
            "and oil container are design choices; no vendor file opened")
ORIGIN = ("the centre of the tank's bottom face (the floor contact plane z = 0); length along x, width along y, z up; the inlets on "
          "the expansion chamber's top (-x half), the water outlet on the right end (+x), the oil container on the front (-y)")
COMMAND = "SEPARATOR-OIL-WATER"
PARAMS = dict()

L, W, H = 500.0, 300.0, 520.0                  # design choices: the settling tank (length x, width y, height z); walls not modelled
WALL = 5.0                                     # design choice: wall thickness, used for the volume only
LID_L, LID_W, LID_T = 520.0, 320.0, 10.0       # design choice: the lid, 10 over the tank on each side
CH_D, CH_X, CH_TOP = 120.0, -150.0, 700.0      # design choice: the expansion chamber, Ø120 on the lid at x = -150, its top at z = 700
CAP_D, CAP_H, CAP_X = 100.0, 20.0, (20.0, 160.0)   # design choice: the two adsorption cartridges' screw caps on the lid
IN_PORT, OUT_PORT = "NPT1/4", "NPT3/8"         # from pneu.THREADS (D1): a drain's hose fitting in, the liquid size out (tank's)
IN_Y = 30.0                                    # design choice: the inlets at y = -30 and +30 on the chamber's top
OUT_Z = 80.0                                   # design choice: the clean-water outlet's axis, 80 above the floor on the right end
BOSS_IN_D, BOSS_OUT_D = 24.0, 28.0            # design choice: port bosses (half couplings)
BOSS_IN_H, BOSS_OUT_H = 16.0, 6.0              # design choice: the inlets' bosses 16 proud (each bore blind in its boss), the outlet's 6
OIL = (60.0, 220.0, 80.0, 260.0, 480.0)        # design choice: the oil container on the front face, x 60 to 220, 80 deep, z 260 to 480
LABEL = (-200.0, -40.0, 300.0, 420.0)          # design choice: the "complexes.org generic" field on the front face (x, x, z, z)
FIELD_T = 0.2                                  # the label field 0.2 proud of the front face (GEO-050)
IN = 0.5                                       # every attached part runs 0.5 into what it sits on (one solid joint)
MAT_TANK, MAT_CH, MAT_BOSS, MAT_CAP, MAT_OIL, MAT_FIELD = "M-GREY-PVC", "M-STEEL-7035", "M-GALV", "M-BLACK-PA", "M-WHITE-PVC", "M-WHITE-PA"


def _bore(port):
    t = pneu.NPT[port]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[port]["length"] + 2.0   # E1 + h (the male stub's diameter), L2 + 2 deep


IN_BORE, IN_DEPTH = _bore(IN_PORT)             # 13.616 x 12.205 (pneu.NPT, ASME B1.20.1 by its formulas)
OUT_BORE, OUT_DEPTH = _bore(OUT_PORT)          # 17.055 x 12.358
PORTS = (("port-in-1", IN_PORT, BOSS_IN_D, BOSS_IN_H, (CH_X, -IN_Y, CH_TOP), (0, 0, 1)),     # condensate inlets on the chamber's top
         ("port-in-2", IN_PORT, BOSS_IN_D, BOSS_IN_H, (CH_X, IN_Y, CH_TOP), (0, 0, 1)),
         ("port-out", OUT_PORT, BOSS_OUT_D, BOSS_OUT_H, (L / 2, 0.0, OUT_Z), (1, 0, 0)))      # clean water out, low on the right end
assert IN_PORT in pneu.THREADS and OUT_PORT in pneu.THREADS
assert BOSS_IN_D - IN_BORE >= 2 * 5.0 and BOSS_OUT_D - OUT_BORE >= 2 * 5.0           # 5 mm of boss wall round each bore
assert IN_DEPTH >= pneu.NPT[IN_PORT]["engagement"] and OUT_DEPTH >= pneu.NPT[OUT_PORT]["engagement"]   # deeper than make-up
assert BOSS_IN_H - IN_DEPTH >= 3.0 and OUT_DEPTH > BOSS_OUT_H + IN     # each inlet bore blind in its boss (3 of floor); the outlet's runs into the tank
assert 2 * IN_Y - BOSS_IN_D >= 30.0 and IN_Y + BOSS_IN_D / 2 <= CH_D / 2 - 10.0      # the inlets 36 apart, 18 in from the chamber's edge (at least 10)
assert CH_X - CH_D / 2 > -LID_L / 2 + 20.0 and CAP_X[0] - CAP_D / 2 - (CH_X + CH_D / 2) >= 50.0   # chamber on the lid, 60 to the cap
assert CAP_X[1] - CAP_X[0] - CAP_D >= 30.0 and CAP_X[1] + CAP_D / 2 < LID_L / 2 - 20.0
assert OIL[4] < H and OIL[1] < L / 2 and OIL[0] > LABEL[1]                         # the oil container clear of the lid, the end and the label
assert OUT_Z - BOSS_OUT_D / 2 >= 50.0                                            # the outlet's boss 66 above the floor: room for a fitting


def volume_l():
    """gross volume of the settling tank in litres: its inner size with WALL-thick walls and bottom (the lid closes the top)"""
    return (L - 2 * WALL) * (W - 2 * WALL) * (H - WALL) / 1e6


def build():
    P = Prims()
    tank = P.box(MAT_TANK, -L / 2, -W / 2, 0.0, L, W, H)                                              # settling tank
    P.box(MAT_TANK, -LID_L / 2, -LID_W / 2, H - IN, LID_L, LID_W, LID_T + IN)                          # lid
    z_lid = H + LID_T
    P.cyl(MAT_CH, (CH_X, 0, z_lid - IN), (CH_X, 0, CH_TOP), CH_D / 2)                        # expansion chamber
    for x in CAP_X:                                                                                  # filter cartridges' caps
        P.cyl(MAT_CAP, (x, 0, z_lid - IN), (x, 0, z_lid + CAP_H), CAP_D / 2)
    x0, x1, d, z0, z1 = OIL
    P.box(MAT_OIL, x0, -W / 2 - d, z0, x1 - x0, d + IN, z1 - z0)                                      # oil container, front face
    lx0, lx1, lz0, lz1 = LABEL
    P.box(MAT_FIELD, lx0, -W / 2 - FIELD_T, lz0, lx1 - lx0, FIELD_T, lz1 - lz0)                        # label field
    for node, unit, boss_d, boss_h, at, ax in PORTS:                                                 # bosses, bores and pivots
        bore_d, depth = _bore(unit)
        p0 = tuple(at[i] - ax[i] * IN for i in range(3)); p1 = tuple(at[i] + ax[i] * boss_h for i in range(3))
        boss = P.cyl(f"node:{node}|{MAT_BOSS}", p0, p1, boss_d / 2.0)
        bot = tuple(p1[i] - ax[i] * depth for i in range(3))                                           # the bore's bottom
        if depth < boss_h:                                                                           # inlet: blind in its boss
            P.hole("M-GASKET", tuple(p1[i] + ax[i] * 1.0 for i in range(3)), bot, bore_d / 2.0, boss)
        else:                                                                                        # outlet: through the boss into the tank
            P.hole("M-GASKET", tuple(p1[i] + ax[i] * 1.0 for i in range(3)), tuple(p0[i] - ax[i] * 1.0 for i in range(3)), bore_d / 2.0, boss)
            P.hole("M-GASKET", tuple(at[i] + ax[i] * 1.0 for i in range(3)), bot, bore_d / 2.0, tank)
        P.pivot(node, "port", p1, axis=ax, range=(0, 0), unit=unit, gender="female")
    P.collider("env", -LID_L / 2, -W / 2 - OIL[2], 0.0, LID_L, W / 2 + OIL[2] + LID_W / 2, CH_TOP + BOSS_IN_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="inlets", az=200, el=60), dict(name="outlet end", az=60, el=20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
