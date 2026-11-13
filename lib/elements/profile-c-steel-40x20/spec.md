# profile-c-steel-40x20 · v1.0 · C-profile, steel, generic, cold-formed galvanised 40 x 20 from 2.0 sheet, inturned lips, slit 20, plain, cut to length

**What** A steel C-profile: the cold-formed, galvanised lipped channel a machine uses as a light mounting channel, a cover, or a
guide a strip, a sliding panel's edge or a cable runs in. Outside 40 wide × 20 high, formed from 2.0 sheet: bottom and legs 2, the
legs' top edges bent inward as lips 2 thick that leave a 20 slit along the run. One straight length, cut to length by the `length`
parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). No holes: a host drills its own.
**Class** rail · **Baseline** our own design: generic C-profile, steel (ETIM 10.0 EC003165), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s
ETIM list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010682 (profile-c-pvc-30x20, mech-r131). Its class
is on file (12 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A cold-formed
lipped channel's sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the section's centre line y = 0, the bottom's outer face z = 0 (the mounting
face). The run goes along +x; the slit is up, at z 20. Extents x 0 to `length`, y ±20, z 0 to 20.
**Built with** toolkit 1.3 · AutoLISP command `CPROFSTL` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC003165 C-profile, steel (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | steel, mild (low-carbon) (lib/materials.csv `steel-mild`) |
| 2 | Material quality (EF001257) | not stated (lib/materials.csv names no grade for steel-mild) |
| 3 | Manufacturing method (EF022801) | cold-formed (roll-formed from strip) |
| 4 | Surface protection (EF000139) | galvanised (zinc-coated strip; coating mass not stated) |
| 5 | Surface treatment (EF025109) | none (plain, unpainted) |
| 6 | Model (EF000010) | lipped channel, inturned lips |
| 7 | Width (EF000008) | 40 mm (y, outside) |
| 8 | Height (EF000040) | 20 mm (z, outside, the bottom's face to the lips' top) |
| 9 | Bottom thickness (EF022841) | 2 mm |
| 10 | Leg thickness (EF023638) | 2 mm |
| 11 | Slit width (EF005247) | 20 mm (between the lips, along the whole run) |
| 12 | Length (EF001438) | cut to length: 1.0 m by default, the `length` parameter |

No ratings.csv: no feature of the class is a rating the checks read, and no load is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it is fixed to | nothing drilled here: the host drills the holes it needs through the bottom and declares them in its own features.csv | ETIM 10.0 EC003165 has no hole feature; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what runs in the channel | the cavity 36 wide × 16 high under the lips, entered through the 20 slit; the lips 2 thick, 8 past the legs each side | this design's choice of section, ETIM 10.0 EC003165 Width / Height / Slit width above; what slides in is the host's element |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 40 × 20 outside, bottom, legs and lips 2 (one strip formed), lips 10 from each outer face, slit 20; area 184 mm² (40 × 20 − 36 × 16 − 20 × 2, asserted in element.py) | a light channel; 2.0 walls are "short" in the gate's fillet pass, and every other edge of the end face is 8 or more, so no 3 to 7 mm free-corner edge is left (mech-r69 / r101) |
| lips | 2 thick, 8 past each leg's inner face | enough to hold a strip, a nut plate or a panel edge in the channel; a C, not a U |
| bends | drawn sharp | a cold-formed section's bend radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | the rail class's 1.0 is too large for a 2 mm wall (mech-r69 / r106) |
| grade, coating mass, load | not claimed | lib/materials.csv steel-mild carries no grade or figures; the class has no load feature |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `bottom` (x 0 to `length`, y ±20, z 0 to 2), `leg-left` / `leg-right` (y −20 to −18 / 18 to 20,
z 2 to 20), `lip-left` / `lip-right` (y −18 to −10 / 10 to 18, z 18 to 20); the cavity and the slit stay free.

## Materials by layer
`M-GALV` the whole profile (galvanised mild steel).

## Decals (Blender)
"complexes.org generic" on the bottom's outer face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less two cuts (the cavity and the slit, `cutbox`), so the inner faces are
cut faces. The AutoCAD gate (mech-r132): 1 solid, 14 edges picked and 14 filleted at r 0.5, 0 rejected, 0 short; removed 225.1 of
225.3 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on the uncut outer faces (y ±20, z 0 and 20, x 0 and `length`). Volume at the default
length: 184 000 mm³ (184 × 1000). No holes, so DFM-010 (sheet holes) has nothing to check.
Not drawn: holes, fasteners, end caps, the bends' radii, what runs in the channel, the host.

## Outputs (out/)
`profile-c-steel-40x20.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003165), our own design (mech-r132, unattended, 2026-11-12): cold-formed galvanised mild-steel lipped channel 40 x 20 from 2.0 sheet, slit 20, plain, cut to length |
