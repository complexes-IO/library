#!/usr/bin/env python3
"""relay-aux-2no2nc: auxiliary contactor (contactor relay), 24 V DC coil, 2 N.O. + 2 N.C., on the 35 mm rail. A generic element (OPERATING.md
12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000196 "Auxiliary contactor, relay", built to the class
values in spec.md "## Class values"; no maker's datasheet. What it meets comes from the contracts on file: the rail clip from
toolkit/din.py (rail_clip, the 35 x 7.5 rail of din-rail-35 / EN 60715 TH35-7.5); every other size is a design choice, said so in
spec.md. Modelled from the outside in: housing, terminal shoulders with one screw-clamp port per terminal, coil LED and the contact
carrier's front tab in its window (the state the twin shows); the magnet system inside is not modelled in 1.0.
1.2 (elec-r32): text only, geometry as 1.1. The coil's 2.4 W / 0.10 A (behaviour.csv's load row) also in ratings.csv (coil_p design,
load_i derived) and spec.md's Notes: one figure, one home (review relay-aux-2no2nc-1.1 finding 1).
1.3 (elec-r33): text only, geometry as 1.2. ratings.csv coil_p's "design:" source names the rule the figure meets, the panel's 24 V
budget (ELR-020), as behaviour.csv's load row does (review relay-aux-2no2nc-1.2 finding 1, elec-r32 finding 2)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "relay-aux-2no2nc", "1.3", "device"
TITLE = "auxiliary contactor relay, 24 V DC coil, 2 NO + 2 NC, 10 A, screw terminals, 35 mm rail (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Auxiliary contactor, relay (ETIM 10.0 EC000196); class values in spec.md; rail clip from "
            "toolkit/din.py (EN 60715 TH35-7.5 rail, din-rail-35); sizes are design choices; the terminals' conductor range is open (spec.md)")
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "RAUX"
PARAMS = dict(operated=False)

# ---- envelope (design choices; the class values Width / Height / Depth in spec.md)
W, H = 45.0, 82.0                    # width (x), height (z): z -41 ... 41, centred on the rail
D_BASE = 40.0                        # base and terminal shoulders: front face at y -40
D = 68.0                             # front housing face at y -68; 75.5 overall with the 7.5 behind the crown (din.rail_clip)
FH_X, FH_Z = (2.0, 43.0), (-24.0, 24.0)   # front housing (coil and contact carrier cover)
# ---- terminals: two rows of five screw clamps (design choices: pitch, head, entry); the conductor range is open (spec.md)
PITCH = 8.4
TOP = ("A1", "13", "21", "31", "43")       # coil + and each contact's first terminal (function-number marking)
BOT = ("A2", "14", "22", "32", "44")
HEAD_R, HEAD_T, HEAD_DZ = 2.2, 1.2, 6.0    # screw head radius, height, centre 6.0 in from the end face
ENTRY = (3.6, 9.0, 0.5)                    # wire entry slot: width (x), depth (y), cut into the end face (z)
# ---- front: coil LED, contact carrier tab in its window, legend field (design choices)
LED = (37.0, -8.0)                         # x, z
WIN = (8.0, 20.0, -14.0, -4.0, 18.0)       # window x0, x1, z0, z1, pocket depth behind the face
TAB = (9.0, 19.0, -13.0, -5.0, 1.0, 9.0)   # carrier tab x0, x1, z0, z1, set back from the face, length (y)
TRAVEL = 3.5                               # carrier travel toward the mounting plane (+y) when the coil pulls in

def terminals(P, marks, up, target):
    """five screw clamps on a shoulder (front face y = -D_BASE): the head is the port node t-<mark>; the wire entry is a slot cut
    into the end face (the toolkit's terminal_row shape, din.py, with a named node per terminal)"""
    s = 1 if up else -1; z_edge = s * H / 2; x0 = (W - len(marks) * PITCH) / 2
    for i, mk in enumerate(marks):
        cx = x0 + PITCH * (i + 0.5); cz = z_edge - s * HEAD_DZ; n = f"t-{mk}"
        P.cyl(f"node:{n}|M-ZINC", (cx, -D_BASE, cz), (cx, -D_BASE - HEAD_T, cz), HEAD_R)
        P.pivot(n, "port", (cx, -D_BASE - HEAD_T, cz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        w, d, t = ENTRY; z0 = z_edge - (t if up else 0.0)
        P.cutbox("M-GASKET", cx - w / 2, -D_BASE + 2.0, z0 - (0.0 if up else 1.0), w, d, t + 1.0, target)          # out past the end face
        P.box("M-GASKET", cx - w / 2, -D_BASE + 2.0, z0, w, d, t)                                                  # the dark slot in its cut

def build(operated=False):
    P = Prims(); G = "M-GREY-PA"
    base = P.box(G, 0, -D_BASE, -H / 2, W, D_BASE, H)                                       # base with the terminal shoulders
    fh = P.box(G, FH_X[0], -D, FH_Z[0], FH_X[1] - FH_X[0], D - D_BASE, FH_Z[1] - FH_Z[0])  # front housing
    din.rail_clip(P, 0, W)                                                                  # the rail latch (toolkit contract)
    terminals(P, TOP, True, base); terminals(P, BOT, False, base)
    x0, x1, z0, z1, pd = WIN
    P.cutbox("M-GASKET", x0, -D - 0.5, z0, x1 - x0, pd + 0.5, z1 - z0, fh)                  # carrier window and its pocket
    tx0, tx1, tz0, tz1, back, ln = TAB; ty = -D + back + (TRAVEL if operated else 0.0)
    P.box("node:carrier|M-YELLOW-PA", tx0, ty, tz0, tx1 - tx0, ln, tz1 - tz0)                # carrier front tab: the contact state shown
    P.pivot("carrier", "translate", ((tx0 + tx1) / 2, -D + back, (tz0 + tz1) / 2), axis=(0, 1, 0), range=(0, TRAVEL))
    din.led(P, "led-coil", "M-LENS-YELLOW", LED[0], -D, LED[1])                              # coil energised
    P.box("M-WHITE-PA", 6.0, -D - 0.1, 4.0, 33.0, 0.1, 17.0)                                 # legend field (decal: marks, 24 V DC, generic label)
    P.collider("env", 0, -D - 0.3, -H / 2, W, D + 7.8, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear rail clip", az=60, el=25),
            dict(name="face LED and carrier window", az=255, el=10, center=(22.5, -68, 0), height=56),
            dict(name="operated carrier pulled in", az=255, el=10, center=(14, -68, -9), height=20, params=dict(operated=True)),
            dict(name="top terminal row and wire entries", az=230, el=55, center=(22.5, -40, 38), height=24)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
