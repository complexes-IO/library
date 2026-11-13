# clamp-beam · v1.0 · clamping beam of a sheet folder, 1000 long, nose relieved 45 degrees, lifts 150 in a portal on beam-folding 1.0's cheeks

**What** The clamping beam of a sheet folder: it holds the sheet down on the bed along the bend line while the folding beam
swings up. It is the clamp-beam of folder-sheet (lib/machines-factory.txt line 24; beam-folding 1.0 carries the bed, the bend
line and the folding beam). A portal (two posts standing on beam-folding's cheeks, a crossbar over them) is the fixed body; the
clamping beam lifts between the posts to open the jaw.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks clamp-beam own_design
"yes"). No product was matched and no vendor file was opened. The length, the posts' places and the bed's depth are read from
beam-folding 1.0 (library.load), so the two cannot drift apart; every other size is a design choice.
**Units / frame** mm, Z up. Origin: beam-folding's origin, the bend line's centre: x = 0 midway along it, y = 0 the bed's front
face, z = 0 the bed's top face, on which the nose's tip rests. The bend line runs along x; the clamp lifts along +z. Extents
x −600 to 600, y −50 to 400, z 0 to 820 at rest.
**Built with** toolkit 1.3 · AutoLISP command `CLAMPBEAM` · no parameters.

## Mechanism
`clamp` (translate along +z, 0 to 150): the clamping beam, nose and upper beam. At 0 (closed) the nose's underside lies in the
bed's plane, its tip on the bend line; at 150 the jaw stands open 150 for the sheet to slide in. Its pivot is the nose's tip at
the bend line's centre (0, 0, 0). Through its travel it stays between the posts (5 clear) and below the crossbar (210 clear when
open). Its guides on the posts and its lift (eccentrics or cylinders) are the machine's or a later version's: not drawn, so the
beam floats between the posts in the model.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| beam-folding 1.0 | the nose 1000 long (x ±500, HALF) on the bed's top face, its underside as deep as the bed (y 0 to 400, BED_D); the posts on the cheeks' tops (x ±560 to ±600, CHEEK_X0 and CHEEK_T; z 60, CHEEK_TOP) | library.load("beam-folding") |
| the folding beam | at 135 degrees its top face leans back at 45 degrees over the bed, along the nose's cut face: the sheet folds between them | beam-folding's FOLD_MAX; the axis adjustment for the sheet's thickness is the machine's (beam-folding's spec) |
| the sheet | clamped between the nose's underside and the bed | no sheet thickness or clamping force is on file: none is stated |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| nose | 1000 × 400 × 200 (x ±500, y 0 to 400, z 0 to 200), its front cut back at 45 degrees from the tip on the bend line, leaving a top land 200 deep (y 200 to 400) | the folding beam reaches 135 degrees against it; one cut solid |
| upper beam | 1110 × 200 × 200 (x ±555, y 200 to 400, z 200 to 400) on the nose's land | stiffens the nose; its ends 5 clear of the posts, where the guides go |
| travel | 0 to 150 | the jaw's opening |
| posts | 2, 40 × 450 × 700 (x ±560 to ±600, y −50 to 400, z 60 to 760) on beam-folding's cheeks | carry the beam |
| crossbar | 1200 × 200 × 60 (y 200 to 400, z 760 to 820) on the posts' tops | ties the portal |
| finish | painted | a design choice |

## Named nodes
`clamp` (translate, above). Colliders `clamp-body` (the beam, at rest; named apart from its node), `post-l`, `post-r` and
`crossbar`.

## Materials by layer
`M-STEEL-7035` everything (painted RAL 7035).

## Notes
No clamping force, sheet capacity or speed: no drive, load or sheet figure is on file, so the beam is not sized against them. The
nose is one straight beam: segments (for boxes) and a crowning are a later version if a machine asks for them. Volume and
triangles: see the gates (lib/materials.csv gives no densities, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`clamp-beam.lsp` · `.glb` (pivot on `clamp`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r81, unattended) |
