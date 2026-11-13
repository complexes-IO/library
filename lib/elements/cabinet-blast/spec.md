# cabinet-blast · v1.0 · sandblast cabinet 1000 × 800 × 800 chamber on legs, sheet 2.0, viewing window, 2 × Ø180 glove-port openings, side door

**What** A sandblast cabinet: a closed work chamber of 2.0 sheet on four legs, in which an operator blasts a part by hand through
two glove ports, watching it through a window in the front wall. The part goes in through a door in the right side wall. The
chamber's floor is open over the abrasive hopper below it; its roof has an opening for the dust collector's duct. It is the
cabinet of the sandblaster system (lib/machines-factory.txt line 106: cabinet-blast (own), gun-blast, nozzle-blast, compressor-air,
frl, dust-collector, hopper-abrasive (own), lamp-machine, footswitch, glove-port, valve-air-shutoff).
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs: cabinets; lib/inventory.csv marks cabinet-blast
own_design "yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the floor z = 0 (the legs' underside) at the middle of the cabinet's width x = 0; y = 0 the
front wall's outer face, where the operator stands (toward −y); the depth toward +y. Extents x −500 to 549 (the door's handle),
y 0 to 800, z 0 to 1650.
**Built with** toolkit 1.3 · AutoLISP command `BLASTCAB` · no parameters.

## Mechanism
| node | kind | pivot | axis | range | what moves |
|---|---|---|---|---|---|
| `door` | rotate | (502, 680, 1250), the door's inner back vertical edge | +z | 0 to 90 degrees | the side door and its handle |

Shut (0), the door lies 2 clear of the right wall's outer face (x 502 to 522) and laps the loading opening by 30 on every side.
Opening, its front edge swings out to +x about its back edge; at 90 degrees it stands square to the wall, every point of it at
x 502 or more, so it never meets the wall. The hinges and the latch are not drawn, so the door touches nothing at rest (it rides on
its pivot).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the abrasive hopper | the chamber's open floor at z 850: inside x −498 to 498, y 2 to 798, between the four legs | hopper-abrasive (our own design, not built yet) is sized to this element when it is built; its fit is checked then |
| the glove ports | two round openings Ø180 in the front wall, centres x −250 and 250, z 1100 | glove-port (a new element, not built yet) is placed in them in a later version (OPERATING.md 12, own designs: the holes are cut, the part placed later); how a port fits the opening is checked when it is on file |
| the dust collector's duct | a round opening Ø150 in the roof, centre x 300, y 600 | dust-collector and duct-round are not built yet; the duct's fit is checked when they are on file |

No fastener hole is cut: the legs stand free on the floor (no anchor), and the lamp, gun, footswitch and air valve are placed by the
assembly.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| chamber | 1000 wide (x −500 to 500), 800 deep (y 0 to 800), 800 high (z 850 to 1650) | a bench-size cabinet for small parts blasted by hand; a design choice |
| sheet | 2.0 everywhere: side walls full depth under the roof, front and back walls between them, the roof over all four | a sheet cabinet; folds, stiffeners and seals are not drawn |
| legs | four, 50 × 50, 850 long, under the chamber's corners | the chamber's floor at z 850 leaves room for the hopper under it; a design choice, not sized against any load |
| floor | open | the abrasive falls through to the hopper; the grate is not drawn |
| front wall | two panels: the glove-port panel z 850 to 1300, the window panel z 1300 to 1648 | each panel carries one kind of opening |
| viewing window | cut-out x −350 to 350, z 1350 to 1600 (700 × 250); a clear pane 6 thick inside the wall, lapping 30 round it (y 2 to 8) | the operator sees the part between the gloves; the pane's grade and impact resistance are not stated |
| glove-port openings | Ø180, 500 apart, centres at z 1100 | two hands reach the part at the chamber's middle height; a design choice |
| loading opening | right wall, y 150 to 650, z 950 to 1550 (500 × 600) | a part goes in from the side while the operator stands at the front |
| side door | 560 × 660 (y 120 to 680, z 920 to 1580), 20 thick (a double wall drawn by its outside), 2 clear of the wall | it laps the opening by 30 each side |
| door swing | 0 to 90 degrees outward about its back edge | hinged at its back edge, the open door stands behind the opening, so the operator reaches in from the front; a design choice |
| handle | one vertical bar 200 long on 15 × 12 × 12 standoffs (hardware-cabinet's section), 40 from the door's front edge | the hand meets it at the free edge |
| roof opening | Ø150 at x 300, y 600 | the extraction draws from the back of the chamber, away from the window; a design choice |
| grate, lamp, gun, nozzle, footswitch, seals, latch, hinges | not drawn | separate elements of the sandblaster or the assembly's |

## Named nodes
`door` (rotate, above). Colliders `leaf` (the door), `roof`, `back`, `front`, `side-l`, `side-r`, `leg-1` to `leg-4`.

## Materials by layer
`M-STEEL-7035` the walls, roof and legs (painted RAL 7035) · `M-BLUE` the door · `M-CASE-CLEAR` the window pane (clear) · `M-ZINC`
the handle.

## Notes
No claim on the blast pressure, the abrasive, the dust or any safety function: those are the sandblaster's and its standards'
(none on file). No load rating, no vendor names, no label.

## Outputs (out/)
`cabinet-blast.lsp` · `.glb` (pivot on `door`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r74, unattended) |
