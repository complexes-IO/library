# gas-regulator · v2.2 · generic shielding gas regulator with tube flowmeter, female NPT ports

**What** a shielding gas regulator with a flowmeter for a welding station (MIG, TIG, plasma). It hangs on a gas cylinder's valve:
gas from the cylinder enters `port-1` on the inlet boss at the back, a preset single-stage regulator in the body reduces it to the
flowmeter's working pressure, and the gas rises through the clear sight tube on top, past the needle valve under the flow `knob`,
and leaves through `port-2` to the torch's gas hose. `port-g` on the body's left face takes a contents gauge.
lib/inventory.csv row `gas-regulator` (own_design generic, "shielding gas regulator and flowmeter"; welder-mig-station,
welder-plasma, welder-tig-station).
**Class** device · **Baseline** our own design: generic pressure reducing valve (ETIM 10.0 EC010122, synonym "Gas regulator"), as
OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or
measured. The class values below are its design inputs; its sizes are design choices; its ports take their thread from the
standard on file (ASME B1.20.1, through toolkit/pneu.py) and inlet and outlet their numbers from ISO 11727 (pneu.NODES). No vendor
names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of `port-1`'s joint plane on the inlet boss's back face (where the cylinder
connection meets it); the gas flows in along +y. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward
the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `GAS-REGULATOR` · no parameters.

The class chosen: EC010122 "Pressure reducing valve" (tier 2, group EG015810, 33 features on file; synonyms "Gas regulator",
"Compressed air regulator"), which is what the regulator half is. Rejected: EC010587 "Air flow meter" (synonyms "Gas flow meter",
"Rotameter"), the flowmeter half alone: it has no inlet-pressure feature, and the part that hangs on a cylinder at full cylinder
pressure is the regulator. The flowmeter is part of this design (the inventory row names both), not a separate element: nothing
else places it.

## Class values (ETIM 10.0 EC010122, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | brass (body and port bosses); bonnet, flowmeter blocks anodised aluminium |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000139 Surface protection | none on the brass; the aluminium parts anodised |
| 4 | EF023193 Nominal diameter connection 1 | 1/4 (NPT, ASME B1.20.1) |
| 5 | EF020122 Outer pipe diameter connection 1 | 13.7 mm (NPT 1/4 pipe OD D = 0.540 in, pneu.NPT) |
| 6 | EF000321 Connection 1 | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1) on the inlet boss's back face, `port-1` |
| 7 | EF013560 Contour code connection 1 | not stated |
| 8 | EF021872 With coupling connection 1 | no: the cylinder-valve nipple and nut are a separate part (see Ports) |
| 9 | EF020151 Length of connection 1 | not stated |
| 10 | EF020153 Working length connection 1 | not stated |
| 11 | EF020052 Nominal diameter connection 2 | 1/4 (NPT, ASME B1.20.1) |
| 12 | EF020123 Outer pipe diameter connection 2 | 13.7 mm (as connection 1) |
| 13 | EF000322 Connection 2 | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1) on the flowmeter's top block, `port-2` |
| 14 | EF013561 Contour code connection 2 | not stated |
| 15 | EF021873 With coupling connection 2 | no: the hose fitting is placed in `port-2` |
| 16 | EF020152 Length of connection 2 | not stated |
| 17 | EF020154 Working length connection 2 | not stated |
| 18 | EF020007 Article compression class | not stated |
| 19 | EF020149 Flange compression class | not stated (no flange) |
| 20 | EF020100 Max. inlet pressure | 300 bar (30 MPa gauge, about 4350 psig): a full gas cylinder's pressure; in ratings.csv as p_max, status "generic design" |
| 21 | EF024003 Reduced pressure | 3.5 to 3.5 bar (350 kPa gauge, about 51 psig): a fixed, preset setting, not a range; the pressure the flowmeter's tube is read at |
| 22 | EF022466 Kvs value | not stated |
| 23 | EF023182 Medium temperature (continuous) | not stated |
| 24 | EF001776 Sealing | not stated |
| 25 | EF002223 With pressure gauge | no: `port-g` (female NPT 1/4, role gauge) takes a contents gauge of its own, a later generic element with a span of at least 400 bar (Ports), placed, never redrawn; not gauge-p |
| 26 | EF021587 With siphon | no |
| 27 | EF007245 Suitable for liquids | no |
| 28 | EF020335 Suitable for steam | no |
| 29 | EF007249 Suitable for gases | yes: inert shielding gases (argon and argon mixes), the inventory row's use |
| 30 | EF000040 Height | 181 mm (body 50, flowmeter base 25, tube 70, top block 24, knob 12) |
| 31 | EF020158 Spindle angle | not stated |
| 32 | EF022259 Wrench width union nut | not stated (no union nut on this element) |
| 33 | EFSE0002 Type approval according to BBR/EKS | no |

