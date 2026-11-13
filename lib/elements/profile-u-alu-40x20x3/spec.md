# profile-u-alu-40x20x3 · v1.0 · U-profile, aluminium, generic, extruded U-channel 40 x 20, bottom and legs 3, sharp corners, anodised, plain (no holes), cut to length

**What** An aluminium U-profile: an extruded U-channel 40 wide and 20 high, bottom and legs 3, sharp corners, anodised. A light
channel, edge guard, cover carrier or guide a machine's guards, covers and fixtures are made with. One straight length, cut to length
by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes.
**Class** rail · **Baseline** our own design: generic U-profile, aluminium (ETIM 10.0 EC011894), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC011891 (profile-t-alu-30x30x3, mech-r140); the classes
between them by name are set aside (lib/needs-em/mech.md, 216). Its class is on file (8 features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. No dimensional standard on file fixes an
extruded aluminium U-section's sizes (a hot-rolled steel channel's are DIN 1026 / EN 10279's, another class and not on file), so every
size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the channel's centre plane y = 0, the bottom's underside z = 0. The run goes along
+x; the bottom lies flat (z 0 to 3), the legs stand upright (z 3 to 20), the opening is up. Extents x 0 to `length`, y ±20, z 0 to 20.
**Built with** toolkit 1.3 · AutoLISP command `UPROFALU` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC011894 U-profile, aluminium (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | aluminium |
| 2 | Material quality (EF001257) | aluminium alloy 6063 (lib/materials.csv `al-6063`, the extrusion alloy on file); temper not stated |
| 3 | Surface protection (EF000139) | anodised (the `M-ALU-ANOD` layer); layer thickness not stated |
| 4 | Model (EF000010) | U-channel, parallel legs of equal height, sharp corners (no root or toe radius drawn) |
| 5 | Width (EF000008) | 40 mm (along y, outside) |
| 6 | Height (EF000040) | 20 mm (along z, outside) |
| 7 | Bottom thickness (EF022841) | 3 mm |
| 8 | Leg thickness (EF023638) | 3 mm |

No ratings.csv: no feature of the class is a rating the checks read, and no load is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs through the bottom or the legs and declares them in its own features.csv (fastener, clearance, position) | ETIM 10.0 EC011894 has no hole feature; plain stock, as sold cut to length (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what sits in the channel | the clear channel 34 wide between the legs and 17 deep above the bottom, open on top | ETIM 10.0 EC011894 Width / Height / Bottom thickness / Leg thickness above; what sits in it is the host's element |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | U 40 × 20, bottom and legs 3, area 222 mm² (40 × 3 + 2 × 3 × 17, asserted in element.py, and = 40 × 20 − 34 × 17); 222 000 mm³ at the default length | a light extruded channel; the 3.0 leg tops are "short" in the gate's fillet pass, and every other end-face edge is 17 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp, inside and outside | an extrusion's small root radii are not drawn (appearance only, no figure claimed) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 3 mm wall (mech-r69 / r106) |
| alloy, temper, film thickness, tolerances, load | alloy 6063 named; the rest not claimed | no material data sheet is on file (lib/materials.csv al-6063 carries no figures); an extrusion's tolerances are EN 755-9's, not on file and not claimed |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `bottom` (x 0 to `length`, y ±20, z 0 to 3), `leg-left` / `leg-right` (y −20 to −17 / 17 to 20,
z 3 to 20); the channel stays free.

## Materials by layer
`M-ALU-ANOD` the whole profile (anodised aluminium).

## Decals (Blender)
"complexes.org generic" on the bottom's underside, centred.

## Notes
No vendor names, part numbers or marks. No load rating: the class has no load feature and no allowable stress is on file. Drawn as
one box less one cut (the channel, `cutbox`), so the legs' inner faces and the bottom's upper face are cut faces. The AutoCAD gate
(mech-r141): 1 solid, 10 edges picked and 10 filleted at r 0.5, 0 rejected; removed 223.0 of 223.2 mm³; STEP vs glb extents 0.0. The
Blender gate's body volume 221 999.9 mm³ (222 × 1000). Every bounding-box
extreme lies on the uncut outer faces (y ±20 on the legs' outer faces, z 0 on the bottom, z 20 on the legs' tops, x 0 and `length`).
Not drawn: holes, fasteners, end caps, the host. A stainless steel U (EC011895) or a hot-rolled steel channel (DIN 1026 / EN 10279) is
another element, once its standard is on file.

## Outputs (out/)
`profile-u-alu-40x20x3.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011894), our own design (mech-r141, unattended, 2026-11-12): extruded U-channel 40 x 20, bottom and legs 3, sharp corners, anodised, plain, cut to length |
