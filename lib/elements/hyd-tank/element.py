#!/usr/bin/env python3
"""hyd-tank: a hydraulic reservoir: a rectangular steel tank on two foot rails, at atmosphere, vented through a filler-breather
on its cover. The pump draws from `port-suction` and the circuit's return oil comes back through `port-return`, two spot-faced
blocks at opposite ends of the cover, so the oil crosses the tank's length (round the baffle inside, not modelled) before it is
drawn again; `port-drain` is a female NPT 3/8 boss low on the return end, a round clean-out cover closes the suction end, and a
level gauge stands on the front. lib/inventory.csv row `hyd-tank` (own_design generic, "hydraulic reservoir"; hpu-assembly-station).
Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010413 "Storage tank" (its synonyms on file
name it: "Oil storage tank", "Pressureless storage tank"), the class tank 2.2 is built to; no vendor file was opened. Its sizes
are design choices. The two oil ports are plain spot faces, unit "hyd-port" (toolkit/hyd.py H1: the dash size open), their thread
a figure of SAE J1926-1 table 1 (class B, spec.md Open figures, not drawn). The drain is NPT 3/8 (ASME B1.20.1; the lane's liquid
port size, as tank's), bored at the male stub's own diameter E1 + h, L2 + 2 deep (tank 2.0's rule), blind in its boss. The
reservoir is pressureless: it carries no pressure rating and no ratings.csv. Nothing moves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "hyd-tank", "1.0", "device"
TITLE = "hydraulic reservoir, generic, rectangular, pressureless, 59 l, on two foot rails, suction and return ports on the cover, NPT 3/8 drain"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic storage tank (ETIM 10.0 EC010413), a rectangular pressureless hydraulic reservoir (inventory "
            "own_design generic); class values in spec.md; suction and return port thread not on file (class B, not drawn); drain "
            "NPT 3/8 female (ASME B1.20.1, toolkit/pneu.py THREADS), bored at E1 + h from pneu.NPT; body, cover, port blocks, foot "
            "rails, filler-breather, clean-out cover and level gauge are design choices; no vendor file opened")
ORIGIN = ("the centre of the two foot rails' underside (the mounting plane z = 0); length along x, width along y, z up; the "
          "suction end at +x, the return and drain end at -x")
COMMAND = "HYD-TANK"
PARAMS = dict()

L, W, H = 500.0, 350.0, 350.0              # design choices: the body (length x, width y, height z)
WALL = 3.0                                 # design choice: wall and bottom thickness, used for the volume only (the inside is not modelled)
FOOT_L, FOOT_W, FOOT_H, FOOT_X = 40.0, 330.0, 50.0, 180.0   # design choice: two foot rails across the tank at x = -180 and +180
COVER_L, COVER_W, COVER_T = 520.0, 370.0, 8.0               # design choice: the cover plate, 10 over the body on each side
BLOCK, BLOCK_H, PORT_X = 44.0, 12.0, 150.0 # design choice: each oil port's block on the cover, at x = +150 (suction) and -150 (return)
SPOT_D, SPOT_T = 32.0, 1.0                 # design choice: each oil port's spot face, 1 proud of its block (hyd-filter-return's, hyd-cooler's)
CAP_D, CAP_H, CAP_Y = 50.0, 40.0, 90.0     # design choice: the filler-breather's cap on the cover, at x = 0, y = +90
CLEAN_D, CLEAN_T = 200.0, 6.0              # design choice: the round clean-out cover on the suction end (+x), at mid height
DRAIN_PORT = "NPT3/8"                      # from pneu.THREADS (D1): the lane's liquid port size (tank's, coolant-pump's)
BOSS_D, BOSS_H = 28.0, 16.0                # design choice: the drain's boss on the return end (-x); the bore blind in it
DRAIN_UP = 20.0                            # design choice: the drain's axis 20 above the body's underside (tank's figure)
GAUGE_W, GAUGE_T, GAUGE_UP = 36.0, 6.0, (100.0, 320.0)   # design choice: the level gauge's frame on the front (y = -W/2), above the body's underside
WIN_W, WIN_T = 20.0, 2.0                   # its clear window, 1 proud of the frame
IN = 0.5                                   # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_BODY, MAT_SPOT, MAT_BOSS, MAT_TRIM, MAT_WIN = "M-STEEL-7035", "M-SILVER", "M-GALV", "M-BLACK-PA", "M-CASE-CLEAR"

Z_BODY = (FOOT_H, FOOT_H + H)              # 50 to 400: the body stands on the rails
Z_COVER = Z_BODY[1] + COVER_T              # 408: the cover's top
Z_BLOCK = Z_COVER + BLOCK_H                # 420: the port blocks' top
Z_PORT = Z_BLOCK + SPOT_T                  # 421: the oil ports' faces
Z_DRAIN = Z_BODY[0] + DRAIN_UP             # 70: the drain's axis
X_DRAIN = -L / 2.0 - BOSS_H                # -266: the drain's face
_t = pneu.NPT[DRAIN_PORT]["table"]
BORE_D, BORE_DEPTH = (_t["E1"] + _t["h"]) * 25.4, pneu.NPT[DRAIN_PORT]["length"] + 2.0   # 17.055 x 12.358 (pneu.NPT, ASME B1.20.1 by its formulas)
assert DRAIN_PORT in pneu.THREADS
assert BOSS_D - BORE_D >= 2 * 5.0                                    # 5 mm of boss wall round the bore
assert BORE_DEPTH >= pneu.NPT[DRAIN_PORT]["engagement"]              # deeper than the make-up
assert BOSS_H - BORE_DEPTH >= 3.0                                    # the bore blind in its boss, 3 of floor
assert Z_DRAIN - BOSS_D / 2.0 >= Z_BODY[0] + WALL                    # the boss wholly above the tank's floor plate
assert SPOT_D <= BLOCK - 2 * 6.0                                     # each spot face keeps 6 of block face round it
assert 2 * PORT_X - BLOCK >= 200.0                                   # suction and return 256 apart: the oil crosses the tank
assert PORT_X + BLOCK / 2.0 <= L / 2.0 - 20.0                        # the blocks over the body, 78 in from its ends
assert CAP_Y + CAP_D / 2.0 <= W / 2.0 - 20.0 and CAP_Y - CAP_D / 2.0 >= BLOCK / 2.0 + 20.0   # the cap over the body, clear of the blocks' row
assert FOOT_W < W and FOOT_X + FOOT_L / 2.0 < L / 2.0                # the rails set in from the body's sides and ends
assert CLEAN_D <= min(W, H) - 2 * 50.0                               # the clean-out cover 50 in from the end face's edges at least
assert CLEAN_T < (COVER_L - L) / 2.0                                 # and inside the cover plate's overhang
assert GAUGE_UP[1] <= H - 20.0 and GAUGE_UP[0] >= 50.0               # the gauge on the front face, 30 below the cover


def volume_l():
    """gross volume in litres: the body's inner size with WALL-thick walls and bottom (the cover closes the top)"""
    return (L - 2 * WALL) * (W - 2 * WALL) * (H - WALL) / 1e6


