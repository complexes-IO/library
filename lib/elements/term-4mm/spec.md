# term-4mm · v1.6 · 4 mm² screw-clamp terminal block, feed-through / ground

**What** 4 mm² screw-clamp terminal block, feed-through / ground. Built from the Stage 0 brief `references/measure.md` (and measure-ground.md).
**Class** device · **Baseline** the 2-D drawings and page tables on file (a distributor's catalogue, not the maker's datasheet; review term-4mm-1.2.md finding 1 open; references/measure.md): feed-through block 6.0 × 44.5 × 47.0 and ground block 5.0 × 43.5 × 44.5, p. 1 (the maker and part numbers are in references/measure.md, measure-ground.md and source.txt only, OPERATING.md 6). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0; blocks stack along +x at the pitch.
**Built with** toolkit 1.3 · AutoLISP command `TERM` · `kind` (feed | ground), `conditions` ('1:corroded': clamp 1 top, 2 bottom).

## Dimensions
| item | value |
|---|---|
| feed-through | 6.0 pitch × 44.5 off the rail × 47.0 across, grey |
| ground | 5.0 pitch × 43.5 × 44.5, green with a yellow stripe, metal bonding foot |
| clamps | two per block, screw heads on the front at 8 from each end, wire entries on the top and bottom faces |
| clamp position | the wire axis 9.0 behind the block's front (`y_ax`; the screw heads then stand 0.4 proud of the drawing's 44.5 / 43.5, review term-4mm-1.3 finding 2, open) and each cage's mouth 4.25 in from its end face (the cage centre 8.0 in). **Assumption (B)**: the drawings on file dimension the envelope only and the STEP read-back gives the cages' and screw heads' sizes, not where they sit; the clamp nodes are what a panel's wires and the twin's probe land on, so the figure is read; the maker's drawing of the clamp is the source that replaces it (1.6) |
| rail foot | 3.0 × 3.0 × 41.0 under the body's centre, both kinds (the ground STEP's foot is 4.8 × 43.5 × 47.0: review term-4mm-1.3 finding 5, open). **Assumption (B)**: the foot is the rail interface, whose catch on the TH 35-7.5 rail (EN 60715, not in lib/standards/sources.csv) is a standard's figure; built as a plain bar that seats the block on the rail crown, no latch modelled (1.6) |
| inside the block | the cage pockets 6.4 deep toward the front from the wire axis, and the current bar 1.7 × 1.5 between the cages (the STEP read-back's bar is 5.2 × 1.7 × 23.4, its orientation not recorded). NOT ON FILE (C): inside the closed body, nothing of them is read by the twin, an assembly or the solver (behaviour.csv: no R for a closed path); the cages' widths 5.1 / 4.5 are the STEP read-back's (measure.md; History 1.2) (1.6) |
| strip | n × 6.0 + m × 5.0; the end stop and end cover are other parts, not modelled here: their figures NOT ON FILE (C) in this element (the end cover is its own element, term-endplate 1.0; the end stop is not built) |

## Named nodes
`clamp-1`, `clamp-2` (kind contact: clamp-screw elements, wire range on file) · `clamp-1.screw`, `clamp-2.screw` (rotate)

## Materials by layer
`M-GREY-PA` / `M-GREEN-YELLOW` + `M-YELLOW-PA` body · `M-ZINC` screws, bonding foot · `M-GASKET` openings

## Decals (Blender)
marker tags on the top face (terminal numbers from the architecture); earth symbol on the ground block

## Notes and assumptions
The vendor model's 8.0 / 7.0 widths are the rail latch; the pitch is the drawing's 6.0 / 5.0 and is what the BOM stacks. The envelopes are the drawings' (Dimensions, first two rows); every built figure the drawings do not give is on its Dimensions row with its class and reason (1.6, review term-4mm-1.3 finding 4: element.py's wire axis, cage mouth, pocket, current bar and rail foot were unmarked). A document figure replaces one as a minor version.

## Outputs (out/)
`term-4mm.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.6 | elec-r48 (2026-11-13, unattended): review term-4mm-1.3 findings 4 and 6 (carried by term-4mm-1.5 finding 1), text: element.py's unmarked figures each on a Dimensions row with its class and reason (clamp position class B, rail foot class B, the pocket and current bar class C); the Notes sentence that claimed every such figure was marked and "set from the usual norm" replaced; the two briefs' stale lines (the origin "EM to confirm", "no named nodes") say what holds now. Text only: nodes, origin, cut-outs and figures as 1.5 |
| 1.5 | elec-r38 (2026-11-12, unattended): review term-4mm-1.4 finding 3, text: the strip row's end stop and end cover carry their class, C (other parts, not modelled here; the end cover is term-endplate 1.0). Text only: nodes, origin, cut-outs and figures as 1.4 |
| 1.4 | elec-r24 (2026-11-09, unattended): review elec-r21 finding 1: BASELINE and the RANGE comment name the source's kind as it is, a distributor's catalogue (its 2-D drawings and page tables), not the maker's datasheet; review term-4mm-1.2.md finding 1 stays open (OPERATING.md 12). Text only: nodes, origin, cut-outs and figures as 1.3 |
| 1.3 | elec-r21 (2026-11-09, unattended): DOC-006 (OPERATING.md 6, EM 2026-11-05): the maker's name, the catalogue's name and the part numbers left BASELINE and this spec for references/; they say "maker's datasheet" and point to the briefs. No shape change: nodes, origin, cut-outs and figures as 1.2 |
| 1.2 | round 3 (2026-11-04): the ground block's clamps are 4.5 wide (ground STEP read-back: clamp parts 4.5 x 8.5 x 13.3): the 5.1 cage stood 0.05 proud of the 5.0 block (gate: on-envelope rejects) |
| 1.1 | the two clamps are clamp-screw elements (cage, screw, contact zone; wire range 22-10 AWG feed, 22-12 AWG ground, on file) in pockets of the body with the wire entry through the end face and screwdriver access through the front; a current bar between the cages (STEP: 5.2 x 1.7 x 23.4); ground: the metal foot shows through the back |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
