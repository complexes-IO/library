#!/usr/bin/env python3
"""lift-stacker: a pallet stacker / destacker (a pallet magazine on a conveyor line), our own design (OPERATING.md 12, own designs;
inventory row lift-stacker, own_design "yes": "pallet stacker / destacker (our own build)", the conveyor family, EM 2026-11-08).
A four-post frame holds a stack of empty pallets on two fork bars; a lift table under the stack takes pallets in and out along x
at the conveyor family's hand-off height (conveyor-roller's TOP, 750, read with library.load).
The table (node `table`) has three stops: 750 (the hand-off), 950 (STOP_MID) and 1094 (the top, LIFT 344); review
lift-stacker-1.0 finding 1, option (a): a 200 travel never reached the stack's underside on the tines (1084).
Destacking: the empty table rises to 1094 under the stack and lifts it 10 off the tines; the forks (nodes `fork-1`, `fork-2`)
draw back 300; the table lowers to 950 (one pallet, 144), the forks go in under the second pallet's stringer boards, through the
pallet's openings between its block columns; the table lowers to 750 with the bottom pallet (the second lands on the tines with
the deck at 940), which leaves along x. Stacking: the table lifts the incoming pallet to 950, so the stack stands 10 off the
tines; the forks draw back; the table rises to 1094 (the incoming pallet's stringer boards 10 over the tines), the forks go in;
the table lowers to 750. The pallet is pallet 1.2, read with library.load: its footprint (1219 x 1016, Assumption (B) there,
ISO 6780 not on file), its height and its block columns, so the tines sit in its openings and the two cannot drift apart.
Not drawn, placed in a later version once their elements are on file (OPERATING.md 12: a host doesn't model holes for a part it
places later): the lift table's drive and the forks' cylinders (folder plan: cylinder-driven fork pairs), the photoeye-m18 that
senses the stack, the infeed / outfeed conveyor sections, the guarding and the controls. Every size is a design choice; the anchor
holes ISO 273. No load, speed, cycle or safety claim. No vendor file was opened (the folder's record says there is none)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "lift-stacker", "2.0", "furniture"
TITLE = "pallet stacker / destacker, own design, four-post frame 1700 x 2300 x 2700, lift table 344 with three stops, two fork bars with tines 300 into the pallet's openings, 20 x M12 anchor holes"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; anchor holes ISO 273 medium for M12; the hand-off "
            "height at conveyor-roller 1.1's TOP and the pallet's footprint, height and openings from pallet 1.2 (library.load; its "
            "footprint an Assumption (B) there, inherited); every other size a design choice; no load, speed, cycle or safety claim; "
            "the drives, cylinders, photoeye, conveyors and guarding placed in a later version; no vendor file opened")
ORIGIN = ("the floor plane z = 0 under the centre of the pallet stack: x along the pallets' flow, in and out of the stacker; y "
          "across it, through the fork bars; the table's top at z 750 at the lower stop")
COMMAND = "LIFTSTACKER"
PARAMS = dict()
FILLET_R = 0.5                                   # the gate's radius, set per primitive below (P.radii): the furniture class's 1.0 reads 10 mm free-corner edges short
CR = library.load("conveyor-roller")             # conveyor-roller 1.1: the family's hand-off height (one home for the figure)
PAL = library.load("pallet")                     # pallet 1.2: footprint, height, block columns (one home for the figures)
LOW = CR.TOP                                     # 750: the table's top at the lower stop, level with a roller conveyor's rollers' tops
PX, PY = PAL.LX, PAL.LY                          # 1219 along x, 1016 along y: the pallet's footprint, Assumption (B) there (ISO 6780 not on file)
PH = PAL.BOT + PAL.BLK + PAL.STR + PAL.DECK      # 144: the pallet's height
OPEN_Z = PAL.BOT + PAL.BLK                       # 104: the openings along y run from the pallet's underside to its stringer boards' underside
GAP0, GAP1 = PAL.B - PX / 2, (PX - PAL.B) / 2 - PX / 2   # -464.5, -72.5: one opening between the block columns, x about the stack's centre (the other mirrored)
STOP_MID = 200.0                                 # the middle stop, deck 950: the forks run in under the second pallet (destacking) / the stack lifts off (stacking): design choice
LIFT_OFF = 10.0                                  # the stack stands 10 above the tines when the table carries it: design choice
TINE_TOP = LOW + STOP_MID + PH + OPEN_Z - LIFT_OFF   # 1188: 10 under the second pallet's stringer boards with the table at the middle stop
LIFT = TINE_TOP - OPEN_Z + LIFT_OFF - LOW        # 344: the top stop, deck 1094, 10 over the stack's underside on the tines (1084): the empty table lifts the stack off
assert LIFT == 344.0 and LIFT - STOP_MID == PH   # the top and middle stops one pallet apart, so the cycle closes (review lift-stacker-1.0 finding 1)
TINE_W, TINE_T, TINE_L = 100.0, 40.0, 300.0      # tines 100 wide, 40 thick, 300 long, one in each opening (centred in it): design choice
assert LOW + LIFT < TINE_TOP - TINE_T            # the deck at the top stop (1094) stays under the tines' underside (1148)
REACH = 300.0                                    # the forks' stroke along y: the tines' tips 20 outside the pallet when out, 280 in when in: design choice
EDGE_GAP = 20.0                                  # the tines' tips 20 clear of the pallet's side when the forks are out: design choice
BAR_T, BAR_H, BAR_X = 60.0, 80.0, 680.0          # fork bar 60 (y) x 80 (z), x +-680, the tines on its inner face, its underside at the tines' underside: design choice
POST, POST_X, POST_Y = 100.0, 700.0, 1000.0      # 4 posts 100 x 100 on centres x +-700, y +-1000 (the pallets pass between them along x): design choice
FOOT, FOOT_T = 300.0, 20.0                       # foot plates 300 x 300 x 20 under each post: design choice
TOP_Z, TOP_H = 2600.0, 100.0                     # the posts' tops; the top frame 100 x 100 on them: 10 pallets (1440) stand on the tines under it: design choice
RAIL_X0, RAIL_W, RAIL_H = 620.0, 80.0, 60.0      # guide rails, x +-620 to +-700, 60 deep under the fork bar, from the tines' line to the post: design choice
BASE_X, BASE_Y, COL = 1200.0, 800.0, 200.0       # the lift's base plate 1200 x 800 x 20 and its column 200 x 200 under the table: design choice
TIE_W = 50.0                                     # 4 floor ties 50 x 450 x 20 from the base plate's y edges (x +-550..600) to the foot plates: design choice
DECK_X, DECK_Y, DECK_T = 1300.0, 900.0, 10.0     # the table's deck 1300 x 900 x 10: under the pallet's three bottom boards: design choice
TB_W, TB_H = 60.0, 100.0                         # three table beams along x, 60 wide, 100 deep (y +-450..390 and the middle): design choice
HOLE, BHX, BHY = 110.0, 500.0, 300.0             # 4 x M12 per foot plate at 220 x 220 about the post; 4 in the base plate at 1000 x 600: design choice
M12_D = 13.5                                     # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)

def build():
    P = Prims(); S = "M-STEEL-7035"; Y = "M-YELLOW"
    yin = PY / 2 + EDGE_GAP                       # 528: the tines' tips (out), the rails' inner ends
    for i, (sx, sy) in enumerate(((-1, -1), (1, -1), (1, 1), (-1, 1)), 1):
        cx, cy = sx * POST_X, sy * POST_Y
        fp = P.box(S, cx - FOOT / 2, cy - FOOT / 2, 0, FOOT, FOOT, FOOT_T)                             # foot plate on the floor
        for hx in (-1, 1):
            for hy in (-1, 1):
                P.hole(S, (cx + hx * HOLE, cy + hy * HOLE, -1), (cx + hx * HOLE, cy + hy * HOLE, FOOT_T + 1), M12_D / 2, fp)   # M12 anchor hole
        P.box(S, cx - POST / 2, cy - POST / 2, FOOT_T, POST, POST, TOP_Z - FOOT_T)                     # post, foot plate to the top frame
        P.collider(f"post-{i}", cx - POST / 2, cy - POST / 2, 0, POST, POST, TOP_Z)
    for sy in (-1, 1):                                                                                  # top frame: two beams along x over the posts...
        P.box(S, -POST_X - POST / 2, sy * POST_Y - POST / 2, TOP_Z, 2 * POST_X + POST, POST, TOP_H)
    for sx in (-1, 1):                                                                                  # ...and two along y between them
        P.box(S, sx * POST_X - POST / 2, -POST_Y + POST / 2, TOP_Z, POST, 2 * POST_Y - POST, TOP_H)
    P.collider("top", -POST_X - POST / 2, -POST_Y - POST / 2, TOP_Z, 2 * POST_X + POST, 2 * POST_Y + POST, TOP_H)
    zb = TINE_TOP - TINE_T                        # 1148: the tines' and the fork bars' underside, the rails' top
    for sy in (-1, 1):                            # guide rails: from the tines' line to the post's inner face, under each bar end
        y0 = yin if sy > 0 else -(POST_Y - POST / 2)
        for sx in (-1, 1):
            x0 = RAIL_X0 if sx > 0 else -RAIL_X0 - RAIL_W
            P.box(S, x0, y0, zb - RAIL_H, RAIL_W, POST_Y - POST / 2 - yin, RAIL_H)
        P.collider(f"rails-{1 if sy < 0 else 2}", -RAIL_X0 - RAIL_W, y0, zb - RAIL_H, 2 * (RAIL_X0 + RAIL_W), POST_Y - POST / 2 - yin, RAIL_H)
    bp = P.box(S, -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, FOOT_T)                                  # the lift's base plate
    for hx in (-1, 1):
        for hy in (-1, 1):
            P.hole(S, (hx * BHX, hy * BHY, -1), (hx * BHX, hy * BHY, FOOT_T + 1), M12_D / 2, bp)        # M12 anchor hole
    for sx in (-1, 1):                            # floor ties: the base plate's corners to the foot plates, so the lift and the frame are one body (GEO-070)
        for sy in (-1, 1):
            x0 = BASE_X / 2 - TIE_W if sx > 0 else -BASE_X / 2
            P.box(S, x0, BASE_Y / 2 if sy > 0 else -(POST_Y - FOOT / 2), 0, TIE_W, POST_Y - FOOT / 2 - BASE_Y / 2, FOOT_T)
    dz = LOW - DECK_T - TB_H                                                                            # 640: the table beams' underside at rest
    P.box(S, -COL / 2, -COL / 2, FOOT_T, COL, COL, dz - FOOT_T)                                         # the lift's column: the table rests on it at the lower stop
    P.collider("lift-base", -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, dz)
    N = "node:table|" + Y
    P.box(N, -DECK_X / 2, -DECK_Y / 2, LOW - DECK_T, DECK_X, DECK_Y, DECK_T)                            # the deck
    for y0 in (-DECK_Y / 2, -TB_W / 2, DECK_Y / 2 - TB_W):
        P.box(N, -DECK_X / 2, y0, dz, DECK_X, TB_W, TB_H)                                              # table beam along x
    P.pivot("table", "translate", (0, 0, LOW), axis=(0, 0, 1), range=(0, LIFT))
    P.collider("lift-deck", -DECK_X / 2, -DECK_Y / 2, dz, DECK_X, DECK_Y, TB_H + DECK_T)
    for k, sy in (("fork-1", -1), ("fork-2", 1)):
        F = f"node:{k}|" + Y
        yb = yin + TINE_L                         # 828: the bar's inner face (out)
        P.box(F, -BAR_X, yb if sy > 0 else -yb - BAR_T, zb, 2 * BAR_X, BAR_T, BAR_H)                  # fork bar on the rails' ends
        for gx in (-1, 1):
            xc = gx * (GAP0 + GAP1) / 2           # +-268.5: the middle of each opening
            P.box(F, xc - TINE_W / 2, yin if sy > 0 else -yb, zb, TINE_W, TINE_L, TINE_T)              # tine, pointing in
        P.pivot(k, "translate", (0, sy * yb, TINE_TOP), axis=(0, -sy, 0), range=(0, REACH))
    for i in range(len(P)): P.radii[i] = FILLET_R                       # the gate reads each primitive's radius (fillet._radii), not FILLET_R (mech-r106)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=20), dict(name="front", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
