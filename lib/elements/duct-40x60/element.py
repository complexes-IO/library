#!/usr/bin/env python3
"""duct-40x60: slotted wiring duct 40 x 60 with snap-on cover, PVC, cut to length. Brief: references/measure.md (reference duct 40 x 60,
2-D drawing p. 1 and the STEP read-back). 1.1 (reviewer's duct-40x60 1.0 findings): base 57.7 high with the cover's skirts 6.4 over
the fingers (measure.md:22); the redrawn screw heads removed (OPERATING.md 12: a screw element is placed in a later version); the floor
slots stay out until their size is on file (spec.md); every figure not on file marked in spec.md with its class and reason. A minor:
nodes, origin and cut-outs as 1.0 (pm-motor-starter pins 1.0). 1.2: CLASS "run" (lib/README.md origins; mech-1-answer.md item 1), the
PVC render layer (item 2), each finger named part="duct-finger" (lib/requests/core/mech-idle-2026-11-06.md); a minor, the part unchanged.
1.3: the `breakout` parameter (lib/requests/core/mech-duct-breakout-2026-11-11.md, from request panel-11 item 1): positions along the run
where a thick cable enters and the installer breaks a finger off; the finger holding each position is left out of that wall, so the
slots either side of it join into one gap PITCH + SLOT (28) wide. The default build ("" = no breakout) is 1.2's part, unchanged."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din
from toolkit.prims import Prims

ID, VERSION, CLASS = "duct-40x60", "1.3", "run"
TITLE = "slotted wiring duct 40 x 60, snap-on cover, PVC, cut to length"
TOOLKIT = "1.3"
BASELINE = "reference duct 40 x 60 (references/measure.md: 2-D drawing p. 1, 40.0 x 60.1 section, 8.0 slots; STEP read-back, base 57.7 and cover 8.8)"
ORIGIN = "panel face y = 0, run start x = 0, section bottom z = 0; run along +x, section 40 along z, 60.1 toward -y"
COMMAND = "DUCT"
PARAMS = dict(length=1000.0, cover=True, breakout="")
W, H = 40.0, 60.1                              # section width (z) and total height off the panel: 2-D drawing p. 1 (measure.md:13-14)
HB, HC = 57.7, 8.8                             # base and cover heights: STEP read-back (measure.md:18, :22)
TL = H - HB                                    # 2.4: the lid, above the finger tops (60.1 - 57.7)
SKIRT = HC - TL                                # 6.4: the cover's skirts over the fingers (measure.md:22, "the cover sits 6.4 mm over the fingers")
T = 1.5                                        # wall and finger thickness: Assumption (B), spec.md
TS, TSC = 1.2, 0.2                             # skirt thickness, clearance to the wall: Assumption (C), spec.md
SLOT = 8.0                                     # slot width: 2-D drawing p. 1, 0.315 in (measure.md:16; product page 0.31 in)
PITCH, FINGER_H = 20.0, 25.0                   # slot pitch, finger height from the top of the wall: Assumption (B), spec.md
TRAVEL = 40.0                                  # cover lift-off travel: Assumption (C), spec.md
MAT = "M-WHITE-PVC"                            # the part is PVC (product page); the layer renders as M-WHITE-PA's white (toolkit/cadout.py, mech-1-answer.md item 2)

def breakouts(spec, L):
    """the `breakout` parameter read: positions along the run in mm joined by '/', each optionally prefixed by its finger wall, `a`
    (z 0) or `b` (z W - T); a bare position names both walls. A BOM row's "278/305" arrives as a string, a single "278" as a number
    (library.parse_params): both are taken. A position outside 0 to L, or a token that is not a position, stops the build (SRC-010's
    rule: no figure from nowhere). Returns {"a": [positions], "b": [positions]}."""
    out = {"a": [], "b": []}
    if spec is None or spec == "" or spec is False: return out
    for tok in str(spec).split("/"):
        t = tok.strip().lower(); walls = ("a", "b")
        if t[:1] in ("a", "b"): walls, t = (t[0],), t[1:]
        try: x = float(t)
        except ValueError: raise ValueError(f"duct-40x60: breakout '{tok}' is not a position along the run (mm, optionally prefixed a or b)")
        if not 0.0 <= x <= L: raise ValueError(f"duct-40x60: breakout {x:g} lies outside the run 0 to {L:g}")
        for w in walls: out[w].append(x)
    return out

def fingers_out(bo, L):
    """the start x of the one finger each breakout position names: the finger whose span holds the position; a position in a slot
    names the nearer of the two fingers beside it (the one before on a tie). One position, one finger."""
    out = set(); fw = PITCH - SLOT
    for p in bo:
        x = int(p // PITCH) * PITCH
        if p > x + fw and (p - (x + fw)) > (x + PITCH - p): x += PITCH               # in the slot after, nearer the next finger
        if x >= L: x -= PITCH                                                         # the run's end: the last finger
        out.add(round(x, 6))
    return out

def build(length=1000.0, cover=True, breakout=""):
    P = Prims(); L = float(length); BO = {w: fingers_out(ps, L) for w, ps in breakouts(breakout, L).items()}
    P.box(MAT, 0, -T, 0, L, T, W)                                     # back wall (floor) on the panel; floor slots: NOT ON FILE (B), spec.md
    web = HB - FINGER_H                                               # solid web of each side wall, 32.7
    for z0, wall in ((0.0, "a"), (W - T, "b")):
        P.box(MAT, 0, -web, z0, L, web, T)                            # side wall web
        x = 0.0
        while x < L:                                                  # fingers: PITCH - SLOT wide, FINGER_H tall, tops at -HB
            fw = min(PITCH - SLOT, L - x)
            if round(x, 6) not in BO[wall]: P.box(MAT, x, -HB, z0, fw, FINGER_H, T, part="duct-finger")   # a breakout leaves it out
            x += PITCH
    if cover:
        C = "node:cover|" + MAT
        P.box(C, 0, -H, 0, L, TL, W)                                  # lid, on the finger tops
        for z0 in (T + TSC, W - T - TSC - TS):                        # skirts inside the walls, over the fingers
            P.box(C, 0, -HB, z0, L, SKIRT, TS)
        P.pivot("cover", "translate", (0, -H, 0), axis=(0, -1, 0), range=(0, TRAVEL))
    P.collider("env", 0, -H, 0, L, H, W)
    return P

PREVIEWS = [dict(name="front three-quarter, 1000", az=250, el=20), dict(name="end section and fingers", az=200, el=15, center=(0, -30, 20), height=110),
            dict(name="open cover off", az=250, el=20, params=dict(cover=False))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
