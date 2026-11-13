# compressor-air · v2.0 · air compressor, generic, oil-free piston, 0.55 kW 120 V 60 Hz, 24 l receiver, 8 bar, outlet NPT 1/4

**What** a small compressor for a trainer bench or a workshop: one oil-free piston pump, driven directly by a single-phase motor,
sits on a 24 l horizontal receiver. A pressure switch starts the motor and stops it at 8 bar; the pump delivers through a copper
pipe and a non-return valve into the receiver; the outlet manifold on the receiver carries the pressure switch, a spring safety
valve and a lever outlet valve with the outlet port (port-2); a quarter-turn drain under the receiver lets the condensate out. It
is our own vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements, EM 2026-11-07): the class values it is
designed to are listed under Class values. No maker's datasheet or CAD was opened or measured.
**Class** machine · **Baseline** our own design: generic air compressor (ETIM 10.0 EC002860). Its outlet takes its figures from the
pneumatic contract, `toolkit/pneu.py` (D1 threads, D7 names, the NPT table); every other size is a design choice
(below). The electrical values are class values, the design inputs of a generic element, not a certification or a listing.
**Units / frame** mm, Z up. Origin: floor machine (lib/README.md): floor plane z = 0; x = 0 at the receiver's left end, y = 0 on
its front-most line; the receiver along +x, the body toward +y, the outlet facing −y. The outlet port follows pneu.py's port frame:
the pivot on the face, its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `COMPRESSOR-AIR` · no parameters.

## Class values
ETIM 10.0 EC002860 "Air compressor" (group EG020014), every feature in ETIM's order (lib/standards/etim/class-features.csv). These
are the values this element is designed to: they define it as a member of the class, and they are design inputs.

