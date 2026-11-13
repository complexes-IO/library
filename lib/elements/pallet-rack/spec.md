# pallet-rack · v1.1 · pallet rack bay 2492 × 1067 × 2500, two beam levels, two pallets per level

**What** One bay of selective pallet rack: two upright frames (front and back upright, horizontal and diagonal bracing,
footplates with floor anchors) and a front and back beam at each level. Each level takes two pallets side by side, 1016 face to
the aisle, plus two on the floor. The outbound conveyor and pallet rack bay systems place it (lib/inventory.csv).
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match), sized around the pallet element
built in the same round. No vendor file was opened. The folder's acquisition record (metadata.json, validation.json) describes a
catalogue product; this element is not built from it. Rack design standards (EN 15512, ANSI MH16.1) are not on file: nothing is
taken from them and no load rating is claimed.
**Units / frame** mm, Z up. Origin: floor plane z = 0 at the front-left corner of the left frame's front upright; the beams run
along +x, the frames' depth along +y, the aisle (front) toward −y. The footplates stand 35 outside the uprights.
**Built with** toolkit 1.3 · AutoLISP command `PRACK` · parameters `levels` (2), `pitch` (1100: the beam tops at 1100, 2200, ...).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| pallet footprint | 1219 × 1016 | lib/elements/pallet (1.1). **Assumption (B)**, inherited: pallet 1.1 marks its footprint so (ISO 6780 not on file; lib/inventory.csv names the size). The clear beam length and the frame depth below follow from it. Closed with the pallet's: when ISO 6780 is on file and the pallet's figure changes, a version here follows it |
| floor anchors | 2 × M12 per footplate, Ø13.5 holes | ISO 273 medium (H13), lib/standards/holes.csv |
| anchor seat (room for the anchor's nut, washer and the tool that turns it) | the holes 21.2 from the upright's corner, 20 from the plate's edges (below) | **NOT ON FILE (B)**: no fastener table (nut and washer sizes, ISO 4032 / ISO 7089) is on file, so that the seat fits the anchor is not checked against a figure. Closed when lib/standards/fasteners.csv is on main: size the seat from it, a version here if it does not fit |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| clear beam length | 2332 | 2 × 1016 pallets + 3 × 100 clear space (at each upright and between the pallets) |
| frame depth | 1067 | the pallet's 1219 less a 76 overhang past the front and back beams |
| upright | 80 × 80 box, 2500 high, perforations not modelled | |
| bracing | 40 × 30, horizontals at 200 and 2300, four diagonals in a zig-zag | |
| beams | 120 × 50 box, front and back, tops at `pitch` × level | 1100 gives 980 between a beam's top and the next beam's underside (2200 − 120 − 1100), and the same 980 from the floor to the first beam's underside; above a 144 pallet that leaves 836 for its load and the lift-off. Rack clearances (EN 15620, ANSI MH16.1) are not on file, so no minimum is claimed |
| footplates | 150 × 150 × 6 galvanised, centred under the upright; the two anchors on the plate's diagonal (front-left and back-right), 55 from the upright's centre in x and in y | 55 is where a hole is as far from the upright's corner (√2 × 15 = 21.2) as from the plate's edges (75 − 55 = 20): the balance point is 54.5, rounded up. 1.0's anchors, 100 apart along x, stood 10 from the upright's faces |
| colours | uprights and bracing blue, beams yellow | |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The checker takes all eight Ø13.5 holes as one pattern across the bay (2.4 m). Each footplate's pair is declared at position
Ø1.2 at MMC (features.csv; H − F = 13.5 − 12 = 1.5), with the footplate as its datum: the anchors are drilled through the placed
plates, so the holes of different plates are not a fit with each other.

## Named nodes
none (nothing moves). Colliders: `frame-0`, `frame-2412` (each upright frame), `beam-<level>-front`, `beam-<level>-back`, so
pallets and forks pass between them in the twin.

## Materials by layer
`M-BLUE` uprights and bracing · `M-YELLOW` beams · `M-GALV` footplates.

## Notes
No load rating and no safety claim (no beam or frame capacity, no load sign). Beam connectors and safety locks are not modelled:
the beams butt the uprights' inner faces.

## Outputs (out/)
`pallet-rack.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r4) |
| 1.1 | review pallet-rack-1.0 findings 1 and 2 (mech-r22): the beam clearance corrected to 980 (836 above a 144 pallet; 1.0 said 956, leaving out the beam's depth); the anchors moved from x ± 50 (10 from the upright's faces) to the footplate's diagonal, ± 55 in x and y; the anchor seat marked open, class B, until a fastener table is on file; the pallet footprint marked as an open figure inherited from the pallet, class B. A minor: origin, nodes, colliders, extents and the hole count are 1.0's; only the eight hole positions move |
