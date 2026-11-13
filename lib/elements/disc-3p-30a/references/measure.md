# disc-3p-30a · measure brief

Element `disc-3p-30a`: Merz ML1-032-E-H03B rotary disconnect switch, non-fusible, 3-pole, 600 VAC 32 A (30 A class), UL 508 / UL 60947, door-mounted with the external black/grey lockable handle (NEMA 4/4X). Control rail: the main disconnect at the top left of the rail, switch body on the panel, handle through the door.

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing ML1-032-E-H03B, one page (p. 1), text layer (mm [in]): mount hole pattern 36.0 x 36.0, 4.2 x4, 12.0.
- `references/ML1-032-E-H03B-2d.dwg`: the same drawing as DWG.
- `references/datasheet.pdf`: AutomationDirect Merz UL 508 disconnect specification pages, 8 pages: handles and shafts table p. 3 ('Two-position, lockable in OFF only', external front mount, NEMA 4/4X, shafts AL-165 / 265 / 365 with 6 x 6 mm shaft lengths), general characteristics p. 6 (polycarbonate enclosure, temperature limits), enclosed versions p. 6-8.
- `model.step`: AutomationDirect STEP (inch), one solid.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| handle plate, square | 69.1 x 69.1 | 2-D drawing |
| door hole pattern | 36.0 x 36.0, 4 x 4.2 holes | 2-D drawing 'MOUNT HOLE PATTERN' |
| handle shaft bore / centre | 12.0 | 2-D drawing (the 12.0 figure beside the pattern) |
| switch body width | 44.6 | 2-D drawing |
| body depths | 50.9 and 58.6 | 2-D drawing (two body figures, stepped body) |
| shaft length | 30.2 | 2-D drawing |
| door thickness, max | 5.0 | 2-D drawing '5.0 MAX' |
| overall depth handle to body back | 86.3 | STEP read-back; not a single figure on the drawing |

## STEP read-back (Open CASCADE)
- 1 solid, 2964 faces, extents 86.3 x 69.129 x 69.129 mm, declared unit inch; the two drawing figures 69.1 x 69.1 within 0.03 mm.
- Single solid: handle, shaft and body are one body in the vendor file, so no per-part figures from the STEP.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
Door mount: 36 x 36 pattern with 4.2 holes plus the shaft hole in the door; body on the panel (ML1 allows DIN rail, base or front mount per the Merz sheet; mounting map section 2). The AL-165 adjustable shaft (datasheet) is the alternative for deeper enclosures; the kit's own shaft is 30.2.

## Build notes (own model)
- Two parts for the twin: body 44.6 wide x 58.6 deep (50.9 at the step) on the panel, handle plate 69.1 x 69.1 on the door, joined by a 30.2 shaft; overall 86.3 from the handle face to the body back as a check.
- Body height is not dimensioned on the drawing (the 69.1 figures are the plate); take it from the STEP (69.1 overall in the vendor pose) and mark it 'from the STEP'.
- Datum: shaft axis through the door, handle face flush with the door front.

## Origin
Door-mounted: cut-out centre class; origin at the shaft axis on the door front face (handle plate centred, y = 0 at the door front, switch body behind at -y by the door thickness plus the shaft). Convention: lib/README.md states mm, Z up, right-handed; the two released specs give the examples (floor machine: floor plane, front-left anchor hole; panel device pbs-6h-22: back face, lower-left mounting hole; operators: panel face y = 0 at the cut-out centre). A DIN-rail device has no mounting hole, so the origin proposed here is the rail class of 'panel device': back face on the rail contact plane (y = 0), rail centreline z = 0, left edge of the module x = 0. Not yet written in the README; EM to confirm before Stage 1.

## Named nodes
- `node:handle`: the rotary handle, kind rotate about the shaft axis (y), two positions OFF / ON (datasheet p. 3 'Two-position, lockable in OFF only'); the rotation angle between the positions is NOT ON FILE (not on the drawing or the sheet; the STEP handle pose is a check only, never the figure).
- Padlock hasp in OFF: fixed geometry, no node.

## Ports
None (screw terminals on the body, 3 poles).

## Decals
- Handle plate: 'OFF' / 'ON' legend and the arrow (drawing p. 1 shows the plate; legend text positions NOT ON FILE).
- Body: Merz rating label, not reproduced (standing rule: no vendor name or logo on a print).

## Status
Figures VERIFIED (2 of 2); body height and overall depth from the STEP only; licence AutomationDirect REVIEW.

---
2026-11-03, extended the same day to Stage 0 of lib/element-qa-checklist.txt (EM's file of 2026-11-03): identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the library convention, named nodes (kind and range), ports, decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
