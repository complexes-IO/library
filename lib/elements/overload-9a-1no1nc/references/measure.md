# overload-9a-1no1nc · measure brief

Element `overload-9a-1no1nc`: WEG RW27-2D3-U010 thermal overload relay (AutomationDirect), bi-metallic, 7.0 to 10.0 A adjustable (set 9 A), trip class 10, phase-loss sensitive, 1 N.O. + 1 N.C. aux, multifunction RESET/TEST button, direct mount to the CWB9 contactor. Control rail: below the contactor in the starter stack (mounting map section 2).

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing RW27-2D3-U010, one page (p. 1), mm [in]: 45.0 [1.77] wide, 71.7 [2.82] high, side view 6.7 [0.26] + 77.0 [3.03] deep, body 47.0 [1.85] behind the pins; title block says '8.0-10A' (vendor inconsistency with the page's 7.0-10.0 A, recorded in source.txt).
- `references/RW27-2D3-U010-2d.dwg`: the same drawing as DWG.
- `references/datasheet.pdf`: AutomationDirect product cutsheet, one page (p. 1): 7.0-10.0 A, bi-metallic, (1) N.O./(1) N.C., class 10, 'Reset Local', phase-loss sensitive, 'Connection Direct mount power', for CWB9 to CWB38.
- `references/technical-specifications-rw-series.pdf`: WEG RW series pages, 18 pages: features and terminals p. 1, operation p. 2 (multifunction RESET/TEST button with four positions A / AUTO / HAND / H, 'selected by rotating without pressing the red button'; 'Dial FLA setting ... continuously adjustable dial'), selection table p. 3 (RW27-2D3-U010; ambient compensation -20 to +60 C), mounting p. 4 and p. 9 (35 mm rail with the BF27-2D bracket), terminal data p. 6, p. 10, p. 16.
- `model.step`: AutomationDirect STEP (mm), 39 solids.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| width | 45.0 | 2-D drawing p. 1 |
| height with the connection pins | 71.7 | 2-D drawing p. 1 |
| depth overall (pins to front) | 83.7 | 2-D drawing p. 1 (6.7 + 77.0) |
| body depth behind the pins | 47.0 | 2-D drawing p. 1 |
| trip current range | 7.0 to 10.0 A | cutsheet p. 1; RW spec p. 3 |

## STEP read-back (Open CASCADE)
- model.step: 39 solids, 2444 faces, extents 45.0 x 71.65 x 83.7 mm (mm); datasheet check 45.0 exact, 71.7 vs 71.65 (0.05), 83.7 exact.
- Largest solids: main body 45.1 x 47.0 x 77.0; front module 45.2 x 27.8 x 54.7 (the button and dial face); a 44.9 x 21.5 x 51.2 inner block; a 43.7 x 32.3 x 9.0 terminal cover; three 7.8 x 9.2 x 15.2 solids at 14.5 pitch, which are the motor terminal clamps T1 T2 T3 at the bottom (corrected 2026-11-03: the 2026-11-02 brief called them the direct-mount pins; the pins are three Ø2.5 rods at 14.0 pitch, see 'Mate with the contactor'); a 16.6 x 9.2 x 8.0 part at the front (the RESET/TEST button).
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
Direct mount: the three pins plug into the CWB9's lower power terminals (cutsheet p. 1; RW spec p. 1); separate 35 mm rail or panel mounting only with the BF27-2D bracket (spec p. 4, p. 9; not on disk, not needed). Mounting map section 2: stack height 136.4 with the contactor.

## Build notes (own model)
- Body 45.0 x 47.0 x 77.0 plus the 6.7 pin offset (83.7 overall) and the pin row on top; front face carries the FLA dial, the RESET/TEST button and the aux terminals 95/96, 97/98.
- Pin pitch **14.0** (drawing p. 1 front view, '14.0 [0.55]' twice; STEP Ø2.5 pins at x 5.3 / 19.3 / 33.3), equal to the CWB9 main-terminal pitch 14.0 (contactor STEP). Corrected 2026-11-03: this line said 14.5 'from the STEP', which was the motor-terminal pitch at the bottom.
- Datum: the contactor's rail centreline; the overload hangs from the contactor's lower terminals.

## Origin
Carried element: it has no rail of its own, so its origin is the contactor's (rail device) and it is placed by the pin row. For a stand-alone build (BF27-2D bracket) the rail-device convention applies: Rail device (README Conventions, EM 2026-11-03): back face on the rail crown y = 0, rail centreline z = 0, left edge x = 0, body toward -y.

## Named nodes
- `node:btn-reset`: the red multifunction RESET/TEST button, kind translate (press) and rotate (four positions A / AUTO / HAND / H, RW spec p. 2); press travel and the index angle are NOT ON FILE.
- `node:dial-fla`: the trip-current dial, kind rotate, 7.0 to 10.0 A (spec p. 2 'continuously adjustable'); the angle span is NOT ON FILE.
- Trip indication: no lamp; whether the button pops on trip is not stated in the pages read, so no indicator node is declared.

## Ports
None of the M12 kind: three direct-mount pins to the contactor (L1/L2/L3 in), T1/T2/T3 motor terminals at the bottom, aux 95/96 (N.C.) and 97/98 (N.O.) at the front (spec p. 2), aux 16-12 AWG (spec p. 6).

## Decals
- Front: dial scale 7 to 10 A, button positions 'A / AUTO / HAND / H', terminal marks 95-96-97-98 (spec p. 2); the WEG label not reproduced.

## Status
Figures VERIFIED (3 of 3 within 0.05 mm); pin pitch 14.0 on the drawing and the STEP (corrected 2026-11-03); button travel and dial angle NOT ON FILE; licence AutomationDirect REVIEW. Stage 0 COMPLETE 2026-11-03.

## Mate with the contactor (2026-11-03, validation suite MATE-010 / GEO-020)
Pitch and seat measured on the two reference STEPs placed as the overload's own drawing installs them (overload `dimensional-drawing.pdf` p. 1, view 'CONTACTOR / OVERLOAD' and table 'OVERLOAD INSTALL DIMENSIONS': A = 136.4 [5.37] for CWB9–CWB18).

| figure | value (mm) | tolerance | source |
|---|---|---|---|
| main terminal pitch (L1-L2-L3 and T1-T2-T3) | 14.0 | NOT ON FILE (drawing note 2: 'dimensions do not imply tolerance'); STEP read-back agrees to 0.05 | contactor STEP read-back: lower clamps at z −14.0 / 0.0 / +14.0, upper clamps the same, terminal screws −13.95 / 0.05 / 14.05 |
| overload pin pitch at the tips | **14.0** | as above | overload drawing p. 1 front view: '14.0 [0.55]' twice between the three Ø2.5 pins; overload STEP: Ø2.5 pins at x 5.3 / 19.3 / 33.3 |
| overload motor-terminal pitch (T1 T2 T3 at the bottom) | 14.5 | as above | overload drawing p. 1: '14.5 [0.57]' twice; STEP terminal clamps at x 8.0 / 22.5 / 37.0. **This is the figure the 2026-11-02 brief wrongly gave as the pin pitch.** |
| pin row offset from the overload body centre line | 3.2 (pins at 19.3, body centre 22.5) | NOT ON FILE | overload STEP read-back; drawing p. 1 front view shows the pins left of centre |
| rail centre line to the contactor top / bottom | +39.6 / −38.8 (body 78.4) | NOT ON FILE | contactor STEP: rail groove lips at y ±18.4 about y = 0, body y −38.8 … +39.6 |
| rail centre line to the overload bottom | −96.8 | derived | +39.6 − 136.4 (drawing install dimension A) |
| rail centre line to the overload's full-depth body top (47.0 above its bottom) | −49.8 | derived | overload drawing p. 1 side view '47.0 [1.85]'; STEP body top at y 0 |
| rail centre line to the overload's upper housing top (57.6 above its bottom) | **−39.2** (0.4 below the contactor's bottom face) | derived | overload STEP read-back (60 mm-deep upper housing around the pins ends at y +10.6) |
| rail centre line to the top of the pin sleeves (Ø4.4 → Ø4.3, 60.9 above the bottom) | −35.9 (2.9 into the contactor) | derived | overload STEP read-back |
| rail centre line to the pin tips (Ø2.5, 71.7 above the bottom) | −25.1 (through the lower clamps at −36.1 … −27.6) | derived | overload drawing p. 1 '71.7 [2.82]'; STEP |
| overload hooks (2, at the rear) top | about −29.5 | derived | overload STEP read-back (y +20.3) |

Consequences for the next versions (figures only; element.py is not edited here): the pin pitch is 14.0 on both parts, so the contactor is right and the overload's `PIN_PITCH = 14.5` is the error; the overload's top-face seat at rail −39.2 (BOM) is right for its upper housing, and the GEO-020 overlap comes from the overload's pins being modelled as 7.8 × 9.2 blocks instead of Ø2.5 rods with Ø4.4 sleeves; the overload's body is 57.6 tall to the upper housing (47.0 at full depth), not 65; the pin row sits 3.2 off the body centre.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
