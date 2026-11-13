# ipc · v1.0 · industrial PC, box, fanless, 24 V DC, 2 × Ethernet RJ45, wall mounting (complexes.org generic)

**What** Industrial PC in a box housing for a machine's cabinet or a wall: a fanless computer fed 24 V DC from the panel's control supply, with two Ethernet ports to the machine's controller and the plant network, fixed by four screws through its back plate. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001413, built to the class values below; no maker's datasheet and no product is matched (the vendor file in references/ was not opened). Inventory row ipc (9 systems: cmm, condition-monitoring-rig, hil-commissioning-bench, iiot-edge-node, laser-cutter-fiber, laser-cutter-sheet, press-brake-cnc, server-rack, vision-inspection-station).
**Class** device · **Baseline** our own design: generic Industrial PC (ETIM 10.0 EC001413), box form. The class values are this element's definition (design inputs); the two Ethernet sockets are placed port-rj45 1.0 elements (past station 6), the supply terminals a placed terminal-plug 2.0 (versions pinned); the fixing holes are ISO 273 medium clearance for M4; every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md). The folder held the core's inventory stub; its record is kept verbatim as the end block of references/source.txt and nothing here is taken from it.
**Units / frame** mm, Z up. Origin: the back plate's back face on the wall y = 0, x = 0 and z = 0 on the housing's centre; the body toward −y; the front face (sockets, plug, lenses) at y = −148.
**Built with** toolkit 1.3 · AutoLISP command `IPC` · no parameters · places port-rj45 1.0 twice (tags `x2`, `x3`) and terminal-plug 2.0 once (tag `x1`, 3 poles).

