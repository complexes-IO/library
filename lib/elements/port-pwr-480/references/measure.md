# port-pwr-480 · measure brief

Element `port-pwr-480`: IEC 60309 pin-and-sleeve receptacle 20 A 480 VAC 3P+E (3-pole 4-wire, 7 h clock position, red), IP67, Bryant BRY420R7W (manufacturer C420R7WA, Hubbell) via AutomationDirect. The panel wall's power port p-m1 for the motor branch (pm-motor-starter BOM; connections.csv section '480 VAC & 120 VAC power').

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing BRY420R7W, one page (p. 1), inches [mm]: plate 3.11 [79.0] square, hole centres 2.36 [60.0] x 2.36 [60.0], holes 0.20 [5.2], cap 3.09 [78.5] dia and 0.89 [22.7] tall, side view 2.36 [60.0] + 1.81 [46.0] + 0.87 [22.2]; 'REFERENCE NUMBER C420R7WA, COLOR CODE RED'.
- `references/BRY420R7W-2d.dwg`: the same drawing as DWG.
- `references/datasheet.pdf`: Bryant watertight pin-and-sleeve pages, 11 pages: overview p. 1 (IEC 60309-1 / -2, IP67, colour code, 'terminal screws are backed out for easy assembly', spring-clamp note), selection tables p. 2 to 8, back boxes and adapter plates p. 9 and p. 11 ('direct mount back boxes', 15 degree angle adapters).
- `references/installation-manual.pdf`: Hubbell instruction sheet, 2 pages: parts p. 1 (terminal screws, gasket, body, interior), wiring and 'Mounting Details: tighten mounting screws to 18 lb-in (2.0 N-m)' p. 2.
- `model.step`: AutomationDirect STEP (mm), 2 solids.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| flange plate W x H | 79.0 x 79.0 | 2-D drawing p. 1 |
| mounting holes | 4 x Ø5.2 on 60.0 x 60.0 | 2-D drawing p. 1 |
| cap diameter / height | 78.5 / 22.7 | 2-D drawing p. 1 |
| depth: cap + body + rear | 60.0 + 46.0 + 22.2 = 128.2 | 2-D drawing p. 1 (derived sum) |
| mounting screw torque | 2.0 N m | instruction sheet p. 2 |

## STEP read-back (Open CASCADE)
- model.step: 2 solids, 735 faces, extents 79.0 x 112.2 x 128.15 mm (mm); datasheet check 79.0 exact, 128.2 vs 128.15 (0.05). The 112.2 height is the hinged cap standing open in the model (not a drawing figure).
- Solids: receptacle body with flange 79.9 x 84.9 x 68.2 (plate plus the angled body); the cap 81.2 x 39.2 x 84.9 at its open pose.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
Four screws on the 60 x 60 pattern through the flange plate into the wall (or a back box, datasheet p. 9 / p. 11), 2.0 N m (sheet p. 2); the rear body passes through a wall cut-out (size NOT ON FILE: the drawing gives the plate and the holes, not the clearance hole; take it from the STEP body behind the plate, 'from the STEP').

## Build notes (own model)
- Plate 79 x 79 x t (t NOT ON FILE, from the STEP) with 4 x Ø5.2 holes on 60 x 60; angled receptacle body 46 deep to the socket face, cap Ø78.5 x 22.7 on a hinge at the top; rear body 22.2 behind the plate.
- Red body (M-RED-PA) per the IEC colour code for 480 V (drawing p. 1); the socket face shows the 3P+E pin pattern at 7 h as a decal.
- Datum: the plate centre on the wall face.

## Origin
Cut-out centre class: plate centre on the wall's front face y = 0, cap and socket toward -y, rear body toward +y through the wall cut-out.

## Named nodes
- `node:cap`: the hinged lid, kind rotate about the hinge axis (x, at the top of the plate), closed 0 to open (the model's open pose; the angle is NOT ON FILE, about 100 degrees in the STEP; record 'from the STEP').
- `node:self`: the socket, kind port, extras `kind=port, unit=480V-3P+E`.

## Ports
- The element is the port: 3P+E, L1 / L2 / L3 / PE at the 7 h keying (IEC 60309-2); terminal screws inside (sheet p. 1); mates the plug BRY420P7W on the machine cable (cable-pwr-480, planned).

## Decals
- Rating '20 A 480 V 3P+E' and the IEC 7 h mark on the plate (positions NOT ON FILE); the Bryant / Hubbell marks not reproduced; port label p-m1 on the wall from the BOM tag.

## Status
Figures VERIFIED (2 of 2 within 0.05 mm); cap angle, plate thickness and the wall cut-out from the STEP only; licence AutomationDirect REVIEW. Stage 0 COMPLETE 2026-11-03.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
