# hardware-cabinet · v1.0 · hardware cabinet 600 × 300 × 700, two doors, sixteen small-parts bins

**What** A sheet-steel cabinet for small parts (screws, nuts, washers, terminals) at the lab bench: a carcass 600 wide, 300 deep
and 700 high, fixed to a wall by four M6 screws through its back or stood on a bench, with four levels of four open bins inside
and two doors in front. The doors are the mechanism: the twin opens them by name.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, references/source.txt, validation.json, batch 19) describes three catalogue hardware
items (a hinge, a pull handle, a caster) filed under this id; this element is not built from them (lib/needs-em/mech.md, r29).
**Units / frame** mm, Z up. Origin: the carcass underside z = 0 at its front-left corner x = 0, y = 0. The person stands at −y;
the doors open toward −y; the back face y = 300 goes against the wall.
**Built with** toolkit 1.3 · AutoLISP command `HWCAB` · no parameters.

## Mechanism
`door-l` rotates about the carcass's front-left vertical edge (x 0, y 0), 0 to −110° about +z; `door-r` about the front-right
vertical edge (x 600, y 0), 0 to +110° about +z. Both free edges swing outward toward −y, away from each other. Each door node
carries its door and its handle. Closed, a door lies in front of the carcass (y −20 to 0), over the carcass edges, 3 from the other
door; through its travel every point of it stays outside the carcass (x < 0 for `door-l`, x > 600 for `door-r`, once it has left
y < 0). The hinges and catches are not modelled.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| wall-fixing hole | Ø6.6, four, M6 | ISO 273 medium (H13), lib/standards/holes.csv |

The M6 screws and wall plugs are not placed (no fastener element is built yet; EM's rule: the holes are modelled, a later version
places the part).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| carcass | 600 × 300 × 700 outside, 1.5 sheet; bottom and top full size, sides between them, back between the sides | reaches a bench's back edge without standing past a 762 deep bench top |
| levels | four; bin floors' tops at z 1.5 (the carcass bottom), 175.5, 349.5, 523.5 (shelves 1.5, full width and depth) | 174 pitch: a hand reaches into a bin under the shelf above |
| bins | four a level, 148.1 wide inside, 297 deep; front lip 50 high, dividers 80 high, 1.5 sheet | sixteen bins |
| doors | 2, each 298.5 × 20 × 700 (double wall), 3 apart, full height over the carcass edges; swing 0 to 110° | |
| handles | vertical bar 12 × 12 × 200 on two 12 × 15 × 12 standoffs, 27 proud of the door, centred at z 350, 40 from each door's free edge | cabinet-tool's handle section, upright |
| wall-fixing holes | x 50 and 550, z 100 and 600 in the back (500 × 500 centres); they open into the bottom and top levels' bins, so a screwdriver reaches them | |
| colours | carcass, shelves and bins RAL 7035, doors blue, handles zinc | as cabinet-tool |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four Ø6.6 wall-fixing holes are one pattern (500 × 500): position Ø0.5 at MMC (features.csv; H − F = 6.6 − 6.0 = 0.6), datum A
the back's outer face, the four holes located to each other.

## Named nodes
`door-l`, `door-r` (rotate, above). Colliders `body` (the carcass) and one per door (`door-l`, `door-r`, the handle included).

## Materials by layer
`M-STEEL-7035` carcass, shelves, bin lips and dividers · `M-BLUE` doors · `M-ZINC` handles.

## Notes
No load rating (no shelf or wall-fixing load is claimed) and no safety claim; no lock. No vendor names; no label in this version.

## Outputs (out/)
`hardware-cabinet.lsp` · `.glb` (pivots on the two doors) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r29, unattended; lib/rounds/mech/next.md #4) |
