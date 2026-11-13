# hmi-7in · v1.1 · operator panel (HMI), 7 in colour touchscreen 800 × 480, 24 V DC, Ethernet, panel cut-out mount (complexes.org generic)

**What** Operator panel for a machine: a 7 in colour touchscreen of 800 × 480 pixels, freely programmable, fed 24 V DC from the panel's control supply, with an Ethernet port to the machine's controller. It goes through a rectangular cut-out in the control panel's door or a console from the front until its bezel seats on the panel's front face, and four clamps behind the panel pull it tight. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC011541, built to the class values below; no maker's datasheet and no product is matched (the vendor file in references/ was not opened).
**Class** device · **Baseline** our own design: generic Display/operator panel (ETIM 10.0 EC011541). The class values are this element's definition (design inputs); the four clamps are placed panel-clamp 1.2 elements (released) in the slot that element defines; the supply terminals are a placed terminal-plug 2.0 (version pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: the cut-out's centre on the panel's front face; the bezel's seating face y = 0, the housing toward +y through the panel, the display toward −y. In a host, `CUTOUT_RECT` (187.0 × 133.0) is the cut-out `library.mount` cuts.
**Built with** toolkit 1.3 · AutoLISP command `HMI7IN` · no parameters · places panel-clamp 1.2 four times (tags `clamp-1` … `clamp-4`) and terminal-plug 2.0 once (tag `x1`, 3 poles).

