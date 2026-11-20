# psu-acdc-24v-1a25 · v1.0 · AC/DC power supply, 120 V AC in, 24 V AC 1.25 A and 24 V DC 1.25 A out (60 W), not stabilised, 35 mm rail (complexes.org generic)

**What** AC/DC power supply for a panel that has both 24 V AC and 24 V DC circuits (AC solenoid and contactor coils beside DC sensors and signal lamps): fed from the 120 V AC control circuit, it gives 24 V AC at up to 1.25 A on one output and 24 V DC at up to 1.25 A on a second (60 W in all), neither stabilised, so both follow the input. psu-ac-24v-2a5 1.0's stepped moulded housing on the rail clip, three pluggable terminal blocks on its front (x1 the input and the protective earth, x2 the AC output, x3 the DC output), two status LEDs and a legend field. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002542, built to the class values below; no maker's datasheet and no product is matched. It has no inventory row: EC002542 is one of the "etim" lines `python lib/build.py inventory elec` lists once no row above them builds unattended.
**Class** device · **Baseline** our own design: generic AC/DC-power supply (ETIM 10.0 EC002542). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the terminals are placed terminal-plug 2.0 elements (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `PSUACDC` · no parameters · places terminal-plug 2.0 three times (tags `x1` 3 poles, `x2` 2 poles, `x3` 2 poles).

## Class choice
ETIM has three sibling classes: EC002540 DC-power supply (psu-24v-2a4's), EC002541 AC-power supply (psu-ac-24v-2a5's) and EC002542 AC/DC-power supply. EC002542's features list AC and DC secondary output voltages side by side, three of each, so the lane read the class as a supply that gives both kinds of output and built one with one of each. That reading is the lane's, written in lib/needs-em/elec.md (r59) for EM or the core to overrule.

## Class values
ETIM 10.0 EC002542 "AC/DC-power supply", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Voltage type (supply voltage) (EF002991) | AC |
| 2 | 1st secondary output voltage AC (EF006793) | 24 … 24 V (one fixed AC output, plug x2) |
| 3 | 2nd secondary output voltage AC (EF006798) | none (one AC output) |
| 4 | 3rd secondary output voltage AC (EF006801) | none (one AC output) |
| 5 | 1st secondary output voltage DC (EF006794) | 24 … 24 V (one fixed DC output, plug x3; at the rated input and the rated load) |
| 6 | 2nd secondary output voltage DC (EF006799) | none (one DC output) |
| 7 | 3rd secondary output voltage DC (EF006802) | none (one DC output) |
| 8 | Max. output current 1 (EF008284) | 1.25 A (the AC output) |
| 9 | Max. output current 2 (EF008285) | 1.25 A (the DC output) |
| 10 | Max. output current 3 (EF008286) | none (two outputs) |
| 11 | Secondary voltage adjustable (EF007002) | no |
| 12 | Short-circuit-proof (EF007332) | no (each output needs its own protection, the panel's to provide) |
| 13 | Rated supply voltage AC 50 Hz (EF007076) | 120 … 120 V |
| 14 | Rated supply voltage AC 60 Hz (EF007077) | 120 … 120 V |
| 15 | Rated supply voltage DC (EF007078) | none (AC supply only) |
| 16 | Output voltage stabilized (EF003092) | no (both outputs follow the input) |
| 17 | Power consumption (EF000346) | 75 VA |
| 18 | Power output (EF003034) | 60 W (24 V × 1.25 A on each of the two outputs) |
| 19 | Stabilized (EF005302) | no |
| 20 | Type of electric connection (EF003961) | screw connection on pluggable terminal blocks (terminal-plug 2.0, three placed) |
| 21 | Suitable for rail mounting (EF003972) | yes (35 mm rail, EN 60715 TH35-7.5) |
| 22 | Suitable for wall mounting (EF000664) | no |
| 23 | Suitable for distribution board (EF001126) | no |
| 24 | Built-in height (EF000332) | 86 mm (in front of the rail crown, the plugs included) |
| 25 | Direct mounting possible (EF005689) | no |
| 26 | Width (EF000008) | 45 mm |
| 27 | Height (EF000040) | 100 mm |
| 28 | Depth (EF000049) | 93.5 mm (86.0 in front of the rail crown, 7.5 behind it) |
| 29 | Suitable for safety functions (EF001597) | no |
| 30 | SIL according to IEC 61508 (EF009889) | none (not a safety device) |
| 31 | Performance level according to EN ISO 13849-1 (EF007399) | none (not a safety device) |
| 32 | Degree of protection (IP) (EF005474) | not stated |
| 33 | Degree of protection (NEMA) (EF011959) | not stated |

These values are what the element claims: they are the class definition, not a certification, and no approval mark is shown. The 120 V input is the control circuit voltage xfmr-control 1.1 gives on its secondary; 24 V AC, 24 V DC, 1.25 A each and 75 VA are this element's design inputs (60 W out of 75 VA in leaves the losses and the magnetising current of an unregulated supply their room; no efficiency is claimed). ETIM's "Max. output current 1 / 2 / 3" do not say which output each belongs to: here 1 is the AC output and 2 the DC output, a design choice. The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC002542 class value" with the feature code (OPERATING.md 12); the input current row "derived" (I = S / U = 75 VA / 120 V = 0.625 A). `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 45.0 × 40.0 × 100.0 (y −40 … 0, z −50 … 50) on the clip | design choice (psu-ac-24v-2a5 1.0's housing) |
| front block | 45.0 × 30.0 × 88.0 (y −70 … −40, z −44 … 44) on the base; 6.0 of the base shows above and below | design choice (psu-ac-24v-2a5 1.0's) |
| input plug | terminal-plug 2.0, 3 poles, tag `x1`, mating face on the front block's face (y −70; body y −86 … −70), x 4 … 19, sockets' axis z 28 (body z 22 … 37.5), poles along +x, wire entries down: L N PE | terminal-plug 2.0 (its own spec; 12 A 250 V, above this element's 120 V and 0.63 A); placement a design choice |
| AC output plug | terminal-plug 2.0, 2 poles, tag `x2`, mating face on the front block's face, x 4 … 14, sockets' axis z −36 (body z −42 … −26.5): AC1 AC2 | as x1 (24 V, 1.25 A) |
| DC output plug | terminal-plug 2.0, 2 poles, tag `x3`, mating face on the front block's face, x 28 … 38, sockets' axis z −36: +V −V; 14.0 to the right of x2's body | as x1 (24 V, 1.25 A); placement a design choice |
| headers | the pins the plugs' sockets take, standing out of the front block into the sockets | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures |
| LEDs | two Ø3.2 lenses, 0.3 proud, at z 8: `led-ac` at x 8 (AC output live, green), `led-dc` at x 15 (DC output live, green) | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 20.0 × 32.0 (x 22 … 42, z −16 … 16), 0.1 proud | design choice |
| overall | 45.0 × 93.5 (y −86.0 … 7.5) × 100.0 | from the parts above; the plugs stand 16.0 proud of the front block |

The input plug sits at the top of the face and the two output plugs at its foot, 48.5 apart (z −26.5 … 22), so the 120 V and the 24 V wiring leave the device apart; the two outputs sit 14.0 apart along x so an AC plug is not taken for the DC one. Both distances are design choices, and no clearance or creepage figure of a standard is claimed for them. The two output plugs are the same 2-pole plug: nothing keys one against the other in 1.0, and the legend field's marks are what tells them apart.

Terminal marks: L / N the 120 V AC input, PE the protective earth, AC1 / AC2 the 24 V AC output, +V / −V the 24 V DC output. The marks are labels, a design choice; the plugs' own pole marks are 1 … n (terminal-plug 2.0 Decals) with these printed on the legend field.

## Named nodes
`led-ac`, `led-dc` (emissive, green: that output is live) · the plugs' nodes `x1.t-1` … `x1.t-3`, `x2.t-1`, `x2.t-2`, `x3.t-1`, `x3.t-2` (clamp screws, gender none) and `x1.s-1` … `x1.s-3`, `x2.s-1`, `x2.s-2`, `x3.s-1`, `x3.s-2` (sockets, gender female), as terminal-plug 2.0 names them under its tag. Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-LENS-GREEN` LEDs · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plugs (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "psu-acdc-24v-1a25", "IN 120 V AC 50/60 Hz 75 VA", "OUT 1 24 V AC 1.25 A", "OUT 2 24 V DC 1.25 A", and the terminal diagram (L N PE; AC1 AC2; +V −V). Beside the LEDs: "AC", "DC". No maker's name, logo or approval mark.

## Notes and open figures
- This element has no open figure of its own: everything it meets is on file (the rail clip, terminal-plug 2.0) and every other size and value is a design choice, a derived figure or a class value; nothing is guessed and shown as sourced. The placed plugs carry their own open line (their clamps' torque, terminal-plug 2.0's behaviour.csv: a document wanted, IEC 60999), which behaviour.csv repeats for each pin as that element writes it.
- Not stabilised: both outputs follow the input. The AC output follows it in the ratio 24 : 120; the DC output is that of a rectified and smoothed winding with no regulator, 24 V at the rated input and the rated load, higher at light load. The phase-1 solver has no ratio (a source gives a fixed voltage), so behaviour.csv gives the rated 24 V on each output whenever the input sees any voltage (as xfmr-control 1.1); the ratio is for the core's circuit model.
- Neither output is short-circuit-proof (Class values 12) and no side carries a fuse: the input's branch protection and each output's protection are the panel's to provide. Which protective device and what size is the panel's design under its own rules; this element states none.
- No output terminal is bonded to PE inside the device, and the two outputs share no terminal (AC2 and −V are separate returns); whether either 24 V circuit is earthed is the panel's choice.
- lib/inventory.csv has no row for this element (an "etim" line): din-clip-35 and led, which a rail device of this kind would place, are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). It holds to the rail by the toolkit's rail clip, and its LEDs are the toolkit's lens.
- Not stated or modelled in 1.0: the transformer and its windings, the rectifier and the smoothing, the DC output's ripple and its no-load voltage, the AC output's no-load voltage and the regulation under load, the no-load current, the efficiency, the inrush current, the isolation between the input and the outputs and between the two outputs, the insulation class, the degree of protection, the operating temperature and the mass.
- Not a safety-function device (Class values 29 to 31); neither output is claimed to be a safety extra-low voltage or a limited-power circuit of any standard.

## Outputs (out/)
`psu-acdc-24v-1a25.lsp` · `.glb` (pivots on the LEDs and the plugs' ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r59 (lib/rounds/elec/), Blender and Godot; the AutoCAD gate waits for AutoCAD to be open.

## History
| version | change |
|---|---|
| 1.0 | elec-r59 (2026-11-20, unattended): first build, generic (ETIM 10.0 EC002542 AC/DC-power supply), our own design; an "etim" line of `inventory elec`, no inventory row; places terminal-plug 2.0 three times (x1 3 poles, x2 2 poles, x3 2 poles) |
