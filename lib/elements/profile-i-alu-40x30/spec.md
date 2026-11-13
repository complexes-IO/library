# profile-i-alu-40x30 · v1.0 · I-profile, aluminium, generic, extruded 40 high x 30 wide, flanges and web 3, sharp corners, anodised, plain (no holes), cut to length

**What** An aluminium I-profile: an extruded I-section 40 high and 30 wide, two flanges 3 thick joined by a web 3 thick, sharp corners,
anodised. A light beam, stiffener or slide-way carrier for guards, frames and fixtures. One straight length, cut to length by the
`length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes.
**Class** rail · **Baseline** our own design: generic I-profile, aluminium (ETIM 10.0 EC012316), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010685 (profile-h-pvc-8x20, mech-r133). Its class is on
file (8 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. No dimensional
standard on file fixes an extruded aluminium I-section's sizes (a rolled steel I-beam's are EN 10365's, another class and not on
file), so every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the web's centre plane y = 0, the lower flange's underside z = 0. The run goes
along +x; the web stands upright (z 3 to 37), the flanges lie flat (z 0 to 3 and 37 to 40). Extents x 0 to `length`, y ±15, z 0 to 40.
**Built with** toolkit 1.3 · AutoLISP command `IPROFALU` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC012316 I-profile, aluminium (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | aluminium |
| 2 | Material quality (EF001257) | aluminium alloy 6063 (lib/materials.csv `al-6063`, the extrusion alloy on file); temper not stated |
| 3 | Surface protection (EF000139) | anodised (the `M-ALU-ANOD` layer); layer thickness not stated |
| 4 | Width (EF000008) | 30 mm (the flanges, along y) |
| 5 | Height (EF000040) | 40 mm (outside the flanges, along z) |
| 6 | Thickness flange (EF020225) | 3 mm |
| 7 | Thickness body (EF009174) | 3 mm (the web) |
| 8 | Cross section (EF000649) | 282 mm² (2 × 30 × 3 + 34 × 3, asserted in element.py) |

No ratings.csv: no feature of the class is a rating the checks read, and no load is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs through a flange and declares them in its own features.csv (fastener, clearance, position) | ETIM 10.0 EC012316 has no hole feature; plain stock, as sold cut to length (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what sits on or beside it | the flanges' outer faces 30 wide; each recess 13.5 deep (flange outstand) and 34 high between the flanges | ETIM 10.0 EC012316 Width / Height / Thickness above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 40 high × 30 wide, flanges and web 3, area 282 mm² (asserted in element.py, and = 30 × 40 − 2 × 13.5 × 34) | a light extruded beam; the 3.0 flange ends and web are "short" in the gate's fillet pass, and every other edge of the end face is 13.5 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp, inside and outside | an extrusion's small root radii are not drawn (appearance only, no figure claimed) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 3 mm wall (mech-r69 / r106) |
| alloy, temper, film thickness, tolerances, load | alloy 6063 named; the rest not claimed | no material data sheet is on file (lib/materials.csv al-6063 carries no figures); an extrusion's tolerances are EN 755-9's, not on file and not claimed |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `flange-bottom` (x 0 to `length`, y ±15, z 0 to 3), `flange-top` (y ±15, z 37 to 40) and `web`
(y ±1.5, z 3 to 37); both recesses stay free.

## Materials by layer
`M-ALU-ANOD` the whole profile (anodised aluminium).

## Decals (Blender)
"complexes.org generic" on the web's +y face, centred.

## Notes
No vendor names, part numbers or marks. No load rating: the class has no load feature and no allowable stress is on file. Drawn as
one box less two cuts (the recesses, `cutbox`), so the recess faces are cut faces. The AutoCAD gate (mech-r134): 1 solid, 8 edges
picked and 8 filleted at r 0.5, 0 rejected, 0 short; removed 220.9 of 221.0 mm³; STEP vs glb extents 0.0. Every bounding-box extreme
lies on the uncut outer faces (y ±15, z 0 and 40, x 0 and `length`). Volume at the default length: 282 000 mm³ (282 × 1000).
Not drawn: holes, fasteners, end caps, the host. A steel I-beam (IPE, EN 10365) is another element, once its standard is on file.

## Outputs (out/)
`profile-i-alu-40x30.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012316), our own design (mech-r134, unattended, 2026-11-12): extruded I-section 40 x 30, flanges and web 3, sharp corners, anodised, plain, cut to length |
