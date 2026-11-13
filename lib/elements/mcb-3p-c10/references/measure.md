# mcb-3p-c10 · measure brief

Element `mcb-3p-c10`: Eaton FAZ-C10/3-NA (AutomationDirect FAZ-C10-3-NA) miniature circuit breaker, 3-pole, 10 A, C curve, 480Y/277 VAC, 10 kA, UL 489, 35 mm DIN rail. Control rail: the motor branch breaker, three modules.

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing FAZ-C10-3-NA, image only (no text layer); read by hand 2026-11-02 at EM's request, units inches [mm].
- `references/FAZ-C10-3-NA-2d.dwg`: the same drawing as DWG (figures as entities).
- `references/datasheet.pdf`: Eaton FAZ-NA series catalogue pages, 19 pages: features p. 1 (module width 17.7 mm per pole, contact position indicator red / green, trip-free handle, 35 mm DIN rail), labeling p. 2, selection guides p. 3-5, technical data p. 6 (endurance 20,000 ON/OFF), 'Dimensions' p. 9-10 (photograph, no figures), mechanical data p. 13 (frame size 45 mm, height 105 mm, width 17.5 mm per pole: 0.2 mm under the p. 1 figure), accessories p. 14-18.
- `model.step`: AutomationDirect STEP (mm), 9 solids.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| width, 3 poles | 53.1 (2.09 in) | 2-D drawing, manual reading |
| height | 105.0 (4.13 in) | 2-D drawing |
| depth | 73.0 (2.87 in) | 2-D drawing |
| pole pitch | 17.7 (0.70 in) | 2-D drawing |
| terminal spacing | 66.0 (2.60 in) | 2-D drawing |
| DIN rail datum (rail centre to the front face) | 45.0 (1.77 in) | 2-D drawing |
| mounting notch | 49.5 (1.95 in) | 2-D drawing |
| other | 16.1 (0.63 in), 10.0 (0.39 in) | 2-D drawing (toggle and terminal figures, assignment not captioned) |

## STEP read-back (Open CASCADE)
- 9 solids, 2352 faces, extents 105.0 x 73.041 x 53.1 mm (unit mm); all three datasheet figures exact (53.1, 73.0 vs 73.041, 105.0).
- Solids: three pole bodies 105.0 x 69.3 x 17.7 at 17.7 pitch (Z = -8.9, -26.6, -44.2); three toggles 16.6 x 17.7 x 16.5 standing 3.7 proud of the body face (69.3 + 3.7 = 73.0); three 7.3 x 3.1 x 9.6 parts at the terminal end (the terminal screws). Toggle 16.6 long is the 0.63 in figure, 16.1, within 0.5.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
35 mm DIN rail, 'DIN-rail mountable', IP20 finger safe, captive terminal screws (Eaton sheet p. 1-2; mounting map section 2: 3 modules, 53.1 wide). Rail datum 45.0 from the front face.

## Build notes (own model)
- One pole body 17.7 x 105.0 x 69.3 with the rail notch at 45.0 from the front, repeated three times at 17.7 pitch; a toggle 16.6 x 17.7 x 3.7 proud per pole; terminal openings at 66.0 spacing.
- The 1-pole C6 (`mcb-1p-c6`) is the same body once: see its brief.
- Datum: rail centreline, front face at +45.0.

## Origin
Rail device: back face on the rail contact plane y = 0, rail centreline z = 0, left face of pole 1 x = 0. Convention: lib/README.md states mm, Z up, right-handed; the two released specs give the examples (floor machine: floor plane, front-left anchor hole; panel device pbs-6h-22: back face, lower-left mounting hole; operators: panel face y = 0 at the cut-out centre). A DIN-rail device has no mounting hole, so the origin proposed here is the rail class of 'panel device': back face on the rail contact plane (y = 0), rail centreline z = 0, left edge of the module x = 0. Not yet written in the README; EM to confirm before Stage 1.

## Named nodes
- `node:toggle`: the common 3-pole handle, kind rotate about an x axis behind the front face, two positions ON / OFF (sheet p. 1, p. 6); the swing angle is NOT ON FILE. The tripped position is the OFF pose.
- `node:indicator`: the contact position window per pole, colour swap red / green (sheet p. 1), no emission; the twin reads it as the toggle state, no separate lamp.

## Ports
None (captive screw terminals top and bottom, sheet p. 1).

## Decals
- Front label per pole: 'C10' and the ratings (sheet p. 2 'the front of each FAZ-NA breaker is labeled'); text layout from the photograph p. 10 only, so positions NOT ON FILE.
- Toggle: 'ON' / 'OFF' marks (sheet p. 1).

## Status
Figures VERIFIED (3 of 3 exact); drawing is image-only, figures read by hand (recorded in metadata 2026-11-02); licence AutomationDirect REVIEW.

---
2026-11-03, extended the same day to Stage 0 of lib/element-qa-checklist.txt (EM's file of 2026-11-03): identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the library convention, named nodes (kind and range), ports, decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
