#!/usr/bin/env python3
"""desk-pc: workstation desk 1400 x 700, top surface 740 above the floor: a 25 top on two steel side frames (foot, two legs, top rail),
a back (modesty) panel, a cable tray hung under the top's back edge, a CPU bay on the floor at the right (side panel, floor plate on
two runners) and one drawer under the top at the left (node `drawer`, translate -y, 0 to 300). Our own design (EM r4 rule): every
size is a design choice. The folder's acquisition record (metadata.json, references/source.txt) names a catalogue desk; no vendor
file was opened and no figure was taken from the record. Nothing outside itself is met: no screw, rail or port. Drawer slides,
levelling feet and fixings are not modelled. No load rating, no ergonomic and no safety claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "desk-pc", "1.0", "furniture"
TITLE = "workstation desk 1400 x 700 x 740, CPU bay, cable tray under, one drawer"
TOOLKIT = "1.3"
BASELINE = "our own design (EM r4 rule, 2026-11-05): no product matched; every size a design choice; nothing outside itself is met"
ORIGIN = "floor machine: floor plane z = 0; x = 0, y = 0 at the top's front-left corner (seen from above); the person sits at -y; the drawer opens toward -y"
COMMAND = "DESKPC"
PARAMS = dict()

W, D, H, TOP_T = 1400.0, 700.0, 740.0, 25.0     # top 1400 x 700, its surface 740 above the floor, 25 thick: design choices
ZU = H - TOP_T                                    # 715: the top's underside
SQ, LEG_X = 50.0, 30.0                            # frame tube 50 x 50 (solid here), side frames 30 in from each end of the top
FOOT_Y, FOOT_H = 20.0, 40.0                       # feet: 20 in from the front and back edges, 40 high
LEG_Y = 40.0                                      # legs 40 in from the front and back edges, standing on the feet
SH = 1.5                                          # sheet: back panel, cable tray, drawer housing, drawer tray, CPU bay side panel
BACK_Z, BACK_Y = 300.0, D - 66.5                  # back panel from z 300 to the top, its front face 66.5 in from the back edge
TRAY_W, TRAY_H = 150.0, 80.0                      # cable tray: 150 wide (y), front wall 80 high; its back wall rises to the top
TRAY_Z = ZU - 120.0                               # 595: the cable tray's underside
DR_X0, DR_W, DR_D, DR_H = 100.0, 460.0, 440.0, 120.0   # drawer housing: x 100 to 560, 440 deep, 120 high under the top
DR_FRONT_T, DR_TRAVEL = 20.0, 300.0               # drawer front 20 thick (proud of the top's front edge); pull-out 300
DR_CLR, DR_TD = 10.0, 400.0                       # drawer tray 10 clear of each housing side, 400 deep (100 stays in at 300 out)
HANDLE_L = 200.0                                  # drawer handle bar on two standoffs, as cabinet-tool's (shorter bar)
CPU_X0 = 1020.0                                   # CPU bay: from its side panel (x 1018.5) to the right side frame (x 1320)
CPU_PH, RUN, PLATE = 560.0, (30.0, 60.0), 3.0     # side panel 560 high; runners 30 wide x 60 high; floor plate 3.0

def build():
    P = Prims(); S, B, F, Z = "M-STEEL-7035", "M-BROWN", "M-BLUE", "M-ZINC"
    P.box(B, 0, 0, ZU, W, D, TOP_T)                                                       # top
    xin0, xin1 = LEG_X + SQ, W - LEG_X - SQ                                               # 80, 1320: the side frames' inner faces
    yl0, yl1 = LEG_Y + SQ, D - LEG_Y - SQ                                                 # 90, 610: the legs' inner faces
    for x in (LEG_X, xin1):                                                               # side frames, left and right
        P.box(S, x, FOOT_Y, 0, SQ, D - 2 * FOOT_Y, FOOT_H)                                # foot along y
        for y in (LEG_Y, yl1): P.box(S, x, y, FOOT_H, SQ, SQ, ZU - FOOT_H)                # front and back legs, foot to the top
        P.box(S, x, yl0, ZU - SQ, SQ, yl1 - yl0, SQ)                                      # top rail, leg to leg
    P.box(S, xin0, BACK_Y, BACK_Z, xin1 - xin0, SH, ZU - BACK_Z)                          # back (modesty) panel, frame to frame
    ty0 = BACK_Y - TRAY_W                                                                 # 483.5: the cable tray's front face
    P.box(S, xin0, ty0, TRAY_Z, xin1 - xin0, TRAY_W, SH)                                  # cable tray bottom
    P.box(S, xin0, ty0, TRAY_Z + SH, xin1 - xin0, SH, TRAY_H - SH)                        # front wall
    P.box(S, xin0, BACK_Y - SH, TRAY_Z + SH, xin1 - xin0, SH, ZU - TRAY_Z - SH)          # back wall, up to the top's underside
    hx0, hx1, hz = DR_X0, DR_X0 + DR_W, ZU - DR_H                                         # drawer housing: x 100 to 560, z 595 to 715
    P.box(S, hx0, 0, hz, DR_W, DR_D, SH)                                                  # housing bottom
    for x in (hx0, hx1 - SH): P.box(S, x, 0, hz + SH, SH, DR_D, DR_H - SH)                # housing sides, up to the top
    P.box(S, hx0 + SH, DR_D - SH, hz + SH, DR_W - 2 * SH, SH, DR_H - SH)                  # housing back
    P.box(S, CPU_X0 - SH, yl0, 0, SH, yl1 - yl0, CPU_PH)                                  # CPU bay side panel, on the floor
    for x in (CPU_X0, xin1 - RUN[0]): P.box(S, x, yl0, 0, RUN[0], yl1 - yl0, RUN[1])      # two runners along y
    P.box(S, CPU_X0, yl0, RUN[1], xin1 - CPU_X0, yl1 - yl0, PLATE)                        # CPU floor plate, z 60 to 63
    n = "drawer"; Ln = lambda m: f"node:{n}|{m}"
    fz0, fz1 = hz + 3.0, ZU - 3.0                                                         # front z 598 to 712, 3 clear of the housing and the top
    P.box(Ln(F), hx0, -DR_FRONT_T, fz0, DR_W, DR_FRONT_T, fz1 - fz0)                      # front
    tx0, tx1, tz0, tz1 = hx0 + SH + DR_CLR, hx1 - SH - DR_CLR, hz + SH + 3.5, ZU - 15.0    # tray x 111.5 to 548.5, z 600 to 700
    P.box(Ln(S), tx0, 0, tz0, tx1 - tx0, DR_TD, SH)                                       # tray bottom
    for x in (tx0, tx1 - SH): P.box(Ln(S), x, 0, tz0 + SH, SH, DR_TD, tz1 - tz0 - SH)     # tray sides
    P.box(Ln(S), tx0 + SH, DR_TD - SH, tz0 + SH, tx1 - tx0 - 2 * SH, SH, tz1 - tz0 - SH)  # tray back
    cx, cz = (hx0 + hx1) / 2, (fz0 + fz1) / 2
    for x in (cx - HANDLE_L / 2, cx + HANDLE_L / 2 - 12.0):
        P.box(Ln(Z), x, -DR_FRONT_T - 15.0, cz - 6.0, 12.0, 15.0, 12.0)                   # handle standoffs
    P.box(Ln(Z), cx - HANDLE_L / 2, -DR_FRONT_T - 27.0, cz - 6.0, HANDLE_L, 12.0, 12.0)   # handle bar
    P.pivot(n, "translate", (cx, -DR_FRONT_T, cz), axis=(0, -1, 0), range=(0, DR_TRAVEL))
    P.collider("top", 0, 0, ZU, W, D, TOP_T)
    for x, nm in ((LEG_X, "frame-left"), (xin1, "frame-right")):
        P.collider(nm, x, FOOT_Y, 0, SQ, D - 2 * FOOT_Y, ZU)
    P.collider("back-panel", xin0, BACK_Y, BACK_Z, xin1 - xin0, SH, ZU - BACK_Z)
    P.collider("cable-tray", xin0, ty0, TRAY_Z, xin1 - xin0, TRAY_W, ZU - TRAY_Z)
    P.collider("drawer-housing", hx0, 0, hz, DR_W, DR_D, DR_H)
    P.collider("cpu-bay", CPU_X0 - SH, yl0, 0, xin1 - CPU_X0 + SH, yl1 - yl0, CPU_PH)
    P.collider(n, hx0, -DR_FRONT_T - 27.0, fz0, DR_W, DR_FRONT_T + 27.0 + DR_TD, fz1 - fz0)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="rear, cable tray and CPU bay", az=40, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
