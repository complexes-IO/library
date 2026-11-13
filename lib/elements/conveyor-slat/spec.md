# conveyor-slat · v1.1 · slat conveyor section, 500 between frames, 1500 long, 15 slats 90 × 490 at 100 pitch, slat tops 750, head and tail shafts, 4 × M12 anchor holes

**What** A slat conveyor, one straight section: goods ride along it on a deck of steel slats that two chains carry over a head
shaft and a tail shaft. The model shows the top run at rest (fifteen slats on two bed rails), the two shafts with their chain
wheels, the two side frames and the two supports with foot plates for floor anchors. The chains, the return run and the drive
are not drawn. lib/machines-from-elements.txt lists it in conveyor-types-bench (one section of every conveyor type), beside
conveyor-roller, whose track width, length, height and anchor pattern it shares. The shafts are the mechanism: the twin turns
them by name.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks conveyor-slat own_design
"yes": "slat conveyor section (our own build)"). No product was matched and no vendor file was opened. The holes it meets are
on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the section, x = 0 midway between the side frames,
y = 0 midway along its length. Goods travel along y toward +y, the head end; the slats' tops are at z 750, the shafts' axes run
along x at z 660. Extents x ±375, y ±750, z 0 to 750.
**Built with** toolkit 1.3 · AutoLISP command `CONVSLAT` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the foot plates at 680 × 1000 (x ±340, y ±500) | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice, the same pattern as conveyor-roller 1.0's. The anchors (anchor-bolt, not built yet) are the assembly's; nothing is placed in the holes |
| floor | the foot plates' undersides, z = 0 | a flat floor; the floor is the assembly's |
| the next section | the section's end faces, y ±750: the side frames' ends; the track 500 wide between the frames and its top at z 750, as conveyor-roller 1.0's | element:conveyor-roller 1.0 (W, L, TOP). No joining plate or hole is drawn: how sections are joined is the assembly's |
| the drive | the head shaft, node `shaft-head`, Ø40, its end faces at x ±245 inside the side frames | none on file: no gearmotor or reducer is placed and no shaft end, key or bore is drawn. What turns the shaft, and how it joins it, is the assembly's and a later version's |
| the goods | the slats' tops, z = 750, 10 above the side frames' tops (z 740) | none on file: goods up to 500 wide run between the frames' lines, wider ones pass over the frames |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane midway between the
side frames) and C (the plane midway along the section) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| side frames | 2, section 50 (x) × 160 (z), 1500 long, drawn by their outside; inner faces at x ±250, z 580 to 740 | stand either side of the deck and the shafts; their tops 10 below the slats' tops |
| slats | 15, each 90 (y) × 490 (x −245 to 245) × 20 (z 730 to 750), drawn by their outside, centres at y −700 to 700 in steps of 100 | 10 between neighbouring slats; the end slats' centres half a pitch (50) from the section's ends; 5 clear of each side frame |
| bed rails | 2, 50 (x, centres ±125) × 40 (z 690 to 730), 1480 long (y ±740) | every slat of the top run rests on them; their ends stand 5 inside the end slats' outer edges and 10 inside the section's ends; they pass 10 above the shafts and 35 inside the chain wheels |
| cross members | 2, 500 long (x ±250) × 50 (y) × 40 (z 650 to 690), frame to frame at y −500 and +500 | carry the bed rails; hold the frames to the track's width |
| shafts | 2, Ø40 × 490 (x −245 to 245), axes at z 660, at y +650 (head) and −650 (tail) | 100 from the section's ends; 5 clear of each side frame (the bearings are not drawn) |
| chain wheels | 2 on each shaft, Ø120 × 30, centres x ±200, plain discs | where the two chains (not drawn) would run; their tops (z 720) 10 below the slats' undersides; their inner faces (x ±185) 35 outside the bed rails |
| supports | 2, at y −500 and +500: each two posts, a lower tie and two foot plates | 1000 apart, 250 from each end; conveyor-roller's |
| posts | 4, 50 × 50, drawn by their outside, z 20 to 580, under the side frames (x 250 to 300 each side) | each stands on its foot plate and carries a frame |
| lower ties | 2, 500 × 50 × 50 (z 150 to 200), post to post | stiffen each support |
| foot plates | 4, 150 (x 225 to 375 each side) × 100 (y) × 20 (z 0 to 20), one under each post, running outward; one Ø13.5 hole in each, 40 outside the post's outer face and 35 from the plate's outer edge | fix the section to the floor; 20 thick |
| the goods | not drawn | the system's, not the conveyor's |

## Mechanism
Two shafts, nodes `shaft-head` (y +650) and `shaft-tail` (y −650), each with its two chain wheels, rotating about its own axis
(along x), 0 to 360 degrees: a spin, with no stop. In the machine the drive turns the head shaft, the chain wheels pull the two
chains and the slats ride with them along the top run, round the head wheels, back underneath and round the tail wheels. The
model draws the top run only, at rest, as part of the fixed body: the slats do not move in the twin; the shafts do. Each shaft
stands 5 clear of the side frames, its wheels 10 below the slats, 35 outside the bed rails and 65 from the cross members (y 590 to their faces at 525), the shaft itself 10 below the rails and 105 from the cross members, so
a shaft touches nothing at rest or as it turns. behaviour.csv: state `still` (default) and `running` (manual toggle: the drive
is the assembly's), pose of both shafts at the range end in `running`.

## Named nodes
`shaft-head`, `shaft-tail`: rotate about x through their axes, range 0 to 360 degrees. Colliders: `frame-l`, `frame-r`, `post-la`,
`post-lb`, `post-ra`, `post-rb`, `foot-la`, `foot-lb`, `foot-ra`, `foot-rb` (l / r the −x / +x side, a / b the −y / +y support),
`rail-l`, `rail-r`, `cross-a`, `cross-b`, `tie-lo-a`, `tie-lo-b`, and `slat-deck` (the box around the fifteen slats, x ±245,
y ±745, z 730 to 750: what goods ride on; none is named like a node).

## Materials by layer
`M-STEEL-7035` the side frames, posts, ties, cross members, bed rails and foot plates (painted steel, RAL 7035) · `M-ZINC` the
slats, the shafts and the chain wheels (steel, zinc-plated).

## Decals (Blender)
"complexes.org" on the +x side frame's outer face.

## Notes
No vendor names, part numbers or marks. No load rating, no speed figure and no safety claim: no goods' mass is on file, no
calculation or test of the model is on file, and the conveyor is not sized against a load. Not drawn: the chains and their
attachments to the slats, the return run and its supports, the wheels' teeth, the bearings, the drive (motor, reducer, the
shaft's drive end), chain tensioning at the tail, side guides, guards over the shaft ends and the return run, joining plates
between sections, height adjustment. The anchor holes are on file; the anchors are the assembly's.

## Outputs (out/)
`conveyor-slat.lsp` · `.glb` (pivots on the two shafts) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r90, unattended, 2026-11-11) |
| 1.1 | review conveyor-slat-1.0 note 2, text only, no figure or geometry changed: Mechanism gives the chain wheels 65 from the cross members (y 590 to their faces at 525) and the bare shaft 105 from them (it gave the shaft the wheels' 65) (mech-r111, unattended, 2026-11-12) |
