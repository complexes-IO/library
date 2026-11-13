# overload-9a-1no1nc · interior brief (Stage 0b, interior first) · 2026-11-03

Template: `lib/stage0b-template.md` (as of 2026-11-03, sections 1 to 6). Figures cite the documents below by page, or are NOT ON FILE. Nothing here is estimated; FIELD KNOWLEDGE marks how such a device works in general, never a figure.

## Identity and documents
Three-pole bi-metallic thermal overload relay, 7.0 to 10.0 A adjustable, trip class 10, 1 N.O. + 1 N.C. auxiliary, direct mount under the 9 A contactor (`contactor-9a-1no1nc`).
- `references/technical-specifications-rw-series.pdf` (spec, 18 pages): features p. 1; RESET/TEST button, recovery time, FLA dial, temperature compensation, phase failure p. 2; selection table p. 3; general data and auxiliary contacts p. 5; terminals and torques p. 6; general technical data and main contacts p. 7; tripping curve and derating p. 8 (the curve is an image); IEC 60947-4-1 trip-class table p. 12 (printed on the RW-E solid-state page; the class 10 row is the standard's limits, not a measured curve of this relay).
- `references/datasheet.pdf` (cut sheet, p. 1): 7.0-10.0 A, bi-metallic, trip class 10, local reset, phase-loss sensitive, direct mount power.
- `references/dimensional-drawing.pdf` (drawing, p. 1): envelope, pin and terminal pitch, install dimension with the contactor. Notes: 'dimensions can be changed by manufacturer without notice', 'dimensions do not imply tolerance'. Title block '8.0-10A' against 7.0-10.0 A on the cut sheet and spec p. 3: inconsistency stated, not resolved.
- `model.step` (vendor STEP, 39 solids): exterior only. No bimetal, heater, slide, latch or contact is modelled; every interior position below is NOT ON FILE unless a page gives it.
- No cutaway, exploded view or section of the relay is on file.

## Mechanism
Each of the three main current paths heats a bimetal strip directly (spec p. 2: 'three that are directly heated by the motor current'). When the current stays above the dial setting long enough, the strips bend far enough to push the trip mechanism, which releases a latch and changes over the two auxiliary contacts: 95-96 (N.C.) opens, 97-98 (N.O.) closes (spec p. 2 table). The 95-96 contact sits in the contactor's coil circuit, so the contactor drops out and the motor stops; the overload itself does not break the motor current (FIELD KNOWLEDGE: its main paths stay closed). A fourth bimetal, not in the current path, bends with the ambient temperature and cancels its effect between -20 and +60 °C (spec p. 2, p. 3, p. 7). Unequal bending of the three strips, as when one phase is lost, trips faster ('phase failure sensitivity', spec p. 2; the differential mechanism that does it is FIELD KNOWLEDGE, its form NOT ON FILE). After a trip the strips must cool before the latch can be reset ('recovery time', 'a few minutes', spec p. 2). The red RESET/TEST button is turned to one of four positions and pressed (spec p. 2).

## Parts with figures (mm unless stated)
| part | figure | source |
|---|---|---|
| housing | 45.0 wide, 47.0 tall at full depth, 77.0 deep; 83.7 overall with the 6.7 front projection | drawing p. 1; STEP solid 45.1 x 47.0 x 77.0 |
| upper housing around the pins | top 57.6 above the bottom face (10.6 above the full-depth top) | STEP read-back |
| hooks (2, rear) | top about 67.3 above the bottom face | STEP read-back |
| pins L1 L2 L3 (to the contactor) | round, Ø2.5, 22.0 long, tips 71.7 above the bottom; pitch 14.0; row 3.2 left of the housing centre (centres x 5.3 / 19.3 / 33.3 of 45.0) | drawing p. 1 ('2.5', '14.0' twice, '71.7'); STEP (cylindrical faces Ø2.5) |
| pin sleeves | Ø4.42 tapering to Ø4.32, top 60.9 above the bottom | STEP read-back |
| motor terminals T1 T2 T3 (bottom) | pitch 14.5; clamps 7.8 x 9.2 x 15.2; screw solids 10.8 x 11.5 x 3.3 | drawing p. 1 ('14.5' twice); STEP |
| auxiliary terminals (4, front) | 6.3 x 7.6 x 11.8 blocks at 10.5 pitch (x 6.75 / 17.25 / 27.75 / 38.25); which block is 95, 96, 97, 98 is NOT ON FILE | STEP read-back; marks per spec p. 2 |
| RESET/TEST button | red, four positions A / AUTO / HAND / H, turned without pressing, pressed to reset or test; STEP solids 16.6 x 9.2 x 8.0 and 8.8 x 9.1 x 5.7 at the front left (x -2.1 … 14.5); press travel and index angle NOT ON FILE | spec p. 2 (photo and text); STEP |
| FLA dial | continuously adjustable 7.0 to 10.0 A; STEP solids 11.7 x 11.0 x 3.0 and a 4.8 x 4.8 x 3.4 boss at the front right (x 26.4 … 42.0); angle span NOT ON FILE | spec p. 2; cut sheet p. 1; STEP |
| heated bimetals (3) | material, length, thickness, deflection per kelvin NOT ON FILE | spec p. 2 (existence and count) |
| compensation bimetal (1) | NOT ON FILE beyond its range -20 to +60 °C | spec p. 2, p. 3, p. 7 |
| trip slide, differential, latch | NOT ON FILE (no section) | FIELD KNOWLEDGE |
| auxiliary contacts | 95-96 N.C., 97-98 N.O., isolated from each other; gap and material NOT ON FILE | spec p. 1 ('Isolated 1 N.O. and 1 N.C.'), p. 2, p. 5 |
| mass | NOT ON FILE (the 0.25 kg on spec p. 13 is the solid-state RWB40E) | - |

## Kinematics
- Bimetals bend with temperature (m19); their free ends drive the trip slide (FIELD KNOWLEDGE); travel NOT ON FILE.
- Trip slide, latch and auxiliary contacts form one coupling: on trip 95-96 opens and 97-98 closes (spec p. 2: 'both N.O. (97-98) and N.C. (95-96) contacts change states'). Their order and overlap are NOT ON FILE.
- RESET/TEST button: rotate (four positions) and translate (press). In HAND and AUTO a press changes both auxiliaries (test); in H and A the test is blocked (spec p. 2 table). In H and HAND a trip stays latched until the button is pressed; in A and AUTO it resets by itself once cool (spec p. 2).
- FLA dial: rotate; it moves the trip point (FIELD KNOWLEDGE), not the heater.
- Touching parts: the pins in the contactor's lower clamps (see Mating features); the aux terminals take wires; nothing else moves outside the case.

## Mating features (measured on both STEPs together, recorded once in `references/measure.md`, 'Mate with the contactor')
- Pin pitch 14.0 equals the contactor's main-terminal pitch 14.0. The generator's `PIN_PITCH = 14.5` is the motor-terminal pitch: the error behind MATE-010.
- Seat: the overload's upper housing top sits at rail −39.2, 0.4 below the contactor's bottom face at −38.8; its bottom at −96.8 (install dimension A = 136.4, drawing p. 1); the pin tips at −25.1, inside the contactor's lower clamps (−36.1 … −27.6).
- Width 45.0 against the contactor's 44.8 (drawings p. 1); `lib/mates.csv` row 'contactor width = overload width' (tol 0.5).

## Section (positions of the moving parts)
NOT ON FILE: no section, cutaway or exploded view of the relay is on file. The CAD chat sets bimetal, slide, latch and contact positions from principle and marks them Assumption. What is on file to place them against: the pin row (x 5.3 / 19.3 / 33.3, where the current enters), the motor-terminal row (x 8.0 / 22.5 / 37.0 at the bottom), the button (front left), the dial (front right) and the four aux blocks across the front top.

## What the mechanism teaches
1. Protection by heat, not by current magnitude: the trip time falls as the current rises (spec p. 8 curve; class 10 limits p. 12), so a motor can start without tripping.
2. The overload does not open the motor circuit; it opens the contactor's coil circuit through 95-96. Wiring 95-96 out of the coil circuit leaves the motor unprotected.
3. The dial must be set to the motor's FLA: a 7-10 A relay on a 0.91 A motor never trips (the cell's ELR-010).

