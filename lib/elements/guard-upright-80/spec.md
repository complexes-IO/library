# guard-upright-80 · v1.0 · ram protection for an 80 × 80 pallet rack upright, generic, U-shaped steel guard 196 × 138 × 400, walls 8, floor flange with 2 M12 anchor holes

**What** A U-shaped ram protection (column guard) for one upright of the pallet rack: a painted steel U that stands on the floor round
the upright's front and both sides, open toward the frame's depth, so a truck's fork or wheel striking from the aisle meets the guard
before the upright. A front wall and two side walls, each 8 thick and 400 high, stand 15 clear of the upright's 150 × 150 footplate all
round (50 clear of the upright itself); a floor flange 60 deep in front of the front wall takes 2 M12 anchors (Ø13.5, ISO 273 medium).
The guard stands free of the rack: it touches neither the upright, its footplate and anchors, the frame's bracing, nor the bay's
floor-level pallet space. Every rack figure is read from pallet-rack 1.1 (`library.load("pallet-rack")` in element.py); the upright is
placed, never redrawn.
**Class** furniture · **Baseline** our own design: generic ram protection (ETIM 10.0 EC004073; synonyms pillar protection, rack ram
protection, U-ram protection), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage
and racking systems is walked by name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r153.md), and EC004073 is the first of
its classes not yet built that meets an element on file (pallet-rack); its shape no dimensional standard fixes. No product was matched
and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the floor z = 0 on the protected upright's centre line (x = 0, y = 0 its centre); the aisle, the
guarded front, toward −y; the frame's depth toward +y. Extents x ±98, y −158 to 40, z 0 to 400.
**Built with** toolkit 1.3 · AutoLISP command `GUPR80` · no parameter.

## Class values (ETIM 10.0 EC004073)
Design inputs. EC004073 Ram protection (for rack element) (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems,
tier 2, 5 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory.
Until they are on file this table gives the values the guard is designed to under plain names, as rack-cantilever 1.0 and
bracket-angle-strut-41 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order
with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted yellow (the `M-YELLOW` layer; the grade not stated) |
| form | U-shaped ram protection, front and both sides of one upright, open toward the frame |
| the upright it protects | pallet-rack 1.1: 80 × 80, on a 150 × 150 × 6 footplate |
| outside size | 196 wide × 138 deep (walls) + 60 flange, 400 high |
| wall thickness | 8 |
| fixing | 2 × M12 anchors through Ø13.5 holes (ISO 273 medium) in the front floor flange |

No ratings.csv: no rating the checks read, and no impact, energy or load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the upright's section | 80 × 80; the guard's inside is 180 wide, 50 clear of the upright's faces at the front and sides | pallet-rack 1.1 (element.py UP_W, UP_D; read with library.load) |
| the upright's footplate | 150 × 150, centred on the upright; the walls' inner faces 15 clear of its edges, so its anchors and their nuts stay free | pallet-rack 1.1 (element.py FOOT) |
| the frame's bracing | starts at the upright's back face (y = 40 here); the side walls end level with it, outside it in x | pallet-rack 1.1 (element.py, bracing between the uprights' inner faces) |
| the bay's floor-level pallet | its nearest edge 100 from the upright's inner face (140 from its centre); the guard's side face is at 98 | pallet-rack 1.1 (element.py GAP) |
| the M12 anchors | Ø13.5 clearance, ISO 273 medium (lib/standards/holes.csv); position Ø1.5 at MMC, floating fastener (features.csv); the anchors, nuts and washers are the host's, not drawn | ISO 273; ASME Y14.5 |

## Its own sizes (design choices; the rack's figures read from pallet-rack 1.1)
| item | value | why |
|---|---|---|
| inside clearance | 15 from the footplate's edge to each wall's inner face | the guard stands free: a struck guard deflects before it reaches the footplate's anchors |
| walls | 8 thick, 400 high | every free edge 8 or more, clear of the gate's 3 to 7 mm trap; 400 a design height, with no claim of what it stops |
| side walls | from the front wall to the upright's back face (y −90.5 to 40) | they cover both sides of the upright and stop where the frame's bracing begins |
| floor flange | 196 × 60 × 8 in front of the front wall | the anchors in the aisle side, so nothing of the guard reaches into the bay's floor-level pallet space |
| anchor holes | 2 × Ø13.5 at x ±60, 30 in front of the front wall | 23.25 of flange between each hole's edge and the wall, and between it and the flange's front edge; 31.25 to its side |
| joints | each side wall runs 0.5 into the front wall, the flange 0.5 into it (one solid) | a welded or formed U; no weld size or bend radius is claimed |

## Mechanism
None: one fixed body, no moving node, no port. Anchoring the guard to the floor is the host's assembly. behaviour.csv is the header only.

## Named nodes
None. Four colliders, axis-aligned boxes named apart from any node: `wall-front` (x ±98, y −98 to −90, z 0 to 400), `wall-left`
(x −98 to −90, y −90 to 40), `wall-right` (x 90 to 98, y −90 to 40), both z 0 to 400, and `flange` (x ±98, y −158 to −98, z 0 to 8),
so the space round the upright stays free.

## Materials by layer
`M-YELLOW` the whole guard (painted steel, the rack beams' yellow).

## Decals (Blender)
No label: the guard's one layer, `M-YELLOW`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as four boxes in one material: the front wall, the two side walls run 0.5 into it, and the
floor flange run 0.5 into it with two through holes. Volume by hand: front wall 196 × 8 × 400 = 627200; side walls 2 × 8 × 130.5 × 400 =
835200; flange 196 × 60.5 × 8 − 2 × π × 6.75² × 8 = 94864 − 2290.2 = 92573.8; together 1554973.8 mm³ (the joints' 0.5 overlaps counted,
3984). Not drawn: the rack, the anchors and their nuts and washers.

## Outputs (out/)
`guard-upright-80.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004073), our own design (mech-r153, unattended, 2026-11-13): a U-shaped ram protection round one upright of pallet-rack 1.1, walls 8 thick and 400 high 15 clear of the footplate, 2 M12 anchor holes in a front floor flange, every rack figure read from pallet-rack |
