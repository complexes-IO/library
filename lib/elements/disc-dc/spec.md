# disc-dc · v1.0 · DC switch disconnector, 2 poles, 25 A, 220 V DC, rotary handle (complexes.org generic)

**What** DC switch disconnector for a machine's control panel: isolates one DC circuit (L+ through pole 1, M through pole 2) under load, such as a 24 V DC supply's output to its loads or a DC bus up to 220 V. 25 A, a rotary handle 0 / I on the front (90°, clockwise to I), screw terminals, on the 35 mm rail. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC004963, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Switch disconnector (DC) (ETIM 10.0 EC004963). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `DISCDC` · parameter `on` (false: handle at 0, poles open; true: handle at I, poles closed).

## Class values
ETIM 10.0 EC004963 "Switch disconnector (DC)", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Version as main switch (EF006981) | no |
| 2 | Version as maintenance-/service switch (EF006986) | no |
| 3 | Version as safety switch (EF006985) | no |
| 4 | Version as emergency stop installation (EF006959) | no |
| 5 | Version as reversing switch (EF009408) | no |
| 6 | Number of switches (EF005586) | 1 |
| 7 | Rated voltage DC (EF007067) | up to 220 V (one DC circuit: L+ through pole 1, M through pole 2) |
| 8 | Rated current (EF000227) | 25 A (each pole) |
| 9 | Number of poles (EF001391) | 2 |
| 10 | Number of auxiliary contacts as normally closed contact (EF001377) | 0 |
| 11 | Number of auxiliary contacts as normally open contact (EF001376) | 0 |
| 12 | Number of auxiliary contacts as change-over contact (EF003531) | 0 |
| 13 | Device construction (EF008240) | built-in device for the 35 mm rail, front-operated |
| 14 | Suitable for floor mounting (EF025108) | no |
| 15 | Suitable for front mounting 4-hole (EF007247) | no |
| 16 | Voltage release optional (EF007491) | no |
| 17 | Suitable for front mounting centre (EF007248) | no |
| 18 | Suitable for distribution board installation (EF007262) | not stated (the distribution-board front profile, DIN 43880, is not on file, so no fit to a board's cover is claimed) |
| 19 | Suitable for intermediate mounting (EF007264) | no |
| 20 | Colour control element (EF007167) | black |
| 21 | Type of control element (EF006976) | rotary handle (grip on a base disc), 0 / I, 90° |
| 22 | Interlockable (EF006281) | no |
| 23 | Housing colour (EF000136) | grey |
| 24 | Type of electrical connection of main circuit (EF006819) | screw connection |
| 25 | With pre-assembled cabling (EF016444) | no |
| 26 | Degree of protection (IP), front side (EF003118) | IP20 |
| 27 | Width (EF000008) | 36 mm |
| 28 | Height (EF000040) | 90 mm |
| 29 | Depth (EF000049) | 82.7 mm (75.2 in front of the rail crown, 7.5 behind it) |
| 30 | Width in number of modular spacings (EF002950) | not stated (the modular spacing of DIN 43880 is not on file; the width is 36 mm) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design"; `ith` is what ELR-014 reads for an isolation device); `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| base | 36.0 × 42.0 × 90.0 (y −42 … 0, z −45 … 45): the terminal shoulders at y −42 | design choice |
| raised front | 34.0 × 20.0 × 44.0 (x 1 … 35, y −62 … −42, z −22 … 22) | design choice |
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| terminals | line 1 and 3 on top, load 2 and 4 below, 18.0 pitch (x 9, 27), screws at z ±38.0; screw heads Ø5.6 × 1.2; wire entries 5.5 × 10.0 slots cut 0.5 into the end faces | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screws' thread and torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by IEC 60947-1 (terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| handle | base disc Ø30.0 × 3.0 (y −65 … −62) centred on the raised front (x 18, z 0); grip 32.0 × 8.0 × 10.0 (y −75 … −65), across (along x) at 0; white pointer 6.0 × 2.0, 0.2 proud, 1.0 in from the grip's left end at 0; turns 90° clockwise (seen from the front) to I, the pointer then up | design choice |
| legend label | 30.0 × 9.0 (x 3 … 33, z −33 … −24) on the lower shoulder, 0.1 proud | design choice |
| overall | 36.0 × 82.7 (y −75.2 … 7.5) × 90.0 | from the parts above |

Terminal marks: odd numbers on the line side, even on the load side, one pair per pole (1-2 L+, 3-4 M), the function-number convention of IEC 60947-1 for main circuits. The marks are labels, a design choice; the standard itself is not on file.

## Named nodes
`handle` (rotate about +y through (18, −62, 0), 0 … 90°: 0 = OFF, both poles open; 90 = I, both closed; built at 0, or at 90 with `on`) · ports `t-1`, `t-2`, `t-3`, `t-4` (kind port, unit screw, gender none: a screw clamp, PIN-002). The twin reads the handle's angle as the poles' state: closed at 90, open below it; pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-BLACK-PA` handle · `M-WHITE-PA` handle pointer and legend label · `M-ZINC` terminal screws · `M-GASKET` wire entries

## Decals (Blender)
On the raised front: "0" left of the handle and "I" above it (where the pointer points in each position). On the legend label: "complexes.org generic", "disc-dc", "DC 220 V 25 A", "2P", the symbol of a two-pole switch disconnector with the marks 1-2 and 3-4, "+" beside 1 and "−" beside 3. Terminal marks beside each screw. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). Everything else this element meets is on file (the rail clip), and every other size is a design choice; nothing is guessed and shown as sourced.
- Polarity: the poles are marked for L+ (1-2) and M (3-4), supply on top; whether a reversed connection changes the DC switching capacity is not stated in 1.0. The DC utilisation category, the short-time withstand current, the contact gap and the operating torque are not features of the class and are not stated or modelled in 1.0.
- Not a safety-function device, a main switch or a maintenance switch (Class values 1 to 4: no): it cannot be padlocked at 0, so it is not the means of isolation for maintenance work; a panel that needs one places a lockable disconnect.

## Outputs (out/)
`disc-dc.lsp` · `.glb` (pivots on the handle and ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004963), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07) |
