# photoeye-m18 · v1.0 · photoelectric sensor, diffuse, M18 × 1 barrel, red light, 400 mm, PNP N.O., 24 V DC (complexes.org generic)

**What** Diffuse reflective photoelectric sensor (an energetic light scanner) for a conveyor's or a station's "part present" signal: a red LED emitter and a receiver behind one lens in the front face of an M18 × 1 threaded barrel; the light goes out along the axis, and a target within 400 mm reflects enough of it back to switch the output. One PNP output, light-switching (normally open: on while a target reflects), fed 24 V DC, so a PLC's 24 V DC input reads it. The barrel goes through a Ø18 bracket hole and is held by two lock nuts, one each side; the cable plugs onto an axial M12 connector at the back, where a green LED shows the supply and a yellow LED the output. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001821 "Diffuse reflective photoelectric sensor", built to the class values below; no maker's datasheet (the folder's earlier stub is reference only and was not used: references/source.txt).
**Class** device · **Baseline** our own design: generic Diffuse reflective photoelectric sensor (ETIM 10.0 EC001821). The class values are this element's definition (design inputs); the barrel's thread M18 × 1 is derived (ISO 68-1 / ISO 965-1 6g); every other size is a design choice, said so below.
**Units / frame** mm, Z up. Origin: the barrel's front face y = 0 on its axis x = 0, z = 0; the light goes out toward −y, the barrel toward +y (in a BOM, the barrel's axis on the bracket hole's, the nuts either side of the bracket).
**Built with** toolkit 1.3 · AutoLISP command `PEYEM18` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC001821 Diffuse reflective photoelectric sensor)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Operating distance (EF004121) | 0 … 400 mm on a white target (the test target not stated) |
| 2 | Pre failure notice (EF004129) | no |
| 3 | With time function (EF003582) | no |
| 4 | Max. switching distance (EF007367) | 400 mm |
| 5 | Max. output current (EF001315) | 100 mA |
| 6 | With reflector (EF003583) | no (diffuse: the target is the reflector) |
| 7 | Analogue output 0 V ... 10 V (EF006807) | no |
| 8 | Analogue output 0 mA ... 20 mA (EF006808) | no |
| 9 | Analogue output 4 mA ... 20 mA (EF006810) | no |
| 10 | Analogue output -10 V ... +10 V (EF006809) | no |
| 11 | With other analogue output (EF007485) | no |
| 12 | Setting procedure (EF003994) | none (a fixed range: no potentiometer and no teach button) |
| 13 | With communication interface analogue (EF007305) | no |
| 14 | With communication interface AS-Interface (EF007306) | no |
| 15 | With communication interface CANOpen (EF007307) | no |
| 16 | With communication interface DeviceNet (EF007308) | no |
| 17 | With communication interface Ethernet (EF007309) | no |
| 18 | With communication interface INTERBUS (EF007310) | no |
| 19 | With communication interface PROFIBUS (EF007311) | no |
| 20 | With communication interface RS-232 (EF007312) | no |
| 21 | With communication interface RS-422 (EF007313) | no |
| 22 | With communication interface RS-485 (EF007314) | no |
| 23 | With communication interface SSD (EF007315) | no |
| 24 | With communication interface SSI (EF007316) | no |
| 25 | Number of semiconductor outputs with signalling function (EF003945) | 1 |
| 26 | Number of contact energized outputs with signalling function (EF003946) | 0 |
| 27 | Number of protected semiconductor outputs (EF003951) | 0 |
| 28 | Number of protected contact energized outputs (EF003952) | 0 |
| 29 | Type of interface for safety communication (EF003956) | none |
| 30 | Type of electric connection (EF003961) | connector M12, axial (receptacle-m12 placed at a later version: Notes) |
| 31 | Type of switching output (EF003962) | PNP |
| 32 | Type of switch function (EF003963) | normally open (light-switching: on while a target reflects) |
| 33 | Operation agent-safety class (EF003982) | none |
| 34 | Explosion safety category for gas (EF003997) | none (no explosion protection claimed) |
| 35 | Explosion safety category for dust (EF003998) | none (no explosion protection claimed) |
| 36 | Construction type housing (EF004008) | cylindrical, threaded M18 × 1 |
| 37 | Width sensor (EF007094) | not stated (a cylinder: its diameter is feature 38) |
| 38 | Diameter sensor (EF007111) | 18 mm (M18 × 1) |
| 39 | Height of sensor (EF007283) | not stated (a cylinder: its diameter is feature 38) |
| 40 | Length of sensor (EF007334) | 63 mm (the lens to the connector seat's face) |
| 41 | Sensing mode (EF007503) | diffuse (energetic) reflection |
| 42 | Material of optical surface (EF004134) | PMMA (acrylic) |
| 43 | Housing material (EF001596) | brass, nickel-plated (the barrel); plastic (the rear cap) |
| 44 | Max. output current at protected output (EF004035) | not stated (no protected output) |
| 45 | Min. reflector distance (EF004046) | not stated (no reflector) |
| 46 | Response time (EF004094) | not stated (the twin switches the output at once) |
| 47 | Transmission range of the safety field (EF004098) | not stated (no safety field) |
| 48 | Switching frequency (EF003587) | not stated |
| 49 | Type of safety according to IEC 61496-1 (EF004105) | none |
| 50 | Switching voltage of OSSD at state "high" (EF004102) | not stated (no OSSD) |
| 51 | Voltage type (EF000187) | DC |
| 52 | With monitoring function downstream switching devices (EF004052) | no |
| 53 | Laser protection class (EF004027) | none (an LED emitter, no laser) |
| 54 | Wavelength of the sensor (EF004132) | not stated (red light) |
| 55 | Type of light (EF004029) | red light (visible) |
| 56 | Light dot (EF004030) | not stated |
| 57 | AWG-number (EF007010) | not stated (a connector: no cable of its own) |
| 58 | Material of cable sheath (EF004136) | not stated (a connector: no cable of its own) |
| 59 | With restart blockage (EF004054) | no |
| 60 | Suitable for safety functions (EF001597) | no |
| 61 | Degree of protection (IP) (EF005474) | not stated (no lens or connector seal is modelled) |
| 62 | Degree of protection (NEMA) (EF011959) | not stated |
| 63 | Ambient temperature (EF002386) | not stated |
| 64 | Rated control supply voltage AC 50 Hz (EF003978) | none (DC only) |
| 65 | Rated control supply voltage AC 60 Hz (EF003979) | none (DC only) |
| 66 | Rated control supply voltage DC (EF003980) | 24 V (the PLC's 24 V DC inputs it feeds; its tolerance band not stated) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. The supply current, the response time and the switching frequency are not stated, and the twin reads none of them. `pins.csv` gives each pin its role; ratings.csv carries the supply voltage, the output current and the sensing range.

## Output
| state | what it gives | twin |
|---|---|---|
| off | no voltage across +V and 0V: the emitter dark, Q off | default |
| powered, no target | the emitter lit, the green LED on; Q off (open) | read: powered while +V is above 0V (behaviour.csv) |
| powered, target detected | Q switched to +V (PNP, normally open), the yellow LED on | the twin places the target (manual toggle): the phase-1 solver traces no light. The output switch's voltage drop is not stated, so Q is taken at the supply's level |

## Dimensions
| item | value | source |
|---|---|---|
| barrel | Ø17.974 × 50.0 (y 0 … 50), the front face y 0 | thread M18 × 1 derived: derive.thread(18.0, 1.0) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6g d 17.797 … 17.974), modelled plain at d max; the length a design choice |
| lens window | Ø14.0, 1.0 proud of the barrel's front face (y −1 … 0) | design choice |
| rear cap | Ø17.974 × 8.0 (y 50 … 58), plastic | design choice (at the barrel's diameter, so both lock nuts thread on from the front) |
| connector seat | Ø12.0 × 4.0 (y 58 … 62), the face receptacle-m12 sits on; port node `port-x1` on its face | design choice; the receptacle and its fixing are receptacle-m12's (Notes) |
| status LEDs | two lenses Ø2.2, 0.3 proud of the cap's back face, on a radius 7.4 at 135° (green, `led-pwr`, upper left seen from the front) and 45° (yellow, `led-out`) | design choice |
| overall | 17.974 × 63.0 × 17.974 (x ±8.987, y −1 … 62, z ±8.987) | from the parts above |

## Named nodes
Port `port-x1` (kind port, unit m12-a, gender none: no contact is modelled until receptacle-m12 is placed on the seat, PIN-002) · `led-pwr` (emissive, green: powered) · `led-out` (emissive, yellow: the output on). pins.csv names the three signals the connector carries; which M12 contact carries which is receptacle-m12's and the cordset's, set when it is placed. Nothing moves.

## Materials by layer
`M-SILVER` barrel · `M-LENS-DARK` lens window · `M-BLACK-PA` rear cap and connector seat · `M-LENS-GREEN`, `M-LENS-YELLOW` the LEDs

## Decals (Blender)
None: the barrel carries no flat field for a legend (a design choice). No maker's name, logo or approval mark.

## Notes
- One open line, class B, a standard's table not on file and asked for once in lib/standards/wanted.md: the least supply voltage at which the output is valid (the IEC 61131-2 24 V DC class's lower limit, which behaviour.csv's `powered` row reads as "above 0"): NOT ON FILE (B): IEC 61131-2. Every rating is a class value (design input), every size a design choice, the barrel's thread derived. Nothing is guessed and shown as sourced.
- Not a safety-function device (Class values 49, 60): a light curtain or a safety light barrier is a safety-class element with EM's sign-off.
- Not placed (OPERATING.md 12, quality at the source): receptacle-m12 (built, not yet past station 6), so the connection is a seat with its port node, as encoder 1.0; nut-m18-lock x2 (not built; a nut's shape is its standard's, never generic), so the barrel is plain for the installer's nuts; led (not built), so the two lenses are drawn here. Nothing is modelled that a later element will place.
- The folder's earlier stub: references/source.txt keeps its record verbatim as the end block (its earlier source.txt and metadata.json; OPERATING.md 6, DOC-007). The stub's validation.json stays in the folder: removing or moving a tracked file is refused to an unattended run (lib/needs-em/elec.md r47, r50).
- The id: the inventory's row is `photoeye-m18`; the id convention (OPERATING.md 6) gives `photoeye-diff-m18-pnp-no`. A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r50.

## Outputs (out/)
`photoeye-m18.lsp` · `.glb` (a port pivot on the connector seat, two emissive LED pivots, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r50 (lib/rounds/elec/r50.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r50 (2026-11-13, unattended): first build, generic ETIM 10.0 EC001821, our own design; inventory elec photoeye-m18 (9 systems) |
