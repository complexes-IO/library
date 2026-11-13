#!/usr/bin/env python3
"""pallet-rack: one bay of selective pallet rack for two pallets per level, sized around the pallet element (1219 x 1016). Our own
design (EM r4 rule): the bay's clearances, sections and levels are design choices; anchors M12 with ISO 273 medium Ø13.5 holes.
No load rating and no safety claim."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "pallet-rack", "1.1", "furniture"
TITLE = "pallet rack bay 2492 x 1067 x 2500, two beam levels, two pallets per level"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): sized around the pallet element (1219 x 1016); M12 anchors in ISO 273 medium holes"
ORIGIN = "floor machine: floor plane z = 0, the front-left corner of the left frame's front upright x = 0, y = 0; the beams run +x, the frames' depth +y, front toward -y"
COMMAND = "PRACK"
PARAMS = dict(levels=2, pitch=1100.0)
PAL_X, PAL_Y = 1219.0, 1016.0    # the pallet element's footprint (lib/elements/pallet): 1219 into the rack, 1016 along the beam.
                                 # Assumption (B), inherited: pallet 1.1 marks it so (ISO 6780 not on file); spec.md
GAP = 100.0                      # clear space at each side of a pallet and between the two: design choice
UP_W, UP_D = 80.0, 80.0          # upright section 80 x 80 (closed box, perforations not modelled): design choice
BAY = 2 * PAL_Y + 3 * GAP        # clear beam length between the uprights: 2332
OVER = 76.0                      # pallet overhang past the front and back beams: design choice
DEPTH = PAL_X - 2 * OVER         # frame depth, front of front upright to back of back upright: 1067
HEIGHT = 2500.0                  # upright height: design choice
BEAM_H, BEAM_D = 120.0, 50.0     # beam section 120 x 50 (box): design choice
BR_W, BR_H = 40.0, 30.0          # frame bracing section: design choice
FOOT, FOOT_T = 150.0, 6.0        # footplate 150 x 150 x 6 under each upright: design choice
ANCHOR_D = 13.5                  # 2 x M12 anchors per footplate; Ø13.5 = M12 clearance, ISO 273 medium H13
ANCHOR_O = 55.0                  # 1.1: the anchors on the footplate's diagonal, 55 from the upright's centre in x and in y (design
                                 # choice): 21.2 from the upright's corner, 20 from the plate's edges (the point where the two are
                                 # equal, 54.5, rounded up). 1.0 had them at x ± 50, 10 from the upright's faces (review finding 2).
                                 # The seat's room for the nut, washer and socket: NOT ON FILE (B), no fastener table on file; spec.md

def _member(P, L, a, b, w, h):
    """a straight bracing member from point a to b (centre line), section w (along x) by h"""
    d = [b[i] - a[i] for i in range(3)]; n = math.sqrt(sum(v * v for v in d)); ex = [v / n for v in d]
    ey = (1.0, 0.0, 0.0); ez = (ex[1] * ey[2] - ex[2] * ey[1], ex[2] * ey[0] - ex[0] * ey[2], ex[0] * ey[1] - ex[1] * ey[0])
    o = [a[i] - ey[i] * w / 2 - ez[i] * h / 2 for i in range(3)]
    return P.obox(L, o, ex, ey, ez, n, w, h)

def build(levels=2, pitch=1100.0):
    P = Prims(); U, B, F = "M-BLUE", "M-YELLOW", "M-GALV"
    xs = (0.0, UP_W + BAY)                                                             # the two frames
    for fx in xs:
        cx = fx + UP_W / 2
        for fy in (0.0, DEPTH - UP_D):
            P.box(U, fx, fy, FOOT_T, UP_W, UP_D, HEIGHT - FOOT_T)                      # upright
            px, py = cx - FOOT / 2, fy + UP_D / 2 - FOOT / 2
            fp = P.box(F, px, py, 0, FOOT, FOOT, FOOT_T)                               # footplate
            for s in (-1, 1):                                                          # front-left and back-right
                hx = cx + s * ANCHOR_O; hy = fy + UP_D / 2 + s * ANCHOR_O
                P.hole(F, (hx, hy, -1), (hx, hy, FOOT_T + 1), ANCHOR_D / 2, fp)
        y0, y1 = UP_D, DEPTH - UP_D                                                    # bracing between the uprights' inner faces
        zs = [200.0 + i * (HEIGHT - 400.0) / 4 for i in range(5)]
        for z in (zs[0], zs[-1]):
            P.box(U, cx - BR_W / 2, y0, z - BR_H / 2, BR_W, y1 - y0, BR_H)             # horizontals
        for i in range(4):
            a, b = (cx, y0, zs[i]), (cx, y1, zs[i + 1])
            if i % 2: a, b = (cx, y1, zs[i]), (cx, y0, zs[i + 1])
            _member(P, U, a, b, BR_W, BR_H)                                            # diagonals, zig-zag
        P.collider(f"frame-{int(fx)}", fx, 0, 0, UP_W, DEPTH, HEIGHT)
    for k in range(1, levels + 1):
        top = k * pitch
        for by in (0.0, DEPTH - BEAM_D):
            P.box(B, UP_W, by, top - BEAM_H, BAY, BEAM_D, BEAM_H)                      # beams, front and back
            P.collider(f"beam-{k}-{'front' if by == 0 else 'back'}", UP_W, by, top - BEAM_H, BAY, BEAM_D, BEAM_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=20), dict(name="frame side", az=180, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
