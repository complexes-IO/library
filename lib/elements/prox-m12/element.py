#!/usr/bin/env python3
"""prox-m12: inductive proximity sensor in an M12 x 1 threaded barrel, flush (embeddable) mounting, switching distance 2 mm on a metal
target, one PNP output, normally open (on while a metal target is within the switching distance), 24 V DC, an axial M12 connector seat at
the back, a yellow LED ring showing the output. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the
ETIM 10.0 class EC002714 "Inductive proximity switch", built to the class values in spec.md "## Class values"; no maker's datasheet (the
folder's earlier stub is reference only and was not used; its record is kept verbatim as the end block of references/source.txt).
What it meets comes from the standards on file: the barrel's thread M12 x 1 is derived (derive.thread(12.0, 1.0): ISO 68-1 basic profile,
ISO 965-1 6g), modelled as a plain barrel at the 6g major diameter's maximum (the thread's form is not modelled). Every other size is a
design choice, said so in spec.md. photoeye-m18 1.0's pattern at M12.
Not placed in this version (OPERATING.md 12, quality at the source: a host places only common parts past station 6): receptacle-m12
(built, not yet past station 6) and nut-m12-lock x2 (not built; a nut is shaped by its standard). So the connection is a connector seat on
the back (port node port-x1, gender none, as photoeye-m18 and encoder 1.0), and the barrel is plain for the installer's two lock nuts on
either side of the bracket. led of the made_of is not built: the LED ring is drawn here.
Modelled from the front: the sensing face (a plastic cap flush with the barrel), the barrel, the plastic rear cap with the LED ring between
its two parts, the connector seat; the coil, the ferrite core and the electronics inside are not modelled. Nothing moves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "prox-m12", "1.0", "device"
TITLE = "inductive proximity sensor, M12 x 1 barrel, flush, 2 mm, PNP N.O., 24 V DC, axial M12 seat (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Inductive proximity switch (ETIM 10.0 EC002714); class values in spec.md; barrel thread M12 x 1 "
            "derived (ISO 68-1, ISO 965-1 6g); every other size a design choice; receptacle-m12 not past station 6, so the connection "
            "is a connector seat with its port node (spec.md)")
ORIGIN = "the sensing face y = 0 on the barrel's axis x = 0, z = 0; the sensing direction toward -y, the barrel toward +y"
COMMAND = "PROXM12"
PARAMS = {}

# ---- barrel: M12 x 1 derived (derive.thread(12.0, 1.0): 6g major diameter 11.7972 ... 11.974), modelled at its maximum
BARREL_D = 11.974                    # derived: the barrel's outside, the thread's form not modelled
# ---- lengths along y (design choices: spec.md Dimensions); every part at the barrel's diameter, face to face, so both lock nuts
# ---- thread on from the front and nothing stands proud of the thread's envelope but the connector seat
FACE_L = 1.5                         # sensing face cap, plastic, y 0 ... 1.5: flush with the barrel (embeddable mounting)
BARREL_L = 40.0                      # threaded barrel, y 1.5 ... 41.5
CAP1_L, RING_L, CAP2_L = 3.0, 1.5, 3.0   # rear cap y 41.5 ... 44.5, LED ring y 44.5 ... 46.0, rear cap y 46.0 ... 49.0
# ---- connector seat on the back face (design choice; receptacle-m12 is placed on the seat at a later version)
SEAT_D, SEAT_L = 10.0, 4.0           # seat Ø10 (inside the M12 x 1 thread's minor diameter), y 49 ... 53: the face the receptacle sits on

assert SEAT_D < BARREL_D
assert FACE_L <= 1.5 and RING_L <= 1.5   # thin parts (the fillet pre-flight skips them)


def build():
    P = Prims(); S = "M-SILVER"; K = "M-BLACK-PA"
    r = BARREL_D / 2
    y = 0.0
    P.cyl("M-ORANGE-PA", (0, y, 0), (0, y + FACE_L, 0), r); y += FACE_L                   # sensing face cap, flush
    P.cyl(S, (0, y, 0), (0, y + BARREL_L, 0), r); y += BARREL_L                            # threaded barrel (plain at the 6g major Ø max)
    P.cyl(K, (0, y, 0), (0, y + CAP1_L, 0), r); y += CAP1_L                                # rear cap, face to face on the barrel
    P.cyl("node:led-out|M-LENS-YELLOW", (0, y, 0), (0, y + RING_L, 0), r)                  # LED ring, face to face between the cap's parts
    P.pivot("led-out", "emissive", (0, y, 0), axis=(0, 1, 0), range=(0, 1)); y += RING_L
    P.cyl(K, (0, y, 0), (0, y + CAP2_L, 0), r); y += CAP2_L                                # rear cap's back part
    y1 = y + SEAT_L
    P.cyl(f"node:port-x1|{K}", (0, y, 0), (0, y1, 0), SEAT_D / 2)                           # connector seat (receptacle-m12 later)
    P.pivot("port-x1", "port", (0, y1, 0), axis=(0, 1, 0), range=(0, 0), unit="m12-a", gender="none")   # PIN-002: no contact modelled yet
    P.collider("env", -r, 0, -r, BARREL_D, y1, BARREL_D)
    return P

PREVIEWS = [dict(name="sensing face three-quarter", az=250, el=20),
            dict(name="back, connector seat and LED ring", az=60, el=20),
            dict(name="side", az=0, el=0)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
