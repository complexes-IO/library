#!/usr/bin/env python3
"""marker-terminal: terminal marker for term-4mm, our own design. One white tag per block on the block's front face, between its two screw
openings; `n` tags make a strip over n neighbouring blocks of the same kind. The pitch and the block's height are term-4mm's figures on file;
the terminal number is a decal."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "marker-terminal", "1.0", "plate"
TITLE = "terminal marker for term-4mm (feed-through or ground), one tag per block, n in a strip"
TOOLKIT = "1.3"
BASELINE = "our own design (complexes.org): tag sizes are design choices; pitch and block height from term-4mm 1.2 (SIZES) on file; the marker groove is NOT ON FILE"
ORIGIN = "term-4mm's frame: back face on the rail crown y = 0, rail centreline z = 0, left face of the first block x = 0; tags on the blocks' front faces"
COMMAND = "MRKT"
PARAMS = dict(kind="feed", n=1)

TAG = (0.15, 2.0, 10.0)        # side clearance to the block's faces (each side), thickness, length along z: design choice
TERM = "term-4mm"              # the block it fits, pinned at the version its figures were read from
TERM_VERSION = "1.2"

def term_sizes(kind):
    t = library.load(TERM, TERM_VERSION)
    return t.SIZES[kind]                                       # (pitch x, height off the rail -y, length z)

def build(kind="feed", n=1):
    P = Prims(); w, h, l = term_sizes(kind); c, t, L = TAG
    for i in range(int(n)):
        P.box("M-WHITE-PA", i * w + c, -h - t, -L / 2, w - 2 * c, t, L)
    P.collider("env", 0.0, -h - t, -L / 2, int(n) * w, t, L)
    return P

PREVIEWS = [dict(name="feed-through tag", az=250, el=20), dict(name="ground tag", az=250, el=20, params=dict(kind="ground")),
            dict(name="strip of ten tags", az=250, el=30, params=dict(n=10))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
