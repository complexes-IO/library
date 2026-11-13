# valve-air-shutoff · v2.1 · compressed air valve, generic, manual 2/2 shut-off, in line, NPT 1/4, quarter-turn lever

**What** a hand shut-off for an air line (an air cock): a ball turned by a lever on top opens or closes the way between port-1 and
port-2; a quarter turn takes it from closed (the lever across the flow) to open (the lever along the flow). It is a 2/2 valve: it
has no exhaust, so closing it traps the air downstream, and it takes no lock. It is our own vendor-neutral design of the ETIM class
below (OPERATING.md 12, generic elements, EM 2026-11-07): the class values it is designed to are listed under Class values. No
maker's datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic compressed air valve (ETIM 10.0 EC010590). What it meets takes its figures
from the pneumatic contract, `toolkit/pneu.py` (D1 threads, D7 names, pneu.NPT for the bores); every size the contract and the
standards on file don't fix is a design choice (below).
**Units / frame** mm, Z up. Origin: port-1's face centre, in line: the port axis is the x axis, flow along +x, the lever on top
(+z), the label face toward −y. Ports follow pneu.py's port frame: the pivot on the face, its axis out of the body toward the
counterpart.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-AIR-SHUTOFF` · no parameters.

## Class values
ETIM 10.0 EC010590 "Compressed air valve" (group EG020069), every feature in ETIM's order (lib/standards/etim/class-features.csv).
These are the values this element is designed to: they define it as a member of the class, and they are design inputs.

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | brass | body, boss and stem; the lever is coated steel |
| 2 | Size of thread connection (inch) 1 | 1/4 | NPT 1/4 (pneu.py D1) |
| 3 | Size of thread connection 1 | not stated | the class asks a metric size in mm; NPT 1/4 is an inch size (class value 2) |
| 4 | Connection 1 | female thread NPT 1/4 | port-1, inlet (pneu.py D1) |
| 5 | Connection 2 | female thread NPT 1/4 | port-2, outlet (pneu.py D1) |
| 6 | Article compression class | not stated | no PN class is claimed |
| 7 | Max. operating pressure at 20 °C | 10 bar | in ratings.csv as p_max, status "generic design" (2.0); 1000 kPa is above P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it on a bench line (element.py asserts it) |
| 8 | Max. medium temperature (continuous) | 60 °C | compressed air |
| 9 | Seal, connection 2 | none on the valve | NPT seals on the thread, with sealant on the male (pneu.py D1; PNE-002) |
| 10 | Operation | hand lever | a quarter turn, closed (across the flow) to open (along the flow) |
| 11 | Double compressed-air valve | no | one way through, one lever |
| 12 | With key | no | it takes no lock and no key |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 44 (x, along the flow) × 26 (y) × 26 (z), brass, centred on the port axis in y and z | carries both ports on its end faces, 6.19 wall around each bore (2.0) |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, on the port axis, one in each end face (2.0) | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0, gauge-p), so a placed male meets the bore face to face (tank 2.0's rule, review cloud-pneu 2026-11-07-r2 finding 1); deeper than a male's make-up L1 + L3 (10.02); 19.6 of body between the two floors, 6.19 of wall round each (element.py asserts at least 10 and 6). Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it (2.0: 16 → 18, a ring round the wider bore) | the ISO 11727 number is a decal; 0.2 proud for GEO-050 |
| stem boss | Ø14 × 5, brass, on the body's top face at mid-length (x = 22) | holds the stem |
| stem | Ø6 × 4 showing between the boss and the lever | turns with the lever |
| lever | 12 wide × 3 thick, reaching 50 from the stem axis with a 6 tail, red coated steel | class value 10; the colour reads as a shut-off |
| lever nut | Ø10 × 3 on the stem's top | holds the lever |
| travel | 0 to 90°, about +z: the lever points toward −y (across the flow) when closed and along +x (toward port-2) when open | a quarter turn |
| label field | 28 × 10, 0.2 proud, centred on the body's label face (−y) | "complexes.org generic" and the flow arrow 1 → 2 |
| height | 41: 26 body + 5 boss + 4 stem + 3 lever + 3 nut | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply (inlet) | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727: 1 inlet) |
| `port-2` | NPT1/4 | female | work (outlet) | as above (ISO 11727: 2 outlet); the ball shuts both ways |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002). pneu.NPT holds NPT 1/4's
figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 13.616 (the bore), L2 = 10.205 (the bore is
L2 + 2 deep), L1 + L3 = 10.02 (a male's make-up). The helix is not modelled: the bore is the thread drawn plain.

## Open figures
None. 1.0's one open figure (the NPT 1/4 thread, while pneu.NPT was empty) is closed in 2.0 by pneu.NPT on file.

ratings.csv (2.0, review cloud-pneu 2026-11-07-r2 finding 2; OPERATING.md 12): p_max 10 bar, status "generic design", source
class value 7 (EF023116), so PNE-003 reads it in an assembly.

## Named nodes
`port-1`, `port-2` (kind port, fixed; range 0) · `lever` (rotate about +z on the boss's top face, 0 to 90°: closed to open; the
stem and the nut are part of the node)

## Materials by layer
`M-BRASS` body, boss, stem · `M-RED-PA` lever coating · `M-ZINC` lever nut · `M-WHITE-PA` fields

## Decals (Blender)
port numbers 1 and 2 on their fields (ISO 11727); the flow arrow 1 → 2 and "complexes.org generic" on the label field; "OPEN" and
"CLOSED" with a quarter-turn arrow on the lever's top. No vendor names, no approval marks.

## Notes
- No safety function. It is not an energy-isolating device: it takes no lock and does not vent the air it traps, so it is not the
  lockable 3/2 shut-off and dump valve PNE-008 asks for first after the drop (29 CFR 1910.147; the frl row). It shuts a branch
  off for convenience.
- In line: it is carried by its pipework or fittings (fitting-pushin 2.0, or another male NPT 1/4, is placed by the assembly). It has no
  mounting holes and no panel nut; either is a later version. The ball and its seats inside are not modelled (the twin reads the
  lever's angle: 0 closed, 90 open).

## Outputs (out/)
`valve-air-shutoff.lsp` · `.glb` (port and lever pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from
the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010590), cloud-pneu round 2, 2026-11-07 (the core chat's cloud builder, the PC being down): body, bores, fields, boss, stem, lever and nut; stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r63 (unattended; review cloud-pneu 2026-11-07-r2 findings 1 and 2): each port's bore Ø11.5 × 12 → Ø13.616 (E1 + h) × 12.205 (L2 + 2) from pneu.NPT, its role in features.csv; port-number fields 16 → 18; the thread line closed (pneu.NPT on file); ratings.csv p_max 10 bar (class value 7); nodes and origin unchanged |
| 2.1 | review valve-air-shutoff-2.0.md finding 2, pneu-r72 (unattended): Notes name fitting-pushin 2.0 (built, station 6) as the male the assembly places. Text only: a minor. Finding 1 (the inventory row's "(lockable)") is the core's: request pneu-7 |
