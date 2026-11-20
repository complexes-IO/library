#!/usr/bin/env python3
"""overload-9a-1no1nc: three-pole bimetallic thermal overload relay, trip class 10, 1 N.O. + 1 N.C., direct mount under the
9 A contactor. Built mechanism-first (v1.1) from references/interior.md, parts.csv and behaviour.md (2026-11-03): three heated
bimetals in the current paths, a compensation bimetal, the differential and trip slides, the latch, the 95-96 / 97-98 contacts,
the RESET/TEST button and the FLA dial; then the housing around them. Envelope, pin row and seat from references/measure.md
('Mate with the contactor'). Every interior position is not in the brief and is set here; spec.md classes them (C: mechanism
and walls the twin doesn't read; B: where a pin or wire meets the part).
1.2 (the backlog's checks): each driver of the trip chain meets its follower at rest, face to face (MOT-020): bimetal-2's tip on
the differential (the bimetals bend toward -y now; 1 and 3 clear it by 1.2, more than their 1.13 swing), the differential on the
trip slide, the latch's tooth held on the trip slide's +y face (the slide moving -y releases it), the latch's pushers on both aux
bridges' +y faces; the aux strips, links and compensation bimetal seated on the housing (GEO-070); genders on the ports (PIN-002);
screws, button, dial inside the 83.7 envelope (the brief's depth). `range` picks the maker's setting range (spec p. 3); the same
body serves all of them."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "overload-9a-1no1nc", "1.2", "device"
TITLE = "thermal overload relay, class 10, 1 NO + 1 NC aux, direct mount to the contactor, range by parameter; mechanism modelled"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet and 2-D drawing (references/measure.md, references/interior.md, references/source.txt: drawing p. 1: 45.0 x 71.7 x 83.7, pins Ø2.5 at 14.0, motor terminals at 14.5; spec p. 2, 3, 5-8; STEP read-back of the housing, pins and terminals)"
ORIGIN = "carried: its back face on the contactor's mounting plane, x = 0 at its left face, z = 0 at the top of the upper housing (contactor rail centre line - 39.2); body hangs toward -z, front toward -y"
COMMAND = "OVLD"
# the maker's setting ranges and maximum fuse (A), spec p. 3 (p. 7 gives lower class RK5 fuse figures: inconsistency stated in ratings.csv)
RANGES = {"D004": (0.28, 0.40, None), "D008": (0.56, 0.80, 15), "D012": (0.8, 1.20, 15), "D018": (1.2, 1.80, 15), "D028": (1.8, 2.80, 15),
          "U004": (2.8, 4.0, 15), "D063": (4.0, 6.30, 25), "U008": (5.6, 8.0, 30), "U010": (7.0, 10.0, 40), "D125": (8.0, 12.5, 50)}
PARAMS = dict(range="D012", view="product", tripped=False, mode="H")

# ---- envelope and mate (measure.md, interior.md: drawing p. 1 and STEP read-back)
W, D, D_FRONT = 45.0, 77.0, 6.7                  # width, body depth, front projection (83.7 overall)
Z_BOT, Z_FULL = -57.6, -10.6                     # bottom; top of the full-depth (47.0) body; z = 0 is the upper housing top
UPPER_D = 60.0                                    # upper housing around the pins: 60 deep (STEP)
PIN_X, PIN_PITCH, PIN_R = (5.3, 19.3, 33.3), 14.0, 1.25            # Ø2.5 pins, row 3.2 left of the body centre line
PIN_TOP, SLEEVE_TOP, SLEEVE_R = 14.1, 3.3, 2.2                      # pin tips 71.7 and sleeve tops 60.9 above the bottom
PIN_Y = -42.0                                     # pin row depth: not on the drawing (spec.md, class B: under the contactor's lower clamps)
T_X, T_PITCH = (8.0, 22.5, 37.0), 14.5            # motor terminals T1 T2 T3 at the bottom (drawing p. 1)
AUX_X = (6.75, 17.25, 27.75, 38.25)               # 95 96 97 98 terminal blocks at 10.5 pitch (STEP; which is which: spec.md, class B)
HOOK_TOP = 9.7                                    # two rear hooks, top 67.3 above the bottom (STEP)
WALL = 1.5                                        # housing wall (spec.md, class C)
# ---- mechanism: not in the brief, set here (spec.md, class C)
BI = dict(t=0.8, w=4.0, root=-14.0, end=-40.0, y=-30.0, bend=2.5)  # heated bimetals: strip, root, free end, plane, deflection (deg) at trip, toward -y
DIFF = dict(y=(-32.7, -31.2), z=(-43.0, -39.0), travel=1.0)        # differential slide across the three free ends, 1.2 in front of them
TIP = dict(x=1.0, z=(-40.5, -39.0))                                # bimetal-2's tip: bridges the 1.2 to the slide (half width, z band)
TRIP = dict(x=(33.0, 41.0), y=(-36.7, -32.7), z=(-45.0, -37.0), travel=1.5)  # its +y face on the differential's -y face
LATCH = dict(x=(33.5, 40.5), y=(-52.0, -46.0), z=(-36.0, -26.0), pivot=(37.0, -49.0, -26.0), swing=12.0)
AUXC = dict(y=(-62.0, -61.0), gap=1.0)            # 95-96 / 97-98 bridges behind the front module
LINK_Z = (-48.0, -46.0)                           # heater links run under the trip slide to the motor clamps' back faces
PUSH_Z = (-19.0, -17.0)                           # the latch's pushers, inside the aux bridges' z band (-19.6 ... -16.6)
INSET = 0.2                                       # button, dial and aux screw faces sit this far inside the front face (the 83.7 depth)

def ratings_for(range="D012", **_):
    a, b, fuse = RANGES[range]
    out = dict(ir_min=(a, "A", "on file", f"maker's datasheet, range {range} (spec p. 3)"), ir_max=(b, "A", "on file", f"maker's datasheet, range {range} (spec p. 3)"))
    if fuse: out["max_fuse"] = (fuse, "A", "on file", f"maker's datasheet, spec p. 3 ({range}); p. 7 gives lower class RK5 figures")
    return out

def build(range="D012", view="product", tripped=False, mode="H"):
    assert range in RANGES, f"range {range}: one of {', '.join(RANGES)}"
    P = Prims(); cut = view == "cutaway"; G = "M-GREY-PA"
    yf = -D - D_FRONT
    # ---------------- housing as a shell (cutaway: front face and -x wall removed)
    P.box(G, 0, -WALL, Z_BOT, W, WALL, -Z_BOT)                                                         # back wall, full height to the upper housing top
    P.box(G, W - WALL, -D, Z_BOT, WALL, D - WALL, Z_FULL - Z_BOT)                                      # +x wall
    if not cut: P.box(G, 0, -D, Z_BOT, WALL, D - WALL, Z_FULL - Z_BOT)                                 # -x wall
    P.box(G, WALL, -D, Z_BOT, W - 2 * WALL, D - WALL, WALL)                                            # bottom
    P.box(G, 0, -D, Z_FULL - WALL, W, D - UPPER_D, WALL)                                              # top of the full-depth body in front of the upper housing
    # upper housing around the pins: 60 deep, 10.6 tall above the full-depth body
    P.box(G, W - WALL, -UPPER_D, Z_FULL, WALL, UPPER_D - WALL, -Z_FULL)
    if not cut: P.box(G, 0, -UPPER_D, Z_FULL, WALL, UPPER_D - WALL, -Z_FULL)
    P.box(G, WALL, -UPPER_D, Z_FULL, W - 2 * WALL, WALL, -Z_FULL)                                      # its front wall
    top = P.box(G, 0, -UPPER_D, -WALL, W, UPPER_D - WALL, WALL)                                        # its top face, the pins come through it
    for x in PIN_X: P.hole("M-GASKET", (x, PIN_Y, -WALL - 1), (x, PIN_Y, 1), SLEEVE_R + 0.1, top)
    # front module (button and dial face): 54.7 deep, 27.8 tall, 6.7 proud of the body face
    if not cut:
        mod = P.box(G, 0, yf, Z_FULL - 27.8, W, D_FRONT, 27.8)                                         # the proud face block
        zc0 = Z_FULL - 20.0
        P.hole("M-GASKET", (8.0, yf - 1.0, zc0), (8.0, yf + 4.5, zc0), 5.2, mod)                          # RESET / TEST counterbore: the cap sits flush and presses 2 into it
        P.hole("M-GASKET", (34.0, yf - 1.0, zc0), (34.0, yf + 1.5, zc0), 6.2, mod)                        # dial recess: flush, inside the 83.7 envelope
        for bx in (8.0, 34.0): P.hole("M-GASKET", (bx, yf - 1.0, zc0), (bx, -D + 1.0, zc0), 2.2, mod)  # stem bores
        for x in AUX_X: P.hole("M-GASKET", (x, yf - 1.0, Z_FULL - 3.5), (x, yf + 1.5, Z_FULL - 3.5), 2.2, mod)  # aux screw counterbores
        P.box("M-WHITE-PA", 3, yf - 0.2, Z_FULL - 13.5, W - 6, 0.2, 6.0)                              # scale and legend field (decal: range, A / AUTO / HAND / H), between the screws and the dial
        P.box(G, WALL, -D, Z_BOT + WALL, W - 2 * WALL, WALL, Z_FULL - 27.8 - Z_BOT - WALL)             # body front face below the module
    P.collider("env", 0, yf, Z_BOT, W, D + D_FRONT, HOOK_TOP - Z_BOT)
    # ---------------- rear hooks into the contactor base
    for hx in (8.0, W - 8.0): P.cyl(G, (hx, -2.75, -0.5), (hx, -2.75, HOOK_TOP), 2.0)               # round hooks into the contactor's lug slots
    # ---------------- main current paths: pin -> heater bimetal -> link -> motor terminal T
    ports = "node:main|M-CU"
    for i, x in enumerate(PIN_X):
        P.cyl(ports, (x, PIN_Y, PIN_TOP - 22.0), (x, PIN_Y, PIN_TOP), PIN_R)                           # Ø2.5 pin, 22 long
        P.cyl("node:main|M-GREY-PA", (x, PIN_Y, Z_FULL + 0.5), (x, PIN_Y, SLEEVE_TOP), SLEEVE_R)        # insulating sleeve
        P.box("M-CU", x - 2.0, PIN_Y - 1.0, PIN_TOP - 22.0 - 2.0, 4.0, 2.0, 2.0)                        # pin foot to the heater
        B = f"node:bimetal-{i + 1}|M-STEEL-7035"                                                       # heated bimetal strip (the heater wraps it: one solid here)
        P.box(B, x - BI["w"] / 2, BI["y"], BI["end"], BI["w"], BI["t"], BI["root"] - BI["end"])
        if i == 1: P.box(B, x - TIP["x"], DIFF["y"][1], TIP["z"][0], 2 * TIP["x"], BI["y"] - DIFF["y"][1], TIP["z"][1] - TIP["z"][0])  # tip on the differential
        P.pivot(f"bimetal-{i + 1}", "rotate", (x, BI["y"] + BI["t"], BI["root"]), axis=(-1, 0, 0), range=(0, BI["bend"]))   # bends toward -y
        yc = -D + 10.0 + 9.2                                                                           # the motor clamp's back face
        P.box("M-CU", min(x, T_X[i]) - 1.5, yc, LINK_Z[0], abs(T_X[i] - x) + 3.0, BI["y"] + 2.0 - yc, LINK_Z[1] - LINK_Z[0])  # link from under the strip to T's clamp
        P.box("M-CU", T_X[i] - 3.9, -D + 10.0, Z_BOT + WALL, 7.8, 9.2, 15.2 - WALL)                    # motor terminal clamp (7.8 x 9.2 x 15.2)
        P.cyl("node:motor|M-ZINC", (T_X[i], -D + 0.01, Z_BOT + 8.0), (T_X[i], -D - 1.5, Z_BOT + 8.0), 3.0)   # clamp screw on the front face
    P.pivot("main", "port", (PIN_X[1], PIN_Y, PIN_TOP), axis=(0, 0, 1), range=(0, 0), unit="pin", gender="male")
    P.pivot("motor", "port", (T_X[1], -D - 1.5, Z_BOT + 8.0), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")
    # ---------------- compensation bimetal (ambient): fixed here, its bending is the model's parameter; hung from the upper housing's top
    P.box("node:comp-bimetal|M-STEEL-7035", TRIP["x"][0] - 3.0, TRIP["y"][0] - 0.8, BI["end"], 2.0, 0.8, BI["root"] - BI["end"])
    P.box(G, TRIP["x"][0] - 3.0, TRIP["y"][0] - 0.8, BI["root"], 2.0, 0.8, -WALL - BI["root"])          # its anchor post
    P.pivot("comp-bimetal", "fixed", (TRIP["x"][0] - 2.0, TRIP["y"][0], BI["root"]))
    # ---------------- differential slide across the free ends, trip slide, latch
    tr = DIFF["travel"] if tripped else 0.0
    P.box("node:differential|M-WHITE-PA", 2.5, DIFF["y"][0] - tr, DIFF["z"][0], W - 5.0, DIFF["y"][1] - DIFF["y"][0], DIFF["z"][1] - DIFF["z"][0])
    P.pivot("differential", "translate", (W / 2, DIFF["y"][0], DIFF["z"][0]), axis=(0, -1, 0), range=(0, DIFF["travel"]))
    tt = TRIP["travel"] if tripped else 0.0
    P.box("node:trip-slide|M-WHITE-PA", TRIP["x"][0], TRIP["y"][0] - tt, TRIP["z"][0], TRIP["x"][1] - TRIP["x"][0], TRIP["y"][1] - TRIP["y"][0], TRIP["z"][1] - TRIP["z"][0])
    P.pivot("trip-slide", "translate", (sum(TRIP["x"]) / 2, TRIP["y"][0], TRIP["z"][0]), axis=(0, -1, 0), range=(0, TRIP["travel"]))
    L_ = "node:latch|M-BLACK-PA"; ly0, ly1 = LATCH["y"]; lz0, lz1 = LATCH["z"]; pz0, pz1 = PUSH_Z
    P.box(L_, LATCH["x"][0], ly0, lz0, LATCH["x"][1] - LATCH["x"][0], ly1 - ly0, lz1 - lz0)                # the latch body on its pivot
    # its tooth, held on the trip slide's +y face: the slide moving -y releases it; the arm runs over the slide, clear of bimetal-3
    P.box(L_, 35.5, ly1, lz0, 5.0, TRIP["y"][1] + 1.0 - ly1, 1.0)                                       # arm
    P.box(L_, 35.5, TRIP["y"][1], DIFF["z"][1] + 0.2, 5.0, 1.0, lz0 - DIFF["z"][1] - 0.2)              # tooth, 0.2 above the differential
    # the pushers on the aux bridges' +y faces: above the pivot, so the latch's turn drives them toward -y
    P.box(L_, 34.0, ly0, lz1, 5.0, 3.0, pz1 - lz1)                                                     # riser on the body's top
    P.box(L_, 34.0, AUXC["y"][1], pz0, 5.0, ly0 - AUXC["y"][1], pz1 - pz0)                             # pusher on 97-98's bridge
    P.box(L_, 9.5, ly0 - 3.0, pz0, 34.0 - 9.5, 3.0, pz1 - pz0)                                         # cross bar
    P.box(L_, 9.5, AUXC["y"][0] - 2.0, pz0, 5.0, ly0 - 3.0 - AUXC["y"][0] + 2.0, pz1 - pz0)            # finger between 95-96's strips onto its bridge
    P.pivot("latch", "rotate", LATCH["pivot"], axis=(1, 0, 0), range=(0, LATCH["swing"]))
    # ---------------- auxiliary contacts: 95-96 N.C. (closed at rest), 97-98 N.O. (open at rest), driven toward -y on a trip
    ya, yb = AUXC["y"]; g = AUXC["gap"]; ta = g if tripped else 0.0
    for name, x0, x1, no in (("aux-95", AUX_X[0], AUX_X[1], False), ("aux-97", AUX_X[2], AUX_X[3], True)):
        for x in (x0, x1): P.box("M-CU", x - 1.5, ya - 2.0, Z_FULL - 14.0, 3.0, 1.0, 14.0 - WALL)         # fixed contact strips from the terminals, seated under the body's top
        y0 = (ya - 3.0) if not no else (ya - 1.0 + g)                                                    # N.C. bridge resting on the strips' front; N.O. bridge a gap behind them
        P.box(f"node:{name}|M-CU", x0 - 1.5, y0 - ta, Z_FULL - 9.0, x1 - x0 + 3.0, 1.0, 3.0)           # a trip moves both toward -y: 95-96 opens, 97-98 closes
        P.pivot(name, "translate", (0.5 * (x0 + x1), y0, Z_FULL - 9.0), axis=(0, -1, 0), range=(0, g))
    if not cut:
        for x in AUX_X: P.cyl("node:aux|M-ZINC", (x, yf + 1.5, Z_FULL - 3.5), (x, yf + INSET, Z_FULL - 3.5), 2.0)   # screw heads in their counterbores
        P.pivot("aux", "port", (AUX_X[0], yf + INSET, Z_FULL - 3.5), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")
    # ---------------- RESET / TEST button (front left) and FLA dial (front right) with their stems into the module
    zc = Z_FULL - 20.0; assert mode in ("H", "HAND", "AUTO", "A"), mode                               # the button's four positions (spec p. 2): a decal mark per mode
    P.cyl("node:btn-reset|M-RED-PA", (8.0, yf + 2.5, zc), (8.0, yf + INSET, zc), 5.0)                  # cap face 0.2 inside the counterbore (no face shared with the front)
    P.cyl("node:btn-reset|M-RED-PA", (8.0, yf + 6.0, zc), (8.0, yf + 2.5, zc), 2.0)
    P.pivot("btn-reset", "translate", (8.0, yf, zc), axis=(0, 1, 0), range=(0, 2.0))
    P.cyl("node:dial-fla|M-WHITE-PA", (34.0, yf + 1.5, zc), (34.0, yf + INSET, zc), 6.0)
    P.cyl("node:dial-fla|M-WHITE-PA", (34.0, yf + 5.0, zc), (34.0, yf + 1.5, zc), 2.0)
    P.pivot("dial-fla", "rotate", (34.0, yf, zc), axis=(0, -1, 0), range=(0, 270))
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="top pins into the contactor", az=250, el=55),
            dict(name="cutaway mechanism", az=240, el=15, params=dict(view="cutaway")),
            dict(name="tripped cutaway", az=240, el=15, params=dict(view="cutaway", tripped=True))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
