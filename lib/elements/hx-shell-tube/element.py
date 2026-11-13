#!/usr/bin/env python3
"""hx-shell-tube: a liquid-to-liquid heat exchanger, shell and tube: a horizontal steel shell on two saddle feet, a bonnet on each end. One
liquid passes through the shell, round the tubes, from `port-shell-in` to `port-shell-out` (two bossed ports on the shell's top);
the other passes through the tubes in two passes, in and out on the same bonnet (`port-tube-in` below, `port-tube-out` above, so
the tubes stay full). Which liquid is the hot one is the loop's choice (the exchanger works either way). lib/inventory.csv row
`hx` (own_design yes; heat-exchanger-loop, process-skid of lib/machines-from-elements.txt). Our own design (OPERATING.md 12, own
designs; core watch 2026-11-11, request pneu-11's answer item 3: EC002515 is a cabinet's air/water cooler, not the liquid-to-liquid
exchanger its systems need, and no class or standard for that is on file, so a plain own design with no ratings of its own, built
unattended; the vendor file in the folder's references/ is reference only and was not opened). What it meets takes its figures from
the thread contract on file: every port is female NPT 3/8 (ASME B1.20.1, toolkit/pneu.py THREADS and D1; the lane's liquid port
size, as coolant-pump's, chiller's and hyd-cooler 1.0's water ports), bored at the male stub's own diameter E1 + h, L2 + 2 deep
(tank 2.0's rule), each blind in its own boss. The shell, bonnets, bosses and feet are design choices (hyd-cooler 1.0's form). The
tubes, tube sheets and baffles inside are not modelled; nothing moves. No pressure, flow, capacity or temperature is claimed (no
ratings.csv): a rated version waits for a standard in sources.csv."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "hx-shell-tube", "1.0", "device"
TITLE = "liquid-to-liquid heat exchanger, shell and tube, two tube passes, four NPT 3/8 female ports"
TOOLKIT = "1.3"
BASELINE = ("our own design (inventory own_design yes; request pneu-11's answer item 3: no ETIM class, no standard on file, no ratings "
            "of its own); shell-and-tube liquid-to-liquid exchanger, one liquid in the shell, the other in the tubes in two passes; "
            "four ports female NPT 3/8 (ASME B1.20.1, toolkit/pneu.py THREADS, D1) bored at E1 + h from pneu.NPT; shell, bonnets, "
            "bosses and feet are design choices; no vendor file opened")
ORIGIN = ("the centre of the two feet's underside (the mounting plane z = 0); the shell's axis along x at z = 90, z up; the tube-side "
          "ports on the -x bonnet's end face, the shell-side ports on the shell's top")
COMMAND = "HX"
PARAMS = dict()

PORT = "NPT3/8"                            # from pneu.THREADS (D1): the lane's liquid port size (coolant-pump's, chiller's, hyd-cooler's water)
SHELL_D, SHELL_L = 100.0, 400.0            # design choices: the shell, its axis along x
Z_AX = 90.0                                # design choice: the shell's axis above the mounting plane
BON_D, BON_L = 110.0, 40.0                 # design choice: each end bonnet (the -x one divided inside for the two tube passes)
BOSS_D, BOSS_H = 28.0, 16.0                # design choice: each tube-side port's boss on the bonnet's end face (the bore blind in it)
TUBE_Z = 25.0                              # design choice: the tube-side ports 25 below and above the shell's axis
SHELL_X = 130.0                            # design choice: the shell-side ports at x = -130 and +130 on the shell's top
SHELL_BOSS_TOP = 160.0                     # design choice: the shell-side bosses' top faces (20 above the shell's crown at z 140)
FOOT_L, FOOT_W, FOOT_H, FOOT_X = 30.0, 120.0, 45.0, 150.0   # design choice: two saddle feet under the shell at x = -150 and +150
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_SHELL, MAT_BON, MAT_BOSS, MAT_FOOT = "M-STEEL-7035", "M-ZINC-CAST", "M-GALV", "M-BLACK-PA"

X_SHELL = (-SHELL_L / 2.0, SHELL_L / 2.0)  # -200 to 200
X_BON = X_SHELL[0] - BON_L                 # -240: the tube-side bonnet's end face
X_TUBE = X_BON - BOSS_H                    # -256: the tube-side ports' faces
Z_CROWN = Z_AX + SHELL_D / 2.0             # 140: the shell's crown
Z_BOSS0 = Z_AX + math.sqrt((SHELL_D / 2.0) ** 2 - (BOSS_D / 2.0) ** 2) - 2.0   # 136: each shell-side boss starts inside the shell across its width
_t = pneu.NPT[PORT]["table"]
BORE_D, BORE_DEPTH = (_t["E1"] + _t["h"]) * 25.4, pneu.NPT[PORT]["length"] + 2.0   # 17.055 x 12.358 (pneu.NPT, ASME B1.20.1 by its formulas)
assert PORT in pneu.THREADS
assert BOSS_D - BORE_D >= 2 * 5.0                                    # 5 mm of boss wall round each bore
assert BORE_DEPTH >= pneu.NPT[PORT]["engagement"]                    # deeper than the make-up
assert BOSS_H - BORE_DEPTH >= 3.0                                    # each tube-side bore blind in its own boss, 3 of floor
assert SHELL_BOSS_TOP - BORE_DEPTH >= Z_CROWN + 3.0                  # each shell-side bore's floor 3 above the shell's crown: blind in its boss
assert 2 * TUBE_Z - BOSS_D >= 20.0 and TUBE_Z + BOSS_D / 2.0 <= BON_D / 2.0 - 10.0   # the bonnet bosses 22 apart, 16 in from the bonnet's edge
assert SHELL_X + BOSS_D / 2.0 <= X_SHELL[1] - 20.0                   # the shell bosses 56 in from the shell's ends
assert Z_AX - math.sqrt((SHELL_D / 2.0) ** 2 - 20.0 ** 2) <= FOOT_H - IN   # each foot holds the shell over 40 of its width at least
assert FOOT_X + FOOT_L / 2.0 <= X_SHELL[1] - 20.0 and FOOT_W >= BON_D     # the feet under the shell, wider than the bonnets
assert Z_AX - BON_D / 2.0 >= 30.0                                    # the bonnets 35 above the mounting plane


def build():
    P = Prims()
    P.cyl(MAT_SHELL, (X_SHELL[0], 0, Z_AX), (X_SHELL[1], 0, Z_AX), SHELL_D / 2.0)                          # shell
    P.cyl(MAT_BON, (X_BON, 0, Z_AX), (X_SHELL[0] + IN, 0, Z_AX), BON_D / 2.0)                              # tube-side bonnet, 0.5 into the shell
    P.cyl(MAT_BON, (X_SHELL[1] - IN, 0, Z_AX), (X_SHELL[1] + BON_L, 0, Z_AX), BON_D / 2.0)                 # return bonnet
    for x in (-FOOT_X, FOOT_X):
        P.box(MAT_FOOT, x - FOOT_L / 2.0, -FOOT_W / 2.0, 0.0, FOOT_L, FOOT_W, FOOT_H)                     # saddle feet
    for node, x in (("port-shell-in", SHELL_X), ("port-shell-out", -SHELL_X)):                            # the shell liquid against the tube liquid's first pass
        boss = P.cyl(f"node:{node}|{MAT_BOSS}", (x, 0, Z_BOSS0), (x, 0, SHELL_BOSS_TOP), BOSS_D / 2.0)     # boss, its foot inside the shell
        P.hole("M-GASKET", (x, 0, SHELL_BOSS_TOP + 1.0), (x, 0, SHELL_BOSS_TOP - BORE_DEPTH), BORE_D / 2.0, boss)   # bore, blind in its boss
        P.pivot(node, "port", (x, 0, SHELL_BOSS_TOP), axis=(0, 0, 1), range=(0, 0), unit=PORT, gender="female")
    for node, z in (("port-tube-in", Z_AX - TUBE_Z), ("port-tube-out", Z_AX + TUBE_Z)):                   # tube liquid in below, out above
        boss = P.cyl(f"node:{node}|{MAT_BOSS}", (X_TUBE, 0, z), (X_BON + IN, 0, z), BOSS_D / 2.0)          # boss, 0.5 into the bonnet
        P.hole("M-GASKET", (X_TUBE - 1.0, 0, z), (X_TUBE + BORE_DEPTH, 0, z), BORE_D / 2.0, boss)         # bore, blind in its boss
        P.pivot(node, "port", (X_TUBE, 0, z), axis=(-1, 0, 0), range=(0, 0), unit=PORT, gender="female")
    P.collider("body", X_TUBE, -FOOT_W / 2.0, 0.0, X_SHELL[1] + BON_L - X_TUBE, FOOT_W, SHELL_BOSS_TOP)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="tube end", az=160, el=15), dict(name="from above", az=225, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
