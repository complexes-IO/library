#!/usr/bin/env python3
"""chuck-magnetic-250x125: generic magnetic chucking block (the switchable permanent-magnet block a grinder's or a mill's table carries,
holding steel work on its top face), our own vendor-neutral design of the ETIM 10.0 class EC004300 (Magnetic chucking system; its
synonyms name the magnet clamp block and plate), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory
mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md). A steel housing
250 x 125 x 75 whose top face is the one clamping surface, a 15 x 15 ledge along each long side at its foot for the table's clamps
(claw-clamping is one), and a hand lever (node `lever`) on the +x end face that turns 180 degrees to switch the magnets on. The
magnet system inside (its poles, its turning core) is internal mechanism the twin doesn't read: not drawn, not claimed; the twin
reads the lever's state. The class values (spec.md, "Class values") are design inputs; every size below is a design choice. No
holding force is designed or claimed. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "chuck-magnetic-250x125", "1.0", "device"
TITLE = "magnetic chucking block, generic, 250 x 125 x 75, one clamping face, switchable by a hand lever turning 180 degrees"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic magnetic chucking system (ETIM 10.0 EC004300), a switchable permanent-magnet block; class "
            "values are design inputs (spec.md); the magnet system inside not drawn or claimed; every size a design choice; no "
            "holding force claimed; no vendor file opened")
ORIGIN = ("the housing's underside (the seat on the machine table) z = 0; the housing's centre x = 0, y = 0; the clamping face "
          "(the top) at z = 75; the lever on the +x end face, turning about the line y = 0, z = 40")
COMMAND = "CHUCKMAG"
PARAMS = dict()

L, W, H = 250.0, 125.0, 75.0                     # housing x -125..125, y -62.5..62.5, z 0..75: the class values length, width, height
LEDGE_W, LEDGE_H = 15.0, 15.0                    # a ledge 15 x 15 along each long side at the foot, y +-62.5..77.5: design choice
AX_Z = 40.0                                      # the lever's axis: y = 0, z = 40 on the +x end face: design choice
BORE_R, BORE_D = 6.0, 30.0                       # Ø12 x 30 deep in the end face for the lever's shaft (features.csv, own)
SH_R = 5.0                                       # the lever's shaft Ø10: 1 clear round in its bore
HUB_GAP, HUB_R, HUB_T = 1.0, 14.0, 12.0          # hub Ø28 x 12, 1 clear of the end face: x 126..138
ARM_X0, ARM_T, ARM_W, ARM_L = 128.0, 8.0, 12.0, 80.0   # arm x 128..136, 12 high, from the axis to y 80 at rest (switched off)
KNOB_Y, KNOB_R, KNOB_L = 72.0, 7.0, 20.0         # knob Ø14 x 20 along +x at y 72: x 136..156
SWING = 180.0                                    # the lever turns 180 degrees, over the top, from +y (off) to -y (on)
STEEL, GRIP = "M-SILVER", "M-BLACK-PA"

X1 = L / 2
assert BORE_R - SH_R == 1.0 and HUB_GAP == 1.0                   # the node 1 clear of the housing everywhere
assert ARM_L > W / 2 + LEDGE_W                                     # off, the knob stands beyond the ledge (y 72 vs 77.5: in x it is clear)
assert ARM_X0 > X1 + HUB_GAP                                       # the arm turns in a plane 3 in front of the end face: nothing fixed there
assert AX_Z - ARM_W / 2 > LEDGE_H and AX_Z + HUB_R < H             # the hub and arm at rest between the ledge's top and the clamping face


def build():
    P = Prims()
    hs = P.box(STEEL, -X1, -W / 2, 0, L, W, H)                                                         # housing, top = clamping face
    P.hole(STEEL, (X1 + 1, 0, AX_Z), (X1 - BORE_D, 0, AX_Z), BORE_R, hs)                               # lever shaft bore Ø12 x 30
    for sy in (-1, 1):
        y0 = W / 2 if sy > 0 else -W / 2 - LEDGE_W
        P.box(STEEL, -X1, y0, 0, L, LEDGE_W, LEDGE_H)                                                  # ledge for the table's clamps
    N = lambda m: f"node:lever|{m}"
    P.cyl(N(STEEL), (X1 - BORE_D + 1, 0, AX_Z), (X1 + HUB_GAP, 0, AX_Z), SH_R)                          # shaft Ø10 in the bore
    P.cyl(N(STEEL), (X1 + HUB_GAP, 0, AX_Z), (X1 + HUB_GAP + HUB_T, 0, AX_Z), HUB_R)                    # hub Ø28
    P.box(N(STEEL), ARM_X0, 0, AX_Z - ARM_W / 2, ARM_T, ARM_L, ARM_W)                                   # arm to y 80
    P.cyl(N(GRIP), (ARM_X0 + ARM_T, KNOB_Y, AX_Z), (ARM_X0 + ARM_T + KNOB_L, KNOB_Y, AX_Z), KNOB_R)     # knob
    P.pivot("lever", "rotate", (X1, 0, AX_Z), axis=(1, 0, 0), range=(0, SWING), unit="deg")            # +y (off) over the top to -y (on)
    P.collider("housing", -X1, -W / 2, 0, L, W, H)
    P.collider("ledges", -X1, -W / 2 - LEDGE_W, 0, L, W + 2 * LEDGE_W, LEDGE_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
