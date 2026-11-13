#!/usr/bin/env python3
"""receptacle-clip-qt-6: generic receptacle clip for a quarter-turn fastener, our own vendor-neutral design of the ETIM 10.0 class
EC011979 (Receptacle clip (quarter turn fastener); synonyms front load receptacle, three part clip), built unattended (OPERATING.md 12,
generic elements; group EG021006 Accessories/components for fasteners and anchoring systems, the next group of lib/toolkit/generic.py's
mech order after EG020045, a tier-2 class by name after the classes skipped in lib/rounds/mech/r144.md). The pressed spring-steel
stirrup riveted under a frame's flange that latch 1.0's Ø6 stud locks into: a base plate against the flange with a keyhole and two
M3 rivet holes, two legs, and a cam plate whose keyhole the stud's cross pin passes at 90 degrees and locks behind at 0. It is the
receptacle latch 1.0 draws inside itself, made its own element so a host (and a later latch version) places it rather than redraws it
(OPERATING.md 12, common parts). Every figure is read from latch with library.load, so the stud and the clip cannot drift apart. The
cam ramps that pull the stud in and the spring take-up are not drawn: the plates are flat. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC011979 rows): spec.md gives the design values under plain names, as rack-cantilever
and fan-exhaust do. Every size is a design choice. No load, holding force or locking claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "receptacle-clip-qt-6", "1.0", "connector-part"
TITLE = ("receptacle clip for a quarter-turn fastener, generic, for a Ø6 stud with a Ø3 x 12 cross pin, pressed spring steel 1.2, "
         "40 x 14 x 10.2, keyholes in both plates, 2 x M3 rivet holes")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic receptacle clip (ETIM 10.0 EC011979), the receptacle of latch 1.0's quarter-turn fastener as its "
            "own part, every figure read from latch (library.load): base and cam plates 40 x 14 x 1.2 joined by two legs, 10.2 deep, "
            "keyholes for the Ø6 stud and its Ø3 x 12 cross pin, 2 x M3 rivet holes ISO 273 medium; class features not on file, "
            "design values under plain names (spec.md); every size a design choice; no load, holding force or locking claim; no "
            "vendor file opened")
ORIGIN = ("the base plate's top face (its seat against the frame flange's underside) z = 0, on the stud's axis; -z into the clip "
          "(the cam plate at the bottom); the keyholes' slots along x, the rivet holes on x")
COMMAND = "RECQT6"
PARAMS = dict()

LT = library.load("latch")                   # latch 1.0: the stud, its cross pin and the receptacle it draws (one home for each figure)
RX, RY, T = LT.REC_X, LT.REC_Y, LT.REC_T     # plates 40 (x) x 14 (y), 1.2 sheet
DEPTH = LT.REC_TOP - (LT.CAM_TOP - LT.REC_T) # 10.2: the base plate's top to the cam plate's underside
CAM_TOP = LT.CAM_TOP - LT.REC_TOP            # -9.0: the cam plate's top face, from the base plate's top
BORE_R = LT.BORE_R                           # Ø7 keyhole bore: 0.5 clear round the Ø6 shank
SLOT_X, SLOT_Y = LT.REC_SLOT                 # the keyhole's slot x ±6.5, y ±2: the Ø3 x 12 pin 0.5 clear at each end and side
RIVET_X, RIVET_D = LT.RIVET_X, LT.RIVET_D    # 2 x Ø3.4 at x ±14: M3 clearance, ISO 273 medium
PIN_TOP = LT.PIN_Z + LT.PIN_R - LT.REC_TOP   # -10.7: the stud's pin top at rest (0 degrees), 0.5 under the cam plate's underside
MAT = "M-SILVER"                             # bright spring steel (lib/materials.csv steel-spring; render layer M-SILVER, not printed)

assert abs(DEPTH - 10.2) < 1e-9 and abs(CAM_TOP + 9.0) < 1e-9                                  # by hand: 4 - (13 - 1.2) ... = 10.2, -13 + 4
assert T <= 3.0                                                                                # 1.2 sheet: every edge of its section "short"
assert SLOT_X * 2 > LT.PIN_L and SLOT_Y * 2 > 2 * LT.PIN_R and BORE_R > LT.SHANK_R              # the pin and shank pass the keyholes
assert abs(PIN_TOP - (CAM_TOP - T - 0.5)) < 1e-9                                                # at rest the pin sits 0.5 under the cam plate
assert RIVET_X + RIVET_D / 2 < RX - T and RIVET_X - RIVET_D / 2 > SLOT_X                        # the rivet holes clear the legs and the slot


def build():
    P = Prims()
    for z0 in (-T, CAM_TOP - T):                                                                 # base plate z -1.2..0, cam plate z -10.2..-9.0
        pl = P.box(MAT, -RX, -RY, z0, 2 * RX, 2 * RY, T)
        P.hole(MAT, (0, 0, z0 - 1), (0, 0, z0 + T + 1), BORE_R, pl)                              # keyhole: the Ø7 bore ...
        P.cutbox(MAT, -SLOT_X, -SLOT_Y, z0 - 0.5, 2 * SLOT_X, 2 * SLOT_Y, T + 1, pl)             # ... and the pin's slot along x
        if z0 > CAM_TOP:                                                                         # the base plate: the two rivet holes
            for sx in (-1, 1): P.hole(MAT, (sx * RIVET_X, 0, z0 - 1), (sx * RIVET_X, 0, z0 + T + 1), RIVET_D / 2, pl)
    for sx in (-1, 1):
        x0 = RX - T if sx > 0 else -RX
        P.box(MAT, x0, -RY, CAM_TOP, T, 2 * RY, -T - CAM_TOP)                                    # leg, plate to plate (z -9.0..-1.2)
    P.collider("clip", -RX, -RY, -DEPTH, 2 * RX, 2 * RY, DEPTH)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