| # | feature | value | note |
|---|---|---|---|
| 1 | Type of motor | single-phase AC induction motor | capacitor start; its windings are not modelled |
| 2 | Connection voltage | 120 V | single phase, so it runs from a receptacle circuit on the campus, which follows US codes (the pneu role card) |
| 3 | Frequency | 60 Hz | |
| 4 | Amperage | 9 A | the rated current at the cut-out pressure; a class value, not a measured or listed figure |
| 5 | Number of cylinders | 1 | |
| 6 | Number of outgoing connections | 1 | port-2, on the outlet valve |
| 7 | Tank capacity | 24 l | the shell's inside, Ø255 × 475 (a 2.5 wall): 24.3 l, the dished ends not counted (`capacity_l()`) |
| 8 | Max. pressure | 8 bar | the pressure switch's cut-out |
| 9 | Max. operating pressure (psi) | 116 psi | 8 bar (800 kPa ÷ 6.894757 kPa per psi, pneu.PSI_KPA) |
| 10 | Delivery quantity | not stated | the free air delivered is a test result at a stated pressure (the pump's volumetric efficiency); the displacement (12) is stated |
| 11 | Motor power | 0.55 kW | |
| 12 | Piston displacement per minute | 115 l | bore 50 × stroke 34 × 1720 1/min = 114.8 l (`displacement_l_min()`) |
| 13 | Rotational speed | 1720 1/min | a four-pole motor at 60 Hz, under load; the pump on the motor's shaft |
| 14 | Lubrication type | oil-free | the air needs no oil filter for the bench (pneu.py D4: no lubricator) |
| 15 | Mobile | no | four rubber feet, no wheels |
| 16 | Degree of protection (IP) | IP20 | indoor, dry; IEC 60529 code, the design target |
| 17 | With motor protection | yes | a thermal cut-out in the motor winding, manual reset; not modelled. The branch circuit's protection is the assembly's |
| 18 | With automatic start/stop | yes | the pressure switch: stop at 8 bar, start when the receiver falls; knob `switch` off / auto |
| 19 | Drive | direct | the crank on the motor's shaft, no belt |
| 20 | Hose connection | not stated | the outlet is a threaded port; a hose or a fitting is the assembly's |
| 21 | Connection size outlet | NPT 1/4 female | port-2 (pneu.py D1; ASME B1.20.1); bored from pneu.NPT (below) |
| 22 | With spring security | yes | a spring safety valve on the outlet manifold, on the receiver's side of the outlet valve; its set pressure is not stated and no relief rating is claimed |
| 23 | With non-return valve | yes | between the delivery pipe and the receiver |
| 24 | With outlet valve | yes | a quarter-turn lever valve, node `lever` |
| 25 | With condensate drain | yes | a quarter-turn drain under the receiver's lowest line, node `drain` |
| 26 | Sound performance level | not stated | a sound power level is measured on the product, not designed here |
| 27 | Colour | blue | the receiver, its ends, feet and saddle plate; the motor is light grey, the pump bare aluminium |
| 28 | Width | 51.8 cm | x, the outlet lever closed (`envelope()`) |
| 29 | Height | 54.0 cm | z, floor to the intake filter's top |
| 30 | Depth | 26.0 cm | y, the receiver's diameter (the label plate 0.2 proud of it) |
| 31 | Weight | not stated | the receiver is modelled solid, so the model gives no mass; a weight is weighed |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| receiver shell | Ø260 × 480 (x 15 to 495), axis at y = 130, z = 170, blue painted steel | holds 24 l at a 2.5 wall (class value 7); its underside 40 above the floor clears the drain |
| dished ends | Ø200 × 15 at each end (x 0 to 15, 495 to 510) | shows the heads without modelling their curve |
| foot brackets | 2 × 40 (x) × 240 (y) × 30 (z), at x = 70 and 400, z 15 to 45 | carry the receiver; 330 apart for a stable stance |
| rubber feet | 4 × Ø30 × 15, under the brackets at y = 30 and 230 | stand it on a floor or bench; no anchor holes |
| saddle plate | 260 (x) × 160 (y) × 10 (z), on the receiver's top, z 296 to 306 | carries the motor and the pump |
| motor | frame Ø130 × 160 along x (x 170 to 330), axis z = 381; feet 120 × 90 × 16; fan cover Ø126 × 30 at its left end | 0.55 kW frame, class value 11; node `motor` |
| pump | crankcase 80 × 80 × 124 on the motor's shaft end (x 330 to 410); cylinder Ø70 × 60 at x = 375 (bore 50, stroke 34 inside, not modelled) with four Ø86 × 3 fins; head 76 × 76 × 22; intake filter Ø50 × 28 on the head | class values 5, 12, 19 |
| delivery pipe | Ø8 copper, from the head's right face (z = 501) over to x = 430 and down to the non-return valve | carries the pump's air to the receiver |
| non-return valve | 24 × 24 × 34 brass block on the receiver's top at x = 430 | class value 23 |
| outlet manifold | 40 × 40 × 34 brass block on the receiver's top, x 452 to 492 | carries the pressure switch, the safety valve and the outlet valve |
| pressure switch | 60 (x) × 64 (y) × 70 (z) grey housing on the manifold; rotary knob Ø24 × 12 on its front face | class value 18 |
| cord grip | Ø14 × 12 on the switch's right face | where the supply cord enters (Notes) |
| safety valve | Ø16 × 20 body and Ø12 × 6 cap on the manifold's right face | class value 22 |
| outlet valve | 26 (x) × 32 (y) × 26 (z) brass body on the manifold's front face (x 459 to 485, z 300 to 326), inside that face and 1.5 above the receiver's shell at its back edge (both asserted); stem Ø6 × 5; lever 45 reach, 6 tail, 10 × 3, red coated; nut Ø8 × 3 | class value 24; the lever lies along +x (across the flow) when closed; 26 square so the bore keeps 6.19 of body round it (asserted ≥ 6, filter-air 2.0's figure) |
| outlet port bore | Ø13.616 × 12.205 deep, blind, into the outlet valve's front face (y = 78) | Ø = E1 + h of NPT 1/4 from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), the diameter fitting-pushin 2.0 and gauge-p draw their male stubs at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up (L1 + L3); 19.8 of body behind its floor. The thread is drawn plain. Role in features.csv (HOLE-010) |
| port-number field | 18 × 18, 0.2 proud, centred on the bore, the bore through it | the ISO 11727 number 2 is a decal; 0.2 proud for GEO-050; a 2.19 ring round the bore; the port pivot is on its outer face (y = 77.8) |
| drain | brass boss Ø14 under the receiver at x = 255; knob Ø18 × 8, red | class value 25; 24 above the floor |
| label plate | 120 × 40, on the receiver's front (x 200 to 320, z 150 to 190), 0.2 proud of its front-most line | "complexes.org generic" and the class values 2, 3, 4, 7 and 8 as decals |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-2` | NPT1/4 | female | work (outlet) | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727: 2, the outlet valve's outlet); the circuit's source in an assembly (air-circuit.csv `source`) |

NPT 1/4 is our choice within pneu.THREADS. The port is female and takes sealant on the male (PNE-002). The pivot is on the
number field's outer face (y = 77.8), the joint plane a placed male's shoulder meets (filter-air 3.0's fix); fitting-pushin 2.0's
NPT 1/4 stub (Ø13.616 × 10.205) goes into the bore face to face.

## Ratings (ratings.csv)
The class values the checks read, each "generic design" with its EC002860 feature (OPERATING.md 12; review compressor-air-1.0.md
finding 2): p_max 8 bar (class value 8), voltage 120 V (2), phases 1 (1), frequency 60 Hz (3), fla 9 A (4, the class's Amperage)
and power 0.55 kW (11). They are design inputs, not tested ratings or a listing. PNE-003 reads p_max against the line the
compressor feeds: 8 bar (800 kPa) is above the bench drop's 100 psig (689.476 kPa, pneu.py D3), so it passes as a part on that
line, and as a source it can put more than the drop's pressure on it: the regulator and relief valve that hold the drop are the
assembly's (Notes).

## Open figures
- NOT ON FILE (B): NEC Table 430.248, the full-load current of a 0.55 kW (3/4 hp) single-phase motor at 115 V: the table
  current a branch circuit's conductors and protection are sized from (NEC 430.6(A)(1)), ratings.csv's `fla_table` as
  motor-iec71-370w's. NFPA 70 is free to view and that table has not been read attended (lib/standards/sources.csv), so
  ratings.csv has no `fla_table` row and nothing is claimed. The class value (Amperage, 9 A) stands as the design input; the
  two are compared when the table is read (review compressor-air-1.0.md note 1). A wired assembly needs the cord and `pwr`
  first (Notes).

The outlet's thread line of 1.0 is closed: pneu.NPT holds NPT 1/4 (calculated from ASME B1.20.1's formulas), and the bore is cut
from it.

## Named nodes
`port-2` (kind port, fixed; range 0) · `motor` (fixed: the motor frame, its feet and fan cover; the twin runs or stops it) ·
`switch` (rotate about −y at the switch housing's front face, 0 to 90°: off to auto) · `lever` (rotate about −z at the outlet
valve's top, 0 to 90°: closed, across the flow, to open, along it; the stem and the nut are part of the node) · `drain` (rotate
about −z at the boss's underside, 0 to 90°: closed to open)

## Materials by layer
`M-BLUE` receiver, ends, foot brackets, saddle plate · `M-GASKET` rubber feet · `M-STEEL-7035` motor frame and feet ·
`M-BLACK-PA` fan cover, intake filter, cord grip · `M-ALU-7035` crankcase, cylinder, fins, head · `M-CU` delivery pipe ·
`M-BRASS` non-return valve, manifold, outlet valve, stem, safety valve, drain boss · `M-GREY-PA` pressure switch housing ·
`M-RED-PA` switch knob, outlet lever coating, drain knob · `M-ZINC` lever nut · `M-WHITE-PA` port field, label plate

## Decals (Blender)
"2" on the port field (ISO 11727); "OFF" and "AUTO" around the switch knob; "OPEN" and "CLOSED" on the outlet lever; "complexes.org
generic", "120 V 60 Hz 9 A", "0.55 kW", "24 l" and "8 bar / 116 psi max" on the label plate; a hot-surface pictogram on the pump
head is the assembly's (signs are their own elements). No vendor names, no approval marks.

## Notes
- The supply cord and its plug are not modelled yet: the cord enters at the cord grip, and its plug (a 120 V, 15 A
  configuration) is shaped by a standard that is not among the standards on file (lib/standards/sources.csv, connectors.csv). The
  cord, its plug, a port node `pwr` and pins.csv come in a later version (a new node: a major one). The pins need a role for the
  neutral conductor, which lib/README.md's pin roles do not have yet (cloud round 2 asked the core; still open at pneu-r82).
  Until then the compressor cannot be wired in an assembly: ratings.csv holds its 120 V and 9 A, and ELR reads them once a
  `pwr` port carries them.
- The receiver can reach 8 bar (116 psi), above the bench drop's 100 psig (pneu.py D3): the room regulator and relief valve that
  hold the drop are the assembly's. The safety valve here is the compressor's own and claims no rating.
- No safety function of its own (inventory.csv has no row for it). A pressure receiver's construction code is not on file; no
  vessel stamp, listing or approval mark is shown or claimed.
- Not placed: the pressure gauges and the outlet regulator a workshop unit often carries, so the receiver has no gauge port in
  this version (gauge-p and regulator are built since; a gauge port and the placed gauge are a later major).

## Outputs (out/)
`compressor-air.lsp` · `.glb` (port, motor, switch, lever and drain pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/,
step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002860), cloud-pneu round 2, 2026-11-07 (the core chat's cloud builder, the PC being down): receiver, ends, feet, saddle plate, motor, pump, delivery pipe, non-return valve, manifold, pressure switch, safety valve, outlet valve with its port and lever, drain, label plate; stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r82 (unattended; review compressor-air-1.0.md findings 1 and 2): the outlet's bore Ø11.5 × 12 → Ø (E1 + h) × (L2 + 2) deep = Ø13.616 × 12.205 from pneu.NPT, its role in features.csv; the outlet valve's body 20 → 26 square (6.19 of wall round the bore, asserted), so the stem, lever and nut sit 3 higher; port-number field 16 → 18; the port pivot on the field's outer face (filter-air 3.0's fix); the thread line closed (pneu.NPT on file); ratings.csv with the class values the checks read (p_max 8 bar, 120 V, single phase, 60 Hz, fla 9 A, 0.55 kW); the table current of NEC Table 430.248 written as a class B line (a document wanted); nodes and envelope unchanged |
