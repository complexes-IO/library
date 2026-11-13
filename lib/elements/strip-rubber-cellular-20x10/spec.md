# strip-rubber-cellular-20x10 · v1.0 · Cellular rubber strip, generic, closed-cell EPDM sponge 20 x 10, black, not self-adhesive, plain, cut to length

**What** A cellular rubber strip: the soft closed-cell sponge a machine bonds or clamps on a door edge, a cover's flange or a panel's
rim as a light seal or buffer. 20 wide × 10 high as delivered (uncompressed), black, rectangular section. One straight length, cut to
length by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6). Not self-adhesive: the host bonds
or clamps it.
**Class** rail · **Baseline** our own design: generic cellular rubber strip (ETIM 10.0 EC010649), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s
ETIM list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC003165 (profile-c-steel-40x20, this round); EC012297
Ceiling profile, between them by name, is a building-trade grid (lib/rounds/mech/r132.md). Its class is on file (7 features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A sponge strip's section is not fixed
by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the strip's centre line y = 0, the bearing face z = 0 (the face that lies on the
host). The run goes along +x; the sealing face is up, at z 10. Extents x 0 to `length`, y ±10, z 0 to 10.
**Built with** toolkit 1.3 · AutoLISP command `STRIPCR` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010649 Cellular rubber strip (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM, closed-cell sponge (lib/materials.csv `epdm`) |
| 2 | Width (EF000008) | 20 mm (y) |
| 3 | Height (EF000040) | 10 mm (z, uncompressed) |
| 4 | Self-adhesive (EF000434) | no |
| 5 | Colour (EF000007) | black (the `M-GASKET` layer) |
| 6 | Shore hardness (EF022944) | not stated (a sponge compound's hardness is a property of the compound; lib/materials.csv epdm carries no figure) |
| 7 | Operating temperature (EF001742) | not stated (lib/materials.csv epdm carries no temperature figure) |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, temperature, compression or sealing figure is
claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it lies on | the bearing face 20 wide, bonded or clamped by the host; nothing drilled | ETIM 10.0 EC010649 Self-adhesive "no" above; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what closes on it | the sealing face 20 wide, 10 above the bearing face uncompressed; how far a door or cover squeezes it is the host's choice | this design's choice of section, ETIM 10.0 EC010649 Width / Height above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 20 × 10, rectangular; area 200 mm² (asserted in element.py) | a light door or cover seal; both end-face edges are 8 or more, so no 3 to 7 mm free-corner edge is left (mech-r69 / r101) |
| state drawn | uncompressed, as delivered | the squeeze belongs to the host's assembly |
| cell structure | closed cells, not drawn | the sponge is drawn solid (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other profiles (mech-r106 / r131) |
| hardness, temperature range, compression set, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; the strip's compression is the host's, not a motion. behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `strip` (x 0 to `length`, y ±10, z 0 to 10).

## Materials by layer
`M-GASKET` the whole strip (EPDM sponge, black).

## Decals (Blender)
"complexes.org generic" on the bearing face, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box. The AutoCAD gate (mech-r132): 1 solid, 12 edges picked and 12 filleted
at r 0.5, 0 rejected; removed 218.8 of 221.0 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on its faces (y ±10, z 0 and 10, x 0 and
`length`). Volume at the default length: 200 000 mm³ (200 × 1000).
Not drawn: the cells, an adhesive or liner, a joint or splice, the host.

## Outputs (out/)
`strip-rubber-cellular-20x10.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010649), our own design (mech-r132, unattended, 2026-11-12): closed-cell EPDM sponge strip 20 x 10, black, not self-adhesive, plain, cut to length |
