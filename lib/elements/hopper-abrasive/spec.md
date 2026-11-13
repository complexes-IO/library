# hopper-abrasive · v1.0 · abrasive hopper for cabinet-blast: rim 1000 × 800, V hopper 900 × 700 to a 100 slot, trough, Ø50 outlet, sheet 2.0

**What** The abrasive hopper of a sandblast cabinet: the spent abrasive falls through the chamber's open floor into it, runs down
its sloped walls into a trough and leaves through one round outlet at the trough's bottom, where the blast gun's pickup or a
metering valve takes it. It is the hopper of the sandblaster system (lib/machines-factory.txt line 106: cabinet-blast (own),
gun-blast, nozzle-blast, compressor-air, frl, dust-collector, hopper-abrasive (own), lamp-machine, footswitch, glove-port,
valve-air-shutoff), and it is sized to cabinet-blast 1.0.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks hopper-abrasive
own_design "yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: cabinet-blast's origin, the floor z = 0 at the middle of the cabinet's width x = 0, y = 0 the
cabinet's front outer face. Placed at the cabinet's origin with no turn, the hopper hangs under the chamber. Extents x −500 to 500,
y 0 to 800, z 176 to 850.
**Built with** toolkit 1.3 · AutoLISP command `BLASTHOP` · no parameters.

## Mechanism
No moving part. The whole hopper is the fixed body.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the chamber's open floor | z 850; the chamber's walls 2.0 sheet over x −500 to 500, y 0 to 800 | cabinet-blast 1.0 (`library.load("cabinet-blast")`: W 1000, D 800, Z0 850, T 2.0): the rim's top lies at z 850 under the walls' lower edges |
| the cabinet's legs | four, 50 × 50, at the chamber's corners, z 0 to 850 | cabinet-blast 1.0 (LEG 50): the rim strips and the hopper's walls stop at the legs' inner faces (x −450 / 450, y 50 / 750), touching, never inside them |
| the pickup or metering valve | the Ø50 outlet and its collar Ø54 × 50 under the trough, centre x 0, y 400 | gun-blast and its pickup are not built yet; how they fit the outlet is checked when they are on file |

No fastener hole is cut: how the hopper is fixed to the cabinet (screws through the rim, or the legs' brackets) is left to a later
version, when the cabinet carries the matching holes. No grate or seal is drawn.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| rim | four strips 2.0 thick, 50 wide, z 848 to 850: front and back x −450 to 450 (y 0 to 50, 750 to 800), sides y 50 to 750 (x −500 to −450, 450 to 500) | it lies under the chamber's walls and stops at the legs, so the hopper fits between them |
| hopper | inside the rim, x −450 to 450, y 50 to 750 at its top (z 848) | the chamber's floor less the legs; abrasive falling on the rim's 48 inside the walls stays there, a design choice |
| sloped walls | front and back, 2.0 sheet, each running 300 inward over a 520 drop (about 60 degrees from the horizontal), between the end walls | steeper than a typical abrasive's angle of repose is meant to be; no flow is claimed, the angle is a design choice |
| end walls | x −450 to −448 and 448 to 450, vertical, cut along the sloped walls' undersides | a V hopper: two sloped walls and two flat ends |
| slot | y 350 to 450 (100 wide) at z 328 | where the sloped walls end |
| trough | 100 deep under the slot (walls z 228 to 328), bottom plate z 226 to 228, x −450 to 450 | collects the abrasive along the slot's length |
| outlet | Ø50 through the trough's middle, x 0, y 400; collar Ø54 (2.0 wall), z 176 to 226 | one pickup point; a design choice |
| sheet | 2.0 everywhere, as cabinet-blast | folds and seams are not drawn |

## Named nodes
None (fixed body only). Colliders `rim`, `funnel`, `trough`, `outlet`.

## Materials by layer
`M-STEEL-7035` everything (painted RAL 7035, as the cabinet).

## Notes
No claim on the abrasive, its flow, the hopper's capacity, a load or any safety function. No vendor names, no label.

## Outputs (out/)
`hopper-abrasive.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design, sized to cabinet-blast 1.0 (mech-r75, unattended) |
