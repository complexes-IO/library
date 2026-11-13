# tensioner-strap-16 · v1.0 · strapping device, generic, hand strap tensioner for plastic strap 12 to 16 wide, feed wheel Ø30, lever 210, sole 160 × 40

**What** A strapping device: the hand strap tensioner a packer sets on a strapped load (a pallet, a crate, a bundle) and pumps by
its lever to pull the strap tight before the joint is sealed. A zinc-plated steel sole plate stands on the load; on it a hardened grip
plate and two cheeks; between the cheeks a knurled feed wheel on its shaft, 1.5 above the grip plate, so the strap's upper layer runs
under the wheel, over the grip plate. The lever is the mechanism (node `lever`): two side plates outside the cheeks, a handle bar
across their rear ends, the shaft pressed in the plates and the feed wheel on the shaft. Lifting the handle turns the lever about the
wheel's axis; on that working stroke the ratchet couples the wheel to the lever, so the wheel turns with it and draws the strap in.
The twin lifts and lowers the lever by name. The first element of ETIM's "Strapping device" class in the library (`python lib/build.py
inventory mech` lists the class to build generic once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic strapping device (ETIM 10.0 EC003373), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its five features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; every size is a design choice.
**Units / frame** mm, Z up. Origin: on the sole plate's underside (z = 0, the face that stands on the load), under the feed wheel's
axis (the line x = 0, z = 24.5 along y), in the strap's centre plane y = 0. The lever points toward −x, the sole's front toward +x.
Extents x −200 to 50, y −20 to 20 (the sole), z 0 to 40 (the cheeks' tops).
**Built with** toolkit 1.3 · AutoLISP command `TENSSTRP` · no parameters.

## Class values
ETIM 10.0 class EC003373 Strapping device (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | hand tensioner: a lever pumped by hand, no drive |
| 2 | Bandwidth (EF011276) | 12 to 16 mm: the feed wheel's face is 16 wide and the channel between the cheeks 18 |
| 3 | Suitable for plastic band (EF011277) | yes |
| 4 | Suitable for metal tape (EF005822) | no: a steel strap's edges and its sealer are not designed for here |
| 5 | Min. contact area (EF011274) | not stated |

No strap tension is designed or claimed (the class states none, and the ratchet is not drawn or rated).

## What it meets
| figure | value | source |
|---|---|---|
| the strap | 12 to 16 wide, in the 1.5 path between the grip plate (z 8) and the feed wheel (z 9.5), the channel between the cheeks 18 wide (y ±9) | design: the class value bandwidth (ETIM 10.0 EC003373, OPERATING.md 12); the strap is not drawn and its thickness is not stated |
| the load | the sole's underside z = 0, 160 × 40 | design: a hand tool set on the load's top face (OPERATING.md 12, an own size); nothing is placed under it |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| sole plate (fixed) | 160 × 40 × 6 (x −110 to 50, y ±20, z 0 to 6) | stands on the load beyond the wheel both ways; the extents' x front and y |
| grip plate (fixed) | 24 × 16 × 2.0 (x ±12, y ±8, z 6 to 8) | the hardened face the wheel presses the strap on; 2.0 thick, so its short edges are skipped by the fillet rule |
| cheeks (fixed) | two, 40 × 3.0 × 34 (x ±20, y ±9 to ±12, z 6 to 40), each bored Ø12 on the wheel's axis | 1 clear of the wheel each side and 1 clear round the shaft (features.csv, kind own); 15.5 above the axis, so the wheel's outline (Ø30) stays inside them |
| feed wheel (node `lever`) | Ø30 × 16 (y ±8), axis z 24.5 | its underside 1.5 above the grip plate: the strap's path; its knurl not drawn |
| shaft (node `lever`) | Ø10 × 35 (y ±17.5) | through the cheeks 1 clear, pressed in the lever's plates, its ends 1.5 proud of them |
| lever (node `lever`) | two side plates 210 × 3.0 × 16 (x −200 to 10, y ±13 to ±16, z 16.5 to 32.5), each bored Ø10 for the shaft; handle bar 14 × 26 × 16 (x −200 to −186, y ±13) between their rear ends | outside the cheeks 1 clear; their front corners (radius 12.8 about the axis) sweep clear of the sole (18.5 below the axis) |
| travel | 60 degrees | one working stroke: the handle bar's centre then 167 above the axis |
| layers | sole, cheeks, lever `M-ZINC` (zinc-plated steel); grip plate, feed wheel, shaft `M-SILVER` (hardened bright steel) | a design choice, no finish claim |

## Mechanism
`lever` (rotate about axis (0, 1, 0), 0 to 60 degrees, pivot (0, 0, 24.5) on the feed wheel's axis): 0 is down, as built (the side
plates level, their undersides at z 16.5, 10.5 above the sole's top); 60 is the top of a working stroke (the handle lifted). The node carries the feed wheel, the
shaft, both side plates and the handle bar: on the working stroke the ratchet couples the wheel to the lever, so the wheel turns with
it. MOT-010 sweeps it through the full range: the wheel and the shaft turn on their own axis (the shaft 1 clear in the cheeks' bores,
the wheel 1 clear of the cheeks), the side plates turn outside the cheeks (1 clear in y), and their front corners never come lower
than z 11.7, 5.7 above the sole.
Not drawn (internal mechanism the twin doesn't read): the ratchet and pawl that let the lever return without the wheel, the feed
wheel's spring loading against the grip plate, the gripper that holds the strap's lower layer, and the release.

## Named nodes
`lever` (rotate). Colliders `sole`, `cheeks` (axis-aligned boxes).

## Materials by layer
`M-ZINC` sole, cheeks, lever · `M-SILVER` grip plate, feed wheel, shaft.

## Decals (Blender)
"complexes.org generic" on the sole plate's −y face.

## Notes
No vendor names, part numbers or marks. No safety claim, no strap tension. The class values are the figures this design is meant to
meet; no calculation or test of the model is on file. No open figure. The gate's fillet rule (r 0.5 for a device): the sole is 6 thick
and the handle bar 14 or more on every edge; the cheeks and the side plates are 3.0 thick and the grip plate 2.0, so their short edges
are skipped; the bores' edges are cut edges. Not drawn: the ratchet, the spring, the lower layer's gripper, a handle grip, the
wheel's knurl. lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`tensioner-strap-16.lsp` · `.glb` (pivot on `lever`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003373), our own design (mech-r129, unattended, 2026-11-12): a hand strap tensioner, the lever with the feed wheel turning 60 degrees about the wheel's axis, bandwidth 12 to 16 |
