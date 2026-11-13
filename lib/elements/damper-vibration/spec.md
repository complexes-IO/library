# damper-vibration · v1.3 · vibration damper, generic, rubber-metal, Ø50 × 40, M10 male studs both ends, 1000 N

**What** A cylindrical rubber-metal vibration damper: a machine mount that carries a machine, a pump, a compressor or a cabinet on
rubber, so the floor or frame takes less of its vibration. A rubber body bonded between two steel plates, an M10 male stud on
each: the lower one into the base (a tapped hole, or through a hole with a nut), the upper one through the machine's foot with a
nut. The rubber and the upper plate are the mechanism: under load the rubber compresses and the machine sinks on it.
**Class** device · **Baseline** our own design: generic vibration damper (ETIM 10.0 EC011696), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design inputs; the studs'
thread is derived (What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face (the lower plate's underside, which seats on the base) on the damper's axis.
The damper stands toward +z with its upper plate's top face at z = 40; the machine-side stud runs up to z = 65, the base-side stud
down to z = −25.
**Built with** toolkit 1.3 · AutoLISP command `VIBDAMPER` · no parameters.

## Class values
ETIM 10.0 class EC011696 Vibration damper (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | cylindrical rubber-metal mount: a rubber body bonded between two steel plates, a male threaded stud on each |
| 2 | Connection 1 (EF000321) | threaded stud, male: the base side (into a tapped hole, or through a hole with a nut) |
| 3 | Connection 2 (EF000322) | threaded stud, male: the machine side (through the machine's foot, with a nut) |
| 4 | Thread size (metric) (EF003563) | 10 (M10), both studs |
| 5 | Diameter (EF000551) | 50 mm: the rubber body (the plates Ø40) |
| 6 | Height (EF000040) | 40 mm: the lower plate's underside to the upper plate's top face, the studs not included (90 overall) |
| 7 | Shore hardness (EF022944) | 55 Shore A: the rubber |
| 8 | Stiffness (EF026398) | 200 N/mm: axial, in compression |
| 9 | Max. load capacity (EF000258) | 1000 N: axial, in compression, static; the rubber then compresses 5 mm (1000 / 200) |
| 10 | Load-carrying at pressure (EF025241) | yes |
| 11 | Load-carrying at pull (EF025242) | no: it carries its load in compression; no pull load is rated |
| 12 | Min. ambient temperature (EF020432) | −30 °C |
| 13 | Max. ambient temperature (EF020188) | 70 °C |

## What it meets
| figure | value | source |
|---|---|---|
| stud threads (both ends) | M10 male, 25 long | M10 is a class value (a design input). The thread, derived: M10 × 1.5 coarse, tolerance class 6g: major Ø 9.7352 to 9.9685, pitch Ø 8.861 to 8.9942, minor Ø d3 max 8.1282 (basic: H 1.299, d2 9.0257, d3 8.1597); derived: derive.thread(10.0, 1.5) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6g; ISO 261 pitch). The base's tapped hole or nut and the machine-side nut meet it. Both studs are modelled plain at the nominal Ø10 (the thread form is not drawn; the model is unchanged) |
| base-side stud tightening torque | M_A 62.3 N·m (preload F_M 25.98 kN): the stud's thread at 8.8, an upper bound. The plate bonded to the rubber, which carries the stud, is not rated, so this is not the damper's own tightening figure | derived: derive.torque(10, 1.5, '8.8', mu_G=0.12, mu_K=0.12, nu=0.7, d_w=40, d_h=11) (M_A = F_M (0.16 P + 0.58 mu_G d2 + mu_K D_Km / 2), ISO 16047 / VDI 2230 Part 1; F_M = nu R_eL,nom A_s, ISO 898-1 clause 4 designation and stress area; design: nu 0.7, mu_G 0.12, mu_K 0.12, d_w 40). design: property class 8.8 (ISO 898-1 clause 4 designation, R_eL,nom 640 MPa, the class the stud is made to; the choice is bounded by the joint's load, VDI 2230 Part 1: the mount's rated 1000 N (class value 9, EF000258) is compression on the base through the lower plate, so the stud carries only its own preload, and at 8.8 its yield load 640 MPa × A_s 58.0 mm² = 37.1 kN stands far over any load of this joint: the stud is never the joint's weakest member, which is what makes the derived torque the upper bound the value says). design: d_w 40 (the element's bearing face: the lower plate's underside Ø40, the mounting face). nu 0.7 and mu_G / mu_K 0.12 are design choices (derive's defaults); d_h 11 is the M10 medium clearance hole (ISO 273, lib/standards/holes.csv) |
| the machine's foot, the base | none in this element | a foot or base the studs pass through cuts an M10 clearance hole there, Ø11.0 medium (ISO 273, lib/standards/holes.csv), and its element or host places the nuts |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| plates | Ø40 × 4, zinc-plated steel, top and bottom, bonded to the rubber | each carries its stud and spreads the load; the rubber stands 5 beyond them all round |
| rubber | Ø50 × 32 between the plates, black | the body whose hardness and stiffness are the class values |
| studs | M10 × 25 at each end | through a foot or base plate with a nut, or into a tapped hole |
| compression at the rated load | 5 mm (1000 N at 200 N/mm, both class values) | the travel of `rubber` and `top` |
| damping, natural frequency, shear stiffness | not claimed | no ETIM feature of this class; no figure is stated |

## Mechanism
`rubber` (compress, origin the rubber's lower bonded face (0, 0, 4), axis +z, 0 to 5 mm): the binder squeezes the rubber toward
the lower plate; at 5 (the max. load capacity) its upper face stands at z 31. It is a spring the twin scales, so MOT-010 does not
sweep it (toolkit/v_geometry: compress nodes are soft).
`top` (translate, axis −z, 0 to 5 mm): the upper plate and the machine-side stud sink with the rubber's upper face. Its origin is
the stud's seat on the plate (0, 0, 40); its extras carry the machine-side connection for the twin: end machine, gender male,
thread M10, length 25. MOT-010 sweeps it through its travel (the rubber it sinks into is soft, so only the lower plate and stud
are in its way, 32 below).
`stud` (port, fixed): the base-side stud. Origin the mounting face (0, 0, 0), axis −z (out toward the base); unit M10, gender
male (PIN-002), thread M10, length 25.
One load moves both by the same value (both in mm): lib/motion.csv ties them, `damper-vibration,top,rubber,follow` (the core's
row, request mech-6 item 1, lib/requests/core/mech-6-answer.md). `top` leads and the rubber follows: a follower is never swept on
its own and a compress node never leads, so with `top` leading MOT-010 still sweeps the plate and its stud through 0 to 5, and
MOT-020 passes the pair (they touch at rest). The twin drives `top`; the rubber is squeezed by the same mm.

## Named nodes
`rubber` (compress) · `top` (translate) · `stud` (port). Colliders `body` (the lower plate), `rubber`, `top` (the upper plate),
`stud`.

## Materials by layer
`M-ZINC` plates and studs · `M-GASKET` rubber (black).

## Decals (Blender)
"complexes.org generic" moulded on the rubber's side.

## Notes
No vendor names, part numbers or marks. No safety claim. The class values are the figures this design is meant to meet; no
calculation or test of the model is on file. No open figure: the thread and the studs' tightening torque are derived (What it meets). The rest are
design choices.

## Outputs (out/)
`damper-vibration.lsp` · `.glb` (pivots on `rubber`, `top` and `stud`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011696), our own design (cloud-mech r2, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
| 1.1 | text only (review damper-vibration-1.0 finding 2, request mech-6 item 1): Mechanism names the lib/motion.csv follow row now on main (`top` leads, the rubber follows, one load) in place of "a question for a later version". No model change (mech-r62, 2026-11-09) |
| 1.2 | text only (review mech-r85 finding 1): element.py's header, BASELINE and comment and this file's Baseline line say the M10 thread is derived (as What it meets has since mech-r85), no longer an open figure; no geometry change (mech-r88, unattended) |
| 1.3 | text only (DOC-009, lib/requests/core/mech-doc009-2026-11-11.md item 1): the stud's property class 8.8, an input of the derived torque in What it meets, names the rule it meets (ISO 898-1 clause 4 designation; VDI 2230 Part 1, the joint's load: the rated 1000 N is compression through the plate, the stud carries only its preload) in place of "this design's choice"; no geometry change (mech-r106, unattended) |
