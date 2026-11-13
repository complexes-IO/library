#!/usr/bin/env python3
"""carriage: the carriage of a conventional lathe, with its cross slide, our own design (OPERATING.md 12, own designs; inventory
row own_design "yes": "lathe carriage with cross slide"). Two way shoes sit on bed-cast's two flat ways and carry a saddle plate
across the bed; an apron hangs from the saddle's front edge in front of the bed's body; on the saddle's top face the cross slide
(node `cross-slide`, translate along +y, toward the spindle axis and past it) carries the tool post a BOM puts on its top face.
The carriage's own travel along the bed (x) is the machine's (its leadscrew), between the elements, so the carriage has no node
for it. The shoes' spacing and width are read from bed-cast itself (library.load), so the two cannot drift apart. Saddle and
apron are drawn by their outsides. The apron's gears and handwheels, the cross slide's screw, dovetail and gib, the compound rest
and the wipers are not drawn. Every other size is a design choice. No load rating, no accuracy claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "carriage", "1.0", "furniture"
TITLE = "lathe carriage 400 x 600 x 380, two shoes on bed-cast's ways, apron, cross slide 200 x 220 with 200 of travel"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; the shoes on bed-cast 1.0's ways, every other "
            "size a design choice; no load rating, no accuracy claim; no vendor file opened")
ORIGIN = ("bed-cast's ways' top plane z = 0 (the carriage's seat) at the carriage's centre x = 0, y = 0; it slides along x, the "
          "bed's length; front (the operator's side, the apron) toward -y; the cross slide's top face (the tool post's seat) at "
          "z = 160")
COMMAND = "CARRIAGE"
PARAMS = dict()
BED = library.load("bed-cast")                    # bed-cast 1.0: the ways it sits on (one home for the figure)
SHOE_Y, SHOE_W = BED.WAY_Y, BED.WAY_W             # shoe centres at y +-170, each as wide as the bed's way, 80
SHOE_L, SHOE_H = 300.0, 40.0                      # way shoes 300 along the bed, 40 high (z 0..40): design choice
SAD_Y0, SAD_Y1 = -280.0, 280.0                    # saddle plate across the bed, y -280..280: design choice
SAD_TOP = 100.0                                   # saddle plate z 40..100: design choice
APR_L, APR_T = 400.0, 40.0                        # apron 400 along the bed (x -200..200), 40 thick (y -320..-280): design choice
APR_BOT = -220.0                                  # apron down to z -220 (210 above the floor on bed-cast): design choice
CS_W, CS_L, CS_H = 200.0, 220.0, 60.0             # cross slide 200 along x, 220 along y, 60 high (z 100..160): design choice
CS_Y0 = -240.0                                    # cross slide at rest y -240..-20 (fully toward the operator): design choice
TRAVEL = 200.0                                    # cross slide travel 0..200 along +y (y -40..180 at the end): design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                   # the slide: bare machined steel, the library's bright-metal layer
    for sy in (-1, 1):
        P.box(S, -SHOE_L / 2, sy * SHOE_Y - SHOE_W / 2, 0, SHOE_L, SHOE_W, SHOE_H)                  # way shoe, on bed-cast's way
    P.box(S, -SHOE_L / 2, SAD_Y0, SHOE_H, SHOE_L, SAD_Y1 - SAD_Y0, SAD_TOP - SHOE_H)                 # saddle plate
    P.box(S, -APR_L / 2, SAD_Y0 - APR_T, APR_BOT, APR_L, APR_T, SAD_TOP - APR_BOT)                  # apron, in front of the bed
    P.box(f"node:cross-slide|{W}", -CS_W / 2, CS_Y0, SAD_TOP, CS_W, CS_L, CS_H)                      # cross slide
    P.pivot("cross-slide", "translate", (0, CS_Y0 + CS_L / 2, SAD_TOP + CS_H), axis=(0, 1, 0), range=(0, TRAVEL))
    P.collider("carriage", -SHOE_L / 2, SAD_Y0, 0, SHOE_L, SAD_Y1 - SAD_Y0, SAD_TOP)
    P.collider("apron", -APR_L / 2, SAD_Y0 - APR_T, APR_BOT, APR_L, APR_T, SAD_TOP - APR_BOT)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="end", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
