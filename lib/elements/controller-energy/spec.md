# controller-energy · v1.0 · energy management controller, 1 × RS-485, 1 × Ethernet RJ45, 24 V DC (complexes.org generic)

**What** Energy management controller for a distribution or power-monitoring panel: it reads the plant's meters over one RS-485 port and reports to the plant's network over one Ethernet port; fed 24 V DC, on the 35 mm rail. It has no power path: it carries and switches no load. daq 1.0's stepped moulded housing on the rail clip, two pluggable terminal blocks on its front (x1 the RS-485 port, x2 the supply and its functional earth), one RJ45 socket (x3), two status LEDs and a legend field. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002758, built to the class values below; no maker's datasheet and no product is matched. An "etim" line of `inventory elec` (no inventory row).
**Class** device · **Baseline** our own design: generic Energy management controller (ETIM 10.0 EC002758), a controller with no power path. The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the terminals are placed terminal-plug 2.0 elements and the Ethernet socket a placed port-rj45 1.0 (past station 6; versions pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Class choice** The class's reading is the lane's (elec-r63). lib/standards/etim/classes.csv gives its synonyms as energy saving lighting, motor management and power quality controller, and its twenty features cover two kinds of device: a controller (application, supply, communication interfaces) and a unit that carries the load (number of phases, power, rated operation currents, the reductions it achieves). Built: the controller alone, the form that claims least and that a panel of meters needs; every load-path feature reads "none" below. The id follows OPERATING.md 6: class `controller` (as controller-thyristor), form `energy`; no size or rating is in it because the element has none to tell it from a sibling. The reading and the id are EM's or the core's to overrule (lib/needs-em/elec.md, r63 item 1).
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `CTRLENERGY` · no parameters · places terminal-plug 2.0 twice (tags `x1` 3 poles, `x2` 3 poles) and port-rj45 1.0 once (tag `x3`).

## Class values
ETIM 10.0 EC002758 "Energy management controller", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Application (EF000041) | energy monitoring: reads the meters of a distribution panel and reports to the plant's network |
| 2 | Supply voltage (EF004127) | 24 V |
| 3 | Voltage type (supply voltage) (EF002991) | DC |
| 4 | Number of phases (EF000351) | none (no power path) |
| 5 | Power (EF000076) | none (no power path: it carries and switches no load) |
| 6 | Rated operation current Ie at AC-1 (EF006069) | none (no power path) |
| 7 | Rated operation current Ie at AC-3 (EF006070) | none (no power path) |
| 8 | Rated operation current Ie at AC-15, 400 V (EF008481) | none (no switching output) |
| 9 | Reduction energy consumption (EF008484) | none (it measures and reports; it reduces nothing by itself) |
| 10 | Reduction apparent power (EF008485) | none (as 9) |
| 11 | Reduction reactive power (EF008482) | none (as 9) |
| 12 | Reduction line voltage (EF008486) | none (as 9) |
| 13 | Supporting protocol for CAN (EF003053) | no |
| 14 | Supporting protocol for Modbus (EF003057) | yes (Modbus RTU on the RS-485 port, Modbus TCP on the Ethernet port; the register map is the firmware's, not stated) |
| 15 | With communication interface Ethernet (EF007309) | yes (RJ45, the placed port-rj45 1.0 socket `x3`) |
| 16 | With communication interface RS-232 (EF007312) | no |
| 17 | With communication interface RS-485 (EF007314) | yes (the placed terminal-plug 2.0 `x1`: A, B, COM) |
| 18 | Width (EF000008) | 45 mm |
| 19 | Depth (EF000049) | 93.5 mm (86.0 in front of the rail crown, 7.5 behind it) |
| 20 | Height (EF000040) | 100 mm |

These values are what the element claims: they are the class definition, not a certification, and no approval mark is shown. The protocols (row 14) and the application (row 1) are design inputs: no check and no solver reads them. The supply row of `ratings.csv` reads status "generic design", source "ETIM 10.0 EC002758 class value" with the feature code (OPERATING.md 12). `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Ratings
The class has no feature for the controller's own consumption (its Power, row 5, is the load's). So one figure is a design figure, written with the rule it meets (OPERATING.md 6):

| figure | value | rule |
|---|---|---|
| own power consumption | design: 2.5 W | the controller's own draw from the panel's 24 V control supply, inside the 24 V budget ELR-020 checks; daq 1.0's figure for the same housing and ports |
| supply current | derived: 0.104 A | I = P / U = 2.5 W / 24 V (ratings.csv `load_i`) |

No rating is claimed for the RS-485 port or the Ethernet port beyond what the placed parts state (terminal-plug 2.0: 12 A 250 V, far above a data line; port-rj45 1.0's own spec).

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 45.0 × 40.0 × 100.0 (y −40 … 0, z −50 … 50) on the clip | design choice (daq 1.0's housing) |
| front block | 45.0 × 30.0 × 88.0 (y −70 … −40, z −44 … 44) on the base; 6.0 of the base shows above and below | design choice (daq 1.0's) |
| RS-485 plug | terminal-plug 2.0, 3 poles, tag `x1`, mating face on the front block's face (y −70; body y −86 … −70), x 4 … 19, sockets' axis z 28 (body z 22 … 37.5), poles along +x, wire entries down: A B COM | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| supply plug | terminal-plug 2.0, 3 poles, tag `x2`, mating face on the front block's face, x 4 … 19, sockets' axis z −36 (body z −42 … −26.5): 24V 0V FE | as x1 |
| Ethernet socket | port-rj45 1.0, tag `x3`, front face on the front block's face (y −70), housing behind it in a pocket its own size (16.0 × 21.0 × 14.0, the socket's W, D, H read from that element; the pocket ends 9.0 inside the front block's back): centre x 32, z −32 (x 24 … 40, z −39 … −25); contacts up, latch slot down; 5.0 from the supply plug's body, from the block's right face and from its lower face | port-rj45 1.0 (its spec: the host places it behind its wall with the front face on the wall's outer face and cuts the opening); position a design choice |
| headers | the pins the plugs' sockets take, standing out of the front block into the sockets | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures |
| LEDs | Ø3.2 lenses, 0.3 proud, at z 8: run (green) x 8; error (red) x 16 | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 20.0 × 32.0 (x 22 … 42, z −16 … 16), 0.1 proud | design choice |
| overall | 45.0 × 93.5 (y −86.0 … 7.5) × 100.0 | from the parts above; the plugs stand 16.0 proud of the front block |

Terminal marks: A / B the RS-485 pair, COM its signal common, 24V / 0V the supply, FE the functional earth (the bus cable's shield; the moulded housing takes none). The marks are labels, a design choice; the plugs' own pole marks are 1 … n (terminal-plug 2.0 Decals) with these printed on the legend field.

## Named nodes
`led-run` (emissive, green: the controller is powered and running) · `led-err` (emissive, red: a fault, such as a meter on the bus that does not answer) · the plugs' nodes `x1.t-1` … `x1.t-3`, `x2.t-1` … `x2.t-3` (clamp screws, gender none) and `x1.s-1` … `x1.s-3`, `x2.s-1` … `x2.s-3` (sockets, gender female), as terminal-plug 2.0 names them under its tag · the socket's contacts `x3.c-1` … `x3.c-8` (port nodes, gender female), as port-rj45 1.0 names them under its tag. Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-LENS-GREEN`, `M-LENS-RED` LEDs · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plugs (terminal-plug 2.0) · `M-BLACK-PA`, `M-GOLD`, `M-GASKET` the placed socket (port-rj45 1.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "controller-energy", "RS-485 / LAN", "24 V DC 2.5 W", and the terminal diagram (A B COM; 24V 0V FE). Beside the LEDs: "RUN", "ERR"; beside the socket: "LAN". No maker's name, logo or approval mark.

## Notes and open figures
- One figure of this element's own is open: the supply's under-voltage threshold, the least voltage at which the controller runs (behaviour.csv's `powered` row reads it as "above 0"): NOT ON FILE (B): IEC 61131-2, the 24 V DC class's lower limit, a standard's table asked for once in lib/standards/wanted.md. Everything else it meets is on file (the rail clip, terminal-plug 2.0, port-rj45 1.0) and every other size and value is a design choice, a derived figure or a class value; nothing is guessed and shown as sourced. The placed plugs carry their own open line (their clamps' torque, terminal-plug 2.0's behaviour.csv), which behaviour.csv repeats for each pin as that element writes it; the placed socket carries its own (its mating face, port-rj45 1.0's spec).
- The RS-485 port is named by the class feature (row 17). The standard that defines its levels, its termination and its bus length is not in lib/standards/sources.csv, so no conformance to it is claimed and no termination resistor is drawn or stated.
- din-clip-35 and led are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). It holds to the rail by the toolkit's rail clip, and its LEDs are the toolkit's lenses.
- The RS-485 bus and the Ethernet link are data, not circuits the phase-1 solver reads: behaviour.csv carries the supply, the states and the LEDs only (its header says so); the RS-485 terminals and the socket's contacts are port nodes the twin's probe can touch.
- Not stated or modelled in 1.0: the number of meters it reads, the bus speed, the register map, the logging memory, the isolation between the ports and the supply, the degree of protection, the operating temperature and the mass.
- The supply's branch protection is the panel's to provide (the 24 V supply's own, psu-24v-2a4).
- Not a safety-function device, and not a revenue meter: it measures nothing itself.

## Outputs (out/)
`controller-energy.lsp` · `.glb` (pivots on the LEDs, the plugs' ports and the socket's contacts, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r63 (lib/rounds/elec/), Blender and Godot; the AutoCAD gate waits for AutoCAD to be open.

## History
| version | change |
|---|---|
| 1.0 | elec-r63 (2026-11-20, unattended): first build, generic (ETIM 10.0 EC002758, read by the lane as the controller alone, no power path), our own design; an "etim" line of inventory elec; places terminal-plug 2.0 twice (x1 3 poles, x2 3 poles) and port-rj45 1.0 once (x3) |
