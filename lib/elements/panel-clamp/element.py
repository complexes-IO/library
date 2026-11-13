#!/usr/bin/env python3
"""panel-clamp: panel mounting clamp, our own design (OPERATING.md 12, own designs; lib/inventory.csv row panel-clamp own_design
"yes", request mech-5's answer). A hook that pulls a device's bezel against the front of a panel: the clamp's hook goes into a
slot in the side wall of the device's housing behind the panel, and a screw in the clamp's tapped hole presses on the back face of
the panel, so the hook pulls the device rearward and its bezel seats on the panel's front face. The clamp defines the slot (its
width, length, depth and its bearing face 30.0 behind the bezel's seating face); hmi-7in and power-meter (elec) cut it from
element:panel-clamp (properties.csv). The screw is a common part not built yet (no screw table is on file) and is placed in a
later version (OPERATING.md 12). The tapped M4 hole's thread limits are derived (spec.md, What it meets: derive.thread, ISO 68-1 /
ISO 965-1); the thread form is not drawn: the hole is modelled plain at the nominal Ø4. Every size below is a design choice. No
vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "panel-clamp", "1.2", "device"
TITLE = "panel mounting clamp, hook 10 x 6 x 2.5, body 8 x 12 x 22, M4 tapped hole, panels 1 to 6 thick"
TOOLKIT = "1.3"
BASELINE = ("our own design: panel mounting clamp, a hook that pulls a device's bezel against the back face of a panel cut-out; "
            "no product matched; the M4 thread derived (ISO 68-1, ISO 965-1), modelled plain; every size a design choice; no vendor "
            "file opened")
ORIGIN = ("the hook's bearing face (z = 0) on the housing wall's outer surface (x = 0) at the hook's centre (y = 0); the housing "
          "toward -x, the screw's axis along +z toward the panel; the bezel's seating face (the panel's front face) at z = 30")
COMMAND = "PANELCLAMP"
PARAMS = dict()
BODY_X, BODY_Y, BODY_Z = 8.0, 12.0, 22.0   # body beside the housing wall, x 0..8, y +-6, z 0..22: design choice
HOOK_X, HOOK_Y, HOOK_Z = 2.5, 10.0, 6.0    # hook into the housing's slot, x -2.5..0, y +-5, z 0..6 (bearing face z = 0): design choice
TAP_D, TAP_L = 4.0, 12.0                   # M4 tapped hole on the body's axis, from the front face z = 22 to z = 10: design choice.
                                           # The thread's limits are derived (spec.md, What it meets); the form is not drawn: plain at Ø4
TAP_X = BODY_X / 2                         # the hole's axis at x = 4, y = 0
SEAT_Z = 30.0                              # the bezel's seating face (the panel's front face) 30.0 in front of the bearing face
T_MIN, T_MAX = 1.0, 6.0                    # panels it clamps, 1.0 to 6.0 thick: the panel's back face at z = 29 to 24

def build():
    P = Prims(); Z = "M-ZINC"                                                                  # steel, zinc-plated
    body = P.box(Z, 0, -BODY_Y / 2, 0, BODY_X, BODY_Y, BODY_Z)                                # body (beside the housing wall)
    P.box(Z, -HOOK_X, -HOOK_Y / 2, 0, HOOK_X, HOOK_Y, HOOK_Z)                                 # hook (in the housing's slot)
    P.hole(Z, (TAP_X, 0, BODY_Z - TAP_L), (TAP_X, 0, BODY_Z + 1), TAP_D / 2, body)            # M4 tapped hole (plain at Ø4)
    P.collider("body", -HOOK_X, -BODY_Y / 2, 0, HOOK_X + BODY_X, BODY_Y, BODY_Z)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="front", az=200, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
