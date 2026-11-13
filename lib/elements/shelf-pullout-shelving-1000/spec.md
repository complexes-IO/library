# shelf-pullout-shelving-1000 · v1.0 · pull-out shelf for a shelf of a 1000 wide steel shelving bay, generic, painted steel, a 868 × 420 × 60 sheet tray on two grooved rails, pulling out 0 to 280

**What** A pull-out shelf that stands on the top face of any of the five shelves of a steel shelving bay, between its uprights. The
fixed body is one frame: two slide rails, painted steel bars 12 × 45 along the bay's depth (y 20 to 480), each 1 inside its uprights'
inner faces, with a groove 6 deep and 25 high along its inner face, joined behind by a tie 874 × 20 × 10 under the grooves. The moving
part is a painted steel sheet 1.5 folded to an open tray 868 × 420 × 60, standing 5 above the shelf and 3 inside the rails, with a
runner 8 × 21 along each side that rides in its rail's groove, 1 clear of the groove's bottom and 2 clear of its lips. The tray pulls
out 0 to 280 toward the bay's front; at full travel each runner keeps 150 of its 420 in its rail: a three-quarter extension. A finger
notch 120 × 30 in the tray's front wall is the grip. Every bay figure is read from shelving-steel 1.0 (`library.load("shelving-steel")`
in element.py); the bay is placed, never redrawn. The slide's balls, its stops and the rails' fixing to the shelf are the host's
assembly: none is drawn and no hole is modelled.
**Class** furniture · **Baseline** our own design: generic rack pull-out shelf (ETIM 10.0 EC004083 Rack pull-out shelf), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by name from
lib/toolkit/generic.py's mech order (lib/rounds/mech/r159.md, Proposed next), and EC004083 is a class not yet built that meets an
element on file (shelving-steel's shelves and uprights); its shape no dimensional standard fixes. No product was matched and no vendor
file was opened.
**Units / frame** mm, Z up. Origin: shelving-steel's own x and y, at the height of a shelf's top face, so the host places the pull-out at
the bay's origin raised to that shelf's top (z 150, 600, 1050, 1500 or 1950 in shelving-steel 1.0): the shelf's top face z = 0, the
middle of the bay's width x = 0, the front uprights' front faces y = 0; the bay's depth toward +y; the tray pulls out toward −y.
Extents x −449 to 449, y 20 to 480, z 0 to 65 (pushed in).
**Built with** toolkit 1.3 · AutoLISP command `SHPO1000` · no parameter.

## Class values (ETIM 10.0 EC004083)
Design inputs. EC004083 Rack pull-out shelf (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 6
features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the shelf is designed to under plain names, as door-shelving-1000 1.0 and wall-side-shelving-500
1.0 do (requests mech-8 and mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not
stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, shelving-steel's; the grade not stated) |
| the rack it fits | shelving-steel 1.0: bay 1000 × 500 × 2000 over 50 × 50 uprights, on any of its five shelves |
| width × depth × height | 898 × 460 × 65 over the rails, pushed in; the tray 868 × 420 × 60 |
| extension | three-quarter: 280 of the tray's 420 depth, toward the bay's front |
| slide | grooved rails with side runners; balls and stops not drawn |
| load capacity | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the shelf's top face | z 0 at x −450 to 450, y 0 to 500 (shelves between the uprights' inner faces, from the bay's front y 0 to its back 500); the rails and the tie stand on it, 20 inside its front and back edges | shelving-steel 1.0 (element.py W, D, UP, SH_TOPS, the shelves from y 0 to D) |
| the uprights | inner faces x ±450 at y 0 to 50 and 450 to 500; the rails' outer faces at x ±449, 1 inside them | shelving-steel 1.0 (element.py W, UP) |
| the shelf above | its underside 410 above this shelf's top (450 apart, 40 deep); the tray's top at 65 stays under it (asserted) | shelving-steel 1.0 (element.py SH_TOPS, SH_T) |

## Its own sizes (design choices; the bay's figures read from shelving-steel 1.0)
| item | value | why |
|---|---|---|
| rails | 12 × 45, y 20 to 480, x ±437 to ±449 | 1 clear of the uprights; every free edge 12 or more |
| grooves | 6 deep from the rails' inner faces, z 10 to 35 | leave lips 10 thick and a web 6 behind the runner |
| rear tie | 874 × 20 × 10 between the rails, y 460 to 480, z 0 to 10 | joins the rails into one frame under the grooves, 10 behind the tray |
| tray sheet | 1.5 | a tray sheet, not a structural part; under 3, so every sheet edge is thin to the gate's fillet check |
| tray | 868 × 420 × 60, x ±434, y 30 to 450, z 5 to 65, open on top | 3 inside the rails, 5 above the shelf, 10 behind the rails' front ends and 10 in front of the tie |
| runners | 8 × 21 × 420, x ±434 to ±442, z 12 to 33, on the tray's sides | in the grooves, 1 short of their bottoms and 2 clear of their lips |
| travel | 0 to 280 toward −y | each runner keeps 150 of its 420 (more than a third) in its rail at full travel; the tray's front then stands 250 in front of the uprights |
| grip | a notch 120 × 30 in the front wall, centred on x 0 | nothing stands proud of the tray |
| folds | drawn sharp (one box less one cutbox) | no bend radius is claimed |

## Mechanism
One moving node, the tray, a manual toggle (behaviour.csv): `tray` translates along (0, −1, 0) from 0 (pushed in) to 280 (pulled
out). The runners ride with it in the rails' grooves, clear of the lips (2) and the groove bottoms (1); the tray's sides stay 3 inside
the rails' inner faces and its bottom 5 above the shelf over the whole travel. At full travel the runners span y −250 to 170 and the
rails start at y 20, so 150 of each runner stays in its rail (asserted in element.py). Moving toward −y the tray never reaches the tie
behind it. No stop and no latched state: none is drawn.

## Named nodes
`tray` (translate). Colliders, axis-aligned boxes named apart from any node: `rail-l` (x −449 to −437, y 20 to 480, z 0 to 45),
`rail-r` (x 437 to 449), `tie` (x −437 to 437, y 460 to 480, z 0 to 10), `pan` (the tray's envelope: x −434 to 434, y 30 to 450,
z 5 to 65).

## Materials by layer
`M-STEEL-7035` the rails, the tie, the tray and its runners (painted steel, shelving-steel's layer).

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Each rail one box (12 × 460 × 45) less one cutbox for its groove; the tie one box; the tray one
box (868 × 420 × 60) less one cutbox from the top (865 × 417 inside it), which leaves the bottom and the four walls as one solid, less
one cutbox for the notch; each runner one box. Volume by hand (asserted in element.py): a rail 248400 − 6 × 460 × 25 = 179400 mm³; the
tie 874 × 20 × 10 = 174800; the tray 868 × 420 × 60 − 865 × 417 × 58.5 = 21873600 − 21101242.5 = 772357.5, less the notch 120 × 1.5 ×
30 = 5400, so 766957.5; a runner 8 × 420 × 21 = 70560; in all 1441677.5 mm³. Every bounding-box extreme lies on a face the cuts leave
standing (x ±449 on the rails' outer faces, y 20 and 480 on the rails' ends, z 0 on the rails' and the tie's bottoms, z 65 on the
tray's rims). Not drawn: the bay and its shelves, the slide's balls, its stops, any fixing.

## Outputs (out/)
`shelf-pullout-shelving-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004083), our own design (mech-r160, unattended, 2026-11-13): two grooved slide rails joined by a rear tie on a shelf of shelving-steel 1.0 and an open sheet tray 868 × 420 × 60 whose side runners ride in the grooves, pulling out 0 to 280 toward the bay's front with 150 of each runner kept in its rail; every bay figure read from shelving-steel |
