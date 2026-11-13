# beam-runway · v1.1 · monorail I-beam 6000 × 200 × 400 (welded: flanges 200 × 20, web 20) on two hanger plates 300 × 300 × 20, running flange as node track, four end stops

**What** A monorail beam for a chain hoist: the beam hung from the building that an underhung trolley runs along, with the hoist
hanging from the trolley. A welded I-section (top flange, web, bottom flange) hung by two hanger plates on its top flange; the
trolley's wheels run on the bottom flange, either side of the web, and a pair of end stops on that flange at each end keeps
them on the beam. hoist-chain-electric in lib/machines-factory.txt (line 75) lists hoist-chain, trolley, pendant-crane,
beam-runway, two limit switches, motor-brake and contactor-reversing; a BOM places the trolley on this beam's `track`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks beam-runway own_design
"yes"). No product was matched and no vendor file was opened. The beam has no hole, thread or standard interface; every size is
a design choice.
**Units / frame** mm, Z up. Origin: the bottom (running) flange's underside z = 0 at the beam's centre x = 0, y = 0; the beam's
length (the trolley's travel) along x. The running flange's top plane, the trolley wheels' seat, is at z = 20; the hanger plates'
top plane, the fixing to the building, is at z = 420.
**Built with** toolkit 1.3 · AutoLISP command `BEAMRUNWAY` · no parameters.

## Mechanism and the trolley's seat
`track` (fixed): the bottom flange, the running flange. Its pivot is the centre of the flange's top plane (0, 0, 20) with the axis
+z: an underhung trolley element is placed there with its own origin on that plane and runs along x on its own nodes, its wheels
on the flange either side of the web, so a BOM row reads `<tag>.track`. The beam itself has no moving part; the travel belongs to
the trolley.

## What it meets
| what | how |
|---|---|
| the building's structure or its hanger brackets (not built) | the beam hangs by its two hanger plates' top faces (z = 420, x −2150 to −1850 and 1850 to 2150). How a bracket or hanger rod holds a plate (bolts, clamps) belongs to that element, so the plates have no hole for it |
| trolley (not built; inventory row for crane-bridge and hoist-chain-electric) | an underhung trolley: its wheels run on the running flange's top plane (z = 20) either side of the web (web y −10 to 10, flange to y ±100), along x between the end stops. The flange is 200 wide and 20 thick, a design choice; the wheels are matched to it when the trolley is built. crane-bridge's trolley runs on top of girder-bridge's rail instead, so the trolley row serves two different seats |
| hoist-chain (not built) | hangs from the trolley, never from the beam |
| the two limit switches, conductor bar, pendant | belong to the hoist system: not built here, no bracket or hole for them |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| beam | welded I-section 400 high (z 0 to 400), 6000 long (x −3000 to 3000): flanges 200 wide (y −100 to 100) and 20 thick, web 20 thick (y −10 to 10) between them (z 20 to 380) | an I-section with a wide bottom flange is the usual monorail form; 6000 is the track's length as a design choice, and a hoist's own version of the beam takes the length its bay needs. Plates welded up to sizes of our own, so no rolled-section table is claimed |
| running flange | the bottom flange (z 0 to 20), 90 of flange each side of the web | the trolley's wheels run on its top face; drawn as its own fixed node, `track`, so the BOM names the seat |
| hanger plates | 300 along the beam, 300 across it (y −150 to 150), 20 thick (z 400 to 420), centred at x −2000 and 2000 | two hanging points 4000 apart with 1000 of beam beyond each; 50 wider than the flange each side for a bracket to hold |
| end stops | 60 along the beam, 70 across (y 10 to 80 and −80 to −10), 80 high (z 20 to 100), against the web on the running flange, one each side at each end (x ±2940 to ±3000), flush with the beam's ends | a block in each wheel path beyond the travel; 20 of flange left outside each stop. No buffer or energy figure is stated |
| colour | yellow (the library's M-YELLOW layer) | a design choice for lifting gear, as girder-bridge and runway-beam; it carries no marking or safety claim |
| stiffeners, splice plates, hanger brackets or rods, conductor bar, limit switch strikers | not drawn | they belong to the hoist system and the building |

## Named nodes
`track` (fixed, above). Colliders follow the solids: `web` (y −10 to 10, z 20 to 380), `top-flange` (y −100 to 100, z 380 to 400),
`stop-a` and `stop-b` (at x −3000 to −2940 and 2940 to 3000: the two end stops and the web between them, y −80 to 80, z 20 to 100),
`hanger-a` and `hanger-b` (the hanger plates) and `flange` (the running flange). The space the trolley's wheels take, either side
of the web above the running flange and between the stops, lies in no collider, so a trolley placed on `track` stands clear of the
beam's colliders along its travel.

## Materials by layer
`M-YELLOW` every part: the running flange, web, top flange, hanger plates and end stops (painted).

## Notes
No load rating: no hoist capacity, wheel load, flange bending, deflection, duty class or fatigue figure is stated, and the beam is
not sized against one. A monorail is designed to its standard by whoever builds that hoist system and building; this element gives
the hoist's model its track and the trolley's seat. No vendor names, no label.

## Outputs (out/)
`beam-runway.lsp` · `.glb` (pivot on `track`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r84, unattended) |
| 1.1 | colliders only (review beam-runway-1.0 finding 1): the one `girder` box, which filled the trolley's seat either side of the web, replaced by `web`, `top-flange`, `stop-a` and `stop-b`; no solid, node, origin or extent changed (mech-r86, unattended) |
