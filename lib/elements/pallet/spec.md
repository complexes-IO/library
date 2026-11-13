# pallet · v1.2 · four-way block pallet 1219 × 1016 × 144

**What** Block pallet: nine blocks between three bottom boards and three stringer boards, seven deck boards on top. Four-way for
a forklift; a pallet truck enters from the two y sides only (the bottom boards cross the x entries: a "partial four-way" pallet).
The load carrier of the AMR dock, outbound conveyor, pallet rack bay and robot tending cell (lib/inventory.csv).
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). The footprint is the one
interface the rack, conveyor and AMR dock meet, so it is a fit and open (class B, EM's) until ISO 6780 is on file
(lib/standards/sources.csv iso-6780, "to get"); lib/inventory.csv only names the size. No vendor file was opened. The folder's
acquisition record (metadata.json, validation.json, batch 20) describes a catalogue product; this element is not built from it.
**Units / frame** mm, Z up. Origin: floor plane z = 0 at the footprint corner x = 0, y = 0; the 1219 length along +x, the 1016
width along +y.
**Built with** toolkit 1.3 · AutoLISP command `PALLET` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| footprint | 1219 × 1016 (1219 along +x, the stringer boards' direction) | **Assumption (B)** (a fit: pallet-rack, and later the conveyor and AMR dock, are sized from it). The size lib/inventory.csv names; ISO 6780 fixes pallet footprints and their tolerances, but its text is not on file, so no clause, no tolerance and no length/width convention is taken from it. Closed when ISO 6780 is on file: cite its clause and table, check which side it calls the length, a minor version if it differs |
| fork fit (forklift fork arms, pallet-truck forks and load wheels) | the openings below | **NOT ON FILE (B)**: no fork or pallet-truck standard or element is on file (ISO 2331, fork arms, is the one to look at; whether it carries the figures needed is not known here). The openings are design choices; that a given fork fits them is not claimed |
| the rack beams and conveyor rollers it rests on | none yet | pallet-rack is built from this pallet's footprint; the conveyor and AMR elements are not built |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| overall height | 144 | 18 bottom boards + 86 blocks + 20 stringer boards + 20 deck boards |
| blocks | 9, 145 × 145 × 86, 3 × 3 flush with the edges | entry from all four sides |
| fork openings, entry along y | 392 wide (between block columns), 104 high from the floor (between two bottom boards, up to the stringer boards) | forklift or pallet truck: the forks and load wheels run on the floor between the bottom boards |
| fork openings, entry along x | 290.5 wide (between block rows), 106 high above the bottom boards (z 18 to the deck boards' underside at z 124; the stringer boards lie only over the block rows) | forklift only: the forks cross the 18 high perimeter bottom board, and a pallet truck's load wheels would land on the far bottom board |
| bottom boards | 3, 145 wide, along y under each block column | |
| stringer boards | 3, 145 wide, along x over each block row | |
| deck boards | 7, 120 wide, along y across the stringer boards, gaps 63.2 | |
| material | wood (brown) | |

## Named nodes
none (nothing moves). Colliders: `deck` (the deck boards, z 124 to 144, over the whole footprint), each stringer board
`stringer-<y>` (z 104 to 124, over its block row), each block `block-<x>-<y>`, each bottom board `base-<x>`, so a fork can enter
the openings in the twin at the part's own heights (104 along y, 106 above the bottom boards along x).

## Materials by layer
`M-BROWN` every board and block.

## Notes
No load rating and no safety claim. Two open figures, both class B and EM's: the footprint and the fork fit (What it meets).
The rest are design choices.

## Outputs (out/)
`pallet.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r4) |
| 1.1 | review pallet-1.0 findings 1 and 2 (mech-r20): the footprint marked as an open figure, class B (inventory.csv is a build list, ISO 6780 not on file); the fork-entry claim corrected (forklift from four sides, pallet truck from the two y sides), the two opening heights given (104 from the floor along y, 86 above the bottom boards along x), the fork fit marked open, class B; "no open figure" withdrawn. Text only: the part, colliders, origin and previews are 1.0's |
| 1.2 | review pallet-1.1 finding 1 (lib/reviews/mech/r20.md): the x-entry height is 106 above the bottom boards, not 86 (86 was the one `deck` collider's, z 104 to 144). The collider split as the review's option (a): three `stringer-<y>` colliders (z 104 to 124) and `deck` (z 124 to 144), so the twin's opening is the part's. The solids, origin and cut-outs unchanged; colliders 13 → 16, a minor (no assembly places pallet; mech-r29, unattended) |
