#!/usr/bin/env python3
"""term-endplate: end cover for a term-4mm strip, our own design. A plate of the block's own profile that closes the open side of the
last block; the profile is term-4mm's figures on file, the thickness a design choice. term-4mm 1.2 leaves the end cover
unmodelled: this is it."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "term-endplate", "1.0", "plate"
TITLE = "end cover for a term-4mm strip (feed-through or ground profile), 2.0 thick"
TOOLKIT = "1.3"
BASELINE = "our own design (complexes.org): thickness a design choice; profile (height and length) from term-4mm 1.2 (SIZES) on file; the rail clip is NOT ON FILE"
ORIGIN = "term-4mm's frame: back face on the rail crown y = 0, rail centreline z = 0; the plate's left face x = 0, thickness along +x"
COMMAND = "TEND"
PARAMS = dict(kind="feed")

T = 2.0                        # plate thickness (x): design choice; a strip of n blocks with one end plate is n x pitch + 2.0 long
TERM, TERM_VERSION = "term-4mm", "1.2"

def profile(kind):
    t = library.load(TERM, TERM_VERSION)
    _, h, l = t.SIZES[kind]                                        # height off the rail (-y), length across the rail (z)
    return h, l

def build(kind="feed"):
    P = Prims(); h, l = profile(kind)
    P.box("M-GREY-PA", 0.0, -h, -l / 2, T, h, l)
    P.collider("env", 0.0, -h, -l / 2, T, h, l)
    return P

PREVIEWS = [dict(name="feed-through profile", az=250, el=20), dict(name="ground profile", az=250, el=20, params=dict(kind="ground"))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
