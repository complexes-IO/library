# strip-rubber-u-20x15 · v1.0 · Rubber U-section, generic, solid EPDM U-channel 20 x 15, flat bottom 3, legs 3, clamping width 14, black, plain, cut to length

**What** A rubber U-section: the black rubber channel a machine lays over the edge of a board or plate 14 thick (a soft edge, a
bumper strip) or along a run as a soft liner. Outside 20 wide × 15 high, a flat bottom 3 thick, two legs 3 thick, a clear channel 14
wide and 12 deep. Solid rubber, not transparent, no reinforcement. Wider and shallower than strip-clamping-8x15 (a 2.0 slot that grips
sheet). One straight length, cut to length by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber U-section (ETIM 10.0 EC010638), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM list
(lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010637 (strip-rubber-t-30x20, this round). Its class is on
file (10 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the channel's centre plane y = 0, the bottom's underside z = 0. The run goes
along +x; the channel opens upward (+z), its floor at z 3, the legs (y −10 to −7 and 7 to 10) up to z 15. Extents x 0 to `length`,
y ±10, z 0 to 15.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERU` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010638 Rubber U-section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element;
they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM (lib/materials.csv `epdm`) |
| 2 | Material structure (EF022835) | solid (not cellular) |
| 3 | Flat bottom (EF011063) | yes |
| 4 | Clamping width (EF005935) | 14 mm (the clear channel between the legs, y) |
| 5 | Width (EF000008) | 20 mm (outside, y) |
| 6 | Bottom thickness (EF022841) | 3 mm (z) |
| 7 | Height (EF000040) | 15 mm (z, outside) |
| 8 | Colour (EF000007) | black (the `M-GASKET` layer) |
| 9 | Transparent (EF006243) | no |
| 10 | IRHD hardness (EF022836) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, holding force, temperature or fire figure is
claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the edge it covers | a board or plate 14 thick, its edge pushed up to 12 into the channel; nothing drilled | ETIM 10.0 EC010638 Clamping width above; the board is the host's element (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the host it lies on | the flat bottom, 20 wide; a host that bonds or clips it declares that in its own files | ETIM 10.0 EC010638 Flat bottom above; plain stock, as sold cut to length (OPERATING.md 12) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 20 wide × 15 high, bottom 3, legs 3, channel 14 × 12; area 132 mm² (20 × 15 − 14 × 12, asserted in element.py, and = 20 × 3 + 2 × 3 × 12) | a light rubber channel; the 3.0 bottom ends and legs' tops are "short" in the gate's fillet pass, and every other end-face edge is 12, 14, 15 or 20, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| leg thickness | 3 | not a class feature; equal to the bottom |
| clamping | interference only: no reinforcement, no grip fins drawn | a plain rubber U; no holding force claimed |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other thin-walled profiles (mech-r106 / r131) |
| hardness, holding force, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; pushing it on is the host's assembly, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `bottom` (x 0 to `length`, y ±10, z 0 to 3), `leg-left` (y −10 to −7, z 3 to 15) and
`leg-right` (y 7 to 10, z 3 to 15); the channel stays free.

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
"complexes.org generic" on the bottom's underside, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less one cut (the channel, `cutbox`), so the channel's faces are cut faces.
The AutoCAD gate (mech-r136): 1 solid, 10 edges picked and 10 filleted at r 0.5, 0 rejected, 0 short, 0 cut edges skipped; removed
219.8 of 219.9 mm³; STEP vs glb extents 0.0. Every bounding-box extreme lies on the uncut outer faces (y ±10, z 0 and 15, x 0 and `length`). Volume at the default length:
132 000 mm³ (132 × 1000).
Not drawn: grip fins, a reinforcement, a joint, the board.

## Outputs (out/)
`strip-rubber-u-20x15.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010638), our own design (mech-r136, unattended, 2026-11-12): solid EPDM U-channel 20 x 15, flat bottom 3, legs 3, clamping width 14, black, plain, cut to length |
