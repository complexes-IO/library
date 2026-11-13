# lift-stacker · v2.0 · pallet stacker / destacker, own design, four-post frame 1700 × 2300 × 2700, lift table 344 with three stops, two fork bars with tines 300 into the pallet's openings, 20 × M12 anchor holes

**What** A pallet stacker / destacker: a magazine for empty pallets on a conveyor line. Four posts on anchored foot plates, tied at
the top by a frame, hold a stack of up to ten pallets on two fork bars, one on each side of the stack; a lift table under the stack
takes pallets in and out along x at the conveyor family's hand-off height. The table has three stops: deck 750 (the hand-off), 950
and 1094. Destacking: the empty table rises to 1094 under the stack, which rests on the tines with its underside at 1084, and lifts
it 10 off them; the forks draw back; the table lowers one pallet's height (144) to 950 and the forks run in again under the second
pallet; the table lowers to 750 with the bottom pallet (the second lands on the tines when the deck passes 940), which leaves along
x. Stacking: the incoming pallet rides the table up to 950 and lifts the stack 10 off the tines; the forks draw back; the table
rises to 1094, so the incoming pallet's stringer boards stand 10 over the tines, and the forks run in; the table lowers to 750. It is the
conveyor family's stacker (lib/inventory.csv row lift-stacker, "pallet stacker / destacker (our own build)", EM 2026-11-08: the conveyor
family); no system row names it yet.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks lift-stacker own_design
"yes"; the folder's record, references/source.txt, says "own build, no vendor search", nothing downloaded). No product was matched
and no vendor file was opened. The hand-off height is read from conveyor-roller 1.1 (its TOP) and the pallet's footprint, height and
openings from pallet 1.2, both with library.load, so they cannot drift apart; the anchor holes are ISO 273's; every other size is a
design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 under the centre of the pallet stack. x along the pallets' flow, in and
out of the stacker between the posts; y across it, through the fork bars. Extents x −850 to 850 and y −1150 to 1150 (the foot
plates), z 0 to 2700 (the top frame).
**Built with** toolkit 1.3 · AutoLISP command `LIFTSTACKER` · no parameters.

