# bolster · v1.0 · press bolster plate 1000 × 700 × 80, plain top, 6 × M12 fixing holes, central knock-out passage Ø100

**What** A press bolster plate: the thick machined plate bolted to the bed of a hydraulic press that the lower die stands on.
The presses of lib/machines-factory.txt (press-hydraulic, press-shop-hydraulic) carry their lower die on a plate of this kind; a
BOM places the die on the bolster's top face, and the bolster on the press bed (frame-welded's `mount` in press-hydraulic).
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks bolster own_design
"yes"). No product was matched and no vendor file was opened. The fixing holes are on file (ISO 273); every other size is a
design choice.
**Units / frame** mm, Z up. Origin: the plate's underside z = 0 (the press bed's top face) at the plate's centre x = 0, y = 0;
the long side along x; front toward −y. The top face, the lower die's seat, is at z = 80.
**Built with** toolkit 1.3 · AutoLISP command `BOLSTER` · no parameters.

## Mechanism and the die's seat
None: the plate is one fixed body. The lower die element is placed with its own base origin at the centre of the top face,
(0, 0, 80) from the bolster's origin. The bolster has no moving part; the press's ram and ejector are the press's own elements.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| fixing holes | 6 × M12, Ø13.5 through the plate, three a side, at 900 × 600 (x −450, 0, 450; y ±300) | ISO 273 medium (H13), lib/standards/holes.csv. The screws and their counterbores are the press's: placed by the assembly, not built here |
| press bed | the plate's underside, 1000 × 700, fits frame-welded 1.0's 1200 × 800 seat with 100 / 50 to spare | frame-welded spec.md (its top plate) |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The six fixing holes carry a declared position tolerance Ø1.2 at MMC to A, the plate's underside (the press bed's face), the
holes located to each other (features.csv; H − F = 13.5 − 12 = 1.5). The ISO 2768-m general tolerance of their 1082 mm diagonal
(±1.2, lib/standards/general-tolerances.csv row m 1000-2000; a Ø3.4 zone) would not hold the pattern, so they are drilled in
one set-up and the press bed is drilled from the plate. The knock-out passage is not a fastener hole (features.csv, kind own).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| plate | 1000 × 700 × 80 | a working area for the dies of a mid-size press of the factory list; 80 thick, in proportion to its size (no load claim is made for it); fits frame-welded's seat |
| fixing holes | three a side at x −450, 0, 450, y ±300 (50 in from the ends and the long edges) | a hole at each corner and one at mid-length a side, outside any die's footprint on the plate's centre |
| knock-out passage | Ø100 through, at the plate's centre | room for the press's ejector or knock-out rod under the die's centre |
| top | plain, no die-clamping slots in this version | the die-clamping T-slots wait on a T-slot table (ISO 299, not on file; lib/needs-em/mech.md item 66): a later version adds them. Dies are clamped meanwhile by the assembly's own clamps at the plate's edges |
| finish | bare machined steel all over | a bolster is machined on both faces; shown in the library's bright-metal layer |

## Named nodes
None (one fixed body). Collider `plate` (the plate's outside).

## Materials by layer
`M-SILVER` the plate (bare machined steel, the library's bright-metal layer; the library has no `M-STEEL` render material).

## Notes
No load rating, no flatness, parallelism or stiffness claim: no press force, die mass or bed opening is on file, so the plate is
not sized against them. The T-slots, the screws that hold the plate to the bed, the die clamps and the ejector come with the
press's assembly or with a later version of the bolster. No vendor names, no label.

## Outputs (out/)
`bolster.lsp` · `.glb` (one body, no pivot) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r57, unattended; EM's inventory pin 3, press-hydraulic first) |
