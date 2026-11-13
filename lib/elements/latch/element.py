#!/usr/bin/env python3
"""latch: quarter-turn fastener, our own vendor-neutral design of the ETIM 10.0 class EC011966 (Stud (quarter turn fastener)), built
unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "latch / quarter-turn lock", own_design yes, etim EC011966). The
set that holds a removable panel (a guard, a cover, an access door) on a frame and lets it off with a quarter turn: a steel stud
with a knurled, slotted knob and a cross pin (node `stud`, turning 0 to 90 degrees about its axis), the grommet that keeps the stud
in the removable panel, and the pressed-steel receptacle riveted under the frame's flange whose cam plate the pin locks behind. At
rest (0, closed) the pin lies across the receptacle's slots under the cam plate; at 90 (open) it lies in line with them and the
panel lifts off with its stud. The class values (spec.md, "Class values") are design inputs. Built for a 2.0 panel on a 2.0 flange
(design choice: the stud's length follows the stack). The receptacle's cam ramps and spring take-up, the grommet's retaining
spring and the rivets are not drawn. Every size below is a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "latch", "1.0", "device"
TITLE = "quarter-turn fastener, generic, stud 21 long with knurled slotted knob Ø20, grommet and receptacle, for a 2.0 panel on a 2.0 flange"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic quarter-turn fastener stud (ETIM 10.0 EC011966), with its grommet and receptacle; class values are "
            "design inputs (spec.md); receptacle rivet holes ISO 273 medium for M3; every size a design choice; no load or locking "
            "claim; no vendor file opened")
ORIGIN = ("the removable panel's outer face plane (z = 0) on the stud's axis; +z toward the operator (the knob), -z into the panel, "
          "the frame's flange and the receptacle under it")
COMMAND = "LATCHQT"
PARAMS = dict()
PANEL_T, FLANGE_T = 2.0, 2.0             # the stack this build sits at: removable panel z 0..-2, frame flange z -2..-4 (both the hosts')
GROM_FL_R, GROM_FL_T = 7.0, 1.0           # grommet flange Ø14 x 1 on the panel's outer face: the knob seats on it
GROM_TUBE_R = 4.5                         # grommet tube Ø9 through the panel's hole (the panel's hole Ø9.2 is the host's)
BORE_R = 3.5                              # Ø7 through the grommet and the receptacle's plates: 0.5 clear round the Ø6 shank (features.csv, own)
SEAT = GROM_FL_T                          # z 1: the knob's underside, seated on the grommet's flange
KNOB_R, KNOB_H = 9.0, 8.0                 # knob core Ø18 x 8 (z 1..9)
RIDGES = 24                               # straight knurl, 24 ridges at 15 degrees, offset 7.5 so none lies on an axis: design choice (appearance)
RIDGE_IN, RIDGE_OUT, RIDGE_W = 8.4, 10.0, 1.2   # each ridge from r 8.4 (inside the core) to r 10: Ø20 over the ridges, the class value (Head diameter)
RIDGE_Z = (SEAT + 0.5, SEAT + KNOB_H - 0.5)     # the ridges stop 0.5 short of the knob's faces (GEO-050)
SLOT_W, SLOT_L, SLOT_D = 2.0, 14.0, 2.0   # screwdriver (coin) slot across the knob's top along y, inside the core (the ridges start at r 8.4 > 7)
SHANK_R = 3.0                             # shank Ø6, plain: no thread (a quarter-turn stud is not screwed)
STUD_L = 21.0                             # class value (Length): the knob's underside to the tip, z 1 to -20
TIP = SEAT - STUD_L                       # -20
PIN_R, PIN_L, PIN_Z = 1.5, 12.0, -16.2    # cross pin Ø3 x 12 along y through the shank, its axis at z -16.2: 0.5 under the cam plate's underside (-14.2 - 1.5)
REC_X, REC_Y, REC_T = 20.0, 7.0, 1.2      # receptacle: plates 40 (x) x 14 (y), pressed from 1.2 sheet (thinner than 2.5 r: the gate skips its edges)
REC_TOP = -(PANEL_T + FLANGE_T)           # -4: the base plate's top, against the flange's underside
CAM_TOP = -13.0                           # the cam plate z -14.2..-13.0; the legs between the plates, z -13.0..-5.2
RIVET_X, RIVET_D = 14.0, 3.4              # 2 x M3 clearance medium (ISO 273) at x +-14 for the rivets or screws that fix the receptacle (the host's)
REC_SLOT = (6.5, 2.0)                     # the slots in both plates for the pin, x +-6.5 (the pin 12 long, 0.5 clear each end) by y +-2 (Ø3 pin, 0.5 clear each side)

def build():
    P = Prims(); Z = "M-ZINC"; S = "M-SILVER"; N = f"node:stud|{Z}"
    # ---- grommet (fixed): flange on the panel's outer face, tube through the panel; bored Ø7
    fl = P.cyl(Z, (0, 0, 0), (0, 0, GROM_FL_T), GROM_FL_R)
    P.hole(Z, (0, 0, -1), (0, 0, GROM_FL_T + 1), BORE_R, fl)
    tb = P.cyl(Z, (0, 0, -PANEL_T), (0, 0, 0), GROM_TUBE_R)
    P.hole(Z, (0, 0, -PANEL_T - 1), (0, 0, 1), BORE_R, tb)
    P.collider("grommet", -GROM_FL_R, -GROM_FL_R, -PANEL_T, 2 * GROM_FL_R, 2 * GROM_FL_R, PANEL_T + GROM_FL_T)
    # ---- stud (node): knob core, knurl ridges, slot, shank, cross pin
    core = P.cyl(N, (0, 0, SEAT), (0, 0, SEAT + KNOB_H), KNOB_R)                                     # knob, seated on the grommet's flange
    P.cutbox(N, -SLOT_W / 2, -SLOT_L / 2, SEAT + KNOB_H - SLOT_D, SLOT_W, SLOT_L, SLOT_D + 0.5, core)    # the slot along y, 2 deep
    for k in range(RIDGES):
        a = 2 * math.pi * (k + 0.5) / RIDGES; ex = (math.cos(a), math.sin(a), 0.0); ey = (-math.sin(a), math.cos(a), 0.0)
        o = (RIDGE_IN * ex[0] - RIDGE_W / 2 * ey[0], RIDGE_IN * ex[1] - RIDGE_W / 2 * ey[1], RIDGE_Z[0])
        P.obox(N, o, ex, ey, (0, 0, 1), RIDGE_OUT - RIDGE_IN, RIDGE_W, RIDGE_Z[1] - RIDGE_Z[0])
    P.cyl(N, (0, 0, TIP), (0, 0, SEAT), SHANK_R)                                                     # shank Ø6, z -20..1
    P.cyl(N, (0, -PIN_L / 2, PIN_Z), (0, PIN_L / 2, PIN_Z), PIN_R)                                   # cross pin along y (closed: across the slots)
    P.pivot("stud", "rotate", (0, 0, SEAT), axis=(0, 0, 1), range=(0, 90), unit="deg")
    P.collider("head", -RIDGE_OUT, -RIDGE_OUT, SEAT, 2 * RIDGE_OUT, 2 * RIDGE_OUT, KNOB_H)
    # ---- receptacle (fixed): base plate under the flange, two legs, cam plate; keyhole (bore + slot along x) in both plates
    for z0 in (REC_TOP - REC_T, CAM_TOP - REC_T):
        pl = P.box(S, -REC_X, -REC_Y, z0, 2 * REC_X, 2 * REC_Y, REC_T)
        P.hole(S, (0, 0, z0 - 1), (0, 0, z0 + REC_T + 1), BORE_R, pl)
        P.cutbox(S, -REC_SLOT[0], -REC_SLOT[1], z0 - 0.5, 2 * REC_SLOT[0], 2 * REC_SLOT[1], REC_T + 1, pl)
        if z0 > CAM_TOP:                                                                             # the base plate: the rivet holes
            for sx in (-1, 1): P.hole(S, (sx * RIVET_X, 0, z0 - 1), (sx * RIVET_X, 0, z0 + REC_T + 1), RIVET_D / 2, pl)
    for sx in (-1, 1):
        x0 = REC_X - REC_T if sx > 0 else -REC_X
        P.box(S, x0, -REC_Y, CAM_TOP, REC_T, 2 * REC_Y, REC_TOP - REC_T - CAM_TOP)                   # leg, plate to plate
    P.collider("receptacle", -REC_X, -REC_Y, CAM_TOP - REC_T, 2 * REC_X, 2 * REC_Y, REC_TOP - (CAM_TOP - REC_T))
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
