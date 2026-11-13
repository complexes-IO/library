# valve-counterbalance · v1.2 · hydraulic counterbalance (load-holding) valve, generic, inline, pilot assisted 3:1, 160 bar, screw set, lock nut

**What** an inline hydraulic counterbalance valve for the line that carries a vertical cylinder's load (lib/inventory.csv row
`valve-counterbalance`, "counterbalance (load-holding) valve for a vertical cylinder's A line", own_design generic, 1 system:
press-hydraulic, EM 2026-11-09: a blocked-centre spool plus a counterbalance valve). Oil from `port-2` (the directional valve's
side) to `port-1` (the cylinder's side) lifts a check and passes free. Oil from `port-1` to `port-2` passes only when the pressure
the load makes at `port-1`, helped by the pilot pressure at `port-12` (taken from the cylinder's other line), overcomes the
spring's setting: the load cannot run ahead of the pump, and it stays held when the directional valve centres or a hose on the
valve's side fails. The screw on top sets the spring; the lock nut under it holds the setting.
**Class** device · **Baseline** our own design: generic hydraulic counterbalance valve (no ETIM class; ISO 4413 values), as
OPERATING.md 12 (generic elements, EM 2026-11-07; a product class ETIM has no class for is generic by the standard whose rating
data its Class values follow, EM 2026-11-08) and the inventory row say. No vendor file was opened or measured. The class values
below are its design inputs; its sizes are design choices. No standard on file shapes it: its ports' standard is not in
lib/standards/sources.csv (Open figures), and an inline valve has no mounting face standard. No vendor names; "generic" in its
title.
**Units / frame** mm, Z up. Origin: port-1's face, the cylinder-side spot face's outer face on the flow axis (x = 0); the flow axis
along +x to port-2, the adjusting screw up (+z), the pilot port down (−z).
**Built with** toolkit 1.3 · AutoLISP command `VALVE-COUNTERBALANCE` · no parameters.

The class chosen: none. lib/standards/etim/classes.csv (ETIM 10.0's subset on file) has no counterbalance, load-holding or
over-centre valve class, as the inventory row records ("no ETIM class found in the subset: ISO 4413 values"). EC011463 "Regulating
valve" (hyd-flow-control 1.0's class) is a throttle and EC011469 "Check valve" (check-valve's) has no pilot or setting: neither
describes a valve that holds a load against a set pressure. The standard named, ISO 4413 (hydraulic fluid power: general rules and
safety requirements for systems and their components), is not in lib/standards/sources.csv: it is named as the standard against
which the valve's rating quantities are stated, as hpu-7.5kw 1.1 names it, and no figure or clause is taken from it.

## Class values (no ETIM class; ISO 4413 values)
Design inputs (OPERATING.md 12): the quantities a counterbalance valve is chosen by, with the value this one is designed to.

| # | quantity | value |
|---|---|---|
| 1 | max. operating pressure | design: 160 bar (rated for the press circuit's relief pressure: hpu-7.5kw 1.1's pressure and its relief setting, hydraulic.csv); in ratings.csv as p_max, status "generic design" |
| 2 | setting range | 10 to 160 bar at `port-1` with no pilot pressure, over the screw's four turns: design: never above the valve's own max. operating pressure (element.py asserts) |
| 3 | pilot ratio | 3:1 (the pilot's area to the seat's): design choice. The pilot pressure that opens the valve is (setting − load pressure) / 3 (element.py pilot_bar) |
| 4 | free-flow check | built in, `port-2` to `port-1`; its cracking pressure not stated |
| 5 | flow | not stated: no flow is claimed. The body is sized for the press's 1/2 in lines (hydraulic.csv), a design choice |
| 6 | fluid | mineral hydraulic oil ISO VG 46 (ISO 11158 HM) |
| 7 | leakage with the load held | not stated: the twin shows the ram held (design.md), not a drift rate |
| 8 | ports | `port-1` (cylinder), `port-2` (directional valve), `port-12` (pilot), their thread open (Open figures) |
| 9 | adjustment | a screw with a lock nut (modelled; the nut fixed), four turns |

These are generic design values (OPERATING.md 12), not tested ratings. No hydraulic check reads the pressure yet (the PNE rules are
for compressed air, toolkit/pneu.py; request pneu-8 proposes HYD rules).

**The setting is the machine's, and it is derived** (OPERATING.md 6, derive before you ask): design.md gives the rule,
p_set = k × W / A with k ≈ 1.3, W the weight the cylinder carries and A the piston area the load's oil stands on. With hyd-cylinder-da-40
1.1 (bore 40, rod 22) `python lib/build.py derive cylinder 40 22 160 22` gives the cap-end area 1256.6 mm² and the rod-end
(annulus) area 876.5 mm² (derived: derive.cylinder(40.0, 22.0, 160.0, 22.0), F = p A). For each 100 kg the rod carries (981 N),
the load pressure is 981 / 876.5 = 1.12 MPa = 11.2 bar on the annulus (the rod hanging down, the load pulling it out) or
981 / 1256.6 = 7.8 bar on the cap end (the rod standing up, the load pushing it in), and the setting 1.3 times that: 14.6 or
10.1 bar per 100 kg, inside this valve's range. The press's own figure waits for the ram's moving mass on the press's sheet
(design.md); it is no figure of this element. Which of the cylinder's two lines carries the load depends on how the cylinder
stands: request pneu-9 (lib/requests/pneu/9.md) asks the core about the press's line.

**No safety claim.** Holding a press's ram is part of the machine's safety design (design.md: the valve's centre and the press's
safety relay, EM's sign-off; the inventory row's `safety` column is empty). This element claims no safety function, performance
level or category of its own (OPERATING.md 12).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| body | 80 long (x 1 to 81) × 40 × 40, the flow axis through its centre (y = 0, z = 0); zinc plated steel (`M-ZINC`) | holds the poppet, the pilot piston, the check and the three ports |
| main port spot faces | Ø26 × 1 proud on each end face, on the flow axis (x 0 to 1.5 and 80.5 to 82, 0.5 into the body) | the joint plane a port fitting meets (hyd-flow-control 1.0's); 7 of end face round each; no bore cut (Open figures) |
| pilot port spot face | Ø18 × 1 proud on the underside under the body's centre (x = 41, z −19.5 to −21, 0.5 into the body) | a small line that carries no flow; 11 of underside round it across the body; no bore cut |
| cartridge | Ø30, from the body's top face to z = 44 (0.5 into the body), over the body's centre (x = 41); `M-SILVER` | houses the spring; 26 clear of each main spot face in x |
| lock nut | Ø20 × 6 on the cartridge's top (z 43.5 to 50, 0.5 into the cartridge); `M-ZINC` | holds the screw's setting |
| adjusting screw | head Ø10 × 10 on the lock nut, face to face (z 50 to 60); `M-BLACK-PA` | the commissioning engineer's setting, four turns lowest to highest |
| poppet, pilot piston, check, spring | not modelled | inside the body and cartridge |
| overall | envelope 82 × 40 × 81 (x 0 to 82, y −20 to 20, z −21 to 60) | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | hyd-port | female | work | the cylinder-side spot face, x = 0, axis −x | design: numbered 1, 2, 12 as the pneumatic numbering does; ISO 9461 (hydraulic port identification) not on file. 1 is the side whose pressure the valve holds; the controlled way runs 1 to 2 |
| `port-2` | hyd-port | female | work | the valve-side spot face, x = 82, axis +x | design, as port-1's: 2, the free way runs 2 to 1 through the check |
| `port-12` | hyd-port | female | pilot | the underside spot face, x = 41, z = −21, axis −z | design, as port-1's: 12, the pilot that opens the way 1 to 2 (control-valve 1.0's pilot is named the same way) |

The valve goes next to the cylinder: `port-1` to the cylinder port whose oil carries the load, `port-2` to the directional valve's
port for that line, `port-12` teed into the cylinder's other line. "hyd-port" is the lane's placeholder unit for a hydraulic port
whose thread is open, as hyd-flow-control 1.0's and hyd-cylinder-da-40 1.1's (no hydraulic contract in toolkit/ yet; request pneu-8
proposes one); it is no air unit, so the PNE checks don't pair it, and no check pairs or rates a hyd-port joint.

## Open figures
- NOT ON FILE (B): the three ports' thread and size (no hydraulic port standard, ISO 6149 or SAE J1926, is in
  lib/standards/sources.csv; request pneu-8 proposes SAE J1926-1). The ports are plain spot faces with their pivots; the bores are
  cut once the standard is on file (a major).
- NOT ON FILE (B): ISO 9461, the ports' marks (toolkit/hyd.py H11, request pneu-10's answer item 2: hydraulic port identification;
  lib/standards/sources.csv iso-9461, wanted). The ports are named by their function (1 the held side, 2 the valve side, 12 the
  pilot, the design's own numbers) and claim no mark of the standard's; when it is on file, hyd.PORT_MARKS takes the marks with
  their clause and a text minor marks these ports from it (hpu-0.37kw 1.0's line).

## Named nodes
`screw` (the adjusting screw's head): kind rotate about +z at x = 41, 0 to 1440° (four turns), at rest 0 (the lowest setting, a
design choice: the setting is the commissioning engineer's). `port-1`, `port-2`, `port-12` (the spot faces): kind port, fixed
(range 0).

## Materials by layer
`M-ZINC` body, lock nut · `M-STEEL-7035` port spot faces · `M-SILVER` cartridge · `M-BLACK-PA` adjusting screw

## Decals (Blender)
None in 1.0 (the port numbers 1, 2, 12 and the "generic" label are a later version). No vendor names, no approval marks.

## Notes
- The twin reads no setting from the screw in 1.0 and solves no oil (behaviour.csv): the ram held, and drifting with the valve
  removed (design.md), comes with the hydraulic solver.
- Inline, carried by its port fittings; no mounting holes in 1.0 (a body bolted to the cylinder's port face is a later version).

## Outputs (out/)
`valve-counterbalance.lsp` · `.glb` (screw and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/
per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (no ETIM class; ISO 4413 values), pneu-r78 (unattended): inline pilot-assisted counterbalance valve (free 2 to 1 through the check, 1 to 2 against the setting), 160 bar, pilot ratio 3:1, setting 10 to 160 bar; body, cartridge, lock nut, `screw` (rotate, four turns), spot faces `port-1` / `port-2` / `port-12`; the ports' thread left open (class B); poppet, pilot piston, check and spring not modelled; nothing placed |
| 1.1 | review pneu-r78 findings 1 and 2 (valve-counterbalance-1.0.md), pneu-r80 (unattended): the ports' numbers 1, 2, 12 are a design choice (the pneumatic numbering's way; ISO 9461 not on file) in Ports and behaviour.csv's three pin rows; ratings.csv p_max's source is the design rule (rated for the press circuit's relief pressure), the standard named only; class value 6 names the oil "ISO VG 46 (ISO 11158 HM)" (review pneu-r74 finding 2b's wording). Text only: a minor |
| 1.2 | text only, pneu-r87 (unattended; request pneu-10's answer item 2): the ports' marks added to Open figures as a class B line, ISO 9461 a document wanted (toolkit/hyd.py H11: the ports named by their function, no mark of the standard's claimed; the line lists the standard once in lib/standards/wanted.md). No shape, node, origin or cut-out change |