## Lesson carried forward
The interior of a thermal relay is on no document on file; only its behaviour is. The brief leans on the behaviour pages (p. 2 table, p. 8 curve, p. 12 class table) and leaves every internal position NOT ON FILE. The tripping curve on p. 8 is an image of mean values (20 °C, from cold; about 25 % of those times when warm, p. 8 text) and is not digitised here: reading points off it would be an estimate.

## 5. Precision at the interfaces
- Tolerances: NOT ON FILE for every figure (drawing note 2 'dimensions do not imply tolerance'; no ISO 286 fit is stated for the pins). STEP and drawing agree to 0.05 on the envelope (measure.md).
- Mating features: pin pitch 14.0 (contactor PITCH = overload PIN_PITCH in `lib/mates.csv`; its 0.2 tolerance was set by the kit, not on file); width 45.0 against 44.8.
- Connector and terminal properties:
  - pins: Ø2.5, round; plating, insertion and retention force NOT ON FILE; clamped by the contactor's main terminals (contactor spec p. 9: Phillips No. 2, 1.7 N-m).
  - motor terminals T1-T3: flexible cable 1 or 2 x 1.5-10 mm²; with terminal or rigid 1 or 2 x 1.5-6 mm²; AWG 16 to 8 (UL); torque 2.3 N-m [1.69 lb-ft] IEC, 2.26 N-m [20 lb-in] UL (spec p. 6); screw type NOT ON FILE; IP10 (spec p. 7).
  - auxiliary terminals: M3.5 x 10 Phillips; 2 x 1-2.5 mm²; AWG 16-12; 1.5 N-m [13 lb-in] (spec p. 6); IP20 (spec p. 7).
  - contact resistance, plating, mating cycles: NOT ON FILE.
