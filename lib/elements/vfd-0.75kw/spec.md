# vfd-0.75kw · v1.2 · variable frequency drive 0.75 kW, 3~ 380-480 V AC in (complexes.org generic)

**What** Variable frequency drive (frequency converter) for a 0.75 kW three-phase induction motor: three-phase 380 … 480 V AC 50 / 60 Hz in, a diode rectifier, a DC link and an IGBT inverter giving three-phase 0 … 480 V at 0 … 400 Hz out, 2.2 A, V/f control, started and reversed by two 24 V DC digital inputs, speed set by a 0 … 10 V analogue input, a fault relay. A finned aluminium heat sink (natural convection) on the 35 mm rail, a moulded housing with the power terminals on its front at the top (supply) and bottom (motor), and two pluggable control terminal blocks. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001857, built to the class values below; no maker's datasheet and no product is matched (the vendor file in references/ was not opened).
**Class** device · **Baseline** our own design: generic Frequency converter =< 1 kV (ETIM 10.0 EC001857). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the control terminals are placed terminal-plug 2.0 elements (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `VFD` · no parameters · places terminal-plug 2.0 twice (tags `x1`, `x2`).

## Class values
ETIM 10.0 EC001857 "Frequency converter =< 1 kV", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Mains voltage (EF006780) | 380 … 480 V AC (line to line) |
| 2 | Mains frequency (EF006783) | 50 / 60 Hz |
| 3 | Number of phases input (EF007117) | 3 |
| 4 | Number of phases output (EF006998) | 3 |
| 5 | Max. output frequency (EF007350) | 400 Hz |
| 6 | Max. output voltage (EF009560) | 480 V (line to line; the output follows the mains voltage at most) |
| 7 | Nominal output current I2N (EF009561) | 2.2 A |
| 8 | Max. output at quadratic load at rated output voltage (EF007366) | 0.75 kW |
| 9 | Max. output at linear load at rated output voltage (EF007364) | 0.75 kW |
| 10 | Power consumption (EF000346) | 35 W (the drive's own loss at rated output: the heat the heat sink is designed to shed) |
| 11 | Relative symmetric net frequency tolerance (EF007454) | 5 % |
| 12 | Relative symmetric net voltage tolerance (EF007453) | 10 % |
| 13 | Number of analogue outputs (EF001995) | 1 (AO: 0 … 10 V = 0 … max. output frequency) |
| 14 | Number of analogue inputs (EF001994) | 1 (AI: speed setpoint 0 … 10 V = 0 … max. output frequency) |
| 15 | Number of digital outputs (EF001993) | 1 (fault relay, N.O. contact RA-RC, closed while ready) |
| 16 | Number of digital inputs (EF001992) | 3 (DI1 run forward, DI2 run reverse, DI3 fault reset; 24 V DC, referred to COM; the switching levels are design: IEC 61131-2 type 1 (the standard's table NOT ON FILE (B): IEC 61131-2), as servo-drive) |
| 17 | With control element (EF001538) | no (no keypad: set and run from the control terminals) |
| 18 | Application in industrial area permitted (EF007294) | yes |
| 19 | Application in domestic- and commercial area permitted (EF007295) | no |
| 20 | Supporting protocol for TCP/IP (EF003050) | no |
| 21 | Supporting protocol for PROFIBUS (EF003052) | no |
| 22 | Supporting protocol for CAN (EF003053) | no |
| 23 | Supporting protocol for INTERBUS (EF003054) | no |
| 24 | Supporting protocol for ASI (EF003051) | no |
| 25 | Supporting protocol for KNX (EF003055) | no |
| 26 | Supporting protocol for Modbus (EF003057) | no |
| 27 | Supporting protocol for Data-Highway (EF003058) | no |
| 28 | Supporting protocol for DeviceNet (EF003059) | no |
| 29 | Supporting protocol for SUCONET (EF003060) | no |
| 30 | Supporting protocol for LON (EF003017) | no |
| 31 | Supporting protocol for PROFINET IO (EF007525) | no |
| 32 | Supporting protocol for PROFINET CBA (EF007524) | no |
| 33 | Supporting protocol for SERCOS (EF006657) | no |
| 34 | Supporting protocol for Foundation Fieldbus (EF007522) | no |
| 35 | Supporting protocol for EtherNet/IP (EF007521) | no |
| 36 | Supporting protocol for AS-Interface Safety at Work (EF007519) | no |
| 37 | Supporting protocol for DeviceNet Safety (EF007520) | no |
| 38 | Supporting protocol for INTERBUS-Safety (EF006662) | no |
| 39 | Supporting protocol for PROFIsafe (EF007526) | no |
| 40 | Supporting protocol for SafetyBUS p (EF007527) | no |
| 41 | Supporting protocol for BACnet (EF011944) | no |
| 42 | Supporting protocol for other bus systems (EF003062) | no |
| 43 | Number of HW-interfaces industrial Ethernet (EF003020) | 0 |
| 44 | Number of interfaces PROFINET (EF006932) | 0 |
| 45 | Number of HW-interfaces RS-232 (EF003021) | 0 |
| 46 | Number of HW-interfaces RS-422 (EF003022) | 0 |
| 47 | Number of HW-interfaces RS-485 (EF003023) | 0 |
| 48 | Number of HW-interfaces serial TTY (EF003024) | 0 |
| 49 | Number of HW-interfaces USB (EF003025) | 0 |
| 50 | Number of HW-interfaces parallel (EF003026) | 0 |
| 51 | Number of HW-interfaces other (EF003027) | 0 |
| 52 | With optical interface (EF003028) | no |
| 53 | With PC connection (EF006107) | no |
| 54 | Integrated breaking resistance (EF007293) | no |
| 55 | 4-quadrant operation possible (EF006803) | no |
| 56 | Type of converter (EF006978) | voltage-source converter (U converter): diode rectifier, DC link, IGBT inverter; V/f control |
| 57 | Degree of protection (IP) (EF005474) | IP20 |
| 58 | Degree of protection (NEMA) (EF011959) | not stated (open type: the panel enclosure gives the NEMA rating) |
| 59 | Height (EF000040) | 140 mm |
| 60 | Width (EF000008) | 72 mm |
| 61 | Depth (EF000049) | 143.5 mm (136.0 in front of the rail crown, 7.5 behind it) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design"); `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| heat sink base | 72.0 × 8.0 × 140.0 (y −8 … 0, z −70 … 70) on the clip | design choice |
| fins | seven, 2.0 thick at 11.67 pitch (x 0 … 72), 22.0 deep (y −30 … −8), the full 140.0 high; the outer two close the sides; channels 9.67 wide, open at the top and bottom | design choice |
| housing | 72.0 × 90.0 × 120.0 (y −120 … −30, z −60 … 60) on the fins' front edges; 10.0 of the channels shows above and below | design choice |
| power terminals | on the housing's front face (y −120): top row L1 L2 L3 PE at 15.0 pitch (x 13.5, 28.5, 43.5, 58.5; z 54), bottom row U V W PE (same x; z −54); screw heads Ø5.0 × 1.2; wire entries 5.0 × 8.0 slots cut 0.5 into the housing's top and bottom faces | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal, as controller-thyristor 1.0) |
| conductor range of the power clamps | the wire sizes and ferrules each clamp takes, and the screws' thread and torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by the terminal standard (IEC 60947-1, terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| control terminals | two terminal-plug 2.0 elements placed on the housing's front, mating face on it (y −120), poles along +x, wire entries down: `x1` 7 poles (x 6 … 41, sockets' axis z −30): DI1 DI2 DI3 COM AI AO AGND; `x2` 2 poles (x 52 … 62): RA RC, apart from the 24 V and analogue poles | terminal-plug 2.0 (its own spec; 12 A 250 V, the relay contact is within it); placement a design choice |
| control headers | the pins the plugs' sockets take, standing out of the housing's front into the sockets | not modelled in 1.1: terminal-plug 2.0 now gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version of this host can model it to those figures |
| switching levels of DI1 … DI3 | the input voltage that reads as high or low, the inputs' current | design: IEC 61131-2 type 1 inputs (Class values 16); the standard's table is NOT ON FILE (B): IEC 61131-2, so the thresholds are not written; behaviour.csv leaves the run command out until the solver reads them (as servo-drive 1.0; review vfd-0.75kw-1.1 finding 1, from review elec-r24 finding 2) |
| AI / AO scaling's accuracy | how closely 0 … 10 V maps to the setpoint and the output frequency | not stated: not a feature of the class, and the phase-1 solver reads no analogue signal |
| LEDs | Ø3.2 lenses, 0.3 proud, at z 44: ready (green) x 20; fault (red) x 32 | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 56.0 × 36.0 (x 8 … 64, z 0 … 36), 0.1 proud | design choice |
| overall | 72.0 × 143.5 (y −136.0 … 7.5) × 140.0 | from the parts above; the plugs stand 16.0 proud of the housing's front |

Terminal marks: L1 L2 L3 supply, U V W motor, PE (twice: the supply's and the motor's earth, one bar); the control marks are this element's own. The marks are labels, a design choice.

## Named nodes
`led-rdy` (emissive, green: supply present, no fault) · `led-flt` (emissive, red: the drive has stopped on a fault and RA-RC is open) · ports `t-L1`, `t-L2`, `t-L3`, `t-PE`, `t-U`, `t-V`, `t-W`, `t-PE-m` (kind port, unit screw, gender none: a screw clamp, PIN-002) · the plugs' nodes `x1.t-1` … `x1.t-7`, `x2.t-1`, `x2.t-2` (clamp screws, gender none) and `x1.s-1` … `x1.s-7`, `x2.s-1`, `x2.s-2` (sockets, gender female), as terminal-plug 2.0 names them under its tag (the same names as 1.0). Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-ALU-ANOD` heat sink (base and fins) · `M-GREY-PA` housing and rail clip · `M-ZINC` terminal screws · `M-GASKET` wire entries · `M-LENS-GREEN`, `M-LENS-RED` LEDs · `M-WHITE-PA` legend field · `M-GREEN` the placed plugs (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "vfd-0.75kw", "3~ 380-480 V AC 50/60 Hz", "3~ 0-480 V 0-400 Hz 2.2 A", "0.75 kW", and the control diagram (DI1 FWD, DI2 REV, DI3 RST, COM; AI 0-10 V, AO 0-10 V, AGND; RA-RC fault relay). Beside the LEDs: "RDY", "FLT". Terminal marks beside each screw; the earth symbol beside both PE; "hot surface" beside the fins (the warning symbol, no text claim of a temperature). No maker's name, logo or approval mark.

## Notes and open figures
- Two figures are open, both class B (a document wanted, not EM's): the power clamps' conductor range (IEC 60947-1) and the digital inputs' switching levels (IEC 61131-2), both above. Everything else this element meets is on file (the rail clip, terminal-plug 2.0), and every other size is a design choice; nothing is guessed and shown as sourced.
- Not placed in this version, though lib/inventory.csv's made_of names them: fan-cooling, led, screw-iso4762, din-clip-35. None is built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). The drive is cooled by natural convection and held by the toolkit's rail clip; placing them is a later version (a fan or screw holes change the shape: a major).
- Not stated or modelled in this version (not features of the class): the input current, the output's overload capacity, the acceleration and deceleration ramps, the carrier frequency, the DC link's discharge time, the relay contact's rating (within terminal-plug's 12 A 250 V), the clearance needed above and below, and the mass.
- The drive's branch protection (fuses or a breaker ahead of L1 L2 L3) and its isolation are the panel's to provide; a panel round that places this element sizes them and cites its standard (NEC 430 Part X for drives is the panel's).
- Not a safety-function device: removing DI1 / DI2 stops the output, but no safe torque off is claimed; a machine's safe stop is the panel's contactor or a safety device.

## Outputs (out/)
`vfd-0.75kw.lsp` · `.glb` (pivots on the LEDs and ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 Blender and Godot PASS in elec-r24, AutoCAD parked (r24: the IGES export, then a hang); 1.1 in elec-r26 and r27 (lib/rounds/elec/r26.md, r27.md); 1.2 in elec-r34 (lib/rounds/elec/r34.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r24 (2026-11-09, unattended): first build, generic (ETIM 10.0 EC001857), our own design; inventory elec pinned 3; places terminal-plug 1.0 twice for the control terminals |
| 1.1 | elec-r26 (2026-11-09, unattended): the plugs pinned at terminal-plug 2.0 (review elec-r22 finding 1: its sockets open 6.0 deep); the drive's own shape, nodes and origin as 1.0, so a minor |
| 1.2 | elec-r34 (2026-11-12, unattended): text only, review vfd-0.75kw-1.1 findings 1 and 2: DI1 … DI3 design IEC 61131-2 type 1, their switching levels NOT ON FILE (B): IEC 61131-2 (was class A; as servo-drive 1.0), the AI / AO accuracy "not stated"; "1.0" in the Notes and the docstring now "this version"; geometry as 1.1 |
