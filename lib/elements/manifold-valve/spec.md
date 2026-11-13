# manifold-valve · v2.0 · manifold valve, generic, two-valve block and bleed, NPT 1/4, calibration port, panel mounted

**What** a two-valve instrument manifold: a brass block between a process line and a pressure instrument (a gauge or a pressure
transmitter), with a block valve and a bleed valve. The process line enters underneath (port-1), the instrument screws into the top
(port-2), and the block valve (black knob) opens or shuts the way between them. The bleed valve (red knob) joins the instrument side
to the calibration port on the right end (port-cal): with the block valve shut, it vents the instrument, and a calibrator joined at
port-cal tests the instrument in place. It is our own vendor-neutral design of the ETIM class below (OPERATING.md 12, generic
elements, EM 2026-11-07): the class values it is designed to are listed under Class values. No maker's datasheet or CAD was opened or
measured.
**Class** device · **Baseline** our own design: generic manifold valve (ETIM 10.0 EC010298). What it meets takes its figures from
the pneumatic contract, `toolkit/pneu.py` (D1 threads and the NPT table, ROLES) or from ISO 273 for its mounting holes
(lib/standards/holes.csv); every other size is a design choice (below).
Which manifold: ETIM's EC010298 is the instrument manifold (its features are the number of valves in the block, the process side,
the instrument side, calibration ports and the type of shut-off valve; its synonyms include two-, three- and five-way manifolds). A
multi-station base for solenoid valves is not this class (manifold-pneu is ETIM EC004934, "Distribution block (pneumatics)"). Both
sides are threaded, so no transmitter flange interface comes into it, and nothing in its shape waits on a dimensional standard.
**Units / frame** mm, Z up. Origin: surface mount (lib/README.md): back face on the panel y = 0, the lower mounting hole's centre at
x = 0, z = 0; body toward −y, the knobs on the front face (−y), the process port underneath (−z), the instrument port on top (+z).
Ports follow pneu.py's port frame: the pivot on the port's number field's outer face (0.2 out of the body's face; 2.0), its axis
out of the body toward the counterpart, so a placed male's hex seats on the field.
**Built with** toolkit 1.3 · AutoLISP command `MANIFOLD-VALVE` · no parameters.

## Class values
ETIM 10.0 EC010298 "Manifold valve" (group EG020069), every feature in ETIM's order (lib/standards/etim/class-features.csv). These
are the values this element is designed to: they define it as a member of the class, and they are design inputs.

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | brass | bare; knobs polyamide |
| 2 | Number of valves, valve block | 2 | a block valve and a bleed valve |
| 3 | Nominal diameter process side | not stated | a threaded port; no DN is claimed |
| 4 | Connection, process side | female thread NPT 1/4 | port-1, underneath (pneu.py D1) |
| 5 | Nominal diameter instrument side | not stated | as 3 |
| 6 | Connection, instrument side | female thread NPT 1/4 | port-2, on top; a gauge with an NPT 1/4 male lower mount screws straight in |
| 7 | Outer pipe diameter, instrument end | not stated | a threaded port, no pipe end |
| 8 | With calibration ports | yes | one: port-cal, female thread NPT 1/4, on the right end, behind the bleed valve |
| 9 | Article compression class | not stated | no PN class is claimed (PN designations are not among the standards on file) |
| 10 | Flange compression class | not stated | no flange |
| 11 | Medium temperature (continuous) | −10 to 60 °C | filtered compressed air (pneu.py D4) |
| 12 | Operation | hand knob | each valve: a knob on a rising spindle, 5 turns closed to open |
| 13 | Type of shut-off valve | needle valve | both valves |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 56 (x) × 28 (y) × 44 (z), brass, x from −28 to 28, z from −8 to 36 | room for two valves side by side on the front face and a port on three faces |
| mounting holes | 2 × Ø5.5 through y, at x = 0, z = 0 and 28 | M5 clearance, medium (ISO 273 H13, 5.5 to 5.68; lib/standards/holes.csv), between the two valves. The screw (screw-iso4762, not built yet) is placed in a later version (OPERATING.md 12) |
| mounting-hole position | Ø0.4 to A (back face), B (bottom face), C (left end); features.csv | design choice within the floating-fastener limit H − F = 0.50 (ASME Y14.5); ISO 2768-m alone gives Ø0.57 over 28 mm (GDT-010) |
| port places | port-1 on the bottom face and port-2 on the top face, both at x = −14, y = −14 (one column under and over the block valve); port-cal on the right end face at y = −14, z = 14 (behind the bleed valve) | the process-instrument way runs straight up through the block valve's seat |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, into each face (2.0) | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0, gauge-p 1.0), so a placed male meets the bore face to face (tank 2.0's rule; review manifold-valve-1.0.md finding 1); deeper than a male's make-up (pneu.NPT engagement). port-1's bore runs z −8 to 4.2 and port-2's 23.8 to 36: 19.6 of body between them; 7.2 of wall front and back; port-cal's runs x 28 to 15.8, 1.8 short of the bleed valve's axis; port-1's bore clears the lower mounting hole by 4.4 (x). element.py asserts each. Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it (2.0: 16 → 18, a ring round the wider bore) | the number (1, 2, "CAL") is a decal; 0.2 proud for GEO-050; each port's pivot on its outer face (2.0). port-1's and port-2's fields span x −23 to −5, clear of the top label field (x 2 to 26) and 5 in from the left end |
| valves | block at x = −14, bleed at x = 14, both at z = 14 on the front face | 28 between them: 8 clear between the knobs |
| bonnet | Ø16 × 8, each valve, on the front face | |
| spindle | Ø6 × 6, between the bonnet and the knob; turns and rises with the knob | |
| knob | Ø20 × 16, black (block) and red (bleed) | the colours tell the valves apart; the red one vents |
| travel | 5 turns closed to fully open; the spindle rises 0.5 per turn | class value 12 |
| label field | 24 × 10, 0.2 proud, on the top face, centred x = 14, y = −14 | "complexes.org generic" and the valves' names ("BLOCK", "BLEED") |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply (process side, the inlet) | pneu.py D1 (NPT, ASME B1.20.1); ISO 11727's 1 for the inlet |
| `port-2` | NPT1/4 | female | gauge (instrument side) | as above; ISO 11727's 2 for the outlet |
| `port-cal` | NPT1/4 | female | gauge (calibration and vent) | as above. Named, not numbered: ISO 11727's 3 is an exhaust, and this port takes a calibrator or a test gauge. In an assembly it is joined or plugged (PNE-004); it vents only through the bleed valve |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002).

