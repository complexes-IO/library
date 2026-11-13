#!/usr/bin/env python3
"""contactor-9a-1no1nc: IEC contactor 9 A AC-3, 24 V DC coil, three main N.O. poles, built-in 1 N.O. + 1 N.C., front aux block option.
Built mechanism-first (v1.1): fixed E-core and coil in the base, armature and contact carrier moving +y (toward the mounting plate,
normal to it: the any-orientation mounting of spec p. 10), three double-break main bridges on contact springs, two built-in aux
bridges, the front block's slide following the carrier; then the housings around them. Briefs: references/measure.md (envelope,
Stage 0) and references/interior.md, parts.csv, behaviour.md (mechanism, Stage 0b; the reference part's record is
references/source.txt). Every internal position is NOT ON FILE in the brief and is set here; spec.md lists them with their class.
1.3: the carrier's stops meet every bridge it drives (MOT-020), the fixed aux strips seat on the housing walls (GEO-070), the
terminals declare gender none (PIN-002), the maker's names live in references/ only (DOC-006)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
from toolkit import library, din, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "contactor-9a-1no1nc", "1.3", "device"
TITLE = "IEC contactor 9 A AC-3, 24 V DC coil, 1 NO + 1 NC aux, front aux block option, 35 mm rail; mechanism modelled"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet and 2-D drawings (references/measure.md, references/source.txt: contactor and front aux block drawings p. 1; series spec p. 5-10, 14, 15, 24; STEP read-back of housings and terminal rows)"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "CONT"
PARAMS = dict(aux=True, view="product", operated=False)

# ---- envelope (2-D drawing p. 1; STEP read-back split of the depth; BFB drawing p. 1)
W, H, D = 44.8, 78.4, 98.5        # D: rail back (mounting plane) to the coil face, drawing p. 1
RAIL_IN = 7.5                      # the 35 x 7.5 rail sits in a groove in the base: the body's back is on the mounting plane (1.2)
DF = D - RAIL_IN                   # rail crown to the coil face: 91.0
GROOVE_Z = 18.4                    # groove lips at ±18.4 about the rail centre line (STEP read-back)
MOUNT = dict(x=17.5, z=35.0, r=2.25)   # 70 x 35 screw pattern and hole Ø4.5 (drawing p. 1; the Ø confirmed by the terminal, round 2)
HOOK_SLOTS = (11.1, 40.1)          # where the overload's two rear hooks enter the lower lug (overload interior brief; x with the overload's 3.1 offset)
BASE_D = 39.2                    # rear base (STEP 45.7 overlapping the housing; the shoulder face sits at -39.2)
HOUSE_H = 56.0                   # coil / contact housing height between the terminal shoulders
WALL = 2.0                       # housing wall: NOT ON FILE (Assumption)
AUX = (45.0, 46.0, 42.0)
PITCH, ROW_Z = 14.0, 31.5        # main terminals: 14.0 pitch across, rows 63 apart (interior brief, STEP read-back)
XP = [W / 2 + (i - 1) * PITCH for i in range(3)]          # pole centres along x
CLAMP_Y = -34.5                  # clamp entry depth (where the overload's pins come up): NOT ON FILE (Assumption)
# ---- mechanism: all NOT ON FILE (Assumptions; the brief names gap and over-travel as the figures to find)
GAP, OVER = 2.0, 1.5             # contact gap per break, over-travel
STROKE = GAP + OVER              # carrier / armature stroke 3.5
CORE = dict(x0=8.0, x1=36.8, back=(-6.0, -10.0), legs_to=-30.0, z_out=(14.0, 20.0), z_mid=5.0)
ARM = (-33.5, -38.5)             # armature plate, released (y range)
REAR = (-38.5, -40.5)            # carrier rear plate behind the armature... in front of it
Y_FIX = (-49.0, -50.5)           # fixed main contact strips; rivet faces at -51.0
Y_BR = (-53.6, -55.6)            # bridge bar, released; rivets from -53.0 (gap 2.0 to -51.0)
Y_XBAR = (-60.0, -62.0)          # carrier crossbar: contact springs between it and the bridges
Y_AUXBAR = (-84.0, -86.0)        # carrier front crossbar carrying the aux bridges
Y_AUXFIX = (-80.0, -81.5)        # fixed aux strips

def _helix(x, z, y0, y1, r=1.5, turns=5, wire=0.3, axis="y"):
    pts = [(x + r * math.cos(2 * math.pi * k / 14), y0 + (y1 - y0) * k / (turns * 14), z + r * math.sin(2 * math.pi * k / 14)) for k in range(turns * 14 + 1)]
    return SW.sweep(pts, SW.circle_profile(wire, 6))

def build(aux=True, view="product", operated=False):
    P = Prims(); s = STROKE if operated else 0.0; g = GAP if operated else 0.0
    cut = view == "cutaway"
    # ---------------- housings as shells (product: all walls; cutaway: face and -x walls removed)
    G = "M-GREY-PA"
    back = P.box(G, 0, -WALL, -H / 2, W, WALL, H)                                                       # base back wall: the groove bottom on the rail crown
    P.box(G, W - WALL, -BASE_D, -H / 2, WALL, BASE_D - WALL, H)                                         # base +x wall
    if not cut: P.box(G, 0, -BASE_D, -H / 2, WALL, BASE_D - WALL, H)                                    # base -x wall
    for sz in (1, -1):                                                                                  # terminal shoulders (top / bottom of the base)
        sh = P.box(G, 0 if not cut else WALL, -BASE_D, sz * HOUSE_H / 2 if sz > 0 else -H / 2, W - (0 if not cut else WALL), WALL, (H - HOUSE_H) / 2)
        ew = P.box(G, 0, -BASE_D + WALL, (H / 2 - WALL) if sz > 0 else -H / 2, W, BASE_D - 2 * WALL, WALL)  # base end walls
        for mx in (W / 2 - MOUNT["x"], W / 2 + MOUNT["x"]):
            P.hole("M-GASKET", (mx, -BASE_D + WALL + 1, sz * MOUNT["z"]), (mx, -BASE_D - 1, sz * MOUNT["z"]), MOUNT["r"], sh)   # screw through the shoulder
            if sz > 0: P.hole("M-GASKET", (mx, 1, sz * MOUNT["z"]), (mx, -WALL - 1, sz * MOUNT["z"]), MOUNT["r"], back)
        for x in XP: P.hole("M-GASKET", (x, CLAMP_Y, sz * (H / 2 + 1)), (x, CLAMP_Y, sz * (H / 2 - WALL - 1)), 2.4, ew)   # clamp entries: wires, and the overload's pins below
    P.box(G, W - WALL, -DF, -HOUSE_H / 2, WALL, DF - BASE_D, HOUSE_H)                                   # housing +x wall
    if not cut:
        P.box(G, 0, -DF, -HOUSE_H / 2, WALL, DF - BASE_D, HOUSE_H)                                      # housing -x wall
        wx, wz = 8.3, 10.3                                                                              # front face with the window the front block's slide passes (1.2)
        P.box(G, WALL, -DF, -HOUSE_H / 2 + WALL, W - 2 * WALL, WALL, HOUSE_H / 2 - WALL - wz)            # below the window
        P.box(G, WALL, -DF, wz, W - 2 * WALL, WALL, HOUSE_H / 2 - WALL - wz)                             # above
        P.box(G, WALL, -DF, -wz, W / 2 - wx - WALL, WALL, 2 * wz); P.box(G, W / 2 + wx, -DF, -wz, W / 2 - wx - WALL, WALL, 2 * wz)   # sides
        if not aux: P.box("M-WHITE-PA", 4, -DF - 0.2, 12.0, W - 8, 0.2, 12.0)                           # label field above the window (decal; with the front block fitted its face carries it)
    for mx in (W / 2 - MOUNT["x"], W / 2 + MOUNT["x"]): P.hole("M-GASKET", (mx, 1, -MOUNT["z"]), (mx, -WALL - 1, -MOUNT["z"]), MOUNT["r"], back)
    for sz in (1, -1): P.box(G, 0 if not cut else WALL, -DF, (HOUSE_H / 2 - WALL) if sz > 0 else -HOUSE_H / 2, W - (0 if not cut else WALL), DF - BASE_D, WALL)   # housing top / bottom
    # rear lugs either side of the rail groove, down to the mounting plane (1.2: was a clip behind a body that stood on the crown)
    for sz in (1, -1):
        lug = P.box(G, 0, 0, GROOVE_Z if sz > 0 else -H / 2, W, RAIL_IN, H / 2 - GROOVE_Z)
        for mx in (W / 2 - MOUNT["x"], W / 2 + MOUNT["x"]): P.hole("M-GASKET", (mx, RAIL_IN + 1, sz * MOUNT["z"]), (mx, -WALL - 1, sz * MOUNT["z"]), MOUNT["r"], lug)
        if sz < 0:
            for hx in HOOK_SLOTS: P.hole("M-GASKET", (hx, RAIL_IN - 2.75, -H / 2 - 1), (hx, RAIL_IN - 2.75, -H / 2 + 11), 2.2, lug)   # overload hook slots
    P.box(G, W / 2 - 3, 1.2, -GROOVE_Z, 6, 1.0, 2.4)                                                    # rail latch tongue behind the rail's lower crown lip
    # ---------------- magnet system (fixed): E-core, coil on the centre leg, leads to A1 / A2
    c = CORE; St = "M-STEEL-7035"
    P.box(St, c["x0"] - 2, c["back"][1], -c["z_out"][1], c["x1"] - c["x0"] + 4, c["back"][0] - c["back"][1], 2 * c["z_out"][1])   # back plate (yoke)
    for z0, z1 in ((c["z_out"][0], c["z_out"][1]), (-c["z_out"][1], -c["z_out"][0]), (-c["z_mid"], c["z_mid"])):
        P.box(St, c["x0"], c["legs_to"], z0, c["x1"] - c["x0"], c["back"][1] - c["legs_to"], z1 - z0)                   # outer legs and centre leg
    P.box("node:coil|M-CU", c["x0"] - 1, c["legs_to"] + 1.5, -c["z_out"][0] + 0.8, c["x1"] - c["x0"] + 2, c["back"][1] - c["legs_to"] - 2.5, 2 * c["z_out"][0] - 1.6)
    P.pivot("coil", "emissive", (W / 2, -20.0, 0), axis=(0, -1, 0), range=(0, 1))                       # x-ray cue: glows while energised
    for zt in (HOUSE_H / 2, -HOUSE_H / 2):                                                                # coil leads along the +x wall to A1 (top) and A2 (bottom)
        sz = math.copysign(1, zt)
        lead = [(c["x1"] + 0.5, -20.0, sz * 8.0), (W - WALL - 1.0, -24.0, sz * 22.0), (W - WALL - 1.0, -DF + 10.0, sz * 22.0), (22.4, -DF + 7.5, zt - sz * 2.5)]
        P.mesh("M-CU", SW.sweep(SW.resample(lead, 2.0), SW.circle_profile(0.35, 6)))
    # ---------------- armature + carrier (one moving assembly, translate +y by the stroke)
    P.box("node:armature|M-STEEL-7035", c["x0"], ARM[1] + s, -c["z_out"][1], c["x1"] - c["x0"], ARM[0] - ARM[1], 2 * c["z_out"][1])
    P.pivot("armature", "translate", (W / 2, ARM[0], 0), axis=(0, 1, 0), range=(0, STROKE))
    C = "node:carrier|M-WHITE-PA"
    P.box(C, 2.5, REAR[1] + s, -22, W - 5, REAR[0] - REAR[1], 44)                                       # rear plate on the armature
    for x0 in (2.5, W - 4.5): P.box(C, x0, Y_XBAR[0] + s, -4, 2.0, REAR[1] - Y_XBAR[0], 8)            # side columns
    P.box(C, 2.5, Y_XBAR[1] + s, -6, W - 5, Y_XBAR[0] - Y_XBAR[1], 12)                                 # crossbar (contact spring seats)
    for x0 in (2.5, W - 4.5): P.box(C, x0, Y_AUXBAR[0] + s, -3, 2.0, Y_XBAR[1] - Y_AUXBAR[0], 6)       # front columns
    xa = W - 8.0                                                                                       # front crossbar with a window for the N.O. aux bridge 13-14 (1.2)
    P.box(C, 2.5, Y_AUXBAR[1] + s, -3, xa - 2.5 - 2.5, Y_AUXBAR[0] - Y_AUXBAR[1], 6); P.box(C, xa + 2.5, Y_AUXBAR[1] + s, -3, W - 2.5 - xa - 2.5, Y_AUXBAR[0] - Y_AUXBAR[1], 6)
    P.box(C, W / 2 - 2, -DF + WALL + s, -3, 4, Y_AUXBAR[1] - (-DF + WALL), 6)                          # stem to the face window (drives the front block's slide)
    # 1.3 (MOT-020): the carrier's stops, each on the face of a bridge it drives, at z -3..3 where no fixed strip runs (|z| >= 6).
    # Main poles: the contact spring presses each bridge +y onto this bar; past the gap the bridge stops on its rivets and the bar
    # runs on by the over-travel (the spring takes it). Design: 1.0 thick, the crossbar's width (Assumption (C), internal mechanism)
    P.box(C, 2.5, Y_BR[0] + s, -3, W - 5, 1.0, 6)                                                      # main bridges' stop bar, y -53.6 ... -52.6
    P.box(C, xa - 3.5, Y_AUXBAR[0] - 0.1 + s, -3, 7.0, 1.1, 6)                                         # N.O. aux 13-14's stop across the window
    P.box(C, 8.0 - 1.0, Y_AUXBAR[0] + s, -3, 2.0, Y_AUXFIX[0] - Y_AUXBAR[0], 6)                         # N.C. aux 21-22's pusher, lifts its bridge +y
    P.pivot("carrier", "translate", (W / 2, REAR[0], 0), axis=(0, 1, 0), range=(0, STROKE))
    # return springs between the base back wall and the carrier rear plate
    for z in (17.0, -17.0): P.mesh("node:spring-return|M-ZINC", _helix(4.2, z, -WALL, REAR[1] + s + (REAR[0] - REAR[1]) * 0, r=1.4, turns=9, wire=0.35))
    P.pivot("spring-return", "compress", (4.2, -WALL, 0), axis=(0, -1, 0), range=(0, STROKE))
    # ---------------- three main poles: fixed strips from the terminals, double-break bridge, contact spring
    for i, x in enumerate(XP):
        for sz in (1, -1):
            zt = sz * ROW_Z
            z_in, z_out = sz * 9.0, sz * (HOUSE_H / 2 - WALL - 0.5)
            P.box("M-CU", x - 3, Y_FIX[1], min(z_in, z_out), 6, Y_FIX[0] - Y_FIX[1], abs(z_out - z_in))         # fixed strip along z
            P.box("M-CU", x - 3, Y_FIX[1], (HOUSE_H / 2 - WALL - 2.0) if sz > 0 else -(HOUSE_H / 2 - WALL), 6, -BASE_D - Y_FIX[1], 2.0)   # riser to the shoulder terminal
            P.cyl("M-SILVER", (x, Y_FIX[1], sz * 10.0), (x, Y_FIX[1] - 0.5, sz * 10.0), 1.8)          # fixed rivet, face at -51.0
        B = f"node:pole-{i + 1}|M-CU"
        P.box(B, x - 3, Y_BR[1] + g, -12.0, 6, Y_BR[0] - Y_BR[1], 24.0)                                 # bridge bar
        for sz in (1, -1): P.cyl(f"node:pole-{i + 1}|M-SILVER", (x, Y_BR[0] + g, sz * 10.0), (x, Y_BR[0] + g + 0.6, sz * 10.0), 1.8)
        P.pivot(f"pole-{i + 1}", "translate", (x, Y_BR[0], 0), axis=(0, 1, 0), range=(0, GAP))
        P.mesh(f"node:spring-contact-{i + 1}|M-ZINC", _helix(x, 0.0, Y_XBAR[0] + s, Y_BR[1] + g, r=1.6, turns=4, wire=0.35))
        P.pivot(f"spring-contact-{i + 1}", "compress", (x, Y_XBAR[0], 0), axis=(0, 1, 0), range=(0, OVER))
    # ---------------- built-in auxiliaries: 13-14 N.O. at x 36.8, 21-22 N.C. at x 8.0
    for name, x, no in (("aux-13", W - 8.0, True), ("aux-21", 8.0, False)):
        for sz in (1, -1):
            P.box("M-CU", x - 2, Y_AUXFIX[1], min(sz * 6.0, sz * (HOUSE_H / 2 - WALL)), 4, Y_AUXFIX[0] - Y_AUXFIX[1], abs(HOUSE_H / 2 - WALL - 6.0))   # 1.3: seated on the housing wall (GEO-070)
        yb = (Y_AUXFIX[1] - 0.6 - GAP) if no else (Y_AUXFIX[0] + 0.0)                                  # N.O. bridge in front with the gap; N.C. bridge resting behind
        P.box(f"node:{name}|M-CU", x - 2, yb - (1.5 if no else 0.0) + s, -8.0, 4, 1.5, 16.0)
        P.pivot(name, "translate", (x, yb, 0), axis=(0, 1, 0), range=(0, STROKE))
    # ---------------- terminals (ports): main 1..6 on the shoulders, A1 / 13 / 21 top edge, A2 / 14 / 22 bottom edge
    for i, x in enumerate(XP):
        for sz, n in ((1, 2 * i + 1), (-1, 2 * i + 2)):
            P.cyl(f"node:t-{n}|M-ZINC", (x, -BASE_D, sz * ROW_Z), (x, -BASE_D - 1.5, sz * ROW_Z), 3.0)
            P.pivot(f"t-{n}", "port", (x, -BASE_D - 1.5, sz * ROW_Z), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
            pass                                                                                    # wire entries are the cut clamp holes (1.2: the dark plates covered them)
    for (x, top, bot) in ((22.4, "a1", "a2"), (W - 8.0, "13", "14"), (8.0, "21", "22")):
        for sz, n in ((1, top), (-1, bot)):
            P.cyl(f"node:t-{n}|M-ZINC", (x, -DF + 8, sz * HOUSE_H / 2), (x, -DF + 8, sz * (HOUSE_H / 2 + 1.2)), 2.2)
            P.pivot(f"t-{n}", "port", (x, -DF + 8, sz * (HOUSE_H / 2 + 1.2)), axis=(0, 0, sz), range=(0, 0), unit="screw", gender="none")
    # ---------------- front aux block: shell, slide following the carrier, 53-54 N.O., 61-62 N.C.
    if aux:
        aw, ah, ad = AUX; x0 = (W - aw) / 2; y0 = -DF
        F = "node:front-block|M-GREY-PA"
        P.box(F, x0, y0 - ad, -ah / 2, aw, WALL, ah)                                                     # block face
        P.box(F, x0 + aw - WALL, y0 - ad + WALL, -ah / 2, WALL, ad - WALL, ah)                           # +x wall
        if not cut: P.box(F, x0, y0 - ad + WALL, -ah / 2, WALL, ad - WALL, ah)
        for sz in (1, -1): P.box(F, x0, y0 - ad + WALL, (ah / 2 - WALL) if sz > 0 else -ah / 2, aw, ad - WALL, WALL)
        P.pivot("front-block", "fixed", (x0, y0, -ah / 2))
        FS = "node:fb-slide|M-WHITE-PA"
        P.box(FS, W / 2 - 8, y0 - 30 + s, -10, 16, 32, 20)                                               # slide, through the face window onto the stem (1.2)
        # 1.3 (MOT-020): the slide's yoke meets both block bridges at z -3..3, clear of the strips (|z| >= 5): a stem, a bar on the
        # N.C. bridge's -y face (it lifts 61-62 off its strips) and a post on the N.O. bridge's +y face (its spring presses 53-54 onto
        # it). Design sizes, Assumption (C), internal mechanism
        P.box(FS, W / 2 - 2, y0 - 33 + s, -3, 4, 3, 6)                                                   # stem, y -124 ... -121
        P.box(FS, 8.0, y0 - 34 + s, -3, 27.8, 1.0, 6)                                                    # bar, y -125 ... -124, x 8 ... 35.8
        P.box(FS, W - 11.0, y0 - 36.5 + s, -3, 2.0, 2.5, 6)                                              # post to 53-54, y -127.5 ... -125
        P.pivot("fb-slide", "translate", (W / 2, y0 - 30, 0), axis=(0, 1, 0), range=(0, STROKE))
        for name, x, no in (("fb-53", W - 10.0, True), ("fb-61", 10.0, False)):
            for sz in (1, -1): P.box("M-CU", x - 2, y0 - 34.5, min(sz * 5.0, sz * (ah / 2 - WALL)), 4, 1.5, abs(ah / 2 - WALL - 5.0))   # 1.3: seated on the block wall (GEO-070)
            yb = (y0 - 34.5 - GAP - 1.5) if no else (y0 - 33.0)
            P.box(f"node:{name}|M-CU", x - 2, yb + s, -7.0, 4, 1.5, 14.0); P.pivot(name, "translate", (x, yb, 0), axis=(0, 1, 0), range=(0, STROKE))
            for sz, n in ((1, "53" if no else "61"), (-1, "54" if no else "62")):
                P.cyl(f"node:t-{n}|M-ZINC", (x, y0 - ad + 8, sz * ah / 2), (x, y0 - ad + 8, sz * (ah / 2 + 1.2)), 2.0)
                P.pivot(f"t-{n}", "port", (x, y0 - ad + 8, sz * (ah / 2 + 1.2)), axis=(0, 0, sz), range=(0, 0), unit="screw", gender="none")
    P.collider("env", 0, -(DF + (AUX[2] if aux else 0)), -H / 2, W, D + (AUX[2] if aux else 0), H)
    return P

PREVIEWS = [dict(name="product three-quarter with aux block", az=250, el=20),
            dict(name="cutaway released: core, coil, armature, carrier, bridges open, aux N.C. closed", az=205, el=18, params=dict(view="cutaway")),
            dict(name="operated cutaway energised: armature on the core, bridges on the fixed contacts, springs compressed", az=205, el=18, params=dict(view="cutaway", operated=True)),
            dict(name="side cutaway released from -x", az=180, el=0, params=dict(view="cutaway", aux=False)),
            dict(name="sideop cutaway operated from -x", az=180, el=0, params=dict(view="cutaway", aux=False, operated=True)),
            dict(name="rear rail clip and main terminals", az=60, el=25)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
