# rack-lifting-gear-1000 · v1.0 · lifting equipment rack, free-standing, generic, 1000 clear between two side frames of painted steel tube 50 x 50 x 2, eight L-hooks Ø20 on a top bar at 1625, four on each face

**What** A free-standing lifting equipment rack: slings, chains and their fittings hang from eight hooks on a top bar, four on the front
face and four on the back, so the rack is used from both sides. Each side frame is painted steel tube 50 × 50 × 2: an upright 1600 high
standing on the middle of a foot 800 long laid front to back. A top bar joins the uprights' tops and a floor tie joins the feet's
middles, both 1000 long between the frames' inner faces. Each hook is round bar Ø20, an arm reaching 150 out of the bar's face and a
tip turned up 25 above the arm's axis, welded on and painted with the frame. The lifting gear is not drawn.
**Class** furniture · **Baseline** our own design: generic lifting equipment rack (ETIM 10.0 EC004245 Lifting equipment rack),
OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by
name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r163.md, Proposed next), and EC004245 is a class not yet built; its shape
no dimensional standard fixes. hook-rack 1.0 is a powder-coating hanger that hangs from a conveyor, not a floor stand: neither draws the
other. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the floor under the middle of the rack: the feet's undersides z = 0, midway between the side frames
x = 0, the top bar's middle y = 0; the hooks stand out toward −y (front) and +y (back). Extents x −550 to 550 (the side frames), y −400
to 400 (the feet), z 0 to 1650.
**Built with** toolkit 1.3 · AutoLISP command `RLGR1000` · no parameter · places no element.

## Class values (ETIM 10.0 EC004245)
Design inputs. EC004245 Lifting equipment rack (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 7
features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the rack is designed to under plain names, as rack-cable-drum-1000 1.0 does (requests mech-8
and mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the design
has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, rack-cable-drum-1000's), the hooks welded on and painted with the frame; the grades not stated |
| construction | free-standing, two side frames joined by a top bar and a floor tie; hooks on both faces of the top bar |
| width | 1100 over the side frames; 1000 between them |
| height | 1650 |
| depth | 800 over the feet (400 in front of the top bar's middle, 400 behind it); 370 over the hooks |
| number of hooks | 8, four on each face, 250 apart |
| hook height | 1625 (the arms' axis) |
| load capacity | not stated (no working load limit is claimed, neither the rack's nor a hook's) |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the lifting gear | a sling's eye, a chain's master link or a ring at least Ø20 inside takes a hook's round bar; the tip stands 15 above the arm's top so the eye stays on; the lifting gear's standards are not on file and none is claimed | design choice (this element) |
| hanging length | the arms' axis 1625 above the floor: gear up to about 1600 long hangs clear of the floor; a longer sling is hung folded | design choice (this element) |
| the hooks' spacing | 250 apart, 230 clear between neighbouring hooks (asserted); the outer hooks 115 clear of the uprights (asserted) | design choice (this element) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| tube | 50 × 50, wall 2, painted steel | rack-cable-drum-1000's tube, one box less one through cutbox |
| feet | x ±500 to ±550, y −400 to 400, z 0 to 50 | reach 400 front and back, 215 past the hooks' outer faces (asserted) |
| uprights | x ±500 to ±550, y −25 to 25, z 50 to 1650 | stand on the middle of the feet; carry the top bar |
| top bar | x −500 to 500, y −25 to 25, z 1600 to 1650 | carries the hooks on both faces; the rack's height 1650 |
| floor tie | x −500 to 500, y −25 to 25, z 0 to 50 | ties the feet's middles, under the top bar, so gear hanging from either face clears it |
| hooks | round bar Ø20 at x −375, −125, 125, 375 on each face; the arm from 2 inside the bar's face (in its wall) to its tip's axis 150 out (y ±175), at z 1625; the tip from z 1615 to 1650 | an L like hook-rack's pins: a sling's eye can't slide off; the tip's top flush with the bar's top |
| tube ends | open (each tube one box less one through cutbox) | no end cap is claimed; the uprights' ends close on the feet, the bars' ends on the uprights and feet |

## Mechanism
None. One fixed body, no node: hanging gear on a hook and fixing the rack to the floor are the host's assembly, not a motion
(behaviour.csv: the header only).

## Named nodes
None. Colliders, axis-aligned boxes: `foot-l`, `foot-r`, `upright-l`, `upright-r`, `bar-top`, `tie-floor` (each its tube's envelope),
`hooks-front`, `hooks-back` (the four hooks of each face, from the bar's face to the hooks' outer faces, z 1615 to 1650).

## Materials by layer
`M-STEEL-7035` the frame and the hooks (painted steel, rack-cable-drum-1000's layer).

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Each tube is one box less one through cutbox (section 50² − 46² = 384 mm²), so its edges are 2,
50 and its length, none in the 3 to 7 fillet trap. Volume by hand (asserted in element.py): the tubes 384 × (2 × 1600 + 2 × 800 + 2 ×
1000) = 2611200 mm³; a hook π × 10² × 152 (the arm) + π × 10² × 35 (the tip) − π × 10² × 2 (the arm in the bar's wall) − 8 × 10³ / 3
(half a Steinmetz solid, where the arm ends on the tip's axis) ≈ 55453, eight of them ≈ 443624; in all about 3054824 mm³. Every
bounding-box extreme lies on an uncut face: x ±550 the side frames, y ±400 the feet's ends, z 0 the feet and the floor tie, z 1650 the
top bar, the uprights' tops and the hooks' tips. A tip-over figure is not claimed: the feet's reach is a design choice, and anchoring the
rack is the host's. Not drawn: the lifting gear, floor anchors.

## Outputs (out/)
`rack-lifting-gear-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004245), our own design (mech-r164, unattended, 2026-11-13): two side frames of painted steel tube 50 × 50 × 2 (an upright on a foot), a top bar and a floor tie, eight welded L-hooks Ø20 on the top bar, four on each face |
