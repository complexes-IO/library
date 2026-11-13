# profile-i-pvc-30x20 · v1.0 · I-profile, plastic, generic, rigid PVC 30 high x 20 wide, post (web) and beams (flanges) 2.5, sharp corners, white, plain, cut to length

**What** A plastic I-profile: an extruded rigid PVC I-section 30 high and 20 wide, an upright post (the web) 2.5 thick between two flat
beams (the flanges) 2.5 thick, sharp corners, white. A light stiffener or spacer strip for covers, trays and partitions. One straight
length, cut to length by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes.
**Class** rail · **Baseline** our own design: generic I-profile, plastic (ETIM 10.0 EC010684), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is a class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM list
(lib/toolkit/generic.py ORDER, by name) that builds unattended, built beside profile-i-alu-40x30 (this round). Its class is on file
(7 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A plastic I-section's sizes
are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the post's centre plane y = 0, the lower beam's underside z = 0. The run goes
along +x; the post stands upright (z 2.5 to 27.5), the beams lie flat (z 0 to 2.5 and 27.5 to 30). Extents x 0 to `length`, y ±10,
z 0 to 30.
**Built with** toolkit 1.3 · AutoLISP command `IPROFPVC` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010684 I-profile, plastic (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs. ETIM names the members "post" and "beam"; this design reads the post as the upright member (the web)
and the beams as the flat members (the flanges), as profile-h-pvc-8x20 reads its upright posts and flat beam.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PVC, rigid (lib/materials.csv `pvc`) |
| 2 | Width (EF000008) | 20 mm (the beams, along y) |
| 3 | Height (EF000040) | 30 mm (outside the beams, along z) |
| 4 | Post thickness (EF022839) | 2.5 mm (the web) |
| 5 | Beam thickness (EF023639) | 2.5 mm (each flange) |
| 6 | Colour (EF000007) | white (the `M-WHITE-PVC` layer) |
| 7 | RAL-number (EF000116) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no load, temperature or fire class is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: a host that fixes it (bonded or screwed through a beam) drills its own hole and declares it in its own features.csv | ETIM 10.0 EC010684 has no hole feature; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what sits on or beside it | the beams' outer faces 20 wide; each recess 8.75 deep (beam outstand) and 25 high between the beams | ETIM 10.0 EC010684 Width / Height / Post thickness / Beam thickness above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 30 high × 20 wide, post and beams 2.5, area 162.5 mm² (2 × 20 × 2.5 + 25 × 2.5, asserted in element.py, and = 20 × 30 − 2 × 8.75 × 25) | a light plastic stiffener; the 2.5 beam ends and post are "short" in the gate's fillet pass, and every other edge of the end face is 8.75 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other thin-walled profiles (mech-r106 / r131) |
| compound, flammability, temperature range, load | not claimed | lib/materials.csv pvc carries no figures; a flammability class belongs to a compound and a thickness (duct-40x60, request mech-1) |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `beam-bottom` (x 0 to `length`, y ±10, z 0 to 2.5), `beam-top` (y ±10, z 27.5 to 30) and `post`
(y ±1.25, z 2.5 to 27.5); both recesses stay free.

## Materials by layer
`M-WHITE-PVC` the whole profile (rigid PVC, white).

## Decals (Blender)
"complexes.org generic" on the post's +y face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less two cuts (the recesses, `cutbox`), so the recess faces are cut faces.
The AutoCAD gate (mech-r134): 1 solid, 8 edges picked and 8 filleted at r 0.5, 0 rejected, 0 short; removed 218.8 of 218.9 mm³; STEP
vs glb extents 0.0. Every bounding-box extreme lies on the uncut outer faces (y ±10, z 0 and 30, x 0 and `length`). Volume at the default length:
162 500 mm³ (162.5 × 1000).
Not drawn: holes, fasteners, end caps, the host.

## Outputs (out/)
`profile-i-pvc-30x20.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010684), our own design (mech-r134, unattended, 2026-11-12): rigid PVC I-section 30 x 20, post and beams 2.5, white, plain, cut to length |
