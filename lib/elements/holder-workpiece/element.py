#!/usr/bin/env python3
"""holder-workpiece: generic workpiece holder (the bench "helping hand": a heavy base, a post and a cross bar with two swivelling
arms whose clips hold a small part or two wires while both of the worker's hands solder, glue or inspect it), our own vendor-neutral
design of the ETIM 10.0 class EC004363 (Workpiece holder; its synonym names the helping hand), built unattended (OPERATING.md 12,
generic elements; `python lib/build.py inventory mech` lists the class once no inventory row builds unattended: group EG020054
Clamping tools, lib/needs-em/mech.md). A cast base; a steel post on it; a head block on the post with the cross bar pressed through
it; at each end of the bar an arm (nodes `arm-left`, `arm-right`): a swivel boss bored 1 clear round the bar, a rod and a plastic
clip block. Each arm turns about the bar. The clips' jaws and springs, the friction that holds an arm where it is set, and a
magnifier or a lamp are not drawn and not claimed (the class values say none is fitted). The class values (spec.md, "Class values")
are design inputs; every size below is a design choice. No holding force is designed or claimed. No vendor file opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "holder-workpiece", "1.1", "device"
TITLE = "workpiece holder, generic, helping hand, two swivelling arms with clips on a cross bar, cast base 150 x 100, height 190"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic workpiece holder (ETIM 10.0 EC004363), a bench helping hand; class values are design inputs "
            "(spec.md); the clips' jaws and springs and the arms' friction not drawn or claimed; no magnifier, no lighting; every "
            "size a design choice; no holding force claimed; no vendor file opened")
ORIGIN = ("on the base's underside (z = 0, the face that stands on the bench) at its centre; the post at x = -50, y = 0; the cross "
          "bar's axis the line x = -50, z = 180 along y; the arms toward +x; the base, post, head and bar are fixed, each arm turns "
          "about the bar")
COMMAND = "HOLDWP"
PARAMS = dict()

BASE_L, BASE_W, BASE_T = 150.0, 100.0, 20.0              # cast base 150 x 100 x 20 (x +-75, y +-50): design choice
POST_X, POST_R = -50.0, 6.0                              # post Ø12 at x -50, y 0
Z_BAR = 180.0                                            # the cross bar's axis z 180
HEAD = 10.0                                              # head block 20 x 20 x 20 round the bar's axis (x -60..-40, y/z +-10)
BAR_R, BAR_Y = 4.0, 100.0                                # cross bar Ø8, y -100..100, pressed through the head
BOSS_Y0, BOSS_Y1, BOSS_H = 84.0, 98.0, 8.0               # swivel bosses 16 x 14 x 16 at y +-84..98 (x/z +-8 round the bar)
BOSS_BORE_R = 5.0                                        # bosses bored Ø10: 1 clear round the bar (features.csv, own)
ROD_R, ROD_X1 = 3.0, 60.0                                # arm rods Ø6 from the boss's face (x -42) to x 60
CLIP_X1, CLIP_HY, CLIP_HZ = 80.0, 5.0, 8.0               # clip blocks x 60..80, 10 wide (y), 16 high (z)
SWING = 60.0                                             # each arm turns 60 degrees down about the bar
CAST, STEEL, ZINC, CLIP = "M-CAST-BLUE", "M-SILVER", "M-ZINC", "M-BLACK-PA"

ARM_Y = (BOSS_Y0 + BOSS_Y1) / 2                          # each arm's centre plane y +-91
REACH = ((CLIP_X1 - POST_X) ** 2 + CLIP_HZ ** 2) ** 0.5  # the clip's far corner, 130.2 from the bar's axis
assert BOSS_BORE_R - BAR_R == 1.0 and BOSS_Y1 < BAR_Y and BOSS_Y0 > HEAD
assert Z_BAR - REACH > BASE_T + 25.0                     # a bound: the corner straight below the bar (86.5 deg) clears the base
SW_SIN, SW_COS = math.sin(math.radians(SWING)), math.cos(math.radians(SWING))
Z_LOW = Z_BAR - ((CLIP_X1 - POST_X) * SW_SIN + CLIP_HZ * SW_COS)  # the clip's far lower corner (130, -8 from the axis) at 60 deg: z 63.4
assert abs(Z_LOW - 63.4) < 0.05 and Z_LOW - BASE_T > 43.0  # spec.md's figure: 43.4 above the base's top (review mech-r129 f1)
assert BOSS_Y0 - CLIP_HY > BASE_W / 2                    # the arms hang outside the base's sides: never over it


def build():
    P = Prims()
    # ---- fixed: base, post, head block, cross bar pressed through the head
    P.box(CAST, -BASE_L / 2, -BASE_W / 2, 0, BASE_L, BASE_W, BASE_T)                                       # base z 0..20
    P.cyl(STEEL, (POST_X, 0, BASE_T), (POST_X, 0, Z_BAR - HEAD), POST_R)                                   # post z 20..170
    hd = P.box(ZINC, POST_X - HEAD, -HEAD, Z_BAR - HEAD, 2 * HEAD, 2 * HEAD, 2 * HEAD)                      # head z 170..190
    P.hole(ZINC, (POST_X, -HEAD - 1, Z_BAR), (POST_X, HEAD + 1, Z_BAR), BAR_R, hd)                          # bored Ø8: bar pressed in
    P.cyl(STEEL, (POST_X, -BAR_Y, Z_BAR), (POST_X, BAR_Y, Z_BAR), BAR_R)                                    # cross bar Ø8 x 200
    P.collider("base", -BASE_L / 2, -BASE_W / 2, 0, BASE_L, BASE_W, BASE_T)
    # ---- nodes arm-left (-y) and arm-right (+y): swivel boss bored 1 clear round the bar, rod, clip block
    for name, sy in (("arm-left", -1), ("arm-right", 1)):
        N = lambda m: f"node:{name}|{m}"
        y0 = BOSS_Y0 if sy > 0 else -BOSS_Y1
        bs = P.box(N(ZINC), POST_X - BOSS_H, y0, Z_BAR - BOSS_H, 2 * BOSS_H, BOSS_Y1 - BOSS_Y0, 2 * BOSS_H)   # boss x -58..-42
        P.hole(N(ZINC), (POST_X, y0 - 1, Z_BAR), (POST_X, y0 + BOSS_Y1 - BOSS_Y0 + 1, Z_BAR), BOSS_BORE_R, bs)  # bored Ø10
        P.cyl(N(STEEL), (POST_X + BOSS_H, sy * ARM_Y, Z_BAR), (ROD_X1, sy * ARM_Y, Z_BAR), ROD_R)            # rod x -42..60
        P.box(N(CLIP), ROD_X1, sy * ARM_Y - CLIP_HY, Z_BAR - CLIP_HZ, CLIP_X1 - ROD_X1, 2 * CLIP_HY, 2 * CLIP_HZ)  # clip x 60..80
        P.pivot(name, "rotate", (POST_X, 0, Z_BAR), axis=(0, 1, 0), range=(0, SWING), unit="deg")            # +x turns down
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
