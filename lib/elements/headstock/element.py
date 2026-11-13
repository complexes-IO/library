#!/usr/bin/env python3
"""headstock: lathe or grinder headstock housing, our own design (OPERATING.md 12, own designs; inventory row own_design
"yes"). The housing that carries the work spindle of the CNC and conventional lathes and the cylindrical grinder of
lib/machines-factory.txt: a base foot that stands on the bed's two ways (bed-cast's `ways`), a closed box housing on it, and a
machined spindle seat on its +x face (node `spindle-seat`, fixed: the spindle a BOM puts in the headstock is placed on the
seat's face, on the spindle axis, and turns on its own node). The spindle, its nose (ISO 702), bearings, gears and drive are not
built, so the seat has no bore for them (OPERATING.md 12: a host doesn't model holes now for a part it places later); the
fixing to the bed is the machine's. Every size is a design choice. No speed, power, load or accuracy claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "headstock", "1.1", "furniture"
TITLE = "headstock housing 480 x 400 x 380 on a 500 x 440 base foot, spindle seat 180 dia at centre height 260"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every "
            "size a design choice; no speed, power, load or accuracy claim")
ORIGIN = ("the base foot's underside z = 0 (the seat on the bed's ways) at the headstock's centre x = 0, y = 0; the spindle "
          "axis along +x (toward the work) at y = 0, z = 260; front toward -y; the spindle seat's face at x = 270")
COMMAND = "HEADSTK"
PARAMS = dict()
FOOT_L, FOOT_W, FOOT_T = 500.0, 440.0, 40.0   # base foot 500 along x, 440 across (spans ways at y +-130 to +-210), 40 thick: design choice
BOX_L, BOX_W, BOX_TOP = 480.0, 400.0, 420.0   # housing 480 x 400, from the foot (z 40) to its top face (z 420): design choice
AXIS_Z = 260.0                                # spindle axis 260 above the foot's underside: design choice
SEAT_D, SEAT_T = 180.0, 30.0                  # spindle seat boss 180 dia, 30 proud of the housing's +x face: design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                  # the seat: bare machined steel, the library's bright-metal layer
    x0 = BOX_L / 2                                                    # the housing's +x face
    P.cyl(f"node:spindle-seat|{W}", (x0, 0, AXIS_Z), (x0 + SEAT_T, 0, AXIS_Z), SEAT_D / 2)        # spindle seat boss
    P.box(S, -FOOT_L / 2, -FOOT_W / 2, 0, FOOT_L, FOOT_W, FOOT_T)                                   # base foot
    P.box(S, -BOX_L / 2, -BOX_W / 2, FOOT_T, BOX_L, BOX_W, BOX_TOP - FOOT_T)                        # housing (the body)
    P.pivot("spindle-seat", "fixed", (x0 + SEAT_T, 0, AXIS_Z), axis=(1, 0, 0))
    P.collider("nose", x0, -SEAT_D / 2, AXIS_Z - SEAT_D / 2, SEAT_T, SEAT_D, SEAT_D)
    P.collider("foot", -FOOT_L / 2, -FOOT_W / 2, 0, FOOT_L, FOOT_W, FOOT_T)
    P.collider("housing", -BOX_L / 2, -BOX_W / 2, FOOT_T, BOX_L, BOX_W, BOX_TOP - FOOT_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="front", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
