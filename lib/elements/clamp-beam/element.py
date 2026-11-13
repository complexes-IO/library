#!/usr/bin/env python3
"""clamp-beam: the clamping beam of a sheet folder, our own design (OPERATING.md 12, own designs; inventory row own_design "yes":
"clamping beam of a sheet folder"; lib/machines-factory.txt line 24, folder-sheet). It holds the sheet down on beam-folding's bed
along the bend line while the folding beam swings up. A portal (two posts standing on beam-folding's cheeks, a crossbar over them)
is the fixed body; the clamping beam (node `clamp`) lifts between the posts, 0 to 150, to open the jaw. Its nose is cut back at 45
degrees from the bend line, so the folding beam reaches 135 degrees against it. Its length, the posts' places and the bed's depth
are read from beam-folding (library.load), so the two cannot drift apart. The beam's guides on the posts, its lift (eccentric or
cylinder), the nose's segments and a crowning are not drawn. Every other size is a design choice. No clamping force claim. No
vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "clamp-beam", "1.0", "furniture"
TITLE = "clamping beam of a sheet folder, 1000 long, nose relieved 45 degrees, lifts 150 in a portal on beam-folding 1.0's cheeks"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; length, posts and bed read from beam-folding "
            "(library.load); every other size a design choice; no clamping force claim; no vendor file opened")
ORIGIN = ("beam-folding's origin: the bend line's centre, x = 0 midway along it, y = 0 the bed's front face, z = 0 the bed's top "
          "face (the nose's tip rests on it); the bend line along x; the clamp lifts along +z")
COMMAND = "CLAMPBEAM"
PARAMS = dict()
BF = library.load("beam-folding")                # beam-folding 1.0: the bend line, the bed and the cheeks (one home for the figures)
HALF = BF.HALF                                   # the nose as long as the folding beam, x +-500
NOSE_D = BF.BED_D                                # the nose's underside as deep as the bed, y 0..400
NOSE_H = 200.0                                   # nose z 0..200, its front face cut back at 45 degrees from the bend line: design choice
POST_X0, POST_T = BF.CHEEK_X0, BF.CHEEK_T        # posts over the cheeks, x +-560..+-600
POST_Z0 = BF.CHEEK_TOP                           # posts stand on the cheeks' tops, z 60
POST_Y0, POST_Y1 = -50.0, 400.0                  # posts y -50..400: design choice
UP_Y0, UP_Z0, UP_Z1 = 200.0, NOSE_H, 400.0       # upper beam y 200..400, z 200..400, on the nose's top land: design choice
UP_HALF = POST_X0 - 5.0                          # the upper beam 5 clear of the posts, x +-555 (the guide's place)
OPEN = 150.0                                     # lifts 0..150 (the jaw's opening): design choice
BAR_Z0, BAR_T = 760.0, 60.0                      # crossbar on the posts' tops, z 760..820, y 200..400: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"
    C = f"node:clamp|{S}"
    nose = P.box(C, -HALF, -20.0, 0, 2 * HALF, NOSE_D + 20.0, NOSE_H)                                # nose (the node's first box)
    a = math.sqrt(0.5); t0 = 30.0                                                                    # the cut: everything above y = z
    o = (-HALF - 1, -t0 * a, -t0 * a)
    P.cut(C, o, (1, 0, 0), (0, a, a), (0, -a, a), 2 * HALF + 2, NOSE_H * math.sqrt(2) + t0 + 30.0, NOSE_H + 50.0, nose)
    P.box(C, -UP_HALF, UP_Y0, UP_Z0, 2 * UP_HALF, NOSE_D - UP_Y0, UP_Z1 - UP_Z0)                     # upper beam on the nose's land
    for sx in (-1, 1):
        x0 = POST_X0 if sx > 0 else -POST_X0 - POST_T
        P.box(S, x0, POST_Y0, POST_Z0, POST_T, POST_Y1 - POST_Y0, BAR_Z0 - POST_Z0)                  # post on beam-folding's cheek
    P.box(S, -POST_X0 - POST_T, UP_Y0, BAR_Z0, 2 * (POST_X0 + POST_T), NOSE_D - UP_Y0, BAR_T)        # crossbar
    P.pivot("clamp", "translate", (0, 0, 0), axis=(0, 0, 1), range=(0, OPEN))
    P.collider("clamp-body", -UP_HALF, 0, 0, 2 * UP_HALF, NOSE_D, UP_Z1)
    for n, x0 in (("post-l", -POST_X0 - POST_T), ("post-r", POST_X0)):
        P.collider(n, x0, POST_Y0, POST_Z0, POST_T, POST_Y1 - POST_Y0, BAR_Z0 - POST_Z0)
    P.collider("crossbar", -POST_X0 - POST_T, UP_Y0, BAR_Z0, 2 * (POST_X0 + POST_T), NOSE_D - UP_Y0, BAR_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
