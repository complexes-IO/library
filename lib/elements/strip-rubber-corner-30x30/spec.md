# strip-rubber-corner-30x30 · v1.0 · Rubber corner guard section, generic, solid EPDM, legs 30 x 30 x 3 with a corner bead D16, not self-adhesive, black, plain, cut to length

**What** A rubber corner guard section: the black rubber angle a machine bonds or clamps over a frame's, a guard's or a cart's square
outside edge, where a person or a load may strike it. Two legs 3 thick lie on the host's two faces, 30 wide each from the host's
corner line (mounting widths 1 and 2), and a round bead Ø16 runs along the outer corner and takes the blow. Solid rubber, no hollow
core, not self-adhesive, no fastening holes: the host bonds or clamps it. One straight length, cut to length by the `length` parameter
(default 1000; a parameter stays out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber corner guard section (ETIM 10.0 EC010648), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: it is a class of EG019710 Profiles in `python lib/build.py inventory mech`'s
ETIM list (lib/toolkit/generic.py ORDER, by name) that builds unattended, beside EC010643 (strip-rubber-cord-10, mech-r139). Its class
is on file (8 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber
section's sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the host's corner line along +x at y = 0, z = 0; the host fills y < 0, z < 0.
Leg 1 lies on the host's top face (z 0 to 3, y -30 to 3), leg 2 on its side face (y 0 to 3, z -30 to 3); the bead's axis runs along
x at y = z = 6 (bead y and z -2 to 14). Extents x 0 to `length`, y -30 to 14, z -30 to 14.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERCORNER` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010648 Rubber corner guard section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the
element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM, solid (lib/materials.csv `epdm`) |
| 2 | Diameter (EF000551) | 16 mm (the corner bead) |
| 3 | Mounting width 1 (EF023017) | 30 mm (leg 1, on the host's top face, from the corner line) |
| 4 | Mounting width 2 (EF023018) | 30 mm (leg 2, on the host's side face, from the corner line) |
| 5 | Self-adhesive (EF000434) | no (the host bonds or clamps it) |
| 6 | Hollow core (EF022577) | no |
| 7 | IRHD hardness (EF022836) | not stated |
| 8 | Colour (EF000007) | black (the `M-GASKET` layer) |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, impact energy, compression, temperature or fire
figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host's edge it covers | a square (90°) outside edge; the legs' inner faces lie on the host's two faces, 30 each from the corner line, bonded or clamped by the host; nothing drilled | ETIM 10.0 EC010648 Mounting width 1 / 2 above; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what strikes it | a person or a load meeting the bead (its crown 14 out from the host's faces on the diagonal); how far it squeezes is the host's assembly, not this element's | ETIM 10.0 EC010648 Diameter above; the striking part is the host's element |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| legs | 3 thick, 30 wide from the corner line (the angle 33 × 33 outside) | the leg end faces' 3 edges sit at the gate's short-edge limit, which skips them (mech-r126); 30 leaves room for a clamping strip or a bond line |
| bead | Ø16, its axis at y = z = 6 on the corner's diagonal | it covers the angle's outer corner (the corner (3, 3) is 4.2 from its axis, inside it) and stands 11 proud of the legs' outer faces; its axis is 8.49 from the host's corner, more than its radius 8, so it never reaches into the host (asserted in element.py); where it crosses the planes y = 0 and z = 0 it lies 0.71 or more outside the host |
| inside corner | sharp, the host's corner line | the legs meet on the host's corner |
| section | the angle 33² − 30² = 189 mm² and the bead π 8² = 201.06 mm², joined where they overlap (the overlap not computed) | by hand, for the Blender volume (summed: 390.06 mm², about 390 060 mm³ at the default length, more than the solid) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other profiles (mech-r106 / r131) |
| hardness, impact energy, compression set, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; the bead's squeeze under a strike is not modelled, and laying it on is the host's
assembly, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `leg-1` (y -30 to 0, z 0 to 3), `leg-2` (y 0 to 3, z -30 to 0) and `bead` (y and z -2 to 14),
each x 0 to `length`.

## Materials by layer
`M-GASKET` the whole section (EPDM, black).

## Decals (Blender)
"complexes.org generic" on leg 1's outer face.

## Notes
No vendor names, part numbers or marks. Drawn as one box with the host's quadrant cut out (`cutbox`), which leaves the angle, and a
round bead (`cyl`) along its outer corner; the two solids overlap where the bead covers the corner. The cut doesn't change the box's
extents (y -30 and z -30 stay on the legs' end faces); y 14 and z 14 lie on the uncut bead. The AutoCAD gate (mech-r139): 2 solids
(the angle and the bead), 8 edges picked and 8 filleted at r 0.5, 0 rejected, 1 buried and 1 cut skipped; removed 119.6 of 119.8 mm³;
STEP vs glb extents 0.0. The Blender gate's body volume 386 771.2 mm³ is the two solids summed (189 000 + 201 062, so the overlap
counts twice) less the bead's tessellation (about 3 290); the solid section is smaller by the overlap. Godot QA 400 triangles, 3
colliders.
Not drawn: a self-adhesive tape, fastening holes, a mitre or a joint, the host.

## Outputs (out/)
`strip-rubber-corner-30x30.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010648), our own design (mech-r139, unattended, 2026-11-12): solid EPDM legs 30 x 30 x 3 with a corner bead D16, not self-adhesive, no hollow core, black, plain, cut to length |
