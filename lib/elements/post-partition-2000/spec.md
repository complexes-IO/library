# post-partition-2000 · v1.0 · post for a storage partition, generic, line post 2000 high, painted steel tube 50 x 50 x 2 on a floor plate 150 x 150 x 8 with 4 M10 anchor holes, six panel tabs with M8 holes

**What** A line post for a storage partition (a mesh partition wall, a storage cage's wall): the partition's panels stand between posts
and bolt to them. A painted steel tube 50 × 50 × 2, 2000 high and closed at its top, stands on a floor plate 150 × 150 × 8 that takes
4 M10 anchors (Ø11, ISO 273 medium). On each of its two side faces (−x and +x) three welded tabs 8 thick, 40 high and reaching 40 out,
at z 250, 1050 and 1850, each with an M8 hole (Ø9, ISO 273 medium) 20 out from the post's face. The tabs all lie on one side of the
post's centre plane (y −18 to −10), so a panel frame 20 deep bolted against their +y faces lies centred on the partition's line y = 0.
The panels, the door and the anchors are not drawn.
**Class** furniture · **Baseline** our own design: generic post for storage partition (ETIM 10.0 EC004104 Post for storage partition;
synonyms corner post, end post, middle post, storage partition attachment pillar), OPERATING.md 12 "Generic elements" (EM, 2026-11-07).
No inventory row names it: group EG010340 Storage and racking systems is walked by name from lib/toolkit/generic.py's mech order
(lib/rounds/mech/r164.md, Proposed next), and EC004104 is the first of the storage partition set (EC004103 element, EC004104 post,
EC004105 door) to build: the other two bolt to it (foundation first, OPERATING.md 12). Its shape no dimensional standard fixes. No
element draws a partition. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the floor under the post's axis: the floor plate's underside z = 0, the post's centre x = 0, y = 0;
the partition runs along x, y = 0 its centre plane. Extents x ±75, y ±75 (the floor plate), z 0 to 2000.
**Built with** toolkit 1.3 · AutoLISP command `PPRT2000` · no parameter · places no element.

## Class values (ETIM 10.0 EC004104)
Design inputs. EC004104 Post for storage partition (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2,
3 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the post is designed to under plain names, as rack-lifting-gear-1000 1.0 does (requests mech-8
and mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the design
has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, rack-lifting-gear-1000's); the grade not stated |
| type of post | line post (middle or end post of a straight run): tabs on two opposite faces; a corner or T post is not this element |
| height | 2000 |
| section | 50 × 50 tube, wall 2 |
| fixing | floor plate 150 × 150 × 8, 4 × M10 anchors |
| panel fixing | 3 × M8 per side, at z 250, 1050, 1850 |

No ratings.csv: no rating the checks read, and no load or impact figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the floor anchors | 4 × Ø11 holes at x, y = ±55, M10 clearance, ISO 273 medium (lib/standards/holes.csv); position Ø1.0 at MMC, floating fastener (features.csv); the anchors, nuts and washers are the host's, not drawn | ISO 273; ASME Y14.5 |
| a partition element's frame (EC004103, not built yet) | bolts with M8 through the tabs' Ø9 holes (ISO 273 medium; position Ø1.0 at MMC, features.csv) against the tabs' +y faces (y = −10); a frame tube 20 wide from x ±35 (10 clear of the post's face) to ±55 is centred on the holes (x ±45) and a frame 20 deep (y −10 to 10) on the partition's line; the fixing heights z 250, 1050, 1850, 800 apart | design choice (this element: the interface the partition element reads with library.load) |
| the M8 and M10 screws, nuts and washers | not drawn; common parts placed later | OPERATING.md 12 (model the holes, place the part later) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| post | tube 50 × 50 × 2, x, y ±25, z 7.5 to 2000 (0.5 into the floor plate), closed at its top by a solid 8 (z 1992 to 2000) | rack-lifting-gear-1000's tube, one box less one blind cutbox; the closed top keeps water and dirt out |
| floor plate | 150 × 150 × 8, x, y ±75, z 0 to 8 | carries the four anchors 24.5 clear of the post's faces (a nut and washer's room) and 14.5 from the plate's edges (asserted) |
| tabs | 40.5 × 8 × 40 (x 24.5 to 65, 0.5 into the tube's wall; y −18 to −10; z ±20 about 250, 1050, 1850), on both side faces | the M8 hole 15.5 from the post's face, the tab's end, top and bottom (asserted); inside the floor plate's outline in x (65 ≤ 65) |
| tab offset | the tabs at y −18 to −10, not on the centre plane | a panel frame 20 deep bolts beside the tabs, so the panels lie on the partition's line y = 0 |
| panel gap | 10 between the post's face and a panel frame's end | design choice; with the tabs' holes at x ±45 a 20-wide frame tube covers them |
| fixing heights | z 250, 1050, 1850 (800 apart; 230 above the floor to the lowest tab's bottom, 130 under the top to the highest tab's top) | three fixings per side; the lowest clears the floor plate and an anchor's nut |

## Mechanism
None. One fixed body, no node: bolting the panels to the tabs and anchoring the plate to the floor are the host's assembly, not a
motion (behaviour.csv: the header only).

## Named nodes
None. Colliders, axis-aligned boxes named apart from any node: `foot` (the floor plate), `post` (x, y ±25, z 8 to 2000), `tabs-l`
(x −65 to −25) and `tabs-r` (x 25 to 65), each y −18 to −10, z 230 to 1870 (the three tabs of a side).

## Materials by layer
`M-STEEL-7035` the whole post (painted steel, rack-lifting-gear-1000's layer); the tabs welded on and painted with it.

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as nine boxes in one material: the floor plate with four through holes, the post (one box
less one blind cutbox, open below onto the plate and closed at its top), and six tabs run 0.5 into the tube's wall, each with one
through hole. Every edge is 2 (the tube's wall), 8, 40 or more, none in the gate's 3 to 7 fillet trap. Volume by hand (asserted in
element.py): the plate 150² × 8 − 4 × π × 5.5² × 8 = 176958.9; the post 50² × 1992.5 − 46² × 1984.5 = 782048; a tab 40.5 × 8 × 40 −
π × 4.5² × 8 = 12451.1, six of them 74706.4; in all about 1033713.3 mm³ (the joints' 0.5 overlaps counted in both parts). Every
bounding-box extreme lies on an uncut face: x, y ±75 the floor plate's sides, z 0 its underside, z 2000 the post's top. Not drawn: the
partition's panels and door, the anchors, screws, nuts and washers.

## Outputs (out/)
`post-partition-2000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004104), our own design (mech-r165, unattended, 2026-11-13): a line post of painted steel tube 50 × 50 × 2, 2000 high and closed at its top, on a floor plate 150 × 150 × 8 with 4 M10 anchor holes, six welded tabs with M8 holes at z 250, 1050, 1850 for the partition's panels |
