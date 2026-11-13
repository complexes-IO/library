# column · v1.1 · machine column 400 × 400 × 1600 on a 600 × 600 base flange, two flat front ways 60 wide, 8 × M12

**What** A machine column: an upright box-section body on a base flange, with two flat machined ways down its front face. The
machines of lib/machines-factory.txt built round a column (pillar and radial drills, vertical and horizontal mills, horizontal
borers, machining centres) carry their head, knee or saddle on ways of this kind; a BOM places that part on the column's `ways`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks column own_design
"yes"). No product was matched and no vendor file was opened. The base flange's bolt holes are on file (ISO 273); every other
size is a design choice.
**Units / frame** mm, Z up. Origin: the base flange's underside z = 0 at the column's centre x = 0, y = 0; the column's height
along z; front (the ways) toward −y. The ways' front plane, the head's seat, is at y = −225.
**Built with** toolkit 1.3 · AutoLISP command `MCOLUMN` · no parameters.

## Mechanism and the head's seat
`ways` (fixed): the two flat ways. Its pivot is the centre of the ways' front plane (0, −225, 980) with the axis −y: a head,
knee or saddle element is placed there with its own base origin and moves along z on its own nodes, so a BOM row reads
`<tag>.ways`. The column itself has no moving part.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| base bolts | 8 × M12, Ø13.5 holes through the base flange, on a 500 × 500 square (x and y −250, 0, 250; the centre left out, under the body) | ISO 273 medium (H13), lib/standards/holes.csv. The bolts and what they meet (the machine's base or bed, or floor anchors) belong to the assembly: not built. The mate's side is a requirement on it: clearance holes, ISO 273 medium, with nuts, or anchors drilled at installation (a floating fastener, GD&T below) |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The eight base holes carry a declared position tolerance Ø1.2 at MMC to A, the base flange's underside, the holes located to each
other (features.csv; H − F = 13.5 − 12 = 1.5). The ISO 2768-m general tolerance of their 707 mm diagonal (±0.8,
lib/standards/general-tolerances.csv row m 400-1000; a Ø2.3 zone) would not hold the pattern, so the flange is drilled in one
set-up with the ways.

The Ø1.2 holds only for a floating fastener: bolts through clearance holes in both parts, with nuts. So the column requires its
mate to have clearance holes, ISO 273 medium (Ø13.5 for M12), with nuts; floor anchors drilled at installation are not a pattern
fit and meet the requirement too. A mate with tapped holes is a fixed fastener (ASME Y14.5-2018 Appendix B, the fixed-fastener
case: the two parts share H − F, Ø0.75 each); it is not this version's mate and takes a version of the column that declares
Ø0.75. ASME Y14.5 is not a row in lib/standards/sources.csv (the core's open item, review mech-r47 finding 2), and GDT-010 checks
every pattern as floating, so this requirement is stated here, not checked.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base flange | 600 × 600 × 25, 100 wide each side of the body | carries the bolts outside the body, where a spanner reaches them |
| body | 400 × 400, from the flange (z 25) to its top face (z 1600) | a closed box section for the mid-size drills and mills of the factory list |
| ways | 2, flat, 60 wide, 25 proud of the body's front face (y −200 to −225), centres at x ±130 (260 apart), from z 400 to z 1560 (40 short of the top) | flat ways carry a head on both; the lowest 400 is left for the table or work below the head |
| bolts | eight, at the corners and mid-sides of a 500 × 500 square (mid-flange: 50 from the body, 50 from the flange's edge) | no span between bolts longer than 250 |
| body | drawn by its outside: a cast or welded box section is closed at its ends, its cores and ribs are not seen | the model shows what can be seen |
| ribs, cores, scraping of the ways, gib strips, counterweight and chain, way covers | not drawn | they belong to the machine that is built on the column |

## Named nodes
`ways` (fixed, above). Colliders `base` (the flange), `body` (the box body) and `ways` (the two ways and the gap between them).

## Materials by layer
`M-STEEL-7035` the base flange and body (painted RAL 7035) · `M-SILVER` the ways (bare machined steel, shown in the library's
bright-metal layer).

## Notes
No load rating, no stiffness or accuracy claim: no machine's mass, forces or way tolerances are on file, so the column is not
sized against them. Whether it stands on a bed, a base or the floor, and the way profile a given machine needs (V, dovetail,
box or linear guides), come with that machine's own version of the column. No vendor names, no label.

## Outputs (out/)
`column.lsp` · `.glb` (pivot on `ways`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r50, unattended) |
| 1.1 | review column-1.0 finding 1, text only: the base holes' Ø1.2 stated as a floating fastener, with its requirement on the mate (clearance holes ISO 273 medium with nuts, or anchors drilled at installation); a tapped mate takes a Ø0.75 version. No model change (mech-r60, unattended) |
