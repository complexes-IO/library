#!/usr/bin/env python3
"""lift-vrc: a vertical reciprocating conveyor (a goods lift between two conveyor levels), our own design (OPERATING.md 12, own
designs; inventory row lift-vrc, own_design "yes": "vertical reciprocating conveyor (our own build: mast, carriage, roller deck)",
the conveyor family, EM 2026-11-08). A two-mast portal: two masts on anchored foot plates, joined at the top by a beam, and one
carriage (node `carriage`) that runs straight up between them, 2250 from the lower level to the upper one. The carriage is a flat
deck 700 x 1600 on two side beams, with an upright on each side facing its mast. At the lower stop the uprights stand on the foot
plates and the deck's top is at the conveyor family's hand-off height (conveyor-roller's TOP, 750, read with library.load, so the
two cannot drift apart); at the upper stop it is at 3000. Goods enter and leave along y, between the masts.
Not drawn, placed in a later version once their elements are on file (OPERATING.md 12: a host doesn't model holes for a part it
places later): the hoist (motor-iec71-370w and gear-reducer per the folder's plan), the guide shoes on
the masts, the enclosure, gates and light curtains that guard the lift (ASME B20.1 is not on file; the guarding is the
assembly's), and the controls. The flat deck is the carrying surface (1.1, review lift-vrc-1.0 finding 1, option b): no roller
section stands on it, because conveyor-roller is floor-standing (its rollers 750 above its own base) and would lift the goods off
the hand-off level. Every size is a design choice; the anchor holes ISO 273. No load, speed, cycle or safety claim. No vendor file
was opened (the folder's record says there is none)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "lift-vrc", "1.1", "furniture"
TITLE = "vertical reciprocating conveyor, own design, two-mast portal 4600 high, carriage with a 700 x 1600 deck rising 2250 from 750 to 3000, 8 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; the lower "
            "level at conveyor-roller 1.0's TOP (library.load); every other size a design choice; no load, speed, cycle or safety "
            "claim; a flat deck carries the goods; the hoist, guide shoes and guarding placed in a later version; no vendor file opened")
ORIGIN = ("the floor plane z = 0 midway between the two masts: x across the lift, through the masts; y along the goods' flow, in and "
          "out between the masts; the deck's top at z 750 at the lower stop, 3000 at the upper")
COMMAND = "LIFTVRC"
PARAMS = dict()
FILLET_R = 0.5                                   # the gate's radius, set per primitive below (P.radii): the furniture class's 1.0 reads 10 mm free-corner edges short
CR = library.load("conveyor-roller")             # conveyor-roller 1.0: the family's hand-off height (one home for the figure)
LOW = CR.TOP                                     # 750: the deck's top at the lower stop, level with a roller conveyor's rollers' tops
TRAVEL = 2250.0                                  # lower to upper level: 750 to 3000, a mezzanine floor's height: design choice
DECK_X, DECK_Y, DECK_T = 700.0, 1600.0, 10.0     # the deck 700 across (x +-350), 1600 along (y +-800; a load off a conveyor-roller section, L 1500, with 50 each end), 10 thick: design choice; the goods ride on it, flat
SB_W, SB_H = 60.0, 100.0                         # two side beams under the deck's long edges, 60 wide, 100 deep, full length: design choice
UP_X, UP_Y = 80.0, 120.0                         # an upright each side, 80 (x) by 120 (y), x 350..430, from the foot plate's top to UP_TOP: design choice
UP_TOP = 1300.0                                  # the uprights' tops at the lower stop (3550 at the upper): design choice
MAST, MAST_GAP = 100.0, 5.0                      # masts 100 x 100, their inner faces 5 clear of the uprights (the guide shoes, not drawn, run in it): design choice
MAST_X = DECK_X / 2 + UP_X + MAST_GAP + MAST / 2 # 485: the masts' centres x +-485
FOOT, FOOT_T = 300.0, 20.0                       # foot plates 300 x 300 x 20 under each mast: design choice
MAST_TOP = 4500.0                                # the masts' tops: 1500 over the upper deck for the load, design choice
BEAM_H = 100.0                                   # the top beam 100 deep, x across both masts' tops, 100 along y: design choice
HOLE = 110.0                                     # 4 x M12 anchor holes per foot plate at 220 x 220 about the mast's centre (40 from the plate's edges): design choice
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S = "M-STEEL-7035"; Y = "M-YELLOW"
    for sx, k in ((-1, "l"), (1, "r")):
        cx = sx * MAST_X
        fp = P.box(S, cx - FOOT / 2, -FOOT / 2, 0, FOOT, FOOT, FOOT_T)                                 # foot plate on the floor
        for hx in (-1, 1):
            for hy in (-1, 1):
                P.hole(S, (cx + hx * HOLE, hy * HOLE, -1), (cx + hx * HOLE, hy * HOLE, FOOT_T + 1), M12_D / 2, fp)   # M12 anchor hole
        P.box(S, cx - MAST / 2, -MAST / 2, FOOT_T, MAST, MAST, MAST_TOP - FOOT_T)                      # mast, foot plate to the top
        P.collider(f"mast-{k}", cx - MAST / 2, -MAST / 2, 0, MAST, MAST, MAST_TOP)
    P.box(S, -MAST_X - MAST / 2, -MAST / 2, MAST_TOP, 2 * MAST_X + MAST, MAST, BEAM_H)                 # top beam on the masts' tops
    P.collider("beam", -MAST_X - MAST / 2, -MAST / 2, MAST_TOP, 2 * MAST_X + MAST, MAST, BEAM_H)
    N = "node:carriage|" + Y
    dz = LOW - DECK_T                                                                                    # 740: the deck's underside
    P.box(N, -DECK_X / 2, -DECK_Y / 2, dz, DECK_X, DECK_Y, DECK_T)                                      # the deck
    for sx in (-1, 1):
        x0 = DECK_X / 2 - SB_W if sx > 0 else -DECK_X / 2
        P.box(N, x0, -DECK_Y / 2, dz - SB_H, SB_W, DECK_Y, SB_H)                                       # side beam under the deck's edge
        u0 = DECK_X / 2 if sx > 0 else -DECK_X / 2 - UP_X
        P.box(N, u0, -UP_Y / 2, FOOT_T, UP_X, UP_Y, UP_TOP - FOOT_T)                                   # upright: stands on the foot plate at the lower stop
    P.pivot("carriage", "translate", (0, 0, LOW), axis=(0, 0, 1), range=(0, TRAVEL))
    P.collider("platform", -DECK_X / 2 - UP_X, -DECK_Y / 2, FOOT_T, DECK_X + 2 * UP_X, DECK_Y, UP_TOP - FOOT_T)
    for i in range(len(P)): P.radii[i] = FILLET_R                       # the gate reads each primitive's radius (fillet._radii), not FILLET_R (mech-r106)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=20), dict(name="front", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
