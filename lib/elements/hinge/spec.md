# hinge · v2.0 · butt hinge 80 x 80 x 3, own design, three knuckles Ø12 on a Ø6 pin, moving leaf 0 to 180 degrees, 4 x M6 holes ISO 273

**What** A butt hinge: the pair of leaves on a pin that hangs a guard door, an oven door, a cabinet door or a hinged cover on its
frame. The fixed leaf is screwed to the frame and carries the two outer knuckles with the pin pressed through them; the moving leaf
is screwed to the door and carries the middle knuckle, bored 0.5 clear round the pin, so the door swings on it from closed (the
leaves flat in one plane) to folded right back (180 degrees). The inventory row lists it as "hinge" (made of four button head screws,
screw-iso7380) for the doors and covers of the machine rows (lib/machines-factory.txt); no system row names it on its own.
**Class** device · **Baseline** our own design, OPERATING.md 12 "Own designs" (EM, 2026-11-05): hinges are in its list and
lib/inventory.csv marks the row own_design "yes". No ETIM 10.0 class on file is a hinge (lib/standards/etim/classes.csv has a hinge
switch and hinged lids only) and no hinge standard is in lib/standards/sources.csv, so there are no class values and no standard's
figures to follow: the holes it meets are on file (ISO 273) and every other size is a design choice. No product was matched and no
vendor file was opened.
**Units / frame** mm, Z up: the pin's axis runs along z. Origin: the fixed leaf's mounting face plane (y = 0) under the pin's axis
at the hinge's mid-length (z = 0); the pin's axis is the line x = 0, y = 6 along z. −x is the fixed leaf (the frame's, x −40 to −6),
+x the moving leaf (the door's, x 6 to 40), +y the knuckle side (outside the door; the knuckles reach y 12), ±z along the pin (the
knuckles z ±40, the pin's ends z ±40.5). Extents x ±40, y 0 to 12, z ±40.5.
**Built with** toolkit 1.3 · AutoLISP command `HINGEBUTT` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| screw holes | 4 × M6, Ø6.6 through the leaves, two per leaf 25 from the pin's axis, staggered along the pin: the fixed leaf's at x −25, z ±28 (56 pitch), the moving leaf's at x 25, z ±8 (16 pitch) | ISO 273 medium (H13), lib/standards/holes.csv. M6 is this design's choice; the stagger is too (2.0, review hinge-1.0 finding 1): folded to 180 the moving leaf's holes land at x −25, z ±8, 20 along the pin from the fixed leaf's, so the two leaves' screw heads, which face each other across the 6 gap between the leaves' screw faces, never stand head to head; any head under Ø20 clears the other's, and a head under 6 high clears the other leaf's plain face (ISO 7380-1's head figures are checked when screw-iso7380 is placed; lib/standards/fasteners.csv is not yet on main); the screws are button head ISO 7380-1 (the inventory's made_of, screw-iso7380 x4, a common part not built yet: the holes are modelled, the part placed later) and the tapped or through holes in the door and the frame are the hosts' |
| the mounting faces | the leaves' undersides, y = 0, both in one plane at rest | design: a flat butt hinge, for a door whose edge lies flush with its frame when closed (the knuckle stands outside, y 0 to 12). A door set back from its frame takes a cranked leaf: another version |
| the pin's seat in the fixed knuckles | Ø6 bores, the Ø6 pin pressed in, features.csv kind `own` | design choice: the fixed leaf, its knuckles and the pin are one body |
| the moving knuckle's bore | Ø7 (0.5 clear round the Ø6 pin), features.csv kind `own` | design choice: the leaf turns free on the pin; no fastener and no standard size |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| leaves | steel 3.0 thick (y 0 to 3), 80 long along the pin (z ±40), each 40 wide from the pin's axis: the plate 34 wide (x 6 to 40, and −6 to −40) with a web 6 wide (x 0 to 6, and −6 to 0) over its own knuckle's length only; 80 × 80 open | a size that carries a guard or oven door panel (guard-panel, door-oven: 2.0 sheet on a 30 tube frame) on two hinges; 3.0 sheet keeps every free edge at 3 (the gate's fillet rule, Notes). The plate stops 6 from the axis so it clears the other leaf's knuckles (Ø12) through the whole swing; the web fills the gap where its own knuckle is |
| knuckles | three, Ø12 about the pin's axis at (0, 6), 26 long each with 1 between them: the fixed leaf's at z −40 to −14 and 14 to 40, the moving leaf's at z −13 to 13; the knuckle's underside is tangent to the mounting plane | equal knuckles share the length; Ø12 round a Ø6 pin leaves a 3 wall (2.5 at the Ø7 bore); the 1 gaps keep the knuckles' end faces apart |
| pin | Ø6 × 81, bright steel, z −40.5 to 40.5: its ends stand 0.5 proud of the outer knuckles | pressed through the fixed knuckles; the proud ends are a peened pin's heads drawn flat, and keep its end faces out of the knuckles' end planes (GEO-050). A lift-off pin (a pin fixed to one leaf and open above) is another version |
| swing | 0 to 180 degrees about the pin's axis, toward +y (the knuckle side) | the full fold of a flat butt hinge: at 180 the moving leaf lies back over the fixed one, knuckle side to knuckle side, 6 above it (y 9 to 12) |
| load, torque to swing, wear | not claimed | no figure is on file for them and the element is not sized against a load; a hinge for a door the twin counts as a guard still needs the door's own guard rule (ISO 14120), which is the door's, not the hinge's |

## Mechanism
One moving node, `leaf` (the moving leaf's plate, web and middle knuckle, one part): rotate about the pin's axis (x = 0, y = 6,
along z) through (0, 6, 0), range 0 to 180 degrees, toward +y. At 0 (closed, the rest position as modelled) the two leaves lie flat
in one plane, y 0 to 3, the door closed against its frame. At 90 the moving leaf stands out along +y (x 3 to 6, y 12 to 46); at 180
(open) it lies folded back over the fixed leaf (x −40 to −6, y 9 to 12). Through the swing the plate's nearest edge (x 6, y 3 at
rest) keeps 6.7 from the axis, 0.7 clear of the fixed knuckles (r 6); the middle knuckle turns on the pin 0.5 clear in its Ø7
bore and 1 clear of the fixed knuckles' end faces; the holes and the webs follow their plates. At 180 the leaves' screw faces
stand 6 apart (y 3 to 9) and the moving leaf's holes sit at z ±8 between the fixed leaf's at z ±28, so the screws placed in them
(screw-iso7380, later) reach the range end without their heads meeting (2.0). Nothing else is in its way; the
door and the frame are the hosts'. behaviour.csv: state `closed` (default) and `open` (manual toggle: the door swung by hand or
by its own actuator), pose of `leaf` at the range end in `open`.

