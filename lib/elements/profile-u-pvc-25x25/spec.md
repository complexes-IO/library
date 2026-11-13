# profile-u-pvc-25x25 · v1.0 · U-profile, plastic, generic, rigid PVC U-section 25 x 25, bottom and legs 2.5, sharp corners, grey, plain (no holes), cut to length

**What** A plastic U-profile: the extruded rigid PVC U-section a machine uses as a cover or edge profile, a socket a panel edge or a
strip sits in, a small open cable channel. Outside 25 wide × 25 high, bottom and legs 2.5, sharp corners, grey. One straight length,
cut to length by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes: a host drills its
own.
**Class** rail · **Baseline** our own design: generic U-profile, plastic (ETIM 10.0 EC010683), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is a class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM list
(lib/toolkit/generic.py ORDER, by name) that builds unattended, beside EC011894 (profile-u-alu-40x20x3, mech-r141). Its class is on
file (7 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A plastic U-section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the section's centre plane y = 0, the bottom's outer face z = 0 (the mounting
face). The run goes along +x; the opening is up, at z 25. Extents x 0 to `length`, y ±12.5, z 0 to 25.
**Built with** toolkit 1.3 · AutoLISP command `UPROFPVC` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010683 U-profile, plastic (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PVC, rigid (lib/materials.csv `pvc`) |
| 2 | Width (EF000008) | 25 mm (y, outside) |
| 3 | Height (EF000040) | 25 mm (z, outside, the bottom's face to the legs' tops) |
| 4 | Bottom thickness (EF022841) | 2.5 mm |
| 5 | Leg thickness (EF023638) | 2.5 mm |
| 6 | Colour (EF000007) | grey (the `M-GREY-PVC` layer) |
| 7 | RAL-number (EF000116) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no load, temperature or fire class is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs through the bottom and declares them in its own features.csv | ETIM 10.0 EC010683 has no hole feature; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what sits in the channel | the clear channel 20 wide between the legs and 22.5 deep above the bottom, open on top | ETIM 10.0 EC010683 Width / Height / Bottom thickness / Leg thickness above; what sits in it is the host's element |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | U 25 × 25, bottom and legs 2.5, area 175 mm² (25 × 2.5 + 2 × 2.5 × 22.5, asserted in element.py, and = 25 × 25 − 20 × 22.5); 175 000 mm³ at the default length | a small cover and edge channel; the 2.5 leg tops are "short" in the gate's fillet pass, and every other end-face edge is 20 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 2.5 mm wall (mech-r69 / r106) |
| compound, flammability, temperature range, load | not claimed | lib/materials.csv pvc carries no figures; a flammability class belongs to a compound and a thickness (duct-40x60, request mech-1) |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `bottom` (x 0 to `length`, y ±12.5, z 0 to 2.5), `leg-left` / `leg-right` (y −12.5 to −10 / 10
to 12.5, z 2.5 to 25); the channel stays free.

## Materials by layer
`M-GREY-PVC` the whole profile (rigid PVC, grey).

## Decals (Blender)
"complexes.org generic" on the bottom's outer face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less one cut (the channel, `cutbox`), so the inner faces are cut faces. The
AutoCAD gate (mech-r141): 1 solid, 10 edges picked and 10 filleted at r 0.5, 0 rejected; removed 222.5 of 222.6 mm³; STEP vs glb
extents 0.0. The Blender gate's body volume 175 000.0 mm³ (175 × 1000). Every
bounding-box extreme lies on the uncut outer faces (y ±12.5, z 0 and 25, x 0 and `length`).
Not drawn: holes, fasteners, end caps, what sits in the channel, the host.

## Outputs (out/)
`profile-u-pvc-25x25.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010683), our own design (mech-r141, unattended, 2026-11-12): rigid PVC U-section 25 x 25, bottom and legs 2.5, grey, plain, cut to length |
