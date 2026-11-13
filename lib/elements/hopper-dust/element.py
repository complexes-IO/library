#!/usr/bin/env python3
"""hopper-dust: dust hopper under a dust collector, our own design (OPERATING.md 12, own designs; inventory row own_design "yes":
"dust hopper under a dust collector"). It is the hopper of the dust collection system (lib/machines-factory.txt line 117:
dust-collector, duct-round, fan-exhaust, filter-cartridge, hopper-dust (own), ...). dust-collector is not built yet, so the hopper
stands on its own sizes: a flat top flange 1000 x 800 of four 2.0 strips 50 wide, on which the collector's housing seats; inside it a
V hopper of 2.0 sheet, as hopper-abrasive 1.0: front and back walls slope down and inward (run 250, drop 600, about 67 degrees from
the horizontal) to a slot 200 wide, the end walls stand vertical; under the slot a trough 150 deep with one round outlet Ø150 in its
bottom, a collar 100 long under it and a flat outlet ring Ø250 at the collar's end, where a dust drum or a discharge valve is fitted
later (not built). No fastener hole is cut, no seal is drawn. Every size is a design choice. No flow, capacity, load, dust or
explosion-protection claim. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hopper-dust", "1.0", "furniture"
TITLE = "dust hopper: flange 1000 x 800, V hopper 900 x 700 to a 200 slot, trough, Ø150 outlet with ring Ø250, sheet 2.0"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; dust-collector not built, so every size a design "
            "choice; no flow, capacity, load or explosion-protection claim; no vendor file opened")
ORIGIN = ("the top flange's top face (where the collector's housing seats) at the middle of the flange, x along its 1000 length, "
          "y along its 800 width; the hopper hangs toward -z")
COMMAND = "DUSTHOP"
PARAMS = dict()

T = 2.0                                         # sheet 2.0 everywhere, as hopper-abrasive: design choice
XO, YO = 500.0, 400.0                           # flange outside x -+500, y -+400: design choice
W = 50.0                                        # flange strips 50 wide: design choice
XI, YI = XO - W, YO - W                         # 450, 350: the hopper's top opening (end walls' outer faces, sloped walls' top edges)
ZT = -T                                         # -2: the flange's underside and the sloped walls' top edge
RUN, DROP = 250.0, 600.0                        # each sloped wall runs 250 inward over a 600 drop (about 67 degrees): design choice
LEN = math.hypot(RUN, DROP)                     # 650 along the slope
ZS = ZT - DROP                                  # -602: the slot's edges, y -100..100 (200 wide)
YS = YI - RUN                                   # 100
TROUGH = 150.0                                  # trough under the slot, 150 deep: walls z -752..-602, bottom plate z -754..-752
OUT_D, COLLAR_L = 150.0, 100.0                  # outlet Ø150 at the trough's middle, collar Ø154 (2.0 wall) 100 long: design choice
RING_D = 250.0                                  # outlet ring Ø250 x 2.0 at the collar's end, for a drum lid or a valve: design choice
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
    P.box(MAT, -XO, -YO, ZT, 2 * XO, W, T)                                              # flange, front strip (full length)
    P.box(MAT, -XO, YI, ZT, 2 * XO, W, T)                                               # flange, back strip
    for x in (-XO, XI): P.box(MAT, x, -YI, ZT, W, 2 * YI, T)                            # flange, side strips (between front and back)
    P.obox(MAT, (-XI + T, -YI, ZT), (1, 0, 0), DF, NF, 2 * (XI - T), LEN, T)            # front sloped wall, between the end walls
    P.obox(MAT, (XI - T, YI, ZT), (-1, 0, 0), DB, NB, 2 * (XI - T), LEN, T)             # back sloped wall
    for x0 in (-XI, XI - T):                                                            # end walls, cut along the sloped walls' undersides
        e = P.box(MAT, x0, -YI, ZS, T, 2 * YI, -ZS)
        P.cut(MAT, pt((x0 + T + 1, -YI, ZT), (-10.0, DF)), (-1, 0, 0), DF, tuple(-v for v in NF), T + 2, LEN + 20, 300.0, e)
        P.cut(MAT, pt((x0 - 1, YI, ZT), (-10.0, DB)), (1, 0, 0), DB, tuple(-v for v in NB), T + 2, LEN + 20, 300.0, e)
        P.box(MAT, x0, -YS, ZS - TROUGH, T, 2 * YS, TROUGH)                             # trough end
    for y in (-YS, YS - T): P.box(MAT, -XI + T, y, ZS - TROUGH, 2 * (XI - T), T, TROUGH)    # trough walls, between its ends
    zb = ZS - TROUGH - T                                                                # -754: trough bottom plate's underside
    b = P.box(MAT, -XI, -YS, zb, 2 * XI, 2 * YS, T)                                     # trough bottom, under its walls and ends
    P.hole(MAT, (0, 0, zb - 1), (0, 0, zb + T + 1), OUT_D / 2, b)                       # outlet
    zc = zb - COLLAR_L                                                                  # -854: the collar's end
    c = P.cyl(MAT, (0, 0, zb), (0, 0, zc), OUT_D / 2 + T)                               # outlet collar
    P.hole(MAT, (0, 0, zb + 1), (0, 0, zc - 1), OUT_D / 2, c)
    r = P.cyl(MAT, (0, 0, zc), (0, 0, zc - T), RING_D / 2)                              # outlet ring at the collar's end
    P.hole(MAT, (0, 0, zc + 1), (0, 0, zc - T - 1), OUT_D / 2, r)
    P.collider("flange", -XO, -YO, ZT, 2 * XO, 2 * YO, T)
    P.collider("funnel", -XI, -YI, ZS, 2 * XI, 2 * YI, ZT - ZS)
    P.collider("trough", -XI, -YS, zb, 2 * XI, 2 * YS, TROUGH + T)
    P.collider("outlet", -RING_D / 2, -RING_D / 2, zc - T, RING_D, RING_D, COLLAR_L + T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="side", az=320, el=15)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
