# controller-thyristor · v1.0 · thyristor power controller, three-phase 480 V AC 20 A (complexes.org generic)

**What** Thyristor (SCR) power controller for a machine's resistive heater loads (barrel, platen or oven heaters): three anti-parallel thyristor pairs, one in each line, fired in bursts of whole mains cycles at the zero crossing, the share of cycles set by a 0 … 10 V setpoint; 208 … 480 V AC, 20 A, 50 / 60 Hz, a 24 V DC auxiliary supply, an enable input and a ready relay. A finned aluminium heat sink (natural convection) on the 35 mm rail, a moulded cover with the power terminals on its shoulders and a raised control front. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC011564, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Thyristor power controller (ETIM 10.0 EC011564). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `SCRPC` · no parameters.

## Class values
ETIM 10.0 EC011564 "Thyristor power controller", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Type of system (EF008552) | three-phase controller, all three lines switched (an anti-parallel thyristor pair in each), burst firing at the zero crossing, for resistive loads |
| 2 | Secondary nominal current (EF006087) | 20 A (each line, resistive load) |
| 3 | Nominal voltage AC (EF008798) | 208 … 480 V (line to line) |
| 4 | Frequency (EF005455) | 50 / 60 Hz |
| 5 | Number of phases input (EF007117) | 3 |
| 6 | Number of phases output (EF006998) | 3 |
| 7 | Output power (EF000426) | 16.6 kW (at 480 V: √3 × 480 V × 20 A, resistive load) |
| 8 | Power loss (EF005387) | 0.08 kW (at 20 A in all three lines: the heat the heat sink is designed to shed) |
| 9 | Auxiliary voltage (DC) (EF005901) | 24 V (19.2 … 28.8 V) |
| 10 | Number of analogue inputs (EF001994) | 1 (AI: setpoint 0 … 10 V = 0 … 100 % of the cycles fired) |
| 11 | Number of analogue outputs (EF001995) | 0 |
| 12 | Number of digital inputs (EF001992) | 1 (EN: enable, 24 V DC) |
| 13 | Number of digital outputs (EF001993) | 1 (ready relay, N.O. contact 13-14) |
| 14 | With fan (EF002196) | no (natural convection through the heat sink's channels) |
| 15 | With control element (EF001538) | no |
| 16 | Control element optional (EF017252) | no |
| 17 | With PC connection (EF006107) | no |
| 18 | PC connection optional (EF017253) | no |
| 19 | Programming according to IEC 61131 (EF017408) | no |
| 20 | Operating temperature (EF001742) | 0 … 40 °C |
| 21 | Allowable relative humidity (EF023900) | 5 … 85 % (no condensation) |
| 22 | Pollution degree (EF002570) | 2 |
| 23 | Mounting method (EF000003) | 35 mm DIN rail (EN 60715 TH35-7.5), heat sink channels vertical |
| 24 | Height (EF000040) | 150 mm |
| 25 | Width (EF000008) | 90 mm |
| 26 | Depth (EF000049) | 106.5 mm (99.0 in front of the rail crown, 7.5 behind it) |
| 27 | Degree of protection (IP) (EF005474) | IP20 |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design"; the output power "derived"); `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| heat sink base | 90.0 × 8.0 × 150.0 (y −8 … 0, z −75 … 75) on the clip | design choice |
| fins | nine, 2.0 thick at 11.0 pitch (x 0, 11, … 88), 40.0 deep (y −48 … −8), the full 150.0 high; the outer two close the sides; channels 9.0 wide, open at the top and bottom | design choice |
| cover shoulders | 90.0 × 30.0 × 110.0 (y −78 … −48, z −55 … 55) on the fins' front edges; 20.0 of the channels shows above and below | design choice |
| raised control front | 86.0 × 20.0 × 64.0 (x 2 … 88, y −98 … −78, z −32 … 32) | design choice |
| power terminals | on the shoulders' front face (y −78): top row L1 L2 L3 PE at 20.0 pitch (x 15, 35, 55, 75; z 48), bottom row T1 T2 T3 (x 25, 45, 65; z −48); screw heads Ø6.0 × 1.5; wire entries 6.0 × 10.0 slots cut 0.5 into the shoulders' top and bottom faces | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| control terminals | on the raised front (y −98): 24V 0V EN AI 13 14 at 7.5 pitch (x 26.25 … 63.75; z 27); screw heads Ø3.2 × 1.0; wire entries 3.0 × 8.0 slots cut 0.5 into the raised front's top face | design choice |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, power and control, and the screws' thread and torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by the terminal standard (IEC 60947-1, terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| LEDs | Ø3.2 lenses, 0.3 proud, at z 10: on (green) x 20; L1, L2, L3 (yellow) x 35, 45, 55; fault (red) x 70 | design choice |
| legend field | 70.0 × 26.0 (x 10 … 80, z −26 … 0), 0.1 proud | design choice |
| overall | 90.0 × 106.5 (y −99.0 … 7.5) × 150.0 | from the parts above; the control screw heads stand 1.0 proud of the raised front |

Terminal marks: L1 L2 L3 supply, T1 T2 T3 load, PE; the control marks are this element's own. The marks are labels, a design choice.

## Named nodes
`led-on` (emissive, green: auxiliary supply present) · `led-l1`, `led-l2`, `led-l3` (emissive, yellow: that line's thyristor pair conducting; in burst firing they follow the cycles fired) · `led-fault` (emissive, red: the controller has stopped firing on a fault and 13-14 is open) · ports `t-L1`, `t-L2`, `t-L3`, `t-PE`, `t-T1`, `t-T2`, `t-T3`, `t-24V`, `t-0V`, `t-EN`, `t-AI`, `t-13`, `t-14` (kind port, unit screw, gender none: a screw clamp, PIN-002). Nothing moves. The twin drives the LEDs from the supply, EN, AI and the fault state; pins.csv names what each terminal carries.

## Materials by layer
`M-ALU-ANOD` heat sink (base and fins) · `M-GREY-PA` cover, raised front and rail clip · `M-ZINC` terminal screws · `M-GASKET` wire entries · `M-LENS-GREEN`, `M-LENS-YELLOW`, `M-LENS-RED` LEDs · `M-WHITE-PA` legend field

## Decals (Blender)
On the legend field: "complexes.org generic", "controller-thyristor", "3~ 208-480 V AC 50/60 Hz", "20 A", "24 V DC", "AI 0-10 V", and the terminal diagram (L1 L2 L3 → T1 T2 T3; 24V 0V EN AI; 13-14 ready). Beside the LEDs: "ON", "L1", "L2", "L3", "FAULT". Terminal marks beside each screw; the earth symbol beside PE; "hot surface" beside the fins (the warning symbol, no text claim of a temperature). No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). Everything else this element meets is on file (the rail clip), and every other size is a design choice; nothing is guessed and shown as sourced.
- Not stated or modelled in 1.0 (not features of the class): the auxiliary supply's current (so the 24 V budget, ELR-020, has no current from this element until a version states one), the ready relay's contact rating, the burst period, which faults the controller detects, the heat sink's temperature rise and the clearance it needs above and below, and the mass.
- The thyristors' short-circuit protection (semiconductor fuses ahead of L1 L2 L3) and the branch's isolation are the panel's to provide; a panel round that places this element sizes them from the class values and cites its standard.
- Not a safety-function device: EN removes the firing, but it is a control input, not a safe stop; a heater circuit's safe off is the panel's contactor or disconnect.

## Outputs (out/)
`controller-thyristor.lsp` · `.glb` (pivots on the LEDs and ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011564), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07) |
