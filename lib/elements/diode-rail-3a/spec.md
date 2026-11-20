# diode-rail-3a · v1.0 · diode module, one rectifier diode A to K, 3 A 250 V, 35 mm rail (complexes.org generic)

**What** A diode on the rail: one rectifier diode between two screw terminals, A (anode) and K (cathode), for a panel's control circuits (a free-wheeling diode across a DC coil, a decoupling diode between two 24 V DC feeds, a lamp-test diode). psu-ac-24v-2a5 1.0's stepped moulded housing at one narrow module's width on the rail clip, one pluggable two-pole terminal block at the foot of its front and a legend field above it. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC004667, built to the class value below; no maker's datasheet and no product is matched. It has no inventory row: EC004667 is one of the "etim" lines `python lib/build.py inventory elec` lists once no row above them builds unattended.
**Class** device · **Baseline** our own design: generic Discrete electronic component (ETIM 10.0 EC004667). The class value is this element's definition (a design input); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the terminals are a placed terminal-plug 2.0 element (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `DIODER` · no parameters · places terminal-plug 2.0 once (tag `x1`, 2 poles).

## Class choice
EC004667 "Discrete electronic component" has one feature on file, "Model" (lib/standards/etim/class-features.csv), and lib/standards/etim/classes.csv gives its synonyms as diode, integrated circuit, operational amplifier, rectifier, thyristor, transistor and Zener diode. The lane read the class as its first synonym in the form a control panel uses: a single diode in a rail housing with screw terminals. That reading, the id (`diode` the class word, `rail` the form, `3a` the rating; OPERATING.md 6) and the two ratings below are the lane's, EM's or the core's to overrule (lib/needs-em/elec.md, r61).

## Class values
ETIM 10.0 EC004667 "Discrete electronic component", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Model (EF000010) | diode (one rectifier diode, anode A to cathode K) |

This value is what the element claims: it is the class definition, not a certification, and no approval mark is shown. ETIM's own list of values for the feature is not in lib/standards/etim/ (the feature's type is a value list); "diode" is the first of the class's synonyms in classes.csv. The class-value row of `ratings.csv` reads status "generic design", source "ETIM 10.0 EC004667 class value" with the feature code (OPERATING.md 12).

## Ratings
The class has no rating feature, so the two ratings are design figures (OPERATING.md 6, "design: <value> (<the rule it meets>)"), written in `ratings.csv` with status "design":

| rating | value | the rule it meets |
|---|---|---|
| forward current, A to K | 3 A | not above the 12 A of the placed terminal-plug 2.0 (ETIM 10.0 EC002021 class value, Rated current In, EF008250); above the 24 V DC coil currents on file (relay-aux-2no2nc 1.3: 0.10 A) |
| repetitive reverse voltage, K to A | 250 V | not above the 250 V of the placed terminal-plug 2.0 (ETIM 10.0 EC002021 class value, Rated voltage, EF000228) |

No forward voltage drop, leakage current, surge current, recovery time or thermal figure is stated: none is a feature of the class and no standard on file fixes one.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 18.0 × 40.0 × 80.0 (y −40 … 0, z −40 … 40) on the clip | design choice (psu-ac-24v-2a5 1.0's housing, one narrow module wide) |
| front block | 18.0 × 20.0 × 68.0 (y −60 … −40, z −34 … 34) on the base; 6.0 of the base shows above and below | design choice |
| plug | terminal-plug 2.0, 2 poles, tag `x1`, mating face on the front block's face (y −60; body y −76 … −60), x 4 … 14, sockets' axis z −22 (body z −28 … −12.5), poles along +x, wire entries down: A K | terminal-plug 2.0 (its own spec; 12 A 250 V, not below this element's 3 A and 250 V); placement a design choice |
| header | the pins the plug's sockets take, standing out of the front block into the sockets | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures |
| legend field | 14.0 × 28.0 (x 2 … 16, z 0 … 28), 0.1 proud | design choice |
| overall | 18.0 × 83.5 (y −76.0 … 7.5) × 80.0 | from the parts above; the plug stands 16.0 proud of the front block |

Terminal marks: A the anode, K the cathode. The marks are labels, a design choice; the plug's own pole marks are 1 and 2 (terminal-plug 2.0 Decals) with A and K printed on the legend field beside the diode's symbol.

## Named nodes
The plug's nodes `x1.t-1`, `x1.t-2` (clamp screws, gender none) and `x1.s-1`, `x1.s-2` (sockets, gender female), as terminal-plug 2.0 names them under its tag. Nothing moves and nothing lights. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plug (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "diode-rail-3a", the diode's graphical symbol with A at its anode and K at its cathode, "3 A", "250 V". No maker's name, logo or approval mark.

## Notes and open figures
- This element has no open figure of its own: everything it meets is on file (the rail clip, terminal-plug 2.0) and every other size and value is a design choice, a design figure with its rule, or the class value; nothing is guessed and shown as sourced. The placed plug carries its own open line (its clamps' torque, terminal-plug 2.0's behaviour.csv: a document wanted, IEC 60999), which behaviour.csv repeats for each pin as that element writes it.
- What the solver reads: phase 1 of the solver has no one-way path (a contact row is one conductor both ways, and V(a,b) is unsigned, lib/behaviour.md Expressions), so behaviour.csv gives the two pins and the two limits and no path between A and K. That is right for a free-wheeling diode across a coil, which is reverse biased whenever the circuit is at rest or driven; it is wrong for a diode in series, which the solver then sees as an open circuit. Request elec-21 asks the core for a one-way path; the contact row is written with its answer, and until then a panel that needs the diode to conduct in the solver should not place this element.
- No heat sink and no thermal path is modelled; the 3 A is not claimed at any ambient temperature.
- lib/inventory.csv has no row for this element (an "etim" line): din-clip-35, which a rail device of this kind would place, is not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). It holds to the rail by the toolkit's rail clip.
- Not stated or modelled in 1.0: the diode itself and its board, the forward voltage drop, the leakage and surge currents, the recovery time, the insulation between the diode and the rail, the degree of protection, the operating temperature and the mass.
- Not a safety-function device.

## Outputs (out/)
`diode-rail-3a.lsp` · `.glb` (pivots on the plug's ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r61 (lib/rounds/elec/), Blender and Godot; the AutoCAD gate waits for AutoCAD to be open.

## History
| version | change |
|---|---|
| 1.0 | elec-r61 (2026-11-20, unattended): first build, generic (ETIM 10.0 EC004667 Discrete electronic component, read as a diode module), our own design; an "etim" line of `inventory elec`, no inventory row; places terminal-plug 2.0 once (x1, 2 poles) |
