# chuck-magnetic-250x125 · v1.0 · magnetic chucking block, generic, 250 × 125 × 75, one clamping face, switchable by a hand lever turning 180 degrees

**What** A magnetic chucking block: the switchable permanent-magnet block a surface grinder's or a mill's table carries, holding
steel work on its top face without clamps. A steel housing whose top face is the one clamping surface, a ledge along each long side
at its foot for the table's clamps, and a hand lever on the +x end face that turns half a turn to switch the magnets on and off.
The lever is the mechanism: the twin switches the block by name and reads its state. The first element of ETIM's "Magnetic chucking
system" class in the library (`python lib/build.py inventory mech` lists the class to build generic once no inventory row builds
unattended: group EG020054 Clamping tools, lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic magnetic chucking system (ETIM 10.0 EC004300), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). The class and its thirteen features are on file (lib/standards/etim/classes.csv, class-features.csv). No
product was matched and no vendor file was opened. The class values below are the design inputs; every size is a design choice.
**Units / frame** mm, Z up. Origin: the housing's underside (its seat on the machine table) at z = 0, the housing's centre at x = 0,
y = 0. The clamping face (the top) at z = 75. The lever on the +x end face turns about the line y = 0, z = 40. Extents x −125 to 156
(the lever's knob), y −77.5 to 80 (the ledges; the lever's arm at rest), z 0 to 75.
**Built with** toolkit 1.3 · AutoLISP command `CHUCKMAG` · no parameters.

## Class values
ETIM 10.0 class EC004300 Magnetic chucking system (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Construction type (EF000767) | rectangular block, permanent magnets, switched by hand |
| 2 | Pole division (EF014820) | not stated: the poles are inside the housing and not drawn |
| 3 | Model (EF000010) | switchable permanent-magnet block with a hand lever |
| 4 | Number of clamping surfaces (EF014882) | 1: the top face, 250 × 125 at z = 75 |
| 5 | Gripping force (EF014817) | not stated: no holding force is designed or claimed |
| 6 | Switchable (EF008037) | yes: the lever, node `lever`, half a turn from off to on |
| 7 | Suitable for grinding works (EF014818) | not stated |
| 8 | Suitable for milling works (EF014819) | not stated |
| 9 | Length (EF001438) | 250 mm: the housing along x (the lever stands 31 beyond it) |
| 10 | Width (EF000008) | 125 mm: the housing along y (155 over the two ledges) |
| 11 | Height (EF000040) | 75 mm: the clamping face above the seat |
| 12 | Diameter (EF000551) | not stated: a rectangular block |
| 13 | Weight (EF000167) | not stated: lib/materials.csv gives no densities |

No holding force is designed or claimed (it depends on the magnet system inside, which is not drawn, and on the work's material,
thickness and contact; the class states none here).

## What it meets
| figure | value | source |
|---|---|---|
| the machine table | the housing's underside, z = 0, 250 × 125, and the two ledges' undersides beside it | design: the block stands on the table's face (OPERATING.md 12, an own size); the table is the host's (table-slotted is one) |
| the table's clamps | a ledge 15 × 15 along each long side, its top at z = 15 | design: the clamps bear on the ledges; claw-clamping 1.1 is one such clamp, placed by the host. Nothing is placed here |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| housing | 250 × 125 × 75 (x ±125, y ±62.5, z 0 to 75), one solid | the class values; its top is the clamping face, its underside the seat |
| ledges | 250 × 15 × 15 each, y ±62.5 to ±77.5, z 0 to 15 | room for a clamp's toe on each long side; 25 below the lever's arm |
| lever shaft bore | Ø12 × 30 deep in the +x end face on the lever's axis (y 0, z 40) | carries the lever's shaft 1 clear; features.csv, kind own |
| lever | shaft Ø10 in the bore; hub Ø28 × 12, 1 clear of the end face (x 126 to 138); arm 8 × 12 to y 80 (x 128 to 136); knob Ø14 × 20 at y 72 (x 136 to 156) | a hand lever on the end face, clear of the clamping face and of the work on it |
| layers | housing, ledges, shaft, hub and arm `M-SILVER` (ground steel); knob `M-BLACK-PA` | a design choice, no finish claim |

## Mechanism
`lever` (rotate about axis (1, 0, 0), 0 to 180 degrees, pivot (125, 0, 40) on the +x end face): 0 is off, as built (the arm along
+y); 180 is on (the arm along −y), turned over the top. The node carries the shaft, the hub, the arm and the knob. MOT-010 sweeps it
through the full range: the shaft turns in its bore 1 clear, the hub stands 1 clear of the end face, and the arm turns in the plane
x 128 to 136, where nothing fixed stands.
The magnet system inside (the poles, the turning core the lever drives) is not drawn: internal mechanism the twin doesn't read. The
twin reads the lever's state (behaviour.csv): on or off, no force.

## Named nodes
`lever` (rotate). Colliders `housing`, `ledges` (axis-aligned boxes).

## Materials by layer
`M-SILVER` housing, ledges, lever shaft, hub and arm · `M-BLACK-PA` the lever's knob.

## Decals (Blender)
"complexes.org generic" on the housing's −y side face.

## Notes
No vendor names, part numbers or marks. No safety claim, no holding force, no flatness or parallelism claim. The class values are
the figures this design is meant to meet; no calculation or test of the model is on file. No open figure: the block stands on its
host's table and is held by its host's clamps. The gate's fillet rule (r 0.5 for a device): every box edge is 8 or longer; the
bore's edges are cut edges, skipped. Not drawn: the pole strips on the clamping face, the magnet system, an end stop for the work.
lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`chuck-magnetic-250x125.lsp` · `.glb` (pivot on `lever`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004300), our own design (mech-r127, unattended, 2026-11-12): a steel block 250 × 125 × 75 with one clamping face, a ledge along each long side and a hand lever turning 180 degrees |
