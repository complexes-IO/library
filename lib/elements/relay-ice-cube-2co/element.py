#!/usr/bin/env python3
"""relay-ice-cube-2co: plug-in DPDT control relay, 24 V DC coil, 15 A, 8 blade pins, on its 35 mm DIN socket. The first element built
mechanism-first (ruling 2026-11-03): magnet system, return spring, actuator card, two changeover poles, pins, then the clear case
and the socket around them. Brief: references/interior.md, parts.csv, behaviour.md (the maker's datasheet and socket drawing, figures
cited there; maker and part numbers only in references/). Every proportion the brief marks NOT ON FILE is set here and listed as an
Assumption, with its class, in spec.md's Assumptions table.

Frame: rail device. The socket's back face sits on the rail crown y = 0, rail centreline z = 0, left face x = 0; everything toward -y.
The relay's base plane (pin root) is the socket's front face, y = -SOCKET_D; the relay's local frame has its base at y = 0 and its
case toward -y, centred on x = 0, z = 0, then shifted into place."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
from toolkit import library, din, sweep as SW
from toolkit.prims import Prims, transform

ID, VERSION, CLASS = "relay-ice-cube-2co", "1.8", "device"
TITLE = "plug-in control relay DPDT 15 A, 24 V DC coil, push-to-test, flag, LED, clear case, on its 8-pin DIN socket"
TOOLKIT = "1.3"
BASELINE = "8-pin DPDT plug-in relay and its 8-pin DIN socket, maker's datasheet (references/interior.md: relay specification p. 1, 3, 5, 7; socket drawing p. 1; STEP read-back of the pin field); open figures: spec.md Assumptions table, each with its class"
ORIGIN = "rail device: socket back face on the rail crown y = 0, rail centreline z = 0, socket left face x = 0, body toward -y"
COMMAND = "RELAY"
PARAMS = dict(view="product", socket=True, operated=False)

# ---- relay envelope and pin field (brief: STEP read-back; spec p. 5)
CW, CL, CH = 21.08, 27.94, 39.12             # case x, z, depth above the base
PIN_W, PIN_T, PIN_L = 4.75, 0.51, 7.4
COL = 5.71                                    # contact pin columns at x = +/-5.71
COIL_X = 6.86                                 # coil pins at x = +/-6.86
Z_COIL, Z_COM, Z_NO, Z_NC = 9.0, 4.3, 4.3 - 5.89, 4.3 - 5.89 - 4.70    # pin rows (rows 5.89 / 4.70 pitch: brief); coil row offset and the commons row's z: Assumption (B)
WALL = 0.8                                    # case wall: NOT ON FILE (Assumption (C))
BASE_T = 2.0                                  # base / pin carrier: NOT ON FILE (Assumption (C))
# ---- mechanism (all NOT ON FILE: Assumptions (C) from the usual clapper construction, sized to fit the envelope)
COIL_Z, COIL_R, CORE_R, BOB_R = 6.5, 4.6, 2.0, 5.4            # coil axis at x = 0, z = 6.5; winding, core, bobbin flange radii (1.1: inside the case)
COIL_Y0, COIL_Y1 = -17.0, -35.0                                # bobbin between these planes (axis along y)
YOKE_Z = 11.9                                                  # yoke plate above the coil, under the case's inner wall (13.17) (1.1: was 13.0, through it)
ARM_Y, ARM_T = -36.6, 1.0                                      # armature plate (released) just above the core face
PIV = (0.0, -36.6, 11.9)                                       # armature hinge on the yoke edge, axis x
TIP_Z = -5.0                                                   # armature tip, over the contacts
TRAVEL = 1.2                                                   # Assumption (B): the contact gap, on neither the relay specification nor the
                                                               # brief; it sets the ranges the twin drives (actuator, pole-1, pole-2), spec row 10
ARM_ANGLE = math.degrees(math.atan(TRAVEL / (PIV[2] - TIP_Z)))  # 4.06 deg (1.1 on); follows TRAVEL, spec rows 9 and 10
CORE_FACE = PIV[1] + math.sin(math.radians(ARM_ANGLE)) * (PIV[2] - (COIL_Z - CORE_R))   # 1.3: the core's pole face where the turned plate meets
                                                               # it at operate (its lower edge, z +4.5): y -36.08, 1.08 proud of the bobbin;
                                                               # released gap 0.52 over the core (Assumption (C), states table "at the core")
CARD_TAB = (4.6, 8.0, -11.3, -5.0)                             # 1.3: card tab in line with the test button, relay-centred x0, x1, z0, z1; its
                                                               # front 0.26 behind the button's inner face (Assumption (C), request elec-4)
FINGER_Y, FINGER_T = -14.8, 0.3                                # common finger height (released) and thickness
TIP_ANGLE = math.degrees(math.asin(TRAVEL / (Z_COM - TIP_Z)))  # 7.4 deg about the finger root; follows TRAVEL, spec rows 10 and 11
# ---- socket (drawing p. 1: 79.2 x 29.2 x 29.7, mounting centres 68.4; spec p. 1: 8 screw terminals 1.0 N-m)
SW_, SL, SOCKET_D = 29.2, 79.2, 29.7         # SL: Assumption (B): the drawing's 79.2 chosen over the STEP's 82.1, whose span is not read, spec row 4
LED_PROUD = 0.89                              # LED boss Ø1.78, 0.89 proud of the face (STEP read-back, interior.md:74): the frontmost figure on file
BTN_TRAVEL = 1.5                              # Assumption (B): test-button travel, not on the specification; the 0.26 recess + the card's 1.2 + 0.04
                                              # taken in the blades; it decides the manual test's reach (pose row "manual"), spec row 14
BTN_OPEN = (4.04, 8.15, -11.46, -7.34)        # push-to-test opening in the case face, relay-centred x / z (STEP read-back, interior.md)
LOCK_TRAVEL = 4.0                             # lock-down slider travel: NOT ON FILE (Assumption (C): its end reaches over half the button)
NIB = (0.84, 2.34, -10.4, -8.4)               # 1.5: the slider's nib, relay-centred x0, x1, z0, z1 at rest, on the slider's +x end; its back at the
                                              # pressed button's front (yf + 0.26 + BTN_TRAVEL), so the locked state holds the button in (request elec-6,
                                              # lib/motion.csv btn-test -> door-lock "requires"); Assumption (C), spec row 21
SLOT = (0.74, 4.04, -10.5, -8.3)              # 1.5: the nib's slot through the face, from 0.1 clear of the nib at rest into the button opening (x 4.04);
                                              # 0.1 clear in z; Assumption (C), spec row 21
FLAG_TRAVEL = 3.6                             # flag slide across its window for the card's 1.2: NOT ON FILE (Assumption (C): lever ratio 3, lib/motion.csv "ratio")

def _relay(view, operated):
    """the relay in its own frame: base plane y = 0, case toward -y, centred on x = z = 0"""
    P = Prims()
    th = ARM_ANGLE if operated else 0.0; tr = TRAVEL if operated else 0.0; ta = TIP_ANGLE if operated else 0.0
    fl = FLAG_TRAVEL if operated else 0.0                                                          # 1.2: the operated build shows the flag at operate (pose check)
    # pins (+y, into the socket): six contact blades 4.75 along x, two coil blades turned 90 deg
    for z in (Z_COM, Z_NO, Z_NC):
        for sx in (-1, 1): P.box("M-BRASS", sx * COL - PIN_W / 2, -0.1, z - PIN_T / 2, PIN_W, PIN_L + 0.1, PIN_T)       # roots inside the base (GEO-050)
    for sx in (-1, 1): P.box("M-BRASS", sx * COIL_X - PIN_T / 2, -0.1, Z_COIL - PIN_W / 2, PIN_T, PIN_L + 0.1, PIN_W)
    P.box("M-BLACK-PA", -CW / 2, -BASE_T, -CL / 2, CW, BASE_T, CL)                                   # base / pin carrier
    # ---- magnet system: core, bobbin, winding, yoke (fixed)
    P.cyl("M-STEEL-7035", (0, COIL_Y0 + 1, COIL_Z), (0, CORE_FACE, COIL_Z), CORE_R)                   # core (fe-si), pole face at CORE_FACE (1.3; 1.2: 0.4 proud of the bobbin)
    P.cyl("M-BLACK-PA", (0, COIL_Y0, COIL_Z), (0, COIL_Y0 - 0.8, COIL_Z), BOB_R)                     # bobbin flanges
    P.cyl("M-BLACK-PA", (0, COIL_Y1 + 0.8, COIL_Z), (0, COIL_Y1, COIL_Z), BOB_R)
    P.cyl("node:coil|M-CU", (0, COIL_Y0 - 0.8, COIL_Z), (0, COIL_Y1 + 0.8, COIL_Z), COIL_R)          # winding (the coil node)
    P.pivot("coil", "emissive", (0, (COIL_Y0 + COIL_Y1) / 2, COIL_Z), axis=(0, -1, 0), range=(0, 1))        # x-ray cue: the winding glows while energised
    P.box("M-STEEL-7035", -4.5, ARM_Y + ARM_T * 0, YOKE_Z, 9.0, COIL_Y0 + 1.0 - ARM_Y, 1.2)          # yoke: upright behind the coil
    P.box("M-STEEL-7035", -4.5, COIL_Y0 + 1.0, COIL_Z - 2.5, 9.0, 1.2, YOKE_Z + 1.2 - COIL_Z + 2.5)   # yoke: foot under the core
    # coil leads to pins 13 / 14 (copper, swept)
    for sx in (-1, 1):
        lead = [(sx * 2.0, COIL_Y0 - 0.8, COIL_Z + COIL_R - 0.3), (sx * 5.0, COIL_Y0 + 3, COIL_Z + 3.5), (sx * COIL_X, -BASE_T - 0.2, Z_COIL)]
        P.mesh("M-CU", SW.sweep(SW.resample(lead, 1.5), SW.circle_profile(0.25, 6)))
    # ---- armature (node): plate from behind the hinge to the tip, rotates about x at PIV
    A = Prims()
    A.box("node:armature|M-STEEL-7035", -4.5, ARM_Y - ARM_T, TIP_Z, 9.0, ARM_T, PIV[2] + 1.0 - TIP_Z)
    # (1.1) no separate hinge lip: the plate's top end bears on the yoke's front edge (the knife edge); a lip over the yoke has no room under the case
    R = _rot_x(th, PIV)
    P.extend(_apply(A, R)); P.pivot("armature", "rotate", PIV, axis=(1, 0, 0), range=(0, round(ARM_ANGLE, 2)))
    # ---- actuator card (node): from the armature tip down to the commons, with a foot over the return spring
    C = "node:actuator|M-WHITE-PA"
    P.box(C, -8.0, ARM_Y + tr, TIP_Z - 1.0, 16.0, 1.0, 2.0)                                           # top bar under the armature tip
    P.box(C, -1.0, ARM_Y + tr + 1.0, TIP_Z - 1.0, 2.0, (FINGER_Y - FINGER_T - 0.1) - (ARM_Y + 1.0), 2.0)   # stem
    P.box(C, -8.0, FINGER_Y - FINGER_T - 1.1 + tr, TIP_Z + 1.0, 16.0, 1.0, 2.5)                       # bearing bar on both commons
    P.box(C, -1.0, FINGER_Y - FINGER_T - 0.1 + tr, TIP_Z - 4.5, 2.0, 1.0, 3.5)                          # foot reaching the spring post
    tx0, tx1, tz0, tz1 = CARD_TAB
    P.box(C, tx0, ARM_Y + tr + 1.0, tz0, tx1 - tx0, 1.0, tz1 - tz0)                                   # 1.3: tab behind the test button (manual test), on the top bar's back face
    P.pivot("actuator", "translate", (0, ARM_Y + 1.0, TIP_Z), axis=(0, 1, 0), range=(0, TRAVEL))
    # ---- return spring (node, compresses with the actuator): helix around a post between the base and the card foot
    sp_top = FINGER_Y - FINGER_T + 0.9 + tr; sp_bot = -BASE_T
    turns = 6; pts = []
    for k in range(turns * 16 + 1):
        a = 2 * math.pi * k / 16; pts.append((1.4 * math.cos(a), sp_bot + (sp_top - sp_bot) * k / (turns * 16), TIP_Z - 3.5 + 1.4 * math.sin(a)))
    P.mesh("node:spring-return|M-ZINC", SW.sweep(pts, SW.circle_profile(0.22, 6)))
    P.pivot("spring-return", "compress", (0, sp_bot, TIP_Z - 3.5), axis=(0, -1, 0), range=(0, TRAVEL))
    # ---- two changeover poles: common blade (node, rotates at its root bend), fixed N.C. above the tip, fixed N.O. below
    for i, sx in enumerate((-1, 1)):
        x = sx * COL; pole = f"pole-{i + 1}"
        P.box("M-BRASS", x - 1.5, FINGER_Y, Z_COM - 0.15, 3.0, -FINGER_Y - BASE_T, 0.3)                  # common riser from pin 9 / 12
        F = Prims()
        F.box(f"node:{pole}|M-BRASS", x - 1.5, FINGER_Y - FINGER_T, TIP_Z - 1.0, 3.0, FINGER_T, Z_COM - TIP_Z + 1.0)   # finger toward the tip
        F.cyl(f"node:{pole}|M-SILVER", (x, FINGER_Y + 0.6, TIP_Z), (x, FINGER_Y - FINGER_T - 0.6, TIP_Z), 1.0)  # double-sided rivet
        P.extend(_apply(F, _rot_x(ta, (0, FINGER_Y, Z_COM))))
        P.pivot(pole, "rotate", (x, FINGER_Y, Z_COM), axis=(1, 0, 0), range=(0, round(TIP_ANGLE, 2)))
        nc_face = FINGER_Y - FINGER_T - 0.6                                                              # released: tip rivet touches N.C.
        P.box("M-BRASS", x - 1.2, nc_face - 0.6 - 0.5, Z_NC - 0.15, 2.4, -(nc_face - 0.6 - 0.5) - BASE_T, 0.3)   # N.C. post from pin 1 / 4
        P.box("M-BRASS", x - 1.2, nc_face - 0.6 - 0.5, min(Z_NC, TIP_Z) - 1.2, 2.4, 0.5, abs(TIP_Z - Z_NC) + 2.4)   # N.C. arm over the tip
        P.cyl("M-SILVER", (x, nc_face, TIP_Z), (x, nc_face - 0.6, TIP_Z), 1.0)                           # N.C. rivet (face at nc_face)
        no_face = FINGER_Y + 0.6 + TRAVEL                                                                # operated: tip rivet touches N.O.
        P.box("M-BRASS", x - 1.2, no_face + 0.6, Z_NO - 0.15, 2.4, -(no_face + 0.6) - BASE_T, 0.3)        # N.O. post from pin 5 / 8
        P.box("M-BRASS", x - 1.2, no_face + 0.6, TIP_Z - 1.2, 2.4, 0.5, Z_NO - TIP_Z + 1.35)              # N.O. arm under the tip
        P.cyl("M-SILVER", (x, no_face + 0.6, TIP_Z), (x, no_face, TIP_Z), 1.0)                           # N.O. rivet
    # ---- front face features: push-to-test button, lock-down door, flag window, LED
    yf = -CH                                                                                         # front face features from the STEP (interior.md, 1.1)
    bx0, bx1, bz0, bz1 = BTN_OPEN
    P.box("node:btn-test|M-ORANGE-PA", bx0 + 0.1, yf + 0.26, bz0 + 0.1, bx1 - bx0 - 0.2, 3.0, bz1 - bz0 - 0.2)   # 3.9 square, recessed 0.26, stem into the case
    P.pivot("btn-test", "translate", (0.5 * (bx0 + bx1), yf + 0.26, 0.5 * (bz0 + bz1)), axis=(0, 1, 0), range=(0, BTN_TRAVEL))   # BTN_TRAVEL: spec row 14
    nx0, nx1, nz0, nz1 = NIB
    P.box("node:door-lock|M-ORANGE-PA", nx0, yf, nz0, nx1 - nx0, 0.26 + BTN_TRAVEL, nz1 - nz0)        # 1.5: the nib, face to face on the slider's back,
                                                                                                     # through the slot to the pressed button's front (y -37.36);
                                                                                                     # first of the node's boxes: the part that holds the button
                                                                                                     # (toolkit/poses.py reads the node's first box)
    P.box("node:door-lock|M-ORANGE-PA", -9.98, yf - 0.5, -11.68, 12.32, 0.5, 4.57)                    # lock-down slider beside the button (STEP: no hinge)
    P.pivot("door-lock", "translate", (-9.98, yf - 0.5, -9.4), axis=(1, 0, 0), range=(0, LOCK_TRAVEL))
    P.box("node:flag|M-ORANGE-PA", 1.8 + fl, yf + WALL + 0.07, 7.1, 3.6, 0.5, 2.9)                    # flag behind its window (x 1.65 ... 9.02), slides along x with the card
    P.pivot("flag", "translate", (1.8, yf + WALL + 0.07, 7.1), axis=(1, 0, 0), range=(0, FLAG_TRAVEL))
    P.cyl("node:led-coil|M-LENS-RED", (-5.33, yf, 11.18), (-5.33, yf - LED_PROUD, 11.18), 0.89)      # the Ø1.78 boss, 0.89 proud, face to face on the case (1.4: GEO-070, 1.3
    P.pivot("led-coil", "emissive", (-5.33, yf, 11.18), axis=(0, -1, 0), range=(0, 1))               # floated 0.39 in front; din.led's 0.5 into the face is GEO-010 on a node)
                                                                                                     # colour Assumption (C): red, spec row 17
    # ---- case (product: clear, all walls; cutaway: front and +x walls removed so the mechanism shows)
    K = "M-CASE-CLEAR"; x0, x1, z0, z1 = -CW / 2, CW / 2, -CL / 2, CL / 2
    bx0, bx1, bz0, bz1 = BTN_OPEN; fz0, fz1 = z0 + WALL, z1 - WALL; fx0, fx1 = x0 + WALL, x1 - WALL
    sx0, sx1, sz0, sz1 = SLOT                                                                        # 1.5: the nib's slot, into the button opening
    walls = [("back", (x0, -CH, z1 - WALL, CW, CH - BASE_T, WALL)), ("frontz", (x0, -CH, z0, CW, CH - BASE_T, WALL)),
             ("xl", (x0, -CH, z0 + WALL, WALL, CH - BASE_T, CL - 2 * WALL)), ("xr", (x1 - WALL, -CH, z0 + WALL, WALL, CH - BASE_T, CL - 2 * WALL)),
             ("face", (fx0, -CH, fz0, sx0 - fx0, WALL, fz1 - fz0)), ("face", (bx1, -CH, fz0, fx1 - bx1, WALL, fz1 - fz0)),      # the face, with the
             ("face", (sx0, -CH, fz0, sx1 - sx0, WALL, sz0 - fz0)), ("face", (sx0, -CH, sz1, sx1 - sx0, WALL, fz1 - sz1)),      # nib's slot (1.5) and the
             ("face", (bx0, -CH, fz0, bx1 - bx0, WALL, bz0 - fz0)), ("face", (bx0, -CH, bz1, bx1 - bx0, WALL, fz1 - bz1))]      # test button's 4.1 square opening (1.1)
    keep = {"product": {"back", "frontz", "xl", "xr", "face"}, "cutaway": {"back", "xr"}}[view]          # cutaway: face, -x wall and bottom removed
    for name, b in walls:
        if name in keep: P.box(f"node:case|{K}", *b)
    P.pivot("case", "fixed", (0, -CH, 0))
    if view == "product": P.box("M-WHITE-PA", x0 + 1.0, -CH * 0.55, z1 + 0.02, CW - 2.0, 10.0, 0.1)        # I.D. tag on the back wall, outside (decal)
    return P

def _rot_x(deg, about):
    a = math.radians(deg); c, s = math.cos(a), math.sin(a); o = np.array(about, float)
    M = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    return lambda p: tuple(M @ (np.array(p, float) - o) + o)

def _apply(prims, f):
    """apply a point map to boxes (as oriented boxes) and cylinders"""
    out = Prims()
    for L, k, q in prims:
        if k == "box":
            x, y, z, dx, dy, dz = q; o = np.array(f((x, y, z))); ex = np.array(f((x + 1, y, z))) - o; ey = np.array(f((x, y + 1, z))) - o; ez = np.array(f((x, y, z + 1))) - o
            out.append((L, "obox", (tuple(o), tuple(ex), tuple(ey), tuple(ez), dx, dy, dz)))
        elif k == "cyl": out.append((L, "cyl", (f(q[0]), f(q[1]), q[2])))
        else: out.append((L, k, q))
    return out

def build(view="product", socket=True, operated=False):
    P = Prims(); xc = SW_ / 2 if socket else CW / 2; yb = -SOCKET_D if socket else 0.0
    R = _relay(view, operated); tp = transform(R, (xc, yb, 0), 0.0, None, 0); P.extend(tp); P.pivots.update(tp.pivots)
    if socket:
        S = "M-GREY-PA"
        P.box(S, 0, -SOCKET_D, -SL / 2 + 8, SW_, SOCKET_D, SL - 16)                                     # socket body
        for sz in (1, -1):                                                                              # terminal shoulders, 4 screws each end; Assumption (C): shoulders 8 long, body inset 8 per end, spec row 18
            P.box(S, 0, -SOCKET_D + 8, sz * (SL / 2 - 8) - (0 if sz > 0 else 8), SW_, SOCKET_D - 8, 8)
        din.rail_clip(P, 0, SW_)
        tmap = {1: ("t-13", "t-14", "t-9", "t-12"), -1: ("t-1", "t-4", "t-5", "t-8")}               # terminal ids = relay pin numbers (spec p. 5)
        for sz in (1, -1):
            for i, name in enumerate(tmap[sz]):
                cx = 4.0 + i * 7.07; cz = sz * (SL / 2 - 4)                                             # Assumption (B): 7.07 pitch, the first 4.0 from the left face, 4.0 in from each end; the drawing gives no pitch, spec row 3
                P.cyl(f"node:{name}|M-ZINC", (cx, -SOCKET_D + 8, cz), (cx, -SOCKET_D + 6.8, cz), 2.6)    # Assumption (C): screw head Ø5.2 × 1.2, appearance, spec row 18
                P.pivot(name, "port", (cx, -SOCKET_D + 6.8, cz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp (OPERATING.md 6)
                P.box("M-GASKET", cx - 2.2, -SOCKET_D + 11, sz * SL / 2 - (0.4 if sz > 0 else 0.1), 4.4, 8, 0.5)   # wire entry 0.1 proud (GEO-050); Assumption (C): 4.4 × 8 × 0.5, spec row 18
        for sz in (1, -1):                                                                              # holding clip (wire bail) at each end of the relay; Assumption (C): Ø1.0 bail, appearance, spec row 19
            P.mesh("M-ZINC", SW.sweep(SW.resample([(xc - 9, -SOCKET_D, sz * (CL / 2 + 1.5)), (xc - 9, -SOCKET_D - 24, sz * (CL / 2 + 0.6)), (xc + 9, -SOCKET_D - 24, sz * (CL / 2 + 0.6)), (xc + 9, -SOCKET_D, sz * (CL / 2 + 1.5))], 2.0), SW.circle_profile(0.5, 6)))
        P.collider("socket", 0, -SOCKET_D, -SL / 2, SW_, SOCKET_D + 7.5, SL)
    P.collider("relay", xc - CW / 2, yb - CH - LED_PROUD, -CL / 2, CW, CH + LED_PROUD, CL)          # 1.4: derived, the case to the LED boss's front (spec row 20)
    return P

PREVIEWS = [dict(name="product three-quarter on its socket", az=250, el=20),
            dict(name="cutaway released: coil, armature, card, spring, commons on N.C.", az=200, el=18, center=(10.5, -20, 1), height=46, params=dict(view="cutaway", socket=False)),
            dict(name="operated cutaway energised: armature on the core, commons on N.O.", az=200, el=18, center=(10.5, -20, 1), height=46, params=dict(view="cutaway", socket=False, operated=True)),
            dict(name="side cutaway released from -x: coil, armature hinge, card, spring, pole-1 on N.C.", az=180, el=0, center=(10.5, -19, 0), height=46, params=dict(view="cutaway", socket=False)),
            dict(name="contacts close-up released, pole-1 tip between N.C. (left) and N.O. (right)", az=180, el=0, center=(10.5, -15, -4), height=12, params=dict(view="cutaway", socket=False)),
            dict(name="contactsop close-up operated, tip on N.O.", az=180, el=0, center=(10.5, -15, -4), height=12, params=dict(view="cutaway", socket=False, operated=True)),
            dict(name="pins relay alone from the pin end: 6 contact blades, 2 coil blades turned 90 deg", az=80, el=25, params=dict(socket=False))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
