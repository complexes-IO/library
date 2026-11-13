# plc-aio · v1.1 · PLC analogue I/O module, 4 AI + 2 AO, 0-10 V / 4-20 mA, 24 V DC (complexes.org generic)

**What** Analogue I/O module for a machine's PLC: four differential analogue inputs and two analogue outputs, each channel set by the program's configuration to 0 … 10 V or 4 … 20 mA, 12-bit resolution, fed 24 V DC, on the 35 mm rail. A stepped moulded housing on the rail clip, two pluggable terminal blocks on its front (x1 the inputs, x2 the supply, its functional earth and the outputs), two status LEDs and a legend field. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001420, built to the class values below; no maker's datasheet and no product is matched (the vendor file in references/ was not opened).
**Class** device · **Baseline** our own design: generic PLC analogue I/O-module (ETIM 10.0 EC001420). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the terminals are placed terminal-plug 2.0 elements (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `PLCAIO` · no parameters · places terminal-plug 2.0 twice (tags `x1` 8 poles, `x2` 7 poles).

## Class values
ETIM 10.0 EC001420 "PLC analogue I/O-module", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Number of analogue inputs (EF001994) | 4 (differential, AI0 … AI3) |
| 2 | Number of analogue outputs (EF001995) | 2 (AO0, AO1) |
| 3 | Analogue inputs configurable (EF008518) | yes (each input voltage or current, by the program's configuration) |
| 4 | Analogue outputs configurable (EF008519) | yes (each output voltage or current, by the program's configuration) |
| 5 | Input, current (EF003204) | yes: 4 … 20 mA |
| 6 | Input, voltage (EF003205) | yes: 0 … 10 V |
| 7 | Input, resistor (EF003206) | no |
| 8 | Input, resistance thermometer (EF003207) | no |
| 9 | Input, thermocouple (EF003208) | no |
| 10 | Input signal, configurable (EF003209) | yes (items 5 and 6, per channel) |
| 11 | Resolution of the analogue inputs (EF003575) | 12 bit |
| 12 | Output, current (EF003212) | yes: 4 … 20 mA |
| 13 | Output, voltage (EF003213) | yes: 0 … 10 V |
| 14 | Output signal configurable (EF003214) | yes (items 12 and 13, per channel) |
| 15 | Resolution of the analogue outputs (EF003577) | 12 bit |
| 16 | Type of electric connection (EF003961) | screw connection on pluggable terminal blocks (terminal-plug 2.0, two placed) |
| 17 | Suitable for safety functions (EF001597) | no |
| 18 | SIL according to IEC 61508 (EF009889) | none (not a safety device) |
| 19 | Performance level according to EN ISO 13849-1 (EF007399) | none (not a safety device) |
| 20 | Appendant operation agent (Ex ia) (EF004141) | no |
| 21 | Appendant operation agent (Ex ib) (EF004142) | no |
| 22 | Explosion safety category for gas (EF003997) | none |
| 23 | Explosion safety category for dust (EF003998) | none |
| 24 | Width (EF000008) | 45 mm |
| 25 | Power consumption (EF000346) | 2.0 W (from the 24 V DC supply, outputs at full scale included) |
| 26 | Height (EF000040) | 100 mm |
| 27 | Depth (EF000049) | 93.5 mm (86.0 in front of the rail crown, 7.5 behind it) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. The signal ranges 0 … 10 V and 4 … 20 mA are this element's design inputs (the ranges a machine's analogue sensors and actuators use); IEC 61131-2, which names analogue I/O ranges for programmable controllers, is not in lib/standards/sources.csv, so no conformance to it is claimed. The module's supply, 24 V DC, is not a class feature: a design choice, the panel's control supply (psu-24v-2a4), within the panel's 24 V budget (ELR-020). The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC001420 class value" with the feature code (OPERATING.md 12); the supply rows "design" and "derived". `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 45.0 × 40.0 × 100.0 (y −40 … 0, z −50 … 50) on the clip | design choice |
| front block | 45.0 × 30.0 × 88.0 (y −70 … −40, z −44 … 44) on the base; 6.0 of the base shows above and below | design choice |
| input plug | terminal-plug 2.0, 8 poles, tag `x1`, mating face on the front block's face (y −70; body y −86 … −70), x 2.5 … 42.5, sockets' axis z 28 (body z 22 … 37.5), poles along +x, wire entries down: AI0+ AI0− AI1+ AI1− AI2+ AI2− AI3+ AI3− | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| supply and output plug | terminal-plug 2.0, 7 poles, tag `x2`, mating face on the front block's face, x 5 … 40, sockets' axis z −36 (body z −42 … −26.5): 24V 0V FE AO0 M0 AO1 M1 | as x1 |
| headers | the pins the plugs' sockets take, standing out of the front block into the sockets | not modelled in this version: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures (as xfmr-control 1.0) |
| link to the controller | how the module reaches its CPU (a backplane, a side bus connector or a fieldbus) | not stated in this version and not modelled: the class has no feature for it; a version for a named controller adds it |
| LEDs | Ø3.2 lenses, 0.3 proud, at z 8: run (green) x 8; error (red) x 16 | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 20.0 × 32.0 (x 22 … 42, z −16 … 16), 0.1 proud | design choice |
| overall | 45.0 × 93.5 (y −86.0 … 7.5) × 100.0 | from the parts above; the plugs stand 16.0 proud of the front block |

Terminal marks: AI<n>+ / AI<n>− the differential inputs, AO<n> the outputs with M<n> their analogue 0 V, 24V / 0V the module supply, FE the functional earth (the analogue cables' shields; the moulded housing takes none). The marks are labels, a design choice; the plugs' own pole marks are 1 … n (terminal-plug 2.0 Decals) with these printed on the legend field.

## Named nodes
`led-run` (emissive, green: the module is powered and running) · `led-err` (emissive, red: a channel fault, an input outside its range or an open 4 … 20 mA loop) · the plugs' nodes `x1.t-1` … `x1.t-8`, `x2.t-1` … `x2.t-7` (clamp screws, gender none) and `x1.s-1` … `x1.s-8`, `x2.s-1` … `x2.s-7` (sockets, gender female), as terminal-plug 2.0 names them under its tag. Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-LENS-GREEN`, `M-LENS-RED` LEDs · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plugs (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "plc-aio", "4 AI / 2 AO", "0-10 V / 4-20 mA", "12 bit", "24 V DC 2 W", and the terminal diagram (AI0± … AI3±; 24V 0V FE; AO0 M0, AO1 M1). Beside the LEDs: "RUN", "ERR". No maker's name, logo or approval mark.

## Notes and open figures
- One figure of this element's own is open: the supply's under-voltage threshold, NOT ON FILE (B): IEC 61131-2 (its 24 V DC supply range table is not in lib/standards/sources.csv; behaviour.csv's `powered` row reads any supply voltage as powered until it is on file). Everything this element meets is on file (the rail clip, terminal-plug 2.0) and every other size and value is a design choice or a class value; nothing is guessed and shown as sourced. The placed plugs carry their own open line (their clamps' torque, terminal-plug 2.0's behaviour.csv), which behaviour.csv repeats for each pin as that element writes it.
- Not placed in this version, though lib/inventory.csv's made_of names them: terminal-plug ×2 are placed; din-clip-35 and led are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). It holds to the rail by the toolkit's rail clip, and its LEDs are the toolkit's lenses.
- Not stated or modelled in this version: the inputs' impedance and the current inputs' burden, the outputs' load limits (the voltage outputs' least load, the current outputs' greatest), the conversion time, the accuracy, the isolation between channels and to the supply, the inputs' overload limits, the bus to the controller and the mass. The phase-1 solver reads no analogue signal, so behaviour.csv carries the supply, the states and the LEDs only (its header says so).
- The supply's branch protection is the panel's to provide (the 24 V supply's own, psu-24v-2a4).
- Not a safety-function device (Class values 17 to 19).

## Outputs (out/)
`plc-aio.lsp` · `.glb` (pivots on the LEDs and the plugs' ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r33, 1.1 in elec-r46 (lib/rounds/elec/).

## History
| version | change |
|---|---|
| 1.0 | elec-r33 (2026-11-12, unattended): first build, generic (ETIM 10.0 EC001420), our own design; inventory elec pinned 6 (7 systems); places terminal-plug 2.0 twice (x1 8 poles, x2 7 poles) |
| 1.1 | elec-r46 (2026-11-13, unattended): text only, the geometry is 1.0's (review elec-r33 findings 1 and 4, element review note 1): the Notes name the supply's under-voltage threshold as the one open figure of the element's own (class B, IEC 61131-2), so DOC-005 counts it; FE is the cables' shields only; references/source.txt keeps the earlier stub's record as its end block, verbatim from git history |
