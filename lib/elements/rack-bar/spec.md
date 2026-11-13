# rack-bar · v1.1 · bar stock rack 1200 × 600 × 1270, floor tray with a 100 rim, top grid of ten cells 192 × 235, bars stood on end

**What** A bar stock rack for the steel store (lib/machines-factory.txt line 122: storage-steel places rack-cantilever,
rack-sheet-vertical, rack-bar, anchor-bolt, sign-iso7010 and floor-marking). Bars that lie flat go on rack-cantilever; this rack
is the vertical kind: bars and tubes stand on end, their feet in a floor tray with a rim, their upper ends leaning in the cells of
a top grid, one size or grade to a cell, so a bar is taken out from above without moving the others.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks rack-bar own_design
"yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the rack's footprint, x = 0, y = 0. The front, the side
a person stands at, is toward −y; the two rows of cells run along x.
**Built with** toolkit 1.3 · AutoLISP command `BARRACK` · no parameters.

## Mechanism
None: one fixed body, no node. A bar placed in the rack is the store's, not the rack's.

## What it meets (figures from files on hand)
Nothing on file: it stands on the floor and holds loose stock. Its fixing to the floor or to a wall (anchor-bolt, a separate
element on the same line of machines-factory.txt) is the assembly's, so the rack has no hole (OPERATING.md 12: a host doesn't
model holes for a part it places later).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| footprint | 1200 × 600 (x ±600, y ±300) | a design choice; two rows of five cells |
| floor tray | one solid: a floor plate 1200 × 600 × 10 (z 0 to 10) and a rim 10 thick, 100 high above it (z 10 to 110), the inside 1180 × 580 open | the bars' feet stand on the plate; the rim keeps them in the tray when they lean. One solid, not five boxes: the rim's 10 mm end edges at the corners failed the fillet gate's 90 % volume test (89 %) in the first AutoCAD run |
| corner posts | 4, 50 × 50, inside the rim's corners, from the floor plate (z 10) to z 1270 | carry the top grid |
| top grid | 3 long rails (front, middle, back) 30 wide × 50 deep (z 1220 to 1270) from post to post (x ±540); 2 side rails the same section, front post to back post (x ±540 to ±570, y ±240), the middle rail's ends abutting them; 4 dividers per row, 30 wide, between the long rails | ten cells, each 192 (x) by 235 (y) clear |
| grid height | top at 1270 | a design choice (no reach or anthropometric table is on file, so no ergonomic claim is made); a bar stands in the rack when it is longer than the grid is high |
| the bars themselves | not drawn | the store's stock, not the rack |

## Named nodes
None. Colliders: `floor`, `rim-front`, `rim-back`, `rim-left`, `rim-right`, `post-lf`, `post-rf`, `post-lb`, `post-rb`, `rail-front`,
`rail-middle`, `rail-back`, `rail-left`, `rail-right` and `divider-1` to `divider-4` (each divider's collider spans both rows), one per member, so a bar in a
cell meets the member it rests on and not an envelope.

## Materials by layer
`M-STEEL-7035` every member (painted steel, RAL 7035).

## Notes
No load rating and no stability claim: no stock's mass or lean angle is on file, so the rack is not sized against them, and
whether it needs fixing to the floor or a wall is decided where it is placed. The volume is 32 480 000 mm³ (floor tray 10 760 000, posts 4 × 3 150 000, long rails 3 × 1 620 000, side rails 2 × 720 000, dividers 8 × 352 500; written as volume only: lib/materials.csv
gives steel no density, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`rack-bar.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r69, unattended) |
| 1.1 | text only (review rack-bar-1.0 finding 1): the footprint is a design choice, two rows of five cells; the reach claim is gone; no geometry change (mech-r79, unattended) |
