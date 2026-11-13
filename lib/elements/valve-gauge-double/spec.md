# valve-gauge-double · v1.1 · double pressure gauge valve, generic, NPT 1/4 male process to two NPT 1/4 female gauge ports, two hand knobs, rising spindles

**What** a shut-off valve that lets two pressure gauges read one tapping: its process connection (port-1, a male thread underneath)
screws into a female port of the line, one gauge screws into its top (port-2, female) and a second into its right side (port-4,
female). Each gauge has its own knob on the front, so either can be shut off and changed with the line under pressure, or a test gauge
put on port-4 to check the working gauge on port-2 against it. It is our own vendor-neutral design of the ETIM class below
(OPERATING.md 12, generic elements, EM 2026-11-07; the first class `python lib/build.py inventory pneu` lists, request pneu-idle
2026-11-12 from the core): the class values it is designed to are listed under Class values. No maker's datasheet or CAD was opened or
measured.
**Class** device · **Baseline** our own design: generic double pressure gauge valve (ETIM 10.0 EC010471). What it meets takes its
figures from the pneumatic contract, `toolkit/pneu.py` (D1 threads, ROLES, NODES, and the NPT table, values calculated from ASME
B1.20.1's formulas, EM 2026-11-07); every other size is a design choice (below). No tension socket and no inspection flange (class
values 5 and 6), so nothing in its shape waits on a dimensional standard.
**Units / frame** mm, Z up. Origin: in line, upright: the process connection's shoulder centre on the body's underside (x = 0,
y = 0, z = 0); the stub toward −z, port-2 on top (+z), port-4 on the right side (+x), both knobs toward −y. Ports follow pneu.py's
port frame: the pivot on the joint plane (a female port's number field's outer face; a male port's shoulder, where the counterpart's
face stands when it is screwed home), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-GAUGE-DOUBLE` · no parameters.

## Class values
ETIM 10.0 EC010471 "Double pressure gauge valve" (group EG020069), every feature in ETIM's order (lib/standards/etim/class-features.csv).
These are the values this element is designed to: they define it as a member of the class, and they are design inputs.

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | brass | knobs polyamide |
| 2 | Connection size | NPT 1/4 | all three connections; pneu.py D1; drawn plain at E1 + h from pneu.NPT (Its own sizes) |
| 3 | Connection 1 | male thread | port-1, process side, underneath |
| 4 | Connection 2 | female thread | port-2 (top) and port-4 (right side), the two gauge connections, alike |
| 5 | With tension socket, connection 2 | no | plain female threads; each gauge is turned to face the reader on its own thread |
| 6 | With inspection flange | no | port-4 serves a test gauge on a thread instead |
| 7 | Article compression class | not stated | no PN class is claimed (PN designations are not among the standards on file) |
| 8 | Max. operating pressure at 20 °C | 10 bar | ratings.csv `p_max` (status "generic design"): PNE-003 reads it |
| 9 | Medium temperature (continuous) | 0 to 60 °C | filtered compressed air (pneu.py D4) |
| 10 | Operation | two hand knobs | each on a rising spindle, 4 turns closed to open |
| 11 | Length of connection 1 | 10.2 mm | the process stub, L2 of NPT 1/4 (10.205, pneu.NPT) |
| 12 | Working length connection 1 | not stated | the stub is drawn plain; no make-up length is claimed beyond pneu.NPT's |
| 13 | Length of connection 2 | 12.2 mm | each gauge bore's depth, L2 + 2 (12.205) |
| 14 | Working length connection 2 | not stated | as 12 |
| 15 | Height | 70 mm | the body: the process connection's shoulder to the top face |
| 16 | Length of handle/diameter of hand wheel | 24 mm | each knob |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 22 × 22 square, 70 high, brass, centred on the port axis | the flats take a 22 open-end spanner, as valve-gauge's; 70 high so the two knobs stand one above the other on the front face with 6 between them, and port-4's bore stays under port-2's |
| process stub (port-1) | Ø13.616 × 10.205 plain, under the body | the male NPT 1/4 drawn as valve-gauge 3.0, fitting-pushin 2.0 and gauge-p draw theirs: Ø = E1 + h, the external thread's major diameter at the hand-tight plane, length L2, the effective thread, both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07). The 1:16 taper and the thread form are not drawn. The body's 22 flats clear the thread's largest major diameter E2 + h = 13.892 (element.py asserts it) |
| gauge bore port-2 | Ø13.616, 12.205 deep, blind, into the top face | the female NPT 1/4 at the male stub's own diameter (E1 + h), so gauge-p's stub and this bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 (10.02); 4.19 of brass round it (asserted ≥ 3); its floor at z = 57.795. Declared in features.csv (HOLE-010) |
| gauge bore port-4 | Ø13.616, 12.205 deep, blind, into the right side face (+x) at z = 22 | as port-2; its floor at x = −1.205 leaves 9.8 of the left wall; its top (z = 28.808) stays more than 3 under port-2's floor (asserted); 15.19 of brass under it above the stub's shoulder (22 − 6.808; the shoulder is the body's underside, z = 0) |
| port-number fields | 18 × 18, 0.2 proud, one on the top face, one on the right side face, each bore through its field | "2" and "4" are decals; 0.2 proud for GEO-050. Each port's pivot stands on its field's outer face (z = 70.2; x = 11.2), so a placed gauge's seat meets the field face to face (filter-air 3.0's rule) |
| knob axes | knob-2 at z = 50, knob-4 at z = 20, on the front face (−y) | one above the other, 6 between the knobs' rims; the upper knob shuts the upper port (2), the lower knob the side port (4) |
| bonnets | Ø14 × 6, on the front face | as valve-gauge |
| spindles | Ø6 × 6, between each bonnet and its knob; turn and rise with the knob | |
| knobs | Ø24 × 12, black | class value 16 |
| travel | 4 turns closed to fully open; each spindle rises 0.5 per turn | class value 10 |
| label field | 16 × 10, 0.2 proud, on the left side face (−x), centred y = 0, z = 35 | "complexes.org generic" and the flow arrows 1 → 2 and 1 → 4 |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | male | supply (process side, the inlet) | pneu.py D1 (NPT, ASME B1.20.1); ISO 11727's 1 for the inlet. The node is the stub itself |
| `port-2` | NPT1/4 | female | gauge (the first gauge's port, on top) | as above; ISO 11727's 2 for an outlet |
| `port-4` | NPT1/4 | female | gauge (the second gauge's port, right side) | as above; ISO 11727's 4 for the second outlet (pneu.NODES work = port-2, port-4) |

NPT 1/4 is our choice within pneu.THREADS. port-1 is the male of its joint and takes the sealant (PNE-002); port-2 and port-4 are
female and the gauges' males take it.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file (pneu.NPT).

## Named nodes
`port-1` (kind port, fixed; the stub), `port-2` (kind port, fixed; the top field, its pivot on the field's outer face z = 70.2),
`port-4` (kind port, fixed; the right side field, its pivot on the field's outer face x = 11.2) · `knob-2` (rotate about −y at its
bonnet's front face, z = 50, 0 to 1440°, closed to fully open, the spindle rising 0.5 per turn: extras `lead`) · `knob-4` (the same
at z = 20)

## Materials by layer
`M-BRASS` body, stub, bonnets, spindles · `M-BLACK-PA` knobs · `M-WHITE-PA` fields

## Decals (Blender)
"2" and "4" on the port fields; "complexes.org generic" and the flow arrows (1 → 2 upward, 1 → 4 to the right) on the label field. No
vendor names, no approval marks.

## Ratings (ratings.csv)
`p_max` 10 bar, status "generic design", source "ETIM 10.0 EC010471 class value" (class value 8; OPERATING.md 12: ratings the checks
read go in ratings.csv). P_SUPPLY (100 psig, 6.9 bar) is below it.

## Notes
- Carried by the line it reads: it has no mounting holes. Gauges (gauge-p 1.0, 0-160 psig, its male NPT 1/4 stub at E1 + h) are
  placed on port-2 and port-4 by the assembly; p_max 10 bar (145 psig) is under gauge-p's span.
- No vent screw: a gauge is vented by unscrewing it with its knob shut. The internal passages and the seats are not modelled; the
  twin reads the knob angles.
- No safety function.

## Outputs (out/)
`valve-gauge-double.lsp` · `.glb` (port and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, pneu-r91 (unattended), generic (ETIM 10.0 EC010471): square body, process stub, two gauge bores with their fields (top, right side), two bonnets, spindles and knobs on the front, label field on the left; ratings.csv p_max (generic design); behaviour.csv (three pins, two knobs' states and poses) |
| 1.1 | text only, pneu-r100 (unattended; review valve-gauge-double-1.0.md finding 1, pneu/r91.md): Its own sizes, gauge bore port-4: the brass under the bore above the stub's shoulder is 15.19 (Z4 − BORE_D / 2 = 22 − 6.808), not 8.19. No shape, node, origin or cut-out change |
