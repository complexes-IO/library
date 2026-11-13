# motor-iec71-370w · measure brief

Element `motor-iec71-370w`: 0.37 kW (1/2 hp) IE2 three-phase TEFC induction motor, IEC 71B frame, B3 rigid base, 230/460 VAC, 1690 rpm, 14 mm shaft with 5 x 5 x 25 key, aluminium, top (F3) terminal box with M20 x 1.5 entry. M.G.M. Electric Motors SMX series, AutomationDirect 0NUL. The machine's motor m1 (mc-motor-1 BOM, planned), fed by port p-m1 through cable-pwr-480.

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing 0NUL (6/3/2024), one page (p. 1), inch [mm] text layer: 111.0, 45.0, 25.0, 30.0, 81.0, 116.0, Ø138.0, 250.5, 90.0, 7.0 (x2), M20-1.5, 5 x 5 x 25 key, 110.0, 75.0, 71.0, 8.0, 104.5, 136.0, 112.0, 2 x 10.5, Ø14.0, 5.0, M5; 'IEC 71 FRAME, ALUMINUM, RIGID BASE (B3)'.
- `references/0NUL-2d.dwg`: the same drawing as DWG.
- `references/datasheet.pdf`: AutomationDirect cutsheet, one page (p. 1): 1/2 hp, 230/460 VAC, 1800 / 1690 rpm, TEFC, 'Shaft Type Round with square key', 'Shaft Diameter 14mm', 'Motor Frame IEC 71B', aluminium, 'Junction Box Orientation F3', 'Mounting Rigid base (B3)', horizontal or vertical, CSA 189724.
- `references/technical-specifications-mgm-iec-motors.pdf`: MGM IEC motor pages, 4 pages: features p. 1 (TEFC, aluminium, F3 top junction box with threaded entries, ring-lug terminals, IP55, class F, 5:1 / 1000:1 inverter ratings, B3 / B5 / B14 / B34 / B35 options), selection table p. 2 (0NUL row; mounting codes), performance table p. 3 (0NUL row: FLA 0.91 A at 460 V, 1.82 A at 230 V; ratings.csv `fla`).
- `references/installation-manual.pdf`: MGM use and maintenance manual, 68 pages: safety and mounting p. 15 to 16 (half key fitted on the shaft end per IEC 60034-14, flat mounting surface for the feet), terminal box p. 17, maintenance p. 21 to 22.
- `model.step`: AutomationDirect STEP (inch), 24 solids.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| overall length | 250.5 | 2-D drawing p. 1 |
| shaft height (foot to shaft centre) | 71.0 | 2-D drawing p. 1 (IEC 71) |
| height above the shaft centre (terminal box top) | 104.5 | 2-D drawing p. 1 |
| overall height | 175.5 | derived: 71.0 + 104.5 |
| fan cover diameter | 138.0 | 2-D drawing p. 1 |
| feet: width across / foot length / foot hole pattern | 136.0 / 90.0 / 112.0 x 90.0, 2 slots per side, 7.0 along the shaft x 10.5 across (K = 7) | 2-D drawing p. 1 (slot reading: 1.2, 2026-11-03) |
| foot thickness | 8.0 | 2-D drawing p. 1 |
| slot width along the shaft | 7.0 (x2: one per slot row) | 2-D drawing p. 1 (1.2 read the 7.0 (x2) as the slots' K, not a foot plate) |
| shaft Ø / extension / key | 14.0 / 30.0 / 5 x 5 x 25 | 2-D drawing p. 1; cutsheet p. 1 |
| shaft end tapped | M5 (detail A) | 2-D drawing p. 1 |
| terminal box W x L / entry | 81.0 x 110.0 / M20 x 1.5 | 2-D drawing p. 1 |
| body length figures | 111.0, 116.0, 45.0, 25.0, 75.0 (positions along the frame) | 2-D drawing p. 1 (assignment to the STEP solids below) |

## STEP read-back (Open CASCADE)
- model.step: 24 solids, 3315 faces, extents 250.5 x 175.501 x 138.0 mm (declared inch); datasheet check 138.0, 175.5, 250.5 all exact.
- Largest solids: stator frame 123.0 long x 148.2 x 137.5 (with the fins); fan cover 72.0 long x Ø149.4 (the cover's outer ribs reach 149.4 while the drawing's 138.0 is the cover body); two end shields 29.0 x 129.2 x 125.0; terminal box 80.0 x 74.0 x 28.5 tall on a 81.0 x 75.0 x 2.0 gasket plate; the shaft 237.0 long x Ø22.0 (the full rotor shaft inside, 14.0 at the extension); a 120.4 x 9.2 x 9.2 bar (the lifting / fin strip); feet and key as smaller solids.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
B3 feet: four bolts on 112.0 (across) x 90.0 (along) through 2 slots per side, 7.0 along the shaft x 10.5 across (drawing p. 1), feet 136.0 wide; flat surface (manual p. 16). Placed on the bench mc-motor-1 (bench-1800 top) by the foot holes.

## Build notes (own model)
- Body: cylindrical frame Ø138.0 (fins as a ribbed skin or plain), two end shields, fan cover Ø138 x 72 with a louvered rear face (decal), terminal box 81 x 110 x 28.5 on top at F3 with the M20 entry on the right, feet 136 wide x 8 thick with 4 slots 7.0 x 10.5 (length: spec.md open figures), shaft Ø14 x 30 with the 5 x 5 x 25 key and the M5 centre hole, overall 250.5 long, shaft centre 71.0 above the feet.
- The frame's internal positions (111.0, 116.0, 45.0, 25.0, 75.0) are the drawing's station figures; assign them to the STEP solids when cutting the generator (frame 123.0 vs drawing 116.0 / 111.0: the drawing dimensions the fin tips and the shield faces separately; keep 250.5 overall exact).
- Datum: the foot plane and the shaft axis; drive end toward -y.

## Origin
Floor / bench machine class (README Conventions: floor machine at the floor plane, front-left anchor hole): the foot plane z = 0, the front-left foot slot centre x = 0, y = 0, shaft axis at z = 71.0 pointing toward -y (drive end).

## Named nodes
- `node:shaft`: the shaft with its key, kind rotate about y, continuous (range 0 to 360, the twin spins it with the drive speed).
- `node:fan`: the external fan behind the cover, kind rotate about y, same speed (only visible through the louvers; optional).
- No lamp; the terminal box lid is fixed.

## Ports
- `node:pwr`: the terminal box entry (M20 x 1.5, drawing p. 1), kind port, unit 480V-3P+E; U1 / V1 / W1 ring-lug terminals inside (spec p. 1), connections.csv row panel-1.p-m1 -> machine-1.m1.pwr.
- PE: the frame bonding terminal (manual p. 17), part of the ground section.

## Decals
- Nameplate on the frame side (cutsheet: 'Nameplate RPM 1690'; the plate's size and position are NOT ON FILE: read from the STEP as a rectangle on the frame if present, else EM's tag-plate device size).
- Rotation arrow on the fan cover, 'M20' at the entry: positions NOT ON FILE.

## Status
Figures VERIFIED (3 of 3 exact); the station figures along the frame are assigned at Stage 1 and marked; nameplate size NOT ON FILE; licence AutomationDirect REVIEW. Stage 0 COMPLETE 2026-11-03.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
2026-11-05 (mech-r13, unattended, no vendor file opened): the foot-hole lines corrected to the 1.2 reading already on file (spec.md history 1.2, features.csv: slots 7.0 x 10.5, K = 7; the 7.0 (x2) is the slot width, not a foot plate); p. 3 of the motor specifications added to the document list from ratings.csv `fla`. Review findings 1 and 2 (the 45.0 / 75.0 / 110.0 assignment) still need a look at drawing p. 1.
