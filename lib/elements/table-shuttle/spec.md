# table-shuttle · v1.0 · shuttle table, runway 6500 × 1700 on eight legs, one pallet 3200 × 1700 carrying bed-slat 1.1, 3300 of travel

**What** The shuttle (pallet-change) table of a sheet laser cutter: a pallet carrying the slat bed runs on two rails from the
cutting position, under the gantry, out to a load station beside the machine and back, so finished parts are unloaded and a new
sheet laid on while the next one is cut. It is the table-shuttle of laser-cutter-sheet (lib/machines-factory.txt line 61:
frame-welded (own), bed-slat (own), gantry-beam (own), linear guides, rack-pinion, servo motors and drives, laser-source-fiber,
laser-head, chiller, fume-extractor, table-shuttle (own), enclosure-machine (own), guard-interlock, light-curtain, op-estop-22-2nc,
relay-safety-2ch-2no1nc, plc0, hmi-7in, ipc, enc-fs-1524x1829x305). A BOM places bed-slat on the pallet's top.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks table-shuttle own_design
"yes"). No product was matched and no vendor file was opened. The pallet is sized to bed-slat 1.1 (read with library.load, so the
two cannot drift apart); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the cutting position, x = 0, y = 0 (the pallet's centre
at rest). The runway runs along +x toward the load station. The pallet's top, bed-slat's seat, is at z = 700, so bed-slat's slats
(its sheet seat, 200 above its frame's underside) stand at z = 900. Extents x −1600 to 4900, y −850 to 850, z 0 to 700 at rest.
**Built with** toolkit 1.3 · AutoLISP command `SHUTTLETABLE` · no parameters.

## Mechanism
`pallet` (translate along +x, 0 to 3300 mm): the pallet frame. At 0 it stands at the cutting position (x −1600 to 1600); at 3300
it stands at the load station (x 1700 to 4900), 100 clear of where it was. Its pivot is the centre of its top face at rest
(0, 0, 700), the axis +x. Its underside rests on the two rails' tops (z 600) through the whole travel; nothing else lies in its
path. The drive that moves it (chain, rack or screw), its locating pins and lift at each end, the end stops and the wheels are
the machine's or a later version's: not drawn, so the pallet slides on the rails' tops in the model. One pallet: the second,
upper pallet of a two-level changer is a later version if a machine asks for it.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| bed-slat 1.1 | the pallet's outside 3200 × 1700 (50 round the bed's 3100 × 1600), its opening 2900 × 1400 (100 inside the bed's outside), so the bed's frame rails (50 wide) bear on the pallet's 150-wide rim | bed-slat's IN_X, IN_Y and RAIL_T (library.load); how the machine locates the bed on the pallet (pins, stops) is the machine's, as bed-slat's spec says, so the pallet has no hole for it |
| the gantry | the cutting position at x = 0 | gantry-beam 1.1 and the cutter's frame are placed by the assembly; the sheet's height (z 900 with bed-slat) is a design choice, checked when laser-cutter-sheet is assembled |
| the floor | eight legs, 100 × 100 | the fixing to the floor (anchor-bolt, a separate element) is the assembly's, so the legs have no hole (OPERATING.md 12: a host doesn't model holes for a part it places later) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| pallet frame | one solid 3200 × 1700 × 100 (z 600 to 700), cut open to 2900 × 1400, a rim 150 wide | the slag falls through the opening; one cut solid, not four bars (rack-bar 1.0's fillet lesson) |
| travel | 3300 along +x | the pallet's length and 100 clear, so at the load station it stands wholly outside the cutting position |
| runway | x −1600 to 4900 (6500 long): the cutting position and the load station end to end | the pallet's whole travel stays on the rails |
| girders | 2, 100 × 200 (z 360 to 560), the runway's full length, centred at y ±775 | carry the rails |
| rails | 2, 60 × 40 (z 560 to 600) on the girders' centres, y ±775, 6460 long (20 inside each girder end) | under the pallet's rim; stopping 20 short leaves no rail face flush with a girder's end (GEO-050, two materials) |
| legs | 8, 100 × 100 (z 0 to 360), under each girder at x −1550, 600, 2750 and 4850 | spans 2150, 2150, 2100; not sized against a load |
| end ties | 2, 100 × 1450 × 200, between the girders at each end of the runway | tie the two sides; 40 under the pallet's underside |
| finish | girders, legs, ties and pallet painted; rails bare steel | a design choice |

## Named nodes
`pallet` (translate, above). Colliders `pallet-frame` (the pallet, at rest), `runway-a` and `runway-b` (each girder with its rail),
`tie-a` and `tie-b` (the end ties) and `leg-a1` to `leg-a4`, `leg-b1` to `leg-b4`.

## Materials by layer
`M-STEEL-7035` the girders, legs, end ties and pallet (painted RAL 7035) · `M-SILVER` the rails (bare steel, shown in the
library's bright-metal layer).

## Notes
No load rating, no speed, change time or positioning accuracy: no sheet or bed mass and no drive figure are on file, so the table
is not sized against them. The volume is 515 808 000 mm³ (girders 2 × 130 000 000, rails 2 × 15 504 000, legs 8 × 3 600 000, end
ties 2 × 29 000 000, pallet 138 000 000; written as volume only: lib/materials.csv gives no densities, so no mass is stated). No
vendor names, no label.

## Outputs (out/)
`table-shuttle.lsp` · `.glb` (pivot on `pallet`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r80, unattended) |
