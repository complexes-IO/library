#!/usr/bin/env python3
"""jaw-prism-125: generic prism clamping jaw for a machine vice, our own vendor-neutral design of the ETIM 10.0 class EC004297
(Clamping jaw), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the class once no
inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md). A steel jaw plate the size of vise-machine
1.0's jaw plates (125 x 40 x 18, read from vise-machine with library.load: one home for the seat), with a vertical 90 degree V-groove
in its clamping face, so a tube or a round bar standing upright is held on both flanks. It takes the place of either of the vice's
plain jaw plates. Two M8 tapped holes in its back face take the screws that hold it to the vice's jaw block from behind: drawn at the
thread's minor diameter, derived (derive.thread(8.0, 1.25): ISO 68-1, ISO 965-1 6H D1 6.6468); the screws (socket head cap screws,
ISO 4762, a common part not built yet) and the jaw block's clearance holes are the host's, placed later. One fixed body, no moving
node, no terminal. The class values (spec.md, "Class values") are design inputs; every other size is a design choice. No clamping
force is claimed. No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "jaw-prism-125", "1.1", "device"
TITLE = "prism clamping jaw, generic, 125 x 40 x 18 for vise-machine's jaw seat, vertical 90 degree V-groove 12 wide, 2 x M8 tapped from behind"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic clamping jaw (ETIM 10.0 EC004297); class values are design inputs (spec.md); the seat 125 x 40 "
            "x 18 read from vise-machine 1.0 (library.load); 2 x M8 tapped holes, the thread's figures derived (ISO 68-1, ISO 965-1), "
            "the screws the host's; every other size a design choice; no clamping force claimed; no vendor file opened")
ORIGIN = ("the clamping face x = 0 (the jaw's +x face, toward the work); the plate's underside z = 0; the plate's centre y = 0; the "
          "back face (the seat on the vice's jaw block) at x = -18; the V-groove's apex line at x = -6, y = 0")
COMMAND = "JAWPRISM"
PARAMS = dict()

VM = library.load("vise-machine")    # vise-machine 1.0: the vice whose jaw seat this plate fills (one home for the plate's size)
W, H, T = VM.JAW_W, VM.JAW_H, VM.JAW_T    # 125 wide (y) x 40 high (z) x 18 thick (x): vise-machine's jaw plate
V_DEPTH = 6.0                        # the V-groove 6 deep, 90 degrees, so 12 wide at the face: design choice
TAP_D1 = 6.6468                      # M8 tapped holes drawn at the thread's minor diameter D1 (6H min): derived: derive.thread(8.0, 1.25) (ISO 68-1; ISO 965-1 clause 10)
TAP_DEPTH = 12.0                     # each tapped hole 12 deep from the back face (1.5 x the nominal diameter): design choice
TAP_Y, TAP_Z = 40.0, 20.0            # the tapped holes at y +-40 on the plate's mid-height: design choice
STEEL = "M-SILVER"
S = math.sqrt(0.5)

R_MAX = V_DEPTH / S                  # a round seats on both flanks while its contact points r*cos45 stay inside the groove: r <= 8.49
R_MIN = V_DEPTH / (1 + math.sqrt(2)) # and stands out past the clamping face while -6 + r*(sqrt2 + 1) > 0: r > 2.49
assert (W, H, T) == (125.0, 40.0, 18.0)                                  # the seat as vise-machine 1.0 gives it
assert 2 * R_MIN < 5.0 and 2 * R_MAX > 16.0                              # rounds Ø5 to Ø16 seat on both flanks and stand proud
assert T - TAP_DEPTH >= V_DEPTH and TAP_Y - TAP_D1 / 2 > V_DEPTH + 25    # 6 of wall in front of each hole; the holes far from the groove
assert W / 2 - TAP_Y - TAP_D1 / 2 >= 15.0 and TAP_Z - TAP_D1 / 2 >= 15.0  # 15 of steel round each hole to the plate's edges


def build():
    P = Prims()
    plate = P.box(STEEL, -T, -W / 2, 0, T, W, H)                                                        # the jaw plate
    P.cut(STEEL, (-V_DEPTH, 0, -1), (S, S, 0), (0, 0, 1), (S, -S, 0), 20.0, H + 2, 20.0, plate)          # vertical 90 degree V-groove
    for sy in (-1, 1):                                                                                  # M8 tapped from behind, 12 deep
        P.hole(STEEL, (-T - 1, sy * TAP_Y, TAP_Z), (-T + TAP_DEPTH, sy * TAP_Y, TAP_Z), TAP_D1 / 2, plate)
    P.collider("jaw", -T, -W / 2, 0, T, W, H)
    return P


PREVIEWS = [dict(name="three-quarter", az=60, el=25), dict(name="back", az=230, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
