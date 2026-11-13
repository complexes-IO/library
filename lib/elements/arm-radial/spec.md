# arm-radial · v1.1 · radial drill arm, reach 1500 from the column's axis, swing 90 each way, seat 400 × 400 on column's top, two flat ways 60 wide

**What** The arm of a radial drill (lib/machines-factory.txt: drill-radial places base-cast, column, arm-radial, spindle-drill,
gearbox-headstock and table-slotted): the part that swings about the column and carries the drill head out over the work. A seat
plate sits on column's top face; on it a round hub carries a box-section beam that reaches forward of the column's axis, with a
short tail behind it; two flat ways on the beam's top face carry the drill head along the arm. A BOM places the drill head on the
arm's `arm` node, so the head swings with it.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks arm-radial own_design
"yes"). No product was matched and no vendor file was opened. The seat's size comes from column 1.1; every other size is a design
choice.
**Units / frame** mm, Z up. Origin: column's top face z = 0 (the arm's seat) on the column's axis x = 0, y = 0; at rest the arm
reaches toward −y, the column's front (the side of its ways); it swings about z. The ways' top plane, the drill head's seat, is at
z = 550.
**Built with** toolkit 1.3 · AutoLISP command `RADARM` · no parameters.

## Mechanism
`arm` (rotate, axis +z through the column's axis, −90 to 90 degrees): the hub, the beam and its two ways. At rest (0) the beam
reaches toward −y; at either end of its range it reaches along ±x. Its pivot is the hub's underside on the axis, (0, 0, 30). The hub
sits on the seat plate (z 30) through the whole swing; the beam stands 200 over the seat plate, so nothing fixed is in its path,
and MOT-010 sweeps it. In this form the arm's height is fixed: it sits on column 1.1's top face and cannot travel along the
column (needs-em 87; an elevating arm is column-round with arm-radial 2.0). The drill head's travel along the ways is the
machine's, between the elements, so the arm has no node for it, as saddle and carriage.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the column's top face | 400 × 400 (x, y ±200), at z 1600 above the column's base flange underside | column 1.1 (`BODY_W`, read by library.load("column"); `BODY_TOP` 1600, element.py) |
| the column's front ways | two flat ways at x ±130, 25 proud of the front face (y −225), from z 400 to 1560 | column 1.1 (element.py): below the seat, so the arm never meets them |

Placed on column at (0, 0, 1600), the seat plate covers the column's top face exactly; the beam's underside stands 1830 above the
column's base flange underside, and the ways' top plane 2150. At rest the beam reaches 1275 beyond the column's front ways'
plane (y −225), 1300 beyond its body's front face (y −200). Where the drill head, the table-slotted and the work sit under the arm is the machine's.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| seat plate | 400 × 400 × 30 (z 0 to 30) | as wide as the column's body, so it covers the top face and no more; 30 thick a design choice |
| hub | Ø380, 200 high (z 30 to 230), on the axis | a design choice: inside the seat plate at every angle |
| beam | 300 wide (x ±150), 300 deep (z 230 to 530), from y 200 (tail) to y −1500 (reach) | a design choice: the reach 1500 from the axis; the 200 tail over the hub |
| ways | 2, 60 wide at x ±90, 20 proud of the beam's top (z 530 to 550), from y −1450 to −300 | a design choice: the drill head's seat, 1150 of length along the arm; kept 50 short of the beam's end and inside its sides |
| swing | 90 degrees each way about the axis | a design choice: a half turn in all; whether the head then reaches a given table or work position is checked when spindle-drill and table-slotted are on file |
| hub, beam | drawn by their outsides: cores, ribs and the beam's inside are not seen | the model shows what can be seen |
| height on the column | fixed: the seat on column 1.1's top face | this form has no elevating screw and no clamp on the column; an elevating arm is column-round with arm-radial 2.0 (needs-em 87) |
| the hub's bearing and clamp, the head's rack and the seat's fixing to the column | not drawn | they belong to later elements |

## Named nodes
`arm` (rotate, above). Colliders `seat` (the seat plate) and `beam` (the hub and the beam with its ways, at rest); neither is named
like a node.

## Materials by layer
`M-STEEL-7035` the seat plate, hub and beam (painted RAL 7035) · `M-SILVER` the two ways (bare machined steel, the library's
bright-metal layer, as column's ways).

## Notes
No load rating, no stiffness or accuracy claim: no machine's mass, drilling forces or way tolerances are on file, so the arm is not
sized against them. The volume is 183 240 000 mm³ (seat plate 4 800 000, hub 22 680 000, beam 153 000 000, ways 2 × 1 380 000;
written as volume only: lib/materials.csv gives steel no density, so no mass is stated). No hole: the seat's fixing, the head's
rack and the clamps come with the parts they hold (OPERATING.md 12: a host doesn't model holes for a part it places later). No
vendor names, no label.

## Outputs (out/)
`arm-radial.lsp` · `.glb` (pivot on `arm`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r68, unattended) |
| 1.1 | text only (review arm-radial-1.0 findings 1 and 2): the reach is 1275 beyond the ways' plane (1300 beyond the body's face); the arm's height is fixed on column 1.1 in this form, no elevating screw or column clamp claimed; no geometry change (mech-r79, unattended) |
