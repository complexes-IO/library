# valve-needle-3way · v1.0 · three-way needle valve, generic, in line, NPT 1/4, gauge port, hand knob, rising spindle

**What** a hand-set needle valve to throttle an air line, with a gauge port: a needle on a rising, rotating spindle closes a seat
between port-1 and port-2; five turns of the knob take it from closed to fully open. The third port, `port-g`, opens into the body
between the seat and port-2, so a gauge (gauge-p) screwed into it reads the throttled pressure the valve is set to. It throttles both
ways (no check valve). It is our own vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements, EM
2026-11-07): the class values it is designed to are listed under Class values. No maker's datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic three-way needle valve (ETIM 10.0 EC010214). What it meets takes its figures
from the pneumatic contract, `toolkit/pneu.py` (D1 threads, D7 names, ROLES, pneu.NPT for the bores); every size the contract and the
standards on file don't fix is a design choice (below).
**Units / frame** mm, Z up. Origin: port-1's end face centre on the port axis, in line: the port axis is the x axis, flow along +x,
the knob toward +z, the gauge port toward +y, the label face toward −y. Ports follow pneu.py's port frame: the pivot on the port's
number field's outer face (0.2 out from its face, where a placed male's hex seats), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-NEEDLE-3WAY` · no parameters.

## Class values
ETIM 10.0 EC010214 "Three-way needle valve" (group EG020069), every feature in ETIM's order (lib/standards/etim/class-features.csv).
These are the values this element is designed to: they define it as a member of the class, and they are design inputs. ETIM's
features for this class are written for piped valves; a feature an air needle valve has no use for is "not stated".

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | brass | body and bonnet |
| 2 | Material quality | not stated | |
| 3 | Surface protection | none | bare brass |
| 4 | Nominal diameter | not stated | threaded ports; no DN is claimed |
| 5 | Outer pipe diameter all connections | not stated | threaded ports, no pipe ends |
| 6 | Connection 1 | female thread NPT 1/4 | port-1 (pneu.py D1) |
| 7 | With coupling connection 1 | no | |
| 8 | Connection 2 | female thread NPT 1/4 | port-2 (pneu.py D1) |
| 9 | With coupling connection 2 | no | |
| 10 | Connection 3 | female thread NPT 1/4 | port-g, the gauge port (pneu.py D1) |
| 11 | With coupling connection 3 | no | |
| 12 | Article compression class | not stated | no PN class is claimed |
| 13 | Flange compression class | not stated | no flanges |
| 14 | Max. operating pressure at 20 °C | 10 bar | |
| 15 | Medium temperature (continuous) | −10 to 60 °C | compressed air |
| 16 | Spindle and/or hand wheel rising | yes | 0.5 per turn, 2.5 over the 5 turns |
| 17 | Operation | hand knob | |
| 18 | Rotating needle | yes | the needle turns with the spindle |
| 19 | Length of connection 1 | 10.2 mm | NPT 1/4's thread length L2 (pneu.NPT, 10.205); the bore is L2 + 2 deep |
| 20 | Working length connection 1 | not stated | ETIM's working length is a piped valve's face-to-centre length; an in-line body threaded at its ends has none of its own |
| 21 | Length of connection 2 | 10.2 mm | as 19 |
| 22 | Working length connection 2 | not stated | as 20 |
| 23 | Length of connection 3 | 10.2 mm | as 19 |
| 24 | Working length connection 3 | not stated | as 20 |
| 25 | Handle/hand wheel height | 16 mm | the knob |
| 26 | Length of handle/diameter of hand wheel | 20 mm | the knob |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 64 (x, along the flow) × 24 (y) × 24 (z), brass, centred on the port axis in y and z | valve-needle 2.0's 24 × 24 section, lengthened from 40 to carry port-g between the seat and port-2 |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind: port-1 and port-2 on the port axis in the end faces, port-g on the +y face at x = 40 | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0, gauge-p), so a placed male meets the bore face to face (tank 2.0's rule); deeper than a male's make-up L1 + L3 (10.02). port-g's bore ends 0.205 past the port axis, 11.795 short of the −y face; its sides are 21.0 from port-1's floor and 5.0 from port-2's (element.py asserts at least 3). Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it | the number (1, 2) or G is a decal; 0.2 proud for GEO-050; each port's pivot on its outer face |
| seat, bonnet | the seat under the bonnet at x = 20; bonnet Ø16 × 12, brass, on the body's top face | valve-needle 2.0's; the bonnet ends at x = 28, before port-g's field (x 31 to 49) |
| spindle | Ø6 × 6 showing between the bonnet and the knob | turns and rises with the knob |
| knob | Ø20 × 16, black polyamide | class values 25 and 26 |
| travel | 5 turns closed to open, counter-clockwise seen from above opens; lead 0.5 per turn | class value 16 |
| label field | 28 × 10, 0.2 proud, centred on the body's label face (−y) | "complexes.org generic" and the flow arrow 1 → 2 |
| height | 58: 24 body + 12 bonnet + 6 spindle + 16 knob, closed | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply (inlet) | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727: 1 inlet); pivot at x = −0.2 (the field's outer face), axis −x |
| `port-2` | NPT1/4 | female | work (outlet) | as above (ISO 11727: 2 outlet); pivot at x = 64.2, axis +x |
| `port-g` | NPT1/4 | female | gauge | pneu.ROLES gauge; pneu.NODES has no gauge number, so named `port-g` as frl 2.0's gauge port; pivot at (40, 12.2, 0), axis +y |

NPT 1/4 is our choice within pneu.THREADS, and gauge-p's own thread, so gauge-p screws into port-g. The ports are female and take
sealant on the male (PNE-002). pneu.NPT holds NPT 1/4's figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07):
E1 + h = 13.616 (the bore), L2 = 10.205 (the bore is L2 + 2 deep), L1 + L3 = 10.02 (a male's make-up). The helix is not modelled:
the bore is the thread drawn plain. A male seated on the field's face reaches L2 − 0.2 = 10.0 past its face, inside the 12.205 bore.

## Open figures
None.

## Ratings (ratings.csv)
p_max 10 bar, status "generic design", source class value 14 (EF023116 Max. operating pressure at 20 °C). 10 bar ≥ P_SUPPLY
(689.5 kPa): PNE-003 passes.

## Named nodes
`port-1`, `port-2`, `port-g` (kind port, fixed; range 0; each the number field with its pivot on the field's outer face) · `knob`
(rotate about +z on the bonnet's top face at x = 20, 0 to 1800°: closed to fully open; the pivot carries `lead` 0.5 mm per turn for
the twin's rise; the spindle is part of the node)

## Materials by layer
`M-BRASS` body, bonnet, spindle · `M-BLACK-PA` knob · `M-WHITE-PA` fields

## Decals (Blender)
port numbers 1 and 2 and the letter G on their fields; the flow arrow 1 → 2 and "complexes.org generic" on the label field; an
open / close arrow on the knob's top. No vendor names, no approval marks.

## Notes
In line: it is carried by its pipework or fittings (fitting-pushin 2.0, or another male NPT 1/4, is placed by the assembly). It has
no mounting holes and no panel nut; either is a later version. The needle and seat inside are not modelled (the twin reads the knob's
angle). port-g is always joined to port-2's side of the seat; with no gauge in it, it takes a plug (pneu.ROLES plug) so PNE's
"every port connected or plugged" holds. No safety function.

## Outputs (out/)
`valve-needle-3way.lsp` · `.glb` (port and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010214), pneu-r96 (unattended, 2026-11-12): valve-needle 2.0's section, bores, fields, bonnet, spindle and knob on a body lengthened to 64, a third female NPT 1/4 port `port-g` (role gauge) on the +y face downstream of the seat; class values 1 to 26; ratings.csv p_max 10 bar (class value 14) |
