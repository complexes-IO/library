# bar-depth-support-1067 · v1.0 · depth support bar for a 1067 deep pallet rack frame, generic, zinc-plated steel, inverted U 40 × 30, end lips hooking over the front and back beams

**What** A depth support bar (front-to-rear support) for one beam level of the pallet rack: a zinc-plated steel bar laid front to rear
across the level's front and back beams, so a pallet, or a load narrower than the frame, has a bearing between the beams. An inverted
U 40 wide and 30 high (a top 8 thick on two webs 8 thick, open below); its webs bear on the beams' tops. At each end a lip 8 thick
hangs 60 down outside the beam's outer face, 2 clear of it, so the bar cannot slide off toward the aisle or the back. Every rack figure
is read from pallet-rack 1.1 (`library.load("pallet-rack")` in element.py); the beams are placed, never redrawn. Where along the beams
the bar sits, and how many a level takes, is the host's assembly.
**Class** furniture · **Baseline** our own design: generic depth support bar (ETIM 10.0 EC004078; synonyms rack front-to-rear support,
rack push-through protection), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage
and racking systems is walked by name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r154.md), and EC004078 is a class not
yet built that meets an element on file (pallet-rack's beams); its shape no dimensional standard fixes. No product was matched and no
vendor file was opened.
**Units / frame** mm, Z up. Origin: the front beam's outer face y = 0, the beams' top face z = 0 (the plane the webs bear on), the
bar's centre plane x = 0; the bar runs +y from the aisle toward the back beam. Extents x ±20, y −10 to 1077, z −60 to 30.
**Built with** toolkit 1.3 · AutoLISP command `BDS1067` · no parameter.

## Class values (ETIM 10.0 EC004078)
Design inputs. EC004078 Depth support bar (rack element) (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems,
tier 2, 6 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory.
Until they are on file this table gives the values the bar is designed to under plain names, as guard-upright-80 1.0 and
rack-cantilever 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order with
their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, zinc-plated (the `M-ZINC` layer; the grade not stated) |
| form | inverted U bar, open below, with a hooked lip at each end |
| the rack it fits | pallet-rack 1.1: frame depth 1067, beams 50 deep × 120 high |
| length | 1087 overall (lip to lip); 1071 between the lips' inner faces |
| section | 40 wide × 30 high; top and webs 8 |
| fixing | none: laid on, held front and back by its lips |

No ratings.csv: no rating the checks read, and no load, deflection or push-through figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the frame's depth | 1067, the front beam's outer face to the back beam's outer face; the lips' inner faces 2 clear of both | pallet-rack 1.1 (element.py DEPTH; read with library.load) |
| the beams' section | 50 deep × 120 high; the webs bear on the beams' tops (z = 0 here); the lips hang 60 down their outer faces, above their underside | pallet-rack 1.1 (element.py BEAM_D, BEAM_H) |
| the clear between the beams | 967 (1067 − 2 × 50); the bar spans it with nothing below its webs | pallet-rack 1.1, by hand |
| the pallet | sits on the bar's top (z 30) where bars are fitted; its 76 overhang past each beam (pallet-rack OVER) lies above the lips, whose top is the bar's top | pallet-rack 1.1 (element.py OVER), the pallet element; the host's assembly |

## Its own sizes (design choices; the rack's figures read from pallet-rack 1.1)
| item | value | why |
|---|---|---|
| section | 40 × 30, top and webs 8, 24 between the webs | every free edge 8 or more, clear of the gate's 3 to 7 mm trap; two webs bear on each beam |
| lip clearance | 2 from each beam's outer face | the bar is laid on, never forced: it never touches the beams' faces |
| lips | 40 × 8, from 60 below the beams' tops to the bar's top (90 high) | they stop the bar sliding off front or back; 60 is half the beam's 120 face, so they never reach its underside |
| joints | the bar runs 0.5 into each lip (one solid) | a welded or formed end; no weld size or bend radius is claimed |

## Mechanism
None: one fixed body, no moving node, no port. Laying the bar across the beams is the host's assembly. behaviour.csv is the header only.

## Named nodes
None. Three colliders, axis-aligned boxes named apart from any node: `bar` (x ±20, y −2 to 1069, z 0 to 30), `lip-front` (y −10 to
−2) and `lip-back` (y 1069 to 1077), both x ±20, z −60 to 30.

## Materials by layer
`M-ZINC` the whole bar (zinc-plated steel, strut's layer).

## Decals (Blender)
No label: the bar's one layer, `M-ZINC`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one box less one cutbox from below (the inverted U, 1072 long, 0.5 into each lip) and
two boxes for the lips. Volume by hand (asserted in element.py): the U (40 × 30 − 24 × 22) × 1072 = 672 × 1072 = 720384; the lips 2 × 40
× 8 × 90 = 57600; together 777984 mm³ as drawn, the joints' 0.5 overlaps (672) counted twice; the solid bar 777312 mm³. Every
bounding-box extreme lies on an uncut face (x ±20 on the webs' and lips' outer faces, y −10 and 1077 and z −60 on the lips, z 30 on
the top). Not drawn: the rack, its beams, the pallet.

## Outputs (out/)
`bar-depth-support-1067.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004078), our own design (mech-r154, unattended, 2026-11-13): an inverted-U zinc-plated steel bar 40 x 30 laid front to rear across one beam level of pallet-rack 1.1, its webs on the beams' tops, a lip 8 thick hanging 60 down outside each beam, 2 clear; every rack figure read from pallet-rack |
