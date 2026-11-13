# chiller · v2.1 · generic recirculating water chiller, 2 kW at L32W18, 460 V 3-phase 60 Hz, supply and return NPT 3/8 female

**What** the water chiller of a machine (lib/inventory.csv row `chiller`, "industrial chiller (water, recirculating)": the CMM, the
two laser cutters, the machining centre, the plasma and spot welders of lib/machines-factory.txt). A free-standing cabinet on a
plinth beside the machine: it cools water in its own reservoir, pumps it to the machine through `port-supply` and takes it back,
warmed, through `port-return`; the condenser's fan draws room air in through the front grille and blows it out through the guard on
the top. The control panel with its temperature display and the reservoir's level gauge are on the front; the fill cap is on the top.
**Class** device · **Baseline** our own design: generic liquid cooling unit (ETIM 10.0 EC002516), as OPERATING.md 12 (generic
elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. EC002516 "Liquid cooling unit (enclosure/cabinet)" (group
EG000011) lists "Chiller", "Recooling unit" and "Cooling system" among its synonyms (lib/standards/etim/classes.csv), it is tier 1,
and its 11 features are on file; its rated performance L32W18 (room air 32 °C, water out 18 °C) is a water chiller's rating, so the
class fits a chiller for a machine as well as one for a cabinet. Rejected: EC002515 "Air/water heat exchanger" (it needs a chilled
water supply, which is what this element makes) and EC004896 "Portable adiabatic cooler" (it cools air, not water). ETIM's list has
no class named for a process chiller. No vendor file was opened or measured. The class values below are its design inputs; its sizes
are design choices; its ports take their thread from the standard on file (ASME B1.20.1, through toolkit/pneu.py). No vendor names.
**Units / frame** mm, Z up. Origin: the centre of the plinth's underside, the floor contact plane (z = 0); width along x, depth
along y; the front toward −y, the rear (ports, cable entry) toward +y. The ports follow pneu.py's port frame: the pivot on the joint
plane (the boss face), its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `CHILLER` · no parameters (one size).

## Class values (ETIM 10.0 EC002516, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF006811 Add-on type | free-standing (on the floor beside the machine, on its own plinth) |
| 2 | EF008206 Operating voltage AC 50 Hz | not stated (a 60 Hz design) |
| 3 | EF008207 Operating voltage AC 60 Hz | 460 V (three-phase; the campus's 480 V system, as motor-iec71-370w and coolant-pump 1.0 are wired) |
| 4 | EF008208 Operating voltage DC | not stated (AC only) |
| 5 | EF000187 Voltage type | AC, three-phase |
| 6 | EF007329 Type of cooling medium | water (a water-glycol mix for frost protection is the user's choice) |
| 7 | EF007392 Nominal cooling performance L32W18 at 50Hz | not stated (a 60 Hz design; its design capacity, 2000 W at L32W18 and 60 Hz, is under Water circuit) |
| 8 | EF007391 Nominal cooling performance L32Oil20 at 50Hz | not stated (a water chiller, not an oil cooler) |
| 9 | EF000008 Width | 500 mm (the cabinet) |
| 10 | EF000040 Height | 960 mm (the cabinet, floor to its top; 990 to the fill cap's top) |
| 11 | EF000049 Depth | 600 mm (the cabinet; 624 over the display window and the port bosses) |

Electrical: ratings.csv holds 460 V, 3 phases and 60 Hz, status "generic design" (OPERATING.md 12). The full-load current and the
input power are open figure 2 (Open figures): a chiller's current is its compressor's, fan's and pump's together, measured on the
unit, so ELR-001 would ask for it (REVIEW) in any assembly that wires the chiller. Generic design values, not tested ratings or a listing. 2.0 adds
the supply port `pwr` (Ports) with its pins in pins.csv, so an assembly can wire it.

## Water circuit (design inputs, our own)
| item | value | why |
|---|---|---|
| cooling capacity | 2000 W at L32W18 (room air 32 °C, water out 18 °C) and 60 Hz | the class's rating point; a size for a small fibre laser, a spindle or a welding torch |
| water out (set point) | 18 °C, settable 10 to 30 °C on the control panel | a design choice, the class's rating point, with no standard behind it. Whether the machine's water lines sweat depends on the room's humidity, not on this figure: at 32 °C room air the dew point reaches 18 °C at about 43 % RH (Magnus formula), so lines at 18 °C sweat in any but a dry shop. The machine's lines are insulated, or the set point is raised above the room's dew point (review chiller-1.0.md finding 3) |
| flow | 10 l/min at the supply port | a design choice for the 2 kW load: about 3 K rise across the machine |
| p_max | not given: Open figures 1 | EC002516 has no pressure feature, and nothing on file gives the water circuit's pressure rating (the pump inside is not modelled, and no head figure for it is on file). 1.0's 4 bar was a chosen figure with no source (review chiller-1.0.md finding 1), so 1.1 drops it from ratings.csv: PNE-003 then has no rating to read and REVIEWs the chiller in any circuit that places it |
| reservoir | 20 l inside the cabinet, filled through the fill cap, seen in the level gauge | not modelled; the gauge spans its height |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| cabinet | 500 (x) × 600 (y) × 900 (z), z 60 to 960; painted steel, light grey | holds the compressor, condenser, evaporator, pump and reservoir for 2 kW |
| plinth | 480 × 580 × 60, z 0 to 60; black | 10 in from the cabinet on each side, a toe recess; fork-lift and pallet-truck handling is the assembly's |
| fan guard | Ø360 × 15 on the top, centred at y = 60 | the condenser fan blows up and out, away from the operator in front |
| fill cap | Ø50 × 30 on the top at x = 150, y = −220 | the reservoir's filler, front right, clear of the fan guard (asserted in element.py) |
| control panel | 160 × 100 on the front, x −80 to 80, z 780 to 880, 8 proud | at eye level for a standing operator |
| display window | 120 × 60 on the panel, z 800 to 860, 2 proud of it | the water temperature and the set point |
| level gauge | frame 36 × 250 (z 450 to 700, 6 proud) at x = 188, a clear window 20 wide, 1 proud of the frame | the reservoir's level, seen from the front |
| air intake grille | 340 × 400 on the front, x −220 to 120, z 150 to 550, 3 proud | room air in to the condenser; its louvres are not modelled |
| port bosses | Ø28, 14 proud of the rear (face y = 314), at x = −120 (`port-supply`) and x = 120 (`port-return`), z = 250; zinc-plated steel | half couplings for NPT 3/8 female threads: at least 3 mm round the pipe OD (17.1) and 14 proud, more than a male's make-up (L1 + L3, 10.3) plus 2; 240 apart, room for a wrench between the two fittings (asserted in element.py) |
| port bores (2.0) | Ø17.055 × 12.36 deep, blind, one in each port boss, on the port's axis from its face | Ø = E1 + h of NPT 3/8 from pneu.NPT, the very diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule, review chiller-1.0.md finding 2); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 and < the boss's 14 proud; 5.47 mm of boss wall round each bore (asserted ≥ 3). Role in features.csv (HOLE-010) |
| cable entry boss | Ø24 × 12 on the rear at x = 180, z = 820; black; the `pwr` node (2.0) | where the supply cable enters; no thread cut (Notes) |
| envelope | 500 × 624 × 990 (x −250 to 250, y −310 to 314, z 0 to 990) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-supply` | NPT3/8 | female | the boss face x = −120, y = 314, z = 250, axis +y | chilled water out, toward the machine |
| `port-return` | NPT3/8 | female | the boss face x = 120, y = 314, z = 250, axis +y | warm water back from the machine |
| `pwr` | 480V-3P+E | none | the cable entry boss's face x = 180, y = 312, z = 820, axis +y | the supply: screw terminals L1 / L2 / L3 and PE inside (pins.csv), the library's 480 V three-phase + PE unit as coolant-pump 2.0 and hpu-7.5kw 1.0 (review pneu-r51 finding 2's kind) |

Thread: NPT (ASME B1.20.1; pneu.NPT holds NPT 3/8's figures as values calculated from its formulas, EM 2026-11-07). pneu.py covers
compressed air and says liquid process ports wait for a process section (request pneu-2); these ports take the same thread as tank
1.0's and coolant-pump 1.0's liquid ports (pneu-r48, r51), because ASME B1.20.1 is a general-purpose pipe thread and NPT 3/8 is the
largest size the lane has on file (pneu.THREADS). When a process section is on file and names another thread or size for water
lines, the ports change with it (a changed cut-out: a major version). The ports carry no role: a chiller is not on the air line.
PNE-002 pairs each with a male NPT 3/8 (sealant on the male). The boss face is the joint plane a placed fitting meets; 2.0 cuts
the bores behind them (Dimensions), a change of cut-outs and a new node (`pwr`), so a major version (OPERATING.md 7): a male NPT 3/8
stub (fitting-pushin 2.0's) now goes into a bore instead of solid steel. `pwr` carries gender none (screw terminals, PIN-002).

## Open figures
1. p_max, the water circuit's pressure rating (a rating the checks read, PNE-003), class A: NOT ON FILE (A). EC002516 has no
   pressure feature and no source on file gives one. EM's: a figure with its source (a process section in pneu.py, request
   pneu-2, or a rating EM accepts) closes it.
2. NOT ON FILE (A): the unit's full-load current (or electrical input power) at 460 V, for pins.csv rated_A and the behaviour.csv
   load row. A chiller's current is its compressor's, condenser fan's and pump's together, measured on the unit; EC002516 has no
   current or power feature, and the 2000 W of the Water circuit is the cooling capacity, not the electrical input. Until it is on
   file pins.csv rated_A stays blank and behaviour.csv has no load row (review coolant-pump-2.0.md finding 1, which names chiller
   2.0's same gap; coolant-pump 2.1's and hpu-7.5kw 1.1's lines are the same case).

Every other figure is a design choice, a class value above, a design input of the water circuit, or from the standard on file.

## Named nodes
`port-supply`, `port-return` (the port bosses), `pwr` (the cable entry boss, 2.0); kind port, fixed (range 0)

## Materials by layer
`M-STEEL-7035` cabinet · `M-BLACK-PA` plinth, fan guard, fill cap, control panel, level gauge frame, air intake grille, cable entry
boss · `M-LENS-DARK` display window · `M-CASE-CLEAR` level gauge window · `M-GALV` port bosses

## Decals (Blender)
None. No vendor names, no approval marks.

## Notes
- Inside the cabinet nothing is modelled: the refrigerant circuit (compressor, condenser, expansion device, evaporator), the
  condenser fan, the water pump and the reservoir. The refrigerant and its charge are not stated: they are a maker's, and the
  pressure-equipment and refrigeration safety codes they fall under are not on file. The twin reads the water temperature and the
  ports, not the refrigerant.
- The supply cable and its gland are not modelled: the cable enters at the cable entry boss, the `pwr` node since 2.0, with its
  pins in pins.csv. A gland (gland-m20, mech's) is placed, never redrawn, and a host doesn't model holes now for a part it will
  place later (OPERATING.md 12, quality at the source), so the entry has no thread or hole.
- No alarm or run contact is modelled; a machine that interlocks on the chiller's fault needs one, with its pins, in that later
  version.
- No drain port: the reservoir drains through its fill cap's side in service. A drain port is a new node (a major version).
- No safety function of its own (inventory.csv's `safety` column is empty for this row). The disconnect and the branch circuit
  protection are the machine's or the building's (NFPA 79 is in lib/standards/sources.csv as view-only; nothing is read from it here).

## Outputs (out/)
`chiller.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002516), pneu-r52 (unattended): cabinet on a plinth, fan guard, fill cap, control panel with display window, level gauge, air intake grille, two NPT 3/8 port bosses with their pivots (supply, return), cable entry boss |
| 1.1 | pneu-r59 (unattended), text only, review chiller-1.0.md findings 1 and 3: p_max 4 bar dropped from ratings.csv (no class feature or source behind it) and written as a class A open figure for EM; the set point no longer claimed to keep the water lines dry; the NFPA 79 note corrected. Nodes, origin, cut-outs unchanged |
| 2.0 | pneu-r62 (unattended), review chiller-1.0.md finding 2 and the power node from its Notes: both port bores cut, Ø17.055 (E1 + h of NPT 3/8, pneu.NPT) × 12.36 (L2 + 2), blind in each boss, role in the new features.csv; the cable entry boss becomes node `pwr` (480V-3P+E, gender none) with pins.csv; origin and envelope unchanged |
| 2.1 | pneu-r73 (unattended), text only, review coolant-pump-2.0.md finding 1 (its last part, on chiller 2.0): the unit's full-load current (or input power) at 460 V written under Open figures as a second open class A line (EM's page through DOC-005), the Electrical paragraph pointing to it; the Decals and Notes lines no longer say "in 1.0" (that review's finding 2 case); behaviour.csv's header points to the open line. Nodes, origin, cut-outs unchanged |
