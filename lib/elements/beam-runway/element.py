#!/usr/bin/env python3
"""beam-runway: monorail beam for a chain hoist, our own design (OPERATING.md 12, own designs; inventory row own_design "yes"). The
track of hoist-chain-electric in lib/machines-factory.txt (line 75: hoist-chain, trolley, pendant-crane, beam-runway, limit-switch
x2, motor-brake, contactor-reversing): a welded I-section (top flange, web, bottom flange) 6000 long and 400 high, hung from the
building by two hanger plates on its top flange, with an underhung trolley's running surface on the bottom flange (node `track`,
fixed: a trolley a BOM hangs on the beam is placed on the flange's top plane and runs along x on its own nodes) and a pair of end
stops on that flange at each end, one each side of the web. Every size is a design choice. No load rating (no hoist capacity or
wheel load), no deflection or duty class claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "beam-runway", "1.1", "furniture"
TITLE = "monorail I-beam 6000 x 200 x 400 (welded: flanges 200 x 20, web 20) on two hanger plates 300 x 300 x 20, running flange as node track, four end stops"
TOOLKIT = "1.3"
BASELINE = ("our own design (OPERATING.md 12, own designs): no product matched; no hole, thread or standard interface; every "
            "size a design choice; no load rating, no hoist capacity, wheel load, deflection or duty class claim")
ORIGIN = ("the bottom flange's underside z = 0 at the beam's centre x = 0, y = 0; the beam's length (the trolley's travel) along x; "
          "the running flange's top plane (the trolley wheels' seat) at z = 20; the hanger plates' top plane (the fixing to the "
          "building) at z = 420")
COMMAND = "BEAMRUNWAY"
PARAMS = dict()
BEAM_L, BEAM_H = 6000.0, 400.0                   # monorail 6000 long (x), 400 high over the flanges: design choice
FLG_W, FLG_T = 200.0, 20.0                       # top and bottom flanges 200 wide (y), 20 thick: design choice
WEB_T = 20.0                                     # web 20 thick, between the flanges: design choice
HANG_L, HANG_W, HANG_T = 300.0, 300.0, 20.0      # hanger plates 300 along the beam, 300 across, 20 thick, on the top flange: design choice
HANG_X = 2000.0                                  # hanger plates centred at x -2000 and 2000 (4000 apart, 1000 overhang each end): design choice
STOP_L, STOP_W, STOP_H = 60.0, 70.0, 80.0        # end stops 60 along the beam, 70 across (y 10 to 80), 80 high on the running flange: design choice

def build():
    P = Prims(); Y = "M-YELLOW"                                          # beam painted yellow (a design choice, no marking claim)
    hl = BEAM_L / 2; zt = BEAM_H                                         # the running flange z 0 to 20; the top flange's top face z 400
    P.box(Y, -hl, -WEB_T / 2, FLG_T, BEAM_L, WEB_T, BEAM_H - 2 * FLG_T)     # web
    P.box(Y, -hl, -FLG_W / 2, zt - FLG_T, BEAM_L, FLG_W, FLG_T)          # top flange
    for sx in (-1, 1):                                                   # hanger plates on the top flange
        P.box(Y, sx * HANG_X - HANG_L / 2, -HANG_W / 2, zt, HANG_L, HANG_W, HANG_T)
    for sx in (-1, 1):                                                   # end stops on the running flange, against the web, flush with the beam's ends
        for sy in (-1, 1):
            P.box(Y, hl - STOP_L if sx > 0 else -hl, WEB_T / 2 if sy > 0 else -WEB_T / 2 - STOP_W, FLG_T, STOP_L, STOP_W, STOP_H)
    P.box(f"node:track|{Y}", -hl, -FLG_W / 2, 0, BEAM_L, FLG_W, FLG_T)   # the running (bottom) flange
    P.pivot("track", "fixed", (0, 0, FLG_T), axis=(0, 0, 1))
    # colliders follow the solids, so the trolley's seat (y 10 to 100 and -100 to -10, z 20 to 380, between the stops) is clear of them (1.1)
    P.collider("web", -hl, -WEB_T / 2, FLG_T, BEAM_L, WEB_T, BEAM_H - 2 * FLG_T)
    P.collider("top-flange", -hl, -FLG_W / 2, zt - FLG_T, BEAM_L, FLG_W, FLG_T)
    for sx in (-1, 1):                                                   # one per end: the two stops and the web between them
        P.collider(f"stop-{'b' if sx > 0 else 'a'}", hl - STOP_L if sx > 0 else -hl, -WEB_T / 2 - STOP_W, FLG_T, STOP_L, WEB_T + 2 * STOP_W, STOP_H)
    for sx in (-1, 1):
        P.collider(f"hanger-{'b' if sx > 0 else 'a'}", sx * HANG_X - HANG_L / 2, -HANG_W / 2, zt, HANG_L, HANG_W, HANG_T)
    P.collider("flange", -hl, -FLG_W / 2, 0, BEAM_L, FLG_W, FLG_T)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="end", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
