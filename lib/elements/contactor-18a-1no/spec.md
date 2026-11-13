# contactor-18a-1no · v1.1 · power contactor 3-pole, AC-3 18 A, 24 V DC coil, 1 NO auxiliary (complexes.org generic)

**What** Power contactor for a motor branch: three main normally open poles rated AC-3 18 A at 400 V, a 24 V DC coil and one auxiliary normally open contact 13-14, screw terminals, on the 35 mm rail; the overload relay overload-9a-1no1nc mounts directly under it. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000066, built to the class values below; no maker's datasheet and no product is matched. Inventory row pinned 6 (request panel-6 1a: the hydraulic power unit's motor contactor k1 in pnl-press-hydraulic; 18 A a design figure above the branch's 11 A sizing figure, which is the panel's (pnl-press-hydraulic spec.md, row m1: the motor's nameplate full-load current is not on file there); the ELR checks read this rating against the motor placed in the panel).
**Class** device · **Baseline** our own design: generic Power contactor, AC switching (ETIM 10.0 EC000066). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the overload's interface is read from overload-9a-1no1nc 1.1 (below; its pin row depth and hook form are that element's own open figures, which this element follows by `library.load`); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `CT18` · parameter `operated` (false; true shows the carrier pulled in).

## Class values
ETIM 10.0 EC000066 "Power contactor, AC switching", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Rated control supply voltage AC 50 Hz (EF003978) | not stated (DC coil) |
| 2 | Rated control supply voltage AC 60 Hz (EF003979) | not stated (DC coil) |
| 3 | Rated control supply voltage DC (EF003980) | 24 V |
| 4 | Voltage type for actuating (EF008242) | DC |
| 5 | Number of normally closed contacts as main contact (EF001375) | 0 |
| 6 | Number of normally open contacts as main contact (EF001374) | 3 |
| 7 | Type of electrical connection of main circuit (EF006819) | screw connection |
| 8 | Operating voltage AC 50 Hz (EF008206) | up to 480 V, the main poles (as 9) |
| 9 | Operating voltage AC 60 Hz (EF008207) | up to 480 V, the main poles: the design's choice, the 480 V AC supply of the panel it is built for (pnl-press-hydraulic, k1); ratings.csv `ue_max`. The coil's voltages are items 1 to 3; the current at 480 V is not stated (item 11 rates 400 V) |
| 10 | Rated operation current Ie at AC-1, 400 V (EF001393) | not stated |
| 11 | Rated operation current Ie at AC-3, 400 V (EF001392) | 18 A |
| 12 | Rated operation power at AC-3, 400 V (EF001364) | not stated (the motor's power is the motor's; the ratings checks read the current) |
| 13 | Rated operation current Ie at AC-4, 400 V (EF008495) | not stated |
| 14 | Rated operation power at AC-4, 400 V (EF008496) | not stated |
| 15 | Rated operation power NEMA (EF011960) | not stated |
| 16 | Number of auxiliary contacts as normally open contact (EF001376) | 1 |
| 17 | Number of auxiliary contacts as normally closed contact (EF001377) | 0 |
| 18 | Suitable for distribution board (EF001126) | no (panel rail mounting) |
| 19 | Width (EF000008) | 45 mm |
| 20 | Height (EF000040) | 85 mm |
| 21 | Depth (EF000049) | 91.6 mm (84.1 in front of the rail crown, 7.5 behind it) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design", source "ETIM 10.0 EC000066 class value" with the feature code, OPERATING.md 12); `pins.csv` gives each terminal its role.

## What it meets: the overload relay (overload-9a-1no1nc 1.1)
The overload relay mounts under the contactor, its three pins in the contactor's lower main terminals, as on contactor-9a-1no1nc (request panel-6 1a: the HPU motor's overload stays overload-9a-1no1nc, range D125). Every figure of the joint is read from overload-9a-1no1nc 1.1 at build time (`library.load`), so it has one home:

| figure | value here | from overload-9a-1no1nc 1.1 |
|---|---|---|
| width | 45.0, so the stack is flush on both sides | `W` |
| main pole centres | x 5.3, 19.3, 33.3 (pitch 14.0), top and bottom rows alike | `PIN_X`, `PIN_PITCH` |
| clamp entry depth position | y −34.5 (the overload's back face on the mounting plane, y = +7.5 here) | `PIN_Y` (−42.0 from its back face) |
| the overload's place in this frame | x 0, y +7.5, z −42.5: its top face on this bottom face, no turn | its ORIGIN (back face on the mounting plane, x 0 at its left face, z 0 at its top) |
| its rear hooks | two slots at x 8.0 and 37.0, y +4.75, in the lower lugs | `build()`: hooks at x 8.0 and W − 8.0, y −2.75 from its back face, r 2.0, up to `HOOK_TOP` 9.7 |

The overload's pins (Ø2.5, 14.1 above its top) and their sleeves (Ø4.4, 3.3 above its top) sit inside the lower entries (4.8 × 4.8, 16.0 deep); the hooks (Ø4.0) inside slots 4.4 × 4.4, 11.0 deep. A mates.csv row (the core's file) is asked for in request elec-12; the figures are already shared, not copied.

