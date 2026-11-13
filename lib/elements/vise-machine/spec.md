# vise-machine · v1.0 · machine vise, generic, jaws 125 × 40, opening 0 to 150, cast body 340 long, 4 × M12 bolting lugs

**What** A machine vise: bolted to a machine table (a drill, a mill, a saw), it holds a workpiece between a fixed jaw and a moving
jaw that a hand-turned spindle drives along the body. A cast body (base, fixed jaw block, rear end block and four bolting lugs),
two hardened jaw plates, and one moving jaw that slides on the base's top face. The moving jaw is the mechanism: the twin opens
and closes the vise by name.
**Class** device · **Baseline** our own design: generic machine vice (ETIM 10.0 EC002173), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No product was matched and no vendor file was opened. The folder's record (metadata.json,
references/source.txt) names a catalogue vise; no size was taken from it. The class values below are the design inputs; the
holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the base's underside (its seat on the machine table) at z = 0, the fixed jaw plate's
clamping face at x = 0, the jaws' centre at y = 0. The moving jaw opens toward +x; the spindle and its handle stand at the +x
end. The jaws' top edges at z = 110.
**Built with** toolkit 1.3 · AutoLISP command `VISEMACH` · no parameters.

## Class values
ETIM 10.0 class EC002173 Machine vice (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Jaw width (EF005637) | 125 mm: each jaw plate, across y |
| 2 | Jaw height (EF013800) | 40 mm: each jaw plate, z 70 to 110 |
| 3 | Max. cheeks opening (EF005976) | 150 mm: the jaws' faces apart at the end of the moving jaw's travel (1 at rest + 149 of travel) |
| 4 | Max. clamping force (EF021596) | not stated: no force is designed or claimed (the spindle, its nut and the handle's torque are not drawn or rated) |
| 5 | With turntable (EF005472) | no: the body bolts straight to the table |
| 6 | Type of excitation (EF001365) | manual: the spindle turned by its handle |
| 7 | Weight (EF000167) | not stated: lib/materials.csv holds no densities, so no mass is given (the solids' volumes are in the Blender gate's record) |

## What it meets
| figure | value | source |
|---|---|---|
| bolting holes | 4 × M12, Ø13.5 through the lugs at 230 × 130 (x −40 and 190, y ±65) | ISO 273 medium (H13), lib/standards/holes.csv. The T-bolts, nuts or clamps that hold it are the machine table's; nothing is placed in the holes |
| machine table | the base's underside, z = 0, 340 × 100 plus the lugs | a flat seat; the table's T-slots are the table's and the assembly places the bolts in them |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four lug holes carry a declared position tolerance Ø1.0 at MMC to A (the base's underside), B (the fixed jaw plate's clamping
face) and C (the jaws' centre plane) (features.csv; H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | 340 × 100 × 60 (x −90 to 250, y ±50, z 0 to 60) | its top face is the moving jaw's ways; long enough for the 150 opening and the rear end block |
| fixed jaw block | 72 × 120 × 40 on the base (x −90 to −18, z 60 to 100) | carries the fixed jaw plate on its +x face |
| jaw plates | 18 thick, 125 × 40, z 70 to 110; fixed x −18 to 0, moving x 1 to 19 at rest | they stand 10 above the ways and 2.5 beyond the jaw blocks each side, so no plate face lies in a block's face plane |
| moving jaw block | 61 × 120 × 40 on the ways (x 19 to 80 at rest, z 60 to 100) | carries the moving jaw plate; slides on the base's top face |
| rear end block | 20 × 80 × 40 (x 230 to 250, z 60 to 100) | the spindle's bearing; the moving jaw stops 1 short of it at the end of its travel |
| lugs | four, 40 × 30 × 20, two each side (x −60 to −20 and 170 to 210, y 50 to 80 and −80 to −50, z 0 to 20) | the bolting holes 8.25 from each lug's outer edge |
| spindle end and handle | spindle end Ø25 on the axis z 80 from x 250 to 298; T-handle Ø16 along y at x 288, y ±90 | the handle a hand's width behind the end block |
| layers | cast body M-CAST-BLUE; jaw plates, spindle end and handle M-SILVER (bright steel) | a design choice, no finish claim |

## Mechanism
`jaw` (translate along +x, 0 to 149, pivot (1, 0, 70) on the moving jaw plate's clamping face): 0 is closed, as built (the jaws
1 apart, so the solids never touch); 149 is open (the jaws 150 apart, the moving jaw block 1 short of the rear end block). The node
carries the moving jaw block and its plate. MOT-010 sweeps it through the full range: it slides on the base's top face, between
nothing else.
The spindle inside the body, its nut in the moving jaw, the guide ways' gibs and the swivel of a swivel-base vise are not drawn
(internal mechanism the twin doesn't read); the handle stays put in this model (its turning moves nothing the twin reads but the
jaw). A workpiece between the jaws sets the real stop in the assembly.

## Named nodes
`jaw` (translate). Colliders `base` (the base with its lugs), `fixed-jaw` (the fixed jaw block and plate), `end-block`.

## Materials by layer
`M-CAST-BLUE` base, jaw blocks, end block, lugs · `M-SILVER` jaw plates, spindle end, handle.

## Decals (Blender)
"complexes.org generic" on the base's −y side face, between the lugs.

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force, no accuracy (parallelism) claim. The class values are
the figures this design is meant to meet; no calculation or test of the model is on file. No open figure: the holes are on file,
and the bolts are the machine table's.

## Outputs (out/)
`vise-machine.lsp` · `.glb` (pivot on `jaw`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002173), our own design (mech-r85, unattended, 2026-11-09) |
