# cross-block-npt · v1.1 · generic block cross, four female NPT ports in a cross

**What** a block cross: a square steel bar with four female NPT ports of one size, two in line on the run (`port-a`, `port-b`) and
two opposed on the branch at a right angle (`port-c`, `port-d`), joining four male NPT ends where one line splits in three (a supply
taken to three valves, a gauge and a drain teed into one line through nipple-hex-npt). The default build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic hydraulic threaded cross piece (ETIM 10.0 EC010805), as OPERATING.md 12
(generic elements, EM 2026-11-07) says: the next ETIM class `python lib/build.py inventory pneu` lists that builds (pneu-r99). No
vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its threads take
their series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names;
"generic" in its title.
**Why generic, and why a block** OPERATING.md 12 keeps a part whose shape a dimensional standard fixes from being generic. A forged
threaded cross is ASME B16.11's (its centre-to-end and band diameter per class and size), and a hydraulic tube-end cross is SAE
J514's or ISO 8434's; this cross is neither. It is machined from square bar (a block cross), tee-block-npt's way, a form no
dimensional standard shapes: no forging or tube-end figure is in it (1.1: whether a standard is on file is no test for being
generic, review cross-block-npt-1.0.md finding 2; the block form is the reason). Its only standard figures are the threads, on file (ASME
B1.20.1 by its formulas, pneu.NPT); the bar's section and length are design choices. A B16.11-exact forged cross is a later element,
if a machine needs one.
**Units / frame** mm, Z up. Origin: the block's centre, on the plane of the four port axes (z = 0); port-a toward −x and port-b
toward +x on the run, port-c toward +y and port-d toward −y on the branch. Ports follow pneu.py's port frame: the pivot on the joint
plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CROSS-BLOCK-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), all four ports the same.

## Class values (ETIM 10.0 EC010805, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel |
| 2 | EF001257 Material quality | not stated (zinc-plated, a design choice for its look) |
| 3 | EF023498 Threaded connection 1 | female thread, NPT (ASME B1.20.1; pneu.py D1) |
| 4 | EF023496 Size of thread connection (inch) 1 | 1/4 (parameter `thread`: 1/8, 1/4, 3/8) |
| 5 | EF023497 Size of thread connection 1 | not stated (an inch thread: feature 4) |
| 6 | EF023578 Connection 1, gland nut end | no |
| 7 | EF023579 Hexagonal seal 1 | none |
| 8 | EF023580 Threaded end seal 1 | none in the cross: the male's sealant seals the joint (NPT seals on its taper; pneu.py D1) |
| 9 | EF023501 Threaded connection 2 | female thread, NPT, as connection 1 |
| 10 | EF023499 Size of thread connection (inch) 2 | 1/4, the same as connection 1 (parameter `thread`) |
| 11 | EF023500 Size of thread connection 2 | not stated (an inch thread: feature 10) |
| 12 | EF023581 Connection 2, gland nut end | no |
| 13 | EF023582 Hexagonal seal 2 | none |
| 14 | EF023583 Threaded end seal 2 | none in the cross, as 8 |
| 15 | EF023584 Threaded connection 3 | female thread, NPT, as connection 1 |
| 16 | EF023585 Size of thread connection (inch) 3 | 1/4, the same as connection 1 (parameter `thread`) |
| 17 | EF023586 Size of thread connection 3 | not stated (an inch thread: feature 16) |
| 18 | EF023587 Connection 3, gland nut end | no |
| 19 | EF023589 Hexagonal seal 3 | none |
| 20 | EF023588 Threaded end seal 3 | none in the cross, as 8 |
| 21 | EF023590 Threaded connection 4 | female thread, NPT, as connection 1 |
| 22 | EF023591 Size of thread connection (inch) 4 | 1/4, the same as connection 1 (parameter `thread`) |
| 23 | EF023592 Size of thread connection 4 | not stated (an inch thread: feature 22) |
| 24 | EF023593 Connection 4, gland nut end | no |
| 25 | EF023595 Hexagonal seal 4 | none |
| 26 | EF023594 Threaded end seal 4 | none in the cross, as 8 |

