#!/usr/bin/env python3
"""compensator-ring-qt-6: generic tolerance compensator for a quarter-turn fastener, our own vendor-neutral design of the ETIM 10.0
class EC011999 (Tolerance compensator (quarter turn fastener); synonyms compensator ring, tolerance ring, protective cup), built
unattended (OPERATING.md 12, generic elements; group EG021006 Accessories/components for fasteners and anchoring systems, a tier-2 class
by name after spring-plate-qt-6, lib/rounds/mech/r147.md "Proposed next"). A flat zinc-plated steel ring that sits round latch 1.0's
stud between the frame flange's underside and the receptacle's base plate and takes up a stack 1.0 thinner than the 4.0 latch's stud
(Length 21) is built for (a 1.0 panel or a 1.0 flange in place of a 2.0): with the ring the receptacle's cam plate lies where latch puts
it, and the stud's cross pin locks 0.5 under it again. 2.0 (mech-r159, review mech-r148 finding 1): the ring is Ø40, the receptacle
plate's length, and carries the receptacle's two rivet holes (Ø3.4 at x ±14), so the rivets clamp flange, ring and base plate as one
solid stack; 1.0's Ø20 ring lay inside the rivets, which then bent the plate's ends up into the 1.0 gap. Every stud and receptacle
figure is read from latch with library.load, so the ring and the stud cannot drift apart. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC011999 rows): spec.md gives the design values under plain names, as
receptacle-clip-qt-6 and spring-plate-qt-6 do. Every size is a design choice. No load, holding force or locking claim. No vendor file
opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "compensator-ring-qt-6", "2.0", "connector-part"
TITLE = ("tolerance compensator ring for a quarter-turn fastener, generic, for a Ø6 stud with a Ø3 x 12 cross pin, zinc-plated steel, "
         "Ø40 x Ø14 x 1.0 with the receptacle's 2 rivet holes, takes up a 1.0 thinner stack")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic tolerance compensator (ETIM 10.0 EC011999), a flat ring Ø40 x Ø14 x 1.0 between the frame flange "
            "and latch 1.0's receptacle, its 2 x Ø3.4 rivet holes on the receptacle's (x +-14) so the rivets clamp the whole stack, that "
            "takes up a stack 1.0 thinner than latch's 4.0, the stud's and receptacle's figures read from latch (library.load); class "
            "features not on file, design values under plain names (spec.md); every size a design choice; no load, holding force or "
            "locking claim; no vendor file opened")
ORIGIN = ("the ring's top face (its seat against the frame flange's underside) z = 0, on the stud's axis, x along the receptacle's "
          "rivet line; -z into the ring (the receptacle's base plate under it)")
COMMAND = "CMPRQT6"
PARAMS = dict()

LT = library.load("latch")                   # latch 1.0: the stud, its cross pin and its receptacle (one home for each figure)
STACK = LT.PANEL_T + LT.FLANGE_T             # 4.0: the panel and flange stack latch's stud (Length 21) is built for
T = 1.0                                      # design: the ring's thickness, the take-up for a stack of 3.0 (a 1.0 panel or flange)
BORE_R = LT.PIN_L / 2 + 1.0                  # Ø14: latch's flange hole (spec.md What it meets), the Ø3 x 12 pin 1.0 clear at either end
OUT_R = LT.REC_X                             # design: Ø40, the receptacle base plate's length (x +-20): the ring carries the rivet holes
RIVET_X, RIVET_R = LT.RIVET_X, LT.RIVET_D / 2   # 2 x Ø3.4 at x +-14: the receptacle's rivet holes (M3 clearance medium, ISO 273)
MAT = "M-ZINC"                               # zinc-plated steel, as latch's grommet (render layer M-ZINC, not printed)

assert abs(BORE_R - 7.0) < 1e-9                                                                 # by hand: 12 / 2 + 1 = 7
assert BORE_R > LT.PIN_L / 2 and BORE_R > LT.BORE_R                                             # the pin passes at any angle, and the shank
assert abs(OUT_R - 20.0) < 1e-9 and abs(RIVET_X - 14.0) < 1e-9 and abs(RIVET_R - 1.7) < 1e-9    # by hand: Ø40, x +-14, Ø3.4
assert OUT_R - (RIVET_X + RIVET_R) >= 4.0                                                       # 20 - 15.7 = 4.3: the rivet holes inside the rim
assert RIVET_X - RIVET_R - BORE_R >= 4.0                                                        # 12.3 - 7 = 5.3: web between bore and rivet hole
assert OUT_R > LT.REC_Y                                                                         # the ring covers the receptacle plate's width (y +-7)
assert T <= 3.0                                                                                 # 1.0 sheet: the gate skips its edges ("thin")
assert abs(STACK - 4.0) < 1e-9 and abs((STACK - T) + T - STACK) < 1e-9                          # a 3.0 stack plus the ring = latch's 4.0
assert abs(LT.REC_TOP + STACK) < 1e-9                                                           # latch's receptacle base plate sits at -4.0: the stack


def build():
    P = Prims()
    ring = P.cyl(MAT, (0, 0, -T), (0, 0, 0), OUT_R)                                              # Ø40 x 1.0, z -1..0
    P.hole(MAT, (0, 0, -T - 1), (0, 0, 1), BORE_R, ring)                                         # Ø14 bore: the stud and its pin pass
    for sx in (-1, 1):                                                                           # the receptacle's rivet holes, x +-14
        P.hole(MAT, (sx * RIVET_X, 0, -T - 1), (sx * RIVET_X, 0, 1), RIVET_R, ring)
    P.collider("ring", -OUT_R, -OUT_R, -T, 2 * OUT_R, 2 * OUT_R, T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