## Dimensions
| item | value | source |
|---|---|---|
| base | 45.0 × 85.0 (z −42.5 … 42.5) × 42.0 deep: the terminal shoulders' front face at y −42 | design choice (width: the overload's, above) |
| front housing | x 2 … 43, z −30 … 30, front face at y −84.0 | design choice |
| overall | 45.0 × 91.6 (y −84.1 … 7.5) × 85.0 | from the parts above; the legend field stands 0.1 proud |
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| lower lugs | two, 10.0 × 7.5 × 12.0, behind the base at x 3 … 13 and 32 … 42, z −42.5 … −30.5, down to the mounting plane (y 7.5); each with a hook slot | design choice (the slots' places: the overload's hooks, above) |
| main terminals | 1 3 5 on the top shoulder, 2 4 6 on the bottom, at the pole centres; screw heads Ø4.4 × 1.2 at z ±36.0 on the shoulders' face; box-clamp entries 4.8 × 4.8 × 16.0 cut into the end faces at y −34.5 | design choice (positions: the overload's pin row, above) |
| coil and auxiliary terminals | A1 and 13 on the front housing's top face, A2 and 14 on its bottom face, at x 10.0 (A1 / A2) and 35.0 (13 / 14), 8.0 behind the front face; screw heads Ø4.4 × 1.2 | design choice |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screw's thread and torque | NOT ON FILE (B): a fit with the wire element; the clamp's connecting capacity is set by IEC 60947-1 (terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| carrier window | 12.0 × 10.0 opening (x 16.5 … 28.5, z −18 … −8), pocket 18.0 deep | design choice |
| carrier tab | 10.0 × 8.0 × 9.0, its face 1.0 behind the housing face; travels 4.0 toward the mounting plane (+y) when the coil pulls in | design choice |
| legend field | 33.0 × 22.0 (x 6 … 39, z 2 … 24), 0.1 proud | design choice |

Terminal marks follow the convention of IEC 60947-4-1 / IEC 60947-1 as labels (main poles 1-2, 3-4, 5-6; coil A1 / A2; the auxiliary's function number 13-14 N.O.). The marks are a design choice printed on the legend field; the standards themselves are not on file.

## Named nodes
`carrier` (translate +y, 0 … 4.0: the contact carrier's front tab; 0 = coil off, contacts open; 4.0 = coil on, the three main poles and 13-14 closed) · ports `t-1` … `t-6`, `t-A1`, `t-A2`, `t-13`, `t-14` (kind port, unit screw, gender none: a screw clamp, PIN-002). The twin drives `carrier` from the coil's state; pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing, lugs and rail clip · `M-ZINC` terminal screws · `M-GASKET` clamp entries, hook slots and the carrier window · `M-YELLOW-PA` carrier tab · `M-WHITE-PA` legend field

## Decals (Blender)
On the legend field: "complexes.org generic", "contactor-18a-1no", "AC-3 18 A 400 V", "coil 24 V DC", and the terminal diagram (A1-A2 coil, 1-2, 3-4, 5-6, 13-14). Terminal marks beside each screw. On the carrier tab: "I" (top) and "O" (bottom) so the window shows the state. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). The rail clip is on file (toolkit/din.py). The overload joint follows overload-9a-1no1nc 1.1: its pin row depth and its hooks' form are that element's own open figures (overload-9a-1no1nc spec.md, Dimensions, lines 16 and 19; it stands at station 2), not sourced there yet. This element is designed to them and reads them by `library.load`, so when the overload's figures are sourced in a new version of it, this element is re-pinned with that version. Every other size is a design choice; nothing is guessed and shown as sourced.
- Coil power: 4.8 W at 24 V DC (0.20 A, 120 Ω), the designer's figure for a generic 24 V DC coil of this size, bounded by the panel's 24 V budget (ELR-020); not a feature of the class, so written "design:" (OPERATING.md 6). It lives in behaviour.csv's load row A1-A2 (the solver's) and in ratings.csv (`coil_p` design, `load_i` derived). The coil's pick-up and drop-out levels are IEC 60947-4-1's operating limits, not on file: NOT ON FILE (B): IEC 60947-4-1, so the twin reads any coil voltage as operated (behaviour.csv). Inrush, operating times, contact life, the auxiliary's rating and the magnet system are not features of the class and are not stated or modelled.
- Not a safety-function device: it switches a motor branch, and no safety function rests on it here (lib/inventory.csv has no row marking it safety).

## Outputs (out/)
`contactor-18a-1no.lsp` · `.glb` (pivots on the carrier and the ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at each version (1.0 in elec-r35, 1.1 in elec-r46).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000066), our own design (elec-r35, unattended, 2026-11-12): the inventory row of request panel-6 1a; lower terminals at overload-9a-1no1nc 1.1's pin row, read from that element |
| 1.1 | text only, the geometry is 1.0's (elec-r46, unattended, 2026-11-13; review elec-r35 findings 1 to 3): Class values 8 and 9 give the main poles' operating voltage, up to 480 V (a design choice, the panel's supply), and ratings.csv gains `ue_max`; the What line calls 11 A the branch's sizing figure, the panel's; the Notes and the Baseline say the overload joint follows that element's own open figures |
