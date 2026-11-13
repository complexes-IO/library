# term-endplate · v1.0 · end cover for a term-4mm strip

**What** End cover: a plate of the terminal block's own profile that closes the open side of the last block in a term-4mm strip. term-4mm 1.2 leaves the end cover unmodelled (its spec, Dimensions, "strip"); this element is it, as our own design.
**Class** plate · **Baseline** our own design (complexes.org; EM rule 2026-11-05: a part with no product to match is our own design). Its thickness is a design choice; what it meets is term-4mm, and its profile comes from term-4mm 1.2 on file (`SIZES`: feed 44.5 × 47.0, ground 43.5 × 44.5).
**Units / frame** mm, Z up. Origin: term-4mm's frame: back face on the rail crown y = 0, rail centreline z = 0; the plate's left face at x = 0, its thickness along +x. A BOM row places it at the x where the strip ends (after the last block: n × pitch).
**Built with** toolkit 1.3 · AutoLISP command `TEND` · parameter `kind` (feed | ground, the profile of the block it closes).

## Dimensions
| item | value | source |
|---|---|---|
| thickness | 2.0 (x); a strip of n blocks with one end plate is n × pitch + 2.0 long | design choice |
| profile, feed | 44.5 off the rail (−y) × 47.0 across the rail (z), centred on the rail | term-4mm 1.2 `SIZES` |
| profile, ground | 43.5 × 44.5 | term-4mm 1.2 `SIZES` |
| the face it closes | term-4mm's side faces are full flat profiles: its clamp pockets (x 0.45–5.55 feed, 0.25–4.75 ground), wire entries, screw access and rail foot all stay inside the block, so the plate meets a plane | term-4mm 1.2 build |

## Named nodes
None: the plate has no state.

## Materials by layer
`M-GREY-PA` plate.

## Decals (Blender)
None.

## Notes and assumptions
- The rail clip (how the plate latches to the rail) is NOT ON FILE (B), a fit (OPERATING.md 6: fits and envelope, EM's; review term-endplate-1.0 finding 1): term-4mm's brief models the block's foot as a 3 × 3 bar, not its latch. The plate stands on the rail crown with the block's profile; a minor adds the clip when it is on file.
- An end stop (the clamp that holds the strip on the rail) is a separate element, not built yet.
- The profile is read from term-4mm at build time (`library.load("term-4mm", "1.2")`), so a term-4mm minor that changes the profile moves the plate with it; a major is refused.

## Outputs (out/)
`term-endplate.lsp` · `.glb` (`env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (elec-r5, 2026-11-05) |
