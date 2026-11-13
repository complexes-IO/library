#!/usr/bin/env python3
"""frl: the bench's air service unit: a 3/2 shut-off and dump valve and a filter-regulator in one line. Generic (OPERATING.md 12,
EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC010122 "Pressure reducing valve" (request pneu-6, core watch
2026-11-09: the class the PNE checks read of an air service unit; the filter half's figures are notes from EC004033 "Compressed
air filter", not a second class); lib/inventory.csv row `frl`, own_design generic (14 systems). Its sizes are design choices, our
own (no vendor file opened or measured). Air enters `port-1` (female NPT 1/4 on the shut-off valve's left face, ISO 11727 number 1
as pneu.NODES), passes the shut-off valve (its `handle` on top: a quarter turn opens the line; closed, the line downstream vents
through `port-3`, female NPT 1/4 on the valve's underside, number 3, exhaust) and the filter-regulator (the bowl below, the
adjusting `knob` on top), and leaves through `port-2` (female NPT 1/4 on the right face, number 2). `port-g` (female NPT 1/4 on
the regulator's front face, role gauge, next.md decision 1) takes gauge-p in a later version, once gauge-p is past station 6
(OPERATING.md 12: a host places only common parts past station 6). Threads ASME B1.20.1 (toolkit/pneu.py THREADS, D1); each port's
bore as regulator 1.0's: Ø E1 + h, L2 + 2 deep, blind in its boss, role in features.csv (HOLE-010). The valve spool, the filter
element, the diaphragm, spring and seat, the bowl's drain mechanism and the knob's lock are not modelled. frl 2.0 (review frl-1.0.md
finding 2) models the padlock hasp: a tab on the handle's +y end and a fixed shelf on the valve block's rear face, each with a Ø8
padlock hole, coaxial only with the handle closed (0), so a padlock through both holds the valve shut and vented; ratings.csv
`lockable` yes is derived from that geometry (PNE-008 reads it), not claimed. No safety claim (spec.md)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "frl", "2.0", "device"
TITLE = "generic air service unit, 3/2 shut-off and dump valve and filter-regulator, NPT 1/4 female ports"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic pressure reducing valve, air service unit (ETIM 10.0 EC010122), a 3/2 shut-off and dump "
            "valve and a filter-regulator in one line (inventory own_design generic; request pneu-6); ports female NPT (ASME B1.20.1, "
            "toolkit/pneu.py THREADS, D1), numbered to ISO 11727 (pneu.NODES); valve block, coupling, body, bowl, bonnet, handle and "
            "knob are design choices")
ORIGIN = ("the centre of port-1's joint plane on the inlet boss's left face (where the supply fitting meets it); the air flows "
          "in along +x, z up, the gauge port toward -y")
COMMAND = "FRL"
PARAMS = dict()

PORT = "NPT1/4"                       # from pneu.THREADS (D1): every port, the bench's FRL and gauge size (pneu.py D3)
BOSS_D, BOSS_L = 20.0, 14.0           # design choices: each port's round boss, its diameter and length along the port's axis
VALVE = (40.0, 40.0, 40.0)            # design choice: the shut-off and dump valve block x, y, z, right of the inlet boss
COUPLE = (10.0, 30.0, 30.0)           # design choice: the coupling block joining the valve to the filter-regulator (x, y, z)
BODY = (40.0, 40.0, 40.0)             # design choice: the filter-regulator body x, y, z
BONNET_D, BONNET_L = 36.0, 30.0       # design choice: the spring bonnet on the body's top face
KNOB_D, KNOB_H = 30.0, 16.0           # design choice: the adjusting knob on the bonnet
BOWL_D, BOWL_L = 36.0, 90.0           # design choice: the filter bowl under the body, clear
DRAIN_D, DRAIN_L = 10.0, 8.0          # design choice: the bowl's manual drain at its foot (fixed; its mechanism not modelled)
HANDLE = (10.0, 40.0, 8.0)            # design choice: the shut-off handle, a lever seated on the valve block's top (x, y, z); at
                                      # rest (0, closed) its long side lies across the line (y), at 90 (open) along it: the trade's
                                      # reading, as valve-air-shutoff's lever (review frl-1.0.md finding 1, frl 1.1)
HASP = (14.0, 36.0, 20.0, 8.0)        # design choices (frl 2.0): the handle's hasp tab, 14 wide (x), from the handle's +y end to
                                      # y = 36, z 20 to 28: the lever's own height, seated on the valve block's top plane as the lever
                                      # (a 4 thick tab's corner edges took no fillet at the AutoCAD gate, first run of 2.0)
SHELF = (21.5, 12.0, 6.0)             # design choices: the fixed shelf under the tab, y 21.5 to 36 (as the tab), z 12 to 18, 2 under it
SUPPORT = (12.0, 3.5, 16.0)           # design choices: the shelf's support plate on the valve block's rear face, 12 wide, 3.5 out
                                      # (y 19.5 to 23, 0.5 into the block), z 0 to 16, into the shelf
LOCK_D, LOCK_Y = 8.0, 29.0            # design choices: the padlock hole, Ø8 (a shackle up to Ø7), vertical at y = 29 through tab and shelf
WALL = 3.0                            # design choice: at least 3 mm of metal round each port's pipe OD
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
TURNS = 5                             # design choice: the knob's travel from the spring unloaded to the top of the range
QUARTER = 90.0                        # the handle's travel: a quarter turn, closed (dumped) to open
MAT_BODY, MAT_KNOB, MAT_HANDLE, MAT_BOWL = "M-ALU-ANOD", "M-BLACK-PA", "M-RED-PA", "M-CASE-CLEAR"
P_MAX_BAR = 10.0                      # class value 20 (EF020100 Max. inlet pressure): ratings.csv p_max
P_OUT_BAR = (0.5, 7.0)                # class value 21 (EF024003 Reduced pressure): the outlet's setting range

assert PORT in pneu.THREADS
assert BOSS_D >= pneu.NPT[PORT]["table"]["D"] * 25.4 + 2 * WALL      # 3 mm round each port's pipe OD
assert BOSS_L >= pneu.NPT[PORT]["length"] + 2.0                       # a male's effective thread L2 fits in each boss
assert BOSS_L >= pneu.NPT[PORT]["engagement"] + 2.0                   # and its make-up depth L1 + L3
assert BOSS_D < min(VALVE[1], VALVE[2], VALVE[0]) and BOSS_D < min(BODY[0], BODY[1], BODY[2])   # each boss inside its face
assert COUPLE[1] < min(VALVE[1], BODY[1]) and COUPLE[2] < min(VALVE[2], BODY[2])               # the coupling inside both faces
assert BONNET_D < min(BODY[0], BODY[1]) and KNOB_D < BONNET_D and BOWL_D < min(BODY[0], BODY[1])
assert HANDLE[0] <= VALVE[0] and HANDLE[1] <= VALVE[1]                # the handle at rest lies on the valve block's top
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY and P_OUT_BAR[1] * 100.0 >= pneu.P_WORK_MAX   # PNE-003 (kPa); the range spans P_WORK_MAX
_T = pneu.NPT[PORT]["table"]
BORE_D = (_T["E1"] + _T["h"]) * 25.4      # 13.616 for NPT 1/4: the male stub's diameter (pneu.NPT, ASME B1.20.1 by its formulas)
BORE_L = pneu.NPT[PORT]["length"] + 2.0   # L2 (10.205) + 2: design choice, a run-out past the male's effective thread (tank 2.0)
assert BORE_L >= pneu.NPT[PORT]["engagement"] and BORE_L < BOSS_L     # deeper than make-up, blind inside its boss
assert BOSS_D - BORE_D >= 2 * WALL                                    # 3 mm of boss wall round each bore


def frame():
    """the main levels along x: valve block, coupling, body, the outlet face; the valve's and the body's centre lines"""
    v0 = BOSS_L; v1 = v0 + VALVE[0]; vc = (v0 + v1) / 2.0
    b0 = v1 + COUPLE[0]; b1 = b0 + BODY[0]; bc = (b0 + b1) / 2.0
    x2 = b1 + BOSS_L
    return v0, v1, vc, b0, b1, bc, x2


_v0, _v1, _vc, _b0, _b1, _bc, _x2 = frame()
_SWEEP = (HANDLE[0] ** 2 + HANDLE[1] ** 2) ** 0.5 / 2.0                 # the handle's sweep radius about its own axis
assert _bc - _vc - BONNET_D / 2.0 > _SWEEP + 5.0                        # the handle clears the bonnet and knob through its travel
assert SHELF[0] > _SWEEP + 0.5 and VALVE[1] / 2.0 - IN + SUPPORT[1] > SHELF[0]   # the shelf outside the handle's sweep; support under it
assert HASP[2] >= SHELF[1] + SHELF[2] + 2.0 and HASP[2] == VALVE[2] / 2.0 and HASP[3] == HANDLE[2]   # tab 2 over the shelf, the lever's height
assert HASP[2] > BOSS_D / 2.0                                           # opening, the tab swings to -x over the inlet boss, clear of it
assert SUPPORT[0] < HASP[0] < VALVE[0] and SUPPORT[2] > SHELF[1] and SUPPORT[2] < SHELF[1] + SHELF[2]   # support into the shelf, sides apart
assert LOCK_Y - LOCK_D / 2.0 - SHELF[0] >= 3.0 and HASP[1] - LOCK_Y - LOCK_D / 2.0 >= 3.0 and HASP[0] - LOCK_D >= 2 * 3.0   # 3 of wall round the hole
assert LOCK_Y - LOCK_D / 2.0 > VALVE[1] / 2.0 - IN + SUPPORT[1]        # the hole clear of the support plate


def build():
    P = Prims(); vx, vy, vz = VALVE; bx, by, bz = BODY; cx, cy, cz = COUPLE
    v0, v1, vc, b0, b1, bc, x2 = frame()
    zk = bz / 2.0 + BONNET_L                                                                                 # bonnet top = knob seat
    yg = -by / 2.0 - BOSS_L                                                                                  # gauge face
    z3 = -vz / 2.0 - BOSS_L                                                                                  # exhaust face
    zb = -bz / 2.0 - BOWL_L                                                                                  # bowl foot
    b1n = P.cyl(f"node:port-1|{MAT_BODY}", (0, 0, 0), (v0 + IN, 0, 0), BOSS_D / 2.0)                        # inlet boss
    P.box(MAT_BODY, v0, -vy / 2, -vz / 2, vx, vy, vz)                                                        # shut-off valve block
    b3n = P.cyl(f"node:port-3|{MAT_BODY}", (vc, 0, -vz / 2 + IN), (vc, 0, z3), BOSS_D / 2.0)               # exhaust boss, underside
    P.box(MAT_BODY, v1 - IN, -cy / 2, -cz / 2, cx + 2 * IN, cy, cz)                                          # coupling block
    P.box(MAT_BODY, b0, -by / 2, -bz / 2, bx, by, bz)                                                        # filter-regulator body
    b2n = P.cyl(f"node:port-2|{MAT_BODY}", (b1 - IN, 0, 0), (x2, 0, 0), BOSS_D / 2.0)                       # outlet boss
    bgn = P.cyl(f"node:port-g|{MAT_BODY}", (bc, -by / 2 + IN, 0), (bc, yg, 0), BOSS_D / 2.0)                # gauge boss, front face
    P.cyl(MAT_BODY, (bc, 0, bz / 2 - IN), (bc, 0, zk), BONNET_D / 2.0)                                     # spring bonnet, top
    P.cyl(MAT_BOWL, (bc, 0, -bz / 2 + IN), (bc, 0, zb), BOWL_D / 2.0)                                      # filter bowl, below
    P.cyl(MAT_KNOB, (bc, 0, zb + IN), (bc, 0, zb - DRAIN_L), DRAIN_D / 2.0)                                # manual drain at its foot
    P.cyl(f"node:knob|{MAT_KNOB}", (bc, 0, zk), (bc, 0, zk + KNOB_H), KNOB_D / 2.0)                        # adjusting knob, seated
    hx, hy, hz = HANDLE
    P.box(f"node:handle|{MAT_HANDLE}", vc - hx / 2, -hy / 2, vz / 2, hx, hy, hz)                             # shut-off handle, seated
    tw, ty1, tz0, tt = HASP; sy0, sz0, st = SHELF; sw, sd, sh = SUPPORT
    tab = P.box(f"node:handle|{MAT_HANDLE}", vc - tw / 2, hy / 2, tz0, tw, ty1 - hy / 2, tt)                 # hasp tab, on the handle's +y end
    P.hole(MAT_HANDLE, (vc, LOCK_Y, tz0 - 1.0), (vc, LOCK_Y, tz0 + tt + 1.0), LOCK_D / 2.0, tab)             # its padlock hole
    P.box(MAT_BODY, vc - sw / 2, vy / 2 - IN, 0.0, sw, sd, sh)                                               # shelf support, rear face
    shelf = P.box(MAT_BODY, vc - tw / 2, sy0, sz0, tw, ty1 - sy0, st)                                        # fixed shelf under the tab
    P.hole(MAT_BODY, (vc, LOCK_Y, sz0 - 1.0), (vc, LOCK_Y, sz0 + st + 1.0), LOCK_D / 2.0, shelf)             # padlock hole, coaxial at 0
    P.hole(MAT_BODY, (-1.0, 0, 0), (BORE_L, 0, 0), BORE_D / 2.0, b1n)                                     # bores: 1 outside each face,
    P.hole(MAT_BODY, (x2 + 1.0, 0, 0), (x2 - BORE_L, 0, 0), BORE_D / 2.0, b2n)                            # L2 + 2 into its boss
    P.hole(MAT_BODY, (bc, yg - 1.0, 0), (bc, yg + BORE_L, 0), BORE_D / 2.0, bgn)
    P.hole(MAT_BODY, (vc, 0, z3 - 1.0), (vc, 0, z3 + BORE_L), BORE_D / 2.0, b3n)
    P.pivot("port-1", "port", (0, 0, 0), axis=(-1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="supply")
    P.pivot("port-2", "port", (x2, 0, 0), axis=(1, 0, 0), range=(0, 0), unit=PORT, gender="female", role="work")
    P.pivot("port-g", "port", (bc, yg, 0), axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role="gauge")
    P.pivot("port-3", "port", (vc, 0, z3), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="female", role="exhaust")
    P.pivot("knob", "rotate", (bc, 0, zk), axis=(0, 0, 1), range=(0, 360 * TURNS), unit="deg")
    P.pivot("handle", "rotate", (vc, 0, vz / 2), axis=(0, 0, 1), range=(0, QUARTER), unit="deg")
    P.collider("env", 0.0, yg, zb - DRAIN_L, x2, HASP[1] - yg, zk + KNOB_H - (zb - DRAIN_L))
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="gauge side", az=300, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
