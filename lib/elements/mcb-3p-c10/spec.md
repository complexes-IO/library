# mcb-3p-c10 · v1.5 · miniature circuit breaker 3-pole C10

**What** miniature circuit breaker 3-pole C10. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** device · **Baseline** maker's datasheet and 2-D drawing (53.1 × 105.0 × 73.0, pitch 17.7, terminals 66.0, rail datum 45.0); sheet p. 1, p. 13; the brief is references/measure.md, and the maker, seller and part number are only in references/source.txt (OPERATING.md 6). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face of pole 1 x = 0.
**Built with** toolkit 1.3 · AutoLISP command `MCB3` · `poles` (3), `rating` (C10).

## Dimensions
| item | value |
|---|---|
| module | 17.7 per pole × 105 high (sheet p. 1; 2-D drawing); raised 45 mm front at 69.3 from the mounting plane, toggle 3.7 proud. Depth 73.0 overall (2-D drawing). **Assumption (B)**: its planes, the mounting plane (the clip region's back, y +7.5, 7.5 behind the rail crown) to the toggle face (y −65.5); the drawing names no plane, and the STEP read-back's 73.041 is its pole body 69.3 plus the toggle's 3.7 (measure.md STEP read-back), so the body is read as standing on the rail's mounting plane, as built (gate STEP 73.0). 1.1's History line ("73.0 from the back face, the clip's 7.5 behind it is the rail") said otherwise and is corrected here |
| terminal shoulders | the line the terminal screws sit on, 45.0 in front of the mounting plane = 37.5 in front of the rail crown (y −37.5). **Assumption (B)**: the drawing's 45.0 ("DIN rail datum, rail centre to the front face", measure.md figures) is read as this shoulder line, since a 45.0 from the toggle face would leave the rail inside the raised front; the six port pivots stand on it (y −29.5 at the entries' mouths) |
| rail clip | toolkit/din.py `rail_clip`, the library's contract for the 35 × 7.5 rail of din-rail-35 (EN 60715 TH35-7.5 as the contract names it; the standard is not in lib/standards/sources.csv). The brief's mounting notch 49.5 and its uncaptioned "other" 16.1 / 10.0 (measure.md figures) are not modelled: the clip is the contract's, not the maker's notch, and the 16.1 is read as the toggle's 16.6 within 0.5 (measure.md STEP read-back), the 10.0 not assigned |
| terminals | captive screws at ±33 (66.0 spacing, 2-D drawing), wire entries on the end faces |
| toggle | common handle 16.6 long, pivot about x at its root on the front face |
| indicators | one window per pole, red / green material swap |

## Named nodes
`toggle` (rotate about x, ±25°. Assumption (C): the swing is not in the brief; a handle swing, class C by OPERATING.md 6) · `indicator-1..3` (material swap, declared emissive without emission) · ports `t-1-line`, `t-1-load`, `t-2-line`, `t-2-load`, `t-3-line`, `t-3-load` (1.4: one per terminal screw, the screw head carrying the node; the pivot at the wire entry's mouth on the end face, x at the pole's centre, y −29.5, z ±52.5, axis the way the wire goes in; kind port, unit screw, gender none, PIN-002). The positions are the element's own terminal geometry (the brief gives the 66.0 screw spacing and the shoulder line; the entry's mouth is where the model shows the clamp), written as the element's design value (the core's pin-nodes note, 2026-11-11). The node names say pole and side, not the printed mark: the marks are an Assumption (A) in behaviour.csv, and EM's ruling on them changes no node name.

## Materials by layer
`M-GREY-PA` body · `M-BLACK-PA` toggle · `M-RED-PA` windows · `M-WHITE-PA` label field · `M-ZINC` screws

## Decals (Blender)
C10 and ratings per pole on the label field; ON / OFF on the toggle (positions NOT ON FILE (C): decal positions, class C by OPERATING.md 6)

## Notes and assumptions
The open figures are marked on their rows above, each with its class and reason; a document figure replaces one as a minor version.

## Outputs (out/)
`mcb-3p-c10.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.5 | elec-r37 (2026-11-12, unattended): text only (review mcb-3p-c10-1.4 findings 1, 2, 3, 5): the 73.0 depth's planes and the terminal shoulder line one class B each on their Dimensions rows; the rail clip row cites its contract and says the notch 49.5 and the 16.1 / 10.0 are not modelled; element.py's toggle swing comment gives its class C; geometry, nodes and origin as 1.4 |
| 1.4 | elec-r30 (2026-11-11, unattended): every terminal screw a port node t-<pole>-line / t-<pole>-load (the core's pin-nodes note of 2026-11-11, request panel-4 item 1; BEH-020); nodes added, none moved; geometry unchanged |
| 1.3 | DOC-006: the maker's and seller's names and the part number out of the Baseline, BASELINE, the docstring and the ratings sources (they stay in references/source.txt); the toggle swing and the decal positions given class C (OPERATING.md 6: handle swing, decal positions); geometry unchanged |
| 1.2 | render fix (GEO-050): the wire-entry plates sat flush with the end faces; now 0.1 proud |
| 1.1 | wire-entry slots inside the end faces (height 105.0, was 106 at the AutoCAD gate); envelope depth is 73.0 from the back face, the rail clip's 7.5 behind it is the rail, not the device |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
