# enclosure-machine · v1.0 · machine enclosure 2400 × 2000 × 2200, sheet 2.0, two sliding front doors with windows, two side windows, 4 × M10 feet

**What** A sheet-metal machine enclosure: a box of 2.0 sheet, open at the bottom, that stands on the floor round a machine tool
(the CNC lathes, vertical mills and machining centres, laser cutters and the measuring machine of lib/machines-factory.txt). The
front wall has a loading opening closed by two sliding doors, each with a clear window; each side wall has a fixed clear window.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks enclosure-machine
own_design "yes"). No product was matched and no vendor file was opened. The floor-anchor holes are on file (ISO 273); every other
size is a design choice.
**Units / frame** mm, Z up. Origin: the floor z = 0 (the enclosure's underside) at the centre of its width x = 0; y = 0 the front
wall's outer face; the depth toward +y. The doors and their rails stand in front of the front wall, toward −y.
**Built with** toolkit 1.3 · AutoLISP command `MENCL` · no parameters.

## Mechanism
| node | kind | pivot | axis | range | what moves |
|---|---|---|---|---|---|
| `door-l` | translate | (−300.5, −10, 1150), the door's back face centre | −x | 0 to 580 | the left door, its window pane and handle |
| `door-r` | translate | (300.5, −10, 1150) | +x | 0 to 580 | the right door, its window pane and handle |

Closed (0), the two doors meet 2 apart at x = 0 and lap the opening by 50 at each side and 60 above and below. Open (580), each
door's meeting edge is at x ∓581, 31 clear of the opening's edge, and its outer edge at x ∓1180, still under the rails (which end at
x ∓1190). The doors hang under the top rail and run over the bottom rail with 5 clear of each; the rollers and guides are not drawn,
so the doors touch nothing at rest (they ride on their pivots).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| floor anchors | 4 × M10, Ø11.0 holes through the four corner feet (centres x ±1158, y 42 and 1958) | ISO 273 medium (H13), lib/standards/holes.csv. The anchors themselves belong to the assembly: not built |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø0.8 at MMC to A, the feet's undersides on the floor, the holes located
to each other (features.csv; H − F = 11.0 − 10 = 1.0). The ISO 2768-m general tolerance of their 3006 mm diagonal (±2.0,
lib/standards/general-tolerances.csv row m 2000-4000) would not hold the pattern, so the floor anchors are drilled through the
feet once the enclosure stands where it goes, and the floor holes follow the feet.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| outside | 2400 wide (x), 2000 deep (y), 2200 high (z) | room round a mid-size machining centre or lathe with its door travel |
| sheet | 2.0 everywhere (walls, roof, feet 6.0) | a sheet enclosure; stiffeners and folded edges are not drawn |
| walls | the side walls full depth under the roof; the front and back walls between them; the roof over all four; the bottom open | the machine's base stands inside on the same floor |
| loading opening | 1100 wide (x −550 to 550), 1500 high (z 400 to 1900) | a pallet or chuck loaded from the front at standing height |
| doors | two, 599 wide, 30 thick (a double wall drawn by its outside), z 340 to 1960, 10 in front of the front wall (y −40 to −10) | two sliding doors open the whole opening without swinging into the aisle |
| door travel | 0 to 580 each, outward | the opening fully clear when open |
| door windows | x 60 in from each door edge, z 900 to 1850, clear pane 6 thick centred in the door | the operator sees the work area at eye height |
| rails | top and bottom, 40 high, 45 deep from the front wall, x −1190 to 1190; top z 1965 to 2005, bottom z 295 to 335 | the doors hang and run on them over their whole travel |
| handles | one vertical bar per door, 300 long, at z 950 to 1250, its inner face 25 from the meeting edge | the hand meets it at the meeting edge |
| side windows | one per side wall, cut-out y 700 to 1300, z 1000 to 1700; a clear pane 6 thick inside the wall, lapping 30 round the cut-out | a view of the work area from the side |
| feet | four, 80 × 80 × 6, inside the corners, on the floor | carry the anchors inside, where nothing stands proud of the walls |
| rollers, guides, door seals, the door interlock, stiffeners, lights, cable entries, chip and coolant parts | not drawn | they belong to the machine and the assembly that places the enclosure |

## Named nodes
`door-l`, `door-r` (translate, above). Colliders `door-l`, `door-r`, `roof`, `back`, `side-l`, `side-r`, and the front wall round
its opening as `front-l`, `front-r`, `front-top` and `front-sill`, so a closed door shuts the opening and an open one leaves it free.

## Materials by layer
`M-STEEL-7035` walls, roof and feet (painted RAL 7035) · `M-BLUE` the doors · `M-CASE-CLEAR` the window panes (clear) · `M-SILVER`
the rails (bare steel, the library's bright-metal layer) · `M-ZINC` the handles.

## Notes
No safety claim. The enclosure is a fixed guard with movable guards (the doors) in its shape only: the safety distances, the
window's impact resistance, the interlocking of the doors and any guard locking are the assembly's and the machine's, and the
standards they would follow are not on file here. No load rating, no vendor names, no label.

## Outputs (out/)
`enclosure-machine.lsp` · `.glb` (pivots on `door-l`, `door-r`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r51, unattended) |
