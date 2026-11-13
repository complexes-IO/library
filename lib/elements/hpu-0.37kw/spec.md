# hpu-0.37kw · v1.1 · hydraulic power unit, generic, small class, 100 bar, 1.6 l/min, 10 l reservoir, 0.37 kW 460 V 3-phase 60 Hz

**What** the hydraulic power unit of a small machine (lib/inventory.csv row `hpu-0.37kw`, "hydraulic power unit (small class)",
own_design generic, 13 systems: the section bender, the sheet folder, the surface grinder, the hose crimper, the hydraulic trainer, the
CNC lathe, the hydraulic lift table, the corner notcher, the hydraulic punch, the turret punch, the plate roll, the automatic band saw
and the sheet shear of lib/machines-factory.txt and lib/machines-from-elements.txt). A steel reservoir on two foot rails; on its lid a
vertical motor-pump group (the drive motor on a bell housing, the pump hung below it inside the oil), a valve block with the pressure
relief valve, a return filter and a filler-breather; a sight gauge on the front shows the oil's level and temperature. The pump
delivers through `port-pressure` to the machine's valve and cylinder; the oil comes back through `port-return` and the return filter;
`port-gauge` takes the pressure gauge (hyd-gauge).
**Class** device · **Baseline** our own design: generic hydraulic power unit, small class (no ETIM class; ISO 4413 values), as
OPERATING.md 12 (generic elements, EM 2026-11-07; a product class ETIM has no class for is generic by the standard whose rating data
its Class values follow, EM 2026-11-08), hpu-7.5kw 1.1 and the inventory row say. No vendor file was opened or measured; the folder's
references/source.txt is the planned-element record of 2026-11-03 (nothing downloaded). The class values below are its design
inputs; its sizes are design choices; the two interfaces a standard fixes and the files don't hold (the ports' thread, the ports'
marks) are open (Open figures). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the foot rails' underside, the mounting plane (z = 0); length along x, width along
y; the motor-pump group toward −x, the valve block and its ports toward +x, the sight gauge on the front (−y).
**Built with** toolkit 1.3 · AutoLISP command `HPU-SMALL` · no parameters (one size).

