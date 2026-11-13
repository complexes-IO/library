#!/usr/bin/env python3
"""servo-drive: servo drive (servo amplifier) for a permanent-magnet synchronous servo motor, 1.0 kW, three-phase 380 ... 480 V AC in,
three-phase 0 ... 480 V 0 ... 400 Hz out, 3.0 A continuous / 9.0 A peak, incremental encoder feedback, on the 35 mm rail. A generic
element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of a product class ETIM 10.0 has no class for, so generic by
the standard whose rating data its class values follow (EM 2026-11-08: "no ETIM class; IEC 61800-2 values"), built to the class
values in spec.md "## Class values"; no maker's datasheet (the vendor file in the folder's references/ is reference only and was not
opened; its record was replaced by this element's, references/source.txt).
What it meets comes from the contracts and elements on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of
din-rail-35 / EN 60715 TH35-7.5); the control, status and encoder terminals are three placed terminal-plug elements (lib/inventory.csv
made_of "terminal-plug x3"), version pinned (2.0); every other size is a design choice, said so in spec.md.
1.1 (elec-r34): text only (review servo-drive-1.0 finding 1): the 1.0 kW is the rated shaft power of the motor the drive is sized
for, and the 3.4 A input current a design margin; geometry as 1.0.
1.2 (elec-r38): text only: pins.csv gives the encoder supply pins x3.t-5 / x3.t-6 the source's roles (supply+:5V, supply0), the
drive being the 5 V source servo-motor 1.0's encoder loads; geometry as 1.0.
Not placed in this version (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no
holes for a part it will place later): fan-cooling, led and screw-iso4762 of the inventory's made_of are not built yet. So it is cooled by
natural convection through the heat sink's vertical channels, its two status lenses are the toolkit's din.led, and it holds to the
rail by the toolkit's rail_clip with no screw mounting (as vfd-0.75kw 1.0).
Modelled from the outside in, the shape of vfd-0.75kw 1.1 (the same family of panel devices): the finned aluminium heat sink on the
rail clip, the moulded housing on the fins' front edges with the power terminals on its front at the top (L1 L2 L3 PE, supply) and
the bottom (U V W PE, motor), two status LEDs, a legend field, and three control plugs on the front (x1 digital and analogue control,
x2 the ready relay, x3 the encoder feedback); the rectifier, DC link, inverter, current loops and position loop inside are not
modelled. No safe torque off is claimed (spec.md Notes)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "servo-drive", "1.2", "device"
TITLE = "servo drive 1.0 kW, 3~ 380-480 V AC in, 3~ 0-480 V 0-400 Hz 3.0 A (9.0 A peak) out, incremental encoder feedback, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic servo drive, 1.0 kW (no ETIM class; IEC 61800-2 values); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); control, status and encoder terminals are placed terminal-plug 2.0 "
            "elements; sizes are design choices; the power terminals' conductor range and the digital inputs' switching levels are open (spec.md)")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "SERVODRV"
PARAMS = {}

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 65.0, 150.0                   # width (x 0 ... 65), heat sink height (z -75 ... 75), centred on the rail
# ---- heat sink: a base on the rail clip and vertical fins toward the front (design choices)
BASE_T = 8.0                         # base y -8 ... 0
FIN_N, FIN_T, FIN_D = 7, 2.0, 22.0   # fins: count, thickness (x), depth (y -30 ... -8); the outer two close the sides
# ---- housing on the fins' front edges (design choices)
HOUSING_D, HOUSING_Z = 90.0, 65.0    # depth (y -120 ... -30), half height (z -65 ... 65): 10.0 of fin channel shows above and below
# ---- power terminals on the housing's front, entries in its top (supply) and bottom (motor) faces (design choices)
P_PITCH = 14.0
LINE = ("L1", "L2", "L3", "PE")      # top: the supply and PE (the heat sink's earth)
MOTOR = ("U", "V", "W", "PE-m")      # bottom: to the motor; PE-m is the motor's earth (printed PE)
P_HEAD = dict(r=2.5, t=1.2, dz=6.0, entry=(5.0, 8.0, 0.5))
# ---- control plugs: terminal-plug 2.0 placed on the housing's front, mating face on it, wire entries down (design choices)
PLUG = "2.0"                         # terminal-plug version pinned
X1 = dict(poles=8, x=4.0, z=-36.0)   # EN RST LIM+ LIM- COM AI+ AI- AGND (spec.md Dimensions)
X2 = dict(poles=2, x=50.0, z=-36.0)  # RA RC: the ready relay, apart from the 24 V and analogue poles
X3 = dict(poles=6, x=17.5, z=-12.0)  # A+ A- B+ B- 5V 0V: the incremental encoder (spec.md Class values)
# ---- LEDs and legend field on the housing's front (design choices)
LEDS = (("led-rdy", "M-LENS-GREEN", 18.0), ("led-flt", "M-LENS-RED", 30.0))
LED_Z = 50.0
LEGEND = (8.0, 57.0, 8.0, 40.0)      # x0, x1, z0, z1

def terminals(P, pitch, nodes, y_face, z_edge, up, target, r, t, dz, entry, mat="M-ZINC"):
    """screw clamps along x, centred on the device, on a front face y_face: the head is the port node t-<name>; the wire entry is a
    slot cut into the end face z_edge (the shape of toolkit/din.py terminal_row, with a named node per terminal; as vfd-0.75kw 1.1)"""
    s = 1 if up else -1; x0 = (W - len(nodes) * pitch) / 2
    for i, nm in enumerate(nodes):
        cx = x0 + pitch * (i + 0.5); cz = z_edge - s * dz; n = f"t-{nm}"
        P.cyl(f"node:{n}|{mat}", (cx, y_face, cz), (cx, y_face - t, cz), r)
        P.pivot(n, "port", (cx, y_face - t, cz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        w, d, sl = entry; z0 = z_edge - (sl if up else 0.0)
        P.cutbox("M-GASKET", cx - w / 2, y_face + 2.0, z0 - (0.0 if up else 1.0), w, d, sl + 1.0, target)       # out past the end face
        P.box("M-GASKET", cx - w / 2, y_face + 2.0, z0, w, d, sl)                                               # the dark slot in its cut

def build():
    P = Prims(); A = "M-ALU-ANOD"; G = "M-GREY-PA"
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    P.box(A, 0, -BASE_T, -H / 2, W, BASE_T, H)                                              # heat sink base on the clip
    pitch = (W - FIN_T) / (FIN_N - 1)
    for i in range(FIN_N):
        P.box(A, i * pitch, -BASE_T - FIN_D, -H / 2, FIN_T, FIN_D, H)                       # fins: vertical channels, air rises through them
    y_f = -BASE_T - FIN_D - HOUSING_D                                                       # the housing's front face (y -120)
    hs = P.box(G, 0, y_f, -HOUSING_Z, W, HOUSING_D, 2 * HOUSING_Z)                          # housing on the fins' front edges
    terminals(P, P_PITCH, LINE, y_f, HOUSING_Z, True, hs, **P_HEAD)                         # supply and PE on top
    terminals(P, P_PITCH, MOTOR, y_f, -HOUSING_Z, False, hs, **P_HEAD)                      # motor and its PE below
    for tag, X in (("x1", X1), ("x2", X2), ("x3", X3)):                                     # control, relay and encoder plugs (placed, pinned)
        library.place(P, dict(element="terminal-plug", version=PLUG, tag=tag, parent="", x=X["x"], y=y_f, z=X["z"], yaw=0.0,
                              params=dict(poles=X["poles"])))
    for node, lens, x in LEDS: din.led(P, node, lens, x, y_f, LED_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: marks, ratings, generic label)
    P.collider("env", 0, y_f - 16.3, -H / 2, W, -y_f + 16.3 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip and heat sink", az=60, el=25),
            dict(name="top fin channels and supply terminals", az=230, el=55, center=(32.5, -60, 65), height=100),
            dict(name="control and encoder plugs", az=250, el=15, center=(32.5, -128, -24), height=50),
            dict(name="motor terminals", az=230, el=-35, center=(32.5, -120, -60), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