## Class values
ETIM 10.0 EC011541 "Display/operator panel", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Mounting method (EF000003) | panel mounting: front installation in a cut-out, held by four clamps from behind |
| 2 | Number of pixels, horizontal (EF003099) | 800 |
| 3 | Number of pixels, vertical (EF003100) | 480 |
| 4 | Number of characters per line (EF021776) | not stated (a graphic display: the program sets what it shows) |
| 5 | Number of lines (EF021777) | not stated (as 4) |
| 6 | Freely programmable display (EF024406) | yes |
| 7 | Voltage type (EF000187) | DC |
| 8 | Supply voltage (EF004127) | 24 V |
| 9 | Communication bus (EF005668) | Ethernet |
| 10 | Communications protocol (EF005669) | not stated (the controller's; a version for a named controller states it) |
| 11 | Communication medium wireless (EF024479) | no |
| 12 | Communication medium fibre optic (EF024478) | no |
| 13 | Communication medium copper (EF024477) | yes (twisted pair, the Ethernet port) |
| 14 | Option for configuring controller (EF024405) | no |
| 15 | Degree of protection (IP) (EF005474) | not stated |
| 16 | Explosion-proof (EF004663) | no |
| 17 | With mounting set (EF021778) | yes (the four clamps, placed panel-clamp 1.2) |
| 18 | With PC connection (EF006107) | yes (over the Ethernet port) |
| 19 | Width (EF000008) | 200 mm (the bezel) |
| 20 | Height (EF000040) | 150 mm (the bezel) |
| 21 | Depth (EF000049) | 74.5 mm (8.5 in front of the panel's front face, 66.0 behind it, the supply plug included) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. The panel's power, 10 W, is not a class feature: a design figure (the display's backlight and its controller on the panel's 24 V DC control supply, psu-24v-2a4, within the panel's 24 V budget, ELR-020); its current is derived (I = P / U = 0.42 A). The class-value row of `ratings.csv` reads status "generic design", source "ETIM 10.0 EC011541 class value" with the feature codes (OPERATING.md 12); the power row "design", the current "derived". `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| display | active area 152.46 × 91.48 (x ±76.23, z −39.74 … 51.74), its face 0.5 proud of the bezel (y −8.5 … −8.0) | computed: the 7 in diagonal (177.8 mm, 1 in = 25.4 mm) on the 5:3 aspect of 800 × 480 square pixels, by Pythagoras (width = 177.8 × 5 / √34, height = 177.8 × 3 / √34); its height on the bezel a design choice |
| bezel | 200.0 × 8.0 × 150.0 (x ±100, y −8 … 0, z ±75); its back face y = 0 seats on the panel's front face | design choice (the bezel 8.0 deep keeps every envelope edge at least 8 long, the AutoCAD gate's fillet pre-flight) |
| housing | 186.0 × 50.0 × 132.0 (x ±93, y 0 … 50, z ±66) through the cut-out | design choice |
| panel cut-out | 187.0 × 133.0, centred on the origin (`CUTOUT_RECT`): the housing with 0.5 a side | design choice |
| panel range | 1.0 to 6.0 thick | panel-clamp 1.2 (its panel range, spec.md "The panel range") |
| clamp slots | four, 10.4 (x) × 7.0 (y 23 … 30) × 3.0 deep, blind, in the housing's top wall (z 63 … 66) and bottom wall (z −66 … −63) at x −60 and +60; the slots' rear (bearing) faces at y 30.0 | panel-clamp 1.2 properties.csv: slot_width 10.4, slot_length 7.0, slot_depth_min 3.0, slot_seat_distance 30.0 (read from that element: `library.load("panel-clamp", "1.2")`, its HOOK_Y + 0.4, HOOK_Z + 1.0 and SEAT_Z); their x positions a design choice |
| clamps | panel-clamp 1.2 placed in each slot (tags `clamp-1`, `clamp-2` top at x −60, +60; `clamp-3`, `clamp-4` bottom), the hook's bearing face on the slot's rear face, the body on the wall's outer face (top: z 66 … 74; bottom: z −74 … −66), y 8 … 30 | panel-clamp 1.2 (its frame: x out of the wall, z toward the panel; placed with yaw 90 / roll −90 on top, yaw −90 / roll 90 below); its screw is not built (that element's spec.md) |
| supply plug | terminal-plug 2.0, 3 poles, tag `x1`, mating face on the housing's back face (y 50; body y 50 … 66), x 65 … 80, sockets' axis z −50 (body z −56 … −40.5), poles along −x, wire entries down: 24V 0V FE | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| header | the pins the plug's sockets take, standing out of the back face into the sockets | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures (as xfmr-control 1.0) |
| Ethernet | the socket on the back face | not modelled in 1.0: port-rj45 (lib/inventory.csv made_of) is not built; it is placed in a later version (OPERATING.md 12) |
| status lens | Ø3.2, 0.3 proud, on the bezel at x 88, z −62 (green: powered) | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 60.0 × 12.0 (x −90 … −30, z −68 … −56) on the bezel, 0.1 proud | design choice |
| overall | 200.0 × 74.5 (y −8.5 … 66.0) × 150.0 | from the parts above |

Terminal marks: 24V / 0V the panel supply, FE the functional earth (the housing's and the Ethernet shield's). The marks are labels, a design choice; the plug's own pole marks are 1 … 3 (terminal-plug 2.0 Decals) with these printed on the housing beside it.

## Named nodes
`screen` (emissive: the display lit while the panel is powered) · `led-run` (emissive, green: powered) · the plug's nodes `x1.t-1` … `x1.t-3` (clamp screws, gender none) and `x1.s-1` … `x1.s-3` (sockets, gender female), as terminal-plug 2.0 names them under its tag. The clamps carry no node (panel-clamp 1.2 is one fixed body). Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-BLACK-PA` bezel · `M-GREY-PA` housing · `M-LENS-DARK` display · `M-LENS-GREEN` status lens · `M-WHITE-PA` legend field · `M-ZINC` the placed clamps (panel-clamp 1.2) · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plug (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "hmi-7in", "24 V DC 10 W". Beside the plug on the housing: "24V 0V FE". No maker's name, logo or approval mark.

## Notes and open figures
- One figure of this element's own is open: the supply's under-voltage threshold, the least voltage at which the panel runs (behaviour.csv's `powered` row reads it as "above 0"): NOT ON FILE (B): IEC 61131-2, the 24 V DC class's lower limit, a standard's table asked for once in lib/standards/wanted.md. Everything else it meets is on file (panel-clamp 1.2 and its slot, terminal-plug 2.0) and every other size and value is a design choice, a computed figure or a class value; nothing is guessed and shown as sourced. The placed plug carries its own open line (its clamps' torque, terminal-plug 2.0's behaviour.csv), which behaviour.csv repeats for each pin as that element writes it.
- Not placed in 1.0, though lib/inventory.csv's made_of names them: panel-clamp ×4 and terminal-plug are placed; port-rj45 and led are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). So the Ethernet port is a class value with no socket drawn yet, and the status lens is the toolkit's.
- The clamps' screws are panel-clamp's later version (that element's Mechanism); when it comes, this element pins it.
- Not stated or modelled in 1.0: the degree of protection of the front and the back, the touch technology, the display's brightness and viewing angles, the protocol, the inrush current, the mass, the operating temperature. The phase-1 solver reads no display content, so behaviour.csv carries the supply, the states, the screen and the LED only (its header says so).
- The supply's branch protection is the panel's to provide (the 24 V supply's own, psu-24v-2a4).
- Not a safety-function device: no emergency stop or enabling device is on it (an e-stop beside it is op-estop-22-2nc).

## Outputs (out/)
`hmi-7in.lsp` · `.glb` (pivots on the screen, the LED and the plug's ports, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r38, 1.1 in elec-r47 (lib/rounds/elec/).

## History
| version | change |
|---|---|
| 1.0 | elec-r38 (2026-11-12, unattended): first build, generic (ETIM 10.0 EC011541), our own design; inventory elec pinned 9 (32 systems); places panel-clamp 1.2 four times and terminal-plug 2.0 once (x1, 3 poles) |
| 1.1 | elec-r47 (2026-11-13, unattended), text only (review hmi-7in-1.0 findings 1 to 3, elec-r38 findings 1, 3 and 4a): the Notes name the supply's under-voltage threshold as this element's one open figure, class B (IEC 61131-2), so the count includes it, and no longer say nothing is open; references/source.txt keeps the earlier stub's record verbatim as its end block (from 863cc366^); element.py's comment calls the 7 in the inventory's design input. Geometry, nodes, origin and pins unchanged |
