# frame-welded · v1.1 · welded machine frame 1200 × 800 × 850, square tube 80 and 60, top plate 15, 4 × M12 floor anchors

**What** A welded steel base frame for a machine: four square-tube legs on foot plates anchored to the floor, a top ring of tube
with one cross member, a lower ring that stiffens the legs, and a top plate whose top face is the machine's seat. The machines of
lib/machines-factory.txt (benders, press brakes, shears, saws, welders and others) stand on a frame of this kind; a BOM places
its machine on the frame's `mount`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks frame-welded
own_design "yes"). No product was matched and no vendor file was opened. The floor anchor holes are on file (ISO 273); every
other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the frame's centre x = 0, y = 0; the long side along x; front toward
−y. The top plate's top face, the machine's seat, is at z = 850.
**Built with** toolkit 1.3 · AutoLISP command `FRMWELD` · no parameters.

## Mechanism and the machine's seat
`mount` (fixed): the top plate. Its pivot is the centre of its top face (0, 0, 850) with the axis +z: a machine element is
placed there with its own base origin, so a BOM row reads `<tag>.mount`. The plate is plain in this version: the holes a machine
needs are drilled to that machine, so they come with the machine's own version of the frame, not with this one.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| floor anchors | 4 × M12, Ø13.5 holes, one in each foot plate's outboard corner, at 1230 × 830 (x ±615, y ±415) | ISO 273 medium (H13), lib/standards/holes.csv. The anchors are the site's: chosen to the floor, not built |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.2 at MMC to A, the foot plates' underside (the floor plane), the
holes located to each other (features.csv; H − F = 13.5 − 12 = 1.5). The ISO 2768-m general tolerance of their 1484 mm diagonal
(±1.2, a Ø3.4 zone) would not hold the pattern, so the frame is welded in a fixture and the foot plates drilled after welding.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| frame outside | 1200 × 800, top face 850 above the floor | a bench-height seat for a machine of the size the factory list holds |
| legs | 4, square tube 80 × 80, from the foot plates (z 15) to the top plate (z 835); outer faces flush with the top plate's edges | the tube carries the top ring at its full width |
| top ring | square tube 80 × 80, z 755 to 835: two long rails along x between the legs, two short rails along y, one cross member along y at x = 0 | the plate rests on the ring and the cross member; no span longer than 1040 |
| lower ring | square tube 60 × 60, z 200 to 260, on the legs' centre lines, welded between the legs | stiffens the legs against sway; 200 above the floor leaves room to clean under it |
| foot plates | 4, 180 × 180 × 15, centred on the legs (x 470 to 650, y 270 to 450) | each anchor hole's centre 15 from its leg's outer face (the hole's edge 8.25 from it) and 35 from the plate's two outer edges (the hole's edge 28.25 from them). Whether an M12 nut and washer clear the leg is not checked: no nut or washer table is on file |
| floor footprint | 1300 × 900 (x ±650, y ±450): the foot plates stand 50 beyond the 1200 × 800 frame on every side | what a layout reserves on the floor |
| top plate | 1200 × 800 × 15 | the machine's seat; plain, drilled to the machine |
| tubes | drawn by their outside: every tube end is welded shut against a leg or a plate, so no bore shows | the model shows what can be seen |
| welds | not drawn | |

## Named nodes
`mount` (fixed, above). Colliders `leg-lf`, `leg-lb`, `leg-rf`, `leg-rb` (the legs), `low-xf`, `low-xb`, `low-yl`, `low-yr`
(the lower ring), `mount` (the top ring and plate).

## Materials by layer
`M-STEEL-7035` everything (steel, painted RAL 7035).

## Notes
No load rating and no safety claim: no machine's mass or forces are on file, so the frame is not sized against them. Levelling
feet, grouting and cable pass-throughs are not modelled. No vendor names, no label.

## Outputs (out/)
`frame-welded.lsp` · `.glb` (pivot on `mount`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r47, unattended) |
| 1.1 | review frame-welded-1.0 finding 1 and note 1, text only: the anchor hole's distances to its leg and to the plate's edges both given centre and edge; the "room for an M12 nut and washer" claim dropped (no nut or washer table on file); the 1300 × 900 floor footprint stated. No model change (mech-r60, unattended) |
