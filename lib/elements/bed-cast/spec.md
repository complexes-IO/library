# bed-cast · v1.0 · machine bed 2000 × 660 × 430, box section, two flat ways 80 wide, 6 × M12 floor anchors

**What** A machine bed: a long box-section body on a base plate anchored to the floor, with two flat machined ways along its
top face. The machines of lib/machines-factory.txt that stand on a bed (lathes, grinders, horizontal mills and borers, machining
centres) carry their carriage, table or headstock on ways of this kind; a BOM places that part on the bed's `ways`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks bed-cast own_design
"yes"). No product was matched and no vendor file was opened. The floor anchor holes are on file (ISO 273); every other size is
a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the bed's centre x = 0, y = 0; the bed's length along x; front
toward −y. The ways' top plane, the carriage's seat, is at z = 430.
**Built with** toolkit 1.3 · AutoLISP command `BEDCAST` · no parameters.

## Mechanism and the carriage's seat
`ways` (fixed): the two flat ways. Its pivot is the centre of the ways' top plane (0, 0, 430) with the axis +z: a carriage,
table or headstock element is placed there with its own base origin and moves along x on its own nodes, so a BOM row reads
`<tag>.ways`. The bed itself has no moving part.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| floor anchors | 6 × M12, Ø13.5 holes through the base plate's flanges, three a side, at 1800 × 580 (x −900, 0, 900; y ±290) | ISO 273 medium (H13), lib/standards/holes.csv. The anchors are the site's: chosen to the floor, not built |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The six anchor holes carry a declared position tolerance Ø1.2 at MMC to A, the base plate's underside (the floor plane), the
holes located to each other (features.csv; H − F = 13.5 − 12 = 1.5). The ISO 2768-m general tolerance of their 1891 mm diagonal
(±1.2, lib/standards/general-tolerances.csv row m 1000-2000; a Ø3.4 zone) would not hold the pattern, so the flanges are drilled
in one set-up with the ways.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| bed length | 2000 along x | a bed for the mid-size lathes, grinders and mills of the factory list |
| base plate | 2000 × 660 × 25, its flanges 80 wide each side of the body | carries the anchors outside the body, where a spanner reaches them |
| body | 2000 × 500, from the base plate (z 25) to its top face (z 400) | a closed box section; height chosen so the ways sit at 430, a carriage then brings the work to a working height |
| ways | 2, flat, 80 wide, 30 proud of the body's top (z 400 to 430), centres at y ±170 (340 apart), 1960 long (20 short of each end) | flat ways carry a carriage on both; 340 apart for a carriage of the body's width; the 20 at each end is the body's machining run-out |
| anchors | three a side at x −900, 0, 900, y ±290 (mid-flange: 40 from the body, 40 from the plate's edge) | an anchor at each end and one at mid-length, so no span between anchors is longer than 900 |
| body | drawn by its outside: a cast or welded box section is closed at its ends, its cores and ribs are not seen | the model shows what can be seen |
| ribs, cores, scraping of the ways, way covers, chip trough | not drawn | they belong to the machine that is built on the bed |

## Named nodes
`ways` (fixed, above). Colliders `body` (the base plate and body) and `ways` (the two ways and the gap between them).

## Materials by layer
`M-STEEL-7035` the base plate and body (painted RAL 7035) · `M-SILVER` the ways (bare machined steel, shown in the library's
bright-metal layer; the library has no `M-STEEL` render material).

## Notes
No load rating, no stiffness or accuracy claim: no machine's mass, forces or way tolerances are on file, so the bed is not sized
against them. Levelling, grouting and the way profile a given machine needs (V, dovetail or linear guides) come with that
machine's own version of the bed. No vendor names, no label.

## Outputs (out/)
`bed-cast.lsp` · `.glb` (pivot on `ways`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r49, unattended) |
