# regulator · v1.1 · generic compressed air pressure regulator, relieving, female NPT ports

**What** an inline compressed air pressure regulator for a bench air line (a pneumatic trainer, a pneumatic test bench) and, in
heat-exchanger-loop and process-skid, for the control air of control-valve's actuator (its `port-12`), never for the loop's
liquid: this regulator is air only (class values 27 and 29), and a liquid regulator would be another element. Air
from the supply enters `port-1` on the inlet boss at the left, a relieving diaphragm regulator in the body reduces it to the
pressure set with the adjusting `knob` on the bonnet, and leaves through `port-2` on the right. `port-g` on the body's front face,
downstream of the seat, takes gauge-p (0 to 160 psig), which reads the set pressure.
lib/inventory.csv row `regulator` (own_design generic, ETIM EC010122, "air pressure regulator, relieving (in heat-exchanger-loop
and process-skid: the control-valve actuator's air ...)"; heat-exchanger-loop, pneumatic-trainer, process-skid,
test-bench-pneumatic; lib/requests/core/pneu-7-answer.md item 2).
**Class** device · **Baseline** our own design: generic pressure reducing valve (ETIM 10.0 EC010122, synonym "Compressed air
regulator"), as OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file
was opened or measured. The class values below are its design inputs; its sizes are design choices; its ports take their thread
from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and inlet and outlet their numbers from ISO 11727 (pneu.NODES).
No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of `port-1`'s joint plane on the inlet boss's left face (where the supply fitting
meets it); the air flows in along +x. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward the
counterpart.
**Built with** toolkit 1.3 · AutoLISP command `REGULATOR` · no parameters.

The class: EC010122 "Pressure reducing valve" (tier 2, group EG015810, 33 features on file), the class lib/standards/etim/classes.csv
maps inventory row `regulator` to; "Compressed air regulator" is one of its synonyms. gas-regulator 2.1 is the same class for a
shielding gas cylinder (300 bar, preset, with a flowmeter); this element is the air line's regulator (10 bar, adjustable), so the
two share no parts.

## Class values (ETIM 10.0 EC010122, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | aluminium, anodised (body, bosses and bonnet); the knob black polyamide |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000139 Surface protection | anodised |
| 4 | EF023193 Nominal diameter connection 1 | 1/4 (NPT, ASME B1.20.1) |
| 5 | EF020122 Outer pipe diameter connection 1 | 13.7 mm (NPT 1/4 pipe OD D = 0.540 in, pneu.NPT) |
| 6 | EF000321 Connection 1 | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1) on the inlet boss's left face, `port-1` |
| 7 | EF013560 Contour code connection 1 | not stated |
| 8 | EF021872 With coupling connection 1 | no: a fitting is placed in `port-1` |
| 9 | EF020151 Length of connection 1 | not stated |
| 10 | EF020153 Working length connection 1 | not stated |
| 11 | EF020052 Nominal diameter connection 2 | 1/4 (NPT, ASME B1.20.1) |
| 12 | EF020123 Outer pipe diameter connection 2 | 13.7 mm (as connection 1) |
| 13 | EF000322 Connection 2 | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1) on the outlet boss's right face, `port-2` |
| 14 | EF013561 Contour code connection 2 | not stated |
| 15 | EF021873 With coupling connection 2 | no: a fitting is placed in `port-2` |
| 16 | EF020152 Length of connection 2 | not stated |
| 17 | EF020154 Working length connection 2 | not stated |
| 18 | EF020007 Article compression class | not stated |
| 19 | EF020149 Flange compression class | not stated (no flange) |
| 20 | EF020100 Max. inlet pressure | 10 bar (1000 kPa gauge, about 145 psig); in ratings.csv as p_max, status "generic design" |
| 21 | EF024003 Reduced pressure | 0.5 to 7 bar (50 to 700 kPa gauge, about 7 to 102 psig): the outlet's setting range, set with `knob` |
| 22 | EF022466 Kvs value | not stated |
| 23 | EF023182 Medium temperature (continuous) | not stated |
| 24 | EF001776 Sealing | not stated |
| 25 | EF002223 With pressure gauge | no: `port-g` (female NPT 1/4, role gauge) takes gauge-p, placed, never redrawn |
| 26 | EF021587 With siphon | no |
| 27 | EF007245 Suitable for liquids | no |
| 28 | EF020335 Suitable for steam | no |
| 29 | EF007249 Suitable for gases | yes: compressed air to ISO 8573-1 [7:4:4] (pneu.py D3) |
| 30 | EF000040 Height | 86 mm (body 40, bonnet 30, knob 16) |
| 31 | EF020158 Spindle angle | not stated |
| 32 | EF022259 Wrench width union nut | not stated (no union nut on this element) |
| 33 | EFSE0002 Type approval according to BBR/EKS | no |

