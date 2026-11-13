# booth-paint · v1.1 · spray paint booth, open front 3000 × 2500, 2400 deep, sheet 2.0, dry filter wall 2600 × 1800, two glazed roof lights, plenum, duct Ø500

**What** An open-front spray paint booth with a dry filter wall, a batch booth: the operator stands in front of it and sprays
parts set or hung inside; the overspray is drawn back through a filter wall that covers the exhaust opening in the back wall,
into a plenum, and from there through a duct to the exhaust fan (which this element does not draw). Two side walls, a roof and a
back wall of sheet steel stand on the floor; the front is open. Two light housings stand on the roof, each over a glazed
opening, so the light fittings are outside the booth's inside. The systems of lib/machines-factory.txt that list it (booth-paint
and booth-spray-paint) place it with the exhaust, the spray gun and its supply.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks booth-paint own_design
"yes", "spray paint booth (walls, filter wall, lighting)"). No product was matched and no vendor file was opened. Every size is a
design choice.
**Units / frame** mm, Z up. Origin: the floor z = 0 under the middle of the open front; x = 0 across the booth's width, y = 0 the
front plane (the work opening), the booth toward +y, the operator toward −y. Extents x ±1500, y 0 to 3000 (the plenum behind),
z 0 to 2650 (the light housings on the roof).
**Built with** toolkit 1.3 · AutoLISP command `PNTBOOTH` · no parameters.

## Mechanism
None: a fixed booth has no moving part. The filter media are changed by hand from inside the booth; the twin does not read them.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the floor | the side walls, back wall and nothing else stand on z = 0 | its fixing to the floor is where a BOM places it (no anchor in this element) |
| the exhaust duct | Ø500 bore of the collar on the plenum's top, axis at (0, 2699), the collar's top at z 2350 | a design choice (features.csv kind `own`): the duct and its clamp are the system's, placed with the exhaust fan |
| the parts sprayed | through the open front, 2996 clear between the side walls, 2490 high to the glazing's underside, 2328 deep to the filter grid | the stands, hangers or a conveyor are the system's; this booth has no conveyor slot |
| the light fittings | inside the two housings on the roof, over the glazing | the fittings, lamps and their gear are the system's; not drawn |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| booth | 3000 wide (x ±1500), 2400 deep (y 0 to 2400), 2500 high | 3000 × 2400 × 2500: a design choice; the part size it suits is the system's |
| sheet | 2.0 for the walls, roof and plenum: side walls x ±1498 to ±1500, roof z 2498 to 2500 across them, back wall y 2398 to 2400 between them | one sheet gauge for the booth; the frame and stiffeners behind it are not drawn |
| exhaust opening | 2600 × 1800 in the back wall (x ±1300, z 300 to 2100) | the filter wall covers most of the back, at the height the parts are sprayed |
| filter media | one bank 2700 × 50 × 1900 (x ±1350, y 2348 to 2398, z 250 to 2150) against the back wall's inner face, lapping the opening 50 on every side | dry filter pads; the media type and its grade are the system's |
| retaining grid | galvanised bars 40 wide, 20 deep (y 2328 to 2348) in front of the media, 10 inside its edges (x ±1340, z 260 to 2140): top and bottom bars, five uprights on a 660 pitch, a middle bar between each pair of uprights (z 1180 to 1220), so 4 × 2 fields | holds the pads against the back wall; a field is one pad's place |
| plenum | 2800 wide (x ±1400), 600 deep (y 2400 to 3000), z 200 to 2200, sheet 2.0 (back, top, bottom, two sides), on the back wall's outer face | 100 round the opening on every side, so the opening opens wholly into it |
| duct collar | Ø500 bore, 2.0 wall (Ø504 outside), 150 high, on the plenum's top, centred (axis x 0, y 2699), through a Ø500 opening in the top | the exhaust duct's connection |
| roof openings | two, 1200 × 300 (x ±600; y 600 to 900 and 1400 to 1700) | over the work area, in front of the filter wall |
| glazing | 8 thick, under the roof (z 2490 to 2498), lapping each opening 20 on every side (1240 × 340) | closes the roof opening from inside |
| light housings | two, 1300 × 400 × 150 (x ±650, 50 beyond each opening), on the roof (z 2500 to 2650), drawn by their outside | the light fittings' place, outside the booth's inside |
| fan, lamps, floor, doors, frame | not drawn | the exhaust is the system's element; the twin reads none of them here |

## Where it stands (the system's)
How much air the exhaust draws through the open front, the filter's grade and load, the fire and explosion protection of a
spray area (its zones, its ignition sources, its sprinklers), the lighting level and the light fittings' protection are figures
of the system and its standards, none of which is on file (NFPA 33, EN 16985). This element makes no
airflow, fire, explosion, lighting or safety claim and names no such figure; the system that places it cites them when they are
on file.

## Named nodes
None. Colliders `roof`, `wall-l`, `wall-r`, `wall-back`, `filter` (media and grid), `plenum`, `light-a`, `light-b`.

## Materials by layer
`M-STEEL-7035` walls, roof, plenum and light housings (sheet steel, light grey). `M-GALV` duct collar and retaining grid
(galvanised). `M-WHITE-PVC` the filter media (shown in the library's white layer; the media is not PVC). `M-CASE-CLEAR` the roof
glazing (the library's clear layer).

## Notes
No load rating and no safety claim. No vendor names, no label. A closed booth with doors, a conveyor booth with silhouette
openings, a water-wash back and the exhaust fan itself are later elements.

## Outputs (out/)
`booth-paint.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r63, unattended) |
| 1.1 | text only, the part unchanged (mech-r73, unattended; review mech-r63 finding 1): the booth's "why" cell written as a design choice, the part size it suits left to the system |
