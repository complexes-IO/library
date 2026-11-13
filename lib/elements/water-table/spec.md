# water-table · v1.0 · water table 3190 × 1690 × 550, open tank 20 thick, two seat ledges carrying bed-slat 1.1 with its underside at 400

**What** The water table under a CNC plasma cutter's slat bed (lib/machines-factory.txt line 13: plasma-cutter-cnc places
frame-welded, bed-slat, gantry-beam, ..., water-table). An open steel tank; bed-slat drops into it and sits on two seat ledges along
the long walls, so the sheet on the slats lies above the tank's rim and the water under it catches the cut's sparks, dross and fume.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks water-table own_design
"yes"). No product was matched and no vendor file was opened. The inside is sized to bed-slat; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the tank's footprint, x = 0, y = 0. The tank's length
runs along x, as bed-slat's does; bed-slat's own origin (its frame's underside, at its centre) sits at x = 0, y = 0, z = 400.
**Built with** toolkit 1.3 · AutoLISP command `WATERTABLE` · no parameters.

## Mechanism
None: one fixed body, no node. The water, its level and the bed are not the tank's moving parts; bed-slat is its own element,
placed on the ledges by the assembly. behaviour.csv is header only.

## What it meets (figures from files on hand)
| what | figure | from |
|---|---|---|
| bed-slat 1.1 (the bed it carries) | outside 3100 × 1600 (x ±1550, y ±800), 200 from its frame's underside to the slats' top; its long rails 50 thick at y ±750 to ±800 | bed-slat/element.py (IN_X, IN_Y, RAIL_T, LEDGE_TOP, SLAT_H), read by library.load, so the two cannot drift apart |

Nothing else on file. No drain, fill or water-level fitting is drawn: no pipe thread or fitting standard is on file, and a host
doesn't model a hole for a part it places later (OPERATING.md 12). The tank's fixing to the floor or to the cutter's frame, if any,
is the assembly's, so it has no hole.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| inside | 3150 × 1650 (x ±1575, y ±825), from the floor plate's top (z 20) to the rim (z 550) | bed-slat's outside with 25 clear all round, so the bed drops in and lifts out |
| tank | one solid: a floor plate 3190 × 1690 × 20 (z 0 to 20) and four walls 20 thick to z 550, open at the top | 20 thick, not 10: rack-bar 1.0's first AutoCAD run failed the fillet gate on a 10 mm rim drawn as separate boxes; one box with the inside cut out (rack-bar 1.0's fix) |
| seat ledges | 2, 3150 × 100 × 20, along the long walls' inside (y ±725 to ±825), z 380 to 400, end wall to end wall | carry bed-slat's two long rails (y ±750 to ±800) with its underside at z 400; 100 wide, so the rail stays on the ledge wherever the 25 clearance lets the bed sit |
| seat height | the bed's underside at z 400, the slats' top at z 600 | a design choice: 380 of the tank's depth under the bed |
| rim | z 550, 50 below the slats' top | a design choice: the sheet on the slats clears the rim |
| the water | not drawn | the machine's, not the tank's; no level is stated |

## Named nodes
None. Colliders: `floor`, `wall-front`, `wall-back`, `wall-left`, `wall-right`, `ledge-front`, `ledge-back`, one per member, so the
bed meets the ledges and not an envelope.

## Materials by layer
`M-STEEL-7035` every member (painted steel, RAL 7035).

## Notes
No load rating, no capacity and no claim about the cutting process: no bed, sheet or water mass is on file, so the tank is not sized
against them. The volume is 223 030 000 mm³ (the tank 2 965 105 000 outside less 2 754 675 000 inside = 210 430 000, the ledges
2 × 6 300 000; written as volume only: lib/materials.csv gives steel no density, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`water-table.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r72, unattended) |
