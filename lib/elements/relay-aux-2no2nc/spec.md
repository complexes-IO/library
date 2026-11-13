# relay-aux-2no2nc · v1.3 · auxiliary contactor relay, 24 V DC coil, 2 NO + 2 NC (complexes.org generic)

**What** Auxiliary contactor (contactor relay) for control circuits: a 24 V DC coil switching two normally open and two normally closed contacts, screw terminals, on the 35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000196, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Auxiliary contactor, relay (ETIM 10.0 EC000196). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `RAUX` · parameter `operated` (false; true shows the carrier pulled in).

## Class values
ETIM 10.0 EC000196 "Auxiliary contactor, relay", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Rated control supply voltage AC 50 Hz (EF003978) | not stated (DC coil) |
| 2 | Rated control supply voltage AC 60 Hz (EF003979) | not stated (DC coil) |
| 3 | Rated control supply voltage DC (EF003980) | 24 V |
| 4 | Voltage type for actuating (EF008242) | DC |
| 5 | Rated operation current (EF007679) | 6 A (AC-15, 230 V) |
| 6 | Rated operation current Ie, 400 V (EF001378) | 3 A (AC-15) |
| 7 | Mounting method (EF000003) | 35 mm DIN rail (EN 60715 TH35-7.5) |
| 8 | With LED indication (EF005950) | yes (coil energised, yellow) |
| 9 | Suitable for manual operation (EF002978) | no |
| 10 | Interface (EF000594) | no |
| 11 | Number of auxiliary contacts as normally closed contact (EF001377) | 2 |
| 12 | Number of auxiliary contacts as normally open contact (EF001376) | 2 |
| 13 | Number of auxiliary contacts as normally closed contact, delayed switching (EF007281) | 0 |
| 14 | Number of auxiliary contacts as normally open contact, leading (EF007282) | 0 |
| 15 | Number of auxiliary contacts as change-over contact (EF003531) | 0 |
| 16 | Operating voltage AC 50 Hz (EF008206) | not stated (DC coil) |
| 17 | Operating voltage AC 60 Hz (EF008207) | not stated (DC coil) |
| 18 | Operating voltage DC (EF008208) | 19.2 … 26.4 V (0.8 … 1.1 × 24 V) |
| 19 | Voltage type (operating voltage) (EF005294) | DC |
| 20 | Rated switch current (EF006706) | 10 A (conventional thermal current of each contact) |
| 21 | Connection type auxiliary circuit (EF006820) | screw connection |
| 22 | Width (EF000008) | 45 mm |
| 23 | Height (EF000040) | 82 mm |
| 24 | Depth (EF000049) | 75.5 mm (68.0 in front of the rail crown, 7.5 behind it) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design", source "ETIM 10.0 EC000196 class value" with the feature code, OPERATING.md 12); `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| base | 45.0 × 82.0 (z −41 … 41) × 40.0 deep: the terminal shoulders at y −40 | design choice |
| front housing | x 2 … 43, z −24 … 24, front face at y −68.0 | design choice |
| overall | 45.0 × 75.8 (y −68.3 … 7.5) × 82.0 | from the parts above; the LED lens stands 0.3 proud |
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| terminals | two rows of five on the shoulders: top A1 13 21 31 43, bottom A2 14 22 32 44; 8.4 pitch, centred; screw heads Ø4.4 × 1.2 at z ±35.0; wire entries 3.6 × 9.0 slots cut 0.5 into the end faces | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screw's thread and torque | NOT ON FILE (B): a fit with the wire element; the clamp's connecting capacity is set by IEC 60947-1 (terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| coil LED | Ø3.2 lens, 0.3 proud, at x 37.0, z −8.0 | design choice |
| carrier window | 12.0 × 10.0 opening (x 8 … 20, z −14 … −4), pocket 18.0 deep | design choice |
| carrier tab | 10.0 × 8.0 × 9.0, its face 1.0 behind the housing face; travels 3.5 toward the mounting plane (+y) when the coil pulls in | design choice |
| legend field | 33.0 × 17.0 (x 6 … 39, z 4 … 21), 0.1 proud | design choice |

Terminal marks follow the function-number convention of IEC 60947-1 (coil A1 / A2; contacts numbered by position, second digit 3-4 for N.O. and 1-2 for N.C.): 13-14 N.O., 21-22 N.C., 31-32 N.C., 43-44 N.O. The marks are labels on the legend field, a design choice; the standard itself is not on file.

## Named nodes
`carrier` (translate +y, 0 … 3.5: the contact carrier's front tab; 0 = coil off, contacts at rest; 3.5 = coil on, 13-14 and 43-44 closed, 21-22 and 31-32 open) · `led-coil` (emissive, yellow: coil energised) · ports `t-A1`, `t-A2`, `t-13`, `t-14`, `t-21`, `t-22`, `t-31`, `t-32`, `t-43`, `t-44` (kind port, unit screw, gender none: a screw clamp, PIN-002). The twin drives `carrier` and `led-coil` from the coil's state; pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-ZINC` terminal screws · `M-GASKET` wire entries and the carrier window · `M-YELLOW-PA` carrier tab · `M-LENS-YELLOW` coil LED · `M-WHITE-PA` legend field

## Decals (Blender)
On the legend field: "complexes.org generic", "relay-aux-2no2nc", "24 V DC", "2 NO + 2 NC", and the terminal diagram (A1-A2 coil, 13-14, 21-22, 31-32, 43-44). Terminal marks beside each screw. On the carrier tab: "I" (top) and "O" (bottom) so the window shows the state. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). Everything else that this element meets is on file (the rail clip), and every other size is a design choice; nothing is guessed and shown as sourced.
- Coil power: 2.4 W at 24 V DC (0.10 A, 240 Ω), the designer's figure for a generic 24 V DC auxiliary relay, bounded by the panel's 24 V budget (ELR-020); not a feature of the class, so written "design:" (OPERATING.md 6). It lives in behaviour.csv's load row A1-A2 (the solver's) and in ratings.csv (`coil_p` design, `load_i` derived from it: the 24 V budget's, ELR-020). Inrush, pick-up and drop-out times, contact life and the magnet system are not features of the class and are not stated or modelled.
- Not a safety-function device: it is a control-circuit relay, and no safety function rests on it here (lib/inventory.csv has no row marking it safety).

## Outputs (out/)
`relay-aux-2no2nc.lsp` · `.glb` (pivots on the carrier, LED and ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at 1.0 (lane round elec-r18) and at 1.1 (elec-r20).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000196), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07) |
| 1.1 | ratings.csv: the five class-value rows to status "generic design" and source "ETIM 10.0 EC000196 class value: <feature> (EFnnnnnn)", OPERATING.md 12's form (review cloud-elec 2026-11-07 r1, finding 1); no shape, node or figure change; gated on the PC (elec-r20, 2026-11-09) |
| 1.2 | elec-r32 (unattended, 2026-11-11): text only, geometry as 1.1. The coil's 2.4 W / 0.10 A, stated in behaviour.csv's load row since elec-r27, now also in ratings.csv (`coil_p` design, `load_i` derived) and in the Notes, which had denied it (review relay-aux-2no2nc-1.1 finding 1: one figure, one home) |
| 1.3 | elec-r33 (unattended, 2026-11-12): text only, geometry as 1.2. ratings.csv `coil_p`'s "design:" source names the rule the 2.4 W meets, the panel's 24 V budget (ELR-020), as behaviour.csv's load row does (review relay-aux-2no2nc-1.2 finding 1, elec-r32 finding 2) |
