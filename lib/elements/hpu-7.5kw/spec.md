# hpu-7.5kw · v1.3 · hydraulic power unit, generic, press class, 160 bar, 22 l/min, 100 l reservoir, 7.5 kW 460 V 3-phase 60 Hz

**What** the hydraulic power unit of a press-class machine (lib/inventory.csv row `hpu-7.5kw`, "hydraulic power unit (press class)",
own_design generic, 7 systems, pin 2, "press-hydraulic first", EM 2026-11-08: the hydraulic press, the press brakes, the ironworker,
the hydraulic shear, the hydraulic test bench and the cylinder test rig of lib/machines-factory.txt). A steel reservoir on two skids;
on its lid a vertical motor-pump group (the drive motor on a bell housing, the pump hung below it inside the oil), a valve block with
the pressure relief valve, a return filter and a filler-breather; a sight gauge on the front shows the oil's level and temperature.
The pump delivers through `port-p` to the machine's valve and cylinder (hyd-cylinder-da-40); the oil comes back through `port-t` and the
return filter; `port-g` takes the pressure gauge (hyd-gauge, a later element).
**Class** device · **Baseline** our own design: generic hydraulic power unit, press class (no ETIM class; ISO 4413 values), as
OPERATING.md 12 (generic elements, EM 2026-11-07; a product class ETIM has no class for is generic by the standard whose rating data
its Class values follow, EM 2026-11-08) and the inventory row say. No vendor file was opened or measured. The class values below are
its design inputs; its sizes are design choices; the one interface a standard fixes and the files don't hold (the ports' thread) is
open (Open figures). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the skids' underside, the floor contact plane (z = 0); length along x, width
along y; the motor-pump group toward −x, the valve block and its ports toward +x, the sight gauge on the front (−y).
**Built with** toolkit 1.3 · AutoLISP command `HPU-LARGE` · no parameters (one size).

