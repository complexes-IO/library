# jaw-prism-125 · v1.1 · prism clamping jaw, generic, 125 × 40 × 18 for vise-machine's jaw seat, vertical 90 degree V-groove 12 wide, 2 × M8 tapped from behind

**What** A prism clamping jaw: a steel jaw plate that takes the place of a machine vice's plain jaw plate, with a vertical 90 degree
V-groove in its clamping face, so a tube or a round bar standing upright is held on both flanks of the groove instead of on one line.
It is the size of vise-machine 1.0's jaw plates (read from vise-machine with library.load), so either of that vice's plates can be
swapped for it, or both. Two M8 tapped holes in its back face take the screws that hold it to the vice's jaw block from behind. One
fixed body: it moves with the jaw block it is screwed to. The first element of ETIM's "Clamping jaw" class in the library (`python
lib/build.py inventory mech` lists the class to build generic once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic clamping jaw (ETIM 10.0 EC004297), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its four features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; the seat is vise-machine 1.0's; the tapped holes'
figures are derived (ISO 68-1, ISO 965-1); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the clamping face (the jaw's +x face, toward the work) at x = 0, the plate's underside at z = 0, its
centre at y = 0. The back face (the seat on the vice's jaw block) at x = −18. The V-groove's apex line at x = −6, y = 0. In
vise-machine 1.0 the plate stands with its underside at the vice's z 70 (its jaw plates' JAW_Z0). Extents x −18 to 0, y −62.5 to
62.5, z 0 to 40.
**Built with** toolkit 1.3 · AutoLISP command `JAWPRISM` · no parameters.

## Class values
ETIM 10.0 class EC004297 Clamping jaw (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Length (EF001438) | 125 mm: across the vice's jaws (y), vise-machine 1.0's jaw width |
| 2 | Width (EF000008) | 18 mm: the plate's thickness, back face to clamping face (x) |
| 3 | Height (EF000040) | 40 mm: z 0 to 40, vise-machine 1.0's jaw height |
| 4 | Suitable for tubes (EF009917) | yes: the vertical 90 degree V-groove seats a tube or a round bar of Ø5 to Ø16 on both flanks, standing proud of the clamping face (element.py asserts both bounds) |

No clamping force is designed or claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the vice's jaw seat | 125 × 40 × 18, the back face on the jaw block's face | vise-machine 1.0's JAW_W, JAW_H, JAW_T (library.load("vise-machine"): one home for the seat) |
| the fixing screws | 2 × M8 tapped holes in the back face at y ±40, z 20, 12 deep, drawn at the minor diameter 6.6468 | derived: derive.thread(8.0, 1.25) (ISO 68-1 basic profile; ISO 965-1 clause 10, internal 6H D1 min; ISO 261 pitch 1.25). The screws (socket head cap screws, ISO 4762, a common part not built yet) and the jaw block's clearance holes (ISO 273) are the host's, placed in a later version |
| the work | tubes and round bars Ø5 to Ø16 standing upright in the groove; flat work against the clamping face beside it | design: the groove's size is this design's (OPERATING.md 12, an own size) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| V-groove | 90 degrees, 6 deep, 12 wide at the clamping face, vertical (along z) on y = 0, the full height | a round of radius r touches both flanks at r·cos 45° from the groove's axis, inside the groove while r ≤ 8.49; it stands out past the face, so the other jaw reaches it, while r > 2.49 |
| tapped holes | 2 × M8, 12 deep (1.5 × the nominal diameter) from the back face, at y ±40, z 20 | 6 of steel left in front of each; 19 to the plate's ends and 17 to its top and bottom; far from the groove (y ±6) |
| layer | `M-SILVER` (bright steel) | a design choice, no hardness or finish claim |

## Mechanism
None: one fixed body. On the vice it moves with the jaw block it is screwed to (vise-machine's node `jaw`, or its fixed jaw).

## Named nodes
None. Collider `jaw` (the plate's box).

## Materials by layer
`M-SILVER` the plate.

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default
M-WHITE-PA, M-BLACK-PA); this part's one layer is M-SILVER, so no tool on file carries the "complexes.org generic" label 1.0 named
(review mech-r125 finding 2; needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force claim. The class values are the figures this design is meant
to meet; no calculation or test of the model is on file. No open figure: the seat is vise-machine's, the tapped holes' figures derived.
The gate's fillet rule (r 0.5 for a device): every box edge is 18 or longer; the groove's and the holes' edges are cut edges, skipped.
Every bounding-box extreme is on the plate's uncut faces. Not drawn: a horizontal groove, serrations, the threads. Hand volume:
87 727.2 mm³ (the plate 90 000 less the groove 1 440 and the two tapped holes 832.8). lib/materials.csv gives no densities, so no mass
is stated.

## Outputs (out/)
`jaw-prism-125.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004297), our own design (mech-r125, unattended, 2026-11-12): a jaw plate on vise-machine 1.0's seat with a vertical 90 degree V-groove and 2 × M8 tapped holes from behind |
| 1.1 | text only (review mech-r125 finding 2): Decals "No label" (no printed layer). The part unchanged; a minor (mech-r144, unattended, 2026-11-13) |
