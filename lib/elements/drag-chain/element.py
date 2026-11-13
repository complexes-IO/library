#!/usr/bin/env python3
"""drag-chain: cable guide chain (cable carrier), our own vendor-neutral design of the ETIM 10.0 class EC002414 (Cable guide
chain), built unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "drag-chain", own_design generic, 5 systems:
gantry-xyz, laser-cutter-fiber, plasma-cutter-cnc, servo-axis-bench, servo-pick-and-place; request mech-13's answer: generic of
EC002414, its 14 features on file, "links as one bent run with the moving end a node" a design choice). The chain that carries a
moving axis's cables and hoses: a run of closed tube links (the cables threaded through) lying on the machine's mounting surface
from the fixed end, a bend of bending radius 100, and an upper run back over it to the moving end, which bolts under the axis's
carriage. The run is drawn at the travel's start: the moving end next to the bend, one link in the upper run. The moving end's
bracket is node `moving-end`, translating 0 to 1000 along +x, away from the links; the links are one fixed run and do not follow it
(the bend rolling half the travel is not modelled: links are no nodes). Both brackets take 2 x M6 in ISO 273 medium clearance holes.
2.0 (review mech-r112 findings 1 and 2): each bracket's upright carries a 50 x 25 window on the way, so the cables leave at both ends,
and the bend is 12 links of 15 degrees whose ways keep the 25 high way clear through it (1.0's 6 links narrowed it to 21). The class values (spec.md "Class
values") are design inputs; every size below is a design choice, and none is taken from the catalogue record that came with the
element's folder (references/source.txt). No load, cantilever or speed claim. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "drag-chain", "2.0", "run"
TITLE = "cable guide chain, generic, inner 50 x 25, bending radius 100, 24 links, travel 1000, 2 x M6 at each end"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic cable guide chain (ETIM 10.0 EC002414); class values are design inputs (spec.md); the end "
            "brackets' holes M6 in ISO 273 medium clearance; every size a design choice; drawn at the travel's start, the moving end's "
            "bracket a node; no load, cantilever or speed claim; no vendor file opened")
ORIGIN = ("the mounting surface (z = 0) under the fixed end: x = 0 at the fixed end's link face (its bracket's upright at x 0 to 3), "
          "y = 0 on the chain's centre plane; the moving end travels along +x from x -500 to +500, the bend lies toward -x")
COMMAND = "DRAGCHAIN"
PARAMS = dict()

W, H = 66.0, 35.0                  # link outside: width (y) 66, height 35 (class values: outer width / outer height)
WI, HI = 50.0, 25.0                # link inside, the cables' room: 50 x 25 (class values: inner width / inner height)
SIDE, BAR = (W - WI) / 2, (H - HI) / 2   # side walls 8, top and bottom walls 5 (design choice)
PITCH = 50.0                       # straight links 50 long (design choice)
R = 100.0                          # bending radius, to the chain's centre line (class value)
N_BEND = 12                        # the bend drawn as 12 links of 15 degrees each (design choice; 2.0, review mech-r112 finding 2)
TRAVEL = 1000.0                    # the moving end's travel, x -500 to +500 about the fixed end (design choice)
N_LO, N_UP = 11, 1                 # drawn at the travel's start: 11 links in the lower run, 1 in the upper (12 straight links in all)
XB = -N_LO * PITCH                 # -550: where the runs meet the bend
XM = XB + N_UP * PITCH             # -500: the moving end's link face at the travel's start
ZC = H / 2 + R                     # 117.5: the bend's centre height; the upper run's centre line at ZC + R = 217.5
RO, RI = R + H / 2, R - H / 2      # 117.5 / 82.5: the bend's outer and inner radius
HALF = math.radians(180.0 / N_BEND / 2)   # 15 degrees: half a bend link's angle
BL = 2 * RO * math.sin(HALF)       # 30.67: a bend link's length, its outer corners on the outer arc
BD = RO * math.cos(HALF) - RI      # 33.99: a bend link's depth, inner radius to its outer face
# The bend's way (2.0, review mech-r112 finding 2): each bend link's way runs from WN_IN to WN_OUT normal to its own faces, so the
# annulus r R - HI/2 to R + HI/2 (87.5 to 112.5, the straight runs' way turned about the bend's centre) is clear through the whole
# bend: a point of a link's inner wall (normal distance < WN_IN, at most BL/2 along it) lies inside r 87.36, and its outer wall
# (normal distance > WN_OUT) outside r 112.5, so neither a link nor its overlapping neighbour narrows the 25 high way.
WN_IN, WN_OUT = 86.0, R + HI / 2   # 86.0 / 112.5: walls 3.5 (inner) and 4.0 (outer, at mid-link) (design choice)
Z_UP = ZC + R - H / 2              # 200: the upper run's underside
BR_T, BR_L, BR_W = 3.0, 40.0, 90.0       # bracket plates 3 thick; foot / top plate 40 (x) x 90 (y) (design choice)
HOLE_X, HOLE_Y = 25.0, 30.0        # 2 x M6 at x 25, y +-30 in each bracket (design choice)
M6_CLR = 6.6                       # ISO 273 medium (H13): lib/standards/holes.csv
CHAIN, STEEL = "M-BLACK-PA", "M-ZINC"

LENGTH_M = ((N_LO + N_UP) * PITCH + math.pi * R) / 1000.0     # 0.914 m: the chain's length on its centre line
assert abs(LENGTH_M - 0.9142) < 1e-3
assert abs(XM + TRAVEL / 2) < 1e-9 and N_UP >= 1 and N_LO - TRAVEL / PITCH / 2 >= 1   # at either end of the travel one link stays straight (bend at -550 / -50)
assert SIDE == 8.0 and BAR == 5.0 and abs(BD - 33.99) < 0.01
assert math.hypot(WN_IN, BL / 2) < R - HI / 2 and WN_OUT >= R + HI / 2 and RI < WN_IN and WN_OUT < RI + BD   # the bend's 25 high way clear
# The end brackets' windows (2.0, review mech-r112 finding 1): each upright carries a 50 x 25 window, the way's own section, so the
# cables leave the chain at both ends; frame left round it: 8 each side, 2 and 5 below / above (fixed), 5 and 2 (moving)
WIN_Z_FIX, WIN_Z_MOV = BAR, Z_UP + BAR   # the windows' lower edges: z 5 (fixed) and z 205 (moving), each 25 high
assert WIN_Z_FIX > BR_T and WIN_Z_FIX + HI < H and WIN_Z_MOV > Z_UP and WIN_Z_MOV + HI < Z_UP + H - BR_T
assert HOLE_X + M6_CLR / 2 < BR_L - 10 and BR_W / 2 - HOLE_Y - M6_CLR / 2 > 10 and HOLE_Y + M6_CLR / 2 < BR_W / 2


def build():
    P = Prims()
    for n, z0 in ((N_LO, 0.0), (N_UP, Z_UP)):                                                           # the two straight runs from the bend
        for i in range(n):
            x0 = XB + i * PITCH
            k = P.box(CHAIN, x0, -W / 2, z0, PITCH, W, H)                                                 # a tube link
            P.cutbox(CHAIN, x0 - 1.0, -WI / 2, z0 + BAR, PITCH + 2.0, WI, HI, k)                          # the cables' way through it
    for k in range(N_BEND):                                                                             # the bend, from the lower run up
        tm = math.radians(-90.0 - (2 * k + 1) * math.degrees(HALF))                                     # the link's middle angle
        u = (math.cos(tm), 0.0, math.sin(tm)); t = (math.sin(tm), 0.0, -math.cos(tm)); ey = (0.0, 1.0, 0.0)   # radial out, along the chain, across
        def at(r, s, w): return (XB + r * u[0] + s * t[0], w, ZC + r * u[2] + s * t[2])
        b = P.obox(CHAIN, at(RI, -BL / 2, -W / 2), t, ey, u, BL, W, BD)
        P.cut(CHAIN, at(WN_IN, -BL / 2 - 1.0, -WI / 2), t, ey, u, BL + 2.0, WI, WN_OUT - WN_IN, b)
    foot = P.box(STEEL, 0.0, -BR_W / 2, 0.0, BR_L, BR_W, BR_T)                                          # fixed end: foot plate
    up = P.box(STEEL, 0.0, -W / 2, BR_T, BR_T, W, H - BR_T)                                             # its upright on the lower run's end face
    P.cutbox(STEEL, -1.0, -WI / 2, WIN_Z_FIX, BR_T + 2.0, WI, HI, up)                                   # its window: the way's section
    for y in (-HOLE_Y, HOLE_Y):
        P.hole(STEEL, (HOLE_X, y, -1.0), (HOLE_X, y, BR_T + 1.0), M6_CLR / 2, foot)                     # 2 x M6, ISO 273 medium
    N = f"node:moving-end|{STEEL}"                                                                      # moving end: the carriage's bracket
    upm = P.box(N, XM, -W / 2, Z_UP, BR_T, W, H - BR_T)                                                 # its upright on the upper run's end face
    P.cutbox(N, XM - 1.0, -WI / 2, WIN_Z_MOV, BR_T + 2.0, WI, HI, upm)                                  # its window: the way's section
    top = P.box(N, XM, -BR_W / 2, Z_UP + H - BR_T, BR_L, BR_W, BR_T)                                    # its top plate under the carriage
    for y in (-HOLE_Y, HOLE_Y):
        P.hole(N, (XM + HOLE_X, y, Z_UP + H - BR_T - 1.0), (XM + HOLE_X, y, Z_UP + H + 1.0), M6_CLR / 2, top)   # 2 x M6, ISO 273 medium
    P.pivot("moving-end", "translate", (XM, 0.0, Z_UP + H), axis=(1, 0, 0), range=(0, TRAVEL), unit="mm")   # away from the links only
    P.collider("run-lower", XB, -W / 2, 0.0, -XB, W, H)
    P.collider("run-upper", XB, -W / 2, Z_UP, N_UP * PITCH, W, H)
    P.collider("bend", XB - RO, -W / 2, 0.0, RO, W, Z_UP + H)
    P.collider("mount-fixed", 0.0, -BR_W / 2, 0.0, BR_L, BR_W, H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
