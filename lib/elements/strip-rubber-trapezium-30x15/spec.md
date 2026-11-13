# strip-rubber-trapezium-30x15 · v1.0 · Rubber trapezium section, generic, solid EPDM, base 30, top 20, height 15, symmetric, no hollow core, black, plain, cut to length

**What** A rubber multi-faced/trapezium section: the solid black wedge strip, buffer or filler a machine lays in a channel or bonds on
a frame. Base 30 wide, top 20 wide, height 15, symmetric about its centre plane; at each side of the base an upright land 2 high,
then the flank slopes in to the top face (six faces: a trapezium on a low rectangular foot). Solid through (no hollow core), not
self-adhesive: the host bonds or clamps it. One straight length, cut to length by the `length` parameter (default 1000; a parameter
stays out of the id, OPERATING.md 6).
**Class** rail · **Baseline** our own design: generic rubber multi-faced/trapezium section (ETIM 10.0 EC010641), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). No inventory row names it: it is the next class of EG019710 Profiles in `python lib/build.py
inventory mech`'s ETIM list (lib/toolkit/generic.py ORDER, by name) after EC010648 (strip-rubber-corner-30x30, mech-r139); the glass
carrier classes EC010645 / EC010646 between them by name are set aside (lib/needs-em/mech.md). Its class is on file (10 features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened. A rubber section's sizes are not fixed
by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the section's centre plane y = 0, the base's underside z = 0 (the face that lies
on the host). The run goes along +x; the top face is at z 15. Extents x 0 to `length`, y ±15, z 0 to 15.
**Built with** toolkit 1.3 · AutoLISP command `RUBBERTRAP` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC010641 Rubber multi-faced/trapezium section (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every
feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These
define the element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | EPDM (lib/materials.csv `epdm`) |
| 2 | Material structure (EF022835) | solid (not cellular) |
| 3 | Shape (EF000051) | trapezium on upright lands 2 high (six faces) |
| 4 | Asymmetrical (EF024260) | no (symmetric about y = 0) |
| 5 | Hollow core (EF022577) | no |
| 6 | Base width (EF022837) | 30 mm (y) |
| 7 | Height (EF000040) | 15 mm (z) |
| 8 | Top width (EF022848) | 20 mm (y) |
| 9 | IRHD hardness (EF022836) | not stated |
| 10 | Colour (EF000007) | black (the `M-GASKET` layer) |

No ratings.csv: no feature of the class is a rating the checks read, and no hardness, sealing, compression, temperature or fire figure
is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host it lies on | the base 30 wide, bonded or clamped by the host, or laid in a channel 30 wide; nothing drilled | ETIM 10.0 EC010641 Base width above; plain stock (OPERATING.md 12: a host takes the figures of what it meets from a standard or an element on file) |
| what closes or bears on it | the top face 20 wide, 15 above the base; the flanks at 68.96° to the base; how far a part squeezes it is the host's choice | this design's choice of section, ETIM 10.0 EC010641 Top width / Height above |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | base 30, top 20, height 15, lands 2; each flank runs in 5 over a rise of 13 (13.93 wide on the end face, 68.96° to the base); area 385 mm² (30 × 2 + (30 + 20) / 2 × 13, asserted in element.py); 385 000 mm³ at the default length | a wedge strip; the lands keep the flanks' cut planes off the box's lower edges, and at 2.0 their end edges are "short" in the gate's fillet pass (mech-r126); every other end-face edge is 13.93 or more, so no 3 to 7 mm free-corner edge is left (mech-r69) |
| corners | sharp (no radius drawn) | an extrusion's small radii are not drawn (appearance only) |
| length | 1000 default, a parameter | the host sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`, set per primitive) | as the other profiles (mech-r106 / r131) |
| hardness, compression set, temperature range, flammability | not claimed | lib/materials.csv epdm carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; its compression is the host's, not a motion. behaviour.csv is the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `foot` (x 0 to `length`, y ±15, z 0 to 2) and `core` (y ±10, z 2 to 15); the flanks' wedges
outside the core carry no collider.

## Materials by layer
`M-GASKET` the whole strip (EPDM, black).

## Decals (Blender)
"complexes.org generic" on the base's underside, centred.

## Notes
No vendor names, part numbers or marks. Drawn as one box less two oblique cuts (`P.cut`, one per flank, each a right-handed frame along
x, the flank and its outward normal, started 3 below the land's top corner so it crosses the box's side face above the land). The
AutoCAD gate (mech-r140): 1 solid, 6 edges picked and 6 filleted at r 0.5, 0 rejected, 2 cut edges skipped; removed 112.6 of 112.7
mm³; STEP vs glb extents 0.0. The Blender gate's body volume 385 000.0 mm³ (385 × 1000). Every
bounding-box extreme lies on uncut faces (y ±15 on the lands, z 0 on the base, z 15 on the top face, x 0 and `length`).
Not drawn: an adhesive or liner, a joint or splice, the host.

## Outputs (out/)
`strip-rubber-trapezium-30x15.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010641), our own design (mech-r140, unattended, 2026-11-12): solid EPDM trapezium section, base 30, top 20, height 15, lands 2, symmetric, no hollow core, black, plain, cut to length |
