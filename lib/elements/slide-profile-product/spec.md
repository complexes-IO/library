# slide-profile-product · v1.1 · product line slide profile, plastic, generic, guide strip 12 × 40 on a 50 × 60 × 3 mounting angle, M6 foot holes, cut to length

**What** A product line slide profile: the plastic strip the goods of a product line (cartons, containers, parts on a light conveyor)
slide along as they pass, so they are guided without wearing on the steel. A low-friction plastic guide strip 12 thick and 40 high is
bonded on the outer face of a steel mounting angle's upright leg; the angle's foot screws to the conveyor's frame beside the belt, so
the strip's face stands along the line as its side guide, the goods sliding against it. Cut to length. It is the first element of
ETIM's "Product line slide profile, plastic" class in the library (`python lib/build.py inventory mech` lists the machine-element
classes in order: EC011968 Gear wheel waits on the gear standards and EC010448 Plastic ball on a sphere solid the AutoCAD gate can
read, lib/needs-em/mech.md); slide-profile-flat-belt (EC010730) is its sibling, with the same plastic, galvanized mounting and holes.
No inventory row or system names it yet.
**Class** rail · **Baseline** our own design: generic product line slide profile, plastic (ETIM 10.0 EC010731), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). The class and its six features are on file (lib/standards/etim/classes.csv, class-features.csv).
No product was matched and no vendor file was opened. The class values below are the design inputs; every other size is a design
choice.
**Units / frame** mm, Z up. Origin: the run's start (x = 0) at the angle's outer corner line (y = 0, the upright leg's outer face the
strip is bonded to), at the foot's underside (z = 0, the face on the frame). The run goes along +x; the foot reaches toward +y, the
strip's guide face looks toward −y at y −12. Extents at the default length: x 0 to 1000, y −12 to 50, z 0 to 60.
**Built with** toolkit 1.3 · AutoLISP command `SLIDEPROFPL` · parameter `length` (default 1000, 200 or more).

## Class values
ETIM 10.0 class EC010731 Product line slide profile, plastic (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every
feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PE-UHMW (ultra-high-molecular-weight polyethylene), the guide strip |
| 2 | Mounting profile (EF023075) | angle 50 × 60 × 3: the strip bonded on the upright leg, the foot screwed to the frame |
| 3 | Material mounting profile (EF023076) | galvanized steel |
| 4 | Height (EF000040) | 60 mm overall (the angle's upright leg); the guide strip 40 |
| 5 | Width (EF000008) | 62 mm overall (the strip's face to the foot's edge); the guide strip 12 |
| 6 | Colour (EF000007) | white (the guide strip) |

The class has no load, speed, friction or temperature feature, so none is designed to or claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the goods | the strip's guide face, y −12, from z 15 to z 55 over the frame's top face, the run's whole length | design: the face's height and place are this design's choices (OPERATING.md 12, generic elements; the class values Height and Width); the goods, their size and the conveyor that moves them are the host's |
| the conveyor's frame | the foot's underside on the frame's top face; 3 × M6 screws through Ø6.6 holes at y 30, x 50, 500 and 950 (at the default length: 50 in from each end, at most 450 apart between) | ISO 273 medium clearance H13 (lib/standards/holes.csv); design: an M6 head up to Ø10.5 clears the upright leg's inner face by 21.75 and the foot's edge by 14.75 (a design allowance; screw-head standards not on file); the screws and the frame's tapped holes are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| guide strip | 12 thick × 40 high, the run's whole length, its underside 15 over the frame | a face high enough to guide low goods above a belt's edge, and thick enough to wear; its end edges 12 and 40, clear of the gate's 3 to 7 mm fillet trap (mech-r101) |
| mounting angle | foot 50 × 3, upright leg 60 × 3, the run's whole length, drawn as one box less its inside (one solid) | the leg carries the strip, the foot the screws; 3.0 thick so its end edges are the gate's "short" edges, skipped |
| foot holes | Ø6.6 on the line y 30 | each 16.7 from the foot's edge (50 − 30 − 3.3), over 1.5 × the sheet's thickness = 4.5 (DFM-010), and 23.7 from the leg's inner face |
| strip to angle | the strip seated on the upright leg's outer face, bonded | an adhesive joint, this design's choice (OPERATING.md 12); not drawn |
| entries | plain square ends | real guides bevel the strip's entry; not drawn |
| load, speed, friction, temperature range | not claimed | no feature of this class states one; no figure is on file |

## Mechanism
None: one fixed body, no moving node, no port. The goods and the conveyor are the host's; behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `guide` (the strip and the upright leg: x 0 to the length, y −12 to 3, z 0 to 60) and `foot`
(x 0 to the length, y 3 to 50, z 0 to 3).

## Materials by layer
`M-WHITE-PA` the guide strip, appearance only (white): the material is PE-UHMW (Class values, feature 1); lib/godot/qa/materials holds
no PE layer. `M-GALV` the mounting angle.

## Notes
No vendor names, part numbers or marks. No load, speed, friction or safety claim. The drawn volume at the default length is about
800 692.1 mm³ (the angle's section 50 × 3 + 3 × 57 = 321 mm² × 1000 = 321 000, less 3 holes π 3.3² × 3 = 307.9; the strip 12 × 40 ×
1000 = 480 000); a mesh's polygonal circles read a little off their true areas. Written as volume only: lib/materials.csv gives no
densities, so no mass is stated. A product line slide profile is not a part a dimensional standard shapes, so it is built generic to its
ETIM class (OPERATING.md 12). The gate's fillet radius is set to 0.5 on every primitive (the rail class's 1.0 reads 10 mm edges short,
mech-r69 / mech-r106): the strip's end edges are 12 and 40; the angle's 3.0 edges are short and skipped; the angle's inside and the
holes' edges are cut edges, skipped. Every bounding-box extreme lies on an uncut face: the strip's face (y −12), the foot's edge (y
50) and underside (z 0), the upright leg's top (z 60), and the end faces (x 0 and the length).

## Outputs (out/)
`slide-profile-product.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010731), our own design (mech-r122, unattended, 2026-11-12): a PE-UHMW guide strip 12 × 40 on a galvanized steel mounting angle 50 × 60 × 3 with M6 foot holes, cut to length |
| 1.1 | text only (review mech-r122 findings 2 and 3): element.py's docstring and BASELINE (and so the catalogue's row) now say the strip sits on the upright leg's outer face, as the geometry, ORIGIN and this spec always had it; the M6 head clearance is a design allowance ("an M6 head up to Ø10.5"), no longer cited from ISO 4762 / ISO 7380 (not on file). The part unchanged; a minor (mech-r143, unattended, 2026-11-13) |
