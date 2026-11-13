# strip-clamping-8x15 · v2.0 · Clamping strip section, generic, solid EPDM U-section 8 x 15, slot 12 deep (grip 1.6, lead-in 2.0 x 2), for sheet 2.0 to 2.5, black, plain, cut to length

**What** A clamping strip section: the black rubber U-strip a machine pushes on a sheet edge (a guard's opening, a cut-out, a cover's
rim) so the raw edge is covered and nothing catches on it. Outside 8 wide × 15 high, a slot 12 deep that takes the sheet edge: a
lead-in 2.0 wide and 2 deep at the mouth, then the grip, 1.6 wide, to the slot's bottom; the crown 3 over it. It grips by its own
interference: the grip is 0.4 narrower than the thinnest sheet it takes, so a 2.0 sheet spreads each wall 0.2 and a 2.5 sheet 0.45.
No steel reinforcement, no sponge seal. One straight length, cut to length by the `length` parameter (default 1000; a parameter stays
out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic clamping strip section (ETIM 10.0 EC010640), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010649 (strip-rubber-cellular-20x10, mech-r132); the
classes between them by name are mounting-rail and flooring parts of the building trade (lib/rounds/mech/r133.md). Its class is on
file (8 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the slot's centre plane y = 0, the slot's mouth z = 0 (the sheet enters from
below). The run goes along +x; the sheet edge seats at the slot's bottom, z 12; the crown's outer face is at z 15. Extents x 0 to
`length`, y ±4, z 0 to 15.
**Built with** toolkit 1.3 · AutoLISP command `STRIPCLMP` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010640 Clamping strip section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material profile (EF021540) | EPDM, solid (lib/materials.csv `epdm`) |
| 2 | Material reinforcement (EF022844) | none (the section grips by its own interference) |
| 3 | With sponge rubber seal (EF022845) | no |
| 4 | Height (EF000040) | 15 mm (z, the mouth to the crown's outer face) |
| 5 | Width (EF000008) | 8 mm (y, outside) |
| 6 | Min. clamping range (EF022846) | 2.0 mm (the lead-in's width; the 1.6 grip spreads each wall 0.2) |
| 7 | Max. clamping range (EF022847) | 2.5 mm (each wall spreads 0.45) |
| 8 | Colour (EF000007) | black (the `M-GASKET` layer) |

No ratings.csv: no feature of the class is a rating the checks read, and no holding force, hardness, temperature or fire figure is
claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the sheet edge it covers | a sheet 2.0 to 2.5 thick, its edge pushed 12 into the slot through the 2.0 lead-in; nothing drilled | ETIM 10.0 EC010640 Min. / Max. clamping range above; the sheet is the host's element (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the hosts on file | a host drawn in 2.0 sheet takes it at the bottom of its range, 0.2 interference each side (panel-operator: sheet T 2.0, its element.py); guard-panel's 1.5 infill is below the range and does not | ETIM 10.0 EC010640 Min. clamping range above; the host's own element.py |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 8 × 15 outside; slot 12 deep: lead-in 2.0 × 2 at the mouth (legs 3 there), grip 1.6 × 10 above it (walls 3.2); crown 3; area 100 mm² (8 × 15 − 2.0 × 2 − 1.6 × 10, asserted in element.py) | a light edge trim for 2 mm sheet; the legs' 3.0 ends, the crown, the 2.0 lead-in and the 1.6 slot bottom are "short" in the gate's fillet pass, the slot's edges are cut edges, and every other edge of the end face is 8 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| slot depth | 12 (2 lead-in + 10 grip) | covers the sheet edge with 12 of rubber on each face |
| lead-in | 2.0 wide (the thinnest sheet), 2 deep | the sheet enters square before it spreads the grip |
| clamping | interference only: the grip 1.6, 0.4 under the thinnest sheet; no reinforcement, no grip fins drawn | a plain rubber U; a 2.0 sheet spreads each wall 0.2, the largest (2.5) 0.45, under a seventh of the 3.2 wall (asserted in element.py: under a quarter) |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row; around a corner it is the host's to bend |
| holding force, hardness, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; pushing it on is the host's assembly, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `leg-left` / `leg-right` (x 0 to `length`, y −4 to −1 / 1 to 4, z 0 to 15), `crown` (y ±1,
z 12 to 15); the slot stays free (the grip's 0.2 of rubber each side of it, |y| 0.8 to 1, has no collider).

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
No label: the strip's one layer, `M-GASKET`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one box less two cuts (the lead-in and the grip slot, `cutbox`), so the slot's faces
are cut faces. Every bounding-box extreme lies on the uncut outer faces (y ±4, z 0 and 15, x 0 and `length`). Volume at the default
length: 100 000 mm³ (100 × 1000).
Not drawn: grip fins, a reinforcement, a sponge seal, a joint, the sheet.

## Outputs (out/)
`strip-clamping-8x15.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010640), our own design (mech-r133, unattended, 2026-11-12): solid EPDM U-section 8 x 15, slot 2.0 x 12 for sheet 2.0 to 2.5, black, plain, cut to length |
| 2.0 | review mech-r133 finding 1 (mech-r144, unattended, 2026-11-13): 1.0's slot was 2.0 over its whole depth, so a 2.0 sheet, the range's bottom, met it with no interference. The slot is now a 2.0 × 2 lead-in at the mouth and a 1.6 grip above it (a cut-out change, so a major, OPERATING.md 7): 0.2 interference each side at 2.0, 0.45 at 2.5; area 96 → 100 mm²; colliders' inner faces at the lead-in, \|y\| 1; Decals "No label". Range, extents, origin and id unchanged; nothing places it |