- Statuses: the element stays REVIEW until its interior positions (Assumption) are signed off; MATE-010 and GEO-020 stay FAIL until the generator uses the pin figures above.

## 6. Data the validation suite reads
- `pins.csv` (written with this brief): L1 L2 L3 and T1 T2 T3 as `pass`; 95 sw-com, 96 sw-nc, 97 sw-com, 98 sw-no, rated 1 A (DC-13 at 24 V, spec p. 5).
- `ratings.csv` (rows added with this brief): ir_min 7.0, ir_max 10.0 (cut sheet p. 1, spec p. 3), trip class 10, auxiliary Ith 6 A, Ie DC-13 24 V 1 A, AC-15 24 V 4 A, minimum 17 V / 5 mA, Ui 690 V, heat loss 0.9 W and 1.7 W at the low and high ends of the setting range (p. 5), dissipation ≤3 W per pole (p. 7), maximum fuse given twice (40 A on p. 3; 25 A class RK5 on p. 7: inconsistency stated).
- `features.csv`: no own mounting holes (carried by the contactor); separate mounting only with the BF27-2D bracket (spec p. 4), not on file.
- `motion.csv` couplings, for the next version and not written to the shared table here: the trip slide drives aux-95 and aux-97 together; btn-reset pressed in HAND or AUTO drives the same slide (test); btn-reset pressed in H or HAND releases the latch (reset); stops NOT ON FILE.
- `contacts.csv` intended overlap, for the next version: the three pins inside the contactor's lower clamps t-2, t-4, t-6, kind insert, depth from the seat above. It is not declared now: today's overlaps (GEO-020) come from the generator's 7.8 x 9.2 pin blocks and 65-tall body, and declaring them would hide the error.
