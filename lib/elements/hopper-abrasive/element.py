#!/usr/bin/env python3
"""hopper-abrasive: abrasive hopper under a sandblast cabinet, our own design (OPERATING.md 12, own designs; inventory row own_design
"yes": "abrasive hopper under a blast cabinet"). It is the hopper of the sandblaster system (lib/machines-factory.txt line 106) and
is sized to cabinet-blast 1.0 through library.load: placed at the cabinet's own origin it hangs under the chamber's open floor at
z 850, between the cabinet's four legs. A rim of four 2.0 strips 50 wide lies under the chamber's walls (the strips stop at the legs);
inside it a V hopper of 2.0 sheet: front and back walls slope down and inward (run 300, drop 520, about 60 degrees from the
horizontal) to a slot 100 wide, the end walls stand vertical; under the slot a trough 100 deep with one round outlet Ø50 in its
bottom and a collar 50 long under it, where the blast gun's pickup or a metering valve is fitted later (not built). The fixing
to the cabinet, the grate and any seal are not drawn. Every size is a design choice. No flow, capacity, load or abrasive claim.
No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hopper-abrasive", "1.0", "furniture"
TITLE = "abrasive hopper for cabinet-blast: rim 1000 x 800, V hopper 900 x 700 to a 100 slot, trough, Ø50 outlet, sheet 2.0"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; sized to cabinet-blast 1.0 (library.load); every "
            "size a design choice; no flow, capacity or load claim; no vendor file opened")
ORIGIN = ("cabinet-blast's origin: the floor z = 0 at the middle of the cabinet's width x = 0, y = 0 the cabinet's front outer face; "
          "placed there, the hopper's rim meets the chamber's open floor at z 850")
COMMAND = "BLASTHOP"
PARAMS = dict()

CAB = library.load("cabinet-blast")             # cabinet-blast 1.0: chamber W 1000 x D 800, floor open at Z0 850, legs 50 x 50
T = 2.0                                         # sheet 2.0 everywhere, as the cabinet: design choice
XO, YD, ZR = CAB.W / 2, CAB.D, CAB.Z0           # rim outside x -+500, y 0..800, its top at z 850 (under the chamber's walls)
XI = CAB.W / 2 - CAB.LEG                        # 450: the hopper's end walls' outer faces, against the legs' inner faces
YF, YB = CAB.LEG, CAB.D - CAB.LEG               # 50, 750: the sloped walls' top edges, between the legs
ZT = ZR - T                                     # 848: the rim strips' underside and the sloped walls' top edge
RUN, DROP = 300.0, 520.0                        # each sloped wall runs 300 inward over a 520 drop (about 60 degrees): design choice
LEN = math.hypot(RUN, DROP)                     # 600.3 along the slope
ZS = ZT - DROP                                  # 328: the slot's edges, y 350..450 (100 wide)
YS0, YS1 = YF + RUN, YB - RUN                   # 350, 450
TROUGH = 100.0                                  # trough under the slot, 100 deep: walls z 228..328, bottom plate z 226..228
OUT_D, COLLAR_L = 50.0, 50.0                    # outlet Ø50 at the trough's middle, collar Ø54 (2.0 wall) 50 long: design choice
MAT = "M-STEEL-7035"

DF = (0.0, RUN / LEN, -DROP / LEN)              # front wall: down the slope
NF = (0.0, DROP / LEN, RUN / LEN)               # front wall: its inward normal (EX x DF)
DB = (0.0, -RUN / LEN, -DROP / LEN)             # back wall: down the slope
NB = (0.0, -DROP / LEN, RUN / LEN)              # back wall: its inward normal ((-EX) x DB)

def pt(o, *terms):
    """o plus each (scale, vector) term"""
    return tuple(o[i] + sum(k * v[i] for k, v in terms) for i in range(3))

def build():
    P = Prims()
    P.box(MAT, -XI, 0, ZT, 2 * XI, YF, T)                                               # rim, front strip (between the front legs)
    P.box(MAT, -XI, YB, ZT, 2 * XI, YD - YB, T)                                         # rim, back strip
    for x in (-XO, XI): P.box(MAT, x, YF, ZT, XO - XI, YB - YF, T)                      # rim, side strips (between the legs)
    P.obox(MAT, (-XI + T, YF, ZT), (1, 0, 0), DF, NF, 2 * (XI - T), LEN, T)             # front sloped wall, between the end walls
    P.obox(MAT, (XI - T, YB, ZT), (-1, 0, 0), DB, NB, 2 * (XI - T), LEN, T)             # back sloped wall
    for x0 in (-XI, XI - T):                                                            # end walls, cut along the sloped walls' undersides
        e = P.box(MAT, x0, YF, ZS, T, YB - YF, ZR - ZS)
        P.cut(MAT, pt((x0 + T + 1, YF, ZT), (-10.0, DF)), (-1, 0, 0), DF, tuple(-v for v in NF), T + 2, LEN + 20, 320.0, e)
        P.cut(MAT, pt((x0 - 1, YB, ZT), (-10.0, DB)), (1, 0, 0), DB, tuple(-v for v in NB), T + 2, LEN + 20, 320.0, e)
        P.box(MAT, x0, YS0, ZS - TROUGH, T, YS1 - YS0, TROUGH)                          # trough end
    for y in (YS0, YS1 - T): P.box(MAT, -XI + T, y, ZS - TROUGH, 2 * (XI - T), T, TROUGH)   # trough walls, between its ends
    zb = ZS - TROUGH - T                                                                # 226: trough bottom plate's underside
    b = P.box(MAT, -XI, YS0, zb, 2 * XI, YS1 - YS0, T)                                  # trough bottom, under its walls and ends
    yc = (YS0 + YS1) / 2                                                                # 400: the outlet's axis
    P.hole(MAT, (0, yc, zb - 1), (0, yc, zb + T + 1), OUT_D / 2, b)                     # outlet
    c = P.cyl(MAT, (0, yc, zb), (0, yc, zb - COLLAR_L), OUT_D / 2 + T)                  # outlet collar
    P.hole(MAT, (0, yc, zb + 1), (0, yc, zb - COLLAR_L - 1), OUT_D / 2, c)
    P.collider("rim", -XO, 0, ZT, 2 * XO, YD, T)
    P.collider("funnel", -XI, YF, ZS, 2 * XI, YB - YF, ZT - ZS)
    P.collider("trough", -XI, YS0, zb, 2 * XI, YS1 - YS0, TROUGH + T)
    P.collider("outlet", -OUT_D / 2 - T, yc - OUT_D / 2 - T, zb - COLLAR_L, OUT_D + 2 * T, OUT_D + 2 * T, COLLAR_L)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=320, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
