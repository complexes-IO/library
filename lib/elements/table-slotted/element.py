#!/usr/bin/env python3
"""table-slotted: a T-slot machine table, our own design (OPERATING.md 12, own designs; lib/inventory.csv row "table-slotted",
own_design "yes": "T-slot machine table", the machines-factory rows drill-pillar, drill-radial, grinder-surface, mill-vertical-cnc,
mill-horizontal, borer-horizontal, notcher-corner and punch-hydraulic). A rectangular plate with three T-slots along its length, on
two way shoes that ride saddle 1.1's cross ways (the one seat on file: their spacing and width are read from saddle itself,
library.load, so the two cannot drift apart). The table travels along the saddle's cross ways (y); that travel is the machine's,
between the elements, so the table has no moving node (as saddle). A vise or fixture is placed on the top face (z = TOP) by its
BOM row's position; the slot pitch is vise-machine 1.0's lug spacing across, so its four M12 lugs fall in two neighbouring
slots. The T-slot profile (the slot width for an M12 T-bolt and its undercut) is a figure ISO 299 tabulates and that standard
is not on file: the slots are drawn at the design figures below until the document is on file (spec.md What it meets, NOT ON
FILE (B); the stand-magnetic 1.1 way). Every other size is a design choice. Gibs, wipers, the feed nut's bracket, the clamps,
end stops and the swarf troughs are not drawn. No load rating, no accuracy claim. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "table-slotted", "1.0", "furniture"
TITLE = "T-slot machine table 500 x 1200 x 100, three T-slots along its length at 130 pitch, two way shoes on saddle's cross ways"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; the shoes on saddle 1.1's cross ways, the slot pitch "
            "vise-machine 1.0's lug spacing, the T-slot profile drawn at design figures until ISO 299 is on file (class B, source "
            "wanted), every other size a design choice; no load rating, no accuracy claim; no vendor file opened")
ORIGIN = ("saddle's cross ways' top plane z = 0 (the table's seat) at the table's centre x = 0, y = 0; the table's length and its "
          "slots run along y, the travel on the saddle; the top face, where a vise or fixture is placed, at z = 100")
COMMAND = "TABLETSLOT"
PARAMS = dict()
SAD = library.load("saddle")                      # saddle 1.1: the cross ways it rides (one home for the figure)
SHOE_X, SHOE_W = SAD.WAY_X, SAD.WAY_W             # shoe centres at x +-200, each as wide as the saddle's cross way, 80
VISE = library.load("vise-machine")               # vise-machine 1.0: its lugs' spacing across sets the slot pitch (one home)
SLOT_PITCH = 2 * VISE.LUG_Y                       # 130: the vise's lug holes at y +-65 fall in two neighbouring slots
TL = 1200.0                                       # table length along the slots and the travel (y -600..600): design choice
TW = 500.0                                        # table width across (x -250..250): design choice
SHOE_H = 30.0                                     # way shoes 30 high (z 0..30): design choice
SHOE_END = 20.0                                   # the shoes stop 20 short of each end of the table: design choice (saddle's WAY_END)
PLATE_T = 70.0                                    # the slotted plate 70 thick (z 30..100): design choice; 42 under the slots
TOP = SHOE_H + PLATE_T                            # 100: the top face, the fixture's seat
N_SLOTS = 3                                       # three slots at x -130, 0, 130: design choice (the outer ones 120 from the edges)
SLOT_A = 14.0                                     # the slot's throat width: NOT ON FILE (B), ISO 299 (the T-slot for an M12 T-bolt); drawn 14, clearing the M12 medium clearance 13.5 of ISO 273 (lib/standards/holes.csv), until the document is on file
SLOT_B = 24.0                                     # the undercut's width: NOT ON FILE (B), ISO 299; drawn 24 until the document is on file
SLOT_C = 10.0                                     # the undercut's height: NOT ON FILE (B), ISO 299; drawn 10 until the document is on file
SLOT_H = 28.0                                     # the slot's depth from the top face to the undercut's floor: NOT ON FILE (B), ISO 299; drawn 28 (the lip over the undercut 18) until the document is on file

def build():
    P = Prims(); W = "M-SILVER"                                       # bare machined steel: the library's bright-metal layer (saddle's ways)
    sl = TL - 2 * SHOE_END
    for sx in (-1, 1):
        P.box(W, sx * SHOE_X - SHOE_W / 2, -sl / 2, 0, SHOE_W, sl, SHOE_H)                      # way shoe, on saddle's cross way
    plate = P.box(W, -TW / 2, -TL / 2, SHOE_H, TW, TL, PLATE_T)                                  # the slotted plate, z 30..100
    for i in range(N_SLOTS):
        xc = (i - (N_SLOTS - 1) / 2) * SLOT_PITCH                                                 # -130, 0, 130
        P.cutbox(W, xc - SLOT_A / 2, -TL / 2 - 1, TOP - SLOT_H, SLOT_A, TL + 2, SLOT_H + 1, plate)   # the throat, open at the top and both ends
        P.cutbox(W, xc - SLOT_B / 2, -TL / 2 - 1, TOP - SLOT_H, SLOT_B, TL + 2, SLOT_C, plate)       # the undercut under it, open at both ends
    P.collider("shoes", -SHOE_X - SHOE_W / 2, -sl / 2, 0, 2 * SHOE_X + SHOE_W, sl, SHOE_H)         # both shoes and the gap between them
    P.collider("table", -TW / 2, -TL / 2, SHOE_H, TW, TL, PLATE_T)                                 # the plate, slots filled
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="end", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
