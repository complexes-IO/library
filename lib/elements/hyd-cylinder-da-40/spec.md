# hyd-cylinder-da-40 · v1.1 · hydraulic cylinder, generic, double acting, tie-rod, bore 40, rod 22, stroke 200, 160 bar

**What** a double-acting hydraulic cylinder of tie-rod construction: a barrel between two square end caps held by four tie rods, a
chromed piston rod leaving through a gland nose on the head cap, and two ports on top, one over each cap. Oil into `port-cap`
extends the rod, oil into `port-rod` retracts it. The actuator of the hydraulic machines in lib/inventory.csv: row `hyd-cylinder-da-40`
(own_design generic, 18 systems, pin 1, "press-hydraulic first", EM 2026-11-08): a double-acting hydraulic cylinder whose mounting
and ports follow ISO 6020-2 once that is on file, and stay open until then.
**Class** actuator · **Baseline** our own design: generic hydraulic cylinder (ETIM 10.0 EC012253), as OPERATING.md 12 (generic
elements, EM 2026-11-07) and the inventory row say. No vendor file was opened or measured: the folder's metadata.json and
references/ were not used (the row's note: "the vendor file in its folder is reference only, never copied"). The class values
below are its design inputs; its sizes are design choices. OPERATING.md 12 never builds an ISO cylinder interface generic: so the
interfaces ISO 6020-2 fixes (the mounting, the rod end, the ports) are not drawn and stay open (Open figures), and the rest, which
no standard on file shapes, is our own. The body envelope and the rod diameter may be ISO 6020-2's too (per bore: the square size,
the cap and body lengths, the rod projection, the rods allowed): they are drawn as design choices and wait on the standard as an
open figure of their own (Open figures), so 2.0 may change the envelope and class values 4, 5 and 8, not only the cut-outs. No
vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the cap end, the rear cap's back face centre on the cylinder's axis (x = y = z = 0); the axis
along +x, the rod out toward +x, the ports up (+z).
**Built with** toolkit 1.3 · AutoLISP command `HYD-CYLINDER` · no parameters.

