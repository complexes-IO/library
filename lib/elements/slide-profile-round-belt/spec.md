# slide-profile-round-belt · v1.1 · circular belt slide profile, generic, 30 × 15 with a 90-degree V-groove for a round belt 8, on a 62 × 3 mounting flat, cut to length

**What** A circular belt slide profile: the strip a round belt's carrying run slides along on a light conveyor (round-belt
transfers, small-parts and carton conveyors), instead of running on rollers. The slide profile, a low-friction plastic, carries a
90-degree V-groove along its top; the belt rests on both flanks with its centre in the profile's top face and stands 4 above it, so the goods ride on the belt and never touch
the profile. The profile sits on a steel mounting flat that screws to the conveyor's frame. Cut to length. It is the first element of
ETIM's "Circular belt slide profile" class in the library (`python lib/build.py inventory mech` lists the class as the next mech
class to build generic once no inventory row builds unattended; EC012003 Ball joint and EC011971 Cardan joint above it wait for
their dimensional standards: lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** rail · **Baseline** our own design: generic circular belt slide profile (ETIM 10.0 EC010729), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). The class and its seven features are on file (lib/standards/etim/classes.csv, class-features.csv). No
product was matched and no vendor file was opened. The class values below are the design inputs; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the run's start (x = 0) on the profile's centre line (y = 0), at the mounting flat's underside
(z = 0, the face on the frame). The run goes along +x; the groove is up, its apex at z 12.34, the belt's axis in the profile's top face at z 18. Extents at the
default length: x 0 to 1000, y −31 to 31 (the flat), z 0 to 18 (the profile's top face).
**Built with** toolkit 1.3 · AutoLISP command `SLIDEPROFRB` · parameter `length` (default 1000, 200 or more).

## Class values
ETIM 10.0 class EC010729 Circular belt slide profile (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature
in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PE-UHMW (ultra-high-molecular-weight polyethylene), the slide profile |
| 2 | Belt number according to DIN 2215 (EF023078) | not stated: DIN 2215 numbers V-belt sections, and this profile carries a round belt Ø8 (the V-groove below); DIN 2215 is not in lib/standards/sources.csv |
| 3 | With mounting profile (EF023186) | yes: a galvanized steel mounting flat 62 × 3 under the slide profile |
| 4 | Material mounting profile (EF023076) | galvanized steel |
| 5 | Height (EF000040) | 18 mm overall (the slide profile 15 on the flat's 3) |
| 6 | Width (EF000008) | 62 mm overall (the flat); the slide profile 30 |
| 7 | Colour (EF000007) | white (the slide profile) |

The class has no load, belt speed, friction or temperature feature, so none is designed to or claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the round belt | a round belt Ø8, resting on both flanks of the 90-degree V-groove (touching them 2.83 under the top face), its centre in the top face, its top 4 above it | design: the belt's size is this design's choice (OPERATING.md 12); no standard in lib/standards/sources.csv tabulates round belt sizes; the belt, its pulleys and its tension are the host's |
| the conveyor's frame | the flat's underside on the frame's top face; 6 × M6 screws through Ø6.6 holes at y ±22.5, x 50, 500 and 950 (at the default length: 50 in from each end, at most 450 apart between) | ISO 273 medium clearance H13 (lib/standards/holes.csv); design: an M6 head up to Ø10.5 clears the profile's side by 2.25 and the flat's edge by 3.25 (screw-head standards not on file: a design allowance); the screws and the frame's tapped holes are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| slide profile | 30 wide × 15 high, the run's whole length | 9.3 of profile each side of the groove at the top, 9.3 under its apex |
| groove | 90-degree V, 11.31 wide at the top face, 5.66 deep (the belt's radius × √2), open at both ends | centres the Ø8 belt on two flanks with its axis in the top face; the belt stands 4 above the profile. A V, not a half-round: a round groove drawn as a hole open at the top breaks out of its part (HOLE-020), and one oriented cut draws the V |
| mounting flat | 62 wide × 3 thick, the run's whole length | carries the profile and the screw holes beside it; each Ø6.6 hole stands 5.2 from the flat's edge (31 − 22.5 − 3.3), over 1.5 × the sheet's thickness = 4.5 (DFM-010) |
| profile to flat | the profile seated on the flat's top face, bonded | an adhesive joint, this design's choice (OPERATING.md 12); not drawn |
| belt entries | plain square ends | real profiles chamfer the groove's entry; not drawn (no cone primitive in the toolkit) |
| load, belt speed, friction, temperature range | not claimed | no feature of this class states one; no figure is on file |

## Mechanism
None: one fixed body, no moving node, no port. The belt is the host's; behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `body` (x 0 to the length, y ±31, z 0 to 18).

## Materials by layer
`M-WHITE-PA` the slide profile, appearance only (white): the material is PE-UHMW (Class values, feature 1); lib/godot/qa/materials
holds no PE layer. `M-GALV` the mounting flat.

## Notes
No vendor names, part numbers or marks. No load, speed, friction or safety claim. The drawn volume at the default length is about
603 384.2 mm³ (the flat 1000 × 62 × 3 = 186 000 less 6 holes π 3.3² × 3 = 615.8; the profile 1000 × 30 × 15 = 450 000 less the
V-groove 11.314 × 5.657 / 2 × 1000 = 32 000); a mesh's polygonal circles read a little off their true areas. Written as volume only:
lib/materials.csv gives no densities, so no mass is stated. A circular belt slide profile is not a part a dimensional standard shapes,
so it is built generic to its ETIM class (OPERATING.md 12). The gate's fillet radius is set to 0.5 on every primitive (the rail class's
1.0 reads 10 mm edges short, mech-r69 / mech-r106): the profile's top end edges are 9.3 between the corner and the groove, its other
edges 15 and longer; the flat's 3.0 edges are short and skipped; the groove's and the holes' edges are cut edges, skipped. Every
bounding-box extreme lies on an uncut face: the flat's sides (y ±31) and underside, the profile's top face (z 18) beside the groove,
and the end faces (x 0 and the length).

## Outputs (out/)
`slide-profile-round-belt.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010729), our own design (mech-r119, unattended, 2026-11-12): a PE-UHMW slide profile 30 × 15 with a 90-degree V-groove for a round belt Ø8, on a galvanized steel mounting flat 62 × 3 with M6 holes, cut to length (mech-r120, same version, nothing released: the flat 60 → 62 so the M6 holes' edge distance 5.2 meets DFM-010's 1.5 t) |
| 1.1 | text only, the part unchanged (mech-r142, unattended, 2026-11-13; review mech-r119 finding 2): the M6 head clearance in What it meets and element.py's HOLE_Y comment written as a design allowance (an M6 head up to Ø10.5 clears the profile's side by 2.25 and the flat's edge by 3.25), no longer cited from ISO 4762 / ISO 7380, which are not on file |
