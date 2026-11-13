# mcb-1p-c6 · measure brief

Element `mcb-1p-c6`: Eaton FAZ-C6/1-NA-SP (AutomationDirect part number FAZ-C6-1-NA-SP, $40.00 in the Eaton FAZ-NA sheet, p. 3) miniature circuit breaker, 1-pole, 6 A, C curve, 480/277 VAC, UL 489, 35 mm DIN rail. Control rail: the control-power breaker ahead of the PSRS-24-60 power supply (milestone-1 electrical architecture; 'listed, not on disk'). No vendor file on disk: this brief is derived from the 3-pole family drawing of `mcb-3p-c10`, which EM's close-out ruling allows without a new vendor search.

## Documents on file
- None for this part number. Used instead: `../mcb-3p-c10/references/datasheet.pdf` (Eaton FAZ-NA sheet, p. 3 single-pole selection guide naming FAZ-C6-1-NA-SP; the 'Dimensions' page is a photograph of a single-pole FAZ) and `../mcb-3p-c10/references/dimensional-drawing.pdf` (3-pole drawing with the 17.7 pole pitch).
- Milestone-1 mounting map, section 2: 'Also the 1-pole C6 (mcb-1p-c6, not yet on disk)'.
- Page numbers of the borrowed sheet: features p. 1 (17.7 mm per pole, indicator red / green), labeling p. 2, single-pole selection p. 3, mechanical data p. 13 (45 mm frame, 105 mm height, 17.5 mm width).

## Figures (mm)
| feature | mm | source |
|---|---|---|
| width, 1 pole | 17.7 | derived: the 3-pole drawing's pole pitch 0.70 in [17.7]; the 3-pole width 53.1 = 3 x 17.7 |
| height | 105.0 | 3-pole drawing (same FAZ-NA body) |
| depth | 73.0 | 3-pole drawing (same body, toggle 3.7 proud) |
| DIN rail datum | 45.0 | 3-pole drawing |
| mounting notch | 49.5 | 3-pole drawing |
| terminal spacing | 66.0 | 3-pole drawing |

## STEP read-back
- No STEP for this part number. The 3-pole model's single pole body measures 105.0 x 69.3 x 17.7 with its toggle 16.6 x 17.7 x 16.5 (Open CASCADE per-solid run 2026-11-03), which is the 1-pole envelope to within the family's variance.

## Mounting
35 mm DIN rail, one module (17.7), same datums as the 3-pole; rides beside the PSRS-24-60 on the control-power row (mounting map section 2).

## Build notes (own model)
- Reuse the `mcb-3p-c10` pole body once: 17.7 x 105.0 x 69.3 plus the 3.7 toggle; rail notch at 45.0 from the front; two terminal openings at 66.0 spacing.
- Mark the model 'derived from the FAZ-C10/3 drawing': the AutomationDirect 1-pole drawing (FAZ-C6-1-NA-SP 2-D) is a two-click fetch if EM later wants the part-specific figures, but it is a vendor search and needs the explicit ask.
- Datum: rail centreline, front face at +45.0.

## Origin
Rail device, as the 3-pole: back face on the rail contact plane y = 0, rail centreline z = 0, left face x = 0. Convention: lib/README.md states mm, Z up, right-handed; the two released specs give the examples (floor machine: floor plane, front-left anchor hole; panel device pbs-6h-22: back face, lower-left mounting hole; operators: panel face y = 0 at the cut-out centre). A DIN-rail device has no mounting hole, so the origin proposed here is the rail class of 'panel device': back face on the rail contact plane (y = 0), rail centreline z = 0, left edge of the module x = 0. Not yet written in the README; EM to confirm before Stage 1.

## Named nodes
- `node:toggle`: single-pole handle, kind rotate about x, ON / OFF (sheet p. 1, p. 6), swing angle NOT ON FILE.
- `node:indicator`: contact position window, red / green (sheet p. 1), no emission.

## Ports
None (captive screw terminals).

## Decals
- Front label 'C6' and the ratings (sheet p. 2); positions NOT ON FILE (derived element, no own photograph).
- Toggle 'ON' / 'OFF'.

## Status
DERIVED (no part-specific document on file; all figures from the 3-pole family drawing); part number and price verified in the Eaton sheet on file; no download, no licence item.

---
2026-11-03, extended the same day to Stage 0 of lib/element-qa-checklist.txt (EM's file of 2026-11-03): identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the library convention, named nodes (kind and range), ports, decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
