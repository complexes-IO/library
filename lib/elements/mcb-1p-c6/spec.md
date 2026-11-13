# mcb-1p-c6 · v1.5 · miniature circuit breaker 1-pole C6

**What** miniature circuit breaker 1-pole C6. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** device · **Baseline** maker's datasheet (references/measure.md; the maker and part number are only in references/source.txt, OPERATING.md 6); figures derived from the 3-pole family drawing on file under mcb-3p-c10 per the 2026-11-03 ruling (one 17.7 module of the same body). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: rail device, as the 3-pole.
**Built with** toolkit 1.3 · AutoLISP command `MCB1` · no parameters (calls the mcb-3p-c10 family build with poles = 1: the one permitted cross-import, a family body, not a carried part).

## Dimensions
| item | value |
|---|---|
| module | 17.7 × 105 × 73, as the 3-pole: built by mcb-3p-c10 1.5's family body with poles = 1 (pinned, element.py `FAMILY`). Its open figures are the family's rows, each with its class there: the 73.0 depth's planes and the terminal shoulder line (class B), the rail clip the library's contract (EN 60715 TH35-7.5, din-rail-35), the brief's notch and uncaptioned figures not modelled |
| width | 17.7 governs: the family drawing's pole pitch, 53.1 / 3 (measure.md figures, "derived: the 3-pole drawing's pole pitch"), the dimensioned document on file. The sheet's mechanical data p. 13 gives 17.5 per pole (measure.md Documents), 0.2 under it; that figure is not built |

## Named nodes
`toggle` (rotate about x, ±25°, as the 3-pole. **Assumption (C)**: the swing is not in the brief (measure.md Named nodes: "swing angle" not given); a handle swing, class C by OPERATING.md 6) · `indicator-1` (material swap, as the 3-pole) · ports `t-1-line`, `t-1-load` (1.4, from mcb-3p-c10 1.4: the terminal screw heads, the pivot at the wire entry's mouth on the end face at x 8.85, y −29.5, z ±52.5, axis the way the wire goes in; kind port, unit screw, gender none, PIN-002; the element's own terminal geometry as the design value, the core's pin-nodes note of 2026-11-11)

## Materials by layer
as the 3-pole

## Decals (Blender)
C6 and the ratings on the label field (sheet p. 2); ON / OFF on the toggle (positions NOT ON FILE (C): decal positions, class C by OPERATING.md 6; a derived element with no photograph of its own, measure.md Decals)

## Notes and assumptions
Derived element; the part-specific drawing is a two-click fetch if ever wanted. The open figures are marked on their rows above (and the family's on mcb-3p-c10's), each with its class and reason; a document figure replaces one as a minor version.

## Outputs (out/)
`mcb-1p-c6.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.5 | elec-r37 (2026-11-12, unattended): review mcb-1p-c6-1.4 findings 1, 2, 3, 5: the family body pinned at mcb-3p-c10 1.5 (text only there, so the geometry is 1.4's); the toggle swing and the decal positions listed with class C; the family's open figures named on the module row; the width row says the drawing's 17.7 governs over the sheet's 17.5; nodes and origin as 1.4 |
| 1.4 | elec-r30 (2026-11-11, unattended): follows mcb-3p-c10 1.4: the terminal screws are port nodes t-1-line / t-1-load (the core's pin-nodes note of 2026-11-11; BEH-020); nodes added, none moved; geometry unchanged |
| 1.3 | DOC-006: the maker's name and part number out of the Baseline, BASELINE, the docstring and the ratings sources (they stay in references/source.txt with file and page); geometry unchanged |
| 1.2 | render fix (GEO-050): built from mcb-3p-c10 1.2 (wire entries 0.1 proud) |
| 1.1 | follows mcb-3p-c10 1.1 |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
