# control-valve-32-mix · v1.1 · generic pneumatic three-way control valve, mixing, spring return (A shut at rest), NPT 3/8 female body ports, NPT 1/8 control port

**What** the valve that switches a liquid loop between two sources on an air signal: a heat-exchanger loop's cooling water taken
through the exchanger (A) or round it (B), a process skid's line. A brass globe body carries the controlled inlet `port-a` and the
common outlet `port-ab` in line on its end faces and the bypass inlet `port-b` on its underside; a bonnet on its top carries a
single-acting piston actuator. At rest the actuator's spring holds the plug against A's seat: A shut, B open to AB. Control air into
`port-12` on the actuator's top lifts the plug by the stroke onto B's seat: A open to AB, B shut; air off, the spring returns it. The
`stem`, a yellow position indicator on the actuator's top, rises with the plug, so the valve's position reads from a distance. It is
control-valve 1.0's three-way sibling (the same body, bonnet and actuator, one more port). Mixing (two inlets, one outlet) in the
id's function, and "32" for its three ways and two positions as ISO 1219 draws a valve (OPERATING.md 6, the id convention). Our own
vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements, EM 2026-11-07; the next class `python lib/build.py
inventory pneu` lists after EC010401): the class values it is designed to are listed under Class values. A 3/2 valve
(valve-sol-32nc-sr) gives it its control air. No maker's datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic pneumatic controlled three-way control valve (ETIM 10.0 EC010030). What it
meets takes its figures from the pneumatic contract, `toolkit/pneu.py` (D1 threads, D3 P_SUPPLY, ROLES, and the NPT table, values
calculated from ASME B1.20.1's formulas, EM 2026-11-07); its control port takes its number from ISO 11727 as control-valve's; every
other size is a design choice (below). Threaded connections only, no coupling and no flange (class values 5 to 10), so nothing in its
shape waits on a dimensional standard.
**Units / frame** mm, Z up. Origin: the inlet A boss's face centre (`port-a`), in line: the port axis is the x axis, flow along +x to
`port-ab`, the bypass `port-b` toward −z, the actuator toward +z, the label face toward −y. Ports follow pneu.py's port frame: the
pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CONTROL-VALVE-32-MIX` · no parameters (one size).

The class: EC010030 "Pneumatic controlled three-way control valve" (group EG020069 "Flow control valves", 41 features on file).

## Class values (ETIM 10.0 EC010030, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value | note |
|---|---|---|---|
| 1 | EF001596 Housing material | brass (body and liquid port bosses); the actuator anodised aluminium | |
| 2 | EF001257 Material quality | not stated | no alloy designation is claimed |
| 3 | EF023191 Nominal diameter | not stated | the ports are NPT 3/8, an inch thread size; DN designations are not among the standards on file |
| 4 | EF020126 Outer pipe diameter all connections | not stated | threaded ports, no pipe-OD connection |
| 5 | EF022472 Connections | female thread NPT 3/8, all three: A and AB in line on the end faces, B on the underside | pneu.py D1 (ASME B1.20.1) |
| 6 | EF021872 With coupling connection 1 | no | connection 1 = A |
| 7 | EF021873 With coupling connection 2 | no | connection 2 = B |
| 8 | EF020148 With coupling connection 3 | no | connection 3 = AB |
| 9 | EF020007 Article compression class | not stated | no PN class is claimed (PN designations are not among the standards on file) |
| 10 | EF020149 Flange compression class | not stated | threaded, no flange |
| 11 | EF024113 Max. pressure difference in opened position | not stated | no flow figure is claimed |
| 12 | EF023182 Medium temperature (continuous) | not stated | |
| 13 | EF000139 Surface protection | not stated | |
| 14 | EF022466 Kvs value | not stated | |
| 15 | EF024114 Leakage loss of Kvs value | not stated | |
| 16 | EF024116 Characteristic curve | not stated | on/off in 1.0 |
| 17 | EF024128 KVS value for bypass | not stated | |
| 18 | EF024129 Leakage loss of KVS value for bypass | not stated | |
| 19 | EF024130 Characteristic curve for bypass | not stated | on/off in 1.0 |
| 20 | EF024131 Installation method, distributive | no | mixing: A and B in, AB out |
| 21 | EF024115 Control ratio (Svo) | not stated | |
| 22 | EF024117 Closing pressure | 4 bar | the liquid line's pressure each seat shuts against, a design input for the actuator, not a rating of the body; below the actuator's 8 bar (element.py asserts it) |
| 23 | EF000513 Control signal | pneumatic on/off: air to `port-12` (female NPT 1/8) opens A and shuts B, the spring returns it | |
| 24 | EF024118 Pressureless opening (NO) | no | the controlled way A is shut without air (B, the bypass, is open) |
| 25 | EF023901 Adjustable operating range | no | |
| 26 | EF022697 With end contacts | no | |
| 27 | EF024109 Auxiliary contacts | no | |
| 28 | EF002978 Suitable for manual operation | no | |
| 29 | EF005474 Degree of protection (IP) | not stated | |
| 30 | EF004663 Explosion-proof | not stated | |
| 31 | EF023900 Allowable relative humidity | not stated | |
| 32 | EF002386 Ambient temperature | not stated | |
| 33 | EF020151 Length of connection 1 | 12.4 mm | A's bore depth, L2 + 2 (12.36) |
| 34 | EF020153 Working length connection 1 | not stated | the thread is drawn plain; no make-up length is claimed beyond pneu.NPT's |
| 35 | EF020152 Length of connection 2 | 12.4 mm | as 33, B |
| 36 | EF020154 Working length connection 2 | not stated | as 34 |
| 37 | EF020159 Length of connection 3 | 12.4 mm | as 33, AB |
| 38 | EF020160 Working length connection 3 | not stated | as 34 |
| 39 | EF000040 Height | 153.5 mm | `port-b`'s face to the stem's top, at rest (element.py height()) |
| 40 | EF000008 Width | 88 mm | x: port face to port face |
| 41 | EF000049 Depth | 80 mm | y: the actuator's diameter |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| liquid port bosses | Ø26 × 16: `port-a` x 0 to 16.5 and `port-ab` x 71.5 to 88 on the port axis (y = 0, z = 0); `port-b` z −38 to −21.5 under the body on the actuator's axis x = 44; brass | control-valve 1.0's bosses: at least 3 mm of metal round the NPT 3/8 pipe OD (17.145 mm, pneu.NPT); 16 is more than a male's make-up depth L1 + L3 from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each |
| port bores | Ø17.055 × 12.36 deep, blind, one in each liquid boss from its face (B's floor at z −25.64, below the body's underside) | Ø = E1 + h of NPT 3/8 from pneu.NPT, the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up and < the boss's 16; 4.47 mm of boss wall (asserted ≥ 3). Each bore in its own boss (separator-oil-water 1.0's lesson). Role in features.csv (HOLE-010) |
| body | 56 (x) × 40 (y) × 44 (z), x 16 to 72, centred on the port axis; brass | the globe body round the two seats and the plug (not modelled), control-valve 1.0's |
| bonnet | Ø30 × 24 on the body's top, z 21.5 to 46 (0.5 into the body), on the axis x = 44; steel | carries the actuator and guides the stem (not modelled) |
| actuator | Ø80 × 60, z 45.5 to 105.5 (0.5 into the bonnet), on the axis; anodised aluminium | the piston and its return spring inside (not modelled); its circle stays inside the ports' faces in x (4 to 84) |
| control port boss | Ø18 × 10 on the actuator's top, x = 68 (24 off the axis), z 105 to 115.5 | at least 3 mm of metal round the NPT 1/8 pipe OD (10.287 mm); 10 holds the bore below; 6 clear of the stem (asserted) |
| control port bore | Ø10.242 × 8.702 deep, blind, from the boss's top | E1 + h and L2 + 2 of NPT 1/8 from pneu.NPT, as above; 3.88 mm of boss wall. Role in features.csv |
| stem (indicator) | Ø12 × 10 on the actuator's top, on the axis, z 105.5 to 115.5 at rest; yellow; seated face to face | `stem`: rises 10 (the stroke) when A opens |
| stroke | 10 mm | the plug's travel, A's seat to B's seat; the indicator shows it |
| label field | 40 × 14, 0.2 proud, centred on the body's front face (−y) | "complexes.org generic" and the mixing arrows A + B → AB |
| overall | envelope 88 × 80 × 153.5 (x 0 to 88, y −40 to 40, z −38 to 115.5) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-a` | NPT3/8 | female | (none: a liquid port) | the inlet A boss's face x = 0, axis −x | pneu.py D1 (NPT, ASME B1.20.1); NPT 3/8 as control-valve's liquid ports; design: marked by the trade's letters A, B, AB (a liquid port has no ISO 11727 number), A the controlled way |
| `port-b` | NPT3/8 | female | (none: a liquid port) | the bypass boss's face z = −38, x = 44, axis −z | as above; B the bypass way |
| `port-ab` | NPT3/8 | female | (none: a liquid port) | the outlet boss's face x = 88, axis +x | as above; AB the common way |
| `port-12` | NPT1/8 | female | pilot | the control boss's top z = 115.5, x = 68, axis +z | ISO 11727 number 12 as control-valve's (the signal that opens the controlled way); NPT 1/8 the smallest of pneu.THREADS, for a signal line |

PNE-002 pairs each with a male NPT of its size (sealant on the male, D1): fitting-pushin 2.0's stub, or a pipe nipple's.

## Ratings (ratings.csv)
`p_max` 8 bar, status "design", source "design: ..." (OPERATING.md 6, derive before you ask: a design figure a rule bounds): the
rating of the actuator's control air at `port-12` only, set above the bench drop's P_SUPPLY (100 psig, 6.89 bar; pneu.py D3; the rule is
ISO 4414:2010 clause 5, each component rated for the highest pressure that can reach it); element.py asserts 800 kPa > P_SUPPLY. The class
has no maximum-pressure feature (its pressure features are 11 and 22), so the row is not a class value. PNE-003 reads one p_max per
element, so until ratings.csv has a port-scoped row this 8 bar is what it reads for the body ports too; no rule on file bounds the brass
body's own rating, which is open below (review control-valve-32-mix-1.0.md finding 1). Class value 22, the closing pressure 4 bar
(EF024117), is the differential each seat shuts against, a design input for the actuator's spring and air, not a rating of the body.

## Open figures
- NOT ON FILE (A): the body's max. process pressure at `port-a`, `port-b` and `port-ab`. EC010030 has no maximum-pressure feature and no
  standard on file rates a generic brass globe body, so it is left for EM (control-valve 1.0's line, the same body); the 8 bar row
  above is the actuator's.

## Named nodes
`port-a`, `port-b`, `port-ab`, `port-12` (the bosses): kind port, fixed (range 0). `stem` (the position indicator): kind translate
along +z from the actuator's top on the valve's axis, 0 to 10 mm (B open to A open), seated face to face on the actuator, so it
sweeps only its own cylinder above it.

## Materials by layer
`M-BRASS` body, liquid port bosses · `M-STEEL-7035` bonnet · `M-ALU-ANOD` actuator, control port boss · `M-YELLOW-PA` stem ·
`M-WHITE-PA` label field

## Decals (Blender)
"complexes.org generic" and the mixing arrows A + B → AB on the label field; the port letters and the number 12 beside their ports
are a later version. No vendor names, no approval marks.

## Notes
- In line: it is carried by its pipework (the loop's lines); it has no mounting holes, and a bracket would be a later element. The
  fittings on its ports are placed by the assembly that pipes it.
- No safety function: it is a process valve, not an emergency shut-off (no inventory row; the class is a process control valve).
  Its spring return to B is a design choice, not a safety claim.
- On/off in 1.0: a modulating version (a positioner, a 3 to 15 psi signal) would be its own version with class values 14 to 21.
- A diverting sibling (one inlet AB, two outlets) would be its own element with class value 20 "yes".

## Outputs (out/)
`control-valve-32-mix.lsp` · `.glb` (port and stem pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from
the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, pneu-r94 (unattended), generic (ETIM 10.0 EC010030): control-valve 1.0's globe body, bonnet and spring-return actuator with `port-a` / `port-ab` in line and `port-b` on the underside (female NPT 3/8, bored Ø (E1 + h) × (L2 + 2)), `port-12` (female NPT 1/8, role pilot), `stem` indicator (translate 0 to 10 mm), label field; ratings.csv p_max (design); behaviour.csv (four pins, the stem's two states); plug, seats, piston and spring not modelled |
| 1.1 | pneu-r109 (unattended), text only (review control-valve-32-mix-1.0.md finding 1): the p_max 8 bar row is the actuator's control air rating at `port-12` and names its rule (ISO 4414 clause 5 above P_SUPPLY); the body's process pressure is now an open class A line for EM (Open figures), as control-valve 1.0's; Ratings and Class values 22 say the 4 bar closing pressure is a seat's shut-off differential, not a rating. No geometry change |
