# valve-needle · v2.0 · needle valve, generic, in line, NPT 1/4, hand knob, rising spindle

**What** a hand-set needle valve to throttle an air line: a needle on a rising, rotating spindle closes a seat between port-1 and
port-2; five turns of the knob take it from closed to fully open. It throttles both ways (no check valve; a flow control with a
check is the flow-control-inline row). It is our own vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements,
EM 2026-11-07): the class values it is designed to are listed under Class values. No maker's datasheet or CAD was opened or
measured.
**Class** device · **Baseline** our own design: generic needle valve (ETIM 10.0 EC010238). What it meets takes its figures from
the pneumatic contract, `toolkit/pneu.py` (D1 threads, D7 names, pneu.NPT for the bores); every size the contract and the
standards on file don't fix is a design choice (below).
**Units / frame** mm, Z up. Origin: port-1's end face centre on the port axis, in line: the port axis is the x axis, flow along +x,
the knob toward +z, the label face toward −y. Ports follow pneu.py's port frame: the pivot on the port's number field's outer face
(2.0: 0.2 out from the end face, where a placed male's hex seats), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-NEEDLE` · no parameters.

## Class values
ETIM 10.0 EC010238 "Needle valve" (group EG020069), every feature in ETIM's order (lib/standards/etim/class-features.csv). These
are the values this element is designed to: they define it as a member of the class, and they are design inputs. ETIM's features
for this class are written for piped valves; a feature an air needle valve has no use for is "not stated".

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | brass | body and bonnet |
| 2 | Material quality | not stated | |
| 3 | Surface protection | none | bare brass |
| 4 | Nominal diameter | not stated | threaded ports; no DN is claimed |
| 5 | Outer pipe diameter all connections | not stated | threaded ports, no pipe ends |
| 6 | Connection 1 | female thread NPT 1/4 | port-1 (pneu.py D1) |
| 7 | Connection 2 | female thread NPT 1/4 | port-2 (pneu.py D1) |
| 8 | Article compression class | not stated | no PN class is claimed |
| 9 | Flange compression class | not stated | no flanges |
| 10 | Max. pressure difference at 20 °C | 10 bar | |
| 11 | Medium temperature (continuous) | −10 to 60 °C | compressed air |
| 12 | Operation | hand knob | |
| 13 | Right-angled model | no | in line: both ports on the x axis |
| 14 | Rotating needle | yes | the needle turns with the spindle |
| 15 | Spindle and/or hand wheel rising | yes | 0.5 per turn, 2.5 over the 5 turns |
| 16 | Zeta value | not stated | |
| 17 | Length of connection 1 | 10.2 mm | NPT 1/4's thread length L2 (pneu.NPT, 10.205); the bore is L2 + 2 deep |
| 18 | Working length connection 1 | not stated | ETIM's working length is a piped valve's face-to-centre length; an in-line body threaded at both ends has none of its own |
| 19 | Length of connection 2 | 10.2 mm | as 17 |
| 20 | Working length connection 2 | not stated | as 18 |
| 21 | Handle/hand wheel height | 16 mm | the knob |
| 22 | Length of handle/diameter of hand wheel | 20 mm | the knob |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 40 (x, along the flow) × 24 (y) × 24 (z), brass, centred on the port axis in y and z | carries both ports on its end faces, 5.19 wall around each bore (2.0) |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, on the port axis, one in each end face (2.0) | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0, gauge-p), so a placed male meets the bore face to face (tank 2.0's rule; review valve-needle-1.0.md finding 1); deeper than a male's make-up L1 + L3 (10.02); 15.59 of body between the two floors, 5.19 of wall round each (element.py asserts at least 10 and 5). Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it (2.0: 16 → 18, a ring round the wider bore) | the ISO 11727 number is a decal; 0.2 proud for GEO-050; each port's pivot on its outer face (2.0) |
| bonnet | Ø16 × 12, brass, on the body's top face at mid-length (x = 20) | holds the spindle |
| spindle | Ø6 × 6 showing between the bonnet and the knob | turns and rises with the knob |
| knob | Ø20 × 16, black polyamide | class values 21 and 22 |
| travel | 5 turns closed to open, counter-clockwise seen from above opens; lead 0.5 per turn | class value 15 |
| label field | 28 × 10, 0.2 proud, centred on the body's label face (−y) | "complexes.org generic" and the flow arrow 1 → 2 |
| height | 58: 24 body + 12 bonnet + 6 spindle + 16 knob, closed | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply (inlet) | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727: 1 inlet); pivot at x = −0.2 (the field's outer face), axis −x |
| `port-2` | NPT1/4 | female | work (outlet) | as above (ISO 11727: 2 outlet); it throttles both ways; pivot at x = 40.2, axis +x |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002). pneu.NPT holds NPT 1/4's
figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 13.616 (the bore), L2 = 10.205 (the bore is
L2 + 2 deep), L1 + L3 = 10.02 (a male's make-up). The helix is not modelled: the bore is the thread drawn plain. A male seated on
the field's face reaches L2 − 0.2 = 10.0 past the end face, inside the 12.205 bore.

## Open figures
None. 1.0's one open figure (the NPT 1/4 thread, while pneu.NPT was empty) is closed in 2.0 by pneu.NPT on file.

## Ratings (ratings.csv)
p_max 10 bar, status "generic design", source class value 10 (EF020150 Max. pressure difference at 20 °C), as review
valve-needle-1.0.md finding 2 asks: the feature is a pressure difference, not a body rating; with port-2 vented and the needle shut
the inlet carries the whole difference, so the lane reads it as the valve's p_max. 10 bar ≥ P_SUPPLY (689.5 kPa): PNE-003 passes.

## Named nodes
`port-1`, `port-2` (kind port, fixed; range 0; each the number field with its pivot on the field's outer face) · `knob` (rotate about +z on the bonnet's top face, 0 to 1800°: closed to fully
open; the pivot carries `lead` 0.5 mm per turn for the twin's rise; the spindle is part of the node)

## Materials by layer
`M-BRASS` body, bonnet, spindle · `M-BLACK-PA` knob · `M-WHITE-PA` fields

## Decals (Blender)
port numbers 1 and 2 on their fields (ISO 11727); the flow arrow 1 → 2 and "complexes.org generic" on the label field; an
open / close arrow on the knob's top. No vendor names, no approval marks.

## Notes
In line: it is carried by its pipework or fittings (fitting-pushin 2.0, or another male NPT 1/4, is placed by the assembly). It has no mounting
holes and no panel nut; either is a later version. The needle and seat inside are not modelled (the twin reads the knob's angle).

## Outputs (out/)
`valve-needle.lsp` · `.glb` (port and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010238), cloud-pneu 2026-11-07 (the core chat's cloud builder, the PC being down): body, bores, fields, bonnet, spindle and knob; stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r74 (unattended; review valve-needle-1.0.md findings 1 and 2): each port's bore Ø11.5 × 12 → Ø13.616 (E1 + h) × 12.205 (L2 + 2) from pneu.NPT, its role in features.csv; port-number fields 16 → 18; each port pivot on its field's outer face (x −0.2 and 40.2; filter-air 3.0's fix); the thread line closed (pneu.NPT on file); class values 17 and 19 the thread length L2, 18 and 20 with their own reason; ratings.csv p_max 10 bar (class value 10); nodes unchanged |
