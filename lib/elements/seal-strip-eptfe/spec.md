# seal-strip-eptfe · v1.0 · generic expanded PTFE sealing strip, 10 x 3, 10 m roll

**What** a roll of expanded PTFE sealing strip: a soft white strip, laid along a flange face or a cover's joint face and pressed flat
when the joint is bolted up, sealing a face that is not machined for an O-ring groove. Its use in the lane: the covers and inspection
plates of the pressureless vessels (tank, hyd-tank's cover, separator-oil-water's lid), a housing's split face. A
consumable: a machine places the roll in its store, and the joint that takes a length of it carries that length in its own spec. The
default build is 10 m of 10 × 3 strip.
**Class** connector-part · **Baseline** our own design: generic expanded PTFE sealing strip (ETIM 10.0 EC010669), as OPERATING.md 12
(generic elements, EM 2026-11-07) says: the next ETIM class `python lib/build.py inventory pneu` lists that builds (pneu-r101; why the
classes before it were passed over is in the round report, lib/rounds/pneu/r101.md section 2). No vendor file was opened or measured.
The class values below are its design inputs; its sizes are design choices; no vendor names; "generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes (an O-ring, a flange gasket cut to a flange
standard's sizes) from being generic. A sealing strip is sold by its section and its length and cut to the joint on site: no standard
fixes its section, so its sizes are the design's. A gasket cut from it to a flange is a later element, once its flange standard is on
file.
**Units / frame** mm, Z up. Origin: the centre of the roll's underside (z = 0) on its axis; the roll lies flat, its axis along +z, the
strip's width along z.
**Built with** toolkit 1.3 · AutoLISP command `SEAL-STRIP-EPTFE` · `size` (10x3; 10x3, 14x5, 20x7, width × thickness) · `length`
(10000; 1000 to 25000 mm of strip on the roll).

## Class values (ETIM 10.0 EC010669)
Design inputs. EC010669 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, tube-pneu 1.0's way). Until they are on file this
table gives the values this strip is designed to under plain names; a later minor restates them in ETIM's order with their EF codes,
"not stated" where the design has no value.

| feature | value |
|---|---|
| material | expanded PTFE (polytetrafluoroethylene), white |
| shape | strip, rectangular section |
| width | 10 mm (parameter `size`: 14 for 14x5, 20 for 20x7) |
| thickness | 3 mm before it is pressed (parameter `size`: 5 for 14x5, 7 for 20x7) |
| length | 10 m on the roll (parameter `length`, 1 to 25 m) |
| adhesive backing | not stated |
| temperature range | not stated |
| max. pressure | not stated: the class rates no pressure here and the strip claims none; a joint's pressure is its own part's (a pressureless cover in the lane's use) |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv: no check reads a sealing strip's figure, and the joint it seals carries its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| strip section | 10 × 3 (14 × 5, 20 × 7 by `size`) | three sections that cover a narrow cover joint, a flange face and a wide vessel lid; each at least 8 wide so the roll's height passes the AutoCAD gate's fillet pre-flight (element.py asserts it) |
| core | Ø76 bore (a 3 in winding core), wall 8, Ø92 outside, as wide as the strip; cardboard | the strip's first turn sits on it face to face; the wall is 8 so every edge passes the fillet pre-flight |
| roll | Ø216.01 outside for 10 m of 10 × 3 | calculated, not chosen: the wound strip's end area, length × thickness, fills the annulus from the core, π / 4 × (D² − 92²) = 10000 × 3, so D = √(92² + 4 × 10000 × 3 / π) = 216.01 (outside_d() in element.py; 200.74 for 5 m of 14 × 5, 230.28 for 5 m of 20 × 7). The strip is drawn as one solid annulus: its turns and its loose end are not drawn |
| envelope | Ø216.01 × 10 (default) | the roll lies flat; at most Ø400 (element.py refuses a larger roll) |

## Ports (toolkit/pneu.py)
None. A sealing strip joins nothing by itself: it lies between two faces that the joint's own fasteners hold.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from them (the roll's outside diameter).

## Named nodes
None. Nothing moves; the roll and its core are the fixed body.

## Materials by layer
`M-WHITE-PVC` the strip (the white material on file closest to PTFE's look) · `M-BROWN` the cardboard core

## Decals (Blender)
None in 1.0 (a size label on the core's end face is a later version). No vendor names.

## Outputs (out/)
`seal-strip-eptfe.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010669), pneu-r101 (unattended): a flat roll of strip on a cardboard core, its outside diameter calculated from the strip's section and length; parameters `size` and `length`; no port, no node, no ratings |
