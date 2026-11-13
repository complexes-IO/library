# robot-pedestal · v1.0 · robot pedestal 600 × 600 × 700, mounting face 400 × 400

**What** Steel pedestal that raises an industrial robot's base to 700 above the floor in the robot cell: a base plate anchored to
the floor, a 300 × 300 column with four gussets, and a 400 × 400 mounting plate whose top face is the robot's seat.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, validation.json) describes a catalogue product; this element is not built from it.
**Units / frame** mm, Z up. Origin: floor plane z = 0 at the base plate's centre, which is the robot's axis; front toward −y.
**Built with** toolkit 1.3 · AutoLISP command `RPED` · no parameters.

## Mechanism and the robot's seat
`mount` (fixed): the mounting plate. Its pivot is the centre of its top face (0, 0, 700) with the axis +z: a robot element is
placed there with its own base origin, so a cell's BOM row reads `<tag>.mount`.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| floor anchors | 4 × M12, Ø13.5 holes at 500 × 500 | ISO 273 medium (H13), lib/standards/holes.csv |
| the robot's base bolt pattern (hole count, circle, size, dowel holes) | NOT ON FILE (B) | class B, a fit (OPERATING.md 6: fits and envelope; mech-r15). No robot element is on file; the mounting plate is blank in this version, and the holes come as a minor version when the robot element (its datasheet) is on file |

## Its own sizes (design choices)
| item | value |
|---|---|
| mounting face height | 700 above the floor |
| base plate | 600 × 600 × 25 |
| column | 300 × 300 closed box |
| gussets | four, 130 × 150 × 12, on the column faces' centre lines |
| mounting plate | 400 × 400 × 25, galvanised |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.2 at MMC (features.csv; H − F = 13.5 − 12 = 1.5). The ISO 2768-m
general tolerance of their 707 mm diagonal (±0.8, a Ø2.26 zone) would not hold the pattern.

## Named nodes
`mount` (fixed, above). Colliders `body`, `mount`.

## Materials by layer
`M-STEEL-7035` base plate, column, gussets · `M-GALV` mounting plate.

## Notes
No load rating and no safety claim: the robot's mass, reach and moments are not on file, so the pedestal is not sized against
them. Grouting, levelling screws and cable pass-throughs are not modelled.

## Outputs (out/)
`robot-pedestal.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r4) |
