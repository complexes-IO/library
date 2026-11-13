#!/usr/bin/env python3
"""disc-3p-30a: 3-pole rotary disconnect, 30 A class, body on the panel, lockable handle through the door. Brief: references/measure.md
(the maker's 2-D drawing p. 1: handle plate 69.1 sq, door pattern 36 x 36 / 4.2, body 44.6 wide, 58.6 deep, shaft 30.2, overall 86.3).
1.4 (elec-r31; the core's pin-nodes note of 2026-11-11, request panel-4 item 1): every terminal screw is a port node t-<pole>-line (top) /
t-<pole>-load (bottom), its pivot at the wire entry's mouth on the end face, axis the way the wire goes in, gender none (PIN-002); the
shaft runs to the coupler's end so the door unit and the body are one body at rest (GEO-070); the maker's names out of the text (DOC-006).
Nothing moved: a minor (nodes added, none moved).
1.5 (elec-r37; review disc-3p-30a-1.4 findings 1, 2, 4, 5): text only. The terminal and entry positions, the plate thickness and front
stack, the door cut-out, the body height and the shaft's round section are each one "Assumption (B)" with its reason (spec.md
Dimensions); the shaft row says what is built and what the `shaft` parameter does; the stale gate line replaced. Geometry as 1.4.
1.7 (elec-r48; review disc-3p-30a-1.5 findings 1 and 2): text only. The lever's width and length are class B (they set the envelope; spec.md
Dimensions, lever), and the 1.3 history row names the toolkit change. Geometry as 1.6."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "disc-3p-30a", "1.7", "device"
TITLE = "rotary disconnect switch, 3-pole 30 A, door-mounted lockable handle, panel-mounted body"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet (references/measure.md: 2-D drawing p. 1 plate 69.1 sq, 36 x 36 / 4.2 pattern, body 44.6 / 58.6 / 50.9, shaft 30.2, overall 86.3; datasheet p. 3 two-position handle, lockable in OFF)"
ORIGIN = "cut-out centre class: shaft axis on the door front face y = 0, handle toward -y, body behind the door toward +y"
COMMAND = "DISC"
CUTOUT = 14.0                       # door centre hole for the handle unit's coupler: Assumption (B), a fit with the host door (spec.md Dimensions, door cut-out); the 36 x 36 / 4.2 screw pattern is on file
PARAMS = dict(door_t=1.9, on=False, shaft=30.2)       # shaft: 30.2 as supplied; the maker's long-shaft class for a deep cabinet (datasheet p. 3)
PLATE, PLATE_T, HOLE_PAT = 69.1, 4.0, 36.0          # plate thickness 4: Assumption (B), with the front stack, so the stack meets 86.3 (spec.md Dimensions, handle plate)
BODY_W, BODY_H, BODY_D, BODY_D2 = 44.6, 69.1, 58.6, 50.9   # BODY_H: Assumption (B), at most the plate's 69.1 (spec.md Dimensions, body); the rest drawing p. 1
SHAFT_L, SHAFT_R = 30.2, 4.0        # the shaft drawn as a Ø8 round: Assumption (B), the brief's shafts are 6 x 6 square (spec.md Dimensions, shaft)
SWING = 90.0                       # OFF to ON; NOT ON FILE in the brief, the rotary-handle norm; recorded as an assumption (C: the twin reads the two ends)
ENTRY = (5.0, 10.0, 0.5)           # the wire entry marker on each end face: x width, y length, proud; the terminal positions: Assumption (B), the brief gives none (spec.md Dimensions, terminals)

def build(door_t=1.9, on=False, shaft=30.2):
    P = Prims(); SHAFT_L = float(shaft)
    DU = "node:door-unit|"                                                                          # the handle unit on the door: swings with the door (1.2)
    P.box(DU + "M-BLACK-PA", -PLATE / 2, -PLATE_T, -PLATE / 2, PLATE, PLATE_T, PLATE)              # handle plate on the door
    for sx in (-1, 1):
        for sz in (-1, 1): P.cyl(DU + "M-ZINC", (sx * HOLE_PAT / 2, -PLATE_T, sz * HOLE_PAT / 2), (sx * HOLE_PAT / 2, -PLATE_T - 0.8, sz * HOLE_PAT / 2), 2.4)   # plate screws
    P.cyl(DU + "M-BLACK-PA", (0, -PLATE_T, 0), (0, -PLATE_T - 4, 0), 16.0)                          # hub
    P.cyl(DU + "M-ZINC", (0, -PLATE_T + 0.5, 0), (0, door_t + 1.5, 0), CUTOUT / 2 - 1.0)           # coupler through the door: takes the shaft's square end (starts inside the plate: GEO-050)
    P.pivot("door-unit", "fixed", (0, 0, 0))
    H = "node:handle|M-GREY-PA"; hw, hl, hd = 14.0, 56.0, 12.0     # 1.6: grey on the black plate, the brief's black / grey handle (measure.md:3); 1.7: hw, hl class B, they set the envelope (spec.md Dimensions, lever)
    P.box(H, -hw / 2, -PLATE_T - 4 - hd, -8.0, hw, hd, hl)                                          # lever, OFF = up (+z): class C (spec.md Named nodes)
    P.box("node:handle|M-BLACK-PA", -hw / 2 + 2, -PLATE_T - 4 - hd - 2, hl - 20, hw - 4, 2, 10)     # padlock hasp end
    P.pivot("handle", "rotate", (0, -PLATE_T - 4, 0), axis=(0, -1, 0), range=(0, SWING))
    front = PLATE_T + 4 + hd + 2                                                                    # plate + hub + lever + hasp in front of the door face
    y0 = 86.3 - BODY_D - front + (SHAFT_L - 30.2)                                                   # body front: 86.3 handle face to body back as supplied (brief); a longer shaft moves the body back
    P.cyl("M-ZINC", (0, door_t + 1.5, 0), (0, y0 + 10, 0), SHAFT_R)                                 # shaft from the body to the coupler's end (1.4: seated on it; 1.2 left 0.5, GEO-070); it stays when the door opens
    P.box("M-GREY-PA", -BODY_W / 2, y0, -BODY_H / 2, BODY_W, BODY_D2, BODY_H)                       # body, stepped
    P.box("M-GREY-PA", -BODY_W / 2 + 4, y0 + BODY_D2, -BODY_H / 2 + 6, BODY_W - 8, BODY_D - BODY_D2, BODY_H - 12)
    ew, el, ep = ENTRY
    for i in range(3):                                                                              # three poles: terminals top and bottom
        cx = -BODY_W / 2 + BODY_W / 6 + i * BODY_W / 3
        for sz, side in ((1, "line"), (-1, "load")):
            n = f"t-{i + 1}-{side}"                                                                 # the port node (1.4): the screw head carries it
            P.cyl(f"node:{n}|M-ZINC", (cx, y0 + 8, sz * (BODY_H / 2)), (cx, y0 + 8, sz * (BODY_H / 2 + 1.0)), 2.6)
            P.box("M-GASKET", cx - ew / 2, y0 + 14, sz * BODY_H / 2 - (0 if sz > 0 else ep), ew, el, ep)
            P.pivot(n, "port", (cx, y0 + 14 + el / 2, sz * (BODY_H / 2 + ep)), axis=(0, 0, -sz), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp; at the entry's mouth on the end face, axis in
    P.collider("plate", -PLATE / 2, -PLATE_T - 4 - hd, -PLATE / 2, PLATE, PLATE_T + 4 + hd + 2, PLATE); P.collider("body", -BODY_W / 2, y0, -BODY_H / 2, BODY_W, BODY_D, BODY_H)
    return P

PREVIEWS = [dict(name="front handle plate on the door", az=260, el=15), dict(name="rear body behind the door", az=60, el=20), dict(name="side shaft through the door", az=180, el=10)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
