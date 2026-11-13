# io-block-m12-8di8do · measure brief

Element `io-block-m12-8di8do`: Lumberg Automation (Belden) LioN-X 0980 XSL 3923-121-007D-01F, part 935708001, 8DI/8DO multiprotocol I/O device: 8 M12 A-coded I/O ports (X1 to X4 inputs type 3, X5 to X8 outputs 2 A), 2 M12 D-coded Ethernet (X01, X02), 2 M12 L-coded power (X03 in, X04 out), zinc die-cast IP65/67/69K, rotary encoding switches for the protocol. Control rail: not on the rail; the field I/O block in the remote-io-node and on the motor-starter cell's machine side.

## Documents on file
- `references/datasheet.pdf`: Belden techdata, 5 pages: p. 1 technical drawing and 'Dimensions (W x H x D): 60 mm x 31 mm x 200 mm', 480 g, IP65/67/69K; p. 2 'Mount Type: 2 hole screw mounting, M4 x 25 / 30 screws', fastening torque M12 0.5 Nm, 'Attachable Labels: 15x', Ethernet M12 4-pole D-coded; p. 3 'Status Indicator (System Supply): LED green, Diagnostic Indicator: LED red', power M12 5-pole L-coded; p. 4 LEDs continued.
- `references/installation-manual.pdf`: Belden LioN-X manual (EtherNet/IP, V1.1 07/2023), 164 pages: designations p. 12 (Ch. A = pin 4, Ch. B = pin 2, DIA diagnostic LED, BF bus fault LED), I/O port overview p. 20 (8DI8DO without isolation: X5 to X8 DO 2 A, X1 to X4 DI type 3 with US), ground FE p. 26 (M4 thread), port assignments p. 32 (Ethernet: 1 TD+, 2 RD+, 3 TD-, 4 RD-), p. 33 (power: 1 US +24 V, 2 GND_UL, 3 GND_US, 4 UL +24 V, 5 FE), p. 35 (I/O: 1 +24 V, 2 Ch. B, 3 GND, 4 Ch. A, 5 FE), rotary switches p. 40, factory reset p. 42 (US LED green / red).
- `references/3D_step_935708001_LionX.zip`: the STEP as served.
- `model.step`: that STEP, 1 solid.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| width | 59.6 (drawing) / 60 (table) | techdata p. 1 drawing read by eye; p. 1 'Dimensions 60 mm' |
| length | 200.0 | techdata p. 1 |
| thickness | 30.7 (drawing) / 31 (table) | techdata p. 1 |
| M12 torque | 0.5 Nm | techdata p. 2 |

## Spacings (not size-checked)
Distances between features, not the size of any one solid, so the gate's size check (STEP overall / per-solid sizes) cannot find them. The element holds them in its constants; figures.md checks them against the vendor STEP each round (decision, round 7 prompt).
- port pitch: 27 (techdata p. 1 drawing)
- mounting holes: 190.5 apart on the length; 20 and 4 (drawing figures) (techdata p. 1 drawing; M4 screws p. 2)

## STEP read-back (Open CASCADE)
- model.step: 1 solid, 3431 faces, extents 59.587 x 199.801 x 30.7 mm (mm); datasheet check 30.7 exact, 59.6 vs 59.587 (0.01), 200.0 vs 199.801 (0.2).
- Single solid 59.6 x 199.9 x 32.4 by the per-solid pass (the 32.4 includes the M12 socket rims proud of the 30.7 body on the other axis of the vendor pose); the ports, switches and LED windows are features of the one body.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
Two M4 x 25 / 30 screws with toothed washers through the end lugs (techdata p. 2), 190.5 apart (drawing); FE stud M4 (manual p. 26). Not a rail device.

## Build notes (own model)
- Body 59.6 x 200.0 x 30.7 die-cast block, two end lugs with the 190.5 holes; 8 M12 sockets in two rows of 4 at 27 pitch, 2 D-coded Ethernet and 2 L-coded power sockets at the ends; LED windows beside each port; three rotary switches under a cover; FE stud.
- Socket positions across the width and the LED layout are from the STEP and the techdata drawing only (mark 'from the STEP').
- Datum: the mounting hole pair; body face flat on the machine frame.

## Origin
Panel / frame device: back face on the mounting surface y = 0, first mounting hole x = 0, z = 0 (README Conventions, panel device: back face, lower-left mounting hole), body toward -y.

## Named nodes
- `node:led-us`: system supply LED, kind emissive, green (red on fault / factory reset; techdata p. 3; manual p. 42).
- `node:led-dia`: diagnostic LED, kind emissive, red (techdata p. 3; manual p. 12).
- `node:led-x1` to `node:led-x8`: per-port channel LEDs (pins 4 and 2), kind emissive; their colours and count per port are NOT read from the pages searched (manual LED chapter not located by text search), confirm before Stage 1.
- `node:sw-x100`, `node:sw-x10`, `node:sw-x1`: rotary encoding switches, kind rotate, 0 to 9 (manual p. 40); the twin does not read them.

## Ports
- X1 to X8: M12 A-coded 5-pin sockets, 1 = +24 V, 2 = Ch. B, 3 = GND, 4 = Ch. A, 5 = FE (manual p. 35); X1 to X4 inputs, X5 to X8 outputs 2 A (manual p. 20).
- X01, X02: M12 D-coded 4-pin Ethernet, 1 TD+, 2 RD+, 3 TD-, 4 RD- (manual p. 32).
- X03 (in) / X04 (out): M12 L-coded 5-pin power, 1 US +24 V, 2 GND_UL, 3 GND_US, 4 UL +24 V, 5 FE (manual p. 33).
- Mates: `port-m12-a` / `cordset-m12-a` (A and D coded), the L-coded power cordset has no id yet.

