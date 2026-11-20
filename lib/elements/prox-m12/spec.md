# prox-m12 · v1.0 · inductive proximity sensor, M12 × 1 barrel, flush, 2 mm, PNP N.O., 24 V DC (complexes.org generic)

**What** Inductive proximity sensor for a "part present" or "end position" signal on a metal target: a coil behind the plastic sensing face of an M12 × 1 threaded barrel sets up a field in front of the face, and a metal target within 2 mm of it damps the field enough to switch the output. One PNP output, normally open (on while a metal target is within the switching distance), fed 24 V DC, so a PLC's 24 V DC input reads it. Flush (embeddable) mounting: the sensing face is level with the barrel's end, so the barrel may sit in metal up to its face. The barrel goes through a Ø12 bracket hole and is held by two lock nuts, one each side; the cable plugs onto an axial M12 connector at the back, and a yellow LED ring on the rear cap shows the output. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002714 "Inductive proximity switch", built to the class values below; no maker's datasheet (the folder's earlier stub is reference only and was not used: references/source.txt). photoeye-m18 1.0's pattern at M12.
**Class** device · **Baseline** our own design: generic Inductive proximity switch (ETIM 10.0 EC002714). The class values are this element's definition (design inputs); the barrel's thread M12 × 1 is derived (ISO 68-1 / ISO 965-1 6g); every other size is a design choice, said so below.
**Units / frame** mm, Z up. Origin: the sensing face y = 0 on the barrel's axis x = 0, z = 0; the sensing direction toward −y, the barrel toward +y (in a BOM, the barrel's axis on the bracket hole's, the nuts either side of the bracket).
**Built with** toolkit 1.3 · AutoLISP command `PROXM12` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC002714 Inductive proximity switch)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Width sensor (EF007094) | not stated (a cylinder: its diameter is feature 4) |
| 2 | Height of sensor (EF007283) | not stated (a cylinder: its diameter is feature 4) |
| 3 | Length of sensor (EF007334) | 53 mm (the sensing face to the connector seat's face) |
| 4 | Diameter sensor (EF007111) | 12 mm (M12 × 1) |
| 5 | Mechanical mounting condition for sensor (EF004041) | flush (embeddable): the sensing face level with the barrel's end |
| 6 | Switching distance (EF003647) | 2 mm on a steel target (the test target not stated) |
| 7 | Suitable for safety functions (EF001597) | no |
| 8 | Type of switch function (EF003963) | normally open (on while a metal target is within the switching distance) |
| 9 | Type of switching output (EF003962) | PNP |
| 10 | Type of electric connection (EF003961) | connector M12, axial (receptacle-m12 placed at a later version: Notes) |
| 11 | Number of semiconductor outputs with signalling function (EF003945) | 1 |
| 12 | Number of contact energized outputs with signalling function (EF003946) | 0 |
| 13 | Number of protected semiconductor outputs (EF003951) | 1 (the output Q, short-circuit protected) |
| 14 | Number of protected contact energized outputs (EF003952) | 0 |
| 15 | Type of actuation (EF006949) | a metal target (inductive) |
| 16 | Type of interface (EF006977) | none (a switching output) |
| 17 | Type of interface for safety communication (EF003956) | none |
| 18 | Construction type housing (EF004008) | cylindrical, threaded M12 × 1 |
| 19 | Coating housing (EF001601) | nickel-plated (the barrel) |
| 20 | Cascadable (EF000507) | no |
| 21 | SIL according to IEC 61508 (EF009889) | none |
| 22 | Performance level according to EN ISO 13849-1 (EF007399) | none |
| 23 | Max. output current at protected output (EF004035) | 100 mA |
| 24 | Supply voltage (EF004127) | 24 V DC (its tolerance band not stated: Notes) |
| 25 | Rated control supply voltage AC 50 Hz (EF003978) | none (DC only) |
| 26 | Rated control supply voltage AC 60 Hz (EF003979) | none (DC only) |
| 27 | Rated control supply voltage DC (EF003980) | 24 V (the PLC's 24 V DC inputs it feeds) |
| 28 | Voltage type (EF000187) | DC |
| 29 | Switching frequency (EF003587) | not stated (the twin switches the output at once) |
| 30 | With monitoring function downstream switching devices (EF004052) | no |
| 31 | Housing material (EF001596) | brass, nickel-plated (the barrel); plastic (the sensing face and the rear cap) |
| 32 | Compression-resistant (EF007106) | no |
| 33 | Explosion safety category for gas (EF003997) | none (no explosion protection claimed) |
| 34 | Explosion safety category for dust (EF003998) | none (no explosion protection claimed) |
| 35 | Interference resistance to magnetic fields (EF008275) | not stated |
| 36 | Degree of protection (NEMA) (EF011959) | not stated |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. The output's 100 mA is the class value of feature 23 (the one output is the protected one, feature 13), as photoeye-m18's. The supply current and the switching frequency are not stated, and the twin reads neither. `pins.csv` gives each pin its role; ratings.csv carries the supply voltage, the output current and the switching distance.

## Output
| state | what it gives | twin |
|---|---|---|
| off | no voltage across +V and 0V: Q off | default |
| powered, no target | the field set up; Q off (open), the LED ring dark | read: powered while +V is above 0V (behaviour.csv) |
| powered, target detected | Q switched to +V (PNP, normally open), the yellow LED ring on | the twin places the target (manual toggle): the phase-1 solver traces no field. The output switch's voltage drop is not stated, so Q is taken at the supply's level |

## Dimensions
| item | value | source |
|---|---|---|
| sensing face | Ø11.974 × 1.5 (y 0 … 1.5), plastic, level with the barrel (flush) | design choice (at the barrel's diameter: an embeddable sensor's face does not stand proud) |
| barrel | Ø11.974 × 40.0 (y 1.5 … 41.5) | thread M12 × 1 derived: derive.thread(12.0, 1.0) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6g d 11.7972 … 11.974), modelled plain at d max; the length a design choice |
| rear cap | Ø11.974, plastic, in two parts y 41.5 … 44.5 and 46.0 … 49.0 | design choice (at the barrel's diameter, so both lock nuts thread on from the front) |
| LED ring | Ø11.974 × 1.5 (y 44.5 … 46.0) between the rear cap's two parts, yellow, node `led-out` | design choice (seen from every side, as the cap is round) |
| connector seat | Ø10.0 × 4.0 (y 49 … 53), the face receptacle-m12 sits on; port node `port-x1` on its face | design choice (inside the M12 × 1 thread's minor diameter 10.9175); the receptacle and its fixing are receptacle-m12's (Notes) |
| overall | 11.974 × 53.0 × 11.974 (x ±5.987, y 0 … 53, z ±5.987) | from the parts above |

## Named nodes
Port `port-x1` (kind port, unit m12-a, gender none: no contact is modelled until receptacle-m12 is placed on the seat, PIN-002) · `led-out` (emissive, yellow: the output on). pins.csv names the three signals the connector carries; which M12 contact carries which is receptacle-m12's and the cordset's, set when it is placed. Nothing moves.

## Materials by layer
`M-ORANGE-PA` sensing face · `M-SILVER` barrel · `M-BLACK-PA` rear cap and connector seat · `M-LENS-YELLOW` the LED ring

## Decals (Blender)
None: the barrel carries no flat field for a legend (a design choice). No maker's name, logo or approval mark.

## Notes
- One open line, class B, a standard's table not on file and asked for once in lib/standards/wanted.md: the least supply voltage at which the output is valid (the IEC 61131-2 24 V DC class's lower limit, which behaviour.csv's `powered` row reads as "above 0"): NOT ON FILE (B): IEC 61131-2. Every rating is a class value (design input) or a design figure, every size a design choice, the barrel's thread derived. Nothing is guessed and shown as sourced.
- Not a safety-function device (Class values 7, 21, 22): a safety position switch is a safety-class element with EM's sign-off.
- Not placed (OPERATING.md 12, quality at the source): receptacle-m12 (built, not yet past station 6), so the connection is a seat with its port node, as photoeye-m18 1.0; nut-m12-lock x2 (not built; a nut's shape is its standard's, never generic), so the barrel is plain for the installer's nuts; led (not built), so the LED ring is drawn here. Nothing is modelled that a later element will place.
- The folder's earlier stub: references/source.txt keeps its record verbatim as the end block (its earlier source.txt and metadata.json; OPERATING.md 6, DOC-007). The stub's validation.json stays in the folder: removing or moving a tracked file is refused to an unattended run (lib/needs-em/elec.md r47, r50, r53).
- The id: the inventory's row is `prox-m12`; the id convention (OPERATING.md 6) gives `prox-ind-m12-pnp-no`. A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r53.

## Outputs (out/)
`prox-m12.lsp` · `.glb` (a port pivot on the connector seat, an emissive LED pivot, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r53 (lib/rounds/elec/r53.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r53 (2026-11-13, unattended): first build, generic ETIM 10.0 EC002714, our own design; inventory elec prox-m12 (9 systems) |
