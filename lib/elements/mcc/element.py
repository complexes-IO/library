#!/usr/bin/env python3
"""mcc: motor control centre, one vertical section. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of
the ETIM 10.0 class EC000712 "Empty enclosure for switchgear", built to the class values in spec.md "## Class values"; no maker's
datasheet, no vendor file opened (the folder's earlier acquisition stub was not read; since 2.0 its record is kept verbatim as the
end block of references/source.txt, under this element's own, and nothing here is taken from it).
Inventory row mcc (pinned 4, EM 2026-11-08: "our own generic design of the section (bus, bucket openings, door) holding the starters,
MCCBs and VFDs on file").
A floor-standing sheet-steel section 600 wide, 500 deep, 2300 high on a 100 plinth: on the left the unit space (four bucket spaces
behind four doors, three of one module and one of two, a module 340 high), on the right a vertical wireway behind its own door, at
the top the horizontal bus compartment behind a fixed cover, at the bottom a pull space behind a fixed cover. Behind the unit space an
insulating barrier with a row of three stab openings per bucket space; behind it three vertical phase bars, each rising to its own
horizontal phase bar in the top compartment; a protective (PE) bar along the bottom of the back. Each horizontal phase bar and the PE
bar is a port node at its right end (x 580, facing +x), where the splice plate to the next section (standing against x = 600) lands;
both side sheets carry a splice opening in front of the bar ends (one for the three phase bars, one for the PE bar), so a splice passes
from one section's bar end to the next one's, reached from the bus compartment and the pull space (PIN-002 gender none).
2.0 (elec-r49, review mcc-1.0 finding 1): the ports moved from the left ends, which faced the closed side sheet 18 away, to the right
ends, and the splice openings were cut; the bars, the zones and the doors are 1.0's.
Buckets, their devices (disc-3p-30a, contactor and overload, vfd-0.75kw), stabs and splice plates are not part of this element: placed
elements, a later version or an assembly. No bus rating, short-circuit rating, clearance, IP or NEMA type is claimed (spec.md). Every
size is a design choice, said so in spec.md."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "mcc", "2.0", "enclosure"
TITLE = "motor control centre section, generic, 600 x 500 x 2300, four bucket doors, vertical wireway, horizontal and vertical bus, PE bar (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Empty enclosure for switchgear (ETIM 10.0 EC000712), one motor control centre section; class values "
            "in spec.md; every size a design choice; bus bars modelled with no rating claimed; buckets and their devices are placed "
            "elements; no vendor file opened")
ORIGIN = ("floor plane z = 0 at the section's front-left corner x = 0, y = 0 (the body's front face; doors and covers at y < 0); the "
          "back face y = 500 toward the wall; the next section stands against x = 600")
COMMAND = "MCC"
PARAMS = dict()

# ---- the section (design choices, spec.md "Its own sizes")
W, D = 600.0, 500.0                  # width (x) and depth (y) of the body
PLINTH = 100.0                       # plinth height: z 0 ... 100
H = 2300.0                           # overall height, plinth included: the body z 100 ... 2300
T, PT = 2.0, 3.0                     # sheet: body, doors, covers 2.0; plinth 3.0
UNIT_X = 398.0                       # unit space x 2 ... 398, the partition x 398 ... 400, the vertical wireway x 400 ... 598
UNIT_Y = 300.0                       # bucket depth: the shelves and the partition y 0 ... 300, the barrier behind them
BAR_T = 3.0                          # the insulating barrier y 300 ... 303
MODULE = 340.0                       # one bucket module (design choice)
Z_UNIT = 300.0                       # unit space z 300 ... 2000; the pull space below it, the bus compartment above
Z_BUS = Z_UNIT + 5 * MODULE          # 2000
DOORS = ((1, 4), (2, 3), (3, 2), (4, 0))   # door k: its bottom module line (0 = Z_UNIT); door 4 is two modules (a drive's bucket)
GAP = 2.0                            # door clearance at each edge (4 between two doors)
DOOR_X = UNIT_X - 1.0                # unit doors x 0 ... 397, hinged at x = 0
WW_X = UNIT_X + 3.0                  # wireway door x 401 ... 600, hinged at x = 600
SWING = 110.0                        # every door opens 0 ... 110 degrees outward
KNOB = (24.0, 16.0, 60.0)            # quarter-turn latch knob on each door: x, y (proud), z (edges >= 8 for the AutoCAD fillet pre-flight)
KNOB_IN = 25.0                       # its near edge from the door's free edge

# ---- bus (design choices; no rating claimed: spec.md)
PH_X = (120.0, 200.0, 280.0)         # vertical phase bars' centres x (L1, L2, L3), 80 apart
PH_Y = (340.0, 370.0, 400.0)         # each phase's bars at their own depth (front face y), so no bar crosses another's
PH_Z = (2100.0, 2160.0, 2220.0)      # each horizontal phase bar's bottom face z; its vertical bar rises to it
BAR = (30.0, 10.0)                   # phase bar section: 30 wide x 10 thick
HB_X = (20.0, 580.0)                 # horizontal bars x 20 ... 580 (the port at the right end, x 580, toward the next section)
SPLICE_PH = (330.0, 420.0, 2090.0, 2260.0)   # splice opening for the phase bars in each side sheet: y 330 ... 420, z 2090 ... 2260 (10 clear round the bars)
SPLICE_PE = (476.0, 496.0, 140.0, 200.0)     # splice opening for the PE bar in each side sheet: y 476 ... 496, z 140 ... 200 (10 clear)
VB_Z0 = Z_UNIT + 20.0                # vertical bars from z 320
SUP_Z = (600.0, 1200.0, 1800.0)      # vertical bars' insulating supports (40 high) to the back sheet
SUP_H, SUP_X = 40.0, ((30.0, 60.0), (540.0, 570.0))   # horizontal bars' supports at both ends
PE_BAR = (6.0, 40.0, 150.0, D - T - 12.0)   # PE bar: thickness (y), height (z), bottom z, front face y (486: y 486 ... 492, on 6 deep brackets to the back sheet)
STAB = (20.0, 40.0)                  # stab opening in the barrier: x, z; three per bucket space at the bars' x, mid-height

def door(P, name, x0, x1, z0, z1, hinge_x):
    """a door leaf over the front edges (y -2 ... 0), its latch knob near the free edge; it rotates about the hinge edge (x = hinge_x, y = 0)"""
    Ld = f"node:{name}|M-STEEL-7035"
    P.box(Ld, x0, -T, z0, x1 - x0, T, z1 - z0)
    kx = (x1 - KNOB_IN - KNOB[0]) if hinge_x < x1 else (x0 + KNOB_IN)
    P.box(f"node:{name}|M-BLACK-PA", kx, -T - KNOB[1], (z0 + z1) / 2 - KNOB[2] / 2, KNOB[0], KNOB[1], KNOB[2])
    rng = (0.0, -SWING) if hinge_x < x1 else (0.0, SWING)                                          # both outward (toward -y)
    P.pivot(name, "rotate", (hinge_x, 0.0, (z0 + z1) / 2), axis=(0, 0, 1), range=rng)
    P.collider(name, x0, -T - KNOB[1], z0, x1 - x0, T + KNOB[1], z1 - z0)

def build():
    P = Prims(); S, G, CU, IN = "M-STEEL-7035", "M-GALV", "M-CU", "M-GREY-PA"
    # ---------------- plinth: four 3.0 plates round the footprint
    P.box(S, 0, 0, 0, W, PT, PLINTH); P.box(S, 0, D - PT, 0, W, PT, PLINTH)
    P.box(S, 0, PT, 0, PT, D - 2 * PT, PLINTH); P.box(S, W - PT, PT, 0, PT, D - 2 * PT, PLINTH)
    # ---------------- body: bottom and top full, sides between them, back between the sides
    P.box(S, 0, 0, PLINTH, W, D, T); P.box(S, 0, 0, H - T, W, D, T)
    for x in (0.0, W - T):                                                                          # side sheets, each with the two splice openings
        side = P.box(S, x, 0, PLINTH + T, T, D, H - PLINTH - 2 * T)
        for y0, y1, z0, z1 in (SPLICE_PH, SPLICE_PE):
            P.cutbox(S, x - 1.0, y0, z0, T + 2.0, y1 - y0, z1 - z0, side)
    P.box(S, T, D - T, PLINTH + T, W - 2 * T, T, H - PLINTH - 2 * T)
    # ---------------- unit space: shelves at the module lines under each door, the partition, the bus compartment's floor
    for zl in (Z_UNIT,) + tuple(Z_UNIT + MODULE * m for m in (2, 3, 4)):
        P.box(G, T, 0, zl, UNIT_X - T, UNIT_Y, T)
    P.box(G, UNIT_X, 0, Z_UNIT, 2.0, UNIT_Y, Z_BUS - Z_UNIT)                                          # partition: unit space | wireway
    P.box(G, T, 0, Z_BUS, W - 2 * T, UNIT_Y, T)                                                      # bus compartment floor (the doors' top line)
    # ---------------- the barrier behind the buckets, a row of three stab openings per bucket space
    bar = P.box(IN, T, UNIT_Y, Z_UNIT + T, UNIT_X + 2.0 - T, BAR_T, Z_BUS - Z_UNIT - T)
    for k, m in DOORS:
        n = 2 if k == 4 else 1; zm = Z_UNIT + MODULE * m + MODULE * n / 2
        for cx in PH_X: P.cutbox(IN, cx - STAB[0] / 2, UNIT_Y - 1.0, zm - STAB[1] / 2, STAB[0], BAR_T + 2.0, STAB[1], bar)
    # ---------------- covers over the pull space and the bus compartment (fixed, bolted: bolts not modelled)
    P.box(S, 0, -T, PLINTH, W, T, Z_UNIT - PLINTH - GAP)
    P.box(S, 0, -T, Z_BUS + GAP, W, T, H - Z_BUS - GAP)
    # ---------------- doors: four bucket doors hinged left, the wireway door hinged right
    for k, m in DOORS:
        n = 2 if k == 4 else 1; z0 = Z_UNIT + MODULE * m
        door(P, f"door-{k}", 0.0, DOOR_X, z0 + GAP, z0 + MODULE * n - GAP, 0.0)
    door(P, "door-ww", WW_X, W, Z_UNIT + GAP, Z_BUS - GAP, W)
    # ---------------- bus: per phase a vertical bar up to its own horizontal bar; insulating supports to the back sheet
    bw, bt = BAR
    for i, (cx, y, zh) in enumerate(zip(PH_X, PH_Y, PH_Z)):
        ph = f"bus-l{i + 1}"
        P.box(CU, cx - bw / 2, y, VB_Z0, bw, bt, zh - VB_Z0)                                          # vertical bar, its top on the horizontal bar
        for zs in SUP_Z: P.box(IN, cx - bw / 2, y + bt, zs, bw, D - T - y - bt, SUP_H)
        P.box(f"node:{ph}|{CU}", HB_X[0], y, zh, HB_X[1] - HB_X[0], bt, bw)                            # horizontal bar, z zh ... zh + 30
        for sx0, sx1 in SUP_X: P.box(IN, sx0, y + bt, zh, sx1 - sx0, D - T - y - bt, bw)
        P.pivot(ph, "port", (HB_X[1], y + bt / 2, zh + bw / 2), axis=(1, 0, 0), range=(0, 0), unit="bus", gender="none")
    pt, ph_, pz, py = PE_BAR
    P.box(f"node:pe-bus|{CU}", HB_X[0], py, pz, HB_X[1] - HB_X[0], pt, ph_)                            # PE bar along the bottom of the back
    for sx0, sx1 in SUP_X: P.box(S, sx0, py + pt, pz, sx1 - sx0, D - T - py - pt, ph_)                 # its steel brackets (bonded to the body)
    P.pivot("pe-bus", "port", (HB_X[1], py + pt / 2, pz + ph_ / 2), axis=(1, 0, 0), range=(0, 0), unit="PE", gender="none")
    P.collider("body", 0, 0, 0, W, D, H)
    return P

PREVIEWS = [dict(name="front three-quarter", az=235, el=18),
            dict(name="rear three-quarter", az=50, el=20),
            dict(name="bus compartment and stab row, front cut away", az=250, el=15, center=(300, 300, 2100), height=500),
            dict(name="pull space and PE bar", az=230, el=20, center=(300, 400, 200), height=400),
            dict(name="right side: splice openings at the bar ends", az=20, el=15, center=(600, 300, 1200), height=2400)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
