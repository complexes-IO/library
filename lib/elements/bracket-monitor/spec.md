# bracket-monitor · v1.1 · display bracket, wall plate and tilting 100 × 100 head

**What** Display bracket for the lab bench's back-board and the operator station: a wall plate screwed to the surface, a 200 mm
arm, and a head that tilts on a hinge and takes a display by its rear hole pattern.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, validation.json) describes a catalogue product; this element is not built from it.
**Units / frame** mm, Z up. Origin: surface mount: the wall plate's back face y = 0 on the mounting surface, its centre x = 0,
z = 0; the arm runs toward −y.
**Built with** toolkit 1.3 · AutoLISP command `BRKMON` · no parameters.

## Mechanism
`tilt` (rotate about +x through the hinge axis at y = −204, z = 0; −20° to +20°): the head plate, its two sleeves and ears. The
sleeves sit beside the arm's knuckle with a 0.5 axial gap, and the head plate's back face is 16 from the axis (the knuckle's
radius is 12), so the head clears the arm over the whole range.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| wall screws | 4 × M6, Ø6.6 holes | ISO 273 medium (H13), lib/standards/holes.csv |
| display screw holes | 4 × Ø4.5, the medium clearance hole for an M4 | ISO 273 medium (H13), lib/standards/holes.csv (the hole for an M4 only; the M4 itself: the row below) |
| display hole pattern and screw size | 100 × 100, 4 × M4 | **Assumption (B)** (a fit: the display's screws meet it): the common display mounting pattern and the screw it takes; the VESA standard (MIS-D) that defines both is not on file, and ISO 273 gives only the hole for a chosen screw. Both come from the standard when it is put on file (a minor version if either differs) |

## Its own sizes (design choices)
| item | value |
|---|---|
| wall plate | 150 × 150 × 4, screws at 120 × 120 |
| arm | 40 × 40, 200 from the plate face to the hinge axis |
| knuckle | Ø24 × 60 on the arm's end |
| head plate | 120 × 120 × 4; sleeves Ø24 × 14 each side, 0.5 from the knuckle |
| tilt range | −20° to +20° |
| material | steel, RAL 7035 powder coat |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
Each 4-hole pattern carries a declared position tolerance at MMC (features.csv): the wall plate Ø0.5 (H − F = 6.6 − 6 = 0.6), the
head Ø0.4 (H − F = 4.5 − 4 = 0.5). The ISO 2768-m general tolerance of the 141 to 170 mm spans (±0.5, a Ø1.41 zone) would
not hold either pattern, so the position tolerance is stated.

## Named nodes
`tilt` (rotate, above). Colliders `body`, `tilt`.

## Materials by layer
`M-STEEL-7035` all parts.

## Notes
No load rating and no safety claim (the display's mass is not specified).

## Outputs (out/)
`bracket-monitor.lsp` · `.glb` (pivot on `tilt`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r4) |
| 1.1 | the reviewer's 1.0 finding 1 (lib/reviews/elements/bracket-monitor-1.0.md), text only: the display screw size M4 moves into the display pattern's open figure (class B, VESA MIS-D not on file); ISO 273 is cited for the Ø4.5 hole only. Part, nodes, origin and cut-outs as 1.0, so a minor (mech-r25) |
