#!/usr/bin/env python3
"""strut: slotted strut channel, our own vendor-neutral design of the ETIM 10.0 class EC000386 (Mounting rail/-profile), built
unattended (OPERATING.md 12, generic elements; lib/inventory.csv row "strut", own_design generic, etim EC000386; 1 system:
process-skid). A cold-formed steel C-channel 41 x 41, wall 2.5, the two top edges returned inward as lips (9.5 wide) that hook down
(10 deep) and leave a 22 opening for channel nuts; the back carries a row of slotted holes 13.5 x 28 on a 50 pitch for M12 bolts
(ISO 273 medium clearance) into the frame it mounts on. Cut to length (the `length` parameter; a parameter stays out of the id,
OPERATING.md 6). Section properties (the class's Iy, Iz, Wy, Wz) are computed from the drawn section in `section()`. No load
rating: no allowable stress is on file. The folder's reference record (an inch-sized catalogue channel, references/source.txt) is not
what this element is built from; every size below is a design choice. No vendor file was opened."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "strut", "1.0", "rail"
TITLE = "strut channel, generic, 41 x 41 x 2.5 C-profile with inturned lips, 22 opening, slotted back 13.5 x 28 at 50, cut to length"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic mounting rail/-profile (ETIM 10.0 EC000386), a slotted strut channel 41 x 41 x 2.5 with inturned "
            "lips; class values are design inputs (spec.md); the back's slots at M12's ISO 273 medium clearance width; section properties "
            "computed from the drawn section; every size a design choice; no load or fire claim; no vendor file opened")
ORIGIN = ("run start x = 0, the channel's centre line y = 0, the back's outer face z = 0 (the mounting face, on the frame); the run "
          "along +x, the open side (the lips) up at z 41")
COMMAND = "STRUTCH"
PARAMS = dict(length=1000.0)
FILLET_R = 0.5                               # the gate's radius: a 2.5 cold-formed section with 9.5 lips and 10 returns (r 1.0, the rail class's default, reads 10 mm edges short, mech-r69)

W, H, T = 41.0, 41.0, 2.5                    # outside width (y), outside height (z), wall: design choices (a metric channel of the 41 class)
OPEN = 22.0                                  # the opening between the lips (the class's "slit width"): design choice
LIP = (W - OPEN) / 2.0                       # 9.5: each lip, from the outer face inward, at the top
RET = 10.0                                   # each lip's return, hooking down from its inner edge: design choice (10, over the gate's 3 to 7 mm free-corner trap at r 0.5)
SLOT_W, SLOT_L = 13.5, 28.0                  # the back's slots: 13.5 wide (y), M12 clearance medium H13 (ISO 273, lib/standards/holes.csv), 28 long (x): design choice
SLOT_PITCH = 50.0                            # slot pitch along the run: design choice
IN = 0.5                                     # a part runs 0.5 into its neighbour (one solid joint, gripper 1.0's way)
MAT = "M-ZINC"                               # zinc-plated steel

assert OPEN + 2 * LIP == W and LIP >= 8.0 and RET >= 8.0 and T <= 3.0                   # lips and returns clear the fillet trap; the wall is "short" (skipped)
assert SLOT_W < W - 2 * T - 2 * 3.0 and SLOT_L < SLOT_PITCH - 10.0                      # 3 of back each side of a slot; 22 of back between slots
assert RET + T < H - T - 3.0                                                            # the returns end well above the back


def rects():
    """the section's rectangles in the y-z plane (y0, z0, dy, dz), exact (no overlap): web, two walls, two lips, two returns"""
    r = [(-(W / 2 - T), 0.0, W - 2 * T, T)]                                             # web (the back) between the walls
    for s in (-1, 1):
        yo = s * W / 2
        r.append((min(yo, yo - s * T), 0.0, T, H))                                      # wall, full height
        yl = min(yo - s * T, yo - s * LIP); r.append((yl, H - T, LIP - T, T))           # lip, inward at the top, from the wall's inner face
        yr = min(yo - s * (LIP - T), yo - s * LIP); r.append((yr, H - T - RET, T, RET))  # return, down from the lip's inner edge
    return r


def section():
    """area (mm²), centroid height zc (mm), Iy and Iz (mm⁴) about the centroid's axes (Iy: the axis parallel to the back, y; Iz: the
    axis of symmetry, z), Wy and Wz (mm³, I over the farthest fibre): the second moment of area of the drawn section, by the
    parallel-axis theorem over its rectangles (a definition, not a standard's table)"""
    R = rects(); A = sum(dy * dz for _, _, dy, dz in R)
    zc = sum(dy * dz * (z0 + dz / 2) for _, z0, dy, dz in R) / A
    Iy = sum(dy * dz ** 3 / 12 + dy * dz * (z0 + dz / 2 - zc) ** 2 for _, z0, dy, dz in R)
    Iz = sum(dz * dy ** 3 / 12 + dy * dz * (y0 + dy / 2) ** 2 for y0, _, dy, dz in R)
    Wy = Iy / max(zc, H - zc); Wz = Iz / (W / 2)
    return dict(area=A, zc=zc, Iy=Iy, Iz=Iz, Wy=Wy, Wz=Wz)


_S = section()
assert abs(_S["area"] - 380.0) < 0.01 and abs(_S["zc"] - 19.4243) < 0.001          # by hand (spec.md Class values 12 to 15): 41² − the cavity 1301
assert abs(_S["Iy"] - 83530) < 5 and abs(_S["Iz"] - 100823) < 5, _S                   # by hand: 8.35 and 10.08 cm⁴
assert abs(_S["Wy"] - 3871) < 2 and abs(_S["Wz"] - 4918) < 2, _S                      # by hand: 3.87 and 4.92 cm³


def build(length=1000.0):
    P = Prims(); L = float(length)
    web = P.box(MAT, 0, -(W / 2 - T) - IN, 0, L, W - 2 * T + 2 * IN, T)                # the back, 0.5 into each wall
    rows = int((L - SLOT_PITCH) // SLOT_PITCH) + 1 if L >= SLOT_PITCH else 0
    x0 = (L - (rows - 1) * SLOT_PITCH) / 2 if rows else 0.0                              # the slots centred on the length (cable-tray's way)
    for k in range(rows):
        cx = x0 + k * SLOT_PITCH
        P.cutbox(MAT, cx - SLOT_L / 2, -SLOT_W / 2, -1.0, SLOT_L, SLOT_W, T + 2.0, web)  # slotted hole through the back, square ends
    for s in (-1, 1):
        yo = s * W / 2
        P.box(MAT, 0, min(yo, yo - s * T), 0, L, T, H)                                   # wall
        yl = min(yo, yo - s * LIP)
        P.box(MAT, 0, yl, H - T, L, LIP, T)                                              # lip, inward at the top (into the wall's top: one solid)
        yr = min(yo - s * (LIP - T), yo - s * LIP)
        P.box(MAT, 0, yr, H - T - RET, L, T, RET + IN)                                   # return, 0.5 into the lip
    P.collider("body", 0, -W / 2, 0, L, W, H)
    return P


PREVIEWS = [dict(name="three-quarter", az=230, el=30), dict(name="section", az=270, el=15, center=(0, 0, 20), height=120)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
