# valve-pinch-22no · v1.1 · pneumatic hose (pinch) valve, generic, 2/2 normally open, NPT 3/8 female process ports, NPT 1/8 control port

**What** the valve that shuts a line of slurry, powder or abrasive grit on an air signal (a blast cabinet's feed, a process skid's
line), where a seat and plug would wear. An elastomer sleeve runs straight through a closed housing from the inlet `port-in` to the
outlet `port-out`, so the medium touches nothing but the sleeve. Control air let into the housing through `port-10` on its top
squeezes the sleeve flat and shuts the line; air off, the sleeve's own stiffness and the medium open it again: a 2/2 valve open at
rest in ISO 1219's terms, hence the id's "22no" (OPERATING.md 6, the id convention; the form "pinch" is the class's synonym). It is
our own vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements, EM 2026-11-07; the next class `python
lib/build.py inventory pneu` lists after EC010102): the class values it is designed to are listed under Class values. A 3/2 valve
(valve-sol-32nc-sr) gives it its control air. No maker's datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic hose valve (ETIM 10.0 EC010401). What it meets takes its figures from the
pneumatic contract, `toolkit/pneu.py` (D1 threads, ROLES, P_SUPPLY, and the NPT table, values calculated from ASME B1.20.1's
formulas, EM 2026-11-07); its control port takes its number from ISO 11727; every other size is a design choice (below). Threaded
connections only, no coupling and no flange (class values 5, 6 and 9), so nothing in its shape waits on a dimensional standard.
**Units / frame** mm, Z up. Origin: the inlet boss's face centre (`port-in`), in line: the port axis is the x axis, flow along +x,
the control port toward +z, the label face toward −y. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis
toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-PINCH-22NO` · no parameters (one size).

The class: EC010401 "Hose valve" (group EG020069 "Flow control valves", 19 features on file; synonyms "Pinch valve", "Pneumatic
hose valve", "Valve cuff").

## Class values (ETIM 10.0 EC010401, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value | note |
|---|---|---|---|
| 1 | EF001596 Housing material | anodised aluminium; the process port bosses brass | |
| 2 | EF001257 Material quality | not stated | no alloy designation is claimed |
| 3 | EF023191 Nominal diameter | not stated | the ports are NPT 3/8, an inch thread size; DN designations are not among the standards on file |
| 4 | EF020126 Outer pipe diameter all connections | not stated | threaded ports, no pipe-OD connection |
| 5 | EF000443 Connection | female thread NPT 3/8, both process ports, in line on the end faces | pneu.py D1 (ASME B1.20.1) |
| 6 | EF022615 With coupling | no | |
| 7 | EF021874 Material hose/sleeve | elastomer | the sleeve is inside and not modelled; no compound is claimed |
| 8 | EF020007 Article compression class | not stated | no PN class is claimed (PN designations are not among the standards on file) |
| 9 | EF020149 Flange compression class | not stated | no flange |
| 10 | EF002147 Operation | pneumatic, normally open | control air at `port-10` shuts; no air, open |
| 11 | EF020449 Max. operating pressure | 4 bar | the process line's pressure it shuts against; control air at least 2.5 bar above the line flattens the sleeve (design choice), and 4 + 2.5 = 6.5 bar is within the bench drop's P_SUPPLY (6.89 bar, 100 psig; pneu.py D3): element.py asserts it |
| 12 | EF020305 Max. control pressure | 8 bar | in ratings.csv as p_max, status "generic design": the rating of the control chamber and so of `port-10` only; 800 kPa is above P_SUPPLY (689.5 kPa), so control air from the bench drop is within it (element.py asserts it). The process ports' rating is class value 11's 4 bar, which no check reads yet (Ratings below) |
| 13 | EF020023 Max. medium temperature (continuous) | 60 °C | the elastomer sleeve's limit by design |
| 14 | EF020151 Length of connection 1 | 12.4 mm | the inlet bore's depth, L2 + 2 (12.36) |
| 15 | EF020153 Working length connection 1 | not stated | the thread is drawn plain; no make-up length is claimed beyond pneu.NPT's |
| 16 | EF020152 Length of connection 2 | 12.4 mm | as 14, the outlet |
| 17 | EF020154 Working length connection 2 | not stated | as 15 |
| 18 | EF000040 Height | 66 mm | the housing's underside to the control boss's top (element.py height()) |
| 19 | EF020156 Length of handle/diameter of hand wheel | not stated | no handle: pneumatic operation |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| process port bosses | Ø26 × 16 along x, `port-in` x 0 to 16.5 and `port-out` x 95.5 to 112, on the port axis (y = 0, z = 0); brass | control-valve 1.0's bosses: at least 3 mm of metal round the NPT 3/8 pipe OD (17.145 mm, pneu.NPT); 16 is more than a male's make-up depth L1 + L3 from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each |
| port bores | Ø17.055 × 12.36 deep, blind, one in each process boss from its face | Ø = E1 + h of NPT 3/8 from pneu.NPT, the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up and < the boss's 16; 4.47 mm of boss wall (asserted ≥ 3). Role in features.csv (HOLE-010) |
| housing | 80 (x) × 56 (y) × 56 (z), x 16 to 96, centred on the port axis; anodised aluminium | the closed chamber round the sleeve (not modelled); square so the label field sits on a flat face |
| control port boss | Ø18 × 10 on the housing's top, on its centre x = 56, z 27.5 to 38 (0.5 into the housing) | at least 3 mm of metal round the NPT 1/8 pipe OD (10.287 mm); the bore stays in the boss, above the housing's top |
| control port bore | Ø10.242 × 8.702 deep, blind, from the boss's top (floor at z 29.3) | E1 + h and L2 + 2 of NPT 1/8 from pneu.NPT, as above; 3.88 mm of boss wall. Role in features.csv |
| label field | 40 × 20, 0.2 proud, centred on the housing's front face (−y) | "complexes.org generic", the 2/2 symbol and the flow arrow in → out |
| overall | envelope 112 × 56.2 × 66 (x 0 to 112, y −28.2 to 28, z −28 to 38) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-in` | NPT3/8 | female | (none: a process port) | the inlet boss's face x = 0, axis −x | pneu.py D1 (NPT, ASME B1.20.1); as control-valve's liquid ports, no ISO 11727 number (that numbering is for the air ports) |
| `port-out` | NPT3/8 | female | (none: a process port) | the outlet boss's face x = 112, axis +x | as above |
| `port-10` | NPT1/8 | female | pilot | the control boss's top z = 38, x = 56, axis +z | ISO 11727 number 10 (the signal that shuts 1 from 2: a normally open valve's pilot); NPT 1/8 the smallest of pneu.THREADS, for a signal line |

