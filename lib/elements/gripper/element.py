#!/usr/bin/env python3
"""gripper: parallel pneumatic gripper, two jaws, our own vendor-neutral design of the ETIM 10.0 class EC004755 (Gripper
(pneumatic/hydraulic)), built unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "gripper", own_design generic,
"parallel gripper", etim EC004755, made_of fitting-pushin x2, prox-m12, screw-iso4762; 4 systems: cobot-bench, robot-cell,
robot-tending-cell, servo-pick-and-place). The end effector a robot or a pick-and-place axis carries: an anodised aluminium body
with a piston inside (not drawn: internal, class C) whose wedge hook drives two jaw carriers in a guide slot across the body's top,
in and out along x, opposed; each carrier ends in a finger block with two tapped M4 holes in its top face where the application's
fingers bolt on (2.0: moved from the gripping face, review gripper-1.0 finding 1, so fingers never stand in the gap the jaws close).
Two female NPT 1/8 air ports in bosses on the body's -y face (toolkit/pneu.py D1): `port-close` and `port-open`; air at port-close drives the
jaws in by the stroke, air at port-open drives them out (double acting). The body's underside is the mounting face, four tapped M6
holes (threads derived, ISO 68-1 / ISO 965-1) for socket head cap screws (ISO 4762, placed later) from the flange it hangs on. As
modelled the jaws stand open (the rest pose); closed each has moved 10 toward the centre and 2 stays between the fingers. The
class values (spec.md "Class values") are design inputs; the holding force is derived from the piston's area and the pressure.
The push-in fittings, the sensor and the screws (the inventory's made_of) are placed later; nothing is drawn for the sensor in
this version. Every size below is a design choice. No vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "gripper", "2.0", "actuator"
TITLE = "parallel pneumatic gripper, generic, 2 jaws, stroke 10 per jaw, body 64 x 40 x 80 with 2 x NPT 1/8 port bosses, 4 x M6 tapped mount"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic gripper (pneumatic/hydraulic) (ETIM 10.0 EC004755), a two-jaw parallel pneumatic gripper; class "
            "values are design inputs (spec.md); air ports NPT 1/8 female (toolkit/pneu.py D1, bores at ASME B1.20.1's calculated "
            "figures); tapped M6 mount and M4 finger holes at their derived minor diameters (ISO 68-1, ISO 965-1); the piston inside "
            "not drawn; every size a design choice; no load or safety claim; no vendor file opened")
ORIGIN = ("the mounting face plane (z = 0, the body's underside) at the body's centre; +z up through the body to the jaws, the "
          "jaws move along x (opposed), the air ports open toward -y")
COMMAND = "GRIPPERPAR"
PARAMS = dict()

BODY_X, BODY_Y, BODY_Z = 64.0, 40.0, 80.0    # the body: x +-32, y +-20, z 0..80 (design choices; the Ø20 piston runs inside along z, not drawn)
SLOT_W, SLOT_D = 20.0, 6.0                   # the guide slot across the body's top along x: y +-10, z 74..80, open at both ends (design choice)
STROKE = 10.0                                # travel of each jaw toward the centre (design choice): 20 between open and closed in all
CAR_X, CAR_Y, CAR_Z = 18.0, 19.0, 12.0       # each jaw carrier 18 (x) x 19 (y: 0.5 clear of each slot wall) x 12 (z 74..86: 6 in the slot, 6 above)
CAR_IN = 11.0                                # the carriers' inner faces at x +-11 open (+-1 closed: 2 stays between the fingers)
FIN_X, FIN_Z = 10.0, 20.0                    # each finger block 10 (x) x 19 (y) x 20 (z 86..106) on the carrier's inner end
IN = 0.5                                     # a finger runs 0.5 into its carrier (one solid joint, hold-down's way)
TAP6_D1, TAP6_DEPTH = 4.9175, 12.0           # 4 x M6 tapped mount holes at the thread's minor diameter D1 (6H min), 12 deep (2 d): derived: derive.thread(6.0, 1.0)
TAP6_X, TAP6_Y = 20.0, 12.0                  # the mount pattern 40 x 24 (x +-20, y +-12) in the underside (design choice)
TAP4_D1, TAP4_DEPTH = 3.2422, 6.0            # 2 x M4 tapped holes per finger at D1 (6H min), 6 deep (1.5 d): derived: derive.thread(4.0, 0.7)
TAP4_Y = (-4.5, 4.5)                         # the two M4 holes in each finger block's top face (z 106, along -z), at the block's centre in x and y +-4.5 (design choice: 9 pitch)
PORT = "NPT1/8"                              # both air ports (pneu.THREADS, D1): fitting-pushin 2.0's thread=NPT1/8 form screws in
PORT_X, PORT_Z = 16.0, 40.0                  # the ports on the -y face at x +-16, z 40 (design choice): clear of the slot above and the mount holes below
BOSS_D, BOSS_L = 18.0, 10.0                  # each port's boss, Ø18 x 10 standing on the -y face (its face at y -30), in the port's node (actuator-valve 1.0's way)
_T = pneu.NPT[PORT]["table"]
PORT_BORE = (_T["E1"] + _T["h"]) * 25.4      # 10.242: the male's major diameter at the hand-tight plane, drawn plain (tank 2.0's rule)
PORT_DEPTH = pneu.NPT[PORT]["length"] + 2.0  # L2 + 2 = 8.702: a run-out past the male's effective thread (actuator-valve 1.0's way)
PISTON_D, ROD_D, P_BAR = 20.0, 8.0, 6.0      # the piston Ø20 with a Ø8 rod, and 600 kPa, the class value's datum pressure (design choices): spec.md Class values 3
MAT_BODY, MAT_JAW = "M-ALU-ANOD", "M-SILVER"

assert PORT in pneu.THREADS and pneu.NPT[PORT]["length"]
assert PORT_DEPTH >= pneu.NPT[PORT]["engagement"] and PORT_DEPTH < BOSS_L + IN       # deeper than the make-up L1 + L3, blind inside its boss
assert BOSS_D >= _T["D"] * 25.4 + 2 * 3.0                                             # 3 of wall round the pipe OD at the boss (actuator-valve's rule)
assert PORT_Z - BOSS_D / 2 > TAP6_DEPTH + 3.0 and PORT_Z + BOSS_D / 2 < BODY_Z - SLOT_D - 3.0        # the bosses clear the mount holes and the slot
assert 2 * PORT_X - BOSS_D > 10.0 and PORT_X + BOSS_D / 2 < BODY_X / 2 - 5.0                        # 10 between the bosses, 5 of face to the sides
assert CAR_Y < SLOT_W and CAR_Z > SLOT_D and CAR_IN + CAR_X < BODY_X / 2 - 2.0                        # carriers clear the slot walls and stay 3 inside the body's sides
assert CAR_IN - STROKE >= 1.0 and FIN_X < CAR_X and TAP4_DEPTH < FIN_Z - 10.0                          # 2 between the blocks closed; the M4 holes keep 14 of finger block under them
assert FIN_X / 2 - TAP4_D1 / 2 >= 3.0 and CAR_Y / 2 - max(TAP4_Y) - TAP4_D1 / 2 >= 3.0                  # 3 of wall round each M4 hole in x and y
assert TAP6_X + TAP6_D1 / 2 < BODY_X / 2 - 5.0 and TAP6_Y + TAP6_D1 / 2 < BODY_Y / 2 - 5.0            # the mount holes keep 5 of wall


def piston_area(): return math.pi * PISTON_D ** 2 / 4.0


def force_n():
    """the piston's push on its full face at P_BAR, in N: p x A (1 bar = 0.1 N/mm²); derived: derive.cylinder(20, 8, 6) (F = p A)"""
    return P_BAR * 0.1 * piston_area()


