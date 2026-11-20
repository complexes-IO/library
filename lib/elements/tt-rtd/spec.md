# tt-rtd · v1.0 · temperature transmitter with a Pt100 probe, 0-200 °C, 4-20 mA two-wire, 24 V DC (complexes.org generic)

**What** Temperature transmitter for a process line or vessel: a Pt100 resistance thermometer at the tip of its probe sits in the medium, and the transmitter in the head sets the current in its two-wire loop from 4 mA at 0 °C to 20 mA at 200 °C, powered by the same loop at 24 V DC. The process temperature reading of the systems the inventory names (lib/inventory.csv row `tt-rtd`: calibration-bench, condition-monitoring-rig, heat-exchanger-loop, iiot-edge-node, oven-cure, powder-coating-system, process-skid, test-bench-hydraulic; 8 systems), an AI 4-20 mA into the PLC as pt 1.0's. A probe sheath, a male NPT 1/4 stub and a hex whose seat face meets the host's port, an extension neck, and pt 1.0's terminal head with two screw clamps behind a front cover and an M20 × 1.5 cable entry in its side. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002919 "Temperature transformer" (synonym "Temperature transmitter"), built to the class values below; no maker's datasheet and no product is matched (lib/inventory.csv row `tt-rtd`, own_design generic).
**Class** device · **Baseline** our own design: generic Temperature transformer (ETIM 10.0 EC002919). The class values are this element's definition (design inputs); the stem meets a host's female NPT 1/4 port as gauge-t 1.2's does (pneu.NPT, calculated from ASME B1.20.1's formulas); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1), as pt 1.0's; the probe, neck and head sizes are design choices, said so below.
**Units / frame** mm, Z up. Origin: the joint plane, the hex's seat face z = 0 on the stem's axis (x = y = 0); the host's port and the probe toward −z, the terminal head up, its front cover toward −y (in a BOM: the host's port node, the stem's axis along the port's).
**Built with** toolkit 1.3 · AutoLISP command `TTRTD` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC002919 Temperature transformer)
ETIM 10.0 EC002919 "Temperature transformer" (lib/standards/etim/classes.csv, group EG020098 Measuring and testing instruments process measurement technology; synonyms "Temperature measuring transducer", "Temperature transducer", "Temperature transmitter"). The class's features are not in the subset on file: lib/standards/etim/class-features.csv has no EC002919 rows (request elec-18 asks the core for them and for the inventory row's etim cell). Until they come, the values this element is designed to, under the names the class's synonyms and the inventory row use, as port-rj45 1.0's; they define the element: design inputs, not open figures (OPERATING.md 12; GEN-010 does not judge a class whose features are not on file, request pneu-4).

