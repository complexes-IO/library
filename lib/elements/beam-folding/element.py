#!/usr/bin/env python3
"""beam-folding: the folding beam of a sheet folder, our own design (OPERATING.md 12, own designs; inventory row own_design "yes":
"folding beam of a sheet folder"; lib/machines-factory.txt line 24, folder-sheet: frame-welded, beam-folding, clamp-beam, ...).
The sheet lies on a fixed bed (the lower beam); the clamping beam (clamp-beam, its own element) holds it down along the bend line,
the bed's top front edge; the folding beam (node `fold`) in front of the bed swings up about that line and folds the part of the
sheet that sticks out, 0 to 135 degrees. The bed and the two end cheeks that carry the beam's pins are drawn here, because the
bend line is the edge the bed and the folding beam share: one home for it. Each cheek has a square window round the pin (the
bearing in it is not drawn); the bed's top front corners are notched where the pins pass. The drive (folder-sheet places two
hyd-cylinders), its lugs, the stops, an angle scale and the sheet-thickness adjustment of the axis are not drawn. Every size is a
design choice. No bending capacity (sheet thickness, length, tensile strength), force or accuracy claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "beam-folding", "1.0", "furniture"
TITLE = "folding beam of a sheet folder, working length 1000, folds 0 to 135 degrees about the bend line, on its bed and two end cheeks"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every size "
            "a design choice; no bending capacity, force or accuracy claim; no vendor file opened")
ORIGIN = ("the bend line's centre: x = 0 midway along the working length, y = 0 the bed's front face, z = 0 the bed's top face (the "
          "sheet's underside); the bend line along x; the folding beam in front (-y), the bed behind (+y)")
COMMAND = "FOLDBEAM"
PARAMS = dict()
HALF = 500.0                                     # working length 1000 (x +-500): the folding beam's and clamp-beam's length: design choice
BED_D, BED_H = 400.0, 200.0                      # bed (lower beam) 400 deep (y 0..400), 200 high (z -200..0): design choice
FOLD_GAP = 2.0                                   # the folding beam's back face 2 in front of the bed's front face: design choice
FOLD_D, FOLD_H = 150.0, 150.0                    # folding beam 150 x 150 (y -152..-2, z -150..0), its top face the bed's plane: design choice
FOLD_MAX = 135.0                                 # folds 0..135 degrees about the bend line: design choice (clamp-beam's 45-degree nose relief)
PIN_R, PIN_X1 = 25.0, 620.0                      # pins Ø50 on the bend line, x +-500..+-620 (20 proud of the cheeks): design choice
CHEEK_X0, CHEEK_T = 560.0, 40.0                  # cheeks 40 thick at x +-560..+-600, the bed's ends against them: design choice
CHEEK_Y0, CHEEK_Y1 = -250.0, 450.0               # cheeks y -250..450: design choice
CHEEK_Z0, CHEEK_TOP = -250.0, 60.0               # cheeks z -250..60; clamp-beam's posts stand on their tops: design choice
WIN = 35.0                                       # square window 70 x 70 round each pin, 10 clear: design choice
NOTCH = 35.0                                     # the bed's top front corners notched 35 x 35 over x +-500..+-560, 10 clear of the pins

def build():
    P = Prims(); S = "M-STEEL-7035"
    F = f"node:fold|{S}"
    P.box(F, -HALF, -FOLD_GAP - FOLD_D, -FOLD_H, 2 * HALF, FOLD_D, FOLD_H)                          # folding beam (the node's first box)
    for sx in (-1, 1):
        P.cyl(F, (sx * HALF, 0, 0), (sx * PIN_X1, 0, 0), PIN_R)                                     # pin on the bend line
    bed = P.box(S, -CHEEK_X0, 0, -BED_H, 2 * CHEEK_X0, BED_D, BED_H)                                 # bed, between the cheeks
    for sx in (-1, 1):
        x0 = HALF if sx > 0 else -CHEEK_X0 - 1
        P.cutbox(S, x0, -1, -NOTCH, CHEEK_X0 - HALF + 1, NOTCH + 1, NOTCH + 1, bed)                   # notch where the pin passes
    for sx in (-1, 1):
        x0 = CHEEK_X0 if sx > 0 else -CHEEK_X0 - CHEEK_T
        ch = P.box(S, x0, CHEEK_Y0, CHEEK_Z0, CHEEK_T, CHEEK_Y1 - CHEEK_Y0, CHEEK_TOP - CHEEK_Z0)     # end cheek
        P.cutbox(S, x0 - 1, -WIN, -WIN, CHEEK_T + 2, 2 * WIN, 2 * WIN, ch)                           # window round the pin
    P.pivot("fold", "rotate", (0, 0, 0), axis=(-1, 0, 0), range=(0, FOLD_MAX), unit="deg")       # about -x: the beam's front rises
    P.collider("fold-beam", -HALF, -FOLD_GAP - FOLD_D, -FOLD_H, 2 * HALF, FOLD_D, FOLD_H)
    P.collider("bed", -CHEEK_X0, 0, -BED_H, 2 * CHEEK_X0, BED_D, BED_H)
    for n, x0 in (("cheek-l", -CHEEK_X0 - CHEEK_T), ("cheek-r", CHEEK_X0)):
        P.collider(n, x0, CHEEK_Y0, CHEEK_Z0, CHEEK_T, CHEEK_Y1 - CHEEK_Y0, CHEEK_TOP - CHEEK_Z0)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
