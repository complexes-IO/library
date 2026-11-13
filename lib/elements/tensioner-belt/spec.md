# tensioner-belt · v2.0 · belt tensioner, generic, spring-activated swing arm, flat roll Ø40 × 25, travel 30, 250 N, base 2 × M8

**What** A spring-activated belt tensioner: screwed to a machine frame beside a belt drive, it holds an idler roll against the
belt's slack side so the belt stays tight as it stretches. A base flange with two M8 holes and a spring housing on it; an arm on a
journal on the housing's axis carries a flat idler roll on its free end, and a torsion spring inside the housing swings the arm
against the belt. The arm is the mechanism: the twin swings it by name as the belt pushes the roll back.
**Class** device · **Baseline** our own design: generic spring-activated belt tensioner (ETIM 10.0 EC010722), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design
inputs; the holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face (the base flange's underside) at z = 0, the arm's pivot axis (the housing's
axis) at x = 0, y = 0, the axis along +z. At the free stop, as built, the arm reaches toward +x with the roll's axis at x = 58,
y = 0; the belt pushes the roll back and the arm round toward +y.
**Built with** toolkit 1.3 · AutoLISP command `BELTTENS` · no parameters.

## Class values
ETIM 10.0 class EC010722 Spring-activated belt tensioner (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every
feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the
element.

| # | feature | value |
|---|---|---|
| 1 | Height (EF000040) | 76 mm: the mounting face to the roll axle's end, along the pivot axis |
| 2 | Width (EF000008) | 50 mm: the base flange and the spring housing across (y), at the free stop |
| 3 | Roll width (EF023008) | 25 mm: the idler roll's running face, along its axis |
| 4 | Max. tensile force (EF000353) | 250 N: the force on the belt at the roll, at the end of the tension travel |
| 5 | Tension travel (EF023006) | 30 mm: the roll's axis, from the free stop to the end stop (the arm's 30° swing at 58 radius: 2 × 58 × sin 15° = 30.0) |
| 6 | Profile shape (EF005179) | flat: a plain cylindrical roll running on the belt's back; no groove or teeth (a design choice, no belt profile) |

## Ratings (ratings.csv)
`max_tensile_force` 250 N, status "generic design", source "ETIM 10.0 EC010722 class value"
(OPERATING.md 12). No check reads a mechanical force today; they sit there for the assembly checks that will.

## What it meets
| figure | value | source |
|---|---|---|
| base screws | 2 × M8, Ø9.0 holes 70 apart (x ±35, y 0) | ISO 273 medium (H13), lib/standards/holes.csv. The screws are not built; the host places them. GDT-010: one hole pair over 70 mm, ISO 2768-m ±0.3 gives a Ø0.85 zone ≤ H − F = 1.0 |
| the belt | none in this element | the roll's flat running face is a design choice, not a belt profile: it runs on any belt's back. The belt and its pulleys are the drive's, placed by the host |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base flange | 90 × 50 × 6, cast with the housing, anodised aluminium | the hole centres stand 10 beyond the housing (x ±35 against ±25), room for the screw heads |
| spring housing | Ø50, z 6 to 36 | holds the torsion spring; the spring is not drawn (the twin reads the arm's angle, not the spring) |
| journal and cap | Ø16 from the housing's top up to z 48.5; retaining cap Ø24 × 2 on it | the arm's hub turns on it in a Ø16.4 bore (features.csv), 0.5 clear under and over the hub |
| arm | hub Ø32, z 36.5 to 48; bar 20 wide, z 38 to 47.5, out to a round end Ø20 at x 58 | 58 from the pivot to the roll's axis |
| roll and axle | roll Ø40 × 25, z 49 to 74, black polyamide, on a Ø12.4 bore (features.csv, 2.0); axle Ø12 from the arm up to z 76 | the roll runs 1.5 above the arm and clear of the cap at every angle (its inner edge 38 from the pivot axis); 0.2 radial on the axle |
| swing | 30° | gives the 30 of tension travel |
| roll bearing, spring preload at the free stop | not modelled, not stated | the twin reads the arm's angle; the force at the end stop is the class value |

## Mechanism
`arm` (rotate about the pivot axis, origin (0, 0, 36.5), axis +z, 0 to 30°): 0 is the free stop, as built (the arm toward +x);
the belt pushes the roll back and the arm round toward +y, against the spring, to the end stop at 30, where the force on the belt
is the max. tensile force. The node carries the hub, the bar, the round end and the axle, and the roll rides it. MOT-010 sweeps
it through the full range with the roll carried: the hub turns on the journal (0.2 radial clearance) between the housing's top
and the cap (0.5 each way), and the roll and arm pass over the housing and flange.
`roll` (rotate about its axle, origin (58, 0, 49), axis +z, 0 to 360°: a spin, it turns freely as the belt runs): its own node
from 2.0, declared on the arm (`P.parents["roll"] = "arm"`, request mech-6 item 2, lib/requests/core/mech-6-answer.md). In the
glTF the roll is a child of `arm`, so the twin carries it with the arm's swing and still spins it on its own pivot; MOT-010 carries
it rigidly in the arm's sweep and sweeps its own spin at the arm's rest pose. The roll is round and turns about its own axis, so
its spin meets nothing it didn't meet at rest; every other arm angle is covered by the arm's sweep carrying it. It turns on the
axle in a Ø12.4 bore (0.2 radial); its bearing is not modelled.

## Named nodes
`arm` (rotate) · `roll` (rotate, a child of `arm`). Colliders `body` (the flange), `housing` (the housing, journal and cap), `arm`
(hub and bar), `idler` (roll and axle; named apart from the node `roll`).

## Materials by layer
`M-ALU-ANOD` base flange and spring housing · `M-ZINC` journal, cap, arm and axle (zinc-plated steel) · `M-BLACK-PA` roll.

## Decals (Blender)
"complexes.org generic" on the housing's side, toward −y.

## Notes
No vendor names, part numbers or marks. No safety claim. The class values are the figures this design is meant to meet; no
calculation or test of the model is on file. No open figure: the holes are on file, the screws are standard parts the host
places, and the roll's contact with the belt is a design choice.

## Outputs (out/)
`tensioner-belt.lsp` · `.glb` (pivots on `arm` and `roll`, `roll` a child of `arm`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010722), our own design (cloud-mech r3, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
| 2.0 | major (a new node): the idler roll is its own node `roll` (rotate 0 to 360° about its axle), declared on `arm` with P.parents so it rides the arm's swing and spins on its own (request mech-6 item 2; review tensioner-belt-1.0 note 1); a Ø12.4 bore on the axle (features.csv); collider `roll` renamed `idler`. Sizes, holes, class values and extents unchanged (mech-r62, 2026-11-09) |
