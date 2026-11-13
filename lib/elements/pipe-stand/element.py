#!/usr/bin/env python3
"""pipe-stand: a roller pipe stand, our own design (OPERATING.md 12, own designs; inventory row own_design "yes": "roller pipe
stand"; lib/machines-factory.txt line 16 places it at the pipe-cutter). A pipe being fed along y rests on two parallel rollers in
the stand's head and rolls on them. A base plate carries a square column (drawn by its outside), a head plate on the column's top,
and four bearing blocks on the head plate, two to each roller. The rollers are nodes `roller-1` and `roller-2`, each spinning
freely about its own axis (along y). The axles and bearings are not drawn: the rollers stand 10 clear of the blocks at each end.
No height adjustment: the stand is one height. One fixed body around the two nodes; no hole: the stand's fixing to the floor, if
any, is the assembly's. Every size is a design choice. No load rating, no pipe size range claim, no stability claim. No vendor
file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "pipe-stand", "1.0", "furniture"
TITLE = "roller pipe stand, two free rollers Ø80 x 200 at 180 centres, roller axes 780 above the floor, base plate 600 x 400"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; every size a design choice; no load rating, "
            "no pipe size claim, no stability claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the base plate x = 0, y = 0; the pipe runs along y over the stand, the rollers' "
          "axes along y at x -90 and +90, z 780")
COMMAND = "PIPESTAND"
PARAMS = dict()
BASE_W, BASE_D, BASE_T = 600.0, 400.0, 20.0     # base plate 600 (x) by 400 (y), 20 thick (z 0..20): design choice
COL = 80.0                                       # column 80 x 80 square tube, drawn by its outside: design choice
HEAD_Z = 700.0                                   # head plate's underside (the column's top): design choice
HEAD_W, HEAD_D, HEAD_T = 400.0, 260.0, 20.0      # head plate 400 (x) by 260 (y), 20 thick (z 700..720), its y ends flush
                                                 # with the blocks' outer faces: design choice
ROLL_X = 90.0                                    # roller axes at x -90 and +90 (180 apart, 100 clear between them): design choice
ROLL_Z = 780.0                                   # roller axes' height above the floor: design choice
ROLL_R, ROLL_L = 40.0, 200.0                     # rollers Ø80, 200 long (y -100..100): design choice
BLK_W, BLK_T = 60.0, 20.0                        # bearing blocks 60 (x) by 20 (y), z 720..800, centred on the roller's axis
BLK_TOP = 800.0                                  # the blocks' top, 20 above the axis: design choice
END_GAP = 10.0                                   # each roller's end face 10 clear of its block (the axle is not drawn)

def build():
    P = Prims(); S = "M-STEEL-7035"; R = "M-SILVER"                     # rollers: bright steel, the library's bright-metal layer
    P.box(S, -BASE_W / 2, -BASE_D / 2, 0, BASE_W, BASE_D, BASE_T)                                     # base plate
    P.box(S, -COL / 2, -COL / 2, BASE_T, COL, COL, HEAD_Z - BASE_T)                                    # column
    P.box(S, -HEAD_W / 2, -HEAD_D / 2, HEAD_Z, HEAD_W, HEAD_D, HEAD_T)                                 # head plate
    yb = ROLL_L / 2 + END_GAP                                                                          # blocks' inner faces y +-110
    for i, sx in enumerate((-1, 1), 1):
        x = sx * ROLL_X
        for y0 in (-yb - BLK_T, yb):
            P.box(S, x - BLK_W / 2, y0, HEAD_Z + HEAD_T, BLK_W, BLK_T, BLK_TOP - HEAD_Z - HEAD_T)       # bearing block
        n = f"roller-{i}"
        P.cyl(f"node:{n}|{R}", (x, -ROLL_L / 2, ROLL_Z), (x, ROLL_L / 2, ROLL_Z), ROLL_R)              # free roller
        P.pivot(n, "rotate", (x, -ROLL_L / 2, ROLL_Z), axis=(0, 1, 0), range=(0, 360), unit="deg")     # spins on its axle
    P.collider("base", -BASE_W / 2, -BASE_D / 2, 0, BASE_W, BASE_D, BASE_T)
    P.collider("post", -COL / 2, -COL / 2, BASE_T, COL, COL, HEAD_Z - BASE_T)
    P.collider("head", -HEAD_W / 2, -HEAD_D / 2, HEAD_Z, HEAD_W, HEAD_D, HEAD_T)
    for i, sx in enumerate((-1, 1), 1):
        x = sx * ROLL_X
        P.collider(f"roll-seat-{i}", x - ROLL_R, -ROLL_L / 2, ROLL_Z - ROLL_R, 2 * ROLL_R, ROLL_L, 2 * ROLL_R)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
