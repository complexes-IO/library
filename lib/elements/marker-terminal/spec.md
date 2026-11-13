# marker-terminal · v1.0 · terminal marker for term-4mm

**What** Terminal marker: one white tag per terminal block, on the block's front face between its two screw openings, carrying the terminal number. `n` tags make a strip over n neighbouring blocks of the same kind.
**Class** plate · **Baseline** our own design (complexes.org; EM rule 2026-11-05: a part with no product to match is our own design). The tag's own sizes are design choices; what it meets is term-4mm, and its pitch and height come from term-4mm 1.2 on file (`SIZES`: feed 6.0 × 44.5 × 47.0, ground 5.0 × 43.5 × 44.5).
**Units / frame** mm, Z up. Origin: term-4mm's frame: back face on the rail crown y = 0, rail centreline z = 0, left face of the first block x = 0. A BOM row places it at the x of its first block.
**Built with** toolkit 1.3 · AutoLISP command `MRKT` · parameters `kind` (feed | ground, as term-4mm), `n` (1: tags in the strip).

## Dimensions
| item | value | source |
|---|---|---|
| tag | (pitch − 0.3) × 2.0 × 10.0: 5.7 on a feed-through block, 4.7 on a ground block; 0.15 clear of each side face | design choice |
| position | on the front face (y = −44.5 feed, −43.5 ground), centred on z = 0 | term-4mm 1.2 `SIZES` |
| strip | n tags at the block pitch (6.0 or 5.0) | term-4mm 1.2 `SIZES` |
| clearance to the screw openings | the openings (Ø4.2) are at z ±15.5 (feed) and ±14.25 (ground), so the front face is free within ±13.4 / ±12.15; the tag spans ±5.0 | term-4mm 1.2 build (clamp-screw 1.1 cage) |
| clearance to the ground stripe | the yellow stripe runs z −18.25 to −10.25; the tag ends at −5.0 | term-4mm 1.2 build |

## Named nodes
None: the tag has no state. The terminal number belongs to the BOM row (decal).

## Materials by layer
`M-WHITE-PA` tags (printed).

## Decals (Blender)
The terminal number (from the architecture, e.g. `X1:12`) in black on each tag's front; `complexes.org` on the tag's back face (it rests against the block).

## Notes and assumptions
- The marker groove of the block and the tag's snap foot are NOT ON FILE (B): class B, a fit (OPERATING.md 6: fits and envelope;
  review marker-terminal-1.0 finding 2, elec-r7): how the tag holds on term-4mm. term-4mm's brief models no groove. The tag sits flat on the front face until the groove is on file; then a minor version adds the foot.
- The figures are read from term-4mm at build time (`library.load("term-4mm", "1.2")`), so a term-4mm minor that changes its pitch or height moves the tag with it; a major is refused.

## Outputs (out/)
`marker-terminal.lsp` · `.glb` (`env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (elec-r4, 2026-11-05) |
