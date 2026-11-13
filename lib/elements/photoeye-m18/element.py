#!/usr/bin/env python3
"""photoeye-m18: diffuse reflective photoelectric sensor (an energetic light scanner) in an M18 x 1 threaded barrel, red light, sensing
range 400 mm on a white target, one PNP output, light-switching (normally open: on while a target reflects), 24 V DC, an axial M12
connector seat at the back, two status LEDs (green: powered, yellow: output on). A generic element (OPERATING.md 12, EM 2026-11-07): our
own vendor-neutral design of the ETIM 10.0 class EC001821 "Diffuse reflective photoelectric sensor", built to the class values in
spec.md "## Class values"; no maker's datasheet (the folder's earlier stub is reference only and was not used; its record is kept
verbatim as the end block of references/source.txt).
What it meets comes from the standards on file: the barrel's thread M18 x 1 is derived (derive.thread(18.0, 1.0): ISO 68-1 basic
profile, ISO 965-1 6g), modelled as a plain barrel at the 6g major diameter's maximum (the thread's form is not modelled). Every other
size is a design choice, said so in spec.md.
Not placed in this version (OPERATING.md 12, quality at the source: a host places only common parts past station 6): receptacle-m12
(built, not yet past station 6) and nut-m18-lock x2 (not built; a nut is shaped by its standard). So the connection is a connector
seat on the back (port node port-x1, gender none, as encoder 1.0 and servo-motor), and the barrel is plain for the installer's two
lock nuts on either side of the bracket. led of the made_of is not built: the two lenses are drawn here (as plc-aio's).
Modelled from the front: the lens window on the barrel's front face, the barrel, the plastic rear cap with the two LED lenses on its
back face, the connector seat; the emitter, receiver and electronics inside are not modelled. Nothing moves."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "photoeye-m18", "1.0", "device"
TITLE = "photoelectric sensor, diffuse, M18 x 1 barrel, red light, 400 mm, PNP N.O., 24 V DC, axial M12 seat (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Diffuse reflective photoelectric sensor (ETIM 10.0 EC001821); class values in spec.md; barrel "
            "thread M18 x 1 derived (ISO 68-1, ISO 965-1 6g); every other size a design choice; receptacle-m12 not past station 6, "
            "so the connection is a connector seat with its port node (spec.md)")
ORIGIN = "the barrel's front face y = 0 on its axis x = 0, z = 0; the sensing direction (light out) toward -y, the barrel toward +y"
COMMAND = "PEYEM18"
PARAMS = {}

# ---- barrel: M18 x 1 derived (derive.thread(18.0, 1.0): 6g major diameter 17.797 ... 17.974), modelled at its maximum
BARREL_D = 17.974                    # derived: the barrel's outside, the thread's form not modelled
BARREL_L = 50.0                      # threaded length y 0 ... 50: design choice
# ---- front lens and rear cap (design choices: spec.md Dimensions)
LENS_D, LENS_T = 14.0, 1.0           # lens window Ø14, 1.0 proud of the barrel's front face (y -1 ... 0)
IN = 0.5                             # a fixed part runs 0.5 into the one it sits on (one solid joint)
CAP_L = 8.0                          # plastic rear cap at the barrel's diameter, y 50 ... 58
# ---- connector seat on the back face (design choice; receptacle-m12 is placed on the seat at a later version)
SEAT_D, SEAT_L = 12.0, 4.0           # seat Ø12 (an M12 connector's size), y 58 ... 62: the face the receptacle sits on
# ---- status LEDs on the cap's back face, beside the seat (design choices)
LED_R, LED_T, LED_PCR = 1.1, 0.3, 7.4   # lenses Ø2.2, 0.3 proud, on a radius 7.4 (6.3 ... 8.5: clear of the seat's 6.0 and the cap's 8.99)
LEDS = (("led-pwr", "M-LENS-GREEN", 135.0), ("led-out", "M-LENS-YELLOW", 45.0))   # node, lens, angle in the x-z plane (0 = +x)

assert LED_PCR - LED_R > SEAT_D / 2 and LED_PCR + LED_R < BARREL_D / 2   # each lens on the cap's ring, clear of the seat
assert 2 * LED_PCR * math.sin(math.radians(45.0)) > 2 * LED_R + 2.0     # the two lenses 90 deg apart, clear of each other
assert LENS_D < BARREL_D


def build():
    P = Prims(); S = "M-SILVER"; K = "M-BLACK-PA"
    r = BARREL_D / 2
    P.cyl("M-LENS-DARK", (0, -LENS_T, 0), (0, IN, 0), LENS_D / 2)                          # lens window, 0.5 into the barrel
    P.cyl(S, (0, 0, 0), (0, BARREL_L, 0), r)                                               # threaded barrel (plain at the 6g major Ø max)
    y0 = BARREL_L + CAP_L
    P.cyl(K, (0, BARREL_L, 0), (0, y0, 0), r)                                              # plastic rear cap, face to face on the barrel (same Ø)
    for node, lens, deg in LEDS:                                                           # status LEDs face to face on the cap's back
        a = math.radians(deg); x = LED_PCR * math.cos(a); z = LED_PCR * math.sin(a)
        P.cyl(f"node:{node}|{lens}", (x, y0, z), (x, y0 + LED_T, z), LED_R)
        P.pivot(node, "emissive", (x, y0, z), axis=(0, 1, 0), range=(0, 1))
    y1 = y0 + SEAT_L
    P.cyl(f"node:port-x1|{K}", (0, y0, 0), (0, y1, 0), SEAT_D / 2)                          # connector seat (receptacle-m12 later)
    P.pivot("port-x1", "port", (0, y1, 0), axis=(0, 1, 0), range=(0, 0), unit="m12-a", gender="none")   # PIN-002: no contact modelled yet
    P.collider("env", -r, -LENS_T, -r, BARREL_D, LENS_T + y1, BARREL_D)
    return P

PREVIEWS = [dict(name="lens three-quarter", az=250, el=20),
            dict(name="back, connector seat and LEDs", az=60, el=20),
            dict(name="back face", az=90, el=0, center=(0, 58, 0), height=24),
            dict(name="side", az=0, el=0)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
