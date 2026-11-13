#!/usr/bin/env python3
"""strip-rubber-u-20x15: generic rubber U-section, our own vendor-neutral design of the ETIM 10.0 class EC010638 (Rubber U-section),
built unattended (OPERATING.md 12, generic elements; the EG019710 Profiles classes in generic.py's order by name, after
strip-rubber-t-30x20, this round). A solid black EPDM U-channel 20 wide and 15 high, flat bottom 3 thick, legs 3 thick, a clear
channel 14 wide and 12 deep: the open rubber channel a machine lays over the edge of a 14 mm board or plate, or along a run as a soft
liner. Wider and shallower than strip-clamping-8x15 (a 2.0 slot that grips sheet). Plain stock, cut to length (the `length`
parameter; a parameter stays out of the id, OPERATING.md 6). The class values (spec.md, "Class values") are design inputs; no
hardness, holding force, temperature or fire figure is claimed, and nothing moves. Every size is a design choice. No vendor file was
opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strip-rubber-u-20x15", "1.0", "rail"
TITLE = "Rubber U-section, generic, solid EPDM U-channel 20 x 15, flat bottom 3, legs 3, clamping width 14, black, plain, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic rubber U-section (ETIM 10.0 EC010638), a solid EPDM U-channel 20 wide x 15 high, flat bottom 3, "
            "legs 3, clamping width 14, black, not transparent, plain stock; class values are design inputs (spec.md); every size a "
            "design choice; no hardness, holding force, temperature or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the channel's centre plane y = 0, the bottom's underside z = 0; the run along +x, the channel open "
          "upward (+z), its floor at z 3, the legs' tops at z 15")
COMMAND = "RUBBERU"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius, set per primitive below (as the other profiles, mech-r106 / r131)

W, H = 20.0, 15.0                            # outside width (y), height (z): design choices (class features)
TB = 3.0                                     # bottom thickness (class feature): design choice
TL = 3.0                                     # each leg's thickness (not a class feature): design choice
CW = W - 2 * TL                              # 14: the clamping width, the clear channel between the legs
DEPTH = H - TB                               # 12: the channel's depth from the legs' tops to its floor
MAT = "M-GASKET"                             # EPDM, solid, black (lib/materials.csv epdm; render layer M-GASKET, the library's black rubber)

assert TB <= 3.0 and TL <= 3.0                                               # bottom ends and legs' tops: "short" edges, skipped by the gate
assert CW >= 8.0 and DEPTH >= 8.0 and W >= 8.0 and H >= 8.0                  # every other end-face edge clears the 3 to 7 mm free-corner trap (mech-r69)
assert abs(CW - 14.0) < 1e-9                                                 # the class's clamping width as designed
AREA = W * H - CW * DEPTH
assert abs(AREA - 132.0) < 1e-9                                              # by hand: 20 x 15 − 14 x 12 = 132 mm²
assert abs(AREA - (W * TB + 2 * TL * DEPTH)) < 1e-9                          # = 20 x 3 + 2 x 3 x 12


def build(length=1000.0):
    P = Prims(); L = float(length)
    assert L >= 100.0, "length 100 or more"
    body = P.box(MAT, 0, -W / 2, 0, L, W, H)                                                 # the section: one box ...
    P.cutbox(MAT, -1.0, -CW / 2, TB, L + 2.0, CW, DEPTH + 1.0, body)                          # ... less the channel (y ±7, z 3 up): one solid
    P.collider("bottom", 0, -W / 2, 0, L, W, TB)
    for s, nm in ((-1, "left"), (1, "right")):
        P.collider(f"leg-{nm}", 0, min(s * W / 2, s * CW / 2), TB, L, TL, DEPTH)
    for i in range(len(P)): P.radii[i] = FILLET_R                                            # the gate reads each primitive's radius (mech-r106)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=15, center=(0, 0, 7.5), height=35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
