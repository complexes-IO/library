# cross-6way-block-npt · v1.0 · generic six-way block cross, six female NPT ports

**What** a six-way block cross: a steel bar with six female NPT ports of one size, two in line on the run (`port-a`, `port-b`), two
opposed on the branch at a right angle (`port-c`, `port-d`) and two opposed on the side branch, square to both (`port-e` on top,
`port-f` underneath), joining six male NPT ends where one line splits in five (a supply taken to four valves and a gauge through
nipple-hex-npt, or a header tying lines from three directions). The default build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic fitting with 6 connections (ETIM 10.0 EC010367; synonym "Ball piece
with 6 connections"), as OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next class of the tier-2 group EG015540
"Fittings, flanges and connectors" in pneu's order that builds, after cross-side-block-npt's EC003097 (pneu-r112). No vendor file
was opened or measured. The class values below are its design inputs; its sizes are design choices; its threads take their series
from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names; "generic" in its
title.
**Why generic, and why a block** OPERATING.md 12 keeps a part whose shape a dimensional standard fixes from being generic. A cast
six-way fitting (a malleable-iron "ball piece") is shaped by its casting standard, and a hydraulic tube-end fitting by SAE J514 or
ISO 8434; this one is neither. It is machined from bar (a block), cross-block-npt's way, a form no dimensional standard shapes: no
casting, forging or tube-end figure is in it. The block form is the reason (review tee-block-npt-1.0.md finding 2: whether a
standard is on file is no test), and EM rules the block reading for the tees and crosses together (lib/needs-em/pneu.md r108 (a)).
Its only standard figures are the threads (ASME B1.20.1 by its formulas, pneu.NPT); the bar's sizes are design choices. A cast
ball piece to its standard is a later element, if a machine needs one.
**Units / frame** mm, Z up. Origin: the block's centre, where the run, branch and side-branch axes meet; port-a toward −x and
port-b toward +x on the run, port-c toward +y and port-d toward −y on the branch, port-e toward +z and port-f toward −z on the side
branch. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CROSS-6WAY-BLOCK-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), all six ports the
same.

## Class values (ETIM 10.0 EC010367)
Design inputs. EC010367 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, cross-side-block-npt's way). Until they are on
file this table gives the values this fitting is designed to under plain names; a later minor restates them in ETIM's order with
their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| type | six-way cross (block form) |
| number of connections | 6 |
| material | steel |
| surface | zinc-plated (a design choice for its look) |
| connections 1 to 6 (port-a to port-f) | female thread, NPT (ASME B1.20.1; pneu.py D1) |
| size of connections (inch) | 1/4, all six the same (parameter `thread`: 1/8, 1/4, 3/8) |
| seal | none in the fitting: the male's sealant seals each joint (NPT seals on its taper; pneu.py D1) |
| max. pressure | not stated: no rating is claimed |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv (the block crosses' case): a fitting carries the pressure of the line it sits in,
and no check reads a figure of its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| block | 46 long on the run (x), 28 across the branch (y), from z −23 to z +23 for NPT 1/4 (34 × 22, z −17 to +17 for NPT 1/8; 48 × 28, z −24 to +24 for NPT 3/8); zinc-plated steel | design choice: cross-block-npt 1.1's run and section across the branch. Above and below the ports' plane the block reaches top(), cross-side-block-npt's: the lowest whole millimetre that keeps 3 mm of steel (WALL, valve-ball-32's figure) between a side bore's floor and the top of the run and branch bores, top − (L2 + 2) − bore Ø / 2 ≥ 3, rounded up (22.01 → 23 for NPT 1/4, 16.82 → 17 for 1/8, 23.89 → 24 for 3/8), the same both ways so port-f mirrors port-e. Element.py asserts it, and that the two side bores' floors keep steel between them, 2 top − 2 (L2 + 2) ≥ 3 (21.59 for NPT 1/4; 16.60 for NPT 1/8, 23.28 for NPT 3/8), and as cross-block-npt: section − bore Ø ≥ 6; run / 2 − (L2 + 2) − bore Ø / 2 ≥ 3 (3.99 for NPT 1/4); section − 2 (L2 + 2) ≥ 3 between the opposed branch floors (3.59; 4.60 for NPT 1/8, 3.28 for NPT 3/8). Every envelope edge ≥ 8 (the AutoCAD gate's fillet pre-flight) |
| ports | six blind bores, Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.36 for NPT 3/8): port-a into the −x end, port-b into the +x end, port-c into the +y face and port-d into the −y face on z 0 at x 0, port-e into the top face and port-f into the bottom face at x 0, y 0 | cross-block-npt's bores (tank 2.0's rule): Ø E1 + h, the male's major diameter at the hand-tight plane, L2 + 2 deep (the 2 a run-out past the male's effective thread), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); deeper than a male's make-up L1 + L3 (asserted). The 1:16 taper and the thread form are not drawn (the library draws threads plain) |
| lands | a square land round each bore, 18 × 18 for NPT 1/4 (14 for 1/8, 21 for 3/8), 0.2 proud of its face, the bore through it; zinc-plated steel | the port's node solid (a pivot needs a solid in its node), cross-block-npt's lands: no number is printed, a fitting's ends are named by the node. Each land is wider than its bore + 2 and inside its face (asserted) |
| flow passages | not drawn | where the six bores meet inside the block (cross-block-npt's way); no check or host reads them; a later version may cut them |
| overall | 46.4 × 28.4 × 46.4 for NPT 1/4 (x across the run's lands, y across the branch's lands, z bottom land to top land); 34.4 × 22.4 × 34.4 for NPT 1/8, 48.4 × 28.4 × 48.4 for NPT 3/8 | calculated from the sizes above |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | female | the −x land's outer face x −23.2, axis −x | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a male NPT end of the same size |
| `port-b` | NPT1/4 (parameter `thread`) | female | the +x land's outer face x 23.2, axis +x | as port-a |
| `port-c` | NPT1/4 (parameter `thread`) | female | the +y land's outer face y 14.2 at x 0, axis +y | as port-a |
| `port-d` | NPT1/4 (parameter `thread`) | female | the −y land's outer face y −14.2 at x 0, axis −y | as port-a |
| `port-e` | NPT1/4 (parameter `thread`) | female | the top land's outer face z 23.2 at x 0, y 0, axis +z | as port-a |
| `port-f` | NPT1/4 (parameter `thread`) | female | the bottom land's outer face z −23.2 at x 0, y 0, axis −z | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's and
cross-block-npt's way): a fitting passes on its line's role. a to f are the class's connections 1 to 6; any male of the size goes
into any port. The block has no plain face to stand on: a host holds it by its pipework, or plugs a port with plug-hex-npt.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a`, `port-b`, `port-c`, `port-d`, `port-e`, `port-f` (the lands); kind port, fixed (range 0). The block is the fixed body.

## Materials by layer
`M-ZINC` block and lands · `M-GASKET` the bores' cut layer (cross-block-npt's)

## Decals (Blender)
None: no face of a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`cross-6way-block-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010367), pneu-r112 (unattended): six-way block cross, six female NPT ports bored from pneu.NPT, six port pivots, parameter `thread`; cross-side-block-npt 1.0's run, section, ports and lands, the block mirrored below the plane for port-f; no ratings (no rating is claimed); flow passages not drawn |
