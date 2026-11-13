# contactor-9a-1no1nc · interior brief (Stage 0b)

Element `contactor-9a-1no1nc`: IEC contactor, 9 A AC-3, three main N.O. poles, one built-in N.O. + one built-in N.C. auxiliary, 24 VDC coil, 35 mm DIN rail or screw mounting, with the front-mounted auxiliary block (1 N.O. + 1 N.C.). The same mechanism as the relay scaled up: coil, armature, return spring, three main contact bridges with their contact springs, auxiliaries driven by the same carrier. Reference parts on file: WEG CWB9-11-30C03 with the BFB-11 front block, via AutomationDirect (a data baseline only; no vendor name on any part).

## Documents on file (references/)
- `technical-specifications-cwb-series.pdf`, 27 pages (CWB pages 1–16; pages 17–27 are the CWBS safety series, not this part): overview and catalogue code p. 1 (C03 = 24 V DC coil); selection p. 2, p. 3 (CWB9-11-30C03: 9 A AC-3; UL 0.75 hp 115 V and 1.5 hp 230 V single-phase; 3 hp 200/230 V, 5 hp 480 V, 7.5 hp 575 V three-phase; 1 N.O. + 1 N.C. built in); accessories p. 4 (BFB-11 63 g, max 4 added contacts; surge suppressors); **terminal markings p. 5** (read from the rendered image); **general and coil specifications p. 6** (read from the rendered table image: the text layer merges the frame columns); **main contacts p. 7–8** (rendered images); auxiliary contacts p. 8 (rendered image), p. 14 (text: A600 / Q600 / R300); **terminal capacity and torque p. 9** (rendered image); mounting position p. 10 (side-view outline, ±30°, 360° in the panel plane); surge suppressors p. 15 (DIB on a DC coil multiplies the opening time by 6; not with N.C. front blocks); B10 / B10d table p. 24 (CWB9 / CWBS9 row).
- `datasheet.pdf`: product cut sheet, 1 page: 9 A, (3) N.O. power poles, (1) N.O./(1) N.C. aux, 24 VDC coil, 'Actuator Type Magnetic', 5 hp, SCCR 5 kA, UL 508, '35mm DIN rail or panel', UL E202315.
- `aux-BFB-11-datasheet.pdf`: cut sheet, 1 page: front mount, (1) N.O./(1) N.C., 6 A at 120 VAC / 0.22 A at 120 VDC, screw terminal, for CWB9 to CWB125.
- `dimensional-drawing.pdf` (p. 1: 44.8 x 78.4 x 98.5; 70.0 / 35.0 hole pattern), `aux-BFB-11-drawing.pdf` (p. 1: 45.0 x 46.0 x 42.0), the two DWGs, `model.step` (44 solids), `aux-BFB-11.step` (29 solids); `measure.md` (the Stage 0 brief).
- Not on file: any section, cutaway, exploded view or construction figure of the magnet system, carrier or contact bridges; contact travel and over-travel; armature mass; contact material; coil resistance or turns; the contactor's weight. The STEPs are exterior only: the coil housing and base are solid blocks with terminal pockets (STEP read-back below), so they give no internal positions.

## Mechanism (one paragraph)
A 24 V DC coil (A1, A2) magnetises the magnet circuit; at pick-up (0.5 to 0.8 of 24 V, p. 6) the armature is drawn to the fixed core and moves the contact carrier, which closes the three main contact bridges (1–2, 3–4, 5–6) and the built-in N.O. auxiliary (13–14) and opens the built-in N.C. (21–22); the front block's contacts (53–54 N.O., 61–62 N.C., p. 5) are driven by the same carrier through the front face. Contact springs on each bridge give the closing force and take up the travel left after the contacts touch (over-travel); one or more return springs bring the carrier back when the coil voltage falls to drop-out (0.1 to 0.4 of 24 V, p. 6). The N.O. contacts close 35 to 45 ms after the coil is energised and open 8 to 12 ms after it is switched off (p. 6). Whether the armature moves straight (the usual contactor construction) or rotates, the contact bridges' double-break form and the number of return springs are FIELD KNOWLEDGE, not shown on any document on file.

## Section (the positions of the moving parts' axes and ends)
NOT ON FILE: no section or construction figure exists among the documents, and the vendor STEP has no internal solids. What the documents do fix: the mounting may tilt ±30° from vertical and rotate 360° in the panel plane (p. 10), so the mechanism works in any in-plane orientation (the moving axis is normal to the mounting plate); the coil housing and the base split the 98.5 depth at about 59 / 46 (STEP read-back); the main terminal rows sit 63 mm apart along the height and 14.0 mm apart across the width (STEP read-back). The coil axis, armature stroke, carrier position and bridge height are for the CAD chat to set (Assumption).

