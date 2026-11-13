# cap-hex-npt · v1.1 · generic hex cap, female NPT 1/4

**What** a hex cap: a short length of hex bar with one female NPT port bored blind into its open end, closing a male NPT end of the
same size. Its use in the lane: a male end a circuit leaves open (nipple-hex-npt's free end, a stub or a pipe end held for a later
branch), which request pneu-1's rule "every port connected or plugged" asks to close. plug-hex-npt 1.0 closes a female port; this cap
is its female sibling. The default build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic fitting with 1 connection (ETIM 10.0 EC003023), as OPERATING.md 12
(generic elements, EM 2026-11-07) says: the next class of the tier-2 group EG015540 "Fittings, flanges and connectors" in pneu's order
that builds, after coupling-clamp-strip's EC011508 (pneu-r106; the round report says why the classes between them were passed over).
No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its thread takes
its series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names; "generic"
in its title.
**Why generic, and why a bar-stock cap** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. ASME B16.11
tabulates forged threaded caps (each class's and size's outside diameter and length), a round forged body; this cap is not one: it
is turned from hex bar, as plug-hex-npt 1.0 and nipple-hex-npt 1.0 are, and a hex-bar cap is, as far as the lane knows, a form no
dimensional standard shapes (1.1: whether a standard is on file is no test for being generic, review cap-hex-npt-1.0.md finding 2;
the form is the reason, as tee-block-npt 1.1's; EM rules the bar-stock reading with the tee's, lib/needs-em/pneu.md r98). Its only standard figure is the thread, and that is on file (ASME B1.20.1 by its formulas, pneu.NPT). A B16.11-exact cap is a
later element, if a machine needs one.
**Units / frame** mm, Z up. Origin: port-a's land face (the cap's open −y face) y = 0 on the thread's axis (x = z = 0); the male it
closes comes from −y, the closed end toward +y. The port follows pneu.py's port frame: the pivot on the joint plane, its axis toward
the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CAP-HEX-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8).

## Class values (ETIM 10.0 EC003023)
Design inputs. EC003023 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, tube-pneu 1.0's and coupling-clamp-strip 1.0's
way). Until they are on file this table gives the values this cap is designed to under plain names; a later minor restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| type | cap with hexagonal (the class's synonym): a blind female end |
| number of connections | 1 |
| material | steel |
| surface | zinc-plated (a design choice for its look) |
| connection 1 | female thread, NPT (ASME B1.20.1; pneu.py D1) |
| size of connection 1 (inch) | 1/4 (parameter `thread`: 1/8, 1/4, 3/8) |
| seal | none in the cap: the male's sealant seals the joint (NPT seals on its taper; pneu.py D1) |
| length | 16.405 mm for NPT 1/4, land face to closed end (12.902 for NPT 1/8, 16.56 for NPT 3/8) |
| width across flats | 21 mm for NPT 1/4 (17 for NPT 1/8, 24 for NPT 3/8) |
| max. pressure | not stated: no rating is claimed |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv (plug-hex-npt 1.0's and tee-block-npt 1.0's case): a cap holds the pressure of the
line it closes, and no check reads a figure of its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| port | one blind bore into the open end, Ø13.616 × 12.205 deep for NPT 1/4 (Ø10.242 × 8.702 for NPT 1/8, Ø17.055 × 12.36 for NPT 3/8) | the female port as the lane draws it (tank 2.0's rule, tee-block-npt 1.0's bores): Ø E1 + h, the male's major diameter at the hand-tight plane, L2 + 2 deep (the 2 a run-out past the male's effective thread), from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07); deeper than a male's make-up L1 + L3 (asserted). The 1:16 taper and the thread form are not drawn (the library draws threads plain) |
| hex body | 21 AF for NPT 1/4 (17 for NPT 1/8, 24 for NPT 3/8), two flats facing ±x, corners turned to 1.06 × AF (22.26; 18.02, 25.44); bore depth + 4 long (16.205; 12.702, 16.36); zinc-plated steel | design choice: flats that keep at least 3 mm of steel round the bore across the flats (WALL, tee-block-npt's figure: 3.69, 3.38, 3.47), the smallest whole flats for NPT 1/8 (17) and NPT 3/8 (24) and 1 over it for NPT 1/4 (21, against 20), a margin chosen, not a minimum (1.1, review cap-hex-npt-1.0.md finding 1), and 4 of steel past the bore's floor (FLOOR) as the closed end. A cap is bigger across than plug-hex-npt's hex because the thread is inside it. The corners are turned closer than plug-hex-npt's 1.12 × AF: the catalogue's envelope is the turned diameter on x and z, rounded to the mm, and the Godot QA allows 2.0 mm between it and the flats' 21 on x (at 1.12 the default read 24 against 21 and failed it; asserted for each size). Element.py asserts each wall, and every envelope edge ≥ 8 (the AutoCAD gate's fillet pre-flight) |
| land | a round land Ø19 for NPT 1/4 (Ø15, Ø22: AF − 2), 0.2 proud of the open face, the bore through it; zinc-plated steel | the port's node solid (a pivot needs a solid in its node), tee-block-npt's lands in the body's own finish; wider than the bore + 2 and inside the flats (asserted) |
| overall | 16.405 long for NPT 1/4 (y); envelope 22.26 across the turned corners (x and z, the primitive's bounding box; the solid is 21 across the flats on x, 22.26 on z); 18.02 × 12.902 for NPT 1/8, 25.44 × 16.56 for NPT 3/8 | calculated from the sizes above |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | female | the land's outer face y = 0, axis −y | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a male NPT end of the same size |

The port carries no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's way): a cap
takes the role of the end it closes. a is the class's connection 1.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a` (the land); kind port, fixed (range 0). The hex body is the fixed body.

## Materials by layer
`M-ZINC` body and land · `M-GASKET` the bore's cut layer (tee-block-npt's)

## Decals (Blender)
None: no face of a cap this size carries a legible mark. No vendor names.

## Outputs (out/)
`cap-hex-npt.lsp` · `.glb` (port pivot, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003023), pneu-r106 (unattended): a hex-bar cap with one blind female NPT port bored from pneu.NPT through a 0.2 land, one port pivot, parameter `thread`; no ratings (no rating is claimed) |
| 1.1 | pneu-r110 (unattended), review cap-hex-npt-1.0.md: text only. (1) the hex body row: 21 AF for NPT 1/4 is 1 over the smallest flats that pass the asserts (20), a margin chosen; 17 and 24 are the smallest; (2) "Why generic" and the docstring give the hex-bar form as the reason, no longer a standard's not being on file. No geometry change |
