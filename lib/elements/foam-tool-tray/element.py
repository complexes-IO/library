#!/usr/bin/env python3
"""foam-tool-tray: a shadow-foam tool insert for one drawer of cabinet-tool, our own design (OPERATING.md 12, own designs; inventory
row own_design "yes": "shadow-foam tool tray for a drawer"; lib/machines-factory.txt line 80, cabinet-tool, places cabinet-tool,
tb-rollcab, hardware-cabinet and foam-tool-tray). One foam block that lies on the drawer tray's bottom and fills it, with two
finger notches at the front edge to lift it out. Its plan is read from cabinet-tool itself (library.load), so the two cannot drift
apart. The block is blank: which tools a drawer holds is not on file, so no tool's outline is cut (a host doesn't model a
cut-out for a part it doesn't place, OPERATING.md 12); each pocket is cut in a later version, or by the user, once they are. One fixed
body, no node, no hole. Every size other than the tray's is a design choice. No load, material or safety claim. No vendor file
was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "foam-tool-tray", "1.0", "furniture"
TITLE = "shadow-foam insert 865 x 555 x 50 for a cabinet-tool 1.1 drawer, blank, two finger notches"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; the plan "
            "sized to cabinet-tool's drawer tray (library.load); every other size a design choice; no tool pocket (the tools "
            "a drawer holds are not on file); no vendor file opened")
ORIGIN = ("the block's underside z = 0 at its front-left corner x = 0, y = 0, the front face toward -y; placed in a cabinet-tool "
          "drawer node at (17.5, 0, the tray bottom's top face)")
COMMAND = "FOAMTRAY"
PARAMS = dict()
CT = library.load("cabinet-tool")                 # cabinet-tool 1.1: the drawer it lies in (one home for the figure)
IN_X = CT.W - 2 * (CT.T + CT.SIDE_CLR + CT.TRAY_T)  # the tray's inside width 869 (x 15.5 to 884.5 in the drawer)
IN_Y = CT.TRAY_D - CT.TRAY_T                      # the tray's inside depth 558.5 (y 0, the front's back face, to 558.5)
CLR_X, CLR_Y = 2.0, 3.5                           # 2 clear each side, 3.5 at the back (lift-out fit): design choice
L, D = IN_X - 2 * CLR_X, IN_Y - CLR_Y             # the block 865 x 555
H = 50.0                                          # 50 thick, under the lowest tray's 118.5 inside height: design choice
NOTCH_W, NOTCH_D, NOTCH_H = 100.0, 40.0, 30.0     # finger notches 100 wide, 40 into the block, 30 deep from the top: design choice
NOTCH_X = (L / 4, 3 * L / 4)                      # their centres at the quarter points of the front edge: design choice

def build():
    P = Prims(); F = "M-BLACK-PA"
    block = P.box(F, 0, 0, 0, L, D, H)                                                      # the foam block
    for cx in NOTCH_X:                                                                      # finger notches, cut from the top
        P.cutbox(F, cx - NOTCH_W / 2, -1.0, H - NOTCH_H, NOTCH_W, NOTCH_D + 1.0, NOTCH_H + 1.0, block)
    P.collider("foam", 0, 0, 0, L, D, H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