## Decals
- Port labels X1 to X8, X01 / X02, X03 / X04 beside the sockets; attachable labels 15x (techdata p. 2); 'FE' at the ground stud (manual p. 26); the Belden / Lumberg marks not reproduced.

## Status
Figures VERIFIED (3 of 3 within 0.2 mm; the table's 60 x 31 rounds the drawing's 59.6 x 30.7); port pinouts on file; per-port LED set NOT ON FILE; licence Belden REVIEW. Stage 0 COMPLETE 2026-11-03.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.

## Face layout, Open CASCADE read-back (terminal 2026-11-04, rounds 5 and 6)
From `3D_step_935708001_LionX.zip` (one solid, 3431 unnamed faces, no thread or PMI entities): every face's type, axis, radius, exact box, normal and XCAF colour, and the edges of chosen faces' wires. Frame: io-block-m12-8di8do's (back face y 0, body toward -y, first mounting slot at x 0, z 0, length along +z): x = x_STEP, y = -(z_STEP + 17.6), z = y_STEP + 165.5. Depths below are given as distances off the back. Port names from techdata p. 1 (read by eye). Angles looking at the face, clockwise, 0° = +z.
These supersede the figures above where they differ: the thickness 30.7 is X03's sleeve only; the FE is a threaded hole, not a stud; the slots are 191.05 apart (the drawing's 190.5 is the screw pattern); there is no switch cover.

| feature | figure | how |
|---|---|---|
| housing face | 17.6 off the back (drawing side view 17.6); female inserts 21.0; X03's sleeve front 30.7 | coaxial faces at each port |
| body | x ±29.79; z -4.50 to 195.30; ends roll over through R5 rounds (housing face to the end face at 12.69 off the back) | face boxes |
| ports, Ø12.3 entries | x ±15.0; X03 (male L) / X04 (female L) z 12.0; X01 / X02 (D) z 39.0; X4 / X8 93.0; X3 / X7 120.0; X2 / X6 147.0; X1 / X5 174.0 (X1 to X4 and X01, X03 at x -15) | entry cylinders |
| clocking | X1 to X4 key 0°; X5 to X8 -90°; X01 tooth 0°; X02 -89.6°; X03 key block 45.0°; X04 recess -45.0° | key faces |
| channel LEDs | Ø3.6, face 0.1 proud; x -5.0 (X1 to X4) / +5.0 (X5 to X8); z port + 3.0 (A, pin 4, yellow) and - 3.0 (B, pin 2, white); colours manual p. 159 | lens faces; drawing A / B marks by eye |
| status LEDs | 7 at x -17.4, -11.6, -5.8, 0, 5.8, 11.6, 17.4, z 77.8 (Lnk/Act X01, Lnk/Act X02, MS / DIA, NS / BF, 5th NOT ON FILE (C), UL, US) | lens faces; labels techdata p. 1 by eye |
| rotary switches | x100 / x10 / x1 at x -20.7 / -6.9 / 6.9, z 66.2; knob Ø6.1, no cover | knob faces |
| cap | Ø12.3 at x 20.7, z 66.2, flush; no document names it (NOT ON FILE (C)) | face |
| FE | M4 threaded hole (Ø4.0 modelled plain) at x 20.0, z 0.504, Ø4.5 to 9.7 off the back, 0.3 chamfer to the seat | hole faces; manual p. 26 |
| mounting slots | 4.5 wide x 6.0: first across x (x ±0.75 centres) at z 0; far along z (z 190.30 / 191.80), centre 191.05 | slot faces; techdata p. 2 M4 x 25 / 30, 1 Nm |
| screw seats | floor 10.0 off the back (not 9.7: the slots' 0.3 chamfers run 9.7 to 10.0). First slot: open at the end, sides leaning 10° from (±5.92, -4.30) to (±4.92, 1.37), R5.0 arc centred (0, 0.504). FE: sides (14.58 / 25.42, -4.30) to (15.57 / 24.43, 1.29), R4.5 centred (20.0, 0.504). Far: R4.5 centred (0, 190.303), sides out to (±5.33, 194.64) | face wires |
| power-end label pocket | floor 13.4 off the back; x -25.70 to the first seat's wall and arc, z from the end round to 4.80; the plate (19.9 x 7.95, 1.0 thick) on it, top 14.4 | face wires |
| label plates | 13 (techdata: 15 attachable; 2 NOT ON FILE (C)): (±12.7, 24.2 / 51.2 / 105.2 / 132.2 / 159.2), (±15.0, 185.2), (-15.6, 0.7) | plate faces |
| back recess | 1.0 deep: x ±28.565, z -3.30 to 194.07, 1.0 x 45° corners, seven 0.19 bumps a side; full-height bosses round the first slot (x ±4.20, R3.45 arcs centred (±0.75, 0)), the FE hole (x 16.8 to 23.2, R3.2 centred (20, 0.504)) and the far slot (x ±3.45, R3.45 centred (0, 190.303)) | face wire |
| thread at the female ports | no thread feature; plain Ø10.917 from 1.10 to 6.00 behind the housing face; engagement and thread length NOT ON FILE (C) | coaxial faces |
