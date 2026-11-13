#!/usr/bin/env python3
"""sign-iso7010: safety sign plate, our own vendor-neutral design of the ETIM 10.0 class EC001777 (Warning/signing plate), built
unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "sign-iso7010", own_design yes, etim EC001777, systems
racks-storage, storage-steel, safety-equipment). A rectangular 200 x 300 x 2 aluminium plate screwed to a wall, a rack upright or a
guard, with two printed fields on its face: a 160 x 160 symbol field above and a 160 x 60 text field below, both blank (the class
values Symbol, Literal imprint and Colour are "not stated": ISO 7010's symbols and ISO 3864's colours are in lib/standards/sources.csv
as "to get"; the sign carries no safety message until a version prints one). Four Ø4.5 clearance holes (M4, ISO 273 medium) at the
corners for the host's screws. One fixed body, no moving node, no terminal. The class values (spec.md, "Class values") are design
inputs; every size is a design choice. No safety claim; no vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "sign-iso7010", "1.0", "plate"
TITLE = "safety sign plate 200 x 300 x 2, generic, aluminium, blank symbol and text fields, 4 x Ø4.5 corner holes (M4, ISO 273)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic warning/signing plate (ETIM 10.0 EC001777), 200 x 300 x 2 aluminium with a blank 160 x 160 symbol "
            "field and a blank 160 x 60 text field; class values are design inputs (spec.md); corner holes ISO 273 medium for M4; every "
            "size a design choice; no safety message, symbol or colour claimed; no vendor file opened")
ORIGIN = ("the mounting face plane (y = 0, the wall's face) at the plate's centre: x = 0 on the vertical centre line, z = 0 on the "
          "horizontal centre line; the plate lies toward -y (y -2 to 0), its printed fields 0.1 proud of its face at y -2.1; width "
          "along x, height along z")
COMMAND = "SIGNPLATE"
PARAMS = dict()
W, H, T = 200.0, 300.0, 2.0                    # the plate: class values Width, Height, Thickness (design choices: a portrait plate a symbol and a line of text fit)
HOLE_D = 4.5                                   # 4 x M4 clearance medium (ISO 273 H13, lib/standards/holes.csv): the host's screws
HOLE_X, HOLE_Z = 90.0, 140.0                   # the holes 10 in from each edge: pattern 180 (x) x 280 (z)
FIELD_T = 0.1                                  # the printed fields stand 0.1 proud of the face (tag-plate 1.0's text fields): a print, not a part
SYM = (-80.0, -30.0, 160.0, 160.0)             # symbol field x, z, w, h: 160 square, 20 under the top edge
TXT = (-80.0, -120.0, 160.0, 60.0)             # text field 160 x 60, 30 above the bottom edge, 30 under the symbol field

def build():
    P = Prims(); A = "M-ALU-ANOD"; F = "M-WHITE-PA"
    pl = P.box(A, -W / 2, -T, -H / 2, W, T, H)                                                        # the plate, y -2..0
    for sx in (-1, 1):
        for sz in (-1, 1):
            P.hole(A, (sx * HOLE_X, -T - 1, sz * HOLE_Z), (sx * HOLE_X, 1, sz * HOLE_Z), HOLE_D / 2, pl)   # Ø4.5 through, along y
    for (x, z, w, h) in (SYM, TXT):
        P.box(F, x, -T - FIELD_T, z, w, FIELD_T, h)                                                  # a blank printed field on the face
    P.collider("sign", -W / 2, -T - FIELD_T, -H / 2, W, T + FIELD_T, H)
    return P

PREVIEWS = [dict(name="face", az=262, el=15), dict(name="three-quarter", az=230, el=25)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
