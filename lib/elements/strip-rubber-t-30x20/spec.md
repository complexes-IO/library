# strip-rubber-t-30x20 · v1.0 · Rubber T-section, generic, solid EPDM, base 30 x 3, post 3, total height 20, black, plain, cut to length

**What** A rubber T-section: the black rubber joint strip a machine lays in a narrow gap between two panels or plates, the post pushed
into the gap and the base lying over both edges, so the joint is covered and soft. A base 30 wide and 3 thick, a post 3 thick standing
up from its middle, 20 high overall. Solid rubber, no sponge, no reinforcement. One straight length, cut to length by the `length`
parameter (default 1000; a parameter stays out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber T-section (ETIM 10.0 EC010637), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM list
(lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010686 (profile-rect-pvc-30x20, mech-r135). Its class is on
file (8 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the post's centre plane y = 0, the base's underside z = 0. The run goes along +x;
the base lies flat (z 0 to 3, y ±15), the post stands upright (y ±1.5, z 3 to 20). Extents x 0 to `length`, y ±15, z 0 to 20.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERT` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010637 Rubber T-section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element;
they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM (lib/materials.csv `epdm`) |
| 2 | Material structure (EF022835) | solid (not cellular) |
| 3 | Base width (EF022837) | 30 mm (y) |
| 4 | Base thickness (EF022838) | 3 mm (z) |
| 5 | Total height (EF001761) | 20 mm (z, the base's underside to the post's top) |
| 6 | Post thickness (EF022839) | 3 mm (y) |
| 7 | Colour (EF000007) | black (the `M-GASKET` layer) |
| 8 | IRHD hardness (EF022836) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, sealing, temperature or fire figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the gap it fills | a joint 3 wide between two panel or plate edges, the post pushed in up to 17 deep, the base 13.5 over each edge; nothing drilled | ETIM 10.0 EC010637 Post thickness / Base width above; the panels are the host's elements (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the host it lies on | the base's underside, flat, 30 wide; a host that bonds or clips it declares that in its own files | ETIM 10.0 EC010637 has no fixing feature; plain stock, as sold cut to length (OPERATING.md 12) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | base 30 × 3, post 3 thick, total height 20 (post 17 above the base); area 141 mm² (30 × 3 + 17 × 3, asserted in element.py, and = 30 × 20 − 2 × 13.5 × 17) | a light joint strip for a 3 mm gap; the 3.0 base ends and post top are "short" in the gate's fillet pass, and every other end-face edge is 13.5, 17, 20 or 30, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other thin-walled profiles (mech-r106 / r131) |
| hardness, sealing, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; laying it in is the host's assembly, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `base` (x 0 to `length`, y ±15, z 0 to 3) and `post` (y ±1.5, z 3 to 20).

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
"complexes.org generic" on the base's upper face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less two cuts (the spaces over the base on each side of the post, `cutbox`),
so those faces are cut faces. The AutoCAD gate (mech-r136): 1 solid, 6 edges picked and 6 filleted at r 0.5, 0 rejected, 0 short,
2 cut edges skipped; removed 110.8 of 110.8 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on uncut faces (y ±15 on the base, z 0 and 20, x 0 and `length`).
Volume at the default length: 141 000 mm³ (141 × 1000).
Not drawn: grip fins, a sponge seal, a joint, the panels.

## Outputs (out/)
`strip-rubber-t-30x20.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010637), our own design (mech-r136, unattended, 2026-11-12): solid EPDM T-section, base 30 x 3, post 3, total height 20, black, plain, cut to length |
