# coolant-pump · v2.1 · generic immersion coolant pump, 0.12 kW 460 V 3-phase 60 Hz, outlet NPT 3/8 female

**What** the coolant pump of a machine tool (lib/inventory.csv row `coolant-pump`, "coolant pump (immersion, with tank)": the lathes,
mills, grinders, borers, drills and saws of lib/machines-factory.txt). It stands upright in a coolant tank: its square mounting
flange sits on the tank's cover, the column, the pump housing and the suction strainer hang in the coolant, and the head with the
outlet, the motor and its fan cover stand above the cover. The motor turns the impeller on its own shaft (close-coupled); coolant
enters through the strainer's open bottom and leaves by `port-out` toward the machine's nozzles.
**Class** device · **Baseline** our own design: generic block pump (ETIM 10.0 EC010732), as OPERATING.md 12 (generic elements, EM
2026-11-07) and lib/inventory.csv (own_design generic) say. ETIM's class list has no class named for an immersion pump; EC010732
"Block pump" (group EG020079 Pumps) is a close-coupled pump-and-motor unit and lists "Coolant pump" among its synonyms
(lib/standards/etim/classes.csv), and its 70 features are on file. Rejected: EC010980 "Built-in circulation pump" (a heating-circuit
pump built into an appliance), EC011334 "Multistage centrifugal pump" (several stages; this design has one). No vendor file was
opened or measured. The class values below are its design inputs; its sizes are design choices; its outlet takes its thread from
the standard on file (ASME B1.20.1, through toolkit/pneu.py). No vendor names.
**Units / frame** mm, Z up. Origin: the centre of the mounting flange's underside, which is the tank cover's top plane (z = 0); the
pump's axis along z, the motor up, the immersed part down; the outlet toward +x, the terminal box toward +y. The port follows
pneu.py's port frame: the pivot on the joint plane (the boss face), its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `COOLANT-PUMP` · no parameters (one size).

## Class values (ETIM 10.0 EC010732, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design. Features 24 to 48 are the class's
radio, interface and bus features: this pump has none of them (rows 24 to 48 below, each "no").

