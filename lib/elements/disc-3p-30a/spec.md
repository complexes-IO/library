# disc-3p-30a · v1.7 · rotary disconnect 3-pole 30 A, door handle

**What** rotary disconnect 3-pole 30 A, door handle. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** device · **Baseline** maker's datasheet (references/measure.md: 2-D drawing p. 1: plate 69.1 sq, 36 × 36 / Ø4.2 pattern, body 44.6 / 58.6 / 50.9, shaft 30.2, overall 86.3; datasheet p. 3 handle). The maker, the part number and the files' licence review are in references/source.txt. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: cut-out centre class: shaft axis on the door front y = 0; handle toward −y, body behind the door toward +y.
**Built with** toolkit 1.3 · AutoLISP command `DISC` · `door_t` (1.9), `on` (false), `shaft` (30.2).

## Dimensions
| item | value |
|---|---|
| handle plate | 69.1 × 69.1 (drawing p. 1), black, four screw heads Ø4.8 × 0.8 on the drawing's 36 × 36 pattern, a Ø32 × 4 hub. **Assumption (B)**: the plate's 4.0 thickness and the front stack in front of the door (plate 4 + hub 4 + lever 12 + hasp 2 = 22) set the envelope and the body's place; the drawing gives none of them, so they are set to make the handle face to body back 86.3 (the STEP read-back, measure.md); the drawing on file is the source an attended reading takes them from |
| lever | 14 × 56 × 12 grey on the black plate, padlock hasp at its end (black); OFF = up (class C, Named nodes). The brief names the handle black / grey (measure.md:3); which part takes which colour is appearance, the reviewer's class C (1.6: was red, review disc-3p-30a-1.3 finding 5: the file's colours, not red). Its 12 depth is in the front stack above. **Assumption (B)**: the lever's 14 width and 56 length (1.7, review disc-3p-30a-1.5 finding 1); the length sets the element's z extent (z −8 … 48.0 against the plate's ±34.55, so 83.55 of the gate's STEP is the lever's) and in ON it reaches 48.0 into x, figures the envelope and an assembly's clearance read; the drawing on file gives neither, so they are set as the plate thickness above is, and an attended reading of the drawing is the source that replaces them. The hasp's size stays appearance, the reviewer's class C (inside the lever's envelope) |
| shaft | what is built: a Ø8 round from the coupler's end (y = door_t + 1.5, 3.4 at door_t 1.9) to 10 inside the body's front (y0 + 10, 15.7), 12.3 long, wholly behind the door; seated on the coupler at rest (1.4: the door unit and the body are one body), it stays with the body when the door swings. The parameter `shaft` (30.2, the drawing's shaft length) is not the drawn length: it places the body, y0 = 86.3 − 58.6 − 22 + (shaft − 30.2) = 5.7, and a longer shaft moves the body back by the difference. **Assumption (B)**: the round section; the brief's shafts are 6 × 6 square (datasheet p. 3, measure.md Documents) and the coupler's square drive is not modelled. The hosts' `shaft=243.1` (pm-motor-starter and pnl-motor-starter bom.csv) is the hosts' figure, setting the body 212.9 further back onto their back panel; it is none of the lengths the brief names, and whether one of the maker's long shafts (datasheet p. 3) reaches it is the hosts' question (lib/needs-em/elec.md r37) |
| body | 44.6 wide, 50.9 deep stepped to 58.6 (drawing p. 1), 69.1 high; three poles, screw terminals top and bottom. **Assumption (B)**: the 69.1 height; the drawing dimensions none, and the STEP's 69.129 square is the handle plate's (measure.md STEP read-back), so the body is at most 69.1 and is built at that |
| terminals | a screw head Ø5.2 on each end face per pole (x −14.9, 0, 14.9: the body's pole thirds; y 8 behind the body front) and a wire entry marker 5 × 10 × 0.5 behind it (y 14 to 24): the entry's mouth is the port pivot (1.4), on the end face, axis into the body. **Assumption (B)**: these positions; where the wire lands is the maker's figure and the brief gives none (Ports: "screw terminals on the body, 3 poles"), and pnl-motor-starter's wire lengths read them; the drawing on file is the source an attended reading takes them from |
| door cut-out | Ø14 at the shaft axis, round the Ø12 coupler of the handle unit. **Assumption (B)**: a fit with the host door; the drawing's 12.0 beside the pattern (measure.md figures, "handle shaft bore / centre") is taken as the coupler's, and the cut-out leaves it 1.0 clear each side. The door's four Ø4.2 holes of the 36 × 36 pattern are on file but not cut here: the door is the host's part |

## Named nodes
`door-unit` (fixed: plate, hub and coupler on the door) · `handle` (rotate about −y at the hub, 0–90°: OFF to ON. **Assumption (C)**: the rotation angle is NOT ON FILE (C); 90° is the two-position norm, and the twin reads the two ends only. The same class covers where OFF is and which way the lever turns, neither on the brief: OFF with the lever up (+z), and OFF to ON counter-clockwise seen from the front (the pivot turns about −y, toward the viewer); IEC 60447's rule for a rotary actuator's direction is not in lib/standards/sources.csv, so 1.6 keeps the built direction and claims no conformity) · `t-1-line`, `t-2-line`, `t-3-line` (the top screw heads, port, unit screw, gender none: a screw clamp, PIN-002) · `t-1-load`, `t-2-load`, `t-3-load` (the bottom ones). The nodes are named by pole and side, not by a printed mark: the marks L1–L3 / T1–T3 are behaviour.csv's Assumption (A), so EM's ruling on them changes no node name.

## Materials by layer
`M-BLACK-PA` plate, hub, padlock hasp · `M-GREY-PA` lever (1.6; was M-RED-PA) · `M-ZINC` shaft, screws, terminal screw heads · `M-GREY-PA` body · `M-GASKET` wire entry markers

## Decals (Blender)
OFF / ON legend and arrow on the plate (positions NOT ON FILE (C)); no vendor label

## Notes and assumptions
The open figures are marked on their rows above, each with its class and reason; a document figure replaces one as a minor version.

## Outputs (out/)
`disc-3p-30a.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.7 | text only (review disc-3p-30a-1.5 findings 1 and 2): the lever's width and length class B on its Dimensions row with the plate thickness's reason (they set the envelope; they were called appearance); the 1.3 row names the toolkit change made at that version. Geometry, nodes, materials and origin as 1.6 (elec-r48, 2026-11-13) |
| 1.6 | review disc-3p-30a-1.3 finding 5: the lever grey (M-GREY-PA, was M-RED-PA) on the black plate, as the brief's black / grey handle; the OFF position (up) and the direction OFF to ON (counter-clockwise from the front) under the handle's class C line with the swing (Named nodes). A material change only: geometry, nodes and origin as 1.5 (elec-r40, 2026-11-12) |
| 1.5 | text only (review disc-3p-30a-1.4 findings 1, 2, 4, 5, and 1.3 finding 1's body height): the terminal positions, the plate thickness with the front stack, the door cut-out, the body height and the shaft's round section each class B on its Dimensions row with its reason; the shaft row says what is built and what the `shaft` parameter does; the stale 2026-11-05 gate line replaced by the 1.4 gate's. Geometry, nodes and origin as 1.4 (elec-r37, 2026-11-12) |
| 1.4 | every terminal screw a port node `t-<pole>-line` / `t-<pole>-load` at the wire entry's mouth (the core's pin-nodes note of 2026-11-11, request panel-4 item 1; BEH-020); the shaft runs to the coupler's end (GEO-070: the door unit stood 0.5 off the body); the maker's names out of spec and BASELINE into references/source.txt (DOC-006); the handle swing and the legend positions class C. Nothing moved: a minor (elec-r31, 2026-11-11) |
| 1.3 | render fix (GEO-050): the coupler's end shared the plate's front plane; it now starts inside the plate. Later at the same version (329cd1b, the core's toolkit change; this row added in 1.7, review disc-3p-30a-1.3 finding 9 / 1.5 finding 2): TOOLKIT 1.2 → 1.3 in element.py and the Built with line, which changed how the holes reach the glTF; no figure, node or origin of the element changed |
| 1.2 | validation suite findings (GEO-020, MOT-010): the shaft ran through the door with no cut-out, so the door could not open; the handle plate, screws, hub and a Ø12 coupler are node `door-unit` (they swing with the door), the shaft stops 2 behind the door and stays with the body; door cut-out CUTOUT Ø14 (an open figure; class B since 1.5, Dimensions) |
| 1.1 | front stack (plate 4 + hub 4 + lever 12; open figures, class B since 1.5, Dimensions) and body position set so handle face to body back is 86.3 (was 83.6 at the AutoCAD gate); long-shaft parameter `shaft` |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |

## Deliberate differences
<!-- acad-gate disc-3p-30a -->
- AutoCAD gate 2026-11-11 at 1.4 (elec-r31): STEP extents [69.1, 86.3, 83.55] mm, equal to the glb's; brief figures (toolkit/figcompare.py, ISO 2768-1 m): 1 found (the 86.3 overall), 7 not located (figcompare matches only the width / height / depth / overall features). Fillet r 0.5 on edges > 3 mm: 0 of 44 rejected (0.0 %, 0 on the envelope). 1.5 is gated again in elec-r37 (lib/rounds/elec/r37.md).
