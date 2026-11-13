# encoder · v1.0 · rotary encoder, incremental, optical, 1024 ppr, push-pull HTL, 24 V DC, size 58, solid shaft 10 (complexes.org generic)

**What** Incremental rotary encoder for a machine axis whose position or speed a controller counts (a servo axis, a rotary index table, a positioner, a press brake's back gauge): an optical code disc on a solid Ø10 shaft gives 1024 pulses per revolution on two channels A and B, a quarter period apart (the direction from which leads), and one zero pulse N per revolution, as push-pull (HTL) outputs at the supply's level, fed 24 V DC, so a PLC's 24 V DC fast inputs count them. Construction size 58: an aluminium housing Ø58 × 42 whose front face is the mounting face, with a Ø36 spigot and three M4 tapped holes; the shaft is coupled to the machine's shaft by the installer's coupling; the cable plugs onto an axial M12 connector at the back. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001486 "Rotary encoder", built to the class values below; no maker's datasheet (the folder's earlier stub is reference only and was not used: references/source.txt).
**Class** device · **Baseline** our own design: generic Rotary encoder (ETIM 10.0 EC001486). The class values are this element's definition (design inputs); the mounting holes are M4 × 0.7 tapped, their minor diameter derived (ISO 68-1 / ISO 965-1); the housing, spigot, shaft and every other size are design choices, said so below.
**Units / frame** mm, Z up. Origin: the housing's front (mounting) face y = 0, shaft axis x = 0, z = 0, shaft toward −y, housing toward +y (in a BOM, the mounting face on the host's bracket, the shaft into the coupling).
**Built with** toolkit 1.3 · AutoLISP command `ENCODER` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC001486 Rotary encoder)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Model (EF000010) | incremental encoder |
| 2 | Physical measurement principle (EF008238) | optical (a slotted code disc between an LED and photodiodes) |
| 3 | Max. pulses per revolution (EF003589) | 1024 |
| 4 | Signal outputs of rotary encoder (EF003590) | push-pull (HTL): A, B (90° apart) and the zero pulse N, at the supply's level; no complement channels |
| 5 | Type of shaft encoder (EF006968) | solid shaft |
| 6 | Type of electric connection (EF003961) | connector M12, axial (receptacle-m12 placed at a later version: Notes) |
| 7 | Construction size (EF012282) | 58 mm |
| 8 | Explosion safety category for gas (EF003997) | none (no explosion protection claimed) |
| 9 | Explosion safety category for dust (EF003998) | none (no explosion protection claimed) |
| 10 | Standard for interfaces (EF004017) | not stated (push-pull pulse outputs, no fieldbus or serial interface) |
| 11 | Number of revolutions (EF006943) | not stated (incremental: no revolution count is kept) |
| 12 | Number of steps per revolution (EF006938) | 1024 (4096 edges counted in quadrature) |
| 13 | Impulse rate per cycle (EF007289) | 1024 per revolution on A and B; 1 on N |
| 14 | Diameter axle (EF007110) | 10 mm |
| 15 | Programmable (EF000841) | no |
| 16 | Type of transmission medium (EF007513) | electrical (copper conductors) |
| 17 | Housing material (EF001596) | aluminium |
| 18 | Degree of protection (IP) (EF005474) | not stated (no shaft seal or connector seal is modelled) |
| 19 | Degree of protection (NEMA) (EF011959) | not stated |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. The class has no supply-voltage feature: the 24 V DC supply is a design choice (ratings.csv `u_supply`, status "design", bounded by IEC 61131-2's 24 V DC class, the PLC inputs the outputs feed). The supply current, the highest output frequency, the highest shaft speed and the shaft's permitted loads are not stated, and the twin reads none of them. `pins.csv` gives each signal its role.

## Signals
| channel | what it gives | twin |
|---|---|---|
| A, B | 1024 pulses per revolution each, a quarter period apart: A leads B turning one way, B leads A the other | not solved: the phase-1 solver is electrical and counts no pulses (behaviour.csv) |
| N | one pulse per revolution, the reference mark | as A, B |
| +V, 0V | the 24 V DC supply | read: the electronics are powered while +V is above 0V (behaviour.csv) |

## Dimensions
| item | value | source |
|---|---|---|
| housing | Ø58.0 × 42.0 (y 0 … 42), the front face y 0 the mounting face | design choice (construction size 58: Class values 7) |
| mounting holes | three M4 × 0.7 tapped, 6.0 deep from the mounting face, on a Ø48 pitch circle at 90°, 210° and 330° (one on top, +z), modelled plain at D1 Ø3.242 | thread derived: derive.thread(4.0, 0.7) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 3.2422 … 3.4224); depth and pitch circle a design choice; features.csv |
| spigot | Ø36.0, 3.0 proud of the mounting face (y −3 … 0); its fit tolerance NOT ON FILE (B): ISO 286-2 | size a design choice; the fit a standard's table not on file (lib/standards/wanted.md) |
| shaft | solid, Ø10.0, 20.0 out from the mounting face (y −3 … −20 beyond the spigot), plain (no flat, no key); its fit tolerance NOT ON FILE (B): ISO 286-2 | size a design choice (Class values 14); the fit as the spigot's |
| connector boss | Ø20.0 × 6.0 on the back face (y 42 … 48) | design choice |
| connector seat | Ø16.0 × 4.0 (y 48 … 52), the face receptacle-m12 sits on; port node `port-x1` on its face | design choice; the receptacle and its fixing are receptacle-m12's (Notes) |
| label field | 24.0 × 11.0 × 0.6 on the back face below the boss (x ±12, z −24 … −13, y 42 … 42.6) | design choice |
| overall | 58.0 × 72.0 × 58.0 (x ±29, y −20 … 52, z ±29) | from the parts above |

