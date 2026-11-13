# hose-coolant-seg-npt · v1.0 · generic segmented coolant hose, male NPT 1/4 base, 16 segments

**What** a segmented (joint) coolant hose for a lathe or a mill: a hex base with one male NPT stub, screwed into a machine's
coolant outlet, then a stack of snap-together plastic segments, each a ball-like body on a neck, that the operator bends by hand to
aim the coolant at the cut, and a round nozzle at the free end. Its use in the lane: on a machine tool's coolant line, after
coolant-pump (EC010732) and its piping. The default build is 16 segments on an NPT 1/4 base.
**Class** connector · **Baseline** our own design: generic coolant hose for lathe/miller (ETIM 10.0 EC010441), as OPERATING.md 12
(generic elements, EM 2026-11-07) says: the next ETIM class in generic.next_classes' order that builds (pneu-r117; EC010442 Composite
hose, the one before it, was passed over: lib/rounds/pneu/r117.md section 2). No vendor file was opened or measured. The class values
below are its design inputs; its sizes are design choices; its thread takes its series from the pneumatic contract
`toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names; "generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. The lane knows of no
dimensional standard for a segmented coolant hose's segments: each system's ball, socket and nozzle sizes are its own, and segments of
two systems don't snap together. The base's thread is ASME B1.20.1's, calculated (pneu.NPT); its hex is nipple-hex-npt 1.0's flats
as a design choice (a hose base is not one of ASME B16.11's forged fitting forms). If EM rules otherwise, the segment's figures become
a "source wanted" line and the element waits for that document.
**Units / frame** mm, Z up. Origin: port-a's seat face (the base hex's −y face) y = 0 on the hose's axis (x = z = 0); the stub and the
host port toward −y, the hose and nozzle toward +y, drawn straight. The port follows pneu.py's port frame: the pivot on the joint
plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `HOSE-COOLANT-SEG-NPT` · `thread` (NPT1/4; NPT1/4, NPT3/8) · `segments` (16; 4 to 40).

## Class values (ETIM 10.0 EC010441)
Design inputs. EC010441 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its four features (the pneu-4 answer's case, tube-pneu 1.0's and sleeve-braid 1.0's way).
Until they are on file this table gives the values this hose is designed to under plain names; a later minor restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| material | acetal (POM) segments, base and nozzle, blue |
| connection | male thread, NPT (ASME B1.20.1; pneu.py D1), 1/4 (parameter `thread`: 1/4 or 3/8) |
| nominal size (the segments' system) | 1/4 in system: segment body Ø16, neck Ø10 |
| length | 288 mm seat face to nozzle tip with 16 segments (parameter `segments`, 4 to 40; 96 with 4) |
| nozzle | round, Ø6 tip |

The class has no pressure or temperature feature on file, and the hose claims none, so there is no ratings.csv: a joint coolant
hose runs at the coolant pump's low pressure, and no check reads a figure of it.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT male stub | from the hex's seat face out L2, 0.5 into the hex: Ø13.62 × 10.21 for NPT 1/4 (Ø17.06 × 10.36 for NPT 3/8) | nipple-hex-npt 1.0's and plug-hex-npt's stub, from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2, diameter E1 + h. The library draws threads as plain cylinders; the 1:16 taper and the thread form are not drawn |
| base hex | 8 long (y 0 to 8), 17 AF for NPT 1/4 (21 for NPT 3/8), corners turned to 1.06 × AF | nipple-hex-npt 1.0's flats per thread size, so one wrench fits; each AF clears its thread's largest major diameter E2 + h and is wider than a segment body (both asserted); corners at 1.06 × AF as cap-hex-npt's, so the Godot gate's envelope rounding holds (asserted); 8 long so every envelope edge is at least 8 (the AutoCAD fillet pre-flight) |
| segment | pitch 16: a neck Ø10 × 6 then a body Ø16 × 10; each neck runs 0.5 into the body or hex on either side (one solid joint) | design choices: a ball-and-socket segment drawn as two cylinders (the toolkit has no sphere); the stack is drawn straight, at rest |
| nozzle | a neck Ø10 × 6, a body Ø10 × 10 and a round tip Ø6 × 8 | design choices: a round nozzle; its tip face is where the coolant leaves |
| coolant passage | not drawn | the hose is drawn solid, plug-hex-npt's stub's way; nothing reads the bore |
| overall | 288 long for 16 segments (8 + 16 × 16 + 6 + 10 + 8), plus the stub's 10.21 below y = 0; envelope 18.02 across the hex's turned corners (x and z, the primitive's bounding box; 17 across the flats) | element.py's length() asserts it |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | male | the hex's −y face y = 0, axis −y; the stub runs L2 along the axis (`length` in the pivot's data) | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a female NPT port of the same size (coolant-pump's outlet is NPT 3/8: `thread` NPT3/8); sealant on this male (D1) |

The port carries no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's way; a
coolant line has no air role, coolant-pump's way). The nozzle's tip is no port: it discharges into the open, to the cut, and joins
nothing.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from ASME B1.20.1's formulas (pneu.NPT).

## Named nodes
`port-a` (the stub); kind port, fixed (range 0). The base, segments and nozzle are the fixed body: the operator's bend is set by
hand and not modelled, so no segment is a moving node.

## Materials by layer
`M-BLUE` base, stub, segments and nozzle (a blue plastic for acetal's look; not M-BLACK-PA or M-WHITE-PA, the Blender gate's printed
materials, pneu-r113)

## Decals (Blender)
None in 1.0: no face on the hose carries a legible mark. No vendor names.

## Outputs (out/)
`hose-coolant-seg-npt.lsp` · `.glb` (port pivot, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010441), pneu-r117 (unattended): a hex base with a male NPT stub from pneu.NPT, a straight stack of neck-and-body segments and a round nozzle; one port pivot; parameters `thread` and `segments`; no ratings, no moving node |
