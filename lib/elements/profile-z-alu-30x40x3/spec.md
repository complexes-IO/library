# profile-z-alu-30x40x3 · v1.0 · Z-profile, aluminium, generic, extruded Z-section, flanges 30 and 30, height 40, thickness 3, sharp corners, anodised, plain (no holes), cut to length

**What** An aluminium Z-profile: an extruded Z-section, a low flange 30 wide to one side of an upright web and a top flange 30 wide to
the other side, total height 40, flanges and web 3, sharp corners, anodised. A light step, offset bracket, cover joint or panel edge
a machine's guards, covers and frames are made with: it joins two faces that lie 37 apart in height and side by side. One straight
length, cut to length by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes.
**Class** rail · **Baseline** our own design: generic Z-profile, aluminium (ETIM 10.0 EC012295), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010683 (profile-u-pvc-25x25, mech-r141); the classes
between them by name are set aside (lib/needs-em/mech.md, 217). Its class is on file (7 features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. No dimensional standard on file fixes an
extruded aluminium Z-section's sizes (EN 755-9 gives an extrusion's tolerances only, not on file and not claimed), so every size is a
design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the web's centre plane y = 0, the low flange's underside z = 0. The run goes along
+x; the low flange lies flat to −y (y −28.5 to 1.5, z 0 to 3), the web stands upright (y ±1.5), the top flange lies flat to +y (y −1.5
to 28.5, z 37 to 40). Extents x 0 to `length`, y ±28.5, z 0 to 40.
**Built with** toolkit 1.3 · AutoLISP command `ZPROFALU` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC012295 Z-profile, aluminium (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | aluminium |
| 2 | Material quality (EF001257) | aluminium alloy 6063 (lib/materials.csv `al-6063`, the extrusion alloy on file); temper not stated |
| 3 | Surface protection (EF000139) | anodised (the `M-ALU-ANOD` layer); layer thickness not stated |
| 4 | Width top base (EF026266) | 30 mm (along +y, outside, the top flange over the web) |
| 5 | Width low base (EF026267) | 30 mm (along −y, outside, the low flange over the web) |
| 6 | Height (EF000040) | 40 mm (along z, outside) |
| 7 | Thickness (EF000125) | 3 mm (flanges and web alike) |

No ratings.csv: no feature of the class is a rating the checks read, and no load is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs through either flange or the web and declares them in its own features.csv (fastener, clearance, position) | ETIM 10.0 EC012295 has no hole feature; plain stock, as sold cut to length (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the two faces it joins | the low flange's underside (z 0, 30 wide) and the top flange's upper face (z 40, 30 wide), 40 apart in height; the clear step under the top flange 27 wide and 37 high, over the low flange 27 wide and 37 high | ETIM 10.0 EC012295 Width top base / Width low base / Height / Thickness above; what they meet is the host's element |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | Z, flanges 30 and 30, height 40, thickness 3, area 282 mm² (30 × 3 + 30 × 3 + 34 × 3, asserted in element.py, and = 57 × 40 − 2 × 27 × 37); 282 000 mm³ at the default length | a light extruded Z; the 3.0 flange free edges are "short" in the gate's fillet pass, and every other end-face edge is 27 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp, inside and outside | an extrusion's small root radii are not drawn (appearance only, no figure claimed) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 3 mm wall (mech-r69 / r106) |
| alloy, temper, film thickness, tolerances, load | alloy 6063 named; the rest not claimed | no material data sheet is on file (lib/materials.csv al-6063 carries no figures); an extrusion's tolerances are EN 755-9's, not on file and not claimed |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `flange-low` (x 0 to `length`, y −28.5 to 1.5, z 0 to 3), `web` (y ±1.5, z 3 to 37) and
`flange-top` (y −1.5 to 28.5, z 37 to 40); the two steps stay free.

## Materials by layer
`M-ALU-ANOD` the whole profile (anodised aluminium).

## Decals (Blender)
No label. The Blender gate puts a decal island only on its printed layers (toolkit/blender/gate.py `--printed`: M-WHITE-PA,
M-BLACK-PA), and this part's one layer is M-ALU-ANOD, so no tool on file carries one.

## Notes
No vendor names, part numbers or marks. No load rating: the class has no load feature and no allowable stress is on file. Drawn as
one box less two cuts (`cutbox`: the step under the top flange and the step over the low flange), so the web's two faces and the
flanges' inner faces are cut faces. Every bounding-box extreme lies on an outer face of the box that the cuts leave in part (y −28.5
on the low flange's free edge, y 28.5 on the top flange's, z 0 under the low flange, z 40 on the top flange, x 0 and `length`).
Not drawn: holes, fasteners, end caps, the host. A steel or stainless Z (no class of its own on file in EG019710) is another element.

## Outputs (out/)
`profile-z-alu-30x40x3.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012295), our own design (mech-r142, unattended, 2026-11-13): extruded Z-section, flanges 30 and 30, height 40, thickness 3, sharp corners, anodised, plain, cut to length |
