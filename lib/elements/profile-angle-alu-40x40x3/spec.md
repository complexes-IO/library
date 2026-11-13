# profile-angle-alu-40x40x3 · v1.0 · angle profile, aluminium, generic, equal legs 40 x 40, wall 3, sharp corners, anodised, plain (no holes), cut to length

**What** An equal-leg aluminium angle: the plain extruded stock a machine's guards, covers, edge trims, light brackets and small
frames are cut from. Legs 40 × 40, wall 3, sharp inner and outer corners, anodised. One straight length, cut to length by the
`length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes: a host that bolts it drills its own and
declares them in its own features.csv.
**Class** rail · **Baseline** our own design: generic angle profile, aluminium (ETIM 10.0 EC012022), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: it is the first class of EG019710 Profiles in `python lib/build.py inventory
mech`'s ETIM list (lib/toolkit/generic.py ORDER), after the machine-element and clamping-tool classes were built or set aside
(lib/needs-em/mech.md). Its class is on file (8 features, lib/standards/etim/class-features.csv). No product was matched and no
vendor file was opened. An extruded aluminium angle's sizes are not fixed by a dimensional standard on file (its tolerances would
be EN 755-9's, not on file and not claimed): every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the angle's outer corner line (the heel) y = 0, z = 0. The run goes along +x;
one leg (the foot) along +y, its underside at z 0; the other (the upright) along +z, its outer face at y 0. Extents x 0 to
`length`, y 0 to 40, z 0 to 40.
**Built with** toolkit 1.3 · AutoLISP command `ANGLEALU` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC012022 Angle profile, aluminium (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define
the element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | aluminium |
| 2 | Material quality (EF001257) | aluminium alloy 6063 (lib/materials.csv `al-6063`, the extrusion alloy on file); temper not stated |
| 3 | Surface protection (EF000139) | anodised (the `M-ALU-ANOD` layer); layer thickness not stated |
| 4 | Model (EF000010) | equal-leg angle, sharp corners (no root or toe radius drawn) |
| 5 | Width (EF000008) | 40 mm (the foot, along y, outside) |
| 6 | Height (EF000040) | 40 mm (the upright, along z, outside) |
| 7 | Thickness (EF000125) | 3 mm (both legs) |
| 8 | Angle (EF008153) | 90° |

No ratings.csv: no feature of the class is a rating the checks read, and no load is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs and declares them in its own features.csv (fastener, clearance, position) | ETIM 10.0 EC012022 has no hole feature; plain stock, as sold cut to length (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what sits in or on the angle | the inner faces of the legs, 37 × 37 free inside the corner | this design's choice of section, ETIM 10.0 EC012022 Width / Height / Thickness above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 40 × 40 outside, wall 3, equal legs, area 231 mm² (40 × 3 + 37 × 3, asserted in element.py) | a common light-guard and trim size; a 3.0 wall is "short" in the gate's fillet pass (every 3.0 edge is at MIN_EDGE or under), so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp, inside and outside | an extruded angle carries small root and toe radii; none is drawn (appearance only, no figure claimed) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 3 mm wall (mech-r69 / r106) |
| alloy, temper, film thickness, load | alloy 6063 named; the rest not claimed | no material data sheet is on file (lib/materials.csv al-6063 carries no figures) |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `foot` (x 0 to `length`, y 0 to 40, z 0 to 3) and `upright` (y 0 to 3, z 3 to 40).

## Materials by layer
`M-ALU-ANOD` the whole angle (anodised aluminium).

## Decals (Blender)
"complexes.org generic" on the foot's underside, centred.

## Notes
No vendor names, part numbers or marks. No load rating: the class has no load feature and no allowable stress is on file. Drawn as
one box less its inside (one `cutbox`), so the inner faces are cut faces. The AutoCAD gate (mech-r131): 1 solid, 7 edges picked and
7 filleted at r 0.5, 0 rejected, 1 cut edge skipped; removed 169.4 of 169.5 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on the uncut
outer faces (y 0 and 40, z 0 and 40, x 0 and `length`). Volume at the default length: 231 000 mm³ (231 × 1000).
Not drawn: holes, fasteners, the host. A stainless steel angle (EC012021) or a steel one is another element; a rolled steel angle's
section is EN 10056-1's (not on file).

## Outputs (out/)
`profile-angle-alu-40x40x3.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012022), our own design (mech-r131, unattended, 2026-11-12): equal-leg angle 40 x 40 x 3, sharp corners, anodised, plain, cut to length |