## Open figures
None. 1.0's one open figure (the NPT 1/4 thread, while pneu.NPT was empty) is closed in 2.0 by pneu.NPT on file: each port is
bored at the male stub's own diameter and depth (Its own sizes), the thread drawn plain.

Not claimed: a pressure rating. The class has no pressure feature (its pressure is the compression class, not stated), and a
generic element states no rating beyond its class values (OPERATING.md 12), so there is no ratings.csv; in an assembly PNE-003
gives REVIEW (rating not on file) until a version states one.

## Named nodes
`port-1`, `port-2`, `port-cal` (kind port, fixed; range 0) · `knob-block`, `knob-bleed` (rotate about −y at the bonnet's front face,
0 to 1800°, closed to fully open, the spindle rising 0.5 per turn: extras `lead`)

## Materials by layer
`M-BRASS` body, bonnets, spindles · `M-BLACK-PA` block knob · `M-RED-PA` bleed knob · `M-WHITE-PA` fields

## Decals (Blender)
"1", "2" and "CAL" on the port fields; "complexes.org generic", "BLOCK" over the black knob's side and "BLEED" over the red one's on
the label field, with the ISO 1219-1 symbol of two shut-off valves. No vendor names, no approval marks.

## Notes
- Panel mounted by two M5 screws through the body, between the knobs, as valve-sol-52-sr and valve-sol-32nc-sr are mounted by M4.
- The internal passages and the needle seats are not modelled; the twin reads the knob angles.
- Fully open (5 turns) each knob stands 2.5 beyond the at-rest envelope (y −60.5 against the collider's −58; review
  manifold-valve-1.0.md note 1): a panel layout that goes by the envelope leaves that much more in front.
- No safety function: the bleed valve vents an instrument for testing; isolating a circuit for work is PNE-008's dump valve.

## Outputs (out/)
`manifold-valve.lsp` · `.glb` (port and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010298), cloud-pneu r3 2026-11-07 (the core chat's cloud builder, the PC being down): body, mounting holes, three port bores and fields, block and bleed valves (bonnet, spindle, knob), label field; stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r77 (unattended; review manifold-valve-1.0.md finding 1): each port's bore Ø11.5 × 12 → Ø13.616 (E1 + h) × 12.205 (L2 + 2) from pneu.NPT, its role in features.csv; port-number fields 16 → 18; each port pivot on its field's outer face (filter-air 3.0's fix); the thread line closed (pneu.NPT on file); the knobs' open reach in Notes (note 1); nodes unchanged; no ratings.csv (the class states no pressure) |
