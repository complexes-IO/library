# profile-angle-pvc-30x30x3 · v1.0 · angle profile, plastic, generic, rigid PVC equal legs 30 x 30, wall 3, sharp corners, white, not perforated, cut to length

**What** A plastic angle profile: an extruded rigid PVC equal-leg angle, legs 30 × 30, wall 3, sharp inner and outer corners, white,
not perforated. An edge trim, corner guard or light cover angle for panels, trays and covers. One straight length, cut to length by
the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes: a host that fixes it drills its own
and declares them in its own features.csv.
**Class** rail · **Baseline** our own design: generic plastic angle profile (ETIM 10.0 EC010681), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is a class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM list
(lib/toolkit/generic.py ORDER, by name) that builds unattended, built beside profile-rect-pvc-30x20 (this round). Its class is on file
(10 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A plastic angle's sizes are
not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the angle's outer corner line (the heel) y = 0, z = 0. The run goes along +x;
one leg (the foot) along +y, its underside at z 0; the other (the upright) along +z, its outer face at y 0. Extents x 0 to
`length`, y 0 to 30, z 0 to 30.
**Built with** toolkit 1.3 · AutoLISP command `ANGLEPVC` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010681 Plastic angle profile (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element;
they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | equal-leg angle, sharp corners (no root or toe radius drawn) |
| 2 | Material (EF002169) | PVC, rigid (lib/materials.csv `pvc`) |
| 3 | Width (EF000008) | 30 mm (the foot, along y, outside) |
| 4 | Height (EF000040) | 30 mm (the upright, along z, outside) |
| 5 | Thickness (EF000125) | 3 mm (both legs) |
| 6 | Length (EF001438) | 1000 mm by default, the `length` parameter (100 or more), set per BOM row |
| 7 | Angle (EF008153) | 90° |
| 8 | Perforated (button facing) (EF014903) | no |
| 9 | Colour (EF000007) | white (the `M-WHITE-PVC` layer) |
| 10 | RAL-number (EF000116) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no load, temperature or fire class is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: a host that fixes it (bonded or screwed through a leg) drills its own hole and declares it in its own features.csv | ETIM 10.0 EC010681 has no hole feature; plain stock, as sold cut to length (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the edge it covers | the inner faces of the legs, 27 × 27 free inside the corner | ETIM 10.0 EC010681 Width / Height / Thickness above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 30 × 30 outside, wall 3, equal legs, area 171 mm² (30 × 3 + 27 × 3, asserted in element.py) | a light trim and corner-guard size; a 3.0 wall is "short" in the gate's fillet pass, and the legs' inner faces are 27, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp, inside and outside | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other thin-walled profiles (mech-r106 / r131) |
| compound, flammability, temperature range, load | not claimed | lib/materials.csv pvc carries no figures; a flammability class belongs to a compound and a thickness (duct-40x60, request mech-1) |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `foot` (x 0 to `length`, y 0 to 30, z 0 to 3) and `upright` (y 0 to 3, z 3 to 30).

## Materials by layer
`M-WHITE-PVC` the whole angle (rigid PVC, white).

## Decals (Blender)
"complexes.org generic" on the foot's underside, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less its inside (one `cutbox`), so the inner faces are cut faces. The
AutoCAD gate (mech-r135): 1 solid, 7 edges picked and 7 filleted at r 0.5, 0 rejected, 0 short, 1 cut edge skipped; removed 167.3 of
167.4 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on the uncut outer faces (y 0 and 30, z 0 and 30, x 0 and `length`). Volume at the default length:
171 000 mm³ (171 × 1000).
Not drawn: holes, fasteners, the host. An aluminium angle is profile-angle-alu-40x40x3 (EC012022), another class.

## Outputs (out/)
`profile-angle-pvc-30x30x3.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010681), our own design (mech-r135, unattended, 2026-11-12): rigid PVC equal-leg angle 30 x 30 x 3, sharp corners, white, not perforated, plain, cut to length |
