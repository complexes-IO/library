# wire-guide-ceramic · v1.0 · ceramic wire guide, generic, flanged eyelet, bore 8, length 12, flange 24 × 4, shank 14 × 8

**What** A ceramic wire guide: a flanged eyelet of hard ceramic that a running wire, thread, strand or fine cable passes through
where it changes direction or leaves a reel, a spooler, a wire feeder or a winding machine, so the wire wears the ceramic and not
the machine's sheet or frame. The flange seats on the host's plate; the shank sits in the host's hole, bonded; the wire runs
through the bore along the axis. It is the first element of ETIM's "Ceramic wire guide" class in the library (`python lib/build.py
inventory mech` lists the class as the next mech class to build generic once no inventory row builds unattended; the two classes
above it, EC012003 Ball joint and EC011971 Cardan joint, are parts a dimensional standard shapes and wait for it: lib/needs-em/mech.md);
no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic ceramic wire guide (ETIM 10.0 EC010725), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). The class and its four features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was
matched and no vendor file was opened. The class values below are the design inputs; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the seating face (the flange's underside, z = 0, where it seats on the host's plate) on the bore's
axis. The bore runs along z. Extents x −12 to 12, y −12 to 12 (the flange), z −8 (the shank's end) to 4 (the flange's top face).
**Built with** toolkit 1.3 · AutoLISP command `WIREGUIDECER` · no parameters.

## Class values
ETIM 10.0 class EC010725 Ceramic wire guide (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | aluminium oxide ceramic (alumina) |
| 2 | Inner diameter (EF000065) | 8 mm: the bore, through |
| 3 | Length (EF001438) | 12 mm: the flange's top face to the shank's end, along the bore |
| 4 | Shape (EF000051) | flanged eyelet (a round flange on a round shank, a round bore) |

The class has no load, wire speed, surface finish or wear feature, so none is designed to or claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host's plate and hole | a Ø14.2 hole through a plate 8 or more thick (the shank's 8 inside it); the flange's 24 seats on the plate's face round the hole, 4.9 over its edge all round | design: a 0.1 radial gap each side of the shank's Ø14 for the adhesive that holds the guide (an adhesive-bonded joint with a clearance, not a fit ISO 286 tabulates; this design's choice, OPERATING.md 12); the hole, the plate and the adhesive are the host's |
| the wire | any wire, thread or cable under Ø8 | the bore, the class value; the wire is the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| flange | Ø24 × 4 | seats the guide on the host's face and takes the wire's pull toward the plate; 8 of ceramic round the bore |
| shank | Ø14 × 8, 0.5 into the flange (one solid) | locates the guide in the host's hole; a wall of 3 round the bore |
| bore | Ø8 through, 12 long | the class value; plain: the rounded entries real guides have at both ends are not drawn (no cone or torus primitive in the toolkit) |
| load, wire speed, surface finish, hardness, temperature range | not claimed | no feature of this class states one; no figure is on file |

## Mechanism
None: one fixed body, no moving node, no port. The wire is the host's; behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `body` (x ±12, y ±12, z −8 to 4).

## Materials by layer
`M-WHITE-PA` the guide, appearance only (white): the material is alumina ceramic (Class values, feature 1); lib/godot/qa/materials
holds no ceramic layer (lib/needs-em/mech.md).

## Notes
No vendor names, part numbers or marks. No load, speed, wear or safety claim. The drawn volume is about 2 437.9 mm³ (flange π 12² × 4
= 1 809.6; shank π 7² × 8 = 1 231.5; less the bore π 4² × 12 = 603.2); a sum of the primitives counts the shank's 0.5 inside the
flange twice (π 7² × 0.5 = 77.0 more), and a mesh's polygonal circles read a little off their true areas. Written as volume only:
lib/materials.csv gives no densities, so no mass is stated. No label: the part is too small for one. A ceramic wire guide is not a
part a dimensional standard shapes, so it is built generic to its ETIM class (OPERATING.md 12). The gate's fillet rule (r 0.5 for a
device): the flange's and the shank's outer edges are whole circles (no free corners); the bore's edges are cut edges, skipped. Every
bounding-box extreme lies on an uncut face: the flange's rim (x, y ±12) and top face z 4, the shank's end face z −8.

## Outputs (out/)
`wire-guide-ceramic.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010725), our own design (mech-r118, unattended, 2026-11-12): a flanged alumina eyelet, bore 8, length 12, flange 24 × 4, shank 14 × 8 |
