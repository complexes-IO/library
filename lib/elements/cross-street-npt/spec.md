# cross-street-npt · v1.0 · generic street cross, three female NPT ports and one male NPT stub

**What** a street cross: a square steel block with four NPT connections of one size, two in line on the run and two opposed on the
branch at a right angle, one of the run ends a male stub (`port-b`) and the other three female ports (`port-a` on the run, `port-c`
and `port-d` on the branch). It screws straight into a female port (a manifold's spare port, a receiver's tapping, a valve's outlet)
and splits it in three, where cross-block-npt 1.1 needs a nipple-hex-npt between them: one joint and one part fewer. The default
build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic fitting with 4 connections (ETIM 10.0 EC003026; synonyms "Ball piece
with 4 connections", "Angle fitting"), as OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next class of the tier-2 group
EG015540 "Fittings, flanges and connectors" in pneu's order that builds, after tee-street-npt's EC003025 (pneu-r110). The all-female
threaded block cross is already cross-block-npt (EC010805), so this element is the form that differs, as tee-street-npt is to
tee-block-npt. No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices;
its threads take their series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No
vendor names; "generic" in its title.
**Why generic, and why a block** OPERATING.md 12 keeps a part whose shape a dimensional standard fixes from being generic. This
cross is machined from square bar, cross-block-npt's section (a block cross with one end male), a form no dimensional standard
shapes: no casting or forging figure is in it. The block form is the reason (review tee-block-npt-1.0.md finding 2: whether a
standard is on file is no test), and EM rules the block reading for the tees and crosses together (lib/needs-em/pneu.md r108 (a)).
Its only standard figures are the threads (ASME B1.20.1 by its formulas, pneu.NPT); the bar's section and length are design choices.
**Units / frame** mm, Z up. Origin: where the run and branch axes meet, on their plane (z = 0); port-a toward −x and port-b (the
stub's seat face) toward +x on the run, port-c toward +y and port-d toward −y on the branch. Ports follow pneu.py's port frame: the
pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CROSS-STREET-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), all four connections
the same.

## Class values (ETIM 10.0 EC003026)
Design inputs. EC003026 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, tee-street-npt's way). Until they are on file this
table gives the values this cross is designed to under plain names; a later minor restates them in ETIM's order with their EF codes,
"not stated" where the design has no value.

| feature | value |
|---|---|
| type | street cross (a cross with one male run end) |
| number of connections | 4 |
| material | steel |
| surface | zinc-plated (a design choice for its look) |
| connection 1 (port-a, run) | female thread, NPT (ASME B1.20.1; pneu.py D1) |
| connection 2 (port-b, run) | male thread, NPT, as connection 1 |
| connection 3 (port-c, branch) | female thread, NPT, as connection 1 |
| connection 4 (port-d, branch) | female thread, NPT, as connection 1 |
| size of connections (inch) | 1/4, all four the same (parameter `thread`: 1/8, 1/4, 3/8) |
| seal | none in the cross: the male's sealant seals each joint (NPT seals on its taper; pneu.py D1) |
| length | 47.405 mm for NPT 1/4, port-a's land face to the stub's end (34.902 for NPT 1/8, 48.558 for NPT 3/8) |
| max. pressure | not stated: no rating is claimed |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv (cross-block-npt's and tee-street-npt's case): a cross carries the pressure of the
line it sits in, and no check reads a figure of its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| block | square bar 28 × 28 (y, z) for NPT 1/4 (22 for NPT 1/8, 28 for NPT 3/8), from x −23 (−17, −24) to x +14 (+11, +14): cross-block-npt's section and its −x half run, the +x end square on the branch axis; zinc-plated steel | design choice: cross-block-npt's section, deeper than the tee's because the two branch bores face each other across it. Element.py asserts each: section − bore Ø ≥ 6; half run − (L2 + 2) − bore Ø / 2 ≥ 3 (3.99 for NPT 1/4); section / 2 − bore Ø / 2 ≥ 3 past the branch bores toward the stub end (7.19); section − 2 (L2 + 2) ≥ 3 between the opposed branch floors (3.59; 4.60 for NPT 1/8, 3.28 for NPT 3/8). Every envelope edge ≥ 8 (the AutoCAD gate's fillet pre-flight) |
| female ports | three blind bores, Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.358 for NPT 3/8): port-a into the −x end, port-c into the +y face and port-d into the −y face at x 0 | cross-block-npt's bores (tank 2.0's rule): Ø E1 + h, the male's major diameter at the hand-tight plane, L2 + 2 deep (the 2 a run-out past the male's effective thread), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); deeper than a male's make-up L1 + L3 (asserted). The 1:16 taper and the thread form are not drawn (the library draws threads plain) |
| male stub | Ø13.616 × 10.205 long for NPT 1/4 (Ø10.242 × 6.702, Ø17.055 × 10.358) on the +x face, 0.5 into the block; zinc-plated steel | plug-hex-npt 1.0's stub: a plain cylinder at E1 + h, L2 long, from pneu.NPT. The block's +x face is its seat (the face that meets the female port's face when made up) and is wider than any female mouth of the size, E2 + h (asserted) |
| lands | a square land round each female bore, 18 × 18 for NPT 1/4 (14 for 1/8, 21 for 3/8), 0.2 proud of its face, the bore through it; zinc-plated steel | the port's node solid (a pivot needs a solid in its node), cross-block-npt's lands: no number is printed, a fitting's ends are named by the node. Each land is wider than its bore + 2 and inside its face (asserted) |
| flow passages | not drawn | where the bores meet and through the stub (cross-block-npt's way); no check or host reads them; a later version may cut them |
| overall | 47.405 × 28.4 × 28 for NPT 1/4 (x land face to stub end, y land face to land face, z); 34.902 × 22.4 × 22 for NPT 1/8, 48.558 × 28.4 × 28 for NPT 3/8 | calculated from the sizes above |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | female | the −x land's outer face x −23.2, axis −x | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a male NPT end of the same size |
| `port-b` | NPT1/4 (parameter `thread`) | male | the stub's seat face x 14 (the block's +x face), axis +x; the stub 10.205 long | as port-a; pairs with a female NPT port of the same size |
| `port-c` | NPT1/4 (parameter `thread`) | female | the +y land's outer face y 14.2 at x 0, axis +y | as port-a |
| `port-d` | NPT1/4 (parameter `thread`) | female | the −y land's outer face y −14.2 at x 0, axis −y | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's and
cross-block-npt's way): a cross passes on its line's role. a, b, c and d are the class's connections 1, 2, 3 and 4.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a`, `port-c`, `port-d` (the lands), `port-b` (the stub); kind port, fixed (range 0). The block is the fixed body.

## Materials by layer
`M-ZINC` block, lands and stub · `M-GASKET` the bores' cut layer (cross-block-npt's)

## Decals (Blender)
None: no face of a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`cross-street-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003026), pneu-r110 (unattended): square-bar street cross, three female NPT ports bored from pneu.NPT and one male NPT stub, four port pivots, parameter `thread`; no ratings (no rating is claimed); flow passages not drawn |
