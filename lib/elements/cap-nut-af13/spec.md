# cap-nut-af13 · v1.0 · Screw/nut cap, generic, soft PVC, grey, round D20 x 16, flat top, socket D15.2 x 14 for a hexagon of 13 across flats

**What** A screw/nut cap: the soft plastic cover pushed over a hexagon nut or a hexagon screw head, with the thread end that stands
past it, so a guard's or a frame's exposed fixing shows no sharp edge or bare thread. A round cap Ø20 and 16 high with a flat top 2
thick; inside, a round socket Ø15.2 and 14 deep that slips over a hexagon of 13 across flats at its corners. How the cap grips (ribs
or a snap bead inside the socket) is not drawn and not claimed.
**Class** connector-part · **Baseline** our own design: generic screw/nut cap (ETIM 10.0 EC002375, whose synonyms name the cover cap,
the protection cap and the hexagon cap), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: it is the first
tier-1 class of group EG020045 Fasteners and anchoring systems, in `python lib/build.py inventory mech`'s ETIM order
(lib/toolkit/generic.py ORDER), whose shape no dimensional standard fixes; the classes before it in the group are building-trade
anchors and nails, inventory rows, or screws, nuts, rivets, pins and washers a standard shapes (never generic, OPERATING.md 12; the
skips are in lib/needs-em/mech.md, mech-r143). Its class is on file (6 features, lib/standards/etim/class-features.csv). No product was
matched and no vendor file was opened. A cover cap's sizes are not fixed by a dimensional standard: every size is a design choice.
**Units / frame** mm, Z up. Origin: the cap's open end (its seat on the clamped part's face) z = 0, on the cap's axis. The axis runs
along +z; the flat top at z 14 to 16. Extents x ±10, y ±10, z 0 to 16.
**Built with** toolkit 1.3 · AutoLISP command `NUTCAP` · no parameters.

## Class values
ETIM 10.0 class EC002375 Screw/nut cap (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element; they
are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | PVC, soft (lib/materials.csv `pvc`) |
| 2 | Material quality (EF001257) | not stated (no compound or grade is named) |
| 3 | Diameter cap (EF001423) | 20 mm (the cap's outside) |
| 4 | Shape (EF000051) | round (a cylinder), over a hexagon socket's corners |
| 5 | Colour (EF000007) | grey (the `M-GREY-PVC` layer) |
| 6 | Round head (EF006173) | no: a flat top (the toolkit has no sphere solid for a domed head) |

No ratings.csv: no feature of the class is a rating the checks read, and no grip, temperature or fire figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the hexagon it covers | a nut or a screw head of 13 across flats; its corner circle Ø15.01 (by geometry: e = s / cos 30° for a regular hexagon); the nut or head and the thread end past it up to 14 high in all. Which screw size carries 13 across flats is the screw standards', not on file, so no screw size is claimed | OPERATING.md 12 (a generic's design input); the screw or nut is the host's element |
| the clamped part's face | the cap's open end, z = 0, seats on the face round the nut (a ring Ø15.2 to Ø20) | OPERATING.md 12, an own size: pushed on by hand, no fixing |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| cap | Ø20 × 16, round, flat top 2 thick (z 14 to 16) | the class value Diameter cap; a wall 2.4 round the socket |
| socket | round Ø15.2, 14 deep from the open end (features.csv: kind own, no fastener, no standard size) | 0.19 over the hexagon's corner circle (15.01), so it slips on; 14 deep for the nut or head and a short thread end |
| grip | not drawn | ribs or a snap bead inside the socket are internal detail the twin doesn't read; no pull-off force claimed |
| volume | π × 10² × 16 − π × 7.6² × 14 = 5 026.5 − 2 540.4 = 2 486.2 mm³ | by hand, for the Blender volume (polygonal cylinders read a little less) |
| fillet radius | the gate's 0.5 | every edge a circle 47 or longer; the socket's edges are cut edges |
| temperature range, flammability, UV resistance | not claimed | lib/materials.csv pvc carries no figures |

## Mechanism
None: one fixed body, no moving node, no port; pushing the cap on is the host's assembly, not a motion. behaviour.csv is the header
only.

## Named nodes
None. Collider, an axis-aligned box: `cap` (x ±10, y ±10, z 0 to 16).

## Materials by layer
`M-GREY-PVC` the whole cap (soft PVC, grey).

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default M-WHITE-PA,
M-BLACK-PA); M-GREY-PVC is not one, and a cap Ø20 has no face a label would fit (needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. Drawn as one `cyl` less one blind `hole` from the open end. Every bounding-box extreme lies on
the cylinder's own faces (z 0 the open end's ring, z 16 the top, x and y ±10 the side). Not drawn: the grip ribs, a dome, the nut, the
screw. lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`cap-nut-af13.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002375), our own design (mech-r143, unattended, 2026-11-13): a soft PVC cap Ø20 × 16, flat top, round socket Ø15.2 × 14 over a hexagon of 13 across flats, grey |
