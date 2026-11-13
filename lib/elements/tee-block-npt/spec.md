# tee-block-npt · v1.1 · generic block tee, three female NPT ports in a T

**What** a block tee: a square steel bar with three female NPT ports of one size, two in line on the run (`port-a`, `port-b`) and one
on the branch at a right angle (`port-c`), joining three male NPT ends where one line splits in two (a supply taken to two valves, a
gauge teed into a line through nipple-hex-npt, a hydraulic drain or water line split). The default build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic hydraulic threaded T-piece (ETIM 10.0 EC010804), as OPERATING.md 12
(generic elements, EM 2026-11-07) says: the next ETIM class `python lib/build.py inventory pneu` lists that builds (pneu-r98). No
vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its threads take
their series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names;
"generic" in its title.
**Why generic, and why a block** OPERATING.md 12 keeps a part whose shape a dimensional standard fixes from being generic. A forged
threaded tee is ASME B16.11's (its centre-to-end and band diameter per class and size), and a hydraulic tube-end tee is SAE J514's or
ISO 8434's; this tee is neither. It is machined from square bar (a block tee), a form no dimensional standard shapes: no
forging or tube-end figure is in it (1.1: whether a standard is on file is no test for being generic, review tee-block-npt-1.0.md
finding 2; the block form is the reason). Its only standard figures are the threads, on file (ASME B1.20.1 by its formulas, pneu.NPT);
the bar's section and length are design choices, as nipple-hex-npt 1.0's hex is. A B16.11-exact forged tee is a later element, if a
machine needs one.
**Units / frame** mm, Z up. Origin: the block's centre, on the plane of the three port axes (z = 0); port-a toward −x and port-b
toward +x on the run, port-c toward +y on the branch, no port toward −y. Ports follow pneu.py's port frame: the pivot on the joint
plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `TEE-BLOCK-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), all three ports the same.

## Class values (ETIM 10.0 EC010804, lib/standards/etim/class-features.csv)
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
| 8 | EF023580 Threaded end seal 1 | none in the tee: the male's sealant seals the joint (NPT seals on its taper; pneu.py D1) |
| 9 | EF023501 Threaded connection 2 | female thread, NPT, as connection 1 |
| 10 | EF023499 Size of thread connection (inch) 2 | 1/4, the same as connection 1 (parameter `thread`) |
| 11 | EF023500 Size of thread connection 2 | not stated (an inch thread: feature 10) |
| 12 | EF023581 Connection 2, gland nut end | no |
| 13 | EF023582 Hexagonal seal 2 | none |
| 14 | EF023583 Threaded end seal 2 | none in the tee, as 8 |
| 15 | EF023584 Threaded connection 3 | female thread, NPT, as connection 1 |
| 16 | EF023585 Size of thread connection (inch) 3 | 1/4, the same as connection 1 (parameter `thread`) |
| 17 | EF023586 Size of thread connection 3 | not stated (an inch thread: feature 16) |
| 18 | EF023587 Connection 3, gland nut end | no |
| 19 | EF023589 Hexagonal seal 3 | none |
| 20 | EF023588 Threaded end seal 3 | none in the tee, as 8 |

The class has no pressure, temperature or surface feature, so the element states none and has no ratings.csv (nipple-hex-npt 1.0's,
dryer-air 2.0's and manifold-valve 2.0's case). A tee carries the pressure of the line it sits in; no rating is claimed.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| block | square bar 22 × 22 (y, z), 46 long on the run (x) for NPT 1/4 (18 × 18 × 34 for NPT 1/8, 26 × 26 × 48 for NPT 3/8); zinc-plated steel | design choice: sizes that keep at least 3 mm of steel round each bore (WALL, valve-ball-32's figure) and between the run bores' floors and the branch bore. The runs are the smallest even lengths that do (34 / 46 / 48); the sections are the smallest even size for NPT 1/8 (18) and 2 mm over it for NPT 1/4 (22, against 20) and NPT 3/8 (26, against 24), a margin chosen, not a minimum (1.1, review tee-block-npt-1.0.md finding 1). Element.py asserts each: section − bore Ø ≥ 6; run / 2 − (L2 + 2) − bore Ø / 2 ≥ 3 (3.99 for NPT 1/4); section − (L2 + 2) ≥ 3. Every envelope edge ≥ 8 (the AutoCAD gate's fillet pre-flight) |
| ports | three blind bores, Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.36 for NPT 3/8): port-a into the −x end, port-b into the +x end, port-c into the +y face at x 0 | the female port as the lane draws it (tank 2.0's rule, valve-ball-32's bores): Ø E1 + h, the male's major diameter at the hand-tight plane, L2 + 2 deep (the 2 a run-out past the male's effective thread), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); deeper than a male's make-up L1 + L3 (asserted). The 1:16 taper and the thread form are not drawn (the library draws threads plain) |
| lands | a square land round each bore, 18 × 18 for NPT 1/4 (14 for 1/8, 21 for 3/8), 0.2 proud of its face, the bore through it; zinc-plated steel | the port's node solid (a pivot needs a solid in its node), valve-ball-32's number fields in the body's own finish: no number is printed, a fitting's ends are named by the node. Each land is wider than its bore + 2 and inside its face (asserted) |
| flow passages | not drawn | where the three bores meet inside the block (valve-ball-32's way); no check or host reads them; a later version may cut them |
| overall | 46.4 × 22.2 × 22 for NPT 1/4 (x across the run's lands, y to the branch land, z); 34.4 × 18.2 × 18 for NPT 1/8, 48.4 × 26.2 × 26 for NPT 3/8 | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | female | the −x land's outer face x −23.2, axis −x | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a male NPT end of the same size |
| `port-b` | NPT1/4 (parameter `thread`) | female | the +x land's outer face x 23.2, axis +x | as port-a |
| `port-c` | NPT1/4 (parameter `thread`) | female | the +y land's outer face y 11.2 at x 0, axis +y | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's and
nipple-hex-npt's way): a tee passes on its line's role. a, b and c are the class's connections 1, 2 and 3; any male of the size
goes into any port.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a`, `port-b`, `port-c` (the lands); kind port, fixed (range 0). The block is the fixed body.

## Materials by layer
`M-ZINC` block and lands · `M-GASKET` the bores' cut layer (valve-ball-32's)

## Decals (Blender)
None: no face of a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`tee-block-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010804), pneu-r98 (unattended): square-bar block tee with three female NPT ports bored from pneu.NPT, three port pivots, parameter `thread`; no ratings (the class states none); flow passages not drawn |
| 1.1 | pneu-r108 (unattended), review tee-block-npt-1.0.md: text only. (1) the block row: the sections 22 (NPT 1/4) and 26 (NPT 3/8) are 2 over the smallest even sizes that pass the asserts, not the smallest; (2) "Why generic" and the docstring give the block form as the reason, no longer a standard's not being on file. No geometry change |