| # | feature | value |
|---|---|---|
| 1 | EF023038 Material pump casing | cast iron, painted blue (flange, head, pump housing) |
| 2 | EF023143 Material quality pump casing | not stated (a grade is the maker's) |
| 3 | EF011652 Material impeller/pump wheel | brass (inside the housing, not modelled) |
| 4 | EF024149 Material quality impeller/pump wheel | not stated |
| 5 | EF014904 Volume flow rate (BEP) | 3 m³/h |
| 6 | EF014905 Discharge head at flow rate (BEP) | 50 kPa (about 5 m of water) |
| 7 | EF000992 Max. static height | 10 m (the head at closed outlet) |
| 8 | EF000991 Max. discharge flow | 5 m³/h |
| 9 | EF020449 Max. operating pressure | 1 bar (ratings.csv p_max) |
| 10 | EF001422 Type of drive | electric motor, close-coupled (the impeller on the motor's shaft) |
| 11 | EF003701 Electrical connection | terminal box with a cable entry: port `pwr` (480V-3P+E, pins.csv L1 / L2 / L3 and PE; the cable is the assembly's) |
| 12 | EF000536 Cable length | not stated (no cable with the pump) |
| 13 | EF003977 Rated voltage | 460 V (three-phase; the campus's 480 V system, as motor-iec71-370w is wired) |
| 14 | EF000351 Number of phases | 3 |
| 15 | EF005455 Frequency | 60 Hz |
| 16 | EF000001 Nominal current | not stated (a motor's full-load current is measured on the motor; NEC Table 430.250 starts at 1/2 hp, above 0.12 kW) |
| 17 | EF012425 Motor power output (P2) per motor | 0.12 kW |
| 18 | EF013710 Minimum Efficiency Index (MEI) | not stated |
| 19 | EF023092 Insulation class according to IEC | F |
| 20 | EF001642 Rotational speed | 3450 1/min (a two-pole motor at 60 Hz, under load) |
| 21 | EF020121 Motor speed control | no |
| 22 | EF020120 Type of speed control | not stated (none) |
| 23 | EF015266 Communication | none |
| 24 | EF007178 Radio standard Bluetooth | no |
| 25 | EF007179 Radio standard WLAN 802.11 | no |
| 26 | EF016790 Mobile communications standard 2G (GSM) | no |
| 27 | EF008525 Mobile communications standard 3G (UMTS) | no |
| 28 | EF016792 Mobile communications standard 4G (LTE) | no |
| 29 | EF016385 Mobile communications standard 5G | no |
| 30 | EF016386 Interface signal 0-10 V / 2-10 V | no |
| 31 | EF016387 Interface signal 0-20 mA / 4-20 mA | no |
| 32 | EF016388 Interface PT100 / PT1000 / PTC | no |
| 33 | EF016389 Interface Pulse Width Modulation (PWM) | no |
| 34 | EF016390 Interface pulse counter | no |
| 35 | EF003626 Potential free switch contact | no |
| 36 | EF007314 With communication interface RS-485 | no |
| 37 | EF007312 With communication interface RS-232 | no |
| 38 | EF007521 Supporting protocol for EtherNet/IP | no |
| 39 | EF003055 Supporting protocol for KNX | no |
| 40 | EF003052 Supporting protocol for PROFIBUS | no |
| 41 | EF007525 Supporting protocol for PROFINET IO | no |
| 42 | EF016391 Supporting protocol for CAN/CANOpen | no |
| 43 | EF016392 Supporting protocol for Modbus TCP | no |
| 44 | EF016393 Supporting protocol for Modbus RTU | no |
| 45 | EF016394 Supporting protocol for BACnet MS/TP | no |
| 46 | EF016395 Supporting protocol for BACnet IP | no |
| 47 | EF016396 Supporting protocol for LON/LONWorks | no |
| 48 | EF016397 Supporting protocol for LIN Bus | no |
| 49 | EF023182 Medium temperature (continuous) | 5 to 40 °C (water-based coolant) |
| 50 | EF002386 Ambient temperature | 0 to 40 °C |
| 51 | EF025116 Connection inlet side | open suction through the strainer (no pipe connection) |
| 52 | EF025117 Nominal diameter connection inlet side | not stated (no pipe connection) |
| 53 | EF025503 Outer pipe diameter connection inlet side | not stated (no pipe connection) |
| 54 | EF026143 Flange compression stage connection inlet side | not stated (no pipe flange) |
| 55 | EF014906 Connection standard inlet side | not stated (no pipe connection) |
| 56 | EF025977 Connection outlet side | female pipe thread |
| 57 | EF025118 Nominal diameter connection outlet side | NPT 3/8 |
| 58 | EF025504 Outer pipe diameter connection outlet side | 17.1 mm: the NPT 3/8 pipe OD D = 0.675 in (pneu.NPT, ASME B1.20.1) |
| 59 | EF026233 Flange compression stage connection outlet side | not stated (no pipe flange) |
| 60 | EF014907 Connection standard outlet side | ASME B1.20.1 (NPT) |
| 61 | EF001339 Flange shape | not stated (no pipe flange; the mounting flange is square, Dimensions) |
| 62 | EF005474 Degree of protection (IP) | IP54, the IP code the feature asks for (IEC 60529 not on file; a design target, not a tested rating) |
| 63 | EF020246 Forced motor cooling | yes: a shaft fan under the fan cover |
| 64 | EF023094 Height of suction end | 250 mm (the flange's underside to the strainer's open bottom: `immersion()`) |
| 65 | EF023095 Height of pressure end | 35 mm (the flange's underside to the outlet's axis) |
| 66 | EF023099 Length of centre pressure/suction connection | 285 mm (the outlet's axis to the strainer's open bottom, along z) |
| 67 | EF023096 Pump length | 500 mm (the strainer's bottom to the fan cover's top) |
| 68 | EF004663 Explosion-proof | no |
| 69 | EF014908 Standard motor | no (the motor is the pump's own, with no IEC frame) |
| 70 | EF014979 Motor efficiency class | not stated |

Pressure: ratings.csv holds p_max 1 bar (gauge), status "generic design", so PNE-003 refuses the pump on any line that carries
the air supply (P_SUPPLY 100 psig, about 6.9 bar): it belongs on a coolant line only. Electrical: ratings.csv holds 460 V, 3
phases, 60 Hz and 0.12 kW, status "generic design" (OPERATING.md 12); the supply reaches the motor through `pwr` (Ports, pins.csv);
no full-load current, so ELR-001 asks for one (REVIEW) in any assembly that wires the pump. Generic design values, not tested ratings or a listing.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| mounting flange | 150 × 150 × 10, z 0 to 10; painted cast iron | carries the pump on a tank cover; its fixing holes are not cut (Notes) |
| pump head | Ø100, z 10 to 60 | the discharge housing; carries the outlet boss between the flange and the motor |
| outlet boss | Ø28, from inside the head (x = 40) to its face at x = 64, on z = 35; zinc-plated steel | a half coupling for an NPT 3/8 female thread: at least 3 mm round the pipe OD (17.1) and 14 proud of the head, more than a male's make-up (L1 + L3, 10.3) plus 2; asserted in element.py |
| outlet bore | Ø17.055 (E1 + h), 12.36 deep (L2 + 2), blind, from the boss face x = 64 to x = 51.64 | the thread drawn plain at the male stub's own diameter (tank 2.0's rule), so a fitting-pushin 2.0 or other male NPT 3/8 stub meets it face to face; inside the boss's 14 mm proud part, 5.47 of metal a side; features.csv role (HOLE-010); asserted in element.py |
| motor frame | Ø120, z 60 to 220; painted steel, light grey | a 0.12 kW frame (class value 17) |
| fan cover | Ø116, z 220 to 250; black polyamide | over the shaft fan (class value 63) |
| terminal box | 70 (x) × 60 (y) × 60 (z), y 45 to 105, z 110 to 170 | on the motor's side, away from the outlet; its inner face runs into the frame |
| cable entry boss (`pwr`) | Ø24 × 12 on the terminal box's +y face, at z = 140 (to y = 117); black polyamide | where the supply cable enters, as hpu-7.5kw 1.0's entry; no thread or hole cut (Notes) |
| column | Ø40, z −180 to 0 | the shaft tube from the flange to the pump housing |
| pump housing | Ø110, z −230 to −180; painted cast iron | the volute round the impeller |
| suction strainer | Ø80, z −250 to −230, open at the bottom; zinc-plated steel | keeps chips out of the impeller; its mesh is not modelled |
| immersion | 250 below the flange's underside | for a coolant tank about 300 deep, the strainer clear of its floor and the sludge |
| envelope | 150 × 192 × 500 (x −75 to 75, y −75 to 117, z −250 to 250) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-out` | NPT3/8 | female | the outlet boss's face x = 64, z = 35, axis +x | the pump's outlet, toward the machine's coolant line |
| `pwr` | 480V-3P+E | none | the cable entry boss's face x = 0, y = 117, z = 140, axis +y | the motor's supply: a cable entry to screw terminals (gender none, PIN-002), pins.csv L1 / L2 / L3 (U1 / V1 / W1) and PE, as motor-iec71-370w's and hpu-7.5kw 1.0's `pwr` (review coolant-pump-1.0.md finding 2) |

Thread: NPT (ASME B1.20.1; pneu.NPT holds NPT 3/8's figures as values calculated from its formulas, EM 2026-11-07). pneu.py covers
compressed air and says liquid process ports wait for a process section (request pneu-2); this outlet takes the same thread as tank
1.0's liquid ports (pneu-r48), because ASME B1.20.1 is a general-purpose pipe thread and NPT 3/8 is the largest size the lane has
on file (pneu.THREADS). When a process section is on file and names another thread or size for coolant lines, the outlet changes
with it (a changed cut-out: a major version). The port carries no role: a coolant pump is not on the air line. PNE-002 pairs it with
a male NPT 3/8 (sealant on the male). 2.0 cuts the port bore (Dimensions, outlet bore; review coolant-pump-1.0.md finding 1): the
boss face stays the joint plane, and a male stub placed in the port lies inside the bore, not inside the boss.

## Open figures
- NOT ON FILE (A): the motor's full-load current (or electrical input power) at 460 V, for pins.csv rated_A and the behaviour.csv
  load row (NFPA 70 Table 430.250 starts at 1/2 hp, above 0.12 kW; the 0.12 kW of class value 17 is the shaft output P2, and the
  efficiency is not stated, class values 18 and 70). Until it is on file pins.csv rated_A stays blank and behaviour.csv has no load
  row (review coolant-pump-2.0.md finding 1; hpu-7.5kw 1.1's line is the same case).

Every other figure is a design choice, a class value above, or from the standard on file.

## Named nodes
`port-out` (the outlet boss) and `pwr` (the cable entry boss); kind port, fixed (range 0)

## Materials by layer
`M-CAST-BLUE` flange, head, pump housing · `M-STEEL-7035` motor frame, terminal box · `M-BLACK-PA` fan cover, cable entry boss ·
`M-GALV` column, strainer, outlet boss

## Decals (Blender)
None. No vendor names, no approval marks.

## Notes
- The supply: `pwr` (480V-3P+E) and pins.csv (L1, L2, L3, PE) are on file from 2.0, so an assembly can wire the pump
  (cable-pwr-480); the terminals inside the box are not modelled. The cable gland (gland-m20, mech's) is placed, never redrawn, and
  a host doesn't model holes now for a part it will place later (OPERATING.md 12, quality at the source), so the entry boss has no
  thread or hole. The pins carry no rated current (not stated, Class values 16), so ELR-001 REVIEWs the pump in any assembly that
  wires it.
- The mounting flange's fixing holes are not cut: holes need their features.csv roles (HOLE-010), and the screws that pass them
  are common parts not yet built in this lane. Cutting them is a major version.
- "With tank" in the inventory row: the tank is its own element (tank 1.0 is the lane's rectangular reservoir, pressureless) and
  the assembly places the pump on a tank's cover; the pump does not draw one. A coolant tank with a cover cut for this flange is a
  later element or a tank version (needs-em/pneu.md, pneu-r51).
- No safety function of its own (inventory.csv's `safety` column is empty for this row). The motor's overload protection and its
  disconnect are the machine's: NFPA 79 is in lib/standards/sources.csv (2024, free to view, read attended), but no clause of it is
  read into a standards table yet, so this element cites none.

## Outputs (out/)
`coolant-pump.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010732), pneu-r51 (unattended): mounting flange, head with the NPT 3/8 outlet boss and its pivot, motor frame, fan cover, terminal box with a cable entry boss, column, pump housing, suction strainer |
| 2.0 | review coolant-pump-1.0.md, pneu-r61 (unattended): finding 1, the outlet bore Ø E1 + h = 17.055, L2 + 2 = 12.36 deep, blind, with its features.csv role; finding 2, the supply port `pwr` (480V-3P+E, gender none) on the cable entry boss with pins.csv L1 / L2 / L3 / PE; finding 3, the IP code and NFPA 79 lines restated against sources.csv. New node and cut-out: a major |
| 2.1 | review coolant-pump-2.0.md, pneu-r72 (unattended): finding 1, the motor's full-load current at 460 V written under Open figures as an open class A line (EM's page through DOC-005); finding 2, two lines no longer say "in 1.0". Text only: a minor |
