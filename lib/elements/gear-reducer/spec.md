# gear-reducer · v1.0 · worm gear reducer, foot mounted, input shaft Ø14 x 30 at motor-iec71-370w's shaft height, output shaft Ø20 x 40, centre distance 40, 4 × M8 foot holes

**What** A worm gear reducer: it takes a motor's speed down by its ratio and turns the output shaft at right angles to the
input. A closed housing stands on its own base plate; the input (worm) shaft comes out of the housing's −y face at the motor's
shaft height, so a foot motor standing on the same floor or plate lines up with it and a coupling joins the two shafts; the output
(wheel) shaft runs along x, 40 above the input, and comes out of the +x face for the machine's drive (a sprocket, a pulley, a
coupling or a pinion, the assembly's). lib/machines-factory.txt and lib/machines-from-elements.txt list it in eight systems
(bender-section, mechanisms-bench, positioner-welding, roll-plate, rotary-index-table, rotator-welding, saw-band-auto,
saw-circular-metal). The two shafts are the mechanism: the twin turns them by name.
**Class** machine · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks the row own_design "yes";
request mech-13's answer, 2026-11-12: no gearbox class on file, EC010529 being a valve actuator's worm gearbox). No product was
matched and no vendor file was opened. The folder held a catalogue search record from 2026-11-03 (another maker's worm gearbox
with a flange input), moved to references/source.txt by `build.py own` (DOC-007); no size is taken from it. What it meets is on
file (ISO 273, motor-iec71-370w) or named below; every other size is a design choice. No torque, efficiency, speed, thermal or
service-factor rating is claimed (mech-13's answer): the reducer has no rating of its own (OPERATING.md 12).
**Units / frame** mm, Z up. Origin: the floor plane z = 0 (the base plate's underside), x = 0 the plane through the input shaft's
axis, y = 0 the plane through the output shaft's axis. The input shaft runs along y at z 71 and comes out toward −y; the output
shaft runs along x at z 111 and comes out toward +x. Extents x −75 to 97, y −92 to 65, z 0 to 160.
**Built with** toolkit 1.3 · AutoLISP command `GEARREDUCER` · parameter `ratio` (default 20; 5 to 100).

## The ratio
The ratio is a design figure and a parameter (mech-13's answer): 20 by default, any value from 5 to 100 for a single worm stage in
this housing (design choice). It changes the worm's starts and the wheel's teeth inside the housing, which are not drawn, so the
outside and the two shafts are the same for every ratio; the output turns 1 / ratio of the input's turn (behaviour.csv). A ratio
outside 5 to 100 is refused by build(). The ratio is the assembly's to choose; no output speed or torque is claimed for any ratio.

## What it meets
| figure | value | source |
|---|---|---|
| foot holes | 4 × M8, Ø9.0 through the base plate at 120 × 100 (x ±60, y ±50) | ISO 273 medium (H13), lib/standards/holes.csv. M8 is this design's choice. The screws are the assembly's; nothing is placed in the holes |
| floor or machine plate | the base plate's underside, z = 0 | a flat surface; the assembly's |
| the motor | the input shaft's axis at z 71 = motor-iec71-370w's shaft height (its SH 71, read by library.load), so the motor standing on the same surface has its shaft on this axis; the input shaft drawn at that motor's shaft size, Ø14 × 30 past the input boss's face (y −62 to −92) | motor-iec71-370w 1.5 (its drawing p. 1 figures, as that element gives them). That motor is a B3 foot motor with no flange, so the reducer meets it by its shaft through a coupling, not by a flange; the coupling (coupling-shaft, not built) and the motor are placed by the assembly, and the motor stands with its shaft end facing y −92 at the coupling's length from it |
| the shafts' keys | the input Ø14 and the output Ø20 are drawn plain: no key and no keyway | NOT ON FILE (B): DIN 6885-1 (parallel keys: the key's section for each shaft diameter and the keyway depths in shaft and hub). The keys are drawn when that table is on file; motor-iec71-370w's keyway waits on the same document |
| the output's drive | the output shaft Ø20 × 40 past the +x boss's face (x 57 to 97), on the axis y 0, z 111 | Ø20 and 40 are this design's choices (OPERATING.md 12, own designs); the sprocket, pulley, coupling or pinion on it is the assembly's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four foot holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane x = 0 through the input
shaft's axis) and C (the plane y = 0 through the output shaft's axis) (features.csv; T ≤ H − F = 9.0 − 8 = 1.0).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate | 150 (x ±75) × 130 (y ±65) × 16 | the reducer's feet as one plate, so it is set and screwed down as one; 16 thick so its corner edges fillet whole |
| housing body | 90 (x ±45) × 100 (y ±50), from the base plate (z 16) to z 160 | holds the worm and the wheel (not drawn) and their bearings; 49 over the output axis for the wheel |
| centre distance | 40, the output axis 40 above the input (z 111 over z 71) | the worm under the wheel, so the input sits at the motor's low shaft height and the output higher for the machine's drive |
| input boss | Ø56 × 12 on the −y face (y −62 to −50), bore Ø16 through it and 30 into the body | carries the input's bearing (not drawn) |
| input end cover | Ø56 × 8 on the +y face (y 50 to 58), closed | closes the worm's other bearing; the input is single-ended |
| output bosses | Ø64 × 12 on both x faces (x ±45 to ±57), bore Ø22 through both and the body | carry the output's bearings (not drawn); the −x side is open for a shaft on that side in a later version |
| input shaft | Ø14 from y −25 (inside its bore) to y −92 | the motor shaft's size, so one coupling size joins them |
| output shaft | Ø20 from x −55 (2 inside the −x boss's face) to x 97 | single-ended toward +x |
| the worm, the wheel, bearings, seals, oil fill, drain and breather plugs, a torque arm, a hollow output | not drawn | internal or the maker's detail; a hollow output or a second output end would be another version |

## Mechanism
Two moving nodes, each a plain shaft turning about its own axis, 0 to 360 degrees: a spin, with no stop. `input` turns about y
through (0, −62, 71); `output` turns about x through (57, 0, 111). The output turns 1 / ratio of the input's turn: the worm and the
wheel that couple them are inside the housing and not drawn, so the twin turns both nodes and the ratio is the coupling between them.
Neither shaft touches the housing: each stands 1 clear of its bore all round (Ø14 in Ø16, Ø20 in Ø22), the bearings not drawn.
behaviour.csv: state `still` (default) and `running` (manual toggle: the assembly's motor), pose of both shafts at the range end in
`running`.

## Named nodes
`input`: rotate about −y through (0, −62, 71), range 0 to 360 degrees. `output`: rotate about +x through (57, 0, 111), range 0 to
360 degrees. Colliders: `base-plate`, `housing` (the body with its bosses and the end cover; none is named like a node).

## Materials by layer
`M-CAST-BLUE` the base plate, housing body, bosses and end cover (painted cast housing) · `M-SILVER` the two shafts (bright steel).

## Decals (Blender)
"complexes.org" on the housing's −x side.

## Notes
No vendor names, part numbers or marks. No torque, power, speed, efficiency, self-locking, thermal or service-factor figure is
claimed, and no safety claim; the reducer is not guarded: a guard over the coupling and the output's drive is the assembly's
(ISO 13857 distances). Not drawn: the worm and the wheel, the bearings and seals, oil plugs, the keys and keyways (DIN 6885-1, above).

## Outputs (out/)
`gear-reducer.lsp` · `.glb` (pivots on both shafts) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r111, unattended, 2026-11-12) |
