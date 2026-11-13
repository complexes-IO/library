# chuck-zero-point-120 · v1.0 · zero-point clamping module, generic, flange Ø120 with 4 × M8 on Ø100, body Ø80, receiving bore Ø25, height 40

**What** A zero-point clamping module: the module bolted to a machine table or a fixture plate that takes a pallet's clamping nipple
in its receiving bore and holds it, so a pallet changed between machines comes back to the same point. A steel flange with four M8
holes carries the round body; the body's top face is the pallet's seat and its centre the receiving bore. The clamping slides, their
springs, the release piston and its air port are inside and are not drawn, so the module has no moving node and no port: the twin
places it as one fixed body. The first element of ETIM's "Zero-point clamping system" class in the library (`python lib/build.py
inventory mech` lists the class to build generic once no inventory row builds unattended: group EG020054 Clamping tools,
lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic zero-point clamping system (ETIM 10.0 EC004396), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). The class and its two features are on file (lib/standards/etim/classes.csv, class-features.csv). No
product was matched and no vendor file was opened. The class values below are the design inputs; the flange holes are on file
(ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: on the flange's underside (z = 0, the mounting face), on the module's axis (x = 0, y = 0). The
seat face is z = 40 and the receiving bore opens upward on the axis; the flange holes lie on the x and y axes. Extents x −60 to 60,
y −60 to 60 (the flange), z 0 to 40 (the seat face).
**Built with** toolkit 1.3 · AutoLISP command `ZEROPNT` · no parameters.

## Class values
ETIM 10.0 class EC004396 Zero-point clamping system (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Number of axles (EF015134) | not stated |
| 2 | Material (EF002169) | steel |

No clamping or pull-in force is designed or claimed (the slides and springs are not drawn or rated).

## What it meets
| figure | value | source |
|---|---|---|
| flange screws | 4 × M8, Ø9.0 holes on a Ø100 circle (x ±50 on y 0, y ±50 on x 0), each 5.5 outside the body and 5.5 inside the flange's rim | ISO 273 medium (H13), lib/standards/holes.csv. The screws are not built; the host places them |
| the pallet | seated on the top face z = 40 (Ø80), its clamping nipple in the receiving bore Ø25 × 18 | design: the module's own receiving bore (ETIM 10.0 EC004396, OPERATING.md 12); the pallet and its nipple are the pallet's and are not drawn |
| the table | the flange's underside z = 0, Ø120 | design: a flange-mounted module (OPERATING.md 12, an own size); nothing is placed under it |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four flange holes carry a declared position tolerance Ø0.8 at MMC to A (the mounting face) and B (the module's axis)
(features.csv; H − F = 9.0 − 8 = 1.0). The pattern is one bolt circle of four.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| flange (fixed) | Ø120 × 12 (z 0 to 12), 4 × Ø9.0 on a Ø100 circle | the holes outside the body by 5.5, so a screw head has room beside it |
| body (fixed) | Ø80 from the flange to the seat face z 40 | the pallet's seat |
| receiving bore | Ø25, 18 deep (z 22 to 40), on the axis | takes the pallet's nipple (features.csv, kind own); its floor 10 above the flange |
| layers | flange and body `M-SILVER` (bright steel) | a design choice, no finish claim |

## Mechanism
None drawn. The clamping slides that close on the nipple, the springs that hold them closed, the release piston and its air port are
internal mechanism the twin doesn't read: not drawn, not claimed, so the module has no node and its behaviour.csv is the header only.

## Named nodes
None (one fixed body). Colliders `flange`, `module` (axis-aligned boxes).

## Materials by layer
`M-SILVER` flange, body.

## Decals (Blender)
"complexes.org generic" on the body's −y face.

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force, no repeatability claimed. The class values are the figures
this design is meant to meet; no calculation or test of the model is on file. No open figure: the flange holes are on file, and the
screws and the pallet are placed by the host. The gate's fillet rule (r 0.5 for a device): every edge is a circle of Ø80 or Ø120; the
holes' and the bore's edges are cut edges. lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`chuck-zero-point-120.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004396), our own design (mech-r130, unattended, 2026-11-12): one flange-mounted zero-point clamping module, Ø120 flange with 4 × M8, receiving bore Ø25 |
