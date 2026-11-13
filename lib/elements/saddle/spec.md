# saddle · v1.1 · mill saddle 600 × 700 × 270, two shoes on bed-cast's ways, two flat cross ways 80 wide for the table

**What** The saddle of a bed-type vertical mill (lib/machines-factory.txt: mill-vertical-cnc places bed-cast, column, saddle and
table-slotted): the part between the bed and the table. Two way shoes sit on bed-cast's two flat ways and carry a box body; two
flat machined ways on its top face run across the bed for the table. A BOM places the table on the saddle's `ways`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks saddle own_design
"yes"). No product was matched and no vendor file was opened. The shoes' spacing and width come from bed-cast 1.0; every other
size is a design choice.
**Units / frame** mm, Z up. Origin: bed-cast's ways' top plane z = 0 (the saddle's seat) at the saddle's centre x = 0, y = 0; the
saddle slides along x, the bed's length; front toward −y. The cross ways' top plane, the table's seat, is at z = 270.
**Built with** toolkit 1.3 · AutoLISP command `SADDLE` · no parameters.

## Mechanism and the table's seat
`ways` (fixed): the two cross ways. Its pivot is the centre of the cross ways' top plane (0, 0, 270) with the axis +z: the table
element is placed there with its own base origin, so a BOM row reads `<tag>.ways`. The saddle's travel along the bed (x) and the
table's across it (y) are the machine's, between the elements (the ballscrews and linear guides of its BOM), so the saddle has
no moving node of its own.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the bed's ways | two flat ways 80 wide, centres at y ±170 (340 apart), their top plane the saddle's seat | bed-cast 1.0 (`WAY_W`, `WAY_Y`, read by library.load("bed-cast")); its seat at z = 430 above the floor |

Placed on bed-cast at (x, 0, 430), the saddle's shoes cover the bed's ways exactly in y; its body (from z 40, 470 above the
floor) clears the bed's body (top at 400) and base plate. The saddle's x travel on the bed is the machine's: from bed-cast's
1960 long ways and this saddle's 600, at most 1360 with the shoes fully on the ways.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| saddle length along the bed | 600 (x ±300) | a design choice; how a table sits on it is checked when table-slotted is on file |
| saddle width across the bed | 700 (y ±350), overhanging the bed's 500 body by 100 each side | a design choice; it carries the cross ways' 660 length; the table's fit and travel are checked when table-slotted is on file |
| way shoes | 2, 600 × 80 × 40 (z 0 to 40), at y ±170 | one on each of bed-cast's ways, as wide as the way |
| body | 600 × 700, from the shoes (z 40) to its top face (z 240) | a closed box section, 200 deep: a design choice, not sized against any load |
| cross ways | 2, flat, 80 wide, 30 proud of the body's top (z 240 to 270), centres at x ±200 (400 apart), 660 long (20 short of each side) | the same section as bed-cast's ways; 400 apart within the saddle's 600; the 20 is the body's machining run-out |
| body | drawn by its outside: its cores and ribs are not seen | the model shows what can be seen |
| gibs, way wipers, the feed nut's bracket, the saddle clamp, oil lines | not drawn | they belong to the machine's own version, with its guides and screws |

## Named nodes
`ways` (fixed, above). Colliders `saddle` (the shoes and body, the space between the shoes included) and `cross-ways` (the two
ways and the gap between them); neither is named like a node.

## Materials by layer
`M-STEEL-7035` the shoes and body (painted RAL 7035) · `M-SILVER` the cross ways (bare machined steel, the library's bright-metal
layer, as bed-cast's ways).

## Notes
No load rating, no stiffness or accuracy claim: no machine's mass, cutting forces or way tolerances are on file, so the saddle is
not sized against them. No hole: the table's fixing, the feed nut and the gib screws come with the parts they hold (OPERATING.md
12: a host doesn't model holes for a part it places later). No vendor names, no label.

## Outputs (out/)
`saddle.lsp` · `.glb` (pivot on `ways`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r66, unattended) |
| 1.1 | text only, the part unchanged (mech-r73, unattended; review mech-r66 finding 1): the length's, width's and body's "why" cells written as design choices, with the table's fit and travel checked when table-slotted is on file and no stiffness claimed |
