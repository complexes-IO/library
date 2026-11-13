#!/usr/bin/env python3
"""hyd-cooler: a hydraulic oil cooler, water cooled, shell and tube: a horizontal steel shell on two saddle feet, a bonnet on each
end. The return oil passes through the shell, round the tubes, from `port-oil-in` to `port-oil-out` (two spot-faced blocks on the
shell's top); the cooling water passes through the tubes in two passes, in and out on the same bonnet (`port-water-in` below,
`port-water-out` above, so the tubes stay full). lib/inventory.csv row `hyd-cooler` (own_design generic, "hydraulic oil cooler";
hpu-assembly-station, test-bench-hydraulic). Generic (OPERATING.md 12, EM 2026-11-07 and 2026-11-08): the ETIM subset on file has
no class for it (EC002515 is a cabinet's air/water exchanger, hx's case; EC004896 an evaporative room cooler), so it is generic by
the standard whose rating quantities its Class values follow, ISO 4413 (as hpu-7.5kw, valve-counterbalance and hyd-filter-return); no
vendor file was opened. Water cooled, not air blast: the chiller on file (chiller 2.1) supplies the water through its NPT 3/8
ports, and the element then has no fan motor and no electrical rating of its own. The shell, bonnets, blocks and feet are design
choices. The two oil ports are plain spot faces, unit "hyd-port" (toolkit/hyd.py H1: the dash size open), their thread a figure of
SAE J1926-1 table 1 (class B, spec.md Open figures, not drawn). The two water ports are female NPT 3/8 (ASME B1.20.1; the lane's
liquid port size, as coolant-pump's and chiller's), each bored at the male stub's own diameter E1 + h, L2 + 2 deep (tank 2.0's
rule), blind in its own boss. The tubes, tube sheets and baffles inside are not modelled; nothing moves."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import hyd, library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "hyd-cooler", "1.0", "device"
TITLE = "hydraulic oil cooler, generic, water cooled, shell and tube, two water passes, oil side 16 bar, NPT 3/8 water ports"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic hydraulic oil cooler (no ETIM class; ISO 4413 values), water cooled, shell and tube, the oil "
            "in the shell and the water in the tubes in two passes; class values in spec.md (oil side 16 bar); oil port thread not "
            "on file (class B, not drawn); water ports NPT 3/8 female (ASME B1.20.1, toolkit/pneu.py THREADS), bored at E1 + h from "
            "pneu.NPT; shell, bonnets, port blocks and feet are design choices; no vendor file opened")
ORIGIN = ("the centre of the two feet's underside (the mounting plane z = 0); the shell's axis along x at z = 90, z up; the water "
          "ports on the -x bonnet's end face, the oil ports on the shell's top")
COMMAND = "HYD-COOLER"
PARAMS = dict()

P_MAX_BAR = 16.0                           # class value 1 "max. operating pressure, oil side" (ratings.csv p_max): design, >= the tank line's
SHELL_D, SHELL_L = 100.0, 400.0            # design choices: the shell, its axis along x
Z_AX = 90.0                                # design choice: the shell's axis above the mounting plane
BON_D, BON_L = 110.0, 40.0                 # design choice: each end bonnet (the -x one divided for the two water passes)
BLOCK, OIL_X = 44.0, 130.0                 # design choice: each oil port's block, 44 square, at x = -130 and +130 on the shell's top
Z_BLK = (130.0, 152.0)                     # the blocks from inside the shell's top (z 140 on the axis plane) to their top face
SPOT_D, SPOT_T = 32.0, 1.0                 # design choice: each oil port's spot face, 1 proud of its block (hyd-filter-return's)
WATER_PORT = "NPT3/8"                      # from pneu.THREADS (D1): the lane's liquid port size (coolant-pump's, chiller's)
BOSS_D, BOSS_H = 28.0, 16.0                # design choice: each water port's boss on the bonnet's end face (the bore blind in it)
WATER_Z = 25.0                             # design choice: the water ports 25 below and above the shell's axis
FOOT_L, FOOT_W, FOOT_H, FOOT_X = 30.0, 120.0, 45.0, 150.0   # design choice: two saddle feet under the shell at x = -150 and +150
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_SHELL, MAT_BON, MAT_BLOCK, MAT_SPOT, MAT_BOSS, MAT_FOOT = "M-STEEL-7035", "M-ZINC-CAST", "M-STEEL-7035", "M-SILVER", "M-GALV", "M-BLACK-PA"

X_SHELL = (-SHELL_L / 2.0, SHELL_L / 2.0)  # -200 to 200
X_BON = X_SHELL[0] - BON_L                 # -240: the water bonnet's end face
X_WATER = X_BON - BOSS_H                   # -256: the water ports' faces
Z_OIL = Z_BLK[1] + SPOT_T                  # 153: the oil ports' faces
_t = pneu.NPT[WATER_PORT]["table"]
BORE_D, BORE_DEPTH = (_t["E1"] + _t["h"]) * 25.4, pneu.NPT[WATER_PORT]["length"] + 2.0   # 17.055 x 12.358 (pneu.NPT, ASME B1.20.1 by its formulas)
assert WATER_PORT in pneu.THREADS
assert BOSS_D - BORE_D >= 2 * 5.0                                    # 5 mm of boss wall round each bore
assert BORE_DEPTH >= pneu.NPT[WATER_PORT]["engagement"]              # deeper than the make-up
assert BOSS_H - BORE_DEPTH >= 3.0                                    # each bore blind in its own boss, 3 of floor
assert 2 * WATER_Z - BOSS_D >= 20.0 and WATER_Z + BOSS_D / 2.0 <= BON_D / 2.0 - 10.0   # the bosses 22 apart, 16 in from the bonnet's edge
assert SPOT_D <= BLOCK - 2 * 6.0                                     # each spot face keeps 6 of block face round it
assert Z_AX + math.sqrt((SHELL_D / 2.0) ** 2 - (BLOCK / 2.0) ** 2) >= Z_BLK[0] + 4.0   # each block's foot is inside the shell across its width
assert OIL_X + BLOCK / 2.0 <= X_SHELL[1] - 20.0                      # the blocks 48 in from the shell's ends
assert Z_AX - math.sqrt((SHELL_D / 2.0) ** 2 - 20.0 ** 2) <= FOOT_H - IN   # each foot holds the shell over 40 of its width at least
assert FOOT_X + FOOT_L / 2.0 <= X_SHELL[1] - 20.0 and FOOT_W >= BON_D     # the feet under the shell, wider than the bonnets
assert Z_AX - BON_D / 2.0 >= 30.0                                    # the bonnets 35 above the mounting plane
assert P_MAX_BAR >= hyd.P_TANK                                       # H5: a return-line part is judged at the tank line's pressure


def build():
    P = Prims(); b = BLOCK / 2.0
    P.cyl(MAT_SHELL, (X_SHELL[0], 0, Z_AX), (X_SHELL[1], 0, Z_AX), SHELL_D / 2.0)                          # shell
    P.cyl(MAT_BON, (X_BON, 0, Z_AX), (X_SHELL[0] + IN, 0, Z_AX), BON_D / 2.0)                              # water bonnet, 0.5 into the shell
    P.cyl(MAT_BON, (X_SHELL[1] - IN, 0, Z_AX), (X_SHELL[1] + BON_L, 0, Z_AX), BON_D / 2.0)                 # return bonnet
    for x in (-FOOT_X, FOOT_X):
        P.box(MAT_FOOT, x - FOOT_L / 2.0, -FOOT_W / 2.0, 0.0, FOOT_L, FOOT_W, FOOT_H)                     # saddle feet
    for node, x in (("port-oil-in", OIL_X), ("port-oil-out", -OIL_X)):                                    # oil against the water's first pass
        P.box(MAT_BLOCK, x - b, -b, Z_BLK[0], BLOCK, BLOCK, Z_BLK[1] - Z_BLK[0])                           # port block
        P.cyl(f"node:{node}|{MAT_SPOT}", (x, 0, Z_BLK[1] - IN), (x, 0, Z_OIL), SPOT_D / 2.0)               # spot face
        P.pivot(node, "port", (x, 0, Z_OIL), axis=(0, 0, 1), range=(0, 0), unit="hyd-port", gender="female")
    for node, z in (("port-water-in", Z_AX - WATER_Z), ("port-water-out", Z_AX + WATER_Z)):               # water in below, out above
        boss = P.cyl(f"node:{node}|{MAT_BOSS}", (X_WATER, 0, z), (X_BON + IN, 0, z), BOSS_D / 2.0)         # boss, 0.5 into the bonnet
        P.hole("M-GASKET", (X_WATER - 1.0, 0, z), (X_WATER + BORE_DEPTH, 0, z), BORE_D / 2.0, boss)        # bore, blind in its boss
        P.pivot(node, "port", (X_WATER, 0, z), axis=(-1, 0, 0), range=(0, 0), unit=WATER_PORT, gender="female")
    P.collider("body", X_WATER, -FOOT_W / 2.0, 0.0, X_SHELL[1] + BON_L - X_WATER, FOOT_W, Z_OIL)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="water end", az=160, el=15), dict(name="from above", az=225, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
