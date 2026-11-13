# check-valve · v2.0 · generic check valve, inline, female NPT both ends

**What** an inline check (non-return) valve for compressed air: air flows from `port-1` (the inlet) to `port-2` (the outlet) and a
spring-loaded poppet inside closes against flow the other way. It keeps a reservoir's pressure when the supply drops (a vacuum
circuit's or a receiver's) and keeps one branch from feeding back into another. It is not a load-holding valve: holding a cylinder
in place against a supply loss is a pilot-operated check valve's duty, a different product (review check-valve-1.0.md finding 2). lib/inventory.csv row `check-valve`
(own_design generic, made_of fitting-pushin x2: a push-in fitting placed in each port, in an assembly). The default build is NPT 1/4,
the size of the bench's FRL and gauge ports (pneu.py D3; next.md decision 1).
**Class** device · **Baseline** our own design: generic check valve (ETIM 10.0 EC011469), as OPERATING.md 12 (generic elements, EM
2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or measured. The class values below are its
design inputs; its sizes are design choices; its ports take their thread from the standard on file (ASME B1.20.1, through
toolkit/pneu.py) and their numbers from ISO 11727 (pneu.NODES). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the valve on its axis; the axis along y, flow toward +y (`port-1` at −y,
`port-2` at +y). Ports follow pneu.py's port frame: the pivot on the joint plane (the hex end's face), its axis toward the
counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CHECK-VALVE` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8).

## Class values (ETIM 10.0 EC011469, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | brass |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000139 Surface protection | none (bare brass) |
| 4 | EF023191 Nominal diameter | NPT 1/4 (parameter `thread`: NPT 1/8, 1/4, 3/8) |
| 5 | EF009322 Standard | ASME B1.20.1 (the port threads; pneu.py D1) |
| 6 | EF020126 Outer pipe diameter all connections | 13.7 mm: the NPT 1/4 pipe OD D = 0.540 in (pneu.NPT); 10.3 for NPT 1/8, 17.1 for NPT 3/8; the ports are female threads |
| 7 | EF022472 Connections | female thread NPT, both ends (ASME B1.20.1; pneu.py D1), sealed on the thread with sealant on the male |
| 8 | EF025254 Contour code | not stated |
| 9 | EF020007 Article compression class | not stated (the pressure is class value 27) |
| 10 | EF020149 Flange compression class | not stated (no flange) |
| 11 | EF000010 Model | inline check valve, spring-loaded poppet |
| 12 | EF020337 Valve shape | straight-through (inline) |
| 13 | EF025138 Low noise | not stated |
| 14 | EF001776 Sealing | soft seat (an elastomer seal on the poppet; not modelled) |
| 15 | EF024004 With balance weight | no |
| 16 | EF011775 Backflow safeguard according to EN 1717 | not stated (a compressed-air valve, not a potable-water device) |
| 17 | EF022466 Kvs value | not stated |
| 18 | EF020338 With lock spring | yes: the poppet's spring closes it in any mounting position |
| 19 | EF020002 Zeta value | not stated |
| 20 | EF020151 Length of connection 1 | 12.2 mm: the port bore's depth, L2 + 2 (NPT 1/8: 8.7, NPT 3/8: 12.4) |
| 21 | EF020153 Working length connection 1 | 10.2 mm: the male's effective thread L2 from pneu.NPT (NPT 1/8: 6.7, NPT 3/8: 10.4) |
| 22 | EF020152 Length of connection 2 | 12.2 mm, as connection 1 |
| 23 | EF020154 Working length connection 2 | 10.2 mm, as connection 1 |
| 24 | EF000040 Height | 28 mm (the body's diameter, the valve lying on its axis; NPT 1/8: 22, NPT 3/8: 33) |
| 25 | EF020339 Angle of non-return valve | not stated (straight-through, inline) |
| 26 | EF023182 Medium temperature (continuous) | not stated |
| 27 | EF023116 Max. operating pressure at 20 °C | 10 bar (1000 kPa gauge, about 145 psig); in ratings.csv as p_max, status "generic design" |
| 28 to 31 | EF021905, EF021907, EF021908, EF021909: the class's quality-mark features | no, each: no approval marks on our elements (OPERATING.md 6) |
| 32 | EF015424 Opening pressure valve cone | 100 mbar (the cracking pressure: about 1.5 psi) |
| 33 | EF024283 Suitable for potable water | no |
| 34 | EF021280 Suitable for central heating water | no |
| 35 to 41 | EFCH0002, EFCH0003, EFDE0010, EFDE0048, EFDE0049, EFNL0001, EFSE0002: the class's certificate, quality-mark and type-approval features | no, each: no approval marks on our elements (OPERATING.md 6) |

Medium: compressed air, ISO 8573-1:2010 class [7:4:4] (pneu.py D4). The pressure (class value 27) is a generic design value
(OPERATING.md 12), not a tested rating: 1000 kPa is above P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it on any
bench line. The cracking pressure (32) is a design value the twin may read; nothing checks it yet.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| hex ends | 13 long each, 22 AF for NPT 1/4 (17 for NPT 1/8, 26 for NPT 3/8); corners turned to 1.12 × AF; bare brass | wrench flats for holding the valve while a fitting is made up in it. Each AF leaves at least 3 mm of metal at the flats round its pipe OD (10.3 / 13.7 / 17.1): element.py asserts it against pneu.NPT. 13 is at least 2 more than a male's effective thread L2 (6.70 / 10.21 / 10.36) and its make-up depth L1 + L3 (6.92 / 10.02 / 10.33), both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): asserted |
| port bores | Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.36 for NPT 3/8), one blind bore in each hex end's face, on the valve's axis | the thread drawn plain at the male stub's own diameter E1 + h, so a placed fitting-pushin 2.0 or gauge-p stub touches the bore and does not overlap the solid (tank 2.0's rule); depth L2 + 2, a run-out past the male's effective thread; both from pneu.NPT (ASME B1.20.1 by its formulas, EM 2026-11-07). Each bore is deeper than the make-up L1 + L3 and blind inside the 13 long hex end (it stops 0.3 short of the body at NPT 1/4), with at least 3 mm of metal at the flats: asserted. Role in features.csv (HOLE-010) |
| body | Ø28 × 26 for NPT 1/4 (Ø22 × 22 for NPT 1/8, Ø33 × 30 for NPT 3/8), between the hex ends, 0.5 into each; bare brass | holds the poppet, seat and spring (not modelled: nothing moves outside the body); proud of the hex corners, asserted |
| overall | 52 long for NPT 1/4 (48 for NPT 1/8, 56 for NPT 3/8); envelope Ø28 × 52 | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 (parameter `thread`) | female | the inlet hex end's face y = −26, axis −y | inlet; ISO 11727 numbering (1 the supply side) as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1) |
| `port-2` | NPT1/4 (parameter `thread`) | female | the outlet hex end's face y = +26, axis +y | outlet; ISO 11727 numbering (2 the side it feeds) |

PNE-002 pairs each with a male NPT of the same size (fitting-pushin's `port-thread`; sealant on the male, D1). The ports carry no
role: a check valve passes on its line's role (supply, work) from the line it sits in. The flow direction is in the node numbers:
1 to 2. Each hex end's face is the joint plane a placed fitting meets; from 2.0 the port bore behind it takes the male's stub
(Dimensions, port bores). Cutting them changed the cut-outs, so 2.0 is a major version, as for tank.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1`, `port-2` (the hex ends); kind port, fixed (range 0)

## Materials by layer
`M-BRASS` hex ends and body

## Decals (Blender)
None in 1.0 (a flow arrow on the body is a later version). No vendor names.

## Outputs (out/)
`check-valve.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011469), pneu-r49 (unattended): two hex ends with female NPT port pivots (`port-1` inlet, `port-2` outlet), round body; port bores, poppet and spring not modelled |
| 2.0 | pneu-r59 (unattended), review check-valve-1.0.md findings 1 and 2: a blind port bore in each hex end, Ø E1 + h × L2 + 2 from pneu.NPT (13.616 × 12.205 at NPT 1/4), roles in features.csv; class values 20 to 23 from it; the first line no longer says the valve holds a cylinder in place |
