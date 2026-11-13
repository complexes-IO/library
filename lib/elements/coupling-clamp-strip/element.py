#!/usr/bin/env python3
"""coupling-clamp-strip: a clamp strip coupling, the band coupling that joins two plain-end pipes of the same outside diameter (or
closes a crack in one) without threads: an EPDM sleeve round the pipe ends, a stainless band round the sleeve, and two lugs on the
band that a pair of screws draw together, so the band squeezes the sleeve onto the pipes. Generic (OPERATING.md 12, EM 2026-11-07):
our own vendor-neutral design of ETIM 10.0 EC011508 "Clamp strip coupling" (synonyms clamp band coupling, repair clamp band, air tube
clamp); the class values it is designed to are in spec.md "## Class values". The pipe's outside diameter is the one figure it meets:
D of ASME B1.20.1 Table 2 for NPS 1/8, 1/4, 3/8 (pneu.NPT_INPUTS, the figures EM sent 2026-11-07), the OD of the steel pipe those
NPT threads are cut on. No dimensional standard on file sizes such a coupling (lib/standards/sources.csv has none): the sleeve, band,
lugs and length are design choices (spec.md Dimensions). The lugs' holes are M5 clearance, medium (ISO 273, lib/standards/holes.csv);
the screws (screw-iso4017, not built) are placed in a later version (OPERATING.md 12: model the holes, place the part later). The
band's split under the lugs is not drawn (an appearance, class C). The pipe passes through: no port, no node, nothing moves. No
vendor file was opened (pneu-r105)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "coupling-clamp-strip", "1.0", "connector-part"
TITLE = "generic clamp strip coupling, plain-end pipe NPS 1/4 (OD 13.72)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic clamp strip coupling (ETIM 10.0 EC011508), an EPDM sleeve in a stainless band drawn up by two "
            "screws through two lugs; pipe OD from pneu.NPT (ASME B1.20.1 Table 2 D); lug holes M5 clearance (ISO 273 medium, "
            "lib/standards/holes.csv), screws not placed; sleeve, band, lugs and length are design choices")
ORIGIN = "the coupling's centre on the pipe axis (x along the pipe, the two pipe ends meet at x = 0); the lugs up (+z)"
COMMAND = "COUPLING-CLAMP-STRIP"
PARAMS = dict(pipe="NPS1/4")

LENGTH = {"NPS1/8": 30.0, "NPS1/4": 40.0, "NPS3/8": 50.0}   # design choices: the coupling's length along the pipe, per pipe size
SLEEVE_T = 3.0                       # design choice: the EPDM sleeve's wall
SLEEVE_IN = 0.5                      # design choice: the sleeve's ends sit 0.5 inside the band's (no shared end plane)
BAND_T = 4.0                         # design choice: the stainless band's wall
GAP = 2.0                            # design choice: the gap between the two lugs (what the screws close)
LUG_T = 6.0                          # design choice: each lug's thickness across the gap (y)
LUG_END = 2.0                        # design choice: each lug stops 2 short of the band's ends
LUG_IN = 0.5                         # the lugs' bottom face 0.5 above the sleeve's outside, inside the band (one solid joint)
HOLE_D = 5.5                         # M5 clearance, medium (ISO 273 H13: 5.5 to 5.68; holes.csv)
HOLE_UP = 4.5                        # design choice: the holes' axis 4.5 above the band's outside
LUG_TOP = 5.0                        # design choice: the lug's top 5.0 above the holes' axis
MAT_BAND, MAT_SLEEVE = "M-SILVER", "M-GASKET"   # class values: stainless steel band and lugs, EPDM sleeve (black)


def pipe_od(pipe="NPS1/4"):
    """the pipe's outside diameter in mm: D of ASME B1.20.1 Table 2 from pneu.NPT (13.716 for NPS 1/4)"""
    return pneu.NPT["NPT" + pipe[3:]]["table"]["D"] * 25.4


def radii(pipe="NPS1/4"):
    """(pipe, sleeve outside, band outside) radii in mm"""
    rp = pipe_od(pipe) / 2.0
    return rp, rp + SLEEVE_T, rp + SLEEVE_T + BAND_T


def holes_x(pipe="NPS1/4"):
    """the two screws' positions along the pipe: one over each pipe end, at +-L/4"""
    return (-LENGTH[pipe] / 4.0, LENGTH[pipe] / 4.0)


for _p, _L in LENGTH.items():
    assert "NPT" + _p[3:] in pneu.THREADS
    _rp, _rs, _rb = radii(_p)
    _yo, _zb = GAP / 2.0 + LUG_T, _rs + LUG_IN
    assert math.sqrt(_rb ** 2 - _yo ** 2) >= _zb + 0.5             # each lug's whole bottom face lies inside the band (joined, no step)
    assert _rb + HOLE_UP - HOLE_D / 2.0 >= _rb + 1.5               # the holes stay in the lugs, 1.5 or more above the band
    assert LUG_TOP - HOLE_D / 2.0 >= 2.0                           # 2 or more of lug above each hole
    assert _L / 2.0 - LUG_END - _L / 4.0 - HOLE_D / 2.0 >= 2.5     # 2.5 or more of lug between each hole and the lug's end
    assert _L / 2.0 - SLEEVE_IN >= 1.0 * pipe_od(_p)               # each pipe end goes in at least one OD (its grip in the sleeve)


def build(pipe="NPS1/4"):
    if pipe not in LENGTH: raise ValueError(f"pipe {pipe}: one of {', '.join(LENGTH)} (plain-end pipe, NPT D1 sizes)")
    P = Prims(); L = LENGTH[pipe]; rp, rs, rb = radii(pipe); x0 = -L / 2.0
    xs = x0 + SLEEVE_IN
    sleeve = P.cyl(MAT_SLEEVE, (xs, 0, 0), (-xs, 0, 0), rs)                                     # EPDM sleeve round the pipe ends
    P.hole(MAT_SLEEVE, (xs - 1.0, 0, 0), (-xs + 1.0, 0, 0), rp, sleeve)                        # its bore: the pipe's OD
    band = P.cyl(MAT_BAND, (x0, 0, 0), (-x0, 0, 0), rb)                                         # stainless band round the sleeve
    P.hole(MAT_BAND, (x0 - 1.0, 0, 0), (-x0 + 1.0, 0, 0), rs, band)                            # its bore: the sleeve's outside
    zb, zh = rs + LUG_IN, rb + HOLE_UP; zt = zh + LUG_TOP; lx = L - 2 * LUG_END
    for s in (1.0, -1.0):                                                                      # the two lugs, the gap between them
        y0 = GAP / 2.0 if s > 0 else -GAP / 2.0 - LUG_T
        lug = P.box(MAT_BAND, x0 + LUG_END, y0, zb, lx, LUG_T, zt - zb)
        for x in holes_x(pipe):
            P.hole(MAT_BAND, (x, s * (GAP / 2.0 - 0.5), zh), (x, s * (GAP / 2.0 + LUG_T + 1.0), zh), HOLE_D / 2.0, lug)   # M5 clearance
    P.collider("env", x0, -rb, -rb, L, 2 * rb, zt + rb)
    return P


PREVIEWS = [dict(name="three-quarter, NPS 1/4", az=250, el=30), dict(name="end on the pipe axis", az=180, el=0),
            dict(name="NPS 1/8", az=250, el=30, params=dict(pipe="NPS1/8")),
            dict(name="NPS 3/8", az=250, el=30, params=dict(pipe="NPS3/8"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
