#!/usr/bin/env python3
"""girder-bridge: bridge crane girder, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). The
girder of crane-bridge in lib/machines-factory.txt (line 74: girder-bridge, runway-beam, end-truck x2, hoist-wire-rope,
trolley, ...): a welded box girder 8000 long, 400 wide and 700 high, on a seat plate at each end (where the two end trucks
carry it along the runway), with a square-bar trolley rail along its top (node `rail`, fixed: the trolley a BOM puts on the
girder is placed on the rail's top plane and moves along the girder on its own nodes) and an end stop beyond each end of the
rail. The body is drawn by its outside: a welded box girder is closed at its ends and its diaphragms are not seen. Every size
is a design choice. No load rating (no safe working load), no deflection, camber or duty class claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "girder-bridge", "1.0", "furniture"
TITLE = "bridge crane box girder 8000 x 400 x 700 on two end seats 400 x 700 x 30, trolley rail 50 x 50 with two end stops"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every "
            "size a design choice; no load rating, no deflection, camber or duty class claim")
ORIGIN = ("the seats' underside z = 0 at the girder's centre x = 0, y = 0; the girder's length (the crane's span) along x; "
          "the trolley rail's top plane (the trolley's seat) at z = 780")
COMMAND = "GIRDERBRIDGE"
PARAMS = dict()
GIR_L, GIR_W, GIR_H = 8000.0, 400.0, 700.0      # box girder 8000 long, 400 wide (y), 700 high: design choice
SEAT_L, SEAT_W, SEAT_T = 400.0, 700.0, 30.0     # end seats 400 along the girder, 700 across it, 30 thick, flush with its ends: design choice
RAIL_W, RAIL_H = 50.0, 50.0                     # square-bar trolley rail 50 x 50 on the girder's centre line: design choice
STOP_L, STOP_W, STOP_H = 100.0, 300.0, 150.0    # end stops 100 along the girder, 300 across, 150 high, flush with its ends: design choice
RAIL_GAP = 10.0                                 # the rail ends 10 short of each stop: design choice

def build():
    P = Prims(); Y = "M-YELLOW"; W = "M-SILVER"                     # girder painted yellow (a design choice, no marking claim); rail bare steel
    hl = GIR_L / 2; zt = SEAT_T + GIR_H                              # the girder's top face, z 730
    rl = hl - STOP_L - RAIL_GAP                                      # the rail runs x -3890 to 3890
    for sx in (-1, 1):                                               # end seats, flush with the girder's ends
        P.box(Y, hl - SEAT_L if sx > 0 else -hl, -SEAT_W / 2, 0, SEAT_L, SEAT_W, SEAT_T)
    P.box(Y, -hl, -GIR_W / 2, SEAT_T, GIR_L, GIR_W, GIR_H)           # box girder
    for sx in (-1, 1):                                               # end stops on the top face, flush with the girder's ends
        P.box(Y, hl - STOP_L if sx > 0 else -hl, -STOP_W / 2, zt, STOP_L, STOP_W, STOP_H)
    P.box(f"node:rail|{W}", -rl, -RAIL_W / 2, zt, 2 * rl, RAIL_W, RAIL_H)   # the trolley rail
    P.pivot("rail", "fixed", (0, 0, zt + RAIL_H), axis=(0, 0, 1))
    for sx in (-1, 1):
        x0 = hl - SEAT_L if sx > 0 else -hl
        P.collider(f"seat-{'b' if sx > 0 else 'a'}", x0, -SEAT_W / 2, 0, SEAT_L, SEAT_W, SEAT_T)
    P.collider("girder", -hl, -GIR_W / 2, SEAT_T, GIR_L, GIR_W, GIR_H)
    for sx in (-1, 1):
        P.collider(f"stop-{'b' if sx > 0 else 'a'}", hl - STOP_L if sx > 0 else -hl, -STOP_W / 2, zt, STOP_L, STOP_W, STOP_H)
    P.collider("rail-bar", -rl, -RAIL_W / 2, zt, 2 * rl, RAIL_W, RAIL_H)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="front", az=270, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
