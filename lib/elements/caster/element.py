#!/usr/bin/env python3
"""caster: swivel plate caster, wheel Ø100, our own design, built unattended (OPERATING.md 12, own designs; lib/inventory.csv row
"caster", own_design yes, made_of screw-iso4017 x4, system table-welding; the machine rows' carts and cabinets place it, tb-rollcab
1.0 already carries its plate pattern as holes). A square top plate with four M8 clearance holes on 80 x 60 centres (the pattern
tb-rollcab's bottom pads carry), a swivel fork under it (node `swivel`: the head disc, the crown plate, two legs and the axle,
turning about the plate's centre axis z) and a wheel on the fork's axle (node `wheel`: a tread and a hub, a child of the swivel,
turning about the axle along y). The axle trails 25 behind the swivel axis, so the wheel follows the push. The swivel bearing
(the ball race between the plate and the head), the wheel's bearing and the axle's nut are not drawn; a brake and a fixed (rigid)
fork are other versions. Every size below is a design choice. No load rating, no speed and no floor claim. No vendor file was
opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "caster", "1.0", "device"
TITLE = "swivel plate caster, own design, plate 100 x 85 with 4 x Ø9.0 holes on 80 x 60 (M8, ISO 273 medium), fork trailing 25, wheel Ø100 x 32, 140 high"
TOOLKIT = "1.3"
BASELINE = ("our own design: swivel plate caster, a 100 x 85 x 3 zinc-plated pressed steel top plate with four Ø9.0 clearance holes on 80 x 60 "
            "centres (M8, ISO 273 medium; hexagon head screws ISO 4017 placed later), a swivel fork (head disc Ø60, crown plate, two 3 "
            "legs, Ø12 axle trailing 25) turning about the plate's centre, a Ø100 x 32 black wheel on a Ø30 hub turning on the axle, "
            "140 from the floor to the plate's top face; every size a design choice; no load rating; no vendor file opened")
ORIGIN = ("the plate's top face (the mounting face, z = 0, the host's underside) on the swivel axis x = 0, y = 0; +z up, so the whole "
          "caster lies below the origin and the floor is the plane z = -140 at rest; at rest the fork trails toward +x (the axle at "
          "x 25) and the axle runs along y")
COMMAND = "CASTERSW"
PARAMS = dict()
PLATE_X, PLATE_Y, PLATE_T = 100.0, 85.0, 3.0        # the top plate 100 (x) x 85 (y), 3 thick (z -3..0): pressed steel, a design choice; at 3 its corner edges are "short" for the gate's fillet pre-flight (toolkit/fillet.py MIN_EDGE) and skipped: a 5 edge with two free corners read 88 % of its fillet volume (mech-r101)
HOLE_D = 9.0                                        # 4 x M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv); the host's pattern is tb-rollcab's pads
HOLE_PX, HOLE_PY = 80.0, 60.0                       # the four holes on 80 (x) x 60 (y) centres: tb-rollcab 1.0's caster pad pattern (design choice there)
HEAD_R, HEAD_T = 30.0, 10.0                         # the swivel head disc Ø60, 10 thick, face to face under the plate (z -13..-3); the ball race is not drawn
CROWN_X0, CROWN_L, CROWN_W, CROWN_T = -10.0, 60.0, 46.0, 3.0   # the crown plate x -10..50, y +-23, z -16..-13: joins the head to the legs (3 pressed steel as the plate)
LEG_X0, LEG_L, LEG_T = 0.0, 50.0, 3.0               # each leg x 0..50 (the axle at its middle), 3 thick, its outer face at y +-23, its inner face at y +-20
LEG_Z0 = -110.0                                     # the legs hang from the crown's underside (z -16) to z -110: 20 below the axle
TRAIL = 25.0                                        # the axle 25 behind the swivel axis (x 25): the wheel trails the push (a swivel caster's offset): design choice
AXLE_R, AXLE_Y = 6.0, 24.0                          # the axle Ø12 along y from y -24 to 24: 1 proud of each leg's outer face (its nut and head are not drawn)
AXLE_Z = -90.0                                      # the axle's axis at z -90: the wheel's bottom at z -140 (the tread's radius below it)
WHEEL_R, WHEEL_W = 50.0, 32.0                       # the tread Ø100, 32 wide (y +-16): 4 clear of each leg's inner face
HUB_R, HUB_W = 15.0, 36.0                           # the hub Ø30, 36 wide (y +-18): 2 proud of the tread each side, 2 clear of the legs
HUB_BORE_D = 13.0                                   # the hub's bore Ø13 on the Ø12 axle: 0.5 radial running clearance, a design choice (as hinge 1.0's moving knuckle)
SWING = 180.0                                       # the fork turns -180..180 about z (a full turn, free): design choice
HEIGHT = -AXLE_Z + WHEEL_R                          # 140: the floor to the plate's top face

def build():
    P = Prims(); Z = "M-ZINC"; T = "M-BLACK-PA"      # plate, fork, axle and hub zinc-plated steel; the tread black polyamide
    plate = P.box(Z, -PLATE_X / 2, -PLATE_Y / 2, -PLATE_T, PLATE_X, PLATE_Y, PLATE_T)                      # the top plate, z -3..0
    for dx in (-HOLE_PX / 2, HOLE_PX / 2):
        for dy in (-HOLE_PY / 2, HOLE_PY / 2):
            P.hole(Z, (dx, dy, -PLATE_T - 1), (dx, dy, 1), HOLE_D / 2, plate)                              # 4 x Ø9.0 through the plate
    P.collider("plate", -PLATE_X / 2, -PLATE_Y / 2, -PLATE_T, PLATE_X, PLATE_Y, PLATE_T)
    S = lambda m: f"node:swivel|{m}"
    z_head = -PLATE_T - HEAD_T                                                                              # -13
    P.cyl(S(Z), (0, 0, z_head), (0, 0, -PLATE_T), HEAD_R)                                                   # the head disc, face to face under the plate
    z_crown = z_head - CROWN_T                                                                              # -16
    P.box(S(Z), CROWN_X0, -CROWN_W / 2, z_crown, CROWN_L, CROWN_W, CROWN_T)                                 # the crown plate under the head
    for sy in (-1, 1):
        y0 = sy * CROWN_W / 2 - (LEG_T if sy > 0 else 0)                                                    # the leg's -y face: 20 or -23
        leg = P.box(S(Z), LEG_X0, y0, LEG_Z0, LEG_L, LEG_T, z_crown - LEG_Z0)                               # a leg, its top face on the crown's underside
        P.hole(S(Z), (TRAIL, y0 - 1, AXLE_Z), (TRAIL, y0 + LEG_T + 1, AXLE_Z), AXLE_R, leg)                 # the axle's bore Ø12 through the leg
    P.cyl(S(Z), (TRAIL, -AXLE_Y, AXLE_Z), (TRAIL, AXLE_Y, AXLE_Z), AXLE_R)                                  # the axle Ø12 through both legs, 1 proud each side
    P.pivot("swivel", "rotate", (0, 0, -PLATE_T), axis=(0, 0, 1), range=(-SWING, SWING), unit="deg")        # turns under the plate about its centre
    P.collider("fork", CROWN_X0, -CROWN_W / 2, LEG_Z0, CROWN_L, CROWN_W, -PLATE_T - LEG_Z0)                  # the fork at rest: head, crown, legs and axle
    W = lambda m: f"node:wheel|{m}"
    hub = P.cyl(W(Z), (TRAIL, -HUB_W / 2, AXLE_Z), (TRAIL, HUB_W / 2, AXLE_Z), HUB_R)                       # the hub Ø30 between the legs
    P.hole(W(Z), (TRAIL, -HUB_W / 2 - 1, AXLE_Z), (TRAIL, HUB_W / 2 + 1, AXLE_Z), HUB_BORE_D / 2, hub)      # bored Ø13 on the axle
    tread = P.cyl(W(T), (TRAIL, -WHEEL_W / 2, AXLE_Z), (TRAIL, WHEEL_W / 2, AXLE_Z), WHEEL_R)               # the tread Ø100 on the hub
    P.hole(W(T), (TRAIL, -WHEEL_W / 2 - 1, AXLE_Z), (TRAIL, WHEEL_W / 2 + 1, AXLE_Z), HUB_R, tread)         # bored Ø30 for the hub (pressed, flush)
    P.pivot("wheel", "rotate", (TRAIL, 0, AXLE_Z), axis=(0, 1, 0), range=(0, 360), unit="deg")              # spins on the axle
    P.parents["wheel"] = "swivel"                                                                           # rides the fork (turntable's rollers' way)
    P.collider("tyre", TRAIL - WHEEL_R, -HUB_W / 2, AXLE_Z - WHEEL_R, 2 * WHEEL_R, HUB_W, 2 * WHEEL_R)      # the wheel at rest: tread and hub
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
