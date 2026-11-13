# clamp-screw · v1.1 · screw clamp of a terminal

**What** The clamp of a terminal as a part: a wire end's state in it (made, marginal with insulation under the clamp or a loose screw, open, blocked by size, high-r when over-torqued, corroded or nicked) is decided by `toolkit/contact.py` `terminate()`, not drawn.
**Class** contact · **Baseline** see element.py BASELINE; nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: the cage's mouth on the wire axis; the wire goes in along +y; the screw head toward −z.
**Built with** toolkit 1.3 · AutoLISP command `CLAMP` · `size_min`, `size_max` (mm²: 0.33, 5.26 = 22-10 AWG), `torque_min`, `torque_max` (N m: 0.5, 0.8), `strip` (10), `condition` (ok | corroded).

## Dimensions
| item | value |
|---|---|
| cage | 5.1 x 7.5 (along the wire) x 10.4 (term-4mm STEP read-back: cage 5.1 x 10.4 x 7.5) |
| window | 4.0 x 5.0 through the cage along the wire |
| screw | M3 (Assumption), head Ø4.0 (STEP read-back), tip at the window floor when open |

## Figures and their sources
| figure | value | source |
|---|---|---|
| wire range (feed-through block) | 22-10 AWG = 0.33-5.26 mm² | McMaster 7641K21 page (term-4mm references) |
| wire range (ground block) | 22-12 AWG = 0.33-3.31 mm² | McMaster 7641K931 page |
| cage, screw head | 5.1 x 10.4 x 7.5; Ø4.0 | term-4mm STEP read-back |
| torque window | 0.5-0.8 N m | Assumption |
| grip (bare conductor under the clamp) | 5.0 | Assumption |

## Named nodes
`self` (kind contact: origin the mouth, axis into the cage, range (0.5, 7.5); extras gender clamp, size_min, size_max, grip 5.0, strip, window, torque, condition) · `screw` (rotate, 2 turns, lead 0.5, torque)

## Materials by layer
`M-ZINC` cage and screw · `M-CU-CORRODED` (condition corroded)

## Decals (Blender)
none

## Notes and assumptions
Torque window, strip length and grip are Assumption: the terminal maker states them (NOT ON FILE for term-4mm's class).

## Outputs (out/)
`clamp-screw.lsp` (solids only: the swept insulation or jacket is glTF only) · `.glb` (contact and port data in the node extras, `-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.1 | round 3 (2026-11-04): `cage_w` (a 5.0 ground block takes the ground STEP's 4.5 cage; 5.1 stood 0.05 proud of each side), the window follows it; fillet r 0.1 (class contact) |
| 1.0 | first build: the element layer reaches the wire and its termination (2026-11-03), toolkit 1.3 |
