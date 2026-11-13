# xfmr-control-3ph · v1.2 · three-phase control transformer 1000 VA, 480 V delta / 208Y-120 V (complexes.org generic)

**What** Three-phase control transformer for a machine's control panel: 1000 VA, primary 480 V in delta, secondary 208 V in star with the neutral brought out (120 V line to neutral for control circuits), open construction (core and coils), screwed to the back panel by two brackets, screw terminals: primary on top, secondary and PE below. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002485, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Three-phase control transformer (ETIM 10.0 EC002485). The class values are this element's definition (design inputs); the panel-screw holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); every other size, the hole pattern included, is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: surface-mount device: back face (the brackets' flanges, on the panel) y = 0, the lower-left mounting hole x = 0, z = 0, body toward −y.
**Built with** toolkit 1.3 · AutoLISP command `XFMR3` · no parameters.

## Class values
ETIM 10.0 EC002485 "Three-phase control transformer", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Built as safety transformer (EF007235) | no |
| 2 | Built as isolating transformer (EF007238) | no (separate windings; not built to the isolating-transformer construction) |
| 3 | Built as energy saving transformer (EF007005) | no |
| 4 | Primary voltage 1 (EF006125) | 480 V (line to line, delta) |
| 5 | Primary voltage 2 (EF006126) | not stated (no tap) |
| 6 | Primary voltage 3 (EF006127) | not stated |
| 7 | Primary voltage 4 (EF007410) | not stated |
| 8 | Primary voltage 5 (EF007411) | not stated |
| 9 | Primary voltage 6 (EF007412) | not stated |
| 10 | Primary voltage 7 (EF007413) | not stated |
| 11 | Primary voltage 8 (EF007414) | not stated |
| 12 | Primary voltage 9 (EF007415) | not stated |
| 13 | Primary voltage 10 (EF007409) | not stated |
| 14 | Secondary voltage 1 (EF007472) | 208 V (line to line) |
| 15 | Secondary voltage 2 (EF007474) | 120 V (line to neutral) |
| 16 | Secondary voltage 3 (EF007475) | not stated |
| 17 | Secondary voltage 4 (EF007476) | not stated |
| 18 | Secondary voltage 5 (EF007477) | not stated |
| 19 | Secondary voltage 6 (EF007478) | not stated |
| 20 | Secondary voltage 7 (EF007479) | not stated |
| 21 | Secondary voltage 8 (EF007480) | not stated |
| 22 | Secondary voltage 9 (EF007481) | not stated |
| 23 | Secondary voltage 10 (EF007473) | not stated |
| 24 | Wiring system (EF002960) | Dyn11 (delta primary, star secondary, neutral brought out) |
| 25 | Rated power (EF007051) | 1000 VA |
| 26 | Type of insulation material according to IEC 85 (EF007299) | B (130 °C) |
| 27 | Short-circuit-proof (EF007332) | no (the secondary is protected by fuses or a breaker sized to its rated current) |
| 28 | Relative short circuit voltage (EF007452) | 4 % |
| 29 | Conductor material (EF001622) | copper |
| 30 | Width (EF000008) | 194 mm |
| 31 | Height (EF000040) | 212 mm |
| 32 | Depth (EF000049) | 98.2 mm |
| 33 | Degree of protection (IP) (EF005474) | IP00 (open core and coils) |
| 34 | Degree of protection (NEMA) (EF011959) | not stated (open, panel-mounted) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. Rated currents follow from them (ratings.csv, derived): primary 1000 / (√3 × 480) = 1.20 A, secondary 1000 / (√3 × 208) = 2.78 A per line. The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC002485 class value" with the feature code (OPERATING.md 12). `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| core | three limbs 36 wide and two yokes 36 high, windows 30 × 90: 168 × 162 in the x-z plane (x 2 … 170, z 15 … 177), stacked 55 deep (y −76 … −21), 21 clear of the panel | design choice (limb section 36 × 55 = 19.8 cm² for 333 VA a phase) |
| coils | a rectangular tube on each limb: 1.0 gap to the limb, 12.0 build, 86 high (2.0 clear of each yoke): 62 × 81 outside, 4.0 apart; y −89 … −8 | design choice |
| clamp bars | steel flats 164 × 32 × 3.0 on the front and back of each yoke | design choice |
| brackets | 2.5 sheet: a web on each yoke's end face (y −74 … −2.5) and a flange 188 × 25 on the panel (x −8 … 180) | design choice |
| panel holes | four Ø5.5 through the flanges, at x 0 / 172.0 and z 0 / 192.0; position Ø0.4 to datum A (the flanges' back face): floating fastener, 0.4 ≤ H − F = 0.5 (GDT-010) | Ø5.5: ISO 273 medium for M5 (lib/standards/holes.csv); the pattern and the position tolerance: design choice (features.csv) |
| terminal blocks | 18 deep on the front clamp bars (front face y −97.0): primary 56 × 32 on top (x 58 … 114, z 143 … 175), secondary 72 × 32 below (x 38 … 110, z 17 … 49), PE block 24 × 32 beside it (x 110 … 134), green-yellow | design choice |
| terminals | 16.0 pitch: 1U 1V 1W on the primary block (screws at z 168, wire entries in its top face), 2U 2V 2W 2N and PE below (screws at z 24, wire entries in the bottom faces); screw heads Ø5.6 × 1.2; entries 5.0 × 10.0 slots cut 0.5 deep | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screws' thread and torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by the terminal standard (IEC 60947-7-1 for terminal blocks), which is not on file (lib/standards/sources.csv), so no size is claimed |
| rating plate | 36 × 38 on the middle coil's front, 0.1 proud | design choice |
| overall | 194 × 98.2 × 212 (x −11 … 183, y −98.2 … 0, z −10 … 202) | from the parts above |

Terminal marks follow the IEC convention for transformer terminals (1U 1V 1W primary; 2U 2V 2W secondary, 2N its neutral; PE). The marks are labels, a design choice; the standard itself is not on file.

## Named nodes
Ports only: `t-1U`, `t-1V`, `t-1W` (primary), `t-2U`, `t-2V`, `t-2W`, `t-2N` (secondary), `t-PE` (kind port, unit screw, gender none: a screw clamp, PIN-002). Nothing moves or lights; the twin reads the secondary's voltages from the class values and the primary's.

## Materials by layer
`M-STEEL-7035` core laminations · `M-CU` coils · `M-GALV` clamp bars and brackets · `M-GREY-PA` terminal blocks · `M-GREEN-YELLOW` PE block · `M-ZINC` terminal screws · `M-GASKET` wire entries and the panel holes · `M-WHITE-PA` rating plate

## Decals (Blender)
On the rating plate: "complexes.org generic", "xfmr-control-3ph", "3~ 1000 VA", "PRI 480 V Δ", "SEC 208Y/120 V", "Dyn11", "uk 4 %", "insulation class B", the connection diagram. Terminal marks beside each screw; the earth symbol on the PE block. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). The panel holes are on file (ISO 273); every other size is a design choice; nothing is guessed and shown as sourced.
- Mass, no-load and load losses, inrush current and efficiency are not features of the class and are not stated in 1.0. The secondary's protection (Class values 27: not short-circuit-proof) is the panel's to provide; a panel that places this element sizes it from the derived 2.78 A (NEC 450.3(B), transformers of 1000 V or less, is the rule a panel round cites when it does).
- The PE terminal bonds the core frame (clamp bars and brackets) to the panel's protective conductor; the bond itself is not modelled.

## Outputs (out/)
`xfmr-control-3ph.lsp` · `.glb` (pivots on the ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at 1.0 (lane round elec-r18), at 1.1 (elec-r20) and at 1.2 (elec-r35).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002485), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07) |
| 1.1 | ratings.csv: the six class-value rows to status "generic design" and source "ETIM 10.0 EC002485 class value: <feature> (EFnnnnnn)", OPERATING.md 12's form (review cloud-elec 2026-11-07 r1, finding 1); the two "derived" rows unchanged; no shape, node or figure change; gated on the PC (elec-r20, 2026-11-09) |
| 1.2 | elec-r35 (2026-11-12, unattended): text only, geometry as 1.1. pins.csv t-PE's source named IEC 60204-1 with no clause; the standard is not in lib/standards/sources.csv, so it now says the rule's standard is not on file (NFPA 79's bonding clause is view-only, for an attended reading) (review elec-r27 finding 1, xfmr-control-3ph-1.1 finding 1) |