## Parts with figures (mm unless stated; document and page, or NOT ON FILE)
| part | figure | source |
|---|---|---|
| contactor, overall | 44.8 x 78.4 x 98.5 (W x H x D) | 2-D drawing p. 1 |
| with the front block fitted | depth 140.5 | derived: 98.5 + 42.0 (latch overlap NOT ON FILE) |
| front block BFB-11 | 45.0 x 46.0 x 42.0; 63 g | BFB drawing p. 1; spec p. 4 |
| contactor weight | NOT ON FILE | - |
| coil housing / base (STEP) | front block 59.3 x 78.0 x 44.8 (149,863 mm3), rear base 45.7 x 78.4 x 44.8 (79,994 mm3): solid housings, no internals | STEP read-back |
| main terminal clamps | two rows of three, 14.0 pitch across the width, rows 63 apart; clamp 12.7 x 8.5 x 12.8 | STEP read-back |
| terminal markings | coil A1, A2; mains 1–2, 3–4, 5–6; built-in aux 13–14 (N.O.), 21–22 (N.C.); front block 53–54 (N.O.), 61–62 (N.C.) | spec p. 5 (image) |
| coil | 24 VDC; operating limits 0.8 to 1.1 x Us; pick-up 0.5 to 0.8 x Us (12.0 to 19.2 V); drop-out 0.1 to 0.4 x Us (2.4 to 9.6 V) | spec p. 6 (DC table, CWB9–38 column) |
| coil power | 5.8 W with the magnetic circuit closed and 5.8 W while closing ('1.0x use the coil cold'); thermal dissipation 5 to 7 W | spec p. 6; p. 24 |
| coil resistance | 99 Ω | derived: 24² / 5.8 W (cold coil, 1.0 x Us); no resistance is printed |
| coil turns, wire gauge, inductance | NOT ON FILE | - |
| operate / release | N.O. contacts close 35 to 45 ms, open 8 to 12 ms (DC coil) | spec p. 6, p. 24 |
| with a DC surge suppressor | opening time x 6; suppressor not usable with front blocks containing N.C. contacts | spec p. 15 note |
| armature | mass, stroke, air gap: NOT ON FILE | - |
| return spring(s) | number, free length, rate: NOT ON FILE | - |
| main contacts | AC-3 9 A (≤440 V), 9 A (≤500 V), 7 A (≤690 V); AC-4 4.4 A; AC-1 / I_th 25 A | spec p. 7 (image) |
| main contacts, motor power | AC-3: 2.2 kW 220/240 V, 4 kW 380/400 V, 4.5 kW 415/440 V, 5.5 kW 500 V and 660/690 V; 600 operations per hour at 100 % | spec p. 7 (image) |
| making / breaking | making 250 A; breaking 250 A (≤400 V), 220 A (500 V), 150 A (690 V) | spec p. 7 |
| short-time current | 210 A 1 s, 105 A 10 s, 60 A 1 min, 30 A 10 min | spec p. 7 |
| short-circuit protection | 5 kA at 600 V UL/CSA; RK5 fuse 25 A (type 1), 20 A (type 2) | spec p. 7 |
| main contact impedance | 2.5 mΩ per pole | spec p. 7 |
| power dissipation per pole | 1.5 W at AC-1, 0.2 W at AC-3 | spec p. 7 |
| contact material | NOT ON FILE | - |
| contact travel, over-travel, gap, force | NOT ON FILE | - |
| auxiliary contacts (built-in and front block) | I_th 10 A; AC-15 10 A 230 V, 4 A 400 V, 2.5 A 500 V, 1.5 A 690 V; DC-13 4 A 24 V, 2 A 48 V, 0.7 A 110 V, 0.3 A 220 V, 0.15 A 440 V; UL A600, R300 (front block cut sheet: 6 A at 120 VAC / 0.22 A at 120 VDC) | spec p. 8 (image), p. 14; BFB cut sheet p. 1 |
| auxiliary reliability and timing | control circuit reliability 17 V / 5 mA; non-overlapping time between N.O. and N.C. 1.5 ms; contact impedance 2.5 mΩ | spec p. 8 (image: mΩ), p. 14 |
| mechanically linked / mirror contacts | not stated for the CWB (the certification on p. 17 is for the CWBS series) | spec p. 17 (CWBS) |
| life | mechanical 10 million cycles (DC coil); electrical AC-3 2.0 million cycles (CWB9); auxiliaries 1 million electrical / 10 million mechanical; B10 1,800,000 and B10d 2,400,000 under AC-3 (IEC 60947-4-1 Annex K) | spec p. 6 (image), p. 8, p. 24 |
| AC-3 life curve | NOT ON FILE (only the single AC-3 figure and the B10 table) | - |
| terminals | power: Phillips No. 2, 1.7 N-m, 1 x 18–10 AWG or 2 x 18–10; coil and auxiliary: Phillips No. 2, 1.0 N-m, 1 x 18–12 or 2 x 18–14; front block: 1 x 16–14 or 2 x 16–14 | spec p. 9 (image) |
| protection, environment | main terminals IP10, coil and auxiliaries IP20 (front); vibration 4 g open or closed; shock 10 g open, 15 g closed; −25 to +55 °C operating; 3000 m | spec p. 6 (image) |
| mounting | screws or 35 mm DIN rail (EN 50022); ±30° from vertical, 360° in the plane | spec p. 6; p. 10 |
| insulation | U_i 690 V (IEC), 600 V (UL / CSA); U_imp 6 kV | spec p. 6 |

