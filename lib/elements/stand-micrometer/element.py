#!/usr/bin/env python3
"""stand-micrometer: micrometer stand, our own design, built unattended (OPERATING.md 12, own designs; inventory row own_design
"yes": "micrometer stand", machines-factory.txt micrometer; request mech-8's answer: no ETIM class on file fits, so an own design as
panel-clamp and stand-magnetic). A flat base block that stands on the bench, a round post on it, a fork on the post's top, and a
tilting head between the fork's cheeks (node `head`: a clamp block with a slot across its top that seats the micrometer's frame,
turning about a horizontal pin through the cheeks so the micrometer's anvils face the hand). The micrometer is not placed
(micrometer is a generic row, not built); the tilt pin, the tilt lock and the clamp's thumb screw are not drawn: this is the plain
stand. Every size below is a design choice. No load, no stiffness and no accuracy claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "stand-micrometer", "1.1", "device"
TITLE = "micrometer stand, base 120 x 90 x 20, post Ø16 x 130, fork on the post's top, tilting clamp head 24 x 26 x 60 with an 8 slot for the micrometer's frame"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched and no class on file fits (request mech-8); every "
            "size a design choice; the head's slot drawn 8 wide for the micrometer frame it seats, its fit NOT ON FILE (B): "
            "ISO 3611 (source wanted); no load, "
            "no stiffness and no accuracy claim; no vendor file opened")
ORIGIN = ("the base's underside (on the bench) z = 0, on the post's axis x = 0, y = 0; the base's long sides along x; the head's "
          "tilt axis along y through the fork's cheeks; the head upright at rest, its slot along x on top")
COMMAND = "STANDMIC"
PARAMS = dict()
BASE_X, BASE_Y, BASE_Z = 120.0, 90.0, 20.0        # the base block, x +-60, y +-45, z 0..20: design choice
POST_R, POST_TOP = 8.0, 150.0                     # post Ø16 from the base's top (z 20) to z 150 (130 long): design choice
FORK_X, FORK_Y, FORK_BASE = 20.0, 40.0, 10.0      # the fork's base block 20 (x) x 40 (y) x 10 on the post's top face (z 150..160): design choice
CHEEK_T, CHEEK_H = 6.0, 30.0                      # two cheeks 20 (x) x 6 (y) x 30 up from the fork's base (z 160..190), at y +-14..+-20: design choice
PIN_Z = 180.0                                     # the tilt axis, along y through the cheeks at z 180 (the pin is not drawn): design choice
HEAD_X, HEAD_Y, HEAD_Z0, HEAD_H = 24.0, 26.0, 168.0, 60.0   # the clamp head 24 (x) x 26 (y, 1 clear of each cheek) x 60 (z 168..228): design choice
SLOT_W, SLOT_D = 8.0, 30.0                        # the micrometer frame's slot across the head's top: 8 wide (y), 30 deep, through along x: drawn so; its fit to the frame NOT ON FILE (B): ISO 3611 (features.csv, kind own; spec.md What it meets)
TILT = 30.0                                       # the head tilts -30..30 degrees about the pin: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; B = "M-SILVER"                           # base and head painted steel; post and fork bright steel
    P.box(S, -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_Z)                                            # the base block
    P.collider("base", -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_Z)
    P.cyl(B, (0, 0, BASE_Z), (0, 0, POST_TOP), POST_R)                                                       # the post, standing on the base
    P.collider("post", -POST_R, -POST_R, BASE_Z, 2 * POST_R, 2 * POST_R, POST_TOP - BASE_Z)
    P.box(B, -FORK_X / 2, -FORK_Y / 2, POST_TOP, FORK_X, FORK_Y, FORK_BASE)                                  # the fork's base, on the post's top face
    for y in (-FORK_Y / 2, FORK_Y / 2 - CHEEK_T):
        P.box(B, -FORK_X / 2, y, POST_TOP + FORK_BASE, FORK_X, CHEEK_T, CHEEK_H)                              # a cheek, up from the fork's base
    P.collider("fork", -FORK_X / 2, -FORK_Y / 2, POST_TOP, FORK_X, FORK_Y, FORK_BASE + CHEEK_H)
    Hd = f"node:head|{S}"
    head = P.box(Hd, -HEAD_X / 2, -HEAD_Y / 2, HEAD_Z0, HEAD_X, HEAD_Y, HEAD_H)                               # the clamp head, between the cheeks (the node's first box)
    z_top = HEAD_Z0 + HEAD_H                                                                                 # 228
    P.cutbox(Hd, -HEAD_X / 2 - 1, -SLOT_W / 2, z_top - SLOT_D, HEAD_X + 2, SLOT_W, SLOT_D + 1, head)         # the frame's slot, across the top, through along x
    P.pivot("head", "rotate", (0, 0, PIN_Z), axis=(0, 1, 0), range=(-TILT, TILT))
    P.collider("clamp", -HEAD_X / 2, -HEAD_Y / 2, HEAD_Z0, HEAD_X, HEAD_Y, HEAD_H)                           # the head at rest
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