assert 58.9 < volume_l() < 59.0                                      # 58.97 l (class value 5, the title's 59 l)


def build():
    P = Prims(); b = BLOCK / 2.0; zc = (Z_BODY[0] + Z_BODY[1]) / 2.0; y0 = -W / 2.0
    for x in (-FOOT_X, FOOT_X):
        P.box(MAT_TRIM, x - FOOT_L / 2.0, -FOOT_W / 2.0, 0.0, FOOT_L, FOOT_W, FOOT_H + IN)                 # foot rails, 0.5 into the body
    P.box(MAT_BODY, -L / 2.0, -W / 2.0, Z_BODY[0], L, W, H)                                               # body
    P.box(MAT_BODY, -COVER_L / 2.0, -COVER_W / 2.0, Z_BODY[1] - IN, COVER_L, COVER_W, COVER_T + IN)       # cover plate
    P.cyl(MAT_TRIM, (0, CAP_Y, Z_COVER - IN), (0, CAP_Y, Z_COVER + CAP_H), CAP_D / 2.0)                   # filler-breather
    P.cyl(MAT_BODY, (L / 2.0 - IN, 0, zc), (L / 2.0 + CLEAN_T, 0, zc), CLEAN_D / 2.0)                     # clean-out cover, suction end
    for node, x in (("port-suction", PORT_X), ("port-return", -PORT_X)):
        P.box(MAT_BODY, x - b, -b, Z_COVER - IN, BLOCK, BLOCK, BLOCK_H + IN)                              # port block
        P.cyl(f"node:{node}|{MAT_SPOT}", (x, 0, Z_BLOCK - IN), (x, 0, Z_PORT), SPOT_D / 2.0)              # spot face
        P.pivot(node, "port", (x, 0, Z_PORT), axis=(0, 0, 1), range=(0, 0), unit="hyd-port", gender="female")
    boss = P.cyl(f"node:port-drain|{MAT_BOSS}", (X_DRAIN, 0, Z_DRAIN), (-L / 2.0 + IN, 0, Z_DRAIN), BOSS_D / 2.0)   # drain boss, 0.5 into the body
    P.hole("M-GASKET", (X_DRAIN - 1.0, 0, Z_DRAIN), (X_DRAIN + BORE_DEPTH, 0, Z_DRAIN), BORE_D / 2.0, boss)        # bore, blind in its boss
    P.pivot("port-drain", "port", (X_DRAIN, 0, Z_DRAIN), axis=(-1, 0, 0), range=(0, 0), unit=DRAIN_PORT, gender="female")
    g0, g1 = Z_BODY[0] + GAUGE_UP[0], Z_BODY[0] + GAUGE_UP[1]                                             # level gauge, front face
    P.box(MAT_TRIM, -GAUGE_W / 2.0, y0 - GAUGE_T, g0, GAUGE_W, GAUGE_T + IN, g1 - g0)
    P.box(MAT_WIN, -WIN_W / 2.0, y0 - GAUGE_T - 1.0, g0 + 8.0, WIN_W, WIN_T, g1 - g0 - 16.0)
    P.collider("body", X_DRAIN, -COVER_W / 2.0, 0.0, COVER_L / 2.0 - X_DRAIN, COVER_W, Z_COVER + CAP_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="suction end", az=60, el=20), dict(name="from above", az=225, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
