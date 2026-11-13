# tag-plate · v1.0 · nameplate / device tag / legend plate

**What** nameplate / device tag / legend plate. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** plate · **Baseline** own, per the 2026-11-03 ruling: nameplate 120 × 60 × 1.5 anodised aluminium with 2 × Ø3.5 at 100 × 40; device tag 30 × 12 × 1 adhesive; legend plate 30 × 50 × 1 (pbs-6h-22). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: panel device: back face on the panel y = 0, lower-left corner x = 0, z = 0, plate toward −y.
**Built with** toolkit 1.3 · AutoLISP command `TAG` · `kind` (tag | device | legend), `text`.

## Dimensions
| item | value |
|---|---|
| tag | 120 × 60 × 1.5 aluminium, four M3 screws at (10,10) (110,10) (10,50) (110,50), engraved three-line field |
| device | 30 × 12 × 1 black, white text field |
| legend | 30 × 50 × 1 black, Ø22.3 cut-out at 0.65 h, white text field |

## Named nodes
none

## Materials by layer
`M-ALU-ANOD` nameplate · `M-BLACK-PA` tag, legend · `M-WHITE-PA` text fields · `M-ZINC` screws

## Decals (Blender)
the plate is the decal: COMPLEXES INSTITUTE OF TECHNOLOGY / assembly · tag / lab · year; device tags K1, Q1, X1…; legend START / STOP / RESET / RUN / FAULT

## Notes and assumptions
The operators still build their own legend plate through std22; migrating them to carry tag-plate rows is a later minor version. Every figure marked **Assumption** here was NOT ON FILE in the brief and is set from the usual norm; a document figure replaces it as a minor version.

## Outputs (out/)
`tag-plate.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
