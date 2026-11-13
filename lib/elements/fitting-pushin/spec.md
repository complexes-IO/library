# fitting-pushin · v2.0 · generic push-in fitting, straight, inch tube to male NPT

**What** a straight push-in fitting (a male connector): one end screws into a female NPT port (manifold-pneu's ports, a cylinder's,
a valve's), the other takes one polyurethane tube of one inch OD, pushed in and held by the collet; pressing the release sleeve
frees it. A common part (lib/inventory.csv: part of 8 devices, 8 systems; pneu-1 fit-pi): the hosts place it, never redraw it.
The default build is tube 1/4 in to NPT 1/8, the size that meets manifold-pneu's work ports and pneu.ISO15552[32]'s port.
**Class** connector · **Baseline** our own design: generic fitting with 2 connections (ETIM 10.0 EC003024), as OPERATING.md 12
(generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or measured. The
class values below are its design inputs; its sizes are design choices; what it meets takes its series from the pneumatic
contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1; D2 inch tube, push-in fittings to ISO 14743) or is
left open (Open figures). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the hex's seat face y = 0 on the thread's axis (x = z = 0); the host port toward −y, the
tube end toward +y. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `FITTING-PUSHIN` · `tube` (1/4; 5/32, 1/4, 3/8) · `thread` (NPT1/8; NPT1/8,
NPT1/4, NPT3/8).

## Class values (ETIM 10.0 EC003024, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF025616 Material connection 1 | brass, nickel-plated (the hex end) |
| 2 | EF025618 Material quality connection 1 | not stated |
| 3 | EF010671 Surface protection connection 1 | nickel-plated |
| 4 | EF010672 Surface treatment connection 1 | not stated |
| 5 | EF025617 Material connection 2 | polyamide (the push-in body) |
| 6 | EF025619 Material quality connection 2 | not stated |
| 7 | EF010673 Surface protection connection 2 | not stated |
| 8 | EF010674 Surface treatment connection 2 | not stated |
| 9 | EF000051 Shape | straight |
| 10 | EF000010 Model | male connector: male thread to push-in |
| 11 | EF005431 Bend angle | 0° |
| 12 | EF020042 Bend radius | not stated |
| 13 | EF022617 Reducing | no |
| 14 | EF020055 Eccentric | no |
| 15 | EF025253 System specific | not stated |
| 16 | EF023193 Nominal diameter connection 1 | NPT 1/8 (parameter `thread`: NPT 1/8, 1/4, 3/8) |
| 17 | EF020122 Outer pipe diameter connection 1 | not stated (a thread) |
| 18 | EF021603 Wall thickness, connection 1 | not stated |
| 19 | EF016801 Wall thickness connecting pipe, connection 1 | not stated |
| 20 | EF000321 Connection 1 | male thread, NPT (ASME B1.20.1; pneu.py D1), sealed on the thread with sealant on the male |
| 21 | EF013560 Contour code connection 1 | not stated |
| 22 | EF020052 Nominal diameter connection 2 | tube 1/4 in (parameter `tube`: 5/32, 1/4, 3/8 in) |
| 23 | EF020123 Outer pipe diameter connection 2 | 6.35 mm (1/4 in); 3.96875 for 5/32, 9.525 for 3/8 (pneu.TUBES_IN, exact conversions) |
| 24 | EF021604 Wall thickness, connection 2 | not stated |
| 25 | EF016802 Wall thickness connecting pipe, connection 2 | not stated |
| 26 | EF000322 Connection 2 | push-in, for plastic tube (ISO 14743; pneu.py D2) |
| 27 | EF013561 Contour code connection 2 | not stated |
| 28 | EF016081 Main colour fitting | black body, grey release sleeve, nickel hex |
| 29 | EF018221 Flange compression class (ANSI) | not stated (no flange) |
| 30 | EF018222 Flange compression class (PN) | not stated (no flange) |
| 31 | EF018223 Flange compression class (JIS) | not stated (no flange) |
| 32 | EF018224 Flange compression class (BS) | not stated (no flange) |
| 33 | EF022606 Material sealing | not stated |
| 34 | EF020217 With buffer stud | no |
| 35 | EF020002 Zeta value | not stated |
| 36 | EF023873 High tensile strength | not stated |
| 37 | EF001438 Length | 30.2 mm: 23.5 above the seat face and the NPT 1/8 stub's 6.70 below it (NPT 1/4: 33.7; NPT 3/8: 33.9) |
| 38 | EF020151 Length of connection 1 | not stated |
| 39 | EF020153 Working length connection 1 | not stated |
| 40 | EF020152 Length of connection 2 | not stated |
| 41 | EF020154 Working length connection 2 | not stated |
| 42 | EF000177 Wrench width | 14 mm (NPT 1/8), 17 (NPT 1/4), 21 (NPT 3/8) |
| 43 | EF022259 Wrench width union nut | not stated (no union nut) |
| 44 | EF005520 Tightening moment | not stated |
| 45 | EF023182 Medium temperature (continuous) | not stated |
| 46 | EF023116 Max. operating pressure at 20 °C | 10 bar (1000 kPa gauge, about 145 psig); in ratings.csv as p_max, status "generic design" |
| 47 | EF014099 Max. operating pressure at max. medium temperature | not stated |
| 48 | EF023821 With thermal insulation | no |
| 49 | EF010669 Ring stiffness class | not stated |
| 50 | EF010670 Standard Dimension Ratio (SDR) | not stated |
| 51 | EF020047 With sealing rings/gaskets | yes: the tube seal inside the push-in end (not modelled in 1.x, Open figures) |
| 52 | EF020028 Capped | no |
| 53 | EF017615 With connection indicator | no |
| 54 | EF020078 With drain valve | no |
| 55 | EF020079 With de-aerator | no |
| 56 to 70 | EF021905, EF021909, EF021908, EF021907, EFDE0006, EFDE0010, EFDE0031, EFDE0048, EFDE0049, EFFR0015, EFNL0001, EFNL0002, EFNL0003, EFNL0016, EFSE0002: the class's quality-mark, certificate and type-approval features | no, each: no approval marks on our elements (OPERATING.md 6) |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT male stub | a plain cylinder from y = −L2 to the seat face (0.5 into the hex), part of the `port-thread` node: Ø10.24 × 6.70 for NPT 1/8, Ø13.62 × 10.21 for NPT 1/4, Ø17.06 × 10.36 for NPT 3/8; nickel-plated brass | from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2 = (0.80D + 6.8)P, the effective thread; diameter E1 + h, the external thread's major diameter at the hand-tight plane (E1 = E0 + L1/16, h = 0.8P). The library draws threads as plain cylinders (gland-m20, shock-buffer); the 1:16 taper (0.42 mm on the diameter over L2 for NPT 1/8) and the thread form are not drawn. Made up hand-tight plus wrench (L1 + L3, pneu.NPT engagement: 6.92 / 10.02 / 10.33), the stub's small end reaches 0.22 short of that depth for NPT 1/8 and the hex stands 0.19 (NPT 1/4) and 0.03 (NPT 3/8) off the port face; the pivot keeps the seat face on the port face |
| hex | 7 long (y 0 to 7), 14 AF for NPT 1/8, 17 for NPT 1/4, 21 for NPT 3/8; corners turned to 1.12 × AF; nickel-plated brass | wrench flats for fitting it; one AF per thread size. Each AF clears its thread's largest major diameter, E2 + h (10.40, 13.89, 17.32): element.py asserts it against pneu.NPT |
| push-in body | Ø12 for tube 1/4 (Ø10 for 5/32, Ø16 for 3/8), 14 long (y 7 to 21), 0.5 into the hex; polyamide | a body wider than its tube's OD |
| release sleeve | Ø(body − 1), 3 long, 0.5 into the body, its face at y = 23.5; grey polyamide | the part pressed to free the tube; its travel is not modelled in 1.x (Open figures) |
| overall | 23.5 above the seat face, 6.70 below it (NPT 1/8); envelope Ø15.7 (the hex's turned corners, NPT 1/8) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-thread` | NPT1/8 (parameter `thread`) | male | the hex's seat face y = 0, axis −y; the stub runs L2 along the axis (`length` in the pivot's data) | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a female NPT port of the same size; sealant on this male (D1) |
| `port-tube` | tube-1/4 (parameter `tube`) | female | the sleeve's face y = 23.5, axis +y | pneu.py D2 (inch tube, ISO 14743 push-in); PNE-001 pairs it with a tube end of the same OD |

The ports carry no role: a fitting passes on its line's role (supply, work, exhaust) from the port it is screwed into.

## Open figures
The one open figure is class B (a fit; OPERATING.md 6), set by the lane in pneu-r47; it wants a source and EM's line.
- NOT ON FILE (B): the push-in bore, insertion depth and release travel for each tube OD (pneu.PUSHIN: depth, release, bore). The
  push-in end is plain in 1.0 and 2.0; `port-tube` is a pivot on the sleeve's face. The bore is cut in a later version, once
  pneu.PUSHIN is on file.

Proposed by the lane (pneu-r47, carried to 2.0 by pneu-r48; OPERATING.md 8.c: EM approves by adding "· EM <date>"; until then it clears nothing):
- REVIEW accepted: the push-in end left plain (the pivot on the sleeve's face only), to be cut once pneu.PUSHIN is on file

The pressure value (class value 46) is a generic design value (OPERATING.md 12), not a tested rating.

## Named nodes
`port-thread` (the hex and the NPT stub), `port-tube` (the release sleeve); kind port, fixed (range 0)

## Materials by layer
`M-SILVER` hex and stub · `M-BLACK-PA` push-in body · `M-GREY-PA` release sleeve

## Decals (Blender)
None: no face on a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`fitting-pushin.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003024), pneu-r47 (unattended): hex, push-in body, release sleeve, two port pivots; thread stub (pneu.NPT came on file after the build) and push-in bore left out (Open figures) |
| 2.0 | pneu-r48 (unattended): the NPT male stub below the seat face from pneu.NPT (L2 long, Ø E1 + h, a plain cylinder in the `port-thread` node); new geometry below the origin, so a major; envelope now from y = −L2; each hex's AF checked against E2 + h; nodes, origin and the push-in end unchanged; the push-in bore still open (class B) |
