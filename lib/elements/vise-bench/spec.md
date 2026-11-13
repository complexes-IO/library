# vise-bench · v1.1 · bench vice, generic, jaws 125 × 50, opening 0 to 100, table foot 118 × 140 with 4 × M10 holes, slide bar 42 × 30

**What** A bench vice: the engineer's vice bolted to a workbench's top at its front edge, holding a workpiece between a fixed jaw
and a moving jaw that a hand-turned spindle drives. A cast body on a table foot (four bolting holes), two exchangeable steel jaw
plates, and one moving jaw: its block, its plate and a rectangular slide bar that runs back through a channel in the body, with the
spindle's front end and its T-handle. The moving jaw is the mechanism: the twin opens and closes the vice by name. The jaws stand
above the bench in front of its edge, so long work hangs down past it. Not the machine vice of vise-manual / vise-machine (ETIM
EC002173: low, bolted to a machine table under a drill); a BOM picks one or the other by id. The first element of ETIM's
"Bench-vice" class in the library (`python lib/build.py inventory mech` lists the class to build generic once no inventory row
builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic bench-vice (ETIM 10.0 EC002199), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its nine features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was
matched and no vendor file was opened. The class values below are the design inputs; the holes it meets are on file (ISO 273);
every other size is a design choice.
**Units / frame** mm, Z up. Origin: the table foot's underside (its seat on the bench top) at z = 0, the fixed jaw plate's clamping
face at x = 0, the jaws' centre at y = 0. The moving jaw opens toward +x, in front of the bench's edge (the foot ends at x −12). The
jaws' top edges at z = 150. Extents x −130 to 100, y −90 to 90 (the handle), z 0 to 150.
**Built with** toolkit 1.3 · AutoLISP command `VISEBNCH` · no parameters.

## Class values
ETIM 10.0 class EC002199 Bench-vice (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Jaw width (EF005637) | 125 mm: each jaw plate, across y |
| 2 | Jaw height (EF013800) | 50 mm: each jaw plate, z 100 to 150 |
| 3 | Max. clamping width (EF009059) | 100 mm: the jaws' faces apart at the end of the moving jaw's travel (1 at rest + 99 of travel) |
| 4 | Exchangeable jaws (EF006290) | yes: the jaw plates are separate steel plates on the jaw blocks' faces (their screws not drawn) |
| 5 | With turntable (EF005472) | no: the body stands straight on its table foot |
| 6 | Material (EF002169) | body, foot, moving jaw block and slide bar cast iron; jaw plates, spindle and handle steel |
| 7 | Table foot (EF008085) | yes: a foot 118 × 140 × 15 with four M10 holes, bolted to the bench top |
| 8 | Chain style model (EF012137) | no |
| 9 | Engineering vice (EF012138) | yes |

No clamping force is designed or claimed (the class states none, and the spindle, its nut and the handle's torque are not drawn or
rated).

## What it meets
| figure | value | source |
|---|---|---|
| bolting holes | 4 × M10, Ø11 through the table foot at 94 × 110 (x −118 and −24, y ±55) | ISO 273 medium (H13), lib/standards/holes.csv. The bolts, nuts and washers are the bench's; nothing is placed in the holes |
| the bench top | the foot's underside, z = 0, 118 × 140, its front edge at x −12 | design: the foot set at the bench's front edge so the jaws stand in front of it (OPERATING.md 12, an own size); the bench is the host's (bench-1800 is one) |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four foot holes carry a declared position tolerance Ø0.5 at MMC to A (the foot's underside), B (the fixed jaw plate's clamping
face) and C (the jaws' centre plane) (features.csv; H − F = 11 − 10 = 1.0).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| table foot | 118 × 140 × 15 (x −130 to −12, y ±70, z 0 to 15) | the holes 12 to 15 from its edges and 9.5 clear of the body's sides, room for a bolt's head and a spanner |
| body | 98 × 80 × 105 on the foot (x −110 to −12, y ±40, z 15 to 120), with a channel 44 × 32 right through it along x (y ±22, z 65 to 97) | carries the fixed jaw plate on its front face and guides the slide bar; the channel's walls 50 below and 23 above |
| jaw plates | 12 thick, 125 × 50, z 100 to 150; fixed x −12 to 0, moving x 1 to 13 at rest | they stand 30 above the body's top (z 120; their lower 20 on its front face) and 22.5 beyond the jaw blocks each side, so no plate face lies in a block's face plane; the slide bar passes 4 under them |
| moving jaw block | 50 × 80 × 80 (x 13 to 63 at rest, y ±40, z 60 to 140) | carries the moving jaw plate, the slide bar and the spindle's front end; it hangs in front of the bench, clear of everything |
| slide bar | 42 × 30 (y ±21, z 66 to 96), x −128 to 13 at rest | runs in the body's channel, 1 clear each side; closed, its tail stands 18 behind the body over the foot; open, 17 of it is still in the body |
| spindle front end and handle | Ø20 on the bar's axis z 81 from the block to x 100; T-handle Ø14 along y at x 90, y ±90 | a bench vice's handle is at its moving jaw and travels with it |
| layers | cast parts `M-CAST-BLUE`; jaw plates, spindle end and handle `M-SILVER` (bright steel) | a design choice, no finish claim |

## Mechanism
`jaw` (translate along +x, 0 to 99, pivot (1, 0, 100) on the moving jaw plate's clamping face): 0 is closed, as built (the jaws 1
apart, so the solids never touch); 99 is open (the jaws 100 apart). The node carries the moving jaw block, its plate, the slide
bar, the spindle's front end and the handle. MOT-010 sweeps it through the full range: the slide bar runs in the body's channel
(1 clear each side), and nothing else is in its path.
The spindle inside the slide bar, its nut in the body and the bar's gibs are not drawn (internal mechanism the twin doesn't read);
the handle doesn't turn in this model (its turning moves nothing the twin reads but the jaw). A workpiece between the jaws sets
the real stop in the assembly.

## Named nodes
`jaw` (translate). Colliders `foot`, `body`, `fixed-jaw` (axis-aligned boxes).

## Materials by layer
`M-CAST-BLUE` foot, body, moving jaw block, slide bar · `M-SILVER` jaw plates, spindle end, handle.

## Decals (Blender)
No label: the vice's layers, `M-CAST-BLUE` and `M-SILVER`, are not printed layers of the Blender gate (review mech-r125 finding 2's
reading).

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force, no accuracy (parallelism) claim. The class values are
the figures this design is meant to meet; no calculation or test of the model is on file. No open figure: the holes are on file,
and the bolts are the bench's. The gate's fillet rule (r 0.5 for a device): every box edge is 12 or longer; the holes' and the
channel's edges are cut edges, skipped. Not drawn: jaw serrations, the jaw plates' screws, a pipe jaw, an anvil face.
lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`vise-bench.lsp` · `.glb` (pivot on `jaw`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002199), our own design (mech-r124, unattended, 2026-11-12): a cast body on a table foot, jaws 125 × 50, opening 100, a slide bar in the body's channel |
| 1.1 | text only, the part unchanged (mech-r144, unattended, 2026-11-13): review vise-bench-1.0 finding 1, the jaw plates stand 30 above the body's top (z 100 to 150 against BZ1 120), not 20; note 1, Decals "No label" |
