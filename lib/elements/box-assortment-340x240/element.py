#!/usr/bin/env python3
"""box-assortment-340x240: generic empty assortment box for small parts, our own vendor-neutral design of the ETIM 10.0 class
EC003616 (Assortment box empty), built unattended (OPERATING.md 12, generic elements; group EG010340 Storage and racking systems, a
tier-2 class, after basin-bulk-shelving-440, lib/rounds/mech/r158.md). A grey plastic case 340 wide, 240 deep and 50 high, walls and
bottom 2.0, divided into twelve fixed compartments (four across, three deep) by 1.5 dividers that stop 2 under the rim, and a clear
plastic lid 2.0 that lies on the rim and turns up about the case's rear top edge (node `lid`, 0 to 110 degrees). The hinge knuckles
and the catch are not modelled: the lid's turn is about the rear top edge itself. The box stands on its own on a bench or a shelf and
meets nothing on file, so no figure is read from another element; every size is a design choice. The class's features are not on file
(lib/standards/etim/class-features.csv has no EC003616 rows): spec.md gives the design values under plain names, as
basin-bulk-shelving-440 does. No load, capacity or safety claim. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "box-assortment-340x240", "1.0", "furniture"
TITLE = ("assortment box for small parts, empty, generic, grey plastic case 340 x 240 x 50 with 12 fixed compartments, clear lid "
         "hinged at the rear top edge, 0 to 110 degrees")
TOOLKIT = "1.3"
BASELINE = ("our own design: generic assortment box, empty (ETIM 10.0 EC003616), a plastic case 340 x 240 x 50, walls and bottom 2.0, "
            "twelve fixed compartments (4 x 3) from 1.5 dividers 2 under the rim, a clear lid 2.0 on the rim turning 0 to 110 degrees "
            "about the rear top edge; hinge knuckles and catch not modelled; meets no element on file; class features not on file, "
            "design values under plain names (spec.md); every size a design choice; no load or safety claim; no vendor file opened")
ORIGIN = ("the case's underside z = 0 at its front-left corner x = 0, y = 0; the width along +x, the depth along +y; the lid's hinge "
          "line is the case's rear top edge (y = 240, z = 50) and the lid opens upward toward the back")
COMMAND = "BOXASRT"
PARAMS = dict()

W, D, H = 340.0, 240.0, 50.0                 # design: the case outside, width (x), depth (y), height (z, to the rim)
T = 2.0                                      # design: walls and bottom (2.0: thin to the gate's fillet check)
DT = 1.5                                     # design: dividers
DROP = 2.0                                   # design: the dividers stop 2 under the rim, so the lid closes on the rim alone
NX, NY = 4, 3                                # design: compartments across (x) and deep (y), 12 in all
LT = 2.0                                     # design: the lid's plate, lying on the rim
SWING = 110.0                                # design: the lid turns 0 to 110 degrees up about the rear top edge
CASE, LID = "M-GREY-PA", "M-CASE-CLEAR"      # grey plastic case (not a printed layer), clear lid

IW, ID_ = W - 2 * T, D - 2 * T               # 336 x 236: the case's inside
CW = (IW - (NX - 1) * DT) / NX               # 82.875: one compartment's width
CD = (ID_ - (NY - 1) * DT) / NY              # 77.666...: one compartment's depth
ZD0, ZD1 = T, H - DROP                       # 2 .. 48: the dividers stand on the bottom and stop 2 under the rim
XS = [T + i * (CW + DT) - DT for i in range(1, NX)]       # the long dividers' low x (3, running the inside's whole depth)
YS = [T + j * (CD + DT) - DT for j in range(1, NY)]       # the cross dividers' low y (2 per column)

assert abs(NX * CW + (NX - 1) * DT - IW) < 1e-9 and abs(NY * CD + (NY - 1) * DT - ID_) < 1e-9   # the grid fills the inside
assert T <= 3.0 and DT <= 3.0 and LT <= 3.0                                                    # every sheet edge thin to the gate
assert min(CW, CD, ZD1 - ZD0, H - T) >= 8.0                                                    # every other free edge >= 8 (the gate's trap)
assert ZD1 < H                                                                                 # the dividers clear of the closed lid
TUB = W * D * H - IW * ID_ * (H - T)                                     # 4080000 - 336 x 236 x 48
DIVS = (NX - 1) * DT * ID_ * (ZD1 - ZD0) + NX * (NY - 1) * CW * DT * (ZD1 - ZD0)   # 3 long + 8 cross dividers, 46 high
VOL = TUB + DIVS
assert abs(TUB - 273792.0) < 1e-6 and abs(DIVS - 94599.0) < 1e-6 and abs(VOL - 368391.0) < 1e-6
assert abs(XS[-1] + DT + CW - (W - T)) < 1e-9 and abs(YS[-1] + DT + CD - (D - T)) < 1e-9     # the last compartment ends at the far wall
assert abs(W * D * LT - 163200.0) < 1e-6                                 # the lid


def build():
    P = Prims()
    cs = P.box(CASE, 0, 0, 0, W, D, H)                                                  # the case's envelope
    P.cutbox(CASE, T, T, T, IW, ID_, H, cs)                                             # open at the top: walls and bottom 2.0
    for x in XS:
        P.box(CASE, x, T, ZD0, DT, ID_, ZD1 - ZD0)                                      # long divider, front wall to back wall
    for i in range(NX):
        x0 = T + i * (CW + DT)
        for y in YS:
            P.box(CASE, x0, y, ZD0, CW, DT, ZD1 - ZD0)                                  # cross divider, between two long ones (or a wall)
    P.collider("case", 0, 0, 0, W, D, H)
    Ll = f"node:lid|{LID}"
    P.box(Ll, 0, 0, H, W, D, LT)                                                        # the lid, on the rim
    P.pivot("lid", "rotate", (W / 2, D, H), axis=(1, 0, 0), range=(0.0, -SWING))        # about the case's rear top edge, opening up
    P.collider("lid-plate", 0, 0, H, W, D, LT)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="behind", az=50, el=30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
