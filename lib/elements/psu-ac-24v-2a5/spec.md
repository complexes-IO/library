# psu-ac-24v-2a5 · v1.0 · AC power supply, 120 V AC in, 24 V AC 2.5 A (60 W) out, not stabilised, 35 mm rail (complexes.org generic)

**What** AC power supply for a panel's 24 V AC circuits (solenoid valve coils, AC contactor coils, signal lamps): fed from the 120 V AC control circuit, it gives 24 V AC at up to 2.5 A (60 W) on one output, not stabilised, so the output follows the input. plc-aio 1.1's stepped moulded housing on the rail clip, two pluggable terminal blocks on its front (x1 the input and the protective earth, x2 the output), one status LED and a legend field. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002541, built to the class values below; no maker's datasheet and no product is matched. It has no inventory row: EC002541 is the first of the "etim" lines `python lib/build.py inventory elec` lists once no row above them builds unattended.
**Class** device · **Baseline** our own design: generic AC-power supply (ETIM 10.0 EC002541). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the terminals are placed terminal-plug 2.0 elements (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `PSUAC` · no parameters · places terminal-plug 2.0 twice (tags `x1` 3 poles, `x2` 2 poles).

## Class values
ETIM 10.0 EC002541 "AC-power supply", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Voltage type (supply voltage) (EF002991) | AC |
| 2 | 1st secondary output voltage (EF006792) | 24 … 24 V (AC, one fixed output) |
| 3 | 2nd secondary output voltage (EF006797) | none (one output) |
| 4 | 3rd secondary output voltage (EF006800) | none (one output) |
| 5 | Max. output current 1 (EF008284) | 2.5 A |
| 6 | Max. output current 2 (EF008285) | none (one output) |
| 7 | Max. output current 3 (EF008286) | none (one output) |
| 8 | Secondary voltage adjustable (EF007002) | no |
| 9 | Short-circuit-proof (EF007332) | no (the output needs its own protection, the panel's to provide) |
| 10 | Rated supply voltage AC 50 Hz (EF007076) | 120 … 120 V |
| 11 | Rated supply voltage AC 60 Hz (EF007077) | 120 … 120 V |
| 12 | Rated supply voltage DC (EF007078) | none (AC supply only) |
| 13 | Output voltage stabilized (EF003092) | no (the output follows the input) |
| 14 | Power consumption (EF000346) | 75 VA |
| 15 | Power output (EF003034) | 60 W (24 V × 2.5 A) |
| 16 | Stabilized (EF005302) | no |
| 17 | Type of electric connection (EF003961) | screw connection on pluggable terminal blocks (terminal-plug 2.0, two placed) |
| 18 | Suitable for rail mounting (EF003972) | yes (35 mm rail, EN 60715 TH35-7.5) |
| 19 | Suitable for wall mounting (EF000664) | no |
| 20 | Suitable for distribution board (EF001126) | no |
| 21 | Built-in height (EF000332) | 86 mm (in front of the rail crown, the plugs included) |
| 22 | Direct mounting possible (EF005689) | no |
| 23 | Width (EF000008) | 45 mm |
| 24 | Height (EF000040) | 100 mm |
| 25 | Depth (EF000049) | 93.5 mm (86.0 in front of the rail crown, 7.5 behind it) |
| 26 | Suitable for safety functions (EF001597) | no |
| 27 | SIL according to IEC 61508 (EF009889) | none (not a safety device) |
| 28 | Performance level according to EN ISO 13849-1 (EF007399) | none (not a safety device) |
| 29 | Degree of protection (IP) (EF005474) | not stated |
| 30 | Degree of protection (NEMA) (EF011959) | not stated |

These values are what the element claims: they are the class definition, not a certification, and no approval mark is shown. The 120 V input is the control circuit voltage xfmr-control 1.1 gives on its secondary; 24 V AC, 2.5 A and 75 VA are this element's design inputs (60 W out of 75 VA in leaves the losses and the magnetising current of an unregulated supply their room; no efficiency is claimed). The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC002541 class value" with the feature code (OPERATING.md 12); the input current row "derived" (I = S / U = 75 VA / 120 V = 0.625 A). `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 45.0 × 40.0 × 100.0 (y −40 … 0, z −50 … 50) on the clip | design choice (plc-aio 1.1's housing) |
| front block | 45.0 × 30.0 × 88.0 (y −70 … −40, z −44 … 44) on the base; 6.0 of the base shows above and below | design choice (plc-aio 1.1's) |
| input plug | terminal-plug 2.0, 3 poles, tag `x1`, mating face on the front block's face (y −70; body y −86 … −70), x 4 … 19, sockets' axis z 28 (body z 22 … 37.5), poles along +x, wire entries down: L N PE | terminal-plug 2.0 (its own spec; 12 A 250 V, above this element's 120 V and 0.63 A); placement a design choice |
| output plug | terminal-plug 2.0, 2 poles, tag `x2`, mating face on the front block's face, x 4 … 14, sockets' axis z −36 (body z −42 … −26.5): AC1 AC2 | as x1 (24 V, 2.5 A) |
| headers | the pins the plugs' sockets take, standing out of the front block into the sockets | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures |
| LED | Ø3.2 lens, 0.3 proud, at x 8, z 8: output live (green) | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 20.0 × 32.0 (x 22 … 42, z −16 … 16), 0.1 proud | design choice |
| overall | 45.0 × 93.5 (y −86.0 … 7.5) × 100.0 | from the parts above; the plugs stand 16.0 proud of the front block |

The input plug sits at the top of the face and the output plug at its foot, 48.5 apart (z −26.5 … 22), so the 120 V and the 24 V wiring leave the device apart; the distance is a design choice, and no clearance or creepage figure of a standard is claimed for it.

Terminal marks: L / N the 120 V AC input, PE the protective earth, AC1 / AC2 the 24 V AC output. The marks are labels, a design choice; the plugs' own pole marks are 1 … n (terminal-plug 2.0 Decals) with these printed on the legend field.

## Named nodes
`led-on` (emissive, green: the output is live) · the plugs' nodes `x1.t-1` … `x1.t-3`, `x2.t-1`, `x2.t-2` (clamp screws, gender none) and `x1.s-1` … `x1.s-3`, `x2.s-1`, `x2.s-2` (sockets, gender female), as terminal-plug 2.0 names them under its tag. Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-LENS-GREEN` LED · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plugs (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "psu-ac-24v-2a5", "IN 120 V AC 50/60 Hz 75 VA", "OUT 24 V AC 2.5 A", and the terminal diagram (L N PE; AC1 AC2). Beside the LED: "ON". No maker's name, logo or approval mark.

## Notes and open figures
- This element has no open figure of its own: everything it meets is on file (the rail clip, terminal-plug 2.0) and every other size and value is a design choice, a derived figure or a class value; nothing is guessed and shown as sourced. The placed plugs carry their own open line (their clamps' torque, terminal-plug 2.0's behaviour.csv: a document wanted, IEC 60999), which behaviour.csv repeats for each pin as that element writes it.
- Not stabilised: the output follows the input in the ratio 24 : 120. The phase-1 solver has no ratio (a source gives a fixed voltage), so behaviour.csv gives the rated 24 V whenever the input sees any voltage (as xfmr-control 1.1); the ratio is for the core's circuit model.
- The output is not short-circuit-proof (Class values 9) and neither side carries a fuse: the input's branch protection and the output's protection are the panel's to provide. Which protective device and what size is the panel's design under its own rules; this element states none.
- Neither output terminal is bonded to PE inside the device; whether the 24 V AC circuit is earthed is the panel's choice.
- lib/inventory.csv has no row for this element (an "etim" line): din-clip-35 and led, which a rail device of this kind would place, are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). It holds to the rail by the toolkit's rail clip, and its LED is the toolkit's lens.
- Not stated or modelled in 1.0: the transformer and its windings, the no-load output voltage and the regulation under load, the no-load current, the efficiency, the inrush current, the isolation between input and output, the insulation class, the degree of protection, the operating temperature and the mass.
- Not a safety-function device (Class values 26 to 28); the output is not claimed to be a safety extra-low voltage or a limited-power circuit of any standard.

## Outputs (out/)
`psu-ac-24v-2a5.lsp` · `.glb` (pivots on the LED and the plugs' ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r58 (lib/rounds/elec/), Blender and Godot; the AutoCAD gate waits for AutoCAD to be open.

## History
| version | change |
|---|---|
| 1.0 | elec-r58 (2026-11-20, unattended): first build, generic (ETIM 10.0 EC002541 AC-power supply), our own design; an "etim" line of `inventory elec`, no inventory row; places terminal-plug 2.0 twice (x1 3 poles, x2 2 poles) |
