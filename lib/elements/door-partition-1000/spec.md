# door-partition-1000 · v1.0 · single door for a storage partition, generic, for posts 1000 apart, painted steel tube frame 20 x 20 x 2 with six M8 fixing holes and a grate leaf 860 x 1820 of flat bars 2 x 20 at 50 pitch, opening 0 to 90 degrees

**What** A single hinged door of a storage partition (a grate partition wall, a storage cage): it stands between two
post-partition-2000 posts whose axes are 1000 apart, in place of a panel-partition-1000, and bolts to the posts' tabs as the panel
does. The fixed body is a door frame of painted steel tube 20 × 20 × 2: two stiles (x ±445 to 465, z 100 to 1930.5) each with three M8
clearance holes (Ø9, ISO 273 medium) along y at x ±455, z 250, 1050 and 1850, on the posts' tab holes, joined at the top by a
full-width head (z 1930 to 1950); no sill, so the opening is clear from the floor. The leaf, node `door`, is a welded grate of the same
tube (two rails, two stiles, a middle rail at z 1050) with 17 vertical flat bars 2 × 20 at 50 pitch, 860 wide (x ±430) and 1820 high
(z 100 to 1920); it turns 0 to 90 degrees toward +y, away from the tabs, about a vertical axis on the left stile's inner front edge (x
−445, y 10). The frame and the closed leaf lie on y −10 to 10 against the tabs' +y faces, centred on the partition's line. The posts,
hinges, lock, screws, nuts and washers are not drawn.
**Class** furniture · **Baseline** our own design: generic door for storage partition (ETIM 10.0 EC004105 Door for storage partition;
synonyms single door, storage partition door, storage partition single door), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No
inventory row names it: group EG010340 Storage and racking systems is walked by name (lib/rounds/mech/r166.md, Proposed next), and the
post it bolts to and the panel whose frame it shares, post-partition-2000 1.0 and panel-partition-1000 1.0, are built and gated first
(foundation first, OPERATING.md 12). Its shape no dimensional standard fixes. No element draws a partition door. No product was matched
and no vendor file was opened.
**Units / frame** mm, Z up. Origin: panel-partition-1000's: the floor at the middle of the bay between two posts: z = 0 the floor (the
posts' floor plates' undersides), x = 0 halfway between the posts' axes (x −500 and 500), y = 0 the partition's centre plane. Extents
(closed) x ±465, y ±10, z 100 to 1950.
**Built with** toolkit 1.3 · AutoLISP command `DRPT1000` · no parameter · places no element; reads post-partition-2000 1.0's and
panel-partition-1000 1.0's figures with library.load.

## Class values (ETIM 10.0 EC004105)
Design inputs. EC004105 Door for storage partition (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2,
3 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the door is designed to under plain names, as panel-partition-1000 1.0 does (requests mech-8
and mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the design
has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, the post's and panel's); the grade not stated |
| type of door | single door, hinged (not a double or sliding door) |
| width | 930 over the frame (for posts 1000 apart); clear opening 890 between the frame's stiles, the leaf 860 |
| height | 1850 over the frame (z 100 to 1950); clear opening from the floor to the head's underside, 1930; the leaf 1820 |
| infill | 17 vertical flat bars 2 × 20, 50 pitch, 48 clear between bars, 9 at the leaf's stiles |
| opening | 0 to 90 degrees toward +y, the hinge on the left (seen from +y) |
| fixing | 3 × M8 per side, at z 250, 1050, 1850 |

No ratings.csv: no rating the checks read, and no load or impact figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the posts (post-partition-2000 1.0) | the tabs' heights z 250, 1050, 1850 (`TAB_Z`); the tabs at x ±435 to 475 = 500 − 25 − 40 (`UP`, `TAB_R`) and y −18 to −10 (`TAB_Y0`, `TAB_Y1`); all read with library.load, asserted in element.py | post-partition-2000 1.0 (the interface it was built to) |
| the panel (panel-partition-1000 1.0) | the pitch 1000; the frame tube 20 × 20 × 2 and its 0.5 joints; the frame's ends x ±465 (10 clear of the posts' faces) and its stiles' axes x ±455 (on the tab holes); the frame on y −10 to 10; the floor gap 100 and the top 1950; the middle rail's height 1050; the flat bars' size, pitch and x places; all read with library.load, so a door and a panel in one partition line up | panel-partition-1000 1.0 |
| the M8 fixings | 6 × Ø9 holes along y through the fixed stiles' two walls, M8 clearance, ISO 273 medium (lib/standards/holes.csv), the post's hole size; position Ø1.0 at MMC, floating fastener (features.csv); the screws, nuts and washers are the host's, not drawn | ISO 273; ASME Y14.5 |
| the hinges and lock | not drawn and no hole modelled: the host's assembly, as door-shelving-1000's | design choice |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| frame stiles | x 445 to 465 (and −465 to −445), z 100 to 1930.5 (0.5 into the head), open below | the panel's stiles' places, centred on the posts' tab holes; each hole inside the bore's x span, so it cuts the two y walls only (asserted) |
| head | full width x ±465, z 1930 to 1950, open at its ends | the panel's top rail; joins the two stiles into one frame, so the fixed body is one body |
| no sill | the opening clear from the floor | a door one walks or wheels a trolley through; the stiles alone carry the frame to the floor gap |
| leaf | x ±430, z 100 to 1920, y −10 to 10 when closed: rails full width, stiles 0.5 into each rail, a middle rail at z 1040 to 1060 0.5 into each stile, 17 flat bars in two runs 0.5 into the rails | the panel's construction; its ends 5 inside the posts' tabs' ends (x ±435), so the closed leaf never rubs a tab, and 15 from the frame's stiles; 10 under the head |
| hinge axis | vertical, through (x −445, y 10): the left stile's inner front edge | a leaf turning about the frame's front edge never moves behind that edge's planes (x ≥ −445, and y ≥ −10 at every angle), so it stays clear of the stile and both posts' tabs (asserted for every degree) |
| swing | 0 to 90 degrees toward +y | away from the tabs (they lie at y −18 to −10) |

