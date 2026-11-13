# plinth-shelving-1000 · v1.0 · plinth panel (base cover) for the front of a 1000 wide steel shelving bay, generic, painted steel sheet 1.5, 896 × 40 × 108 channel

**What** A plinth panel (base cover) for the front of one bay of steel shelving: a painted steel sheet 1.5 thick, folded to a channel
open at the back and below, standing on the floor between the bay's two front uprights and closing the space under the lowest shelf,
so nothing rolls or is pushed under it. A front face 896 wide and 108 high, a top fold 40 deep and an end return 40 deep at each end.
It stands 2 clear of the uprights' inner faces and of the lowest shelf's underside, and its front face 2 behind the uprights' front
faces. Every bay figure is read from shelving-steel 1.0 (`library.load("shelving-steel")` in element.py); the bay is placed, never
redrawn. How the panel is held to the bay is the host's assembly: no fixing is drawn and no hole is modelled.
**Class** furniture · **Baseline** our own design: generic plinth panel (ETIM 10.0 EC004074; synonyms 19 inch plinth panel, base
cover for rack), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking
systems is walked by name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r155.md), and EC004074 is a class not yet built
that meets an element on file (shelving-steel's front uprights and lowest shelf); its shape no dimensional standard fixes. No product
was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: shelving-steel's own, so the host places the panel at the bay's origin: the floor z = 0, the
middle of the bay's width x = 0, the front uprights' front faces y = 0; the bay's depth toward +y. Extents x ±448, y 2 to 42, z 0 to
108.
**Built with** toolkit 1.3 · AutoLISP command `PLSH1000` · no parameter.

## Class values (ETIM 10.0 EC004074)
Design inputs. EC004074 Base/base element (rack element) (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems,
tier 2, 5 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory.
Until they are on file this table gives the values the panel is designed to under plain names, as guard-upright-80 1.0 and
bar-depth-support-1067 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order
with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel sheet, painted (the `M-STEEL-7035` layer, shelving-steel's; the grade not stated) |
| form | plinth panel: a channel folded from one sheet, open behind and below |
| the rack it fits | shelving-steel 1.0: bay 1000 wide over 50 × 50 uprights, lowest shelf's underside 110 above the floor |
| width | 896 (900 between the uprights' inner faces, less 2 each end) |
| height | 108 (the shelf's underside 110, less 2) |
| depth | 40 (the top fold and the end returns, the front face included) |
| fixing | not drawn: the host's assembly |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the uprights' inner faces | x ±450 (the bay 1000 wide over uprights 50 × 50); the end returns' outer faces at x ±448, 2 clear | shelving-steel 1.0 (element.py W, UP; read with library.load) |
| the lowest shelf | top 150, 40 deep: its underside 110; the panel's top 108, 2 clear | shelving-steel 1.0 (element.py SH_TOPS, SH_T) |
| the uprights' front faces | y = 0; the panel's front face at y 2, set back 2 | shelving-steel 1.0 (its origin) |
| the anchor plates | 50 wide, behind the front uprights at x ±(450 to 500), y 50 to 150; the panel lies inside x ±448 and in front of y 42, clear of them | shelving-steel 1.0 (element.py PL_W, PL_L) |
| the floor | z = 0; the panel's front face and returns stand on it | shelving-steel 1.0 (its origin) |

## Its own sizes (design choices; the bay's figures read from shelving-steel 1.0)
| item | value | why |
|---|---|---|
| sheet | 1.5 | a folded cover, not a structural part; under 3, so every sheet edge is thin to the gate's fillet check |
| clearances | 2 to each upright's inner face and to the shelf's underside | the panel is set in, never forced: it touches neither the uprights nor the shelf |
| set-back | 2 behind the uprights' front faces | the uprights' faces stay the bay's front |
| top fold and returns | 40 deep (the front face included) | they stiffen the sheet; every free edge other than the sheet's is 40 or more |
| folds | drawn sharp (one box less one cutbox) | no bend radius is claimed |

## Mechanism
None: one fixed body, no moving node, no port. Setting the panel into the bay and holding it there is the host's assembly.
behaviour.csv is the header only.

## Named nodes
None. One collider, an axis-aligned box named apart from any node: `plinth` (x ±448, y 2 to 42, z 0 to 108).

## Materials by layer
`M-STEEL-7035` the whole panel (painted steel, shelving-steel's layer).

## Decals (Blender)
No label: the panel's one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one box (896 × 40 × 108) less one cutbox from behind and below (893 × 38.5 × 106.5
inside it), which leaves the front face, the top fold and the two end returns as one solid. Volume by hand (asserted in element.py):
3870720 − 893 × 38.5 × 106.5 = 3870720 − 3661523.25 = 209196.75 mm³; by parts, the front 896 × 1.5 × 108 = 145152, the top fold
896 × 38.5 × 1.5 = 51744, the returns 2 × 1.5 × 38.5 × 106.5 = 12300.75. Every bounding-box extreme lies on an uncut face (x ±448 on
the returns' outer faces, y 2 on the front face, z 108 on the top, z 0 on the front face's foot); y 42 is the top fold's and the
returns' back edge. Not drawn: the bay, its uprights, anchor plates and shelves, any fixing.

## Outputs (out/)
`plinth-shelving-1000.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004074), our own design (mech-r155, unattended, 2026-11-13): a painted steel sheet 1.5 folded to a channel 896 x 40 x 108, standing on the floor between the two front uprights of shelving-steel 1.0, 2 clear of them and of the lowest shelf; every bay figure read from shelving-steel |
