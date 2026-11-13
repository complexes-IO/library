#!/usr/bin/env python3
"""tank: a rectangular storage tank (reservoir) for a liquid, pressureless, vented through a filler-breather. Generic (OPERATING.md 12,
EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010413 "Storage tank"; lib/inventory.csv row `tank`, own_design
generic (its used_by: cleaner-industrial, heat-exchanger-loop, process-skid, test-bench-hydraulic). Its sizes are design choices. Its three
ports are female NPT 3/8 (ASME B1.20.1; the lane's thread series, toolkit/pneu.py THREADS and D1), each a pivot on the face of a
boss: `port-out` (the outlet / suction, low on the right end), `port-return` (on the cover) and `port-drain` (low on the left end).
2.0 (pneu-r55, review pneu-r48 finding 1) cuts each port's bore: a plain cylinder at the male stub's own diameter, E1 + h (the
major diameter at the hand-tight plane, pneu.NPT's table, as fitting-pushin 2.0 draws its stub), so a placed fitting's stub
and the bore touch and never overlap (the library draws threads plain at one diameter, as m12.py and gland-m20 do)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "tank", "2.2", "device"
TITLE = "generic storage tank, rectangular, pressureless, 23 l, three NPT 3/8 female ports, sight gauge"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic storage tank (ETIM 10.0 EC010413), a rectangular pressureless reservoir (inventory own_design "
            "generic); ports NPT 3/8 female (ASME B1.20.1, toolkit/pneu.py THREADS); body, cover, bosses, filler-breather and sight "
            "gauge are design choices")
ORIGIN = "the centre of the bottom face (the floor contact plane z = 0); length along x, width along y, z up"
COMMAND = "TANK"
PARAMS = dict()

L, W, H = 400.0, 250.0, 240.0          # design choices: the body (length x, width y, height z), 3 mm walls not modelled
WALL = 3.0                             # design choice: wall thickness, used for the volume only
COVER_L, COVER_W, COVER_T = 420.0, 270.0, 8.0   # design choice: cover plate, 10 over the body on each side
BOSS_D, BOSS_H = 28.0, 6.0             # design choice: port boss (a half coupling), Ø28, 6 proud of its face
PORT = "NPT3/8"                        # from pneu.THREADS (ASME B1.20.1), the lane's largest size on file
CAP_D, CAP_H, CAP_X = 40.0, 30.0, -120.0         # design choice: filler-breather cap on the cover
GAUGE_W, GAUGE_T, GAUGE_Z = 36.0, 6.0, (40.0, 210.0)   # design choice: sight gauge frame on the front face (y = -W/2)
WIN_W, WIN_T = 20.0, 2.0               # its clear window, 1 proud of the frame
IN = 0.5                               # every attached part runs 0.5 into what it sits on (one solid joint)
MAT_BODY, MAT_BOSS, MAT_CAP, MAT_WIN = "M-STEEL-7035", "M-GALV", "M-BLACK-PA", "M-CASE-CLEAR"
PORTS = (("port-out", (L / 2, 0.0, 40.0), (1, 0, 0)),           # outlet / suction: right end, 40 above the floor
         ("port-return", (120.0, 0.0, H + COVER_T), (0, 0, 1)),  # return: on the cover, on the outlet's half (review pneu-r48 finding 2, open)
         ("port-drain", (-L / 2, 0.0, 20.0), (-1, 0, 0)))        # drain: left end, 20 above the floor
assert PORT in pneu.THREADS and pneu.NPT[PORT]["length"]
assert BOSS_D > pneu.NPT[PORT]["table"]["D"] * 25.4 + 6.0          # the boss stands at least 3 mm round the pipe OD
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4   # from pneu.NPT (ASME B1.20.1 by its formulas): the male stub's diameter, 17.055 for NPT 3/8
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.358) + 2: design choice, a run-out past the male's effective thread
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BOSS_D - BORE_D >= 2 * 5.0   # deeper than make-up; 5 mm of boss wall round it


def volume_l():
    """gross volume in litres: the body's inner size with WALL-thick walls and bottom (the cover closes the top)"""
    return (L - 2 * WALL) * (W - 2 * WALL) * (H - WALL) / 1e6


def build():
    P = Prims()
    body = P.box(MAT_BODY, -L / 2, -W / 2, 0.0, L, W, H)                                             # body
    cover = P.box(MAT_BODY, -COVER_L / 2, -COVER_W / 2, H - IN, COVER_L, COVER_W, COVER_T + IN)      # cover plate
    P.cyl(MAT_CAP, (CAP_X, 0, H + COVER_T - IN), (CAP_X, 0, H + COVER_T + CAP_H), CAP_D / 2.0)       # filler-breather
    for node, at, ax in PORTS:                                                                      # bosses, bores and pivots
        p0 = tuple(at[i] - ax[i] * IN for i in range(3)); p1 = tuple(at[i] + ax[i] * BOSS_H for i in range(3))
        boss = P.cyl(f"node:{node}|{MAT_BOSS}", p0, p1, BOSS_D / 2.0)
        bot = tuple(p1[i] - ax[i] * BORE_L for i in range(3))                                       # the bore's bottom
        P.hole("M-GASKET", tuple(p1[i] + ax[i] * 1.0 for i in range(3)), tuple(p0[i] - ax[i] * 1.0 for i in range(3)), BORE_D / 2.0, boss)
        P.hole("M-GASKET", tuple(at[i] + ax[i] * 1.0 for i in range(3)), bot, BORE_D / 2.0, cover if ax[2] else body)
        P.pivot(node, "port", p1, axis=ax, range=(0, 0), unit=PORT, gender="female")
    y0 = -W / 2                                                                                     # sight gauge, front face
    P.box(MAT_CAP, -GAUGE_W / 2, y0 - GAUGE_T, GAUGE_Z[0], GAUGE_W, GAUGE_T + IN, GAUGE_Z[1] - GAUGE_Z[0])
    P.box(MAT_WIN, -WIN_W / 2, y0 - GAUGE_T - 1.0, GAUGE_Z[0] + 8.0, WIN_W, WIN_T, GAUGE_Z[1] - GAUGE_Z[0] - 16.0)
    P.collider("env", -COVER_L / 2, -COVER_W / 2, 0.0, COVER_L, COVER_W, H + COVER_T + CAP_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="outlet end", az=60, el=20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
