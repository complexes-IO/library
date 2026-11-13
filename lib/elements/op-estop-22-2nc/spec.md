# op-estop-22-2nc · v1.1 · 22.5 mm emergency stop

**What** Emergency-stop operator, Ø40 red mushroom, push-to-latch, twist-to-release, on a 60 × 60 yellow legend plate, two NC contact blocks.
**Class** operator-22 · **Baseline** IEC 60947-5-5 / ISO 13850 E-stop on the 22.5 mm cut-out (Rockwell 800F / Siemens 3SU1 class, measured, not shipped).
**Units / frame** mm, Z up. Origin: the cut-out centre on the panel's front face; mushroom toward −y. The host cuts the Ø22.5 hole.
**Built with** toolkit 1.3 · AutoLISP command `OPES` · parameter `panel_t` (set by the host).

## Dimensions
| item | value |
|---|---|
| yellow plate | 60 × 60 × 1.5 on the panel face, with the Ø22.5 hole |
| collar | Ø32 × 6 black |
| mushroom | Ø40, 24 high (crown Ø32, the last 4 mm) |
| behind the panel | Ø30 × 8 latch, two 22 × 30 × 25 NC blocks stacked, two terminal screws each |

## Named nodes
`self` (the mushroom head: press 6 mm and latch, twist 45° to release; renamed to the host's tag, e.g. `estop-1`).

## Materials by layer
`M-YELLOW` plate · `M-BLACK-PA` collar, latch, blocks · `M-RED` head · `M-ZINC` screws.

## Decals (Blender)
EMERGENCY STOP around the mushroom on the yellow plate (ISO 13850 arrows for the twist release).

## Outputs (out/)
`op-estop-22-2nc.lsp` · `.glb` · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.1 | validation suite finding (MOT-010): the mushroom pressed straight into its collar (blocked at 0.2 of 6); the head now has a Ø32.6 × 6.2 skirt recess and slides over the collar |
| 1.0 | first build, split out of the shared operators code when the library became element folders |
