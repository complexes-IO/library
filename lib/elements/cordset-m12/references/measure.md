# cordset-m12 · measure brief

## Cordset files, Open CASCADE read-back (terminal 2026-11-04)
Files in `lib/elements/cordset-m12/references/` (one copy; source.txt there). OCC STEPControl_Reader in mm (inch files converted), exact face boxes, positions along the connector axis.
Carrier face = the plane at the bottom of the male sleeve bore; insert face = the female's foremost plane. DIFF = differs from m12.py 1.2 by more than 0.05 (reported, m12.py not edited).

| figure | value | file, view / how |
|---|---|---|
| male A / D sleeve bore | Ø8.300, front 8.900 ahead of the carrier face | 7700-40121-U040300.STEP solid 0 (male A); 7700-44511-S4U0100.STEP solid 0 (male D, inch file) |
| male A / D lip | Ø10.500 x 2.200 | 7700-40121-U040300.STEP solid 0 (male A); 7700-44511-S4U0100.STEP solid 0 (male D, inch file) |
| male A / D thread | Ø12.000, 6.850 long, 0.900 behind → 5.950 ahead of the carrier face (two flats 10.5 across, as modelled) | 7700-40121-U040300.STEP solid 0 (male A); 7700-44511-S4U0100.STEP solid 0 (male D, inch file) |
| male A key peg | Ø1.200 at r 3.550, front 8.400 ahead | 7700-40121-U040300.STEP solid 0 (male A) |
| male D keys | three ribs on the sleeve wall to 8.400 ahead: V ribs at 108.8° / 161.2°, flat rib at 28.5° (pins at 0/90/180/270°) | 7700-44511-S4U0100.STEP solid 0 (male D, inch file), rib front faces |
| male A / D pins | Ø1.000, 6.450 + 0.450 tip = 6.900 ahead, on Ø5.000 | 7700-40121-U040300.STEP solid 0 (male A); 7700-44511-S4U0100.STEP solid 0 (male D, inch file) |
| male A / D knurl | Ø15.000 | 7700-40121-U040300.STEP solid 0 (male A); 7700-44511-S4U0100.STEP solid 0 (male D, inch file) |
| overall, male A axial | 40.7 | 7700-40121-U040300.pdf p. 1; OCC 40.700 |
| overall, male D axial | 47.5 (right-angle male 39.6) | 7700-44511-S4U0100.PDF p. 1, 7700-44541-S4U0500.pdf p. 1; OCC 47.500 |
| overall, female A 90° | 27.0 along the axis, 38.9 along the cable (OCC 27.000 / 39.000); the axial female's 38 is the catalogue B, no model on file | 7700-40121-U040300.pdf p. 1; m12patchcbl.pdf p. 1 |
| overall, L male / female | 53.8 / 53.0 | 7700-P4241-U0D0750.pdf p. 1; OCC 53.800 / 53.000 |
| knurl L | Ø17.900 (male body, female nut) | 7700-P4241-U0D0750.STEP solid 2 (male L, inch file); 7700-P4241-U0D0750.STEP solids 1 + 0 (female L body and nut); drawing 17.9 |
| cable Ø | D S4U 6.6; L 9.8 (16 AWG) / 10.5 (14 AWG); A CDP12 PVC 5.0 (7700 TPE: NOT ON FILE). STEP stubs are simplified (A 5.5, D 6.5, L 8.7) | connectioncablesdata.pdf p. 2; connectioncablespower.pdf p. 2; m12patchcbl.pdf p. 2 |
| tightening torque | ≤ 0.6 N·m | m12patchcbl.pdf p. 2; connectioncablesdata.pdf p. 2; connectioncablespower.pdf p. 2 |
| ratings | A 4 A 250 VAC/VDC; D 4 A (UL 1.5 A) 60 VDC; L 12 A 16 AWG / 16 A 14 AWG, 63 VDC | cut sheets; connectioncablesdata.pdf p. 2; connectioncablespower.pdf p. 2 |
| D colours | 1 TD+ white/orange, 2 RD+ white/green, 3 TD− orange, 4 RD− green | 7700-44541-S4U0500.pdf p. 1 |
| seal | NOT ON FILE (no seal modelled, drawn or named) | all four STEP, drawings, cut sheets, catalogues |
