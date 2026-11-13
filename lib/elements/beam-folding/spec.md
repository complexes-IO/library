# beam-folding · v1.0 · folding beam of a sheet folder, working length 1000, folds 0 to 135 degrees about the bend line, on its bed and two end cheeks

**What** The folding beam of a sheet folder (a swing-beam folding machine): the sheet lies on a fixed bed, the clamping beam holds
it down along the bend line (the bed's top front edge), and the folding beam in front of the bed swings up about that line and
folds the part of the sheet that sticks out. It is the beam-folding of folder-sheet (lib/machines-factory.txt line 24:
frame-welded (own), beam-folding (own), clamp-beam (own), hpu-0.37kw, hyd-cylinder-da-40 (x2), encoder, backgauge, ballscrew,
servo-motor, servo-drive, footswitch, op-estop-22-2nc, plc0, hmi-7in, light-curtain). The bed and the two end cheeks that carry the
beam's pins are drawn with it, because the bend line is the edge the bed and the folding beam share: one home for that line.
clamp-beam 1.0 reads its figures from this element.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks beam-folding own_design
"yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the bend line's centre: x = 0 midway along the working length, y = 0 the bed's front face,
z = 0 the bed's top face (the sheet's underside). The bend line runs along x; the folding beam stands in front (−y), the bed
behind (+y). Extents x −620 to 620, y −250 to 450, z −250 to 60 at rest.
**Built with** toolkit 1.3 · AutoLISP command `FOLDBEAM` · no parameters.

## Mechanism
`fold` (rotate about −x through the bend line (0, 0, 0), 0 to 135 degrees): the folding beam with its two pins. At 0 its top face
lies in the bed's plane (z = 0), its back face 2 in front of the bed's front face. Turning about −x lifts its front edge: at 90
degrees the beam stands upright in front of the bend line, at 135 degrees its top face leans back over the bed at 45 degrees, the
angle clamp-beam's nose is cut back to. Through the whole swing the beam stays in front of the bed's front face or above its top
face, and between the cheeks; the pins turn about their own axis in the cheeks' windows. The drive (folder-sheet places two
hyd-cylinders), its lugs, the end stops, an angle scale and the adjustment that moves the axis for the sheet's thickness are the
machine's or a later version's: not drawn.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| clamp-beam 1.0 | its nose 1000 long on the bed (y 0 to 400), its posts on the cheeks' tops (x ±560 to ±600, z 60) | clamp-beam reads HALF, BED_D, CHEEK_X0, CHEEK_T and CHEEK_TOP from this element (library.load) |
| frame-welded 1.1 | the cheeks' feet span 1200 × 700, inside the frame's top plate 1200 × 800 | the placing is the assembly's; the cheeks have no hole for it (OPERATING.md 12: a host doesn't model holes for a part it places later) |
| the sheet | lies on the bed's top face (z = 0) and sticks out past the bend line over the folding beam | no sheet thickness, length or strength is on file: no bending capacity is stated |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| working length | 1000 (x ±500): the folding beam's length | a bench-size folder on frame-welded |
| bed (lower beam) | 1120 × 400 × 200 (x ±560, y 0 to 400, z −200 to 0), between the cheeks | carries the sheet and clamp-beam's nose |
| folding beam | 1000 × 150 × 150 (y −152 to −2, z −150 to 0) | its top face the bed's plane at rest; 2 clear of the bed |
| swing | 0 to 135 degrees | 45 degrees past square, matched by clamp-beam's 45-degree nose relief |
| pins | Ø50, on the bend line, x ±500 to ±620 (20 proud of the cheeks) | the beam's hinge on the bend line itself |
| cheeks | 2, 40 × 700 × 310 (x ±560 to ±600, y −250 to 450, z −250 to 60), each with a 70 × 70 window round its pin (10 clear) | carry the pins; the bearing in the window is not drawn |
| bed notches | 35 × 35 at the bed's top front corners over x ±500 to ±560 | the pins pass there, 10 clear |
| finish | painted | a design choice |

## Named nodes
`fold` (rotate, above). Colliders `fold-beam` (the folding beam, at rest; named apart from its node), `bed`, `cheek-l` and
`cheek-r`.

## Materials by layer
`M-STEEL-7035` everything (painted RAL 7035).

## Notes
No bending capacity (sheet thickness, length, tensile strength), no folding force, speed or angle accuracy: no sheet, drive or load
figure is on file, so the beam is not sized against them. Volume and triangles: see the gates (lib/materials.csv gives no
densities, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`beam-folding.lsp` · `.glb` (pivot on `fold`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r81, unattended) |
