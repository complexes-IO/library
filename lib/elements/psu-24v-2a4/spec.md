# psu-24v-2a4 · v1.4 · 24 V DC power supply 60 W

**What** 24 V DC power supply 60 W. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** device · **Baseline** maker's datasheet (references/measure.md): 2-D drawing p. 1 (32.0 × 90.0 × 110.0; clip 3.3; rail CL 44.7 / 45.4; legend DC OK, DC LOW, V.ADJ); sheet p. 1-2. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0 (44.7 from the lower end), left face x = 0.
**Built with** toolkit 1.3 · AutoLISP command `PSU` · no parameters.

## Dimensions
| item | value | source |
|---|---|---|
| housing | 32 × 90 × 110, vent bands top and bottom, clip tab 3.3 below | 2-D drawing p. 1 (measure.md); vent bands a design choice |
| overall | 32.0 × 110.2 × 93.3 (y −102.7 … 7.5, z −48.0 … 45.3) | 93.3 and 110.0 from the 2-D drawing p. 1. The front features standing 0.2 proud of the 110.0 face is a design choice that makes the envelope equal the STEP read-back's overall extent 110.2 (measure.md "STEP read-back": one solid, extents only); which feature gives the STEP its 0.2 is NOT ON FILE (C), until an attended read of the drawing settles it with the 110.0's datum (review psu-24v-2a4-1.0 finding 5) |
| terminals | input L N PE (3) at the top, output +V −V +V −V (4) at the bottom, 7.5 pitch | **Assumption (B)**: the count, order and pitch; the sheet's terminal page (measure.md "Ports": sheet p. 2) is not read. Screw heads 0.2 proud, wire entries cut 0.5 into the end faces (the shape of toolkit din.terminal_row, request elec-2; drawn per terminal since 1.3 so each screw head is a port node) |
| terminal ports | `t-l`, `t-n`, `t-pe` at the top (x 8.5, 16.0, 23.5), `t-vp`, `t-vn`, `t-vp2`, `t-vn2` at the bottom (x 4.75, 12.25, 19.75, 27.25); each pivot at its wire opening's mouth on the end face (y −102.5 … −93.5, centre y −98.0), axis the way the wire goes in (−z at the top, +z at the bottom) | 1.3 (lib/requests/core/elec-pin-nodes-2026-11-11.md): the positions are the element's own terminal geometry as built (the class B row above), written as the element's design value |
| front | DC OK green Ø3.2 at z 20, DC LOW red at z 12, V.ADJ pot Ø6 at (22, 16), legend field 28 × 32 (0.1 proud, the lenses and pot 0.2: 0.1 above it, GEO-050) | **Assumption (C)**: positions and sizes; the drawing names the features (legend 1-3) but dimensions none, and the STEP read-back records no position (one solid) |

## Named nodes
`led-dcok`, `led-dclow` (emissive) · `vadj` (rotate about −y, 0–270°. **Assumption (C)**: the angle is NOT ON FILE (C); the twin does not read it, measure.md "Named nodes") · ports `t-l`, `t-n`, `t-pe`, `t-vp`, `t-vn`, `t-vp2`, `t-vn2` (the terminal screws; kind port, unit screw, gender none: screw clamps, PIN-002; since 1.3)

## Materials by layer
`M-GREY-PA` housing · `M-LENS-GREEN` / `M-LENS-RED` · `M-WHITE-PA` pot and legend field · `M-ZINC` screws

## Decals (Blender)
DC OK / DC LOW / V.ADJ beside the features; no vendor label

## Notes and assumptions
Open figures: the terminal set and pitch (class B, above), the front positions, the pot angle and the feature behind the STEP's 0.2 (class C, above), and the derate 0.8 in ratings.csv (its status column marks it; class A: a design rule with no standard cited; review psu-24v-2a4-1.0 finding 3). A document figure replaces each as a minor version.

## Outputs (out/)
`psu-24v-2a4.lsp` · `.glb` (pivots on the moving nodes and the ports, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist. Gates at 1.4 in elec-r39 (lib/rounds/elec/r39.md).

## History
| version | change |
|---|---|
| 1.4 | 2026-11-12 (elec-r39, unattended): review psu-24v-2a4-1.3 finding 1 (carried from 1.0 finding 3) and note 2: ratings.csv records the input range 85–264 V AC and the output adjust range 21.6–27.6 V DC from the sheet p. 1 on file (as behaviour.csv already cites), and iout in the derived form (I = P / U). The output class (PELV / SELV) still needs the sheet read. Text only: same nodes, origin, shapes and envelope |
| 1.3 | 2026-11-11 (elec-r29, unattended): lib/requests/core/elec-pin-nodes-2026-11-11.md (request panel-4 item 1): every terminal screw is a port node t-<mark> with its pivot at the wire opening's mouth, so behaviour.csv's pins name a node (BEH-020) and the panel shop's wire routes end on it. The terminals are drawn per terminal in the shape of toolkit din.terminal_row (the same three solids each); nodes added, none moved, same origin, shapes and envelope (OPERATING.md 7: a minor). The output row's second +V / −V pair is named +V' / −V' in behaviour.csv and joined to the first (the printed marks repeat) |
| 1.2 | 2026-11-08 (elec-r17, unattended): review psu-24v-2a4-1.1 finding 1: the 0.2 front protrusion is written as a design choice that makes the envelope equal the STEP's overall extent, and the feature that gives the STEP its 0.2 as an open figure, class C (appearance), until the drawing is read; the STEP read-back records one solid's extents, not which feature stands proud. Text only: same nodes, origin, shapes and envelope |
| 1.1 | request elec-2 (lib/requests/core/elec-2-answer.md item 2): `target=` the housing on both terminal rows, so the wire entries are cut 0.5 into the end faces (1.0: 0.5 proud; height 93.8 → 93.3, the drawing's). Review psu-24v-2a4-1.0: finding 1, the screw heads, LEDs and pot stand 0.2 proud (1.0: 1.2, 0.3, 0.8) and the legend field 0.1 (1.0: 0.2), depth 111.2 → 110.2 (the STEP's), collider to that envelope; finding 2, the terminal and front figures marked with their classes (B, C) in the dimension table; finding 4, maker and part number only in references/ (spec, BASELINE, docstring, ratings sources); finding 6, the open figures listed. No node, origin or cut-out moves (OPERATING.md 7: a minor) |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
