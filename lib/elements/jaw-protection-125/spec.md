# jaw-protection-125 · v1.1 · protection jaw, generic, aluminium angle 3 thick for vise-bench's jaw plate 125 × 50 × 12, hangs on the plate's top edge

**What** A protection jaw for a bench vice: the soft aluminium angle a fitter hangs over the vice's hard steel jaw plate so the
plate's face doesn't mark finished work. Its front leg covers the plate's clamping face; its top leg rests on the plate's top edge, so
it hangs there by its own weight and comes off by hand. It is the size of vise-bench 1.0's jaw plates (read from vise-bench with
library.load), so it fits either of that vice's jaws; a pair covers both. One fixed body: it moves with the jaw it hangs on. The first
element of ETIM's "Vice plate for bench-vice" class in the library (its synonyms name protection jaws and vice protection jaws;
`python lib/build.py inventory mech` lists the class to build generic once no inventory row builds unattended: group EG020054
Clamping tools, lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic vice plate for bench-vice (ETIM 10.0 EC002202), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). The class and its three features are on file (lib/standards/etim/classes.csv, class-features.csv). No
product was matched and no vendor file was opened. The class values below are the design inputs; the plate it covers is vise-bench
1.0's; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the protection face (the front leg's +x face, toward the work) at x = 0, the front leg's underside
at z = 0 (level with the vice plate's underside), the jaw's centre at y = 0. The front leg's back face (on the vice plate's clamping
face) at x = −3; the top leg's underside (on the plate's top edge) at z = 50. On vise-bench 1.0's fixed jaw the element's origin sits
at the vice's (3, 0, 100) (the plate's face x = 0, its underside JAW_Z0 = 100); on the moving jaw it is turned 180 degrees about z.
Extents x −15 to 0, y −62.5 to 62.5, z 0 to 53.
**Built with** toolkit 1.3 · AutoLISP command `JAWPROT` · no parameters.

## Class values
ETIM 10.0 class EC002202 Vice plate for bench-vice (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Width (EF000008) | 125 mm: across the vice's jaws (y), vise-bench 1.0's jaw width |
| 2 | Material (EF002169) | aluminium |
| 3 | Magnetic (EF004911) | no: it hangs on the jaw plate's top edge by its top leg |

No clamping force or protection (marking) claim is designed or made.

## What it meets
| figure | value | source |
|---|---|---|
| the vice's jaw plate | 125 × 50 × 12: the front leg's back face on the plate's clamping face, the top leg's underside on its top edge | vise-bench 1.0's JAW_W, JAW_H, JAW_T (library.load("vise-bench"): one home for the plate's size) |
| the work | flat work against the protection face, x = 0, 125 × 53 | design: the face's size is this design's (OPERATING.md 12, an own size) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| front leg | 3 × 125 × 53 (x −3 to 0, y ±62.5, z 0 to 53) | covers the plate's whole clamping face and reaches the top leg above the plate's top edge |
| top leg | 12 × 125 × 3 (x −15 to −3, y ±62.5, z 50 to 53) | rests on the plate's 12 thick top edge, its back end flush with the plate's back face; the angle hangs by it |
| thickness | 3 | soft enough to take the work's shape a little; every free-corner edge 3 (the gate's short-edge rule) or 12 and longer |
| layer | `M-ALU-ANOD` (aluminium) | a design choice, no alloy, hardness or finish claim |

## Mechanism
None: one fixed body. On the vice it moves with the jaw it hangs on (vise-bench's node `jaw`, or its fixed jaw).

## Named nodes
None. Colliders `front-leg`, `top-leg` (the two legs' boxes, so the vice plate's seat under the top leg stays free).

## Materials by layer
`M-ALU-ANOD` the angle.

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default
M-WHITE-PA, M-BLACK-PA); this part's one layer is M-ALU-ANOD, so no tool on file carries the "complexes.org generic" label 1.0 named
(review mech-r126 finding 2; needs-em 218 asks the core for the rule). Should the core settle on a label for unprinted parts, its place
is the top leg's upper face (z 53, the visible flat face when hung); 1.0's front leg's back face lies on the vice's jaw plate and could
not be seen (the review's note).

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force or protection claim. The class values are the figures this
design is meant to meet; no calculation or test of the model is on file. No open figure: the plate it covers is vise-bench's. The
gate's fillet rule (r 0.5 for a device): the legs' 3 edges are at the short-edge limit, skipped; every other edge is 12 or longer.
Every bounding-box extreme is on an uncut box. Not drawn: a fibre or rubber facing, a horizontal or vertical prism groove, magnets.
Hand volume: 24 375 mm³ (front leg 19 875, top leg 4 500). lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`jaw-protection-125.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002202), our own design (mech-r126, unattended, 2026-11-12): an aluminium angle 3 thick over vise-bench 1.0's jaw plate, hung on its top edge |
| 1.1 | text only (review mech-r126 finding 2): Decals "No label" (no printed layer), the visible face for a later label named. The part unchanged; a minor (mech-r144, unattended, 2026-11-13) |
