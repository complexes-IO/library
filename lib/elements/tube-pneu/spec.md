# tube-pneu · v1.2 · generic pneumatic tube, polyurethane, inch OD, straight

**What** a straight length of polyurethane air tube, cut square at both ends: the line between a push-in fitting (fitting-pushin's
`port-tube`) and the next one. lib/inventory.csv row `tube-pneu` (own_design generic; its `used_by` names the systems that place
it), a common part every air circuit of the bench uses. The default build is 1/4 in OD × 500 mm, the bench's main
size (fitting-pushin's default tube; pneu.py D2).
**Class** tube · **Baseline** our own design: generic plastic hose without inlay (ETIM 10.0 EC011348), as OPERATING.md 12 (generic
elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or measured. The class values
below are its design inputs; its length and end nodes are design choices; its OD comes from the contract on file (toolkit/pneu.py
D2, TUBES_IN). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of `port-a`'s end face (y = 0) on the tube's axis; the tube runs along +y to `port-b`
at y = length. Ports follow pneu.py's port frame: the pivot on the joint plane (the end face), its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `TUBE-PNEU` · `tube` (1/4; 5/32, 1/4, 3/8) · `length` (500; 30 to 30000 mm).

## Class values (ETIM 10.0 EC011348)
Design inputs. EC011348 is a tier-2 class on no inventory row yet, so lib/standards/etim/class-features.csv (tier-1 classes and the
classes the inventory uses) does not list its 11 features; request pneu-4 asks the core to give the inventory row its class, which
brings them in. Until then this table gives the values this tube is designed to under plain names, and the next minor version
restates them in ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| material | polyurethane (PU), blue, one colour for the whole run |
| inlay | none (the class: a plastic hose without inlay) |
| outer diameter | 6.35 mm (1/4 in; parameter `tube`: 3.97 for 5/32, 9.53 for 3/8), the exact conversion of the size name (pneu.TUBES_IN, D2) |
| inner diameter | not stated (Open figures) |
| length | 500 mm (parameter `length`, 30 to 30000) |
| medium | compressed air, ISO 8573-1:2010 class [7:4:4] (pneu.py D4) |
| max. operating pressure at 20 °C | not stated: a rating with no source on file (Open figures 2, class A); no p_max row in ratings.csv |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

The pressure is not stated (1.2; review pneu-r62 finding 1). PNE-003 reads a tube's p_max against the pressure that can reach it,
so it is a rating that decides what the twin reports: class A, EM's (OPERATING.md 6). No EC011348 feature on file names a
pressure (class-features.csv lists none for the class; request pneu-4), and the 10 bar of the parts at either end (fitting-pushin,
check-valve) says nothing of the tube's own rating, which falls with temperature. 1.1's p_max row (10 bar, "design choice") is
gone; the figure is open below until a source or EM gives it, and PNE-003 then has no rating to read on a line that places the tube.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| tube | Ø6.35 (the OD, pneu.TUBES_IN) × 500 for the default; drawn solid; blue PU | the OD is the one figure a push-in fitting grips (ISO 14743), so it is the tube's interface; the bore is not cut (Open figures) |
| end nodes | the last 10 of each end (`port-a` y 0 to 10, `port-b` the last 10 before y = length), face to face with the run between them | the part of the tube the twin binds to at each joint; a design choice, not an insertion depth (pneu.PUSHIN holds none) |
| length | 500 by default; 30 to 30000 by parameter | 30 holds both end nodes and a run between them; 30 m is one coil, a longer line is two tubes and a union |
| envelope | Ø6.35 × 500 (default) | |

The tube is straight in 1.0. A routed tube (a `path` parameter, as cordset-m12 and wire take) bends, and how tight it may bend is
pneu.TUBE's `bend_min`, which is empty: routing waits for it.

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | tube-1/4 (parameter `tube`) | male | the end face y = 0, axis −y | pneu.py D2 (inch tube; a tube end is male, a push-in port female); PNE-001 pairs it with a push-in port of the same OD |
| `port-b` | tube-1/4 (parameter `tube`) | male | the end face y = length (500), axis +y | as `port-a` |

The ports carry no role: a tube passes on its line's role (supply, work, exhaust). PNE-001 fails a tube in a push-in port of another
OD or series (1/4 in and 6 mm are look-alikes; neither holds in the other's collet). Either end may go first: a tube has no flow
direction.

## Open figures
Two open figures. The first is class B (a fit; OPERATING.md 6), set by the lane in pneu-r50; it wants a source and EM's line.
- NOT ON FILE (B): the tube's inside diameter for each OD (pneu.TUBE: `id`). The tube is drawn solid to its OD in 1.0; the bore is
  cut in a later version, once pneu.TUBE's `id` is on file (ISO 7628 or a standard's table EM puts on file).
- NOT ON FILE (A): the tube's max. operating pressure (p_max, a rating PNE-003 reads; added in 1.2, review pneu-r62 finding 1).
  EC011348 has no feature on file that gives it (request pneu-4) and no standard on file rates a polyurethane tube. EM's: a figure
  with its source, or a rating he accepts, closes it.

Proposed by the lane (pneu-r50; OPERATING.md 8.c: EM approves by adding "· EM <date>"; until then it clears nothing):
- REVIEW accepted: the tube drawn solid to its OD (the bore not cut), to be cut once pneu.TUBE's inside diameter is on file

## Named nodes
`port-a`, `port-b` (the end nodes); kind port, fixed (range 0)

## Materials by layer
`M-BLUE` the whole tube

## Decals (Blender)
None in 1.0 (a size print along the tube is a later version). No vendor names.

## Outputs (out/)
`tube-pneu.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011348), pneu-r50 (unattended): a straight solid tube at its inch OD, two end nodes with male tube port pivots (`port-a`, `port-b`), `tube` and `length` parameters; the bore and a routed path left for later (Open figures, class B) |
| 1.1 | pneu-r62 (unattended), text only, review tube-pneu-1.0.md finding 3: ratings.csv's p_max source no longer names a class feature that is not on file; it says design choice, as fitting-pushin and check-valve. Nodes, origin, cut-outs unchanged |
| 1.2 | pneu-r68 (unattended), text only, review pneu-r62 finding 1: the 10 bar p_max had no source, so ratings.csv drops its row and the max. operating pressure becomes the second open line, class A, EM's (chiller 1.1's way); Class values says not stated. Nodes, origin, cut-outs unchanged |
