# profile-h-pvc-8x20 · v1.0 · H-profile, plastic, generic, rigid PVC 8 x 20, posts and beam 2.5, two slots 3.0 x 8.75 for 3 mm panels, grey, plain, cut to length

**What** A plastic H-profile: the extruded rigid PVC joining strip that holds two 3 mm panels edge to edge in one plane (a guard's
infill, a cover, a partition). Outside 8 wide × 20 high: two posts 2.5 thick joined at mid-height by a beam 2.5 thick, leaving a
slot 3.0 wide and 8.75 deep above the beam and another below it. One straight length, cut to length by the `length` parameter
(default 1000; a parameter stays out of the id, OPERATING.md 6). No holes.
**Class** rail · **Baseline** our own design: generic H-profile, plastic (ETIM 10.0 EC010685), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010640 (strip-clamping-8x15, this round); the classes
between them by name are building-trade parts (lib/rounds/mech/r133.md). Its class is on file (7 features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A plastic H-section's sizes are not
fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the slots' centre plane y = 0, the posts' lower ends z = 0. The run goes along
+x; the beam lies at mid-height (z 8.75 to 11.25); the panels lie in the plane y = 0, one entering from above, one from below.
Extents x 0 to `length`, y ±4, z 0 to 20.
**Built with** toolkit 1.3 · AutoLISP command `HPROFPVC` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010685 H-profile, plastic (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PVC, rigid (lib/materials.csv `pvc`) |
| 2 | Width (EF000008) | 8 mm (y, outside the posts) |
| 3 | Height (EF000040) | 20 mm (z, the posts' length) |
| 4 | Post thickness (EF022839) | 2.5 mm |
| 5 | Beam thickness (EF023639) | 2.5 mm |
| 6 | Colour (EF000007) | grey (the `M-GREY-PVC` layer) |
| 7 | RAL-number (EF000116) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no load, temperature or fire class is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the two panels it joins | each 3.0 thick, its edge 8.75 into a slot, both in the plane y = 0; nothing drilled | ETIM 10.0 EC010685 Width / Post thickness above (8 − 2 × 2.5 = 3.0); the panels are the host's elements (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the host it is fixed to | nothing drilled here: it is held by the panels it joins; a host that fixes it drills its own hole and declares it in its own features.csv | ETIM 10.0 EC010685 has no hole feature; plain stock |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 8 × 20 outside, posts and beam 2.5, two slots 3.0 × 8.75; area 107.5 mm² (2 × 2.5 × 20 + 3 × 2.5, asserted in element.py, and = 8 × 20 − 2 × 3 × 8.75) | a joining strip for 3 mm panels; the 2.5 posts and beam and the 3.0 slot bottoms are "short" in the gate's fillet pass, and every other edge of the end face is 8 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| slot width | 3.0, the panel's thickness | a slide fit; the fit's clearance is the host's choice of panel tolerance |
| beam | at mid-height, so both slots are 8.75 deep | the two panels go in equally far |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| compound, flammability, temperature range, load | not claimed | lib/materials.csv pvc carries no figures; a flammability class belongs to a compound and a thickness (duct-40x60, request mech-1) |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `post-left` / `post-right` (x 0 to `length`, y −4 to −1.5 / 1.5 to 4, z 0 to 20), `beam`
(y ±1.5, z 8.75 to 11.25); both slots stay free.

## Materials by layer
`M-GREY-PVC` the whole profile (rigid PVC, grey).

## Decals (Blender)
"complexes.org generic" on a post's outer face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less two cuts (the slots, `cutbox`), so the slots' faces are cut faces.
The AutoCAD gate (mech-r133): 1 solid, 8 edges picked and 8 filleted at r 0.5, 0 rejected, 0 short; removed 218.8 of 218.9 mm³;
STEP vs glb extents 0.0. Every bounding-box extreme lies on the uncut outer faces (y ±4, z 0 and 20, x 0 and `length`). Volume at the default length:
107 500 mm³ (107.5 × 1000).
Not drawn: holes, fasteners, end caps, the panels, the host.

## Outputs (out/)
`profile-h-pvc-8x20.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010685), our own design (mech-r133, unattended, 2026-11-12): rigid PVC H-section 8 x 20, posts and beam 2.5, two slots 3.0 for 3 mm panels, grey, plain, cut to length |
