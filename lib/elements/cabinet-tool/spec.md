# cabinet-tool · v1.1 · tool cabinet 900 × 600 × 1000, five drawers

**What** Floor-standing steel tool cabinet for the lab bench and the machining station: a carcass on a recessed plinth with five
pull-out drawers, each with a handle. The drawers are the mechanism: the twin opens them by name.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, validation.json) describes a catalogue product; this element is not built from it.
**Units / frame** mm, Z up. Origin: floor plane z = 0 at the carcass's front-left corner x = 0, y = 0; the drawers open toward
−y.
**Built with** toolkit 1.3 · AutoLISP command `TOOLCAB` · no parameters.

## Mechanism
`drawer-1` (bottom) to `drawer-5` (top): translate along −y, 0 to 450 each. Each drawer node carries its front, its tray (bottom,
two sides, back) and its handle. The trays run 12.5 inside each carcass side (the room drawer slides take; the slides are not
modelled) and inside their own front's height band, so a drawer at any travel clears the carcass and the other drawers. At 450
out, 110 of the 560 tray stays inside.

## Its own sizes (design choices)
| item | value |
|---|---|
| carcass | 900 × 600 × 1000 outside, 1.5 sheet; plinth 80 high, set back 30 |
| drawer fronts | 20 thick, full width (over the carcass edges), heights 222, 200, 180, 150, 150 from the bottom, 3 apart |
| trays | 872 wide (12.5 clear each side), 560 deep, 1.5 sheet; bottom 10 above the lower edge of their front, sides 20 below its top |
| pull-out | 450 |
| handles | bar 300 × 12 × 12 on two standoffs, 27 proud of the front, centred on each front |
| colours | carcass and trays RAL 7035, fronts blue, handles zinc |

## What it meets
Nothing outside itself: it stands on the floor. No figure comes from a standard or another element.

## Named nodes
`drawer-1` … `drawer-5` (translate, above). Colliders `body` and one per drawer (`drawer-<n>`).

## Materials by layer
`M-STEEL-7035` carcass, plinth, trays · `M-BLUE` drawer fronts · `M-ZINC` handles.

## Notes
No load rating and no safety claim (no drawer capacity, no anti-tilt interlock claimed). Drawer slides, locks and liners are not
modelled.

## Outputs (out/)
`cabinet-tool.lsp` · `.glb` (pivots on the five drawers) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r4) |
| 1.1 | review cabinet-tool-1.0 finding 1 (mech-r18): the trays row said the tray sits 30 below the top of its front; the code builds 20 (element.py `tz1`), the size 1.0 was gated with. The spec now gives the built figures (bottom 10 above the front's lower edge, sides 20 below its top). Text only: geometry, nodes, origin unchanged (a minor) |
