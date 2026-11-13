# relay-safety-2ch-2no1nc · measure brief

Element `relay-safety-2ch-2no1nc`: Allen-Bradley Guardmaster 440R-S13R2 (Rockwell, RESTRICTED licence) Compatibility Input safety relay, one dual-channel universal input, 2 N.O. safety outputs (13/14, 23/24), one N.C. auxiliary (41/42), single-wire safety output L11, 22.5 mm DIN-rail housing with four removable terminal blocks. Control rail: the safety relay of the E-stop circuit (electrical architecture section 4).

## Documents on file
- `references/installation-manual.pdf`: Rockwell 440R-UM013I-EN-P (July 2024), 84 pages: hardware features p. 9 ('only 22.5 mm wide with four removable terminal blocks', PWR/Fault status indicator), mounting dimensions p. 11 (Figure 2, 113.6 x 119.14 mm; 35 x 7.5 x 1 mm rail; 10 mm to the neighbour, 50.8 mm clearance above, below and in front), wire size p. 13 (0.2 to 2.5 mm2), face markings p. 14 (Figure 6 image; Table 2 terminal functions: A1, A2, S11, S21, S12, S22, S34, L11, 13/14, 23/24, 41/42 for the CI), status indicators p. 31, Appendix A p. 73 ('Dimensions, HxWxD 119.14 x 22.5 x 113.6', 225 g), outputs p. 75.
- `references/440r-td001-msr-technical-data.pdf`: Guardmaster technical data, 24 pages (per-relay tables p. 3 to 23: 22.5 mm, 35 mm rail, reset and terminal data).
- `references/cutsheet.html`, `references/dimensional-drawing.dwg`: Rockwell product page copy and the family 2-D drawing (440R-S12R2 family file).
- `references/440r-s12r2_new_asm.zip`: the family STEP as served (440R-S12R2 SI model, Pro/ENGINEER 2011 surface export).
- `model.step`: that STEP unpacked: 0 solids, 757 faces (surfaces only).

## Figures (mm)
| feature | mm | source |
|---|---|---|
| height | 119.14 | manual p. 11 Figure 2; Appendix A p. 73 |
| width | 22.5 | manual p. 9, p. 73 |
| depth | 113.6 | manual p. 11, p. 73 |
| rail | 35 x 7.5 x 1 (EN 50022-35x7.5) | manual p. 11 |
| clearance | 50.8 above, below, in front; 10 to the neighbour | manual p. 11 |
| terminal wire | 0.2 to 2.5 mm2 (24 to 14 AWG) | manual p. 13 |

## STEP read-back (Open CASCADE)
- model.step: 0 solids, 757 faces, extents 118.58 x 117.87 x 22.50 mm (mm): a surface model, no closed shells; datasheet check 22.5 exact, 119.14 vs 118.58 (0.56, the removable terminal blocks' lips), 113.6 vs 117.87 (4.27 OVER: the family model carries the terminal blocks proud of the front face, MISMATCH recorded).
- No per-solid figures possible (no solids); the face set gives the housing, four terminal blocks and the rail latch as surfaces only.
- AutoCAD 2026 import VERIFIED as surfaces, extents match OCC.

## Mounting
35 mm rail (manual p. 11), in an IP54 enclosure; terminal blocks removable (manual p. 9, p. 70). Mounting map section 2.

## Build notes (own model)
- Housing 22.5 x 119.14 x 113.6 per the manual; four terminal blocks (two top, two bottom) 22.5 wide, each 4 terminals, proud of the front by the STEP's 4.3 (mark 'from the STEP'); rail latch at the back; front face with the status LEDs and the rotary configuration switch (CI has a mode selector per manual chapter 4; its position from the STEP only).
- Keep the RESTRICTED licence note: nothing of the Rockwell file ships; it is the baseline only.
- Datum: rail centreline, front face at +113.6 from the rail crown.

## Origin
Rail device (README Conventions, EM 2026-11-03): back face on the rail crown y = 0, rail centreline z = 0, left edge x = 0, body toward -y.

## Named nodes
- `node:led-pwr`: the PWR/Fault status indicator, kind emissive, green steady / red flashing fault codes (manual p. 9, p. 31).
- `node:led-in1`, `node:led-out`: input and output status indicators as marked on the face (manual p. 14 Figure 6, an image; names taken from Table 2's terminal functions, exact LED legend NOT read from text: confirm against p. 31 before Stage 1).
- `node:sw-mode`: the rotary configuration switch on the front, kind rotate, positions per manual chapter 4; the angle index is NOT ON FILE.

## Ports
None of the M12 kind: removable screw terminal blocks A1 / A2 (24 V), S11 / S21 (pulse test outputs), S12 / S22 (dual-channel input), S34 (reset), L11 (single-wire safety out), 13/14 and 23/24 (safety relay outputs), 41/42 (auxiliary N.C.) (manual p. 14 Table 2, CI column).

## Decals
- Front face markings: terminal identifiers above and below each block, LED legend, '440R-S13R2' and the Guardmaster mark (manual p. 14 Figure 6; the Rockwell marks are not reproduced on our print).

## Status
Figures: 2 of 3 VERIFIED (22.5, 119.14 within 0.6), depth MISMATCH explained (terminal blocks proud, 4.3 mm); surface-only STEP; licence Rockwell RESTRICTED (baseline only). Stage 0 COMPLETE 2026-11-03.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
