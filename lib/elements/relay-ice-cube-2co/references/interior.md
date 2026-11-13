# relay-ice-cube-2co · interior brief (Stage 0b)

Element `relay-ice-cube-2co`: plug-in "ice cube" control relay, DPDT (two changeover poles), 24 VDC coil, 15 A contacts, 8 blade pins, on a 35 mm DIN-rail socket with screw terminals. Reference part on file: AutomationDirect 782-2C-24D with socket 782-2C-SKT (a dimensional and data baseline only; no vendor name on any part). The template element of the interior-first programme (EM 2026-11-03): coil, armature, spring, contacts, pins, case.

## Documents on file (references/)
- `technical-specifications-78-relays.pdf`, 7 pages: features p. 1 (contact "silver alloy gold flashed"; open-contact dielectric "up to 2500V rms"; LED indicator; mechanical flag indicator "shows relay status in manual or powered condition"; pushbutton for manual operation without coil power; lock-down door "holds pushbutton and contacts in the operate position"; finger grip cover; I.D. tag), selection p. 2 (note: not for low-current switching), **specifications p. 3** (contact ratings, life, response time, weight, coil resistance, power, pull-in and drop-out, contact material, minimum switching, dielectric; read from the rendered table image 2026-11-03 because the text layer merges the pull-in and drop-out cells), **wiring diagram p. 5** (pin numbers and IEC numbers, viewed from the pin end; read from the rendered image), protection modules p. 7 (diode and MOV plug-in modules; inductive transients and contact bounce explained).
- `datasheet.pdf`: product cut sheet, 1 page: "encapsulated push-to-test", 24 VDC, DPDT, (2) N.O. (2) N.C., 15 A, 8-pin, LED, requires the socket; UL Recognized E191059, CSA 244610.
- `technical-specifications-78-sockets.pdf`, 2 pages: socket p. 1 (35 mm DIN rail or panel; all terminals 9 in-lb / 1.0 N-m; 12 to 20 AWG, one or two identical wires; holding clips included), wiring p. 2 (same as relay p. 5).
- `socket-782-2C-SKT-datasheet.pdf`, 1 page; `socket-782-2C-SKT-drawing.pdf`, 1 page (image; read by eye 2026-11-02: 79.2 long, 29.2 wide, 29.7 high, 68.4 mounting centres, 2 x 6.0 x 4.6 slots); `socket-782-2C-SKT.step`, `socket-782-2C-SKT-2d.dwg`.
- `model.step`: relay STEP, one solid (case, base and pins merged), read back with Open CASCADE 2026-11-03 (sections below the base).
- Not on file: any cutaway, exploded view, principle-of-operation drawing, coil winding data, spring data, contact gap, UL 508 / IEC 60947-5-1 figure. The internal construction below is therefore stated as principle; every proportion not on a document is NOT ON FILE.

## Mechanism (one paragraph)
Current through the coil (pins 13 A1 +, 14 A2 −) magnetises an iron core; the magnetic pull across the air gap draws a hinged iron armature to the core once the coil voltage reaches the pull-in level (at or below 80 % of 24 V, p. 3). The armature, through an actuator, moves the two moving contact blades (the commons, pins 9 and 12) away from the normally closed contacts (pins 1 and 4) onto the normally open contacts (pins 5 and 8). A return spring opposes the magnet; when the coil voltage falls to the drop-out level (the relay has released by 10 % of 24 V, p. 3) the spring returns the armature and the commons go back to the normally closed contacts. The same armature can be moved by hand with the push-to-test button, held there by the lock-down door, and its position is shown by the mechanical flag; an LED shows that the coil is powered (p. 1). Construction detail (clapper armature on a yoke, a card or lifter between armature and contact blades, the exact spring) is the usual ice-cube relay construction and is FIELD KNOWLEDGE, not shown on any document on file.

