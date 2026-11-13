# gripper · v2.0 · parallel pneumatic gripper, generic, 2 jaws, stroke 10 per jaw, body 64 x 40 x 80 with 2 x NPT 1/8 port bosses, 4 x M6 tapped mount

**What** A parallel pneumatic gripper: the end effector a robot (robot-cell, robot-tending-cell, cobot-bench) or a pick-and-place
axis (servo-pick-and-place) carries to take and release a part. An anodised aluminium body hangs from a flange by four tapped
holes in its underside; a piston inside (not drawn) drives two jaw carriers through a wedge hook, in and out along x in a guide
slot across the body's top, opposed and together; each carrier ends in a finger block with two tapped M4 holes in its top face
where the application's fingers bolt on, so a finger stands on its block and its own gripping face is the application's. Two female NPT 1/8 air ports in bosses on the −y face: air at `port-close` drives the jaws in by
the stroke, air at `port-open` drives them out (double acting, no spring). lib/inventory.csv row `gripper` (own_design generic,
"parallel gripper", etim EC004755, made of fitting-pushin x2, prox-m12, screw-iso4762; 4 systems).
**Class** actuator · **Baseline** our own design: generic gripper (pneumatic/hydraulic) (ETIM 10.0 EC004755), OPERATING.md 12
"Generic elements" (EM, 2026-11-07); the inventory row is own_design "generic" with its class on file (three features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened: the folder's reference record
(an electric collaborative gripper, references/source.txt) is not what this element is built from. The ports follow the pneumatic
contract on file (toolkit/pneu.py D1: NPT, bores from ASME B1.20.1's formulas); the threads it carries are derived from ISO 68-1
and ISO 965-1; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face plane (z = 0, the body's underside) at the body's centre. +z goes up through
the body (z 0 to 80) to the jaws (z 74 to 106); the jaws move along x, opposed; the port bosses stand toward −y (their faces at
y −30). Extents x ±32, y −30 to 20, z 0 to 106.
**Built with** toolkit 1.3 · AutoLISP command `GRIPPERPAR` · no parameters.

## Class values
ETIM 10.0 class EC004755 Gripper (pneumatic/hydraulic) (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every
feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the
element.

| # | feature | value |
|---|---|---|
| 1 | Type of drive (EF001422) | pneumatic: double acting, a Ø20 piston with a Ø8 rod inside the body (not drawn), one port each way |
| 2 | Number of arms (EF009111) | 2 (the jaws `jaw-l` and `jaw-r`, parallel, opposed, moving together) |
| 3 | Holding force (EF013335) | 94 N per jaw, 188 N in all, at 600 kPa (6 bar), the class value's datum pressure (a design choice): the piston's push 0.6 N/mm² × 314.2 mm² = 188.5 N (derived: derive.cylinder(20.0, 8.0, 6.0) (F = p A), as `python lib/build.py derive cylinder 20 8 6` prints it) shared by the two jaws through a 45-degree wedge hook (tan 45° = 1), ideal, no friction and no return-side loss. At the bench's highest working pressure, 551.6 kPa (toolkit/pneu.py P_WORK_MAX, 80 psig), 87 N per jaw. element.py `jaw_force_n` |

No ratings.csv: the class has no pressure, flow or temperature feature, and a "generic design" rating needs a class feature behind
it (GEN-010). The pressure the twin feeds the ports is the circuit's (pneu.py P_SUPPLY, P_WORK_MAX; PNE checks where it is placed).

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-close` | NPT1/8 | female | work | the left boss's face, (−16, −30, 40), axis −y | toolkit/pneu.py D1 (every threaded air port NPT 1/8, 1/4 or 3/8); the name is this design's (pneu.NODES names cylinder ends port-cap / port-rod and no gripper port): air here drives the jaws in |
| `port-open` | NPT1/8 | female | work | the right boss's face, (16, −30, 40), axis −y | as port-close: air here drives the jaws out |

Each port is a blind bore Ø10.242 × 8.702 in its boss: E1 + h, the male's major diameter at the hand-tight plane, drawn plain so
the halves touch (tank 2.0's rule, as fitting-pushin 2.0 draws its stub), L2 + 2 deep (a run-out past the male's effective
thread, actuator-valve 1.0's way), from ASME B1.20.1's formulas in toolkit/pneu.py (EM 2026-11-07: calculated values until a
licensed Table 2 is on file). The push-in fittings (fitting-pushin 2.0, thread=NPT1/8, tube 1/4, past station 6) are placed in a
later version from a bom.csv; 1.0 models the ports only.

## What it meets
| figure | value | source |
|---|---|---|
| the flange it hangs on | four tapped M6 holes in the underside (z = 0) on a 40 × 24 pattern (x ±20, y ±12), 12 deep, drawn at the thread's minor diameter Ø4.9175 | derived: `python lib/build.py derive thread M6` (ISO 68-1 basic profile; ISO 965-1 clause 10, internal 6H: D1 4.9175 to 5.1475; ISO 261 pitch 1). M6 and the pattern are this design's choices (no robot flange standard is on file, so no ISO 9409-1 pattern is claimed); the flange's Ø6.6 clearance holes (ISO 273 medium, lib/standards/holes.csv) and the socket head cap screws (ISO 4762, the inventory's made_of screw-iso4762, a common part not built yet: the holes are modelled, the part placed later) are the host's. Position: with the host's clearance holes the two parts share T ≤ H − F = 0.6 (ASME Y14.5 fixed fastener); this design takes Ø0.3 at MMC for its tapped pattern and leaves Ø0.3 to the host, a design choice written here (features.csv kind `own`: no clearance hole of its own) |
| the application's fingers | two tapped M4 holes in each finger block's top face (z 106, drilled along −z) at the block's centre x ±16, y ±4.5, 6 deep, at Ø3.2422 | derived: `derive thread M4` (ISO 965-1 6H D1 3.2422 to 3.4224; pitch 0.7). The fingers themselves are the application's (not drawn): each stands on its block's top, so nothing bolted on lies in the gap the jaws close (22 open, 2 closed) and the closed pose stays reachable with fingers on; how far the fingers' own gripping faces close is the application's |
| the air lines | two female NPT 1/8 ports (Ports) | toolkit/pneu.py D1 |
| the sensor | nothing drawn | the inventory's made_of lists prox-m12 (jaw position sensing); its bracket and the sensing target are a later version's, once the application fixes where it reads (open, closed or a part held) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 64 (x) × 40 (y) × 80 (z 0 to 80), anodised aluminium (`M-ALU-ANOD`) | room for a Ø20 piston along z with 10 of wall each way, the guide slot above it and the ports beside it; the piston, its rod, the wedge hook, the end cap and the seals are inside and not drawn (internal mechanism, class C) |
| guide slot | 20 wide (y ±10) × 6 deep (z 74 to 80) across the top along x, open at both ends | the carriers run in it, 0.5 clear of each wall; open ends so the slot is two plain cuts (the gate skips cut edges) |
| jaw carriers | 18 (x) × 19 (y) × 12 (z 74 to 86) each, bright steel (`M-SILVER`); inner faces at x ±11 open, outer at ±29 | 6 in the slot and 6 above; 3 inside the body's sides at full open, so no carrier face lies in a body face's plane (GEO-050) |
| finger blocks | 10 (x) × 19 (y) × 20 (z 86 to 106) on each carrier's inner end, 0.5 into it (one joint) | the top face is where the application's fingers bolt on; 10 thick so its 10 top edges clear the gate's 3 to 7 mm free-corner trap at r 0.5 (mech-r101), 3.4 of steel round each M4 hole in x and y and 14 under the 6-deep holes |
| stroke | 10 per jaw: 22 between the fingers open, 2 closed | a small-part gripper's range; the 2 keeps the two nodes apart at the end of travel (MOT-010) |
| port bosses | Ø18 × 10 on the −y face at x ±16, z 40, 0.5 into the body, in their port's node | 3.9 of wall round the pipe OD 10.29 (3 is actuator-valve 1.0's rule); 10 long takes the male's effective thread L2 6.70 and its make-up L1 + L3 6.92 with 2 to spare; the axes 32 apart (14 between the bosses) leave 16.3 between two fittings' hexes (fitting-pushin's 14 AF, corners 15.7) |
| mount holes | 4 × M6, 12 deep (2 d), 40 × 24 pattern | a thread engagement of 2 d in aluminium; 5 or more of wall to every face; the ports' bosses start 19 above them |
| piston, rod, datum pressure | Ø20, Ø8, 600 kPa | the Holding force class value's inputs (Class values 3); the piston is not drawn |
| load, mass, speed, repeatability, finish | not claimed | no figure is on file for them and no ETIM feature of this class states them; the layers show anodised aluminium and bright steel, no grade is claimed |

## Mechanism
Two moving nodes, `jaw-l` (the left carrier with its finger block) and `jaw-r` (the right), each translate along x toward the
centre, range 0 to 10 mm: jaw-l along +x from its pivot (−20, 0, 74), jaw-r along −x from (20, 0, 74). As modelled both stand
open (the rest pose: 22 between the fingers); at the end of travel 2 stays between them. Through the travel each carrier slides on
the slot's floor (face to face at z 74) between the slot's walls (0.5 clear); nothing else is in its way (the port bosses are on
the −y face, z 31 to 49, well under the slot). The piston drives both through its wedge hook, so they move together: one state
pair for both. behaviour.csv: states `open` (default) and `closed` (manual toggle, the stand-in for air at port-close until the
pneumatic circuit model drives it), pose of both jaws at the range end in `closed`, a limit row with the holding force per jaw.
`port-close` and `port-open` are fixed port nodes (range 0).

## Named nodes
`jaw-l`, `jaw-r`: translate along x, range 0 to 10 (Mechanism). `port-close`, `port-open`: kind port, fixed. Colliders, axis-aligned
boxes: `housing` (x ±32, y ±20, z 0 to 80), `finger-l` (x −29 to −11, y ±9.5, z 74 to 106), `finger-r` (x 11 to 29, the same);
none shares a name with a glb node (2.0: the body's collider renamed from `body`, the fixed mesh node's name).

## Materials by layer
`M-ALU-ANOD` the body and the port bosses (anodised aluminium) · `M-SILVER` the jaw carriers and finger blocks (bright hardened
steel).

## Decals (Blender)
"complexes.org generic" on the body's +y face, centred.

## Notes
No vendor names, part numbers or marks. No load, mass, speed or repeatability claim: no figure is on file for them and the element is
not sized against a load; the holding force is the piston's arithmetic (Class values 3), not a test. A gripper is in the ETIM
classes on file and not a part a dimensional standard shapes, so it is built generic to its class (OPERATING.md 12); an angular
gripper, a three-jaw gripper or an electric gripper is another class value or another element. Not drawn: the piston, rod, wedge
hook, end cap and seals (inside the body), the push-in fittings, the screws, the sensor and its bracket, the application's fingers,
the flange it hangs on (the hosts' or later versions'). No open figure: the ports and threads come from the contract and standards on
file (toolkit/pneu.py, ISO 68-1, ISO 965-1), the host's holes are ISO 273's, the holding force is derived, and the rest are design
choices.
The gate's fillet rule (r 0.5 for an actuator, lib/toolkit/fillet.py): every free-corner edge is 10 or longer (the finger blocks'
10, the carriers' 12, 18 and 19, the body's 40, 64 and 80, the bosses' circular edges Ø18); the slot's and bores' edges are cut
edges, skipped; the bosses' inner circular edges and the fingers' lower edges lie buried. The bounding box's extremes lie on the
body (x ±32, y 20, z 0: an axis-aligned box), the bosses' end faces (y −30: cylinder ends on the y axis) and the finger blocks'
tops (z 106: top-level nodes); nothing is tilted or nested.

## Outputs (out/)
`gripper.lsp` · `.glb` (pivots on `jaw-l`, `jaw-r`, `port-close`, `port-open`; `-colonly` colliders) · `preview-*.png`. Terminal:
dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004755), our own design (mech-r104, unattended, 2026-11-11): body with guide slot, two jaw nodes with finger blocks, two NPT 1/8 port bosses, four tapped M6 mount holes; the fittings, screws and sensor placed later |
| 2.0 | review gripper-1.0 (mech-r109, unattended, 2026-11-12). Finding 1: the four M4 finger holes moved from the finger blocks' gripping faces to their top faces (x ±16, y ±4.5, 6 deep along −z), so fingers bolted on never stand in the gap the jaws close; a cut-out change, so a major (OPERATING.md 7; nothing places gripper). Finding 2: Class values 3 cites derive.cylinder's F = p A with no clause; the bosses' spacing reads 32 between axes; the body's collider renamed `housing`. behaviour.csv: the NPT pins' torque `not claimed` (lib/behaviour.md, pin). Nodes, origin, ports and the jaws' range unchanged |
