#!/usr/bin/env python3
"""gl-xr-1: the institute's own display glasses, a prop for the site and the virtual campus: a generic wayfarer-style frame with
thick temples (the electronics housing), dark lenses that the twin treats as screens. Our design; not a vendor's shape."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
from toolkit import library, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "gl-xr-1", "1.2", "prop"
TITLE = "display glasses, wayfarer frame, thick temples, dark lenses as screens"
TOOLKIT = "1.3"
BASELINE = "display-glasses envelope from a published spec sheet (155 x 50.1 x 56.5 mm folded, 79 g, IPD 64 +/- 6, diopter dials, magnetic nose pads); the shape is our own"
ORIGIN = "bridge centre on the front face; lenses in the xz plane, temples toward +y (the wearer's side)"
COMMAND = "GLXR"
PARAMS = dict(fold=0.0)                                   # temple fold angle, degrees (0 open)

LENS_W, LENS_H, BRIDGE, TEMPLE = 56.0, 42.0, 10.0, 150.0   # from the published envelope: 155 wide x 50 high folded, IPD 64-70
FRAME = dict(w=5.5, d=4.5, r=1.8)                         # frame tube section: radial x depth
TEMPLE_SEC = dict(w=4.0, h=8.0, r=1.5)                    # temple section: thickness x height
CX = BRIDGE / 2 + LENS_W / 2                              # lens centre x

def lens_corners(off=0.0):
    """wayfarer lens outline corners (x, z) relative to the lens centre, outer-top highest; off pushes the outline outward"""
    return [(-26 - off, -19 - off), (24 + off * 0.4, -17 - off), (28 + off, 21 + off), (-25 - off, 18 + off)], [12 + off, 16 + off, 6 + off, 4.5 + off]

def build(fold=0.0):
    P = Prims(); F = "node:frame|M-BLACK-PA"
    prof = SW.rounded_rect_profile(FRAME["d"], FRAME["w"], FRAME["r"])
    for s in (-1, 1):
        c, r = lens_corners(3.0); o = SW.rounded_outline([(s * x, z) for x, z in c][::s], r[::s], 8)
        path = [(s * CX + x, 0.0, z) for x, z in o] if s > 0 else [(s * CX + x, 0.0, z) for x, z in o]
        pts = SW.resample(path + path[:1], 2.0)
        P.mesh(F, SW.sweep(pts, prof, closed=True))                                              # frame rim
        lc, lr = lens_corners(0.0); lo = SW.rounded_outline([(s * x, z) for x, z in lc][::s], lr[::s], 8)
        P.mesh(f"node:lens-{'r' if s > 0 else 'l'}|M-LENS-DARK", SW.plate(lo, lambda a, b: (s * CX + a, 1.0, b), 1.5, (0, 1, 0)))   # lens plate
        # brow bar: the optics housing, 12 deep along the top of the rim from the inner-top to the outer-top corner
        xi, xo = s * (CX - 23), s * (CX + 26); zb = 23.0
        bp = SW.resample([(xi, 6.0, zb - 1.5), (s * CX, 6.0, zb), (xo, 6.0, zb - 1.0)], 2.0)
        P.mesh(F, SW.sweep(bp, SW.rounded_rect_profile(12.0, 8.0, 2.5)))
        dx = s * (CX + 12); P.cyl("node:dial-%s|M-GREY-PA" % ("r" if s > 0 else "l"), (dx, 6.0, zb + 2.0), (dx, 6.0, zb + 5.0), 3.5)   # diopter dial
        # hinge block and temple
        hx = s * (CX + LENS_W / 2 + 3.0); hz = 15.0
        P.box("node:frame|M-BLACK-PA", min(hx, hx + s * 5), 0, hz - 5, 5, 9, 12)
        a = math.radians(fold); tp = f"node:temple-{'r' if s > 0 else 'l'}|M-BLACK-PA"
        hinge = np.array([hx, 9.0, hz]); xd0 = np.array([s * math.cos(a), math.sin(a), 0.0]); base = hinge + 4.5 * xd0   # turns about the inner rear corner (1.1)
        ydir = np.array([-s * math.sin(a), math.cos(a), 0.0]); xdir = np.array([s * math.cos(a), math.sin(a), 0.0])
        def tp_(y, x_out, z): return tuple(base + ydir * y + xdir * x_out + np.array([0, 0, z]))
        path = [tp_(0, 0, 0), tp_(14, 0.5, 0), tp_(40, 1.5, -0.5), tp_(95, 1.5, -1.5), tp_(112, 1.0, -4), tp_(125, 0, -9), tp_(TEMPLE - 7, -2, -17)]
        pts = SW.resample(path, 2.5)
        tprof = SW.rounded_rect_profile(TEMPLE_SEC["w"], TEMPLE_SEC["h"], TEMPLE_SEC["r"]); P.mesh(tp, SW.sweep(pts, tprof, up=(0, 0, 1)))
        hp = tp_(2, 0, 0); P.mesh(tp, SW.sweep(SW.resample([tp_(1, 0, 0), tp_(38, 1.0, 0)], 2.0), SW.rounded_rect_profile(9.0, 12.0, 3.0)))   # housing
        P.box("M-TITANIUM", min(hx, hx + s * 1.5) - s * 0.2, 2.0, hz - 2.5, 1.5, 4, 5)              # hinge pin cover, 0.2 proud of the block (GEO-050)
    bp = SW.resample([(-6, 0, 17), (-2.5, 0, 20), (2.5, 0, 20), (6, 0, 17)], 1.5)
    P.mesh(F, SW.sweep(bp, SW.rounded_rect_profile(FRAME["d"], 5.5, 2.0)))                           # bridge
    for s in (-1, 1): P.mesh(F, SW.sweep(SW.resample([(s * 6.5, 3, 8), (s * 7, 10, 0)], 1.5), SW.circle_profile(1.6, 10)))   # nose pad arms
    for s in (-1, 1): P.box("M-GREY-PA", min(s * 7.5, s * 7.5 - s * 2.5), 9.5, -5, 2.5, 3, 9)             # nose pads
    P.box("M-TITANIUM", CX + 2, -0.6, 22.5, 6, 1.0, 1.5)                                             # the small status mark on the right brow
    P.pivot("frame", "fixed", (0, 0, 0))
    for s in (-1, 1):
        sd = "r" if s > 0 else "l"; hx = s * (CX + LENS_W / 2 + 3.0)
        P.pivot(f"lens-{sd}", "emissive", (s * CX, 1.0, 0), axis=(0, -1, 0), range=(0, 1))                  # the screen
        P.pivot(f"temple-{sd}", "rotate", (hx, 9.0, 15.0), axis=(0, 0, 1), range=(0, 74 * s))                 # hinge at the inner rear corner; folds to 74 where it meets the brow housing (1.1)
        P.pivot(f"dial-{sd}", "rotate", (s * (CX + 12), 6.0, 25.0), axis=(0, 0, 1), range=(0, 300))
    P.collider("front", -73, -2.5, -24, 146, 14, 50); P.collider("temple-l", -78, 9, -18, 10, 141, 36); P.collider("temple-r", 68, 9, -18, 10, 141, 36)
    return P

PREVIEWS = [dict(name="front", az=270, el=4), dict(name="three-quarter", az=238, el=14), dict(name="side temples and housing", az=180, el=8),
            dict(name="folded temples", az=238, el=14, params=dict(fold=95))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
