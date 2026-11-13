# strip-rubber-rect-30x10 · v1.0 · Rubber rectangular section, generic, solid EPDM 30 x 10, not chamfered, no hollow core, not self-adhesive, black, plain, cut to length

**What** A rubber rectangular section: the solid black block gasket, pad or wear strip a machine bonds or clamps on a frame, a cover's
flange or a guide. 30 wide × 10 high, square-edged, solid through (no hollow core), not self-adhesive: the host bonds or clamps it. One
straight length, cut to length by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber rectangular section (ETIM 10.0 EC010642), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: it is a class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name), built in the same round as EC010644 (strip-rubber-bumper-40x22, mech-r138); the classes
between them by name (EC010643 cord, EC010648 corner guard, EC010641 multi-faced/trapezium section) are the next rounds'. Its class is
on file (11 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the strip's centre line y = 0, the bearing face z = 0 (the face that lies on the
host). The run goes along +x; the upper face is at z 10. Extents x 0 to `length`, y ±15, z 0 to 10.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERRECT` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010642 Rubber rectangular section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM (lib/materials.csv `epdm`) |
| 2 | Material structure (EF022835) | solid (not cellular) |
| 3 | Width (EF000008) | 30 mm (y) |
| 4 | Height (EF000040) | 10 mm (z) |
| 5 | Self-adhesive (EF000434) | no |
| 6 | Chamfered (EF001586) | no (square edges) |
| 7 | Hollow core (EF022577) | no |
| 8 | IRHD hardness (EF022836) | not stated |
| 9 | Shore hardness (EF022944) | not stated |
| 10 | Colour (EF000007) | black (the `M-GASKET` layer) |
| 11 | Operating temperature (EF001742) | not stated (lib/materials.csv epdm carries no temperature figure) |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, sealing, compression, temperature or fire figure
is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it lies on | the bearing face 30 wide, bonded or clamped by the host; nothing drilled | ETIM 10.0 EC010642 Self-adhesive "no" above; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what closes or bears on it | the upper face 30 wide, 10 above the bearing face; how far a cover or a part squeezes it is the host's choice | this design's choice of section, ETIM 10.0 EC010642 Width / Height above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 30 × 10, rectangular, solid; area 300 mm² (asserted in element.py); 300 000 mm³ at the default length | a block gasket or pad; both end-face edges are 8 or more, so no 3 to 7 mm free-corner edge is left (mech-r69 / r101) |
| corners | sharp (Chamfered "no") | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other profiles (mech-r106 / r131) |
| hardness, compression set, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; its compression is the host's, not a motion. behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `strip` (x 0 to `length`, y ±15, z 0 to 10).

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
"complexes.org generic" on the bearing face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box. The AutoCAD gate (mech-r138): 1 solid, 12 edges picked and 12 filleted
at r 0.5, 0 rejected; removed 223.0 of 223.2 mm³; STEP vs glb extents 0.0. The Blender gate's body volume 300 000.0 mm³ (300 × 1000).
Every bounding-box extreme lies on its faces (y ±15, z 0 and 10, x 0 and
`length`).
Not drawn: an adhesive or liner, a joint or splice, the host.

## Outputs (out/)
`strip-rubber-rect-30x10.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010642), our own design (mech-r138, unattended, 2026-11-12): solid EPDM rectangular section 30 x 10, not chamfered, no hollow core, not self-adhesive, black, plain, cut to length |
