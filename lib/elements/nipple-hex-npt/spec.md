# nipple-hex-npt · v1.1 · generic hex nipple, straight, male NPT at both ends

**What** a straight hex nipple: a wrench hex with one male NPT stub on each side, joining two female NPT ports of the same size face
to face. Its use in the lane: drain-auto hung from receiver-air's `port-drain` (both female NPT 1/4, the joint needs-em r79 asked
about), a gauge or a valve stood off a port, a hydraulic drain or water port (hyd-tank's, hyd-cooler's) to a female fitting. The
default build is NPT 1/4.
**Class** connector · **Baseline** our own design: generic hydraulic nipple, 2 connections (ETIM 10.0 EC010803), as OPERATING.md 12
(generic elements, EM 2026-11-07) says: the next ETIM class `python lib/build.py inventory pneu` lists that builds (pneu-r97). No
vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its threads take
their series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names;
"generic" in its title.
**Why generic** OPERATING.md 12 keeps a part a dimensional standard shapes (pipe among them) from being generic. A hex nipple is
turned from hex bar, not cut from pipe: no pipe wall or OD of ASME B36.10M is in it (a pipe nipple, threaded pipe, would be
pipe-asme's, waiting on that table). Its only standard figures are the threads, and those are on file (ASME B1.20.1 by its
formulas, pneu.NPT); the hex is a design choice, as on fitting-pushin 2.0. SAE J514's hydraulic hex nipple (its own hex and
length table) is not in lib/standards/sources.csv and is not used: a J514-exact version is a later element, if a machine needs one.
**Units / frame** mm, Z up. Origin: port-a's seat face (the hex's −y face) y = 0 on the thread's axis (x = z = 0); port-a's host
port toward −y, port-b's toward +y. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `NIPPLE-HEX-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), both ends the same.

## Class values (ETIM 10.0 EC010803, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000051 Shape | straight (hex nipple) |
| 4 | EF023498 Threaded connection 1 | male thread, NPT (ASME B1.20.1; pneu.py D1) |
| 5 | EF023496 Size of thread connection (inch) 1 | 1/4 (parameter `thread`: 1/8, 1/4, 3/8) |
| 6 | EF023497 Size of thread connection 1 | not stated (an inch thread: feature 5) |
| 7 | EF023578 Connection 1, gland nut end | no |
| 8 | EF023579 Hexagonal seal 1 | none (no seal under the hex) |
| 9 | EF023580 Threaded end seal 1 | sealant on the male thread (NPT seals on its taper; pneu.py D1) |
| 10 | EF023501 Threaded connection 2 | male thread, NPT (ASME B1.20.1; pneu.py D1) |
| 11 | EF023499 Size of thread connection (inch) 2 | 1/4, the same as connection 1 (parameter `thread`) |
| 12 | EF023500 Size of thread connection 2 | not stated (an inch thread: feature 11) |
| 13 | EF023581 Connection 2, gland nut end | no |
| 14 | EF023582 Hexagonal seal 2 | none |
| 15 | EF023583 Threaded end seal 2 | sealant on the male thread, as 9 |
| 16 | EF005431 Bend angle | 0° |

The class has no pressure, temperature or surface feature, so the element states none and has no ratings.csv (dryer-air 2.0's and
manifold-valve 2.0's case): the zinc plating below is a design choice for its look, not a class value. A nipple carries the pressure
of the ports it joins; no rating is claimed.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT male stubs | one each side of the hex, a plain cylinder from the hex face out L2, 0.5 into the hex: Ø13.62 × 10.21 for NPT 1/4 (Ø10.24 × 6.70 for NPT 1/8, Ø17.06 × 10.36 for NPT 3/8); zinc-plated steel | fitting-pushin 2.0's stub, from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2 = (0.80D + 6.8)P, the effective thread; diameter E1 + h, the external thread's major diameter at the hand-tight plane (E1 = E0 + L1/16, h = 0.8P). The library draws threads as plain cylinders (gland-m20, shock-buffer, fitting-pushin); the 1:16 taper and the thread form are not drawn. A bore drawn at E1 + h (the lane's female ports, tank 2.0's rule) takes each stub whole |
| hex | 8 long (y 0 to 8), 17 AF for NPT 1/4 (14 for NPT 1/8, 21 for NPT 3/8), corners turned to 1.12 × AF; zinc-plated steel | fitting-pushin 2.0's flats per thread size, so one wrench fits both; each AF clears its thread's largest major diameter, E2 + h (10.40, 13.89, 17.32): element.py asserts it against pneu.NPT. 8 long so every envelope edge is at least 8 (the AutoCAD gate's fillet pre-flight) |
| flow bore | not drawn | the bore is inside the ports once made up; no check or host reads it; a later version may cut it |
| overall | 28.41 long for NPT 1/4 (L2 + 8 + L2; 21.40 for NPT 1/8, 28.72 for NPT 3/8); envelope 17 across the flats (x) by 19.04 across the turned corners (z) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | male | the hex's −y face y = 0, axis −y; the stub runs L2 along the axis (`length` in the pivot's data) | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a female NPT port of the same size; sealant on this male (D1) |
| `port-b` | NPT1/4 (parameter `thread`) | male | the hex's +y face y = 8, axis +y; the stub as port-a's | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's way): a
nipple passes on its line's role from the port it is screwed into. a and b are the class's connections 1 and 2; either end goes
into either port.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a` (stub a), `port-b` (stub b); kind port, fixed (range 0). The hex is the fixed body.

## Materials by layer
`M-ZINC` hex and both stubs

## Decals (Blender)
None: no face on a nipple this size carries a legible mark. No vendor names.

## Outputs (out/)
`nipple-hex-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010803), pneu-r97 (unattended): hex with a male NPT stub each side from pneu.NPT, two port pivots, parameter `thread`; no ratings (the class states none); flow bore not drawn |
| 1.1 | pneu-r109 (unattended), text only (review nipple-hex-npt-1.0.md finding 2): element.py's material comment cited class values 1 and 3; 3 is Shape, so it now cites class value 1 (steel) and calls the zinc plating a design choice, as this spec does. Finding 1 (whether SAE J514's hex nipple table shapes this part) is EM's ruling (lib/needs-em/pneu.md r108 (b)): nothing moved to class B before it. No geometry change |
