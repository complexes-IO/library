# hold-down · v1.1 · hydraulic sheet hold-down, generic, single acting plunger, Ø32, stroke 25, 160 bar, flange mount

**What** a shear's hydraulic sheet hold-down: a single-acting plunger cylinder that sits in a bore of the shear's hold-down beam,
its square flange screwed to the beam's top. Before the blade comes down, oil into `port-cap` (on the flange's top) presses the
plunger and its polyurethane foot pad down onto the sheet, holding it on the table; when the oil is let out, a spring inside lifts
the plunger back. A shear carries a row of them along its beam, each placed by the shear. lib/inventory.csv row `hold-down`
(own_design generic, "hydraulic sheet hold-down (shear)"; 2 systems: shear-hydraulic, shear-sheet).
**Class** actuator · **Baseline** our own design: generic hydraulic cylinder (ETIM 10.0 EC012253), as OPERATING.md 12 (generic
elements, EM 2026-11-07) and the inventory row say. No vendor file was opened or measured. The class values below are its design
inputs; its sizes are design choices. It is not built as an ISO 6020-2 tie-rod cylinder (the standard hyd-cylinder-da-40 waits on): it
has no tie rods and none of that standard's mounting styles, but its own form, a plunger in a round body under a square flange,
so no standard on file or named in the inventory shapes it. The flange's holes take their size from ISO 273 (lib/standards/holes.csv).
No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the mounting face, the flange's underside centre on the plunger's axis (z = 0); the plunger
down (−z), the port up (+z).
**Built with** toolkit 1.3 · AutoLISP command `HOLD-DOWN` · no parameters.

The class: the inventory row names none. EC012253 "Hydraulic cylinder" (group EG020017, 11 features on file; synonyms "Flat
cylinder", "Linear hydraulic motor") is the class lib/standards/etim/classes.csv gives for a hydraulic linear actuator, and a
hold-down is one: a single-acting cylinder (class value 11, "Dual-action", no). It fits both of the row's systems, each a shear
whose hold-down beam carries it. It is the class hyd-cylinder-da-40 1.1 uses.

## Class values (ETIM 10.0 EC012253)
Design inputs, in ETIM's order (lib/standards/etim/class-features.csv). "not stated": the design has no value for the feature.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel (flange, body, plunger); the foot pad polyurethane |
| 2 | EF001257 Material quality | not stated |
| 3 | EF020449 Max. operating pressure | 160 bar (hpu-7.5kw 1.1's pressure, so one unit can feed it); in ratings.csv as p_max, status "generic design" |
| 4 | EF025564 Max. push load | 12.9 kN: 160 bar on the Ø32 plunger's 804.2 mm² (element.py push_kn; theoretical, the spring's force and friction not deducted) |
| 5 | EF000353 Max. tensile force | not stated: single acting, the oil never pulls (the spring lifts the plunger) |
| 6 | EF025541 Bore | 32 mm: the plunger's diameter, its working area (a plunger cylinder has no piston) |
| 7 | EF021866 Stroke length | 25 mm |
| 8 | EF014993 Overall height retracted | 138 mm: the port's face (z = 16) to the pad's face (z = −122), raised (element.py retracted_height) |
| 9 | EF000065 Inner diameter | not stated: the plunger is solid |
| 10 | EF002386 Ambient temperature | not stated |
| 11 | EF022580 Dual-action | no: single acting, spring return |

The pressure, bore and stroke are generic design values (OPERATING.md 12), not tested ratings. No hydraulic check reads them yet
(the PNE rules are for compressed air, toolkit/pneu.py). The pad's clamping force on the sheet is the push less the spring's force,
which is not modelled and not stated.

**No safety claim.** The pad closing on the sheet is a pinch point at the shear's front; guarding it is the shear's (its guard and
its codes, not on file here). This element claims no safety function (OPERATING.md 12).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| flange | 80 × 80 square, 15 thick (z 0 to 15) | seats on the hold-down beam's top face; carries the port and the four holes |
| flange holes | 4 × Ø9.0 through, on a 60 × 60 square (x, y = ±30) | M8 clearance, medium (ISO 273 H13, holes.csv); position Ø1.0 to A (the underside), B, C (the sides) in features.csv (GDT-010: T = H − F = 1.0); 5.5 of flange to each edge; clear of the body by 9.9 (asserted) |
| body | Ø56, 95 long under the flange (z −95 to 0), 0.5 into it | goes down the beam's bore (the host's); 11.5 of wall round the Ø33 plunger bore (12 round the Ø32 plunger) |
| plunger bore | Ø33 up the body from its foot to z = −18, blind (features.csv) | 0.5 clear round the plunger (it never touches the body at rest or through its travel); the floor 2 above the plunger's inner end |
| plunger | Ø32, z −110 to −20 at rest; chromed (`M-SILVER`) | 15 out of the body raised; at full stroke 50 of it stays in the body (≥ 1.5 × Ø, asserted) |
| foot pad | Ø50 × 12 under the plunger, face to face (z −122 to −110); polyurethane (`M-ORANGE-PA`) | the face that meets the sheet; moves with the plunger |
| return spring, seals | not modelled | inside the body, above the plunger |
| port spot face | Ø24 × 1 proud on the flange's top, on the axis (z 14.5 to 16, 0.5 into the flange) | the joint plane a port fitting meets; no bore cut (Open figures); inside the screw heads' circle by 15.9 |
| overall | envelope 80 × 80 × 138 raised (x, y −40 to 40, z −122 to 16); the pad's face at z −147 pressed | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-cap` | hyd-port | female | work | the flange's spot face, z = 16, axis +z | pneu.NODES cylinder end ("port-cap"): oil in presses the plunger down; the only port (single acting) |

"hyd-port" is the lane's placeholder unit for a hydraulic port whose thread is open, as hyd-cylinder-da-40 1.1's and hpu-7.5kw 1.1's (no
hydraulic contract in toolkit/ yet, so the unit is the core's to settle); it is no air unit, so the PNE checks don't pair it, and
no check pairs or rates a hyd-port joint.

## Open figures
- NOT ON FILE (B): the port's thread and size (no hydraulic port standard, such as an ISO 6149 or SAE straight-thread port, is
  in lib/standards/sources.csv). The port is a plain spot face with its pivot; the bore is cut once the standard is on file (a major).

## Named nodes
`plunger` (the plunger and its foot pad): kind translate along −z, 0 to 25 (the stroke), at rest raised; the twin moves it by the
stroke it reads. Through its travel it stays in the Ø33 bore (0.5 clear). `port-cap` (the spot face): kind port, fixed (range 0).

## Materials by layer
`M-CAST-BLUE` flange, body · `M-SILVER` plunger · `M-ORANGE-PA` foot pad · `M-STEEL-7035` port spot face

## Decals (Blender)
None in 1.0 (the "generic" label is a later version). No vendor names, no approval marks.

## Outputs (out/)
`hold-down.lsp` · `.glb` (plunger and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012253), pneu-r70 (unattended): single-acting plunger hold-down, Ø32, stroke 25, 160 bar; square flange with four M8 clearance holes (ISO 273), round body, `plunger` with its polyurethane foot pad (translate −z, the stroke), spot face `port-cap`; the port's thread left open (class B), the spring and seals not modelled; nothing placed |
| 1.1 | text, pneu-r81 (unattended; review pneu-r70 finding 1, hold-down-1.0.md finding 1): the Dimensions body row's wall is 11.5 round the Ø33 bore, (56 − 33) / 2, and 12 round the Ø32 plunger; no geometry, node, origin or cut-out changed |
