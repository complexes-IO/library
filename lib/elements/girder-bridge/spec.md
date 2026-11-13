# girder-bridge · v1.0 · bridge crane box girder 8000 × 400 × 700 on two end seats 400 × 700 × 30, trolley rail 50 × 50 with two end stops

**What** A bridge crane girder: the beam that spans the bay between the two runways and carries the trolley and its hoist. A
welded box girder on a seat plate at each end, with a square-bar trolley rail along its top and an end stop beyond each end of
the rail. crane-bridge in lib/machines-factory.txt (line 74) lists girder-bridge, runway-beam, two end trucks, the wire rope
hoist and its trolley; the end trucks carry the girder along the runways on its seats, and a BOM places the trolley on the
girder's `rail`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks girder-bridge own_design
"yes"). No product was matched and no vendor file was opened. The girder has no hole, thread or standard interface; every size
is a design choice.
**Units / frame** mm, Z up. Origin: the seats' underside z = 0 at the girder's centre x = 0, y = 0; the girder's length (the
crane's span) along x. The trolley rail's top plane, the trolley's seat, is at z = 780.
**Built with** toolkit 1.3 · AutoLISP command `GIRDERBRIDGE` · no parameters.

## Mechanism and the trolley's seat
`rail` (fixed): the trolley rail. Its pivot is the centre of the rail's top plane (0, 0, 780) with the axis +z: a trolley element
is placed there with its own base origin and moves along x on its own nodes, so a BOM row reads `<tag>.rail`. The girder itself
has no moving part; its own travel along the runways belongs to the end trucks.

## What it meets
| what | how |
|---|---|
| the two end trucks (end-truck, not built) | the girder stands on its two seats' undersides (z = 0, x ±3600 to ±4000). How an end truck locates and holds a seat (bolts, fitted bolts, shear blocks) belongs to that element, so the seats have no hole for it |
| the trolley (trolley, not built) | runs on the rail's top plane (z = 780) between the end stops, along x on its own nodes. The rail is a 50 × 50 square bar, a design choice; the trolley's wheels are matched to it when the trolley is built |
| runway-beam (not built) | the end trucks run on it; the girder never touches it |
| the wire rope hoist, pendant, festoon, drives, walkway | belong to the crane: not built |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| girder | box section 400 wide (y −200 to 200) and 700 high (z 30 to 730), 8000 long (x −4000 to 4000) | a closed box section for a factory bay; 8000 is the crane's span as a design choice, and the crane's own version of the girder takes the span its bay needs |
| seats | 400 along the girder, 700 across it (y −350 to 350), 30 thick (z 0 to 30), one under each end, flush with the girder's ends (x ±3600 to ±4000) | 150 each side of the girder to seat on an end truck |
| trolley rail | square bar 50 × 50 (y −25 to 25, z 730 to 780) on the girder's centre line, from x −3890 to 3890 | one rail on top of a single box girder; its ends 10 short of the stops |
| end stops | 100 along the girder, 300 across it (y −150 to 150), 150 high (z 730 to 880), one at each end (x ±3900 to ±4000), flush with the girder's ends | a block beyond each end of the rail; 100 above the rail's top. No buffer or energy figure is stated |
| colour | yellow (the library's M-YELLOW layer) | a design choice for a crane; it carries no marking or safety claim |
| body | drawn by its outside: a welded box girder is closed at its ends, its diaphragms and stiffeners are not seen | the model shows what can be seen |
| diaphragms, stiffeners, camber, rail clips, buffers, walkway, lifting lugs | not drawn | they belong to the crane that is built on the girder |

## Named nodes
`rail` (fixed, above). Colliders `seat-a` and `seat-b` (the end seats), `girder` (the box girder), `stop-a` and `stop-b` (the end
stops) and `rail-bar` (the rail).

## Materials by layer
`M-YELLOW` the seats, girder and end stops (painted) · `M-SILVER` the trolley rail (bare steel, shown in the library's bright-metal
layer).

## Notes
No load rating: no safe working load, deflection, camber, duty class or wheel load is stated, and the girder is not sized against
one. A crane's girder is designed to its standard by whoever builds that crane; this element gives the crane's model its girder
and the trolley's seat. No vendor names, no label.

## Outputs (out/)
`girder-bridge.lsp` · `.glb` (pivot on `rail`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r82, unattended) |
