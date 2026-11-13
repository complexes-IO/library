# conveyor-roller · v1.1 · roller conveyor, generic, gravity, 500 between frames, 1500 long, 20 rollers Ø50 at 75 pitch, roller tops 750, 4 × M12 anchor holes

**What** A gravity roller conveyor, one straight section: cartons, totes and trays ride along it on a bed of free rollers,
pushed by hand, by the goods behind them or by a slope the assembly gives the section. Nothing in it is driven. Two side frames
carry twenty rollers across the track; the frames stand on two supports with foot plates for floor anchors. The systems of
lib/machines-from-elements.txt that list it (inbound-conveyor, sorting-line, conveyor-types-bench) place it beside the driven
conveyor-seg. The rollers are the mechanism: the twin turns them by name.
**Class** furniture · **Baseline** our own design: generic roller conveyor (ETIM 10.0 EC004418), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07); lib/inventory.csv marks the row own_design "generic", etim EC004418. No product was matched and no
vendor file was opened. The element's folder came with a catalogue record (references/source.txt); none of its sizes is used
here. The class values below are the design inputs; the holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the section, x = 0 midway between the side frames,
y = 0 midway along its length. Goods travel along y; the rollers' axes run along x at z 725, their tops at z 750. Extents
x ±375, y ±750, z 0 to 750.
**Built with** toolkit 1.3 · AutoLISP command `CONVROLLER` · no parameters.

## Class values
ETIM 10.0 class EC004418 Roller conveyor (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Width (effective dimension) (EF011644) | 500 mm: between the side frames' inner faces (the rollers 490 long, 5 clear of each frame) |
| 2 | Total length (EF000369) | 1500 mm |
| 3 | Height (EF005454) | 750 to 750 mm: the rollers' tops above the floor; the supports are one height, not adjustable |
| 4 | Number of axles (EF015134) | 20 |
| 5 | Type of axle (EF012860) | a fixed axle through each roller, held in the side frames; not drawn |
| 6 | Type of carrier rollers (EF015132) | plain cylindrical tube rollers, free-running (gravity; not driven) |
| 7 | Diameter rollers (EF015135) | 50 mm |
| 8 | Material carrier rollers (EF015133) | steel, zinc-plated |
| 9 | Frame material (EF021453) | steel |
| 10 | Surface treatment frame (EF024699) | painted (RAL 7035) |

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the foot plates at 680 × 1000 (x ±340, y ±500) | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice. The anchors (anchor-bolt, not built yet) are the assembly's; nothing is placed in the holes |
| floor | the foot plates' undersides, z = 0 | a flat floor; the floor is the assembly's |
| the next section | the section's end faces, y ±750: the side frames' ends, with the end rollers' axes 37.5 inside them | sections of this element placed end to end keep the 75 pitch across the joint. No joining plate or hole is drawn: how sections are joined is the assembly's |
| the goods | the rollers' tops, z = 750, 10 above the side frames' tops (z 740) | none on file: goods up to 500 wide run between the frames' lines, wider ones pass over the frames. By the pitch alone, goods shorter than 225 along y rest on fewer than three rollers |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane midway between the
side frames) and C (the plane midway along the section) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| side frames | 2, section 50 (x) × 80 (z), 1500 long, drawn by their outside; inner faces at x ±250, z 660 to 740 | carry the rollers' axles (not drawn); their tops 10 below the rollers' tops |
| rollers | 20, Ø50 × 490 (x −245 to 245), axes at z 725, at y −712.5 to 712.5 in steps of 75 | 25 clear between neighbouring rollers; the end rollers' axes half a pitch (37.5) from the section's ends |
| supports | 2, at y −500 and +500: each two posts, an upper and a lower tie and two foot plates | 1000 apart, 250 from each end |
| posts | 4, 50 × 50, drawn by their outside, z 20 to 660, under the side frames (x 250 to 300 each side) | each stands on its foot plate and carries a frame; their faces in line with the frames' |
| upper ties | 2, 500 long (x ±250) × 50 (y) × 40 (z 600 to 640), post to post | hold the posts to the track's width; 60 clear below the rollers' undersides (z 700) |
| lower ties | 2, 500 × 50 × 50 (z 150 to 200), post to post | stiffen each support |
| foot plates | 4, 150 (x 225 to 375 each side) × 100 (y) × 20 (z 0 to 20), one under each post, running outward; one Ø13.5 hole in each, 40 outside the post's outer face and 35 from the plate's outer edge | fix the section to the floor; 20 thick |
| the goods | not drawn | the system's, not the conveyor's |

## Mechanism
Twenty free rollers, nodes `roller-1` to `roller-20` (1 at the −y end, y −712.5; 20 at the +y end, y 712.5), each rotating about
its own axis (along x), 0 to 360 degrees: a spin, with no stop. Goods moving along the track turn the rollers under them. The
axles and their bearings are not drawn: each roller's end faces stand 5 clear of the side frames, 25 clear of the next roller and
60 above the upper ties, so a roller touches nothing at rest or as it turns. The section is level in its own frame; a slope, if
the system wants one, is the assembly's placement. behaviour.csv: state `still` (default) and `turning` (manual toggle, the
goods' passage), pose of the twenty rollers at the range end in `turning`.

## Named nodes
`roller-1` to `roller-20`: rotate about x through their axes, range 0 to 360 degrees. Colliders: `frame-l`, `frame-r`, `post-la`,
`post-lb`, `post-ra`, `post-rb`, `foot-la`, `foot-lb`, `foot-ra`, `foot-rb` (l / r the −x / +x side, a / b the −y / +y support),
`tie-up-a`, `tie-up-b`, `tie-lo-a`, `tie-lo-b`, and `roll-bed` (the box around the twenty rollers, x ±245, y ±750, z 700 to 750:
what goods ride on; none is named like a node).

## Materials by layer
`M-STEEL-7035` the side frames, posts, ties and foot plates (painted steel, RAL 7035) · `M-ZINC` the rollers (steel,
zinc-plated).

## Decals (Blender)
"complexes.org generic" on the +x side frame's outer face.

## Notes
No vendor names, part numbers or marks. No load rating, no speed or slope figure and no safety claim: no goods' mass is on file,
no calculation or test of the model is on file, and the conveyor is not sized against a load. The class values are the figures
this design is meant to meet. Not drawn: the axles and bearings, side guides, end stops, joining plates between sections, height
adjustment. The anchor holes are on file; the anchors are the assembly's.

## Outputs (out/)
`conveyor-roller.lsp` · `.glb` (pivots on the twenty rollers) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004418), our own design (mech-r88, unattended, 2026-11-10) |
| 1.1 | review conveyor-roller-1.0 note 1, text only, no figure or geometry changed: element.py's TIE_UP comment gives the upper tie's top at z 640, 60 below the rollers' undersides at z 700, as Its own sizes says (it read 40) (mech-r111, unattended, 2026-11-12) |
