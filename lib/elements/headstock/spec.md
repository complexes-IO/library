# headstock · v1.1 · headstock housing 480 × 400 × 380 on a 500 × 440 base foot, spindle seat 180 dia at centre height 260

**What** A headstock housing: the box at the left end of a lathe or a cylindrical grinder that carries the work spindle. A base
foot that stands on the bed's two ways, a closed box housing on it, and a machined spindle seat on the face toward the work. The
CNC and conventional lathes (lathe-cnc, lathe-conventional) and the cylindrical grinder (grinder-cylindrical) of
lib/machines-factory.txt carry their work spindle in a housing of this kind; a BOM places the spindle on the headstock's
`spindle-seat` and the headstock on the bed's `ways` (bed-cast).
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks headstock own_design
"yes"). No product was matched and no vendor file was opened. The headstock has no hole, thread or standard interface; every
size is a design choice.
**Units / frame** mm, Z up. Origin: the base foot's underside z = 0 (its seat on the bed's ways) at the headstock's centre x = 0,
y = 0; the spindle axis along +x (toward the work and the tailstock) at y = 0, z = 260; front toward −y. The spindle seat's face
is at x = 270.
**Built with** toolkit 1.3 · AutoLISP command `HEADSTK` · no parameters.

## Mechanism and the spindle's seat
`spindle-seat` (fixed): the machined boss on the housing's +x face. Its pivot is the centre of the boss's face (270, 0, 260) with
the axis +x, the spindle axis: a spindle element is placed there with its own origin on its nose's seat and turns on its own node,
so a BOM row reads `<tag>.spindle-seat`. The headstock has no moving part of its own: on a lathe it stands fixed on the bed.

## What it meets
| what | how |
|---|---|
| the bed's ways (bed-cast 1.0, `ways` at its top plane z = 430; ways 80 wide at y ±130 to ±210) | the foot's underside (z = 0) stands on both ways: the foot is 440 across (y ±220), so it covers each way's full width with 10 to spare outside. How the headstock is clamped and aligned to the bed (bolts, clamping plates, a key) belongs to the machine, so the foot has no hole for it in this version |
| the work spindle, its nose, bearings and drive | placed on `spindle-seat`. None is built yet, so the seat has no bore (OPERATING.md 12: a host doesn't model holes now for a part it places later). The spindle nose follows ISO 702 once that standard is on file; the bore and the bearing seats come with the headstock's next version, from the spindle element |
| the gears, belts, motor, lubrication and controls | belong to the machine: placed by its assembly, not built here |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base foot | 500 along x (x −250 to 250), 440 across (y −220 to 220), 40 thick (z 0 to 40) | spans the two ways of bed-cast with 10 outside each; 10 longer than the housing at each end and 20 wider at each side, a step that shows the foot |
| housing | 480 along x (x −240 to 240), 400 across (y −200 to 200), from the foot (z 40) to its top face (z 420) | a design choice; whether a spindle and its bearings fit is checked when the spindle element is on file; drawn by its outside: a cast housing is closed, its cores and ribs are not seen |
| spindle axis | y = 0, z = 260 above the foot's underside (so 690 above the bed's base when placed on bed-cast) | a design choice: the housing's centre across, 160 below the housing's top; whether the spindle's bearings fit about it is checked when the spindle element is on file |
| spindle seat | a boss 180 dia, 30 proud of the housing's +x face (x 240 to 270), on the spindle axis | the machined face the spindle's nose flange seats against |
| covers, oil level window, lifting eyes, the clamping to the bed | not drawn | they belong to the machine, or to a later version once their parts are on file |

## Named nodes
`spindle-seat` (fixed, above). Colliders `nose` (the spindle seat; not named like its node, so Godot keeps the node's name),
`foot` (the base foot) and `housing` (the housing).

## Materials by layer
`M-STEEL-7035` the base foot and housing (painted RAL 7035) · `M-SILVER` the spindle seat (bare machined steel, shown in the
library's bright-metal layer; the library has no `M-STEEL` render material).

## Notes
No speed, power, load, run-out or accuracy claim: no spindle, bearing or cutting force figures are on file, so the headstock is
not sized against them. The volume is 82 523 407 mm³ (foot 8 800 000, housing 72 960 000, seat 763 407; written as volume only:
lib/materials.csv gives steel no density, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`headstock.lsp` · `.glb` (pivot on `spindle-seat`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r60, unattended) |
| 1.1 | text only, the part unchanged (mech-r67, unattended; review headstock-1.0 finding 1): the housing's and the spindle axis's "why" cells written as design choices, with no fit claimed for a spindle or bearings not on file; behaviour.csv added (lib/behaviour.md: no terminal, no moving node, no state) |
