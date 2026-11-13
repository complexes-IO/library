# strip-rubber-cord-10 · v1.0 · Rubber cord, generic, solid EPDM, diameter 10, no hollow core, black, plain, cut to length

**What** A rubber cord: the black round rubber cord a machine lays in a groove as a seal or a buffer, threads through a channel, or
bonds end to end into a ring. Ø10, solid rubber (not sponge), no hollow core. One straight length, cut to length by the `length`
parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). It is cord stock, not an O-ring: no ring and no ISO 3601
size is claimed.
**Class** rail · **Baseline** our own design: generic rubber cord (ETIM 10.0 EC010643), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM list
(lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010644 (strip-rubber-bumper-40x22, mech-r138). Its class is on
file (8 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A cord's diameter is not
fixed by a dimensional standard: it is a design choice; the DIN 7715 tolerance class (a class feature) is not stated, and no standard
for it is on file.
**Units / frame** mm, Z up. Origin: run start x = 0, the cord's axis along +x at y = 0, z = 0 (its centre line). Extents x 0 to
`length`, y ±5, z ±5.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERCORD` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010643 Rubber cord (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element; they
are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM (lib/materials.csv `epdm`) |
| 2 | Material structure (EF022835) | solid (not cellular) |
| 3 | Diameter (EF000551) | 10 mm |
| 4 | Hollow core (EF022577) | no |
| 5 | Tolerance class according to DIN 7715 (EF022849) | not stated |
| 6 | IRHD hardness (EF022836) | not stated |
| 7 | Colour (EF000007) | black (the `M-GASKET` layer) |
| 8 | Operating temperature (EF001742) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, compression, sealing, temperature or fire figure
is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the groove or channel it lies in | Ø10 nominal; the groove's width, depth and squeeze are the host's design, nothing is drilled in the cord | ETIM 10.0 EC010643 Diameter above; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| a ring made from it | cut and joined by the host's assembly; no ring size is claimed | not an O-ring: ISO 3601 sizes are not this element's (OPERATING.md 12, a part a dimensional standard shapes is never generic) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| diameter | 10 | a common cord size for a groove seal or a buffer; the end faces' round edges (31.4 around) clear the gate's 3 to 7 mm free-corner trap (mech-r69) |
| section area | π 5² = 78.54 mm² (asserted in element.py); about 78 540 mm³ at the default length | by hand, for the Blender volume |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other profiles (mech-r106 / r131) |
| hardness, compression set, sealing force, temperature range, flammability, diameter tolerance | not claimed | lib/materials.csv epdm carries no figures; DIN 7715 is not on file |

## Mechanism
None: one fixed body, no moving node, no port; its squeeze in a groove is not modelled, and laying it in is the host's assembly, not
a motion. behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `cord` (x 0 to `length`, y ±5, z ±5).

## Materials by layer
`M-GASKET` the whole cord (EPDM, black).

## Decals (Blender)
"complexes.org generic" along the cord.

## Notes
No vendor names, part numbers or marks. Drawn as one round solid (`cyl`). Every bounding-box extreme lies on the uncut cylinder.
The AutoCAD gate (mech-r139): 1 solid, 2 edges (the end faces' circles) picked and 2 filleted at r 0.5, 0 rejected; removed 3.3 of
3.4 mm³; STEP vs glb extents 0.0. The Blender gate's body volume 77 254.5 mm³ is the cylinder's 78 540 less its tessellation (about
1 290); Godot QA 236 triangles, 1 collider.
Not drawn: a joint, a ring, the host's groove.

## Outputs (out/)
`strip-rubber-cord-10.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010643), our own design (mech-r139, unattended, 2026-11-12): solid EPDM round cord D10, no hollow core, black, plain, cut to length |
