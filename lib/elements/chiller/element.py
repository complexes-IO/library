#!/usr/bin/env python3
"""chiller: an industrial recirculating water chiller for a machine (a fibre laser's source and head, a machining centre's spindle,
a welder's torch, a CMM's room loop). A free-standing cabinet on a plinth: it cools water in its own reservoir and pumps it to the
machine by `port-supply`, and takes it back by `port-return`, both on the rear. Generic (OPERATING.md 12, EM 2026-11-07): our own
vendor-neutral design of ETIM 10.0 EC002516 "Liquid cooling unit (enclosure/cabinet)" (its synonyms in
lib/standards/etim/classes.csv include "Chiller" and "Recooling unit"); lib/inventory.csv row `chiller`, own_design generic (6
machines in lib/machines-factory.txt). Its sizes are design choices. Both ports are female NPT 3/8 (ASME B1.20.1; the lane's thread
series, toolkit/pneu.py THREADS and D1, as tank 1.0 and coolant-pump 1.0 took it for their liquid ports): each a pivot on the face of
a boss, axis +y. 2.0 cuts each port's bore as tank 2.0 and coolant-pump 2.0 do (review chiller-1.0.md finding 2): Ø E1 + h (the
male stub's own diameter, fitting-pushin 2.0's rule), L2 + 2 deep, blind inside the boss's proud part, role in features.csv
(HOLE-010). 2.0 also adds the supply port `pwr`: the cable entry boss is the node, unit 480V-3P+E, gender none (screw terminals),
pins.csv L1 / L2 / L3 and PE, coolant-pump 2.0's and hpu-7.5kw 1.0's pattern; no hole in the entry (the gland is placed, never
redrawn). The refrigerant circuit, the pump, the reservoir and the fan inside are not modelled; the supply cable is the
assembly's."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "chiller", "2.1", "device"
TITLE = "generic recirculating water chiller, 2 kW at L32W18, 460 V 3-phase 60 Hz, free-standing, supply and return NPT 3/8 female"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic liquid cooling unit (ETIM 10.0 EC002516), a free-standing recirculating water chiller for a "
            "machine (inventory own_design generic); supply and return female NPT 3/8 (ASME B1.20.1, toolkit/pneu.py THREADS, D1); "
            "cabinet, plinth, fan guard, fill cap, control panel, level gauge, grille and bosses are design choices")
ORIGIN = ("the centre of the plinth's underside (the floor contact plane, z = 0); width along x, depth along y, z up; the front "
          "(control panel, level gauge, air intake) toward -y, the rear (ports, cable entry) toward +y")
COMMAND = "CHILLER"
PARAMS = dict()

W, D, H0, H1 = 500.0, 600.0, 60.0, 960.0   # design choices: the cabinet, width x, depth y, from z 60 (plinth top) to 960 (its top)
PLINTH_IN = 10.0                            # the plinth stands 10 in from the cabinet on each side (a toe recess)
FAN_D, FAN_Y, FAN_H = 360.0, 60.0, 15.0     # design choice: condenser fan guard on the top (air out upward), Ø360, 15 proud
CAP_D, CAP_H, CAP_XY = 50.0, 30.0, (150.0, -220.0)   # design choice: reservoir fill cap on the top, front right
PANEL = (-80.0, 80.0, 780.0, 880.0, 8.0)    # design choice: control panel on the front (x0, x1, z0, z1, proud)
DISP = (-60.0, 60.0, 800.0, 860.0, 2.0)     # its temperature display window, 2 proud of the panel
GAUGE_X, GAUGE_W, GAUGE_T, GAUGE_Z = 188.0, 36.0, 6.0, (450.0, 700.0)   # design choice: reservoir level gauge frame on the front
WIN_W, WIN_T = 20.0, 2.0                    # its clear window, 1 proud of the frame
GRILLE = (-220.0, 120.0, 150.0, 550.0, 3.0) # design choice: condenser air intake grille on the front (x0, x1, z0, z1, proud)
PORT = "NPT3/8"                             # from pneu.THREADS (ASME B1.20.1), the lane's largest size on file
BOSS_D, BOSS_H = 28.0, 14.0                 # design choice: port boss (a half coupling), Ø28, 14 proud of the rear
ENTRY_D, ENTRY_L, ENTRY_XZ = 24.0, 12.0, (180.0, 820.0)   # design choice: cable entry boss on the rear (`pwr`; no thread cut, Notes)
PWR_UNIT = "480V-3P+E"                      # the library's 480 V three-phase + PE power unit (coolant-pump 2.0, hpu-7.5kw 1.0)
IN = 0.5                                    # every attached part runs 0.5 into what it sits on (one solid joint)
MAT_BODY, MAT_DARK, MAT_BOSS, MAT_DISP, MAT_WIN = "M-STEEL-7035", "M-BLACK-PA", "M-GALV", "M-LENS-DARK", "M-CASE-CLEAR"
PORTS = (("port-supply", (-120.0, D / 2, 250.0)),   # chilled water out to the machine: rear, left seen from the rear's outside
         ("port-return", (120.0, D / 2, 250.0)))    # warm water back from the machine
assert PORT in pneu.THREADS and pneu.NPT[PORT]["length"]
assert BOSS_D > pneu.NPT[PORT]["table"]["D"] * 25.4 + 6.0          # the boss stands at least 3 mm round the pipe OD
assert BOSS_H >= pneu.NPT[PORT]["engagement"] + 2.0                 # a male makes up (L1 + L3) inside the boss's proud part
assert abs(PORTS[0][1][0] - PORTS[1][1][0]) >= BOSS_D + 60.0        # room for a wrench between the two fittings
assert (CAP_XY[0] ** 2 + (CAP_XY[1] - FAN_Y) ** 2) ** 0.5 > (FAN_D + CAP_D) / 2.0 + 20.0   # the fill cap stands clear of the fan guard
assert GRILLE[1] < GAUGE_X - GAUGE_W / 2.0 - 20.0 and GRILLE[3] < PANEL[2]                 # the front parts don't touch


def bore():
    """each port's bore (diameter, depth): Ø E1 + h, the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas), and L2 + 2,
    a design choice: a run-out past the male's effective thread (tank 2.0, coolant-pump 2.0)"""
    t = pneu.NPT[PORT]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[PORT]["length"] + 2.0


