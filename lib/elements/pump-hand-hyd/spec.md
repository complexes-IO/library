# pump-hand-hyd · v1.1 · hand hydraulic pump, generic, lever operated, single-acting outlet, release valve, horizontal reservoir, base mounted

**What** a hand hydraulic pump for a small shop press: the operator works the lever up and down; each stroke drives a plunger in
the pump head, which draws oil from the horizontal reservoir behind it and delivers it out of the one oil port `port-p` to a
single-acting press cylinder. Turning the release knob on the head's front opens the release valve: the oil goes back to the
reservoir and the cylinder's spring or the load returns it. The pump stands on the press's base or the floor, its plate screwed
down with four M8 screws. lib/inventory.csv row `pump-hand-hyd` (own_design generic, "hand hydraulic pump"; 1 system:
press-shop-hydraulic, whose line in lib/machines-factory.txt places it with hyd-cylinder-da-40, hyd-gauge, bolster and guard-panel).
**Class** device · **Baseline** our own design: generic hand pump (hydraulic) (ETIM 10.0 EC004260), as OPERATING.md 12 (generic
elements, EM 2026-11-07) and the inventory row say. No vendor file was opened or measured. Its sizes are design choices; the
base's holes take their size from ISO 273 (lib/standards/holes.csv). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the mounting face, the base plate's underside (z = 0); x = 0 at the pump head's front face;
y = 0 on the reservoir's axis. The reservoir and the lever toward +x, the port and the release knob on the head's front (−x).
**Built with** toolkit 1.3 · AutoLISP command `PUMP-HAND-HYD` · no parameters.

The class: the inventory row names none. EC004260 "Hand pump (hydraulic)" (group EG020079 Pumps, tier 2) is the class
lib/standards/etim/classes.csv gives for a hand-worked hydraulic pump, and the row's type is one. EC010463 "Hand membrane pump"
and EC010268 "Hand vane pump" are pumps for liquids at low pressure, not a press pump. It fits the row's one system.

## Class values (ETIM 10.0 EC004260)
Design inputs. EC004260 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (tier-1 classes and the
classes the inventory uses) does not list its 3 features: the case request pneu-4 raised for tube-pneu, which the core answered
(lib/requests/core/pneu-4-answer.md): the features come with an attended core session and EM's ETIM download, and the element is
built meanwhile with its design values under plain names. When they are on main, a minor version restates this table in ETIM's
order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| material | steel (base, head, reservoir, lever); the grip, knob and filler cap polyamide |
| operation | manual, by the lever; single acting: one delivery port, the return through the release valve |
| max. operating pressure | not stated: a rating with no source on file (Open figures 2, class A); no p_max row in ratings.csv |
| delivery per stroke | not stated: the plunger is not modelled |
| usable oil volume | not stated: the reservoir's inside is not modelled |
| connection | one oil port, its thread open (Open figures 1, class B) |

The pressure is not stated. A hand press pump's pressure decides the force the press's cylinder can make, so it is a rating that
decides what the twin reports: class A, EM's (OPERATING.md 6). No EC004260 feature is on file to carry a value, and no other
figure on file gives one: hpu-7.5kw's 160 bar is that unit's own value, not this pump's (tube-pneu 1.2 dropped a borrowed figure the
same way, review pneu-r62 finding 1). No hydraulic check reads it yet (the PNE rules are for compressed air, toolkit/pneu.py;
request pneu-8 proposes HYD-001..008).

