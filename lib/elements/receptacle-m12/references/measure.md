# receptacle-m12 · measure brief

Element `receptacle-m12`: M12 receptacle (device side). Own design to the M12 interface: the figures live in `lib/toolkit/m12.py` and are shared by every M12 element.

## Documents on file
- none yet. Web sources read 2026-11-03 (not on file): SEW-EURODRIVE, M12 connector with mating connector (tightening torque 0.4-0.6 N m); Baumer CAM12 cordset technical data (tightening torque 0.6 N m, IP67, 5 poles A-coded, max 7.5 A, 50 V).

## Figures (mm)
See spec.md 'M12 interface figures used': every figure except the thread designation and the torque is an Assumption.

## Wanted (round-3 terminal brief)
A maker drawing (any A-coded 5-pole M12 male cordset and female receptacle; D-coded 4-pole; L-coded 5-pole power) giving: contact Ø, pole layout and pitch circle, pin protrusion from the carrier face, socket depth, mating (engagement) length, number of nut turns or thread length, seal position. NOT ON FILE is an acceptable answer.

---
2026-11-03. Stage 0 for an own-design element: the interface table is the brief; nothing is guessed silently (each open figure is marked).

## Cordset files, Open CASCADE read-back (terminal 2026-11-04)
Files in `lib/elements/cordset-m12/references/` (one copy; source.txt there). OCC STEPControl_Reader in mm (inch files converted), exact face boxes, positions along the connector axis.
Carrier face = the plane at the bottom of the male sleeve bore; insert face = the female's foremost plane. DIFF = differs from m12.py 1.2 by more than 0.05 (reported, m12.py not edited).

| figure | value | file, view / how |
|---|---|---|
| female insert front A | Ø8.200, 9.000 from the bore floor to the insert face (0.5 x 30° entry chamfer) | 7700-40121-U040300.STEP solid 1 (90° female A) |
| female thread bore A | Ø11.000 x 6.900, from 2.100 behind the insert face | 7700-40121-U040300.STEP solid 1 (90° female A) |
| female insert front L | Ø8.700; FE pin Ø1.500 in a recess 8.2 deep (the L key) | 7700-P4241-U0D0750.STEP solids 1 + 0 (female L body and nut) |
| LioN-X: insert face proud of the housing | 3.40 (A, D and L female); no receptacle body proud, no Ø13.5 bore (DIFF against 1.5) | io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid), coaxial faces at each port |
| LioN-X: Ø10.917 bore | 4.90 long (1.10 → 6.00 behind the housing face), Ø12.3 counterbore in front; annulus round the insert 9.50 deep from the insert face (DIFF 0.5 against 9.0) | io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| LioN-X X03 male sleeve | Ø12.0 thread to 12.14, sleeve front 13.10 out of the housing; bore Ø8.9, 8.9 deep | io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| LioN-X D keying (X01 / X02) | three notches in the insert wall, 8.7 deep: pair at 64.2° / 115.8°, single at −16.1° (poles ±45° / ±135°) | io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| LioN-X L keying | X03: key block over 74.6° at the FE position, face 0.8 behind the sleeve front; X04: recess at the FE side, floor 8.5 below the insert face | io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
