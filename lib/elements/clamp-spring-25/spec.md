# clamp-spring-25 · v1.1 · spring clamp, generic, clamping range 25, overhang 54, two steel arms on a Ø8 pin, plastic pads 16 × 24

**What** A spring clamp: the hand clamp a joiner squeezes open and lets close on an edge, a glued joint or a sheet; a spring round its
pin holds the jaws shut. Two zinc-plated steel arms on one pin, each a jaw bar in front of the pin and a handle bar behind it, each
jaw with a plastic pad. The lower arm is fixed: its jaw bar, its handle bar and two cheeks bored for the pressed pin. The upper arm
is the mechanism (node `jaw`): its boss turns on the pin between the cheeks, and squeezing the handles together opens the jaws. The
twin opens and closes the clamp by name. The first element of ETIM's "Spring clamp" class in the library (`python lib/build.py
inventory mech` lists the class to build generic once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic spring clamp (ETIM 10.0 EC004294), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its two features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; every size is a design choice.
**Units / frame** mm, Z up. Origin: on the pin's axis (the line x = 0, z = 0 along y), in the clamp's centre plane y = 0. The jaws
point toward +x, the handles toward −x. The pads' clamping faces stand 1 apart at rest, at z −0.5 and 0.5. Extents x −110 to 70, y −12
to 12 (the pads), z −34 to 34.
**Built with** toolkit 1.3 · AutoLISP command `CLAMPSPR` · no parameters.

## Class values
ETIM 10.0 class EC004294 Spring clamp (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Max. clamping range (EF022847) | 25 mm: the pads' centres (x 60) 25.4 apart at the end of the upper arm's travel (24 degrees) |
| 2 | Overhang length (EF000303) | 54 mm: from the pads' tips (x 68) back to the lower arm's cheeks' front faces (x 14), the reach over the work's edge: work wider than the 12 between the cheeks stops there (element.py `OVERHANG`, asserted) |

No clamping force is designed or claimed (the class states none here, and the spring is not drawn or rated).

## What it meets
| figure | value | source |
|---|---|---|
| the work | between the pads, 1 to 25.4 thick at the pads' centres; the jaw bars 7 apart behind the pads | design: a hand tool's opening (OPERATING.md 12, an own size); nothing is placed in it |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| lower arm (fixed) | jaw bar 59 × 18 × 8 (x 11 to 70, y ±9, z −11.5 to −3.5); handle bar 99 × 18 × 8 (x −110 to −11, z −34 to −26); two cheeks 28 × 3.0 × 36 (x ±14, y ±6 to ±9, z −30 to 6) joining them, each bored Ø8 for the pin | the jaw bar starts 11 from the pin, beyond the radius the upper arm's boss sweeps (9.9); the cheeks 3.0 thick |
| pin | Ø8 × 19 (y ±9.5), pressed through the cheeks, its ends 0.5 proud | the upper arm turns on it |
| upper arm (node `jaw`) | boss 14 × 10 × 41 (x ±7, y ±5, z −7 to 34) bored Ø10; jaw bar 63 × 10 × 8 (x 7 to 70, z 3.5 to 11.5); handle bar 103 × 10 × 8 (x −110 to −7, z 26 to 34) | the boss turns between the cheeks 1 clear each side and 1 clear round the pin (features.csv, kind own) |
| pads | 16 × 24 × 3.0 (x 52 to 68, y ±12), on each jaw bar's inner face: the lower's face at z −0.5, the upper's at 0.5 | 1 apart at rest, so the solids never touch; wider than the bars to spread the grip |
| travel | 24 degrees | the handles' ends then stand 5 apart (the upper handle's corner at z −21.0 over the lower handle's top at −26), the stop a hand meets |
| layers | arms `M-ZINC` (zinc-plated steel); pin `M-SILVER` (bright steel); pads `M-ORANGE-PA` (plastic) | a design choice, no finish claim |

## Mechanism
`jaw` (rotate about axis (0, −1, 0), 0 to 24 degrees, pivot (0, 0, 0) on the pin's axis): 0 is closed, as built (the pads 1 apart);
24 is open (the pads' centres 25.4 apart, the handles squeezed to 5 apart at their ends). The node carries the upper arm's boss, its
jaw bar, its handle bar and its pad. MOT-010 sweeps it through the full range: the boss turns between the cheeks (1 clear each side)
and round the pin (1 clear), its lower corners (radius 9.9) never reach the lower jaw bar (from x 11), the upper jaw turns up away
from the lower, and the upper handle comes down to 5 above the lower one.
The spring round the pin is not drawn (internal mechanism the twin doesn't read): it holds the jaws shut, so closed is the state at
rest. A workpiece between the pads sets the real stop in the assembly.

## Named nodes
`jaw` (rotate). Colliders `lower-jaw`, `lower-handle` (axis-aligned boxes).

## Materials by layer
`M-ZINC` both arms · `M-SILVER` the pin · `M-ORANGE-PA` the pads.

## Decals (Blender)
No label: the clamp's layers, `M-ZINC`, `M-SILVER` and `M-ORANGE-PA`, are not printed layers of the Blender gate (review mech-r125
finding 2's reading).

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force. The class values are the figures this design is meant to
meet; no calculation or test of the model is on file. No open figure. The gate's fillet rule (r 0.5 for a device): the bars and the
boss have no edge under 8; the cheeks and the pads are 3.0 thick, so their short edges are skipped; the bores' edges are cut edges.
Not drawn: the spring, swivelling pads, handle grips. lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`clamp-spring-25.lsp` · `.glb` (pivot on `jaw`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004294), our own design (mech-r127, unattended, 2026-11-12): two steel arms on a Ø8 pin, the upper arm turning 24 degrees, plastic pads, clamping range 25 |
| 1.1 | text only, the part unchanged (mech-r144, unattended, 2026-11-13): review mech-r127 / clamp-spring-25-1.0 finding 1, class value Overhang length 61 → 54, the pads' tips to the cheeks' front faces (x 68 − 14), the model's own measure (element.py `OVERHANG`, asserted; TITLE); note 1, Decals "No label" |
