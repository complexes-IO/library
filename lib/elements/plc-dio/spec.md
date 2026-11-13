# plc-dio · v1.0 · PLC digital I/O module, 8 DI + 8 DO, 24 V DC, transistor outputs 0.5 A (complexes.org generic)

**What** Digital I/O module for a machine's PLC: eight 24 V DC digital inputs and eight transistor outputs, each sourcing 0.5 A from its own output supply, fed 24 V DC, on the 35 mm rail. A stepped moulded housing on the rail clip (the body of plc-aio 1.0, 60 wide), two pluggable terminal blocks on its front (x1 the module supply, its functional earth and the inputs; x2 the output supply and the outputs), a row of input LEDs, a row of output LEDs, two status LEDs and a legend field. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001419, built to the class values below; no maker's datasheet and no product is matched (the vendor file in references/ was not opened).
**Class** device · **Baseline** our own design: generic PLC digital I/O-module (ETIM 10.0 EC001419). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the terminals are placed terminal-plug 2.0 elements (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `PLCDIO` · no parameters · places terminal-plug 2.0 twice (tags `x1` 11 poles, `x2` 10 poles).

## Class values
ETIM 10.0 EC001419 "PLC digital I/O-module", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Supply voltage AC 50 Hz (EF007532) | none (a DC module) |
| 2 | Supply voltage AC 60 Hz (EF007533) | none (a DC module) |
| 3 | Supply voltage DC (EF007534) | 24 … 24 V (24 V DC nominal) |
| 4 | Voltage type (supply voltage) (EF002991) | DC |
| 5 | Number of digital inputs (EF001992) | 8 (DI0 … DI7) |
| 6 | Number of digital outputs (EF001993) | 8 (DO0 … DO7) |
| 7 | Digital inputs configurable (EF008516) | no |
| 8 | Digital outputs configurable (EF008520) | no |
| 9 | Power consumption (EF000346) | 2.0 W (from the module supply 24V-0V; the outputs' load current is drawn from the output supply 24VO-0VO) |
| 10 | Input current at signal 1 (EF001428) | 3 mA (at 24 V) |
| 11 | Permitted voltage at input (EF007554) | 0 … 30 V |
| 12 | Type of voltage (input voltage) (EF003033) | DC |
| 13 | Type of digital output (EF003601) | transistor (sourcing: the output switches 24VO to the load, the load returns to 0VO) |
| 14 | Output current (EF003202) | 0.5 A (each output) |
| 15 | Permitted voltage at output (EF007553) | 24 … 24 V (the output supply's 24 V DC) |
| 16 | Type of output voltage (EF008222) | DC |
| 17 | Short-circuit protection, outputs available (EF003203) | not stated |
| 18 | Redundancy (EF003156) | no |
| 19 | Type of electric connection (EF003961) | screw connection on pluggable terminal blocks (terminal-plug 2.0, two placed) |
| 20 | Time delay at signal change (EF002382) | not stated |
| 21 | Suitable for safety functions (EF001597) | no |
| 22 | SIL according to IEC 61508 (EF009889) | none (not a safety device) |
| 23 | Performance level according to EN ISO 13849-1 (EF007399) | none (not a safety device) |
| 24 | Appendant operation agent (Ex ia) (EF004141) | no |
| 25 | Appendant operation agent (Ex ib) (EF004142) | no |
| 26 | Explosion safety category for gas (EF003997) | none |
| 27 | Explosion safety category for dust (EF003998) | none |
| 28 | Width (EF000008) | 60 mm |
| 29 | Height (EF000040) | 100 mm |
| 30 | Depth (EF000049) | 93.5 mm (86.0 in front of the rail crown, 7.5 behind it) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. The 24 V DC supply is the panel's control supply (psu-24v-2a4), within the panel's 24 V budget (ELR-020). IEC 61131-2, which tabulates the supply range and the input types' switching levels for programmable controllers, is not in lib/standards/sources.csv, so no conformance to it is claimed and no threshold is modelled from it (behaviour.csv: any voltage reads as present / signal 1, the thresholds "NOT ON FILE (B): IEC 61131-2" in the rows' sources). The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC001419 class value" with the feature code (OPERATING.md 12); `load_i` reads "derived". `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 60.0 × 40.0 × 100.0 (y −40 … 0, z −50 … 50) on the clip | design choice (plc-aio 1.0's base, 60 wide for the 11-pole plug) |
| front block | 60.0 × 30.0 × 88.0 (y −70 … −40, z −44 … 44) on the base; 6.0 of the base shows above and below | design choice (as plc-aio 1.0) |
| supply and input plug | terminal-plug 2.0, 11 poles, tag `x1`, mating face on the front block's face (y −70; body y −86 … −70), x 2.5 … 57.5, sockets' axis z 28 (body z 22 … 37.5), poles along +x, wire entries down: 24V 0V FE DI0 DI1 DI2 DI3 DI4 DI5 DI6 DI7 | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| output plug | terminal-plug 2.0, 10 poles, tag `x2`, mating face on the front block's face, x 5 … 55, sockets' axis z −36 (body z −42 … −26.5): 24VO 0VO DO0 DO1 DO2 DO3 DO4 DO5 DO6 DO7 | as x1 |
| headers | the pins the plugs' sockets take, standing out of the front block into the sockets | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures (as plc-aio 1.0) |
| link to the controller | how the module reaches its CPU (a backplane, a side bus connector or a fieldbus) | not stated in 1.0 and not modelled: the class has no feature for it; a version for a named controller adds it (needs-em r33 item 1, plc-aio's question, covers both) |
| channel LEDs | Ø3.2 lenses, 0.3 proud, yellow, eight in a row at 5.0 pitch, x 17.5 … 52.5: inputs at z 14 (led-di0 … led-di7, above the inputs' poles), outputs at z −18 (led-do0 … led-do7) | design choice (toolkit/din.py `led`; the led element is not built yet) |
| status LEDs | Ø3.2 lenses, 0.3 proud, at z −2: run (green) x 6; error (red) x 12 | design choice (as plc-aio 1.0) |
| legend field | 38.0 × 16.0 (x 17 … 55, z −10 … 6), 0.1 proud | design choice |
| overall | 60.0 × 93.5 (y −86.0 … 7.5) × 100.0 | from the parts above; the plugs stand 16.0 proud of the front block |

Terminal marks: 24V / 0V the module supply (0V the inputs' reference), FE the functional earth, DI<n> the inputs, 24VO / 0VO the output supply, DO<n> the outputs. The marks are labels, a design choice; the plugs' own pole marks are 1 … n (terminal-plug 2.0 Decals) with these printed on the legend field.

## Named nodes
`led-di0` … `led-di7` (emissive, yellow: the input is at signal 1) · `led-do0` … `led-do7` (emissive, yellow: the output is commanded on) · `led-run` (emissive, green: the module is powered and running) · `led-err` (emissive, red: a module fault) · the plugs' nodes `x1.t-1` … `x1.t-11`, `x2.t-1` … `x2.t-10` (clamp screws, gender none) and `x1.s-1` … `x1.s-11`, `x2.s-1` … `x2.s-10` (sockets, gender female), as terminal-plug 2.0 names them under its tag. Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-LENS-YELLOW`, `M-LENS-GREEN`, `M-LENS-RED` LEDs · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plugs (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "plc-dio", "8 DI / 8 DO", "24 V DC", "DO 0.5 A", and the terminal diagram (24V 0V FE DI0 … DI7; 24VO 0VO DO0 … DO7). Beside the LEDs: the channel numbers 0 … 7 over each row, "RUN", "ERR". No maker's name, logo or approval mark.

## Notes and open figures
- Nothing of the element's own is open in 1.0: everything it meets is on file (the rail clip, terminal-plug 2.0) and every other size and value is a design choice or a class value; nothing is guessed and shown as sourced. The placed plugs carry their own open line (their clamps' torque, terminal-plug 2.0's behaviour.csv), which behaviour.csv repeats for each pin as that element writes it; the supply and input thresholds are IEC 61131-2's tables, a document wanted (class B), named in behaviour.csv's sources.
- Not placed in 1.0, though lib/inventory.csv's made_of names them: terminal-plug ×2 are placed; din-clip-35 and led ×16 are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). 1.0 holds to the rail by the toolkit's rail clip, and its LEDs are the toolkit's lenses.
- Not stated or modelled in 1.0: the outputs' short-circuit protection (class value 17), the input filter delay (20), the inputs' impedance, the outputs' voltage drop and leakage, the isolation between the input, output and bus sides, the bus to the controller and the mass. behaviour.csv's outputs give the output supply's nominal 24 V.
- The output supply 24VO-0VO carries up to 8 × 0.5 = 4.0 A (pins.csv); its branch protection and the module supply's are the panel's to provide.
- Not a safety-function device (Class values 21 to 23).

## Outputs (out/)
`plc-dio.lsp` · `.glb` (pivots on the LEDs and the plugs' ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock in elec-r34 (lib/rounds/elec/r34.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r34 (2026-11-12, unattended): first build, generic (ETIM 10.0 EC001419), our own design; inventory elec pinned 6 (5 systems); plc-aio 1.0's body, 60 wide; places terminal-plug 2.0 twice (x1 11 poles, x2 10 poles) |
