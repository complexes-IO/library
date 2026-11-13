# profile-rect-pvc-30x20 · v1.0 · rectangular profile, plastic, generic, rigid PVC hollow section 30 wide x 20 high, posts and beams 2.5, sharp corners, grey, cut to length

**What** A plastic rectangular profile: an extruded rigid PVC rectangular hollow section 30 wide and 20 high, two upright posts (the
side walls) and two flat beams (the top and bottom walls), each 2.5 thick, sharp corners, grey, open at both ends. A light spacer,
sleeve or cover tube. One straight length, cut to length by the `length` parameter (default 1000; a parameter stays out of the id,
OPERATING.md 6). No holes.
**Class** rail · **Baseline** our own design: generic rectangular profile, plastic (ETIM 10.0 EC010686), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: it is a class of EG019710 Profiles in `python lib/build.py inventory mech`'s
ETIM list (lib/toolkit/generic.py ORDER, by name) that builds unattended, built beside profile-angle-pvc-30x30x3 (this round). Its
class is on file (7 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A plastic
rectangular section's sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the section's centre plane y = 0, the bottom beam's underside z = 0. The run goes
along +x; the posts stand upright (y −15 to −12.5 and 12.5 to 15), the beams lie flat (z 0 to 2.5 and 17.5 to 20). Extents x 0 to
`length`, y ±15, z 0 to 20.
**Built with** toolkit 1.3 · AutoLISP command `RECTPVC` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010686 Rectangular profile, plastic (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature
in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define
the element; they are design inputs. ETIM names the members "post" and "beam"; this design reads the posts as the upright members
(the side walls) and the beams as the flat members (the top and bottom walls), as profile-h-pvc-8x20 and profile-i-pvc-30x20 read
them. The class's synonyms (rectangular section, square profile) leave hollow or solid open; with two wall thicknesses as features,
this design is the hollow section.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PVC, rigid (lib/materials.csv `pvc`) |
| 2 | Width (EF000008) | 30 mm (outside, along y) |
| 3 | Height (EF000040) | 20 mm (outside, along z) |
| 4 | Post thickness (EF022839) | 2.5 mm (each side wall) |
| 5 | Beam thickness (EF023639) | 2.5 mm (the top and the bottom wall) |
| 6 | Colour (EF000007) | grey (the `M-GREY-PVC` layer) |
| 7 | RAL-number (EF000116) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no load, temperature or fire class is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: a host that fixes it (bonded, clipped or screwed through a wall) drills its own hole and declares it in its own features.csv | ETIM 10.0 EC010686 has no hole feature; plain stock, as sold cut to length (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what passes through or sits on it | the clear bore 25 × 15, open at both ends; the outer faces 30 wide and 20 high | ETIM 10.0 EC010686 Width / Height / Post thickness / Beam thickness above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 30 wide × 20 high, posts and beams 2.5, bore 25 × 15, area 225 mm² (30 × 20 − 25 × 15, asserted in element.py, and = 2 × 30 × 2.5 + 2 × 15 × 2.5) | a light plastic spacer tube; the 2.5 wall edges are "short" in the gate's fillet pass, the bore's edges are cut edges, and the outer end-face edges are 20 and 30, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp, inside and outside | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other thin-walled profiles (mech-r106 / r131) |
| compound, flammability, temperature range, load | not claimed | lib/materials.csv pvc carries no figures; a flammability class belongs to a compound and a thickness (duct-40x60, request mech-1) |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `beam-bottom` (x 0 to `length`, y ±15, z 0 to 2.5), `beam-top` (y ±15, z 17.5 to 20),
`post-left` (y −15 to −12.5, z 2.5 to 17.5) and `post-right` (y 12.5 to 15, z 2.5 to 17.5); the bore stays free.

## Materials by layer
`M-GREY-PVC` the whole profile (rigid PVC, grey).

## Decals (Blender)
"complexes.org generic" on the top beam's upper face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less its bore (one `cutbox` through the whole length), so the bore faces are
cut faces. The AutoCAD gate (mech-r135): 1 solid, 12 edges picked and 12 filleted at r 0.5, 0 rejected, 0 short, 0 cut edges
skipped; removed 225.1 of 225.3 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on the uncut outer faces (y ±15, z 0 and 20, x 0 and `length`). Volume at the default
length: 225 000 mm³ (225 × 1000).
Not drawn: holes, fasteners, end caps, the host.

## Outputs (out/)
`profile-rect-pvc-30x20.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010686), our own design (mech-r135, unattended, 2026-11-12): rigid PVC rectangular hollow section 30 x 20, posts and beams 2.5, grey, plain, cut to length |