The pressures (class values 20 and 21) are generic design values (OPERATING.md 12), not tested ratings. 30 MPa is far above
P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it anywhere on a bench line too. The flowmeter's scale (its flow
range and graduations) is not designed in 1.0: no flow figure is given or checked. A flowmeter tube reads true only at the pressure
it is calibrated at, so the regulator is preset to class value 21 and has no adjusting screw: the knob sets the flow, not the
pressure.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| inlet boss | Ø20 × 14 along y, bare brass, 0.5 into the body; `port-1` on its back face y = 0 | at least 3 mm of metal round the NPT 1/4 pipe OD (13.7 mm, pneu.NPT); 14 is at least 2 more than a male's effective thread L2 (10.21) and its make-up depth L1 + L3 (10.02), both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each, for every boss |
| port bores (2.0) | Ø13.616 × 12.205 deep, blind, one in each boss (inlet, gauge, outlet), on the port's axis from its face | Ø = E1 + h of NPT 1/4 from pneu.NPT, the very diameter fitting-pushin 2.0 and gauge-p draw their male stubs at, so stub and bore touch and never overlap (tank 2.0's rule, review pneu-r48 finding 1); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 and < the boss's 14; 3.19 mm of boss wall round each bore (asserted ≥ 3). Role in features.csv (HOLE-010) |
| body | 50 × 40 × 50 (x, y, z), bare brass, y 14 to 54 | holds the regulator's seat and diaphragm |
| bonnet | Ø40 × 20 on the body's front face, anodised aluminium | the spring housing; preset, so no adjusting screw |
| gauge boss | Ø20 × 14 along −x on the body's left face, at the flowmeter's centre line y = 34; `port-g` | as the inlet boss |
| flowmeter base block | 24 × 24 × 25 on the body's top face, anodised aluminium | carries the tube |
| sight tube | Ø22 × 70, clear, z 50 to 120 | the flowmeter's tube; the float inside is not modelled |
| top block | 28 × 28 × 24 over the tube, anodised aluminium | holds the needle valve and the outlet |
| outlet boss | Ø20 × 14 along +x on the top block's right face, 12 below its top; `port-2` | as the inlet boss |
| flow knob | Ø18 × 12 on the top block, black, seated face to face (it turns) | the needle valve's knob, `knob` |
| overall | envelope 67 × 74 × 181 (x −39 to 28, y 0 to 74, z −25 to 156) | |

All three ports are NPT 1/4, the size of the bench's FRL and gauge ports (pneu.py D3; next.md decision 1), so one male NPT 1/4 hose
fitting fits `port-2`. The thread of `port-g` fits a gauge's NPT 1/4 stub, but no gauge on file has the span for it (Ports).

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | the inlet boss's back face y = 0, axis −y | inlet; ISO 11727 number 1 as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1) |
| `port-g` | NPT1/4 | female | gauge | the gauge boss's face x = −39, axis −x | the contents gauge's port, upstream of the seat (it reads cylinder pressure); named as frl's `port-g` (next.md decision 1) |
| `port-2` | NPT1/4 | female | work | the outlet boss's face x = 28, axis +x | outlet to the torch's gas hose; ISO 11727 number 2 as pneu.NODES; pneu.py D1 |