The class has no pressure, temperature or surface feature, so the element states none and has no ratings.csv (tee-block-npt 1.0's
and nipple-hex-npt 1.0's case). A cross carries the pressure of the line it sits in; no rating is claimed.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| block | square bar 28 × 28 (y, z), 46 long on the run (x) for NPT 1/4 (22 × 22 × 34 for NPT 1/8, 28 × 28 × 48 for NPT 3/8); zinc-plated steel | design choice: the run lengths are tee-block-npt 1.0's; the section is the smallest even millimetre that keeps 3 mm of steel (WALL, valve-ball-32's figure) between the floors of the two opposed branch bores, section − 2 × (L2 + 2) ≥ 3 (3.59 for NPT 1/4, 4.60 for 1/8, 3.28 for 3/8); the tee's 18 / 22 / 26 would leave 0.60 (NPT 1/8) and 1.28 (NPT 3/8), under WALL, and NPT 1/4's opposed bores would meet, by 2.41 (1.1, review cross-block-npt-1.0.md finding 1). Element.py asserts it, and as the tee: section − bore Ø ≥ 6; run / 2 − (L2 + 2) − bore Ø / 2 ≥ 3 (3.99 for NPT 1/4). Every envelope edge ≥ 8 (the AutoCAD gate's fillet pre-flight) |
| ports | four blind bores, Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.36 for NPT 3/8): port-a into the −x end, port-b into the +x end, port-c into the +y face and port-d into the −y face at x 0 | the female port as the lane draws it (tank 2.0's rule, valve-ball-32's and tee-block-npt's bores): Ø E1 + h, the male's major diameter at the hand-tight plane, L2 + 2 deep (the 2 a run-out past the male's effective thread), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); deeper than a male's make-up L1 + L3 (asserted). The 1:16 taper and the thread form are not drawn (the library draws threads plain) |
| lands | a square land round each bore, 18 × 18 for NPT 1/4 (14 for 1/8, 21 for 3/8), 0.2 proud of its face, the bore through it; zinc-plated steel | the port's node solid (a pivot needs a solid in its node), tee-block-npt's lands: no number is printed, a fitting's ends are named by the node. Each land is wider than its bore + 2 and inside its face (asserted) |
| flow passages | not drawn | where the four bores meet inside the block (valve-ball-32's way); no check or host reads them; a later version may cut them |
| overall | 46.4 × 28.4 × 28 for NPT 1/4 (x across the run's lands, y across the branch's lands, z); 34.4 × 22.4 × 22 for NPT 1/8, 48.4 × 28.4 × 28 for NPT 3/8 | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | female | the −x land's outer face x −23.2, axis −x | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a male NPT end of the same size |
| `port-b` | NPT1/4 (parameter `thread`) | female | the +x land's outer face x 23.2, axis +x | as port-a |
| `port-c` | NPT1/4 (parameter `thread`) | female | the +y land's outer face y 14.2 at x 0, axis +y | as port-a |
| `port-d` | NPT1/4 (parameter `thread`) | female | the −y land's outer face y −14.2 at x 0, axis −y | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's,
nipple-hex-npt's and tee-block-npt's way): a cross passes on its line's role. a, b, c and d are the class's connections 1 to 4; any
male of the size goes into any port.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a`, `port-b`, `port-c`, `port-d` (the lands); kind port, fixed (range 0). The block is the fixed body.

## Materials by layer
`M-ZINC` block and lands · `M-GASKET` the bores' cut layer (valve-ball-32's)

## Decals (Blender)
None: no face of a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`cross-block-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010805), pneu-r99 (unattended): square-bar block cross with four female NPT ports bored from pneu.NPT, four port pivots, parameter `thread`; tee-block-npt 1.0's run, ports and lands on a deeper section; no ratings (the class states none); flow passages not drawn |
| 1.1 | pneu-r108 (unattended), review cross-block-npt-1.0.md: text only. (1) the block row: the tee's sections would leave 0.60 / 1.28 between the opposed branch floors (NPT 1/8 / 3/8) and NPT 1/4's would meet, not "leave none"; (2) "Why generic" and the docstring give the block form as the reason, no longer a standard's not being on file. No geometry change |
