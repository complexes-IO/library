# plunger-spring · v1.1 · spring plunger, generic, M8 × 16, slotted, thrust pin Ø4, travel 2, 10 to 30 N

**What** A spring plunger: a threaded steel body with a spring-loaded thrust pin standing out of its front face. Screwed into a
tapped hole in a fixture, a slide or a guard, it locates a part, holds it in a detent, or pushes it off. A screwdriver sets it
by the slot in its rear face. The pin is the mechanism: the twin presses it in by name when a part rides over it.
**Class** device · **Baseline** our own design: generic spring plunger (ETIM 10.0 EC011996), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design inputs; the body's
thread is derived and the slot's fit, which no file gives, is open (What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the front face (the face the pin stands out of) on the plunger's axis. The threaded body runs
toward −z to its slotted rear face at z = −16; the pin stands toward +z, its end at z = 2 at rest.
**Built with** toolkit 1.3 · AutoLISP command `SPRPLUNGER` · no parameters.

## Class values
ETIM 10.0 class EC011996 Spring plunger (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | steel: the body zinc-plated, the thrust pin hardened |
| 2 | Screwing system (EF000013) | slot in the rear face (a screwdriver) |
| 3 | With ball (EF009150) | no: a cylindrical thrust pin with a flat end |
| 4 | Double-sided (EF001067) | no: one pin, at the front face |
| 5 | Thread size (metric) (EF003563) | 8 (M8), over the body's full length |
| 6 | Diameter (EF000551) | 4 mm: the thrust pin (the body is given by its thread size) |
| 7 | Length (EF001438) | 16 mm: the threaded body, rear face to front face; the pin stands 2 beyond it at rest (18 overall) |
| 8 | Spring force (EF025825) | 10 to 30 N: 10 on the pin at rest, 30 pressed in flush (2 of travel) |

## What it meets
| figure | value | source |
|---|---|---|
| body thread | M8 male, 16 long (the whole body) | M8 is a class value (a design input). The thread, derived: M8 × 1.25 coarse, tolerance class 6g: major Ø 7.7652 to 7.9713, pitch Ø 7.0382 to 7.1594, minor Ø d3 max 6.4377 (basic: H 1.0825, d2 7.1881, d3 6.4664); derived: derive.thread(8.0, 1.25) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6g; ISO 261 pitch). The host's tapped hole meets it. The body is modelled plain at the nominal Ø8 (the thread form is not drawn; the model is unchanged) |
| screwdriver slot | 1.2 wide × 2.0 deep, across the rear face | the blade it takes is **NOT ON FILE (B)** (a fit: no screwdriver-blade or slot-size table is in lib/standards/). The slot is modelled at these sizes as a design choice; closed when such a table is on file: cite it, a minor version if the slot changes |
| what rides over the pin | none in this element | the part it locates or holds (its detent hole or groove) is the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| pin | Ø4 × 8, 2 proud of the front face at rest, 6 inside | presses in flush: its travel 2 |
| pin bore | Ø4.2, 9 deep from the front face (features.csv) | 0.1 radial clearance round the pin; 1 below the pin's inner end at full travel |
| spring, the pin's retaining collar, the crimped front edge | not modelled | inside the bore; the twin reads the pin's travel only |
| slot | 1.2 × 2.0, across the full Ø8 | 5 of solid body between the slot's floor (z −14) and the bore's bottom (z −9) |

## Mechanism
`pin` (translate, axis −z, 0 to 2 mm): 0 is at rest, as built (2 proud); 2 is pressed in flush with the front face. The pivot's
origin is the pin's end (0, 0, 2). The spring force (a class value) runs from 10 N at 0 to 30 N at 2. MOT-010 sweeps it through
its travel in its bore.
`self` (port, fixed): the threaded body. Origin the front face (0, 0, 0), axis −z (into the host's tapped hole); unit M8, gender
male (PIN-002), thread M8, length 16. Placed, it takes the BOM tag; the pin becomes `<tag>.pin`.

## Named nodes
`self` (port) · `pin` (translate). Colliders `self` (the body), `pin` (the pin's part outside the body at rest).

## Materials by layer
`M-ZINC` body and pin.

## Decals (Blender)
"complexes.org generic" laser-marked on the rear face, either side of the slot (small: the body is Ø8 and threaded over its
full length, so no side face stays in view once it is fitted).

## Notes
No vendor names, part numbers or marks. No safety claim: a plunger that locates a guard is not an interlock here. The class
values are the figures this design is meant to meet; no calculation or test of the model is on file. The thread is derived (What it
meets). One figure waits on a source, class B: the slot's screwdriver fit (What it meets). The body's tightening torque is not
claimed (behaviour.csv `pin` row, lib/behaviour.md, request mech-10's answer 2): the body is threaded over its whole length and has
no head, shoulder or collar, so no face of its own bears and derive.torque has no d_w to take; the lock nut or the stop that sets it
is the host's, and the host's figure is the host's. The rest are design choices.

## Outputs (out/)
`plunger-spring.lsp` · `.glb` (pivots on `self` and `pin`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011996), our own design (cloud-mech r2, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
| 1.1 | text only (mech-r89, review mech-r85 finding 1): element.py's header, BASELINE and the BODY_D comment say the M8 thread is derived (derive.thread, ISO 68-1 / ISO 965-1), as "What it meets" has had it since mech-r85; the slot's fit stays open, class B. Model unchanged |
