# seal-tape-epdm · v1.0 · generic EPDM sponge sealing tape, self-adhesive, 15 x 5, 5 m roll

**What** a roll of closed-cell EPDM sponge sealing tape, self-adhesive on one face under a paper release liner: stuck along the joint
face of a cover, a guard's panel, an access door, a duct flange or a reservoir's inspection lid, and pressed flat when the joint is
closed, so dust, splash and draughts stay out. It is a joint seal, not a pressure seal: it holds no fluid under pressure and claims
none. A consumable: a machine places the roll in its store; a joint's spec does not draw the tape on its face. The default build is
5 m of 15 wide, 5 thick tape.
**Class** connector-part · **Baseline** our own design: generic sealing tape (ETIM 10.0 EC003185), as OPERATING.md 12 (generic
elements, EM 2026-11-07) says: the next ETIM class in the Seals group's order that builds, after seal-tape-ptfe's EC010670 (pneu-r103;
why the classes between them were passed over is in lib/rounds/pneu/r103.md section 2). EC003185's synonyms (butyl tape fleece, EPDM
foil, elasto cell band, glazing tape, joint sealing tape, sealing adhesive tape, sealing strip) name a family of adhesive joint tapes;
this element is its cellular-rubber form ("elasto cell band"), the one a machine's covers and guards use. No vendor file was opened or
measured. The class values below are its design inputs; its sizes are design choices; no vendor names; "generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. A sponge sealing tape is sold
by its width, its thickness and its length and cut to the joint: no standard on file fixes its section (lib/standards/sources.csv has
none for it), so its sizes are the design's.
**Units / frame** mm, Z up. Origin: the centre of the roll's underside (z = 0) on its axis; the roll lies flat, its axis along +z, the
tape's width along z.
**Built with** toolkit 1.3 · AutoLISP command `SEAL-TAPE-EPDM` · `size` (15x5; 10x3, 15x5, 20x10, width × thickness in mm) · `length`
(5000; 1000 to 25000 mm of tape on the roll, as long as the roll stays within Ø400).

## Class values (ETIM 10.0 EC003185)
Design inputs. EC003185 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, tube-pneu 1.0's, seal-strip-eptfe 1.0's and
seal-tape-ptfe 1.0's way). Until they are on file this table gives the values this tape is designed to under plain names; a later
minor restates them in ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| material | EPDM, closed-cell sponge, black |
| shape | tape, on a roll |
| adhesive | self-adhesive on one face, under a paper release liner (the adhesive's chemistry not stated) |
| width | 15 mm (parameter `size`: 10 or 20) |
| thickness | 5 mm uncompressed (parameter `size`: 3 or 10) |
| length | 5 m on the roll (parameter `length`, 1 to 25 m) |
| temperature range | not stated |
| fire behaviour | not stated: no fire class is claimed |
| max. pressure | not stated: a joint seal, not a pressure seal; it rates no pressure and claims none |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv: no check reads a sealing tape's figure, and the joint it seals carries its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| tape | 15 wide × 5 thick (10 × 3, 20 × 10 by `size`) | three common joint sections, a thin one for covers, the default for panels and doors, a thick one for uneven duct flanges; each at least 8 wide so the roll's height passes the AutoCAD gate's fillet pre-flight, and wider than it is thick (element.py asserts both) |
| core | Ø76 bore, wall 8, Ø92 outside, as wide as the tape; cardboard | a 3 in winding core, seal-strip-eptfe's; the tape's first turn sits on it face to face; the wall is 8 so every edge passes the fillet pre-flight |
| roll | Ø200.74 outside for 5 m of 15 × 5 | calculated, not chosen: the wound tape's end area, length × thickness, fills the annulus from the core, π / 4 × (D² − 92²) = 5000 × 5, so D = √(92² + 4 × 5000 × 5 / π) = 200.74 (outside_d() in element.py; 216.01 for 10 m of 10 × 3, 216.01 for 3 m of 20 × 10). The release liner's thickness is not counted, and the tape is drawn as one solid annulus: its turns and its loose end are not drawn |
| length range | 1 m to 25 m, Ø400 at most | 1 m is still 9.42 of wound tape radially for the thinnest section (the fillet pre-flight, asserted for every size); a size and length whose roll would pass Ø400 is refused (build() raises) |
| envelope | Ø200.74 × 15 (default) | the roll lies flat |

## Ports (toolkit/pneu.py)
None. The tape joins nothing by itself: it lies in a joint that the cover's or door's own fasteners close.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from them (the roll's outside diameter).

## Named nodes
None. Nothing moves; the roll and its core are the fixed body.

## Materials by layer
`M-GASKET` the tape (black rubber) · `M-BROWN` the core

## Decals (Blender)
None in 1.0 (a size label on the core's end face is a later version). No vendor names.

## Outputs (out/)
`seal-tape-epdm.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003185), pneu-r103 (unattended): a flat roll of self-adhesive EPDM sponge sealing tape on a cardboard core, seal-strip-eptfe 1.0's pattern, its outside diameter calculated from the tape's section and length; parameters `size` and `length`; no port, no node, no ratings |
