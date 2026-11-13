# door-oven · v1.0 · oven door, double, insulated leaves 100, for oven-cure's opening 1800 × 2100, frame 2000 × 2200

**What** The door of oven-cure, the batch powder cure oven: a fixed door frame round the oven's door opening and two insulated
leaves hung on it, which open outward to let a cart of coated parts roll in at floor level and close the oven for the cure.
oven-cure 1.0 models the opening and leaves the door to this element (its spec.md, "What it meets"); the systems of
lib/machines-factory.txt that list oven-cure (oven-cure and powder-coating-system) place the two together, at the same origin.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks door-oven own_design
"yes", "insulated oven door"). No product was matched and no vendor file was opened. The opening's figures come from oven-cure
1.0; every other size is a design choice.
**Units / frame** mm, Z up. Origin: oven-cure's, the floor z = 0 under the middle of the door opening, y = 0 the oven's front
face; the door stands on that face toward −y, the oven toward +y. Extents x ±1000, y −210 to 0 (the handles' front), z 0 to 2200.
**Built with** toolkit 1.3 · AutoLISP command `OVENDOOR` · no parameters.

## Mechanism
`door-l` and `door-r`: each leaf rotates about its outer back vertical edge, the line x = ∓1000, y = −50 (the frame's front face),
z up: `door-l` 0 to −110° about +z, `door-r` 0 to +110°, so each free edge swings outward (−y) and round to its own side. Every
point of a leaf stays at x ≤ −5 (`door-l`) or x ≥ 5 (`door-r`) through the travel, so the two never meet, whichever opens first;
up to 90° every point stays at y ≤ −50, in front of the frame, and from 90° to 110° only the corner by the hinge goes behind that
plane, and only outside x ±1000, beside the frame, never into it; at 110° the leaf's back corner is 15.8 in front of the oven's
face (y = 0). The
twin reads the two leaves' angles (closed at 0). The hinges, the latch and the seal are not drawn in this version: a hinge and a
latch are later own designs, placed in a later version; the interlock that stops the oven with a leaf open is the system's
(machines-factory.txt's oven-cure line lists guard-interlock).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the door opening | 1800 wide × 2100 high (x ±900, z 0 to 2100) at floor level in oven-cure's front wall, its front face y = 0 | oven-cure 1.0 `DOOR_X`, `DOOR_H` (element.py loads oven-cure, so the two cannot drift apart) |
| the oven's front face | y = 0; the frame stands on it, x ±1000, z 0 to 2200, inside the front wall's x ±1100 and under its top at z 2300 | oven-cure 1.0 (front wall y 0 to 100, x ±1100, z 0 to 2300) |
| the leaves' panel | 100 thick, the oven's insulated panel | oven-cure 1.0 `T` |
| the floor | the jambs stand on z = 0; the leaves clear it by 10 | the floor is the system's |
| the frame's fixing to the oven | not drawn: oven-cure 1.0 has no fixing holes round its opening; the fixing goes into both in a later version | a later version of both |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| frame | two jambs 100 wide × 50 deep × 2200 high (x ±900 to ±1000) on the floor, a head 1800 × 50 × 100 between them (z 2100 to 2200), all y −50 to 0, M-STEEL-7035 | the edge of the opening the leaves close on, and the hinges' place |
| leaves | two, each 995 wide (x −1000 to −5 and 5 to 1000), 2190 high (z 10 to 2200), 100 thick (y −150 to −50), M-STEEL-7035 | the oven's own panel; each laps the opening by 100 at its side and at the head |
| between the leaves | 10 (x −5 to 5) | the seal's place, not drawn; the leaves never touch |
| above the floor | 10 (z 0 to 10) | the leaves swing clear of the floor |
| swing | 0 to 110° outward each | open past square for the cart; at 110° the leaf's back corner is still 15.8 in front of the oven's face |
| handles | one per leaf, a vertical bar 20 × 20 × 400 (z 900 to 1300) on two standoffs 20 × 40 × 20, 60 in from the free edge, M-ZINC | to pull the leaf open |
| hinges, latch, seal, fixing | not drawn | later own designs and versions |

## Where it stands (the system's)
The door's insulation value and its outside skin temperature, the seal, the oven's temperature, and the interlock and every
fire, explosion and safety figure of an oven are figures of the system and its standards, none of which is on file
(lib/standards/sources.csv lists no oven standard). This element makes no temperature, thermal, seal or safety claim and names no
such figure.

## Named nodes
`door-l`, `door-r` (rotate, above); the frame is the fixed `body`. Colliders `jamb-l`, `jamb-r`, `head` (the frame) and `leaf-l`,
`leaf-r` (each leaf with its handle, closed); none is named like a node.

## Materials by layer
`M-STEEL-7035` the frame and the leaves (painted sheet skins, light grey, as oven-cure). `M-ZINC` the handles.

## Notes
No load rating and no safety claim. No vendor names, no label. Placing the door on oven-cure in one element (a door node on the
oven) would be oven-cure 2.0; the systems place the two side by side at the same origin instead.

## Outputs (out/)
`door-oven.lsp` · `.glb` (pivots on `door-l`, `door-r`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r65, unattended) |