## Parts with figures (mm unless stated; document and page, or NOT ON FILE)
| part | figure | source |
|---|---|---|
| relay, overall (case + pins) | 21.08 x 27.94 x 46.48 | STEP read-back (no relay dimension drawing exists; datasheet_dims_note) |
| case above the base plane | 21.08 x 27.94 x 39.12 | STEP read-back (base plane at the pin root, y = 0 in the vendor file) |
| relay mass | 36 g | 78 spec p. 3 ('Weight 36g', 782 series) |
| case / cover | encapsulated, finger-grip cover, IP40; material NOT ON FILE; wall thickness NOT ON FILE | spec p. 1, p. 3; datasheet p. 1 |
| contact pins (6) | blade 4.75 x 0.51, about 7.4 long below the base, with a hole at mid-length (section at 3.7 mm shows two 0.99 mm webs) | STEP read-back |
| contact pin field | two columns 11.42 apart (x ±5.71); three rows at 5.89 and 4.70 pitch | STEP read-back |
| coil pins (2) | blade 0.51 x 4.75 (turned 90° to the contact pins), 13.72 apart (x ±6.86), one row beyond the contact rows | STEP read-back |
| pin assignment | pole 1: common 9 (IEC 11), N.C. 1 (12), N.O. 5 (14); pole 2: common 12 (41), N.C. 4 (42), N.O. 8 (44); coil 13 (A1, +), 14 (A2, −) | spec p. 5 (viewed from the pin end) |
| pin rows to pin numbers | row next to the coil pins = commons 9 / 12; middle row = N.O. 5 / 8; far row = N.C. 1 / 4 | derived: the p. 5 diagram layout matched to the STEP rows; left and right as viewed from the pin end |
| coil | 24 VDC, 640 Ω, 1.15 W DC | spec p. 3 |
| coil current | 37.5 mA from V / R; 47.9 mA from P / V | derived; the two disagree: 24² / 640 = 0.90 W, not the stated 1.15 W (recorded, not resolved) |
| coil turns, wire gauge, inductance, bobbin size | NOT ON FILE | - |
| pull-in voltage | ≤ 80 % of nominal = 19.2 V | spec p. 3 (782, 24 VDC column, table image) |
| drop-out voltage | ≥ 10 % of nominal = 2.4 V | spec p. 3 (same) |
| max continuous coil voltage | 110 % = 26.4 V | spec p. 3 |
| response time | 20 ms (operate or release not stated) | spec p. 3 |
| core, yoke | NOT ON FILE (material, section, length) | - |
| armature | NOT ON FILE (mass, pivot, travel, air gap) | - |
| return spring | NOT ON FILE (free length, rate, preload) | - |
| contact material | silver alloy, gold flashed (alloy NOT ON FILE) | spec p. 1, p. 3 |
| contact gap, contact diameter, contact force, over-travel | NOT ON FILE | - |
| contact rating, resistive | 15 A at 28 VDC, 120 VAC, 277 VAC (nominal and UL); CSA 12 A at 28 VDC and 277 VAC | spec p. 3 |
| contact rating, motor | 1/2 hp at 120 VAC, 1 hp at 277 VAC (UL); 1,000 cycles in a motor application (UL 508 Table 45.1) | spec p. 3 |
| pilot duty | NEMA B300 (5 A thermal; 120 V: 30 A make / 3 A break; 3600 / 360 VA) | spec p. 3 |
| minimum switching | 10 mA at 17 VDC | spec p. 3; p. 2 note 'not recommended for low current switching' |
| dielectric strength | coil to contact 2000 V rms; between poles 2000 V rms; across open contacts 1500 V rms | spec p. 3 (p. 1 says 'up to 2500V rms' open contact: the two disagree, recorded) |
| life | mechanical 10,000,000 operations (not powered); electrical 100,000 operations at rated resistive load | spec p. 3 |
| environment | −40 to +55 °C; vibration ±1 mm 10–35 Hz and 3 gn 35–50 Hz; shock 15 gn | spec p. 3 |
| LED indicator | present (colour, forward voltage, series resistor, polarity protection NOT ON FILE) | datasheet p. 1; spec p. 1 |
| mechanical flag | present, shows status in manual or powered condition (geometry NOT ON FILE) | spec p. 1 |
| push-to-test button, lock-down door | present; button operates the contacts without coil power; door holds button and contacts in the operate position (travel, force NOT ON FILE) | spec p. 1; datasheet p. 1 'encapsulated push-to-test' |
| socket | 79.2 x 29.2 x 29.7; mounting centres 68.4; 2 x 6.0 x 4.6 slots; 35 mm DIN or panel; 8 screw terminals, 1.0 N-m, 12–20 AWG one or two identical wires; holding clip | socket drawing p. 1 (by eye); sockets spec p. 1 |
| suppression module (option) | diode module for the 782 socket, 6–250 VDC; MOV modules 24 / 120 / 240 V; "fit within the maximum dimensions of the relay and socket" | spec p. 7 |