## Class values
ETIM 10.0 EC001413 "Industrial PC", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Supply voltage AC 50 Hz (EF007532) | none (DC supply only) |
| 2 | Supply voltage AC 60 Hz (EF007533) | none (DC supply only) |
| 3 | Supply voltage DC (EF007534) | 24 V |
| 4 | Voltage type (supply voltage) (EF002991) | DC |
| 5 | Number of HW-interfaces industrial Ethernet (EF003020) | 2 (RJ45, the placed port-rj45 1.0 sockets `x2`, `x3`) |
| 6 | Number of interfaces PROFINET (EF006932) | 0 (no PROFINET-specific interface; a protocol on the Ethernet ports is the software's) |
| 7 | Number of HW-interfaces RS-232 (EF003021) | 0 |
| 8 | Number of HW-interfaces RS-422 (EF003022) | 0 |
| 9 | Number of HW-interfaces RS-485 (EF003023) | 0 |
| 10 | Number of HW-interfaces serial TTY (EF003024) | 0 |
| 11 | Number of HW-interfaces USB (EF003025) | 0 in 1.0 (no USB socket element is on file; a later version places one) |
| 12 | Number of HW-interfaces parallel (EF003026) | 0 |
| 13 | Number of HW-interfaces wireless (EF006933) | 0 |
| 14 | Number of HW-interfaces other (EF003027) | 0 |
| 15 | Supporting protocol for PROFIBUS (EF003052) | no |
| 16 | Supporting protocol for CAN (EF003053) | no |
| 17 | Supporting protocol for EtherCAT (EF017564) | not stated (an Ethernet protocol: the installed software's) |
| 18 | Supporting protocol for INTERBUS (EF003054) | no |
| 19 | Supporting protocol for ASI (EF003051) | no |
| 20 | Supporting protocol for KNX (EF003055) | no |
| 21 | Supporting protocol for Modbus (EF003057) | not stated (Modbus TCP on the Ethernet ports is the installed software's) |
| 22 | Supporting protocol for Data-Highway (EF003058) | no |
| 23 | Supporting protocol for DeviceNet (EF003059) | no |
| 24 | Supporting protocol for SUCONET (EF003060) | no |
| 25 | Supporting protocol for LON (EF003017) | no |
| 26 | Supporting protocol for PROFINET IO (EF007525) | not stated (as 17) |
| 27 | Supporting protocol for PROFINET CBA (EF007524) | not stated (as 17) |
| 28 | Supporting protocol for SERCOS (EF006657) | not stated (as 17) |
| 29 | Supporting protocol for Foundation Fieldbus (EF007522) | no |
| 30 | Supporting protocol for EtherNet/IP (EF007521) | not stated (as 17) |
| 31 | Supporting protocol for AS-Interface Safety at Work (EF007519) | no |
| 32 | Supporting protocol for DeviceNet Safety (EF007520) | no |
| 33 | Supporting protocol for INTERBUS-Safety (EF006662) | no |
| 34 | Supporting protocol for PROFIsafe (EF007526) | no (not suitable for safety functions, 79) |
| 35 | Supporting protocol for SafetyBUS p (EF007527) | no |
| 36 | Supporting protocol for other bus systems (EF003062) | no |
| 37 | Radio standard Bluetooth (EF007178) | no |
| 38 | Radio standard WLAN 802.11 (EF007179) | no |
| 39 | Radio standard GPRS (EF008523) | no |
| 40 | Radio standard GSM (EF008524) | no |
| 41 | Mobile communications standard 3G (UMTS) (EF008525) | no |
| 42 | IO link master (EF007298) | no |
| 43 | Suitable for operating system Windows 9x (EF003041) | not stated (the element is the hardware; the operating system is the installed software's) |
| 44 | Suitable for operating system Windows 2000 (EF003043) | not stated (as 43) |
| 45 | Suitable for operating system Windows XP (EF003044) | not stated (as 43) |
| 46 | Suitable for operating system Windows ME (EF003045) | not stated (as 43) |
| 47 | Suitable for operating system Windows C-E (EF003046; ETIM's name joins the two letters, written apart here so DOC-006 does not read them as an approval mark) | not stated (as 43) |
| 48 | Suitable for operating system Linux (EF003047) | not stated (as 43) |
| 49 | Suitable for operating system Windows Vista (EF007091) | not stated (as 43) |
| 50 | Suitable for operating system Windows 2003 Server (EF007090) | not stated (as 43) |
| 51 | Suitable for operating system Windows 7 (EF008526) | not stated (as 43) |
| 52 | Suitable for operating system Windows 8 (EF009923) | not stated (as 43) |
| 53 | Suitable for other operating system (EF003048) | not stated (as 43) |
| 54 | Preinstalled operating system (EF007535) | none |
| 55 | Max. main memory (EF003123) | not stated |
| 56 | Degree of protection (IP) (EF005474) | not stated |
| 57 | Degree of protection (NEMA) (EF011959) | not stated |
| 58 | Operating temperature (EF002393) | not stated |
| 59 | Construction type housing (EF004008) | box PC (wall mounting on its back plate) |
| 60 | With hard disc (EF002000) | no |
| 61 | Processor type (EF003122) | not stated |
| 62 | Processor clock rate (EF011957) | not stated |
| 63 | With graphic card (EF003130) | no |
| 64 | With sound card (EF003131) | no |
| 65 | With optical drive (EF012515) | no |
| 66 | With floppy disc drive (EF003128) | no |
| 67 | Number of free AGP-slots (EF003133) | 0 |
| 68 | Number of free PCI-slots (EF003134) | 0 |
| 69 | Number of free PCIe-slots (EF017219) | 0 |
| 70 | With other storage media (EF003129) | not stated |
| 71 | Number of free ISA-slots (EF003135) | 0 |
| 72 | Number of free PCMCIA-slots (EF003136) | 0 |
| 73 | Number of other free slots (EF003137) | 0 |
| 74 | Suitable for rail mounting (EF003972) | no |
| 75 | Wall mounting/direct mounting (EF007020) | yes (four M4 screws through the back plate) |
| 76 | Front built-in possible (EF007016) | no |
| 77 | Rack-assembly possible (EF007018) | no |
| 78 | Number of storage media bays (EF011958) | 0 |
| 79 | Suitable for safety functions (EF001597) | no |
| 80 | Width (EF000008) | 110 mm (the back plate; the housing 80) |
| 81 | Height (EF000040) | 240 mm (the back plate; the housing 200) |
| 82 | Depth (EF000049) | 164 mm (back plate 8, housing 140, the supply plug 16 in front) |
| 83 | Memory capacity hard disc (EF004682) | none (no hard disc, 60) |

These values are what the element claims: they are the class definition, not a certification, and no approval mark is shown. The "not stated" rows are what a PC's software, its board's figures or a test would state (protocols, operating systems, memory, processor, degree of protection, temperature): none of them is a figure this element's geometry or the phase-1 solver reads, so none is open. The PC's power, 24 W, is not a class feature: a design figure (a fanless box PC's board, processor, memory and storage on the panel's 24 V DC control supply, psu-24v-2a4, within the panel's 24 V budget, ELR-020); its current is derived (I = P / U = 1.00 A). The class-value row of `ratings.csv` reads status "generic design", source "ETIM 10.0 EC001413 class value" with the feature codes (OPERATING.md 12); the power row "design", the current "derived". `pins.csv` gives each terminal its role; `behaviour.csv` what the solver reads.

## Dimensions
| item | value | source |
|---|---|---|
| back plate | 110.0 × 8.0 × 240.0 (x ±55, y −8 … 0, z ±120), anodised aluminium, its back face on the wall | design choice (the housing's heat spreader; 8.0 thick keeps every envelope edge at least 8 long, the AutoCAD gate's fillet pre-flight) |
| fixing holes | 4 × Ø4.5 through the back plate at x ±47.5, z ±110 (95 × 220), beyond the housing; position Ø0.5 (features.csv) | ISO 273 medium clearance for M4 (lib/standards/holes.csv); the pattern a design choice; position Ø0.5 = H − F (GDT-010). The screws (the inventory's screw-iso7380 x4, M4 the design's size) are not built, so not placed; 7.5 lies between a hole's centre and the housing for the screw's head |
| housing | 80.0 × 140.0 × 200.0 (x ±40, y −148 … −8, z ±100), aluminium RAL 7035 | design choice |
| Ethernet sockets | port-rj45 1.0 placed twice, front face on the housing's front face (y −148), housing behind it in a pocket its own size (16.0 × 21.0 × 14.0, the socket's W, D, H read from that element): `x2` (LAN1) at x −12, `x3` (LAN2) at x +12, both z 50; contacts up, latch slot down | port-rj45 1.0 (its spec: the host places it behind its wall with the front face on the wall's outer face and cuts the opening); positions a design choice |
| supply plug | terminal-plug 2.0, 3 poles, tag `x1`, mating face on the housing's front face (y −148; body y −164 … −148), x −7.5 … 7.5, sockets' axis z −75, poles along +x, wire entries down: 24V 0V FE | terminal-plug 2.0 (its own spec; 12 A 250 V); placement a design choice |
| header | the pins the plug's sockets take, standing out of the front face into the sockets | not modelled in 1.0 (inside the plug; terminal-plug 2.0 gives the header pin, 1.0 × 1.0, at most 5.0 past the mating face) |
| status lenses | Ø3.2, 0.3 proud, at z 88: x −30 green (`led-pwr`: powered), x −22 yellow (`led-run`: running) | design choice (toolkit/din.py `led`; the led element is not built yet) |
| legend field | 44.0 × 12.0 (x −10 … 34, z 82 … 94), 0.1 proud | design choice |
| overall | 110.0 × 164.0 (y −164 … 0) × 240.0 | from the parts above |

Terminal marks: 24V / 0V the PC supply, FE the functional earth (the housing's). The marks are labels, a design choice; the plug's own pole marks are 1 … 3 (terminal-plug 2.0 Decals) with these printed on the housing beside it.

## Named nodes
`led-pwr` (emissive, green: powered) · `led-run` (emissive, yellow: running) · the plug's nodes `x1.t-1` … `x1.t-3` (clamp screws, gender none) and `x1.s-1` … `x1.s-3` (sockets, gender female), as terminal-plug 2.0 names them under its tag · the sockets' contacts `x2.c-1` … `x2.c-8` and `x3.c-1` … `x3.c-8` (port nodes, gender female), as port-rj45 1.0 names them under its tags. Nothing moves. pins.csv names what each supply terminal carries.

## Materials by layer
`M-ALU-ANOD` back plate · `M-ALU-7035` housing · `M-LENS-GREEN`, `M-LENS-YELLOW` status lenses · `M-WHITE-PA` legend field · `M-GASKET` the fixing holes' cut · `M-BLACK-PA`, `M-GOLD` the placed sockets (port-rj45 1.0) · `M-GREEN`, `M-ZINC`, `M-GASKET` the placed plug (terminal-plug 2.0)

## Decals (Blender)
On the legend field: "complexes.org generic", "ipc", "24 V DC 24 W". Beside the sockets: "LAN1", "LAN2"; beside the plug: "24V 0V FE". No maker's name, logo or approval mark.

## Notes and open figures
- One figure of this element's own is open: the supply's under-voltage threshold, the least voltage at which the PC runs (behaviour.csv's `powered` row reads it as "above 0"): NOT ON FILE (B): IEC 61131-2, the 24 V DC class's lower limit, a standard's table asked for once in lib/standards/wanted.md. Everything else it meets is on file (port-rj45 1.0, terminal-plug 2.0, ISO 273) and every other size and value is a design choice, a derived figure or a class value; nothing is guessed and shown as sourced. The placed plug carries its own open line (its clamps' torque, terminal-plug 2.0's behaviour.csv), which behaviour.csv repeats for each pin as that element writes it; the placed sockets carry theirs (their mating face, port-rj45 1.0's spec).
- lib/inventory.csv's made_of: port-rj45 ×2 and terminal-plug are placed; led ×2 and screw-iso7380 ×4 are not built, so the lenses are the toolkit's and the screws' holes are modelled (OPERATING.md 12, quality at the source). A later version places them when they pass station 6.
- The Ethernet links are data, not a circuit the phase-1 solver reads: behaviour.csv carries the supply, the states and the lenses only (its header says so); the sockets' contacts are port nodes the twin's probe can touch.
- Not stated or modelled in 1.0: the processor, memory and storage, the operating system, the protocols, the degree of protection, the operating temperature, the inrush current, the mass, the cooling fins (the back plate stands for the heat spreader). The supply's branch protection is the panel's to provide (the 24 V supply's own, psu-24v-2a4).
- Not a safety-function device (class value 79).

## Outputs (out/)
`ipc.lsp` · `.glb` (pivots on the two lenses, the plug's ports and the sockets' contacts, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r49 (lib/rounds/elec/).

## History
| version | change |
|---|---|
| 1.0 | elec-r49 (2026-11-13, unattended): first build, generic (ETIM 10.0 EC001413), our own design; inventory elec, 9 systems; places port-rj45 1.0 twice (x2, x3) and terminal-plug 2.0 once (x1, 3 poles); the folder's stub record kept as source.txt's end block |
