#!/usr/bin/env python3
"""runway-beam: crane runway beam and rail, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). The
runway of crane-bridge in lib/machines-factory.txt (line 74: girder-bridge, runway-beam, end-truck x2, hoist-wire-rope,
trolley, ...): a welded plate girder (I-section: top flange, web, bottom flange) 12000 long and 700 high, on a bearing plate
under each end (where a column's bracket carries it), with a square-bar crane rail along its top (node `rail`, fixed: an end
truck a BOM puts on the runway is placed on the rail's top plane and moves along it on its own nodes) and an end stop beyond
each end of the rail. A crane takes two runway beams, one each side of its bay. Every size is a design choice. No load
rating (no wheel load), no deflection or duty class claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "runway-beam", "1.0", "furniture"
TITLE = "crane runway plate girder 12000 x 400 x 700 (I-section) on two bearing plates 400 x 500 x 30, crane rail 50 x 50 with two end stops"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every "
            "size a design choice; no load rating, no wheel load, deflection or duty class claim")
ORIGIN = ("the bearing plates' underside z = 0 at the beam's centre x = 0, y = 0; the beam's length (the crane's travel) "
          "along x; the crane rail's top plane (the end trucks' seat) at z = 780")
COMMAND = "RUNWAYBEAM"
PARAMS = dict()
BEAM_L, BEAM_H = 12000.0, 700.0                  # runway 12000 long (x), 700 high over the flanges: design choice
FLG_W, FLG_T = 400.0, 30.0                       # top and bottom flanges 400 wide (y), 30 thick: design choice
WEB_T = 20.0                                     # web 20 thick, between the flanges: design choice
PLATE_L, PLATE_W, PLATE_T = 400.0, 500.0, 30.0   # bearing plates 400 along the beam, 500 across, 30 thick, flush with its ends: design choice
RAIL_W, RAIL_H = 50.0, 50.0                      # square-bar crane rail 50 x 50 on the centre line (girder-bridge's trolley rail size): design choice
STOP_L, STOP_W, STOP_H = 100.0, 300.0, 150.0     # end stops 100 along the beam, 300 across, 150 high, flush with its ends: design choice
RAIL_GAP = 10.0                                  # the rail ends 10 short of each stop: design choice

def build():
    P = Prims(); Y = "M-YELLOW"; W = "M-SILVER"                      # beam painted yellow (a design choice, no marking claim); rail bare steel
    hl = BEAM_L / 2; zb = PLATE_T; zt = PLATE_T + BEAM_H              # the beam's underside z 30, its top face z 730
    rl = hl - STOP_L - RAIL_GAP                                       # the rail runs x -5890 to 5890
    for sx in (-1, 1):                                                # bearing plates, flush with the beam's ends
        P.box(Y, hl - PLATE_L if sx > 0 else -hl, -PLATE_W / 2, 0, PLATE_L, PLATE_W, PLATE_T)
    P.box(Y, -hl, -FLG_W / 2, zb, BEAM_L, FLG_W, FLG_T)                # bottom flange
    P.box(Y, -hl, -WEB_T / 2, zb + FLG_T, BEAM_L, WEB_T, BEAM_H - 2 * FLG_T)   # web
    P.box(Y, -hl, -FLG_W / 2, zt - FLG_T, BEAM_L, FLG_W, FLG_T)       # top flange
    for sx in (-1, 1):                                                # end stops on the top flange, flush with the beam's ends
        P.box(Y, hl - STOP_L if sx > 0 else -hl, -STOP_W / 2, zt, STOP_L, STOP_W, STOP_H)
    P.box(f"node:rail|{W}", -rl, -RAIL_W / 2, zt, 2 * rl, RAIL_W, RAIL_H)    # the crane rail
    P.pivot("rail", "fixed", (0, 0, zt + RAIL_H), axis=(0, 0, 1))
    for sx in (-1, 1):
        P.collider(f"plate-{'b' if sx > 0 else 'a'}", hl - PLATE_L if sx > 0 else -hl, -PLATE_W / 2, 0, PLATE_L, PLATE_W, PLATE_T)
    P.collider("beam", -hl, -FLG_W / 2, zb, BEAM_L, FLG_W, BEAM_H)
    for sx in (-1, 1):
        P.collider(f"stop-{'b' if sx > 0 else 'a'}", hl - STOP_L if sx > 0 else -hl, -STOP_W / 2, zt, STOP_L, STOP_W, STOP_H)
    P.collider("rail-bar", -rl, -RAIL_W / 2, zt, 2 * rl, RAIL_W, RAIL_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
