# seamer-80 · v1.1 · hand seamer, generic, blades 80 wide with a 30 bite, clamping spread 19.7, length 250, two steel arms crossed on a Ø8 pin, plastic grips

**What** A hand seamer: the sheet-metal worker's seaming pliers. Two wide flat blades grip a sheet's edge so it can be bent up, folded
into a seam or held taut while it is fixed. Two zinc-plated steel arms crossed on one pin, as pliers: the fixed arm carries the lower
blade (through a neck and two cheeks bored for the pressed pin) and the upper handle; the moving arm (node `jaw`) carries the upper
blade above the pin's axis and the lower handle below it, on a boss that turns on the pin between the cheeks. Squeezing the handles
together closes the blades on the sheet; spreading them opens the blades. Each handle ends in a plastic grip. The twin opens and
closes it by name. The first element of ETIM's "Seaming tool" class in the library (`python lib/build.py inventory mech` lists the
class to build generic once no inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md); no inventory
row or system names it yet.
**Class** device · **Baseline** our own design: generic seaming tool (ETIM 10.0 EC004320), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its five features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; every size is a design choice. The pin, the cheeks and
the boss follow clamp-spring-25 1.0's pattern (Ø8 pin pressed, Ø10 boss bore, cheeks 3.0 thick, 1 clear each side).
**Units / frame** mm, Z up. Origin: on the pin's axis (the line x = 0, z = 0 along y), in the seamer's centre plane y = 0. The blades
point toward +x, the handles toward −x. The blades' gripping faces stand 1 apart at rest (closed), at z −0.5 and 0.5. Extents x −200
to 50, y −40 to 40 (the blades), z −26 to 26 (the grips).
**Built with** toolkit 1.3 · AutoLISP command `SEAMER` · no parameters.

