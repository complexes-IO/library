# knob-knurled · v1.2 · knurled knob, generic, Ø32 × 22, PA black, M6 × 20 male stud

**What** A knurled knob: a hand-turned clamping knob that holds a cover, a guide, a fence or an adjustable stop without a tool.
A moulded polyamide knob (a knurled grip over a plain collar) on a moulded-in M6 steel stud, screwed into a tapped hole in the
host or through a hole into a nut. The collar's underside seats on the work and clamps it.
**Class** device · **Baseline** our own design: generic knurled knob (ETIM 10.0 EC011970), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design inputs; the stud's
thread is derived (What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the collar's underside (the face that seats on the work) on the knob's axis. The knob stands
toward +z with its top face at z = 22; the stud points toward −z, to z = −20.
**Built with** toolkit 1.3 · AutoLISP command `KNOBKNURL` · no parameters.

## Class values
ETIM 10.0 class EC011970 Knurled knob (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | knurled knob with a threaded stud (male), moulded in |
| 2 | Type of button (EF001546) | round, straight-knurled grip over a plain collar |
| 3 | Diameter (EF000551) | 32 mm, over the knurl ridges (the grip's core Ø30, the collar Ø20) |
| 4 | Thread size (metric) (EF003563) | 6 (M6) |
| 5 | Total height (EF001761) | 22 mm: the collar's seating face to the knob's top face, the stud not included (42 overall) |
| 6 | Thread length (EF000368) | 20 mm: the stud below the seating face |
| 7 | Material (EF002169) | plastic (the knob), steel (the stud) |
| 8 | Material quality (EF001257) | knob polyamide 66, glass filled (lib/materials.csv pa66-gf); stud steel, zinc-plated, property class 8.8 (ISO 898-1 clause 4; What it meets, the torque row; the layer steel-mild is its appearance in lib/materials.csv) |
| 9 | Colour (EF000007) | black |

## What it meets
| figure | value | source |
|---|---|---|
| stud thread | M6 male, 20 long | M6 is a class value (a design input). The thread, derived: M6 × 1 coarse, tolerance class 6g: major Ø 5.7972 to 5.974, pitch Ø 5.2168 to 5.3245, minor Ø d3 max 4.7471 (basic: H 0.866, d2 5.3505, d3 4.7731); derived: derive.thread(6.0, 1.0) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6g; ISO 261 pitch). The host's tapped hole or nut meets it. The stud is modelled plain at the nominal Ø6 (the thread form is not drawn; the model is unchanged) |
| stud tightening torque | M_A 12.0 N·m (preload F_M 9.02 kN), the upper bound the stud's thread allows | derived: derive.torque(6, 1, '8.8', mu_G=0.12, mu_K=0.12, nu=0.7, d_w=20, d_h=6.6) (M_A = F_M (0.16 P + 0.58 mu_G d2 + mu_K D_Km / 2), ISO 16047 / VDI 2230 Part 1; F_M = nu R_eL,nom A_s, ISO 898-1 clause 4 designation and stress area; design: nu 0.7, mu_G 0.12, mu_K 0.12, d_w 20). design: property class 8.8 (ISO 898-1 clause 4 designation, R_eL,nom 640 MPa, the class the stud is made to; the choice is bounded by the joint's load, VDI 2230 Part 1: a clamping knob carries no working load of its own, so the stud's only load is the preload the knob is turned to, the clamped part's load being the host's; at 8.8 its yield load 640 MPa × A_s 20.12 mm² = 12.9 kN stands over the preload F_M 9.02 kN the derived torque gives (nu 0.7), so the stud is never the joint's weakest member, which is what makes the derived torque the upper bound the value says). design: d_w 20 (the element's bearing face: the collar's underside Ø20, the seating face). nu 0.7 and mu_G / mu_K 0.12 are design choices (derive's defaults); d_h 6.6 is the M6 medium clearance hole (ISO 273, lib/standards/holes.csv). It is the stud's figure: what a hand puts on the Ø32 grip is not claimed (Its own sizes) |
| the clamped part | none in this element | a part the knob clamps takes the stud through an M6 clearance hole, Ø6.6 medium (ISO 273, lib/standards/holes.csv), cut by that part's element; a nut, if used, is placed by the host |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| collar | Ø20 × 6, plain | its underside is the seating face: a flat ring round the stud that clamps the work; the hand stays above it |
| grip | core Ø30 × 16 (z 6 to 22), 30 straight knurl ridges 1.2 wide standing 1.0 proud (Ø32 over them), each 15 long, stopping 0.5 short of the grip's faces | a grip a hand can turn; the ridges stop short of the faces so no two faces lie in one plane (GEO-050). The ridges are moulded, not a cut knurl (appearance, class C) |
| stud | M6 × 20, moulded into the knob | the stud below the seating face; the part held inside the knob is not modelled |
| hand torque on the grip, clamping force | not claimed | no ETIM feature of this class; no figure is stated. The stud's own tightening torque is derived (What it meets) |

## Mechanism
No part moves inside the element: the knob and its stud are one part, and turning the knob screws the whole element into its
host or out of it. How far a turn moves it is the thread's pitch (M6 × 1, What it meets); no moving node is
declared for it: a host that animates the knob places it and moves it as a whole.
`stud` (port, fixed): origin the seating face (0, 0, 0), axis −z (into the host); unit M6, gender male (PIN-002), thread M6,
length 20.

## Named nodes
`stud` (port). Colliders `body` (the collar and grip), `stud`.

## Materials by layer
`M-BLACK-PA` collar, grip and knurl ridges · `M-ZINC` stud.

## Decals (Blender)
"complexes.org generic" moulded on the knob's top face.

## Notes
No vendor names, part numbers or marks. No safety claim. The class values are the figures this design is meant to meet; no
calculation or test of the model is on file. No open figure: the thread and the stud's tightening torque are derived (What it meets). The rest are
design choices. An all-steel knurled thumb screw or knurled nut is a screw or a nut, built from its dimensional standard once that
is on file, never generic (OPERATING.md 12): this element is a moulded knob on a stud, and no dimensional standard fixes its shape.

## Outputs (out/)
`knob-knurled.lsp` · `.glb` (pivot on `stud`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011970), our own design (cloud-mech r2, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
| 1.1 | text only: element.py's header, BASELINE and comment and this file's Baseline line say the M6 thread is derived (as What it meets has since mech-r85), no longer an open figure; no geometry change (mech-r87, unattended) |
| 1.2 | text only (DOC-009, lib/requests/core/mech-doc009-2026-11-11.md item 1): the stud's property class 8.8, an input of the derived torque in What it meets, names the rule it meets (ISO 898-1 clause 4 designation; VDI 2230 Part 1, the joint's load: the stud carries only the preload the knob is turned to, under its 12.9 kN yield load) in place of "this design's choice"; the Material quality class value names the class to match; torque, model and behaviour.csv unchanged (mech-r107, unattended) |
