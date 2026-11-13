# port-pwr-480 · v1.1 · pin-and-sleeve receptacle 3P+E 480 V 20 A

**What** pin-and-sleeve receptacle 3P+E 480 V 20 A. Built from the Stage 0 brief `references/measure.md`.
**Class** connector · **Baseline** Bryant C420R7WA class via AutomationDirect, 2-D drawing p. 1 (plate 79 sq, 4 × Ø5.2 on 60 × 60, cap Ø78.5 × 22.7, depth 128.2); instruction sheet p. 2. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: cut-out centre: plate centre on the wall's front face y = 0, cap toward −y, rear body toward +y.
**Built with** toolkit 1.3 · AutoLISP command `P480` · `open` · CUTOUT 52 (Assumption: rear body Ø48 + 4); plate thickness 4 (Assumption).

## Named nodes
`self` (kind port, unit 480V-3P+E) · `cap` (rotate about x at the hinge, 0–100°, from the STEP pose)

## Decals (Blender)
20 A 480 V 3P+E and the 7 h mark on the plate; port label from the BOM tag

## Notes and assumptions
Figures marked **Assumption** were NOT ON FILE in the brief; a document figure replaces them as a minor version. Exterior only: the interior (mechanism-first ruling) arrives per interior-first-prompt.txt.

## History
| version | change |
|---|---|
| 1.1 | validation suite finding (MOT-010): the cap's pivot opened it into the receptacle body; range now 0 to −100 (outward) |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
