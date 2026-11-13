#!/usr/bin/env python3
"""platen: belt grinder platen, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). The flat steel
plate a belt grinder's abrasive belt runs over between its contact wheel and its idler (grinder-belt in lib/machines-factory.txt
line 111: frame-welded, motor-iec, belt-abrasive, platen, wheel-contact, tensioner-belt, guard-panel, ...): the work is pressed
against the belt where the platen backs it, so the belt grinds flat. A ground face plate 60 x 250 x 10 (the belt runs on its front
face, along z), held 30 off the machine by a stand-off block on a mounting flange 130 x 80 x 10 with 2 x M8 clearance holes, ISO 273
medium (lib/standards/holes.csv), outside the face plate's outline so the screws are reached from the front. One fixed body, no
node. belt-abrasive is not built and no belt-size standard is on file, so the face is sized for a belt up to 50 wide as a design
choice; the fit is checked when the belt is on file. Every size is a design choice. No load, wear, flatness or safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "platen", "1.0", "furniture"
TITLE = "belt grinder platen, face 60 x 250 x 10, stand-off 30, mounting flange 130 x 80 x 10 with 2 x M8 holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; mounting holes M8 in ISO 273 medium holes; "
            "the belt's width not on file, the face sized for a belt up to 50 wide as a design choice; every size a design choice; "
            "no load, wear, flatness or safety claim")
ORIGIN = ("the mounting flange's back face y = 0 (the grinder frame's face) at the flange's centre x = 0, z = 0; the belt runs "
          "along z over the face plate's front face at y = -50; x across the belt")
COMMAND = "PLATEN"
PARAMS = dict()
FACE_W, FACE_L, FACE_T = 60.0, 250.0, 10.0      # face plate 60 wide (x) x 250 long (z) x 10 thick: design choice (a belt up to 50 wide)
STAND_W, STAND_H, STAND_D = 40.0, 70.0, 30.0    # stand-off block 40 (x) x 70 (z) x 30 deep (y): design choice
FL_W, FL_H, FL_T = 130.0, 80.0, 10.0            # mounting flange 130 (x) x 80 (z) x 10 thick: design choice
HOLE_X = 50.0                                   # 2 x M8 at x = +-50, z = 0 (100 apart, 20 clear of the face plate's sides): design choice
M8_D = 9.0                                      # M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S, B = "M-SILVER", "M-STEEL-7035"                  # ground face plate; painted bracket
    y_stand = -FL_T - STAND_D                                       # the stand-off's front face, y -40
    flange = P.box(B, -FL_W / 2, -FL_T, -FL_H / 2, FL_W, FL_T, FL_H)                                     # mounting flange
    for sx in (-1, 1):
        x = sx * HOLE_X
        P.hole(B, (x, -FL_T - 1, 0), (x, 1, 0), M8_D / 2, flange)                                        # 2 x M8 clearance
    P.box(B, -STAND_W / 2, y_stand, -STAND_H / 2, STAND_W, STAND_D, STAND_H)                              # stand-off block
    P.box(S, -FACE_W / 2, y_stand - FACE_T, -FACE_L / 2, FACE_W, FACE_T, FACE_L)                         # face plate (the belt's back-up)
    P.collider("face", -FACE_W / 2, y_stand - FACE_T, -FACE_L / 2, FACE_W, FACE_T, FACE_L)
    P.collider("bracket", -FL_W / 2, y_stand, -FL_H / 2, FL_W, STAND_D + FL_T, FL_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="side", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