The class chosen: none. lib/standards/etim/classes.csv (ETIM 10.0's subset on file) has no hydraulic power unit class (hpu-7.5kw 1.0
read its 31 hydraulic entries: fittings, seals, pumps, the cylinder, a gripper and lifting gear; the pump classes are the pump alone).
The row's old EC001185 was cleared by the core (request pneu-11's answer, item 2: "its features are on file but classes.csv has no
name for it, and hpu-7.5kw already set the pattern for this family"). The standard named, ISO 4413 (hydraulic fluid power: general
rules and safety requirements for systems and their components), is not in lib/standards/sources.csv: it is named as the standard
against which a power unit's rating quantities (working pressure, flow, reservoir, drive) are stated, and no figure or clause is taken
from it (hpu-7.5kw's case, needs-em r58).

One element, not an assembly (request pneu-11's answer, item 2): the inventory row names the parts it stands for (hyd-tank, hyd-pump,
motor-iec71-370w, hyd-valve-d03, hyd-gauge), and the core ruled it one generic unit with no parts placed, as hpu-7.5kw 1.1, so it
builds now; an assembly of placed parts under lib/assemblies/ comes later, once hyd-valve-d03 is on file (ISO 4401-03, a document
wanted). The drive is sized to the row's motor class (motor-iec71-370w, IEC 71 frame, 0.37 kW), which fixes the small class's
hydraulic power (Class values 3 to 5).

## Class values (no ETIM class; ISO 4413 values)
Design inputs (OPERATING.md 12): the quantities a hydraulic power unit is rated by, with the value this one is designed to.

| # | quantity | value |
|---|---|---|
| 1 | max. working pressure | 100 bar (the pressure relief valve's setting); in ratings.csv as p_max, status "generic design". The small class's pressure: hyd-gauge 1.1's 0-250 bar span reads 40 % at it (HYD-006 / PNE-009's 75 % line), hyd-cylinder-da-40 1.1 (160 bar) and every pressure-side hydraulic element on file is rated at or above it (toolkit/hyd.py H5: the pressure side; a tank-line part such as hyd-filter-return, 16 bar, is judged at hyd.P_TANK) |
| 2 | flow | 1.6 l/min at the pump's outlet at the motor's rated speed (a fixed-displacement pump) |
| 3 | hydraulic power | 0.267 kW: 100 bar × 1.6 l/min / 600 (element.py hydraulic_kw) |
| 4 | reservoir | 10 l usable oil; 16.3 l inside the reservoir to its lid (340 × 240 × 200), so the oil fills at most 85 % (61 %: an air space above it) and holds more than three minutes of the pump's delivery (4.8 l; element.py asserts both) |
| 5 | drive | one three-phase motor, 0.37 kW rated output (ratings.csv power), the IEC 71 frame class of motor-iec71-370w, the motor the inventory row names: 0.267 kW / 0.8 (the pump and coupling efficiency the drive is sized with, a design choice as hpu-7.5kw's) = 0.333 kW ≤ 0.37 (asserted) |
| 6 | supply | 460 V three-phase 60 Hz (the campus's 480 V system, as hpu-7.5kw 1.1, chiller and coolant-pump are wired); ratings.csv voltage, phases, frequency, status "derived" from that supply (hpu-large-1.0.md finding 1: not "generic design", the supply is the campus's, not a quantity the power unit is rated by). The full-load current, ratings.csv fla 0.91 A, is open, class A, EM's (1.1; Open figures): it is the figure on file in motor-iec71-370w's ratings.csv (the maker's performance table of the 0.37 kW IEC 71 motor the row names as the drive) applied to a unit that draws its own motor and places none, and the ELR checks read fla as the motor's current exactly (toolkit/v_electrical.py, ELR-010 to ELR-012), so it decides what an assembly's check reports (OPERATING.md 6: a rating the twin reads is class A; review hpu-small-1.0.md finding 1, as hpu-large-1.0.md finding 2 ruled for hpu-7.5kw's current). It is neither "derived" (no formula gives it from figures on file) nor "generic design" (GEN-010 reads such a row as an ISO 4413 value, which a current is not). fla_table 1.1 A, NEC Table 430.250's 1/2 hp three-phase row at 460 V as that file carries it, is the standard's figure and does not depend on the maker: status "standard". hpu-7.5kw's 7.5 kW current stays open too (no 10 hp motor on file) |
| 7 | fluid | mineral hydraulic oil ISO VG 46, ISO 11158 category HM (toolkit/hyd.py H7) |
| 8 | filtration | a return-line filter on the lid; its rating not stated |
| 9 | ports | `port-pressure`, `port-return`, `port-gauge`, their thread and their marks open (Open figures); `pwr`, the motor's supply (Ports) |

These are generic design values (OPERATING.md 12), not tested ratings or a listing. With hyd-cylinder-da-40 1.1 (bore 40, rod 22) the unit
extends the rod at 1.6 l/min / 1256.6 mm² = 21.2 mm/s and pushes 12.6 kN at 100 bar (derived: derive.cylinder(40, 22, 100, 1.6), F =
p A, v = Q / A, ISO 4413 5.3); a machine's own cylinder, pressure and speed are the machine's. ELR-001 reads fla in any assembly that
wires the unit, so it REVIEWs nothing for the current; the figure itself waits for EM's line (Open figures), as hpu-7.5kw's does.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| reservoir | 340 (x) × 240 (y) × 200 (z), z 40 to 240; painted steel, light grey | 16.3 l inside for 10 l of oil (Class values 4) |
| foot rails | two, 30 wide × 40 high × 324 long (x −162 to 162), under the reservoir's long sides (y −112 to −82 and 82 to 112), 8 in from its sides and ends; black | lift the reservoir off the bench or floor; set in so no rail face is flush with the reservoir's (GEO-050: coplanar faces flicker in Godot); no anchor holes in 1.0 |
| lid | 356 × 256 × 10, z 239.5 to 249.5 (8 over the reservoir all round) | carries the motor-pump group, the valve block, the filter and the breather |
| bell housing | Ø120 × 60 on the lid at x = −90, y = 0; zinc-plated | joins the motor's flange to the pump below the lid (the pump and its coupling are not modelled) |
| motor flange | Ø160 × 12 on the bell housing; blue | |
| motor body | Ø140 × 200, z 320.5 to 520; blue | the 0.37 kW motor's envelope as drawn here is our own: no IEC frame figure (IEC 60072-1 is not in sources.csv) is used, and motor-iec71-370w's measured body is not copied |
| fan cowl | Ø130 × 40 on the motor's top, to z = 559.5 | the motor's fan, air drawn in from above |
| terminal box | 70 × 60 × 60 on the motor's +y side (x −125 to −55, y 45 to 105, z 380 to 440) | the drive motor's terminals |
| cable entry boss (`pwr`) | Ø24 × 12 on the terminal box's +y face at x = −90, z = 410 (to y = 117); zinc-plated | where the supply cable enters, as motor-iec71-370w's and hpu-7.5kw's entry; no thread or hole cut (Notes) |
| valve block | 100 (x) × 90 (y) × 60 (z) on the lid, x 70 to 170, z 249 to 309; zinc-plated | holds the relief valve and the three ports; the check valve and passages inside are not modelled |
| relief valve | cartridge Ø24 × 40 up from the block's top at x = 95, its adjusting knob Ø32 × 14 on it (to z = 362.5) | the knob is fixed in 1.x (the setting is the class value, 100 bar) |
| port spot faces | Ø24 × 1 proud: `port-pressure` and `port-return` on the block's +x face (x = 171) at y = −32 and +32, z = 279.5; `port-gauge` on the block's top (z = 310) at x = 145 | the joint plane a fitting meets (hyd-cylinder-da-40's, hpu-7.5kw's); 64 apart, room for a wrench between the two fittings; no bore cut (Open figures) |
| return filter | Ø50 × 80 on the lid at x = 120, y = 90; black | the return oil passes it into the reservoir |
| filler-breather | Ø40 × 35 on the lid at x = 20, y = −80; black | fills the reservoir and lets air in and out as the level moves |
| sight gauge | frame 24 × 120 on the front (x = 120, z 80 to 200, 5 proud), a clear window 12 wide, 1 proud of the frame | the oil's level and temperature, seen from the front |
| envelope | 356 × 256 × 559.5 (x −178 to 178, y −128 to 128, z 0 to 559.5) | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-pressure` | hyd-port | female | supply | the block's +x face, x = 171, y = −32, z = 279.5, axis +x | the pump's delivery, through the relief valve's block, to the machine; design: named by its function (toolkit/hyd.py H11, as hyd-filter-return 1.0's and hyd-tank 1.0's ports); the hydraulic port marking standard (ISO 9461) is not on file, so no letter is claimed (Open figures) |
| `port-return` | hyd-port | female | none | the block's +x face, x = 171, y = 32, z = 279.5, axis +x | the machine's return oil, through the return filter to the reservoir; named by its function, as above |
| `port-gauge` | hyd-port | female | gauge | the block's top, x = 145, y = 0, z = 310, axis +z | the pressure gauge's port (hyd-gauge 1.1, whose span reads 40 % at 100 bar); named by its function, as above |
| `pwr` | 480V-3P+E | none | | the cable entry boss's face, x = −90, y = 117, z = 410, axis +y | the drive motor's supply: a cable entry to screw terminals (gender none, PIN-002), pins.csv L1 / L2 / L3 (U1 / V1 / W1) and PE, as motor-iec71-370w's and hpu-7.5kw's `pwr` |

"hyd-port" is the hydraulic contract's unit for a port whose dash size is open (toolkit/hyd.py H1: SAE J1926-1 straight-thread
O-ring boss; "hyd-port-<dash>" once the lane states it); HYD-001 reads the pair REVIEW while a dash size is open. It is no air unit, so
the PNE checks (toolkit/pneu.py, compressed air only) don't pair it. A hydraulic fitting (inventory `fitting-hyd-iso8434`) or hose
(`hose-hyd`) meets each port once the table is on file.

## Open figures
- NOT ON FILE (B): SAE J1926-1 table 1, the three oil ports' dash size, thread, spot face and depth (toolkit/hyd.py H1 and H4:
  every cell of DASH is open; the standard is not in lib/standards/sources.csv), as hpu-7.5kw 1.1's and hyd-tank 1.0's ports. Each
  port is a plain spot face with its pivot; the bores are cut once the table is on file (changed cut-outs: a major version).
- NOT ON FILE (B): ISO 9461, the oil ports' marks (toolkit/hyd.py H11, request pneu-10's answer item 2: hydraulic port
  identification; lib/standards/sources.csv iso-9461, wanted). The ports are named by their function and claim no letter or number;
  when the standard is on file, hyd.PORT_MARKS takes the marks with their clause and a text minor marks these ports from it.
- Class A, EM's, one line on his page (ratings.csv `fla`, its status marked there and not repeated here, so it counts once): the
  drive motor's full-load current at 460 V, 0.91 A, motor-iec71-370w's on-file figure (its ratings.csv, the maker's performance
  table) for the IEC 71 0.37 kW motor the inventory row names as this unit's drive. This unit draws its own motor and places none,
  and the ELR checks read `fla` as the motor's current (ELR-010 to ELR-012), so the figure is another product's rating applied to
  ours: EM accepts it as the row's named motor's, refuses it, or a later version places motor-iec71-370w and carries its own
  (review hpu-small-1.0.md finding 1; pneu/r85.md finding 1). Until his line, hpu-0.37kw waits at station 7 as hpu-7.5kw does.

## Named nodes
`port-pressure`, `port-return`, `port-gauge` (the spot faces) and `pwr` (the cable entry boss); kind port, fixed (range 0). No
moving node: the relief valve's knob is fixed in 1.x.

## Materials by layer
`M-STEEL-7035` reservoir, lid, port spot faces · `M-BLACK-PA` foot rails, relief valve knob, return filter, filler-breather, sight
gauge frame · `M-CAST-BLUE` motor flange, body, fan cowl, terminal box · `M-GALV` bell housing, valve block · `M-ZINC` relief valve
cartridge, cable entry boss · `M-CASE-CLEAR` sight gauge window

## Decals (Blender)
None in 1.x (the "generic" label and the port names are a later version). No vendor names, no approval marks.

## Notes
- One element, as hpu-7.5kw 1.1 and compressor-air are: the motor, pump, filter and valves are its own parts, not the inventory's
  motor-iec71-370w, hyd-pump, hyd-filter-return or hyd-valve-d03 elements placed (the row has no made_of; request pneu-11's answer item 2).
  The assembly of those placed parts is the core's, later, once hyd-valve-d03 is on file.
- Inside nothing is modelled: the pump, its coupling, the suction line and strainer, the return line, the baffle, the oil, the check
  valve and the passages in the block.
- The supply: `pwr` (480V-3P+E) and pins.csv (L1, L2, L3, PE) are on file, so an assembly can wire the unit (cable-pwr-480: 14 AWG,
  15 A, above the 0.91 A full-load and the 1.1 A table current); the terminals inside the box are not modelled. The cable gland is
  placed, never redrawn, and a host doesn't model holes now for a part it will place later (OPERATING.md 12, quality at the source),
  so the entry boss has no hole or thread.
- No drain port, no level or temperature switch, no accumulator or cooler in 1.0 (each a new node, a major; the cooler and
  accumulator are inventory elements of their own, hyd-cooler and accumulator). A hydraulic trainer's unit may want a drain: a later
  version.
- The planned-element record in references/source.txt (2026-11-03) read "1 to 2 kW, 10 to 20 l ... assembled from library
  elements"; the inventory row of 2026-11-11 (core watch, request pneu-11 2) names motor-iec71-370w as the drive and rules one
  generic unit, so the build follows the row: 0.37 kW, 10 l. A 1 to 2 kW small unit would be a sibling or a parameter, if a system
  asks for one.
- No safety function of its own (inventory.csv's `safety` column is empty for this row): the relief valve's setting is the class
  value, not a safety sign-off. The machine's hydraulic safety review against ISO 4413 is EM's once the standard is on file.

## Outputs (out/)
`hpu-0.37kw.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (no ETIM class; ISO 4413 values), pneu-r85 (unattended; request pneu-11's answer item 2): reservoir on two foot rails, lid, vertical motor-pump group (bell housing, flange, motor, fan cowl, terminal box), valve block with relief valve and knob, spot faces `port-pressure` / `port-return` / `port-gauge` named by function (hyd.py H11), cable entry boss `pwr` (480V-3P+E, pins.csv), return filter, filler-breather, sight gauge; ratings.csv p_max 100 bar, 0.37 kW, 460 V, fla 0.91 A from motor-iec71-370w's record; behaviour.csv; the oil ports' thread (SAE J1926-1 table 1) and marks (ISO 9461) left open (class B) |
| 1.1 | text only, pneu-r89 (unattended; review hpu-small-1.0.md finding 1, pneu/r85.md finding 1): ratings.csv `fla` 0.91 A is no longer "derived" (no formula gives it): its status marks it open, class A, for EM (motor-iec71-370w's on-file figure applied to a unit that draws its own motor; the ELR checks read it), one line on his page; Class values 1 says "pressure-side" (note 1: hyd.py H5 is the pressure side, the tank line's parts are judged at P_TANK); Class values 6 and the ELR sentence reworded; behaviour.csv's header the same. Built under the id core round 30 gave the element (hpu-small, request pneu-12). No geometry, node, origin or cut-out changed |