_D, _L = bore()
assert _L >= pneu.NPT[PORT]["engagement"] and _L < BOSS_H                     # deeper than make-up, blind inside the boss's proud part
assert BOSS_D - _D >= 2 * 3.0                                                  # 3 mm of metal round each bore


def build():
    P = Prims(); w, d = W / 2.0, D / 2.0
    P.box(MAT_DARK, -w + PLINTH_IN, -d + PLINTH_IN, 0.0, W - 2 * PLINTH_IN, D - 2 * PLINTH_IN, H0 + IN)   # plinth
    P.box(MAT_BODY, -w, -d, H0, W, D, H1 - H0)                                                        # cabinet
    P.cyl(MAT_DARK, (0, FAN_Y, H1 - IN), (0, FAN_Y, H1 + FAN_H), FAN_D / 2.0)                         # fan guard
    P.cyl(MAT_DARK, (CAP_XY[0], CAP_XY[1], H1 - IN), (CAP_XY[0], CAP_XY[1], H1 + CAP_H), CAP_D / 2.0) # fill cap
    x0, x1, z0, z1, t = PANEL
    P.box(MAT_DARK, x0, -d - t, z0, x1 - x0, t + IN, z1 - z0)                                          # control panel
    a0, a1, b0, b1, s = DISP
    P.box(MAT_DISP, a0, -d - t - s, b0, a1 - a0, s + IN, b1 - b0)                                      # display window
    g0 = GAUGE_X - GAUGE_W / 2.0
    P.box(MAT_DARK, g0, -d - GAUGE_T, GAUGE_Z[0], GAUGE_W, GAUGE_T + IN, GAUGE_Z[1] - GAUGE_Z[0])      # level gauge frame
    P.box(MAT_WIN, GAUGE_X - WIN_W / 2.0, -d - GAUGE_T - 1.0, GAUGE_Z[0] + 8.0, WIN_W, WIN_T, GAUGE_Z[1] - GAUGE_Z[0] - 16.0)
    x0, x1, z0, z1, t = GRILLE
    P.box(MAT_DARK, x0, -d - t, z0, x1 - x0, t + IN, z1 - z0)                                          # air intake grille
    bd, bl = bore()
    for node, at in PORTS:                                                                            # bosses, bores and pivots
        boss = P.cyl(f"node:{node}|{MAT_BOSS}", (at[0], d - IN, at[2]), (at[0], d + BOSS_H, at[2]), BOSS_D / 2.0)
        yf = d + BOSS_H
        P.hole(MAT_BOSS, (at[0], yf + 1.0, at[2]), (at[0], yf - bl, at[2]), bd / 2.0, boss)          # its bore, L2 + 2 deep
        P.pivot(node, "port", (at[0], yf, at[2]), axis=(0, 1, 0), range=(0, 0), unit=PORT, gender="female")
    P.cyl(f"node:pwr|{MAT_DARK}", (ENTRY_XZ[0], d - IN, ENTRY_XZ[1]), (ENTRY_XZ[0], d + ENTRY_L, ENTRY_XZ[1]), ENTRY_D / 2.0)   # cable entry
    P.pivot("pwr", "port", (ENTRY_XZ[0], d + ENTRY_L, ENTRY_XZ[1]), axis=(0, 1, 0), range=(0, 0), unit=PWR_UNIT, gender="none")
    y0 = -d - PANEL[4] - DISP[4]
    P.collider("env", -w, y0, 0.0, W, d + BOSS_H - y0, H1 + CAP_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=20), dict(name="rear ports", az=45, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
