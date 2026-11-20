# rack-cable-drum-1000 · v1.0 · cable drum rack, free-standing, generic, 1000 clear between two side frames of painted steel tube 50 x 50 x 2, two removable axles Ø40 for drums up to Ø700 x 960

**What** A free-standing cable drum rack: cable drums hang on two removable axles, one above the other, between two side frames, and
turn on them as cable is paid out to the front. Each side frame is painted steel tube 50 × 50 × 2: an upright 1600 high standing on the
middle of a foot 700 long laid front to back. A top bar joins the uprights' tops and a floor tie joins the feet's rear ends, both 1000
long between the frames' inner faces. Each axle is a round bright-steel bar Ø40 × 1180 through Ø42 bores in both uprights; it draws out
sideways to take a drum on. The drums and the axles' retention (a pin or a collar at each end) are not drawn.
**Class** furniture · **Baseline** our own design: generic cable drum rack (ETIM 10.0 EC004067 Cable drum rack), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by name from
lib/toolkit/generic.py's mech order (lib/rounds/mech/r162.md, Proposed next), and EC004067 is a class not yet built; its shape no
dimensional standard fixes. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the floor under the middle of the rack: the feet's undersides z = 0, midway between the side frames
x = 0, the axles' axis (the uprights' middle) y = 0; cable pays out toward −y. Extents x −590 to 590 (the axles' ends), y −350 to 350
(the feet), z 0 to 1650.
**Built with** toolkit 1.3 · AutoLISP command `RCDR1000` · no parameter · places no element.

## Class values (ETIM 10.0 EC004067)
Design inputs. EC004067 Cable drum rack (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 7
features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the rack is designed to under plain names, as rack-bins-1000 1.0 does (requests mech-8 and
mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the design
has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel: the frame painted (the `M-STEEL-7035` layer, rack-bins-1000's), the axles bright (`M-SILVER`); the grades not stated |
| construction | free-standing, two side frames joined by a top bar and a floor tie; two tiers of removable axles |
| width | 1100 over the side frames; 1000 between them; 1180 over the axles' ends |
| height | 1650 |
| depth | 700 over the feet (350 in front of the axles' axis, 350 behind it) |
| number of axles | 2, at z 450 and 1200 |
| drum size | up to Ø700 and 960 wide, one drum width per axle |
| load capacity | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the drums | up to Ø700 × 960 wide on each axle; 20 clear of each frame's inner face (asserted 960 < 1000) | design choice (this element) |
| the drums' bores | an axle Ø40: a drum's bore at least Ø40 takes it; the drum standard is not on file and none is claimed | design choice (this element) |
| the tiers | the axles 750 apart: two drums Ø700 clear each other by 50 (asserted); the lower drum's rim 100 above the floor, over the floor tie's top 50 (asserted); the upper drum's top 1550, 50 under the top bar (asserted) | design choice (this element) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| tube | 50 × 50, wall 2, painted steel | rack-bins-1000's tube, one box less one through cutbox |
| feet | x ±500 to ±550, y −350 to 350, z 0 to 50 | reach 350 front and back of the axles' axis, as far as a Ø700 drum's rim (asserted) |
| uprights | x ±500 to ±550, y −25 to 25, z 50 to 1650 | stand on the middle of the feet; carry the axle bores |
| top bar | x −500 to 500, y −25 to 25, z 1600 to 1650 | ties the uprights' tops; the rack's height 1650 |
| floor tie | x −500 to 500, y 300 to 350, z 0 to 50 | ties the feet's rear ends, under and behind the lower drum; the front stays open for a drum to be wheeled in |
| axles | round bright-steel bar Ø40 × 1180, x −590 to 590, at y 0, z 450 and 1200 | draw out sideways to take a drum; 40 past each upright's outer face for a pin or collar (not drawn) |
| axle bores | Ø42 through both walls of each upright (features.csv kind own) | a loose sliding fit, 1 clear all round, so the axle draws out by hand |
| tube ends | open (each tube one box less one through cutbox) | no end cap is claimed; the uprights' ends close on the feet, the bars' ends on the uprights and feet |

## Mechanism
None. One fixed body, no node: the axles stand in their bores (their boxes meet the uprights', GEO-070's joint), a drum turning on its
axle, drawing an axle out, and fixing the rack to the floor are the host's assembly, not a motion (behaviour.csv: the header only).

## Named nodes
None. Colliders, axis-aligned boxes: `foot-l`, `foot-r`, `upright-l`, `upright-r`, `bar-top`, `tie-floor` (each its tube's envelope),
`axle-1`, `axle-2` (each axle's envelope, lower then upper).

## Materials by layer
`M-STEEL-7035` the frame (painted steel, rack-bins-1000's layer) · `M-SILVER` the axles (bright steel).

## Decals (Blender)
No label: neither layer, `M-STEEL-7035` nor `M-SILVER`, is a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Each tube is one box less one through cutbox (section 50² − 46² = 384 mm²), so its edges are 2,
50 and its length, none in the 3 to 7 fillet trap. Volume by hand (asserted in element.py): the tubes 384 × (2 × 1600 + 2 × 700 + 2 ×
1000) = 2534400 mm³ before the bores; the four bores take 4 bores × 2 walls × π × 21² × 2 ≈ 22167, so the frame is about 2512233;
the axles 2 × π × 20² × 1180 ≈ 2965663; in all about 5477896 mm³. Every bounding-box extreme lies on an uncut face: x ±590 the axles' ends, y ±350
the feet's ends, z 0 the feet, z 1650 the top bar and the uprights' tops. A tip-over figure is not claimed: the feet's reach is a design
choice, and anchoring the rack is the host's. Not drawn: the drums, the axles' retention, floor anchors.

## Outputs (out/)
`rack-cable-drum-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004067), our own design (mech-r163, unattended, 2026-11-13): two side frames of painted steel tube 50 × 50 × 2 (an upright on a foot), a top bar and a floor tie, two removable bright-steel axles Ø40 through Ø42 bores in the uprights for drums up to Ø700 × 960 |
