#!/usr/bin/env python3
"""psu-24v-2a4: 24 V DC DIN-rail switching power supply, 60 W. Brief: references/measure.md (maker's 2-D drawing p. 1:
32 x 90 x 110, clip 3.3, rail centreline 44.7 from one end, DC OK green / DC LOW red / V.ADJ).
1.3 (elec-r29; lib/requests/core/elec-pin-nodes-2026-11-11.md, request panel-4 item 1): every terminal is a port node t-<mark> (BEH-020: the
twin's probe and the panel's wire routes end on it), its pivot at the wire opening's mouth on the end face, axis the way the wire goes in.
The terminals keep toolkit din.terminal_row's shape (screw head, slot cut into the end face, dark slot) drawn here per terminal so each
screw head carries its node; nothing moves (a minor, OPERATING.md 7)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "psu-24v-2a4", "1.4", "device"
TITLE = "24 V DC power supply 2.5 A / 60 W, plastic housing, 35 mm rail"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet (references/measure.md: 2-D drawing p. 1, 32.0 x 90.0 x 110.0, 93.3 with the clip; sheet p. 1-2)"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0 (44.7 from the lower end), left face x = 0, body toward -y"
COMMAND = "PSU"
PARAMS = {}
W, H, D0, CLIP = 32.0, 90.0, 110.0, 3.3
D = D0 - 7.5                                      # the drawing's 110 is the full depth including the 7.5 clip region behind the crown
Z0 = -44.7                                        # lower end of the body
PROUD = 0.2                                       # front features 0.2 proud: a design choice so the envelope equals the STEP read-back's overall 110.2
                                                  # (measure.md: one solid, extents only); the feature giving the STEP its 0.2 is NOT ON FILE (C), spec "overall"
PITCH = 7.5                                       # terminal pitch: Assumption (B), the sheet's terminal page not read (measure.md "Ports")
TERMINALS = ((True, (("L", "t-l"), ("N", "t-n"), ("PE", "t-pe"))),                     # input row at the top end: marks and port nodes (brief "Ports": L / N / ground)
             (False, (("+V", "t-vp"), ("-V", "t-vn"), ("+V'", "t-vp2"), ("-V'", "t-vn2"))))   # output row at the bottom: +V -V +V -V (the order is the class B row of spec.md); ' names the second of a pair
OPENING, SLOT_DEPTH, SCREW_R = (3.6, 5.0), 9.0, 2.2                                   # din.terminal_row's figures (toolkit 1.3), kept

def terminal(P, node, cx, y_face, z_edge, up, hb):
    """one screw terminal as din.terminal_row draws it (screw head on the front, the wire entry a slot din.SLOT deep cut into the end
    face with the dark slot filling it), the screw head named as the port node; the pivot at the slot's mouth, axis the way the wire goes in"""
    s = 1 if up else -1
    P.cyl(f"node:{node}|M-ZINC", (cx, y_face, z_edge - s * 6.0), (cx, y_face - 1.2, z_edge - s * 6.0), SCREW_R)       # screw head
    z0 = z_edge - (din.SLOT if up else 0.0)
    P.cutbox("M-GASKET", cx - OPENING[0] / 2, y_face + 2.0, z0 - (0.0 if up else 1.0), OPENING[0], SLOT_DEPTH, din.SLOT + 1.0, hb)   # out past the face
    P.box("M-GASKET", cx - OPENING[0] / 2, y_face + 2.0, z0, OPENING[0], SLOT_DEPTH, din.SLOT)                       # the dark slot in its cut
    P.pivot(node, "port", (cx, y_face + 2.0 + SLOT_DEPTH / 2, z_edge), axis=(0, 0, -s), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp

def build():
    P = Prims()
    hb = P.box("M-GREY-PA", 0, -D, Z0, W, D, H)                                                   # housing
    P.box("M-GASKET", 2, -D + 8, Z0 + 2, W - 4, 20, 2.0); P.box("M-GASKET", 2, -D + 8, Z0 + H - 4, W - 4, 20, 2.0)   # vent grilles top and bottom (dark bands)
    din.rail_clip(P, 0, W); P.box("M-GREY-PA", W / 2 - 4, -2, Z0 - CLIP, 8, 6, CLIP)                # the 3.3 clip projection below the body
    for up, marks in TERMINALS:                                                                   # terminal rows: input top (L N PE), output bottom (+V -V +V -V): Assumption (B)
        n = len(marks); x0 = W / 2 - n * PITCH / 2
        for i, (_, node) in enumerate(marks):                                                     # 1.1: heads 0.2 proud (were 1.2); slots cut into the housing (request elec-2); 1.3: a port node each
            terminal(P, node, x0 + PITCH * (i + 0.5), -D + 1.2 - PROUD, Z0 + H if up else Z0, up, hb)
    din.led(P, "led-dcok", "M-LENS-GREEN", 8.0, -D, 20.0, proud=PROUD); din.led(P, "led-dclow", "M-LENS-RED", 8.0, -D, 12.0, proud=PROUD)   # positions Assumption (C)
    P.cyl("node:vadj|M-WHITE-PA", (22.0, -D + 0.5, 16.0), (22.0, -D - PROUD, 16.0), 3.0); P.pivot("vadj", "rotate", (22.0, -D, 16.0), axis=(0, -1, 0), range=(0, 270))   # angle Assumption (C)
    P.box("M-WHITE-PA", 2, -D - 0.1, -8, W - 4, 0.1, 32)                                           # front legend field: DC OK / DC LOW / V.ADJ (decal); Assumption (C). 1.1: 0.1 proud, so the lenses and pot stand 0.1 above it (GEO-050)
    P.collider("env", 0, -D - PROUD, Z0 - CLIP, W, D0 + PROUD, H + CLIP)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="rear rail clip and vents", az=60, el=25), dict(name="face LEDs and pot", az=265, el=8, center=(16, -110, 16), height=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
