# actuator-valve · v1.0 · generic pneumatic quarter-turn valve actuator, rack and pinion, double-acting, NPT 1/4 female ports

**What** the pneumatic actuator that turns a quarter-turn valve (a ball valve, a butterfly valve) open and shut: two pistons in an
aluminium body drive racks on one pinion, whose shaft turns the valve below it through 90°. Air into `port-2` drives the pistons
apart and turns the shaft counter-clockwise seen from above, to open; air into `port-4` drives them together, to close; a 5/2 valve
(valve-sol-52-sr) feeds the two. The `shaft`'s top carries a position indicator bar: along the body closed, across it open.
lib/inventory.csv row `actuator-valve` (own_design generic, ETIM EC011197, gap list 2026-11-05): the actuator valve-ball and
valve-butterfly are made of (0 systems of its own; it counts through those two). Its row's made_of, two fitting-pushin, is placed
by the host that pipes it, not drawn here (fitting-pushin 2.0 is not yet past station 6; OPERATING.md 12, quality at the source).
**Class** actuator · **Baseline** our own design: generic pneumatic servomotor for valves (ETIM 10.0 EC011197), as OPERATING.md 12
(generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or measured. The class
values below are its design inputs; its sizes are design choices; its ports take their thread from the standard on file (ASME
B1.20.1, through toolkit/pneu.py) and their numbers from ISO 11727 (pneu.NODES). The valve interface underneath is ISO 5211's, which
is not on file, so it is not drawn (Open figures). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the mounting pad's underside, on the shaft's axis (the face the valve's flange
meets); the shaft along +z, the body's length along x, the air ports on the front (−y). Ports follow pneu.py's port frame: the
pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `ACTUATOR-VALVE` · no parameters (one size).

The class: EC011197 "Pneumatic servomotor for valves" (tier 2, group EG020084 "Valve actuators", 26 features on file; synonyms
"Pneumatic actuator for valve", "Actuator for valves"), the class inventory row `actuator-valve` names.

## Class values (ETIM 10.0 EC011197, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF000513 Control signal | pneumatic: air to `port-2` (open) or `port-4` (close) from a 5/2 valve |
| 2 | EF000010 Model | rack and pinion, double-acting |
| 3 | EF020488 Air supply connection | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1), `port-2` and `port-4` on the front face; not a VDI/VDE 3845 (NAMUR) valve face, which is not on file |
| 4 | EF022697 With end contacts | no |
| 5 | EF024109 Auxiliary contacts | no |
| 6 | EF024118 Pressureless opening (NO) | no: double-acting, no spring; without air the shaft stays where it was |
| 7 | EF021869 Spring return | no |
| 8 | EF023901 Adjustable operating range | no (no end-stop screws in 1.0) |
| 9 | EF002978 Suitable for manual operation | no |
| 10 | EF021864 Torque | not stated (a double-acting actuator: value 11) |
| 11 | EF025130 Double-acting torque | 35.1 N·m at 551.6 kPa (80 psig, pneu.P_WORK_MAX): 2 pistons × p × π × 52² / 4 × 15 mm pinion pitch radius (element.py torque_nm; theoretical, no friction or seal drag) |
| 12 | EF025136 Torque single acting start air | not stated (double-acting) |
| 13 | EF025137 Torque single acting end spring | not stated (double-acting) |
| 14 | EF024111 Adjusting force | not stated |
| 15 | EF021866 Stroke length | 23.6 mm: each piston's travel for the quarter turn, 15 × π / 2 (element.py stroke_mm) |
| 16 | EF024112 Self-adjusting travel length | no |
| 17 | EF023860 Max. angle of rotation | 90° (`shaft`, 0 closed to 90 open) |
| 18 | EF025129 Mounting flange connection | ISO 5211 by intent; its flange size, bolt circle, threads and drive are open (Open figures), so the pad is plain |
| 19 | EF025128 Top flange connection | none in 1.0: a plain shaft top with the indicator bar |
| 20 | EF001596 Housing material | aluminium, anodised (body, pad, port bosses); end caps black polyamide |
| 21 | EF005474 Degree of protection (IP) | not stated |
| 22 | EF023900 Allowable relative humidity | not stated |
| 23 | EF002386 Ambient temperature | not stated |
| 24 | EF000040 Height | 99.5 mm (pad underside to the indicator's top) |
| 25 | EF000008 Width | 86 mm (y: the port bosses' faces to the caps' back) |
| 26 | EF000049 Depth | 171 mm (x: cap to cap) |

The torque and stroke are generic design values (OPERATING.md 12), computed from the design's own piston and pinion sizes, not
tested ratings. No class feature states a pressure, so ratings.csv holds no p_max (GEN-010 refuses a "generic design" row with no
class feature behind it); the max. operating pressure is an open figure (Open figures, class A), as vacuum 1.0's.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| mounting pad | Ø66 × 8, z 0 to 8, on the shaft's axis | the place of the ISO 5211 flange (Open figures): no bolt holes and no drive are cut; 2 inside the body's 70 on each side |
| body | 160 (x) × 70 (y) × 70 (z), z 7.5 to 77.5 (0.5 into the pad); anodised aluminium | holds two Ø52 pistons (6 of wall, asserted) with their racks (30 each), the 15 pinion and each piston's 23.6 travel in its half (asserted); none of them modelled |
| end caps | 6 × 74 × 74 on each end, x ±79.5 to ±85.5 (0.5 into the body), centred on the body; black | close the two cylinders; 2 proud of the body all round |
| port bosses | Ø20 × 14 along −y on the front face, at x = −16 (`port-2`) and +16 (`port-4`), z = 42.5 (the body's mid-height) | at least 3 mm of metal round the NPT 1/4 pipe OD (13.7 mm, pneu.NPT); 14 is at least 2 more than a male's effective thread L2 (10.21) and its make-up depth L1 + L3 (10.02), both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each; 32 apart, 12 clear between the bosses |
| port bores | Ø13.616 × 12.205 deep, blind, one in each boss, on the port's axis from its face | Ø = E1 + h of NPT 1/4 from pneu.NPT, the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up L1 + L3 and < the boss's 14; 3.19 mm of boss wall (asserted ≥ 3). Role in features.csv (HOLE-010) |
| shaft top | Ø20 × 16 on the body's top face, seated face to face (it turns), z 77.5 to 93.5; steel | `shaft`: the pinion's upper end |
| indicator bar | 56 × 10 × 6 on the shaft's top, along x when closed, z 93 to 99.5; yellow | shows the valve's position from a distance; turns with the shaft |
| overall | envelope 171 × 86 × 99.5 (x −85.5 to 85.5, y −49 to 37, z 0 to 99.5) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-2` | NPT1/4 | female | work | the left boss's face y = −49, x = −16, z = 42.5, axis −y | air in opens (pistons apart); ISO 11727 number 2 as pneu.NODES work; pneu.py D1 (NPT, ASME B1.20.1) |
| `port-4` | NPT1/4 | female | work | the right boss's face y = −49, x = 16, z = 42.5, axis −y | air in closes (pistons together); ISO 11727 number 4 as pneu.NODES work |

PNE-002 pairs each with a male NPT 1/4 (sealant on the male, D1): fitting-pushin 2.0's stub, or a valve's own. Each face is the joint
plane a placed fitting meets; the bore behind it takes the male's stub.

## Open figures
- NOT ON FILE (A): the actuator's max. operating pressure. EC011197 has no pressure feature, and no standard on file states one for
  a valve actuator, so ratings.csv holds no p_max; PNE-003 REVIEWs the actuator in an assembly until EM gives a figure or a source.
  The torque above is stated at P_WORK_MAX (80 psig), the bench regulator's highest setting.
- NOT ON FILE (B): the mounting flange to ISO 5211 (flange size for 35 N·m, bolt circle, thread, the drive's square or star and its
  depth). ISO 5211 is not in lib/standards/sources.csv, so the pad is plain: no holes, no drive. A host (valve-ball, valve-butterfly)
  can't couple the actuator until it is on file (then a major version, new cut-outs).

## Named nodes
`port-2`, `port-4` (the bosses): kind port, fixed (range 0). `shaft` (the shaft top and its indicator bar): kind rotate about +z on
the shaft's axis through the body's top face, 0 to 90° (closed to open, counter-clockwise seen from above), seated face to face on
the body, so it sweeps only its own cylinder and the bar's circle (r 28.4) above the body's top.

## Materials by layer
`M-ALU-ANOD` mounting pad, body, port bosses · `M-BLACK-PA` end caps · `M-STEEL-7035` shaft top · `M-YELLOW-PA` indicator bar

## Decals (Blender)
None in 1.0 (port numbers 2 and 4, OPEN / SHUT on the body's top, and the "generic" label are a later version). No vendor names.

## Notes
- A common part of valve-ball and valve-butterfly (made_of in lib/inventory.csv): placed, never redrawn, by each, version pinned.
  Neither host can place it until the ISO 5211 flange is on file and the actuator past station 6.
- No safety function: it is not an emergency shut-off on its own (no spring return, inventory `safety` blank). A fail-safe
  (spring-return) actuator would be a variant with its own class values 6, 7, 12 and 13.
- No position switches: a switch box on top (VDI/VDE 3845) would be its own element, and the top interface is none in 1.0.

## Outputs (out/)
`actuator-valve.lsp` · `.glb` (shaft and port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011197), pneu-r65 (unattended): mounting pad, body, two end caps, port bosses `port-2` / `port-4` (female NPT 1/4, bored Ø (E1 + h) × (L2 + 2)), `shaft` with its indicator bar (rotate 0 to 90°); the max. operating pressure (class A) and the ISO 5211 flange (class B) left open, the pistons and pinion not modelled |
