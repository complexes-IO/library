# nut-m12 · measure brief

Element `nut-m12`: M12 x 1 coupling nut. Own design to the M12 interface: the figures live in `lib/toolkit/m12.py` and are shared by every M12 element.

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
| male thread A / D | Ø12.000 x 6.850, 0.900 behind → 5.950 ahead of the carrier face | 7700-40121-U040300.STEP solid 0 (male A); 7700-44511-S4U0100.STEP solid 0 (male D, inch file) |
| male thread L | Ø11.900 x 7.639, from 1.200 behind the carrier face (DIFF 0.30) | 7700-P4241-U0D0750.STEP solid 2 (male L, inch file) |
| male front lip A / D | Ø10.500 x 2.200 (wall round the Ø8.3 bore 1.1) | 7700-40121-U040300.STEP solid 0 (male A); 7700-44511-S4U0100.STEP solid 0 (male D, inch file) |
| female thread bore A | Ø11.000 x 6.900, from 2.100 behind the insert face; 45° entry chamfer to Ø11.6 at the nut front | 7700-40121-U040300.STEP solid 1 (90° female A) |
| female thread bore L | Ø11.000 x 8.711, from 1.589 behind the insert face, 0.289 behind the nut front after a 60° chamfer (DIFF 0.51 from 2.1) | 7700-P4241-U0D0750.STEP solids 1 + 0 (female L body and nut), nut solid 0 |
| nut front face to insert face | A 1.500; L 1.300 (the insert stands ahead of the nut) | 7700-40121-U040300.STEP solid 1 (90° female A); 7700-P4241-U0D0750.STEP solids 1 + 0 (female L body and nut) |
| knurl | A / D Ø15.000; L Ø17.900 | STEP; drawings 15.0 / 17.9 |
| torque | ≤ 0.6 N·m | catalogues p. 2 |
