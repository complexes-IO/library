# contactor-9a-1no1nc · measure brief

Element `contactor-9a-1no1nc`: WEG CWB9-11-30C03 IEC contactor (AutomationDirect), 9 A AC-3, 3 N.O. power poles, built-in 1 N.O. + 1 N.C. auxiliary, 24 VDC coil, UL 508, 5 kA SCCR, 5 hp at 480 V; with the front-mount auxiliary block BFB-11 (1 N.O. + 1 N.C., 6 A at 120 VAC). Control rail: the motor contactor of the starter stack, overload RW27 direct-mounted below it (mounting map section 2).

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing CWB9-11-30C03, one page (p. 1), mm [in]: 98.5 [3.88], 78.4 [3.09], 44.8 [1.76]; 35 mm rail; 70.0 / 35.0 hole pattern.
- `references/CWB9-11-30C03-2d.dwg`: the same drawing as DWG.
- `references/datasheet.pdf`: AutomationDirect product cutsheet, one page (p. 1): 9 A, 24 VDC coil, (1) N.O./(1) N.C. aux, 5 hp, 5 kA SCCR, 'Mounting 35mm DIN rail or panel', UL E202315.
- `references/technical-specifications-cwb-series.pdf`: WEG CWB series pages, 27 pages: features p. 1, auxiliary blocks table p. 4 (BFB-11: for CWB9 through CWB80, max 4 added contacts, 63 g), general specifications p. 6 and p. 11 ('Mounting with screws or DIN 35mm rail (EN 50022)', main terminals IP10, coil and aux IP20), terminal capacity p. 9 (CWB9 power 1 x 18-10 AWG, Phillips No. 2), frame widths p. 17 ('45mm wide up to 38A').
- `references/aux-BFB-11-datasheet.pdf` (p. 1: 'Mounting Front', screw terminal, 6 A at 120 VAC), `references/aux-BFB-11-drawing.pdf` (p. 1) and `-2d.dwg`, `references/aux-BFB-11.step`: the front auxiliary block.
- `references/source.txt`: page verification (the 24 VAC twin CWB9-11-30D02 is not this part).
- `model.step`: AutomationDirect STEP (inch), 44 solids.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| width (3 poles) | 44.8 | 2-D drawing p. 1; '45mm wide' CWB spec p. 17 |
| height (terminals top to bottom) | 78.4 | 2-D drawing p. 1 |
| depth alone (rail back to coil face) | 98.5 | 2-D drawing p. 1 |
| screw-mount hole pattern | 70.0 x 35.0, four holes Ø4.5 [0.18] (2026-11-03) | 2-D drawing p. 1 |
| aux block BFB-11 W x H x D | 45.0 x 46.0 x 42.0 | BFB-11 drawing p. 1 |
| depth with the BFB-11 fitted | 140.5 | derived: 98.5 + 42.0 (the block sits on the coil face; overlap of the latch not dimensioned) |
| rail | 35 mm EN 50022 | CWB spec p. 6 / p. 11; cutsheet p. 1 |

## STEP read-back (Open CASCADE)
- model.step: 44 solids, 2405 faces, extents 98.65 x 78.4 x 44.8 mm (declared inch); datasheet check 44.8 exact, 78.4 exact, 98.5 vs 98.65 (0.15).
- Largest solids: coil / front housing 59.3 x 78.0 x 44.8; rear base 45.7 x 78.4 x 44.8 (the two halves of the 98.65 depth); a 55.2 x 10.0 x 41.6 bar at the front (the aux terminal row); two 10.5 to 11.5 wide lugs 44.8 long (the rail latch and the mounting foot); eight 12.7 x 8.5 to 9.7 x 13 terminal clamps (six power, two aux).
- aux-BFB-11.step: 29 solids, 3300 faces, extents 45.0 x 46.0 x 42.0 mm; body 45.1 x 35.8 x 42.1 plus a 14.0 x 44.1 x 27.2 latch tongue and five 11.7 x 12.7 x 7.0 clamps.
- AutoCAD 2026 import VERIFIED for model.step, extents match.

## Mounting
35 mm rail or two screws on the 70 x 35 pattern (drawing p. 1; spec p. 6). The overload clips directly to the lower power terminals (RW spec: 'direct mount power connection'); the BFB-11 snaps on the front. Mounting map section 2: CWB9 + RW27 stack 44.8 wide, 136.4 high with the overload below.

## Build notes (own model)
- Body 44.8 x 78.4 x 98.5 as two blocks: rear base (rail foot, 45.7 deep) and front coil housing (59.3 deep) with the stepped terminal row; three power terminals top and bottom (6 screws), two aux terminals at the front top; rail notch at the back face.
- BFB-11 as a separate carried element (bom.csv), 45.0 x 46.0 x 42.0 on the coil face; its latch overlap with the contactor is NOT ON FILE (take the fitted depth from the two STEPs mated, mark 'from the STEP').
- Datum: rail centreline; the overload's position below follows from the terminal pitch, which is not dimensioned on the drawing (NOT ON FILE; read from the two STEPs when mating).

## Origin
Rail device (README Conventions, EM 2026-11-03): back face on the rail crown y = 0, rail centreline z = 0, left edge x = 0, body toward -y.

## Named nodes
- None that moves visibly: the armature is inside; no mechanical position indicator is documented on the cutsheet or the spec pages read. The twin carries the contactor state in the circuit (coil energised), not in geometry.
- Terminal screws: fixed, no node.

## Ports
None of the M12 kind: screw terminals L1/T1, L2/T2, L3/T3 (power, 1 x 18-10 AWG, spec p. 9), A1/A2 coil, 13/14 and 21/22 built-in aux; BFB-11 adds 53/54 and 61/62 (terminal marks per IEC 60947; the drawing shows the terminal row, individual marks not dimensioned).

## Decals
- Front: terminal marks and the WEG rating label (not reproduced: no vendor name or logo on a print).
- Coil face: '24 VDC' coil mark, position NOT ON FILE.

## Status
Figures VERIFIED (3 of 3 within 0.15 mm; aux block 3 of 3 exact); fitted depth and terminal pitch NOT ON FILE; licence AutomationDirect REVIEW. Stage 0 COMPLETE 2026-11-03.

## Mate with the overload (2026-11-03, validation suite MATE-010 / GEO-020)
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
