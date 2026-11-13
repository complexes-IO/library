# insert-m12 · measure brief

Element `insert-m12`: M12 coded insert with its contacts. Own design to the M12 interface: the figures live in `lib/toolkit/m12.py` and are shared by every M12 element.

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
| insert front A / D female | Ø8.200; face Ø7.62 after a 0.5 x 30° chamfer | 7700-40121-U040300.STEP solid 1 (90° female A); io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| insert front L female | Ø8.700 | 7700-P4241-U0D0750.STEP solids 1 + 0 (female L body and nut); io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| A keyway | Ø1.300 on r 3.550, along the insert edge (8.2 long on the cordset, 8.56 on LioN-X) | 7700-40121-U040300.STEP solid 1 (90° female A); io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| A pole layout | centre + 4 on Ø5.000, 45° either side of the key | 7700-40121-U040300.STEP solid 1 (90° female A); 7700-40121-U040300.STEP solid 0 (male A) |
| A numbering, female face | clockwise from the key 2, 3, 4, 1; key between 1 and 2; centre 5 (unnumbered on this 4-pole part); male face the mirror | 7700-40121-U040300.pdf p. 1, Details A and B |
| A key peg (male) | Ø1.200 at r 3.550, 8.400 ahead of the carrier face | 7700-40121-U040300.STEP solid 0 (male A) |
| D keys | male: ribs at 108.8° / 161.2° (V) and 28.5° (flat), 8.4 long; female (LioN-X X01): notches at 64.2° / 115.8° and −16.1°, 8.7 deep; pins on Ø5.0 at 45° steps from the notch pattern | 7700-44511-S4U0100.STEP solid 0 (male D, inch file); io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
| L layout | 4 contacts + FE on Ø5.880, 72° apart; male: pins Ø1.5, FE a bore Ø1.85 in the key block; female: bores Ø1.6, FE a pin Ø1.5 in the recess | 7700-P4241-U0D0750.STEP solid 2 (male L, inch file); 7700-P4241-U0D0750.STEP solids 1 + 0 (female L body and nut); io-block-m12-8di8do/references/3D_step_935708001_LionX.zip (STEP, one solid) |
