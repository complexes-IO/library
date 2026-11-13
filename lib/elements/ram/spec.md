# ram · v1.1 · press ram 2600 × 60 × 400 with two cylinder pads 200 × 120 × 30 and a tool seat 2500 × 40 × 20

**What** A press ram: the moving beam of a press brake that carries the upper tool down onto the sheet. A steel plate with a pad
on its top edge at each end, where the press's two cylinders bear on it, and a machined tool seat along its lower edge. The CNC
and sheet press brakes of lib/machines-factory.txt (press-brake-cnc, press-brake-sheet, each with two hyd-cylinder-da-40 that the two
pads take) carry their upper tool on a ram of this kind; a BOM places the tool clamp or the upper tool on the ram's `tool-seat`.
lib/inventory.csv also lists the turret punch (punch-turret) under this row; a turret punch strikes one punch at a time with a
short ram over its punching station, with no bending length and no pair of end cylinders, so this element is not that part
(lib/needs-em/mech.md item 84).
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks ram own_design "yes").
No product was matched and no vendor file was opened. The ram has no hole, thread or standard interface; every size is a design
choice.
**Units / frame** mm, Z up. Origin: the tool seat's underside z = 0 (the upper tool's seat) at the ram's centre x = 0, y = 0;
the ram's length along x; front toward −y. The cylinder pads' top faces are at z = 450.
**Built with** toolkit 1.3 · AutoLISP command `RAM` · no parameters.

## Mechanism and the upper tool's seat
`tool-seat` (fixed): the machined strip along the ram's lower edge. Its pivot is the centre of the seat's underside (0, 0, 0)
with the axis −z: a tool clamp or upper tool element is placed there with its own top origin, so a BOM row reads
`<tag>.tool-seat`. The ram has no moving part of its own. Its up and down stroke belongs to the press: the assembly moves the
whole element along z with its cylinders, and the ram carries the seat and whatever stands on it.

## What it meets
| what | how |
|---|---|
| the press's cylinders (hyd-cylinder-da-40, x2) | each bears on a pad's top face (z = 450, centres x ±1050, 2100 apart). How a rod end is held to its pad (a flange, a ball seat, a pin) belongs to the cylinder and the press, so the pads have no hole for it in this version |
| the press's frame and guides | the ram's end faces (x ±1300) and its 60-thick faces run in the frame's side guides. The guides, gibs and their clearances belong to the press (frame-welded's own version for a press brake), so the ram carries no guide of its own |
| the tool clamp (clamp-tooling) and the upper tool (tooling-press-brake) | stand under the seat's underside (z = 0, 2500 × 40). Neither is built yet, so the seat has no hole for them (OPERATING.md 12: a host doesn't model holes now for a part it places later); the clamp's fixing comes with the ram's next version, once the clamp defines it |
| the stroke's sensors (encoder, x2) | belong to the press: placed by its assembly, not built here |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| ram plate | 2600 long (x −1300 to 1300), 60 thick (y −30 to 30), 400 high (z 20 to 420) | a mid-size press brake of the factory list, its seat as long as a 2500 bending length with 50 to spare at each end; 400 high and 60 thick in proportion (no force or deflection claim is made for it) |
| tool seat | 2500 long (x −1250 to 1250), 40 deep (y −20 to 20), 20 high (z 0 to 20), on the plate's centre line | the upper tool's seat over the full bending length, narrower than the plate so its machined faces stand clear of the plate's |
| cylinder pads | 200 along x, 120 across (y −60 to 60, 30 over each face of the plate), 30 thick (z 420 to 450), centres at x ±1050 | a flat seat for each cylinder's rod end, inside the ram's ends so both cylinders push on the plate and not on its corners |
| body | drawn by its outside: one plate, solid | the model shows what can be seen |
| crowning, stroke stops, lifting eyes, the clamp's fixing holes | not drawn | they belong to the press, or to a later version once their parts are on file |

## Named nodes
`tool-seat` (fixed, above). Colliders `seat` (the tool seat; not named like its node, so Godot keeps the node's name), `ram` (the plate), `pad-a` and `pad-b` (the cylinder pads).

## Materials by layer
`M-STEEL-7035` the plate and pads (painted RAL 7035) · `M-SILVER` the tool seat (bare machined steel, shown in the library's
bright-metal layer; the library has no `M-STEEL` render material).

## Notes
No force rating, no stiffness, deflection, parallelism or crowning claim: no press force, bending length rating or tool load is
on file, so the ram is not sized against them. The volume is 65 840 000 mm³ (plate 62 400 000, seat 2 000 000, pads
2 × 720 000; written as volume only: lib/materials.csv gives steel no density, so no mass is stated). No vendor names, no
label.

## Outputs (out/)
`ram.lsp` · `.glb` (pivot on `tool-seat`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r59, unattended) |
| 1.1 | text only, the part unchanged (mech-r67, unattended; review ram-1.0 finding 1): "What" and element.py's docstring name the two press brakes only; the turret punch's ram is put to EM and the core as its own row (needs-em 84); behaviour.csv added (lib/behaviour.md: no terminal, no moving node, no state) |
