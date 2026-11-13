#!/usr/bin/env python3
"""enc-wm: generic wall-mount enclosure, our own vendor-neutral design of the ETIM 10.0 class EC000261 (Enclosure/cabinet (empty)),
built unattended (OPERATING.md 12, generic elements). Sheet steel 600 wide x 800 high x 250 deep, open at the front and closed by one
flat door hinged at its left edge (node `door`, rotates about the box's front-left vertical edge, 0 to 110 degrees outward; a host,
so door operators cut through it). Inside, a galvanised mounting plate 500 x 700 x 2.5 (node `back-panel`, fixed; a host) on four
welded standoffs with M8 studs through its corner holes. Two M20 cable-entry holes in the bottom (gland-m20 `CUTOUT`) and four M8
wall-fixing holes in the back (Ø9.0, ISO 273 medium; the four ISO 4762 screws its inventory row names are placed in a later
version, once screw-iso4762 is built). Three M8 earth studs as port nodes (1.3, lib/requests/core/mech-enc-wm-2026-11-11.md):
`pe-body` on the bottom's inner face beside the cable entries, `pe-door` on the door's inner face (a child of `door`, so it swings
with it), `pe-plate` on the mounting plate's front face (top-level: the plate is fixed); gender none (PIN-002); their torque waits for the welded
stud's property class (ISO 13918, not on file: spec.md "What it meets", behaviour.csv; 1.4). The parameter `swing` (degrees, 0 by default, 0 to SWING) builds the door turned open by that
angle, so an assembly can render and check the panel with its door open (as enc-fs-1524x1829x305's swing_l / swing_r); the default
build is unchanged. The class values (spec.md, "Class values") are design inputs; every size is a design choice. The studs' M8 thread
is derived (derive.thread, ISO 68-1 / ISO 965-1; spec.md, "What it meets"); they are modelled plain at the nominal Ø8.
No latch, seal, IP rating, load rating or safety claim. No vendor file was opened."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "enc-wm", "1.4", "enclosure"
TITLE = "wall-mount enclosure, generic, 600 x 800 x 250, one door, mounting plate, two M20 entries"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic wall-mount enclosure (ETIM 10.0 EC000261); class values are design inputs (spec.md); the M8 "
            "stud thread derived (ISO 68-1, ISO 965-1), modelled plain; every size a design choice; mates M20 glands (gland-m20), M8 wall-fixing screws "
            "(ISO 273); three M8 earth studs as port nodes pe-body, pe-door, pe-plate; no vendor file opened")
ORIGIN = ("the box's underside z = 0 at its front-left corner x = 0, y = 0; the door opens toward -y; the back face y = 250 goes "
          "against the wall")
COMMAND = "ENCWM"
PARAMS = dict(swing=0.0)                        # the door's angle in degrees, 0 (closed) to SWING: the build turns the door and what rides on it

W, H, D, T = 600.0, 800.0, 250.0, 2.0           # class values width, height, depth (outside, door not included); 2.0 sheet: design choice
DOOR_T = 2.0                                    # the door, a flat 2.0 plate over the box's front edges: design choice
SWING = 110.0                                   # the door opens 0 to 110 degrees outward about the front-left edge: design choice
GLAND_CUT = library.load("gland-m20").CUTOUT    # 20.5: gland-m20 1.3 (lib/standards/holes.csv M20 x 1.5 entry 20.2 to 20.7)
GLAND_XY = ((200.0, 100.0), (400.0, 100.0))     # two cable entries in the bottom, 200 pitch, centred on the width, 100 behind the
                                                # front (clear of the mounting plate's studs): design choice
FIX_D = 9.0                                     # M8 clearance, ISO 273 medium (H13), lib/standards/holes.csv
FIX_XZ = ((25.0, 25.0), (575.0, 25.0), (25.0, 775.0), (575.0, 775.0))   # wall-fixing holes 550 x 750 in the back: design choice
PLATE = (500.0, 700.0, 2.5)                     # mounting plate width (x), height (z), thickness (y): design choice
PLATE_X, PLATE_Z = (W - PLATE[0]) / 2, (H - PLATE[1]) / 2      # 50, 50: centred, 48 clear of the walls' inner faces
STANDOFF_D, STANDOFF_L = 16.0, 15.0             # welded standoffs Ø16 x 15 off the back's inner face: design choice
STUD_D, STUD_L = 8.0, 12.0                      # M8 studs, 12 beyond the plate's front face. The thread is derived (derive.thread(8.0, 1.25),
                                                # spec.md): modelled plain at the designation's nominal Ø8
STUD_INSET = 25.0                               # stud centres 25 in from the plate's edges (450 x 650): design choice
PE_D, PE_L = 8.0, 12.0                          # the three M8 earth studs (1.3), welded, plain at Ø8, 12 proud of their face; the same derived thread
PE_BODY = (100.0, 100.0)                        # pe-body: x, y on the bottom's inner face (z = T), 100 beside the first cable entry, up: design choice
PE_DOOR = (50.0, 700.0)                         # pe-door: x, z on the door's inner face (y = 0), 50 from the hinge edge and 100 below the top (the top hinge corner,
                                                # so its lead is short and clear of the operators a panel cuts lower down), into the box: design choice. Above the
                                                # door pivot's origin (z 400): the AutoCAD gate's glb reader places a nested node relative to its parent's origin
                                                # (request mech-12), so a stud below it would read outside the box's extents and fail the gate for no defect
PE_PLATE = (W / 2, PLATE_Z + STUD_INSET)        # pe-plate: x, z on the plate's front face (y 230.5), bottom edge centre, 25 up as the plate studs: design choice
MAT, PL, ZN = "M-STEEL-7035", "M-GALV", "M-ZINC"

def build(swing=0.0):
    swing = float(swing)
    if not 0.0 <= swing <= SWING: raise ValueError(f"swing {swing}: the door opens 0 to {SWING:g} degrees")
    P = Prims()
    b = P.box(MAT, 0, 0, 0, W, D, T)                                                    # bottom, the entries in it
    for x, y in GLAND_XY: P.hole(MAT, (x, y, -1.0), (x, y, T + 1.0), GLAND_CUT / 2, b)
    P.box(MAT, 0, 0, H - T, W, D, T)                                                    # top
    for x in (0.0, W - T): P.box(MAT, x, 0, T, T, D, H - 2 * T)                         # sides, between the bottom and the top
    back = P.box(MAT, T, D - T, T, W - 2 * T, T, H - 2 * T)                             # back, between the sides
    for x, z in FIX_XZ: P.hole(MAT, (x, D - T - 1.0, z), (x, D + 1.0, z), FIX_D / 2, back)
    P.collider("body", 0, 0, 0, W, D, H)
    px, py = PE_BODY                                                                    # pe-body: the body's bonding stud, up from the bottom's inner face
    P.cyl(f"node:pe-body|{ZN}", (px, py, T), (px, py, T + PE_L), PE_D / 2)
    P.pivot("pe-body", "port", (px, py, T + PE_L), axis=(0, 0, 1), range=(0, 0), unit="PE", gender="none")
    yb = D - T - STANDOFF_L                                                             # 233: the standoffs' front faces, the plate's back face
    Lp = f"node:back-panel|{PL}"
    plate = P.host("back-panel", P.box(Lp, PLATE_X, yb - PLATE[2], PLATE_Z, PLATE[0], PLATE[2], PLATE[1]), PLATE[2])
    for sx in (PLATE_X + STUD_INSET, PLATE_X + PLATE[0] - STUD_INSET):
        for sz in (PLATE_Z + STUD_INSET, PLATE_Z + PLATE[1] - STUD_INSET):
            P.hole(Lp, (sx, yb + 1.0, sz), (sx, yb - PLATE[2] - 1.0, sz), FIX_D / 2, plate)   # Ø9.0 over each stud (M8 clearance medium)
            P.cyl(ZN, (sx, D - T, sz), (sx, yb, sz), STANDOFF_D / 2)                     # standoff, welded to the back
            P.cyl(ZN, (sx, yb, sz), (sx, yb - PLATE[2] - STUD_L, sz), STUD_D / 2)        # M8 stud through the plate (plain at Ø8)
    P.pivot("back-panel", "fixed", (PLATE_X, yb - PLATE[2], PLATE_Z))
    P.collider("back-panel", PLATE_X, yb - PLATE[2], PLATE_Z, PLATE[0], PLATE[2], PLATE[1])
    qx, qz, yf = PE_PLATE[0], PE_PLATE[1], yb - PLATE[2]                                # pe-plate: the plate's bonding stud, out of its front face
    P.cyl(f"node:pe-plate|{ZN}", (qx, yf, qz), (qx, yf - PE_L, qz), PE_D / 2)
    P.pivot("pe-plate", "port", (qx, yf - PE_L, qz), axis=(0, -1, 0), range=(0, 0), unit="PE", gender="none")
    # pe-plate is a top-level node: the plate is fixed, so a child of it would move no differently, and a nested node's mesh is placed
    # by the AutoCAD gate's glb reader relative to its parent's origin (request mech-12: read 12 outside the box here, FAIL)
    Ld = f"node:door|{MAT}"
    th = -math.radians(swing); c, s = math.cos(th), math.sin(th)                        # the door turned about the hinge edge (0, 0, z): outward = toward -y
    ex, ey, ez = (c, s, 0), (-s, c, 0), (0, 0, 1)
    off = lambda x, y, z: (x * ex[0] + y * ey[0], x * ex[1] + y * ey[1], z)              # a point of the closed door, turned
    if swing == 0.0:
        door = P.box(Ld, 0, -DOOR_T, 0, W, DOOR_T, H)                                   # door over the box's front edges (the default build, unchanged)
        P.collider("door", 0, -DOOR_T, 0, W, DOOR_T, H)
    else:
        door = P.obox(Ld, off(0, -DOOR_T, 0), ex, ey, ez, W, DOOR_T, H)                 # the same door, turned open by `swing`
        xs, ys = zip(*(off(x, y, 0)[:2] for x in (0, W) for y in (-DOOR_T, 0)))
        P.collider("door", min(xs), min(ys), 0, max(xs) - min(xs), max(ys) - min(ys), H)   # its axis-aligned box in that position
    P.host("door", door, DOOR_T)                                                        # operators cut through it
    P.pivot("door", "rotate", (0.0, 0.0, H / 2), axis=(0, 0, 1), range=(0.0, -SWING))   # about the front-left vertical edge
    dx, dz = PE_DOOR                                                                    # pe-door: the door's bonding stud, into the box from its inner face
    P.cyl(f"node:pe-door|{ZN}", off(dx, 0, dz), off(dx, PE_L, dz), PE_D / 2)
    P.pivot("pe-door", "port", off(dx, PE_L, dz), axis=(ey[0], ey[1], 0), range=(0, 0), unit="PE", gender="none")
    P.parents["pe-door"] = "door"                                                       # swings with the door, keeps its own pivot
    return P

PREVIEWS = [dict(name="three-quarter", az=230, el=22), dict(name="rear and bottom, fixing and entry holes", az=40, el=-25),
            dict(name="open door 110 deg: mounting plate, earth studs", az=250, el=18, params=dict(swing=110))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
