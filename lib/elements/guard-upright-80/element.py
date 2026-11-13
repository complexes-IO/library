#!/usr/bin/env python3
"""guard-upright-80: generic U-shaped ram protection for a pallet rack's 80 x 80 upright, our own vendor-neutral design of the ETIM
10.0 class EC004073 (Ram protection (for rack element); synonyms pillar protection, rack ram protection, U-ram protection), built
unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class, after bracket-angle-strut-41,
lib/rounds/mech/r153.md). A steel U standing on the floor round the front and both sides of one upright, open toward the frame's
depth: a front wall and two side walls, 8 thick and 400 high, 15 clear of the upright's footplate all round, and a floor flange in
front of the front wall with 2 x M12 anchor holes (ISO 273 medium). The guard stands free of the rack: it touches neither the upright,
nor its footplate and anchors, nor the frame's bracing, nor the bay's floor-level pallet space (asserted below). The upright is
placed, never redrawn: its section, footplate and the bay's side gap are read from pallet-rack with library.load. The class's
features are not on file (lib/standards/etim/class-features.csv has no EC004073 rows): spec.md gives the design values under plain
names, as rack-cantilever and bracket-angle-strut-41 do. Every size is a design choice. No impact, energy or load claim; no safety
claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "guard-upright-80", "1.0", "furniture"
TITLE = ("ram protection for an 80 x 80 pallet rack upright, generic, U-shaped steel guard 196 x 138 x 400, walls 8, "
         "floor flange with 2 M12 anchor holes")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic ram protection (ETIM 10.0 EC004073), a U-shaped floor-anchored guard round one upright of "
            "pallet-rack 1.1 (80 x 80 on a 150 x 150 footplate): front and side walls 15 clear of the footplate, 2 M12 anchor holes "
            "(ISO 273 medium) in a front floor flange, the rack's figures read from pallet-rack (library.load); class features not on "
            "file, design values under plain names (spec.md); every size a design choice; no impact, energy, load or safety claim; "
            "no vendor file opened")
ORIGIN = ("the floor z = 0 on the protected upright's centre line: x = 0, y = 0 its centre; the aisle (the guarded front) toward -y, "
          "the frame's depth toward +y; the guard's walls stand round the upright's front and sides")
COMMAND = "GUPR80"
PARAMS = dict()

PR = library.load("pallet-rack")             # pallet-rack 1.1: the rack whose upright the guard protects (one home for each figure)
UP_W, UP_D = PR.UP_W, PR.UP_D                # 80 x 80: the upright's section
FOOT = PR.FOOT                               # 150: the upright's square footplate (its anchors lie on it)
GAP = PR.GAP                                 # 100: the bay's clear space between an upright's inner face and its floor-level pallet
CLR = 15.0                                   # design: clear space from the footplate's edge to each wall's inner face
T = 8.0                                      # design: wall and flange thickness (>= 8, over the gate's 3 to 7 mm free-corner trap)
H = 400.0                                    # design: wall height above the floor
FL = 60.0                                    # design: the floor flange's reach in front of the front wall
IN = 0.5                                     # each joint runs 0.5 into the wall it meets (one solid, strut's and bracket's way)
HOLE_D = 13.5                                # M12 clearance, ISO 273 medium (H13), lib/standards/holes.csv
HX = 60.0                                    # design: the two anchor holes at x = +-60
HALF_I = FOOT / 2 + CLR                      # 90: half the guard's inside width and the front wall's inner face (y = -90)
HALF_O = HALF_I + T                          # 98: half the outside width; the front wall's outer face y = -98
BACK = UP_D / 2                              # 40: the side walls end level with the upright's back face (the frame's bracing starts there)
FY = -HALF_O - FL / 2                        # -128: the anchor holes' line, half way out on the flange
MAT = "M-YELLOW"                             # painted steel, the rack beams' yellow

assert UP_W == UP_D                                                                  # a square upright: one inside width serves both directions
assert HALF_I - FOOT / 2 == CLR and HALF_I - UP_W / 2 >= 50.0                        # 15 clear of the footplate, 50 of the upright
assert HALF_O < UP_W / 2 + GAP                                                       # 98 < 140: out of the bay's floor-level pallet space
assert FY + HOLE_D / 2 <= -HALF_O - 20.0 and FY - HOLE_D / 2 >= -HALF_O - FL + 20.0  # 23.25 of flange each side of a hole (to the wall, to the edge)
assert HX + HOLE_D / 2 <= HALF_O - 20.0                                              # 31.25 from a hole's edge to the flange's side
assert min(T, H, FL, BACK + HALF_I) >= 8.0                                           # every free edge >= 8 (the gate's 3 to 7 mm trap)


def build():
    P = Prims()
    P.box(MAT, -HALF_O, -HALF_O, 0, 2 * HALF_O, T, H)                                             # front wall, y -98..-90
    for s in (-1, 1):                                                                              # side walls, x +-(90..98), y -90.5..40
        x0 = HALF_I if s > 0 else -HALF_O
        P.box(MAT, x0, -HALF_I - IN, 0, T, BACK + HALF_I + IN, H)
    fl = P.box(MAT, -HALF_O, -HALF_O - FL, 0, 2 * HALF_O, FL + IN, T)                             # floor flange, y -158..-97.5
    for s in (-1, 1):
        P.hole(MAT, (s * HX, FY, -1), (s * HX, FY, T + 1), HOLE_D / 2, fl)                         # M12 anchor clearance
    P.collider("wall-front", -HALF_O, -HALF_O, 0, 2 * HALF_O, T, H)
    P.collider("wall-left", -HALF_O, -HALF_I, 0, T, BACK + HALF_I, H)
    P.collider("wall-right", HALF_I, -HALF_I, 0, T, BACK + HALF_I, H)
    P.collider("flange", -HALF_O, -HALF_O - FL, 0, 2 * HALF_O, FL, T)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
