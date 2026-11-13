# hopper-dust · v1.0 · dust hopper: flange 1000 × 800, V hopper 900 × 700 to a 200 slot, trough, Ø150 outlet with ring Ø250, sheet 2.0

**What** The dust hopper of a dust collector: the dust the filters shed falls into it, runs down its sloped walls into a trough and
leaves through one round outlet at the trough's bottom, where a dust drum or a discharge valve takes it. It is the hopper of the
dust collection system (lib/machines-factory.txt line 117: dust-collector, duct-round, fan-exhaust, filter-cartridge, hopper-dust
(own), enc-wm, vfd-0.75kw, pressure-switch, valve-sol-32nc-sr, compressor-air). dust-collector is not built yet, so the hopper stands
on its own sizes; the collector is sized to its flange when it is built.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks hopper-dust own_design
"yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the top flange's top face, at the middle of the flange; x along its 1000 length, y along its 800
width. The hopper hangs toward −z. Extents x −500 to 500, y −400 to 400, z −856 to 0.
**Built with** toolkit 1.3 · AutoLISP command `DUSTHOP` · no parameters.

## Mechanism
No moving part. The whole hopper is the fixed body.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the collector's housing | seats on the flange's top face, z 0, over x −500 to 500, y −400 to 400 | dust-collector is not built yet; its housing is sized to this flange when it is, and the fit is checked then |
| a dust drum or discharge valve | the Ø150 outlet, its collar Ø154 × 100 and the outlet ring Ø250 × 2.0 under the trough, centre x 0, y 0 | neither is built yet; how they fit the ring is checked when they are on file |

No fastener hole is cut: how the hopper is fixed to the collector (screws through the flange) and how the drum or valve is fixed
to the ring are left to a later version, when the matching parts carry their holes. No seal, level probe or inspection door is
drawn.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| top flange | four strips 2.0 thick, 50 wide, z −2 to 0: front and back x −500 to 500 (y −400 to −350, 350 to 400), sides y −350 to 350 (x −500 to −450, 450 to 500) | a flat seat for the collector's housing all round the opening |
| hopper | inside the flange, x −450 to 450, y −350 to 350 at its top (z −2) | the flange's opening |
| sloped walls | front and back, 2.0 sheet, each running 250 inward over a 600 drop (about 67 degrees from the horizontal), between the end walls | steeper than hopper-abrasive's 60 degrees, as fine dust bridges more readily; no flow is claimed, the angle is a design choice |
| end walls | x −450 to −448 and 448 to 450, vertical, z −602 to 0, cut along the sloped walls' undersides | a V hopper: two sloped walls and two flat ends (hopper-abrasive's construction) |
| slot | y −100 to 100 (200 wide) at z −602 | where the sloped walls end |
| trough | 150 deep under the slot (walls z −752 to −602), bottom plate z −754 to −752, x −450 to 450 | collects the dust along the slot's length |
| outlet | Ø150 through the trough's middle, x 0, y 0; collar Ø154 (2.0 wall), z −854 to −754 | one discharge point; a design choice |
| outlet ring | Ø250 × 2.0, bore Ø150, z −856 to −854 | a flat face for a drum lid or a valve to seat on |
| sheet | 2.0 everywhere, as hopper-abrasive | folds and seams are not drawn |

## Named nodes
None (fixed body only). Colliders `flange`, `funnel`, `trough`, `outlet`.

## Materials by layer
`M-STEEL-7035` everything (painted RAL 7035).

## Notes
No claim on the dust, its flow, the hopper's capacity, a load, any explosion protection or any other safety function. No vendor
names, no label.

## Outputs (out/)
`hopper-dust.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design, hopper-abrasive's construction (mech-r77, unattended) |
