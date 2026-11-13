# op-pb-22-1no · v1.1 · 22.5 mm flush pushbutton

**What** Flush pushbutton operator, momentary, 22.5 mm mount, one contact block, legend plate. Colour is a parameter.
**Class** operator-22 · **Baseline** IEC 60947-5-1 22.5 mm operator standard (Rockwell 800F / Siemens 3SU1 class, measured, not shipped).
**Units / frame** mm, Z up. Origin: the cut-out centre on the panel's front face; the panel occupies 0 ≤ y ≤ panel_t; cap toward −y. The host cuts the Ø22.5 hole (library.mount); this element cuts only through its own legend plate and bezel.
**Built with** toolkit 1.3 · AutoLISP command `OPPB` · parameters `colour` (M-GREEN default; M-RED, M-BLUE, M-YELLOW, M-BLACK-PA), `legend` (true), `panel_t` (set by the host), `blocks` (1).

## Dimensions
| item | value |
|---|---|
| cut-out | Ø22.5 |
| legend plate | 30 × 50 × 1 black, on the panel face, 65 % of its height below the centre |
| bezel | Ø29.7 ring, 3 proud of the legend plate, bored Ø22.1 |
| cap | Ø21.5 flush with the bezel, crown Ø18.5 0.6 proud; travel 4 |
| behind the panel | Ø30 × 8 latch, then a 22 × 30 × 25 contact block with two terminal screws per block |

## Named nodes
`self` (the cap; renamed to the host's tag when placed, e.g. `btn-start`).

## Materials by layer
`M-ZINC` bezel, terminal screws · `M-BLACK-PA` legend plate, latch, block · cap in the `colour` material.

## Decals (Blender)
Legend text (the host's BOM note names it) in white on the plate.

## Outputs (out/)
`op-pb-22-1no.lsp` · `.glb` · `preview-*.png` (green default, red variant, the parts behind).

## History
| version | change |
|---|---|
| 1.1 | validation suite finding (MOT-010): the cap hit the solid latch after 2.2 of its 4.0 travel; the latch now has a Ø22.1 plunger bore |
| 1.0 | first build, split out of the shared operators code when the library became element folders |
