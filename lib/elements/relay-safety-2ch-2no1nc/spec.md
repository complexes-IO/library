# relay-safety-2ch-2no1nc · v1.2 · safety relay, dual-channel input, 22.5 mm

**What** safety relay, dual-channel input, 22.5 mm. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** device · **Baseline** maker's datasheet: the installation manual on file, p. 9 / 11 / 14 / 31 / 73 (22.5 × 119.14 × 113.6; terminal blocks 4.3 proud from the STEP); the maker, product and part numbers are in references/measure.md and source.txt only (OPERATING.md 6). Vendor file RESTRICTED: baseline only, nothing shipped. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0.
**Built with** toolkit 1.3 · AutoLISP command `SR` · no parameters.

## Dimensions
| item | value |
|---|---|
| housing | 22.5 × 119.14 × 109.3 + four removable terminal blocks 4.3 proud (113.6 overall), 4 terminals each at 5.5 pitch |
| face | five LEDs Ø3 at x 6 from z 24 down in 7 steps; rotary mode switch Ø8 at (15, 8); legend field |

## Named nodes
`led-pwr`, `led-in1`, `led-in2`, `led-logic`, `led-out` (emissive; names per the 2026-11-03 ruling, to be confirmed against manual p. 31) · `sw-mode` (rotate, 0–300°, **Assumption (A)**: the switch's travel is NOT ON FILE in the brief; manual on hand, not yet read for it; class A because its positions select the relay's configuration, behaviour the twin reports, review sr-440r-1.1 finding 1)

## Materials by layer
`M-GREY-PA` housing · `M-BLACK-PA` blocks, switch · `M-LENS-GREEN` LEDs · `M-ZINC` screws

## Decals (Blender)
terminal ids above and below each block, LED legend; no maker's marks

## Notes and assumptions
none beyond the brief Every figure marked **Assumption** here was NOT ON FILE in the brief and is set from the usual norm; a document figure replaces it as a minor version.

## Outputs (out/)
`relay-safety-2ch-2no1nc.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.2 | elec-r21 (2026-11-09, unattended): DOC-006 (OPERATING.md 6, EM 2026-11-05): the maker's, product and part numbers left BASELINE, this spec and ratings.csv's sources for references/; they say "maker's datasheet" (the installation manual on file) and keep the page. No shape change: nodes, origin, cut-outs and figures as 1.1 |
| 1.1 | render fix (GEO-050): the lower terminal blocks sat flush with the housing's bottom face; now mirrored to the upper ones, 1.0 short of it |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
