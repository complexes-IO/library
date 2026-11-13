# lift-transfer · v1.0 · lift-and-transfer unit, own design, for a conveyor-roller 1.0 section: base 480 × 240 with 4 × M12 anchor holes, two posts, lift carriage with three strips rising 20

**What** A pneumatic lift-and-transfer unit: it stands on the floor inside a roller conveyor section, between the rollers, and
moves goods from that line onto the one beside it. A base plate anchored to the floor carries two guide posts; on them rests the
lift carriage, a plate with three transfer strips that stand up through the gaps between the conveyor's rollers. Lowered, the strips'
tops are 5 under the rollers' tops and goods roll over them along the line; raised 20, the strips stand 15 above the rollers, take
the goods off them and carry them sideways (along x) onto the next line. It is the lift-transfer of conveyor-types-bench
(lib/machines-from-elements.txt line 22: one section of every conveyor type, EM 2026-11-08).
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks lift-transfer own_design "yes";
the folder's record, metadata.json and references/source.txt, says "own build, no vendor search", nothing downloaded). No product was
matched and no vendor file was opened. The strips are placed in conveyor-roller 1.0's roller gaps (read with library.load, so the two
cannot drift apart); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the base plate, which is the conveyor section's centre
(conveyor-roller's origin): x across the conveyor, the transfer direction; y along it. Extents x −240 to 240, y −120 to 120, z 0 to
745 at rest (765 raised).
**Built with** toolkit 1.3 · AutoLISP command `LIFTTRANSFER` · no parameters.

## Mechanism
`lift` (translate along +z, 0 to 20 mm): the carriage, a plate 460 × 170 × 10 (z 660 to 670) with three strips 470 × 12 × 75 on its
top (z 670 to 745). At 0 it rests on the two posts' tops (z 660) with the strips' tops at z 745, 5 under the rollers' tops (750):
goods pass over them. At 20 the plate's top stands at z 690, 10 under the rollers' undersides (700), and the strips' tops at z 765,
15 above the rollers' tops: the goods ride on the strips. Its pivot is the centre of the plate's top face at rest (0, 0, 670), the
axis +z. Nothing of this element lies in its path (MOT-010 sweeps it). The cylinder that lifts it (between the posts, under the
plate's centre), its valve, the sensors that read its two positions, and the transfer drive on the strips (rollers, belts or a
pusher) are placed in a later version once their elements are on file: none is drawn here, so the carriage lifts without a visible
actuator in the model and the strips are plain bars.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| conveyor-roller 1.0 | the strips stand in the gaps between rollers 9-10, 10-11 and 11-12 (y −75, 0, 75; the gaps are 25 wide at the rollers' axes, the strips 12, so 6.5 clear of each roller); their ends at x ±235 are 10 inside the rollers' end faces (±245) and 15 inside the side frames' inner faces (±250); lowered the strips' tops are 5 under the rollers' tops (750), raised 15 above; the carriage plate's top stays 10 under the rollers' undersides (700) at full lift; the base plate (y ±120) and posts stand clear of the section's supports (y ±500) | conveyor-roller's TOP, ROLL_R, PITCH, roller_y, W and ROLL_GAP (library.load); the section is placed by the assembly with its centre on this origin |
| the floor | 4 × Ø13.5 holes in the base plate at 400 × 180 (x ±200, y ±90) | M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv); position Ø1.0 at MMC to A the floor plane, B the plane midway between the posts, C the plane through the posts' centres (ASME Y14.5 floating fastener, T ≤ H − F = 1.50; features.csv). The anchors are the assembly's |
| the next conveyor line | none in this element | the transfer height, the strips' tops at z 765 raised, is a design choice; the receiving line's hand-off height is the assembly's to match |
| the cylinder | none in this element | the air cylinder, its mounting and ports come with the cylinder element, placed in a later version (OPERATING.md 12: a host doesn't model holes for a part it places later) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate | 480 × 240 × 10 (x ±240, y ±120, z 0 to 10), 4 × Ø13.5 anchor holes at 400 × 180 | the unit's footprint on the floor, inside the section's frames (x ±250) and between its supports; the holes clear the posts |
| guide posts | 2, 40 × 40, at x ±200 on y 0, z 10 to 660 | carry the carriage at rest and guide it (the guide bushes are not drawn); 360 apart, so the cylinder fits between them |
| carriage plate | 460 × 170 × 10 (x ±230, y ±85), z 660 to 670 | the plate the strips stand on; its ends 5 inside the strips' ends, so no face is flush across the two materials (GEO-050) |
| strips | 3, 470 × 12 × 75 (x ±235), at y −75, 0, 75, z 670 to 745, bare steel | one per roller gap at the section's centre; 12 wide for 6.5 clear of each roller; 75 tall so the tops stand at 745 |
| lift | 20 | 5 under the rollers' tops to 15 above them: enough to lift the goods clear |
| finish | base, posts and plate painted; strips bare steel | a design choice |

## Named nodes
`lift` (translate, above). Colliders `base` (the base plate), `post-l` and `post-r`, `carriage` (the plate and strips as one box, at
rest).

## Materials by layer
`M-STEEL-7035` the base plate, posts and carriage plate (painted RAL 7035) · `M-SILVER` the strips (bare steel, shown in the
library's bright-metal layer).

## Notes
No load rating, no speed or cycle time: no goods mass, no air pressure and no cylinder figure are on file, so the unit is not sized
against them. The volume is 5 277 274 mm³ (base 1 152 000 less four holes 5 726, posts 2 × 1 040 000, plate 782 000, strips
3 × 423 000; written as volume only: lib/materials.csv gives no densities, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`lift-transfer.lsp` · `.glb` (pivot on `lift`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r106, unattended) |
