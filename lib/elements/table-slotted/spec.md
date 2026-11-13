# table-slotted · v1.0 · T-slot machine table 500 × 1200 × 100, three T-slots along its length at 130 pitch, two way shoes on saddle's cross ways

**What** A T-slot machine table (lib/machines-factory.txt: drill-pillar, drill-radial, grinder-surface, mill-vertical-cnc,
mill-horizontal, borer-horizontal, notcher-corner and punch-hydraulic place table-slotted): a rectangular plate with three T-slots
along its length, on two way shoes that ride the saddle's cross ways. A vise (vise-machine) or a fixture is bolted to it through
the slots; the machine's BOM places it on the saddle's `ways` and the vise on its top face.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks table-slotted own_design
"yes", "T-slot machine table"). No product was matched and no vendor file was opened. The shoes' spacing and width come from
saddle 1.1, the slot pitch from vise-machine 1.0's lugs; the T-slot profile is a figure ISO 299 tabulates (not on file: class B,
source wanted, What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: saddle's cross ways' top plane z = 0 (the table's seat) at the table's centre x = 0, y = 0; the
table's length and its slots run along y, its travel on the saddle; the top face, where a vise or fixture is placed, is at z = 100.
Extents x ±250, y ±600, z 0 to 100.
**Built with** toolkit 1.3 · AutoLISP command `TABLETSLOT` · no parameters.

## Mechanism and the fixture's seat
No moving node: the table's travel along the saddle's cross ways (y) is the machine's, between the elements (the ballscrew and
its nut, or the handwheel's screw, in the machine's BOM), as saddle's own travel along the bed. No fixed node either: the top face
is the plane z = 100 from the origin, and a BOM row places a vise or fixture there by its position (`x, y, 100` under the table's
tag), its T-bolts in the slots. The twin reads nothing from the table.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the saddle's cross ways | two flat ways 80 wide, centres at x ±200 (400 apart), their top plane the table's seat | saddle 1.1 (`WAY_W`, `WAY_X`, read by library.load("saddle")); the saddle's seat at z = 270 above bed-cast's ways |
| the vise's lugs | four M12 lugs on 230 × 130 (vise-machine 1.0: `LUG_Y` ±65 across, read by library.load("vise-machine")) | the slot pitch is 2 × 65 = 130, so a vise set with its length along the slots has its four lugs over two neighbouring slots; its Ø13.5 holes are ISO 273 medium (lib/standards/holes.csv) |
| the T-slot profile | the slot's throat width, the undercut's width and height, and the depth, for an M12 T-bolt; drawn 14 / 24 / 10 / 28 | **NOT ON FILE (B)**: the T-slot profile for a 12 bolt is a figure ISO 299 (T-slots and corresponding bolts) tabulates, a fit the T-bolts and T-nuts meet, so it is a source wanted (OPERATING.md 6 and 12; the stand-magnetic 1.1 way), not this design's: the slots are drawn at the design figures 14 (the throat, clearing the M12 medium clearance 13.5 of ISO 273 on file) / 24 / 10 / 28 until the document is on file, and then the profile is read from it (a later version if a figure differs). No T-bolt, T-nut or clamp is drawn or placed |

Placed on saddle 1.1 at `<saddle tag>.ways` (0, 0, 270 above bed-cast's ways), the table's shoes cover the saddle's cross ways
exactly in x; its plate (from z 30) clears the saddle's body (top at 240, the ways 30 proud). The table's y travel on the 660
long cross ways is the machine's: from those 660 (y ±330) and the shoes' 1160 (y ±580), at most 250 each way with the cross ways
fully under the shoes, as the machine's BOM sets it.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| table length along the slots | 1200 (y ±600) | a design choice: room for a vise (340 long) and work beside it; the travel is the machine's |
| table width across | 500 (x ±250) | a design choice: it covers the saddle's cross ways (x ±240) with 10 to spare each side |
| way shoes | 2, 1160 × 80 × 30 (z 0 to 30), at x ±200, 20 short of each end | one on each of saddle's cross ways, as wide as the way; the 20 is the plate's machining run-out |
| plate | 500 × 1200 × 70 (z 30 to 100) | 42 of solid under the slots' floors; a design choice, not sized against any load |
| T-slots | 3, along y through the plate's full length, at x −130, 0, 130 | three slots at vise-machine's lug pitch; the outer slots 120 from the plate's edges |
| T-slot profile | throat 14 wide and 18 deep, undercut 24 wide and 10 high, floor 28 below the top face | drawn so until ISO 299 is on file (What it meets) |
| plate | drawn by its outside: ribs under it are not seen | the model shows what can be seen |
| gibs, way wipers, the feed nut's bracket, the table clamps, end stops, swarf troughs, the coolant drain | not drawn | they belong to the machine's own version, with its guides and screws |

## Named nodes
None. Colliders `shoes` (both shoes and the gap between them) and `table` (the plate, the slots filled).

## Materials by layer
`M-SILVER` the shoes and the plate (bare machined steel, the library's bright-metal layer, as saddle's and bed-cast's ways).

## Notes
No load rating, no flatness, stiffness or accuracy claim: no machine's mass, cutting forces or way tolerances are on file, so the
table is not sized against them. No hole: the T-bolts, the feed nut and the gib screws come with the parts they hold
(OPERATING.md 12: a host doesn't model holes for a part it places later). The table serves nine machine rows with one size;
a different length or slot count is a parameter of a later version when a machine row asks for it. No vendor names, no label.

## Outputs (out/)
`table-slotted.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r103, unattended) |
