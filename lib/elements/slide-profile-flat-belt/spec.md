# slide-profile-flat-belt · v1.1 · flat belt slide profile, generic, 66 × 12 with a tread 50 between two guide lips, on a 100 × 3 mounting flat, cut to length

**What** A flat belt slide profile: the strip a flat belt's carrying run slides along on a light conveyor (small-parts, carton and
transfer conveyors), instead of running on rollers. The slide profile, a low-friction plastic, carries a flat tread 50 wide along its
top, sunk 2 between two guide lips 8 wide; a flat belt up to 50 wide slides on the tread and the lips keep it on the run. The profile
sits on a steel mounting flat that screws to the conveyor's frame. Cut to length. It is the first element of ETIM's "Flat belt slide
profile" class in the library (`python lib/build.py inventory mech` lists the class as the next mech class to build generic once no
inventory row builds unattended; EC012003 Ball joint and EC011971 Cardan joint above it wait for their dimensional standards:
lib/needs-em/mech.md); slide-profile-round-belt (EC010729) is its sibling, with the same flat, holes and construction. No inventory
row or system names it yet.
**Class** rail · **Baseline** our own design: generic flat belt slide profile (ETIM 10.0 EC010730), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). The class and its seven features are on file (lib/standards/etim/classes.csv, class-features.csv). No
product was matched and no vendor file was opened. The class values below are the design inputs; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the run's start (x = 0) on the profile's centre line (y = 0), at the mounting flat's underside
(z = 0, the face on the frame). The run goes along +x; the tread is up at z 13, the lips' tops at z 15. Extents at the default length:
x 0 to 1000, y −50 to 50 (the flat), z 0 to 15 (the lips' tops).
**Built with** toolkit 1.3 · AutoLISP command `SLIDEPROFFB` · parameter `length` (default 1000, 200 or more).

## Class values
ETIM 10.0 class EC010730 Flat belt slide profile (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PE-UHMW (ultra-high-molecular-weight polyethylene), the slide profile |
| 2 | Tread width (EF023079) | 50 mm: the flat tread between the guide lips, for a flat belt up to 50 wide |
| 3 | With mounting profile (EF023186) | yes: a galvanized steel mounting flat 100 × 3 under the slide profile |
| 4 | Material mounting profile (EF023076) | galvanized steel |
| 5 | Height (EF000040) | 15 mm overall (the slide profile 12 on the flat's 3) |
| 6 | Width (EF000008) | 100 mm overall (the flat); the slide profile 66 |
| 7 | Colour (EF000007) | white (the slide profile) |

The class has no load, belt speed, friction or temperature feature, so none is designed to or claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the flat belt | a flat belt up to 50 wide on the tread (z 13), its edges between the lips (y ±25); a 50 belt runs with no side play, so a host wanting play picks a narrower one | design: the belt's width is this design's choice (OPERATING.md 12, generic elements; the class value Tread width); the belt's thickness, its pulleys and its tension are the host's |
| the conveyor's frame | the flat's underside on the frame's top face; 6 × M6 screws through Ø6.6 holes at y ±41, x 50, 500 and 950 (at the default length: 50 in from each end, at most 450 apart between) | ISO 273 medium clearance H13 (lib/standards/holes.csv); design: an M6 head up to Ø10.5 clears the profile's side by 2.75 and the flat's edge by 3.75 (a design allowance; screw-head standards not on file); the screws and the frame's tapped holes are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| slide profile | 66 wide × 12 high, the run's whole length | the tread 50 and a lip 8 each side; 10 of profile under the tread |
| tread and lips | the tread 50 wide, sunk 2 under the lips' tops, open at both ends (one axis-aligned cut) | the lips guide the belt's edges; 8 wide so their end edges stay clear of the gate's 3 to 7 mm fillet trap (mech-r101) |
| mounting flat | 100 wide × 3 thick, the run's whole length | carries the profile and the screw holes beside it; each Ø6.6 hole stands 5.7 from the flat's edge (50 − 41 − 3.3), over 1.5 × the sheet's thickness = 4.5 (DFM-010) |
| profile to flat | the profile seated on the flat's top face, bonded | an adhesive joint, this design's choice (OPERATING.md 12); not drawn |
| belt entries | plain square ends | real profiles round or chamfer the tread's entry; not drawn |
| load, belt speed, friction, temperature range | not claimed | no feature of this class states one; no figure is on file |

## Mechanism
None: one fixed body, no moving node, no port. The belt is the host's; behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `body` (x 0 to the length, y ±50, z 0 to 15).

## Materials by layer
`M-WHITE-PA` the slide profile, appearance only (white): the material is PE-UHMW (Class values, feature 1); lib/godot/qa/materials
holds no PE layer. `M-GALV` the mounting flat.

## Notes
No vendor names, part numbers or marks. No load, speed, friction or safety claim. The drawn volume at the default length is about
991 384.2 mm³ (the flat 1000 × 100 × 3 = 300 000 less 6 holes π 3.3² × 3 = 615.8; the profile 1000 × 66 × 12 = 792 000 less the tread
50 × 2 × 1000 = 100 000); a mesh's polygonal circles read a little off their true areas. Written as volume only: lib/materials.csv
gives no densities, so no mass is stated. A flat belt slide profile is not a part a dimensional standard shapes, so it is built
generic to its ETIM class (OPERATING.md 12). The gate's fillet radius is set to 0.5 on every primitive (the rail class's 1.0 reads 10
mm edges short, mech-r69 / mech-r106): the lips' top end edges are 8, the profile's other edges 12 and longer; the flat's 3.0 edges
are short and skipped; the tread's and the holes' edges are cut edges, skipped. Every bounding-box extreme lies on an uncut face: the
flat's sides (y ±50) and underside, the lips' tops (z 15), and the end faces (x 0 and the length).

## Outputs (out/)
`slide-profile-flat-belt.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010730), our own design (mech-r121, unattended, 2026-11-12): a PE-UHMW slide profile 66 × 12 with a tread 50 between two guide lips 8 × 2, on a galvanized steel mounting flat 100 × 3 with M6 holes, cut to length |
| 1.1 | text only (review mech-r121 finding 2 and note 1): the M6 head clearance is a design allowance ("an M6 head up to Ø10.5"), no longer cited from ISO 4762 / ISO 7380 (not on file); the belt row says a 50 belt has no side play. The part unchanged; a minor (mech-r143, unattended, 2026-11-13) |
