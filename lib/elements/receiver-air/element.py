#!/usr/bin/env python3
"""receiver-air: a vertical compressed air receiver (air tank) for a compressor station: the vessel between the compressor and
the line that stores air and lets condensate settle. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of
ETIM 10.0 EC012187 "Pressured air vessel" (synonyms "Compressed air reservoir", "Compressed air tank"); lib/inventory.csv row
`receiver-air` (own_design generic, "compressed air receiver"; compressor-station, compressors-plant). The row has no class; this
one is the class classes.csv names for a compressed air tank, and it fits both systems (a station's receiver). Its sizes are design
choices, our own (no vendor file opened). A shell standing on four legs with a dished end top and bottom (drawn as a stepped
cylinder each, appearance only); air enters `port-1` (female NPT 3/8, low on the left side, ISO 11727 number 1 as pneu.NODES)
and leaves through `port-2` (female NPT 3/8, high on the right side, number 2); `port-g` (female NPT 1/4, role gauge) and
`port-relief` (female NPT 1/4, no role) stand on the top end; `port-drain` (female NPT 1/4, no role) under the bottom end.
Threads ASME B1.20.1 (toolkit/pneu.py THREADS, D1); NPT 3/8 is the largest size on file, as tank's and coolant-pump's liquid
ports. Each bore as regulator 1.0's: Ø E1 + h, L2 + 2 deep, blind in its boss, role in features.csv (HOLE-010). No relief valve,
gauge or drain valve is part of this element: the ports take them (the relief valve is no element yet: needs-em r68). No
pressure-vessel code is on file, so the shell's wall is not designed to one: it is used for the capacity only, and the vessel is
modelled solid. No safety claim.
2.0 (pneu-r79, review receiver-air-1.0.md findings 1 and 2): the vessel stands 100 higher on longer legs, so `port-drain`'s face
is 206 above the floor: room below it for drain-auto (its height read from its own element, not copied), a male-male nipple
between the two female ports (no element on file: an allowance, a design choice), a fitting-pushin in drain-auto's own drain port
(its length read from its element) and the tube's bend. Every port node moved in z with the vessel: a major."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "receiver-air", "2.0", "device"
TITLE = "generic compressed air receiver, vertical, 50 l, 11 bar, NPT 3/8 inlet and outlet, four legs"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic pressured air vessel, a vertical compressed air receiver (ETIM 10.0 EC012187; inventory "
            "own_design generic); ports female NPT (ASME B1.20.1, toolkit/pneu.py THREADS, D1), inlet and outlet numbered to ISO 11727 "
            "(pneu.NODES); shell, dished ends, legs and bosses are design choices")
ORIGIN = "the floor contact plane z = 0 on the vessel's axis (x = y = 0); z up, the inlet toward -x, the outlet toward +x"
COMMAND = "RECEIVER-AIR"
PARAMS = dict()

SHELL_D, SHELL_Z = 300.0, (260.0, 960.0)   # design choices: the shell's diameter and its height (z from, to); 2.0: 100 higher
WALL = 3.0                                 # design choice: wall thickness, used for the capacity only (modelled solid)
DOME_D, DOME_L = 240.0, 40.0               # design choice: each dished end drawn as a Ø240 x 40 step (appearance, not a head shape)
LEG, LEG_Z1, LEG_IN = 40.0, 340.0, 2.0     # design choices: four square legs 40 x 40, from the floor to z 340, 2 into the shell
BIG, SMALL = "NPT3/8", "NPT1/4"            # from pneu.THREADS (D1): inlet and outlet; gauge, relief and drain
BOSS = {BIG: 28.0, SMALL: 20.0}            # design choices: each port's round boss diameter by its size
PROUD = 14.0                               # design choice: each boss stands 14 proud of the surface it sits on
SINK = 10.0                                # each boss runs 10 into the shell or end it sits on (one solid joint on a curved face)
Z_IN, Z_OUT = 400.0, 860.0                 # design choices: the inlet low (the condensate settles below the outlet), the outlet high
NIPPLE = 10.0                              # design choice, an allowance: the gap a male-male NPT 1/4 nipple's hex keeps between
                                           # port-drain's face and drain-auto's inlet face (both female; no nipple element on file)
TUBE_ROOM = 30.0                           # design choice, an allowance: room under the drain's own fitting for the tube's bend
X_TOP = 60.0                               # design choice: gauge (-x) and relief (+x) bosses on the top end, 60 off the axis
CAPACITY_L = 50.0                          # class value 7 (EF000364 Capacity): the nominal volume
P_MAX_BAR = 11.0                           # class value 8 (EF020449 Max. operating pressure): ratings.csv p_max
IN = 0.5                                   # every other fixed part runs 0.5 into what it sits on
MAT_BODY, MAT_BOSS = "M-STEEL-7035", "M-GALV"

R = SHELL_D / 2.0
ZB = SHELL_Z[0] - DOME_L                   # the bottom end's lowest face
ZT = SHELL_Z[1] + DOME_L                   # the top end's top face


def volume_l():
    """inner volume in litres: the shell's bore over its height and both ends' steps, each less one WALL"""
    d, dd = SHELL_D - 2 * WALL, DOME_D - 2 * WALL
    shell = math.pi / 4 * d * d * (SHELL_Z[1] - SHELL_Z[0])
    ends = 2 * math.pi / 4 * dd * dd * (DOME_L - WALL)
    return (shell + ends) / 1e6


def bore(size):
    """the bore at the male stub's diameter, E1 + h (pneu.NPT, ASME B1.20.1 by its formulas), and its depth L2 + 2"""
    t = pneu.NPT[size]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[size]["length"] + 2.0