## Class values
ETIM 10.0 class EC004320 Seaming tool (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Clamping spread (EF006203) | 19.7 mm: the blades' tips (x 50) 19.69 apart at the end of the moving arm's travel (22 degrees; element.py SPREAD) |
| 2 | Max. clamping force (EF021596) | not stated: no hand force, lever calculation or test is on file, and none is claimed |
| 3 | Width (EF000008) | 80 mm: the blades' width (y ±40) |
| 4 | Length (EF001438) | 250 mm overall: the blades' tips (x 50) to the grips' ends (x −200) |
| 5 | Grip design (EF007841) | plastic grips on both handles, 112 long, 2 proud of the steel bar all round (a plain name: ETIM's value list is not on file) |

## What it meets
| figure | value | source |
|---|---|---|
| the work | a sheet's edge between the blades, up to 19.7 thick at the tips, gripped over the bite 30 × 80 | design: a hand tool's opening (OPERATING.md 12, an own size); nothing is placed in it |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| fixed arm | lower blade 30 × 80 × 8 (x 20 to 50, y ±40, z −8.5 to −0.5); neck 6 × 18 × 8 (x 14 to 20, z −8.5 to −0.5), face to face with the cheeks; two cheeks 30 × 3.0 × 30 (x −16 to 14, y ±6 to ±9, z −10 to 20), each bored Ø8 for the pin; upper handle bar 77 × 18 × 8 (x −90 to −13, z 16 to 24), 3 into the cheeks | the neck starts at x 14, so the moving arm's boss sweeps 2.8 clear of it (element.py asserts it: its lower inner corner reads x 9.80 in the turned arm's frame against the boss's face at 7); the cheeks end at x 14, so the upper blade's back top corner, which turns to (15.36, 15.4) at 22 degrees, passes 1.36 clear of them (asserted; the first validate's MOT-010 found cheeks to x 16 hit at 21.4 degrees, fixed at the same version before any Blender or Godot run) |
| pin | Ø8 × 19 (y ±9.5), pressed through the cheeks, its ends 0.5 proud | the moving arm turns on it (clamp-spring-25's) |
| moving arm (node `jaw`) | boss 14 × 10 × 32.5 (x ±7, y ±5, z −24 to 8.5) bored Ø10; neck 13 × 10 × 8 (x 7 to 20, z 0.5 to 8.5); upper blade 30 × 80 × 8 (x 20 to 50, z 0.5 to 8.5); lower handle bar 83 × 10 × 8 (x −90 to −7, z −24 to −16) | the arms cross at the pin, as pliers: the boss turns between the cheeks 1 clear each side and 1 clear round the pin (features.csv, kind own); its upper corners (radius 11.0) never reach the fixed neck |
| grips | 112 long (x −200 to −88), 2 proud of their bar all round: the upper 22 × 12 (z 14 to 26), the lower 14 × 12 (z −26 to −14); each steel bar ends 2 inside its grip | 28 apart at rest (closed), a hand's squeeze; plastic, a plain appearance choice |
| blades | 8 thick, faces 1 apart at rest | so the solids never touch; the bite 30 deep from the tips |
| travel | 22 degrees | the blades' tips then 19.7 apart, the grips' ends about 102 apart (the lower grip's corner at z −87.9 under the upper grip's 14) |
| layers | arms `M-ZINC` (zinc-plated steel); pin `M-SILVER` (bright steel); grips `M-ORANGE-PA` (plastic) | a design choice, no finish claim |

## Mechanism
`jaw` (rotate about axis (0, −1, 0), 0 to 22 degrees, pivot (0, 0, 0) on the pin's axis): 0 is closed, as built (the blades' faces 1
apart, the grips 28 apart); 22 is open (the blades' tips 19.7 apart, the handles spread). The node carries the moving arm's boss, its
neck, the upper blade, the lower handle bar and its grip. MOT-010 sweeps it through the full range: the boss turns between the cheeks
(1 clear each side) and round the pin (1 clear), its face stays 2.8 clear of the fixed neck, the upper blade turns up away from the
lower one and its back passes 1.36 in front of the cheeks, and the lower handle turns down away from the upper. No return spring is drawn or claimed: the hand closes and opens it,
and a sheet between the blades sets the real stop in the assembly.

## Named nodes
`jaw` (rotate). Colliders `lower-blade`, `upper-handle` (axis-aligned boxes; neither is named like the node).

## Materials by layer
`M-ZINC` both arms · `M-SILVER` the pin · `M-ORANGE-PA` the grips.

## Decals (Blender)
No label: the seamer's layers, `M-ZINC`, `M-SILVER` and `M-ORANGE-PA`, are not printed layers of the Blender gate (review mech-r125
finding 2's reading).

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force. The class values are the figures this design is meant to
meet; no calculation or test of the model is on file. No open figure. The gate's fillet rule (r 0.5 for a device): the blades, necks,
bars, boss and grips have no edge under 8; the cheeks are 3.0 thick, so their short edges are skipped; the bores' edges are cut edges.
Not drawn: a return spring, a lock, offset or angled blades (straight blades, a design choice). lib/materials.csv gives no densities,
so no mass is stated.
Hand volume (as the sum of primitives, overlaps counted in each): fixed arm M-ZINC 36 250.4 mm³ (blade 19 200, neck 864, cheeks
5 400 less their bores 301.6, handle bar 11 088), pin 955.0, upper grip 29 568; node jaw M-ZINC 30 644.6 (boss 4 550 less its bore
785.4, neck 1 040, blade 19 200, handle bar 6 640), lower grip 18 816.

## Outputs (out/)
`seamer-80.lsp` · `.glb` (pivot on `jaw`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004320), our own design (mech-r128, unattended, 2026-11-12): two steel arms crossed on a Ø8 pin, the moving arm turning 22 degrees, blades 80 wide, clamping spread 19.7, plastic grips |
| 1.1 | text only, the part unchanged (mech-r144, unattended, 2026-11-13): review mech-r128 / seamer-80-1.0 finding 1, behaviour.csv's header and `open` note and features.csv's two notes name this element's arms (the fixed arm's cheeks, the moving arm's boss, upper blade and lower handle; the handles spread apart to open), not clamp-spring-25's; note 1, Decals "No label" |
