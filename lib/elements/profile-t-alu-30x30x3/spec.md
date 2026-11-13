# profile-t-alu-30x30x3 · v1.0 · T-profile, aluminium, generic, extruded equal T 30 x 30, base and post 3, sharp corners, anodised, plain (no holes), cut to length

**What** An aluminium T-profile: an extruded equal T-section, base (flange) 30 wide and 3 thick, post (web) 3 thick, total height 30,
sharp corners, anodised. A light stiffener, divider, edge trim or guide a machine's guards, covers and fixtures are made with. One
straight length, cut to length by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes.
**Class** rail · **Baseline** our own design: generic T-profile, aluminium (ETIM 10.0 EC011891), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010641 (strip-rubber-trapezium-30x15, mech-r140); the
classes between them by name are set aside (lib/needs-em/mech.md). Its class is on file (8 features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. No dimensional standard on file fixes an
extruded aluminium T-section's sizes (a hot-rolled steel T's are EN 10055's, another class and not on file), so every size is a design
choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the post's centre plane y = 0, the base's underside z = 0. The run goes along +x;
the base lies flat (z 0 to 3), the post stands upright (z 3 to 30). Extents x 0 to `length`, y ±15, z 0 to 30.
**Built with** toolkit 1.3 · AutoLISP command `TPROFALU` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC011891 T-profile, aluminium (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | aluminium |
| 2 | Material quality (EF001257) | aluminium alloy 6063 (lib/materials.csv `al-6063`, the extrusion alloy on file); temper not stated |
| 3 | Surface protection (EF000139) | anodised (the `M-ALU-ANOD` layer); layer thickness not stated |
| 4 | Model (EF000010) | equal T (base width = total height), sharp corners (no root or toe radius drawn) |
| 5 | Base width (EF022837) | 30 mm (along y) |
| 6 | Base thickness (EF022838) | 3 mm |
| 7 | Total height (EF001761) | 30 mm (along z) |
| 8 | Post thickness (EF022839) | 3 mm |

No ratings.csv: no feature of the class is a rating the checks read, and no load is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs through the base or the post and declares them in its own features.csv (fastener, clearance, position) | ETIM 10.0 EC011891 has no hole feature; plain stock, as sold cut to length (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what sits on or beside it | the base's underside 30 wide; each side of the post 27 high and 13.5 clear over the base to its edge | ETIM 10.0 EC011891 Base width / Base thickness / Total height / Post thickness above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | equal T 30 × 30, base and post 3, area 171 mm² (30 × 3 + 27 × 3, asserted in element.py, and = 30 × 30 − 2 × 13.5 × 27); 171 000 mm³ at the default length | a light extruded T; the 3.0 base ends and post top are "short" in the gate's fillet pass, and every other end-face edge is 13.5 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp, inside and outside | an extrusion's small root radii are not drawn (appearance only, no figure claimed) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 3 mm wall (mech-r69 / r106) |
| alloy, temper, film thickness, tolerances, load | alloy 6063 named; the rest not claimed | no material data sheet is on file (lib/materials.csv al-6063 carries no figures); an extrusion's tolerances are EN 755-9's, not on file and not claimed |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `base` (x 0 to `length`, y ±15, z 0 to 3) and `post` (y ±1.5, z 3 to 30); the spaces beside the
post stay free.

## Materials by layer
`M-ALU-ANOD` the whole profile (anodised aluminium).

## Decals (Blender)
"complexes.org generic" on the base's underside, centred.

## Notes
No vendor names, part numbers or marks. No load rating: the class has no load feature and no allowable stress is on file. Drawn as
one box less two cuts (the spaces beside the post, `cutbox`), so the post's sides and the base's upper face are cut faces. The
AutoCAD gate (mech-r140): 1 solid, 6 edges picked and 6 filleted at r 0.5, 0 rejected, 2 cut edges skipped; removed 110.8 of 110.8
mm³; STEP vs glb extents 0.0. The Blender gate's body volume 171 000.0 mm³ (171 × 1000). Every
bounding-box extreme lies on the uncut outer faces (y ±15 on the base's ends, z 0 on the base, z 30 on the post's top, x 0 and
`length`).
Not drawn: holes, fasteners, end caps, the host. A stainless steel T (EC011892) or a hot-rolled steel T (EN 10055) is another element,
once its standard is on file.

## Outputs (out/)
`profile-t-alu-30x30x3.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011891), our own design (mech-r140, unattended, 2026-11-12): extruded equal T 30 x 30, base and post 3, sharp corners, anodised, plain, cut to length |
