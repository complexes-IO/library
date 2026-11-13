# clamp-toggle-hook · v1.0 · toggle clamp, generic, hook type, horizontal, span 88, opening 90 degrees, base 70 × 50 with 4 × M5

**What** A hook-type toggle clamp: the latch a lid, a door or a fixture plate is drawn shut with. The base is screwed to one part; its
U-hook catches a keeper on the other part, and pressing the handle down pulls the hook tight. A zinc-plated steel base plate with four
M5 holes carries two cheeks; the lever (node `lever`) is two side plates on a pivot pin through the cheeks, a red polyamide handle across
their front ends, and the U-hook on a second pin in the plates: two arms joined at their front by the catch lip. Lifting the handle
turns the lever about the pivot and lifts the hook off the keeper. The twin lifts and lowers the lever by name. The first element of
ETIM's "Toggle clamp" class in the library (`python lib/build.py inventory mech` lists the class to build generic once no inventory row
builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md); the library's clamp-toggle is the group's other class
(EC003935 Machine toggle clamp, a hold-down), and this is the hook type, its own element. No inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic toggle clamp (ETIM 10.0 EC011973), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its eleven features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; the base holes are on file (ISO 273); every other size is a
design choice.
**Units / frame** mm, Z up. Origin: on the base plate's underside (z = 0, the mounting face), under the lever's pivot axis (the line
x = 0, z = 14 along y), in the clamp's centre plane y = 0. The hook reaches toward +x. Extents x −30 to 110 (the base's rear edge to the
handle's end), y −25 to 25 (the base), z 0 to 30 (the handle's top, closed).
**Built with** toolkit 1.3 · AutoLISP command `HOOKCLMP` · no parameters.

## Class values
ETIM 10.0 class EC011973 Toggle clamp (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Type (EF001139) | hook type, horizontal: the hook draws along the mounting face |
| 2 | Span (EF006495) | 88 mm, fixed: from the pivot axis to the catch lip's inner face (x 88) |
| 3 | Material (EF002169) | steel; the handle polyamide |
| 4 | Surface protection (EF000139) | zinc-plated |
| 5 | Max. tensile force (EF000353) | not stated |
| 6 | Max. opening angle (EF002642) | 90° |
| 7 | Length (EF001438) | 140 mm (x −30 to 110, closed) |
| 8 | Width (EF000008) | 50 mm (the base) |
| 9 | Height (EF000040) | 30 mm (closed) |
| 10 | Adjustable (EF000996) | no: the hook's length is fixed |
| 11 | With safety function (EF020677) | no: no catch against opening is designed; not a safety device |

No tensile force is designed or claimed (the over-centre linkage is not drawn or rated).

## What it meets
| figure | value | source |
|---|---|---|
| base screws | 4 × M5, Ø5.5 holes at 52 × 35 (x −22 and 30, y ±17.5), outside the cheeks' x range (−10 to 14), the hole centres 5.5 beyond the lever's plates in y (y 12), so a screw head has room | ISO 273 medium (H13), lib/standards/holes.csv. The screws are not built; the host places them |
| the keeper | caught behind the lip's inner face x 88, the lip reaching down to z 2 | design: the class value span (ETIM 10.0 EC011973, OPERATING.md 12); the keeper is the other part's and is not drawn |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four base holes carry a declared position tolerance Ø0.4 at MMC to A (the mounting face), B (the base's rear edge) and C (its
left edge) (features.csv; H − F = 5.5 − 5 = 0.5). The ISO 2768-m general tolerance of their 62.7 mm diagonal (±0.3, a Ø0.85 zone)
would not hold the pattern.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate (fixed) | 70 × 50 × 3 (x −30 to 40, y ±25, z 0 to 3) | the holes' edge distance 4.75 (y) and 5.25 (x) or more; 3 thick, so its short edges are skipped by the fillet rule |
| cheeks (fixed) | two, 24 × 3.0 × 19 (x −10 to 14, y ±13 to ±16, z 3 to 22), each bored Ø7 on the pivot axis | 1 clear round the pivot pin (features.csv, kind own); every point of them within 17.8 of the axis |
| pivot pin (node `lever`) | Ø5 × 35 (y ±17.5) on x 0, z 14 | through the cheeks 1 clear, pressed in the side plates, 1.5 proud of the cheeks |
| side plates (node `lever`) | two, 76 × 3.0 × 12 (x −6 to 70, y ±9 to ±12, z 8 to 20), each bored Ø5 at x 0 and x 24 | 1 clear inside the cheeks; their rear corners (8.5 from the axis) sweep 2.5 above the base |
| hook pin (node `lever`) | Ø5 × 27 (y ±13.5) on x 24, z 14 | pressed in the plates and the hook arms; 21.5 or more from the axis, so its sweep clears the cheeks |
| U-hook (node `lever`) | two arms 76 × 3.0 × 8 (x 20 to 96, y ±5 to ±8, z 10 to 18), each bored Ø5 at x 24; catch lip 8 × 16 × 8 (x 88 to 96, y ±8, z 2 to 10) under their front ends | 1 clear inside the plates; the lip's inner face x 88 is the span |
| handle (node `lever`) | 50 × 24 × 10 (x 60 to 110, y ±12, z 20 to 30) on the plates' front ends | the grip, red polyamide |
| travel | 90 degrees | the hook lifted clear of the keeper: the lip then stands 88 to 96 above the axis |
| layers | base, cheeks, side plates, hook `M-ZINC` (zinc-plated steel); pins `M-SILVER` (bright steel); handle `M-RED-PA` | a design choice, no finish claim |

## Mechanism
`lever` (rotate about axis (0, −1, 0), 0 to 90 degrees, pivot (0, 0, 14) on the pivot pin's axis): 0 is closed, as built (the side plates
level, their undersides at z 8, 5 above the base; the hook reaching toward +x); 90 is open (the handle and the hook lifted). The node
carries both pins, the side plates, the U-hook and the handle. MOT-010 sweeps it through the full range: the pivot pin turns on its own
axis 1 clear in the cheeks' bores, the side plates turn inside the cheeks (1 clear in y) and their rear corners never come lower than
z 5.5, and everything else in the node stands farther from the axis than any point of the cheeks, and above the base.
Not drawn (internal mechanism the twin doesn't read): the hook's own swing on its pin and the over-centre toggle that holds the clamp
closed; the hook is drawn riding with the lever. Not drawn either: the keeper (the other part's).

## Named nodes
`lever` (rotate). Colliders `base`, `cheeks` (axis-aligned boxes).

## Materials by layer
`M-ZINC` base, cheeks, side plates, hook · `M-SILVER` pivot pin, hook pin · `M-RED-PA` handle.

## Decals (Blender)
"complexes.org generic" on the base plate's −y face.

## Notes
No vendor names, part numbers or marks. No safety claim, no tensile force. The class values are the figures this design is meant to
meet; no calculation or test of the model is on file. No open figure: the base holes are on file, and the screws and the keeper are
placed by the host. The gate's fillet rule (r 0.5 for a device): the base is 3 thick, the cheeks, side plates and hook arms 3.0, so their
short edges are skipped; the lip and the handle are 8 or more on every edge; the holes' edges are cut edges. lib/materials.csv gives no
densities, so no mass is stated.

## Outputs (out/)
`clamp-toggle-hook.lsp` · `.glb` (pivot on `lever`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011973), our own design (mech-r130, unattended, 2026-11-12): a hook-type horizontal toggle clamp, the lever with the U-hook turning 90 degrees about its pivot, span 88 |