## Mechanism
`table` (translate along +z, 0 to 344 mm): the deck 1300 × 900 × 10 (x ±650, y ±450, z 740 to 750 at rest) on three beams 60 × 100
along x (y −450 to −390, −30 to 30, 390 to 450; z 640 to 740). At 0, the lower stop (state `down`), the middle beam rests on the
lift's column (its top z 640) and the deck's top is at z 750, level with conveyor-roller's rollers' tops: a pallet rolls on and off
along x. At 200, the middle stop (`mid`), the deck's top is at z 950. At 344, the top stop (`up`), it is at z 1094, still 54 under
the tines' underside (1148) and inside the rails' y ±528 (the deck reaches y ±450), so it passes nothing fixed. Its pivot is the
deck's top centre at rest (0, 0, 750), the axis +z.
`fork-1` and `fork-2` (translate 0 to 300 mm toward the stack's centre: `fork-1` on the −y side along +y, `fork-2` on the +y side along
−y): each a bar 1360 × 60 × 80 (x ±680, z 1148 to 1228; y ±828 to ±888 at rest) with two tines 100 × 40 × 300 on its inner face (x
±218.5 to ±318.5, z 1148 to 1188; y ±528 to ±828 at rest). The bar's ends run on the guide rails. At 0 (out) the tines' tips are 20
outside the pallet's sides (y ±528 against ±508); at 300 (in) they reach y ±228, 280 into the pallet. Pivots (0, ∓828, 1188), the
bars' inner faces at the tines' tops.
The tines' height: with the table at the middle stop the stack's bottom pallet stands on the deck at z 950 and the second pallet's
underside is at 1094, its stringer boards' underside at 1198 (pallet 1.2: bottom boards 18 + blocks 86); the tines' tops are at 1188,
10 under it, so they run in clear. The table then lowers 10 and the second pallet rests on the tines by its stringer boards (its
underside at 1084); the bottom pallet goes down with the table to 750 to 894, 190 under the second. The stack left on the tines has
its underside at 1084, so the empty table's top stop is 1084 + 10 = 1094, one pallet (144) over the middle stop: element.py asserts
both (the 1.0 table stopped at 950, 134 under the stack, and could neither take the next pallet off nor put one on: review
lift-stacker-1.0 finding 1, option (a), the tines kept at 1188). Each tine runs in the middle of one of the
pallet's openings between its block columns (x ±72.5 to ±464.5, 392 wide; the tine 100 wide at its middle, ±268.5), so the blocks and
the bottom boards under them never meet a tine. Nothing of this element lies in any node's path (MOT-010 sweeps them): the rails start
at the tines' line (y ±528), outside the pallet and the deck.
Not drawn, placed in a later version once their elements are on file: the table's drive (a scissor or cylinder lift under the deck),
the forks' cylinders (the folder's plan: cylinder-driven fork pairs), the photoeye-m18 that senses the stack's height, the infeed and
outfeed conveyor sections, the guarding and the controls. So the nodes move without a visible drive in the model.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| conveyor-roller 1.1 | the table's top at the lower stop, z 750 = the rollers' tops | conveyor-roller's TOP (library.load); the infeed and outfeed lines are placed by the assembly |
| pallet footprint | 1219 × 1016, the stack's centre at x 0, y 0; the tines' tips 20 clear of its sides when out, the rails and posts outside it | pallet 1.2 (library.load: LX, LY). **Assumption (B)**, inherited: pallet 1.2 marks its footprint so (ISO 6780 not on file; lib/inventory.csv names the size). Closed with the pallet's: when ISO 6780 is on file and the pallet's figure changes, this element follows it through library.load, a version here if the frame no longer fits |
| pallet height and openings | 144 high; openings along y between the block columns, x ±72.5 to ±464.5, from the underside to the stringer boards' underside (104) | pallet 1.2 (library.load: BOT, BLK, STR, DECK, B); its openings are that element's design figures. The tines are sized to them, not to a fork arm; the table's three stops follow from them (Mechanism) |
| the floor | 20 × Ø13.5 holes: 4 in each foot plate at 220 × 220 about the post's centre (x ±700 ± 110, y ±1000 ± 110), 4 in the lift's base plate at 1000 × 600 (x ±500, y ±300) | M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv); position Ø1.0 at MMC to A the floor plane, B the plane x 0, C the plane y 0 (ASME Y14.5 floating fastener, T ≤ H − F = 1.50; features.csv). The anchors are the assembly's |
| the drives and the photoeye | none in this element | the lift's drive, the forks' cylinders and photoeye-m18 come with their elements, placed in a later version (OPERATING.md 12: a host doesn't model holes for a part it places later) |
| the guarding | none in this element | the guards and their interlocks around a moving table and forks are the assembly's elements, with their safety sign-off (ISO 12100 and ISO 14120 are not in lib/standards/sources.csv); this element claims nothing for them |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| foot plates | 4, 300 × 300 × 20 (x ±550 to ±850, y ±850 to ±1150, z 0 to 20), 4 × Ø13.5 each at 220 × 220 | each post's footprint on the floor; the holes 40 from the plate's edges |
| posts | 4, 100 × 100 (x ±650 to ±750, y ±950 to ±1050), z 20 to 2600, drawn solid by their outside | the pallets pass between them along x (1900 clear in y against the pallet's 1016); a hollow section's wall is a later version's |
| top frame | two beams 1500 × 100 × 100 along x over the posts (y ±950 to ±1050), two 100 × 1900 × 100 along y between them (x ±650 to ±750); z 2600 to 2700 | ties the posts; ten pallets on the tines (1084 to 2524) stand under it |
| guide rails | 4, 80 × 422 × 60 (x ±620 to ±700, y ±528 to ±950, z 1088 to 1148), each from the tines' line to its post's inner face | carry the fork bars' ends (x ±620 to ±680) over the whole stroke; 10.5 clear of the pallet's ends (x ±609.5) |
| fork bars and tines | bars 1360 × 60 × 80, tines 100 × 40 × 300, two per bar | one tine in each of the pallet's two openings from each side; 40 thick fits the 104 opening with the 10 lift-off |
| fork stroke | 300 | the tines 280 into the pallet, each under the full width of its outer stringer board (145) |
| lift table | deck 1300 × 900 × 10 on three beams 60 × 100 × 1300; travel 344, stops 0 / 200 / 344 (deck 750 / 950 / 1094) | the deck under the pallet's three bottom boards (x ±609.5); the middle stop 200 sets the tines' height (1188 = 950 + 144 + 104 − 10, so the forks run in under the second pallet); the top stop is one pallet (144) higher, 10 over the stack's underside on the tines (1084), so the empty table lifts the stack off and a carried pallet's stringer boards clear the tines |
| lift-off | 10 | the tines run in and out clear of the stringer boards |
| lift base | plate 1200 × 800 × 20 (x ±600, y ±400), column 200 × 200 (z 20 to 640) | the table rests on the column at the lower stop with its drive slack |
| floor ties | 4, 50 × 450 × 20 (x ±550 to ±600, y ±400 to ±850, z 0 to 20), from the base plate's long edges to the foot plates | join the lift's base to the frame, so the two are one body and keep their places (GEO-070); on the floor, under every pallet's path |
| finish | posts, frame, rails, base painted RAL 7035; table and forks yellow | a design choice: the moving parts in a signal colour (an appearance, not a safety marking) |

## Named nodes
`table`, `fork-1`, `fork-2` (translate, above). Colliders `post-1` to `post-4` (the posts, floor to the top frame), `top` (the top
frame as one box), `rails-1`, `rails-2` (each side's two rails as one box), `lift-base` (base plate and column, z 0 to 640),
`lift-deck` (the table at rest, z 640 to 750).

## Materials by layer
`M-STEEL-7035` the foot plates, posts, top frame, guide rails, base plate, column and floor ties (painted RAL 7035) · `M-YELLOW` the table and
the two fork bars with their tines.

## Notes
No load rating, no speed, no cycle time and no safety claim: no pallet or stack mass, no drive figure and no stacker standard are
on file, so the frame, the tines and the table are not sized against them; a stacker's moving table and forks are guarded by its
assembly. The volume is 285 201 144 mm³ (foot plates 4 × 1 800 000, posts 4 × 25 800 000, top frame 2 × 15 000 000 + 2 × 19 000 000,
rails 4 × 2 025 600, base plate 19 200 000, column 24 800 000, floor ties 4 × 450 000, less twenty holes 57 256; table 11 700 000 + 3 × 7 800 000; forks
2 × (6 528 000 + 2 × 1 200 000); written as volume only: lib/materials.csv gives no densities, so no mass is stated). No vendor names,
no label. The gate's fillet radius is set per primitive (0.5, `P.radii`; mech-r106): every free-corner edge is 20 or longer.

## Outputs (out/)
`lift-stacker.lsp` · `.glb` (pivots on `table`, `fork-1`, `fork-2`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r108, unattended) |
| 2.0 | review lift-stacker-1.0 findings 1 and 2 (mech-r121, unattended): the table's range 0 to 200 → 0 to 344 with three stops (states down / mid / up in behaviour.csv), so the destacking and stacking cycles close; the tines stay at 1188. "pallet 1.1" → pallet 1.2 and conveyor-roller 1.0 → 1.1, the versions library.load reads (the figures are the same). A node's range changed: a major. Nothing places lift-stacker, so no pin breaks |
