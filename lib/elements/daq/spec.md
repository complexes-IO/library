# daq · v1.0 · data acquisition module, 4 differential AI, 0-10 V / 4-20 mA, 16 bit, 1 × Ethernet RJ45, 24 V DC (complexes.org generic)

**What** Data acquisition module for a test bench, a monitoring rig or an edge node: four differential analogue inputs, each set by the configuration to 0 … 10 V or 4 … 20 mA, 16-bit resolution, read by a computer or a controller over one Ethernet port; fed 24 V DC, on the 35 mm rail. plc-aio 1.1's stepped moulded housing on the rail clip, two pluggable terminal blocks on its front (x1 the inputs, x2 the supply and its functional earth), one RJ45 socket (x3), two status LEDs and a legend field. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001596, built to the class values below; no maker's datasheet and no product is matched (the vendor file in references/ was not opened). Inventory row daq (7 systems: calibration-bench, condition-monitoring-rig, iiot-edge-node, power-monitoring-panel, test-bench-hydraulic, test-bench-pneumatic, test-rig-cylinder).
**Class** device · **Baseline** our own design: generic Fieldbus, decentr. periphery - analogue I/O module (ETIM 10.0 EC001596), a data acquisition module. The class values are this element's definition (design inputs); the rail clip is the library's contract (toolkit/din.py `rail_clip`, the 35 × 7.5 rail of din-rail-35, EN 60715 TH35-7.5); the terminals are placed terminal-plug 2.0 elements and the Ethernet socket a placed port-rj45 1.0 (past station 6; versions pinned); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md). The folder held the core's inventory stub; its record is kept verbatim as the end block of references/source.txt and nothing here is taken from it.
**Class choice** lib/inventory.csv's row daq names no ETIM class and lib/standards/etim/classes.csv has no class named for data acquisition. The lane chose EC001596 (elec-r57): a module that reads analogue signals at the machine and hands them to a computer over a network is ETIM's decentralised-periphery analogue module, the fieldbus sibling of plc-aio's EC001420; its features cover what a data acquisition module states (inputs, their signals and resolution, the network interfaces and protocols, the supply, the mounting). The row's etim cell is the core's to write.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (in a BOM, y = the rail's y − 7.5).
**Built with** toolkit 1.3 · AutoLISP command `DAQ` · no parameters · places terminal-plug 2.0 twice (tags `x1` 8 poles, `x2` 3 poles) and port-rj45 1.0 once (tag `x3`).

