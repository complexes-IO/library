# fan-cooling · v1.0 · axial cooling fan 60 × 60 × 25, 24 V DC (complexes.org generic)

**What** An axial cooling fan for a drive's or a rack unit's heat sink: a square frame with a round bore, an impeller with five pitched blades that turns about the fan's axis while 24 V DC is across its terminals, and the motor's stator boss held on four struts at the outlet face. A terminal block on the frame's side carries two screw clamps (1 = +24 V, 2 = 0 V). Four M4 clearance holes in the corners screw it to the host's wall or heat sink. A common part (lib/inventory.csv row `fan-cooling`, own_design generic, "cooling fan, 24 V DC"): vfd-0.75kw, servo-drive and ups-rack list it in their made_of. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001143, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic cooling fan (ETIM 10.0 EC001143). The class's nine features are on file (lib/standards/etim/class-features.csv); its name is not in the classes.csv subset, so the inventory row's type names it. The class values are this element's definition (design inputs); the four holes are M4 clearance, ISO 273 medium; every other size is a design choice, said so below.
**Units / frame** mm, Z up. Origin: the frame's inlet face y = 0 on the fan's axis (x = z = 0); air flows toward +y, the struts at the outlet face y = 25, the terminal block toward +x (in a BOM: the inlet face on the host's wall, the axis through the host's air opening).
**Built with** toolkit 1.3 · AutoLISP command `FANCOOL` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC001143)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Mains frequency (EF001639) | not stated (a DC fan: no mains frequency) |
| 2 | Rated voltage (EF000228) | 24 V DC (the panel's control supply) |
| 3 | Type of electric connection (EF003961) | screw terminals 1 (+24 V) and 2 (0 V) on a terminal block |
| 4 | Diameter impeller (EF001643) | 52 mm |
| 5 | Rotational speed (EF001642) | not stated (the twin reads running or still only) |
| 6 | Height (EF000040) | 60 mm (the frame, z) |
| 7 | Width (EF000008) | 69.3 mm (the frame with the label field and the terminal block, x) |
| 8 | Depth (EF000049) | 25 mm (inlet face to outlet face, y) |
| 9 | Degree of protection (IP) (EF005474) | not stated (no finger guard or seal is modelled) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the ones the checks may read (status "generic design", source "ETIM 10.0 EC001143 class value"); the fan's power, 2.4 W, is not a feature of EC001143: a design figure inside psu-24v-2a4's output (the 24 V budget, ELR-020), its current derived (0.1 A at 24 V). `pins.csv` gives each terminal its role.

## Mechanism
| node | kind | travel | what moves it |
|---|---|---|---|
| `impeller` | rotate about the fan's axis y, through (0, 10.5, 0) | 0 … 360° | the motor, while 24 V DC is across 1-2 (behaviour.csv state running); still when no supply |

The impeller (hub Ø22 × 17.5 and five blades) turns inside the Ø56 bore with the blade tips' corners 1.4 clear of it, and its hub's back face 0.5 clear of the stator boss (asserted in element.py). The direction of turning and the speed are not modelled (class C: motion the twin doesn't read).

## Dimensions
| item | value | source |
|---|---|---|
| frame | 60 × 25 × 60 (x ±30, y 0 … 25, z ±30), M-BLACK-PA | design choice: the frame fits inside vfd-0.75kw's 72 mm width (its spec.md overall); no fan frame standard is on file |
| venturi bore | Ø56 through the frame on the axis (2 of wall at the sides' middles) | design choice; features.csv |
| mounting holes | 4 × Ø4.5 through the frame at x, z = ±25 (pitch 50 × 50), 2.75 of wall to the frame's edges | M4 clearance, ISO 273 medium H13 (lib/standards/holes.csv); the pitch a design choice; features.csv, position Ø0.5 at MMC (T ≤ H − F) |
| impeller | hub Ø22, y 2 … 19.5; five blades r 10 … 26 (impeller Ø52), chord 14, 1 thick, set 50° from the axis, mid plane y 10.5 (y 5.6 … 15.4) | design choice |
| stator boss | Ø20, y 20 … 24 | design choice; the motor's windings and electronics inside are not modelled |
| struts | four, along ±x and ±z, 1.2 wide, y 20 … 24, from the boss (r 9.5) into the bore's wall (r 28.5) | design choice |
| terminal block | x 29.5 … 37.5 (0.5 into the frame's +x face), y 4 … 21, z ±8 | design choice |
| terminals | two screw clamps on the block's +x face (x 37.5): heads Ø4.4 × 1.2 at y 12.5, 1 at z +4.5, 2 at z −4.5; conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions and marks a design choice (1 + / 2 −); the clamp's figures a standard's table not on file (lib/standards/wanted.md), as pt 1.0's |
| label field | 0.6 × 17 × 20 on the frame's −x face (x −30.6 … −30, y 4 … 21, z ±10) | design choice |
| overall | 69.3 (x −30.6 … 38.7) × 25.0 (y 0 … 25) × 60.0 (z ±30) | from the parts above |

## Named nodes
`impeller` (kind rotate, axis y, 0 … 360°) · ports `t-1`, `t-2` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads, axis +x. pins.csv names what each terminal carries.

## Materials by layer
`M-BLACK-PA` frame, stator boss, struts and terminal block · `M-BLACK-PC` impeller · `M-ZINC` terminal screw heads · `M-WHITE-PA` label field (the bore and holes are cuts, no layer of their own)

## Decals (Blender)
On the label field: "complexes.org generic", "fan-cooling", "24 V DC", "1 + / 2 −", "air → +y". No maker's name, logo or approval mark.

## Notes
- The screw clamps' conductor range and torque: class B, IEC 60947-1 (Dimensions; behaviour.csv), as pt 1.0's. Every rating is a class value (design input) or a design figure (the 2.4 W, ELR-020); every size a design choice; the holes ISO 273. Nothing is guessed and shown as sourced.
- The airflow, pressure and noise are not claimed (EC001143's features on file have none): the twin reads the fan running or still. A host that needs a flow for its heat sink states it at its own level.
- A maker's fan of this size usually carries two leads; this design takes screw clamps so the terminals are port nodes the twin's probe can touch (BEH-020) and the host's wires land on them.
- Not placed and not modelled: a finger guard, a filter, the motor's windings and electronics in the boss, the screws (the host's: M4, ISO 273 medium).
- Not a safety-function device.

## Outputs (out/)
`fan-cooling.lsp` · `.glb` (pivots on the impeller and the two terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r45 (lib/rounds/elec/r45.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r45 (2026-11-13, unattended): first build, generic ETIM 10.0 EC001143, our own design; a common part of vfd-0.75kw, servo-drive and ups-rack |
