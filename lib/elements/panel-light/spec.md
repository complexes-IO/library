# panel-light · v2.1 · enclosure LED light bar with door switch

**What** Enclosure light: an aluminium bar screwed to the inner face of the enclosure's top door-frame flange, a row of LED windows into a light channel that glows in the twin, and a door-switch plunger that the closing door presses (light off when the door is shut). No electrical ratings are stated or claimed.
**Class** device · **Baseline** our own design (complexes.org; EM rule 2026-11-05: a part with no product to match is our own design). Its sizes are design choices. What it meets: the enclosure panel through two M4 screws (clearance per ISO 273 medium, lib/standards/holes.csv), and the led element, whose figures are NOT ON FILE: the LED window is an **Assumption**.
**Units / frame** mm, Z up. Origin: surface-mount device: the back face (the mounting face, on the flange's inner face), at the left mounting hole's centre; body toward −y; the bar runs along +x; the plunger toward +y, below the flange's edge.
**Built with** toolkit 1.3 · AutoLISP command `PLIT` · no parameters.

## Dimensions
| item | value | source |
|---|---|---|
| bar | 300 × 25 × 28 (x −15 to 285, z −16 to 12: the hole line 12 below the top), anodised aluminium | design choice |
| mounting holes | 2 × Ø4.5 through, at x 0 and 270 on the hole line z = 0; position Ø0.4 (features.csv) | ISO 273 medium for M4; T = H − F = 0.5 floating fastener (the library's rule GDT-010), Ø0.4 our choice |
| light channel | 230 × 10 × 16 from the back face (x 20 to 250, z −8 to 8), closed by the flange; `lamp` fills it with 0.1 clearance | design choice |
| LED windows | 9 × Ø5.2 from the front into the channel, x 35 to 235 at pitch 25 | **Assumption**: a 5 mm LED; the led element is NOT ON FILE |
| door-switch block | 24 × 25 × 12 black (x 246 to 270, z −28 to −16), seated under the bar's right end, its back face in the bar's back-face plane | design choice |
| door switch | Ø8.0 zinc plunger in a Ø8.4 × 10 bore in the block at x 258, z −22: 2 inside, 32 proud toward +y (the door); travel 7 (pressed by the door) | design choice: what the door frame on file asks (mounting, below) |
| mounting (what it meets) | the inner face of the top door-frame flange of enc-fs-1524x1829x305 (flange FL 30 tall, sheet T 1.9); the bar's top 2 below the roof sheet, so the whole bar (holes and channel) sits on the flange and its bottom edge is the flange's edge; the switch block hangs below the edge; the shut door's inner skin stands 25.0 in front of the flange's inner face (DOOR_RET 25 − DOOR_T 1.9 = 23.1 in front of its front face), so the plunger's tip at rest (y 32) is pressed 7 to y 25; the door's top return (y 1.9 to 26.9, z −0.9 to 1.0) and gasket (y 1.9 to 3.9, z −16 to −8) clear the bar, the block and the plunger (2 above its top); the door stay (80 to 280 from each hinge axis, y 1.9 to 5.9, z −39 to −31: enc-fs 1.9 element.py:101, DH − 40 from the door's bottom) stands 5 below the plunger (z −26 to −18) and clears it at any x. The flange has no holes on file: the enclosure's version that places this bar drills them | enc-fs-1524x1829x305 1.9 element.py (FL, T, DOOR_RET, DOOR_T, the gasket, the door stay) |

## Named nodes
`lamp` (emissive) · `door-switch` (translate −y, 0–7: pressed into the block by the door).

## Materials by layer
`M-ALU-ANOD` bar · `M-LENS-WHITE` lamp (emissive) · `M-BLACK-PA` door-switch block · `M-ZINC` plunger · `M-GASKET` holes, channel.

## Decals (Blender)
None (no label on 2.0).

## Notes and assumptions
- **Assumption**: LED window Ø5.2 and pitch 25, for a 5 mm LED; the led element is NOT ON FILE yet. When it is built, a later version places it in each window (new nodes `led-1` …: a major version) and takes the window's size from it.
- The two ISO 7380 M4 screws (inventory.csv made_of) are not built yet: the holes are modelled, the screws come in a later version.
- The door switch's contact (N.C., opened by the door) is the twin's logic; this element states no switch rating. Its switching travel and differential are behaviour.csv's `limit` row (class A, for EM: they decide what the twin reports).
- The floating-fastener rule is cited as the library's GDT-010 (toolkit/rules.py: "ASME Y14.5 / ISO 5459 virtual condition; ISO 2768-1"); neither standard's edition is in lib/standards/sources.csv, so no clause is named here (lib/needs-em/elec.md, r31).
- 2.0 against 1.0: on the back panel (1.0) the plunger stood 33 from the panel, 270 short of the shut door of enc-fs-1524x1829x305 (review panel-light-1.0 re-reads, finding 1). Every other mounting face on that enclosure is behind its door-frame flange (y 0 to 1.9, 30 wide round the opening), which a plunger from the roof or a side wall would have to pass through; below the top flange's edge the opening is free, so the bar sits on the flange's inner face and the plunger reaches the door below the edge.

## Outputs (out/)
`panel-light.lsp` · `.glb` (pivots on the moving nodes, `env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 2.1 | review panel-light-2.0 finding 1 (text): the door stay's z read again from enc-fs 1.9 (−39 to −31, not −26 to −18), so it clears the plunger at any x and the constraint on the placing assembly is dropped; no geometry change (elec-r39, 2026-11-12) |
| 2.0 | the bar on the enclosure's top door-frame flange (28 tall, all of it on the flange), the door switch in its own block under the bar's end, the plunger toward the door below the flange's edge, 32 proud (review panel-light-1.0 re-reads, findings 1 to 3): the mounting face and the plunger's axis changed, so a major; nodes `lamp` and `door-switch` kept; the switching travel a behaviour.csv limit row (class A); GDT-010 cited as the rule (elec-r31, 2026-11-11) |
| 1.0 | first build, our own design (elec-r4, 2026-11-05) |
