# tensioner-chain · v1.0 · chain tensioner, generic, spring-activated linear, slide shoe 60 × 24, travel 25, 200 N, simplex 08B, base 2 × M8

**What** A spring-activated chain tensioner: screwed to a machine frame under (or beside) a roller chain drive, it presses a slide
shoe against the chain's slack side so the chain stays tight as it wears and lengthens. A base flange with two M8 holes and a
spring housing on it; a plunger slides in the housing's bore and carries a flat slide shoe, and a compression spring inside the
housing presses it up against the chain. The head (plunger and shoe) is the mechanism: the twin presses it in by name as the
chain pushes the shoe back.
**Class** device · **Baseline** our own design: generic spring-activated chain tensioner (ETIM 10.0 EC010720), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design
inputs; the holes it meets are on file (ISO 273); the one fit no file gives is open (What it meets); every other size is a design
choice.
**Units / frame** mm, Z up. Origin: the mounting face (the base flange's underside) at z = 0, the plunger's axis (the centre of the
two-hole pattern) at x = 0, y = 0. The head stands toward +z, the shoe's running face at z = 94 at the free stop; the chain runs
along x across it.
**Built with** toolkit 1.3 · AutoLISP command `CHAINTENS` · no parameters.

## Class values
ETIM 10.0 class EC010720 Spring-activated chain tensioner (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every
feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the
element.

| # | feature | value |
|---|---|---|
| 1 | Duplex (EF023003) | no: simplex, one strand |
| 2 | Pitch measure (EF023963) | 08B (1/2 in): the chain the tensioner is designed for is a simplex 08B-1 roller chain (ISO 606 designation) |
| 3 | Roller size (EF023004) | not stated: the chain guide is a slide shoe, with no roller of its own |
| 4 | Chain guide (EF023005) | slide shoe: a flat running face of PE-UHMW, 60 along the chain and 24 across (a design choice, no sprocket or chain profile) |
| 5 | Height (EF000040) | 94 mm: the mounting face to the shoe's running face, at the free stop (69 at the end stop) |
| 6 | Width (EF000008) | 32 mm: the base flange and the spring housing across the chain's line (y); the shoe 24 |
| 7 | Tension travel (EF023006) | 25 mm: the head pressed in from the free stop to the end stop |
| 8 | Max. tensile force (EF000353) | 200 N: the force on the chain at the shoe, at the end of the tension travel |

## Ratings (ratings.csv)
`max_tensile_force` 200 N, status "generic design", source "ETIM 10.0 EC010720 class value" (OPERATING.md 12). No check reads a
mechanical force today; it sits there for the assembly checks that will.

## What it meets
| figure | value | source |
|---|---|---|
| base screws | 2 × M8, Ø9.0 holes 56 apart (x ±28, y 0) | ISO 273 medium (H13), lib/standards/holes.csv. The screws are not built; the host places them. GDT-010: one hole pair over 56 mm, ISO 2768-m ±0.3 gives a Ø0.85 zone ≤ H − F = 1.0 |
| the chain | simplex 08B-1 (a class value), its side plates running on the shoe's flat face | 08B-1 is a class value (a design input). The chain's own figures, the width over its plates and their height (ISO 606), are **NOT ON FILE (B)** (a fit: the shoe's 24-wide running face must carry the chain's plates). No chain table is in lib/standards/, so the shoe's width is a design size. Closed when an ISO 606 table is on file: cite it, a minor version if the shoe changes. The chain and its sprockets are the drive's, never generic (OPERATING.md 12) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base flange | 76 × 32 × 6, zinc-plated steel | the hole centres stand 12 beyond the housing (x ±28 against ±16), room for the screw heads |
| spring housing | Ø32, z 6 to 56, with the plunger's bore Ø20.4 from its top down to z 16 (features.csv) | holds the compression spring under the plunger; the spring is not drawn (the twin reads the head's travel, not the spring) |
| plunger | Ø20, z 46 to 82 at the free stop (10 in the bore, 26 out) | 0.2 radial clearance in its bore; at the end stop its lower end stands 5 above the bore's bottom |
| slide shoe | 60 × 24 × 12, PE-UHMW, white, on the plunger's top | the chain's line along x; at the end stop the shoe stands 1 above the housing's top |
| the plunger's key against turning, its stop at the free position, the shoe's lead-in at each end | not modelled | the twin reads the head's travel only |

## Mechanism
`head` (translate, origin the shoe's running face (0, 0, 94), axis −z, 0 to 25 mm): 0 is the free stop, as built; the chain
presses the shoe down, against the spring, to the end stop at 25, where the force on the chain is the max. tensile force. The node
carries the plunger and the shoe. MOT-010 sweeps it through the full range: the plunger slides in its bore (0.2 radial clearance,
its lower end from z 46 down to z 21, the bore's bottom at z 16), and the shoe comes down to 1 above the housing's top.

## Named nodes
`head` (translate). Colliders `body` (the flange), `housing`, `head` (the shoe and the plunger above the housing).

## Materials by layer
`M-ZINC` base flange, housing and plunger (zinc-plated steel) · `M-WHITE-PA` slide shoe (PE-UHMW).

## Decals (Blender)
"complexes.org generic" on the housing's side, toward −y.

## Notes
No vendor names, part numbers or marks. No safety claim. The class values are the figures this design is meant to meet; no
calculation or test of the model is on file. One open figure, class B and EM's: the chain's figures the shoe must carry (What it
meets). The rest are design choices.

## Outputs (out/)
`tensioner-chain.lsp` · `.glb` (pivot on `head`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010720), our own design (cloud-mech r3, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
