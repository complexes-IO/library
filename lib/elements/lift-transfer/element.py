#!/usr/bin/env python3
"""lift-transfer: a pneumatic lift-and-transfer unit, our own design (OPERATING.md 12, own designs; inventory row own_design "yes":
"pneumatic lift-and-transfer between two conveyor lines (our own build)"; lib/machines-from-elements.txt, conveyor-types-bench). It
stands on the floor inside a conveyor-roller 1.0 section, between the rollers: a base plate with four M12 anchor holes, two guide
posts, and one lift carriage (node `lift`) that rises 20 straight up. The carriage is a plate with three transfer strips that stand
in the gaps between the conveyor's rollers (gaps 9-10, 10-11 and 11-12, read from conveyor-roller with library.load, so the two
cannot drift apart): lowered, the strips' tops are 5 under the rollers' tops and goods roll over them; raised, they stand 15 above
the rollers and carry the goods sideways (along x) onto the next line. The conveyor it stands in is placed by the assembly beside
it; nothing of it is drawn here. The cylinder that lifts the carriage, its valve, its sensing and the transfer drive (rollers, belts
or a pusher on the strips) are placed in a later version (OPERATING.md 12: a host doesn't model holes for a part it places later;
no cylinder element is on file yet). Every size is a design choice. No load, speed or cycle claim. No vendor file was opened (the
folder's record, references/source.txt, says there is none)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "lift-transfer", "1.0", "furniture"
TITLE = "lift-and-transfer unit, own design, for a conveyor-roller 1.0 section: base 480 x 240 with 4 x M12 anchor holes, two posts, lift carriage with three strips rising 20"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; strips placed in "
            "conveyor-roller 1.0's roller gaps (library.load); every other size a design choice; no load, speed or cycle claim; the "
            "cylinder, valve and sensing placed in a later version; no vendor file opened")
ORIGIN = ("the floor plane z = 0 at the centre of the base plate, which is the conveyor section's centre (conveyor-roller's origin): "
          "x across the conveyor (the transfer direction), y along it; the strips' tops at z 745 lowered, 765 raised")
COMMAND = "LIFTTRANSFER"
PARAMS = dict()
FILLET_R = 0.5                                   # the gate's radius: the furniture class's 1.0 reads 10 and 12 mm free-corner edges short (mech-r69, r101, r105)
CR = library.load("conveyor-roller")             # conveyor-roller 1.0: the section this unit stands in (one home for its figures)
TOP = CR.TOP                                     # 750: the rollers' tops, the conveyor's hand-off height
ROLL_UNDER = TOP - 2 * CR.ROLL_R                 # 700: the rollers' undersides
GAPS = tuple((CR.roller_y(i) + CR.roller_y(i + 1)) / 2 for i in (9, 10, 11))   # the gaps between rollers 9-10, 10-11, 11-12: y -75, 0, 75
GAP_W = CR.PITCH - 2 * CR.ROLL_R                 # 25: the clear gap between two rollers at their axes' height
ROLL_END = CR.W / 2 - CR.ROLL_GAP                # 245: the rollers' end faces, x +-245
TRAVEL = 20.0                                    # the lift: design choice (the strips end 15 above the rollers' tops)
LOW = 5.0                                        # the strips' tops 5 under the rollers' tops when lowered: design choice
STRIP_W, STRIP_L = 12.0, 470.0                   # strips 12 wide (6.5 clear of each roller in the 25 gap), x +-235 (10 inside the rollers' ends): design choice
PLATE_X, PLATE_Y, PLATE_T = 460.0, 170.0, 10.0   # the carriage plate 460 x 170 x 10: design choice (its ends 5 inside the strips' ends: no flush face across materials)
PLATE_TOP = ROLL_UNDER - TRAVEL - 10.0           # 670: the plate's top; raised 20 it stands 10 under the rollers' undersides
PLATE_Z = PLATE_TOP - PLATE_T                    # 660
STRIP_H = TOP - LOW - PLATE_TOP                  # 75: the strips, plate top to z 745
POST, POST_X = 40.0, 200.0                       # guide posts 40 x 40 at x +-200, from the base to the plate's underside: design choice
BASE_X, BASE_Y, BASE_T = 480.0, 240.0, 10.0      # base plate 480 x 240 x 10 on the floor: design choice
HOLE_X, HOLE_Y = 200.0, 90.0                     # 4 x M12 anchor holes at 400 x 180 (x +-200, y +-90), clear of the posts (y +-20): design choice
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S = "M-STEEL-7035"; B = "M-SILVER"                    # strips: bare steel, the library's bright-metal layer
    base = P.box(S, -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_T)                             # base plate on the floor
    for sx in (-1, 1):
        for sy in (-1, 1):
            P.hole(S, (sx * HOLE_X, sy * HOLE_Y, -1), (sx * HOLE_X, sy * HOLE_Y, BASE_T + 1), M12_D / 2, base)   # M12 anchor hole
    for sx, k in ((-1, "l"), (1, "r")):
        P.box(S, sx * POST_X - POST / 2, -POST / 2, BASE_T, POST, POST, PLATE_Z - BASE_T)              # guide post, base to the plate
        P.collider(f"post-{k}", sx * POST_X - POST / 2, -POST / 2, BASE_T, POST, POST, PLATE_Z - BASE_T)
    N = "node:lift|"
    P.box(N + S, -PLATE_X / 2, -PLATE_Y / 2, PLATE_Z, PLATE_X, PLATE_Y, PLATE_T)                    # the carriage plate, on the posts' tops
    for y in GAPS:
        P.box(N + B, -STRIP_L / 2, y - STRIP_W / 2, PLATE_TOP, STRIP_L, STRIP_W, STRIP_H)            # a transfer strip in a roller gap
    P.pivot("lift", "translate", (0, 0, PLATE_TOP), axis=(0, 0, 1), range=(0, TRAVEL))
    P.collider("base", -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_T)
    P.collider("carriage", -STRIP_L / 2, -PLATE_Y / 2, PLATE_Z, STRIP_L, PLATE_Y, PLATE_T + STRIP_H)
    for i in range(len(P)): P.radii[i] = FILLET_R                       # the gate reads each primitive's radius (fillet._radii), not FILLET_R:
    return P                                                            # run 1 filleted at the class's r 1.0 and read the 10 / 12 mm corners short

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
