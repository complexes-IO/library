# xfmr-control · v1.1 · single-phase control transformer 250 VA, 480 V / 120 V (complexes.org generic)

**What** Control transformer for a machine's control panel: 250 VA, primary 480 V (the library's panels are fed at 480 V), secondary 120 V for the control circuit, open construction (core and coil), screwed to the back panel by two brackets. Primary on screw clamps (1U 1V: a 250 V plug can't take 480 V), secondary on a placed terminal-plug 2.0 (2U 2V, 12 A 250 V) so the control wiring unplugs with the panel's other plug-in terminals, PE on a screw clamp of a green-yellow block. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002486, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic One-phase control transformer (ETIM 10.0 EC002486). The class values are this element's definition (design inputs); the panel-screw holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); the secondary header is built to terminal-plug 2.0's spec; every other size, the hole pattern included, is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: surface-mount device: back face (the brackets' flanges, on the panel) y = 0, the lower-left mounting hole x = 0, z = 0, body toward −y.
**Built with** toolkit 1.3 · AutoLISP command `XFMR1` · no parameters · places terminal-plug 2.0 once (tag `x2`, 2 poles).

## Class values
ETIM 10.0 EC002486 "One-phase control transformer", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Built as safety transformer (EF007235) | no |
| 2 | Built as isolating transformer (EF007238) | no (separate primary and secondary windings on one bobbin; the isolating-transformer construction of IEC 61558 is not on file, so it is not claimed) |
| 3 | Built as energy saving transformer (EF007005) | no |
| 4 | Primary voltage 1 (EF006125) | 480 V |
| 5 | Primary voltage 2 (EF006126) | not stated (no tap) |
| 6 | Primary voltage 3 (EF006127) | not stated |
| 7 | Primary voltage 4 (EF007410) | not stated |
| 8 | Primary voltage 5 (EF007411) | not stated |
| 9 | Primary voltage 6 (EF007412) | not stated |
| 10 | Primary voltage 7 (EF007413) | not stated |
| 11 | Primary voltage 8 (EF007414) | not stated |
| 12 | Primary voltage 9 (EF007415) | not stated |
| 13 | Primary voltage 10 (EF007409) | not stated |
| 14 | Secondary voltage 1 (EF007472) | 120 V |
| 15 | Secondary voltage 2 (EF007474) | not stated (no tap) |
| 16 | Secondary voltage 3 (EF007475) | not stated |
| 17 | Secondary voltage 4 (EF007476) | not stated |
| 18 | Secondary voltage 5 (EF007477) | not stated |
| 19 | Secondary voltage 6 (EF007478) | not stated |
| 20 | Secondary voltage 7 (EF007479) | not stated |
| 21 | Secondary voltage 8 (EF007480) | not stated |
| 22 | Secondary voltage 9 (EF007481) | not stated |
| 23 | Secondary voltage 10 (EF007473) | not stated |
| 24 | Rated apparent power (EF008864) | 250 VA |
| 25 | Power (EF000076) | not stated (the rating is the apparent power, 24; the load's power factor is the control circuit's) |
| 26 | Power consumption in standby mode (EF012331) | not stated (the no-load loss is not stated in 1.0) |
| 27 | Type of insulation material according to IEC 85 (EF007299) | B (130 °C) |
| 28 | Short-circuit-proof (EF007332) | no (the secondary is protected by a fuse or breaker sized to its rated current) |
| 29 | Relative short circuit voltage (EF007452) | 4 % |
| 30 | Width (EF000008) | 116 mm |
| 31 | Height (EF000040) | 130 mm |
| 32 | Depth (EF000049) | 108 mm |
| 33 | Degree of protection (IP) (EF005474) | IP00 (open core and coil) |
| 34 | Ring core (EF006170) | no (E-I laminated core) |
| 35 | Suitable for mounting on PCB (EF006157) | no |
| 36 | Suitable for distribution board (EF001126) | no (open construction, panel-mounted by its brackets inside a machine's control enclosure) |
| 37 | Conductor material (EF001622) | copper |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. Rated currents follow from them (ratings.csv, derived): primary 250 / 480 = 0.52 A, secondary 250 / 120 = 2.08 A. The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC002486 class value" with the feature code (OPERATING.md 12). `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| core | E-I laminations in the x-z plane: two outer limbs 16 wide, a centre limb 32 wide, two yokes 16 high, windows 16 × 48: 96 × 80 (x 2 … 98, z 15 … 95), stacked 50 deep (y −71 … −21), 21 clear of the panel | design choice (centre-limb section 32 × 50 = 16 cm² for 250 VA) |
| coil | a rectangular tube on the centre limb, both windings on one bobbin: 1.0 gap to the limb, 12.0 build, 38 high (5.0 clear of each yoke): 58 × 76 outside (x 21 … 79, y −84 … −8), z 36 … 74; 3.0 clear of each outer limb | design choice |
| clamp bars | steel flats 92 × 12 × 3.0 on the front and back of each yoke (z 17 … 29 and 81 … 93) | design choice |
| brackets | 2.5 sheet: a web on each yoke's end face (y −69 … −2.5) and a flange 116 × 25 on the panel (x −8 … 108; z −10 … 15 and 95 … 120) | design choice |
| panel holes | four Ø5.5 through the flanges, at x 0 / 100.0 and z 0 / 110.0; position Ø0.4 to datum A (the flanges' back face): floating fastener, 0.4 ≤ H − F = 0.5 (GDT-010) | Ø5.5: ISO 273 medium for M5 (lib/standards/holes.csv); the pattern and the position tolerance: design choice (features.csv) |
| terminal blocks | 18 deep × 18 high on the front clamp bars (front face y −92.0, back face on the bar at y −74; the 6 above or below the bar face the yoke across the bar's 3.0): primary 40 × 18 on top (x 30 … 70, z 75 … 93), the secondary header block 24 × 18 below (x 26 … 50, z 17 … 35), PE block 24 × 18 beside it (x 50 … 74), green-yellow; each 1.0 clear of the coil | design choice |
| primary terminals | 1U 1V screw clamps at 16.0 pitch (x 42, 58; screws at z 86, wire entries in the block's top face); screw heads Ø5.6 × 1.2; entries 5.0 × 10.0 slots cut 0.5 deep | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| secondary header | two pins 1.0 × 1.0, 5.0 past the header block's front face (y −97 … −92), at x 35.5 / 40.5 on z 25.0: each sits in a socket of the placed plug, 0.5 clear of its walls and floor | terminal-plug 2.0 spec.md Dimensions (the header pin: 1.0 × 1.0 square, free length at most 5.0); the pins' position follows the plug's placement |
| secondary plug | terminal-plug 2.0, 2 poles, placed on the header block's front face (mating face y −92, body y −108 … −92, x 33 … 43, z 19 … 34.5), poles along +x, wire entries down: pole 1 = 2U, pole 2 = 2V | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| PE terminal | one screw clamp on the PE block (x 62, screw at z 24, wire entry in the block's bottom face), as the primary's | design choice |
| conductor range of the clamps | the wire sizes and ferrules the 1U, 1V and PE clamps take, and the screws' thread and torque | NOT ON FILE (B): IEC 60947-1 (a fit with the wire element; the clamps' connecting capacity is set by the terminal standard, which is not on file, lib/standards/sources.csv, so no size is claimed) |
| rating plate | 36 × 28 on the coil's front, 0.1 proud (x 32 … 68, z 41 … 69) | design choice |
| overall | 116 × 108 × 130 (x −8 … 108, y −108 … 0, z −10 … 120); the plug's front at y −108 is the element's front | from the parts above |

Terminal marks follow the IEC convention for transformer terminals (1U 1V primary; 2U 2V secondary; PE). The marks are labels, a design choice; the standard itself is not on file. The plug's own pole marks are 1 and 2 (terminal-plug 2.0 Decals); 2U and 2V are printed on the header block beside each pole.

## Named nodes
Ports `t-1U`, `t-1V` (primary) and `t-PE` (kind port, unit screw, gender none: a screw clamp, PIN-002). The placed plug brings its own: `x2.t-1`, `x2.t-2` (its clamps, 2U and 2V) and `x2.s-1`, `x2.s-2` (its sockets, female, on the header pins). Nothing moves or lights; the twin reads the secondary's voltage from the class values while the primary is fed.

## Materials by layer
`M-STEEL-7035` core laminations · `M-CU` coil · `M-GALV` clamp bars and brackets · `M-GREY-PA` terminal and header blocks · `M-GREEN-YELLOW` PE block · `M-ZINC` terminal screws and header pins · `M-GASKET` wire entries and the panel holes · `M-WHITE-PA` rating plate · `M-GREEN` the placed plug (terminal-plug 2.0)

## Decals (Blender)
On the rating plate: "complexes.org generic", "xfmr-control", "1~ 250 VA", "PRI 480 V", "SEC 120 V", "uk 4 %", "insulation class B", the connection diagram. Terminal marks beside each screw (1U 1V, PE) and beside each pole of the header (2U 2V); the earth symbol on the PE block. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the screw clamps' conductor range, thread and torque (class B, above: IEC 60947-1, a document wanted). The panel holes are on file (ISO 273), the secondary terminals are terminal-plug 2.0's (past station 6 before this host placed it, OPERATING.md 12); every other size is a design choice; nothing is guessed and shown as sourced.
- Not placed in 1.0 though lib/inventory.csv's made_of names them: screw-iso4762 x4. The panel screws are the installer's; only their ISO 273 clearance holes are modelled (OPERATING.md 12: a host places only common parts past station 6; the screws are not built).
- Mass, no-load and load losses, inrush current, efficiency and the winding resistances are not features of the class and are not stated in 1.0. The secondary's protection (Class values 28: not short-circuit-proof) is the panel's to provide; a panel that places this element sizes it from the derived 2.08 A (NEC 450.3(B), transformers of 1000 V or less, is the rule a panel round cites when it does).
- The PE terminal bonds the core frame (clamp bars and brackets) to the panel's protective conductor; the bond itself is not modelled.
- The solver's phase 1 has no transformer ratio (lib/behaviour.md: a `source` row gives a fixed voltage): behaviour.csv gives the secondary its rated 120 V while any voltage is on the primary. A ratio (secondary = primary × 120 / 480) is for the core's circuit model; said so in behaviour.csv and lib/rounds/elec/r27.md.

## Outputs (out/)
`xfmr-control.lsp` · `.glb` (pivots on the ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): 1.0 in elec-r27 (lib/rounds/elec/r27.md), 1.1 in elec-r35.

## History
| version | change |
|---|---|
| 1.0 | elec-r27 (2026-11-11, unattended): first build, generic (ETIM 10.0 EC002486), our own design; inventory elec pinned 5; places terminal-plug 2.0 (2 poles) for the secondary |
| 1.1 | elec-r35 (2026-11-12, unattended): text only, geometry as 1.0. pins.csv t-PE's source named IEC 60204-1 with no clause; the standard is not in lib/standards/sources.csv, so it now says the rule's standard is not on file (NFPA 79's bonding clause is view-only, for an attended reading) (review elec-r27 finding 1) |