## Kinematics
- Armature and contact carrier: one moving assembly normal to the mounting plate (FIELD KNOWLEDGE for the construction; the any-orientation mounting of p. 10 is consistent with it). Stroke NOT ON FILE. Nodes `armature`, `carrier` (translate).
- Main bridges (3): ride on the carrier; each touches its two fixed contacts when the carrier has travelled the contact gap, then its contact spring compresses for the over-travel (gap and over-travel NOT ON FILE). Nodes `pole-1`, `pole-2`, `pole-3` (translate with the carrier; `flex` for the spring).
- Built-in auxiliaries: 13–14 closes and 21–22 opens with the carrier; the 1.5 ms non-overlap means the N.C. opens before the N.O. closes (p. 8). Nodes `aux-13`, `aux-21`.
- Front block: its own carrier is pushed by the contactor's carrier through the front face (FIELD KNOWLEDGE); 53–54 closes, 61–62 opens. Node `front-block` with `fb-53`, `fb-61`.
- Return spring: compressed by the carrier when operated (motion `compress`).
- What touches what: armature on the core (operated); bridges on their fixed contacts; carrier on the front block's slide; terminals take the field wires (x06).

## What the mechanism teaches
1. Pick-up versus drop-out at a larger scale than the relay (12–19.2 V against 2.4–9.6 V), and a DC coil that takes the same 5.8 W closing and holding, so there is no inrush on the 24 V supply (x03, e17).
2. Contact travel and over-travel: the contacts touch before the armature seats, and the contact spring keeps them pressed as the contacts wear; operate (35–45 ms) is slower than release (8–12 ms) (m18, e17).
3. Utilization categories: the same contacts are rated 25 A AC-1, 9 A AC-3 and 4.4 A AC-4, because breaking a motor's locked-rotor current erodes the contacts; life is counted in AC-3 operations (2 million, B10 1.8 million) (x07, x17, x19).

## For the next version (2026-11-03, validation suite MOT-010 / GEO-010): front block and auxiliary bridge
Figures only; element.py is not edited here.
- Front-block slide travel and the room behind it: NOT ON FILE on any document (no section of the BFB-11; its cut sheet and drawing give only the 45.0 × 46.0 × 42.0 envelope). STEP read-back of `aux-BFB-11.step`: a 14.0 × 44.1 × 27.2 part (the likely slide, FIELD KNOWLEDGE) spans z −19.4 … +7.8 inside the 42.1-deep housing (z −21.0 … +21.1): 1.6 to the mounting face, 13.3 to the front face; it stands 3.8 / 4.5 beyond the housing at its two ends in y. Its travel is NOT ON FILE.
- The contactor side of that interface: the contactor STEP has a 55.2 × 10.0 × 41.6 bar (x 38.5 … 93.7, y −4.6 … +5.4) that ends flush with the front face (93.65), the part the front block bears on (FIELD KNOWLEDGE); the housings are solid in the STEP, so the room behind the bar when the carrier moves is NOT ON FILE. The suite's 2.0 of 3.5 mm block is a property of the model's assumed stroke (3.5) and slide placement, not of a figure on file.
- N.O. auxiliary bridge 13-14 in the carrier: its slot, gap and stop are NOT ON FILE (no internals in the STEP; no section). What is on file: the auxiliaries' 1.5 ms non-overlap between N.O. and N.C. (spec p. 8), which fixes their order (N.C. opens first), not their positions.

---
2026-11-03, Stage 0b on the template updated after the relay (motion column, section item). Figures are cited by document and page; rendered page images were read where the text layer merges table cells (p. 5, 6, 7, 8, 9); 'derived' marks arithmetic on cited figures; 'FIELD KNOWLEDGE' marks construction no document on file shows; NOT ON FILE is never filled in.
