#!/usr/bin/env python3
"""tube-pneu: a straight length of polyurethane air tube, one inch OD, cut square at both ends. Generic (OPERATING.md 12, EM
2026-11-07): our own vendor-neutral design of ETIM 10.0 EC011348 "Plastic hose without inlay" (its synonyms: air hose, control air
hose); lib/inventory.csv row `tube-pneu`, own_design generic. The OD series is the contract's (toolkit/pneu.py D2: inch tube 5/32,
1/4 and 3/8 in, TUBES_IN, exact conversions of the size names); the OD is the only figure a push-in fitting grips (ISO 14743), so it
is the tube's interface. Each end is a male tube unit (`tube-<od>`) for PNE-001: `port-a` at the origin, `port-b` at the far end,
each a pivot on its end face, the axis along y. The bore is not cut: pneu.TUBE holds no inside diameter (its `id` is empty, never
guessed), so the tube is drawn solid to its OD until it is on file (spec.md Open figures, class B). The tube is straight: a routed
path waits for pneu.TUBE's minimum bend radius. The end nodes' length is a design choice (the part the twin binds to), not an
insertion depth (pneu.PUSHIN's depth is empty too)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, pneu
from toolkit.prims import Prims

ID, VERSION, CLASS = "tube-pneu", "1.2", "tube"
TITLE = "generic pneumatic tube, polyurethane, 1/4 in OD, straight 500 mm (bore not cut)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic plastic hose without inlay (ETIM 10.0 EC011348), a polyurethane air tube (inventory own_design "
            "generic); OD series from toolkit/pneu.py D2 (TUBES_IN, inch 5/32, 1/4, 3/8); ends male tube units for PNE-001 "
            "(ISO 14743 push-in); length and end nodes are design choices; bore not cut (pneu.TUBE id empty)")
ORIGIN = "the centre of the end face of `port-a` (y = 0) on the tube's axis; the tube along +y to `port-b` at y = length, z up"
COMMAND = "TUBE-PNEU"
PARAMS = dict(tube="1/4", length=500.0)

END_L = 10.0                                   # design choice: each end node's length along y (what the twin binds to; not an insertion depth)
LENGTH_MIN = 3 * END_L                         # design choice: the shortest cut length built (two end nodes and a body between them)
LENGTH_MAX = 30000.0                           # design choice: one coil's worth; longer runs are two tubes and a union
MAT = "M-BLUE"                                 # design choice: blue polyurethane (one colour for the whole run)

for _o in pneu.TUBES_IN: assert pneu.TUBES_IN[_o] >= 2.5 * 0.5        # every OD is thick enough for the gate's 0.5 fillet (fillet.py: 2.5 r)


def build(tube="1/4", length=500.0):
    if tube not in pneu.TUBES_IN: raise ValueError(f"tube {tube}: one of {', '.join(pneu.TUBES_IN)} (pneu.TUBES_IN, D2)")
    length = float(length)
    if not LENGTH_MIN <= length <= LENGTH_MAX: raise ValueError(f"length {length:g}: {LENGTH_MIN:g} to {LENGTH_MAX:g} mm")
    P = Prims(); r = pneu.TUBES_IN[tube] / 2.0; unit = f"tube-{tube}"
    P.cyl(f"node:port-a|{MAT}", (0, 0, 0), (0, END_L, 0), r)                      # end a, face to face with the body
    P.cyl(MAT, (0, END_L, 0), (0, length - END_L, 0), r)                          # the run between the ends
    P.cyl(f"node:port-b|{MAT}", (0, length - END_L, 0), (0, length, 0), r)        # end b
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=unit, gender="male")
    P.pivot("port-b", "port", (0, length, 0), axis=(0, 1, 0), range=(0, 0), unit=unit, gender="male")
    P.collider("env", -r, 0, -r, 2 * r, length, 2 * r)
    return P


PREVIEWS = [dict(name="three-quarter, tube 1/4 in x 500", az=250, el=25), dict(name="end a", az=200, el=10),
            dict(name="tube 5/32 in x 200", az=250, el=25, params=dict(tube="5/32", length=200.0)),
            dict(name="tube 3/8 in x 200", az=250, el=25, params=dict(tube="3/8", length=200.0))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