PNE-002 pairs each with a male NPT of its size (sealant on the male, D1): fitting-pushin 2.0's stub, or a pipe nipple's.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file (pneu.NPT).

## Named nodes
`port-in`, `port-out`, `port-10` (the bosses): kind port, fixed (range 0). Nothing moves outside: the sleeve flattens inside the
housing and is not modelled; the twin reads its state from behaviour.csv (open by default, shut on control air).

## Materials by layer
`M-ALU-ANOD` housing, control port boss · `M-BRASS` process port bosses · `M-WHITE-PA` label field

## Decals (Blender)
"complexes.org generic", the 2/2 symbol (ISO 1219-1, drawn as a decal) and the flow arrow in → out on the label field; the port
number 10 beside the control port is a later version. No vendor names, no approval marks.

## Ratings (ratings.csv)
`p_max` 8 bar, status "generic design", source "ETIM 10.0 EC010401 class value" (class value 12, EF020305; OPERATING.md 12: ratings
the checks read go in ratings.csv). It guards `port-10`, the control port, only: P_SUPPLY (100 psig, 6.89 bar) is below it. The
process side (`port-in`, `port-out`) is rated 4 bar by class value 11 (EF020449), and no check reads that figure yet: PNE-003 reads one
p_max per element (toolkit/v_pneu.py), so it cannot tell a process line above 4 bar from control air (ISO 4414:2010 clause 5 wants each
component rated for the highest pressure that can reach it). The 4 bar goes in as port-in / port-out rows once ratings.csv has a
port-scoped rating (review valve-pinch-22no-1.0.md finding 1, the core's half); until then a line feeding the process ports above 4 bar is
the assembly's to keep out.

## Notes
- In line: it is carried by its pipework or fittings (placed by the assembly that pipes it); it has no mounting holes, and a
  bracket would be a later element.
- No safety function: it is a process valve, not an emergency shut-off. It is open at rest, so it does not shut on loss of air.
- On/off only: the sleeve's travel is not read as a position, and no flow figure is claimed.

## Outputs (out/)
`valve-pinch-22no.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, pneu-r93 (unattended), generic (ETIM 10.0 EC010401): square housing, `port-in` / `port-out` (female NPT 3/8, bored Ø (E1 + h) × (L2 + 2)) in brass bosses on its end faces, `port-10` (female NPT 1/8, role pilot) on its top, label field; ratings.csv p_max (generic design); behaviour.csv (three pins, the sleeve's two states); the sleeve not modelled |
| 1.1 | pneu-r109 (unattended), text only (review valve-pinch-22no-1.0.md finding 1): Class values 12, Ratings and the ratings.csv source say the 8 bar p_max guards `port-10` only and that the process side's 4 bar (class value 11) is read by no check until a port-scoped rating exists; the "PNE-003 passes it on a bench line" claim for the whole element dropped. No geometry change |