## Class values
ETIM 10.0 EC001596 "Fieldbus, decentr. periphery - analogue I/O module", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Supply voltage AC 50 Hz (EF007532) | none (DC supply only) |
| 2 | Supply voltage AC 60 Hz (EF007533) | none (DC supply only) |
| 3 | Supply voltage DC (EF007534) | 24 V |
| 4 | Voltage type (supply voltage) (EF002991) | DC |
| 5 | Power consumption (EF000346) | 2.5 W (from the 24 V DC supply) |
| 6 | Input, current (EF003204) | yes: 4 … 20 mA |
| 7 | Input, voltage (EF003205) | yes: 0 … 10 V |
| 8 | Input, resistor (EF003206) | no |
| 9 | Input, resistance thermometer (EF003207) | no |
| 10 | Input, thermocouple (EF003208) | no |
| 11 | Input signal, configurable (EF003209) | yes (items 6 and 7, per channel) |
| 12 | Resolution of the analogue inputs (EF003575) | 16 bit |
| 13 | Output, current (EF003212) | no (no analogue output) |
| 14 | Output, voltage (EF003213) | no (no analogue output) |
| 15 | Output signal configurable (EF003214) | no (no analogue output) |
| 16 | Resolution of the analogue outputs (EF003577) | none (no analogue output) |
| 17 | Number of analogue inputs (EF001994) | 4 (differential, AI0 … AI3) |
| 18 | Number of analogue outputs (EF001995) | 0 |
| 19 | Analogue inputs configurable (EF008518) | yes (each input voltage or current, by the configuration) |
| 20 | Analogue outputs configurable (EF008519) | no (no analogue output) |
| 21 | Number of HW-interfaces industrial Ethernet (EF003020) | 1 (RJ45, the placed port-rj45 1.0 socket `x3`) |
| 22 | Number of interfaces PROFINET (EF006932) | 0 |
| 23 | Number of HW-interfaces RS-232 (EF003021) | 0 |
| 24 | Number of HW-interfaces RS-422 (EF003022) | 0 |
| 25 | Number of HW-interfaces RS-485 (EF003023) | 0 |
| 26 | Number of HW-interfaces serial TTY (EF003024) | 0 |
| 27 | Number of HW-interfaces parallel (EF003026) | 0 |
| 28 | Number of HW-interfaces wireless (EF006933) | 0 |
| 29 | Number of HW-interfaces USB (EF003025) | 0 |
| 30 | Number of HW-interfaces other (EF003027) | 0 |
| 31 | Supporting protocol for EtherCAT (EF017564) | no |
| 32 | Supporting protocol for TCP/IP (EF003050) | yes (the readings are served over TCP/IP on the Ethernet port) |
| 33 | Supporting protocol for PROFIBUS (EF003052) | no |
| 34 | Supporting protocol for CAN (EF003053) | no |
| 35 | Supporting protocol for INTERBUS (EF003054) | no |
| 36 | Supporting protocol for ASI (EF003051) | no |
| 37 | Supporting protocol for KNX (EF003055) | no |
| 38 | Supporting protocol for Modbus (EF003057) | yes (Modbus TCP, the readings as input registers; the register map is the firmware's, not stated) |
| 39 | Supporting protocol for Data-Highway (EF003058) | no |
| 40 | Supporting protocol for DeviceNet (EF003059) | no |
| 41 | Supporting protocol for SUCONET (EF003060) | no |
| 42 | Supporting protocol for LON (EF003017) | no |
| 43 | Supporting protocol for PROFINET IO (EF007525) | no |
| 44 | Supporting protocol for PROFINET CBA (EF007524) | no |
| 45 | Supporting protocol for SERCOS (EF006657) | no |
| 46 | Supporting protocol for Foundation Fieldbus (EF007522) | no |
| 47 | Supporting protocol for EtherNet/IP (EF007521) | no |
| 48 | Supporting protocol for AS-Interface Safety at Work (EF007519) | no |
| 49 | Supporting protocol for DeviceNet Safety (EF007520) | no |
| 50 | Supporting protocol for INTERBUS-Safety (EF006662) | no |
| 51 | Supporting protocol for PROFIsafe (EF007526) | no (not suitable for safety functions, 69) |
| 52 | Supporting protocol for SafetyBUS p (EF007527) | no |
| 53 | Supporting protocol for other bus systems (EF003062) | no |
| 54 | Radio standard Bluetooth (EF007178) | no |
| 55 | Radio standard WLAN 802.11 (EF007179) | no |
| 56 | Radio standard GPRS (EF008523) | no |
| 57 | Radio standard GSM (EF008524) | no |
| 58 | Mobile communications standard 3G (UMTS) (EF008525) | no |
| 59 | IO link master (EF007298) | no |
| 60 | System accessory (EF004118) | no (a device on its own) |
| 61 | Degree of protection (IP) (EF005474) | not stated |
| 62 | Degree of protection (NEMA) (EF011959) | not stated |
| 63 | Type of electric connection (EF003961) | screw connection on pluggable terminal blocks (terminal-plug 2.0, two placed) |
| 64 | Fieldbus connection over separate bus coupler possible (EF004002) | no (the Ethernet port is its own) |
| 65 | Suitable for rail mounting (EF003972) | yes (35 mm rail, EN 60715 TH35-7.5) |
| 66 | Wall mounting/direct mounting (EF007020) | no |
| 67 | Front built-in possible (EF007016) | no |
| 68 | Rack-assembly possible (EF007018) | no |
| 69 | Suitable for safety functions (EF001597) | no |
| 70 | SIL according to IEC 61508 (EF009889) | none (not a safety device) |
| 71 | Performance level according to EN ISO 13849-1 (EF007399) | none (not a safety device) |
| 72 | Appendant operation agent (Ex ia) (EF004141) | no |
| 73 | Appendant operation agent (Ex ib) (EF004142) | no |
| 74 | Explosion safety category for gas (EF003997) | none |
| 75 | Explosion safety category for dust (EF003998) | none |
| 76 | Certified for U-L hazardous location class I (EF017622) | no |
| 77 | Certified for U-L hazardous location class II (EF017625) | no |
| 78 | Certified for U-L hazardous location class III (EF017627) | no |
| 79 | Certified for U-L hazardous location division 1 (EF017628) | no |
| 80 | Certified for U-L hazardous location division 2 (EF017629) | no |
| 81 | Certified for U-L hazardous location group A (acetylene) (EF017632) | no |
| 82 | Certified for U-L hazardous location group B (hydrogen) (EF017633) | no |
| 83 | Certified for U-L hazardous location group C (ethylene) (EF017635) | no |
| 84 | Certified for U-L hazardous location group D (propane) (EF017636) | no |
| 85 | Certified for U-L hazardous location group E (metal dusts) (EF017637) | no |
| 86 | Certified for U-L hazardous location group F (carbonaceous dusts) (EF017638) | no |
| 87 | Certified for U-L hazardous location group G (non-conductive dusts) (EF017639) | no |
| 88 | Width (EF000008) | 45 mm |
| 89 | Height (EF000040) | 100 mm |
| 90 | Depth (EF000049) | 93.5 mm (86.0 in front of the rail crown, 7.5 behind it) |

In rows 76 to 87 ETIM's feature name joins the two letters of the certifier's name; they are written apart here so DOC-006 does not read them as an approval mark (as ipc 1.0's row 47). The element carries no certification of any kind.

These values are what the element claims: they are the class definition, not a certification, and no approval mark is shown. The signal ranges 0 … 10 V and 4 … 20 mA are this element's design inputs (the ranges a machine's analogue sensors use; pt, tt-rtd and flow-meter give 4 … 20 mA); IEC 61131-2, which names analogue input ranges, is not in lib/standards/sources.csv, so no conformance to it is claimed. The protocols (rows 32 and 38) are design inputs too: no check and no solver reads them. The class-value rows of `ratings.csv` read status "generic design", source "ETIM 10.0 EC001596 class value" with the feature code (OPERATING.md 12); the current row "derived" (I = P / U = 0.104 A). `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| rail clip | two lips behind the back face over the rail's 35 mm (z ±17.5 … ±19.5), 7.5 deep, release tab below | toolkit/din.py `rail_clip` (the library's contract for the TH35-7.5 rail, din-rail-35) |
| housing base | 45.0 × 40.0 × 100.0 (y −40 … 0, z −50 … 50) on the clip | design choice (plc-aio 1.1's housing) |
| front block | 45.0 × 30.0 × 88.0 (y −70 … −40, z −44 … 44) on the base; 6.0 of the base shows above and below | design choice (plc-aio 1.1's) |
| input plug | terminal-plug 2.0, 8 poles, tag `x1`, mating face on the front block's face (y −70; body y −86 … −70), x 2.5 … 42.5, sockets' axis z 28 (body z 22 … 37.5), poles along +x, wire entries down: AI0+ AI0− AI1+ AI1− AI2+ AI2− AI3+ AI3− | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| supply plug | terminal-plug 2.0, 3 poles, tag `x2`, mating face on the front block's face, x 4 … 19, sockets' axis z −36 (body z −42 … −26.5): 24V 0V FE | as x1 |
| Ethernet socket | port-rj45 1.0, tag `x3`, front face on the front block's face (y −70), housing behind it in a pocket its own size (16.0 × 21.0 × 14.0, the socket's W, D, H read from that element; the pocket ends 9.0 inside the front block's back): centre x 32, z −32 (x 24 … 40, z −39 … −25); contacts up, latch slot down; 5.0 from the supply plug's body, from the block's right face and from its lower face | port-rj45 1.0 (its spec: the host places it behind its wall with the front face on the wall's outer face and cuts the opening); position a design choice |
| headers | the pins the plugs' sockets take, standing out of the front block into the sockets | not modelled in 1.0: terminal-plug 2.0 gives the header pin (1.0 × 1.0, at most 5.0 past the mating face, its spec.md), so a later version can model it to those figures |
| LEDs | Ø3.2 lenses, 0.3 proud, at z 8: run (green) x 8; error (red) x 16 | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 20.0 × 32.0 (x 22 … 42, z −16 … 16), 0.1 proud | design choice |
| overall | 45.0 × 93.5 (y −86.0 … 7.5) × 100.0 | from the parts above; the plugs stand 16.0 proud of the front block |

Terminal marks: AI<n>+ / AI<n>− the differential inputs, 24V / 0V the module supply, FE the functional earth (the analogue cables' shields; the moulded housing takes none). The marks are labels, a design choice; the plugs' own pole marks are 1 … n (terminal-plug 2.0 Decals) with these printed on the legend field.

## Named nodes
`led-run` (emissive, green: the module is powered and running) · `led-err` (emissive, red: a channel fault, an input outside its range or an open 4 … 20 mA loop) · the plugs' nodes `x1.t-1` … `x1.t-8`, `x2.t-1` … `x2.t-3` (clamp screws, gender none) and `x1.s-1` … `x1.s-8`, `x2.s-1` … `x2.s-3` (sockets, gender female), as terminal-plug 2.0 names them under its tag · the socket's contacts `x3.c-1` … `x3.c-8` (port nodes, gender female), as port-rj45 1.0 names them under its tag. Nothing moves. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing and rail clip · `M-LENS-GREEN`, `M-LENS-RED` LEDs · `M-WHITE-PA` legend field · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plugs (terminal-plug 2.0) · `M-BLACK-PA`, `M-GOLD`, `M-GASKET` the placed socket (port-rj45 1.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "daq", "4 AI", "0-10 V / 4-20 mA", "16 bit", "24 V DC 2.5 W", and the terminal diagram (AI0± … AI3±; 24V 0V FE). Beside the LEDs: "RUN", "ERR"; beside the socket: "LAN". No maker's name, logo or approval mark.

## Notes and open figures
- One figure of this element's own is open: the supply's under-voltage threshold, the least voltage at which the module runs (behaviour.csv's `powered` row reads it as "above 0"): NOT ON FILE (B): IEC 61131-2, the 24 V DC class's lower limit, a standard's table asked for once in lib/standards/wanted.md. Everything else it meets is on file (the rail clip, terminal-plug 2.0, port-rj45 1.0) and every other size and value is a design choice, a derived figure or a class value; nothing is guessed and shown as sourced. The placed plugs carry their own open line (their clamps' torque, terminal-plug 2.0's behaviour.csv), which behaviour.csv repeats for each pin as that element writes it; the placed socket carries its own (its mating face, port-rj45 1.0's spec).
- lib/inventory.csv's made_of: terminal-plug is placed (twice) and the Ethernet socket is a placed port-rj45 1.0; din-clip-35 and led are not built yet, and a host places only common parts past station 6 and models no holes for a part it will place later (OPERATING.md 12, quality at the source). It holds to the rail by the toolkit's rail clip, and its LEDs are the toolkit's lenses.
- The Ethernet link is data, not a circuit the phase-1 solver reads, and the solver reads no analogue signal: behaviour.csv carries the supply, the states and the LEDs only (its header says so); the input terminals and the socket's contacts are port nodes the twin's probe can touch.
- Not stated or modelled in 1.0: the inputs' impedance and the current inputs' burden, the sampling rate, the accuracy, the isolation between channels and to the supply and the network, the inputs' overload limits, the register map, the degree of protection, the operating temperature and the mass.
- The supply's branch protection is the panel's to provide (the 24 V supply's own, psu-24v-2a4).
- Not a safety-function device (Class values 69 to 71).

## Outputs (out/)
`daq.lsp` · `.glb` (pivots on the LEDs, the plugs' ports and the socket's contacts, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r57 (lib/rounds/elec/), Blender and Godot; the AutoCAD gate waits for AutoCAD to be open.

## History
| version | change |
|---|---|
| 1.0 | elec-r57 (2026-11-20, unattended): first build, generic (ETIM 10.0 EC001596, the lane's class choice), our own design; inventory elec, 7 systems; places terminal-plug 2.0 twice (x1 8 poles, x2 3 poles) and port-rj45 1.0 once (x3); the folder's stub record kept as source.txt's end block |
