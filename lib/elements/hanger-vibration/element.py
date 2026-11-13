#!/usr/bin/env python3
"""hanger-vibration: generic vibration isolation hanger (the rubber hanger a duct, a pipe or a fan hangs from on threaded rods, so
the ceiling takes less of its vibration), our own vendor-neutral design of the ETIM 10.0 class EC010829 (Vibration isolation
hanger), built unattended (OPERATING.md 12, generic elements; `python lib/build.py inventory mech` lists the class once no inventory
row builds unattended and the machine-element classes above it wait for a dimensional standard or a toolkit primitive,
lib/needs-em/mech.md). Rubber in compression in a closed frame: a galvanized steel frame 60 x 40 x 90 of 3.0 sheet (top, bottom
and two sides) hangs from the ceiling's M10 rod through a hole in its top plate (the nut inside the frame); the load's M10 rod comes
up through a free passage in the bottom plate, a rubber element and a steel cap, its nut on the cap, so the load presses the rubber
onto the bottom plate. The class values (spec.md, "Class values") are design inputs; the class's load, deflection and damping
figures are not stated, so none is claimed and nothing moves in the model. Every size is a design choice. No vendor file was
opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "hanger-vibration", "1.1", "device"
TITLE = "vibration isolation hanger, generic, rubber in compression, frame 60 x 40 x 90, M10 rod top and bottom"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic vibration isolation hanger (ETIM 10.0 EC010829), rubber in compression in a closed frame; "
            "class values are design inputs (spec.md); the rods' holes at M10's ISO 273 medium clearance; every other size a design "
            "choice; no load, deflection or damping claim; no vendor file opened")
ORIGIN = ("the frame's top face (z = 0, against the ceiling rod's nut and washer side) at the ceiling rod's axis; the frame hangs "
          "below it to z -90; x across the frame's sides, y through its open faces")
COMMAND = "VIBHANG"
PARAMS = dict()

FL, FW, FH, S = 60.0, 40.0, 90.0, 3.0            # class values: length (x +-30), width (y +-20), height (z -90..0); the frame's sheet 3.0
ROD_D = 11.0                                     # M10 clearance medium H13 (ISO 273, lib/standards/holes.csv): ceiling rod and cap
PASS_D = 22.0                                    # the load rod's free passage through the bottom plate: design choice (6 clear around M10)
RUB_D, RUB_H, RUB_BORE = 36.0, 30.0, 12.0        # rubber element 36 x 30 with a 12 bore: design choice
CAP_D, CAP_T = 32.0, 3.0                         # steel cap on the rubber: design choice
STEEL, RUB = "M-GALV", "M-GASKET"

Z_BOT = -FH + S                                  # the bottom plate's top face, -87: the rubber's seat
Z_RUB = Z_BOT + RUB_H                            # the rubber's top, -57: the cap's seat
Z_CAP = Z_RUB + CAP_T                            # the cap's top, -54: the load rod's nut

assert RUB_D / 2 < FW / 2 and RUB_D / 2 < FL / 2 - S                       # the rubber inside the frame's plan
assert CAP_D < RUB_D and RUB_BORE > 10.0 and PASS_D > RUB_BORE             # the cap on the rubber; the rod free in the rubber and the plate
assert (FW - PASS_D) / 2 >= 1.5 * S and (FW - ROD_D) / 2 >= 1.5 * S        # DFM-010: hole to edge >= 1.5 t in the 3.0 sheet
assert -S - Z_CAP >= 45.0                                                  # 51 inside the frame for the two rods' nuts


def build():
    P = Prims(); hl, hw = FL / 2, FW / 2
    P.box(STEEL, -hl, -hw, -FH, S, FW, FH)                                                      # side plate -x, full height
    P.box(STEEL, hl - S, -hw, -FH, S, FW, FH)                                                   # side plate +x, full height
    top = P.box(STEEL, -hl + S, -hw, -S, FL - 2 * S, FW, S)                                     # top plate, between the sides
    P.hole(STEEL, (0, 0, -S - 1.0), (0, 0, 1.0), ROD_D / 2, top)                                # the ceiling rod's hole
    bot = P.box(STEEL, -hl + S, -hw, -FH, FL - 2 * S, FW, S)                                    # bottom plate, the rubber's seat
    P.hole(STEEL, (0, 0, -FH - 1.0), (0, 0, Z_BOT + 1.0), PASS_D / 2, bot)                     # the load rod's free passage
    rub = P.cyl(RUB, (0, 0, Z_BOT), (0, 0, Z_RUB), RUB_D / 2)                                  # rubber element, in compression
    P.hole(RUB, (0, 0, Z_BOT - 1.0), (0, 0, Z_RUB + 1.0), RUB_BORE / 2, rub)                   # the load rod's bore
    cap = P.cyl(STEEL, (0, 0, Z_RUB), (0, 0, Z_CAP), CAP_D / 2)                                # steel cap, takes the load rod's nut
    P.hole(STEEL, (0, 0, Z_RUB - 1.0), (0, 0, Z_CAP + 1.0), ROD_D / 2, cap)                    # the load rod's hole
    P.collider("body", -hl, -hw, -FH, FL, FW, FH)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="front", az=180, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
