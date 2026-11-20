# term-dist-12a-1p · v1.0 · distribution terminal block, one potential on six plug-in screw clamps, 12 A 250 V, 35 mm rail (complexes.org generic)

**What** A distribution block on the rail: six screw clamps joined by one bar, so one wire in gives five wires out at the same potential (a panel's 24 V DC or 0 V fanned out to its devices, a neutral shared by several circuits). diode-rail-3a 1.0's stepped moulded housing at twice its width on the rail clip, one pluggable six-pole terminal block at the foot of its front and a legend field above it. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000276, built to the class values below; no maker's datasheet and no product is matched. It has no inventory row: EC000276 is one of the "etim" lines `python lib/build.py inventory elec` lists once no row above them builds unattended.
**Class** device · **Baseline** our own design: generic Distribution terminal block (ETIM 10.0 EC000276). The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the clamps are a placed terminal-plug 2.0 element (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `TERMDIST` · no parameters · places terminal-plug 2.0 once (tag `x1`, 6 poles).

## Class choice
EC000276 "Distribution terminal block" has three features on file (lib/standards/etim/class-features.csv) and lib/standards/etim/classes.csv gives its synonyms as clamp, clip, connection clamp, connection rail, connection terminal, earthing rail for distribution board and neutral busbar. The lane read the class in the form a control panel uses: one rail-mounted housing whose clamps all share one bar. "Number of poles" is read as the number of separate potentials (one), not the number of clamps (six). That reading, the id (`term` the class word, `dist` the form, `12a` the rating, `1p` the one potential; OPERATING.md 6) and the two ratings below are the lane's, EM's or the core's to overrule (lib/needs-em/elec.md, r62).

## Class values
ETIM 10.0 EC000276 "Distribution terminal block", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Core cross section (EF000018) | not stated (the conductor range of the placed plug's clamps is that element's open line, class B: Notes) |
| 2 | Number of poles (EF001391) | 1 (one potential: six clamps on one bar) |
| 3 | With seal head (EF000277) | no |

These values are what the element claims: they are the class definition, not a certification, and no approval mark is shown. The class-value row of `ratings.csv` reads status "generic design", source "ETIM 10.0 EC000276 class value" with the feature code (OPERATING.md 12).

## Ratings
The class has no rating feature, so the two ratings are design figures (OPERATING.md 6, "design: <value> (<the rule it meets>)"), written in `ratings.csv` with status "design":

| rating | value | the rule it meets |
|---|---|---|
| current, through any one clamp and through the bar | 12 A | not above the 12 A of the placed terminal-plug 2.0 (ETIM 10.0 EC002021 class value, Rated current In, EF008250). The feeding wire comes in through one clamp, so the block as a whole carries no more than one clamp does: the five outgoing wires share 12 A |
| voltage, the bar to the rail | 250 V | not above the 250 V of the placed terminal-plug 2.0 (ETIM 10.0 EC002021 class value, Rated voltage, EF000228) |

No short-circuit, temperature-rise or insulation figure is stated: none is a feature of the class and no standard on file fixes one.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 36.0 × 40.0 × 80.0 (y −40 … 0, z −40 … 40) on the clip | design choice (diode-rail-3a 1.0's housing at twice its width) |
| front block | 36.0 × 20.0 × 68.0 (y −60 … −40, z −34 … 34) on the base; 6.0 of the base shows above and below | design choice |
| plug | terminal-plug 2.0, 6 poles, tag `x1`, mating face on the front block's face (y −60; body y −76 … −60), x 3 … 33, sockets' axis z −22 (body z −28 … −12.5), poles along +x, wire entries down: 1 2 3 4 5 6 | terminal-plug 2.0 (its own spec; 12 A 250 V, this element's 12 A and 250 V); placement a design choice |
| header and bar | the six pins the plug's sockets take, standing out of the front block into the sockets, and the bar inside that joins them | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures; the bar's section is not stated |
| legend field | 30.0 × 28.0 (x 3 … 33, z 0 … 28), 0.1 proud | design choice |
| overall | 36.0 × 83.5 (y −76.0 … 7.5) × 80.0 | from the parts above; the plug stands 16.0 proud of the front block |

Terminal marks: 1 to 6 from the left, the plug's own pole marks (terminal-plug 2.0 Decals); a design choice. Any clamp may take the feeding wire.

## Named nodes
The plug's nodes `x1.t-1` … `x1.t-6` (clamp screws, gender none) and `x1.s-1` … `x1.s-6` (sockets, gender female), as terminal-plug 2.0 names them under its tag. Nothing moves and nothing lights. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plug (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "term-dist-12a-1p", one line joining six dots numbered 1 to 6 (the bar), "12 A", "250 V". No maker's name, logo or approval mark.

## Notes and open figures
- This element has no open figure of its own: everything it meets is on file (the rail clip, terminal-plug 2.0) and every other size and value is a design choice, a design figure with its rule, or a class value; nothing is guessed and shown as sourced. The placed plug carries its own open line (its clamps' conductor range and torque, terminal-plug 2.0's spec.md and behaviour.csv: a document wanted, IEC 60999), which behaviour.csv repeats for each pin as that element writes it; that is why class value 1 reads "not stated".
- What the solver reads: the six pins are one conductor (five `always` contact rows through the part `bar`, term-jumper 2.0's form), ideal in phase 1; no resistance is given since the bar is not modelled and its section is not stated.
- The block's 12 A is the feeding clamp's: a panel that needs more than 12 A in total on one potential wants a larger block (a later element of this class, with clamps of a larger rating once one is on file).
- lib/inventory.csv has no row for this element (an "etim" line): din-clip-35, which a rail device of this kind would place, is not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). It holds to the rail by the toolkit's rail clip.
- Not stated or modelled in 1.0: the bar and the header, the insulation between the bar and the rail, a cover over the clamps, the degree of protection, the operating temperature and the mass. Not a protective earth bar: no bond to the rail is made or claimed.
- Not a safety-function device.

## Outputs (out/)
`term-dist-12a-1p.lsp` · `.glb` (pivots on the plug's ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r62 (lib/rounds/elec/), Blender and Godot; the AutoCAD gate waits for AutoCAD to be open.

## History
| version | change |
|---|---|
| 1.0 | elec-r62 (2026-11-20, unattended): first build, generic (ETIM 10.0 EC000276 Distribution terminal block, read as one potential on six clamps), our own design; an "etim" line of `inventory elec`, no inventory row; places terminal-plug 2.0 once (x1, 6 poles) |
