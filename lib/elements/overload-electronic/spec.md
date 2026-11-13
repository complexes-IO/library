# overload-electronic · v1.1 · electronic overload relay, self-powered, 0.4 … 2.0 A, class 10 (complexes.org generic)

**What** Electronic motor overload relay: three-pole, self-powered from the motor current, setting 0.4 … 2.0 A, trip class 10, one N.C. (95-96) and one N.O. (97-98) auxiliary contact, push-button reset, separate mounting on the 35 mm rail with line terminals L1 L2 L3 on top and motor terminals T1 T2 T3 below. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001080, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Electronic overload relay (ETIM 10.0 EC001080). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `OLEL` · parameters `setting` (0: the dial's angle, 0 … 270°), `pressed` (false: the reset button at the end of its stroke).

## Class values
ETIM 10.0 EC001080 "Electronic overload relay", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Mounting method (EF000003) | 35 mm DIN rail, separate mounting (EN 60715 TH35-7.5) |
| 2 | Type of electrical connection of main circuit (EF006819) | screw connection |
| 3 | Adjustable current range (EF008211) | 0.4 … 2.0 A |
| 4 | External power supply required (EF003292) | no (self-powered from the main circuit) |
| 5 | Rated control supply voltage AC 50 Hz (EF003978) | not stated (no control supply) |
| 6 | Rated control supply voltage AC 60 Hz (EF003979) | not stated (no control supply) |
| 7 | Rated control supply voltage DC (EF003980) | not stated (no control supply) |
| 8 | Voltage type for actuating (EF008242) | not stated (no control supply) |
| 9 | Number of auxiliary contacts as normally closed contact (EF001377) | 1 (95-96) |
| 10 | Number of auxiliary contacts as normally open contact (EF001376) | 1 (97-98) |
| 11 | Number of auxiliary contacts as change-over contact (EF003531) | 0 |
| 12 | Voltage type (operating voltage) (EF005294) | AC |
| 13 | Operating voltage AC 50 Hz (EF008206) | up to 690 V |
| 14 | Operating voltage AC 60 Hz (EF008207) | up to 690 V |
| 15 | Operating voltage DC (EF008208) | not stated (AC main circuit only) |
| 16 | Rated switch current (EF006706) | 5 A (auxiliary contacts, conventional thermal current) |
| 17 | Release class (EF006668) | CLASS 10 |
| 18 | Reset function automatic (EF011941) | no |
| 19 | Reset function input (EF011940) | no |
| 20 | Reset function push-button (EF011942) | yes |
| 21 | Width (EF000008) | 45 mm |
| 22 | Height (EF000040) | 90 mm |
| 23 | Depth (EF000049) | 83.5 mm (76.0 in front of the rail crown, 7.5 behind it; the dial stands 1.3 proud of that) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (ELR-010 reads `ir_min` / `ir_max`; status "generic design", source "ETIM 10.0 EC001080 class value" with the feature code, OPERATING.md 12); `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| base | 45.0 × 90.0 (z −45 … 45) × 46.0 deep: the main terminal shoulders at y −46 | design choice |
| front housing | x 2 … 43, z −28 … 18, front face at y −76.0 | design choice |
| auxiliary block | x 2 … 43, z 18 … 28, its face at y −66.0, on the upper shoulder | design choice |
| overall | 45.0 × 84.8 (y −77.3 … 7.5) × 90.0 | from the parts above; the dial and its pointer stand 1.3 proud |
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| main terminals | L1 L2 L3 on the top shoulder, T1 T2 T3 on the bottom one, 13.0 pitch at x 9.5 / 22.5 / 35.5; screw heads Ø5.6 × 1.2 at z ±38.0; wire entries 5.0 × 10.0 slots cut 0.5 into the end faces | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| auxiliary terminals | 95 96 97 98 on the block's face, 9.0 pitch at x 9 / 18 / 27 / 36; screw heads Ø4.0 × 1.2 at z 23.0; wire entries 3.2 × 8.0 slots cut 0.5 into the block's top face | design choice |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes (main and auxiliary), and the screws' thread and torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by IEC 60947-1 (terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| current-setting dial | Ø12.0 × 1.0 at x 13.0, z 4.0, pointer 4.8 × 1.2 × 0.3; turns 270° clockwise (seen from the front) from 0.4 A to 2.0 A | design choice |
| reset button | 7.2 square, 1.0 proud, in an 8.0 square pocket 7.0 deep at x 30.0, z 4.0; 2.0 stroke toward the mounting plane; blue, the reset colour of IEC 60204-1 10.2.1 (not on file: the colour is a design choice following it) | design choice |
| trip indicator | 6.0 × 4.0 window at x 27 … 33, z −12 … −8 | toolkit/din.py `indicator` (red tripped / green ready in the twin) |
| legend field | 35.0 × 10.0 (x 5 … 40, z −25 … −15), 0.1 proud | design choice |

## Named nodes
`dial-ir` (rotate about +y through the dial's centre, 0 … 270°: the current setting, 0° = 0.4 A, 270° = 2.0 A, linear) · `btn-reset` (translate +y, 0 … 2.0: pressed resets a tripped relay; reset is manual only) · `ind-trip` (emissive window: red when tripped, green when ready) · ports `t-L1`, `t-L2`, `t-L3`, `t-T1`, `t-T2`, `t-T3`, `t-95`, `t-96`, `t-97`, `t-98` (kind port, unit screw, gender none: a screw clamp, PIN-002). The twin reads the setting from `dial-ir`, trips by class 10 and shows it on `ind-trip`, with 95-96 open and 97-98 closed while tripped.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-ZINC` terminal screws · `M-GASKET` wire entries and the button pocket · `M-BLACK-PA` dial · `M-WHITE-PA` pointer and legend field · `M-BLUE` reset button · `M-RED-PA` trip indicator

## Decals (Blender)
On the legend field: "complexes.org generic", "overload-electronic", "CLASS 10", "0.4 – 2.0 A", the contact diagram (95-96 N.C., 97-98 N.O.). Around the dial: the scale 0.4 / 0.8 / 1.2 / 1.6 / 2.0 A over its 270°. "RESET" above the button, "TRIP" beside the indicator. Terminal marks beside each screw. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). Everything else this element meets is on file (the rail clip), and every other size is a design choice; nothing is guessed and shown as sourced.
- The trip curve is the class's: CLASS 10 is the release class (Class values 17), and the twin takes its trip times from the class 10 limits of IEC 60947-4-1 as the library already does for overload-9a-1no1nc (behaviour.md there); no curve of a product is copied. Phase-loss sensitivity, thermal memory, heat loss and the maximum back-up fuse are not features of the class and are not stated in 1.0.
- Separate mounting: it stands on the rail beside its contactor and is wired to it (T1 T2 T3 of the contactor to L1 L2 L3 here); it does not plug into contactor-9a-1no1nc (overload-9a-1no1nc is that one).
- Motor overload protection is protective, not a safety function to ISO 13849-1, and lib/inventory.csv has no row marking it safety; no safety sign-off is asked.

## Outputs (out/)
`overload-electronic.lsp` · `.glb` (pivots on the dial, button, indicator and ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at 1.0 (lane round elec-r18) and at 1.1 (elec-r20).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC001080), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07) |
| 1.1 | ratings.csv: the six class-value rows to status "generic design" and source "ETIM 10.0 EC001080 class value: <feature> (EFnnnnnn)", OPERATING.md 12's form (review cloud-elec 2026-11-07 r1, finding 1); no shape, node or figure change; gated on the PC (elec-r20, 2026-11-09) |
