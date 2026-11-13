#!/usr/bin/env python3
"""frame-welded: welded steel machine frame, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). Four
80 x 80 square-tube legs on foot plates, a top ring of 80 x 80 tube with one cross member, a lower ring of 60 x 60 tube, and a
15 top plate (node `mount`, fixed: the machine a BOM puts on the frame is placed on its top face). Each foot plate has one M12
floor-anchor hole, ISO 273 medium (lib/standards/holes.csv). The tubes are drawn by their outside: every tube end is welded shut
against a leg or a plate, so no bore shows. The welds are not drawn. Every size is a design choice. No load rating."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "frame-welded", "1.1", "furniture"
TITLE = "welded machine frame 1200 x 800 x 850, square tube 80 and 60, top plate 15, 4 x M12 floor anchors"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; floor anchors M12 in ISO 273 medium holes; "
            "every size a design choice; no load rating")
ORIGIN = ("floor plane z = 0 at the frame's centre x = 0, y = 0; the long side along x; front toward -y; the top plate's top face "
          "(the machine's seat) at z = 850")
COMMAND = "FRMWELD"
PARAMS = dict()
L, W, H = 1200.0, 800.0, 850.0         # outside of the frame (top plate) and the seat height: design choice
LEG = 80.0                             # legs and top ring: square tube 80 x 80, drawn by its outside: design choice
LOW = 60.0                             # lower ring: square tube 60 x 60: design choice
LOW_Z = 200.0                          # the lower ring's underside above the floor: design choice
FOOT, FOOT_T = 180.0, 15.0             # foot plates 180 x 180 x 15, centred on the legs: design choice
TOP_T = 15.0                           # top plate 15: design choice
ANCHOR_D = 13.5                        # M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
ANCHOR_OUT = 55.0                      # the anchor hole 55 out from the leg's centre in x and y (centre 15 from the leg's outer face, edge 8.25): design choice

def build():
    P = Prims(); S = "M-STEEL-7035"
    cx, cy = L / 2 - LEG / 2, W / 2 - LEG / 2                    # leg centres +-560, +-360
    top_z = H - TOP_T                                            # 835: the legs' and the top ring's top
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * cx, sy * cy
            fp = P.box(S, x - FOOT / 2, y - FOOT / 2, 0, FOOT, FOOT, FOOT_T)                      # foot plate
            ax, ay = x + sx * ANCHOR_OUT, y + sy * ANCHOR_OUT                                     # outboard corner
            P.hole(S, (ax, ay, -1), (ax, ay, FOOT_T + 1), ANCHOR_D / 2, fp)                       # floor anchor M12
            P.box(S, x - LEG / 2, y - LEG / 2, FOOT_T, LEG, LEG, top_z - FOOT_T)                  # leg
    ix, iy = cx - LEG / 2, cy - LEG / 2                          # the legs' inner faces: x +-520, y +-320
    for sy in (-1, 1):                                           # top ring, long rails along x
        P.box(S, -ix, sy * cy - LEG / 2, top_z - LEG, 2 * ix, LEG, LEG)
    for sx in (-1, 1):                                           # top ring, short rails along y
        P.box(S, sx * cx - LEG / 2, -iy, top_z - LEG, LEG, 2 * iy, LEG)
    P.box(S, -LEG / 2, -iy, top_z - LEG, LEG, 2 * iy, LEG)       # cross member under the top plate's centre
    for sy in (-1, 1):                                           # lower ring, long rails along x (on the legs' centre lines)
        P.box(S, -ix, sy * cy - LOW / 2, LOW_Z, 2 * ix, LOW, LOW)
    for sx in (-1, 1):                                           # lower ring, short rails along y
        P.box(S, sx * cx - LOW / 2, -iy, LOW_Z, LOW, 2 * iy, LOW)
    P.box(f"node:mount|{S}", -L / 2, -W / 2, top_z, L, W, TOP_T)  # top plate: the machine sits on its top face
    P.pivot("mount", "fixed", (0, 0, H), axis=(0, 0, 1))
    for sx in (-1, 1):
        for sy in (-1, 1):
            n = ("r" if sx > 0 else "l") + ("b" if sy > 0 else "f")
            P.collider(f"leg-{n}", sx * cx - LEG / 2, sy * cy - LEG / 2, 0, LEG, LEG, top_z - LEG)
    for sy in (-1, 1):
        P.collider(f"low-x{'b' if sy > 0 else 'f'}", -ix, sy * cy - LOW / 2, LOW_Z, 2 * ix, LOW, LOW)
    for sx in (-1, 1):
        P.collider(f"low-y{'r' if sx > 0 else 'l'}", sx * cx - LOW / 2, -iy, LOW_Z, LOW, 2 * iy, LOW)
    P.collider("mount", -L / 2, -W / 2, top_z - LEG, L, W, LEG + TOP_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="low, the lower ring", az=210, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
