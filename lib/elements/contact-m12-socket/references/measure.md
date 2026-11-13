# contact-m12-socket · measure brief

Element `contact-m12-socket`: M12 female contact (socket). Own design to the M12 interface: the figures live in `lib/toolkit/m12.py` and are shared by every M12 element.

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
| A socket hole | Ø1.200, 7.000 deep below the insert face | 7700-40121-U040300.STEP solid 1 (90° female A) |
| L socket bore | Ø1.600 (cordset); LioN-X X04 Ø1.6 | 7700-P4241-U0D0750.STEP solids 1 + 0 (female L body and nut); io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| LioN-X A / D entries | Ø1.05, counterbore Ø1.65 behind (as round 3) | io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| L FE (male side) | bore Ø1.850, 8.000 deep | 7700-P4241-U0D0750.STEP solid 2 (male L, inch file) |
