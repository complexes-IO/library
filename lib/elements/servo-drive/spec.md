# servo-drive · v1.2 · servo drive 1.0 kW, 3~ 380-480 V AC in, incremental encoder feedback (complexes.org generic)

**What** Servo drive (servo amplifier) for a 1.0 kW permanent-magnet synchronous servo motor: three-phase 380 … 480 V AC 50 / 60 Hz in, a diode rectifier, a DC link and an IGBT inverter giving three-phase 0 … 480 V at 0 … 400 Hz out, 3.0 A continuous and 9.0 A peak, current, speed and position loops closed on an incremental encoder (TTL / RS-422 line driver, fed 5 V from the drive), enabled and reset by 24 V DC digital inputs, two end-of-travel limit inputs, a ±10 V differential reference input, a ready relay. A finned aluminium heat sink (natural convection) on the 35 mm rail, a moulded housing with the power terminals on its front at the top (supply) and bottom (motor), and three pluggable terminal blocks (control, relay, encoder). A generic element (OPERATING.md 12, EM 2026-11-07): ETIM 10.0 has no class for a servo drive, so it is our own vendor-neutral design by the standard whose rating data its class values follow (EM 2026-11-08: "no ETIM class; IEC 61800-2 values"), built to the class values below; no maker's datasheet and no product is matched (the vendor file in references/ was not opened).
**Class** device · **Baseline** our own design: generic servo drive, 1.0 kW (no ETIM class; IEC 61800-2 values). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the control, relay and encoder terminals are placed terminal-plug 2.0 elements (version pinned); every other size is a design choice, said so below. The rating items are named as IEC 61800-2 (adjustable speed electrical power drive systems, low-voltage AC drives: rating data) names them; the standard is not in lib/standards/sources.csv, and no figure is taken from it: every value is this element's design input.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `SERVODRV` · no parameters · places terminal-plug 2.0 three times (tags `x1`, `x2`, `x3`).

