#!/usr/bin/env python3
"""post-partition-2000: generic post for a storage partition (a mesh partition, a storage cage's wall), 2000 high, our own
vendor-neutral design of the ETIM 10.0 class EC004104 (Post for storage partition; synonyms corner post, end post, middle post, storage
partition attachment pillar), built unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2
class walked by name after rack-lifting-gear-1000, lib/rounds/mech/r164.md). The post comes first of the partition set (foundation
first, OPERATING.md 12): the partition's elements (EC004103) and door (EC004105) bolt to its tabs, so the tabs' figures here are the
interface those elements read with library.load. A line post: a painted steel tube 50 x 50 x 2, closed at its top, standing on a floor
plate 150 x 150 x 8 with 4 x M10 anchor holes (ISO 273 medium), and on each of its two side faces (x) three welded tabs 8 thick with an
M8 hole (ISO 273 medium) at z 250, 1050 and 1850, all on one side of the post's centre plane (y -18 to -10), so a panel frame 20 deep
bolted against the tabs' +y faces lies centred on the partition's line y = 0. No element is placed or redrawn. The class's features
are not on file (lib/standards/etim/class-features.csv has no EC004104 rows): spec.md gives the design values under plain names, as
rack-lifting-gear-1000 does. Every size is a design choice. No load, impact or safety claim: a partition is no guard here, and fixing
it to the floor is the host's. No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "post-partition-2000", "1.0", "furniture"
TITLE = ("post for a storage partition, generic, line post 2000 high, painted steel tube 50 x 50 x 2 on a floor plate 150 x 150 x 8 "
         "with 4 M10 anchor holes, six panel tabs with M8 holes")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic post for storage partition (ETIM 10.0 EC004104), a line post of painted steel tube 50 x 50 x 2, "
            "2000 high and closed at its top, on a floor plate 150 x 150 x 8 with 4 x M10 anchor holes (ISO 273 medium) at +-55; on "
            "each side face (x) three welded tabs 40.5 x 8 x 40 at z 250, 1050, 1850, each with an M8 hole (ISO 273 medium) 20 out "
            "from the post's face, the tabs at y -18 to -10 so a panel frame 20 deep against them lies on the partition's line; class "
            "features not on file, design values under plain names (spec.md); every size a design choice; the panels, door and "
            "anchors not drawn; no load, impact or safety claim; no vendor file opened")
ORIGIN = ("the floor under the post's axis: z = 0 the floor plate's underside, x = 0 and y = 0 the post's centre; the partition runs "
          "along x (the tabs on the post's -x and +x faces), y = 0 the partition's centre plane")
COMMAND = "PPRT2000"
PARAMS = dict()

UP = 50.0                                       # design: the post's tube section, rack-lifting-gear-1000's (50 x 50)
T = 2.0                                         # design: the tube's wall
H = 2000.0                                      # design: the post's height (its top)
CAP = 8.0                                       # design: the tube closed at its top, a solid 8 (one box less one blind cutbox)
FP = 150.0                                      # design: the floor plate's side
FT = 8.0                                        # design: the floor plate's thickness
IN = 0.5                                        # each joint runs 0.5 into the part it meets (one body, a weld; strut's and bracket's way)
ANC_D = 11.0                                    # M10 clearance, ISO 273 medium (H13), lib/standards/holes.csv
ANC_P = 55.0                                    # design: the four anchor holes at x, y = +-55
TAB_Z = (250.0, 1050.0, 1850.0)                 # design: the tabs' middles, the panel's fixing heights (the interface EC004103 reads)
TAB_H = 40.0                                    # design: a tab's height
TAB_R = 40.0                                    # design: a tab's reach out of the post's face (x 25 to 65)
TAB_Y0, TAB_Y1 = -18.0, -10.0                   # design: the tabs' faces; a panel frame bolts against y = -10 (the interface)
TAB_HOLE_D = 9.0                                # M8 clearance, ISO 273 medium (H13), lib/standards/holes.csv
TAB_HOLE_X = UP / 2 + TAB_R / 2                 # 45: the tab hole's axis, 20 out from the post's face (the interface)
PANEL_GAP = 10.0                                # design: a panel frame's end 10 clear of the post's face (x 35); a frame tube 20 wide covers the hole
MAT = "M-STEEL-7035"                            # painted steel (rack-lifting-gear-1000's layer)

assert ANC_P + ANC_D / 2 <= FP / 2 - 12.0                                                   # 14.5 from an anchor hole's edge to the plate's edge
assert ANC_P - ANC_D / 2 >= UP / 2 + 20.0                                                   # 24.5 from the hole's edge to the post's face, for a nut and washer
assert UP / 2 + TAB_R <= FP / 2 - 10.0                                                      # 65 <= 65: the tabs stay inside the floor plate's outline in x
assert TAB_HOLE_X - TAB_HOLE_D / 2 - UP / 2 >= 15.0                                         # 15.5 from the tab hole's edge to the post's face, a nut's room
assert UP / 2 + TAB_R - TAB_HOLE_X - TAB_HOLE_D / 2 >= 15.0                                 # 15.5 to the tab's end
assert TAB_H / 2 - TAB_HOLE_D / 2 >= 15.0                                                   # 15.5 to the tab's top and bottom
assert -UP / 2 < TAB_Y0 and TAB_Y1 < 0.0 and TAB_Y1 - TAB_Y0 == 8.0                         # each tab on the post's face, 8 thick, on the -y side
assert UP / 2 + PANEL_GAP + 10.0 == TAB_HOLE_X                                              # a 20-wide frame tube from x 35 is centred on the hole
assert min(TAB_Z) - TAB_H / 2 >= 200.0 and max(TAB_Z) + TAB_H / 2 <= H - CAP - 100.0          # the tabs clear the floor plate and the top
assert min(b - a for a, b in zip(TAB_Z, TAB_Z[1:])) == 800.0                                # 800 between fixing heights
# Every edge is 2 (the tube's wall), 8, 40 or more: none falls in the gate's 3 to 7 mm free-corner fillet trap.
assert min(FT, CAP, TAB_Y1 - TAB_Y0, TAB_H, TAB_R) >= 8.0
# Volume by hand: the plate less 4 anchor holes; the tube from z 7.5 (0.5 in the plate) to 2000 less its bore from z 7.5 to 1992; six tabs
# 40.5 x 8 x 40 (0.5 in the tube's wall) less an M8 hole each. The joints' 0.5 overlaps are counted in both parts.
PLATE = FP * FP * FT - 4 * math.pi * (ANC_D / 2) ** 2 * FT
TUBE = UP * UP * (H - FT + IN) - (UP - 2 * T) ** 2 * (H - CAP - FT + IN)
TAB = (TAB_R + IN) * (TAB_Y1 - TAB_Y0) * TAB_H - math.pi * (TAB_HOLE_D / 2) ** 2 * (TAB_Y1 - TAB_Y0)
VOL = PLATE + TUBE + 6 * TAB
assert abs(PLATE - 176958.9) < 0.1 and abs(TUBE - 782048.0) < 1e-6 and abs(TAB - 12451.1) < 0.1 and abs(VOL - 1033713.3) < 0.1


def build():
    P = Prims()
    fp = P.box(MAT, -FP / 2, -FP / 2, 0.0, FP, FP, FT)                                         # the floor plate
    for sx in (-1, 1):
        for sy in (-1, 1):
            P.hole(MAT, (sx * ANC_P, sy * ANC_P, -1.0), (sx * ANC_P, sy * ANC_P, FT + 1.0), ANC_D / 2, fp)  # M10 anchor clearance
    P.collider("foot", -FP / 2, -FP / 2, 0.0, FP, FP, FT)
    t = P.box(MAT, -UP / 2, -UP / 2, FT - IN, UP, UP, H - FT + IN)                             # the post, 0.5 into the plate
    P.cutbox(MAT, -UP / 2 + T, -UP / 2 + T, FT - 1.0, UP - 2 * T, UP - 2 * T, H - CAP - FT + 1.0, t)  # its bore, open below, closed at the top
    P.collider("post", -UP / 2, -UP / 2, FT, UP, UP, H - FT)
    for sx, s in ((-1, "l"), (1, "r")):
        x0 = UP / 2 - IN if sx > 0 else -UP / 2 - TAB_R
        for z in TAB_Z:
            tb = P.box(MAT, x0, TAB_Y0, z - TAB_H / 2, TAB_R + IN, TAB_Y1 - TAB_Y0, TAB_H)    # a tab, 0.5 into the tube's wall
            P.hole(MAT, (sx * TAB_HOLE_X, TAB_Y0 - 1.0, z), (sx * TAB_HOLE_X, TAB_Y1 + 1.0, z), TAB_HOLE_D / 2, tb)  # M8 clearance
        xc = UP / 2 if sx > 0 else -UP / 2 - TAB_R
        P.collider(f"tabs-{s}", xc, TAB_Y0, min(TAB_Z) - TAB_H / 2, TAB_R, TAB_Y1 - TAB_Y0, max(TAB_Z) - min(TAB_Z) + TAB_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="behind", az=50, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