def jaw_force_n():
    """holding force per jaw: the piston's push shared by the two jaws through a 45-degree wedge hook (tan 45 = 1), ideal, no friction"""
    return force_n() / 2.0


def jaw(P, sx):
    """one jaw (node jaw-l at sx = -1, jaw-r at sx = +1): the carrier in the slot, its finger block on the inner end, two tapped M4 holes
    in the finger block's top face; the pivot translates it toward the centre by the stroke"""
    name = "jaw-l" if sx < 0 else "jaw-r"; N = f"node:{name}|{MAT_JAW}"
    x_in = sx * CAR_IN                                                                                  # the inner face, x -11 or +11
    x0 = min(x_in, x_in + sx * CAR_X)                                                                   # the carrier's lower x
    P.box(N, x0, -CAR_Y / 2, BODY_Z - SLOT_D, CAR_X, CAR_Y, CAR_Z)                                      # carrier, on the slot's floor
    fx0 = min(x_in, x_in + sx * FIN_X)
    fin = P.box(N, fx0, -CAR_Y / 2, BODY_Z - SLOT_D + CAR_Z - IN, FIN_X, CAR_Y, FIN_Z + IN)            # finger block, 0.5 into the carrier
    top = BODY_Z - SLOT_D + CAR_Z + FIN_Z; xc = x_in + sx * FIN_X / 2                                  # the block's top face z 106 and centre x +-16
    for y in TAP4_Y:                                                                                   # tapped M4 from the top face, 6 deep
        P.hole(N, (xc, y, top + 1.0), (xc, y, top - TAP4_DEPTH), TAP4_D1 / 2, fin)
    P.pivot(name, "translate", (x_in + sx * CAR_X / 2, 0, BODY_Z - SLOT_D), axis=(-sx, 0, 0), range=(0, STROKE), unit="mm")
    P.collider(f"finger-{'l' if sx < 0 else 'r'}", x0, -CAR_Y / 2, BODY_Z - SLOT_D, CAR_X, CAR_Y, CAR_Z + FIN_Z)


