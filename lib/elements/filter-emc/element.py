#!/usr/bin/env python3
"""filter-emc: three-phase EMC line filter (radio interference suppression), 480 V AC, 16 A, 50 / 60 Hz, a closed steel housing on a
base plate screwed to the back panel by four M5 screws, LINE terminals on top and LOAD terminals below, each row with its PE.
A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002564 "Filter for
low-voltage", built to the class values in spec.md "## Class values"; no maker's datasheet. What it meets comes from the standards on
file: the four panel-screw holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); their pattern, and every other size,
is a design choice, said so in spec.md. Modelled from the outside in: base plate, housing, two terminal blocks with a green-yellow PE
block beside each, rating plate; the chokes and capacitors inside are not modelled in 1.0."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "filter-emc", "1.0", "device"
TITLE = "EMC line filter, three-phase 480 V AC 16 A, 50 / 60 Hz, steel housing on a base plate for four M5 panel screws, screw terminals (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Filter for low-voltage (ETIM 10.0 EC002564); class values in spec.md; panel-screw holes ISO 273 "
            "medium for M5 (lib/standards/holes.csv); sizes and the hole pattern are design choices; the terminals' conductor range is "
            "open (spec.md)")
ORIGIN = "surface-mount device: back face (the base plate) y = 0, lower-left mounting hole x = 0, z = 0, body toward -y"
COMMAND = "EMCFLT"
PARAMS = {}

# ---- base plate and panel holes (design choices; Ø5.5 = ISO 273 medium for M5, holes.csv)
PLATE_X, PLATE_Z, PLATE_T = (-10.0, 50.0), (-10.0, 220.0), 2.0   # base plate x, z span and sheet thickness (y -2 ... 0)
HOLES_X, HOLES_Z = (0.0, 40.0), (0.0, 210.0)                     # the four M5 holes: a 40.0 x 210.0 pattern in the plate's end tabs
HOLE_D = 5.5
# ---- housing (design choices; Class values Width / Height / Depth are not features of this class)
HOUSING_Z, HOUSING_D = (25.0, 185.0), 50.0                       # housing z span (160 tall), depth in front of the plate (y -52 ... -2)
# ---- terminal blocks on the housing front, LINE on top, LOAD below (design choices); the conductor range is open (spec.md)
PITCH, BLOCK_D, BLOCK_H, BLOCK_M = 12.0, 18.0, 24.0, 2.5         # terminal pitch, block depth (y), height (z), margin at each end
BLOCK_X0 = -9.0                                                  # blocks start 1.0 in from the housing's left side
TOP_Z1, BOT_Z0 = 181.0, 29.0                                     # LINE block's top face, LOAD block's bottom face: 4.0 in from the housing ends
HEAD = dict(r=2.5, t=1.2, dz=6.0, entry=(4.5, 9.0, 0.5))         # screw head radius, height, centre in from the end face; entry slot w, d, depth
LINE = ("L1", "L2", "L3")
LOAD = ("L1-load", "L2-load", "L3-load")
# ---- rating plate on the housing front (design choice)
PLATE_LBL = (-4.0, 44.0, 68.0, 142.0)                            # x0, x1, z0, z1

def terminals(P, x0, nodes, y_face, z_edge, up, target, r, t, dz, entry, mat="M-ZINC"):
    """screw clamps along x from x0 on a block's front face y_face: the head is the port node t-<name>; the wire entry is a slot cut
    into the block's end face z_edge (the shape of toolkit/din.py terminal_row, with a named node per terminal)"""
    s = 1 if up else -1
    for i, nm in enumerate(nodes):
        cx = x0 + PITCH * (i + 0.5); cz = z_edge - s * dz; n = f"t-{nm}"
        P.cyl(f"node:{n}|{mat}", (cx, y_face, cz), (cx, y_face - t, cz), r)
        P.pivot(n, "port", (cx, y_face - t, cz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        w, d, sl = entry; z0 = z_edge - (sl if up else 0.0)
        P.cutbox("M-GASKET", cx - w / 2, y_face + 2.0, z0 - (0.0 if up else 1.0), w, d, sl + 1.0, target)       # out past the end face
        P.box("M-GASKET", cx - w / 2, y_face + 2.0, z0, w, d, sl)                                               # the dark slot in its cut

def row(P, nodes, pe, up):
    """one terminal row: a grey block with the three line terminals and a green-yellow block with the PE terminal beside it"""
    yf = -PLATE_T - HOUSING_D - BLOCK_D                                                     # the blocks' front face
    z0 = TOP_Z1 - BLOCK_H if up else BOT_Z0; ze = TOP_Z1 if up else BOT_Z0
    w1 = len(nodes) * PITCH + 2 * BLOCK_M; w2 = PITCH + 2 * BLOCK_M
    b = P.box("M-GREY-PA", BLOCK_X0, yf, z0, w1, BLOCK_D, BLOCK_H)
    terminals(P, BLOCK_X0 + BLOCK_M, nodes, yf, ze, up, b, **HEAD)
    g = P.box("M-GREEN-YELLOW", BLOCK_X0 + w1, yf, z0, w2, BLOCK_D, BLOCK_H)
    terminals(P, BLOCK_X0 + w1 + BLOCK_M, (pe,), yf, ze, up, g, **HEAD)

def build():
    P = Prims(); G = "M-GALV"
    (px0, px1), (pz0, pz1) = PLATE_X, PLATE_Z
    plate = P.box(G, px0, -PLATE_T, pz0, px1 - px0, PLATE_T, pz1 - pz0)                   # base plate on the panel
    for x in HOLES_X:
        for z in HOLES_Z:
            P.hole("M-GASKET", (x, 0.5, z), (x, -PLATE_T - 0.5, z), HOLE_D / 2, plate)      # M5 panel screw, ISO 273 medium
    hz0, hz1 = HOUSING_Z
    P.box(G, px0, -PLATE_T - HOUSING_D, hz0, px1 - px0, HOUSING_D, hz1 - hz0)              # housing (closed steel box)
    row(P, LINE, "PE", True)                                                                # LINE: from the supply
    row(P, LOAD, "PE-load", False)                                                          # LOAD: to the drive or controller
    x0, x1, z0, z1 = PLATE_LBL
    P.box("M-WHITE-PA", x0, -PLATE_T - HOUSING_D - 0.1, z0, x1 - x0, 0.1, z1 - z0)        # rating plate (decal)
    yf = -PLATE_T - HOUSING_D - BLOCK_D - HEAD["t"]
    P.collider("env", px0, yf, pz0, px1 - px0, -yf, pz1 - pz0)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear base plate and panel holes", az=60, el=20),
            dict(name="elevation", az=270, el=0),
            dict(name="line terminals and PE", az=230, el=40, center=(20, -60, 168), height=70),
            dict(name="load terminals and PE", az=230, el=-30, center=(20, -60, 42), height=70)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