PNE-002 pairs each with a male NPT of the same size (sealant on the male, D1). The cylinder side: a gas cylinder's valve outlet and
the nipple and nut that meet it are shaped by a dimensional standard (in the US, CGA V-1, with a connection number per gas), which
is not in lib/standards/sources.csv. That nipple is never generic (OPERATING.md 12): it is a separate element, built from its
standard once that is on file. `port-1`'s NPT 1/4 is this design's choice, taken from pneu.py D1 and D3, which are the
compressed-air bench contract (100 psig); nothing on file says which thread the cylinder connection's nipple carries or that an
NPT 1/4 port is right for a 30 MPa gas inlet, so that fit is open (Open figures; review gas-regulator-1.0.md finding 2).
Each face is the joint plane a placed fitting meets. 2.0 cuts the bores behind them (Dimensions), a change of cut-outs and so a
major version (OPERATING.md 7), as for tank 2.0: a male NPT 1/4 stub (fitting-pushin 2.0's) now goes into a bore instead of solid
brass. `port-g` reads cylinder pressure (up to class value 20, 300 bar): it takes a contents gauge of its own, a later generic
element (a Bourdon gauge as gauge-p, ETIM EC011170) whose span is at least 300 / 0.75 = 400 bar, so that PNE-009 (a gauge reads at
most pneu.GAUGE_FRACTION 0.75 of its span, a figure pneu.py holds open for EM, class A, ASME B40.100 not on file; not a
settled one, and no figure of this element depends on it) passes it at full cylinder pressure. gauge-p 1.0 (0 to 160 psig,
for air lines) is not for it: PNE-009 would FAIL it there (review gas-regulator-1.0.md finding 1).

## Open figures
1. The cylinder connection at `port-1`, class B (a fit): NPT 1/4 female is the design's choice; the thread of the nipple that
   meets it (CGA V-1 in the US) is NOT ON FILE (B) until that standard is in lib/standards/sources.csv. EM's to accept on
   his page, or the standard on file closes it.

Every other figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (inlet boss), `port-g` (gauge boss), `port-2` (outlet boss): kind port, fixed (range 0). `knob`: kind rotate about its own
axis (+z, through the tube's centre line), 0 to 360°, seated face to face on the top block, so it sweeps only its own cylinder;
the needle it turns is inside and not modelled. The twin reads no flow from it in 1.0.

## Materials by layer
`M-BRASS` inlet boss, body, gauge boss, outlet boss · `M-ALU-ANOD` bonnet, flowmeter base and top blocks · `M-CASE-CLEAR` sight
tube · `M-BLACK-PA` flow knob

## Decals (Blender)
None in 1.0 (the flowmeter's scale, a flow arrow and the "generic" label are a later version). No vendor names.

## Outputs (out/)
`gas-regulator.lsp` · `.glb` (port and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010122), pneu-r54 (unattended): brass body with the female NPT 1/4 inlet `port-1` at the back and gauge port `port-g` on the left, preset bonnet, tube flowmeter on top with the outlet `port-2` and the flow `knob`; port bores, the cylinder nipple, float and needle not modelled |
| 2.0 | pneu-r56 (unattended): the three port bores cut, Ø13.616 (E1 + h of NPT 1/4, pneu.NPT) × 12.205 (L2 + 2), blind in each boss, role in the new features.csv; nodes, origin and envelope unchanged |
| 2.1 | pneu-r59 (unattended), text only, review gas-regulator-1.0.md findings 1, 2 and 4: `port-g`'s gauge is a contents gauge of its own (span at least 400 bar), never gauge-p; the cylinder connection's thread at `port-1` written as a class B open figure, the nipple no longer said to carry NPT 1/4; class value 21 as a fixed setting, class value 33 with its name |
| 2.2 | pneu-r66 (unattended), text only, review pneu-r59 finding 1: Ports no longer calls pneu.GAUGE_FRACTION "the core's figure" but a figure pneu.py holds open for EM (class A); the reviewer's exact words are not used because DOC-005 would count them as an open line of this element; Open figures unchanged |
