#!/usr/bin/env python3
"""conveyor-ball-transfer: ball transfer table, one straight section, our own design (lib/inventory.csv row own_design yes: "ball units
on a plate, four-way manual transfer"; no ETIM class on file fits, request mech-9's answer item 3), built unattended (OPERATING.md 12,
own designs). A flat steel deck on the conveyor family's track carries 32 ball transfer units in a square grid at 125 pitch: a
carton, tote or tray set on the balls is pushed by hand in any direction, so the table turns goods, joins lines that meet at an
angle, or lets an operator slide a pack off to the side. Nothing in it is driven. The track (two side frames 500 apart on two
supports of two posts, two ties and a foot plate each, one M12 clearance hole per plate, ISO 273 medium) and the height (the balls'
tops at 750) are conveyor-roller 1.0's, so a roller, wheel, slat or belt section of the family runs up to any side of it. Each ball
is a node `ball-<line>-<k>` (line 1 at the -y end; k from -x), turning freely in its housing; the twin turns it about x for goods
moving along y, the housing's seat balls that let it roll any way are not drawn (as the wheel conveyor's axles are not). A ball is
a sphere, which the toolkit has no solid for: it is a `mesh` primitive, in the glTF only, as a cable or a relay's spring (the
AutoCAD gate builds the solids and records the meshes; its STEP-vs-glb extents compare the solids). Every size is a design choice;
no load rating, no safety claim. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "conveyor-ball-transfer", "1.0", "furniture"
TITLE = "ball transfer table, our own design, 500 between frames, 1000 long, 32 ball units Ø25 at 125 pitch in a 4 x 8 grid, ball tops 750, 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design: ball transfer table on the conveyor family's track (conveyor-roller 1.0's frames, supports, height and "
            "anchor pattern); anchor holes ISO 273 medium for M12; every size a design choice; the balls are glTF meshes (no sphere "
            "solid in the toolkit); no load rating, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the centre of the table, x = 0 midway between the side frames, y = 0 midway along its length; "
          "goods move on the balls in any direction, the balls' tops at z 750, their centres at z 737.5")
COMMAND = "CONVBALL"
PARAMS = dict()
W = 500.0                                        # between the side frames' inner faces (x +-250): the family's track (conveyor-roller 1.0)
L = 1000.0                                       # the table's length, y -500..500: design choice (a transfer table is short: goods turn on it)
TOP = 750.0                                      # the balls' tops above the floor: the family's height (conveyor-roller 1.0)
BALL_R = 12.5                                    # balls Ø25: design choice
BALL_Z = TOP - BALL_R                            # 737.5: the balls' centres
PITCH = 125.0                                    # the grid, the same both ways (goods move any way): design choice
NL, NK = 8, 4                                    # 8 lines along y (ends 62.5 inside the deck's ends), 4 balls a line across x (x +-62.5, +-187.5)
BOSS_R, BOSS_H, BORE_R = 20.0, 15.0, 15.0        # each ball unit's housing: a Ø40 boss 15 high on the deck, bored Ø30 through for the ball: design choice
DECK_T = 10.0                                    # the deck plate, 10 thick: design choice
DECK_TOP = BALL_Z - BALL_R - 5.0                 # 720: the deck's top, 5 below the balls' undersides (725); the bosses' tops at 735
DECK_X = W / 2 + 50.0                            # 300: the deck spans the frames' outsides (x +-300), so goods leave over the frames sideways
FR_W, FR_H = 50.0, 80.0                          # side frames 50 (x) by 80 (z), drawn by their outside: the family's (conveyor-roller 1.0)
FR_TOP = DECK_TOP - DECK_T                       # 710: the frames' tops carry the deck
FR_Z = FR_TOP - FR_H                             # 630: the frames' undersides, the posts' tops
SUP_Y = 250.0                                    # the two supports' centres, y +-250: 250 from each end, as the family's
POST = 50.0                                      # posts 50 x 50 under each side frame, drawn by their outside: the family's
PL_W, PL_L, PL_T = 150.0, 100.0, 20.0            # foot plates 150 (x) by 100 (y), 20 thick, under each post, running outward: the family's
PL_X0 = W / 2 - 25.0                             # 225: a foot plate's inner edge, 25 inside the post's inner face
HOLE_X = W / 2 + POST + 40.0                     # 340: anchor hole centres x +-340, 40 outside the post, 35 from the plate's outer edge
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
TIE_UP = (570.0, 40.0)                           # upper tie between the posts: underside z 570, 40 deep (20 below the frames' undersides at 630): design choice
TIE_LO = (150.0, 50.0)                           # lower tie between the posts: underside z 150, 50 deep: design choice

def line_y(i):
    return -(NL - 1) / 2 * PITCH + (i - 1) * PITCH                                                   # line i, i = 1..NL from the -y end: y -437.5 .. 437.5

def ball_x(k):
    return -(NK - 1) / 2 * PITCH + (k - 1) * PITCH                                                   # ball k, k = 1..NK from -x: x -187.5 .. 187.5

def balls():
    return [(f"ball-{i}-{k}", ball_x(k), line_y(i)) for i in range(1, NL + 1) for k in range(1, NK + 1)]

def sphere(c, r, nseg=12, nring=6):
    """a sphere of radius r about c as outward-facing triangles: nseg meridians, nring bands pole to pole (120 triangles at 12 x 6)"""
    cx, cy, cz = c
    ring = [[(cx + r * math.sin(math.pi * i / nring) * math.cos(2 * math.pi * j / nseg),
              cy + r * math.sin(math.pi * i / nring) * math.sin(2 * math.pi * j / nseg),
              cz + r * math.cos(math.pi * i / nring)) for j in range(nseg)] for i in range(1, nring)]
    top, bot = (cx, cy, cz + r), (cx, cy, cz - r); tris = []
    for j in range(nseg):
        k = (j + 1) % nseg
        tris.append((top, ring[0][j], ring[0][k])); tris.append((bot, ring[-1][k], ring[-1][j]))                      # the polar caps
        for i in range(nring - 2):
            a, b, c2, d = ring[i][j], ring[i][k], ring[i + 1][k], ring[i + 1][j]
            tris.append((a, d, c2)); tris.append((a, c2, b))                                                            # a band's quad
    vol = sum((p[0] * (q[1] * s[2] - q[2] * s[1]) - p[1] * (q[0] * s[2] - q[2] * s[0]) + p[2] * (q[0] * s[1] - q[1] * s[0]))
              for p, q, s in (((t[0][0] - cx, t[0][1] - cy, t[0][2] - cz), (t[1][0] - cx, t[1][1] - cy, t[1][2] - cz), (t[2][0] - cx, t[2][1] - cy, t[2][2] - cz)) for t in tris)) / 6.0
    return tris if vol > 0 else [(t[0], t[2], t[1]) for t in tris]                                 # outward: a positive signed volume

def build():
    P = Prims(); S = "M-STEEL-7035"; Z = "M-ZINC"; B = "M-SILVER"            # housings: zinc-plated steel; balls: hardened steel, bright
    x0 = W / 2                                                              # the frames' and posts' inner faces: x +-250
    for sx, k in ((-1, "l"), (1, "r")):
        fx = x0 if sx > 0 else -x0 - FR_W
        P.box(S, fx, -L / 2, FR_Z, FR_W, L, FR_H)                                                    # side frame
        P.collider(f"frame-{k}", fx, -L / 2, FR_Z, FR_W, L, FR_H)
        for sy, j in ((-1, "a"), (1, "b")):
            y = sy * SUP_Y
            P.box(S, fx, y - POST / 2, PL_T, POST, POST, FR_Z - PL_T)                                # post, on its foot plate
            px = PL_X0 if sx > 0 else -PL_X0 - PL_W
            pl = P.box(S, px, y - PL_L / 2, 0, PL_W, PL_L, PL_T)                                     # foot plate
            P.hole(S, (sx * HOLE_X, y, -1), (sx * HOLE_X, y, PL_T + 1), M12_D / 2, pl)               # M12 anchor hole
            P.collider(f"post-{k}{j}", fx, y - POST / 2, PL_T, POST, POST, FR_Z - PL_T)
            P.collider(f"foot-{k}{j}", px, y - PL_L / 2, 0, PL_W, PL_L, PL_T)
    for sy, j in ((-1, "a"), (1, "b")):
        y = sy * SUP_Y
        for n, (z, h) in (("up", TIE_UP), ("lo", TIE_LO)):
            P.box(S, -x0, y - POST / 2, z, W, POST, h)                                               # tie, post to post
            P.collider(f"tie-{n}-{j}", -x0, y - POST / 2, z, W, POST, h)
    P.box(S, -DECK_X, -L / 2, FR_TOP, 2 * DECK_X, L, DECK_T)                                         # the deck, on the frames' tops
    P.collider("deck-plate", -DECK_X, -L / 2, FR_TOP, 2 * DECK_X, L, DECK_T)
    for n, x, y in balls():
        bs = P.cyl(Z, (x, y, DECK_TOP), (x, y, DECK_TOP + BOSS_H), BOSS_R)                          # the ball unit's housing, a boss on the deck
        P.hole(Z, (x, y, DECK_TOP - 1), (x, y, DECK_TOP + BOSS_H + 1), BORE_R, bs)                   # bored through: the ball's socket
        P.mesh(f"node:{n}|{B}", sphere((x, y, BALL_Z), BALL_R))                                      # the ball, free in its socket
        P.pivot(n, "rotate", (x, y, BALL_Z), axis=(1, 0, 0), range=(0, 360), unit="deg")            # turns any way; drawn turning about x
    xb = ball_x(NK) + BALL_R; yb = line_y(NL) + BALL_R                                               # 200, 450: the ball bed's half extents
    P.collider("ball-bed", -xb, -yb, BALL_Z - BALL_R, 2 * xb, 2 * yb, 2 * BALL_R)                  # the ball bed: what goods ride on
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
