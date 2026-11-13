#!/usr/bin/env python3
"""claw-clamping: generic clamping claw (a machine-table fork clamp), our own vendor-neutral design of the ETIM 10.0 class EC004295
(Clamping claw), built unattended (OPERATING.md 12, generic elements). A steel strap 110 x 32 x 16 with a fork slot open at the
rear for an M12 bolt, a nose pad under its front end that bears on the work, and two heel legs under its rear end that stand on the
machine table either side of the slot. The bolt (a T-slot bolt), its nut and washer are standard parts, never generic: the slot is
cut and they are placed in a later version. Slot width: the M12 clearance, ISO 273 coarse (lib/standards/holes.csv). The class
values (spec.md, "Class values") are design inputs; every size below is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "claw-clamping", "1.1", "device"
TITLE = "clamping claw, generic, fork clamp 110 x 32 x 16, M12 bolt slot, heel legs and nose pad"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic clamping claw (ETIM 10.0 EC004295); class values are design inputs (spec.md); fork slot for "
            "M12 to ISO 273 coarse; the bolt, nut and washer placed later; every size a design choice; no vendor file opened")
ORIGIN = ("the heel legs' underside (the face that stands on the machine table) z = 0, the bolt's axis (the centre of the fork "
          "slot's closed end) at x = 0, y = 0; the nose toward +x, the fork open toward -x")
COMMAND = "CLAMPCLAW"
PARAMS = dict()
L, W, T = 110.0, 32.0, 16.0                      # class values: length 110, width 32; strap 16 thick: design choice
REAR, FRONT = -70.0, 40.0                        # the strap from x -70 (the fork's open end) to x 40 (the nose): design choice
STRAP_Z = 22.0                                   # the strap's underside, 22 above the table: design choice
M12_D = 14.5                                     # the slot's width and its closed end's Ø: M12 clearance, ISO 273 coarse H14 (lib/standards/holes.csv)
HEEL_L = 14.0                                    # heel legs 14 long under the rear end, either side of the slot: design choice
NOSE_L, NOSE_H = 12.0, 2.0                       # nose pad 12 long, 2 below the strap, at the front end: design choice

def build():
    P = Prims(); Z = "M-ZINC"
    strap = P.box(Z, REAR, -W / 2, STRAP_Z, L, W, T)                                                       # the strap
    P.hole(Z, (0, 0, STRAP_Z - 1), (0, 0, STRAP_Z + T + 1), M12_D / 2, strap)                              # the slot's closed end, Ø14.5
    P.cutbox(Z, REAR - 1, -M12_D / 2, STRAP_Z - 1, -REAR + 1, M12_D, T + 2, strap)                         # the fork slot, open to the rear
    for s in (-1, 1):                                                                                     # heel legs, either side of the slot
        y0 = M12_D / 2 if s > 0 else -W / 2
        P.box(Z, REAR, y0, 0, HEEL_L, W / 2 - M12_D / 2, STRAP_Z)
    P.box(Z, FRONT - NOSE_L, -W / 2, STRAP_Z - NOSE_H, NOSE_L, W, NOSE_H)                                  # nose pad, bears on the work
    P.collider("body", REAR, -W / 2, STRAP_Z, L, W, T)
    P.collider("heel", REAR, -W / 2, 0, HEEL_L, W, STRAP_Z)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="fork end", az=195, el=35)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
