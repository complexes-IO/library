# door-shelving-1000 · v1.0 · door pair for the open front of a 1000 wide steel shelving bay, generic, painted steel, two 498 × 1980 sheet leaves 1.5 on 50 × 20 jambs, each opening 0 to 90 degrees

**What** A pair of doors for the open front of a bay of steel shelving. Two jambs, painted steel bars 50 × 20, stand on the floor
against the front uprights' front faces, floor to the uprights' tops, joined at the top by a head 900 × 20 × 40 above the top shelf:
the fixed body, one frame. Two leaves, each a painted steel sheet 1.5 folded
to a shallow tray (a face 498 wide and 1980 high with a flange 20 deep on each of its four edges, turned in toward the bay), hang 2 in
front of the jambs with 4 between them. Each leaf turns 0 to 90 degrees outward about its outer front edge, where a concealed hinge's
pivot lies, so at every angle the leaf stays within its bay's width (x −500 to 500), never comes within 2 of the jambs, and the two
leaves' swept spaces stay apart: a bay beside it can carry its own doors. A finger notch 30 × 120 in each leaf's free edge is the grip.
Every bay figure is read from shelving-steel 1.0 (`library.load("shelving-steel")` in element.py); the bay is placed, never redrawn.
Hinges, lock and the jambs' fixing are the host's assembly: none is drawn and no hole is modelled.
**Class** furniture · **Baseline** our own design: generic rack door (ETIM 10.0 EC004077 Door (rack element); synonyms extension door,
rack door), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is
walked by name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r158.md, Proposed next), and EC004077 is a class not yet built
that meets an element on file (shelving-steel's uprights); its shape no dimensional standard fixes. No product was matched and no vendor
file was opened.
**Units / frame** mm, Z up. Origin: shelving-steel's own, so the host places the doors at the bay's origin: the floor z = 0, the middle
of the bay's width x = 0, the front uprights' front faces y = 0; the jambs and the leaves in front of that plane, toward −y. Extents x
−500 to 500, y −42 to 0, z 0 to 2000 (closed).
**Built with** toolkit 1.3 · AutoLISP command `DRSH1000` · no parameter.

## Class values (ETIM 10.0 EC004077)
Design inputs. EC004077 Door (rack element) (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 4
features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the doors are designed to under plain names, as wall-side-shelving-500 1.0 and
box-assortment-340x240 1.0 do (requests mech-8 and mech-9, the core's answers); a later minor version restates them in ETIM's order
with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, shelving-steel's; the grade not stated) |
| form | double door, hinged leaves (two leaves on two jambs) |
| the rack it fits | shelving-steel 1.0: bay 1000 × 500 × 2000 over 50 × 50 uprights |
| width × height | 1000 × 2000 over the jambs; each leaf 498 × 1980 |
| opening | 0 to 90 degrees each leaf, outward |
| lock | none drawn |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the front uprights | x −500 to −450 and 450 to 500, front faces y 0, floor to z 2000; the jambs stand against those faces over the same width and height | shelving-steel 1.0 (element.py W, UP, H; read with library.load) |
| the bay's outside planes | x ±500; the leaves' outer edges on them, and at every angle of their swing inside them (asserted) | shelving-steel 1.0 (element.py W) |
| the shelves | their front edges at y 0 (between the uprights); the leaves' backs at y −22, 22 in front of them; the top shelf's top at z 1950, the head from 1960 (asserted) | shelving-steel 1.0 (element.py SH_TOPS, the shelves from y 0) |

## Its own sizes (design choices; the bay's figures read from shelving-steel 1.0)
| item | value | why |
|---|---|---|
| jambs | 50 × 20, floor to 2000 | the uprights' face width and height, so the jambs read as the uprights' front; deep enough that every free edge is 20 or more |
| head | 900 × 20 × 40, between the jambs at z 1960 to 2000 | joins the jambs into one frame (the build's GEO-070 found two loose jambs in 1.0's first build), above the top shelf and behind the leaves' swing (y −20 to 0) |
| leaf sheet | 1.5 | a door sheet, not a structural part; under 3, so every sheet edge is thin to the gate's fillet check |
| leaf flanges | 20 deep (the face included), on all four edges, turned in | they stiffen the tall sheet |
| leaf clearances | 2 in front of the jambs; 10 above the floor and 10 below the uprights' tops; 4 between the leaves | the leaves touch nothing at rest or in their swing |
| hinge axis | each leaf's outer front edge (x ±500, y −42) | the pivot of a concealed hinge on an overlay door: the leaf's every point stays at x' ≥ 0 from it and y' ≤ 20 behind its face, so it never leaves the bay's width and stays 2 clear of the jambs; the free corner sweeps a radius of 498.4 (√(498² + 20²)), 3.6 short of the other leaf's edge at x ±2 (asserted) |
| swing | 0 to 90 degrees | at 90 the leaf lies against its own bay's side plane (x −500 to −480 for the left); past 90 it would leave the bay's width |
| grip | a notch 30 × 120 in each leaf's free edge, centred at z 1000 | the two notches make a 64 × 120 opening for the fingers; nothing stands proud of the face, so nothing sweeps past the bay's side |
| folds | drawn sharp (one box less one cutbox per leaf) | no bend radius is claimed |

## Mechanism
Two moving nodes, the leaves, each a manual toggle (behaviour.csv): `door-l` rotates about the vertical axis through (−500, −42) from 0
(shut) to −90 degrees (open); `door-r` about the axis through (500, −42) from 0 to 90 degrees. The sign: a negative turn about +z
swings the left leaf's free edge toward −y, outward, as door-oven 1.0's left leaf. Worked for the left leaf (the right mirrors it): a
point (dx, dy) from the hinge, dx 0 to 498, dy 0 to 20, turned by a in [−90, 0], lies at x' = dx cos a − dy sin a ≥ 0 and y' = dx
sin a + dy cos a ≤ 20, so at x ≥ −500 and y ≤ −22; element.py asserts it at every degree for the leaf's four corners. With both leaves
open together they stay in x −500 to −1.6 and 1.6 to 500. No lock and no latched state: none is drawn.

## Named nodes
`door-l`, `door-r` (rotate). Colliders, axis-aligned boxes named apart from any node: `jamb-l` (x −500 to −450, y −20 to 0, z 0 to
2000), `jamb-r` (x 450 to 500), `head` (x −450 to 450, y −20 to 0, z 1960 to 2000), `leaf-l` (x −500 to −2, y −42 to −22, z 10 to 1990), `leaf-r` (x 2 to 500).

## Materials by layer
`M-STEEL-7035` the jambs and the leaves (painted steel, shelving-steel's layer).

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Each jamb and the head one box; each leaf one box (498 × 20 × 1980) less one cutbox from the bay's side
(495 × 18.5 × 1977 inside it), which leaves the face and the four flanges as one solid, less one cutbox for the notch. Volume by hand
(asserted in element.py): a leaf's tray 19720800 − 495 × 18.5 × 1977 = 19720800 − 18104377.5 = 1616422.5 mm³, less the notch 120 ×
(30 × 1.5 + 1.5 × 18.5) = 8730, so 1607692.5 a leaf; the jambs 50 × 20 × 2000 = 2000000 each; the head 900 × 20 × 40 = 720000; in all 7935385 mm³. Every bounding-box
extreme lies on an uncut face (x ±500 on the jambs' and the leaves' outer faces, y −42 on the leaves' faces away from the notch, y 0 on
the jambs' backs, z 0 and 2000 on the jambs' ends). Not drawn: the bay, its uprights and shelves, the hinges, a lock, any fixing.

## Outputs (out/)
`door-shelving-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004077), our own design (mech-r159, unattended, 2026-11-13): a frame of two jambs 50 × 20 and a head on shelving-steel 1.0's front uprights and two folded sheet leaves 498 × 1980 in front of them, each turning 0 to 90 degrees outward about its outer front edge, so it never leaves the bay's width; every bay figure read from shelving-steel |
