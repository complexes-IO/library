# threaded-sleeve-m8 · v1.0 · threaded sleeve, generic, steel zinc plated, round D14 tapped M8 through (thread drawn at its minor diameter), cut to length (default 20)

**What** A threaded sleeve: the plain round steel standoff tapped M8 right through, set between two parts (a panel and its frame, a
cover and its base, a guard and a bracket) to hold them a fixed distance apart, with an M8 screw driven into each end. Ø14 outside,
tapped M8 × 1.25 through, cut to length (default 20). Where spacer-sleeve-m8 lets one screw pass and a nut clamp both parts, this one
takes a screw from each side, so neither part needs a nut behind it. Placed by a host, never redrawn: a host sets the `length` it needs.
**Class** connector-part · **Baseline** our own design: generic threaded sleeve (ETIM 10.0 EC002350, whose synonyms name the adapter,
the distance holder, the sleeve and the spacer sleeve), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it.
It is the next class of group EG021006 Accessories/components for fasteners and anchoring systems that the lane builds, by name after
spacer-sleeve-m8 (mech-r145's list; the classes between are skipped there for the standards that shape them: square taper washers DIN
434 / 435, tab washer DIN 93, taper pin ISO 2339, threaded rod DIN 976; spring plate and the tolerance compensator are next). The class is in
lib/standards/etim/classes.csv (tier 2, 6 features); its features are not in class-features.csv (tier 1 and inventory classes only),
so the class values below are this design's under plain names, as spacer-sleeve-m8's are under the core's answers to mech-8 and
mech-9, until the features come (needs-em 226). No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: one end face (its seat on the lower part) z = 0, on the sleeve's axis. The axis runs along +z; the
other end face at z = `length`. Extents x ±7, y ±7, z 0 to 20 at the default length.
**Built with** toolkit 1.3 · AutoLISP command `THRDSLV` · parameter `length` (mm, default 20, 16 to 200).

## Class values
ETIM 10.0 class EC002350 Threaded sleeve (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md). Its 6 features are not on file
(class-features.csv holds tier 1 and inventory classes only), so the values are given under plain names, with the value this element is
designed to; when the features are on main, a 1.1 restates them in ETIM's order with their EF codes (the core's answer to mech-8). These
define the element; they are design inputs.

| # | feature (plain name) | value |
|---|---|---|
| 1 | Material | mild steel (lib/materials.csv `steel-mild`) |
| 2 | Surface protection | zinc plated (the `M-ZINC` layer; no coating thickness stated) |
| 3 | Thread | M8 × 1.25 internal, right through (ISO 261 coarse pitch; tolerance class 6H, ISO 965-1) |
| 4 | Outer diameter | 14 mm, round |
| 5 | Length | the `length` parameter, default 20 mm (16 to 200; a BOM row sets it) |
| 6 | Shape | round, plain (no hexagon, no flange, no slot) |

No ratings.csv: no value above is a rating the checks read, and no load, torque or temperature figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the M8 screws in it | one tapped bore through, on the sleeve's axis, drawn at the minor diameter 6.6468; a screw driven into each end | derived: derive.thread(8.0, 1.25) (ISO 68-1 basic profile; ISO 965-1 clause 10, internal 6H: D1 6.6468 to 6.9157, D2 7.1881 to 7.348; ISO 261 pitch 1.25). The screws (ISO 4762 / ISO 4017, inventory rows not built yet) are the host's, placed later |
| the two parts it spaces | the end faces z = 0 and z = `length`, each a ring Ø6.6468 to Ø14 | OPERATING.md 12, an own size: the host's faces bear on the rings; each part's clearance hole for M8 (ISO 273, lib/standards/holes.csv) is the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| outside | Ø14, round | spacer-sleeve-m8's outside, so a host can swap one for the other on the same ring; a wall of 3.0 outside the thread's nominal Ø8 |
| bore | M8 tapped through, drawn at Ø6.6468 (features.csv: M8 tapped through, kind own) | the thread's minor diameter, derived; the thread itself is not drawn (jaw-prism-125's way) |
| length | 20 by default, `length` 16 to 200 | 16 leaves at least one nominal diameter (8) of thread for the screw at each end (element.py asserts it); 20 stands a panel off a frame by a hand's grip; over 200 is a threaded rod's job |
| layer | `M-ZINC` (steel, zinc plated) | a design choice, no grade or coating-thickness claim |
| volume | π × 7² × 20 − π × 3.3234² × 20 = 3 078.8 − 694.0 = 2 384.8 mm³ at the default length | by hand, for the Blender volume (polygonal cylinders read a little less) |
| fillet radius | the gate's 0.5 | every edge a circle (Ø14 outside; the bore's edges are cut edges) |

## Mechanism
None: one fixed body, no moving node, no port. The screws in it and the parts it spaces are the host's assembly. behaviour.csv is
the header only.

## Named nodes
None. Collider, an axis-aligned box: `sleeve` (x ±7, y ±7, z 0 to `length`).

## Materials by layer
`M-ZINC` the whole sleeve (steel, zinc plated).

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default M-WHITE-PA,
M-BLACK-PA); M-ZINC is not one, and a sleeve Ø14 has no face a label would fit (needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. Drawn as one `cyl` less one through `hole`. Every bounding-box extreme lies on the cylinder's
own faces (z 0 and z = `length` the end rings, x and y ±7 the side). Not drawn: the thread, chamfers or countersinks at the bore's ends,
the screws. lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`threaded-sleeve-m8.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002350), our own design (mech-r146, unattended, 2026-11-13): a steel zinc plated sleeve Ø14 tapped M8 × 1.25 through (drawn at the derived minor diameter 6.6468), length a parameter, default 20 |
