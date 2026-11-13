#!/usr/bin/env python3
"""vfd-0.75kw: variable frequency drive (frequency converter), 0.75 kW, three-phase 380 ... 480 V AC in, three-phase 0 ... 480 V
0 ... 400 Hz out, 2.2 A, on the 35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the
ETIM 10.0 class EC001857 "Frequency converter =< 1 kV", built to the class values in spec.md "## Class values"; no maker's datasheet
(the vendor file in the folder's references/ is reference only and was not opened).
What it meets comes from the contracts and elements on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of
din-rail-35 / EN 60715 TH35-7.5); the control terminals are two placed terminal-plug elements (lib/inventory.csv made_of
"terminal-plug x2"), version pinned (2.0 from vfd 1.1); every other size is a design choice, said so in spec.md.
1.1 (elec-r26): the plugs' pin moves to terminal-plug 2.0 (review elec-r22 finding 1 gave the plug's sockets a 6.0 engagement depth);
the drive's own shape, nodes and origin are as 1.0, so a minor.
1.2 (elec-r34): text only (review vfd-0.75kw-1.1 findings 1 and 2): the inputs DI1 ... DI3 are IEC 61131-2 type 1 by design and
their switching levels that standard's table, a document wanted (class B), as servo-drive; geometry as 1.1.
Not placed in this version (OPERATING.md 12, quality at the source: a host places only common parts past station 6 and models no
holes for a part it will place later): fan-cooling, led, screw-iso4762 and din-clip-35 of the inventory's made_of are not built
yet. So the drive is cooled by natural convection through the heat sink's vertical channels, its two status lenses are the toolkit's din.led, it
holds to the rail by the toolkit's rail_clip, and it has no screw mounting.
Modelled from the outside in: the finned aluminium heat sink on the rail clip, the moulded housing on the fins' front edges with the
power terminals on its front at the top (L1 L2 L3 PE, supply) and the bottom (U V W PE, motor), two status LEDs, a legend field, and
the two control plugs on the front; the rectifier, DC link, inverter and control board inside are not modelled."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "vfd-0.75kw", "1.2", "device"
TITLE = "variable frequency drive 0.75 kW, 3~ 380-480 V AC in, 3~ 0-480 V 0-400 Hz 2.2 A out, V/f, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Frequency converter =< 1 kV (ETIM 10.0 EC001857); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); control terminals are placed terminal-plug 2.0 elements; sizes are "
            "design choices; the power terminals' conductor range (IEC 60947-1) and the inputs' switching levels (design: IEC 61131-2 "
            "type 1) are a standard's tables not on file (spec.md)")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "VFD"
PARAMS = {}

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 72.0, 140.0                   # width (x 0 ... 72), heat sink height (z -70 ... 70), centred on the rail
# ---- heat sink: a base on the rail clip and vertical fins toward the front (design choices)
BASE_T = 8.0                         # base y -8 ... 0
FIN_N, FIN_T, FIN_D = 7, 2.0, 22.0   # fins: count, thickness (x), depth (y -30 ... -8); the outer two close the sides
# ---- housing on the fins' front edges (design choices)
HOUSING_D, HOUSING_Z = 90.0, 60.0    # depth (y -120 ... -30), half height (z -60 ... 60): 10.0 of fin channel shows above and below
# ---- power terminals on the housing's front, entries in its top (supply) and bottom (motor) faces (design choices)
P_PITCH = 15.0
LINE = ("L1", "L2", "L3", "PE")      # top: the supply and PE (the heat sink's earth)
MOTOR = ("U", "V", "W", "PE-m")      # bottom: to the motor; PE-m is the motor's earth (printed PE)
P_HEAD = dict(r=2.5, t=1.2, dz=6.0, entry=(5.0, 8.0, 0.5))
# ---- control plugs: terminal-plug 2.0 placed on the housing's front, mating face on it, wire entries down (design choices)
PLUG = "2.0"                         # terminal-plug version pinned (1.0 at vfd 1.0)
X1 = dict(poles=7, x=6.0, z=-30.0)   # DI1 DI2 DI3 COM AI AO AGND (spec.md Dimensions)
X2 = dict(poles=2, x=52.0, z=-30.0)  # RA RC: the relay output, apart from the 24 V and analogue poles
# ---- LEDs and legend field on the housing's front (design choices)
LEDS = (("led-rdy", "M-LENS-GREEN", 20.0), ("led-flt", "M-LENS-RED", 32.0))
LED_Z = 44.0
LEGEND = (8.0, 64.0, 0.0, 36.0)      # x0, x1, z0, z1

def terminals(P, pitch, nodes, y_face, z_edge, up, target, r, t, dz, entry, mat="M-ZINC"):
    """screw clamps along x, centred on the device, on a front face y_face: the head is the port node t-<name>; the wire entry is a
    slot cut into the end face z_edge (the shape of toolkit/din.py terminal_row, with a named node per terminal; as
    controller-thyristor 1.0)"""
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
    for tag, X in (("x1", X1), ("x2", X2)):                                                 # control plugs (placed elements, pinned)
        library.place(P, dict(element="terminal-plug", version=PLUG, tag=tag, parent="", x=X["x"], y=y_f, z=X["z"], yaw=0.0,
                              params=dict(poles=X["poles"])))
    for node, lens, x in LEDS: din.led(P, node, lens, x, y_f, LED_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: marks, ratings, generic label)
    P.collider("env", 0, y_f - 16.3, -H / 2, W, -y_f + 16.3 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip and heat sink", az=60, el=25),
            dict(name="top fin channels and supply terminals", az=230, el=55, center=(36, -60, 60), height=100),
            dict(name="control plugs", az=250, el=15, center=(36, -128, -28), height=40),
            dict(name="motor terminals", az=230, el=-35, center=(36, -120, -55), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
