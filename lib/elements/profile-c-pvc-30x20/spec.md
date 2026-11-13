# profile-c-pvc-30x20 · v1.0 · C-profile, plastic, generic, rigid PVC 30 x 20, bottom and legs 3, inturned lips 3 thick, slit 14, grey, plain, cut to length

**What** A plastic C-profile: the extruded rigid PVC channel a machine uses as a cover strip, a small cable channel, a guide a
sliding panel's edge or a strip runs in. Outside 30 wide × 20 high, bottom and legs 3, the legs' top edges turned inward as lips 3
thick that leave a 14 slit along the run. One straight length, cut to length by the `length` parameter (default 1000; a parameter
stays out of the id, OPERATING.md 6). No holes: a host drills its own.
**Class** rail · **Baseline** our own design: generic C-profile, plastic (ETIM 10.0 EC010682), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s
ETIM list (lib/toolkit/generic.py ORDER) that builds unattended (lib/needs-em/mech.md: the stainless angle and the bulb flats are
rolled sections their standards shape). Its class is on file (8 features, lib/standards/etim/class-features.csv). No product was
matched and no vendor file was opened. A plastic C-section's sizes are not fixed by a dimensional standard: every size is a design
choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the section's centre line y = 0, the bottom's outer face z = 0 (the mounting
face). The run goes along +x; the slit is up, at z 20. Extents x 0 to `length`, y ±15, z 0 to 20.
**Built with** toolkit 1.3 · AutoLISP command `CPROFPVC` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010682 C-profile, plastic (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PVC, rigid (lib/materials.csv `pvc`) |
| 2 | Width (EF000008) | 30 mm (y, outside) |
| 3 | Height (EF000040) | 20 mm (z, outside, the bottom's face to the lips' top) |
| 4 | Bottom thickness (EF022841) | 3 mm |
| 5 | Leg thickness (EF023638) | 3 mm |
| 6 | Slit width (EF005247) | 14 mm (between the lips, along the whole run) |
| 7 | Colour (EF000007) | grey (the `M-GREY-PVC` layer) |
| 8 | RAL-number (EF000116) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no load, temperature or fire class is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs through the bottom and declares them in its own features.csv | ETIM 10.0 EC010682 has no hole feature; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what runs in the channel | the cavity 24 wide × 14 high under the lips, entered through the 14 slit; the lips 3 thick, 5 past the legs each side | this design's choice of section, ETIM 10.0 EC010682 Width / Height / Slit width above; what slides in is the host's element |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 30 × 20 outside, bottom and legs 3, lips 3 thick and 8 from each outer face, slit 14; area 222 mm² (30 × 20 − 24 × 14 − 14 × 3, asserted in element.py) | a small cover and guide channel; 3.0 walls are "short" in the gate's fillet pass, and every other edge of the end face is 8 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| lips | 3 thick, 5 past each leg's inner face | enough to hold a strip or a panel edge in the channel; a C, not a U |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 3 mm wall (mech-r69 / r106) |
| compound, flammability, temperature range, load | not claimed | lib/materials.csv pvc carries no figures; a flammability class belongs to a compound and a thickness (duct-40x60, request mech-1) |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `bottom` (x 0 to `length`, y ±15, z 0 to 3), `leg-left` / `leg-right` (y −15 to −12 / 12 to 15,
z 3 to 20), `lip-left` / `lip-right` (y −12 to −7 / 7 to 12, z 17 to 20); the cavity and the slit stay free.

## Materials by layer
`M-GREY-PVC` the whole profile (rigid PVC, grey).

## Decals (Blender)
"complexes.org generic" on the bottom's outer face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less two cuts (the cavity and the slit, `cutbox`), so the inner faces are
cut faces. The AutoCAD gate (mech-r131): 1 solid, 14 edges picked and 14 filleted at r 0.5, 0 rejected, 0 short; removed 223.6 of
223.8 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on the uncut outer faces (y ±15, z 0 and 20,
x 0 and `length`). Volume at the default length: 222 000 mm³ (222 × 1000).
Not drawn: holes, fasteners, end caps, what runs in the channel, the host.

## Outputs (out/)
`profile-c-pvc-30x20.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010682), our own design (mech-r131, unattended, 2026-11-12): rigid PVC C-section 30 x 20, bottom and legs 3, lips 3, slit 14, grey, plain, cut to length |
