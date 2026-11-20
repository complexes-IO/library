#!/usr/bin/env python3
"""rack-bins-1000: generic storage bins rack, free-standing, 1000 wide and 1800 high, our own vendor-neutral design of the ETIM 10.0
class EC004069 (Storage bins rack; synonyms Sight storage box rack, Storage box rack), built unattended (OPERATING.md 12, generic
elements; group EG010340 Storage and racking systems, a tier-2 class walked by name after rail-suspension-shelving-1000,
lib/rounds/mech/r161.md). A single-sided frame of painted steel tube 50 x 50 x 2: two uprights on two feet that reach forward under the
bins and back behind the frame, a bottom bar and a top bar between the uprights; four suspension rails across it, 400 apart, on which
open-fronted bins hang by their rear hooks in front of the frame. The rails are placed rail-suspension-shelving-1000 1.0 elements,
never redrawn: the uprights take that element's section (50 x 50) and inner faces (x +-450), so its end plates stand on their inner
faces as they do on shelving-steel's rear uprights, and its height and room under it set the rails' pitch. The bins are not drawn.
The class's features are not on file (lib/standards/etim/class-features.csv has no EC004069 rows): spec.md gives the design values
under plain names, as rail-suspension-shelving-1000 does. Every size is a design choice. No load, stability or safety claim: fixing the
rack to the floor or a wall is the host's. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "rack-bins-1000", "1.0", "furniture"
TITLE = ("storage bins rack, free-standing, generic, 1000 wide x 1800 high, painted steel tube 50 x 50 x 2 on two feet, four placed "
         "suspension rails 400 apart for hanging bins")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic storage bins rack (ETIM 10.0 EC004069), a free-standing single-sided frame of painted steel tube "
            "50 x 50 x 2 (two uprights 1750 high on two feet 650 long reaching 400 forward and 200 back, a bottom bar and a top bar "
            "900 long between the uprights), carrying four placed rail-suspension-shelving-1000 1.0 rails 400 apart (their bottoms at "
            "380, 780, 1180, 1580) on the uprights' inner faces x +-450; the rail's figures read from that element (library.load); "
            "class features not on file, design values under plain names (spec.md); every size a design choice; bins not drawn; no "
            "load, stability or safety claim; no vendor file opened")
ORIGIN = ("the floor under the middle of the rack: z = 0 the feet's undersides, x = 0 the middle of the rack's width, y = 0 the "
          "uprights' front faces; the bins hang in front of the frame, toward -y; the feet reach to y -400 in front and y 250 behind")
COMMAND = "RBIN1000"
PARAMS = dict()

RAIL_V = "1.0"                                  # the rail's version, pinned
RS = library.load("rail-suspension-shelving-1000", RAIL_V)   # the rail (one home for each of its figures)
UP = RS.UP                                      # 50: the tube's section, the rail's uprights' section (shelving-steel's)
XI = RS.XI                                      # 450: the uprights' inner faces x +-450, where the rail's end plates stand
XO = XI + UP                                    # 500: the uprights' outer faces, the rack's width 1000
RY = -RS.YB0                                    # -450: the rail placed so its uprights' band (y 450 to 500) is this rack's y 0 to 50
T = 2.0                                         # design: the tube's wall (painted steel tube 50 x 50 x 2)
FH = UP                                         # 50: the feet's height (the tube laid flat), the uprights stand on them
FY0, FY1 = -400.0, 250.0                        # design: the feet reach 400 in front of the uprights and 200 behind them
H = 1800.0                                      # design: the rack's height (the top bar's top face)
PITCH = 400.0                                   # design: the rails 400 apart
ZB = (380.0, 780.0, 1180.0, 1580.0)             # design: the rails' bottom faces
MAT = "M-STEEL-7035"                            # painted steel, the rail's layer

RAIL_H = RS.H                                   # 80: the rail's height
ROOM = RS.Z0                                    # 300: the room under the rail the rail element leaves for a hanging bin
LIFT = 2 * (RS.LIP - RS.CH_Z - RS.T)            # 26: the rise a hook needs over the rail's lip (rail-suspension's own check)
assert abs(XI - 450.0) < 1e-9 and abs(UP - 50.0) < 1e-9 and abs(RY + 450.0) < 1e-9                  # the rail's figures as read
assert all(abs(b - a - PITCH) < 1e-9 for a, b in zip(ZB, ZB[1:]))                                    # one pitch
assert PITCH - RAIL_H >= ROOM                                                                          # 320 >= 300 between rails
assert ZB[0] - FH >= ROOM                                                                              # 330 under the lowest rail
assert (H - UP) - (ZB[-1] + RAIL_H) >= LIFT                                                            # 90 >= 26 under the top bar
assert FY0 < RS.RY0 + RY < UP < FY1                                                                   # feet in front of the rails' front (y 20), behind the uprights
# The tube: section 50 x 50, wall 2; every tube is one box less one through cutbox, so its edges are 2, 50 and its length: none falls in
# the 3 to 7 fillet trap. Volume by hand: section 50^2 - 46^2 = 384 mm^2.
SEC = UP * UP - (UP - 2 * T) ** 2
L_UP, L_FOOT, L_BAR = H - FH, FY1 - FY0, 2 * XI                                                      # 1750, 650, 900
TUBES = SEC * (2 * L_UP + 2 * L_FOOT + 2 * L_BAR)                                                    # 384 x 6600 = 2534400
RAILS = 4 * (2 * RS.XE * RS.SECTION + 2 * RS.EP_T * RS.EP_W * RS.H)                                  # 4 x 217668 = 870672
assert abs(SEC - 384.0) < 1e-9 and abs(TUBES - 2534400.0) < 1e-6 and abs(RAILS - 870672.0) < 1e-6


def build():
    P = Prims()
    for sx, s in ((-1, "l"), (1, "r")):
        x0 = -XO if sx < 0 else XI
        f = P.box(MAT, x0, FY0, 0.0, UP, L_FOOT, FH)                                            # the foot, a tube laid along y
        P.cutbox(MAT, x0 + T, FY0 - 1.0, T, UP - 2 * T, L_FOOT + 2.0, FH - 2 * T, f)
        P.collider(f"foot-{s}", x0, FY0, 0.0, UP, L_FOOT, FH)
        u = P.box(MAT, x0, 0.0, FH, UP, UP, L_UP)                                               # the upright on its foot
        P.cutbox(MAT, x0 + T, T, FH - 1.0, UP - 2 * T, UP - 2 * T, L_UP + 2.0, u)
        P.collider(f"upright-{s}", x0, 0.0, FH, UP, UP, L_UP)
    for z0, c in ((FH, "bar-bottom"), (H - UP, "bar-top")):
        b = P.box(MAT, -XI, 0.0, z0, L_BAR, UP, UP)                                             # a bar between the uprights' inner faces
        P.cutbox(MAT, -XI - 1.0, T, z0 + T, L_BAR + 2.0, UP - 2 * T, UP - 2 * T, b)
        P.collider(c, -XI, 0.0, z0, L_BAR, UP, UP)
    for k, zb in enumerate(ZB, start=1):
        n0 = len(P)
        library.place(P, dict(element="rail-suspension-shelving-1000", version=RAIL_V, tag=f"rail-{k}", parent="",
                              x=0.0, y=RY, z=zb - RS.Z0, yaw=0.0, params={}))
        for i in range(n0, len(P)):                                                             # the rail's colliders under its tag
            if P[i][0].startswith("collider:"): P[i] = (f"collider:rail-{k}-{P[i][0][9:]}",) + tuple(P[i][1:])
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
