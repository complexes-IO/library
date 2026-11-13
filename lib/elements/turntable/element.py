#!/usr/bin/env python3
"""turntable: rotary conveyor turntable, our own design, built unattended (OPERATING.md 12, own designs; inventory row own_design
"yes": "rotary conveyor turntable (our own build: slewing ring, roller deck, gearmotor)"). A short roller track on a round deck
that turns about a vertical axis, so goods arriving along one line leave along another. The deck (node `deck`: a round plate
with two side frames on it) rests on the fixed race of a slewing ring, which a square base frame on four posts carries; the
posts stand on two floor rails that run the base's full length, each rail with two M12 clearance holes (ISO 273 medium) for floor
anchors in the pattern of the conveyor family's (conveyor-roller, -slat, -mattop, -incline). The track is the family's: 500
between the side frames, the rollers' tops at z 750, so a horizontal section can feed the deck and take from it. Six free rollers
lie across the track as nodes `roller-1` to `roller-6`, children of `deck` (P.parents): each spins about its own axis and turns
with the deck. The ring's rotating race, its balls and gear, the deck's drive (the gearmotor is not placed: motor-iec71-370w is
not past station 6, OPERATING.md 12 quality at the source), the rollers' axles and bearings, stops and sensors are not drawn.
Every size below is a design choice. No load rating, no speed, no safety claim. No vendor file was opened; the folder's record
(references/source.txt) is a search that found nothing and is not used.
Gate note (mech-r92, r93): the bounding box's extremes lie on axis-aligned solids of top-level nodes: the floor rails give x and
y, the track's side frames (node deck) give z. The round deck stays inside the rails' plan (r 450 against x 475, y 500). The
rollers, nested nodes, are inside the frames' box: the AutoCAD gate's glb extents reader does not descend into a nested node
(r93's first run: the rollers' tops at 750 were the STEP's z extreme, the glb read 740, FAIL by 10.0), so a nested node must
never carry an extreme (request mech-12)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "turntable", "1.1", "furniture"
TITLE = "rotary conveyor turntable, round deck Ø900 turning about z on a slewing ring, roller track 500 between frames, 660 long, 6 rollers Ø50 at 100 pitch, roller tops 750, side guides to 760, base frame on floor rails with 4 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; every size a "
            "design choice; no load rating, no speed, no safety claim; no vendor file opened")
ORIGIN = ("floor plane z = 0 on the deck's axis of rotation (x = 0, y = 0, the centre of the base's plan); at rest the track runs "
          "along y between the side frames (x +-250) with the rollers' axes along x at z 725 and their tops at z 750; the deck "
          "turns about z")
COMMAND = "TURNTABLE"
PARAMS = dict()
W = 500.0                                        # between the track's side frames' inner faces (x +-250): design choice, conveyor-roller's
TOP = 750.0                                      # the rollers' tops above the floor: design choice, conveyor-roller's track height
RUN = 1000.0                                     # the floor rails' length, y -500..500: the base's plan
DECK_R, DECK_T = 450.0, 15.0                     # the round deck plate Ø900, 15 thick: its edge stays inside the rails' plan
TRK_L = 660.0                                    # the track's side frames 660 long (y +-330): their corners (r 446.0) stay inside the deck's edge
FR_W = 50.0                                      # side frames 50 (x) wide, drawn by their outside, standing on the deck plate
FR_TOP = TOP + 10.0                              # 760: the frames' tops, 10 above the rollers' tops: side guides that keep goods on the deck while it turns (and the model's z extreme, on an axis-aligned top-level solid: see the gate note)
ROLL_R, ROLL_GAP = 25.0, 5.0                     # rollers Ø50, their end faces 5 clear of the side frames (the axles are not drawn)
N, PITCH = 6, 100.0                              # six rollers at 100 pitch, y -250..250, the end rollers 80 from the frames' ends
AXIS_Z = TOP - ROLL_R                            # 725: the rollers' axes
RING_R, RING_T = 380.0, 40.0                     # the slewing ring's fixed race Ø760, 40 high, under the deck: design choice
PLATE, PLATE_T = 820.0, 15.0                     # the ring's base plate 820 x 820 x 15 on the base frame: 10 past the frame's outer faces
POST, POST_C = 50.0, 375.0                       # posts 50 x 50 at x, y +-375 (outer faces +-400), drawn by their outside
BEAM = 50.0                                      # top frame beams 50 x 50, post to post, on the posts
TIE_LO = (150.0, 50.0)                           # lower ties between each pair of posts along x: underside z 150, 50 deep
RL_W, RL_T = 150.0, 20.0                         # floor rails 150 (x) wide, 20 thick, 1000 long, one under each side's posts, running outward
RL_X0 = POST_C - POST / 2 - 25.0                 # 325: a rail's inner edge, 25 inside the posts' inner faces; outer edge x 475
HOLE_X = POST_C + POST / 2 + 40.0                # 440: anchor hole centres x +-440, 40 outside the posts, 35 from the rail's outer edge
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
FR_H = 145.0                                     # side frames 145 (z) high: from the deck plate's top (615) to 760
Z_BEAM = FR_TOP - FR_H - DECK_T - RING_T - PLATE_T - BEAM            # 495: the beams' undersides (the posts' tops); the stack above them reaches the frames' tops at 760

def roller_y(i):
    return (i - (N + 1) / 2) * PITCH                                                                 # roller i's axis, i = 1..N from the -y end

def build():
    P = Prims(); S = "M-STEEL-7035"; R = "M-ZINC"; C = "M-SILVER"       # rollers zinc-plated tube, the ring's race bright steel
    z_plate = Z_BEAM + BEAM                                             # 545: the base plate's underside, on the beams
    z_ring = z_plate + PLATE_T                                          # 560: the race's underside
    z_deck = z_ring + RING_T                                            # 600: the deck plate's underside, on the race
    z_fr = z_deck + DECK_T                                              # 615: the side frames' undersides, on the deck plate
    for sx, k in ((-1, "l"), (1, "r")):
        rx = RL_X0 if sx > 0 else -RL_X0 - RL_W
        rl = P.box(S, rx, -RUN / 2, 0, RL_W, RUN, RL_T)                                              # floor rail, the base's full length
        P.collider(f"rail-{k}", rx, -RUN / 2, 0, RL_W, RUN, RL_T)
        px = POST_C - POST / 2 if sx > 0 else -POST_C - POST / 2
        for sy, j in ((-1, "a"), (1, "b")):
            py = sy * POST_C - POST / 2
            P.box(S, px, py, RL_T, POST, POST, Z_BEAM - RL_T)                                        # post, on the floor rail
            P.collider(f"post-{k}{j}", px, py, RL_T, POST, POST, Z_BEAM - RL_T)
            P.hole(S, (sx * HOLE_X, sy * POST_C, -1), (sx * HOLE_X, sy * POST_C, RL_T + 1), M12_D / 2, rl)   # M12 anchor hole, beside the post
        P.box(S, px, -POST_C - POST / 2, Z_BEAM, BEAM, 2 * POST_C + POST, BEAM)                      # top frame beam along y, over the side's posts
        P.collider(f"beam-{k}", px, -POST_C - POST / 2, Z_BEAM, BEAM, 2 * POST_C + POST, BEAM)
    for sy, j in ((-1, "a"), (1, "b")):
        py = sy * POST_C - POST / 2
        P.box(S, -POST_C + POST / 2, py, Z_BEAM, 2 * POST_C - POST, BEAM, BEAM)                      # top frame beam along x, between the beams along y
        P.collider(f"beam-{j}", -POST_C + POST / 2, py, Z_BEAM, 2 * POST_C - POST, BEAM, BEAM)
        P.box(S, -POST_C + POST / 2, py, TIE_LO[0], 2 * POST_C - POST, POST, TIE_LO[1])              # lower tie, post to post along x
        P.collider(f"tie-lo-{j}", -POST_C + POST / 2, py, TIE_LO[0], 2 * POST_C - POST, POST, TIE_LO[1])
    P.box(S, -PLATE / 2, -PLATE / 2, z_plate, PLATE, PLATE, PLATE_T)                                 # the ring's base plate, on the top frame
    P.collider("plate", -PLATE / 2, -PLATE / 2, z_plate, PLATE, PLATE, PLATE_T)
    P.cyl(C, (0, 0, z_ring), (0, 0, z_deck), RING_R)                                                 # the slewing ring's fixed race, a plain disc
    P.collider("ring", -RING_R, -RING_R, z_ring, 2 * RING_R, 2 * RING_R, RING_T)
    D = f"node:deck|{S}"
    P.cyl(D, (0, 0, z_deck), (0, 0, z_fr), DECK_R)                                                   # the deck plate, resting on the race
    for sx, k in ((-1, "l"), (1, "r")):
        fx = W / 2 if sx > 0 else -W / 2 - FR_W
        P.box(D, fx, -TRK_L / 2, z_fr, FR_W, TRK_L, FR_H)                                            # the track's side frame, standing on the deck
        P.collider(f"frame-{k}", fx, -TRK_L / 2, z_fr, FR_W, TRK_L, FR_H)
    P.collider("deck-plate", -DECK_R, -DECK_R, z_deck, 2 * DECK_R, 2 * DECK_R, DECK_T)
    xr = W / 2 - ROLL_GAP                                               # the rollers' end faces: x +-245
    for i in range(1, N + 1):
        n, y = f"roller-{i}", roller_y(i)
        P.cyl(f"node:{n}|{R}", (-xr, y, AXIS_Z), (xr, y, AXIS_Z), ROLL_R)                            # free roller, across the track
        P.pivot(n, "rotate", (-xr, y, AXIS_Z), axis=(1, 0, 0), range=(0, 360), unit="deg")           # spins on its axle (not drawn)
        P.parents[n] = "deck"                                                                        # rides the deck, keeps its own pivot (tensioner-belt 2.0's way)
    P.pivot("deck", "rotate", (0, 0, z_deck), axis=(0, 0, 1), range=(0, 360), unit="deg")            # turns on the slewing ring; the drive is the assembly's
    P.collider("roll-bed", -xr, roller_y(1) - ROLL_R, AXIS_Z - ROLL_R, 2 * xr, (N - 1) * PITCH + 2 * ROLL_R, 2 * ROLL_R)   # the roller bed at rest: what goods ride on
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