def build():
    P = Prims(); hx, hy = BODY_X / 2, BODY_Y / 2
    body = P.box(MAT_BODY, -hx, -hy, 0.0, BODY_X, BODY_Y, BODY_Z)                                      # body
    P.cutbox(MAT_BODY, -hx - 1.0, -SLOT_W / 2, BODY_Z - SLOT_D, BODY_X + 2.0, SLOT_W, SLOT_D + 1.0, body)   # guide slot along x, open both ends
    for x in (-TAP6_X, TAP6_X):
        for y in (-TAP6_Y, TAP6_Y):
            P.hole(MAT_BODY, (x, y, -1.0), (x, y, TAP6_DEPTH), TAP6_D1 / 2, body)                      # tapped M6 mount holes from the underside
    for sx, name in ((-1, "port-close"), (1, "port-open")):
        yb = -hy - BOSS_L; c = (sx * PORT_X, yb, PORT_Z)
        boss = P.cyl(f"node:{name}|{MAT_BODY}", (c[0], -hy + IN, c[2]), (c[0], yb, c[2]), BOSS_D / 2)   # port boss, 0.5 into the body, its face at y -30
        P.hole(f"node:{name}|{MAT_BODY}", (c[0], yb - 1.0, c[2]), (c[0], yb + PORT_DEPTH, c[2]), PORT_BORE / 2, boss)   # female NPT 1/8, blind, plain at E1 + h
        P.pivot(name, "port", c, axis=(0, -1, 0), range=(0, 0), unit=PORT, gender="female", role="work")
    P.collider("housing", -hx, -hy, 0.0, BODY_X, BODY_Y, BODY_Z)                                     # not named like the fixed mesh node `body` (review 1.0 finding 2)
    for sx in (-1, 1): jaw(P, sx)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="ports", az=270, el=10), dict(name="jaws", az=0, el=60)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
