# wall-side-shelving-500 · v1.0 · side wall for one open side of a 500 deep steel shelving bay, generic, painted steel sheet 1.5, 396 × 1976 tray with 20 flanges

**What** A side wall for one open side of a bay of steel shelving: a painted steel sheet 1.5 thick, folded to a shallow tray, a face
396 wide and 1976 high with a flange 20 deep on each of its four edges, turned in toward the shelves. It stands in the left uprights'
band (x −500 to −450) between the front and the rear upright and closes the side, so goods are not pushed out sideways. It stands 2
clear of each upright, 2 above the anchor plates and 2 below the uprights' tops; its face is 2 inside the bay's outside plane and its
flanges' edges 28 clear of the shelves' ends. The right side takes the same part turned 180° about the bay's vertical centre line (x
= 0, y = 250), which maps the part's y band 52 to 448 onto itself. Every bay figure is read from shelving-steel 1.0
(`library.load("shelving-steel")` in element.py); the bay is placed, never redrawn. How the wall is held to the bay is the host's
assembly: no fixing is drawn and no hole is modelled.
**Class** furniture · **Baseline** our own design: generic side wall (ETIM 10.0 EC004075; synonyms side panel (rack element), shelf
wall, rack wall, partition for rack block), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group
EG010340 Storage and racking systems is walked by name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r156.md), and
EC004075 is a class not yet built that meets an element on file (shelving-steel's uprights, anchor plates and shelves); its shape no
dimensional standard fixes. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: shelving-steel's own, so the host places the left wall at the bay's origin: the floor z = 0, the
middle of the bay's width x = 0, the front uprights' front faces y = 0; the bay's depth toward +y. The face toward −x, the flanges
toward +x. The right wall: the same placement turned 180° about the vertical line x = 0, y = 250. Extents x −498 to −478, y 52 to
448, z 22 to 1998.
**Built with** toolkit 1.3 · AutoLISP command `WSSH500` · no parameter.

## Class values (ETIM 10.0 EC004075)
Design inputs. EC004075 Side wall/partition (rack element) (lib/standards/etim/classes.csv: group EG010340 Storage and racking
systems, tier 2, 10 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from
memory. Until they are on file this table gives the values the wall is designed to under plain names, as plinth-shelving-1000 1.0 and
bar-depth-support-1067 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order
with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel sheet, painted (the `M-STEEL-7035` layer, shelving-steel's; the grade not stated) |
| form | side wall: a shallow tray folded from one sheet, flanges on four edges, open toward the shelves |
| the rack it fits | shelving-steel 1.0: bay 1000 × 500 × 2000 over 50 × 50 uprights, anchor plates 20 thick |
| width | 396 (400 between the front and the rear upright, less 2 each end) |
| height | 1976 (from 22, 2 above the anchor plates, to 1998, 2 below the uprights' tops) |
| depth | 20 (the flanges, the face included) |
| perforation | none |
| fixing | not drawn: the host's assembly |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the front and the rear upright | y 0 to 50 and 450 to 500 (the bay 500 deep over uprights 50 × 50); the wall's end flanges at y 52 and 448, 2 clear | shelving-steel 1.0 (element.py D, UP; read with library.load) |
| the bay's outside plane | x −500 (the left uprights' outer faces); the wall's face at x −498, 2 inside it | shelving-steel 1.0 (element.py W) |
| the shelves | x ±450 (between the uprights' inner faces); the flanges' edges at x −478, 28 clear of their ends | shelving-steel 1.0 (element.py W, UP) |
| the anchor plates | 20 thick, in the uprights' band behind the front upright and in front of the rear one; the wall's foot at z 22, 2 above them | shelving-steel 1.0 (element.py PL_T, PL_L) |
| the uprights' tops | z 2000; the wall's top at 1998, 2 below them | shelving-steel 1.0 (element.py H) |

## Its own sizes (design choices; the bay's figures read from shelving-steel 1.0)
| item | value | why |
|---|---|---|
| sheet | 1.5 | a cladding sheet, not a structural part; under 3, so every sheet edge is thin to the gate's fillet check |
| clearances | 2 to each upright, to the anchor plates and to the uprights' tops | the wall is set in, never forced: it touches no part of the bay |
| set-in | 2 inside the bay's outside plane | the uprights' outer faces stay the bay's side |
| flanges | 20 deep (the face included), on all four edges, turned in | they stiffen the tall sheet; every free edge other than the sheet's is 20 or more |
| folds | drawn sharp (one box less one cutbox) | no bend radius is claimed |
| hand | one part for both sides: the right wall is the left one turned 180° about x = 0, y = 250 | the part is symmetric in y about the bay's middle (asserted), so no mirrored part is needed |

## Mechanism
None: one fixed body, no moving node, no port. Setting the wall into the bay and holding it there is the host's assembly.
behaviour.csv is the header only.

## Named nodes
None. One collider, an axis-aligned box named apart from any node: `wall` (x −498 to −478, y 52 to 448, z 22 to 1998).

## Materials by layer
`M-STEEL-7035` the whole wall (painted steel, shelving-steel's layer).

## Decals (Blender)
No label: the wall's one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one box (20 × 396 × 1976) less one cutbox from the shelves' side (18.5 × 393 × 1973
inside it), which leaves the face and the four flanges as one solid. Volume by hand (asserted in element.py): 15649920 − 18.5 × 393 ×
1973 = 15649920 − 14344696.5 = 1305223.5 mm³; by parts, the face 1.5 × 396 × 1976 = 1173744, the top and bottom flanges 2 × 18.5 ×
396 × 1.5 = 21978, the end flanges 2 × 18.5 × 1.5 × 1973 = 109501.5. Every bounding-box extreme lies on an uncut face (x −498 on the
face's outer side, y 52 and 448 on the end flanges' outer faces, z 22 and 1998 on the bottom and top flanges' outer faces); x −478 is
the flanges' edge. Not drawn: the bay, its uprights, anchor plates and shelves, any fixing.

## Outputs (out/)
`wall-side-shelving-500.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004075), our own design (mech-r156, unattended, 2026-11-13): a painted steel sheet 1.5 folded to a tray 396 x 1976 with 20 flanges, standing in the left uprights' band of shelving-steel 1.0 between the front and the rear upright, 2 clear of them, of the anchor plates and of the uprights' tops; the right side the same part turned 180 degrees; every bay figure read from shelving-steel |
