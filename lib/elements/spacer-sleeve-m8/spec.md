# spacer-sleeve-m8 · v1.1 · spacer sleeve, generic, steel zinc plated, round D14 with an M8 clearance bore D9.0 (ISO 273 medium), cut to length (default 20)

**What** A spacer sleeve: the plain round steel bush an M8 screw passes through, set between two parts (a panel and its frame, a
bracket and a profile, a guard and its post) to hold them a fixed distance apart while the screw clamps them. Ø14 outside, a through
bore Ø9.0, cut to length (default 20). Placed by a host, never redrawn: a frame, a guard or a bracket that stands a part off its face
places it with the `length` it needs.
**Class** connector-part · **Baseline** our own design: generic spacer sleeve (ETIM 10.0 EC002334, whose synonyms name the bush, the
distance bush and the spacer bush), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it. It is the first
class of group EG021006 Accessories/components for fasteners and anchoring systems, in `python lib/build.py inventory mech`'s ETIM
order (lib/toolkit/generic.py ORDER: the tier-1 classes of the groups before it are built or skipped, mech-r143), whose shape no
dimensional standard fixes and whose use carries no rated load; the classes before it are skipped in lib/rounds/mech/r145.md ("What the recovered work is").
The class is in lib/standards/etim/classes.csv (tier 2, 6 features); its features are not in class-features.csv (tier 1 and inventory
classes only), so the class values below are this design's under plain names, as rack-cantilever's and shelving-steel's are under the
core's answers to mech-8 and mech-9, until the features come (needs-em 226). No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: one end face (its seat on the lower clamped part) z = 0, on the sleeve's axis. The axis runs along
+z; the other end face at z = `length`. Extents x ±7, y ±7, z 0 to 20 at the default length.
**Built with** toolkit 1.3 · AutoLISP command `SPACERSL` · parameter `length` (mm, default 20, 3 to 200).

## Class values
ETIM 10.0 class EC002334 Spacer sleeve (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md). Its 6 features are not on file
(class-features.csv holds tier 1 and inventory classes only), so the values are given under plain names, with the value this element is
designed to; when the features are on main, a 1.1 restates them in ETIM's order with their EF codes (the core's answer to mech-8). These
define the element; they are design inputs.

| # | feature (plain name) | value |
|---|---|---|
| 1 | Material | mild steel (lib/materials.csv `steel-mild`) |
| 2 | Surface protection | zinc plated (the `M-ZINC` layer; no coating thickness stated) |
| 3 | Outer diameter | 14 mm |
| 4 | Inner diameter | 9.0 mm, a through bore: ISO 273 medium clearance for M8 (lib/standards/holes.csv, 9.0 to 9.22, H13) |
| 5 | Length | the `length` parameter, default 20 mm (3 to 200; a BOM row sets it) |
| 6 | Shape | round, plain (no thread, no flange, no slot) |

No ratings.csv: no value above is a rating the checks read, and no load, torque or temperature figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the M8 screw through it | the bore Ø9.0, through, on the sleeve's axis | ISO 273 medium clearance for M8 (lib/standards/holes.csv); the screw is the host's element (screw-iso4762 / screw-iso4017, inventory rows not built yet: placed later) |
| the two parts it spaces | the end faces z = 0 and z = `length`, each a ring Ø9.0 to Ø14 | OPERATING.md 12, an own size: the host's faces bear on the rings; the head's and the nut's sizes are the screw standards' (not on file), so no bearing area on them is claimed |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| outside | Ø14, round | a wall 2.5 round the Ø9.0 bore; small enough to sit inside a 20 or 40 profile's face |
| bore | Ø9.0 through (features.csv: M8 clearance medium, kind clearance) | ISO 273 medium for M8, so an M8 screw passes with the clearance class the library's hosts use for M8 |
| length | 20 by default, `length` 3 to 200 | 20 stands a panel off a frame by a hand's grip; a host sets its own; under 3 is a washer's job, over 200 a tube's |
| layer | `M-ZINC` (steel, zinc plated) | a design choice, no grade or coating-thickness claim |
| volume | π × 7² × 20 − π × 4.5² × 20 = 3 078.8 − 1 272.3 = 1 806.4 mm³ at the default length | by hand, for the Blender volume (polygonal cylinders read a little less) |
| fillet radius | the gate's 0.5 | every edge a circle (Ø14 outside, the bore's edges are cut edges) |

## Mechanism
None: one fixed body, no moving node, no port. The screw through it and the parts it spaces are the host's assembly. behaviour.csv is
the header only.

## Named nodes
None. Collider, an axis-aligned box: `sleeve` (x ±7, y ±7, z 0 to `length`).

## Materials by layer
`M-ZINC` the whole sleeve (steel, zinc plated).

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default M-WHITE-PA,
M-BLACK-PA); M-ZINC is not one, and a sleeve Ø14 has no face a label would fit (needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. Drawn as one `cyl` less one through `hole`. Every bounding-box extreme lies on the cylinder's
own faces (z 0 and z = `length` the end rings, x and y ±7 the side). Not drawn: chamfers, the screw, a washer. lib/materials.csv gives
no densities, so no mass is stated.

## Outputs (out/)
`spacer-sleeve-m8.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002334), our own design (mech-r145, the 03:31 run's work, recovered; r145.md; unattended, 2026-11-13): a steel zinc plated sleeve Ø14 with an M8 clearance bore Ø9.0 (ISO 273 medium), length a parameter, default 20 |
| 1.1 | review mech-r145 finding 1 / spacer-sleeve-m8-1.0 finding 1 (mech-r159, unattended, 2026-11-13; text only, the model unchanged): the cross-references hold: the round is mech-r145 (the 03:31 run's work, recovered), the skipped classes are listed in lib/rounds/mech/r145.md, the class's features are needs-em 226; the 1.0 row's round corrected likewise. The class values stay under plain names: class-features.csv still has no EC002334 rows |
