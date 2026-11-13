# duct-40x60 · measure brief

Element `duct-40x60`: slotted wiring duct with snap-on cover, McMaster-Carr 7578K811 (family 7578K17, white, 6 1/2 ft), maker not stated (made in Italy). Control rail: the horizontal duct runs above and below the DIN rail, the vertical runs frame the rail section.

## Documents on file
- `references/dimensional-drawing.pdf`: McMaster 2-D drawing 7578K811, one page (p. 1), text layer in inches: 1.5748, 2.3661, 6.5 ft, 0.315, 0.7874, 0.9843, 0.1772.
- `references/source.txt`: product-page specification table (2 1/4 in high x 1 1/2 in wide, 6 1/2 ft, slot 0.31 in, screw-on mount, PVC UL 94 V-0).
- `model.step`: McMaster 3-D STEP (AP203, inch), base and cover.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| section width | 40.0 (1.5748 in) | 2-D drawing |
| section height, base + cover | 60.1 (2.3661 in) | 2-D drawing |
| length as supplied | 1981.2 (6.5 ft) | 2-D drawing; cut to row length on the panel |
| slot width | 8.0 (0.315 in) | 2-D drawing (page: 0.31 in) |
| other drawing figures | 20.0 (0.7874 in), 25.0 (0.9843 in), 4.5 (0.1772 in), 6.5 (0.2559 in) | 2-D drawing; slot pitch, finger height, wall and finger thickness in that order is the reading of the drawing image, not confirmed by a caption |
| cover height | 8.8 | STEP read-back, cover solid; not on the drawing |

## STEP read-back (Open CASCADE, 2026-11-02 validation, per-solid 2026-11-03)
- 2 solids, 7602 faces, extents 40.0 x 60.1 x 1981.2 mm, declared unit inch; all three datasheet figures exact.
- Base: 40.0 x 57.7 x 1981.2 (slotted fingers modelled, origin at the section centre, length along -Z/+Z). Cover: 40.0 x 8.8 x 1981.2, overlapping the finger tops (base + cover = 60.1 overall, so the cover sits 6.4 mm over the fingers).
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
Screw-on base through the floor slots (page); no rail. On our panel the duct is cut to the row lengths of the mounting map (`lib/milestone-1/MILESTONE_1_MOUNTING_MAP.md`, section 2 'Wiring duct'), covers snapped on after wiring.

## Build notes (own model)
- Model the base as a 40 x 57.7 channel (the read-back above) with 8.0 slots at 20.0 pitch on both walls if the drawing's 0.7874 in figure is the pitch (check against the STEP fingers before cutting: finger count per 1981.2 mm run); cover 40 x 8.8 overlapping the finger tops by 6.4 (57.7 + 8.8 - 60.1). Corrected by mech-r11 (2026-11-05, reviewer's finding 2): the earlier note read "40 x 51.3 (60.1 less the 8.8 cover)", which left out the overlap recorded above.
- Keep the section exact (40.0 x 60.1); lengths are a cut list, not a figure.
- Datum: the origin below (panel face, run start, section bottom), run along the row. Corrected by mech-r11 (reviewer's finding 5): the earlier line said "section centre at the panel face", which the origin below does not use.

## Origin
Mounted on the panel plate, not a device: origin at the panel face (y = 0), run start x = 0, section bottom z = 0 (the row's lower edge in the mounting map). Convention: lib/README.md states mm, Z up, right-handed; the two released specs give the examples (floor machine: floor plane, front-left anchor hole; panel device pbs-6h-22: back face, lower-left mounting hole; operators: panel face y = 0 at the cut-out centre). A DIN-rail device has no mounting hole, so the origin proposed here is the rail class of 'panel device': back face on the rail contact plane (y = 0), rail centreline z = 0, left edge of the module x = 0. Not yet written in the README; EM to confirm before Stage 1.

## Named nodes
- `node:cover`: the snap-on lid, kind translate (lifted off along -y, away from the panel in the origin's frame; corrected by mech-r11, reviewer's finding 5, from "+y"), range 0 to the lid height 8.8 mm plus clearance; no figure for the snap travel on file.
- Nothing lights or is pressed.

## Ports
None.

## Decals
None (plain white PVC; no print on the McMaster page or drawing).

## Status
Figures VERIFIED against the STEP (3 of 3 within 2 mm); slot pitch and finger figures need one look at the drawing image before they are used; licence McMaster REVIEW.

---
2026-11-03, extended the same day to Stage 0 of lib/element-qa-checklist.txt (EM's file of 2026-11-03): identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the library convention, named nodes (kind and range), ports, decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
