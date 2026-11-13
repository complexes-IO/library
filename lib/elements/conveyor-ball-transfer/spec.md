# conveyor-ball-transfer · v1.0 · ball transfer table, our own design, 500 between frames, 1000 long, 32 ball units Ø25 at 125 pitch in a 4 × 8 grid, ball tops 750, 4 × M12 anchor holes

**What** A ball transfer table, one section: a flat steel deck on the conveyor family's track carries thirty-two ball transfer
units in a square grid, and a carton, tote or tray set on the balls is pushed by hand in any direction. It turns goods, joins
conveyor lines that meet at an angle, and lets an operator slide a pack off to the side; nothing in it is driven. The deck spans
the side frames' outsides and the balls stand 10 above the frames' tops, so goods leave over either side as well as either end.
lib/machines-from-elements.txt lists it in conveyor-types-bench, beside conveyor-roller and the rest of the family. The balls are
the mechanism: the twin turns them by name.
**Class** furniture · **Baseline** our own design, OPERATING.md 12 "Own designs" (EM, 2026-11-05): lib/inventory.csv marks the row
own_design "yes" ("ball units on a plate, four-way manual transfer"); request mech-9's answer (item 3) says no ETIM class on file
fits, so it is not generic. No product was matched and no vendor file was opened; the element had no folder or record before this
build. The holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the table, x = 0 midway between the side frames, y = 0
midway along its length. Goods move on the balls in any direction; the balls' centres are at z 737.5, their tops at z 750.
Extents x ±375, y ±500, z 0 to 750: the family's track and height (conveyor-roller 1.0), 1000 long instead of 1500, so a
roller, wheel, slat or belt section runs up to either end at the same height.
**Built with** toolkit 1.3 · AutoLISP command `CONVBALL` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the foot plates at 680 × 500 (x ±340, y ±250) | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice, conveyor-roller 1.0's pattern, on this table's 1000 length. The anchors (anchor-bolt, not built yet) are the assembly's; nothing is placed in the holes |
| floor | the foot plates' undersides, z = 0 | a flat floor; the floor is the assembly's |
| the next section | the table's end faces, y ±500 (the side frames' and the deck's ends) and the deck's side edges, x ±300 | a section of the family placed against either end, or a line arriving at either side, hands goods over at z 750: its rollers', wheels' or belt's top. The deck's top (z 720) and the bosses (z 735) stay below that line, so nothing catches. No joining plate or hole is drawn: how sections are joined is the assembly's |
| the goods | the balls' tops, z = 750 | none on file: goods ride on the ball bed (x ±200, y ±450); a base shorter than 125 in either direction rests on fewer than two balls and may tip. A ball table wants a flat, firm base (a carton, a tote, a tray) |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane midway between the
side frames) and C (the plane midway along the table) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5). The Ø30 ball sockets are this
design's own openings (features.csv kind `own`): no fastener goes in them.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| deck | one plate 600 (x ±300) × 1000 (y ±500) × 10 (z 710 to 720), on the side frames' tops | carries the ball units; spans the frames' outsides so goods can leave sideways over the frames (their tops at z 710, 40 below the balls' tops) |
| ball units | 32: a Ø40 housing boss 15 high on the deck (z 720 to 735), bored Ø30 through, and a Ø25 ball with its centre at z 737.5 (top 750, underside 725, 5 above the deck's top); line i at y −437.5 + 125 (i − 1), i = 1 to 8; ball k at x −187.5 + 125 (k − 1), k = 1 to 4 | a square 125 grid, the same both ways, so goods move the same in any direction; the end lines 62.5 inside the deck's ends and the outer balls 62.5 inside the frames' inner faces. The ball clears its socket by 2.5 all round at its widest (z 737.5) and by 2.75 at the boss's top; its seat balls, the housing's cap and its fixing to the deck are not drawn (as the wheel conveyor's axles) |
| the ball bed | x ±200, y ±450, z 725 to 750 (the collider `ball-bed`) | what goods ride on: the balls' outlines |
| side frames | 2, section 50 (x) × 80 (z), 1000 long, drawn by their outside; inner faces at x ±250, z 630 to 710 | the family's frames (conveyor-roller 1.0), their tops carrying the deck |
| supports | 2, at y −250 and +250: each two posts, an upper and a lower tie and two foot plates | 500 apart, 250 from each end (the family's end distance) |
| posts | 4, 50 × 50, drawn by their outside, z 20 to 630, under the side frames (x 250 to 300 each side) | each stands on its foot plate and carries a frame |
| upper ties | 2, 500 long (x ±250) × 50 (y) × 40 (z 570 to 610), post to post | hold the posts to the track's width; 20 clear below the frames' undersides |
| lower ties | 2, 500 × 50 × 50 (z 150 to 200), post to post | stiffen each support |
| foot plates | 4, 150 (x 225 to 375 each side) × 100 (y) × 20 (z 0 to 20), one under each post, running outward; one Ø13.5 hole in each, 40 outside the post's outer face and 35 from the plate's outer edge | fix the table to the floor; 20 thick |
| the goods | not drawn | the system's, not the table's |

## Mechanism
Thirty-two free balls, nodes `ball-<line>-<k>` (line 1 at the −y end, y −437.5; line 8 at the +y end, y 437.5; k counts from −x,
1 to 4), each a sphere turning in its housing's socket. A ball transfer ball turns about any axis; the twin draws the turn as a
rotation about x through the ball's centre, 0 to 360 degrees (a spin, with no stop), which is what goods moving along y give it.
The seat balls under the ball, which let it roll any way, and the housing's cap are not drawn: a ball touches nothing at rest or
as it turns (its underside 5 above the deck, 2.5 clear of the socket wall). The table is level in its own frame. behaviour.csv:
state `still` (default) and `turning` (manual toggle, the goods' passage), pose of the thirty-two balls at the range end in
`turning`.
The balls are `mesh` primitives (toolkit/prims.py): the toolkit has no sphere solid, and a sphere is what a ball is. They are in
the glTF only, as a cable's sweep or relay-ice-cube-2co's spring is; AutoCAD builds the housings, deck and frames (the LISP lists
each mesh as "not built in AutoCAD"), and the AutoCAD gate's STEP-vs-glb check compares the solids' extents (acad-gate.py,
`glb_includes_mesh`). The catalogue's size and the Godot QA read the glTF with the balls, so both show z 750.

## Named nodes
`ball-1-1` to `ball-8-4` (32): rotate about x through their centres, range 0 to 360 degrees. Colliders: `frame-l`, `frame-r`,
`post-la`, `post-lb`, `post-ra`, `post-rb`, `foot-la`, `foot-lb`, `foot-ra`, `foot-rb` (l / r the −x / +x side, a / b the −y / +y
support), `tie-up-a`, `tie-up-b`, `tie-lo-a`, `tie-lo-b`, `deck-plate` and `ball-bed` (x ±200, y ±450, z 725 to 750: what goods
ride on; none is named like a node).

## Materials by layer
`M-STEEL-7035` the side frames, posts, ties, foot plates and deck (painted steel, RAL 7035) · `M-ZINC` the ball-unit housings
(steel, zinc-plated) · `M-SILVER` the balls (hardened steel, bright).

## Decals (Blender)
"complexes.org" on the +x side frame's outer face.

## Notes
No vendor names, part numbers or marks. No load rating, no speed figure and no safety claim: no goods' mass is on file, no
calculation or test of the model is on file, and the table is not sized against a load. Not drawn: the ball units' seat balls,
caps, seals and fixings, side guides, end stops, joining plates between sections, height adjustment. The anchor holes are on
file; the anchors are the assembly's.

## Outputs (out/)
`conveyor-ball-transfer.lsp` · `.glb` (pivots on the thirty-two balls) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r97, unattended, 2026-11-11) |
