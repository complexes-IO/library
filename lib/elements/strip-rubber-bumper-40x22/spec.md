# strip-rubber-bumper-40x22 · v1.1 · Rubber bumping section, generic, solid EPDM, base 40 x 12 with a half-round crown D20, height 22, no fastening holes, black, plain, cut to length

**What** A rubber bumping section: the black rubber buffer strip a machine bonds or clamps along a frame's, a cart's or a guard's
edge, where a trolley, a door or a hand may strike it. A rectangular base 40 wide and 12 high with a half-round crown Ø20 on its centre
line, 22 high overall. Solid rubber (not sponge), no fastening holes: the host bonds or clamps it. One straight length, cut to length
by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber bumping section (ETIM 10.0 EC010644), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM
list (lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010639 (strip-rubber-bulb-30x18, mech-r137). Its class is
on file (7 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the strip's centre plane y = 0, the base's underside z = 0 (the face that lies on
the host). The run goes along +x; the base lies flat (z 0 to 12, y ±20), the crown's axis runs along x at z 12 (crown z 12 to 22 above
the base, y ±10). Extents x 0 to `length`, y ±20, z 0 to 22.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERBUMP` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010644 Rubber bumping section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element;
they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM, solid (lib/materials.csv `epdm`) |
| 2 | With fastening holes (EF006008) | no (the host bonds or clamps it) |
| 3 | Shape (EF000051) | rectangular base with a half-round crown (D crown, Ø20, on the centre line) |
| 4 | Width (EF000008) | 40 mm (y, the base) |
| 5 | Height (EF000040) | 22 mm (z, the base's underside to the crown's top) |
| 6 | IRHD hardness (EF022836) | not stated |
| 7 | Colour (EF000007) | black (the `M-GASKET` layer) |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, impact energy, compression, temperature or fire
figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it lies on | the base's underside, flat, 40 wide, bonded or clamped by the host; nothing drilled; a 10 flat each side of the crown for a clamping strip or bar | ETIM 10.0 EC010644 With fastening holes "no" above; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what strikes it | a trolley, a door or a hand meeting the crown's top at z 22; how far it squeezes is the host's assembly, not this element's | ETIM 10.0 EC010644 Shape / Height above; the striking part is the host's element |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | 40 × 12 | a 10 flat each side of the crown for a clamping bar; the end-face edges 40 and 12 clear the gate's 3 to 7 mm free-corner trap (mech-r69) |
| crown | half-round Ø20, its axis at z 12 on the base's upper face, so its lower half lies inside the base (its underside at z 2, never tangent to the bearing face) | a round striking face that turns a glancing blow |
| section area | 40 × 12 + π 10² / 2 = 480 + 157.08 = 637.08 mm² (asserted in element.py); about 637 080 mm³ at the default length | by hand, for the Blender volume |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other profiles (mech-r106 / r131) |
| hardness, impact energy, compression set, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; the crown's squeeze under a strike is not modelled, and laying it on is the host's
assembly, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `base` (x 0 to `length`, y ±20, z 0 to 12) and `crown` (y ±10, z 12 to 22).

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
No label: the strip's one layer, `M-GASKET`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as a base box and a round crown (`cyl`) whose lower half lies inside the base; the two
solids join along the crown's equator on the base's upper face. The AutoCAD gate (mech-r138, at 1.0; 1.1 changes no geometry): 2
solids (base and crown), 12 edges picked and 12 filleted at r 0.5, 0 rejected, 2 buried skipped; removed 228.0 of 228.2 mm³ (the gate's
summary line; the base's 10 edges alone are its solid 0 line, 221.3 of 221.5); STEP vs glb extents 0.0. The Blender gate's
body volume 789 019.3 mm³ is the two solids summed (480 000 + the whole crown cylinder's 314 159, so its lower half, inside the base,
counts twice) less the cylinder's tessellation (about 5 140): the solid strip is about 637 080 mm³ (Its own sizes). Every bounding-box extreme lies on uncut faces (y ±20 and z 0 on the
base, z 22 on the crown's top, x 0 and `length`).
Not drawn: fastening holes or a T-foot, grip ribs, a joint, the host.

## Outputs (out/)
`strip-rubber-bumper-40x22.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010644), our own design (mech-r138, unattended, 2026-11-12): solid EPDM base 40 x 12 with a half-round crown D20, height 22, no fastening holes, black, plain, cut to length |
| 1.1 | text only, no geometry (mech-r154, unattended, 2026-11-13): review strip-rubber-bumper-40x22-1.0 finding 1 (mech-r138): Notes quote the AutoCAD gate's summary, removed 228.0 of 228.2 mm³ (221.3 of 221.5 was the base's line alone); Decals "No label" (`M-GASKET` is not a printed layer) |
