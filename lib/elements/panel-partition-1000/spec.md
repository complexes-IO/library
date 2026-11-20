# panel-partition-1000 · v1.0 · element for a storage partition, generic, grate panel 930 x 1850 for posts 1000 apart, painted steel tube frame 20 x 20 x 2 with vertical flat bars 2 x 20 at 50 pitch, six M8 fixing holes

**What** A panel of a storage partition (a grate partition wall, a storage cage's wall): it stands between two post-partition-2000
posts whose axes are 1000 apart and bolts to their tabs. A welded frame of painted steel tube 20 × 20 × 2, 930 wide (x ±465, 10 clear
of each post's face) and 1850 high (z 100 to 1950): two full-width rails, two stiles between them and a middle rail at z 1050, filled
with 17 vertical flat bars 2 × 20 at 50 pitch. Each stile carries three M8 clearance holes (Ø9, ISO 273 medium) along y at x ±455, z
250, 1050 and 1850, on the posts' tab holes, and the frame lies on y −10 to 10 against the tabs' +y faces, centred on the partition's
line. The posts, screws, nuts and washers are not drawn.
**Class** furniture · **Baseline** our own design: generic element for storage partition (ETIM 10.0 EC004103 Element for storage
partition; synonyms grate partition, storage partition element, storage partition system), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by name (lib/rounds/mech/r165.md, Proposed
next), and the post it bolts to, post-partition-2000 1.0, is built and gated first (foundation first, OPERATING.md 12). Its shape no
dimensional standard fixes. No element draws a partition panel. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the floor at the middle of the bay between two posts: z = 0 the floor (the posts' floor plates'
undersides), x = 0 halfway between the posts' axes (x −500 and 500), y = 0 the partition's centre plane. Extents x ±465, y ±10, z 100
to 1950.
**Built with** toolkit 1.3 · AutoLISP command `PPNL1000` · no parameter · places no element; reads post-partition-2000 1.0's figures
with library.load.

## Class values (ETIM 10.0 EC004103)
Design inputs. EC004103 Element for storage partition (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier
2, 3 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until
they are on file this table gives the values the panel is designed to under plain names, as post-partition-2000 1.0 does (requests
mech-8 and mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where
the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, the post's); the grade not stated |
| type of element | grate panel (frame with vertical flat bars); not a sheet or wire-mesh panel, not a door |
| width | 930 (for posts 1000 apart) |
| height | 1850 (z 100 to 1950) |
| infill | 17 vertical flat bars 2 × 20, 50 pitch, 48 clear between bars, 44 at the stiles |
| fixing | 3 × M8 per side, at z 250, 1050, 1850 |

No ratings.csv: no rating the checks read, and no load or impact figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the posts (post-partition-2000 1.0) | posts' axes at x ±500 (the pitch 1000, a design choice); the frame's ends at x ±465 = 500 − 25 (the post's half section) − 10 (its panel gap, `PANEL_GAP`); the stiles' axes at x ±455 = 500 − 45 (the tab hole's offset, `TAB_HOLE_X`); the frame's −y face at y −10 (the tabs' +y face, `TAB_Y1`); the fixing heights z 250, 1050, 1850 (`TAB_Z`); all read with library.load, asserted in element.py | post-partition-2000 1.0 (the interface it was built to) |
| the M8 fixings | 6 × Ø9 holes along y through each stile's two walls, M8 clearance, ISO 273 medium (lib/standards/holes.csv), the post's hole size; position Ø1.0 at MMC, floating fastener (features.csv); the screws, nuts and washers are the host's, not drawn | ISO 273; ASME Y14.5 |
| the posts' floor plates | the frame's bottom at z 100, clear of the plates (8 thick) and their anchors' nuts | design choice |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| frame tube | 20 × 20 × 2 | the post's interface (a frame tube 20 wide covers the tab hole, a frame 20 deep lies on the partition's line); its holes 5.5 from the tube's sides (asserted) |
| rails | two full width, x ±465, at z 100 to 120 and 1930 to 1950, open at their ends (10 from the post's face) | the stiles' ends buried in them, so the stiles' bores are closed off |
| stiles | x 445 to 465 (and −465 to −445), z 119.5 to 1930.5 (0.5 into each rail) | centred on the posts' tab holes; each hole inside the bore's x span, so it cuts the two y walls only (asserted) |
| middle rail | z 1040 to 1060, x ±445.5 (0.5 into each stile) | stiffens the bars' runs; on the middle fixing height, its end clear of that hole |
| flat bars | 17, 2 × 20, at x −400 to 400 every 50, in two runs (z 119.5 to 1040.5 and 1059.5 to 1930.5, 0.5 into the rails) | a grate's infill; 48 clear between bars, 44 at the stiles (asserted) |
| floor gap | 100 under the frame | clear of the posts' floor plates and a broom's reach under it |

## Mechanism
None. One fixed body, no node: bolting the panel to the posts is the host's assembly, not a motion (behaviour.csv: the header only).

## Named nodes
None. One collider, an axis-aligned box named apart from any node: `grate` (x ±465, y ±10, z 100 to 1950).

## Materials by layer
`M-STEEL-7035` the whole panel (painted steel, the post's layer); the bars and rails welded in and painted with it.

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as 39 boxes in one material: five tubes (each one box less one through cutbox), the
stiles with three through holes each, and 34 flat bar runs. Every edge is 2 (a wall, a bar's thickness), 20 or more, none in the gate's
3 to 7 fillet trap. Volume by hand (asserted in element.py), with the tube section 20² − 16² = 144: two rails 144 × 930 = 133920 each;
two stiles 144 × 1811 − 3 × 2 × π × 4.5² × 2 = 260020.6 each; the middle rail 144 × 891 = 128304; 17 bars 2 × 20 × (921 + 871) =
1218560; in all about 2134745.2 mm³ (the joints' 0.5 overlaps counted in both parts). Every bounding-box extreme lies on an uncut face:
x ±465 the stiles' outer faces, y ±10 the frame's faces, z 100 the bottom rail's underside, z 1950 the top rail's top. Not drawn: the
posts, screws, nuts and washers.

## Outputs (out/)
`panel-partition-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004103), our own design (mech-r166, unattended, 2026-11-13): a grate panel 930 × 1850 for post-partition-2000 1.0 posts 1000 apart, tube frame 20 × 20 × 2 with a middle rail and 17 flat bars 2 × 20, six M8 fixing holes on the posts' tab holes |