The class chosen: EC012253 "Hydraulic cylinder" (group EG020017, 11 features; synonyms "Flat cylinder", "Linear hydraulic
motor"), the class inventory row `hyd-cylinder-da-40` names.

## Class values (ETIM 10.0 EC012253)
Design inputs, in ETIM's order (lib/standards/etim/class-features.csv). "not stated": the design has no value for the feature.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel (barrel, caps, gland, tie rods, rod) |
| 2 | EF001257 Material quality | not stated |
| 3 | EF020449 Max. operating pressure | 160 bar; in ratings.csv as p_max, status "generic design" |
| 4 | EF025564 Max. push load | 20.1 kN: 160 bar on the 40 bore's 1256.6 mm² (element.py forces_kn; theoretical, no friction, no buckling check) |
| 5 | EF000353 Max. tensile force | 14.0 kN: 160 bar on the annulus, 1256.6 − 380.1 = 876.5 mm² (as 4) |
| 6 | EF025541 Bore | 40 mm |
| 7 | EF021866 Stroke length | 200 mm |
| 8 | EF014993 Overall height retracted | 340 mm: the rear cap's back face to the rod's end, retracted (element.py retracted_length; the mounting, not drawn, adds to it) |
| 9 | EF000065 Inner diameter | not stated: the rod is solid (no hollow rod); the barrel's inner diameter is the bore (6) |
| 10 | EF002386 Ambient temperature | not stated |
| 11 | EF022580 Dual-action | yes: `port-cap` extends, `port-rod` retracts |

The pressure, bore and stroke are generic design values (OPERATING.md 12), not tested ratings. 160 bar is a design input for a
press-class cylinder; no hydraulic check reads it yet (the PNE rules are for compressed air, toolkit/pneu.py).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| rear cap (cap end) | 60 × 60 square (y, z), 35 long (x 0 to 35) | holds `port-cap`; square caps for the tie rods |
| barrel | Ø50 OD, between the caps (x 35 to 260), 0.5 into each | 5 wall round the 40 bore (not modelled); its length holds the 25 piston and the 200 stroke |
| head cap (rod end) | 60 × 60, 40 long (x 260 to 300) | holds `port-rod` and the rod's guide |
| gland nose | Ø36 × 10 on the head cap's front face (x 300 to 310) | carries the rod seal and wiper (not modelled) |
| tie rods | four, Ø10, at y, z = ±22, cap face to cap face (x 35 to 260), 0.5 into each cap; zinc | clear the barrel by 1.1 and stay inside the caps (element.py asserts both); no nuts drawn |
| piston rod | Ø22, x 60 to 340 retracted; chromed (`M-SILVER`) | rod-to-bore 0.55 (design choice); 30 out of the gland retracted; its end plain (Open figures) |
| rod bore | Ø23 through the gland, head cap and barrel to x = 58 (features.csv) | 0.5 clear round the rod (it never touches the body at rest or through its travel); the floor 2 behind the rod's inner end |
| piston | not modelled: x 35 to 60 retracted, 235 to 260 at full stroke | the rod's inner end (x 60) is its rod-side face; at full stroke it stops at the head cap's inner face (element.py asserts it) |
| port spot faces | Ø24 × 1 proud on each cap's top face, at x = 17.5 (cap end) and x = 280 (rod end), y = 0; 0.5 into the cap | the joint plane a port fitting meets; no bore cut (Open figures) |
| overall | envelope 340 × 60 × 61 retracted (x 0 to 340, y −30 to 30, z −30 to 31); 540 long extended | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-cap` | hyd-port | female | work | the rear cap's spot face, z = 31, axis +z | pneu.NODES cylinder ends ("port-cap", "port-rod"); oil in extends the rod |
| `port-rod` | hyd-port | female | work | the head cap's spot face, z = 31, axis +z | as above; oil in retracts the rod |

"hyd-port" is the lane's placeholder unit for a hydraulic port whose thread is open (no hydraulic contract in toolkit/ yet, so the
unit is the core's to settle); it is no air unit, so the PNE checks (toolkit/pneu.py, compressed air only) don't pair it, and no
check pairs or rates a hyd-port joint. A hydraulic fitting (inventory `fitting-hyd-iso8434`) meets each port once the
port's thread is on file.

## Open figures
- NOT ON FILE (B): the mounting interface (ISO 6020-2's mounting styles and their dimensions: flanges, feet, clevis, trunnion, tapped
  cap holes). Not in lib/standards/sources.csv, so the caps carry no mounting feature; a host can't place the cylinder until it is
  on file (then a major version, new cut-outs).
- NOT ON FILE (B): the rod-end thread (ISO 6020-2's rod-end form and its thread size for a 22 rod). The rod ends plain at x = 340.
- NOT ON FILE (B): the two ports' thread and size (no hydraulic port standard, such as an ISO 6149 or SAE straight-thread port,
  is in sources.csv). Each port is a plain spot face with its pivot; the bore is cut once the standard is on file (a major).
- NOT ON FILE (B): the body envelope and rod diameter ISO 6020-2 fixes for bore 40 (square size, cap and body lengths, rod
  projection, the rods allowed with the bore); drawn as design choices (Dimensions) until it is on file (review hyd-cylinder-1.0.md
  finding 1).

## Named nodes
`rod` (the piston rod): kind translate along +x, 0 to 200 (the stroke), at rest retracted; the twin moves it by the stroke it
reads. Through its travel it stays in the 23 bore (0.5 clear); at 200 its inner end is at the head cap's inner face. `port-cap`,
`port-rod` (the spot faces): kind port, fixed (range 0).

## Materials by layer
`M-CAST-BLUE` caps, barrel, gland · `M-SILVER` rod · `M-ZINC` tie rods · `M-STEEL-7035` port spot faces

## Decals (Blender)
None in 1.0 (the "generic" label and the port letters are a later version). No vendor names.

## Outputs (out/)
`hyd-cylinder-da-40.lsp` · `.glb` (rod and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012253), pneu-r57 (unattended): tie-rod cylinder, bore 40, rod 22, stroke 200, 160 bar; square caps, barrel, four tie rods, gland nose, rod `rod` (translate, the stroke), spot faces `port-cap` / `port-rod`; mounting, rod-end thread and port thread left open (class B), piston and seals not modelled |
| 1.1 | text only, pneu-r65 (unattended; review hyd-cylinder-1.0.md findings 1 and 2, pneu-r57 findings 1 and 2): a fourth open figure, class B, for the body envelope and rod diameter ISO 6020-2 may fix, and the What line says the envelope waits on it too; "hyd-port" called the lane's placeholder unit; behaviour.csv added (BEH-010). No shape change |
