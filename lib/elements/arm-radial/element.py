#!/usr/bin/env python3
"""arm-radial: the arm of a radial drill, our own design (OPERATING.md 12, own designs; inventory row own_design "yes": "radial
drill arm, swings on the column"). A seat plate as wide as column's body sits on column's top face (the fixed body); on it a round
hub carries a box-section arm beam (node `arm`, rotate about the column's axis, 90 degrees each way), which reaches 1500 forward of
the axis and has a 200 tail behind it; two flat ways on the beam's top face carry the drill head (spindle-drill, a later element)
along the arm. The seat's size is read from column itself (library.load), so the two cannot drift apart. Hub and beam are drawn
by their outsides. In this form the arm's height is fixed on column's top: it has no elevating screw or clamp on the column (an
elevating arm is column-round with arm-radial 2.0, needs-em 87). The hub's bearing and clamp, the head's rack and the seat's
fixing to the column are not drawn. Every other size is a design choice. No load rating, no accuracy claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "arm-radial", "1.1", "furniture"
TITLE = "radial drill arm, reach 1500 from the column's axis, swing 90 each way, seat 400 x 400 on column's top, two flat ways 60 wide"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; the seat on column 1.1's top face, every other "
            "size a design choice; no load rating, no accuracy claim; no vendor file opened")
ORIGIN = ("column's top face z = 0 (the arm's seat) on the column's axis x = 0, y = 0; the arm reaches toward -y (column's front) "
          "at rest and swings about z; the ways' top plane (the drill head's seat) at z = 550")
COMMAND = "RADARM"
PARAMS = dict()
COL = library.load("column")                      # column 1.1: the top face it sits on (one home for the figure)
SEAT_W = COL.BODY_W                               # seat plate as wide as the column's body, 400 x 400
SEAT_T = 30.0                                     # seat plate 30 thick (z 0..30): design choice
HUB_R, HUB_TOP = 190.0, 230.0                     # round hub Ø380, z 30..230: design choice
ARM_W, ARM_TOP = 300.0, 530.0                     # arm beam 300 wide (x +-150), z 230..530 (300 deep): design choice
REACH, TAIL = 1500.0, 200.0                       # beam from y +200 (tail) to y -1500 (reach): design choice
WAY_X, WAY_W, WAY_H = 90.0, 60.0, 20.0            # flat ways 60 wide at x +-90, 20 proud of the beam's top: design choice
WAY_Y0, WAY_Y1 = -1450.0, -300.0                  # the ways run y -1450..-300 along the arm: design choice
SWING = 90.0                                      # the arm swings -90..90 degrees about the column's axis: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                   # the ways: bare machined steel, the library's bright-metal layer
    A = lambda m: f"node:arm|{m}"
    P.box(S, -SEAT_W / 2, -SEAT_W / 2, 0, SEAT_W, SEAT_W, SEAT_T)                                     # seat plate, on column's top
    P.box(A(S), -ARM_W / 2, -REACH, HUB_TOP, ARM_W, REACH + TAIL, ARM_TOP - HUB_TOP)                 # arm beam (the node's first box)
    P.cyl(A(S), (0, 0, SEAT_T), (0, 0, HUB_TOP), HUB_R)                                              # round hub, under the beam
    for sx in (-1, 1):
        P.box(A(W), sx * WAY_X - WAY_W / 2, WAY_Y0, ARM_TOP, WAY_W, WAY_Y1 - WAY_Y0, WAY_H)          # flat way, the head's seat
    P.pivot("arm", "rotate", (0, 0, SEAT_T), axis=(0, 0, 1), range=(-SWING, SWING))
    P.collider("seat", -SEAT_W / 2, -SEAT_W / 2, 0, SEAT_W, SEAT_W, SEAT_T)
    P.collider("beam", -ARM_W / 2, -REACH, SEAT_T, ARM_W, REACH + TAIL, ARM_TOP + WAY_H - SEAT_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
