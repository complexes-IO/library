# shock-buffer · v1.2 · shock buffer, generic, rubber, Ø40 × 34, M10 male stud

**What** A cylindrical rubber buffer: an end stop that takes the blow of a slide, carriage, door or arm at the end of its travel.
An elastomer pad bonded to a steel base plate, fixed by an M10 male stud into a tapped hole or through a plate with a nut. The pad
is the mechanism: the twin squeezes it by name when a moving part strikes it.
**Class** device · **Baseline** our own design: generic shock buffer (ETIM 10.0 EC011714), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design inputs; the stud's
thread is derived (What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face (the base plate's underside, which seats on the host) on the buffer's axis.
The buffer stands toward +z with its impact face up at z = 34; the stud points toward −z.
**Built with** toolkit 1.3 · AutoLISP command `SHOCKBUF` · no parameters.

## Class values
ETIM 10.0 class EC011714 Shock buffer (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | cylindrical rubber buffer: one male threaded stud, a flat impact face |
| 2 | Type of fastening (EF002442) | threaded stud, male: into a tapped hole, or through a plate with a nut |
| 3 | Size of attachment thread connection (metric) (EF023656) | 10 (M10) |
| 4 | Diameter (EF000551) | 40 mm |
| 5 | Height (EF000040) | 34 mm: the mounting face to the impact face, the stud not included |
| 6 | Width (EF000008) | not stated: a round buffer, given by its diameter |
| 7 | Length (EF001438) | not stated: a round buffer, given by its height; the stud adds 20 below the mounting face (54 overall) |

## What it meets
| figure | value | source |
|---|---|---|
| stud thread | M10 male, 20 long | M10 is a class value (a design input). The thread, derived: M10 × 1.5 coarse, tolerance class 6g: major Ø 9.7352 to 9.9685, pitch Ø 8.861 to 8.9942, minor Ø d3 max 8.1282 (basic: H 1.299, d2 9.0257, d3 8.1597); derived: derive.thread(10.0, 1.5) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6g; ISO 261 pitch). The host's tapped hole or nut meets it. The stud is modelled plain at the nominal Ø10 (the thread form is not drawn; the model is unchanged). A host that takes the stud through a plate cuts an M10 clearance hole there (ISO 273, lib/standards/holes.csv) and places the nut |
| stud tightening torque | M_A 62.3 N·m (preload F_M 25.98 kN): the stud's thread at 8.8, an upper bound. The plate bonded to the rubber, which carries the stud, is not rated, so this is not the buffer's own tightening figure | derived: derive.torque(10, 1.5, '8.8', mu_G=0.12, mu_K=0.12, nu=0.7, d_w=40, d_h=11) (M_A = F_M (0.16 P + 0.58 mu_G d2 + mu_K D_Km / 2), ISO 16047 / VDI 2230 Part 1; F_M = nu R_eL,nom A_s, ISO 898-1 clause 4 designation and stress area; design: nu 0.7, mu_G 0.12, mu_K 0.12, d_w 40). design: property class 8.8 (ISO 898-1 clause 4 designation, R_eL,nom 640 MPa, the class the stud is made to; the choice is bounded by the joint's load, VDI 2230 Part 1: a blow on the impact face is compression on the host through the base plate, so the stud carries only its own preload, and at 8.8 its yield load 640 MPa × A_s 58.0 mm² = 37.1 kN stands far over any load of this joint: the stud is never the joint's weakest member, which is what makes the derived torque the upper bound the value says). design: d_w 40 (the element's bearing face: the base plate's underside Ø40, the mounting face). nu 0.7 and mu_G / mu_K 0.12 are design choices (derive's defaults); d_h 11 is the M10 medium clearance hole (ISO 273, lib/standards/holes.csv) |
| what strikes it | none in this element | the moving part that meets the impact face is the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate | Ø40 × 4, zinc-plated steel, bonded to the pad | it carries the stud and spreads the load on the host |
| pad | Ø40 × 30, elastomer (black rubber) | |
| stud | M10 × 20 | stud length |
| pad travel under a blow | 7.5 (25 % of the pad's 30) | the compress pivot's range |
| energy absorbed, force at full travel, hardness | not claimed | no ETIM feature of this class; no figure is stated |

## Mechanism
`pad` (compress, origin the pad's bonded face (0, 0, 4), axis +z, 0 to 7.5 mm): the binder squeezes the pad toward the base
plate; at 7.5 the impact face stands at z 26.5. It is a spring the twin scales, so MOT-010 does not sweep it (toolkit/v_geometry:
compress nodes are soft).
`stud` (port, fixed): origin the mounting face (0, 0, 0), axis −z (out toward the host); unit M10, gender male (PIN-002), thread
M10, length 20.

## Named nodes
`pad` (compress) · `stud` (port). Colliders `body` (the base plate), `pad`, `stud`.

## Materials by layer
`M-ZINC` base plate and stud · `M-GASKET` pad (black rubber).

## Decals (Blender)
"complexes.org generic" moulded on the pad's side.

## Notes
No vendor names, part numbers or marks. No safety claim: an end stop is not a safety device here. The class values are the
figures this design is meant to meet; no calculation or test of the model is on file. No open figure: the thread and the
stud's tightening torque are derived (What it meets). The rest are design choices.

## Outputs (out/)
`shock-buffer.lsp` · `.glb` (pivots on `pad` and `stud`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011714), our own design (cloud-mech, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
| 1.1 | text only: element.py's header, BASELINE and comment and this file's Baseline line say the M10 thread is derived (as What it meets has since mech-r85), no longer an open figure; no geometry change (mech-r87, unattended) |
| 1.2 | text only (DOC-009, lib/requests/core/mech-doc009-2026-11-11.md item 1): the stud's property class 8.8, an input of the derived torque in What it meets, names the rule it meets (ISO 898-1 clause 4 designation; VDI 2230 Part 1, the joint's load: a blow is compression through the base plate, the stud carries only its preload) in place of "this design's choice"; no geometry change (mech-r106, unattended) |
