#!/usr/bin/env python3
"""thermowell-npt: a thermowell (temperature sensor fitting): a closed-ended protective tube that goes into the medium through a
line's or a vessel's female port, so a thermometer's or sensor's stem reads the medium's temperature without touching it and can be
taken out without opening the line. A wrench hex, a male NPT 3/8 stub below it into the host (the process connection), the well tube
below the stub, closed at its tip, and on top a female NPT 1/4 port with a bore down the well that takes gauge-t's stem.
Generic (OPERATING.md 12, EM 2026-11-07; autopilot.md 2.b2: the next ETIM class in pneu's order that builds): our own vendor-neutral
design of ETIM 10.0 EC004716 "Temperature sensor fitting" (synonym "Temperature measuring fitting"); the class values it is designed to
are in spec.md "## Class values". The NPT series and units come from toolkit/pneu.py (request pneu-1: D1 NPT threads). The male stub
is nipple-hex-npt's (a plain cylinder L2 long at E1 + h), the female port cap-hex-npt's (a bore at E1 + h, through a land 0.2 proud),
both from pneu.NPT (calculated from ASME B1.20.1's formulas, EM 2026-11-07). The instrument port, the stem bore and the well's length
are read from gauge-t (library.load: its PORT, STEM_D and INSERT_L), so the thermometer on file fits it face to face. The hex, the
well's wall and tip and the clearances are design choices. No vendor file was opened (pneu-r115)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "thermowell-npt", "1.0", "connector"
TITLE = "generic thermowell, male NPT 3/8 process, female NPT 1/4 instrument, for gauge-t's 100 mm stem"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic temperature sensor fitting (ETIM 10.0 EC004716), a thermowell turned from bar; NPT series from "
            "toolkit/pneu.py D1, the male process stub and the female instrument port from pneu.NPT (calculated from ASME B1.20.1's "
            "formulas); the instrument port, stem bore and well length read from gauge-t; the hex, well wall, tip and clearances are "
            "design choices")
ORIGIN = ("joint plane: the hex's seat face (the face that bears on the host's port) z = 0 on the well's axis (x = y = 0); the host "
          "and the medium toward -z, the instrument port up (+z)")
COMMAND = "THERMOWELL-NPT"
PARAMS = dict()

G = library.load("gauge-t")           # the thermometer on file the well is made for: its port, stem diameter and insertion length
PROCESS = "NPT3/8"                    # design choice: the largest size of our series (pneu.THREADS, D1), so the well passes through it
INSTRUMENT = G.PORT                   # gauge-t's back connection, NPT 1/4 female here
HEX_AF, HEX_L = 22.0, 13.0            # design choices: the wrench flats (>= 3 of steel round the instrument bore) and the hex's length
HEX_D = 1.05                          # corners turned to 1.05 x AF; round(AF x HEX_D) - AF <= 1.5 (cap-hex-npt r106's Godot check)
LAND_D, LAND_T = 19.0, 0.2            # design choice: the round land round the instrument bore (port-b's node), cap-hex-npt's
WELL_D = 12.7                         # design choice: the well tube's outside Ø (1/2 in), inside the process stub's E1 + h
STEM_CLEAR = 0.65                     # design choice: the stem bore over gauge-t's stem Ø (6.35 -> 7.0), a slip fit for the stem
TIP_CLEAR = 2.0                       # design choice: the stem's end stands 2 clear of the bore's floor
TIP_T = 4.0                           # design choice: the well's closed tip
WALL = 3.0                            # design choice: at least 3 of steel round each bore (tee-block-npt's, cap-hex-npt's)
IN = 0.5                              # each part runs 0.5 into the one above it (one solid joint)
MAT, MAT_BORE = "M-SILVER", "M-GASKET"   # stainless steel (class value); the bores' layer as cap-hex-npt's


def stub():
    """(diameter, length) of the male process stub in mm from pneu.NPT: E1 + h and L2 (nipple-hex-npt's rule)"""
    t = pneu.NPT[PROCESS]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[PROCESS]["length"]


def bore():
    """(diameter, depth) of the female instrument port in mm from pneu.NPT: E1 + h and L2 + 2 (cap-hex-npt's rule)"""
    t = pneu.NPT[INSTRUMENT]["table"]
    return (t["E1"] + t["h"]) * 25.4, pneu.NPT[INSTRUMENT]["length"] + 2.0


TOP = HEX_L + LAND_T                                  # 13.2: port-b's face, where gauge-t's hex seats
STEM_BORE = G.STEM_D + STEM_CLEAR                     # 7.0
FLOOR = TOP - G.INSERT_L - TIP_CLEAR                  # -88.8: the stem bore's floor
TIP = FLOOR - TIP_T                                   # -92.8: the well's closed end, the insertion length below the seat face

_sd, _sl = stub(); _bd, _bl = bore(); _gd, _gl = G.stub()
assert PROCESS in pneu.THREADS and INSTRUMENT in pneu.THREADS
assert TOP - IN >= _bl and _bl >= pneu.NPT[INSTRUMENT]["engagement"]   # the instrument bore (down to the stub's top) is L2 + 2 deep or more
assert abs(_gd - _bd) < 1e-6 and TOP - _gl > IN                     # gauge-t's stub fills the bore face to face and ends above its floor
assert HEX_AF - _bd >= 2 * WALL and HEX_AF > _sd                     # steel round the instrument bore; the hex covers the process stub
assert _bd + 2.0 < LAND_D < HEX_AF                                   # the land rings its bore, inside the flats
assert STEM_BORE < _bd and WELL_D - STEM_BORE >= 2 * 2.5 and WELL_D < _sd   # the stem bore steps down; well wall >= 2.5; well inside the stub
assert -_sl > TIP + 8.0                                              # the well reaches below the process stub
assert HEX_L >= 8.0 and round(HEX_AF * HEX_D) - HEX_AF <= 1.5        # fillet pre-flight; the glb's corners within the catalogue's rounding


def build():
    P = Prims(); d = HEX_AF * HEX_D
    hx = P.cyl(MAT, (0, 0, 0), (0, 0, HEX_L), d / 2.0); w = d + 4.0                                  # hex, seat face on z = 0
    for k in range(6):                                                                               # six flats (gauge-t's pattern)
        t = math.radians(30 + 60 * k); n = (math.cos(t), math.sin(t), 0.0); tg = (-math.sin(t), math.cos(t), 0.0)
        o = (n[0] * HEX_AF / 2.0 + tg[0] * w / 2.0, n[1] * HEX_AF / 2.0 + tg[1] * w / 2.0, -1.0)
        P.cut(MAT, o, n, (0, 0, 1), (-tg[0], -tg[1], 0.0), 4.0, HEX_L + 2.0, w, hx)
    P.hole(MAT_BORE, (0, 0, -1.0), (0, 0, HEX_L + 1.0), _bd / 2.0, hx)                                 # instrument bore through the hex
    f = P.cyl(f"node:port-b|{MAT}", (0, 0, HEX_L), (0, 0, TOP), LAND_D / 2.0)                          # the land (port-b's node)
    P.hole(MAT_BORE, (0, 0, HEX_L - 1.0), (0, 0, TOP + 1.0), _bd / 2.0, f)                             # the bore through the land
    s = P.cyl(f"node:port-a|{MAT}", (0, 0, -_sl), (0, 0, IN), _sd / 2.0)                               # male NPT 3/8 stub; its top the bore's floor
    P.hole(MAT_BORE, (0, 0, -_sl - 1.0), (0, 0, IN + 1.0), STEM_BORE / 2.0, s)                          # the stem bore through the stub
    wl = P.cyl(MAT, (0, 0, TIP), (0, 0, -_sl + IN), WELL_D / 2.0)                                      # the well, 0.5 up into the stub
    P.hole(MAT_BORE, (0, 0, FLOOR), (0, 0, -_sl + IN + 1.0), STEM_BORE / 2.0, wl)                      # the stem bore, blind at FLOOR
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, 0, -1), range=(0, 0), unit=PROCESS, gender="male", length=round(_sl, 3))
    P.pivot("port-b", "port", (0, 0, TOP), axis=(0, 0, 1), range=(0, 0), unit=INSTRUMENT, gender="female")
    r = d / 2.0
    P.collider("env", -r, -r, TIP, 2 * r, 2 * r, TOP - TIP)
    return P


PREVIEWS = [dict(name="three-quarter", az=225, el=25), dict(name="top", az=200, el=70), dict(name="tip", az=300, el=-20)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
