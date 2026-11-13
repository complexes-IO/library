#!/usr/bin/env python3
"""jack-screw: generic screw jack (a workpiece support set under a part on a machine table and wound up to meet it), our own
vendor-neutral design of the ETIM 10.0 class EC003406 (Bolt block), built unattended (OPERATING.md 12, generic elements; `python
lib/build.py inventory mech` lists the class once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md). A round cast base (the class's outer diameter) with a bore, and one moving node `screw`: the screw, its collar
with two spanner flats (the class's wrench width) whose top face is the bearing face, and the plug-in peg on top that takes a pad or
a prism head. The screw winds up and down in the base: node `screw` translates +z (the class's height range). The screw's thread and
the base's nut thread are internal mechanism, drawn plain and not claimed. It stands loose on the table: no fixing hole. The class
values (spec.md, "Class values") are design inputs; every size below is a design choice. No load bearing capacity is designed or
claimed. No vendor file opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "jack-screw", "1.1", "device"
TITLE = "screw jack, generic, base Ø50, bearing face 80 to 110, wrench width 24, plug-in peg Ø10"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic bolt block (ETIM 10.0 EC003406), a screw jack; class values are design inputs (spec.md); "
            "the screw's thread and the base's nut thread not drawn or claimed; every size a design choice; no load bearing "
            "capacity claimed; no vendor file opened")
ORIGIN = ("the base's underside (the seat on the machine table) z = 0 on the screw's axis (x = y = 0); the screw winds up along +z; "
          "the bearing face (the collar's top) at z = 80 at rest, 110 at the end of the travel")
COMMAND = "JACKSCRW"
PARAMS = dict()

BASE_D, BASE_H = 50.0, 55.0          # base Ø50 (class value outer diameter) x 55 high, z 0..55: design choice
SCREW_D, SCREW_Z0 = 16.0, 8.0        # screw Ø16 drawn plain, its foot at z 8 at rest: design choice
BORE_D, BORE_Z0 = 18.0, 6.0          # the base's bore Ø18 from z 6 up through the top: 1 clear of the screw each side, 2 under its foot
COL_D, COL_Z0, COL_Z1 = 30.0, 56.0, 80.0   # collar Ø30, z 56..80 at rest (1 above the base's top); its top is the bearing face
WW = 24.0                            # wrench width: two flats 24 apart across y (class value): design choice
PEG_D, PEG_H = 10.0, 12.0            # plug-in peg Ø10 x 12 on the bearing face (class value diameter of plug-in peg): design choice
TRAVEL = 30.0                        # node `screw` translates +z 0..30: bearing face 80..110 (class value height)
CAST, STEEL = "M-CAST-BLUE", "M-SILVER"

assert (BORE_D - SCREW_D) / 2 >= 1.0 and SCREW_Z0 - BORE_Z0 >= 2.0          # the screw never touches the bore's wall or floor
assert COL_Z0 - BASE_H >= 1.0                                                 # the collar 1 above the base at rest, rising away from it
assert BASE_H - (SCREW_Z0 + TRAVEL) >= 15.0                                   # at the top of the travel 17 of the screw is still in the base
assert WW < COL_D and WW / 2 < BASE_D / 2 and COL_D / 2 < BASE_D / 2          # the flats cut the collar; the base keeps the x / y extremes


def build():
    P = Prims()
    base = P.cyl(CAST, (0, 0, 0), (0, 0, BASE_H), BASE_D / 2)                                           # base
    P.hole(CAST, (0, 0, BORE_Z0), (0, 0, BASE_H + 1), BORE_D / 2, base)                                 # its bore for the screw
    S = lambda m: f"node:screw|{m}"
    P.cyl(S(STEEL), (0, 0, SCREW_Z0), (0, 0, COL_Z0 + 1), SCREW_D / 2)                                  # screw (thread not drawn)
    col = P.cyl(S(STEEL), (0, 0, COL_Z0), (0, 0, COL_Z1), COL_D / 2)                                    # collar, the bearing face on top
    for sy in (-1, 1):                                                                                  # two spanner flats, 24 apart
        y0 = WW / 2 if sy > 0 else -WW / 2 - 10.0
        P.cutbox(S(STEEL), -COL_D / 2 - 1, y0, COL_Z0 - 1, COL_D + 2, 10.0, COL_Z1 - COL_Z0 + 2, col)
    P.cyl(S(STEEL), (0, 0, COL_Z1), (0, 0, COL_Z1 + PEG_H), PEG_D / 2)                                  # plug-in peg
    P.pivot("screw", "translate", (0, 0, COL_Z1), axis=(0, 0, 1), range=(0, TRAVEL))
    P.collider("base", -BASE_D / 2, -BASE_D / 2, 0, BASE_D, BASE_D, BASE_H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=25), dict(name="side", az=270, el=5)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
