# strip-rubber-angle-25x20 · v1.0 · Rubber angle profile, generic, solid EPDM, width 25, height 20, base and post 3, black, plain, cut to length

**What** A rubber angle profile: the black rubber strip a machine lays over the outer edge of a panel, a plate or a frame member, so the
edge is covered and soft. A base 25 wide and 3 thick, a post 20 high and 3 thick, joined at the heel (an unequal angle). Solid rubber,
no sponge, no reinforcement. One straight length, cut to length by the `length` parameter (default 1000; a parameter stays out of the
id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber angle profile (ETIM 10.0 EC010647), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010638 (strip-rubber-u-20x15, mech-r136). Its class is on
file (9 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the angle's outer corner line y = 0, z = 0 (the heel). The run goes along +x; the
base lies flat along +y (y 0 to 25, z 0 to 3), the post stands along +z (y 0 to 3, z 0 to 20). Extents x 0 to `length`, y 0 to 25,
z 0 to 20.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERANG` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010647 Rubber angle profile (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element;
they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM (lib/materials.csv `epdm`) |
| 2 | Material structure (EF022835) | solid (not cellular) |
| 3 | Width (EF000008) | 25 mm (y, the base leg's outer width) |
| 4 | Base thickness (EF022838) | 3 mm (z) |
| 5 | Height (EF000040) | 20 mm (z, the post leg's outer height) |
| 6 | Post thickness (EF022839) | 3 mm (y) |
| 7 | Length (EF001438) | 1000 mm by default: the `length` parameter, set per BOM row |
| 8 | IRHD hardness (EF022836) | not stated |
| 9 | Colour (EF000007) | black (the `M-GASKET` layer) |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, sealing, temperature or fire figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the edge it covers | an outer 90-degree edge of a panel, plate or frame member: the base on one face, the post on the other, 22 and 17 clear inside the legs; nothing drilled | ETIM 10.0 EC010647 Width / Height above; the panel is the host's element (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the host it lies on | the legs' inner faces, flat; a host that bonds or clips it declares that in its own files | ETIM 10.0 EC010647 has no fixing feature; plain stock, as sold cut to length (OPERATING.md 12) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | base 25 × 3, post 20 × 3, joined at the heel; area 126 mm² (25 × 3 + 17 × 3, asserted in element.py, and = 25 × 20 − 22 × 17) | a light edge strip; the 3.0 leg ends are "short" in the gate's fillet pass, and every other end-face edge is 17, 20, 22 or 25, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other thin-walled profiles (mech-r106 / r131) |
| hardness, sealing, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; laying it on is the host's assembly, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `base` (x 0 to `length`, y 0 to 25, z 0 to 3) and `post` (y 0 to 3, z 3 to 20).

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
"complexes.org generic" on the base's upper face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less one cut (the space inside the legs, `cutbox`), so those faces are cut
faces. The AutoCAD gate (mech-r137): 1 solid, 7 edges picked and 7 filleted at r 0.5, 0 rejected, 0 short, 1 cut edge skipped;
removed 165.7 of 165.8 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on uncut faces (y 0 and 25, z 0 and 20, x 0 and
`length`).
Volume at the default length: 126 000 mm³ (126 × 1000).
Not drawn: grip fins, a sponge seal, a joint, the host.

## Outputs (out/)
`strip-rubber-angle-25x20.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010647), our own design (mech-r137, unattended, 2026-11-12): solid EPDM angle, width 25, height 20, base and post 3, black, plain, cut to length |
