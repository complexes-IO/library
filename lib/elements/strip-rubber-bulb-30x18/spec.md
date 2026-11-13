# strip-rubber-bulb-30x18 · v1.0 · Rubber bulb section, generic, solid EPDM, base 30 x 3, hollow round centric bead D16 wall 3, height 18, black, plain, cut to length

**What** A rubber bulb section: the black rubber seal a machine lays along a frame or a cover's rebate, the base held flat and the
hollow bead pressed by the closing door or cover. A base 30 wide and 3 thick with a round hollow bead on its centre line: bead Ø16
outside, wall 3 (a Ø10 hollow core), 18 high overall. Solid rubber (not sponge), no reinforcement. One straight length, cut to length
by the `length` parameter (default 1000; a parameter stays out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber bulb section (ETIM 10.0 EC010639), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py inventory mech`'s ETIM list
(lib/toolkit/generic.py ORDER, by name) that builds unattended, after EC010647 (strip-rubber-angle-25x20, mech-r137). Its class is on
file (11 features, lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's
sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the bead's centre plane y = 0, the base's underside z = 0. The run goes along +x;
the base lies flat (z 0 to 3, y ±15), the bead's axis runs along x at z 10 (bead z 2 to 18, y ±8, core Ø10 z 5 to 15). Extents x 0 to
`length`, y ±15, z 0 to 18.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERBULB` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010639 Rubber bulb section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element;
they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM (lib/materials.csv `epdm`) |
| 2 | Material structure (EF022835) | solid (not cellular) |
| 3 | Bead shape (EF023016) | round (circular, Ø16 outside) |
| 4 | Hollow core (EF022577) | yes (Ø10, through) |
| 5 | Centric bead (EF023014) | yes (on the base's centre line, y 0) |
| 6 | Width (EF000008) | 30 mm (y, the base) |
| 7 | Base thickness (EF022838) | 3 mm (z) |
| 8 | Bead height (EF022843) | 15 mm (z, the base's upper face to the bead's crown; 18 overall from the base's underside) |
| 9 | Bead wall thickness (EF023015) | 3 mm (Ø16 outside, Ø10 core) |
| 10 | Colour (EF000007) | black (the `M-GASKET` layer) |
| 11 | IRHD hardness (EF022836) | not stated |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, sealing force, compression, temperature or fire
figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the face it seals against | a door's or cover's flat face closing onto the bead's crown at z 18; how far the bead is squeezed is the host's design, not this element's | ETIM 10.0 EC010639 Bead height / Hollow core above; the door is the host's element (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| the host it lies on | the base's underside, flat, 30 wide, with a 7 flat each side of the bead for a clip or bond; a host that bonds or clips it declares that in its own files | ETIM 10.0 EC010639 has no fixing feature; plain stock, as sold cut to length (OPERATING.md 12) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | 30 × 3 | a 7 flat each side of the bead to hold it down; the 3.0 base ends are "short" in the gate's fillet pass, and its other end-face edges are 30 long (mech-r69) |
| bead | round Ø16, wall 3, hollow core Ø10 through (features.csv: kind own, no fastener, no standard size); its axis at z 10, so it sinks 1 into the base and the two join along a band, not a tangent line | a door seal's soft crown; the wall as thick as the base |
| section area | 30 × 3 + π (8² − 5²) − the 1 deep segment of the bead inside the base, about 90 + 122.5 − 5.2 = 207.3 mm² (the segment: 8² acos(7/8) − 7 √(8² − 7²) = 32.34 − 27.11 = 5.23); about 207 300 mm³ at the default length | by hand, for the Blender volume |
| corners | sharp | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other thin-walled profiles (mech-r106 / r131) |
| hardness, sealing force, compression set, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; the bead's squeeze under a door is not modelled, and laying it in is the host's
assembly, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `base` (x 0 to `length`, y ±15, z 0 to 3) and `bead` (y ±8, z 3 to 18; boxes, so the core is
not a collider gap).

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
"complexes.org generic" on the base's upper face, beside the bead.

## Notes
No vendor names, part numbers or marks. Drawn as a base box and a round bead (`cyl`) 1 into it, the core a `hole` through the bead
only (it stays 2 above the base's upper face, asserted in element.py). The AutoCAD gate (mech-r137): 2 solids (base and bead), 8
edges picked and 8 filleted at r 0.5, 0 rejected, 4 short and 2 buried skipped; removed 223.1 of 223.2 mm³; STEP vs glb extents 0.0.
The Blender gate's body volume 210 516.7 mm³ is the two solids summed (90 000 + the ring's 122 522, so the 1 deep overlap of about
5 230 counts twice) less the ring's tessellation (about 2 000): the solid strip is about 207 300 mm³ (Its own sizes). Every
bounding-box extreme lies on uncut faces (y ±15 on the base, z 0 on the base and z 18 on the bead's crown, x 0 and `length`).
Not drawn: grip fins in the base, a sponge bead, a joint, the door.

## Outputs (out/)
`strip-rubber-bulb-30x18.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010639), our own design (mech-r137, unattended, 2026-11-12): solid EPDM base 30 x 3 with a hollow round centric bead D16 wall 3, height 18, black, plain, cut to length |
