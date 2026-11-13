#!/usr/bin/env python3
"""tensioner-chain: generic spring-activated chain tensioner, our own vendor-neutral design of the ETIM 10.0 class EC010720
(Spring-activated chain tensioner), built unattended (OPERATING.md 12, generic elements). A linear tensioner: a base flange with
2 x M8 holes and a spring housing Ø32 on it; a plunger Ø20 (node `head`) slides in the housing's bore and carries a flat slide
shoe 60 x 24 that a compression spring inside (not drawn) presses up against the chain. The head presses in 25 (the tension
travel). The shoe's flat running face is a design choice, not a sprocket or a chain profile. The chain it is designed for, 08B-1
(a class value), is ISO 606's: the chain's own figures are NOT ON FILE (B), so the shoe's width is a design size. Holes: ISO 273
medium (lib/standards/holes.csv). The class values (spec.md, "Class values") are design inputs; every size below is a design
choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "tensioner-chain", "1.0", "device"
TITLE = "chain tensioner, generic, spring-activated linear, slide shoe 60 x 24, travel 25, 200 N, simplex 08B, base 2 x M8"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic spring-activated chain tensioner (ETIM 10.0 EC010720); class values are design inputs (spec.md); "
            "base holes M8 to ISO 273 medium; the shoe's flat running face a design choice; the 08B-1 chain's figures (ISO 606) "
            "NOT ON FILE (B); every size a design choice; no vendor file opened")
ORIGIN = ("the mounting face (the base flange's underside) z = 0, the plunger's axis (the centre of the two-hole pattern) at x = 0, "
          "y = 0; the head toward +z, the chain running along x across the shoe's top face")
COMMAND = "CHAINTENS"
PARAMS = dict()
BASE_X, BASE_Y, BASE_T = 76.0, 32.0, 6.0         # base flange 76 x 32 x 6, centred on the plunger's axis: design choice
HOLE_X = 28.0                                    # 2 x M8 at x = +-28, y = 0 (56 apart): design choice
M8_D = 9.0                                       # M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv)
HOUSING_R, HOUSING_TOP = 16.0, 56.0              # spring housing Ø32 from the flange up to z 56 (the spring inside not drawn): design choice
BORE_R, BORE_BOT = 10.2, 16.0                    # the plunger's bore Ø20.4 from the housing's top down to z 16 (features.csv): design choice
PLUNGER_R = 10.0                                 # plunger Ø20, 0.2 radial clearance in its bore: design choice
PLUNGER_Z = (46.0, 82.0)                         # plunger z 46 to 82 at the free stop: 10 in the bore, 26 out; design choice
SHOE_L, SHOE_W, SHOE_T = 60.0, 24.0, 12.0        # slide shoe 60 along the chain, 24 across, 12 thick, PE-UHMW: design choice. That 24 carries an
                                                 # 08B-1 chain's plates is a fit with ISO 606, NOT ON FILE (B)
TRAVEL = 25.0                                    # class value: tension travel, the head pressed in from the free stop to the end stop

def build():
    P = Prims(); Z, W = "M-ZINC", "M-WHITE-PA"
    base = P.box(Z, -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_T)                                 # base flange
    for sx in (-1, 1):
        x = sx * HOLE_X
        P.hole(Z, (x, 0, -1), (x, 0, BASE_T + 1), M8_D / 2, base)                                         # 2 x M8 clearance
    housing = P.cyl(Z, (0, 0, BASE_T), (0, 0, HOUSING_TOP), HOUSING_R)                                    # spring housing (spring not drawn)
    P.hole(Z, (0, 0, HOUSING_TOP + 1), (0, 0, BORE_BOT), BORE_R, housing)                                 # the plunger's bore
    N = lambda m: f"node:head|{m}"                                                                        # the head: plunger and shoe
    P.cyl(N(Z), (0, 0, PLUNGER_Z[0]), (0, 0, PLUNGER_Z[1]), PLUNGER_R)                                    # plunger
    top = PLUNGER_Z[1] + SHOE_T
    P.box(N(W), -SHOE_L / 2, -SHOE_W / 2, PLUNGER_Z[1], SHOE_L, SHOE_W, SHOE_T)                           # slide shoe, flat running face on top
    P.pivot("head", "translate", (0, 0, top), axis=(0, 0, -1), range=(0, TRAVEL))                         # + : pressed in by the chain
    P.collider("body", -BASE_X / 2, -BASE_Y / 2, 0, BASE_X, BASE_Y, BASE_T)
    P.collider("housing", -HOUSING_R, -HOUSING_R, BASE_T, 2 * HOUSING_R, 2 * HOUSING_R, HOUSING_TOP - BASE_T)
    P.collider("head", -SHOE_L / 2, -SHOE_W / 2, HOUSING_TOP, SHOE_L, SHOE_W, top - HOUSING_TOP)
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