## Mechanism
One moving node, the leaf `door`: rotate about the vertical axis through (−445, 10, 1010), range 0 to 90 degrees (toward +y). Closed it
lies in the frame's opening, 15 from each fixed stile and 10 under the head. Its sweep, worked in element.py for every degree on the
leaf's section corners and every 5 along its faces: never past the hinge stile's inner face (x ≥ −445), and within 2 of that plane only
2 or more in front of the stile (y ≥ 12); never past the tabs' +y plane (y ≥ −10), and within 2 of it only at |x| ≤ 433, 2 inside the
tabs' ends; its free edge never within 2 of the other stile (x ≤ 443, the free corner's radius 875.2 from the axis); the axis is vertical,
so the leaf stays under the head at every angle. behaviour.csv: states `closed` (default) and `open` (manual toggle), pose `door` at its
end in `open`.

## Named nodes
`door` (rotate, the leaf). Colliders, axis-aligned boxes named apart from any node: `frame-l`, `frame-r` (the fixed stiles, z 100 to
1930), `head` (z 1930 to 1950), `leaf` (the leaf's box, carried by `door`).

## Materials by layer
`M-STEEL-7035` the whole door (painted steel, the post's and panel's layer), the leaf on `node:door|M-STEEL-7035`; the bars and rails
welded in and painted with it.

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as 42 boxes in one material: three frame tubes and five leaf tubes (each one box less one
through cutbox; the fixed stiles open below), the fixed stiles with three through holes each, and 34 flat bar runs. Every edge is 2 (a
wall, a bar's thickness), 20 or more, none in the gate's 3 to 7 fillet trap. Volume by hand (asserted in element.py), with the tube
section 20² − 16² = 144: the fixed stiles 144 × 1830.5 − 3 × 2 × π × 4.5² × 2 = 262828.6 each, the head 144 × 930 = 133920 (the frame
659577.2); the leaf's rails 144 × 860 = 123840 each, its stiles 144 × 1781 = 256464 each, its middle rail 144 × 821 = 118224, 17 bars 2
× 20 × (921 + 841) = 1198160 (the leaf 2076992); in all about 2736569.2 mm³ (the joints' 0.5 overlaps counted in both parts). Every
bounding-box extreme lies on an uncut face: x ±465 the fixed stiles' outer faces, y ±10 the frame's faces, z 100 the leaf's bottom rail's
underside (the fixed stiles' open ends lie there too), z 1950 the head's top. Not drawn: the posts, hinges, lock, screws, nuts and washers.

## Outputs (out/)
`door-partition-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004105), our own design (mech-r167, unattended, 2026-11-13): a single door for post-partition-2000 1.0 posts 1000 apart, panel-partition-1000 1.0's tube frame (two stiles with six M8 fixing holes and a head, no sill) and a grate leaf 860 × 1820 with a middle rail and 17 flat bars 2 × 20, turning 0 to 90 degrees toward +y about the left stile's inner front edge |
