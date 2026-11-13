# turntable · v1.1 · rotary conveyor turntable, round deck Ø900 turning about z on a slewing ring, roller track 500 between frames, 660 long, 6 rollers Ø50 at 100 pitch, roller tops 750, side guides to 760, base frame on floor rails with 4 × M12 anchor holes

**What** A rotary conveyor turntable: a short roller track on a round deck that turns about a vertical axis, so goods arriving
along one conveyor line leave along another (a turn in the line, a diverter between lines, or a reversal). The model shows the
deck (a round plate carrying the track's two side frames and six free rollers), the fixed race of the slewing ring it rests on,
a square base frame of four posts and four top beams that carries the ring, two lower ties, and two floor rails under the posts
that carry the anchor holes. The ring's rotating race, balls and gear, the deck's drive, the rollers' axles and bearings, stops
and sensors are not drawn.
lib/machines-from-elements.txt lists it in conveyor-types-bench (one section of every conveyor type), beside conveyor-roller,
conveyor-slat, conveyor-mattop and conveyor-incline, whose track width, track height and anchor-hole pattern it shares, so a
horizontal section can feed the deck and another take from it. The deck and the rollers are the mechanism: the twin turns them
by name.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks turntable own_design
"yes": "rotary conveyor turntable (our own build: slewing ring, roller deck, gearmotor)"). No product was matched: the folder's
record (references/source.txt) is a search that found no conveyor turntable with CAD at the approved vendors, and nothing in it
is used. No vendor file was opened. The holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 on the deck's axis of rotation, x = 0, y = 0 at the centre of the
base's plan. At rest the track runs along y between the side frames (x ±250), the rollers' axes along x at z 725 and their tops
at z 750; the deck turns about z. Extents x ±475, y ±500 (the floor rails), z 0 to 760 (the side frames' tops).
**Built with** toolkit 1.3 · AutoLISP command `TURNTABLE` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the floor rails at 880 × 750 (x ±440, y ±375), one beside each post | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice, the pattern of conveyor-roller 1.0's foot plates (680 across; here 880 across and 750 apart). The anchors (anchor-bolt, not built yet) are the assembly's; nothing is placed in the holes |
| floor | the floor rails' undersides, z = 0 | a flat floor; the floor is the assembly's |
| the sections before and after it | the track: 500 between the side frames' inner faces, the rollers' tops at z 750, at both ends of the deck (y ±330 at rest); the frames' tops at 760 are side guides, 20 above a horizontal section's frame tops (740) | element:conveyor-roller 1.0 (W, TOP): a horizontal section's track is 500 wide with its roller tops at z 750, so goods pass from it onto the deck and off again; goods must be under 500 wide to enter between the deck's guides. The gap between a section's end and the deck's edge (the deck's plate reaches r 450, the frames' ends y ±330 at rest) and any transfer plate are the assembly's |
| the drive | none placed: the deck is node `deck`, turning about z on the slewing ring; no gearmotor, pinion or gear ring is drawn | none on file: the inventory row names a gearmotor, but motor-iec71-370w is not past station 6 (OPERATING.md 12, quality at the source: a host places only common parts past station 6), and no gearmotor element is on file. What turns the deck, and where it mounts on the base, is a later version's and the assembly's |
| the slewing ring | its fixed race, a disc Ø760 × 40 on the base plate, the deck plate resting on its top face | none on file: no slewing-ring standard or product is on file; the race is this design's plain disc and its rotating race, balls, seals and gear are not drawn |
| the goods | the rollers' tops, between the side frames, which stand 10 above them as side guides | none on file: goods under 500 wide ride the rollers between the guides; what they weigh and how fast they move are the system's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane x = 0 through the
deck's axis) and C (the plane y = 0 through the deck's axis) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| plan | floor rails 1000 long (y ±500), 150 wide (x 325 to 475 each side); the base frame's posts at x, y ±375 | a square base one third shorter than the family's 1500 sections: the deck needs only its own diameter and the sections before and after it butt against its edge. The rails run the posts' full length and 100 past them, so they, not the round deck, are the x and y extremes (see Notes) |
| deck plate | Ø900 (r 450) × 15 (z 600 to 615), on the race's top face | round, so it turns inside a fixed guard or between the sections' ends; its edge stays 25 inside the rails' outer edges (x) and 50 inside their ends (y) |
| track | two side frames 50 (x) × 145 (z) × 660 (y ±330), inner faces x ±250, standing on the deck plate (z 615 to 760) | the family's 500 between frames; 660 long so each frame's corner (r 446.0 from the axis, √(300² + 330²)) stays inside the deck's edge; their tops 10 above the rollers' tops (unlike conveyor-roller's, 10 below): on a deck that turns they are side guides that keep the goods on the rollers, and they put the model's z extreme on an axis-aligned solid of a top-level node (Notes) |
| rollers | 6, Ø50 × 490 (x ±245), axes along x at z 725, at y −250, −150, −50, 50, 150, 250 (100 pitch); the end rollers 80 from the frames' ends | the family's roller size and track height; six at 100 pitch carry goods 200 and longer across the deck; each roller's end faces 5 clear of the side frames (the axles and bearings are not drawn) |
| slewing ring's fixed race | a disc Ø760 (r 380) × 40 (z 560 to 600), on the base plate, on the deck's axis | 70 inside the deck's edge, 30 past the base frame's beams; a plain disc stands for the ring's fixed race, its gear and balls not drawn |
| base plate | 820 × 820 × 15 (z 545 to 560), on the top frame beams | carries the race; 10 past the beams' outer faces (x, y ±400) so no face is flush with them |
| top frame | 4 beams 50 × 50 (z 495 to 545): two along y (x 350 to 400 each side, y ±400) over each side's posts, two along x (y 350 to 400 each side, x ±350) between them | a square frame on the posts, under the plate |
| posts | 4, 50 × 50, drawn by their outside, at x, y ±375 (faces 350 and 400), from the rail's top (z 20) to the beams' undersides (z 495): 475 tall | each stands on a floor rail and carries the top frame |
| lower ties | 2, 700 × 50 × 50 (z 150 to 200), post to post along x at y ±375 | stiffen each pair of posts |
| the goods | not drawn | the system's, not the turntable's |

## Mechanism
The deck, node `deck` (the round plate and the two side frames), turns about z through the deck's axis, 0 to 360 degrees: a
spin on the slewing ring, with no stop (the indexing angles, 90 or 180 between lines, are the drive's and the controls', not
drawn). The six rollers, nodes `roller-1` to `roller-6` (from the −y end at rest), are children of `deck` (element.py,
P.parents, as tensioner-belt 2.0's roll on its arm): each turns about its own axis, along x at rest, 0 to 360 degrees, and turns
with the deck, so its axis follows the track. At rest the deck plate rests face to face on the race's top (z 600); turning, its
underside stays on that plane and nothing fixed rises above it under the deck (the race r 380 lies inside the plate's r 450;
the base plate and frame are below it). The rollers stand 5 clear of the side frames at their end faces, 50 apart edge to edge
along the track, 85 above the deck plate at their undersides and 10 below the frames' tops, so no roller touches anything at
rest or as it turns.
behaviour.csv: `home` (default) and `turning` (manual toggle: the drive is the assembly's) for the deck, `still` (default) and
`rolling` (manual toggle: the goods turn the free rollers) for the rollers, a pose row each at the range end.

## Named nodes
`deck`: rotate about z through (0, 0, 600), range 0 to 360 degrees; `roller-1` to `roller-6`: rotate about x through their own
axes, range 0 to 360 degrees, children of `deck`. Colliders, axis-aligned boxes: `rail-l`, `rail-r` (l / r the −x / +x side),
`post-la`, `post-lb`, `post-ra`, `post-rb` (a / b the −y / +y side), `beam-l`, `beam-r`, `beam-a`, `beam-b`, `tie-lo-a`,
`tie-lo-b`, `plate`, `ring`, `deck-plate` (the deck's plan as a square box at rest), `frame-l`, `frame-r` (the track's side
frames at rest), `roll-bed` (the roller bed at rest: what goods ride on). None is named like a node.

## Materials by layer
`M-STEEL-7035` the floor rails, posts, ties, top frame beams, base plate, deck plate and the track's side frames (painted
steel, RAL 7035) · `M-SILVER` the slewing ring's fixed race (bright steel) · `M-ZINC` the rollers (steel tube, zinc-plated).
The layer names say the colour and the kind of material shown; no grade is claimed.

## Decals (Blender)
"complexes.org" on the +x floor rail's outer face.

## Notes
No vendor names, part numbers or marks. No load rating, no speed or indexing figure and no safety claim: no goods' mass is on
file, no calculation or test of the model is on file, and the turntable is not sized against a load. Not drawn: the slewing
ring's rotating race, balls, seals and gear ring; the drive (gearmotor, pinion, its mount on the base), stops, a home sensor,
guards round the deck's edge, side guides, transfer plates to the sections before and after, height adjustment, the rollers'
axles and bearings. The anchor holes are on file; the anchors are the assembly's.
Gate note (mech-r92's lesson, and r93's): the bounding box's x and y extremes are the floor rails (axis-aligned boxes) and the
z extreme the side frames' tops (node `deck`, a top-level node); the round deck and the race stay inside the rails' plan. The
first build had the frames' tops 10 below the rollers' tops, as conveyor-roller's: its AutoCAD gate read the STEP's z extent as
750 (the rollers) and the glb's as 740, because the gate's glb extents reader does not descend into nested nodes (the rollers are
children of `deck`), and failed by 10.0 on the 0.5 allowance. The guides at 760 are the fix, at the same version; request
mech-12 asks the core to read nested nodes' extents.

## Outputs (out/)
`turntable.lsp` · `.glb` (pivots on the deck and the six rollers, the rollers nested in the deck) · `preview-*.png`. Terminal:
dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r93, unattended, 2026-11-11) |
| 1.1 | review turntable-1.0 note 1, text only, no figure changed: the side frames' corners stand at r 446.0 from the axis (√(300² + 330²)), not 445.7, in spec.md and element.py's TRK_L comment (mech-r110, unattended, 2026-11-12) |
