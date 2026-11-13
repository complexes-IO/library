#!/usr/bin/env python3
"""term-4mm: screw-clamp DIN-rail terminal block, feed-through (6.0 pitch, grey) or ground (5.0 pitch, green/yellow, rail-bonded).
Briefs: references/measure.md and measure-ground.md (the maker's 2-D drawings, p. 1; maker and part numbers in references/ only).
1.6: review term-4mm-1.3 findings 4 and 6: the figures the drawings don't give are marked here and on spec.md's Dimensions rows with
their class (clamp position and rail foot B, pocket and current bar C); the briefs' stale lines say what holds now. No shape change.
1.5: review term-4mm-1.4 finding 3: spec.md's end stop / end cover line carries its class (C). No shape change.
1.4: review elec-r21 finding 1: the figures come from a distributor's catalogue (its 2-D drawings and page tables), not the maker's
datasheet; BASELINE and the RANGE comment say so (review term-4mm-1.2.md finding 1 stays open). No shape change.
1.3: DOC-006 (OPERATING.md 6): no vendor name or part number in BASELINE, TITLE or the spec; the briefs carry them.
1.1: the two clamps are clamp-screw elements (cage, screw, contact zone, wire range 22-10 AWG / ground 22-12 AWG on file): a wire end's
state in the block is decided by toolkit/contact.py terminate(), not drawn."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "term-4mm", "1.6", "device"
TITLE = "4 mm2 screw-clamp terminal block, feed-through or ground, 35 mm rail"
TOOLKIT = "1.3"
BASELINE = "the 2-D drawings and page tables on file (a distributor's catalogue, not the maker's datasheet; review term-4mm-1.2.md finding 1 open): feed-through block 6.0 x 44.5 x 47.0 and ground block 5.0 x 43.5 x 44.5, p. 1 (references/measure.md, measure-ground.md)"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0; blocks stack along +x at the pitch"
COMMAND = "TERM"
PARAMS = dict(kind="feed", conditions="")
RANGE = dict(feed=(0.33, 5.26), ground=(0.33, 3.31))                 # mm²: 22-10 AWG and 22-12 AWG (the distributor catalogue's page tables, not the maker's datasheet: references/measure.md)
SIZES = dict(feed=(6.0, 44.5, 47.0), ground=(5.0, 43.5, 44.5))       # pitch (x), height off the rail (-y), length across the rail (z)

def build(kind="feed", conditions=""):
    """conditions: per clamp, '1:corroded' (1 = the top clamp, 2 = the bottom one)"""
    P = Prims(); w, h, l = SIZES[kind]; mat = "M-GREY-PA" if kind == "feed" else "M-GREEN-YELLOW"
    cond = {k.strip(): v.strip() for k, v in (p.split(":", 1) for p in str(conditions or "").replace(";", "/").split("/") if ":" in p)}
    body = P.box(mat, 0, -h, -l / 2, w, h, l)                                            # body
    stripe = P.box("M-YELLOW-PA", 0, -h - 0.3, -l / 2 + 4, w, 0.3, 8) if kind == "ground" else None   # yellow stripe on the front
    cl = library.load("clamp-screw"); _, cL, ch = cl.CAGE; cw = 5.1 if kind == "feed" else 4.5; wx, wz = min(cl.WINDOW[0], cw - 1.0), cl.WINDOW[1]   # ground cage 4.5 (ground STEP)
    y_ax = -h + 9.0                                                                       # the wire axis: the screw head stands 0.4 proud of the front; class B (spec.md Dimensions, clamp position)
    z_m = l / 2 - 4.25                                                                    # the cage's mouth, under the wire entry (cage centre 8.0 in from the end); class B, as y_ax
    for n, sgn in (("1", 1.0), ("2", -1.0)):                                              # 1: top clamp, wire goes in downward; 2: bottom clamp, upward
        zm = sgn * z_m; zc = zm - sgn * cL / 2
        P.cutbox("M-GASKET", w / 2 - cw / 2, y_ax - 6.4, min(zm, zm - sgn * cL), cw, ch, cL, body)                           # the cage's pocket, 6.4 deep: class C (spec.md Dimensions, inside the block)
        P.cutbox("M-GASKET", w / 2 - wx / 2, y_ax - wz / 2, min(zm - sgn * (cL + 3.0), sgn * (l / 2 + 1.0)), wx, wz, cL + 3.0 + (l / 2 + 1.0 - z_m), body)   # wire entry, through the end face
        P.hole("M-GASKET", (w / 2, -h - 1.0, zc), (w / 2, y_ax - 6.4, zc), 2.1, body)                                         # screwdriver access
        if stripe is not None and -l / 2 + 4 - 2.1 < zc < -l / 2 + 12 + 2.1: P.hole("M-GASKET", (w / 2, -h - 1.0, zc), (w / 2, -h + 1.0, zc), 2.1, stripe)
        library.place(P, dict(element="clamp-screw", version="1.1", tag=f"clamp-{n}", parent="", x=w / 2, y=y_ax, z=zm, yaw=0.0 if sgn > 0 else 180.0, pitch=-90.0 if sgn > 0 else 90.0,
                              params=dict(size_min=RANGE[kind][0], size_max=RANGE[kind][1], condition=cond.get(n, "ok"), cage_w=cw)))
    P.box("M-CU", w / 2 - 0.85, y_ax + 2.5, -z_m + cL, 1.7, 1.5, 2 * (z_m - cL))         # current bar between the cages (STEP: 5.2 x 1.7 x 23.4); 1.7 x 1.5 class C (spec.md Dimensions, inside the block)
    P.box("M-GREY-PA" if kind == "feed" else "M-ZINC", w / 2 - 1.5, -3.0, -20.5, 3.0, 3.0, 41.0)   # rail foot / bonding spring (ground: metal); class B (spec.md Dimensions, rail foot)
    if kind == "ground": P.cutbox("M-GASKET", w / 2 - 1.5, -3.0, -20.5, 3.0, 4.0, 41.0, body)      # the metal foot shows through the back (no shared face)
    P.collider("env", 0, -h - 0.4, -l / 2, w, h + 0.4, l)
    return P

PREVIEWS = [dict(name="front three-quarter feed-through", az=250, el=20), dict(name="ground variant", az=250, el=20, params=dict(kind="ground")),
            dict(name="strip ten blocks and two ground", az=250, el=20, params=dict(kind="feed"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
