# conveyor-wheel · v1.1 · wheel conveyor, generic, gravity, 500 between frames, 1500 long, 38 skate wheels Ø50 on 15 lines at 100 pitch, wheel tops 750, 4 × M12 anchor holes

**What** A skate-wheel gravity conveyor, one straight section: cartons, totes and trays with a flat, firm base ride along it on a
bed of small free wheels, pushed by hand, by the goods behind them or by a slope the assembly gives the section. Nothing in it is
driven. Fifteen axle lines cross the track between two side frames; three wheels sit on each odd line and two on each even line,
staggered, so goods ride on five wheel tracks and a wheel conveyor stays lighter than a roller one for the same track. The frames
stand on two supports with foot plates for floor anchors. lib/machines-from-elements.txt lists it in conveyor-types-bench, beside
conveyor-roller and the rest of the family. The wheels are the mechanism: the twin turns them by name.
**Class** furniture · **Baseline** our own design: generic wheel conveyor (ETIM 10.0 EC004417), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07); lib/inventory.csv marks the row own_design "generic" (request mech-9's answer, item 3: the row's
`etim` cell and the class's features come with the attended ETIM push). No product was matched and no vendor file was opened; the
element had no folder or record before this build. The class values below are the design inputs; the holes it meets are on file
(ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the section, x = 0 midway between the side frames,
y = 0 midway along its length. Goods travel along y; the wheels' axes run along x at z 725, their tops at z 750. Extents
x ±375, y ±750, z 0 to 750: the same frame as conveyor-roller 1.0, so sections of the two line up end to end.
**Built with** toolkit 1.3 · AutoLISP command `CONVWHEEL` · no parameters.

## Class values (ETIM 10.0 EC004417)
Design inputs. EC004417 Wheel conveyor (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, 11 features)
is a tier-2 class whose features lib/standards/etim/class-features.csv does not list (the tier-1 classes and the classes the
inventory uses), and none is written from memory. Request mech-9's answer (item 3) puts the row's class and its features in the
same attended push as rack-cantilever's and shelving-steel's. Until then this table gives the values the conveyor is designed to
under plain names, as rack-cantilever 1.0 does; the next minor version restates them in ETIM's order with their EF codes, "not
stated" where the design has no value.

| value | this element |
|---|---|
| width between the side frames | 500 mm (inner faces; the wheel bed 325 wide, x ±162.5) |
| total length | 1500 mm |
| height | 750 mm, the floor to the wheels' tops; one height, not adjustable |
| axle lines | 15, at 100 pitch, the end lines 50 inside the section's ends |
| wheels per line | 3 on the odd lines (x −150, 0, 150), 2 on the even lines (x −75, 75): 38 wheels, five wheel tracks |
| wheel diameter | 50 mm |
| wheel width | 25 mm |
| wheel material | steel, zinc-plated (layer M-ZINC) |
| frame material | steel |
| surface treatment, frame | painted (RAL 7035) |
| load per wheel, load per metre | not stated: no load is designed or claimed |

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the foot plates at 680 × 1000 (x ±340, y ±500) | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice, conveyor-roller 1.0's pattern. The anchors (anchor-bolt, not built yet) are the assembly's; nothing is placed in the holes |
| floor | the foot plates' undersides, z = 0 | a flat floor; the floor is the assembly's |
| the next section | the section's end faces, y ±750: the side frames' ends, with the end lines' axes 50 inside them | sections of this element placed end to end keep the 100 pitch across the joint; a conveyor-roller 1.0 section (the same track and height) carries on from either end. No joining plate or hole is drawn: how sections are joined is the assembly's |
| the goods | the wheels' tops, z = 750, 10 above the side frames' tops (z 740) | none on file: goods ride on the five wheel tracks (x ±162.5); a carton narrower than 150 rides on one track and may tip; goods shorter than 200 along y rest on fewer than two lines. A wheel conveyor wants a flat, firm base (a carton, a tote, a tray): soft or open bases are the roller conveyor's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane midway between the
side frames) and C (the plane midway along the section) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| side frames | 2, section 50 (x) × 80 (z), 1500 long, drawn by their outside; inner faces at x ±250, z 660 to 740 | conveyor-roller 1.0's frames: carry the axles (not drawn); their tops 10 below the wheels' tops |
| wheels | 38, Ø50 × 25 wide, axes at z 725; line i at y −700 + 100 (i − 1); three at x −150, 0, 150 on the odd lines, two at x −75, 75 on the even ones | 150 clear between neighbours along a track (the same x, two lines and 200 apart); 50 clear along y between a wheel and the next line's, which sit on another track; the end lines 50 inside the section's ends |
| supports | 2, at y −500 and +500: each two posts, an upper and a lower tie and two foot plates | 1000 apart, 250 from each end (conveyor-roller 1.0's) |
| posts | 4, 50 × 50, drawn by their outside, z 20 to 660, under the side frames (x 250 to 300 each side) | each stands on its foot plate and carries a frame |
| upper ties | 2, 500 long (x ±250) × 50 (y) × 40 (z 600 to 640), post to post | hold the posts to the track's width; 60 clear below the wheels' undersides (z 700) |
| lower ties | 2, 500 × 50 × 50 (z 150 to 200), post to post | stiffen each support |
| foot plates | 4, 150 (x 225 to 375 each side) × 100 (y) × 20 (z 0 to 20), one under each post, running outward; one Ø13.5 hole in each, 40 outside the post's outer face and 35 from the plate's outer edge | fix the section to the floor; 20 thick |
| the goods | not drawn | the system's, not the conveyor's |

## Mechanism
Thirty-eight free skate wheels, nodes `wheel-<line>-<k>` (line 1 at the −y end, y −700; line 15 at the +y end, y 700; k counts
from −x: 1 to 3 on an odd line, 1 to 2 on an even one), each rotating about its own axis (along x), 0 to 360 degrees: a spin, with
no stop. Goods moving along the track turn the wheels under them. The axles and their bearings are not drawn: a wheel's end faces
stand 87.5 (odd lines) or 162.5 (even lines) clear of the side frames, 150 clear of the next wheel on its track (50 along y from the next line's, on another track) and 60 above the
upper ties, so a wheel touches nothing at rest or as it turns. The section is level in its own frame; a slope, if the system wants
one, is the assembly's placement. behaviour.csv: state `still` (default) and `turning` (manual toggle, the goods' passage), pose of
the thirty-eight wheels at the range end in `turning`.

## Named nodes
`wheel-1-1` to `wheel-15-3` (38): rotate about x through their axes, range 0 to 360 degrees. Colliders: `frame-l`, `frame-r`,
`post-la`, `post-lb`, `post-ra`, `post-rb`, `foot-la`, `foot-lb`, `foot-ra`, `foot-rb` (l / r the −x / +x side, a / b the −y / +y
support), `tie-up-a`, `tie-up-b`, `tie-lo-a`, `tie-lo-b`, and `wheel-bed` (the box around the wheels, x ±162.5, y ±750, z 700 to
750: what goods ride on; none is named like a node).

## Materials by layer
`M-STEEL-7035` the side frames, posts, ties and foot plates (painted steel, RAL 7035) · `M-ZINC` the wheels (steel, zinc-plated).

## Decals (Blender)
"complexes.org generic" on the +x side frame's outer face.

## Notes
No vendor names, part numbers or marks. No load rating, no speed or slope figure and no safety claim: no goods' mass is on file,
no calculation or test of the model is on file, and the conveyor is not sized against a load. The class values are the figures
this design is meant to meet. Not drawn: the axles and bearings, wheel hubs and flanges, side guides, end stops, joining plates
between sections, height adjustment. The anchor holes are on file; the anchors are the assembly's.

## Outputs (out/)
`conveyor-wheel.lsp` · `.glb` (pivots on the thirty-eight wheels) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004417), our own design (mech-r96, unattended, 2026-11-11) |
| 1.1 | review conveyor-wheel-1.0 note, text only, no figure changed: Its own sizes (wheels) and Mechanism give 150 clear between neighbours along a track (200 apart), the 50 being the y gap to the next line's wheels on another track; element.py's NL / PITCH comment calls the 15 lines at 100 pitch class values, as the Class values table does (mech-r110, unattended, 2026-11-12) |
