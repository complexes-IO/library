# hose-flex-npt · v1.0 · generic braided connecting hose, male NPT 1/4 both ends, 300 long

**What** a flexible connecting hose: a synthetic rubber core under a stainless steel wire braid, with a crimped ferrule and a hex
end fitting at each end, each end a male NPT stub. It joins two female NPT ports that move against each other or don't line up: a
valve on a moving carriage, an air or coolant line across a hinge, a gauge set off a vibrating pump. The default build is 300 long
seat face to seat face, NPT 1/4 at both ends.
**Class** connector · **Baseline** our own design: generic flexible connecting hose, plastic/silicone/rubber core (ETIM 10.0
EC004090), as OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next ETIM class in generic.next_classes' order that builds
(pneu-r118; EC011399 Flexible connecting hose (metal), the one before it, was passed over: lib/rounds/pneu/r118.md section 2). No
vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its threads take
their series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads, ASME B1.20.1). No vendor names;
"generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. The lane knows of no
dimensional standard on file for a braided connecting hose's section or its crimped end fittings (a rubber hose's bore and wall
tolerances are a hose standard's, and none is on file; the hose here is drawn solid, so no bore figure is used). The end threads are
ASME B1.20.1's, calculated (pneu.NPT); the hex is nipple-hex-npt 1.1's flats as a design choice (a crimped hose end is not one of
ASME B16.11's forged fitting forms). The class's common form ends in female swivel nuts on a straight thread; this element ends in
male NPT stubs instead, since the library's thread series is NPT (pneu.py D1) and every port it meets on file is a female NPT port.
If EM rules otherwise, the section's figures become a "source wanted" line and the element waits for that document.
**Units / frame** mm, Z up. Origin: port-a's seat face (the first hex's −y face) y = 0 on the hose's axis (x = z = 0); port-a's host
port toward −y, the hose toward +y, drawn straight, port-b's seat face at y = `length`. The ports follow pneu.py's port frame: the
pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `HOSE-FLEX-NPT` · `thread` (NPT1/4; NPT1/4, NPT3/8) · `length` (300; 100 to 1500, seat
face to seat face).

## Class values (ETIM 10.0 EC004090)
Design inputs. EC004090 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its 34 features (the pneu-4 answer's case, tube-pneu 1.0's and hose-coolant-seg-npt 1.0's
way). Until they are on file this table gives the values this hose is designed to under plain names; a later minor restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| core material | synthetic rubber (NBR), not drawn (inside the braid) |
| braid | stainless steel wire, one braid layer |
| end fitting material | steel, zinc plated (hex ends and crimped ferrules) |
| connection, both ends | male thread, NPT (ASME B1.20.1; pneu.py D1), 1/4 (parameter `thread`: 1/4 or 3/8) |
| outside diameter | 12 over the braid for NPT 1/4 (16 for NPT 3/8) |
| inside diameter | not drawn, so not stated |
| length | 300 seat face to seat face (parameter `length`, 100 to 1500) |
| medium | compressed air, ISO 8573-1:2010 class [7:4:4] (pneu.py D4), or a machine's water-based coolant |
| max. operating pressure | not stated: a rating with no source on file (Open figures, class A); no ratings.csv |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

The pressure is not stated, tube-pneu 1.2's way (review pneu-r62 finding 1): a hose's working pressure is the rating PNE-003 reads
against the pressure that can reach it, so it decides what the twin reports, class A, EM's (OPERATING.md 6). No EC004090 feature is
on file to give it, and the parts at either end say nothing of the hose's own rating, which falls with temperature. Until a source or
EM gives it there is no ratings.csv, and PNE-003 has no rating to read on a line that places the hose.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT male stubs | from each hex's seat face out L2, 0.5 into the hex: Ø13.62 × 10.21 for NPT 1/4 (Ø17.06 × 10.36 for NPT 3/8) | nipple-hex-npt 1.1's stubs, from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2, diameter E1 + h. The library draws threads as plain cylinders; the 1:16 taper and the thread form are not drawn |
| end hexes | 8 long each (y 0 to 8 and length − 8 to length), 17 AF for NPT 1/4 (21 for NPT 3/8), corners turned to 1.06 × AF | nipple-hex-npt 1.1's flats per thread size, so one wrench fits; each AF clears its thread's largest major diameter E2 + h and is the widest part (both asserted); corners at 1.06 × AF as cap-hex-npt's, so the Godot gate's envelope rounding holds (asserted); 8 long so every envelope edge is at least 8 (the AutoCAD fillet pre-flight) |
| ferrules | Ø15 × 22 for NPT 1/4 (Ø19 × 22 for NPT 3/8), each running 0.5 into its hex | design choices: a crimped sleeve 2 under the hex's flats, so the hex stays the envelope; drawn as a plain cylinder (the crimp's flutes are not drawn) |
| hose | Ø12 over the braid for NPT 1/4 (Ø16 for NPT 3/8), between the ferrules, running 0.5 into each; drawn solid and straight | design choices: a 1/4 in and a 3/8 in bore hose's usual size class; the bore is not cut (nothing reads it) and the bend a machine gives it is not modelled |
| length | 300 seat face to seat face by default; 100 to 1500 by parameter | 100 keeps 20 of bare hose between the ferrules (asserted); a longer run is two hoses and a nipple |
| overall | 300 + 2 × 10.21 = 320.42 stub end to stub end for the default; envelope 18.02 across the hexes' turned corners (x and z, the primitive's bounding box; 17 across the flats) | element.py's overall() gives it |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | male | the first hex's −y face y = 0, axis −y; the stub runs L2 along the axis (`length` in the pivot's data) | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a female NPT port of the same size; sealant on this male (D1) |
| `port-b` | NPT1/4 (parameter `thread`) | male | the second hex's +y face y = `length` (300), axis +y | as `port-a` |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, fitting-pushin's and
nipple-hex-npt's way; a hose passes on its line's role). Either end may go first: the hose has no flow direction.

## Open figures
One open figure, class A (a rating; OPERATING.md 6), EM's.
- NOT ON FILE (A): the hose's max. operating pressure (p_max, a rating PNE-003 reads). EC004090 has no feature on file that gives
  it and no standard on file rates a braided rubber hose. EM's: a figure with its source, or a rating he accepts, closes it.

## Named nodes
`port-a`, `port-b` (the stubs); kind port, fixed (range 0). The hexes, ferrules and hose are the fixed body: the bend a machine gives
the hose is not modelled, so no part of it is a moving node.

## Materials by layer
`M-ZINC` hexes, stubs and ferrules · `M-SILVER` the braided hose (not M-BLACK-PA or M-WHITE-PA, the Blender gate's printed
materials, pneu-r113)

## Decals (Blender)
None in 1.0: no face on the hose carries a legible mark. No vendor names.

## Outputs (out/)
`hose-flex-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004090), pneu-r118 (unattended): a braided hose between two crimped ferrules and two hex end fittings, each with a male NPT stub from pneu.NPT; two port pivots; parameters `thread` and `length`; the max. operating pressure open (class A), no ratings.csv, no moving node |
