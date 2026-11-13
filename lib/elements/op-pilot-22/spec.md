# op-pilot-22 · v1.0 · 22.5 mm pilot light

**What** Pilot light, 22.5 mm mount, Ø22 domed lens, LED lamp block, legend plate. Lens colour is a parameter; the lens is emissive in the twin when its output bit is on.
**Class** operator-22 · **Baseline** IEC 60947-5-1 22.5 mm operator standard (Rockwell 800F / Siemens 3SU1 class, measured, not shipped).
**Units / frame** mm, Z up. Origin: the cut-out centre on the panel's front face; lens toward −y. The host cuts the Ø22.5 hole.
**Built with** toolkit 1.3 · AutoLISP command `OPPL` · parameters `colour` (M-LENS-GREEN default; M-LENS-RED, M-LENS-WHITE), `legend` (true), `panel_t` (set by the host).

## Dimensions
| item | value |
|---|---|
| legend plate | 30 × 50 × 1 black |
| bezel | Ø29.7 ring, 3 proud, bored Ø22.6 |
| lens | Ø22, domed 6 past the bezel (crown Ø16) |
| behind the panel | Ø30 × 8 latch, one 22 × 30 × 25 lamp block with two terminal screws |

## Named nodes
`self` (the lens; renamed to the host's tag, e.g. `lamp-run`).

## Materials by layer
`M-ZINC` bezel, screws · `M-BLACK-PA` legend plate, latch, block · lens in the `colour` material (emissive factor in the glTF).

## Outputs (out/)
`op-pilot-22.lsp` · `.glb` · `preview-*.png` (green default, white variant, the parts behind).

## History
| version | change |
|---|---|
| 1.0 | first build, split out of the shared operators code when the library became element folders |
