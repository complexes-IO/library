# panel-clamp · v1.2 · panel mounting clamp, hook 10 × 6 × 2.5, body 8 × 12 × 22, M4 tapped hole, panels 1 to 6 thick

**What** The clamp that holds a cut-out-mounted device (an operator panel, a power meter) in a panel. The device goes through the
panel's cut-out from the front until its bezel seats on the panel's front face. Behind the panel, the clamp's hook goes into a
slot in the side wall of the device's housing; a screw in the clamp's tapped hole is turned until its tip presses on the panel's
back face. The screw's push on the panel pulls the hook rearward, and the hook pulls the device's bezel tight against the panel.
Two clamps, on opposite walls, hold one device. hmi-7in and power-meter (lane elec) each place two (lib/inventory.csv `made_of`).
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks panel-clamp own_design
"yes", request mech-5's answer lib/requests/core/mech-5-answer.md). No product was matched and no vendor file was opened. No ETIM
class on file fits a device's panel clamp (mech-5's answer), so the element is not generic and carries no class values. The
clamp defines the slot its hosts cut; every size is a design choice. The tapped hole's thread is derived (What it meets).
**Units / frame** mm, Z up in the element's frame (in a host it lies along the host's depth). Origin: the hook's bearing face
(z = 0) on the housing wall's outer surface (x = 0), at the hook's centre (y = 0). The housing is toward −x; the screw's axis runs
along +z toward the panel; the bezel's seating face (the panel's front face) is at z = 30. Extents x −2.5 to 8, y ±6, z 0 to 22.
**Built with** toolkit 1.3 · AutoLISP command `PANELCLAMP` · no parameters.

## The slot it takes (the interface its hosts cut)
The host's housing takes these figures from this element (properties.csv, read as `element:panel-clamp <property>`), not the
other way round (mech-5's answer: foundation first, the clamp is the common part).

| property | value | why |
|---|---|---|
| slot_width | 10.4 across the hook (y) | the hook's 10.0 with 0.2 a side |
| slot_length | 7.0 along the screw (z) | the hook's 6.0 with 1.0 in front of it, room to tip the hook in |
| slot_depth_min | 3.0, through the housing's wall or blind | the hook goes 2.5 into the wall; nothing of the host within 3.0 of the wall's outer face behind the slot |
| slot_seat_distance | 30.0 from the slot's rear (bearing) face to the bezel's seating face | sets the panel range below with the body's 22 length |
| slots_per_host | 2, on opposite walls | the two pulls balance; the host may cut more |

## The panel range
| panel thickness | the panel's back face | the screw's tip stands out of the body's front face (z = 22) |
|---|---|---|
| 1.0 (thinnest) | z = 29.0 | 7.0 |
| 6.0 (thickest) | z = 24.0 | 2.0 (2.0 clear between the body and the panel) |

A panel thinner than 1.0 or thicker than 6.0 is outside this clamp's range (a design choice for sheet-steel and plastic panels).

## What it meets
| figure | value | source |
|---|---|---|
| tapped hole | M4, on the body's axis (x 4, y 0), from the front face z = 22 to z = 10, 12 deep | M4 is this design's choice of screw. The thread, derived: M4 × 0.7 coarse, tolerance class 6H: minor Ø D1 3.2422 to 3.4224, pitch Ø D2 3.5453 to 3.6637 (basic: H 0.6062, d2 3.5453, d1 3.2422), tap drill Ø3.3; derived: derive.thread(4.0, 0.7) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6H; ISO 261 pitch). The screw meets it. The hole is modelled plain at the nominal Ø4 (the thread form is not drawn; the model is unchanged), as feet-leveling and knob-knurled model their studs |
| the screw | an M4 screw whose tip presses the panel's back face | a common part not built yet (no screw table on file): placed in a later version (OPERATING.md 12, own designs). The hole is modelled now, as the rule asks |
| the host's slot | the table above | defined here; cut by the host's element |
| the panel | its back face, 1.0 to 6.0 behind the bezel's seating face | none: any flat panel in the range |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 8 × 12 × 22 (x 0 to 8, y ±6, z 0 to 22), lies on the housing wall's outer face | long enough to carry 12 of thread; 2.0 of wall each side of the hole |
| hook | 10 × 6 × 2.5 (y ±5, z 0 to 6, x −2.5 to 0), its rear face z = 0 bears on the slot's rear face | under 3 deep, so a thin housing wall takes it |
| tapped hole | M4, 12 deep | a design choice: M4 is the screw the 8-wide body carries with 2.0 of wall each side of the hole; 12 deep (z 10 to 22), also a design choice |
| material | steel, zinc-plated | a hook that takes the screw's reaction |
| volume | 2111 mm³ (body 2112, less the hole 151, plus the hook 150) | computed from the model; the mass waits on a steel density (lib/materials.csv steel-mild states none) |
| clamping force | not claimed | no screw, torque or panel figure is on file |

## Mechanism
None in this version: the body and hook are one fixed part, and the screw comes in a later version. When it does, it is a
`screw` node turning on the hole's axis, and its travel covers the panel range above (the tip from 7.0 to 2.0 out of the body),
so the clamp closes on every panel it takes.

## Named nodes
None (one fixed body). Collider `body` (the body and hook).

## Materials by layer
`M-ZINC` the body and hook (steel, zinc-plated).

## Notes
No vendor names, part numbers or marks. No label (the part is too small to carry one). No clamping-force or safety claim. No
open figure: the thread is derived (What it meets). The rest are design choices.

## Outputs (out/)
`panel-clamp.lsp` · `.glb` (one body, no pivot) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r58, unattended; request mech-5's answer) |
| 1.1 | text only, the part unchanged (mech-r67, unattended; review panel-clamp-1.0 finding 1): the tapped hole's M4 given as a plain design choice (the 8-wide body's 2.0 of wall each side), no clearance-hole table cited for it; properties.csv names the screw as spec.md does ("an M4 screw", its type not chosen); behaviour.csv added (lib/behaviour.md: no terminal, no moving node, no state) |
| 1.2 | text only, the part unchanged (mech-r88, unattended; re-read panel-clamp-1.1 finding 1, review mech-r85 finding 1): properties.csv's thread_form row holds the derived M4 figures with their source (as What it meets has since mech-r85); element.py's header, BASELINE and comment and this file's Baseline and Notes lines say the thread is derived, no longer an open figure |
