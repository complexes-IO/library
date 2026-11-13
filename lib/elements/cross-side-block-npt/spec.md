# cross-side-block-npt · v1.0 · generic block cross with side branch, five female NPT ports

**What** a block cross with a side branch: a steel bar with five female NPT ports of one size, two in line on the run (`port-a`,
`port-b`), two opposed on the branch at a right angle (`port-c`, `port-d`) and a fifth on the top face (`port-e`), square to both,
joining five male NPT ends where one line splits in four (a supply taken to three valves and a gauge, through nipple-hex-npt). The
default build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic fitting with 5 connections (ETIM 10.0 EC003097; synonyms "Cross piece
with side branch", "T-piece with double branch", "Ball piece with 5 connections"), as OPERATING.md 12 (generic elements, EM
2026-11-07) says: the next class of the tier-2 group EG015540 "Fittings, flanges and connectors" in pneu's order that builds, after
cross-street-npt's EC003026 (pneu-r111). No vendor file was opened or measured. The class values below are its design inputs; its
sizes are design choices; its threads take their series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT
threads, ASME B1.20.1). No vendor names; "generic" in its title.
**Why generic, and why a block** OPERATING.md 12 keeps a part whose shape a dimensional standard fixes from being generic. A cast
five-way fitting (a malleable-iron "ball piece") is shaped by its casting standard, and a hydraulic tube-end fitting by SAE J514 or
ISO 8434; this one is neither. It is machined from bar (a block), cross-block-npt's way, a form no dimensional standard shapes: no
casting, forging or tube-end figure is in it. The block form is the reason (review tee-block-npt-1.0.md finding 2: whether a
standard is on file is no test), and EM rules the block reading for the tees and crosses together (lib/needs-em/pneu.md r108 (a)).
Its only standard figures are the threads (ASME B1.20.1 by its formulas, pneu.NPT); the bar's sizes are design choices. A cast
ball piece to its standard is a later element, if a machine needs one.
**Units / frame** mm, Z up. Origin: where the run and branch axes meet, on their plane (z = 0); port-a toward −x and port-b toward
+x on the run, port-c toward +y and port-d toward −y on the branch, port-e toward +z. The underside (z −14 for NPT 1/4) is plain.
Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CROSS-SIDE-BLOCK-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), all five ports the
same.

## Class values (ETIM 10.0 EC003097)
Design inputs. EC003097 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, cross-street-npt's way). Until they are on file
this table gives the values this fitting is designed to under plain names; a later minor restates them in ETIM's order with their EF
codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| type | cross with side branch (block form) |
| number of connections | 5 |
| material | steel |
| surface | zinc-plated (a design choice for its look) |
| connections 1 to 5 (port-a to port-e) | female thread, NPT (ASME B1.20.1; pneu.py D1) |
| size of connections (inch) | 1/4, all five the same (parameter `thread`: 1/8, 1/4, 3/8) |
| seal | none in the fitting: the male's sealant seals each joint (NPT seals on its taper; pneu.py D1) |
| max. pressure | not stated: no rating is claimed |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv (cross-block-npt's and cross-street-npt's case): a fitting carries the pressure of
the line it sits in, and no check reads a figure of its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| block | 46 long on the run (x), 28 across the branch (y), from z −14 to z +23 for NPT 1/4 (34 × 22, z −11 to +17 for NPT 1/8; 48 × 28, z −14 to +24 for NPT 3/8); zinc-plated steel | design choice: cross-block-npt 1.1's run and section below the ports' plane. Above it the top is raised: it is the lowest whole millimetre that keeps 3 mm of steel (WALL, valve-ball-32's figure) between the side bore's floor and the top of the run and branch bores, top − (L2 + 2) − bore Ø / 2 ≥ 3, rounded up (top(): 22.01 → 23 for NPT 1/4, 16.82 → 17 for 1/8, 23.89 → 24 for 3/8). A square section (top 14) would put the side bore's floor at z 1.80, 5.01 below the top of the run and branch bores (z 6.81, NPT 1/4): the bores would meet. Element.py asserts it, and as cross-block-npt: section − bore Ø ≥ 6; run / 2 − (L2 + 2) − bore Ø / 2 ≥ 3 (3.99 for NPT 1/4); section − 2 (L2 + 2) ≥ 3 between the opposed branch floors (3.59; 4.60 for NPT 1/8, 3.28 for NPT 3/8). Every envelope edge ≥ 8 (the AutoCAD gate's fillet pre-flight) |
| ports | five blind bores, Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.36 for NPT 3/8): port-a into the −x end, port-b into the +x end, port-c into the +y face and port-d into the −y face on z 0 at x 0, port-e into the top face at x 0, y 0 | cross-block-npt's bores (tank 2.0's rule): Ø E1 + h, the male's major diameter at the hand-tight plane, L2 + 2 deep (the 2 a run-out past the male's effective thread), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); deeper than a male's make-up L1 + L3 (asserted). The 1:16 taper and the thread form are not drawn (the library draws threads plain) |
| lands | a square land round each bore, 18 × 18 for NPT 1/4 (14 for 1/8, 21 for 3/8), 0.2 proud of its face, the bore through it; zinc-plated steel | the port's node solid (a pivot needs a solid in its node), cross-block-npt's lands: no number is printed, a fitting's ends are named by the node. Each land is wider than its bore + 2 and inside its face (asserted) |
| flow passages | not drawn | where the five bores meet inside the block (cross-block-npt's way); no check or host reads them; a later version may cut them |
| overall | 46.4 × 28.4 × 37.2 for NPT 1/4 (x across the run's lands, y across the branch's lands, z underside to the top land); 34.4 × 22.4 × 28.2 for NPT 1/8, 48.4 × 28.4 × 38.2 for NPT 3/8 | calculated from the sizes above |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | female | the −x land's outer face x −23.2, axis −x | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a male NPT end of the same size |
| `port-b` | NPT1/4 (parameter `thread`) | female | the +x land's outer face x 23.2, axis +x | as port-a |
| `port-c` | NPT1/4 (parameter `thread`) | female | the +y land's outer face y 14.2 at x 0, axis +y | as port-a |
| `port-d` | NPT1/4 (parameter `thread`) | female | the −y land's outer face y −14.2 at x 0, axis −y | as port-a |
| `port-e` | NPT1/4 (parameter `thread`) | female | the top land's outer face z 23.2 at x 0, y 0, axis +z | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's and
cross-block-npt's way): a fitting passes on its line's role. a to e are the class's connections 1 to 5; any male of the size goes
into any port.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a`, `port-b`, `port-c`, `port-d`, `port-e` (the lands); kind port, fixed (range 0). The block is the fixed body.

## Materials by layer
`M-ZINC` block and lands · `M-GASKET` the bores' cut layer (cross-block-npt's)

## Decals (Blender)
None: no face of a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`cross-side-block-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003097), pneu-r111 (unattended): block cross with side branch, five female NPT ports bored from pneu.NPT, five port pivots, parameter `thread`; cross-block-npt 1.1's run, section, ports and lands, the top raised so the side bore keeps WALL over the others; no ratings (no rating is claimed); flow passages not drawn |
