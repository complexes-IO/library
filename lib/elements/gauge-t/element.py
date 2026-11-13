#!/usr/bin/env python3
"""gauge-t: a bimetal dial thermometer, back (axial) connection, for the liquid and air lines of the process skids and the
heat-exchanger loop. Generic (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC011165 "Bimetal
thermometer", synonym "Thermometer"; lib/inventory.csv row `gauge-t` (own_design generic, 2 systems). No vendor file was opened
(the folder's metadata.json and references/ were not used). It is gauge-p's case, bezel, window, dial and pointer turned to face up
(+z), with the stem on the dial's axis below: a hex, a male NPT 1/4 stub (`port-1`, role gauge) drawn as gauge-p draws its stub,
a plain cylinder at E1 + h, length L2, both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), so it
meets a female NPT 1/4 port bored at E1 + h face to face (the stem needs a port that bores through into the medium: no host on
file has one yet, spec.md Ports); and below the stub the insertion stem that carries the bimetal coil
into the medium. The range is 0 to 120 °C and the max. operating pressure 10 bar, both class values (design inputs). Every size
is a design choice. The pointer (`pointer`, rotate about the dial's axis, 0 to 270 degrees) is the one moving part: the twin
turns it to the temperature it reads. The bimetal coil inside the stem is not modelled."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "gauge-t", "1.2", "device"
TITLE = "generic bimetal dial thermometer, 0-120 C, 63 mm case, 100 mm stem, NPT 1/4 male back mount"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Bimetal thermometer (ETIM 10.0 EC011165, synonym thermometer), a dial thermometer with a "
            "back (axial) NPT 1/4 male connection and a 100 mm insertion stem (inventory own_design generic); NPT stub from "
            "pneu.NPT (calculated from ASME B1.20.1's formulas, pneu.py D1); range 0-120 C and max. operating pressure 10 bar "
            "as class values; case, bezel, window, dial, hex, stem and pointer are design choices")
ORIGIN = "joint plane: the hex's seat face z = 0 on the stem's axis (x = y = 0); the host's port and the stem toward -z, the dial up"
COMMAND = "GAUGE-T"
PARAMS = dict()

PORT = "NPT1/4"                       # pneu.THREADS (D1); the gauge size from request pneu-1's element list (gauge-p), as gauge-p
RANGE_C = (0.0, 120.0)                # class value 6 (EF001836 Measuring range): design input
P_MAX_BAR = 10.0                      # class value 12 (EF020449 Max. operating pressure): design input, >= P_SUPPLY
INSERT_L, STEM_D = 100.0, 6.35        # design choices: insertion length below the seat face (class value 8), stem Ø (1/4 in)
HEX_AF, HEX_L = 15.0, 9.0             # design choices: the wrench flats and their length along z (as gauge-p)
HEX_D = 1.12                          # corners turned to 1.12 x AF (as fitting-pushin, gauge-p)
NECK_D = 12.0                         # design choice: the neck between the hex and the case
CASE_D, CASE_Z = 63.0, (12.0, 33.0)   # design choices: the case (class value 7, the 2.5 in nominal dial class), its depth along z
BEZEL_D, BEZEL_Z = 64.0, (32.0, 39.0)     # design choice: the front ring, 0.5 proud of the case, 1.0 down into it
OPEN_D = 57.0                         # design choice: the bezel's window opening (features.csv role)
WINDOW_D, WINDOW_Z = 58.0, (37.5, 38.5)   # design choice: the clear window, held 0.5 into the ring all round
DIAL_D, DIAL_Z = 57.6, (32.5, 34.0)       # design choice: the white dial plate, 0.5 into the case, its face at z = 34
HUB_D, HUB_Z = 5.0, (34.0, 35.8)          # design choice: the pointer's hub, seated face to face on the dial (it turns)
NEEDLE = dict(tail=4.0, reach=24.0, w=1.6, z=(34.4, 35.3))    # design choice: the pointer, clear of the dial and the window
SWEEP = 270.0                         # degrees from the range's bottom to its top, clockwise seen from above (design choice)
IN = 0.5                              # each fixed part runs 0.5 into the one it sits on (one solid joint)
MAT_METAL, MAT_DIAL, MAT_WINDOW, MAT_POINTER = "M-SILVER", "M-WHITE-PA", "M-CASE-CLEAR", "M-BLACK-PA"

assert PORT in pneu.THREADS
_T = pneu.NPT[PORT]["table"]
assert HEX_AF > (_T["E2"] + _T["h"]) * 25.4                     # the flats clear the thread's largest major diameter (E2 + h)
assert NECK_D < HEX_AF and NECK_D < CASE_D
assert STEM_D < (_T["E1"] + _T["h"]) * 25.4 and INSERT_L > pneu.NPT[PORT]["length"] + 10.0   # the stem leaves the stub below it
assert pneu.to_kpa(P_MAX_BAR, "bar") >= pneu.P_SUPPLY             # PNE-003 passes on any bench line (1000 >= 689.5 kPa)
assert NEEDLE["reach"] < OPEN_D / 2.0 and NEEDLE["tail"] > HUB_D / 2.0   # the pointer sweeps inside the opening, through its hub
assert WINDOW_Z[0] > NEEDLE["z"][1] and WINDOW_Z[0] > HUB_Z[1] and NEEDLE["z"][0] > DIAL_Z[1] and HUB_Z[0] == DIAL_Z[1]
assert DIAL_D > OPEN_D and WINDOW_D > OPEN_D and BEZEL_Z[0] < CASE_Z[1] and DIAL_Z[0] < CASE_Z[1] < DIAL_Z[1]


def stub():
    """(diameter, length) of the NPT male stub in mm from pneu.NPT: E1 + h and L2 (fitting-pushin 2.0's rule)"""
    return (_T["E1"] + _T["h"]) * 25.4, pneu.NPT[PORT]["length"]


def _hex_z(P, L, z0, z1, af, d):
    """a hex prism on the z axis: a cylinder of diameter d with six flats cut at af / 2 (gauge-p's pattern)"""
    c = P.cyl(L, (0, 0, z0), (0, 0, z1), d / 2.0); w = d + 4.0
    for k in range(6):
        t = math.radians(30 + 60 * k); n = (math.cos(t), math.sin(t), 0.0); tg = (-math.sin(t), math.cos(t), 0.0)
        o = (n[0] * af / 2.0 + tg[0] * w / 2.0, n[1] * af / 2.0 + tg[1] * w / 2.0, z0 - 1.0)
        P.cut(L, o, n, (0, 0, 1), (-tg[0], -tg[1], 0.0), 4.0, abs(z1 - z0) + 2.0, w, c)
    return c


def build():
    P = Prims(); sd, sl = stub(); R = CASE_D / 2.0
    P.cyl(f"node:port-1|{MAT_METAL}", (0, 0, -sl), (0, 0, IN), sd / 2.0)                               # NPT male stub, L2 below
    _hex_z(P, f"node:port-1|{MAT_METAL}", 0.0, HEX_L, HEX_AF, HEX_AF * HEX_D)                         # hex, seat face on z = 0
    P.cyl(MAT_METAL, (0, 0, -INSERT_L), (0, 0, -sl + IN), STEM_D / 2.0)                               # insertion stem below the stub
    P.cyl(MAT_METAL, (0, 0, HEX_L - IN), (0, 0, CASE_Z[0] + 3 * IN), NECK_D / 2.0)                   # neck into the case
    P.cyl(MAT_METAL, (0, 0, CASE_Z[0]), (0, 0, CASE_Z[1]), R)                                          # case
    ring = P.cyl(MAT_METAL, (0, 0, BEZEL_Z[0]), (0, 0, BEZEL_Z[1]), BEZEL_D / 2.0)                     # bezel
    P.hole(MAT_METAL, (0, 0, BEZEL_Z[0] - 1.0), (0, 0, BEZEL_Z[1] + 1.0), OPEN_D / 2.0, ring)        # its window opening
    P.cyl(MAT_WINDOW, (0, 0, WINDOW_Z[0]), (0, 0, WINDOW_Z[1]), WINDOW_D / 2.0)                       # clear window in the ring
    P.cyl(MAT_DIAL, (0, 0, DIAL_Z[0]), (0, 0, DIAL_Z[1]), DIAL_D / 2.0)                               # dial plate
    P.cyl(f"node:pointer|{MAT_POINTER}", (0, 0, HUB_Z[0]), (0, 0, HUB_Z[1]), HUB_D / 2.0)            # pointer hub
    a = math.sqrt(0.5); d = (-a, -a, 0.0); u = (0.0, 0.0, 1.0); ez = (-a, a, 0.0)   # at rest (0 °C) the pointer points to the lower left; ez = d x u
    t, w = NEEDLE["tail"], NEEDLE["w"]; z0, z1 = NEEDLE["z"]
    o = (-d[0] * t - ez[0] * w / 2.0, -d[1] * t - ez[1] * w / 2.0, z0)
    P.obox(f"node:pointer|{MAT_POINTER}", o, d, u, ez, t + NEEDLE["reach"], z1 - z0, w)               # pointer, right-handed axes
    P.pivot("port-1", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PORT, gender="male", role="gauge", length=round(sl, 3))
    P.pivot("pointer", "rotate", (0, 0, HUB_Z[1]), axis=(0, 0, -1), range=(0, SWEEP), unit="deg")      # -z: clockwise seen from above
    rb = BEZEL_D / 2.0
    P.collider("env", -rb, -rb, -INSERT_L, 2 * rb, 2 * rb, BEZEL_Z[1] + INSERT_L)
    return P


PREVIEWS = [dict(name="dial", az=200, el=60), dict(name="three-quarter", az=225, el=25), dict(name="stem", az=300, el=-20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
