# claw-clamping · v1.1 · clamping claw, generic, fork clamp 110 × 32 × 16, M12 bolt slot, heel legs and nose pad

**What** A clamping claw for a machine table: a steel strap that holds a workpiece down on a milling or drilling table. A bolt in
the table's T-slot passes up through the claw's fork slot; tightening its nut presses the nose pad down on the work while the two
heel legs stand on the table behind it. The fork is open at the rear, so the claw slides onto a bolt already in place and off it
with the nut only slackened. One rigid part: no moving node.
**Class** device · **Baseline** our own design: generic clamping claw (ETIM 10.0 EC004295), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design inputs; the bolt
slot it meets is on file (ISO 273); every other size is a design choice. It is not built to a strap-clamp size standard (none is
on file) and claims conformity with none.
**Units / frame** mm, Z up. Origin: the heel legs' underside (the face that stands on the machine table) at z = 0, the bolt's axis
(the centre of the fork slot's closed end) at x = 0, y = 0. The nose is toward +x, the fork open toward −x; the strap's top face is
at z = 38.
**Built with** toolkit 1.3 · AutoLISP command `CLAMPCLAW` · no parameters.

## Class values
ETIM 10.0 class EC004295 Clamping claw (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Width (EF000008) | 32 mm: the strap across (y), and the heel and nose with it |
| 2 | Length (EF001438) | 110 mm: the strap, from the fork's open end to the nose |
| 3 | Diameter (EF000551) | not stated: a flat claw; it has no round part of its own (the slot takes the bolt, feature 4) |
| 4 | Suitable for bolt size (metric) (EF003566) | 12 (M12): the bolt through the fork slot |

## What it meets
| figure | value | source |
|---|---|---|
| the bolt | M12, through the fork slot: 14.5 wide, its closed end a Ø14.5 half-round at x = 0, open to the rear end at x = −70 | ISO 273 coarse (H14) for M12, 14.5 to 14.93, lib/standards/holes.csv: coarse, so the claw slides on and off the bolt freely. The bolt (a T-slot bolt), its nut and its washer are standard parts, never generic (OPERATING.md 12): the slot is cut, and they are placed in a later version once those elements are built. GDT-010: one hole, no pattern |
| the machine table, its T-slot | none in this element | the heel legs stand on the table's top face; the T-slot holds the bolt, not the claw (the table's element or host carries it) |
| the work | none in this element | the nose pad bears on its top face |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| strap | 110 × 32 × 16, x −70 to 40, z 22 to 38, zinc-plated steel | 16 thick: a design choice; no strength calculation or test is on file, so the strap claims no load |
| fork slot | the bolt 70 from the rear end and 40 from the nose: the bolt nearer the work | so the larger share of the bolt's force goes to the work (34 from the bolt to the nose's centre, 63 to the heel's) |
| heel legs | two, 14 × 8.75 × 22, under the rear end either side of the slot | they stand on the table and leave the slot open, so the claw slides onto the bolt |
| nose pad | 12 × 32 × 2 under the front end, its face at z 20 | with the strap level it clamps work 20 high above the table; other heights take a step block under the heel (not built) |
| one body | strap, heel legs and nose pad | one forged part; the AutoCAD gate may UNION them |

## Mechanism
None: one rigid part, placed and clamped by the bolt. No node, no pivot, no port.

## Named nodes
None. Colliders `body` (the strap and nose) and `heel` (the heel legs).

## Materials by layer
`M-ZINC` strap, heel legs and nose pad (zinc-plated steel).

## Decals (Blender)
"complexes.org generic" stamped on the strap's side face toward −y, between the slot's closed end and the nose.

## Notes
No vendor names, part numbers or marks. No safety claim. The class values are the figures this design is meant to meet; no
clamping force is stated (ETIM's class has no such feature) and no calculation or test of the model is on file. No open figure:
the slot is on file, and the bolt, nut and washer are standard parts placed later.

## Outputs (out/)
`claw-clamping.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004295), our own design (cloud-mech r3, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
| 1.1 | text only (review cloud-2026-11-07-r3 finding 1): the strap's 16 thickness written as a design choice with no strength calculation on file, not as carrying a load; model, nodes, origin and slot unchanged (mech-r52, unattended) |