## Class values (no ETIM class; IEC 61800-2 values)
The rating data of a low-voltage AC power drive system's converter, in the order IEC 61800-2 lists its ratings, with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | rating item (IEC 61800-2) | value |
|---|---|---|
| 1 | Rated input voltage | 3~ 380 … 480 V AC (line to line) |
| 2 | Rated input frequency | 50 / 60 Hz |
| 3 | Number of input phases | 3 |
| 4 | Rated input current | 3.4 A rms (design input: the branch ahead of L1 L2 L3 is sized to it by the panel, NEC 430 Part X). A design margin, said so: a 1.0 kW three-phase load at 380 V and cos φ 0.85 draws 1000 / (√3 × 380 × 0.85) = 1.79 A (I = P / (√3 U cos φ)); 3.4 A is set above it for the drive's losses and the rectifier's non-sinusoidal input current, conservative for the panel's branch |
| 5 | Input voltage tolerance | ±10 % (342 … 528 V) |
| 6 | Rated output voltage | 3~ 0 … 480 V AC (line to line; the output follows the input voltage at most) |
| 7 | Rated output current (continuous) | 3.0 A rms |
| 8 | Peak output current | 9.0 A rms for 3 s (300 %), then the continuous rating |
| 9 | Rated output power | 1.0 kW: the rated shaft power of the servo motor the drive is sized for (continuous). Not the product of items 6 and 7: the 3.0 A continuous output current (item 7) is a design input set above such a motor's full-load current, for low-voltage windings and margin (review servo-drive-1.0 finding 1) |
| 10 | Output frequency | 0 … 400 Hz (rotating field: 6000 min⁻¹ for an 8-pole motor) |
| 11 | Overload capability | 300 % for 3 s (item 8); the thermal model limits the mean to item 7 |
| 12 | Power loss at rated output | 45 W (the drive's own loss: the heat the heat sink is designed to shed by natural convection) |
| 13 | Motor type | permanent-magnet synchronous servo motor, three-phase; the motor's rating is the motor element's (servo-motor, not built) |
| 14 | Feedback | incremental encoder, A / B quadrature, TTL / RS-422 line-driver levels, fed 5 V DC 200 mA from the drive (x3: A+ A− B+ B− 5V 0V); no absolute encoder, no resolver |
| 15 | Control inputs | 4 digital inputs at 24 V DC referred to COM (x1: EN enable, RST fault reset, LIM+ and LIM− end-of-travel limits, closed = travel allowed); the switching levels are design: IEC 61131-2 type 1 (the standard's table NOT ON FILE (B): IEC 61131-2) |
| 16 | Reference input | 1 analogue, differential ±10 V (x1: AI+ AI−, AGND the analogue 0 V): speed reference 0 … ±rated speed; torque mode not stated |
| 17 | Status output | 1 digital output: the ready relay, N.O. contact RA-RC (x2), closed while powered and no fault; its contact rating is within terminal-plug 2.0's (12 A 250 V, its spec), the drive claims none of its own |
| 18 | Dynamic braking | no (no brake chopper or resistor terminals; the regenerative energy the DC link absorbs is not stated) |
| 19 | Safe torque off | none: no safety function is claimed (Notes) |
| 20 | Degree of protection | IP20 (open type: the panel enclosure gives the NEMA rating) |
| 21 | Cooling | natural convection through the heat sink's vertical channels (fan-cooling is not placed in this version) |
| 22 | Height | 150 mm |
| 23 | Width | 65 mm |
| 24 | Depth | 143.5 mm (136.0 in front of the rail crown, 7.5 behind it) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design", source "IEC 61800-2 value"); `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| heat sink base | 65.0 × 8.0 × 150.0 (y −8 … 0, z −75 … 75) on the clip | design choice |
| fins | seven, 2.0 thick at 10.5 pitch (x 0 … 65), 22.0 deep (y −30 … −8), the full 150.0 high; the outer two close the sides; channels 8.5 wide, open at the top and bottom | design choice |
| housing | 65.0 × 90.0 × 130.0 (y −120 … −30, z −65 … 65) on the fins' front edges; 10.0 of the channels shows above and below | design choice |
| power terminals | on the housing's front face (y −120): top row L1 L2 L3 PE at 14.0 pitch (x 11.5, 25.5, 39.5, 53.5; z 59), bottom row U V W PE (same x; z −59); screw heads Ø5.0 × 1.2; wire entries 5.0 × 8.0 slots cut 0.5 into the housing's top and bottom faces | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal, as vfd-0.75kw 1.1) |
| conductor range of the power clamps | the wire sizes and ferrules each clamp takes, and the screws' thread and torque | NOT ON FILE (B): IEC 60947-1: a fit with the wire element; the clamps' connecting capacity is set by the terminal standard (IEC 60947-1, terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| control plugs | three terminal-plug 2.0 elements placed on the housing's front, mating face on it (y −120), poles along +x, wire entries down: `x1` 8 poles (x 4 … 44, sockets' axis z −36): EN RST LIM+ LIM− COM AI+ AI− AGND; `x2` 2 poles (x 50 … 60, z −36): RA RC, apart from the 24 V and analogue poles; `x3` 6 poles (x 17.5 … 47.5, z −12): A+ A− B+ B− 5V 0V, the encoder, above the control row | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| control headers | the pins the plugs' sockets take, standing out of the housing's front into the sockets | not modelled in this version: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version of this host can model it to those figures (as vfd-0.75kw) |
| switching levels of EN, RST, LIM+, LIM− | the input voltage that reads as high or low, the inputs' current | design: IEC 61131-2 type 1 inputs (Class values 15); the standard's table is NOT ON FILE (B): IEC 61131-2, so the thresholds are not written; behaviour.csv leaves the enable out until the solver reads them |
| LEDs | Ø3.2 lenses, 0.3 proud, at z 50: ready (green) x 18; fault (red) x 30 | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 49.0 × 32.0 (x 8 … 57, z 8 … 40), 0.1 proud | design choice |
| overall | 65.0 × 143.5 (y −136.0 … 7.5) × 150.0 | from the parts above; the plugs stand 16.0 proud of the housing's front |

Terminal marks: L1 L2 L3 supply, U V W motor, PE (twice: the supply's and the motor's earth, one bar); the control, relay and encoder marks are this element's own. The marks are labels, a design choice.

## Named nodes
`led-rdy` (emissive, green: supply present, no fault) · `led-flt` (emissive, red: the drive has stopped on a fault and RA-RC is open) · ports `t-L1`, `t-L2`, `t-L3`, `t-PE`, `t-U`, `t-V`, `t-W`, `t-PE-m` (kind port, unit screw, gender none: a screw clamp, PIN-002) · the plugs' nodes `x1.t-1` … `x1.t-8`, `x2.t-1`, `x2.t-2`, `x3.t-1` … `x3.t-6` (clamp screws, gender none) and `x1.s-1` … `x1.s-8`, `x2.s-1`, `x2.s-2`, `x3.s-1` … `x3.s-6` (sockets, gender female), as terminal-plug 2.0 names them under its tag. Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-ALU-ANOD` heat sink (base and fins) · `M-GREY-PA` housing and rail clip · `M-ZINC` terminal screws · `M-GASKET` wire entries · `M-LENS-GREEN`, `M-LENS-RED` LEDs · `M-WHITE-PA` legend field · `M-GREEN` the placed plugs (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "servo-drive", "3~ 380-480 V AC 50/60 Hz", "3~ 0-480 V 0-400 Hz 3.0 A (9.0 A pk)", "1.0 kW", and the control diagram (EN, RST, LIM+, LIM−, COM; AI+ AI− ±10 V, AGND; RA-RC ready relay; ENC A+ A− B+ B− 5V 0V). Beside the LEDs: "RDY", "FLT". Terminal marks beside each screw; the earth symbol beside both PE; "hot surface" beside the fins (the warning symbol, no text claim of a temperature). No maker's name, logo or approval mark.

## Notes and open figures
- Two figures are open, both class B (a document wanted, not EM's): the power clamps' conductor range (IEC 60947-1) and the digital inputs' switching thresholds (IEC 61131-2), both above. Everything else this element meets is on file (the rail clip, terminal-plug 2.0), and every other size is a design choice; nothing is guessed and shown as sourced.
- The standard named in the Baseline, IEC 61800-2, is not in lib/standards/sources.csv: it gives this element's rating items their names and order, as OPERATING.md 12 asks for a product class ETIM has no class for; no figure is taken from it (lib/needs-em/elec.md r30).
- Not placed in this version, though lib/inventory.csv's made_of names them: terminal-plug ×3 are placed; fan-cooling, led, screw-iso4762 are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). The drive is cooled by natural convection and held by the toolkit's rail clip; placing them is a later version (a fan or screw holes change the shape: a major).
- Not stated or modelled in this version: the DC link's voltage and capacitance, its discharge time, the carrier frequency, the loop bandwidths, the encoder's line count the drive accepts, the motor's rating, the relay contact's own rating, the clearance needed above and below, and the mass.
- The drive's branch protection (fuses or a breaker ahead of L1 L2 L3) and its isolation are the panel's to provide; a panel round that places this element sizes them and cites its standard (NEC 430 Part X for drives is the panel's).
- Not a safety-function device: no safe torque off is claimed; removing EN stops the output, but a machine's safe stop is the panel's contactor or a safety device (relay-safety-2ch-2no1nc). A version with STO inputs would be a safety-function class and need EM's safety sign-off.
- The id: the inventory's row is `servo-drive`; the id convention (OPERATING.md 6) would add the size (servo-drive-1kw, as vfd-0.75kw and hpu-7.5kw). The rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r30.

## Outputs (out/)
`servo-drive.lsp` · `.glb` (pivots on the LEDs and ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r30 (lib/rounds/elec/r30.md); 1.1 in elec-r34 (lib/rounds/elec/r34.md); 1.2 in elec-r38 (lib/rounds/elec/r38.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r30 (2026-11-11, unattended): first build, generic (no ETIM class; IEC 61800-2 values), our own design; inventory elec pinned 6; places terminal-plug 2.0 three times |
| 1.1 | elec-r34 (2026-11-12, unattended): text only, review servo-drive-1.0 finding 1: Class values 9 says the 1.0 kW is the rated shaft power of the motor the drive is sized for (not "at the rated output current and voltage"), Class values 4 says the 3.4 A input current is a design margin, with the formula; "1.0" in the Notes and the docstring now "this version"; geometry as 1.0. Finding 2 (x3's wire entries onto x1, a node moves) is a 2.0, not this minor |
| 1.2 | elec-r38 (2026-11-12, unattended): text only, pins.csv: the encoder supply pins x3.t-5 (5V) and x3.t-6 (0V) take the source's roles `supply+:5V` and `supply0` (were `out` and `load0`): the drive feeds servo-motor 1.0's encoder (its port-enc 5V `in`, 0V `load0`), so a 0 V net joining the two has its source (needs-em r37 item 4); geometry as 1.0 |