## Kinematics
- Armature: rotates about a pivot on the yoke (axis, position and angle NOT ON FILE); travel ends at the core (energised) and at the back stop (released). Node `armature`.
- Commons (moving contact blades, one per pole): driven by the armature through the actuator; each common rests on its N.C. contact released and on its N.O. contact energised. Nodes `pole-1`, `pole-2` (the twin needs only which side each touches; the blade bend itself is NOT ON FILE).
- Return spring: stretched or bent by the armature when energised; returns it on release. Node fixed (its state is the armature's).
- Push-to-test button: translates into the case and drives the actuator to the operate position (travel NOT ON FILE). Node `btn-test`.
- Lock-down door: rotates over the button to hold it in (angle NOT ON FILE). Node `door-lock`.
- Flag: follows the actuator (indicates operate in manual or powered condition). Node `flag`.
- LED: lit while the coil has voltage (p. 1); it does not show the contact position (the flag does). Node `led-coil`.
- Contacts touch: common 9 with 1 (released) or 5 (operated); common 12 with 4 or 8. Pins touch the socket's contact clips; the socket's screw terminals take the field wires (x06).

## What the mechanism teaches
1. Pull-in versus drop-out: the relay operates at 19.2 V or less but holds down to 2.4 V or less; the magnetic pull grows as the gap closes, so it takes far less current to hold than to pull in (x03, e17).
2. A changeover contact: one moving common, one N.C. and one N.O. contact per pole, and the spring that brings it back (m18, e17); contact life (100,000 electrical against 10,000,000 mechanical operations) shows that switching current, not motion, wears the contacts (x07, m17).
3. A coil is an inductor: switching it off makes a voltage spike, which the diode or MOV module clamps (p. 7, e13, x13); and contacts bounce on closing (p. 7, x14).

## For relay-ice-cube-2co 1.1 (2026-11-03, validation suite GEO-010 / MOT-010): what the STEP shows
Figures only; element.py is not edited here.
- The vendor STEP is one solid, 100 % filled (22,953 mm3 against a 23,041 mm3 case box): the case's inner width, wall thickness, the yoke and the hinge position are NOT ON FILE (the model's 0.8 wall and the hinge at z 13 stay Assumptions; the suite's 14.2 against 13.17 is between two Assumptions).
- Front face (relay-centred coordinates, case face at y −39.12), read from the STEP's plane and cylinder faces:
  - push-to-test button: a 4.1 × 4.1 square at x +4.04 … +8.15, z −11.46 … −7.34 (centre x +6.1, z −9.4), recessed 0.26, with a Ø2.16 centre feature 0.51 deep. The model puts the button at x 0, z −9: it should move +6.1 in x, which also takes it out of the door's path.
  - lock-down door: a 12.3 × 4.6 strip at x −9.98 … +2.34, z −11.68 … −7.11, recessed 0.13 / 0.18, beside the button in the same z band; the STEP shows no hinge or pivot, which reads as a slider along x rather than a door rotating 180°. Its travel is NOT ON FILE (spec p. 1 says only that it 'holds pushbutton and contacts in the operate position').
  - LED: a Ø1.78 boss at x −5.33, z +11.18, 0.89 proud (the model: x −6.5, z +10, r 1.4).
  - flag window: 7.4 × 3.2 at x +1.65 … +9.02, z +6.97 … +10.15, 1.27 deep.
  - the test-button opening in the case is therefore the 4.1 square at the position above; the suite's 'no opening' finding is a model gap.

---
2026-11-03, Stage 0b of the interior-first programme (kit-and-interior prompt Part B with the addendum). Figures are cited by document and page or read back from the vendor STEP; 'derived' marks arithmetic on cited figures; 'FIELD KNOWLEDGE' marks construction that no document on file shows; NOT ON FILE is never filled in.
