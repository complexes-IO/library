# psu-24v-2a4 · measure brief

Element `psu-24v-2a4`: RHINO SELECT PSRS-24-60 (AutomationDirect) DIN-rail switching power supply, 24 VDC 2.5 A / 60 W adjustable 21.6-27.6 V, 85-264 VAC input, plastic housing, IP20, screw terminals. Control rail: the 24 V source for the safety relay, contactor coil, remote I/O, PLC and lamps (milestone-1 electrical architecture).

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing PSRS-24-60 (2025-08-27), one page (p. 1), text layer (mm [in]): 32.0, 90.0, 93.3, 110.0, 3.3, 44.7, 45.4, '35MM DIN CL'; legend 1 = output indicator (DC OK, green), 2 = output low voltage indicator (DC LOW, red), 3 = output voltage adjuster (V.ADJ).
- `references/PSRS-24-60-2d.dwg`: the same drawing as DWG.
- `references/datasheet.pdf`: RHINO SELECT PSRS specification pages, 6 pages: overview and selection chart p. 1 (30 x 90 x 110 W x H x D; red low-output-voltage LED and green output LED), specifications p. 2 ('Mounting Type 35 mm DIN rail', screw terminals, IP20, cULus E197592, 75 mm clearance note), p. 3-6 derating and notes.
- `model.step`: AutomationDirect STEP (mm), one solid.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| width | 32.0 (1.26 in) | 2-D drawing (selection chart says 30: the drawing governs) |
| body height | 90.0 (3.54 in) | 2-D drawing |
| overall height with the rail clip | 93.3 (3.67 in) | 2-D drawing |
| depth | 110.0 (4.33 in) | 2-D drawing |
| DIN rail centreline from the body ends | 44.7 and 45.4 (1.76 / 1.79 in) | 2-D drawing '35MM DIN CL' |
| clip projection | 3.3 (0.13 in) | 2-D drawing |
| front features | DC OK (green), DC LOW (red) indicators, V.ADJUST pot; terminals top and bottom | 2-D drawing legend 1-3 |

## STEP read-back (Open CASCADE)
- 1 solid, 1700 faces, extents 32.0 x 93.3 x 110.2 mm (unit mm); datasheet check 32.0 exact, 93.3 exact, 110.0 vs 110.2.
- Single solid, so terminals and indicators are surface features of one body.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
35 mm DIN rail (datasheet 'Mounting Type'); rail centreline 44.7 / 45.4 from the body ends (the body is not symmetric about the rail by 0.7); the deepest DIN device of the row after the contactor stack (mounting map: 110 deep).

## Build notes (own model)
- Box 32.0 x 90.0 x 110.0 with the rail clip adding 3.3 to 93.3 overall; rail notch on the back face centred 44.7 from one end; terminal rows at the top and bottom front edge; two indicator holes and the pot on the front face (positions from the STEP, not dimensioned).
- Datum: rail centreline, front face at +110.0 from the rail back (the drawing's 110.0 is the full depth).

## Origin
Rail device: back face on the rail contact plane y = 0, rail centreline z = 0 (44.7 from one body end, drawing p. 1), left face x = 0. Convention: lib/README.md states mm, Z up, right-handed; the two released specs give the examples (floor machine: floor plane, front-left anchor hole; panel device pbs-6h-22: back face, lower-left mounting hole; operators: panel face y = 0 at the cut-out centre). A DIN-rail device has no mounting hole, so the origin proposed here is the rail class of 'panel device': back face on the rail contact plane (y = 0), rail centreline z = 0, left edge of the module x = 0. Not yet written in the README; EM to confirm before Stage 1.

## Named nodes
- `node:led-dcok`: green output indicator, kind emissive, on when 24 V is present (drawing p. 1 legend 1; sheet p. 1).
- `node:led-dclow`: red low-voltage indicator, kind emissive (drawing legend 2; sheet p. 1).
- `node:vadj`: the trim pot, kind rotate, 21.6 to 27.6 V (sheet p. 1 'adjustable'); the mechanical angle is NOT ON FILE; the twin does not read it.

## Ports
None of the M12 / Ethernet kind: screw terminals, input L / N / ground and output +V / -V (drawing p. 1 'connection terminal' rows; pin order from the sheet p. 2 when connections.csv is written).

## Decals
- Front face: 'DC OK' / 'DC LOW' / 'V.ADJ' legend beside the two LEDs and the pot (drawing p. 1 legend); the RHINO SELECT rating label is not reproduced (standing rule: no vendor name or logo).

## Status
Figures VERIFIED (3 of 3 within 0.2 mm); licence AutomationDirect REVIEW.

---
2026-11-03, extended the same day to Stage 0 of lib/element-qa-checklist.txt (EM's file of 2026-11-03): identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the library convention, named nodes (kind and range), ports, decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
