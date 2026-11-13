# basin-bulk-shelving-440 · v1.0 · bulk material basin for one half of a shelf of a 1000 × 500 steel shelving bay, generic, painted steel sheet 1.5, 440 × 480 × 250 open tub, front lowered to 120

**What** A bulk material basin for a bay of steel shelving: a painted steel sheet 1.5 thick, folded to an open-topped tub 440 wide,
480 deep and 250 high, for loose goods (screws, nuts, small stock) taken out by hand or with a scoop. It stands on the bay's lowest
shelf in its left half, 5 clear of the left uprights' inner faces and 5 short of the bay's middle, 10 in from the shelf's front and
rear edges. Its front is lowered to 120 high over the first 100 of its depth, so the goods are reached from the front; the back and
the rest of the sides stand 250, which leaves 160 clear under the second shelf. The right half of the shelf takes the same part moved
450 in x; the shelf is symmetric about the bay's middle, so the moved part keeps the same clearances. Every bay figure is read from
shelving-steel 1.0 (`library.load("shelving-steel")` in element.py); the bay is placed, never redrawn. The basin stands on the shelf by
its own weight: no fixing is drawn and no hole is modelled.
**Class** furniture · **Baseline** our own design: generic bulk material basin (ETIM 10.0 EC004076; synonym rack bulk material
basin), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is
walked by name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r157.md), and EC004076 is a class not yet built that meets an
element on file (shelving-steel's shelves and uprights); its shape no dimensional standard fixes. No product was matched and no vendor
file was opened.
**Units / frame** mm, Z up. Origin: shelving-steel's own, so the host places the left basin at the bay's origin: the floor z = 0, the
middle of the bay's width x = 0, the front uprights' front faces y = 0; the bay's depth toward +y. The lowered front toward −y. The
right basin: the same placement moved 450 in +x. Extents x −445 to −5, y 10 to 490, z 150 to 400.
**Built with** toolkit 1.3 · AutoLISP command `BBSH440` · no parameter.

## Class values (ETIM 10.0 EC004076)
Design inputs. EC004076 Bulk material basin (rack element) (lib/standards/etim/classes.csv: group EG010340 Storage and racking
systems, tier 2, 7 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from
memory. Until they are on file this table gives the values the basin is designed to under plain names, as wall-side-shelving-500 1.0
and plinth-shelving-1000 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order
with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel sheet, painted (the `M-STEEL-7035` layer, shelving-steel's; the grade not stated) |
| form | open-topped tub folded from one sheet, front lowered for taking goods out |
| the rack it fits | shelving-steel 1.0: bay 1000 × 500 × 2000 over 50 × 50 uprights, shelves 40 deep with their tops at 150, 600, 1050, 1500 and 1950 |
| width | 440 (two to a shelf: 900 between the uprights' inner faces, less 5 at each upright and 5 each side of the middle) |
| depth | 480 (the shelf 500 deep, less 10 at the front and 10 at the back) |
| height | 250 (back and sides); the front 120, over the first 100 of the depth |
| capacity | not stated (no volume of goods is claimed) |
| fixing | none: it stands on the shelf |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the lowest shelf | top face z 150, x −450 to 450 between the uprights' inner faces, y 0 to 500; the basin's bottom on that face | shelving-steel 1.0 (element.py SH_TOPS[0], W, UP, D; read with library.load) |
| the left uprights' inner faces | x −450; the basin's left side at x −445, 5 clear | shelving-steel 1.0 (element.py W, UP) |
| the bay's middle | x 0; the basin's right side at x −5, 5 short of it; the moved right basin from x 5 to 445, 5 clear of the right uprights' inner faces at 450 | shelving-steel 1.0 (element.py W, UP) |
| the shelf's front and rear edges | y 0 and 500; the basin from y 10 to 490, 10 in | shelving-steel 1.0 (element.py D) |
| the second shelf | top face z 600, 40 deep, so its underside at 560; the basin's top at 400, 160 below it | shelving-steel 1.0 (element.py SH_TOPS[1], SH_T) |

## Its own sizes (design choices; the bay's figures read from shelving-steel 1.0)
| item | value | why |
|---|---|---|
| sheet | 1.5 | a light container, not a structural part; under 3, so every sheet edge is thin to the gate's fillet check |
| clearances | 5 to each upright and to the bay's middle, 10 in from the shelf's front and rear edges | two basins set on one shelf side by side, never forced against the uprights or each other |
| height | 250 | 160 left under the second shelf to reach in over the back |
| lowered front | 120 high over the first 100 of the depth | the goods are scooped out from the front; the side walls step down with it |
| folds | drawn sharp (one box less two cutboxes) | no bend radius is claimed |
| hand | one part for both halves: the right basin is the left one moved 450 in x | the shelf is symmetric about x = 0 (asserted), so no second part is needed |

## Mechanism
None: one fixed body, no moving node, no port. Setting the basin on the shelf is the host's assembly. behaviour.csv is the header
only.

## Named nodes
None. One collider, an axis-aligned box named apart from any node: `basin` (x −445 to −5, y 10 to 490, z 150 to 400).

## Materials by layer
`M-STEEL-7035` the whole basin (painted steel, shelving-steel's layer).

## Decals (Blender)
No label: the basin's one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one box (440 × 480 × 250) less one cutbox from the top (437 × 477 inside it, from 1.5
above the bottom up through the top), which leaves the bottom and the four walls as one solid, less a second cutbox over the front 100
of the depth from z 270 up, which lowers the front wall and the first 98.5 of each side wall to 120. Volume by hand (asserted in
element.py): the tub 52800000 − 437 × 477 × 248.5 = 52800000 − 51799576.5 = 1000423.5 mm³; the lowered front takes 440 × 1.5 × 130 +
2 × 1.5 × 98.5 × 130 = 85800 + 38415 = 124215 mm³; the basin 876208.5 mm³. Every bounding-box extreme lies on a face the first cutbox
leaves whole (x −445 and −5 on the side walls' outer faces, y 10 on the front wall's outer face below 270, y 490 on the back wall's,
z 150 on the bottom, z 400 on the back wall's top edge). Not drawn: the bay, its uprights and shelves, the goods, any label holder.

## Outputs (out/)
`basin-bulk-shelving-440.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004076), our own design (mech-r157, unattended, 2026-11-13): a painted steel sheet 1.5 folded to an open tub 440 x 480 x 250, front lowered to 120 over 100, standing on the lowest shelf of shelving-steel 1.0 in its left half, 5 clear of the uprights and of the middle, 10 in from the shelf's edges, 160 under the second shelf; the right half the same part moved 450 in x; every bay figure read from shelving-steel |
