#!/usr/bin/env python3
"""ram: press ram (beam) carrying the upper tool, our own design (OPERATING.md 12, own designs; inventory row own_design
"yes"). The moving beam of the CNC and sheet press brakes of lib/machines-factory.txt (not the turret punch's short ram): a steel plate
2600 long, 60 thick and 400 high, a pad on its top edge at each end where the press's cylinder (hyd-cylinder-da-40, x2) bears on it,
and a machined tool seat along its lower edge (node `tool-seat`, fixed: the tool clamp or upper tool a BOM puts on the ram is
placed on the seat's underside and the ram carries it). The ram's own up and down travel is the press's (its frame, cylinders
and guides): the element is one body that the assembly moves. The tool clamp is not built yet, so the seat has no hole for it
(OPERATING.md 12: a host doesn't model holes now for a part it places later). Every size is a design choice. No force rating,
no stiffness, deflection or crowning claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "ram", "1.1", "furniture"
TITLE = "press ram 2600 x 60 x 400 with two cylinder pads 200 x 120 x 30 and a tool seat 2500 x 40 x 20"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every "
            "size a design choice; no force rating, no stiffness, deflection or crowning claim")
ORIGIN = ("the tool seat's underside z = 0 (the upper tool's seat) at the ram's centre x = 0, y = 0; the ram's length along "
          "x; front toward -y; the cylinder pads' top faces at z = 450")
COMMAND = "RAM"
PARAMS = dict()
RAM_L, RAM_T, RAM_H = 2600.0, 60.0, 400.0     # ram plate 2600 long (x), 60 thick (y), 400 high: design choice
SEAT_L, SEAT_D, SEAT_H = 2500.0, 40.0, 20.0   # tool seat 2500 long (the bending length), 40 deep, 20 high: design choice
PAD_L, PAD_W, PAD_T = 200.0, 120.0, 30.0      # cylinder pads 200 along x, 120 across (30 over each face), 30 thick: design choice
PAD_X = 1050.0                                # pad centres at x +-1050 (the two cylinders 2100 apart): design choice

def build():
    P = Prims(); S = "M-STEEL-7035"; W = "M-SILVER"                  # the seat: bare machined steel, the library's bright-metal layer
    P.box(f"node:tool-seat|{W}", -SEAT_L / 2, -SEAT_D / 2, 0, SEAT_L, SEAT_D, SEAT_H)             # tool seat
    P.box(S, -RAM_L / 2, -RAM_T / 2, SEAT_H, RAM_L, RAM_T, RAM_H)                                 # ram plate (the body)
    for sx in (-1, 1):                                                                            # cylinder pads
        P.box(S, sx * PAD_X - PAD_L / 2, -PAD_W / 2, SEAT_H + RAM_H, PAD_L, PAD_W, PAD_T)
    P.pivot("tool-seat", "fixed", (0, 0, 0), axis=(0, 0, -1))
    P.collider("seat", -SEAT_L / 2, -SEAT_D / 2, 0, SEAT_L, SEAT_D, SEAT_H)
    P.collider("ram", -RAM_L / 2, -RAM_T / 2, SEAT_H, RAM_L, RAM_T, RAM_H)
    for sx in (-1, 1):
        P.collider(f"pad-{'b' if sx > 0 else 'a'}", sx * PAD_X - PAD_L / 2, -PAD_W / 2, SEAT_H + RAM_H, PAD_L, PAD_W, PAD_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="front", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
