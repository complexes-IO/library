# booth-powder · v1.0 · powder coating booth, open front 2000 × 2200, 1200 deep, sheet 2.0, back extraction opening 1200 × 1000, plenum, duct Ø300

**What** An open-front powder coating booth, a batch booth: the operator stands in front of it and sprays powder onto parts hung
inside; the overspray is drawn back through an opening in the back wall into a plenum, and from there through a duct to the
extraction (filters, fan and powder recovery, which this element does not draw). Two side walls, a roof and a back wall of sheet
steel stand on the floor; the front is open. The systems of lib/machines-factory.txt that list it (booth-powder and the
powder-coating-system) place it with the extraction, the gun and the cure oven (oven-cure, a later element).
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks booth-powder
own_design "yes", "powder coating booth (sheet-metal walls, extraction opening)"). No product was matched and no vendor file was
opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the floor z = 0 under the middle of the open front; x = 0 across the booth's width, y = 0 the
front plane (the work opening), the booth toward +y, the operator toward −y. Extents x ±1000, y 0 to 1600 (the plenum behind),
z 0 to 2200.
**Built with** toolkit 1.3 · AutoLISP command `PWDBOOTH` · no parameters.

## Mechanism
None: a fixed booth has no moving part.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the floor | the side walls, back wall and nothing else stand on z = 0 | its fixing to the floor is where a BOM places it (no anchor in this element) |
| the extraction duct | Ø300 bore of the collar on the plenum's top, axis at (0, 1399), the collar's top at z 1700 | a design choice (features.csv kind `own`): the duct and its clamp are the system's, placed with the extraction unit |
| the parts sprayed | through the open front, 1996 clear between the side walls, 2198 high to the roof's underside | the hanger and the overhead conveyor (if any) are the system's; this booth has no conveyor slot |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| booth | 2000 wide (x ±1000), 1200 deep (y 0 to 1200), 2200 high | a batch booth for parts up to about 1500 × 1500 on a hanger, with room to spray round them |
| sheet | 2.0 everywhere: side walls x ±998 to ±1000, roof z 2198 to 2200 across them, back wall y 1198 to 1200 between them | one sheet gauge for the whole booth; the frame and stiffeners behind it are not drawn |
| extraction opening | 1200 × 1000 in the back wall (x ±600, z 500 to 1500) | in front of the plenum, at the height the parts hang |
| plenum | 1400 wide (x ±700), 400 deep (y 1200 to 1600), z 400 to 1600, sheet 2.0 (back, top, bottom, two sides), on the back wall's outer face | 100 round the opening on every side, so the opening opens wholly into it |
| duct collar | Ø300 bore, 2.0 wall (Ø304 outside), 100 high, on the plenum's top, centred (axis x 0, y 1399), through a Ø300 opening in the top | the extraction duct's connection |
| fan, filter cartridges, powder recovery, lights | not drawn | the extraction is the system's element; the twin reads none of them here |

## Where it stands (the system's)
How much air the extraction draws through the open front, the explosion protection of a powder booth (its zone, its ignition
sources, its venting), the fire protection and the lighting level are figures of the system and its standards, none of which is
on file (EN 16985, NFPA 33). This element makes no airflow, fire, explosion or safety claim and names no such figure; the system
that places it cites them when they are on file.

## Named nodes
None. Colliders `roof`, `wall-l`, `wall-r`, `wall-back`, `plenum`.

## Materials by layer
`M-STEEL-7035` walls, roof and plenum (sheet steel, light grey). `M-GALV` duct collar (galvanised sheet).

## Notes
No load rating and no safety claim. No vendor names, no label. A booth with a conveyor slot and silhouette openings for an
overhead conveyor, and the extraction unit itself, are later elements.

## Outputs (out/)
`booth-powder.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r62, unattended) |
