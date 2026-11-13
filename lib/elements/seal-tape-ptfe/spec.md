# seal-tape-ptfe · v1.1 · generic PTFE thread-seal tape, 12 wide, 15 m roll

**What** a roll of PTFE thread-seal tape: a thin white tape wound two or three turns onto a tapered male thread, with the thread's
hand, before the joint is made up; it fills the thread's flank and root clearances and lubricates the make-up. Its use in the lane:
the sealant toolkit/pneu.py D1 names, "sealed on the thread with sealant on the male", for every male NPT on our elements (fitting-pushin,
silencer, gauge-p, nipple-hex-npt, plug-hex-npt and the rest). A consumable: a machine places the roll in its store; a joint's spec
does not draw the tape on its thread. The default build is 15 m of 12 wide tape.
**Class** connector-part · **Baseline** our own design: generic PTFE sealing tape (ETIM 10.0 EC010670), as OPERATING.md 12 (generic
elements, EM 2026-11-07) says: the next ETIM class `python lib/build.py inventory pneu` lists that builds, after seal-strip-eptfe's
EC010669 in the Seals group (pneu-r102; why the classes between them were passed over is in lib/rounds/pneu/r102.md section 2). No
vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; no vendor names;
"generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic, whether that standard is on
file or not. Thread-seal tape is a consumable sold by its width, its thickness and its length and wound on by hand; documents do
specify it (the US federal commercial item description A-A-58092, which replaced MIL-T-27730A, and EN 751-3 for gas and hot-water
joints, as the review names them), and whether OPERATING.md 12's list of standard-shaped parts (screws to timing belts, all solid
parts) reaches a consumable's section is EM's ruling (lib/needs-em/pneu.md r108 (c)). Until he rules, the width and thickness
below are this design's choices, not taken from either document; if he rules that a standard shapes the tape, they become a
"source wanted" line on A-A-58092 and the element waits for it.
**Units / frame** mm, Z up. Origin: the centre of the roll's underside (z = 0) on its axis; the roll lies flat, its axis along +z, the
tape's width along z.
**Built with** toolkit 1.3 · AutoLISP command `SEAL-TAPE-PTFE` · `width` (12; 12, 19, 25 mm) · `length` (15000; 15000 to 50000 mm of
tape on the roll).

## Class values (ETIM 10.0 EC010670)
Design inputs. EC010670 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, tube-pneu 1.0's and seal-strip-eptfe 1.0's way).
Until they are on file this table gives the values this tape is designed to under plain names; a later minor restates them in ETIM's
order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| material | PTFE (polytetrafluoroethylene), unsintered, white |
| shape | tape, on a roll |
| width | 12 mm (parameter `width`: 19 or 25) |
| thickness | 0.1 mm |
| length | 15 m on the roll (parameter `length`, 15 to 50 m) |
| density | not stated |
| medium | not stated: the lane winds it on compressed-air and water NPT males; gas and oxygen service are not claimed |
| temperature range | not stated |
| max. pressure | not stated: the tape rates no pressure here and claims none; a joint's pressure is its own parts' (the NPT port's element) |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv: no check reads a sealing tape's figure, and the joint it seals carries its own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| tape | 12 wide (19, 25 by `width`), 0.1 thick | the trade's three widths for 1/8 to 1 in threads, rounded to whole mm; each at least 8 wide so the roll's height passes the AutoCAD gate's fillet pre-flight (element.py asserts it) |
| spool | Ø25 bore, wall 8, Ø41 outside, as wide as the tape; plastic | the tape's first turn sits on it face to face; the wall is 8 so every edge passes the fillet pre-flight |
| roll | Ø59.92 outside for 15 m | calculated, not chosen: the wound tape's end area, length × thickness, fills the annulus from the spool, π / 4 × (D² − 41²) = 15000 × 0.1, so D = √(41² + 4 × 15000 × 0.1 / π) = 59.92 (outside_d() in element.py; 74.17 for 30 m, 89.71 for 50 m; the width does not enter it). The tape is drawn as one solid annulus: its turns and its loose end are not drawn |
| length range | 15 m to 50 m | 15 m is the shortest roll whose wound tape is still 8 thick radially (9.46 at 15 m: the fillet pre-flight, asserted); 50 m keeps the roll under Ø100 (asserted) |
| envelope | Ø59.92 × 12 (default) | the roll lies flat |

## Ports (toolkit/pneu.py)
None. The tape joins nothing by itself: it lies in a thread that the joint's own male and female hold.

## Open figures
None. Every figure is a class value, a design choice above, or calculated from them (the roll's outside diameter).

## Named nodes
None. Nothing moves; the roll and its spool are the fixed body.

## Materials by layer
`M-WHITE-PVC` the tape (the white material on file closest to PTFE's look) · `M-BROWN` the spool

## Decals (Blender)
None in 1.0 (a width label on the spool's end face is a later version). No vendor names.

## Outputs (out/)
`seal-tape-ptfe.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010670), pneu-r102 (unattended): a flat roll of thread-seal tape on a plastic spool, seal-strip-eptfe 1.0's pattern, its outside diameter calculated from the tape's thickness and length; parameters `width` and `length`; no port, no node, no ratings |
| 1.1 | pneu-r111 (unattended), review seal-tape-ptfe-1.0.md finding 1: text only. "Why it may be generic" and the docstring put the rule's test (does a standard shape it, on file or not), name A-A-58092 and EN 751-3 as the review does, and leave the consumable question to EM (needs-em r108 (c)); the reason "no standard on file" is dropped. No geometry change |