## Named nodes
`shaft` (rotate 0 … 360° about the y axis at the spigot's face, (0, −3, 0)) · port `port-x1` (kind port, unit m12-a, gender none: no contact is modelled until receptacle-m12 is placed on the seat, PIN-002). pins.csv names the signals the connector carries; which M12 contact carries which signal is receptacle-m12's and the cordset's, set when it is placed.

## Materials by layer
`M-ALU-ANOD` housing and spigot · `M-ZINC` shaft · `M-BLACK-PA` connector boss and seat · `M-WHITE-PA` label field (the tapped holes are cuts, no layer of their own)

## Decals (Blender)
On the label field: "complexes.org generic", "encoder", "1024 ppr HTL", "24 V DC". No maker's name, logo or approval mark.

## Notes
- Open lines, each class B, a standard's table not on file and asked for once in lib/standards/wanted.md: the shaft's and the spigot's fit tolerances (ISO 286-2), and the supply's least voltage at which the outputs are valid (the IEC 61131-2 24 V DC class's lower limit, which behaviour.csv's `powered` row reads as "above 0"): NOT ON FILE (B): IEC 61131-2. Every rating is a class value (design input) or a design choice bounded by a rule, every size a design choice, the hole thread derived. Nothing is guessed and shown as sourced.
- Not a safety-function device: no safe speed or position monitoring is claimed (an encoder in a safety function needs a safety-class element and EM's sign-off).
- Not placed (OPERATING.md 12, quality at the source): receptacle-m12 (built, not yet past station 6), so the connection is a seat with its port node, as servo-motor's for receptacle-m23; coupling-shaft and screw-iso4762 x3 (not built), so the shaft is plain and the holes bare. Nothing is modelled that a later element will place.
- The folder's earlier stub: references/source.txt keeps its record verbatim as the end block (OPERATING.md 6, DOC-007; reviews servo-motor-1.0 finding 5, hmi-7in-1.0 finding 2). The stub's validation.json stays in the folder: removing or moving a tracked file is refused to an unattended run (lib/needs-em/elec.md r47).
- The id: the inventory's row is `encoder`; the id convention (OPERATING.md 6) would add the form, size and output (encoder-inc-58-htl). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r47.

## Outputs (out/)
`encoder.lsp` · `.glb` (pivots on the shaft and the connector seat, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r47 (lib/rounds/elec/r47.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r47 (2026-11-13, unattended): first build, generic ETIM 10.0 EC001486, our own design; inventory elec encoder (11 systems) |
