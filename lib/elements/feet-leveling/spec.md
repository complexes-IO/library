# feet-leveling · v1.2 · levelling foot, fixed base Ø80, rubber pad, M12 × 80 male stud

**What** A machine levelling foot: it carries a bench, a frame, a cabinet or a machine on the floor and sets its height. A rubber
anti-slip pad is bonded under a steel base disc; a hub on the base carries an M12 steel stud that screws into a tapped hole, or
through a hole into a nut, in the host's foot. Turning the stud in the host raises or lowers the host until it stands level. The
systems of lib/machines-from-elements.txt that list it (the alignment machine, the lab bench, the welding table and the assembly
workbench) place one under each corner of a frame.
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks feet-leveling own_design
"yes"). No product was matched and no vendor file was opened. The element's folder holds a catalogue record (references/source.txt); none of
its sizes is used here: every size below is a design choice. The stud's thread is derived (What it meets).
**Units / frame** mm, Z up. Origin: the pad's underside (the face that stands on the floor) on the foot's axis. The foot stands
toward +z; the stud's root is at z = 30, its tip at z = 110. Extents x, y ±40, z 0 to 110.
**Built with** toolkit 1.3 · AutoLISP command `FEETLEVEL` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| stud thread | M12 male, 80 long | M12 is this design's choice of stud. The thread, derived: M12 × 1.75 coarse, tolerance class 6g: major Ø 11.7067 to 11.9657, pitch Ø 10.6848 to 10.8291, minor Ø d3 max 9.8187 (basic: H 1.5155, d2 10.8633, d3 9.853); derived: derive.thread(12.0, 1.75) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6g; ISO 261 pitch). The host's tapped hole or nut meets it. The stud is modelled plain at the nominal Ø12 (the thread form is not drawn; the model is unchanged), as knob-knurled, damper-vibration and gas-spring do |
| stud tightening torque | M_A 88.4 N·m (preload F_M 37.75 kN), the stud screwed home against the hub | derived: derive.torque(12, 1.75, '8.8', mu_G=0.12, mu_K=0.12, nu=0.7, d_w=30, d_h=13.5) (M_A = F_M (0.16 P + 0.58 mu_G d2 + mu_K D_Km / 2), ISO 16047 / VDI 2230 Part 1; F_M = nu R_eL,nom A_s, ISO 898-1 clause 4 designation and stress area; design: nu 0.7, mu_G 0.12, mu_K 0.12, d_w 30). design: property class 8.8 (ISO 898-1 clause 4 designation, R_eL,nom 640 MPa, the class the stud is made to; the choice is bounded by the joint's load, VDI 2230 Part 1: the host's weight on the foot is compression through the stud into the hub and the pad, so in tension the stud carries only its own preload; at 8.8 its yield load 640 MPa × A_s 84.27 mm² = 53.9 kN stands over the preload F_M 37.75 kN the derived torque gives (nu 0.7), so the stud is never the joint's weakest member, which is what makes the derived torque the upper bound for the stud screwed home). design: d_w 30 (the element's bearing face: the hub's top face Ø30 at the stud's root). nu 0.7 and mu_G / mu_K 0.12 are design choices (derive's defaults); d_h 13.5 is the M12 medium clearance hole (ISO 273, lib/standards/holes.csv). At a levelled height the stud is locked by the host's nut, whose bearing face is the nut's: that torque is the host's to derive |
| the host's foot | a tapped M12 hole, or an M12 clearance hole Ø13.5 medium (ISO 273, lib/standards/holes.csv) with a nut | cut by the host's element; a lock nut or a nut, if used, is a standard part (ISO 4032, not on file, not built yet) that the host places |
| the floor | the pad's underside at z = 0 | none: the foot stands on any floor |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| pad | rubber, Ø76 × 6 (z 0 to 6), bonded under the base | stops the foot sliding on a smooth floor; 2 inside the base's rim, so its side face is not flush with the base's (GEO-050) |
| base | steel disc Ø80 × 10 (z 6 to 16) | spreads the host's weight over the pad |
| hub | Ø30 × 14 on the base (z 16 to 30) | carries the stud; its top face is where the stud starts |
| stud | M12 × 80 (z 30 to 110), fixed in the hub | 80 gives the height setting its range in a host's tapped hole or nut |
| swivel | none: the base is fixed to the stud | a fixed foot; a swivel foot for uneven floors is a later element |
| load rating | not claimed | no calculation or test is on file |

## ETIM features (EC004043 Levelling foot)
The inventory row's ETIM 10.0 class (ETIM International, ODC-BY 1.0; lib/standards/etim/class-features.csv), each feature with this
design's value, for a twin or a BOM that reads them. They describe the element; they are not the source of its sizes.

| # | feature | value |
|---|---|---|
| 1 | Material shaft (EF018372) | steel, property class 8.8 (ISO 898-1 clause 4; What it meets, the torque row; the layer steel-mild in lib/materials.csv is its appearance) |
| 2 | Surface protection shaft (EF018373) | zinc-plated |
| 3 | Shaft length (EF000178) | 80 mm |
| 4 | Thread size (metric) (EF003563) | 12 (M12) |
| 5 | Thread type (EF001758) | metric (M12 × 1.75 coarse, derived, What it meets) |
| 6 | With locknut (EF005049) | no |
| 7 | Positioning height (EF018374) | not stated: it depends on how far the stud goes into the host |
| 8 | Max. pivoting range (EF004988) | 0° (fixed base) |
| 9 | Diameter foot (EF018371) | 80 mm |
| 10 | Material foot (EF017481) | steel, with a rubber pad (lib/materials.csv epdm) |
| 11 | Sound-damping (EF022677) | not stated |
| 12 | With vibration damper (EF008394) | no |
| 13 | Max. bearing capacity (EF012752) | not stated (no load rating) |
| 14 | Pre-punched installation holes (EF015275) | no |
| 15 | With mounting plate (EF000118) | no |

## Mechanism
No part moves inside the element: the pad, base, hub and stud are one part. Turning the stud in the host moves the host along the
stud's axis; how far a turn moves it is the thread's pitch (M12 × 1.75, What it meets); no moving node is declared for it. The
assembly places the foot at the height the host needs, along the port's axis.
`stud` (port, fixed): origin the stud's root on the hub (0, 0, 30), axis +z (into the host); unit M12, gender male (PIN-002),
thread M12, length 80.

## Named nodes
`stud` (port). Colliders `body` (the pad, base and hub), `stud`.

## Materials by layer
`M-GASKET` the pad (rubber) · `M-ZINC` the base, hub and stud (steel, zinc-plated).

## Notes
No vendor names, part numbers or marks. No load rating and no safety claim. No open figure: the thread and the stud's tightening
torque are derived (What it meets). The rest are design choices. The foot is not anchored to the floor.

## Outputs (out/)
`feet-leveling.lsp` · `.glb` (pivot on `stud`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r53, unattended) |
| 1.1 | text only (review mech-r85 finding 1): element.py's header, BASELINE and comment, this file's Baseline line and the ETIM table's thread-type row say the M12 thread is derived (as What it meets has since mech-r85), no longer an open figure; no geometry change (mech-r88, unattended) |
| 1.2 | text only (DOC-009, lib/requests/core/mech-doc009-2026-11-11.md item 1): the stud's property class 8.8, an input of the derived torque in What it meets, names the rule it meets (ISO 898-1 clause 4 designation; VDI 2230 Part 1, the joint's load: the host's weight is compression through the stud, which carries only its preload, under its 53.9 kN yield load) in place of "this design's choice"; the Material shaft class value names the class to match; torque, model and behaviour.csv unchanged (mech-r107, unattended) |
