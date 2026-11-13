# runway-beam · v1.0 · crane runway plate girder 12000 × 400 × 700 (I-section) on two bearing plates 400 × 500 × 30, crane rail 50 × 50 with two end stops

**What** A crane runway beam: the beam that runs the length of a bay on the building's columns and carries a bridge crane's end
trucks. A welded plate girder (top flange, web, bottom flange) on a bearing plate under each end, with a square-bar crane rail
along its top and an end stop beyond each end of the rail. crane-bridge in lib/machines-factory.txt (line 74) lists
girder-bridge, runway-beam, two end trucks, the wire rope hoist and its trolley; a crane takes two runway beams, one each side of
its bay, and a BOM places each end truck on a runway's `rail`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks runway-beam own_design
"yes"). No product was matched and no vendor file was opened. The beam has no hole, thread or standard interface; every size is
a design choice.
**Units / frame** mm, Z up. Origin: the bearing plates' underside z = 0 at the beam's centre x = 0, y = 0; the beam's length
(the crane's travel) along x. The crane rail's top plane, the end trucks' seat, is at z = 780.
**Built with** toolkit 1.3 · AutoLISP command `RUNWAYBEAM` · no parameters.

## Mechanism and the end trucks' seat
`rail` (fixed): the crane rail. Its pivot is the centre of the rail's top plane (0, 0, 780) with the axis +z: an end truck
element is placed there with its own base origin and moves along x on its own nodes, so a BOM row reads `<tag>.rail`. The
runway itself has no moving part; the crane's travel along it belongs to the end trucks.

## What it meets
| what | how |
|---|---|
| the building's columns or their brackets (not built) | the beam stands on its two bearing plates' undersides (z = 0, x ±5600 to ±6000). How a bracket locates and holds a plate (bolts, slotted holes, shims) belongs to that element, so the plates have no hole for it |
| the end trucks (end-truck, not built) | run on the rail's top plane (z = 780) between the end stops, along x on their own nodes. The rail is a 50 × 50 square bar, a design choice (girder-bridge's trolley rail is the same bar); the wheels are matched to it when the end truck is built |
| girder-bridge 1.0 | spans between the two runways on the end trucks; it never touches the runway |
| a second runway beam | the crane's span sets how far apart the two runways stand; the BOM places them, this element doesn't |
| the crane's conductor bar, buffers on the trucks, walkway | belong to the crane: not built |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| beam | welded plate girder 700 high (z 30 to 730), 12000 long (x −6000 to 6000): flanges 400 wide (y −200 to 200) and 30 thick, web 20 thick (y −10 to 10) between them | an I-section, the usual runway form; 12000 is the bay's length as a design choice, and a crane's own version of the runway takes the length its bay needs. Plates welded up to sizes of our own, so no rolled-section table is claimed |
| bearing plates | 400 along the beam, 500 across it (y −250 to 250), 30 thick (z 0 to 30), one under each end, flush with the beam's ends (x ±5600 to ±6000) | 50 each side of the flange to seat on a bracket |
| crane rail | square bar 50 × 50 (y −25 to 25, z 730 to 780) on the beam's centre line, from x −5890 to 5890 | one rail on the top flange, over the web; its ends 10 short of the stops |
| end stops | 100 along the beam, 300 across it (y −150 to 150), 150 high (z 730 to 880), one at each end (x ±5900 to ±6000), flush with the beam's ends | a block beyond each end of the rail; 100 above the rail's top. No buffer or energy figure is stated |
| colour | yellow (the library's M-YELLOW layer) | a design choice for a crane, as girder-bridge; it carries no marking or safety claim |
| web stiffeners, rail clips, crane stop buffers, conductor bar, walkway | not drawn | they belong to the crane and the building that are built on the runway |

## Named nodes
`rail` (fixed, above). Colliders `plate-a` and `plate-b` (the bearing plates), `beam` (the plate girder's outline), `stop-a` and
`stop-b` (the end stops) and `rail-bar` (the rail).

## Materials by layer
`M-YELLOW` the bearing plates, flanges, web and end stops (painted) · `M-SILVER` the crane rail (bare steel, shown in the
library's bright-metal layer).

## Notes
No load rating: no wheel load, deflection, lateral load, duty class or fatigue figure is stated, and the beam is not sized
against one. A crane runway is designed to its standard by whoever builds that crane and building; this element gives the
crane's model its runway and the end trucks' seat. No vendor names, no label.

## Outputs (out/)
`runway-beam.lsp` · `.glb` (pivot on `rail`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r83, unattended) |
