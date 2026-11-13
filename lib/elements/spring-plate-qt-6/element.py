#!/usr/bin/env python3
"""spring-plate-qt-6: generic spring plate for a quarter-turn fastener, our own vendor-neutral design of the ETIM 10.0 class EC011978
(Spring plate (quarter turn fastener); synonyms rivet spring plate, spring bracket, weld spring plate), built unattended (OPERATING.md
12, generic elements; group EG021006 Accessories/components for fasteners and anchoring systems, a tier-2 class by name after
threaded-sleeve-m8, lib/rounds/mech/r146.md "Proposed next"). The one-piece pressed spring-steel bridge riveted behind a frame's flange
that latch 1.0's Ø6 stud locks under: two rivet tabs against the flange, two legs, and a bridge plate whose keyhole the stud's cross pin
passes at 90 degrees and locks behind at 0. It is the other form of the receptacle beside receptacle-clip-qt-6: a hat section with its
tabs OUTSIDE the legs, so nothing lies under the flange's hole and the rivets sit clear of the stud. Every stud figure is read from latch
with library.load, so the stud and the plate cannot drift apart. The cam ramps and the bridge's spring take-up are not drawn: the bridge
is flat. The class's features are not on file (lib/standards/etim/class-features.csv has no EC011978 rows): spec.md gives the design
values under plain names, as receptacle-clip-qt-6 and rack-cantilever do. Every size is a design choice. No load, holding force or
locking claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "spring-plate-qt-6", "1.0", "connector-part"
TITLE = ("spring plate for a quarter-turn fastener, generic, for a Ø6 stud with a Ø3 x 12 cross pin, pressed spring steel 1.2, "
         "hat section 52 x 14 x 10.2, keyhole in the bridge, 2 x M3 rivet holes in the tabs")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic spring plate (ETIM 10.0 EC011978), a hat-section receptacle for latch 1.0's quarter-turn stud, "
            "the stud's figures read from latch (library.load): bridge 21.6 x 14 x 1.2 with a keyhole for the Ø6 stud and its Ø3 x 12 "
            "cross pin, 10.2 deep, two legs and two rivet tabs 14 x 14 x 1.2 with 2 x M3 rivet holes ISO 273 medium at 38 pitch; class "
            "features not on file, design values under plain names (spec.md); every size a design choice; no load, holding force or "
            "locking claim; no vendor file opened")
ORIGIN = ("the tabs' top face (their seat against the frame flange's underside) z = 0, on the stud's axis; -z into the plate (the "
          "bridge at the bottom); the keyhole's slot and the rivet holes along x")
COMMAND = "SPRQT6"
PARAMS = dict()

LT = library.load("latch")                   # latch 1.0: the stud, its cross pin and its receptacle (one home for each figure)
RY, T = LT.REC_Y, LT.REC_T                   # 14 wide (y ±7), 1.2 sheet: the receptacle's width and gauge
DEPTH = LT.REC_TOP - (LT.CAM_TOP - LT.REC_T) # 10.2: the tabs' top to the bridge's underside (latch's receptacle depth)
BORE_R = LT.BORE_R                           # Ø7 keyhole bore: 0.5 clear round the Ø6 shank
SLOT_X, SLOT_Y = LT.REC_SLOT                 # the keyhole's slot x ±6.5, y ±2: the Ø3 x 12 pin 0.5 clear at each end and side
RIVET_D = LT.RIVET_D                         # Ø3.4: M3 clearance, ISO 273 medium
PIN_TOP = LT.PIN_Z + LT.PIN_R - LT.REC_TOP   # -10.7: the stud's pin top at rest (0 degrees), 0.5 under the bridge's underside
LEG_X = 12.0                                 # design: the legs' outer faces at x ±12, so the bridge's clear span is ±10.8
TAB_X = 26.0                                 # design: the tabs run x ±12 to ±26 (14 long, square on the 14 width)
RIVET_X = (LEG_X + TAB_X) / 2                # 19: the rivet holes on the tabs' centres, 38 pitch
MAT = "M-SILVER"                             # bright spring steel (lib/materials.csv steel-spring; render layer M-SILVER, not printed)

assert abs(DEPTH - 10.2) < 1e-9                                                                 # by hand: -4 - (-13 - 1.2) = 10.2
assert T <= 3.0                                                                                 # 1.2 sheet: every edge of its section "short"
assert DEPTH >= 8.0 and TAB_X - LEG_X >= 8.0 and 2 * (LEG_X - T) >= 8.0                         # every other edge >= 8: none in the 3-7 fillet trap
assert SLOT_X * 2 > LT.PIN_L and SLOT_Y * 2 > 2 * LT.PIN_R and BORE_R > LT.SHANK_R               # the pin and shank pass the keyhole
assert abs(PIN_TOP - (-DEPTH - 0.5)) < 1e-9                                                     # at rest the pin sits 0.5 under the bridge
assert LT.PIN_L / 2 < LEG_X - T and SLOT_X < LEG_X - T                                          # the pin's turn (r 6) and the slot clear the legs
assert RIVET_X - RIVET_D / 2 > LEG_X and RIVET_X + RIVET_D / 2 < TAB_X                          # the rivet holes lie on the tabs, clear of the legs


def build():
    P = Prims()
    br = P.box(MAT, -(LEG_X - T), -RY, -DEPTH, 2 * (LEG_X - T), 2 * RY, T)                       # bridge x ±10.8, z -10.2..-9.0
    P.hole(MAT, (0, 0, -DEPTH - 1), (0, 0, -DEPTH + T + 1), BORE_R, br)                          # keyhole: the Ø7 bore ...
    P.cutbox(MAT, -SLOT_X, -SLOT_Y, -DEPTH - 0.5, 2 * SLOT_X, 2 * SLOT_Y, T + 1, br)             # ... and the pin's slot along x
    for sx in (-1, 1):
        x0 = LEG_X - T if sx > 0 else -LEG_X
        P.box(MAT, x0, -RY, -DEPTH, T, 2 * RY, DEPTH)                                            # leg x ±10.8..±12, z -10.2..0
        t0 = LEG_X if sx > 0 else -TAB_X
        tab = P.box(MAT, t0, -RY, -T, TAB_X - LEG_X, 2 * RY, T)                                  # tab x ±12..±26, z -1.2..0
        P.hole(MAT, (sx * RIVET_X, 0, -T - 1), (sx * RIVET_X, 0, 1), RIVET_D / 2, tab)           # rivet hole Ø3.4 at x ±19
    P.collider("plate", -TAB_X, -RY, -DEPTH, 2 * TAB_X, 2 * RY, DEPTH)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
