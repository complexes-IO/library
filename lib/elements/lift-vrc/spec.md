# lift-vrc · v1.1 · vertical reciprocating conveyor, own design, two-mast portal 4600 high, carriage with a 700 × 1600 deck rising 2250 from 750 to 3000, 8 × M12 anchor holes

**What** A vertical reciprocating conveyor (VRC): a goods lift that carries loads between two conveyor levels, the floor line and
a mezzanine. Two masts stand on anchored foot plates and are joined at the top by a beam; between them one carriage runs straight
up and down. The carriage is a flat deck on two side beams, with an upright on each side facing its mast: the hoist lifts it by
the uprights and the guide shoes on them run on the masts. Goods roll on and off along y, between the masts, at the lower level
(the deck's top level with a roller conveyor's rollers' tops) and at the upper one. It is the conveyor family's VRC (lib/inventory.csv
row lift-vrc, "vertical reciprocating conveyor (our own build: mast, carriage, roller deck)", EM 2026-11-08: the conveyor family); no
system row names it yet.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks lift-vrc own_design "yes";
the folder's record, references/source.txt, says "own build, no vendor search", nothing downloaded). No product was matched and no
vendor file was opened. The lower level is read from conveyor-roller 1.0 with library.load (its TOP), so the two cannot drift apart;
the anchor holes are ISO 273's; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 midway between the two masts. x across the lift, through the masts (the
fixed side); y along the goods' flow, in and out between the masts. Extents x −635 to 635 (the foot plates), y −800 to 800 (the
deck), z 0 to 4600 (the top beam).
**Built with** toolkit 1.3 · AutoLISP command `LIFTVRC` · no parameters.

## Mechanism
`carriage` (translate along +z, 0 to 2250 mm): the deck 700 × 1600 × 10 (x ±350, y ±800, z 740 to 750 at rest), two side beams
60 × 100 under its long edges (x ±290 to ±350, z 640 to 740, the deck's full length) and two uprights 80 × 120 (x ±350 to ±430,
y ±60) from z 20 to 1300. At 0, the lower stop, the uprights stand on the foot plates (z 20) and the deck's top is at z 750, level
with conveyor-roller's rollers' tops: goods roll on and off. At 2250, the upper stop, the deck's top is at z 3000 and the uprights'
tops at 3550, 950 under the top beam (4500). Each upright's outer face is 5 clear of its mast's inner face (x ±430 against ±435):
the guide shoes that run there are not drawn. Its pivot is the deck's top centre at rest (0, 0, 750), the axis +z. Nothing of this
element lies in its path (MOT-010 sweeps it). Not drawn, placed in a later version once their elements are on file: the hoist (the
folder's plan: motor-iec71-370w with gear-reducer), the guide shoes, the gates, enclosure and light curtains that guard the
lift, and its controls. So the carriage moves without a visible drive in the model. The flat deck is the carrying surface: goods
ride on it as they come off the infeed's rollers. No roller section stands on the deck: conveyor-roller is a floor-standing section
(its rollers' tops 750 above its own base), so one placed on the deck would put the rollers at 1500 at the lower stop and lose the
hand-off (review lift-vrc-1.0 finding 1, option b, mech-r117).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| conveyor-roller 1.0 | the deck's top at the lower stop, z 750 = the rollers' tops, so goods pass from the infeed's rollers onto the flat deck; the deck 1600 along y takes a load the length of a 1500 section with 50 each end | conveyor-roller's TOP (library.load); the infeed and the outfeed lines are placed by the assembly, beside the deck, not on it |
| the floor | 8 × Ø13.5 holes, 4 in each foot plate at 220 × 220 about the mast's centre (x ±485 ± 110, y ±110) | M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv); position Ø1.0 at MMC to A the floor plane, B the plane midway between the masts (x 0), C the plane through the masts' centres (y 0) (ASME Y14.5 floating fastener, T ≤ H − F = 1.50; features.csv). The anchors are the assembly's |
| the upper level | the deck's top at z 3000 at the upper stop | design: a mezzanine floor's height for the conveyor family's bench; the upper line's hand-off height is the assembly's to match |
| the guarding | none in this element | a VRC's enclosure, gates and their interlocks follow its own standard (ASME B20.1 is not in lib/standards/sources.csv); they are the assembly's elements, with their safety sign-off, and this element claims nothing for them |
| the hoist | none in this element | the motor and the reducer come with their elements, placed in a later version (OPERATING.md 12: a host doesn't model holes for a part it places later) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| foot plates | 2, 300 × 300 × 20 (x ±335 to ±635, y ±150, z 0 to 20), 4 × Ø13.5 each at 220 × 220 | each mast's footprint on the floor; the holes 40 from the plate's edges; the uprights stand on the plates' inner part at the lower stop |
| masts | 2, 100 × 100 (x ±435 to ±535, y ±50), z 20 to 4500, drawn solid by their outside | 1500 over the upper deck's top for the load's height; a hollow section's wall is the hoist version's |
| top beam | 1070 × 100 × 100 (x ±535, y ±50, z 4500 to 4600) on the masts' tops | ties the masts into a portal |
| deck | 700 × 1600 × 10, x ±350, y ±800 | the flat carrying surface: a load off a conveyor-roller section (W 500 between its frames, 600 over them) with room each side; no roller deck (Mechanism) |
| side beams | 2, 60 × 100 × 1600 under the deck's long edges | stiffen the deck along its length |
| uprights | 2, 80 × 120, z 20 to 1300 at rest, outside the deck's long edges | carry the deck from the hoist; at the lower stop they stand on the foot plates, so the carriage rests on the floor's plates with the hoist slack |
| travel | 2250 (750 to 3000) | one mezzanine level above the conveyor line |
| clearance to the masts | 5 each side | room for the guide shoes, not drawn |
| finish | masts, beam, plates painted RAL 7035; carriage yellow | a design choice: the moving part in a signal colour (an appearance, not a safety marking) |

## Named nodes
`carriage` (translate, above). Colliders `mast-l`, `mast-r` (the masts, floor to the top), `beam` (the top beam), `platform` (the
carriage as one box at rest, x ±430, y ±800, z 20 to 1300).

## Materials by layer
`M-STEEL-7035` the foot plates, masts and top beam (painted RAL 7035) · `M-YELLOW` the carriage (deck, side beams, uprights).

## Notes
No load rating, no speed, no cycle time and no safety claim: no goods mass, no hoist figure and no VRC standard are on file, so the
lift is not sized against them, and a VRC that carries goods between levels is guarded by its assembly. The volume is 158 853 099 mm³
(foot plates 2 × 1 800 000 less eight holes 22 901, masts 2 × 44 800 000, beam 10 700 000, deck 11 200 000, side beams 2 × 9 600 000,
uprights 2 × 12 288 000; written as volume only: lib/materials.csv gives no densities, so no mass is stated). No vendor names, no
label. The gate's fillet radius is set per primitive (0.5, `P.radii`; mech-r106): every free-corner edge is 10 or longer.

## Outputs (out/)
`lift-vrc.lsp` · `.glb` (pivot on `carriage`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r107, unattended) |
| 1.1 | text only (review lift-vrc-1.0 finding 1, option b): the flat deck is the carrying surface; "a conveyor-roller section on the deck" dropped from Mechanism, What it meets, the deck's row, element.py's docstring and BASELINE; geometry unchanged (mech-r117, unattended) |
