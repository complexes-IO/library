# gas-spring · v1.2 · gas spring, generic, rod Ø8, tube Ø18, stroke 100, 280 extended, M8 male both ends

**What** A gas compression spring: a sealed steel tube whose gas charge pushes a Ø8 piston rod out. It holds lids, guards and
hoods open and balances flaps on machines and benches. An M8 male stud at each end takes an end fitting (eye, ball socket,
clevis), which a host places. The rod is the mechanism: the twin slides it into the tube by name.
**Class** actuator · **Baseline** our own design: generic gas spring (ETIM 10.0 EC012096), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design inputs; what it
meets comes from what is on file, and the studs' thread is derived (What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the cylinder end's shoulder (the face its end fitting seats on), on the spring's axis. The
axis runs along +x: the cylinder-end stud toward −x, the tube from x = 0 to 150, the rod out toward +x to x = 268 at full
extension.
**Built with** toolkit 1.3 · AutoLISP command `GASSPRING` · no parameters.

## Class values
ETIM 10.0 class EC012096 Gas spring (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | gas compression spring: the gas pushes the rod out |
| 2 | Lockable gas spring (EF026003) | no |
| 3 | Material (EF002169) | steel (tube and rod) |
| 4 | Connection piston rod (EF025989) | external thread (male stud) |
| 5 | Thread size connection piston rod (EF026403) | M8 |
| 6 | Connection cylinder (EF025991) | external thread (male stud) |
| 7 | Thread size connection cylinder (EF026404) | M8 |
| 8 | Stroke (EF025993) | 100 mm |
| 9 | Pressure (EF007105) | 400 N: the force pushing the rod out at full extension (ETIM states this feature in N, as a force) |
| 10 | Outer diameter piston rod (EF025995) | 8 mm |
| 11 | Outer diameter cylinder (EF025996) | 18 mm |
| 12 | Cylinder length (EF025994) | 150 mm: the tube, from the shoulder to its rod-end face |
| 13 | Total length (EF000369) | 280 mm extended, over both studs (180 mm fully compressed) |

## What it meets
| figure | value | source |
|---|---|---|
| end threads (both ends) | M8 male, 12 long | M8 is a class value (a design input). The thread, derived: M8 × 1.25 coarse, tolerance class 6g: major Ø 7.7652 to 7.9713, pitch Ø 7.0382 to 7.1594, minor Ø d3 max 6.4377 (basic: H 1.0825, d2 7.1881, d3 6.4664); derived: derive.thread(8.0, 1.25) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6g; ISO 261 pitch). The end fittings screw onto it. Both studs are modelled plain at the nominal Ø8 (the thread form is not drawn; the model is unchanged) |
| cylinder-end stud tightening torque | M_A 24.8 N·m (preload F_M 16.4 kN): the stud's thread at 8.8, an upper bound. The tube end that carries the stud is not rated, so this is not the gas spring's own tightening figure | derived: derive.torque(8, 1.25, '8.8', mu_G=0.12, mu_K=0.12, nu=0.7, d_w=18, d_h=9) (M_A = F_M (0.16 P + 0.58 mu_G d2 + mu_K D_Km / 2), ISO 16047 / VDI 2230 Part 1; F_M = nu R_eL,nom A_s, ISO 898-1 clause 4 designation and stress area; design: nu 0.7, mu_G 0.12, mu_K 0.12, d_w 18). design: property class 8.8 (ISO 898-1 clause 4 designation, R_eL,nom 640 MPa, the class the stud is made to; the choice is bounded by the joint's load, VDI 2230 Part 1: the spring's 400 N (class value 9, EF007105) is the tension the stud carries through its end fitting, and at 8.8 its yield load 640 MPa × A_s 36.6 mm² = 23.4 kN stands far over it: the stud is never the joint's weakest member, which is what makes the derived torque the upper bound the value says). design: d_w 18 (the element's bearing face: the tube's shoulder Ø18 at x = 0, where the end fitting seats). nu 0.7 and mu_G / mu_K 0.12 are design choices (derive's defaults); d_h 9 is the M8 medium clearance hole (ISO 273, lib/standards/holes.csv) |
| end fittings (eye, ball socket, clevis) | none in this element | a host places them on the studs once they are built |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| tube | Ø18 × 150 (the class values), steel painted RAL 7035 | the finish is a design choice |
| rod | Ø8, 138 long: 20 inside the tube at full extension, 118 out (106 plain and the 12 stud) | 20 inside stands for the guide and piston |
| rod out at full stroke | 18 (6 plain and the 12 stud) | 6 stay clear between the rod-end fitting's seat and the tube |
| studs | M8 × 12 at each end | stud length |
| rod bore in the tube | Ø8.4, 130 deep from the rod-end face (features.csv) | 0.2 radial clearance round the rod; the model's stand-in for the guide and seal |
| inside the tube (gas, oil, piston, guide, seal) | not modelled | the twin reads the rod's travel only |

## Mechanism
`rod` (translate, axis −x, 0 to 100 mm, the stroke): 0 is full extension, as built; 100 is fully compressed, the rod's inner end
then 10 short of the bore's bottom. The pivot's origin is the rod stud's seat (256, 0, 0). Its extras carry the rod-end
connection for the twin: end rod, gender male, thread M8, length 12. MOT-010 sweeps it through the stroke.
`end-cyl` (port, fixed): the cylinder-end stud. Origin the shoulder (0, 0, 0), axis −x (out toward its end fitting); unit M8,
gender male (PIN-002), thread M8, length 12.

## Named nodes
`rod` (translate) · `end-cyl` (port). Colliders `body` (the tube), `end-cyl`, `rod` (the rod's part outside the tube at rest).

## Materials by layer
`M-STEEL-7035` tube · `M-ZINC` rod and cylinder-end stud (bright plated steel).

## Decals (Blender)
"complexes.org generic" on the tube, a printed label at mid-length.

## Notes
No vendor names, part numbers or marks. No safety claim. The class values are the figures this design is meant to meet; no
calculation or test of the model is on file. No open figure: the thread and the studs' tightening torque are derived (What it meets). The rest
are design choices.

## Outputs (out/)
`gas-spring.lsp` · `.glb` (pivots on `rod` and `end-cyl`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012096), our own design (cloud-mech, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
| 1.1 | text only: element.py's header, BASELINE and comment and this file's Baseline line say the M8 thread is derived (as What it meets has since mech-r85), no longer an open figure; no geometry change (mech-r87, unattended) |
| 1.2 | text only (DOC-009, lib/requests/core/mech-doc009-2026-11-11.md item 1): the stud's property class 8.8, an input of the derived torque in What it meets, names the rule it meets (ISO 898-1 clause 4 designation; VDI 2230 Part 1, the joint's load: the spring's 400 N in tension) in place of "this design's choice"; no geometry change (mech-r106, unattended) |
