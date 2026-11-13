# pt · v1.0 · pressure transmitter for hydraulic oil, 0-250 bar, 4-20 mA two-wire, 24 V DC (complexes.org generic)

**What** Pressure transmitter for a hydraulic line: oil at the stem's port loads a sensing cell, and the transmitter sets the current in its two-wire loop from 4 mA at 0 bar to 20 mA at 250 bar, powered by the same loop at 24 V DC. The press-hydraulic machine's pressure reading (lib/assemblies/press-hydraulic/controls.csv row pressure: "pt 0-250 bar (two-wire, loop powered from the panel's 24 V)", an AI 4-20 mA into the PLC for the HMI's reading and the over-pressure alarm; circuits.csv row machine.pt1; hydraulic.csv: it tees off the P line at the HPU's gauge port, beside the gauge and the pressure switch). A hex stem whose seat face meets the host's gauge port, a round sensor body, and a terminal head with two screw clamps behind a front cover and an M20 × 1.5 cable entry in its side. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC011478 "Pressure transmitter", built to the class values below; no maker's datasheet and no product is matched (lib/inventory.csv row `pt`, own_design generic, pin 11).
**Class** device · **Baseline** our own design: generic Pressure transmitter (ETIM 10.0 EC011478). The class values are this element's definition (design inputs); the stem meets a host's gauge port as hyd-gauge 1.1's and pressure-switch 1.0's do (unit "hyd-port", its thread open, Notes); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1), as pressure-switch 1.0's; the body and head sizes are design choices, said so below.
**Units / frame** mm, Z up. Origin: the joint plane, the hex's seat face z = 0 on the stem's axis (x = y = 0); the host's port toward −z, the terminal head up, its front cover toward −y (in a BOM: the host's gauge port node, the stem's axis along the port's).
**Built with** toolkit 1.3 · AutoLISP command `PTRANS` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC011478 Pressure transmitter)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Output signal (EF000506) | 4-20 mA, two-wire (the loop carries the supply and the signal) |
| 2 | Electrical connection (EF003701) | screw terminals 1 (+) and 2 (−), cable entry M20 × 1.5 |
| 3 | Supply voltage (EF000104) | 24 V DC (the loop's) |
| 4 | Feed pressure (EF020276) | not stated |
| 5 | Measuring range (EF001836) | 0 … 25 MPa (0 … 250 bar), gauge pressure (press-hydraulic controls.csv: 0-250 bar) |
| 6 | Accuracy class (EF001532) | not stated (the twin reads no measuring error) |
| 7 | With temperature sensor (EF006034) | no |
| 8 | Medium temperature (continuous) (EF023182) | −20 … +80 °C (hydraulic mineral oil, as press-hydraulic's HM 46 and pressure-switch 1.0) |
| 9 | Readable (EF024476) | no (no local reading) |
| 10 | With display (EF000458) | no |
| 11 | Max. overpressure (EF022533) | not stated |
| 12 | Suitable for air (EF021466) | not stated |
| 13 | Suitable for water (EF020334) | not stated |
| 14 | Suitable for gases (EF007249) | not stated |
| 15 | Suitable for glycol (EF002310) | not stated |
| 16 | Suitable for oil (EF021672) | yes (hydraulic mineral oil) |
| 17 | Suitable for ammonia (EF021671) | not stated |
| 18 | Suitable for steam (EF020335) | not stated |
| 19 | Housing material (EF001596) | steel stem and body, polyamide terminal head |
| 20 | Degree of protection (IP) (EF005474) | not stated (no cover or entry seal is modelled) |
| 21 | Explosion-proof (EF004663) | no |
| 22 | Connection (EF000443) | male stem with a hex, into a host's gauge port |
| 23 | Thread size (EF022694) | not stated (open: Notes) |
| 24 | Flange compression class (EF020149) | not stated (no flange) |
| 25 | Measuring element (EF021417) | not stated (the cell inside is not modelled) |
| 26 | Height (EF000040) | 96 mm (seat face to the head's top) |
| 27 | Width (EF000008) | 40 mm (the head) |
| 28 | Depth (EF000049) | 36.6 mm (the head with its label field) |
| 29 | Cable length (EF000536) | not stated (no cable: a cable entry) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the ones the checks may read (status "generic design", source "ETIM 10.0 EC011478 class value"); `pins.csv` gives each terminal its role.

## Output
| pressure at port-p | loop current (1 to 2) |
|---|---|
| 0 bar | 4 mA |
| 0 … 250 bar | 4 mA + 16 mA × p / 250 bar, linear |
| 250 bar | 20 mA |

Two-wire (IEC 60381-1 names the 4-20 mA signal; not on file): terminal 1 takes the loop's +24 V DC, terminal 2 returns the current to the PLC's analogue input (plc-aio's AI+), whose input closes the loop to 0 V. The least voltage the transmitter needs across 1-2 (its lift-off voltage) and the current it signals a fault with are the standard's figures: NOT ON FILE (B): IEC 60381-1, asked for once in lib/standards/wanted.md. The twin reads three states (behaviour.csv): off (no voltage across 1-2), live (the loop powered), and a sensor fault it sets by hand; the electrical solver computes no pressure and no analogue value, so the current between 4 and 20 mA is the circuit model's, and the load row draws the full-scale 0.48 W (20 mA × 24 V, derived from the class values).

## Dimensions
| item | value | source |
|---|---|---|
| hex | 15 across flats × 9 (z 0 … 9), corners turned to 1.12 × AF (Ø16.8); zinc-plated steel; the node `port-p` | design choice, hyd-gauge 1.1's and pressure-switch 1.0's; Ø16.8 sits inside the Ø24 spot face of hpu-7.5kw's and hyd-cylinder-da-40's ports (asserted in element.py) |
| stem below the seat face | not drawn (Notes) | its thread and length are open, as hyd-gauge 1.1's |
| neck | Ø12 (z 8.5 … 13.5) | design choice |
| sensor body | Ø27 (z 13 … 60.5, 0.5 into the head) | design choice; the sensing cell and electronics inside are not modelled |
| terminal head | 40 × 36 × 36 (x ±20, y ±18, z 60 … 96): bottom plate z 60 … 66, top plate z 90 … 96, side walls 4 (−x) and 8 (+x), back wall y 14 … 18, front cover y −18 … −15; the terminal compartment x −16 … 12, y −15 … 14, z 66 … 90 | design choice, pressure-switch 1.0's head made smaller (two terminals, no setting screw) |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis along x at y 0, z 78, through the +x wall (x 12 … 20) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| terminals | two screw clamps on the back wall's front face (y 14): heads Ø4.4 × 1.2, 1 at (x −7, z 78), 2 at (x 3, z 78); conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions a design choice; the marks a design choice (1 loop +, 2 loop −); the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| label field | 0.6 × 24 × 16 on the cover (x ±12, y −18.6 … −18, z 70 … 86) | design choice |
| overall | 40.0 × 36.6 (y −18.6 … 18) × 96.0 (z 0 … 96) | from the parts above |

## Named nodes
`port-p` (the hex: kind port, fixed, unit "hyd-port", gender male, role gauge, at the seat face z = 0, axis −z; as hyd-gauge 1.1's `port-1` and pressure-switch 1.0's `port-p`, the host's gauge port `port-g` female) · ports `t-1`, `t-2` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries. Nothing moves.

## Materials by layer
`M-ZINC` hex and terminal screw heads · `M-SILVER` neck and sensor body · `M-GREY-PA` terminal head (plates, walls, cover) · `M-WHITE-PA` label field (the entry is a cut, no layer of its own)

## Decals (Blender)
On the label field: "complexes.org generic", "pt", "0-250 bar · 4-20 mA", "24 V DC · 1 + / 2 −". No maker's name, logo or approval mark.

## Notes
- The stem's thread, size and length: NOT ON FILE (B): no hydraulic port standard, such as an ISO 6149 or SAE straight-thread port, is in lib/standards/sources.csv (as hyd-gauge 1.1's, pressure-switch 1.0's and hpu-7.5kw's ports), asked for once in lib/standards/wanted.md. No stub is drawn below the seat face; the seat face meets the host's port face to face. A major adds the stub once the standard is on file.
- The screw clamps' conductor range and torque: class B, IEC 60947-1 (Dimensions; behaviour.csv). The loop's lift-off voltage and fault current: class B, IEC 60381-1 (Output). Every rating is a class value (design input); every size a design choice; the entry thread and the load's 0.48 W derived. Nothing is guessed and shown as sourced.
- Not a safety-function device: the PLC reads it as a process signal (the HMI's reading, an over-pressure alarm). A pressure monitor in a safety function needs a safety-class element and EM's sign-off.
- Not placed (OPERATING.md 12, quality at the source): the inventory row lists receptacle-m12 as its part; it is not past station 6, so this version is the cable-entry form with screw clamps (as pressure-switch 1.0), with no M12 receptacle. A later version may place it (a major: the terminals become the receptacle's contacts). The installer's cable gland in the M20 entry, and the sensing cell and electronics inside, are not modelled.
- The id: the inventory's row is `pt`; the id convention (OPERATING.md 6) would name the class, the medium and the output (pressure-transmitter-hyd-4-20ma, or the like). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r43.

## Outputs (out/)
`pt.lsp` · `.glb` (pivots on port-p and the two terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r43 (lib/rounds/elec/r43.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r43 (2026-11-12, unattended): first build, generic ETIM 10.0 EC011478, our own design; inventory elec pinned 11 |