| # | feature | value |
|---|---|---|
| 1 | Input (sensor) | Pt100 resistance thermometer in the probe's tip (the inventory row: "temperature transmitter with Pt100 RTD"); its tolerance class and connection not stated (the element inside is not modelled) |
| 2 | Output signal | 4-20 mA, two-wire (the loop carries the supply and the signal) |
| 3 | Electrical connection | screw terminals 1 (+) and 2 (−), cable entry M20 × 1.5 |
| 4 | Supply voltage | 24 V DC (the loop's) |
| 5 | Measuring range | 0 … 200 °C (the cure ovens and the heat-exchanger loop of the inventory's systems inside it) |
| 6 | Accuracy | not stated (the twin reads no measuring error) |
| 7 | With display | no (no local reading) |
| 8 | Process connection | male NPT 1/4 with a 15 mm hex, into a host's port that bores through into the medium |
| 9 | Insertion length | 100 mm below the seat face |
| 10 | Probe diameter | 6 mm |
| 11 | Housing material | stainless steel probe, stem and neck; polyamide terminal head |
| 12 | Degree of protection (IP) | not stated (no cover or entry seal is modelled) |
| 13 | Explosion-proof | no |
| 14 | Height | 176 mm (the probe's tip to the head's top) |
| 15 | Width | 40 mm (the head) |
| 16 | Depth | 36.6 mm (the head with its label field) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the ones the checks may read (status "generic design", source "ETIM 10.0 EC002919 class value"); `pins.csv` gives each terminal its role.

## Output
| temperature at the probe's tip | loop current (1 to 2) |
|---|---|
| 0 °C | 4 mA |
| 0 … 200 °C | 4 mA + 16 mA × t / 200 °C, linear |
| 200 °C | 20 mA |

Two-wire (IEC 60381-1 names the 4-20 mA signal; not on file): terminal 1 takes the loop's +24 V DC, terminal 2 returns the current to the PLC's analogue input (plc-aio's AI+), whose input closes the loop to 0 V. The least voltage the transmitter needs across 1-2 (its lift-off voltage) and the current it signals a fault with are the standard's figures: NOT ON FILE (B): IEC 60381-1, asked for once in lib/standards/wanted.md (pt 1.0's line). The twin reads three states (behaviour.csv): off (no voltage across 1-2), live (the loop powered), and a sensor fault it sets by hand; the electrical solver computes no temperature and no analogue value, so the current between 4 and 20 mA is the circuit model's, and the load row draws the full-scale 0.48 W (20 mA × 24 V, derived from the class values). The Pt100's resistance against temperature is IEC 60751's table, which the twin does not read (the transmitter's output is the signal): the standard is named, not relied on.

## Dimensions
| item | value | source |
|---|---|---|
| probe sheath | Ø6 from the stub's end (0.5 into it) to z = −100; stainless steel | design choice (Class values 9 and 10); holds the Pt100 element at its tip (not modelled); it needs a host whose port bores through into the medium, as gauge-t 1.2's stem |
| NPT 1/4 male stub | Ø13.616 × 10.205 below the seat face (z −10.205 to 0.5), part of `port-1` | pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): Ø = E1 + h, the external thread's major diameter at the hand-tight plane; length L2, the effective thread; drawn plain, as gauge-t 1.2's stub: the 1:16 taper and the thread form are not drawn |
| hex | 15 across flats × 9 (z 0 … 9), corners turned to 1.12 × AF (Ø16.8); part of `port-1` | design choice, gauge-t 1.2's; the flats clear the thread's largest major diameter E2 + h (asserted in element.py) |
| extension neck | Ø12 (z 8.5 … 40.5, 0.5 into the hex and the head) | design choice: keeps the head 31 mm off the hex, away from the process's heat (the head's own temperature limit is not stated) |
| terminal head | 40 × 36 × 36 (x ±20, y ±18, z 40 … 76): bottom plate z 40 … 46, top plate z 70 … 76, side walls 4 (−x) and 8 (+x), back wall y 14 … 18, front cover y −18 … −15; the terminal compartment x −16 … 12, y −15 … 14, z 46 … 70 | design choice, pt 1.0's head raised onto the neck |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis along x at y 0, z 58, through the +x wall (x 12 … 20) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| terminals | two screw clamps on the back wall's front face (y 14): heads Ø4.4 × 1.2, 1 at (x −7, z 58), 2 at (x 3, z 58); conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions a design choice; the marks a design choice (1 loop +, 2 loop −); the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| label field | 0.6 × 24 × 16 on the cover (x ±12, y −18.6 … −18, z 50 … 66) | design choice |
| overall | 40.0 × 36.6 (y −18.6 … 18) × 176.0 (z −100 … 76) | from the parts above |

## Named nodes
`port-1` (the stub and the hex: kind port, fixed, unit "NPT1/4", gender male, role gauge, length 10.205, at the seat face z = 0, axis −z; as gauge-t 1.2's `port-1`) · ports `t-1`, `t-2` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries. Nothing moves.

## Materials by layer
`M-SILVER` stub, hex, probe sheath and neck · `M-ZINC` terminal screw heads · `M-GREY-PA` terminal head (plates, walls, cover) · `M-WHITE-PA` label field (the entry is a cut, no layer of its own)

## Decals (Blender)
On the label field: "complexes.org generic", "tt-rtd", "Pt100 · 0-200 °C · 4-20 mA", "24 V DC · 1 + / 2 −". No maker's name, logo or approval mark.

## Notes
- The screw clamps' conductor range and torque: class B, IEC 60947-1 (Dimensions; behaviour.csv). The loop's lift-off voltage and fault current: class B, IEC 60381-1 (Output), kept under their document as pt 1.1's (review pt-1.0 finding 3 weighed them as design figures): the lift-off voltage is the `live` state's threshold, which the twin reads, and a design value for it is bounded only by what the loop's receiver may drop at 20 mA, which the loop's standard sets. Every rating is a class value (design input); every size a design choice; the stub's figures calculated (pneu.NPT), the entry thread and the load's 0.48 W derived. Nothing is guessed and shown as sourced.
- The host: no element on file has a port that bores through into a medium for a probe (gauge-t 1.2's stem waits on the same); the blind NPT 1/4 bores on file clear only their first 12.2 mm. An assembly that places tt-rtd gives it a through port or a thermowell (a separate element, not built).
- Not a safety-function device: the PLC reads it as a process signal (the HMI's reading, an over-temperature alarm). A temperature limiter in a safety function needs a safety-class element and EM's sign-off.
- Not placed (OPERATING.md 12, quality at the source): the inventory row lists receptacle-m12 as its part; it is not past station 6, so this version is the cable-entry form with screw clamps (as pt 1.0), with no M12 receptacle. A later version may place it (a major: the terminals become the receptacle's contacts). The installer's cable gland in the M20 entry, and the Pt100 element and electronics inside, are not modelled.
- The id: the inventory's row is `tt-rtd`; the id convention (OPERATING.md 6) would name the class, the sensor and the output (temp-transmitter-pt100-4-20ma, or the like). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r54.

## Outputs (out/)
`tt-rtd.lsp` · `.glb` (pivots on port-1 and the two terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r54 (lib/rounds/elec/r54.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r54 (2026-11-13, unattended): first build, generic ETIM 10.0 EC002919, our own design; gauge-t 1.2's stem and pt 1.0's head |
