#!/usr/bin/env python3
"""tslot-40: aluminium T-slot framing profile 40 x 40, our own design (OPERATING.md 12, own designs; lib/inventory.csv row "tslot-40",
own_design yes, "aluminium T-slot profile, 40 x 40", made_of tslot-nut, bracket-angle, screw-iso4762; 10 systems: gantry-xyz,
guarded-machine-door, machining-station, mechanisms-bench, pneumatic-pick-and-place, pneumatic-trainer, robot-cell,
rotary-index-table, servo-pick-and-place, vision-inspection-station). Request mech-13's answer (core watch 2026-11-12): no ETIM 10.0
class on file fits (T-slot profiles are one of ETIM's gaps), so an own design; profile, slot width and length are design choices.
A square anodised aluminium bar 40 x 40 with one T-slot along the whole length in each of its four faces and a plain centre bore
along its axis at M8's tapping (minor) diameter, so an end can be tapped M8 for an end fastening. Cut to length (the `length`
parameter; a parameter stays out of the id, OPERATING.md 6). The slot is this design's: the slot nut (tslot-nut 1.0, EC000096,
generic) and the inner-corner bracket (bracket-angle 1.2) read it by library.load; brackets, nuts and screws are the hosts' (placed later). The
section is drawn solid apart from the slots and the bore. Section properties are computed from the drawn section in `section()`
(a definition, not a rating). No load, stiffness or alloy claim. The folder's reference record (a catalogue rail,
references/source.txt) is not what this element is built from: no figure was taken from it and no vendor file was opened."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "tslot-40", "1.1", "rail"
TITLE = "T-slot framing profile 40 x 40, four T-slots 10 wide (undercut 15 x 6.5), centre bore at M8 tapping, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: aluminium T-slot framing profile 40 x 40 (no ETIM class on file fits, request mech-13); four T-slots "
            "and a centre bore at M8's minor diameter (derived, ISO 68-1 / ISO 965-1); section properties computed from the drawn "
            "section; every size a design choice; no load, stiffness or alloy claim; no vendor file opened")
ORIGIN = ("run start x = 0, the profile's centre line y = 0, the underside face z = 0; the run along +x, the section y +-20, "
          "z 0 to 40, the centre bore's axis at (y 0, z 20)")
COMMAND = "TSLOT40"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius for this profile (the rail class's 1.0 is too large for its 15 mm end-face edges, mech-r69 / r101);
                                             # the gate reads each primitive's radius (P.radii), set in build() (mech-r106)

S = 40.0                                     # the square section 40 x 40: design choice (the inventory row's size)
THROAT = 10.0                                # each slot's opening in the face: design choice (an M8 screw's shank passes it with 1 each side)
LIP = 4.0                                    # the lip, from the face to the undercut: design choice
UNDER_W, UNDER_H = 15.0, 6.5                 # the undercut 15 wide x 6.5 high under the lips, 2.5 of lip each side for a slot nut to bear on: design choice
SLOT_DEPTH = LIP + UNDER_H                   # 10.5 from the face to the slot's floor
BORE_D = 6.6468                              # the centre bore, plain, at M8's minor diameter D1 (6H min): derived: derive.thread(8.0, 1.25) (ISO 68-1; ISO 965-1 clause 10)
MAT = "M-ALU-ANOD"                           # anodised aluminium (no alloy or temper is claimed)

C = S / 2.0                                  # 20: the face from the centre line
assert THROAT < UNDER_W and (UNDER_W - THROAT) / 2 >= 2.0                                        # the lips overhang the undercut 2.5 each side
assert C - SLOT_DEPTH > UNDER_W / 2 and math.hypot(C - SLOT_DEPTH - UNDER_W / 2, C - SLOT_DEPTH - UNDER_W / 2) >= 2.5   # neighbouring undercuts keep 2.8 of web between their corners
assert C - SLOT_DEPTH - BORE_D / 2 >= 5.0                                                         # 6.2 of core round the bore
assert (S - THROAT) / 2 >= 8.0 and LIP >= 3.0                                                     # the face's end edges 15 long (over the gate's 3 to 7 mm trap); the lips 4 thick


def cuts():
    """the material removed from the 40 x 40 square, as exact non-overlapping rectangles (yc, zc, dy, dz) about the section's centre:
    per face the throat (from the face to the undercut) and the undercut"""
    r = []
    for s in (-1, 1):
        r.append((0.0, s * (C - LIP / 2), THROAT, LIP)); r.append((0.0, s * (C - LIP - UNDER_H / 2), UNDER_W, UNDER_H))     # z faces
        r.append((s * (C - LIP / 2), 0.0, LIP, THROAT)); r.append((s * (C - LIP - UNDER_H / 2), 0.0, UNDER_H, UNDER_W))     # y faces
    return r


def section():
    """area (mm²), Iy = Iz (mm⁴, about the centre's axes; the section is symmetric under a quarter turn) and W (mm³, I over the
    farthest fibre, 20): the square less the slots and the bore, by the parallel-axis theorem (a definition, not a standard's table)"""
    R = cuts(); rb = BORE_D / 2
    A = S * S - sum(dy * dz for _, _, dy, dz in R) - math.pi * rb ** 2
    Iy = S ** 4 / 12 - sum(dy * dz ** 3 / 12 + dy * dz * zc ** 2 for _, zc, dy, dz in R) - math.pi * rb ** 4 / 4
    Iz = S ** 4 / 12 - sum(dz * dy ** 3 / 12 + dy * dz * yc ** 2 for yc, _, dy, dz in R) - math.pi * rb ** 4 / 4
    return dict(area=A, Iy=Iy, Iz=Iz, W=Iy / C)


_S = section()
assert abs(_S["area"] - 1015.30) < 0.01, _S                                         # by hand (spec.md Section): 1600 - 4 x 137.5 - 34.70
assert abs(_S["Iy"] - 150501.7) < 1 and abs(_S["Iz"] - _S["Iy"]) < 1e-6, _S          # by hand: 213 333.3 - 58 412.9 - 4 322.9 - 95.8 = 15.05 cm⁴
assert abs(_S["W"] - 7525.1) < 0.1, _S                                               # by hand: 7.53 cm³


def build(length=1000.0):
    P = Prims(); L = float(length)
    bar = P.box(MAT, 0.0, -C, 0.0, L, S, S)                                           # the 40 x 40 bar, x 0 to L
    zc = C                                                                            # the centre line's height
    for s in (-1, 1):
        zf = zc + s * C                                                               # the top (z 40) or the underside (z 0)
        z_ut = zf - s * SLOT_DEPTH                                                    # the slot's floor
        P.cutbox(MAT, -1.0, -UNDER_W / 2, min(z_ut, z_ut + s * UNDER_H), L + 2.0, UNDER_W, UNDER_H, bar)                       # undercut
        P.cutbox(MAT, -1.0, -THROAT / 2, min(z_ut, zf + s * 1.0), L + 2.0, THROAT, SLOT_DEPTH + 1.0, bar)                     # throat, from the floor out through the face
        yf = s * C                                                                    # the +y or -y face
        y_ut = yf - s * SLOT_DEPTH
        P.cutbox(MAT, -1.0, min(y_ut, y_ut + s * UNDER_H), zc - UNDER_W / 2, L + 2.0, UNDER_H, UNDER_W, bar)                  # undercut
        P.cutbox(MAT, -1.0, min(y_ut, yf + s * 1.0), zc - THROAT / 2, L + 2.0, SLOT_DEPTH + 1.0, THROAT, bar)                 # throat
    P.hole(MAT, (-1.0, 0.0, zc), (L + 1.0, 0.0, zc), BORE_D / 2, bar)                 # the centre bore, through, plain at M8's D1
    for i in range(len(P)): P.radii[i] = FILLET_R                                     # the gate fillets at each primitive's radius
    P.collider("profile", 0.0, -C, 0.0, L, S, S)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=180, el=10, center=(0, 0, 20), height=80)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
