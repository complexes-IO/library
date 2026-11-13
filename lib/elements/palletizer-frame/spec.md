# palletizer-frame · v1.1 · robot palletizing cell frame, own design, four posts 3300 × 2700 × 2500 with a top frame, floor ties, pallet back stop and side guides sized to pallet 1.2, 16 × M12 anchor holes

**What** The frame of a robot palletizing cell. Four posts on anchored foot plates, tied at the top by a frame, stand around a floor
area 2900 × 2300 between them. The cell's −x half is the robot's: the infeed conveyor brings the goods in through the open −x end and
the robot stands between it and the pallet. The +x half is the pallet station: an empty pallet is set down against a back stop and
between two side guides, loaded, and taken out through the open +x end along x. Two floor ties along the cell's long sides join the
foot plates and carry the stop and the guides, so the whole frame is one body on the floor. It is the conveyor family's palletizer
frame (lib/inventory.csv row palletizer-frame, "palletizer gantry frame around robot-arm (our own build)", EM 2026-11-08: the conveyor
family); no system row names it yet.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks palletizer-frame own_design
"yes"; the folder's record, references/source.txt, says "own build, no vendor search", nothing downloaded). No product was matched
and no vendor file was opened. The pallet's footprint is read from pallet 1.2 with library.load, so the stop and the guides cannot
drift from it; the anchor holes are ISO 273's; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the cell between the four posts. x along the flow, from the
infeed end (−x, the robot's half) to the pallet end (+x); y across it. Extents x −1650 to 1650 and y −1350 to 1350 (the foot plates),
z 0 to 2500 (the top frame).
**Built with** toolkit 1.3 · AutoLISP command `PALLETIZERFRAME` · no parameters.

## Mechanism
None: one fixed body, no named moving node. The robot, the conveyor and the light curtains that move or sense in the cell are their
own elements.
Not drawn, placed in a later version once their elements are on file (OPERATING.md 12: a host doesn't model holes for a part it
places later): the robot (robot-arm is not built) and its pedestal, the infeed conveyor section (conveyor-seg), the guard panels on
the long sides, the light curtain or safety scanner at the two open ends, and the controls. The frame's −x half is left clear of
every solid above the floor for them.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| pallet footprint | 1219 × 1016, its centre at x 700, y 0 (x 90.5 to 1309.5, y ±508); the back stop's face at x 80.5 and the side guides' faces at y ±518, each 10 clear of it | pallet 1.2 (library.load: LX, LY). **Assumption (B)**, inherited: pallet 1.2 marks its footprint so (ISO 6780 not on file; lib/inventory.csv names the size). Closed with the pallet's: when ISO 6780 is on file and the pallet's figure changes, the stop and guides follow it through library.load, a version here if they no longer fit |
| the floor | 16 × Ø13.5 holes, 4 in each foot plate at 220 × 220 about the post's centre (x ±1500 ± 110, y ±1200 ± 110) | M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv); position Ø1.0 at MMC to A the floor plane, B the plane x 0, C the plane y 0 (ASME Y14.5 floating fastener, T ≤ H − F = 1.50; features.csv). The anchors are the assembly's |
| the robot and the infeed conveyor | none in this element | robot-arm (not built) and conveyor-seg come with their elements, placed in a later version (OPERATING.md 12: a host doesn't model holes for a part it places later) |
| the guarding | none in this element | the guards, light curtains and their interlocks around a robot cell are the assembly's elements, with their safety sign-off (ISO 10218-2, ISO 13857 and ISO 14120 are not in lib/standards/sources.csv); this element claims nothing for them |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| foot plates | 4, 300 × 300 × 20 (x ±1350 to ±1650, y ±1050 to ±1350, z 0 to 20), 4 × Ø13.5 each at 220 × 220 | each post's footprint on the floor; the holes 40 from the plate's edges |
| posts | 4, 100 × 100 on centres x ±1500, y ±1200 (x ±1450 to ±1550, y ±1150 to ±1250), z 20 to 2400, drawn solid by their outside | 2900 clear along x and 2300 across between them, for a robot beside a 1219 × 1016 pallet; a hollow section's wall is a later version's |
| top frame | two beams 3100 × 100 × 100 along x over the posts (y ±1150 to ±1250), two 100 × 2300 × 100 along y between them (x ±1450 to ±1550); z 2400 to 2500 | ties the posts at the top; 2400 clear under it for a stacked pallet and the robot's reach over it |
| floor ties | 2, 2700 × 100 × 20 along x (x −1350 to 1350, y ±1150 to ±1250, z 0 to 20), foot plate to foot plate | join the four posts at the floor and carry the stop and the guides, so the frame is one body (GEO-070); on the long sides, out of the pallet's and the conveyor's paths |
| back stop | a floor bar 80 × 2300 × 20 across the cell (x 0.5 to 80.5, y −1150 to 1150, z 0 to 20), tie to tie, with an upright 20 × 1200 × 100 at its face (x 60.5 to 80.5, y ±600, z 20 to 120) | the pallet is set down against it; 10 behind the pallet's −x end so it goes down clear; the upright stops the pallet's bottom boards and blocks, not its load |
| side guides | 2, a floor plate 600 × 632 × 20 (x 400 to 1000, y ±518 to ±1150, z 0 to 20) from the pallet's side to the tie, with an upright 600 × 20 × 100 at its inner edge (y ±518 to ±538, z 20 to 120) | centre the pallet across the cell, 10 clear each side; 600 long under the middle of the pallet's sides, open at both ends so a fork truck sets it down and takes it out along x |
| finish | posts, frame and ties painted RAL 7035; stop and guides yellow | a design choice: the parts a pallet meets at floor level in a signal colour (an appearance, not a safety marking) |

## Named nodes
None. Colliders `post-1` to `post-4` (the posts with their foot plates' height, z 0 to 2400), `top` (the top frame as one box),
`tie-1`, `tie-2` (the floor ties), `stop` (the back stop's bar and upright as one box), `guide-1`, `guide-2` (each side guide as one
box).

## Materials by layer
`M-STEEL-7035` the foot plates, posts, top frame and floor ties (painted RAL 7035) · `M-YELLOW` the back stop and the two side
guides.

## Notes
No load rating, no reach, no cycle time and no safety claim: no robot, no goods' mass and no palletizer standard are on file, so the
frame is not sized against them; the cell's guarding and its safety functions are its assembly's. The volume is 244 802 196 mm³ (foot
plates 4 × 1 800 000, posts 4 × 23 800 000, top frame 2 × 31 000 000 + 2 × 23 000 000, floor ties 2 × 5 400 000, back stop
3 680 000 + 2 400 000, side guides 2 × (7 584 000 + 1 200 000), less sixteen holes 45 804; written as volume only: lib/materials.csv
gives no densities, so no mass is stated). No vendor names, no label. The gate's fillet radius is set per primitive (0.5, `P.radii`;
mech-r106): every free-corner edge is 20 or longer.

## Outputs (out/)
`palletizer-frame.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r116, unattended) |
| 1.1 | review mech-r116 finding 1, text only: the pallet it reads is cited as pallet 1.2 (main's, since mech-r20's review), not 1.1, in element.py's docstring, TITLE, BASELINE and the PAL comment and in this spec; the footprint LX 1219 × LY 1016 is the same in both, so no figure, node, origin or cut-out changes (mech-r128, unattended, 2026-11-12) |
