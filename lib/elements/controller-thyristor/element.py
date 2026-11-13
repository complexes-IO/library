#!/usr/bin/env python3
"""controller-thyristor: three-phase thyristor (SCR) power controller for resistive heater loads, 480 V AC, 20 A, burst firing from a
0 ... 10 V setpoint, on the 35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the
ETIM 10.0 class EC011564 "Thyristor power controller", built to the class values in spec.md "## Class values"; no maker's datasheet.
What it meets comes from the contracts on file: the rail clip from toolkit/din.py (rail_clip, the 35 x 7.5 rail of din-rail-35 /
EN 60715 TH35-7.5); every other size is a design choice, said so in spec.md. Modelled from the outside in: the finned aluminium heat
sink on the rail clip (vertical channels, natural convection), the moulded cover on the fins' front edges with the power terminals on
its shoulders (LINE on top with PE, LOAD below), and the raised control front with its six control terminals, five LEDs and legend
field; the thyristors and the firing electronics inside are not modelled in 1.0."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "controller-thyristor", "1.0", "device"
TITLE = "thyristor power controller, three-phase 480 V AC 20 A, burst firing, 0-10 V setpoint, 24 V DC supply, finned heat sink, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Thyristor power controller (ETIM 10.0 EC011564); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); sizes are design choices; the terminals' conductor range is open (spec.md)")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "SCRPC"
PARAMS = {}

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 90.0, 150.0                   # width (x 0 ... 90), height (z -75 ... 75), centred on the rail
# ---- heat sink: a base on the rail clip and vertical fins toward the front (design choices)
BASE_T = 8.0                         # base y -8 ... 0
FIN_N, FIN_T, FIN_D = 9, 2.0, 40.0   # fins: count, thickness (x), depth (y -48 ... -8); the outer two close the sides
# ---- cover on the fins' front edges: shoulders carry the power terminals, the raised front the control (design choices)
COVER_D, COVER_Z = 30.0, 55.0        # shoulder depth (y -78 ... -48), half height (z -55 ... 55): 20.0 of fin channel shows above and below
RAISED = (2.0, 88.0, 20.0, 32.0)     # raised front x0, x1, depth in front of the shoulders (y -98 ... -78), half height (z -32 ... 32)
# ---- power terminals on the shoulders (design choices); the conductor range is open (spec.md)
P_PITCH = 20.0
LINE = ("L1", "L2", "L3", "PE")      # top: the supply and PE (the heat sink's earth)
LOAD = ("T1", "T2", "T3")            # bottom: to the heaters
P_HEAD = dict(r=3.0, t=1.5, dz=7.0, entry=(6.0, 10.0, 0.5))
# ---- control terminals on the raised front, wire entries in its top face (design choices)
C_PITCH = 7.5
CTRL = ("24V", "0V", "EN", "AI", "13", "14")
C_HEAD = dict(r=1.6, t=1.0, dz=5.0, entry=(3.0, 8.0, 0.5))
# ---- LEDs and legend field on the raised front (design choices)
LEDS = (("led-on", "M-LENS-GREEN", 20.0), ("led-l1", "M-LENS-YELLOW", 35.0), ("led-l2", "M-LENS-YELLOW", 45.0),
        ("led-l3", "M-LENS-YELLOW", 55.0), ("led-fault", "M-LENS-RED", 70.0))
LED_Z = 10.0
LEGEND = (10.0, 80.0, -26.0, 0.0)    # x0, x1, z0, z1

def terminals(P, pitch, nodes, y_face, z_edge, up, target, r, t, dz, entry, mat="M-ZINC"):
    """screw clamps along x, centred on the device, on a front face y_face: the head is the port node t-<name>; the wire entry is a
    slot cut into the end face z_edge (the shape of toolkit/din.py terminal_row, with a named node per terminal)"""
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
    y_sh = -BASE_T - FIN_D - COVER_D                                                        # the shoulders' front face (y -78)
    sh = P.box(G, 0, y_sh, -COVER_Z, W, COVER_D, 2 * COVER_Z)                               # cover on the fins' front edges
    terminals(P, P_PITCH, LINE, y_sh, COVER_Z, True, sh, **P_HEAD)                          # LINE and PE on top
    terminals(P, P_PITCH, LOAD, y_sh, -COVER_Z, False, sh, **P_HEAD)                        # LOAD below
    x0, x1, rd, rz = RAISED; y_f = y_sh - rd
    rf = P.box(G, x0, y_f, -rz, x1 - x0, rd, 2 * rz)                                        # raised control front (y -98)
    terminals(P, C_PITCH, CTRL, y_f, rz, True, rf, **C_HEAD)                                # control terminals, entries in its top face
    for node, lens, x in LEDS: din.led(P, node, lens, x, y_f, LED_Z)
    lx0, lx1, lz0, lz1 = LEGEND
    P.box("M-WHITE-PA", lx0, y_f - 0.1, lz0, lx1 - lx0, 0.1, lz1 - lz0)                     # legend field (decal: marks, ratings, generic label)
    P.collider("env", 0, y_f - 0.3, -H / 2, W, -y_f + 0.3 + 7.5, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip and heat sink", az=60, el=25),
            dict(name="top fin channels and line terminals", az=230, el=55, center=(45, -50, 60), height=120),
            dict(name="control front LEDs and terminals", az=255, el=15, center=(45, -98, 10), height=50),
            dict(name="load terminals", az=230, el=-35, center=(45, -78, -50), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