## Named nodes
`leaf`: rotate about z through (0, 6, 0), range 0 to 180 degrees. Colliders: `fixed` (the fixed leaf's plate, x −40 to −6, y 0 to
3, z ±40), `knuckle` (x ±6, y 0 to 12, z ±40.5), `swing` (the moving leaf's plate, x 6 to 40, y 0 to 3, z ±40); none is named like
the node.

## Materials by layer
`M-ZINC` both leaves with their webs and knuckles (steel, zinc-plated) · `M-SILVER` the pin (bright steel).

## Decals (Blender)
"complexes.org" on the fixed leaf's underside, between its two holes.

## Notes
No vendor names, part numbers or marks. No load, torque or wear claim: no figure is on file for them and the element is not sized
against a load. Not drawn: the screws (placed later from screw-iso7380), the pin's peened heads (its ends are flat, 0.5 proud),
the door and the frame (the hosts'). No open figure: the holes it meets are on file (ISO 273) and the rest are design choices. A
hinge is in OPERATING.md 12's list of own designs and no dimensional standard for one is on file, so it is built as our own design
with no class values; a lift-off hinge, a cranked (offset) hinge, a weld-on bullet hinge, a concealed hinge or a torque hinge is
another version or another element.
The gate's fillet rule (fillet r 0.5 for a device, lib/toolkit/fillet.py): every free edge is 3 or longer (the leaves 3.0, the
webs 3.0, the pin's proud ends 0.5 tall on a Ø6 that is its own 81-long solid), so no edge falls in the 1.5 to 2.5 range that
reads under 90 % of its fillet volume (mech-r4, r98); the knuckle bores and the pin's seat are buried or free.

## Outputs (out/)
`hinge.lsp` · `.glb` (pivot on `leaf`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r99, unattended, 2026-11-11) |
| 2.0 | review hinge-1.0 finding 1: the screw holes staggered along the pin (fixed leaf z ±28, moving leaf z ±8, both 25 from the axis) so the button heads of the two leaves never meet when the hinge is folded to 180; a major (the cut-outs move). Nodes, origin, range, extents and every other size unchanged (mech-r107, unattended, 2026-11-12) |