The class chosen: none. lib/standards/etim/classes.csv (ETIM 10.0's subset on file) has no hydraulic power unit class: its 31
hydraulic entries are fittings, seals, pumps, the cylinder, a gripper and lifting gear; its pump classes (group EG020079: "Gear pump"
EC012031, "Block pump" EC010732, ...) are the pump alone, not a unit with its reservoir, drive and valves. hpu-0.37kw's inventory row
names EC001185, which is not in classes.csv (as gauge-p's EC011112 was not, request pneu-5), so it is not used here. Whether the full
ETIM 10.0 release has a power unit class is for the attended session that checks the silencer's (pneu-3 answer). The standard
named, ISO 4413 (hydraulic fluid power: general rules and safety requirements for systems and their components), is not in
lib/standards/sources.csv: it is named as the standard against which a power unit's rating quantities (working pressure, flow,
reservoir, drive) are stated, and no figure or clause is taken from it (needs-em r58).

## Class values (no ETIM class; ISO 4413 values)
Design inputs (OPERATING.md 12): the quantities a hydraulic power unit is rated by, with the value this one is designed to.

| # | quantity | value |
|---|---|---|
| 1 | max. working pressure | 160 bar (the pressure relief valve's setting), the press class of hyd-cylinder-da-40 1.0; in ratings.csv as p_max, status "generic design" |
| 2 | flow | 22 l/min at the pump's outlet at the motor's rated speed (a fixed-displacement pump) |
| 3 | hydraulic power | 5.87 kW: 160 bar × 22 l/min / 600 (element.py hydraulic_kw) |
| 4 | reservoir | 100 l usable oil; 126 l inside the reservoir to its lid, so the oil fills at most 85 % (an air space above it) and holds more than three minutes of the pump's delivery (element.py asserts both) |
| 5 | drive | one three-phase motor, 7.5 kW rated output (ratings.csv power): 5.87 kW / 0.8 (the pump and coupling efficiency the drive is sized with, a design choice) = 7.33 kW ≤ 7.5 (asserted) |
| 6 | supply | 460 V three-phase 60 Hz (the campus's 480 V system, as chiller 1.0 and coolant-pump 1.0 are wired); ratings.csv voltage, phases, frequency, status "derived" from that supply (motor-iec71-370w's 460 V nameplate on the 480 V system), not "generic design" ISO 4413 values: the supply is the campus's, not a quantity the power unit is rated by (review hpu-large-1.0.md finding 1; GEN-010 reads every "generic design" row as a value of the named standard) |
| 7 | fluid | mineral hydraulic oil; its viscosity grade not stated |
| 8 | filtration | a return-line filter on the lid; its rating not stated |
| 9 | ports | `port-p` (pressure), `port-t` (return), `port-g` (gauge), their thread open (Open figures); `pwr`, the motor's supply (Ports) |

These are generic design values (OPERATING.md 12), not tested ratings or a listing. With hyd-cylinder-da-40 1.0 (bore 40, 160 bar) the
unit extends the rod at 22 l/min / 1256.6 mm² = 292 mm/s; a press's own cylinder and speed are the machine's. The drive motor's
full-load current is derived from its power and voltage (OPERATING.md 6, derive before you ask; review hpu-large-1.2.md finding 1):
`python lib/build.py derive motor 7.5 460` gives 12.08 A, "derived: derive.motor_current(7.5, 460.0, eta=0.917, pf=0.85) (P = √3 V I
η cosφ; η IEC 60034-30-1 Table 3 IE3 4-pole 60 Hz; pf a design value)", in ratings.csv as `fla` (the name the ELR checks read). The
table current NEC 430.6(A)(1) sizes conductors and protection by is a separate figure, tabulated with no formula: NFPA 70 Table 430.250
is not held as a standards table on file, so it stays open, class B, a document wanted (Open figures), not EM's line.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| reservoir | 700 (x) × 450 (y) × 400 (z), z 60 to 460; painted steel, light grey | 126 l inside for 100 l of oil (Class values 4) |
| skids | two, 60 wide × 60 high × 680 long (x −340 to 340), under the reservoir's long sides (y −215 to −155 and 155 to 215), 10 in from its sides and ends; black | lift the reservoir off the floor (a pallet truck's forks go between them); set in so no skid face is flush with the reservoir's (GEO-050: coplanar faces flicker in Godot); no anchor holes in 1.0 |
| lid | 720 × 470 × 12, z 459.5 to 471.5 (10 over the reservoir all round) | carries the motor-pump group, the valve block, the filter and the breather |
| bell housing | Ø250 × 150 on the lid at x = −170, y = 0; zinc-plated | joins the motor's flange to the pump below the lid (the pump and its coupling are not modelled) |
| motor flange | Ø300 × 18 on the bell housing; blue | |
| motor body | Ø260 × 350, z 638 to 988; blue | the 7.5 kW motor's envelope as drawn here is our own: no IEC frame figure (IEC 60072-1 is not in sources.csv) is used |
| fan cowl | Ø240 × 80 on the motor's top, to z = 1067.5 | the motor's fan, air drawn in from above |
| terminal box | 140 × 120 × 120 on the motor's +y side (x −240 to −100, y 100 to 220, z 760 to 880) | the drive motor's terminals |
| cable entry boss (`pwr`) | Ø24 × 12 on the terminal box's +y face at x = −170, z = 800 (to y = 232); zinc-plated | where the supply cable enters, as motor-iec71-370w's entry; no thread or hole cut (Notes) |
| valve block | 170 (x) × 140 (y) × 110 (z) on the lid, x 120 to 290, z 471 to 581; zinc-plated | holds the relief valve and the three ports; the check valve and passages inside are not modelled |
| relief valve | cartridge Ø36 × 70 up from the block's top at x = 165, its adjusting knob Ø50 × 20 on it (to z = 671) | the knob is fixed, no moving node (the setting is the class value, 160 bar) |
| port spot faces | Ø24 × 1 proud: `port-p` and `port-t` on the block's +x face (x = 291) at y = −35 and +35, z = 526.5; `port-g` on the block's top (z = 582) at x = 250 | the joint plane a fitting meets (hyd-cylinder-da-40's); 70 apart, room for a wrench between the two fittings; no bore cut (Open figures) |
| return filter | Ø90 × 128 on the lid at x = 230, y = 150; black | the return oil passes it into the reservoir |
| filler-breather | Ø60 × 50 on the lid at x = 40, y = −150; black | fills the reservoir and lets air in and out as the level moves |
| sight gauge | frame 36 × 200 on the front (x = 250, z 200 to 400, 6 proud), a clear window 20 wide, 1 proud of the frame | the oil's level and temperature, seen from the front |
| envelope | 720 × 470 × 1067.5 (x −360 to 360, y −235 to 235, z 0 to 1067.5) | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-p` | hyd-port | female | supply | the block's +x face, x = 291, y = −35, z = 526.5, axis +x | the pump's delivery, through the relief valve's block, to the machine; design: named P, the trade's letter for the pressure port (toolkit/hyd.py H11); the hydraulic port marking standard (ISO 9461) is not on file, so no mark of the standard's is claimed (Open figures) |
| `port-t` | hyd-port | female | none | the block's +x face, x = 291, y = 35, z = 526.5, axis +x | the machine's return oil, through the return filter to the reservoir; design: named T, the trade's letter for the tank port; ISO 9461 not on file, as `port-p` |
| `port-g` | hyd-port | female | gauge | the block's top, x = 250, y = 0, z = 582, axis +z | the pressure gauge's port (hyd-gauge, a later element); design: named G as frl's and gas-regulator's gauge ports; ISO 9461 not on file, as `port-p` |
| `pwr` | 480V-3P+E | none | | the cable entry boss's face, x = −170, y = 232, z = 800, axis +y | the drive motor's supply: a cable entry to screw terminals (gender none, PIN-002), pins.csv L1 / L2 / L3 (U1 / V1 / W1) and PE, as motor-iec71-370w's `pwr`; review pneu-r51 finding 2 (a 460 V device needs its power port) |

"hyd-port" is the lane's placeholder unit for a hydraulic port whose thread is open (hyd-cylinder-da-40 1.0; no hydraulic contract in
toolkit/ yet, so the unit is the core's to settle); it is no air unit, so the PNE checks
(toolkit/pneu.py, compressed air only) don't pair it, and the roles are what each port does, read by no check yet. A hydraulic
fitting (inventory `fitting-hyd-iso8434`) or hose (`hose-hyd`) meets each port once the port's thread is on file.

## Open figures
- NOT ON FILE (B): the three ports' thread and size (no hydraulic port standard, such as an ISO 6149 or SAE straight-thread port, is
  in lib/standards/sources.csv), as hyd-cylinder-da-40 1.0's ports. Each port is a plain spot face with its pivot; the bores are cut once
  the standard is on file (changed cut-outs: a major version).
- NOT ON FILE (B): ISO 9461, the three oil ports' marks (toolkit/hyd.py H11, request pneu-10's answer item 2: hydraulic port
  identification; lib/standards/sources.csv iso-9461, wanted). The ports are named P, T and G, the trade's letters (Ports), and
  claim no mark of the standard's; when it is on file, hyd.PORT_MARKS takes the marks with their clause and a text minor marks
  these ports from it (hpu-0.37kw 1.0's line).
- NOT ON FILE (B): NFPA 70 Table 430.250, the drive motor's table current at 460 V (NEC 430.6(A)(1): the figure conductors and
  short-circuit protection are sized by; tabulated with no formula; NFPA 70 is free to view, read attended into a standards table).
  The running current is derived (Class values), so no figure of the unit's waits on EM.

## Named nodes
`port-p`, `port-t`, `port-g` (the spot faces) and `pwr` (the cable entry boss); kind port, fixed (range 0). No moving node: the
relief valve's knob is fixed.

## Materials by layer
`M-STEEL-7035` reservoir, lid, port spot faces · `M-BLACK-PA` skids, relief valve knob, return filter, filler-breather, sight gauge
frame · `M-CAST-BLUE` motor flange, body, fan cowl, terminal box · `M-GALV` bell housing, valve block · `M-ZINC` relief valve
cartridge, cable entry boss · `M-CASE-CLEAR` sight gauge window

## Decals (Blender)
None in 1.0 (the "generic" label and the port letters P, T, G are a later version). No vendor names, no approval marks.

## Notes
- One element, as compressor-air 1.0 is: the motor, pump, filter and valves are its own parts, not the inventory's motor-iec,
  hyd-pump, hyd-filter-return or hyd-valve elements placed (the row has no made_of). hpu-0.37kw is the lane's assembly of those elements
  (its row), after them.
- Inside nothing is modelled: the pump, its coupling, the suction line and strainer, the return line, the baffle, the oil, the check
  valve and the passages in the block.
- The supply: `pwr` (480V-3P+E) and pins.csv (L1, L2, L3, PE) are on file, so an assembly can wire the unit (cable-pwr-480); the
  terminals inside the box are not modelled. The cable gland is placed, never redrawn, and a host doesn't model holes now for a part
  it will place later (OPERATING.md 12, quality at the source), so the entry boss has no hole or thread. The motor's full-load
  current is ratings.csv `fla`, 12.08 A derived (Class values); the ELR checks read it in any assembly that wires the unit.
- No drain port, no level or temperature switch, no accumulator or cooler in 1.0 (each a new node, a major; the cooler and
  accumulator are inventory elements of their own, hyd-cooler and accumulator).
- No safety function of its own (inventory.csv's `safety` column is empty for this row): the relief valve's setting is the class
  value, not a safety sign-off. The machine's hydraulic safety review against ISO 4413 is EM's once the standard is on file.

## Outputs (out/)
`hpu-7.5kw.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (no ETIM class; ISO 4413 values), pneu-r58 (unattended): reservoir on two skids, lid, vertical motor-pump group (bell housing, flange, motor, fan cowl, terminal box), valve block with relief valve and knob, spot faces `port-p` / `port-t` / `port-g`, cable entry boss `pwr` (480V-3P+E, pins.csv), return filter, filler-breather, sight gauge; the oil ports' thread left open (class B) |
| 1.1 | text only, pneu-r65 (unattended; review hpu-large-1.0.md findings 1 and 2, pneu-r58 findings 2 and 3): ratings.csv voltage, phases and frequency "derived" from the campus 480 V supply, p_max and power keep their ISO 4413 form; the drive motor's full-load current added to Open figures as class A; "hyd-port" called the lane's placeholder unit (hyd-cylinder-1.0.md finding 2); behaviour.csv added (BEH-010). No shape change |
| 1.2 | text only, pneu-r87 (unattended; request pneu-10's answer item 2): the three oil ports' marks P, T, G called the trade's letters, a design choice, in Ports and behaviour.csv's three pin rows, and added to Open figures as a class B line, ISO 9461 a document wanted (toolkit/hyd.py H11; the line lists the standard once in lib/standards/wanted.md). No shape, node, origin or cut-out change |
| 1.3 | text only, pneu-r90 (unattended; review hpu-large-1.2.md finding 1, ESCAPE, repeated in hpu-7.5kw-1.2.md; note 1 of hpu-large-1.1.md): the drive motor's full-load current derived, 12.08 A from 7.5 kW and 460 V (derive.motor_current, OPERATING.md 6), in ratings.csv as `fla`, so the class A line leaves Open figures; the table current of NFPA 70 Table 430.250 written as a class B line, a document wanted; "fixed in 1.0" read "fixed" (relief knob, Named nodes). No shape, node, origin or cut-out change |
