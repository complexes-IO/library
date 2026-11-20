#!/usr/bin/env python3
"""reel-cable-630: generic cable storage and transport reel, flanges Ø630, 500 wide over the flanges, our own vendor-neutral design of the
ETIM 10.0 class EC004844 (Storage/transport reel; synonyms Cable reel, Cable storage reel, Cable transport reel, Storage reel for cable,
Transport reel for cable), built unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a tier-2 class
walked by name after the storage partition set, lib/rounds/mech/r168.md). Two wooden flanges Ø630 x 25 on a wooden barrel Ø315 x 450
(drawn as one solid: its staves and spokes are not drawn), a Ø50 arbor bore through all three on the reel's axis, and one Ø30 drive-pin
hole in each flange at a radius of 220. It is the reel rack-cable-drum-1000 1.0 carries (foundation first, OPERATING.md 12: the rack is
built and gated, so its figures are read with library.load and the fit is asserted here: the reel's diameter and width under the rack's
largest drum, the bore over the rack's Ø40 axle). No element is placed or redrawn. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC004844 rows): spec.md gives the design values under plain names, as rack-cable-drum-1000
does. Every size is a design choice; no drum standard is on file and none is claimed. No load, mass or safety claim. No vendor file
opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "reel-cable-630", "1.0", "furniture"
TITLE = ("cable storage and transport reel, generic, wooden flanges Ø630 x 25 on a barrel Ø315, 500 wide over the flanges, arbor bore "
         "Ø50")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic storage/transport reel (ETIM 10.0 EC004844), two wooden flanges Ø630 x 25 on a wooden barrel Ø315 "
            "x 450 drawn as one solid, 500 wide over the flanges, a Ø50 arbor bore through flanges and barrel, one Ø30 drive-pin hole in "
            "each flange at r 220; sized to ride on rack-cable-drum-1000 1.0's Ø40 axle (read with library.load, fit asserted); class "
            "features not on file, design values under plain names (spec.md); every size a design choice; the cable not drawn; no load, "
            "mass or safety claim; no vendor file opened")
ORIGIN = ("the reel's axis, midway between the flanges' outer faces: x along the axis (the flanges' outer faces x -250 and 250), y and "
          "z across it; on rack-cable-drum-1000 the origin goes on an axle's axis, standing on the floor at z = 315 (the flanges' rims)")
COMMAND = "RLCB630"
PARAMS = dict()

RACK_V = "1.0"
RK = library.load("rack-cable-drum-1000", RACK_V)   # the rack that carries the reel (its axle and largest drum: the fit)

DF = 630.0                                      # design: the flanges' diameter
TF = 25.0                                       # design: the flanges' thickness (wood)
DB = 315.0                                      # design: the barrel's diameter, half the flange's, the cable's smallest wrap
W = 500.0                                       # design: the reel's width over the flanges' outer faces
LT = W - 2 * TF                                 # 450: the traverse, the barrel's length between the flanges' inner faces
RBO = 25.0                                      # design: the arbor bore Ø50
RDP = 15.0                                      # design: the drive-pin hole Ø30, one in each flange
RPC = 220.0                                     # design: the drive-pin hole's radius from the axis
MAT = "M-BROWN"                                 # wood (flanges and barrel)

RF, RBL = DF / 2, DB / 2                        # 315, 157.5
XF = W / 2                                      # 250: the flanges' outer faces x +-250
XI = XF - TF                                    # 225: their inner faces x +-225
assert DF <= RK.D_MAX                                                                               # 630 <= 700: under the rack's largest drum
assert W <= RK.W_MAX and W < 2 * RK.XI                                                              # 500 <= 960, inside the frames' 1000
assert RBO - RK.RA >= 2.0                                                                           # 5 clear all round on the rack's Ø40 axle: the reel turns on it
assert RF <= RK.ZA[0] - RK.UP                                                                       # 315 <= 400: on the lower axle the rim clears the floor tie's top
assert RK.ZA[1] - RK.ZA[0] >= DF                                                                    # 750 >= 630: two reels, one on each axle, clear each other
assert RBL + RDP + 20.0 <= RPC <= RF - RDP - 20.0                                                   # the drive hole 47.5 outside the barrel, 80 inside the rim
assert RBO < RBL and TF >= 8.0 and LT > 0                                                           # the bore inside the barrel; no edge in the 3 to 7 fillet trap
# Volume by hand: the flanges 2 x pi x 315^2 x 25, the barrel pi x 157.5^2 x 450, less the bore pi x 25^2 x 500 and the two drive holes
# 2 x pi x 15^2 x 25.
VOL = math.pi * (2 * RF ** 2 * TF + RBL ** 2 * LT - RBO ** 2 * W - 2 * RDP ** 2 * TF)
assert abs(VOL - 49638146.0) < 1.0


def build():
    P = Prims()
    fl = P.cyl(MAT, (-XF, 0.0, 0.0), (-XI, 0.0, 0.0), RF)                                       # the left flange
    br = P.cyl(MAT, (-XI, 0.0, 0.0), (XI, 0.0, 0.0), RBL)                                       # the barrel between the flanges' inner faces
    fr = P.cyl(MAT, (XI, 0.0, 0.0), (XF, 0.0, 0.0), RF)                                         # the right flange
    P.hole(MAT, (-XF - 1.0, 0.0, 0.0), (-XI + 1.0, 0.0, 0.0), RBO, fl)                          # the arbor bore, through each part
    P.hole(MAT, (-XI - 1.0, 0.0, 0.0), (XI + 1.0, 0.0, 0.0), RBO, br)
    P.hole(MAT, (XI - 1.0, 0.0, 0.0), (XF + 1.0, 0.0, 0.0), RBO, fr)
    P.hole(MAT, (-XF - 1.0, 0.0, RPC), (-XI + 1.0, 0.0, RPC), RDP, fl)                          # the drive-pin holes, above the axis
    P.hole(MAT, (XI - 1.0, 0.0, RPC), (XF + 1.0, 0.0, RPC), RDP, fr)
    P.collider("reel", -XF, -RF, -RF, W, DF, DF)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
