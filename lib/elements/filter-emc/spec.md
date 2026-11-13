# filter-emc · v1.0 · EMC line filter, three-phase 480 V AC 16 A (complexes.org generic)

**What** Three-phase EMC line filter (radio interference suppression filter) for a machine's control panel: wired between the supply and a drive or a thyristor power controller, it keeps their conducted interference off the supply. 480 V AC, 16 A, 50 / 60 Hz, three lines with no neutral, a closed steel housing on a base plate screwed to the back panel by four M5 screws, screw terminals: LINE (from the supply) on top, LOAD (to the drive) below, each row with its PE terminal. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002564, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Filter for low-voltage (ETIM 10.0 EC002564). The class values are this element's definition (design inputs); the panel-screw holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); every other size, the hole pattern included, is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: surface-mount device: back face (the base plate) y = 0, the lower-left mounting hole x = 0, z = 0, body toward −y.
**Built with** toolkit 1.3 · AutoLISP command `EMCFLT` · no parameters.

## Class values
ETIM 10.0 EC002564 "Filter for low-voltage", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Suitable as sinus filter (EF007236) | no |
| 2 | Suitable as du/dt-filter (EF007229) | no |
| 3 | Suitable as radio interference suppression filter (EF007231) | yes (a line filter on the supply side of a drive or power controller) |
| 4 | Suitable as audio frequency blockage (EF007237) | no |
| 5 | Number of poles, primary side (EF007403) | 3 (L1, L2, L3; no neutral) |
| 6 | Rated clock frequency (EF007502) | not stated (not a sine or du/dt filter: no switching frequency is designed to) |
| 7 | Rated operating frequency (EF007024) | 50 … 60 Hz |
| 8 | Max. rated operation voltage Ue (EF007357) | 480 V (AC, line to line) |
| 9 | Rated current AC (EF007500) | 16 A (each line) |
| 10 | Max. rated current (Ith) at rated voltage DC (EF007359) | not stated (an AC filter) |
| 11 | Degree of protection (IP) (EF005474) | IP20 (the terminals) |
| 12 | Degree of protection (NEMA) (EF011959) | not stated (panel-mounted, inside the enclosure) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design"); `pins.csv` gives each terminal its role. The class has no Width / Height / Depth features; the sizes below are design choices.

## Dimensions
| item | value | source |
|---|---|---|
| base plate | 2.0 steel sheet, 60.0 × 230.0 (x −10 … 50, z −10 … 220), on the panel (y −2 … 0); an end tab of 35.0 above and below the housing | design choice |
| panel holes | four Ø5.5 through the plate's end tabs, at x 0 / 40.0 and z 0 / 210.0; position Ø0.4 to datum A (the plate's back face): floating fastener, 0.4 ≤ H − F = 0.5 (GDT-010); edge distance 7.25 ≥ 1.5 t = 3.0 (DFM-010) | Ø5.5: ISO 273 medium for M5 (lib/standards/holes.csv); the pattern and the position tolerance: design choice (features.csv) |
| housing | closed steel box 60.0 × 50.0 × 160.0 (x −10 … 50, y −52 … −2, z 25 … 185) on the plate | design choice |
| terminal blocks | 18.0 deep on the housing front (front face y −70.0), 24.0 high: LINE on top (z 157 … 181), LOAD below (z 29 … 53); each a grey block 41.0 wide (x −9 … 32) with three terminals and a green-yellow PE block 17.0 wide beside it (x 32 … 49) | design choice |
| terminals | 12.0 pitch, screws 6.0 in from the block's end face (z 175 on top, z 35 below), wire entries in the top face of the LINE blocks and the bottom face of the LOAD blocks; screw heads Ø5.0 × 1.2; entries 4.5 × 9.0 slots cut 0.5 deep | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screws' thread and torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by the terminal standard (IEC 60947-7-1 for terminal blocks), which is not on file (lib/standards/sources.csv), so no size is claimed |
| rating plate | 48.0 × 74.0 on the housing front (x −4 … 44, z 68 … 142), 0.1 proud | design choice |
| overall | 60.0 × 71.2 × 230.0 (x −10 … 50, y −71.2 … 0, z −10 … 220) | from the parts above |

## Named nodes
Ports only: `t-L1`, `t-L2`, `t-L3`, `t-PE` (LINE side, from the supply) and `t-L1-load`, `t-L2-load`, `t-L3-load`, `t-PE-load` (LOAD side, to the drive or controller) (kind port, unit screw, gender none: a screw clamp, PIN-002). Nothing moves or lights. The twin reads the filter as a pass-through on each line; pins.csv names what each terminal carries.

## Materials by layer
`M-GALV` base plate and housing (zinc-plated steel) · `M-GREY-PA` terminal blocks · `M-GREEN-YELLOW` PE blocks · `M-ZINC` terminal screws · `M-GASKET` wire entries and the panel holes · `M-WHITE-PA` rating plate

## Decals (Blender)
On the rating plate: "complexes.org generic", "filter-emc", "3~ 480 V AC 50/60 Hz", "16 A", "LINE" with an arrow up, "LOAD" with an arrow down, and the circuit symbol of a three-line filter. Beside the blocks: "LINE L1 L2 L3" on top and "LOAD L1' L2' L3'" below; the earth symbol on each PE block. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). The panel holes are on file (ISO 273); every other size is a design choice; nothing is guessed and shown as sourced.
- Attenuation, leakage current, the discharge resistors, power loss and mass are not features of the class and are not stated or modelled in 1.0. A panel that places this element connects its PE terminals to the PE bar before the lines: the filter's capacitors to earth carry a leakage current, whose figure (not stated in 1.0) and the bonding it calls for are the panel round's to state from the standard it cites.
- The LINE / LOAD direction matters: the twin's wiring must bring the supply to the top row. pins.csv gives the side of each terminal.
- Not a safety-function device.

## Outputs (out/)
`filter-emc.lsp` · `.glb` (pivots on the ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002564), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07) |