for _s in (BIG, SMALL):
    assert _s in pneu.THREADS
    assert BOSS[_s] - bore(_s)[0] >= 2 * 3.0                         # at least 3 mm of boss wall round each bore
    assert BOSS[_s] >= pneu.NPT[_s]["table"]["D"] * 25.4 + 6.0       # and round the pipe OD
    assert PROUD > bore(_s)[1] >= pneu.NPT[_s]["engagement"]         # bore deeper than make-up, blind inside the proud part
assert volume_l() >= CAPACITY_L                                      # 50.7 l inner: the nominal 50 l
assert P_MAX_BAR * 100.0 >= pneu.P_SUPPLY                            # PNE-003 (kPa): 1100 >= 689.5
assert DOME_D < SHELL_D and BOSS[SMALL] / 2.0 + X_TOP < DOME_D / 2.0  # the top bosses on the top end's face
def drain_stack():
    """what hangs below port-drain's face, in mm: the nipple's gap, drain-auto (its height from its own element), a fitting-pushin
    in drain-auto's drain port (its length from its own element) and the tube's bend room"""
    return NIPPLE + library.load("drain-auto").height() + library.load("fitting-pushin").length() + TUBE_ROOM


assert ZB - PROUD >= drain_stack()                                   # port-drain's face (206) clears the stack (193.5) above the floor
assert Z_IN - BOSS[BIG] / 2.0 > LEG_Z1 and Z_OUT + BOSS[BIG] / 2.0 < SHELL_Z[1]   # side bosses clear of the legs, on the shell
assert SHELL_Z[0] < LEG_Z1


def ports():
    """(node, size, face point (the joint plane's centre), axis, start point inside what it sits on, role)"""
    return (("port-1", BIG, (-R - PROUD, 0.0, Z_IN), (-1, 0, 0), (-R + SINK, 0.0, Z_IN), "supply"),
            ("port-2", BIG, (R + PROUD, 0.0, Z_OUT), (1, 0, 0), (R - SINK, 0.0, Z_OUT), "work"),
            ("port-g", SMALL, (-X_TOP, 0.0, ZT + PROUD), (0, 0, 1), (-X_TOP, 0.0, ZT - IN), "gauge"),
            ("port-relief", SMALL, (X_TOP, 0.0, ZT + PROUD), (0, 0, 1), (X_TOP, 0.0, ZT - IN), None),
            ("port-drain", SMALL, (0.0, 0.0, ZB - PROUD), (0, 0, -1), (0.0, 0.0, ZB + IN), None))


def build():
    P = Prims()
    P.cyl(MAT_BODY, (0, 0, SHELL_Z[0]), (0, 0, SHELL_Z[1]), R)                                         # shell
    P.cyl(MAT_BODY, (0, 0, ZB), (0, 0, SHELL_Z[0] + IN), DOME_D / 2.0)                                 # bottom end
    P.cyl(MAT_BODY, (0, 0, SHELL_Z[1] - IN), (0, 0, ZT), DOME_D / 2.0)                                 # top end
    for sx, sy in ((1, 0), (-1, 0), (0, 1), (0, -1)):                                                  # four legs, on x and y
        r0, r1 = R - LEG_IN, R - LEG_IN + LEG
        if sx: x0, y0, dx, dy = (r0 if sx > 0 else -r1), -LEG / 2, LEG, LEG
        else: x0, y0, dx, dy = -LEG / 2, (r0 if sy > 0 else -r1), LEG, LEG
        P.box(MAT_BODY, x0, y0, 0.0, dx, dy, LEG_Z1)
    for node, size, face, ax, start, role in ports():                                                  # bosses, bores, pivots
        d, l = bore(size)
        boss = P.cyl(f"node:{node}|{MAT_BOSS}", start, face, BOSS[size] / 2.0)
        P.hole(MAT_BOSS, tuple(face[i] + ax[i] * 1.0 for i in range(3)), tuple(face[i] - ax[i] * l for i in range(3)), d / 2.0, boss)
        extra = dict(role=role) if role else {}
        P.pivot(node, "port", face, axis=ax, range=(0, 0), unit=size, gender="female", **extra)
    e = R - LEG_IN + LEG
    P.collider("env", -e, -e, 0.0, 2 * e, 2 * e, ZT + PROUD)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="outlet side", az=60, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
