# tee-street-npt · v1.1 · generic street tee, two female NPT ports and one male NPT stub

**What** a street tee: a square steel block with three NPT connections of one size, two in line on the run and one on the branch at a
right angle, one of the run ends a male stub (`port-b`) and the other two female ports (`port-a` on the run, `port-c` on the branch).
It screws straight into a female port (a manifold's spare port, a receiver's tapping, a valve's outlet) and splits it in two, where
tee-block-npt 1.0 needs a nipple-hex-npt between them: one joint and one part fewer. The default build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic fitting with 3 connections (ETIM 10.0 EC003025; synonyms "Angle Tee",
"3-way knee"), as OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next class of the tier-2 group EG015540 "Fittings,
flanges and connectors" in pneu's order that builds, after cap-hex-npt's EC003023 (EC003024 is fitting-pushin's inventory class;
pneu-r107). The all-female threaded block tee is already tee-block-npt (EC010804), so this element is the form that differs. No vendor
file was opened or measured. The class values below are its design inputs; its sizes are design choices; its threads take their
series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names; "generic" in
its title.
**Why generic, and why a block** OPERATING.md 12 keeps a part whose shape a dimensional standard fixes from being generic. A
malleable-iron street tee is ASME B16.3's (centre-to-end and band per class and size); this tee is not one. It is machined from
square bar, tee-block-npt's section (a block tee with one end male), a form no dimensional standard shapes: no casting or forging
figure is in it (1.1: whether a standard is on file is no test for being generic, review tee-street-npt-1.0.md finding 2; the block
form is the reason, as tee-block-npt 1.1's). Its only standard figures are the threads, on file (ASME B1.20.1 by its formulas, pneu.NPT); the bar's
section and length are design choices. A B16.3-exact street tee is a later element, if a machine needs one.
**Units / frame** mm, Z up. Origin: where the run and branch axes meet, on their plane (z = 0); port-a toward −x and port-b (the
stub's seat face) toward +x on the run, port-c toward +y on the branch, no port toward −y. Ports follow pneu.py's port frame: the pivot
on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `TEE-STREET-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), all three connections the
same.

## Class values (ETIM 10.0 EC003025)
Design inputs. EC003025 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, cap-hex-npt 1.0's and coupling-clamp-strip 1.0's
way). Until they are on file this table gives the values this tee is designed to under plain names; a later minor restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| type | street tee (a T with one male run end), the class's "Angle Tee" form |
| number of connections | 3 |
| material | steel |
| surface | zinc-plated (a design choice for its look) |
| connection 1 (port-a, run) | female thread, NPT (ASME B1.20.1; pneu.py D1) |
| connection 2 (port-b, run) | male thread, NPT, as connection 1 |
| connection 3 (port-c, branch) | female thread, NPT, as connection 1 |
| size of connections (inch) | 1/4, all three the same (parameter `thread`: 1/8, 1/4, 3/8) |
| seal | none in the tee: the male's sealant seals each joint (NPT seals on its taper; pneu.py D1) |
| length | 44.405 mm for NPT 1/4, port-a's land face to the stub's end (32.902 for NPT 1/8, 47.56 for NPT 3/8) |
| max. pressure | not stated: no rating is claimed |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv (tee-block-npt 1.0's and cap-hex-npt 1.0's case): a tee carries the pressure of the
line it sits in, and no check reads a figure of its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| block | square bar 22 × 22 (y, z) for NPT 1/4 (18 for NPT 1/8, 26 for NPT 3/8), from x −23 (−17, −24) to x +11 (+9, +13): tee-block-npt's section and its −x half run, the +x end square on the branch axis; zinc-plated steel | design choice: tee-block-npt's section (1.1, review tee-street-npt-1.0.md finding 1): sizes that keep at least 3 mm of steel round each bore (WALL), the smallest even size for NPT 1/8 (18) and 2 mm over it for NPT 1/4 (22, against 20) and NPT 3/8 (26, against 24), a margin chosen, not a minimum. Element.py asserts each: section − bore Ø ≥ 6; half run − (L2 + 2) − bore Ø / 2 ≥ 3 (3.99 for NPT 1/4); section / 2 − bore Ø / 2 ≥ 3 past the branch bore toward the stub end (4.19); section − (L2 + 2) ≥ 3. Every envelope edge ≥ 8 (the AutoCAD gate's fillet pre-flight) |
| female ports | two blind bores, Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.36 for NPT 3/8): port-a into the −x end, port-c into the +y face at x 0 | tee-block-npt 1.0's bores (tank 2.0's rule): Ø E1 + h, the male's major diameter at the hand-tight plane, L2 + 2 deep (the 2 a run-out past the male's effective thread), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); deeper than a male's make-up L1 + L3 (asserted). The 1:16 taper and the thread form are not drawn (the library draws threads plain) |
| male stub | Ø13.616 × 10.205 long for NPT 1/4 (Ø10.242 × 6.702, Ø17.055 × 10.36) on the +x face, 0.5 into the block; zinc-plated steel | plug-hex-npt 1.0's stub: a plain cylinder at E1 + h, L2 long, from pneu.NPT. The block's +x face is its seat (the face that meets the female port's face when made up) and is wider than any female mouth of the size, E2 + h (asserted) |
| lands | a square land round each female bore, 18 × 18 for NPT 1/4 (14 for 1/8, 21 for 3/8), 0.2 proud of its face, the bore through it; zinc-plated steel | the port's node solid (a pivot needs a solid in its node), tee-block-npt's lands: no number is printed, a fitting's ends are named by the node. Each land is wider than its bore + 2 and inside its face (asserted) |
| flow passages | not drawn | where the two bores meet and through the stub (tee-block-npt's way); no check or host reads them; a later version may cut them |
| overall | 44.405 × 22.2 × 22 for NPT 1/4 (x land face to stub end, y to the branch land, z); 32.902 × 18.2 × 18 for NPT 1/8, 47.56 × 26.2 × 26 for NPT 3/8 | calculated from the sizes above |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | female | the −x land's outer face x −23.2, axis −x | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a male NPT end of the same size |
| `port-b` | NPT1/4 (parameter `thread`) | male | the stub's seat face x 11 (the block's +x face), axis +x; the stub 10.205 long | as port-a; pairs with a female NPT port of the same size |
| `port-c` | NPT1/4 (parameter `thread`) | female | the +y land's outer face y 11.2 at x 0, axis +y | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's and
tee-block-npt's way): a tee passes on its line's role. a, b and c are the class's connections 1, 2 and 3.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a`, `port-c` (the lands), `port-b` (the stub); kind port, fixed (range 0). The block is the fixed body.

## Materials by layer
`M-ZINC` block, lands and stub · `M-GASKET` the bores' cut layer (tee-block-npt's)

## Decals (Blender)
None: no face of a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`tee-street-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003025), pneu-r107 (unattended): square-bar street tee, two female NPT ports bored from pneu.NPT and one male NPT stub, three port pivots, parameter `thread`; no ratings (no rating is claimed); flow passages not drawn |
| 1.1 | pneu-r110 (unattended), review tee-street-npt-1.0.md: text only. (1) the block row: the sections 22 (NPT 1/4) and 26 (NPT 3/8) are 2 over the smallest even sizes that pass the asserts, not the smallest (tee-block-npt 1.1's sentence); (2) "Why generic" and the docstring give the block form as the reason, no longer a standard's not being on file, and name B16.3 only. No geometry change |
