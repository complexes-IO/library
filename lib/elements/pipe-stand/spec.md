# pipe-stand · v1.0 · roller pipe stand, two free rollers Ø80 × 200 at 180 centres, roller axes 780 above the floor, base plate 600 × 400

**What** A roller pipe stand for the pipe-cutter (lib/machines-factory.txt line 16: pipe-cutter places frame-welded, motor-iec,
chuck-3jaw, blade-circular, pipe-stand, coolant-pump, limit-switch, pbs-6h-22, op-estop-22-2nc and guard-panel). A long pipe fed into
the cutter rests on the stand's two rollers and rolls along them, or turns on them, so its far end needs no hand to hold it.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks pipe-stand own_design
"yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the base plate, x = 0, y = 0. The pipe runs along y
over the stand; the rollers' axes run along y at x −90 and +90, z 780.
**Built with** toolkit 1.3 · AutoLISP command `PIPESTAND` · no parameters.

## Mechanism
Two free rollers, nodes `roller-1` (x −90) and `roller-2` (x +90), each rotating about its own axis (along y), 0 to 360 degrees:
a spin, with no stop. A pipe resting on them turns them as it is fed along or turned. The axles and their bearings are not drawn:
each roller's end faces stand 10 clear of the bearing blocks and 20 above the head plate, so a roller touches nothing at rest or
as it turns. No height adjustment: the stand is one height. behaviour.csv: state `still` (default) and `turning` (manual toggle,
the pipe's handling), pose of both rollers at the range end in `turning`.

## What it meets (figures from files on hand)
Nothing on file. The pipe is the cutter's stock: no pipe size table is on file, so the stand is not sized to one. By its geometry a
pipe wider than the 100 clear between the rollers rests on both; a narrower one drops between them onto the head plate. The pipe
cutter's work height is not on file either, so the rollers' height is not matched to it (the assembly places the stand). Its
fixing to the floor, if any, is the assembly's, so the base plate has no hole (OPERATING.md 12).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate | 600 × 400 × 20 (x ±300, y ±200, z 0 to 20) | a design choice; 20 thick, not 10, so no edge of 3 to 10 stands between two free corners at the fillet gate (rack-bar 1.0's first AutoCAD run) |
| column | 80 × 80 square tube, drawn by its outside, z 20 to 700 | a design choice; its top is closed by the head plate |
| head plate | 400 × 260 × 20 (x ±200, y ±130, z 700 to 720) | carries the four bearing blocks; its y ends flush with the blocks' outer faces |
| bearing blocks | 4, each 60 (x) × 20 (y) × 80 (z), z 720 to 800, centred on a roller's axis in x, at y 110 to 130 and −130 to −110 | hold the (not drawn) axles; the blocks' top is 20 above the axes |
| rollers | 2, Ø80 × 200 (y −100 to 100), axes at x ±90, z 780 | 180 between centres, 100 clear between the rollers; their tops at z 820, their undersides 20 above the head plate |
| the pipe | not drawn | the cutter's stock, not the stand |

## Named nodes
`roller-1` (x −90), `roller-2` (x +90): rotate about y through their axes, range 0 to 360 degrees. Colliders: `base`, `post`, `head`,
`roll-seat-1`, `roll-seat-2` (each roller's bounding box; none is named like a node).

## Materials by layer
`M-STEEL-7035` the base plate, column, head plate and bearing blocks (painted steel, RAL 7035) · `M-SILVER` the rollers (bright
steel, the library's bright-metal layer).

## Notes
No load rating, no pipe size range and no stability claim: no pipe's mass or diameter is on file, so the stand is not sized
against them, and whether it needs fixing to the floor is decided where it is placed. The volume is 13 626 619 mm³: the fixed body
11 616 000 (base plate 4 800 000, column 4 352 000, head plate 2 080 000, blocks 4 × 96 000) and the rollers 2 × 1 005 310
(written as volume only: lib/materials.csv gives steel no density, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`pipe-stand.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r71, unattended) |
