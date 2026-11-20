# flow-meter · v1.0 · liquid flow meter, in line, NPT 3/8 female × 2, 1-20 l/min, 4-20 mA two-wire, 24 V DC (complexes.org generic)

**What** Flow meter for a liquid line: the liquid passes through the body from `port-1` to `port-2`, and the transmitter in the head sets the current in its two-wire loop from 4 mA at no flow to 20 mA at 20 l/min, powered by the same loop at 24 V DC. The flow reading of the systems the inventory names (lib/inventory.csv row `flow-meter`: calibration-bench, heat-exchanger-loop, process-skid, test-bench-hydraulic, test-bench-pneumatic, test-rig-cylinder; 6 systems), an AI 4-20 mA into the PLC as pt 1.1's and tt-rtd 1.0's. A brass body block with a female NPT 3/8 port in each end face, a neck on its top face, and tt-rtd 1.0's terminal head with two screw clamps behind a front cover and an M20 × 1.5 cable entry in its side. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC010586 "Liquid flow meter", built to the class values below; no maker's datasheet and no product is matched (lib/inventory.csv row `flow-meter`, own_design generic).
**Class** device · **Baseline** our own design: generic Liquid flow meter (ETIM 10.0 EC010586). The class values are this element's definition (design inputs); each port meets a male NPT 3/8 stub as flow-control-inline 1.0's ports meet theirs (pneu.NPT, calculated from ASME B1.20.1's formulas); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1), as pt 1.1's; the body, neck and head sizes are design choices, said so below.
**Units / frame** mm, Z up. Origin: in line, port-1's end face centre on the port axis (port-1's pivot 0.2 out, on its number field); the port axis is the x axis, the flow along +x from port-1 to port-2, the terminal head toward +z, its front cover toward −y.
**Built with** toolkit 1.3 · AutoLISP command `FLOWMETER` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC010586 Liquid flow meter)
ETIM 10.0 EC010586 "Liquid flow meter" (lib/standards/etim/classes.csv, group EG020050 Flow and pressure measurement instruments; synonyms "Flow meter", "Flowmeter", "Liquid flowmeter", "Oil meter", "Water meter"). The class's 22 features (lib/standards/etim/class-features.csv), each with the value this element is designed to, or "not stated"; they define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature | value |
|---|---|---|
| 1 | Housing material (EF001596) | brass |
| 2 | Material quality (EF001257) | not stated (no alloy designation: no material standard for it is on file) |
| 3 | Connection 1 (EF000321) | internal thread NPT (ASME B1.20.1), `port-1`, the inlet |
| 4 | Nominal diameter connection 1 (EF023193) | 3/8 inch |
| 5 | Outer pipe diameter connection 1 (EF020122) | 17.145 mm (the NPT 3/8 pipe's outside diameter D = 0.675 in, toolkit/pneu.py NPT_INPUTS) |
| 6 | Connection 2 (EF000322) | internal thread NPT (ASME B1.20.1), `port-2`, the outlet |
| 7 | Nominal diameter connection 2 (EF020052) | 3/8 inch |
| 8 | Outer pipe diameter connection 2 (EF020123) | 17.145 mm |
| 9 | Flange compression class (EF020149) | not stated (no flange: both connections are threaded) |
| 10 | Article compression class (EF020007) | not stated (the pressure this element is designed to is value 14) |
| 11 | Suitable for oil (EF021672) | yes (a brass body; mineral oil in a line inside value 14, a hydraulic return or drain line) |
| 12 | Continuous volume flow (Q3) (EF014723) | 1.2 m³/h (20 l/min) |
| 13 | Volume flow (EF002464) | 1 … 20 l/min |
| 14 | Max. operating pressure at 20 °C (EF023116) | 1000 kPa |
| 15 | Medium temperature (continuous) (EF023182) | 0 … 60 °C |
| 16 | Working length (EF006318) | 70 mm (end face to end face) |
| 17 | Length of connection 1 (EF020151) | 12.358 mm (the bore's depth, L2 + 2) |
| 18 | Working length connection 1 (EF020153) | 10.329 mm (a male's make-up L1 + L3, pneu.NPT "engagement") |
| 19 | Length of connection 2 (EF020152) | 12.358 mm |
| 20 | Working length connection 2 (EF020154) | 10.329 mm |
| 21 | Diameter (EF000551) | not stated (a block body 32 × 32, not a round one) |
| 22 | With shut-off valve (EF022484) | no |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the ones the checks may read (status "generic design", source "ETIM 10.0 EC010586 class value"). The class has no feature for an electrical output: the transmitter's supply and signal are design figures (Output), in ratings.csv with status "design".

## Output
| flow from port-1 to port-2 | loop current (1 to 2) |
|---|---|
| none | 4 mA |
| 1 … 20 l/min (class value 13) | 4 mA + 16 mA × Q / 20 l/min, linear |
| 20 l/min | 20 mA |

A flow under 1 l/min is below the measuring range: the element claims no reading there. Two-wire (IEC 60381-1 names the 4-20 mA signal; not on file): terminal 1 takes the loop's +24 V DC, terminal 2 returns the current to the PLC's analogue input (plc-aio's AI+), whose input closes the loop to 0 V; a design choice, the form pt 1.1 and tt-rtd 1.0 use, so one analogue input type reads all three. The least voltage the transmitter needs across 1-2 (its lift-off voltage) and the current it signals a fault with are the standard's figures: NOT ON FILE (B): IEC 60381-1, asked for once in lib/standards/wanted.md (pt 1.1's line). The twin reads three states (behaviour.csv): off (no voltage across 1-2), live (the loop powered), and a fault it sets by hand; the electrical solver computes no flow and no analogue value, so the current between 4 and 20 mA is the circuit model's, and the load row draws the full-scale 0.48 W (20 mA × 24 V, derived). The measuring principle is not chosen: the element in the flow and its pick-up are inside and not modelled, and no accuracy is claimed.

## Dimensions
| item | value | source |
|---|---|---|
| body | 70 × 32 × 32 block (x 0 … 70, y ±16, z ±16), brass, centred on the port axis | design choice (Class values 1 and 16); at least 5 of wall round each bore and 10 of body between the bores' floors (asserted in element.py) |
| ports | two, female NPT 3/8, one in each end face on the x axis: a plain bore Ø17.055 × 12.358 deep | pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): Ø = E1 + h, the male's major diameter at the hand-tight plane, so the halves touch; depth L2 + 2, past a male's make-up L1 + L3 = 10.329; drawn plain, as flow-control-inline 1.0's: the 1:16 taper and the thread form are not drawn; features.csv |
| port-number fields | 22 × 22 × 0.2 on each end face, the bore through them (the nodes `port-1`, `port-2`) | design choice, flow-control-inline 1.0's |
| flow-arrow field | 30 × 10 × 0.2 on the body's front face (x 20 … 50, y −16.2 … −16, z ±5) | design choice |
| neck | Ø12 on the body's top face at x 35 (z 15.5 … 40.5, 0.5 into the body and the head) | design choice: holds the head 24 mm above the body, clear of a wrench on the line's fittings |
| terminal head | 40 × 36 × 36 (x 15 … 55, y ±18, z 40 … 76): bottom plate z 40 … 46, top plate z 70 … 76, side walls 4 (−x) and 8 (+x), back wall y 14 … 18, front cover y −18 … −15; the terminal compartment x 19 … 47, y −15 … 14, z 46 … 70 | design choice, tt-rtd 1.0's head |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis along x at y 0, z 58, through the +x wall (x 47 … 55) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| terminals | two screw clamps on the back wall's front face (y 14): heads Ø4.4 × 1.2, 1 at (x 28, z 58), 2 at (x 38, z 58); conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions a design choice; the marks a design choice (1 loop +, 2 loop −); the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| label field | 0.6 × 24 × 16 on the cover (x 23 … 47, y −18.6 … −18, z 50 … 66) | design choice |
| overall | 70.4 (x −0.2 … 70.2) × 36.6 (y −18.6 … 18) × 92.0 (z −16 … 76) | from the parts above |

## Named nodes
`port-1`, `port-2` (the number fields: kind port, fixed, unit "NPT3/8", gender female, role work, each on its field's outer face, axis out of the body; as flow-control-inline 1.0's) · ports `t-1`, `t-2` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries. Nothing moves.

## Materials by layer
`M-BRASS` body · `M-SILVER` neck · `M-ZINC` terminal screw heads · `M-GREY-PA` terminal head (plates, walls, cover) · `M-WHITE-PA` port-number fields, flow-arrow field, label field (the bores and the entry are cuts, no layer of their own)

## Decals (Blender)
On the label field: "complexes.org generic", "flow-meter", "1-20 l/min · 4-20 mA", "24 V DC · 1 + / 2 −". On the port-number fields: "1", "2". On the flow-arrow field: an arrow from 1 to 2. No maker's name, logo or approval mark.

## Notes
- The screw clamps' conductor range and torque: class B, IEC 60947-1 (Dimensions; behaviour.csv). The loop's lift-off voltage and fault current: class B, IEC 60381-1 (Output), kept under their document as pt 1.1's and tt-rtd 1.0's. Every class figure is a class value (design input); the loop's 24 V DC and 4-20 mA are design figures, said so; every size a design choice; the bores' figures calculated (pneu.NPT), the entry thread and the load's 0.48 W derived. Nothing is guessed and shown as sourced.
- The ports are in the pneumatic series' thread (toolkit/pneu.py THREADS: NPT 1/8, 1/4, 3/8), the only pipe thread on file with its figures, so the PNE checks read a joint made onto them as one of that series; their role is "work" on both, as flow-control-inline 1.0's. A hydraulic pressure line (hyd-port, ISO 6149; hpu-7.5kw's working pressure is far above value 14) does not take this element: in the hydraulic test bench it belongs in a return, drain or cooling-water line inside 1000 kPa. A form with ISO 6149 ports for the pressure line would be its own element or a later major; none is built or claimed here.
- The passage through the body between the two bores, the measuring element in it and the electronics are not modelled; the twin reads the loop only.
- Not a safety-function device: the PLC reads it as a process signal (the HMI's reading, a low-flow alarm). A flow monitor in a safety function needs a safety-class element and EM's sign-off.
- Not placed (OPERATING.md 12, quality at the source): the inventory row lists no part. The installer's cable gland in the M20 entry and the line's fittings (fitting-pushin, or a pipe nipple) are an assembly's to place.
- The id: the inventory's row is `flow-meter`; the id convention (OPERATING.md 6) would also name the size and the output (flow-meter-npt38-4-20ma, or the like). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r56.

## Outputs (out/)
`flow-meter.lsp` · `.glb` (pivots on the two line ports and the two terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r56 (lib/rounds/elec/r56.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r56 (2026-11-20, unattended): first build, generic ETIM 10.0 EC010586, our own design; flow-control-inline 1.0's line ports at NPT 3/8 and tt-rtd 1.0's head |
