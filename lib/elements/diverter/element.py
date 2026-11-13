#!/usr/bin/env python3
"""diverter: a swing-arm conveyor diverter, our own design (OPERATING.md 12, own designs; inventory row own_design "yes": "our own
design (core watch 2026-11-12, request mech-13): no diverter class on file; an arm on a pivot node on conveyor-roller's track, the
cylinder placed in a later version"). It stands on the floor beside a conveyor-roller section, outside its left side frame near the
section's upstream end: a base plate with four M12 anchor holes, a post, and one arm (node `arm`) that turns about the post's vertical
axis. At rest the arm lies along the track outside the left frame and goods pass by; turned 45 degrees it lies across the track and its
face guides the goods passing along y over to the right-hand side, where the assembly places the branch line. The arm's underside stays
10 above the rollers' tops over its whole sweep, so it never meets the section (figures read from conveyor-roller with library.load,
so the two cannot drift apart). The conveyor is placed by the assembly beside it; nothing of it is drawn here. The cylinder that turns
the arm, its valve and its sensing are placed in a later version (OPERATING.md 12: a host doesn't model holes for a part it places
later; no cylinder element is on file yet). Every size is a design choice. No load, speed or cycle claim. No vendor file was opened,
and no size is taken from the catalogue record that came with the folder (references/source.txt)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "diverter", "1.0", "furniture"
TITLE = "swing-arm diverter, own design, for a conveyor-roller 1.1 section: post on a 160 x 160 base with 4 x M12 anchor holes, arm 800 turning 0 to 45 degrees over the rollers"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; placed beside "
            "conveyor-roller 1.1's left side frame and above its rollers (library.load); every other size a design choice; no load, "
            "speed or cycle claim; the cylinder, valve and sensing placed in a later version; no vendor file opened")
ORIGIN = ("the floor plane z = 0 at the conveyor section's centre (conveyor-roller's origin): x across the conveyor, y along it, the "
          "goods travelling along +y; the arm's pivot axis vertical at x -340, y -650")
COMMAND = "DIVERTER"
PARAMS = dict()
FILLET_R = 0.5                                   # the gate's radius for every primitive (P.radii below): the furniture class's 1.0 reads short free-corner edges (mech-r69, r101, r106)
CR = library.load("conveyor-roller")             # conveyor-roller 1.1: the section this diverter stands beside (one home for its figures)
TOP = CR.TOP                                     # 750: the rollers' tops
FR_OUT = CR.W / 2 + CR.FR_W                      # 300: the side frames' outer faces, x +-300
FR_IN = CR.W / 2                                 # 250: the side frames' inner faces
END_Y = -CR.L / 2                                # -750: the section's upstream end
FOOT_Y = CR.SUP_Y + CR.PL_L / 2                  # 550: the section's foot plates' outer edges, y +-550 (they span x +-225..+-375)
PX, PY = -(FR_OUT + 40.0), END_Y + 100.0         # the pivot axis: x -340 (40 outside the left frame), y -650 (100 from the section's end): design choice
POST = 60.0                                      # post 60 x 60, centred on the pivot axis, x -370..-310 (10 clear of the frame): design choice
HUB_R, HUB_Z0, HUB_Z1 = 40.0, TOP, TOP + 110.0   # the arm's hub Ø80, z 750 to 860, resting on the post's top: design choice
ARM_L, ARM_T = 800.0, 10.0                       # the arm 800 from the pivot axis, 10 thick: design choice (turned 45 its tip's outer corner stands 21 inside the right frame)
ARM_Z0, ARM_Z1 = TOP + 10.0, HUB_Z1              # the arm's face z 760 to 860: 10 above the rollers' tops, 20 above the frames' tops (740): design choice
SWING = 45.0                                     # the arm's turn, degrees, toward +x: design choice
BASE, BASE_T = 160.0, 12.0                       # base plate 160 x 160 x 12 centred on the pivot (y -730..-570: 20 clear of the foot plates at -550): design choice
HOLE = 55.0                                      # 4 x M12 anchor holes at 110 x 110 (pivot +-55), clear of the post (+-30): design choice
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

TIP_X = PX + ARM_L * math.sin(math.radians(SWING)) + ARM_T / 2 * math.cos(math.radians(SWING))   # the arm's tip, outer corner, turned 45: x 229.2
assert TIP_X < FR_IN, TIP_X                      # turned, the tip stays inside the right frame's inner face
assert -(PY - BASE / 2) < CR.L / 2 and -(PY + BASE / 2) >= FOOT_Y + 20.0  # the base plate inside the section's end and 20 clear of its foot plates

def build():
    P = Prims(); S = "M-STEEL-7035"; Y = "M-YELLOW"                    # the arm in safety yellow: a moving part (appearance only)
    base = P.box(S, PX - BASE / 2, PY - BASE / 2, 0, BASE, BASE, BASE_T)                              # base plate on the floor
    for sx in (-1, 1):
        for sy in (-1, 1):
            P.hole(S, (PX + sx * HOLE, PY + sy * HOLE, -1), (PX + sx * HOLE, PY + sy * HOLE, BASE_T + 1), M12_D / 2, base)   # M12 anchor hole
    P.box(S, PX - POST / 2, PY - POST / 2, BASE_T, POST, POST, TOP - BASE_T)                          # post, base to z 750
    N = "node:arm|"
    P.cyl(N + Y, (PX, PY, HUB_Z0), (PX, PY, HUB_Z1), HUB_R)                                           # hub, on the post's top
    P.box(N + Y, PX - ARM_T / 2, PY, ARM_Z0, ARM_T, ARM_L, ARM_Z1 - ARM_Z0)                           # arm, along +y at rest
    P.pivot("arm", "rotate", (PX, PY, HUB_Z0), axis=(0, 0, -1), range=(0, SWING), unit="deg")        # turns toward +x across the track
    P.collider("base", PX - BASE / 2, PY - BASE / 2, 0, BASE, BASE, BASE_T)
    P.collider("post", PX - POST / 2, PY - POST / 2, BASE_T, POST, POST, TOP - BASE_T)
    P.collider("paddle", PX - HUB_R, PY - HUB_R, HUB_Z0, 2 * HUB_R, ARM_L + HUB_R, HUB_Z1 - HUB_Z0)  # hub and arm as one box, at rest
    for i in range(len(P)): P.radii[i] = FILLET_R                       # the gate reads each primitive's radius (fillet._radii), not FILLET_R
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
