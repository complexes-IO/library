# mat-vibration · v1.0 · vibration absorber mat, generic, NBR 500 × 500 × 16, ribbed both faces, ribs crossed for stacking

**What** A vibration absorber mat: the loose rubber pad laid under a machine's feet, a bench, a press or a cabinet, so the floor
takes less of its vibration and the machine doesn't walk on a smooth floor. A 500 × 500 sheet of nitrile rubber (NBR) 16 thick: a
10 core with 3 high ribs on both faces, the top ribs along x, the bottom ribs along y. The ribs give the rubber room to bulge under a
foot; crossed, they let two mats stack rib across rib for a thicker pad (the class's Stackable feature). It is cut to size or laid
whole; nothing fixes it. The first element of ETIM's "Vibration absorber mat" class in the library (`python lib/build.py inventory
mech` lists the class to build generic once no inventory row builds unattended; the machine-element classes above it wait for a
dimensional standard or a toolkit primitive: lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic vibration absorber mat (ETIM 10.0 EC011715), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). The class and its six features are on file (lib/standards/etim/classes.csv, class-features.csv). No
product was matched and no vendor file was opened. The class values below are the design inputs; every size is a design choice.
**Units / frame** mm, Z up. Origin: the floor face (the bottom ribs' underside, z = 0) at the mat's centre. x along the top ribs, y
along the bottom ribs. Extents x −250 to 250, y −250 to 250, z 0 to 16 (the top ribs' top face, where a foot stands).
**Built with** toolkit 1.3 · AutoLISP command `VIBMAT` · no parameters.

## Class values
ETIM 10.0 class EC011715 Vibration absorber mat (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Length (EF001438) | 500 mm (x) |
| 2 | Width (EF000008) | 500 mm (y) |
| 3 | Thickness (EF000125) | 16 mm unloaded: core 10, ribs 3 on each face |
| 4 | Max. load (EF005977) | not stated |
| 5 | Oil resistant (EF000022) | not stated (the material is NBR; no resistance test or rating is on file) |
| 6 | Stackable (EF006212) | yes: the top ribs run along x and the bottom ribs along y, so a mat laid on another rests rib across rib |

The class states no stiffness, deflection or damping figure and its Max. load is not stated here, so none is designed to or
claimed: the mat carries what its host's design gives it, and the twin draws it unloaded.

## What it meets
| figure | value | source |
|---|---|---|
| the floor | the bottom ribs' underside, z 0, laid loose | design: a loose mat, nothing fixes it (OPERATING.md 12, an own size); the floor is the host's |
| the machine's feet | the top ribs' top face, z 16, 500 × 500 | design: any foot inside the mat's plan (OPERATING.md 12, an own size); the feet and their load are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| core sheet | 500 × 500 × 10, NBR (`M-GASKET`) | carries the ribs; 10 thick, so its corner edges are clear of the gate's 3 to 7 fillet trap |
| ribs | 3 high × 10 wide, at 25 centres, 20 a face, full length; the outer ribs 7.5 in from the edges | the rubber bulges into the 15 gaps under a foot; 3 high, so their end edges are "short" for the gate |
| crossed faces | top ribs along x, bottom ribs along y | two mats stack rib across rib |
| load, deflection, stiffness, damping, natural frequency, hardness, temperature range | not claimed | the class states no figure for them; no calculation or test is on file |

## Mechanism
None: one fixed body, no moving node, no port. The mat is drawn unloaded; with no stiffness or load figure in the class or on file, a
loaded pose (the ribs pressed flat) has no figure to come from, so none is drawn. behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `body` (x ±250, y ±250, z 0 to 16).

## Materials by layer
`M-GASKET` the mat (black rubber).

## Decals (Blender)
"complexes.org generic" on the core's −y edge.

## Notes
No vendor names, part numbers or marks. No load, deflection, damping or safety claim. The drawn volume is 3 100 000 mm³ of rubber
(core 500 × 500 × 10 = 2 500 000; 40 ribs 500 × 10 × 3 = 15 000 each, 600 000); written as volume only: lib/materials.csv gives no
densities, so no mass is stated. A vibration absorber mat is not a part a dimensional standard shapes, so it is built generic to its
ETIM class (OPERATING.md 12). The gate's fillet rule (r 0.5 for a device): every free-corner edge is 3 or shorter (the ribs' heights,
skipped as short) or 10 or longer (the core's 10, the ribs' 10 widths, 500 lengths); no hole or cut. Every bounding-box extreme lies
on an uncut axis-aligned box face: the core's and ribs' ends at x ±250 and y ±250, the bottom ribs' z 0, the top ribs' z 16. The ribs
and the core are one material in one node, so their flush end faces are not a GEO-050 pair.

## Outputs (out/)
`mat-vibration.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011715), our own design (mech-r123, unattended, 2026-11-12): a 500 × 500 NBR mat, core 10, 3 high ribs on both faces at 25 centres, crossed for stacking |
