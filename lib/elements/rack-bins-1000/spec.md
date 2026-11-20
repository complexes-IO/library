# rack-bins-1000 · v1.0 · storage bins rack, free-standing, generic, 1000 wide x 1800 high, painted steel tube 50 x 50 x 2 on two feet, four placed suspension rails 400 apart for hanging bins

**What** A free-standing, single-sided storage bins rack: open-fronted bins hang by their rear hooks on four suspension rails across
a frame, in front of it. The frame is painted steel tube 50 × 50 × 2: two uprights 1750 high, each standing on a foot that reaches 400
forward under the bins and 200 back behind the frame, a bottom bar and a top bar 900 long between the uprights' inner faces. The four
rails are placed rail-suspension-shelving-1000 1.0 elements (tags `rail-1` … `rail-4`, bottom to top), never redrawn: the uprights take
that rail's section (50 × 50) and inner faces (x ±450), so its end plates stand on the uprights' inner faces as they do on
shelving-steel's rear uprights, and the rail's height (80) and the room it leaves under it for a bin (300) set the rails' pitch, 400.
Every rail figure is read from that element (`library.load("rail-suspension-shelving-1000", "1.0")` in element.py). The bins are not
drawn.
**Class** furniture · **Baseline** our own design: generic storage bins rack (ETIM 10.0 EC004069 Storage bins rack), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by name from
lib/toolkit/generic.py's mech order (lib/rounds/mech/r161.md, Proposed next, its first candidate), and EC004069 is a class not yet built
that places an element on file (rail-suspension-shelving-1000 1.0, station 6 passed); its shape no dimensional standard fixes. No
product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the floor under the middle of the rack: the feet's undersides z = 0, the middle of the rack's width
x = 0, the uprights' front faces y = 0; the bins hang in front of the frame, toward −y. Extents x −500 to 500, y −400 to 250, z 0 to
1800.
**Built with** toolkit 1.3 · AutoLISP command `RBIN1000` · no parameter · places rail-suspension-shelving-1000 1.0 four times (tags
`rail-1` … `rail-4`), at x 0, y −450, z 80, 480, 880, 1280 (its origin), so the rails' bottoms stand at 380, 780, 1180 and 1580.

## Class values (ETIM 10.0 EC004069)
Design inputs. EC004069 Storage bins rack (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 6
features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the rack is designed to under plain names, as rail-suspension-shelving-1000 1.0 and
shelf-pullout-shelving-1000 1.0 do (requests mech-8 and mech-9, the core's answers); a later minor version restates them in ETIM's order
with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, the rail's and shelving-steel's; the grade not stated) |
| construction | free-standing, single-sided: bins on the front only |
| width | 1000 over the uprights; 900 between them, the rails' length over their end plates |
| height | 1800 |
| depth | 650 over the feet (400 in front of the uprights, 200 behind them) |
| bin carriers | four suspension rails (rail-suspension-shelving-1000 1.0), 400 apart |
| load capacity | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the rails' end plates | on the uprights' inner faces x ±450, y 5 to 45 (the rail's y 455 to 495, placed at y −450 so its uprights' band y 450 to 500 is this rack's y 0 to 50) | rail-suspension-shelving-1000 1.0 (element.py XI, YB0, EP_Y0, EP_W) |
| the uprights' section | 50 × 50, the section the rail's end plates were designed against | rail-suspension-shelving-1000 1.0 (element.py UP, read from shelving-steel 1.0) |
| the rails' pitch | 400: the rail 80 high leaves 320 between one rail's top and the next one's bottom, at least the 300 the rail element leaves under it for a hanging bin (asserted) | rail-suspension-shelving-1000 1.0 (element.py H, Z0) |
| the lowest rail | its bottom at 380, 330 above the bottom bar's top (asserted ≥ 300) | rail-suspension-shelving-1000 1.0 (element.py Z0) |
| the top rail | its top at 1660, 90 under the top bar (asserted at least the 26 a hook needs to lift out over the lip, the rail's own check) | rail-suspension-shelving-1000 1.0 (element.py LIP, CH_Z, T) |

## Its own sizes (design choices; the rail's figures read from rail-suspension-shelving-1000 1.0)
| item | value | why |
|---|---|---|
| tube | 50 × 50, wall 2, painted steel | the rail's uprights' section, so the placed rail fits as it fits shelving-steel |
| uprights | x ±450 to ±500, y 0 to 50, z 50 to 1800 | stand on the feet; their inner faces carry the rails' end plates |
| feet | x as the uprights, y −400 to 250, z 0 to 50 | reach 400 forward under the hanging bins and 200 back; the rack stands on them |
| bottom bar | x −450 to 450, y 0 to 50, z 50 to 100 | ties the uprights at the feet |
| top bar | x −450 to 450, y 0 to 50, z 1750 to 1800 | ties the uprights at the top; the rack's height 1800 |
| rails | four, bottoms at 380, 780, 1180, 1580 (pitch 400) | see "What it meets" |
| tube ends | open (each tube one box less one through cutbox) | no end cap is claimed; the uprights' ends close on the feet, the bars' ends on the uprights |

## Mechanism
None. One fixed body, no node: hanging a bin on a rail and fixing the rack to the floor or a wall are the host's assembly, not a motion
(behaviour.csv: the header only). The placed rails carry no node.

## Named nodes
None. Colliders, axis-aligned boxes: `foot-l`, `foot-r`, `upright-l`, `upright-r`, `bar-bottom`, `bar-top` (each its tube's envelope),
and each placed rail's three under its tag: `rail-1-hook-rail`, `rail-1-end-l`, `rail-1-end-r` … `rail-4-end-r` (renamed from the rail's
own `hook-rail`, `end-l`, `end-r`, so no two colliders share a name, as hmi-7in does with its placed clamps).

## Materials by layer
`M-STEEL-7035` the frame and the placed rails (painted steel, the rail's layer).

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Each tube is one box less one through cutbox (section 50² − 46² = 384 mm²), so its edges are 2,
50 and its length, none in the 3 to 7 fillet trap. Volume by hand (asserted in element.py): the tubes 384 × (2 × 1750 + 2 × 650 + 2 ×
900) = 2534400 mm³; the four rails 4 × 217668 = 870672 (rail-suspension-shelving-1000 1.0's own figure); in all 3405072 mm³. Every
bounding-box extreme lies on an outer face of a tube (x ±500 the uprights and feet, y −400 and 250 the feet's ends, z 0 the feet, z 1800
the top bar and the uprights' tops). A tip-over figure is not claimed: the feet's reach is a design choice, and anchoring the rack is
the host's. Not drawn: the bins, any fixing of the rails to the uprights (the rail element models none), floor anchors.

## Outputs (out/)
`rack-bins-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004069), our own design (mech-r162, unattended, 2026-11-13): a free-standing frame of painted steel tube 50 × 50 × 2 (two uprights on two feet, a bottom and a top bar) carrying four placed rail-suspension-shelving-1000 1.0 rails 400 apart on the uprights' inner faces; every rail figure read from that element |
