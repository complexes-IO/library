# capacitor-run · v1.1 · motor-run capacitor 10 µF 450 V AC, cylindrical, screw terminals, strap bracket (complexes.org generic)

**What** Motor-run capacitor for a single-phase motor's auxiliary winding (or a three-phase motor run on one phase): one 10 µF section rated 450 V AC in a cylindrical can Ø45 × 95, two screw terminals on its cap with a barrier between them, held to the back panel by a strap round the can whose foot takes two M5 panel screws. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001516, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Capacitor (ETIM 10.0 EC001516). The class values are this element's definition (design inputs); the two panel-screw holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); their pattern, and every other size, is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: surface-mount device: the back face (the strap's foot) on the panel y = 0, the left mounting hole x = 0, z = 0, body toward −y; the can stands on its axis along z, terminals up.
**Built with** toolkit 1.3 · AutoLISP command `CAPRUN` · no parameters.

## Class values
ETIM 10.0 EC001516 "Capacitor", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Capacity (EF000364) | 10 µF |
| 2 | Capacity 2 (EF012194) | not stated (one section) |
| 3 | Nominal voltage (EF005127) | 450 V AC |
| 4 | Model (EF000010) | motor-run capacitor: cylindrical can, strap-bracket mounting, two screw terminals |
| 5 | With insert contacts (EF003783) | no (screw terminals) |
| 6 | Diameter (EF000551) | 45 mm (the can) |
| 7 | Length (EF001438) | 109.5 mm overall along the axis (the can 95.0, its cap 3.0, the barrier 11.5 above the cap) |
| 8 | Width (EF000008) | 80 mm (the strap's foot) |
| 9 | Depth (EF000049) | 50 mm (the panel face to the strap's front) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design", source "ETIM 10.0 EC001516 class value" with the feature code, OPERATING.md 12), with the current the capacitor draws at its nominal voltage (derived: 2π f C U, 1.70 A at 60 Hz, 1.41 A at 50 Hz); `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| can | Ø45.0 × 95.0, its axis at x 32.0, y −26.0, centred on the strap in z (z −47.5 … 47.5) | design choice (Class values 6) |
| strap | ring Ø48.0 outside, 16.0 high (z −8 … 8), 1.5 sheet, its bore Ø45.0 line on line with the can (features.csv: can seat); it touches the foot's face along one line | design choice |
| foot | 80.0 (x −8 … 72) × 16.0 (z −8 … 8) × 2.0 sheet on the panel (y −2 … 0) | design choice (Class values 8) |
| panel-screw holes | two Ø5.5 through the foot at x 0 and 64.0, z 0; position Ø0.4 (features.csv), ≤ H − F = 0.5 for a floating M5 | Ø5.5: ISO 273 medium for M5 (lib/standards/holes.csv); the pattern and its tolerance are design choices |
| terminal cap | Ø41.0 × 3.0 on the can's top (z 47.5 … 50.5) | design choice |
| terminals | two screw-clamp blocks 12.0 × 12.0 × 9.0 on the cap, centred 10.0 either side of the axis (x 22.0 and 42.0); screw heads Ø4.4 × 1.2 on top; wire entries 5.0 (y) × 4.0 (z) slots cut 0.5 into each block's outer face, 4.0 below its top | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| barrier | 2.0 × 16.0 × 11.5 between the blocks, 2.5 above them | design choice |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screw's thread and torque | NOT ON FILE (B): a fit with the wire element; the clamp's connecting capacity is set by IEC 60947-1 (terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| overall | 80.0 × 50.0 (y −50 … 0) × 109.5 (z −47.5 … 62.0) | from the parts above |

## Named nodes
Ports `t-1`, `t-2` (kind port, unit screw, gender none: a screw clamp, PIN-002; axis +z). No moving or lit part. pins.csv gives both terminals the role `pass`: a capacitor has no polarity, and the motor circuit it is wired into says what each terminal carries.

## Materials by layer
`M-GREY-PA` the can · `M-BLACK-PA` terminal cap, blocks and barrier · `M-GALV` strap and foot · `M-ZINC` terminal screws · `M-GASKET` panel-screw holes, the strap's bore and the wire entries

## Decals (Blender)
On the can's front, a wrap label: "complexes.org generic", "capacitor-run", "10 µF", "450 V~", and a capacitor symbol. Terminal marks "1" and "2" on the cap beside each block. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range (class B, above). Everything else this element meets is on file (the M5 clearance holes), and every other size is a design choice; nothing is guessed and shown as sourced.
- The film winding, the discharge resistor across the terminals, the pressure disconnector, the capacitance tolerance, the operating class and the temperature range are not features of the class and are not stated or modelled in 1.0; the mass is not stated.
- The screws through the foot are the mechanical lane's M5 screws once they are on main (OPERATING.md 12, common parts); 1.0 models the holes and places no screw.
- Not a safety-function device.

## Outputs (out/)
`capacitor-run.lsp` · `.glb` (pivots on the two ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at 1.1 (lane round elec-r19).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC001516), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07, round 2) |
| 1.1 | ratings.csv: the two class-value rows to status "generic design" and source "ETIM 10.0 EC001516 class value: <feature> (EFnnnnnn)", OPERATING.md 12's form (review cloud-elec 2026-11-07 r2, finding 1); the two derived currents stay "derived"; no shape, node or figure change; gated on the PC (elec-r19, 2026-11-08) |
