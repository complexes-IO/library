# reactor-line-3p-4a · v1.0 · three-phase line reactor 4 A, 480 V, 50/60 Hz, 7.35 mH (complexes.org generic)

**What** Three-phase line reactor for a machine's control panel: three coils on one core, one in series with each supply line of a drive (a net reactance coil), 4 A a line, 480 V, 50 / 60 Hz, 7.35 mH a phase (uk 4 %), open construction (core and coils), screwed to the back panel by two brackets, screw terminals: line side on top, load side and PE below. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002563, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Coil for low-voltage (ETIM 10.0 EC002563). The class values are this element's definition (design inputs); the panel-screw holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); every other size, the hole pattern included, is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: surface-mount device: back face (the brackets' flanges, on the panel) y = 0, the lower-left mounting hole x = 0, z = 0, body toward −y.
**Built with** toolkit 1.3 · AutoLISP command `REACTOR3` · no parameters.

## Class choice
The line is an "etim" line of `python lib/build.py inventory elec` (no inventory row). EC002563's sixteen features describe a reactor (net, commutation, output and interference suppression reactance coils, ripple filter chokes), not a contactor's coil: the lane read the class that way and built the form the drives on file meet first, a three-phase net reactance coil sized above vfd-0.75kw 1.2's 2.2 A output current. The id follows OPERATING.md 6: class `reactor`, form `line-3p`, rating `4a`. The reading is the lane's, for EM or the core to overrule (lib/needs-em/elec.md, r60).

## Class values
ETIM 10.0 EC002563 "Coil for low-voltage", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Suitable as interference suppression reactance coil (EF007230) | no |
| 2 | Suitable as net reactance coil (EF007234) | yes |
| 3 | Suitable as commutation reactance coil (EF007233) | no |
| 4 | Suitable as ripple filter choke (EF007232) | no |
| 5 | Suitable as output reactance coil (EF007227) | no |
| 6 | Number of poles, primary side (EF007403) | 3 |
| 7 | Rated clock frequency (EF007502) | not stated (a supply-side reactor) |
| 8 | Rated operating frequency (EF007024) | 50 … 60 Hz |
| 9 | Max. rated operation voltage Ue (EF007357) | 480 V (line to line) |
| 10 | Rated current AC (EF007500) | 4 A (each line) |
| 11 | Max. rated current (Ith) at rated voltage DC (EF007359) | not stated (AC only) |
| 12 | Rated inductance (EF007291) | 7.35 mH (each phase) |
| 13 | Degree of protection (IP) (EF005474) | IP00 (open core and coils) |
| 14 | Relative short circuit voltage (EF007452) | 4 % |
| 15 | Resonance frequency (EF007455) | not stated |
| 16 | Degree of protection (NEMA) (EF011959) | not stated (open, panel-mounted) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. Values 12 and 14 agree with each other at both rated frequencies: the drop across one coil at the rated current is ω L I = 2π × 60 Hz × 7.35 mH × 4 A = 11.1 V, 4 % of 480 V / √3 = 277 V; and 2π × 50 Hz × 7.35 mH × 4 A = 9.2 V, 4 % of 400 V / √3 = 231 V. The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC002563 class value" with the feature code (OPERATING.md 12). `pins.csv` gives each terminal its role.

## Dimensions
| item | value | source |
|---|---|---|
| core | three limbs 20 wide and two yokes 20 high, windows 16 × 44: 92 × 84 in the x-z plane (x 2 … 94, z 15 … 99), stacked 30 deep (y −51 … −21), 21 clear of the panel | design choice |
| coils | a rectangular tube on each limb: 1.0 gap to the limb, 6.0 build, 40 high (2.0 clear of each yoke): 34 × 44 outside, 2.0 apart; y −58 … −14 | design choice |
| clamp bars | steel flats 88 × 16 × 3.0 on the front and back of each yoke | design choice |
| brackets | 2.5 sheet: a web on each yoke's end face (y −49 … −2.5) and a flange 112 × 25 on the panel (x −8 … 104) | design choice |
| panel holes | four Ø5.5 through the flanges, at x 0 / 96.0 and z 0 / 114.0; position Ø0.4 to datum A (the flanges' back face): floating fastener, 0.4 ≤ H − F = 0.5 (GDT-010) | Ø5.5: ISO 273 medium for M5 (lib/standards/holes.csv); the pattern and the position tolerance: design choice (features.csv) |
| terminal blocks | 18 deep on the front clamp bars (front face y −72.0): line side 56 × 16 on top (x 20 … 76, z 81 … 97), load side 56 × 16 below (x 8 … 64, z 17 … 33), PE block 24 × 16 beside it (x 64 … 88), green-yellow | design choice |
| terminals | 16.0 pitch: 1U1 1V1 1W1 on the upper block (screws at x 32 / 48 / 64, z 90, wire entries in its top face), 1U2 1V2 1W2 (x 20 / 36 / 52) and PE (x 76) below (screws at z 24, wire entries in the bottom faces); screw heads Ø5.6 × 1.2; entries 5.0 × 10.0 slots cut 0.5 deep | design choice (xfmr-control-3ph 1.2's `terminals`: the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screws' thread and torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by the terminal standard (IEC 60947-7-1 for terminal blocks), which is not on file (lib/standards/sources.csv), so no size is claimed |
| rating plate | 24 × 26 on the middle coil's front, 0.1 proud | design choice |
| overall | 112 × 73.2 × 134 (x −8 … 104, y −73.2 … 0, z −10 … 124) | from the parts above |

Terminal marks 1U1 1V1 1W1 (line side) and 1U2 1V2 1W2 (load side) are labels, a design choice in the form of xfmr-control-3ph's marks; no standard for them is on file.

## Named nodes
Ports only: `t-1U1`, `t-1V1`, `t-1W1` (line side), `t-1U2`, `t-1V2`, `t-1W2` (load side), `t-PE` (kind port, unit screw, gender none: a screw clamp, PIN-002). Nothing moves or lights.

## Materials by layer
`M-STEEL-7035` core laminations · `M-CU` coils · `M-GALV` clamp bars and brackets · `M-GREY-PA` terminal blocks · `M-GREEN-YELLOW` PE block · `M-ZINC` terminal screws · `M-GASKET` wire entries and the panel holes · `M-WHITE-PA` rating plate

## Decals (Blender)
On the rating plate: "complexes.org generic", "reactor-line-3p-4a", "3~ 4 A", "480 V 50/60 Hz", "7.35 mH", "uk 4 %", the connection diagram. Terminal marks beside each screw; the earth symbol on the PE block. No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range and torque (class B, above; behaviour.csv repeats it a clamp). The panel holes are on file (ISO 273); every other size is a design choice; nothing is guessed and shown as sourced.
- behaviour.csv writes each phase as a pass-through from its line-side clamp to its load-side clamp, as filter-emc's lines: the solver's phase 1 is ideal, so the series drop of value 14 and the inductance of value 12 are stated here and not modelled.
- Mass, losses, the saturation current, the thermal class and the air gap are not features of the class and are not stated in 1.0. The core's and coils' sizes are design choices for the look of a reactor of this rating; no magnetic design is claimed from them.
- The PE terminal bonds the core frame (clamp bars and brackets) to the panel's protective conductor; the bond itself is not modelled.
- Not placed: the M5 panel screws (the holes are modelled; the host places the screws).

## Outputs (out/)
`reactor-line-3p-4a.lsp` · `.glb` (pivots on the ports, `env-colonly` collider) · `preview-*.png`. Gates: Blender and Godot run on the PC at 1.0 (lane round elec-r60); the AutoCAD gate waits in the lane's gate queue (AutoCAD was not open on the PC).

## History
| version | change |
|---|---|
| 1.0 | elec-r60 (2026-11-20, unattended): first build, generic (ETIM 10.0 EC002563), our own design, in xfmr-control-3ph 1.2's form |
