#!/usr/bin/env python3
"""tensioner-belt: generic spring-activated belt tensioner, our own vendor-neutral design of the ETIM 10.0 class EC010722
(Spring-activated belt tensioner), built unattended (OPERATING.md 12, generic elements). A swing-arm tensioner: a base flange with
2 x M8 holes and a spring housing Ø50 on it; an arm (node `arm`) on a journal on the housing's axis carries a flat idler roll
Ø40 x 25 on its free end (2.0: node `roll`, a child of `arm` through P.parents, spinning on its axle; request mech-6 item 2), and a
torsion spring in the housing (not drawn) swings it against the belt. The arm swings 30° from its
free stop, so the roll's axis travels 30 (the tension travel). The roll's flat running face is a design choice, not a belt
profile. Holes: ISO 273 medium (lib/standards/holes.csv). The class values (spec.md, "Class values") are design inputs; every size
below is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "tensioner-belt", "2.0", "device"
TITLE = "belt tensioner, generic, spring-activated swing arm, flat roll Ø40 x 25, travel 30, 250 N, base 2 x M8"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic spring-activated belt tensioner (ETIM 10.0 EC010722); class values are design inputs (spec.md); "
            "base holes M8 to ISO 273 medium; the roll's flat running face a design choice; every size a design choice; no vendor file opened")
ORIGIN = ("the mounting face (the base flange's underside) z = 0, the arm's pivot axis (the housing's axis) at x = 0, y = 0 along +z; "
          "at the free stop the arm reaches toward +x, the roll's axis at x = 58; the belt pushes the arm round toward +y")
COMMAND = "BELTTENS"
PARAMS = dict()
FLANGE_X, FLANGE_Y, FLANGE_T = 90.0, 50.0, 6.0   # base flange 90 x 50 x 6, centred on the pivot axis: design choice
HOLE_X = 35.0                                     # 2 x M8 at x = +-35, y = 0 (70 apart): design choice
M8_D = 9.0                                        # M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
HOUSING_R, HOUSING_TOP = 25.0, 36.0               # spring housing Ø50 from the flange up to z 36 (the spring inside not drawn): design choice
JOURNAL_R, BORE_R = 8.0, 8.2                      # journal Ø16 in the arm hub's Ø16.4 bore (features.csv): design choice
CAP_R, CAP_T = 12.0, 2.0                          # retaining cap Ø24 x 2 on the journal, 0.5 above the hub: design choice
GAP = 0.5                                         # running clearance under and over the hub: design choice
HUB_R, HUB_TOP = 16.0, 48.0                       # arm hub Ø32, z 36.5 to 48: design choice
ARM_W, ARM_BOT, ARM_TOP = 20.0, 38.0, 47.5       # arm bar 20 wide, z 38 to 47.5 (0.5 under the hub's top): design choice
ARM_L = 58.0                                      # pivot axis to the roll's axis: design choice (30° of swing gives 2 x 58 x sin 15° = 30.0 of travel)
BOSS_R = 10.0                                     # the arm's round end Ø20 round the roll's axle: design choice
AXLE_R, AXLE_TOP = 6.0, 76.0                      # roll axle Ø12 from the arm's top up to z 76: design choice
ROLL_R, ROLL_Z = 20.0, (49.0, 74.0)               # class value roll width 25 (z 49 to 74); roll Ø40, 1.5 above the arm: design choice
ROLL_BORE_R = 6.2                                 # 2.0: the roll's Ø12.4 bore on the Ø12 axle, 0.2 radial (features.csv): design choice
SWING = 30.0                                      # the arm's swing from the free stop to the end stop (tension travel 30 at the roll's axis)

def build():
    P = Prims(); A_, Z, R = "M-ALU-ANOD", "M-ZINC", "M-BLACK-PA"
    flange = P.box(A_, -FLANGE_X / 2, -FLANGE_Y / 2, 0, FLANGE_X, FLANGE_Y, FLANGE_T)                    # base flange
    for sx in (-1, 1):
        x = sx * HOLE_X
        P.hole(A_, (x, 0, -1), (x, 0, FLANGE_T + 1), M8_D / 2, flange)                                    # 2 x M8 clearance
    P.cyl(A_, (0, 0, FLANGE_T), (0, 0, HOUSING_TOP), HOUSING_R)                                          # spring housing (spring not drawn)
    cap_z = HUB_TOP + GAP
    P.cyl(Z, (0, 0, HOUSING_TOP), (0, 0, cap_z), JOURNAL_R)                                              # journal on the housing's axis
    P.cyl(Z, (0, 0, cap_z), (0, 0, cap_z + CAP_T), CAP_R)                                                # retaining cap
    N = lambda m: f"node:arm|{m}"                                                                        # the arm: hub, bar, axle, roll
    hub = P.cyl(N(Z), (0, 0, HOUSING_TOP + GAP), (0, 0, HUB_TOP), HUB_R)
    P.hole(Z, (0, 0, HOUSING_TOP), (0, 0, HUB_TOP + 1), BORE_R, hub)                                     # the hub's bore on the journal
    P.box(N(Z), HUB_R - 4.0, -ARM_W / 2, ARM_BOT, ARM_L - HUB_R + 4.0, ARM_W, ARM_TOP - ARM_BOT)          # arm bar, from inside the hub
    P.cyl(N(Z), (ARM_L, 0, ARM_BOT), (ARM_L, 0, ARM_TOP), BOSS_R)                                        # the arm's round end
    P.cyl(N(Z), (ARM_L, 0, ARM_TOP), (ARM_L, 0, AXLE_TOP), AXLE_R)                                       # roll axle
    roll = P.cyl(f"node:roll|{R}", (ARM_L, 0, ROLL_Z[0]), (ARM_L, 0, ROLL_Z[1]), ROLL_R)                  # idler roll, flat running face (2.0: its own node)
    P.hole(R, (ARM_L, 0, ROLL_Z[0] - 1), (ARM_L, 0, ROLL_Z[1] + 1), ROLL_BORE_R, roll)                    # the roll's bore on the axle
    P.pivot("arm", "rotate", (0, 0, HOUSING_TOP + GAP), axis=(0, 0, 1), range=(0, SWING), unit="deg")     # + : pushed back by the belt
    P.pivot("roll", "rotate", (ARM_L, 0, ROLL_Z[0]), axis=(0, 0, 1), range=(0, 360), unit="deg")         # spins on its axle (0 to 360: a spin)
    P.parents["roll"] = "arm"                                                                            # request mech-6 item 2: rides the arm, keeps its own pivot
    P.collider("body", -FLANGE_X / 2, -FLANGE_Y / 2, 0, FLANGE_X, FLANGE_Y, FLANGE_T)
    P.collider("housing", -HOUSING_R, -HOUSING_R, FLANGE_T, 2 * HOUSING_R, 2 * HOUSING_R, cap_z + CAP_T - FLANGE_T)
    P.collider("arm", -HUB_R, -HUB_R, HOUSING_TOP + GAP, ARM_L + BOSS_R + HUB_R, 2 * HUB_R, HUB_TOP - HOUSING_TOP - GAP)
    P.collider("idler", ARM_L - ROLL_R, -ROLL_R, ARM_TOP, 2 * ROLL_R, 2 * ROLL_R, AXLE_TOP - ARM_TOP)    # roll and axle (not named like the node)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="top", az=270, el=80)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
