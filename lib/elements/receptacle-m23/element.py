#!/usr/bin/env python3
"""receptacle-m23: M23 circular connector, mounting (device side, without cable), flange mounted, male contacts in an M23 x 1 threaded
sleeve; kind power (3 poles + PE, Ø1.2 contacts) or signal (6 poles, Ø1.0 contacts). A generic element (OPERATING.md 12, EM 2026-11-07):
our own vendor-neutral design of ETIM 10.0 EC003569 "Circular connector, mounting (without cable)", built to the class values in
spec.md "## Class values"; no maker's datasheet and no product is matched. A common part (lib/inventory.csv: "M23 power / signal
receptacle (servo)"): servo-motor's two connector seats wait on it (port-pwr kind power, port-enc kind signal).
What it meets comes from the standards on file: the sleeve's thread M23 x 1 is derived (derive.thread(23.0, 1.0): ISO 68-1 basic
profile, ISO 965-1 6g), modelled as a plain sleeve at the 6g major diameter's maximum (the thread's form is not modelled); the four
flange holes are ISO 273 medium clearance for M3 (lib/standards/holes.csv). The mating face (contact layout, the coding key, the
sleeve's length and the plug's coupling) is tabulated by no standard on file, so it is the design's: the layout in spec.md (1.1).
Every other size is a design choice, said so in spec.md.
Modelled: the square flange with its four holes, the threaded sleeve (a plain bore), the insulating contact carrier, the contacts
(each a port node, gender male), the body behind the flange that passes through the host's wall. Not modelled: the coding key, the
thread's form, the seal, the contacts' crimp or solder ends and the cable side behind the body."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "receptacle-m23", "1.1", "connector"
TITLE = "M23 receptacle (device side), flange mounted, male contacts, M23 x 1 sleeve, power 3 + PE or signal 6 poles (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Circular connector, mounting (without cable) (ETIM 10.0 EC003569); class values in spec.md; "
            "thread M23 x 1 derived (ISO 68-1, ISO 965-1 6g), flange holes ISO 273 medium for M3 (lib/standards/holes.csv); the mating "
            "face (contact layout, coding, sleeve length) a design layout, no standard on file fixing it; every other size a design choice")
ORIGIN = ("the flange's back face (the face that sits on the host's outer wall) y = 0 on the sleeve's axis x = 0, z = 0; the sleeve and "
          "the mating plug toward -y, the body behind the flange (inside the host) toward +y")
COMMAND = "M23RCP"
PARAMS = dict(kind="power")

# ---- flange (design choices; holes ISO 273 medium for M3, lib/standards/holes.csv; features.csv)
FL, FL_T = 30.0, 3.0                  # square flange 30 x 30, 3.0 thick (y -3 ... 0)
HOLE_D, HOLE_A = 3.4, 11.0            # four Ø3.4 holes at x, z = ±11.0 (a 22 x 22 square): 15.56 from the axis, 4.07 outside the
                                      # sleeve, so a screw head up to Ø8.1 seats clear of it (the head's size is not on file)
# ---- threaded sleeve: M23 x 1 derived (derive.thread(23.0, 1.0): 6g major diameter 22.797 ... 22.974), modelled at its maximum
SLEEVE_D = 22.974                     # derived: the sleeve's outside, the thread's form not modelled
SLEEVE_L = 12.0                       # out of the flange's front face (y -3 ... -15): design choice
BORE_D = 19.0                         # the sleeve's bore: design choice (the plug's insert enters it)
# ---- contact carrier and contacts (a design layout, no standard on file fixing the M23 face: spec.md)
CARRIER_D, CARRIER_L = 18.9, 4.0      # insulating carrier in the bore, its back on the flange (y -3 ... -7); 0.05 clear of the bore
PIN_L = 5.0                           # contacts 5.0 out of the carrier face (y -7 ... -12), 3.0 inside the sleeve's front
BODY_D, BODY_L = 21.0, 18.0           # body behind the flange (y 0 ... 18), through the host's Ø22 wall hole: design choice
KINDS = {                             # contact: mark, x, z, diameter; unit of the port; contact plating material
    "power":  dict(unit="m23-power", mat="M-SILVER", pins=[("1", 90.0, 5.5, 1.2), ("2", 210.0, 5.5, 1.2), ("3", 330.0, 5.5, 1.2),
                                                           ("PE", 0.0, 0.0, 1.2)]),   # Ø1.2: the AutoCAD gate rejected Ø2.0 tips (r39)
    "signal": dict(unit="m23-signal", mat="M-GOLD", pins=[(str(k + 1), 90.0 - 60.0 * k, 5.0, 1.0) for k in range(6)]),
}

def contacts(kind="power"):
    """[(mark, x, z, d)] of the kind's contacts in this frame (angle from +x toward +z, on a circle of radius r about the axis)"""
    out = []
    for mark, ang, r, d in KINDS[kind]["pins"]:
        a = math.radians(ang)
        out.append((mark, round(r * math.cos(a), 4), round(r * math.sin(a), 4), d))
    return out

def build(kind="power"):
    if kind not in KINDS:
        raise SystemExit(f"receptacle-m23: kind {kind!r} NOT ON FILE: power or signal")
    P = Prims(); Z = "M-ZINC"; K = KINDS[kind]; h = FL / 2
    fl = P.box(Z, -h, -FL_T, -h, FL, FL_T, FL)                                                    # square flange, back face y = 0
    for sx in (-1, 1):
        for sz in (-1, 1):                                                                        # four M3 clearance holes, ISO 273 medium
            P.hole("M-GASKET", (sx * HOLE_A, -FL_T - 0.5, sz * HOLE_A), (sx * HOLE_A, 0.5, sz * HOLE_A), HOLE_D / 2, fl)
    y0, y1 = -FL_T, -FL_T - SLEEVE_L
    sl = P.cyl(Z, (0, y0, 0), (0, y1, 0), SLEEVE_D / 2)                                           # the M23 x 1 sleeve (plain)
    P.hole("M-GASKET", (0, y1 - 0.5, 0), (0, y0 + 0.5, 0), BORE_D / 2, sl)                        # its bore, through to the flange's face
    yc = y0 - CARRIER_L
    P.cyl("M-BLACK-PA", (0, y0, 0), (0, yc, 0), CARRIER_D / 2)                                    # contact carrier on the flange's face
    for mark, x, z, d in contacts(kind):                                                          # contacts: male pins on the carrier face
        node = f"c-{mark.lower()}"
        P.cyl(f"node:{node}|{K['mat']}", (x, yc, z), (x, yc - PIN_L, z), d / 2)
        P.pivot(node, "port", (x, yc - PIN_L, z), axis=(0, -1, 0), range=(0, 0), unit=K["unit"], gender="male")
    P.cyl(Z, (0, 0, 0), (0, BODY_L, 0), BODY_D / 2)                                               # body behind the flange, in the host
    P.collider("env", -h, y1, -h, FL, BODY_L - y1, FL)
    return P

PREVIEWS = [dict(name="power three-quarter", az=250, el=25), dict(name="power mating face", az=270, el=0, center=(0, -15, 0), height=30),
            dict(name="signal three-quarter", az=250, el=25, params=dict(kind="signal")),
            dict(name="signal mating face", az=270, el=0, center=(0, -15, 0), height=30, params=dict(kind="signal"))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