The pressures (class values 20 and 21) are generic design values (OPERATING.md 12), not tested ratings. 1000 kPa is above
P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it on a bench line; the setting range's top, 700 kPa, is above
P_WORK_MAX (551.6 kPa, 80 psig), the bench regulator's highest setting, so the range covers it. element.py asserts both. The
regulator is relieving: a set pressure turned down vents the outlet's excess through a small hole in the bonnet (not modelled),
not through a port, so it has no exhaust port and nothing to silence. The twin reads no pressure from the knob in 1.0.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| inlet boss | Ø20 × 14 along x, 0.5 into the body; `port-1` on its left face x = 0 | at least 3 mm of metal round the NPT 1/4 pipe OD (13.7 mm, pneu.NPT); 14 is at least 2 more than a male's effective thread L2 (10.21) and its make-up depth L1 + L3 (10.02), both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each, for every boss |
| port bores | Ø13.616 × 12.205 deep, blind, one in each boss (inlet, outlet, gauge), on the port's axis from its face | Ø = E1 + h of NPT 1/4 from pneu.NPT, the very diameter fitting-pushin 2.0 and gauge-p draw their male stubs at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 and < the boss's 14; 3.19 mm of boss wall round each bore (asserted ≥ 3). Role in features.csv (HOLE-010) |
| body | 40 × 40 × 40 (x, y, z), x 14 to 54, centred on the port axis | holds the seat and the diaphragm |
| outlet boss | Ø20 × 14 along +x on the body's right face; `port-2` at x = 68 | as the inlet boss, on the same axis (inline) |
| gauge boss | Ø20 × 14 along −y on the body's front face, at the body's centre x = 34; `port-g` at y = −34 | as the inlet boss |
| bonnet | Ø36 × 30 on the body's top face, 0.5 into it, z 20 to 50 | the spring housing, under the knob |
| adjusting knob | Ø30 × 16 on the bonnet, black, seated face to face (it turns) | `knob` |
| overall | envelope 68 × 54 × 86 (x 0 to 68, y −34 to 20, z −20 to 66) | |

All three ports are NPT 1/4, the size of the bench's FRL and gauge ports (pneu.py D3; next.md decision 1), so fitting-pushin 2.0's
male NPT 1/4 stub fits `port-1` and `port-2`, and gauge-p's fits `port-g`.

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | the inlet boss's face x = 0, axis −x | inlet; ISO 11727 number 1 as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1) |
| `port-2` | NPT1/4 | female | work | the outlet boss's face x = 68, axis +x | outlet; ISO 11727 number 2 as pneu.NODES; pneu.py D1 |
| `port-g` | NPT1/4 | female | gauge | the gauge boss's face y = −34, axis −y | downstream of the seat, so the gauge reads the set pressure; named as frl's `port-g` (next.md decision 1) |

PNE-002 pairs each with a male NPT of the same size (sealant on the male, D1). gauge-p 1.0 (0 to 160 psig) at `port-g`: PNE-009
judges a gauge at P_SUPPLY (100 psig, 62.5 % of its span, under pneu.GAUGE_FRACTION 0.75), so it passes there. Each face is the
joint plane a placed fitting meets; the bores behind them take the male stubs.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (inlet boss), `port-2` (outlet boss), `port-g` (gauge boss): kind port, fixed (range 0). `knob`: kind rotate about its own
axis (+z, through the bonnet's centre line), 0 to 1800° (five turns from the spring unloaded to the top of the range, a design
choice), seated face to face on the bonnet, so it sweeps only its own cylinder; the spring and stem it turns are inside and not
modelled.

## Materials by layer
`M-ALU-ANOD` inlet boss, body, outlet boss, gauge boss, bonnet · `M-BLACK-PA` adjusting knob

## Decals (Blender)
None (a flow arrow and the "generic" label are a later version). No vendor names.

## Outputs (out/)
`regulator.lsp` · `.glb` (port and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010122), pneu-r62 (unattended): inline anodised body with female NPT 1/4 inlet `port-1`, outlet `port-2` and gauge port `port-g`, each bored at E1 + h; bonnet with the adjusting `knob`; diaphragm, spring, seat and relief vent not modelled |
| 1.1 | pneu-r79 (unattended; review regulator-1.0.md finding 1, answered by lib/requests/core/pneu-7-answer.md item 2): text only. The What line and element.py's docstring say what the regulator does in the row's two process systems: it sets the control air of control-valve's actuator, never the loop's liquid (air only). No geometry, node, origin or cut-out changed |
