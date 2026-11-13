#!/usr/bin/env python3
"""term-jumper: plug-in jumper (cross-connector) for term-4mm feed-through blocks: a comb of copper blades on one bar under an insulating cap,
one blade per block, at the block's pitch; it joins neighbouring blocks into one potential (a panel's +24 V or 0 V group) without taking a
clamp. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC000489 "Cross-connector for terminal
block", built to the class values in spec.md "## Class values"; no maker's datasheet. Inventory row term-jumper (pinned 6; request panel-3
item 1, lib/requests/core/elec-term-jumper-2026-11-11.md: pnl-motor-starter's X1 groups, 2 and 4 poles).
What it meets is term-4mm 1.4 on file: the pitch (SIZES, read at build time) and the depth from the block's front face to its current bar
(term-4mm element.py: the wire axis 9.0 off the front, the bar 2.5 behind it: 11.5). The block's jumper channel is NOT ON FILE (B): the document
wanted is the maker's drawing of term-4mm's bar jumper (listed in term-4mm's brief, not downloaded; no standard tabulates it), so the blades are
built to this element's own design channel (spec.md Dimensions). Every other size is a design choice, said so in spec.md. Each blade is a port
node p-<k> (PIN-002 male). 2.0 (review term-jumper-1.0 findings 1 to 3): the channel at z 9.2 so the 8.0 cap clears clamp 1's screwdriver
hole (z 13.4 ... 17.6) and the marker tag (z <= 5.0), and each blade 1.5 x 2.7 = 4.05 mm2, at least the block's own rated section."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "term-jumper", "2.0", "device"
TITLE = "plug-in jumper for term-4mm feed-through blocks, 6.0 mm pitch, 4 poles (2 to 12 by parameter), 32 A 500 V (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Cross-connector for terminal block (ETIM 10.0 EC000489); class values in spec.md; pitch and reach from "
            "term-4mm 1.4 on file; the block's channel is open (NOT ON FILE (B), spec.md) and the blades are built to a design channel")
ORIGIN = ("the cap's seating face on the block's front y = 0, blades toward +y (into the block, toward the rail); pole 1's blade on x = 0, "
          "poles along +x at the pitch; z = 0 on the blades' axis (the design channel: z = 9.2 of the block's frame)")
COMMAND = "TERMJMP"
PARAMS = dict(poles=4)
POLES = (2, 12)                      # the poles a host may ask for (design choice; class value 2)

TERM, TERM_VERSION = "term-4mm", "1.4"   # the block it bridges, pinned at the version its figures were read from
REACH = 11.5                         # blade length past the seating face: the block's front face to its current bar's face (term-4mm 1.4 element.py: y_ax = -h + 9.0, bar at y_ax + 2.5)
CHANNEL_Z = 9.2                      # the design channel's z in the block's frame: the cap (8 wide, z 5.2 ... 13.2) between the marker tag (z <= 5.0, marker-terminal)
                                     # and clamp 1's screwdriver hole (term-4mm 1.4 P.hole radius 2.1 at z 15.5: z 13.4 ... 17.6), 0.2 clear of each (2.0; 1.0 read the radius as a diameter)
BLADE = (1.5, 2.7)                   # a blade's section: x (across the pitch), z (along the block); 4.05 mm2, at least the block's rated section (term-4mm's brief: 4 mm2 class), 2.0.
                                     # 1.5 thick, as 1.0: the first 2.0 gate run (1.6 x 2.5) had 8 of the blades' 12.5 mm edges rejected by the AutoCAD fillet pre-flight
BAR = (2.0, 2.5)                     # the bar's section inside the cap: y, z; 5.0 mm2 (design choice)
CAP = (8.0, 8.0, 2.75)               # the cap: thickness (y, above the seating face), width (z), reach past the end blades' axes (x): overall (n - 1) x pitch + 5.5.
                                     # 8 x 8, not 4 x 5: the AutoCAD gate's fillet pre-flight rejects 4 and 5 mm end-face edges on the envelope (run 1; pneu r70's 4 mm tab, passed at 8)

def pitch():
    return library.load(TERM, TERM_VERSION).SIZES["feed"][0]          # 6.0: the feed-through block's pitch on file

def build(poles=4):
    n = int(poles)
    if not POLES[0] <= n <= POLES[1]: raise ValueError(f"term-jumper: poles {n} outside {POLES[0]} ... {POLES[1]} (spec.md Class values 2)")
    P = Prims(); p = pitch(); bx, bz = BLADE; by, brz = BAR; ct, cw, ce = CAP
    x0, W = -ce, (n - 1) * p + 2 * ce
    cap = P.box("M-RED-PA", x0, -ct, -cw / 2, W, ct, cw)                                                  # the insulating cap
    P.cutbox("M-RED-PA", -bx / 2, -1.0 - by, -brz / 2, (n - 1) * p + bx, by, brz, cap)                     # the bar's pocket, 1.0 under the seating face
    P.box("M-CU", -bx / 2, -1.0 - by, -brz / 2, (n - 1) * p + bx, by, brz)                                 # the bar joining the blades
    for k in range(1, n + 1):
        cx = (k - 1) * p
        P.cutbox("M-RED-PA", cx - bx / 2, -1.0, -bz / 2, bx, 2.0, bz, cap)                                 # the blade's slot through the cap's floor
        P.box(f"node:p-{k}|M-CU", cx - bx / 2, -1.0, -bz / 2, bx, 1.0 + REACH, bz)                         # the blade: seated on the bar, out to the block's current bar
        P.pivot(f"p-{k}", "port", (cx, REACH, 0.0), axis=(0, 1, 0), range=(0, 0), unit="pin", gender="male")   # PIN-002: a plug-in blade
    P.collider("env", x0, -ct, -cw / 2, W, ct + REACH, cw)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="blades from below", az=230, el=-40),
            dict(name="two poles", az=250, el=20, params=dict(poles=2)),
            dict(name="ten poles", az=250, el=20, params=dict(poles=10))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
