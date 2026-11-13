# valve-gauge · v3.0 · pressure gauge valve, generic, straight, NPT 1/4 male to NPT 1/4 female, hand knob, rising spindle

**What** a shut-off valve that stands between a pressure gauge and the line it reads: its process connection (port-1, a male thread
underneath) screws into a female port of the line, and the gauge screws into its top (port-2, female). The knob on the front shuts
the gauge off, so the gauge can be changed with the line under pressure, or damped by throttling. It is our own vendor-neutral design
of the ETIM class below (OPERATING.md 12, generic elements, EM 2026-11-07): the class values it is designed to are listed under Class
values. No maker's datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic pressure gauge valve (ETIM 10.0 EC010262). What it meets takes its figures
from the pneumatic contract, `toolkit/pneu.py` (D1 threads, ROLES, and the NPT table, values calculated from ASME B1.20.1's
formulas, EM 2026-11-07); every other size is a design choice (below). Not to DIN 16270 or DIN 16271 (neither is on file: class values 27 and 28), with no test connection and no tension
socket, so nothing in its shape waits on a dimensional standard.
**Units / frame** mm, Z up. Origin: in line, upright: the process connection's shoulder centre on the body's underside (x = 0,
y = 0, z = 0); the stub toward −z, the gauge port on top (+z), the knob toward −y. Ports follow pneu.py's port frame: the pivot on the
joint plane (a female port's face, which on port-2 is its number field's outer face from 3.0; a male port's shoulder, where the
counterpart's face stands when it is screwed home), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-GAUGE` · no parameters.

## Class values
ETIM 10.0 EC010262 "Pressure gauge valve" (group EG020069), every feature in ETIM's order (lib/standards/etim/class-features.csv).
These are the values this element is designed to: they define it as a member of the class, and they are design inputs.

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | brass | knob polyamide |
| 2 | Housing material quality | not stated | no alloy designation is claimed |
| 3 | Surface protection | none | bare brass |
| 4 | Connection 1 | male thread | port-1, process side, underneath |
| 5 | Connection 2 | female thread | port-2, gauge side, on top |
| 6 | Connection size 1 | NPT 1/4 | pneu.py D1; drawn plain at E1 + h from pneu.NPT (Its own sizes) |
| 7 | With gland nut and soldering pipe, connection 1 | no | |
| 8 | Connection size 2 | NPT 1/4 | pneu.py D1; a gauge with an NPT 1/4 male lower mount screws straight in |
| 9 | With tension socket, connection 2 | no | a plain female thread; the gauge is turned to face the reader on its own thread |
| 10 | With test connection | no | |
| 11 | Type of test connection | not stated | none (10) |
| 12 | Size of test spigot | not stated | none (10) |
| 13 | Article compression class | not stated | no PN class is claimed (PN designations are not among the standards on file) |
| 14 | Flange compression class | not stated | no flange |
| 15 | Max. operating pressure at 20 °C | 10 bar | ratings.csv `p_max` (status "generic design"): PNE-003 reads it |
| 16 | Max. medium temperature (continuous) | 60 °C | filtered compressed air (pneu.py D4) |
| 17 | Max. operating pressure at max. medium temperature | 10 bar | no derating up to 60 °C, a design input |
| 18 | Operation | hand knob | a knob on a rising spindle, 4 turns closed to open |
| 19 | Length of connection 1 | 10.2 mm | the process stub, L2 of NPT 1/4 (10.205, pneu.NPT) |
| 20 | Working length connection 1 | not stated | the stub is drawn plain; no make-up length is claimed beyond pneu.NPT's |
| 21 | Length of connection 2 | 12.2 mm | the gauge bore's depth, L2 + 2 (12.205) |
| 22 | Working length connection 2 | not stated | as 20 |
| 23 | Height | 40 mm | the body: the process connection's shoulder to the top face |
| 24 | Length of handle/diameter of hand wheel | 24 mm | the knob |
| 25 | Construction length | 50.2 mm | the process stub's end to the gauge port's face: 10.205 + 40 |
| 26 | Wrench width | 22 mm | across the square body's flats (both pairs) |
| 27 | According to DIN 16270 | no | our own design; the standard is not on file |
| 28 | According to DIN 16271 | no | as 27 |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 22 × 22 square, 40 high, brass, centred on the port axis | the flats take a 22 open-end spanner (class value 26); the knob stands on one flat |
| process stub (port-1) | Ø13.616 × 10.205 plain, under the body (2.0) | the male NPT 1/4 drawn as fitting-pushin 2.0 and gauge-p draw theirs: Ø = E1 + h, the external thread's major diameter at the hand-tight plane, length L2, the effective thread, both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07). The 1:16 taper and the thread form are not drawn. It meets a female NPT 1/4 bored at E1 + h (tank 2.0, gas-regulator 2.0) face to face. The body's 22 flats clear the thread's largest major diameter E2 + h = 13.892 (element.py asserts it) |
| gauge bore (port-2) | Ø13.616, 12.205 deep, blind, into the top face (2.0) | the female NPT 1/4 at the male stub's own diameter (E1 + h), so gauge-p's stub and this bore touch and never overlap (tank 2.0's rule, review pneu-r48 finding 1); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 (10.02) and < the body's 40; 4.19 of brass round it (asserted ≥ 3); its floor (z = 27.795) stays above the bonnet's top (z = 25). Declared in features.csv (HOLE-010) |
| port-number field | 18 × 18, 0.2 proud, on the top face, the bore through it (2.0: 16 → 18, a ring round the wider bore) | "2" is a decal; 0.2 proud for GEO-050. From 3.0 port-2's pivot stands on the field's outer face (z = 40.2), so a placed gauge's seat meets the field face to face and does not sit 0.2 into it (review valve-gauge-2.0.md finding 1; filter-air 3.0's fix); the gauge's stub then reaches z = 40.2 − 10.205 = 29.995, still above the bore's floor (27.795) |
| knob axis | z = 18 on the front face (−y) | the bonnet's top (z = 25) below the gauge bore's floor (z = 27.795), clear of the gauge above |
| bonnet | Ø14 × 6, on the front face | |
| spindle | Ø6 × 6, between the bonnet and the knob; turns and rises with the knob | |
| knob | Ø24 × 12, black | class value 24 |
| travel | 4 turns closed to fully open; the spindle rises 0.5 per turn | class value 18 |
| label field | 16 × 10, 0.2 proud, on the right side face (+x), centred y = 0, z = 20 | "complexes.org generic" and the flow arrow 1 → 2 (upward) |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | male | supply (process side, the inlet) | pneu.py D1 (NPT, ASME B1.20.1); ISO 11727's 1 for the inlet. The node is the stub itself |
| `port-2` | NPT1/4 | female | gauge (the gauge's port) | as above; ISO 11727's 2 for the outlet |

NPT 1/4 is our choice within pneu.THREADS. port-1 is the male of its joint and takes the sealant (PNE-002); port-2 is female and the
gauge's male takes it. 2.0 draws both at E1 + h from pneu.NPT (Its own sizes): the 1.0 stand-ins (a Ø11 stub, a Ø11.5 bore) are
gone, so 1.0's one open figure (the thread, class B) closed with pneu.NPT on file. A changed stub and bore are a change of
cut-outs, so this is a major version (OPERATING.md 7). The lane's other cloud-built elements still have Ø11.5 bores (lib/rounds/pneu/next.md
takes them one a round); a male stub of 2.0's Ø13.616 would overlap them, so this valve's stub goes into a 2.0-bored port only.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file (pneu.NPT).

## Named nodes
`port-1` (kind port, fixed; the stub), `port-2` (kind port, fixed; the field, its pivot on the field's outer face z = 40.2) · `knob` (rotate about −y at the bonnet's front face,
0 to 1440°, closed to fully open, the spindle rising 0.5 per turn: extras `lead`)

## Materials by layer
`M-BRASS` body, stub, bonnet, spindle · `M-BLACK-PA` knob · `M-WHITE-PA` fields

## Decals (Blender)
"2" on the port field; "complexes.org generic" and an upward flow arrow (1 → 2) on the label field. No vendor names, no approval
marks.

## Ratings (ratings.csv)
`p_max` 10 bar, status "generic design", source "ETIM 10.0 EC010262 class value" (class value 15; OPERATING.md 12 as the core
answered on 2026-11-07: ratings the checks read go in ratings.csv). P_SUPPLY (100 psig, 6.9 bar) is below it.

## Notes
- Carried by the line it reads: it has no mounting holes. A gauge (gauge-p 1.0, 0-160 psig, its male NPT 1/4 stub at E1 + h) is
  placed on port-2 by the assembly; p_max 10 bar (145 psig) is under gauge-p's span.
- No vent screw: the gauge is vented by unscrewing it with the valve shut. The internal passage and the seat are not modelled; the
  twin reads the knob angle.
- No safety function.

## Outputs (out/)
`valve-gauge.lsp` · `.glb` (port and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010262), cloud-pneu r3 2026-11-07 (the core chat's cloud builder, the PC being down): square body, process stub, gauge bore and field, bonnet, spindle, knob, label field; ratings.csv p_max (generic design); stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r57 (unattended): process stub Ø13.616 × 10.205 (E1 + h, L2 of NPT 1/4 from pneu.NPT) and gauge bore Ø13.616 × 12.205 (L2 + 2), blind, role in features.csv; port field 16 → 18; the thread line closed (pneu.NPT on file); nodes and origin unchanged |
| 3.0 | pneu-r71 (unattended): review valve-gauge-2.0.md finding 1 (pneu-r58 finding 1, filter-air 3.0's fix): port-2's pivot moved 0.2 up, from the body's top face (z = 40) to its number field's outer face (z = 40.2), so a placed male's seat meets the field face to face; nodes, origin, stub, bore and envelope unchanged |
