# servo-motor · v1.2 · servo motor 1.0 kW 3000 min⁻¹, 3~ 400 V 2.5 A, incremental encoder, square flange 80 (complexes.org generic)

**What** Permanent-magnet synchronous servo motor: 1.0 kW rated output at 3000 min⁻¹ (3.18 N·m rated torque, 9.55 N·m peak), three-phase 400 V, 2.5 A rated and 7.5 A peak current, 8 poles, totally enclosed and cooled by natural convection from its housing, an incremental encoder at the non-drive end (A / B quadrature, RS-422 line driver, fed 5 V from the drive), no holding brake. A square flange 80 with a Ø70 spigot and four M6 clearance holes, a plain Ø19 shaft 35 long, a square housing, an encoder cover, and two connector seats on top (power and encoder). Sized for servo-drive 1.1 on file: every rating sits inside the drive's (Class values). A generic element (OPERATING.md 12, EM 2026-11-07): ETIM 10.0 has no class for a servo motor, so it is our own vendor-neutral design by the standard whose rating items its class values follow (EM 2026-11-08: "no ETIM class; IEC 60034-1 values"; lib/inventory.csv: the flange and shaft a design choice stated as such), built to the class values below; no maker's datasheet and no product is matched (the folder's earlier stub was not used: references/source.txt).
**Class** device · **Baseline** our own design: generic servo motor, 1.0 kW (no ETIM class; IEC 60034-1 values). The class values are this element's definition (design inputs); the flange holes are ISO 273 medium clearance for M6 (lib/standards/holes.csv); the flange, spigot, shaft and every other size are design choices, said so below. The rating items of a rotating machine are named as IEC 60034-1 (rotating electrical machines: rating and performance) names them, and the servo class adds its own (Class values); the standard is not in lib/standards/sources.csv, and no figure is taken from it: every value is this element's design input.
**Units / frame** mm, Z up. Origin: flange motor: the flange's mounting face y = 0, shaft axis x = 0, z = 0, shaft toward −y, body toward +y (in a BOM, the machine's mounting face at y = 0 and the shaft into it).
**Built with** toolkit 1.3 · AutoLISP command `SERVOMTR` · no parameters · places no element (receptacle-m23 and screw-iso4762 are not built: Notes).

## Class values (no ETIM class; IEC 60034-1 values)
The items this element is designed to, each with its value or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12). Items 1 to 5, 10, 12, 19, 21 and 22 are a rotating electrical machine's rating items as IEC 60034-1 names them; 13 is the thermal class as IEC 60085 designates it, 17 and 18 the codes of IEC 60034-6 and -7; items 6 to 9, 11, 14 to 16, 20 and 23 to 25 are the servo class's own, the figures a servo axis is sized by. The order is this table's, not a standard's (the standards are not on file: Notes).

