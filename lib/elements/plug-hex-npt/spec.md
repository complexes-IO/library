# plug-hex-npt · v1.1 · generic hex-head plug, male NPT 1/4

**What** a hex-head plug: a wrench hex with one male NPT stub under it, closing a female NPT port of the same size. Its use in the
lane: a port a circuit leaves unused (a manifold's spare station port, tee-block-npt's or cross-block-npt's unused branch, a
receiver's or tank's spare tapping), which request pneu-1's rule "every port connected or plugged" asks to close. The default build
is NPT 1/4.
**Class** connector · **Baseline** our own design: generic hydraulic threaded plug (ETIM 10.0 EC010806), as OPERATING.md 12 (generic
elements, EM 2026-11-07) says: the next ETIM class `python lib/build.py inventory pneu` lists that builds (pneu-r100; the three it
still shows first, EC010596, EC001202 and EC010809, were skipped in pneu-r97 for the reasons given there). No vendor file was opened
or measured. The class values below are its design inputs; its sizes are design choices; its thread takes its series from the
pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names; "generic" in its title.
**Which standard shapes it** (1.1, review plug-hex-npt-1.0.md finding 1) OPERATING.md 12 keeps a part a dimensional standard
shapes from being generic. A hex head over a male NPT end is the form of ASME B16.11's hex-head plug (square, hex and round head,
each head's size and height tabulated per size), and turning it from hex bar does not take it outside that standard, so the head's
across-flats and height are B16.11's figures, not the lane's design choices. B16.11 is not on file: the head's two figures are one
class B line under Open figures (a document wanted, lib/standards/wanted.md), and the head drawn meanwhile is nipple-hex-npt 1.0's
hex, a stand-in kept until the table is on file (then a major, if its figures differ). The thread is ASME B1.20.1's, calculated
(pneu.NPT). Whether the plug stays generic at all is EM's (lib/needs-em/pneu.md r100, r110); the 1.0 reasoning from a standard's not
being on file is withdrawn.
**Units / frame** mm, Z up. Origin: port-a's seat face (the hex's −y face) y = 0 on the thread's axis (x = z = 0); the stub and the
host port toward −y, the head toward +y. The port follows pneu.py's port frame: the pivot on the joint plane, its axis toward the
counterpart.
**Built with** toolkit 1.3 · AutoLISP command `PLUG-HEX-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8).

## Class values (ETIM 10.0 EC010806, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000051 Shape | hex head |
| 4 | EF023498 Threaded connection 1 | male thread, NPT (ASME B1.20.1; pneu.py D1) |
| 5 | EF023496 Size of thread connection (inch) 1 | 1/4 (parameter `thread`: 1/8, 1/4, 3/8) |
| 6 | EF023497 Size of thread connection 1 | not stated (an inch thread: feature 5) |
| 7 | EF023578 Connection 1, gland nut end | no |
| 8 | EF023579 Hexagonal seal 1 | none (no seal under the hex) |
| 9 | EF023580 Threaded end seal 1 | sealant on the male thread (NPT seals on its taper; pneu.py D1) |
| 10 | EF020007 Article compression class | not stated |
| 11 | EF001438 Length | 18.21 mm for NPT 1/4, stub end to head top (14.70 for NPT 1/8, 18.36 for NPT 3/8) |
| 12 | EFDE0036 Load class (DIN 2353) | not stated (DIN 2353 is a cutting-ring fitting's load class; this plug is not one) |

The class has no pressure, temperature or surface feature, so the element states none and has no ratings.csv (nipple-hex-npt 1.0's
case): the zinc plating below is a design choice for its look, not a class value. A plug holds the pressure of the port it closes;
no rating is claimed.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT male stub | from the hex's seat face out L2, 0.5 into the hex: Ø13.62 × 10.21 for NPT 1/4 (Ø10.24 × 6.70 for NPT 1/8, Ø17.06 × 10.36 for NPT 3/8); zinc-plated steel | nipple-hex-npt 1.0's and fitting-pushin 2.0's stub, from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2 = (0.80D + 6.8)P, the effective thread; diameter E1 + h, the external thread's major diameter at the hand-tight plane (E1 = E0 + L1/16, h = 0.8P). The library draws threads as plain cylinders; the 1:16 taper and the thread form are not drawn. A bore drawn at E1 + h (the lane's female ports, tank 2.0's rule) takes the stub whole |
| hex head | 8 long (y 0 to 8), 17 AF for NPT 1/4 (14 for NPT 1/8, 21 for NPT 3/8), corners turned to 1.12 × AF; zinc-plated steel | a stand-in for B16.11's head (its across-flats and height are the class B line under Open figures, 1.1): nipple-hex-npt 1.0's hex, so one wrench fits the plug, the nipple and fitting-pushin; each AF clears its thread's largest major diameter, E2 + h (10.40, 13.89, 17.32): element.py asserts it against pneu.NPT. 8 long so every envelope edge is at least 8 (the AutoCAD gate's fillet pre-flight) |
| overall | 18.21 long for NPT 1/4 (L2 + 8); envelope 19.04 across the turned corners (x and z, the primitive's bounding box; 17 across the flats) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | male | the hex's −y face y = 0, axis −y; the stub runs L2 along the axis (`length` in the pivot's data) | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a female NPT port of the same size; sealant on this male (D1) |

The port carries no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's way): a
plug takes the role of the port it closes. a is the class's connection 1.

## Open figures
- NOT ON FILE (B): ASME B16.11, the hex-head plug's head: its across-flats and height per thread size (the standard is not in
  lib/standards/sources.csv). The head drawn is nipple-hex-npt 1.0's hex as a stand-in; once the table is on file the head takes its
  figures (a major if they differ). Every other figure is a class value, a design choice above, or calculated from ASME B1.20.1's
  formulas (pneu.NPT).

## Named nodes
`port-a` (the stub); kind port, fixed (range 0). The hex head is the fixed body.

## Materials by layer
`M-ZINC` head and stub

## Decals (Blender)
None: no face on a plug this size carries a legible mark. No vendor names.

## Outputs (out/)
`plug-hex-npt.lsp` · `.glb` (port pivot, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010806), pneu-r100 (unattended): nipple-hex-npt's hex as the head with one male NPT stub from pneu.NPT, one port pivot, parameter `thread`; no ratings (the class states none) |
| 1.1 | pneu-r110 (unattended), review plug-hex-npt-1.0.md finding 1, its option (b): text only. A hex head over a male NPT end is ASME B16.11's hex-head plug's form, so the head's across-flats and height are now one class B line (B16.11 a document wanted) and the drawn head a stand-in; the "not in sources.csv, so not B16.11's shape" reasoning dropped from spec.md and the docstring. Whether the plug stays generic is EM's. No geometry change |
