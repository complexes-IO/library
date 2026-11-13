# valve-ball-32 · v1.1 · three-way ball valve, generic, manual 3/2 (L-port ball), three NPT 1/4 female ports in a T, quarter-turn lever

**What** a hand-worked three-way valve: three ports in a T round a square body and a ball with one L-shaped passage, turned a
quarter turn by a lever on top. In position a (the lever at 0°) the ball joins port-1 to port-2 and shuts port-3; in position b
(90°) it joins port-2 to port-3 and shuts port-1. With the supply on port-1, a single-acting cylinder or a line on port-2 and port-3
to atmosphere (through a silencer), it fills the line or vents it by hand: a manual 3/2 valve in ISO 1219's terms, hence the id's
"32" (OPERATING.md 6, the id convention; valve-ball-42's sibling, no rest state since the lever stays where it is put). It is our
own vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements, EM 2026-11-07; the next class `python
lib/build.py inventory pneu` lists after EC010030): the class values it is designed to are listed under Class values. It is not the
inventory's `valve-ball` row (a 2-way ball valve with an ISO 5211 actuator flange, which waits on that standard). No maker's
datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic three-way ball valve (ETIM 10.0 EC011540). What it meets takes its figures
from the pneumatic contract, `toolkit/pneu.py` (D1 threads, ROLES, NODES, and the NPT table, values calculated from ASME B1.20.1's
formulas, EM 2026-11-07); every other size is a design choice (below). Threaded connections only, no coupling and no flange (class
values 7, 10, 13 and 15), so nothing in its shape waits on a dimensional standard.
**Units / frame** mm, Z up. Origin: the body's centre, on the plane of the three port axes (x = 0, y = 0, z = 0): port-1 toward −x,
port-2 +y, port-3 +x, no port on the −y face; the lever on top (+z). Ports follow pneu.py's port frame: the pivot on the joint plane
(the number field's outer face, where the counterpart's face stands when it is screwed home), its axis out of the body toward the
counterpart.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-BALL-32` · no parameters.

## Class values
ETIM 10.0 EC011540 "Three-way ball valve" (group EG020069), every feature in ETIM's order (lib/standards/etim/class-features.csv).
These are the values this element is designed to: they define it as a member of the class, and they are design inputs.

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | brass | body, boss and stem; the lever is coated steel |
| 2 | Material quality | not stated | no alloy designation is claimed |
| 3 | Nominal diameter | not stated | the class asks a DN; NPT 1/4 is an inch thread size (class values 5, 8, 11) and DN designations are not among the standards on file |
| 4 | Outer pipe diameter connection 1 | not stated | a threaded connection: no pipe end is claimed |
| 5 | Connection 1 | female thread NPT 1/4 | port-1, supply (pneu.py D1) |
| 6 | Outer pipe diameter connection 2 | not stated | as 4 |
| 7 | With coupling connection 1 | no | |
| 8 | Connection 2 | female thread NPT 1/4 | port-2, work |
| 9 | Outer pipe diameter connection 3 | not stated | as 4 |
| 10 | With coupling connection 2 | no | |
| 11 | Connection 3 | female thread NPT 1/4 | port-3, exhaust |
| 12 | Article compression class | not stated | no PN class is claimed (PN designations are not among the standards on file) |
| 13 | Flange compression class | not stated | no flange |
| 14 | Max. pressure difference at 20 °C | 10 bar | the shut port against the other two: in position b port-1 at supply pressure stands against port-3 at atmosphere; the same figure as 16 |
| 15 | With coupling connection 3 | no | |
| 16 | Max. operating pressure | 10 bar | in ratings.csv as p_max, status "generic design"; 1000 kPa is above P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it on a bench line (element.py asserts it) |
| 17 | Medium temperature (continuous) | 0 to 60 °C | filtered compressed air (pneu.py D4) |
| 18 | Surface protection | none | bare brass; the lever coated |
| 19 | Medically clean | no | |
| 20 | Grease-free | not stated | the seats' lubricant is not claimed |
| 21 | Operation | hand lever | a quarter turn between position a (0°) and position b (90°) |
| 22 | Sealing | PTFE seats | the ball's seats (not modelled); the NPT joints seal on the thread with sealant on the male (pneu.py D1; PNE-002) |
| 23 | Full bore | no | the passage is not modelled; no flow figure is claimed |
| 24 | Ball bore | L-port | one L-shaped passage: 1-2 or 2-3 |
| 25 | Zeta value | not stated | no flow figure is claimed |
| 26 | Length of connection 1 | 12.2 mm | each bore's depth, L2 + 2 (12.205) |
| 27 | Working length connection 1 | not stated | the thread is drawn plain; no make-up length is claimed beyond pneu.NPT's |
| 28 | Length of connection 2 | 12.2 mm | as 26 |
| 29 | Working length connection 2 | not stated | as 27 |
| 30 | Length of connection 3 | 12.2 mm | as 26 |
| 31 | Working length connection 3 | not stated | as 27 |
| 32 | Handle height | 30 mm | the port axes' plane to the lever nut's top: 15 + 5 boss + 4 stem + 3 lever + 3 nut |
| 33 | Handgrip length | 60 mm | the lever's reach from the stem axis |
| 34 | Side 1 - side 2 angle | 90° | port-2 on +y, at a right angle to port-1 on −x |
| 35 | Side 1 - side 3 angle | 180° | port-3 on +x, opposite port-1: the T's run |
| 36 | Kvs value | not stated | no flow figure is claimed |
| 37 | Suitable for heating | no | an air valve |
| 38 | Suitable for cooling | no | an air valve |
| 39 | EFSE0002 Type approval according to BBR/EKS | no | no approval marks on our elements (OPERATING.md 6) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 50 × 50 in plan, 30 high, brass, centred on the origin | valve-ball-42 1.0's body, carrying one port on each of three side faces; each bore's floor 12.795 from the centre, so 5.99 of brass between port-2's floor and port-1's or port-3's side and 8.47 across each corner, 25.59 between port-1's and port-3's floors (element.py asserts at least 3), and 8.19 above and below each bore |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, one on each of the −x, +y and +x faces on its port axis at z = 0 | the female NPT 1/4 at the male stub's own diameter, so a placed male (fitting-pushin 2.0, silencer 1.0) meets the bore face to face and never overlaps it (tank 2.0's rule); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 (10.02). Declared in features.csv (HOLE-010) |
| port-number fields | 18 × 18, 0.2 proud, one on each ported side face, each bore through its field | "1" to "3" are decals (ISO 11727); 0.2 proud for GEO-050. Each port's pivot stands on its field's outer face (±25.2), so a placed fitting's seat meets the field face to face (filter-air 3.0's rule) |
| stem boss | Ø14 × 5, brass, on the top face's centre | holds the stem |
| stem | Ø6 × 4 showing between the boss and the lever | turns with the lever |
| lever | 12 wide × 3 thick, reaching 60 from the stem axis with a 6 tail, black coated steel, 9 above the body's top | class values 21 and 33; it sweeps over the body's top, clear of the ports and the fittings placed in them |
| lever nut | Ø10 × 3 on the stem's top | holds the lever |
| travel | 0 to 90°, about −z: the lever points toward −y (the unported face) in position a and toward −x (over port-1, the shut port) in position b | a quarter turn; the lever's position names the state, the 3/2 symbol on the label shows the passage. The L passage turns with the lever: its legs toward −x and +y (1 to 2) go to +y and +x (2 to 3); turned about +z they would go to −y and −x and shut all three (1.1, review valve-ball-32-1.0.md finding 1) |
| label field | 16 × 10, 0.2 proud, on the top face, centred at x = −14, y = 15 (the quarter the lever never sweeps) | "complexes.org generic" and the 3/2 symbol (ISO 1219-1, drawn as a decal) |
| height | 45: 30 body + 5 boss + 4 stem + 3 lever + 3 nut | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | pneu.py D1 (NPT, ASME B1.20.1); ISO 11727's 1 for the supply (pneu.NODES) |
| `port-2` | NPT1/4 | female | work | as above; ISO 11727's 2, the work port |
| `port-3` | NPT1/4 | female | exhaust | as above; ISO 11727's 3, the exhaust (pneu.NODES exhaust) |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002). pneu.NPT holds NPT 1/4's
figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 13.616 (the bore), L2 = 10.205 (the bore is
L2 + 2 deep), L1 + L3 = 10.02 (a male's make-up). The helix is not modelled: the bore is the thread drawn plain.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file (pneu.NPT).

## Named nodes
`port-1`, `port-2`, `port-3` (kind port, fixed; each its number field, the pivot on the field's outer face) · `lever` (rotate about
−z on the boss's top face, 0 to 90°: position a to position b, −y to −x; the stem and the nut are part of the node)

## Materials by layer
`M-BRASS` body, boss, stem · `M-BLACK-PA` lever coating · `M-ZINC` lever nut · `M-WHITE-PA` fields

## Decals (Blender)
"1" to "3" on the port fields (ISO 11727); "complexes.org generic" and the 3/2 symbol on the label field; "A" and "B" with a
quarter-turn arrow on the lever's top. No vendor names, no approval marks.

## Ratings (ratings.csv)
`p_max` 10 bar, status "generic design", source "ETIM 10.0 EC011540 class value" (class value 16, EF020449; OPERATING.md 12:
ratings the checks read go in ratings.csv). P_SUPPLY (100 psig, 6.9 bar) is below it.

## Notes
- In line: it is carried by its pipework or fittings (fitting-pushin 2.0, or another male NPT 1/4, placed by the assembly; a
  silencer 1.0 on port-3). It has no mounting holes and no panel nut; either is a later version.
- The ball, its seats and passage are not modelled; the twin reads the lever's angle (0 position a, 90 position b).
- No safety function: it holds no position by itself against a load and is not the lockable 3/2 shut-off and dump valve PNE-008
  asks for after the drop (it has no hasp and no spring to the vented position).

## Outputs (out/)
`valve-ball-32.lsp` · `.glb` (port and lever pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, pneu-r95 (unattended), generic (ETIM 10.0 EC011540): valve-ball-42 1.0's square body with three port bores and their fields in a T (−x, +y, +x), boss, stem, lever and nut, label field on top; ratings.csv p_max (generic design); behaviour.csv (three pins, the lever's two states and pose) |
| 1.1 | pneu-r108 (unattended), review valve-ball-32-1.0.md: (1) the lever turns about −z (−y to −x, over port-1 in position b), so the L passage joins 2 to 3 in position b as What and behaviour.csv say; about +z it shut all three ports; (2) the coupling and flange class values are 7, 10, 13 and 15 (18 is Surface protection). Nodes, origin and cut-outs unchanged (a minor); geometry at rest unchanged |
