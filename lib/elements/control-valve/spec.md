# control-valve · v1.0 · generic pneumatic two-way control valve, normally closed, spring return, NPT 3/8 female body ports, NPT 1/8 control port

**What** the valve that opens and shuts a liquid line on an air signal: a heat-exchanger loop's cooling water, a process skid's
line. A brass in-line globe body carries the inlet `port-in` and the outlet `port-out` on its end faces; a bonnet on its top
carries a single-acting piston actuator. The actuator's spring holds the plug on its seat (normally closed); control air into
`port-12` on the actuator's top lifts it open by the stroke; air off, the spring closes it. The `stem`, a yellow position indicator
on the actuator's top, rises with the plug, so the valve's position reads from a distance. lib/inventory.csv row `control-valve`
(own_design generic, ETIM EC010171; used by heat-exchanger-loop and process-skid). A 3/2 valve (valve-sol-32nc-sr) gives it its air.
**Class** device · **Baseline** our own design: generic pneumatic controlled two-way control valve (ETIM 10.0 EC010171), as
OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or
measured (the reference file in the folder is the core's, kept as reference only). The class values below are its design inputs;
its sizes are design choices; its ports take their thread from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and the
control port its number from ISO 11727. No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the inlet boss's face centre (`port-in`), in line: the port axis is the x axis, flow along +x,
the actuator toward +z, the label face toward −y. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward
the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CONTROL-VALVE` · no parameters (one size).

The class: EC010171 "Pneumatic controlled two-way control valve" (group EG020069 "Flow control valves", 34 features on file;
synonyms "Control valve", "Pneumatic control valve"), the class inventory row `control-valve` names.

## Class values (ETIM 10.0 EC010171, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | brass (body and liquid port bosses); the actuator anodised aluminium |
| 2 | EF001257 Material quality | not stated |
| 3 | EF023191 Nominal diameter | not stated (the ports are NPT 3/8; no DN is assigned) |
| 4 | EF020126 Outer pipe diameter all connections | not stated (threaded ports, no pipe-OD connection) |
| 5 | EF022472 Connections | female thread NPT 3/8 both (ASME B1.20.1; pneu.py D1), in line on the end faces |
| 6 | EF021872 With coupling connection 1 | no |
| 7 | EF021873 With coupling connection 2 | no |
| 8 | EF020007 Article compression class | not stated |
| 9 | EF020149 Flange compression class | not stated (threaded, no flange) |
| 10 | EF024113 Max. pressure difference in opened position | not stated |
| 11 | EF023182 Medium temperature (continuous) | not stated |
| 12 | EF000139 Surface protection | not stated |
| 13 | EF022466 Kvs value | not stated |
| 14 | EF024114 Leakage loss of Kvs value | not stated |
| 15 | EF024116 Characteristic curve | not stated (on/off in 1.0) |
| 16 | EF024115 Control ratio (Svo) | not stated |
| 17 | EF024117 Closing pressure | not stated |
| 18 | EF000513 Control signal | pneumatic on/off: air to `port-12` (female NPT 1/8) opens, the spring closes |
| 19 | EF023901 Adjustable operating range | no |
| 20 | EF024118 Pressureless opening (NO) | no: normally closed, the spring shuts it without air |
| 21 | EF022697 With end contacts | no |
| 22 | EF024109 Auxiliary contacts | no |
| 23 | EF002978 Suitable for manual operation | no |
| 24 | EF005474 Degree of protection (IP) | not stated |
| 25 | EF004663 Explosion-proof | not stated |
| 26 | EF023900 Allowable relative humidity | not stated |
| 27 | EF002386 Ambient temperature | not stated |
| 28 | EF020151 Length of connection 1 | not stated |
| 29 | EF020153 Working length connection 1 | not stated |
| 30 | EF020152 Length of connection 2 | not stated |
| 31 | EF020154 Working length connection 2 | not stated |
| 32 | EF000040 Height | 137.5 mm (body underside to the stem's top, closed; element.py height()) |
| 33 | EF000008 Width | 88 mm (x: port face to port face) |
| 34 | EF000049 Depth | 80 mm (y: the actuator's diameter) |

No class feature states a pressure the checks read, so there is no ratings.csv (GEN-010 refuses a "generic design" row with no
class feature behind it); the pressure ratings are one open figure (Open figures, class A), as actuator-valve 1.0's.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| liquid port bosses | Ø26 × 16 along x, `port-in` x 0 to 16.5 and `port-out` x 71.5 to 88, on the port axis (y = 0, z = 0) | at least 3 mm of metal round the NPT 3/8 pipe OD (17.145 mm, pneu.NPT); 16 is at least 2 more than a male's effective thread L2 (10.36) and its make-up depth L1 + L3, both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each |
| port bores | Ø17.055 × 12.36 deep, blind, one in each liquid boss from its face | Ø = E1 + h of NPT 3/8 from pneu.NPT, the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up and < the boss's 16; 4.47 mm of boss wall (asserted ≥ 3). Role in features.csv (HOLE-010) |
| body | 56 (x) × 40 (y) × 44 (z), x 16 to 72, centred on the port axis; brass | the globe body round the seat and plug (not modelled) |
| bonnet | Ø30 × 24 on the body's top, z 21.5 to 46 (0.5 into the body), on the axis x = 44; steel | carries the actuator and guides the stem (not modelled) |
| actuator | Ø80 × 60, z 45.5 to 105.5 (0.5 into the bonnet), on the axis; anodised aluminium | the piston and its return spring inside (not modelled); its circle stays inside the ports' faces in x (4 to 84) |
| control port boss | Ø18 × 10 on the actuator's top, x = 68 (24 off the axis), z 105 to 115.5 | at least 3 mm of metal round the NPT 1/8 pipe OD (10.287 mm); 10 holds the bore below; 6 clear of the stem (asserted) |
| control port bore | Ø10.242 × 8.702 deep, blind, from the boss's top | E1 + h and L2 + 2 of NPT 1/8 from pneu.NPT, as above; 3.88 mm of boss wall. Role in features.csv |
| stem (indicator) | Ø12 × 10 on the actuator's top, on the axis, z 105.5 to 115.5 closed; yellow; seated face to face | `stem`: rises 10 (the stroke) when the valve opens |
| stroke | 10 mm | the plug's lift, closed to open; the indicator shows it |
| label field | 40 × 14, 0.2 proud, centred on the body's front face (−y) | "complexes.org generic" and the flow arrow in → out |
| overall | envelope 88 × 80 × 137.5 (x 0 to 88, y −40 to 40, z −22 to 115.5) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-in` | NPT3/8 | female | (none: a liquid port) | the inlet boss's face x = 0, axis −x | pneu.py D1 (NPT, ASME B1.20.1); NPT 3/8 as coolant-pump's and chiller's liquid ports, no ISO 11727 number (that numbering is for pneumatic ports) |
| `port-out` | NPT3/8 | female | (none: a liquid port) | the outlet boss's face x = 88, axis +x | as above |
| `port-12` | NPT1/8 | female | pilot | the control boss's top z = 115.5, x = 68, axis +z | ISO 11727 number 12 (the signal that joins 1 to 2); NPT 1/8 the smallest of pneu.THREADS, for a signal line |

PNE-002 pairs each with a male NPT of its size (sealant on the male, D1): fitting-pushin 2.0's stub, or a pipe nipple's.

## Open figures
- NOT ON FILE (A): the pressure ratings: the actuator's max. control air pressure at `port-12` and the body's max. process pressure.
  EC010171's pressure features (10 and 17) are not stated in this design and no standard on file states either for a generic
  valve, so ratings.csv holds no p_max; PNE-003 REVIEWs the control port in an assembly until EM gives a figure or a source.

## Named nodes
`port-in`, `port-out`, `port-12` (the bosses): kind port, fixed (range 0). `stem` (the position indicator): kind translate along +z
from the actuator's top on the valve's axis, 0 to 10 mm (closed to open), seated face to face on the actuator, so it sweeps only its
own cylinder above it.

## Materials by layer
`M-BRASS` body, liquid port bosses · `M-STEEL-7035` bonnet · `M-ALU-ANOD` actuator, control port boss · `M-YELLOW-PA` stem ·
`M-WHITE-PA` label field

## Decals (Blender)
"complexes.org generic" and the flow arrow in → out on the label field; the port number 12 beside the control port is a later
version. No vendor names, no approval marks.

## Notes
- In line: it is carried by its pipework (the heat-exchanger loop's lines); it has no mounting holes, and a bracket would be a
  later element. The fittings on its ports are placed by the assembly that pipes it.
- No safety function: it is a process valve, not an emergency shut-off (inventory `safety` blank). Its fail-closed spring is a
  design choice, not a safety claim.
- On/off in 1.0: a modulating version (a positioner, a 3 to 15 psi signal) would be its own version with class values 13 to 18.

## Outputs (out/)
`control-valve.lsp` · `.glb` (port and stem pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010171), pneu-r67 (unattended): globe body with `port-in` / `port-out` (female NPT 3/8, bored Ø (E1 + h) × (L2 + 2)), bonnet, spring-return actuator with `port-12` (female NPT 1/8, role pilot), `stem` indicator (translate 0 to 10 mm), label field; the pressure ratings (class A) left open; plug, seat, piston and spring not modelled |
