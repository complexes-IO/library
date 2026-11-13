# hanger-vibration · v1.1 · vibration isolation hanger, generic, rubber in compression, frame 60 × 40 × 90, M10 rod top and bottom

**What** A vibration isolation hanger: the rubber hanger a duct, a pipe run, a fan or a suspended platform hangs from on threaded
rods, so the ceiling takes less of its vibration. Rubber in compression in a closed frame: a galvanized steel frame of 3.0 sheet
(top plate, bottom plate, two side plates; open at its ±y faces) hangs from the ceiling's M10 rod through a hole in its top plate,
the rod's nut inside the frame. The load's M10 rod comes up through a free passage in the bottom plate, a rubber element and a steel
cap, its nut on the cap: the load pulls the cap down and presses the rubber onto the bottom plate, so the rods never touch through
steel. The first element of ETIM's "Vibration isolation hanger" class in the library (`python lib/build.py inventory mech` lists the
class to build generic once no inventory row builds unattended; the machine-element classes above it wait for a dimensional standard
or a toolkit primitive: lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic vibration isolation hanger (ETIM 10.0 EC010829), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). The class and its fifteen features are on file (lib/standards/etim/classes.csv, class-features.csv). No
product was matched and no vendor file was opened. The class values below are the design inputs; the rods' holes are ISO 273's;
every other size is a design choice.
**Units / frame** mm, Z up. Origin: the frame's top face (z = 0) on the ceiling rod's axis. x across the side plates, y through the
open faces. Extents x −30 to 30, y −20 to 20, z −90 to 0.
**Built with** toolkit 1.3 · AutoLISP command `VIBHANG` · no parameters.

## Class values
ETIM 10.0 class EC010829 Vibration isolation hanger (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature
in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | rubber in compression, closed frame |
| 2 | Material (EF002169) | frame and cap steel, galvanized; element NBR rubber |
| 3 | Damping value (EF023650) | not stated |
| 4 | Attachment connection (EF023655) | through hole for a threaded rod, the nut inside the frame |
| 5 | Size of attachment thread connection (metric) (EF023656) | M10 |
| 6 | Connection facility (EF020239) | threaded rod through the bottom plate, the rubber element and the cap, the nut on the cap |
| 7 | Size of connection facility thread connection (metric) (EF023657) | M10 |
| 8 | Max. ambient temperature (EF020188) | not stated |
| 9 | Load bearing capacity (EF017206) | not stated |
| 10 | Min. ambient temperature (EF020432) | not stated |
| 11 | Hinging (EF001076) | no |
| 12 | Deflection (EF026195) | not stated |
| 13 | Length (EF001438) | 60 mm: the frame across its side plates (x) |
| 14 | Width (EF000008) | 40 mm: the frame's depth (y) |
| 15 | Height (EF000040) | 90 mm: the frame's top face to its underside (z), unloaded |

The class's load, deflection, damping and temperature figures are not stated here, so none is designed to or claimed: the hanger
carries what its host's design gives it, and the twin draws it unloaded.

## What it meets
| figure | value | source |
|---|---|---|
| the ceiling's rod | Ø11 through the top plate at the origin | M10 clearance, ISO 273 medium H13 (lib/standards/holes.csv). Position Ø0.5 at MMC ≤ H − F = 1.0 to A the top face, B the plane x 0, C the plane y 0 (ASME Y14.5 floating fastener, features.csv). The rod, its nut and washer (M10, ISO 261's nominal diameter) are the host's |
| the load's rod | Ø22 free passage through the bottom plate; Ø12 bore through the rubber; Ø11 through the cap, its nut on the cap's top at z −54 | the cap's hole: M10 clearance, ISO 273 medium H13 (features.csv); the passage and the bore: design, 6 and 1 clear around an M10 rod (ISO 261 nominal 10) so it never bears on steel or rubs the rubber (OPERATING.md 12). The rod, its nut and washer are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| frame | 60 × 40 × 90 of 3.0 sheet, galvanized steel (`M-GALV`): side plates 3 × 40 × 90, top and bottom plates 54 × 40 × 3 between them | a closed frame carries the load from the bottom plate up the sides to the top plate; 3.0 sheet, so every short edge is skipped by the gate; holes 9 and 14.5 from the plates' edges (DFM-010: ≥ 1.5 t = 4.5) |
| rubber element | Ø36 × 30, NBR (`M-GASKET`), on the bottom plate's top face (z −87 to −57), Ø12 bore | the damping element, in compression; 2 inside the frame's open faces, 9 inside the side plates |
| cap | Ø32 × 3, galvanized steel, on the rubber (z −57 to −54), Ø11 hole | spreads the load rod's nut on the rubber |
| room for the nuts | 51 between the cap's top and the top plate's underside | the two rods' nuts and their ends |
| load, deflection, damping, temperature range, natural frequency | not claimed | the class states these as features, and this design states none: no calculation or test is on file |

## Mechanism
None: one fixed body, no moving node, no port. The rubber is drawn unloaded; with no stiffness or load figure on file, a loaded
pose (the cap sunk on the rubber) has no figure to come from, so none is drawn. behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `body` (x ±30, y ±20, z −90 to 0).

## Materials by layer
`M-GALV` the frame and the cap (steel, galvanized) · `M-GASKET` the rubber element (black).

## Decals (Blender)
No label: the hanger's layers, `M-GALV` and `M-GASKET`, are not printed layers of the Blender gate (toolkit/blender/gate.py
`--printed`, default M-WHITE-PA, M-BLACK-PA), so no tool on file carries the "complexes.org generic" label 1.0 named (review
hanger-vibration-1.0 finding 1, mech-r125 finding 2's reading; needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. No load, deflection, damping or safety claim. The drawn volume is about 35 262 mm³ of steel
(sides 21 600; top 6 480 less its hole 285.1; bottom 6 480 less its passage 1 140.4; cap 2 412.7 less its hole 285.1) and 27 143 mm³
of rubber (Ø36 × 30 less its Ø12 bore); written as volume only: lib/materials.csv gives no densities, so no mass is stated. A mesh's
cylinders and bores are polygons inside their circles, so the Blender gate reads 61 949.7 mm³ in all (0.7 % under the circles'
62 405.5). Not drawn: the rods, nuts and washers (the
host's). A vibration isolation hanger is not a part a dimensional standard shapes, so it is built generic to its ETIM class
(OPERATING.md 12). The gate's fillet rule (r 0.5 for a device): every plate is 3.0 thick, so its 3 edges are "short" and skipped and
its others are 40 or longer; the rubber and the cap are cylinders; the holes' edges are cut edges, skipped. Every bounding-box
extreme lies on an uncut axis-aligned box face: the side plates' x ±30, y ±20, z −90 and z 0.

## Outputs (out/)
`hanger-vibration.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010829), our own design (mech-r123, unattended, 2026-11-12): a 60 × 40 × 90 galvanized frame of 3.0 sheet, an NBR element Ø36 × 30 in compression, a cap, M10 rods top and bottom |
| 1.1 | text only, the part unchanged (mech-r145, unattended, 2026-11-13): review hanger-vibration-1.0 finding 1, Decals "No label" (its layers are not printed) |
