#!/usr/bin/env python3
"""stand-magnetic: magnetic indicator stand, our own design, built unattended (OPERATING.md 12, own designs; inventory row
own_design "yes": "magnetic indicator stand", machines-factory.txt dial-indicator; request mech-8's answer: no ETIM class on file
fits, so an own design as panel-clamp). A switchable magnetic base (a steel block whose underside and -y side face are the pole
faces; its magnet and rotor are not drawn) with an on/off lever on its -x end face (node `switch`: the knob and its lever, turning
90 degrees about the knob's axis), a round post standing on the base's top face, and a swivel arm on the post's top (node `arm`:
a square hub, a round boom and a clamp block, turning about the post's axis) whose clamp block has a vertical bore for a dial
indicator's stem. The dial indicator is not placed (dial-indicator is not built); the clamp screw, the arm's elbow and fine
adjuster that a stand may have, and the base's V groove are not drawn: this is the plain stand. Every size below is a design
choice. No holding force, no load and no accuracy claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "stand-magnetic", "1.1", "device"
TITLE = "magnetic indicator stand, switchable base 50 x 60 x 55 with on/off lever, post Ø12 x 200, swivel arm Ø10 on the post's top reaching 185, clamp block with Ø8 bore for the indicator's stem"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched and no class on file fits (request mech-8); every "
            "size a design choice but the clamp bore's fit to the indicator's stem, a figure ISO 463 tabulates and the document is "
            "not on file (class B, source wanted; the bore drawn Ø8 until it is); no holding force, "
            "no load and no accuracy claim; no vendor file opened")
ORIGIN = ("the base's underside (the pole face that seats on the work) z = 0, on the post's axis x = 0, y = 0; the base's long "
          "sides along y; the switch lever on the -x end face, up at rest (off); the arm along +x at rest and turning about z")
COMMAND = "STANDMAG"
PARAMS = dict()
BASE_X, BASE_Y, BASE_Z = 50.0, 60.0, 55.0         # the magnetic base block, x +-25, y +-30, z 0..55: design choice
KNOB_R, KNOB_L, KNOB_Z = 11.0, 12.0, 30.0         # on/off knob Ø22, 12 long, proud of the -x end face at z 30 (its axis along x): design choice
LEV_L, LEV_W, LEV_H = 8.0, 6.0, 22.0              # the lever on the knob's outer face: 8 (x) x 6 (y) x 22 (z), from the axis upward at rest: design choice
POST_R, POST_TOP = 6.0, 255.0                     # post Ø12 from the base's top (z 55) to z 255 (200 long): design choice
HUB, HUB_H = 30.0, 25.0                           # the arm's square hub 30 x 30 x 25 on the post's top face (z 255..280): design choice
BOOM_R, BOOM_X1 = 5.0, 165.0                      # the boom Ø10 along +x from the hub's face (x 15) to x 165, on the hub's mid-height z 267.5
BLK_X, BLK_Y, BLK_Z = 20.0, 20.0, 24.0            # the clamp block 20 x 20 x 24 on the boom's end (x 165..185, z 255.5..279.5), 0.5 inside the hub's faces
BORE_D = 8.0                                      # the clamp's bore along z for the indicator's stem: the stem's diameter and tolerance are ISO 463's (not on file, class B source wanted, spec.md What it meets); drawn Ø8 until the document is on file (features.csv, kind own)
SWING = 180.0                                     # the arm turns -180..180 about the post's axis: design choice
SW_ANGLE = 90.0                                   # the lever turns 0 (off, up) to 90 (on) about the knob's axis: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; B = "M-SILVER"; K = "M-BLACK-PA"      # base painted steel; post and arm bright steel; knob moulded
    P.box(S, -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_Z)                                            # the magnetic base block
    P.collider("base", -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_Z)
    P.cyl(B, (0, 0, BASE_Z), (0, 0, POST_TOP), POST_R)                                                       # the post, standing on the base
    P.collider("post", -POST_R, -POST_R, BASE_Z, 2 * POST_R, 2 * POST_R, POST_TOP - BASE_Z)
    W = lambda m: f"node:switch|{m}"
    x0 = -BASE_X / 2                                                                                          # the -x end face
    P.cyl(W(K), (x0 - KNOB_L, 0, KNOB_Z), (x0, 0, KNOB_Z), KNOB_R)                                           # the knob, face to face on the end face
    P.box(W(K), x0 - KNOB_L - LEV_L, -LEV_W / 2, KNOB_Z, LEV_L, LEV_W, LEV_H)                                 # the lever, up from the axis at rest (off)
    P.pivot("switch", "rotate", (x0, 0, KNOB_Z), axis=(1, 0, 0), range=(0, SW_ANGLE))
    P.collider("lever-knob", x0 - KNOB_L - LEV_L, -KNOB_R, KNOB_Z - KNOB_R, KNOB_L + LEV_L, 2 * KNOB_R, KNOB_R + LEV_H)
    A = lambda m: f"node:arm|{m}"
    P.box(A(B), -HUB / 2, -HUB / 2, POST_TOP, HUB, HUB, HUB_H)                                                # the hub, on the post's top face (the node's first box)
    z_boom = POST_TOP + HUB_H / 2                                                                             # 267.5
    P.cyl(A(B), (HUB / 2, 0, z_boom), (BOOM_X1, 0, z_boom), BOOM_R)                                           # the boom, from the hub's +x face
    blk = P.box(A(B), BOOM_X1, -BLK_Y / 2, z_boom - BLK_Z / 2, BLK_X, BLK_Y, BLK_Z)                           # the clamp block, on the boom's end face
    bx = BOOM_X1 + BLK_X / 2
    P.hole(A(B), (bx, 0, z_boom - BLK_Z / 2 - 1), (bx, 0, z_boom + BLK_Z / 2 + 1), BORE_D / 2, blk)          # the bore for the indicator's stem, along z
    P.pivot("arm", "rotate", (0, 0, POST_TOP), axis=(0, 0, 1), range=(-SWING, SWING))
    P.collider("boom", -HUB / 2, -HUB / 2, POST_TOP, BOOM_X1 + BLK_X + HUB / 2, HUB, HUB_H)                   # the arm at rest: hub, boom and block
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