**No safety claim.** A press worked by this pump crushes what is under its ram; guarding it is the press's (its guard and its
codes, not on file here). The release valve is the operator's control, not a safety function, and the pump has no pressure relief
of its own modelled or claimed (OPERATING.md 12).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| base plate | 440 × 140 × 8 (x −10 to 430, y ±70, z 0 to 8) | carries the head and the reservoir; stands 10 past the head's front and 20 past the reservoir's end, so no face is flush with its ends or sides |
| base holes | 4 × Ø9.0 through, at x = 10 and 410, y = ±57.5 | M8 clearance, medium (ISO 273 H13, holes.csv); position Ø1.0 to A (the underside), B (the front end), C (the side) in features.csv (GDT-010: T = H − F = 1.0); 8 of plate to the side edges; 8 clear of the head and the reservoir for a screw head (asserted) |
| pump head | 80 × 90 × 102.5 (x 0 to 80, y ±45, z 7.5 to 110), 0.5 into the base | holds the plunger, the check valves and the release valve (none modelled); the port and the knob on its front face |
| reservoir | Ø84 tube, x 79.5 to 410 (0.5 into the head), its axis at z = 49.5, its underside 0.5 into the base | the oil tank; its top at z = 91.5, under the head's top |
| filler / breather cap | Ø30, z 87.5 to 98, on the reservoir's top at x = 370 | where the oil goes in; polyamide |
| fulcrum post | 20 × 30 (x 5 to 25), z 109.5 to 150, 0.5 into the head | carries the lever's pivot at its rear upper edge |
| plunger housing | Ø36, z 109.5 to 150, its axis at x = 40 | the plunger under the lever (not modelled inside) |
| lever | socket 65 × 24 × 20 (x 5 to 70, z 150 to 170) seated face to face on the post and the housing; tube Ø25 to x = 480.5; grip Ø30 × 80 to x = 560 | 555 from the pivot to the grip's end; at rest it lies along +x, the tube 49.5 above the filler cap's top |
| release knob | Ø24 × 14 on the head's front face, its axis at y = 20, z = 40, face to face | turned by hand; one turn from shut to open |
| port spot face | Ø26 × 1 proud of the head's front face (x −1 to 0.5, 0.5 into the head), its axis at y = −20, z = 70 | the joint plane a fitting meets; no bore cut (Open figures); 50 from the knob's axis, room for a spanner |
| overall | envelope 574 × 140 × 175 (x −14 to 560, y ±70, z 0 to 175) at rest | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-p` | hyd-port | female | supply | the head's front spot face, x = −1, axis −x | hpu-7.5kw's delivery port `port-p` (the pump's pressure port): to the press cylinder's `port-cap` through a hose |

"hyd-port" is the lane's placeholder unit for a hydraulic port whose thread is open, as hold-down 1.0's, hyd-flow-control 1.0's and
hpu-7.5kw 1.1's (no hydraulic contract in toolkit/ yet; request pneu-8 proposes SAE J1926-1 ports); it is no air unit, so the PNE
checks don't pair it, and no check pairs or rates a hyd-port joint.

## Open figures
- NOT ON FILE (B): the port's thread and size (no hydraulic port standard, such as SAE J1926-1 or ISO 6149, is in
  lib/standards/sources.csv; request pneu-8). The port is a plain spot face with its pivot; the bore is cut once the standard is on
  file (a major).
- NOT ON FILE (A): the max. operating pressure (Class values): no feature of EC004260 and no figure on file gives it; EM's.

## Named nodes
`lever` (socket, tube and grip): kind rotate about −y at its socket's rear lower edge (x = 5, z = 150), 0 to 60°: at rest down on
its seat, lifted by the operator; through its travel every point of it stays at or above the seat plane z = 150 (the post's and
the housing's top: a point dx behind and dz above the pivot is at height dx·sin θ + dz·cos θ ≥ 0 for 0 to 60°), so it never meets
the post, the housing, the reservoir or the cap. `knob` (the release knob): kind rotate about −x on its own axis, 0 to 360° (shut to open). `port-p` (the spot
face): kind port, fixed (range 0).

## Materials by layer
`M-STEEL-7035` base plate, port spot face · `M-CAST-BLUE` head, reservoir, post, plunger housing · `M-SILVER` lever socket and tube ·
`M-BLACK-PA` grip, release knob, filler cap

## Decals (Blender)
None in 1.0 (the "generic" label and the knob's open / shut arrows are a later version). No vendor names, no approval marks.

## Outputs (out/)
`pump-hand-hyd.lsp` · `.glb` (lever, knob and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per
the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004260), pneu-r75 (unattended): base plate with four M8 clearance holes (ISO 273), pump head, horizontal reservoir with filler cap, fulcrum post and plunger housing, `lever` (rotate, lifting 60°), release `knob` (rotate, one turn), spot face `port-p`; the port's thread (class B) and the max. operating pressure (class A) left open; the plunger, check valves and oil not modelled; nothing placed |
| 1.1 | text, pneu-r81 (unattended; review pneu-r75 finding 1, pump-hand-hyd-1.0.md finding 1): Named nodes gives the lever's clearance its right reason, every point of it stays at or above the seat plane z = 150 (the socket's rear upper edge does go down and back as it lifts); no geometry, node, origin or cut-out changed |