| # | rating item | value |
|---|---|---|
| 1 | Rated output | 1.0 kW (shaft power, duty S1); the rated output servo-drive 1.1 is sized for (its Class values 9) |
| 2 | Rated voltage | 3~ 400 V AC, line to line: the supply class, the mains voltage of the drive that feeds it (within servo-drive 1.1's 0 … 480 V output). Not the terminal voltage at rated speed: item 16 gives a back-EMF of about 1000 / (√3 × 2.5) = 231 V line to line at 3000 min⁻¹ (rms phase current, a sinusoidal machine), which the drive's output sets; the terminal voltage is not claimed |
| 3 | Number of phases | 3 |
| 4 | Rated current | 2.5 A rms at rated torque (within servo-drive 1.1's 3.0 A continuous) |
| 5 | Rated speed | 3000 min⁻¹ |
| 6 | Rated torque | 3.18 N·m: T = P / (2π n / 60) = 1000 / (2π × 3000 / 60) = 3.183 N·m, from items 1 and 5 |
| 7 | Peak torque | 9.55 N·m (300 % of item 6, for 3 s, at item 8's current) |
| 8 | Peak current | 7.5 A rms for 3 s (300 %; within servo-drive 1.1's 9.0 A peak) |
| 9 | Number of poles | 8 |
| 10 | Rated frequency | 200 Hz: f = p n / 120 = 8 × 3000 / 120, from items 5 and 9 |
| 11 | Maximum speed | 5000 min⁻¹ (333 Hz, within servo-drive 1.1's 400 Hz output) |
| 12 | Duty type | S1, continuous running duty |
| 13 | Thermal class | 155 (F) |
| 14 | Feedback | incremental encoder, A / B quadrature, 2500 lines per revolution, RS-422 line-driver outputs, fed 5 V DC 200 mA by the drive (A+ A− B+ B− 5V 0V, as servo-drive 1.1's x3); no index channel, no absolute encoder, no resolver |
| 15 | Holding brake | none |
| 16 | Torque constant | 1.27 N·m/A: item 6 / item 4 (3.18 / 2.5) |
| 17 | Cooling method | totally enclosed, natural convection from the housing's surface (IC 410 in IEC 60034-6's code) |
| 18 | Mounting | flange with through holes, shaft horizontal or vertical (IM B5 / V1 in IEC 60034-7's code) |
| 19 | Degree of protection | not stated (no shaft seal or gasket is modelled) |
| 20 | Rotor moment of inertia | not stated |
| 21 | Mass | not stated |
| 22 | Ambient temperature and altitude | not stated |
| 23 | Flange | square 80, spigot Ø70 × 3, four Ø6.6 holes on Ø90 (Dimensions) |
| 24 | Shaft | Ø19 × 35, plain (no key) |
| 25 | Length | 210 (35 shaft + 175 flange face to the encoder cover's end) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical and mechanical ones the checks may read (status "generic design", source "IEC 60034-1 value"); `pins.csv` gives each contact its role.

## Dimensions
| item | value | source |
|---|---|---|
| flange | 80.0 × 10.0 × 80.0 (x ±40, y 0 … 10, z ±40), mounting face y 0 | design choice (lib/inventory.csv: the flange a design choice) |
| flange holes | four Ø6.6 through the flange on a Ø90 pitch circle at 45° (x, z = ±31.82); position Ø0.5 to A (mounting face), B (spigot axis), C (upper-right hole) | ISO 273 medium clearance for M6 (lib/standards/holes.csv); pattern and tolerance design choices; Ø0.5 ≤ H − F = 6.6 − 6.0 (GDT-010, features.csv) |
| spigot | Ø70 × 3.0 proud of the mounting face (y −3 … 0); its fit tolerance NOT ON FILE (B): IEC 60072-1 | size a design choice: it locates the motor in the machine's bore; the tolerance a standard tabulates for the flange size (a document wanted, lib/standards/wanted.md) |
| shaft | Ø19, plain, 35 out from the mounting face (y −3 … −35 beyond the spigot); its fit tolerance NOT ON FILE (B): IEC 60072-1 | size a design choice (lib/inventory.csv: the shaft a design choice); the tolerance as the spigot's; no key or keyway (a keyed shaft needs DIN 6885-1, which lib/standards/sources.csv does not list, so this version claims none) |
| housing | 76.0 × 130.0 × 76.0 (x, z ±38, y 10 … 140), its four long corners relieved to ±24 the full length (a cross section: a centre part x ±38, z ±24 and two slabs x ±24, z ±24 … ±38), so each flange hole has 7.82 clear to the housing in x and z behind the flange for an M6 screw head or nut (design: a head or a nut across its corners up to Ø12 turns in the 7.82 relief, a design allowance; the screw-head and nut standards are not on file) | design choice (1.1: review servo-motor-1.0 finding 1; 1.2: review elec-r47 finding 2, the allowance named with no standard) |
| encoder cover | 70.0 × 35.0 × 70.0 (x, z ±35, y 140 … 175) | design choice |
| connector bosses | two, 30 × 30 × 10 on the housing's top (z 38 … 48), centred x 0 at y 118 (power) and y 82 (encoder) | design choice |
| connector seats | Ø23 × 8 on each boss (z 48 … 56): `port-pwr` and `port-enc`; the face receptacle-m23 sits on at a later version | design choice (Notes) |
| rating-plate field | 0.6 × 60 × 40 on the housing's +x side (x 38 … 38.6, y 40 … 100, z −20 … 20) | design choice |
| overall | 80.0 × 210.0 (y −35 … 175) × 96.0 (z −40 … 56) | from the parts above |

## Named nodes
`shaft` (rotate 0 … 360° about the y axis, at the spigot's face) · ports `port-pwr` (unit m23-power: U V W PE) and `port-enc` (unit m23-signal: A+ A− B+ B− 5V 0V), kind port, axis +z, gender none: no contact is modelled on the seats until receptacle-m23 is placed (PIN-002). pins.csv names what each contact carries.

## Materials by layer
`M-ALU-ANOD` flange, spigot, housing and bosses · `M-BLACK-PA` encoder cover and connector seats · `M-ZINC` shaft · `M-WHITE-PA` rating-plate field (the flange holes are cuts, no layer of their own)

## Decals (Blender)
On the rating-plate field: "complexes.org generic", "servo-motor", "3~ 400 V 2.5 A (7.5 A pk)", "1.0 kW 3000 min-1 3.18 N·m", "8 poles · S1 · th. cl. 155", "ENC 2500 ppr 5 V". Beside the seats: "POWER U V W PE" and "ENCODER". The earth symbol beside the power seat. No maker's name, logo or approval mark.

## Notes
- Two lines are open, each class B, a standard's table not on file and asked for once in lib/standards/wanted.md: the spigot's and the shaft's fit tolerances (IEC 60072-1, which tabulates them for a flange motor's frame; the sizes are design choices by EM's inventory line, the tolerances are not). Every rating is a class value (design input), every size a design choice, the holes ISO 273 on file. Nothing is guessed and shown as sourced.
- The standard named in the Baseline, IEC 60034-1, is not in lib/standards/sources.csv: it gives the rotating machine's rating items their names (Class values says which), as OPERATING.md 12 asks for a product class ETIM has no class for; no figure is taken from it. IEC 60034-6 and -7 give only the codes named in items 17 and 18 (lib/needs-em/elec.md r37).
- Not placed in this version, though lib/inventory.csv's made_of names them: receptacle-m23 ×2 and screw-iso4762 ×4 are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). So the connections are two connector seats with their port nodes, gender none, and the flange's holes are clearance holes for the installer's M6 screws. Placing receptacle-m23 on the seats is a later version (its contacts and coding replace the seats' faces: a major).
- The windings' load (resistance, inductance, back-EMF constant) is not a class value here, so behaviour.csv writes no load row (its header); the rotor's running state is a manual toggle, as motor-iec71-370w.
- The motor's protective earth is its housing (an exposed conductive part): the PE contact of port-pwr. Its bonding is the cable's and the panel's (servo-drive 1.1's t-PE-m).
- Not stated or modelled: the stator, rotor, magnets, bearings and encoder disc inside; the shaft's run-out and the flange's perpendicularity; permitted radial and axial shaft loads; the cogging torque; the thermal time constant; the winding's insulation test voltage.
- Not a safety-function device: no brake, no safe torque or safe position function is claimed.
- The folder's earlier stub: references/source.txt keeps its record verbatim as the end block (OPERATING.md 6, DOC-007). The stub's validation.json stays in the folder: removing or moving a tracked file is refused to an unattended run (lib/needs-em/elec.md r47).
- The id: the inventory's row is `servo-motor`; the id convention (OPERATING.md 6) would add the size (servo-motor-1kw, as vfd-0.75kw). The folder `servo-motor-1kw` already holds an acquisition stub, so a rename is the library's to settle on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r37.

## Outputs (out/)
`servo-motor.lsp` · `.glb` (pivots on the shaft and the two ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r37, 1.1 in elec-r47, 1.2 in elec-r53 (lib/rounds/elec/).

## History
| version | change |
|---|---|
| 1.0 | elec-r37 (2026-11-12, unattended): first build, generic (no ETIM class; IEC 60034-1 values), our own design; inventory elec pinned 7; sized for servo-drive 1.1; receptacle-m23 and screw-iso4762 not placed (not built) |
| 1.1 | elec-r47 (2026-11-13, unattended), review servo-motor-1.0 findings 1 to 5 and servo-drive-1.2 finding 2: the housing's corners relieved to ±24 behind the flange holes (finding 1; nodes, origin, holes and overall size unchanged); Class values 2 calls 400 V the supply class and says why it is not the terminal voltage (finding 2; ratings.csv `voltage` the same); the order claim dropped and the items split into the rotating machine's and the servo class's own (finding 3); the spigot's and shaft's fit tolerances class B, IEC 60072-1 (finding 4); references/source.txt keeps the earlier stub's record verbatim as its end block (finding 5, from 2bd1e027); pins.csv port-enc 5V role `load+:5V` (servo-drive-1.2 finding 2) |
| 1.2 | elec-r53 (2026-11-13, unattended): review elec-r47 finding 2 / servo-motor-1.1 (text only, geometry as 1.1): the housing row's relief justified by a design allowance (a head or nut up to Ø12 across its corners), no longer by figures of screw and nut standards not on file |
