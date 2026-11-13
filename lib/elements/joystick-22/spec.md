# joystick-22 · v1.1 · joystick control switch, 2 directions (up / down), spring return, 1 NO per direction, 22.5 mm front mounting (complexes.org generic)

**What** Joystick control switch for jog and hoist controls: a lever that tilts up or down from its centre position and springs back to 0 when released, one normally open contact per direction (13-14 up, 23-24 down), mounted from the front through the 22.5 mm cut-out like the library's other 22 mm operators, with a legend plate, a metal front ring with a fork that keeps the lever in its one plane, and two contact blocks with screw terminals behind the panel. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000632, built to the class values below; no maker's datasheet and no product is matched.
**Class** operator-22 · **Baseline** our own design: generic Control switch, Joystick (ETIM 10.0 EC000632). The class values are this element's definition (design inputs); the Ø22.5 cut-out, the legend plate, the Ø29.7 front ring, the Ø30 × 8 latch and the 22 × 30 × 25 contact blocks are the library's 22 mm contract (toolkit/std22.py `CUTOUT`, `LEGEND`, `BEZEL`, `LATCH`, `BLOCK`, and `legend()` / `bezel()`; the cut-out window Ø22.3 … 22.7 in lib/standards/holes.csv, "22.5 operator cut-out"); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: panel device: the cut-out centre on the panel's front face; the panel occupies 0 ≤ y ≤ panel_t; the lever toward −y (the std22 operator frame). The host cuts the Ø22.5 hole (`CUTOUT`, library.mount).
**Built with** toolkit 1.3 · AutoLISP command `JOY22` · parameters `panel_t` (3.0: the panel the body passes through), `legend` (true: the legend plate under the ring), `tilt` (0: the lever at 0; −20 builds it up, +20 down).

## Class values
ETIM 10.0 EC000632 "Control switch, Joystick", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Rated operation current Ie at AC-21, 400 V (EF002417) | 6 A (each contact) |
| 2 | Centre mounting, hole diameter (EF002424) | 22.5 mm (toolkit/std22.py `CUTOUT`) |
| 3 | Joy stick length (EF006524) | 50 mm (the front ring's face to the knob's tip) |
| 4 | Number of actuation directions (EF002425) | 2 (up, down) |
| 5 | Number of switch positions (EF000231) | 3 (up, 0, down) |
| 6 | Number of normally open contacts per actuation direction (EF002427) | 1 |
| 7 | Number of normally closed contacts per actuation direction (EF008263) | 0 |
| 8 | Number of make-and-break contacts per direction (EF005599) | 0 |
| 9 | With retraction in 0-position (EF002428) | yes (spring return to 0 from either direction) |
| 10 | Locking in 0-position (EF006283) | no |
| 11 | Coder (EF005666) | no |
| 12 | Analogue output signal configurable (EF003236) | no |
| 13 | With front ring (EF006014) | yes |
| 14 | Material front ring (EF005972) | metal (zinc) |
| 15 | Colour front ring (EF002429) | silver (bright metal) |
| 16 | Degree of protection (IP) (EF005474) | not stated (no lever seal or boot is designed or tested in 1.0) |
| 17 | Degree of protection (NEMA) (EF011959) | not stated (as 16) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design", source "ETIM 10.0 EC000632 class value" with the feature code, OPERATING.md 12); `pins.csv` gives each terminal its role.

## Switching program
| lever | tilt (about +x through the hub) | closed | open |
|---|---|---|---|
| up | −20° (the knob rises) | 13-14 | 23-24 |
| 0 (released) | 0° | none | both |
| down | +20° (the knob drops) | 23-24 | 13-14 |

The lever springs back to 0 from either side (Class values 9); the travel of 20° each way is a design choice. Two actuation directions on one axis are the class value of 1.0: a four-direction version needs the lever to tilt about two axes, which one rotate pivot does not carry (a node's pivot has one axis, `P.pivot(node, kind, origin, axis, range)`, lib/README.md), so it is a later version, not a figure left open here.

## Dimensions
| item | value | source |
|---|---|---|
| cut-out | Ø22.5 in the host panel, cut by the host | toolkit/std22.py `CUTOUT` (lib/standards/holes.csv "22.5 operator cut-out", Ø22.3 … 22.7) |
| legend plate | 30.0 × 50.0 × 1.0 on the panel face (y −1 … 0, z −32.5 … 17.5), its own Ø22.5 hole | toolkit/std22.py `LEGEND`, `legend()` |
| front ring | Ø29.7, 3.0 proud of the legend plate (y −1 … −4) | toolkit/std22.py `BEZEL`, `bezel()` |
| the ring's bore | Ø12.0, behind the lever's hub (features.csv: lever linkage bore) | design choice |
| fork | two cheeks 3.5 (x ±6.5 … ±10.0) × 10.0 (y −4 … −14) × 12.0 (z −6 … 6) on the ring's face: the gate of the lever's one plane | design choice |
| lever | hub Ø9.0 × 12.0 along x, its axis 5.5 in front of the ring's face (y −9.5), 0.5 clear of each cheek and 1.0 of the ring; rod Ø6.0 from the hub's axis; knob Ø16.0 × 12.0 at 30.5 … 42.5 from the axis, cap Ø12.0 × 2.0 to the tip at 44.5 (y −54.0) | design choice |
| travel | ±20° about +x through the hub's axis | design choice |
| body through the cut-out | Ø22.0 from the legend plate's face to the panel's back (y −1 … panel_t) | design choice: 0.3 under the cut-out's smallest Ø22.3 (holes.csv), so it never bears on the panel |
| mounting latch | Ø30.0 × 8.0 behind the panel (y panel_t … panel_t + 8) | toolkit/std22.py `LATCH` |
| panel thickness | `panel_t`, 3.0 built; 1.0 … 6.0 the latch's design range | design choice, the same range as std22 `PANEL_RANGE` so the hosts' mates (lib/mates.csv) hold for it as for the other 22 mm operators |
| contact blocks | two, 22.0 × 30.0 deep × 25.0, behind the latch (y panel_t + 8 … panel_t + 38): 13-14 centred on the axis (z −12.5 … 12.5), 23-24 below it with 1.0 between (z −38.5 … −13.5) | toolkit/std22.py `BLOCK` and its place in `behind()` |
| terminals | two screw clamps per block on its back face at x ±6.0, 4.0 above the block's centre: heads Ø4.4 × 1.5 (as std22 `behind()` draws them); wire entries 5.0 (y) × 4.0 (z) slots cut 0.5 into the side faces, 4.5 in front of the back face | heads: toolkit/std22.py; entries: design choice |
| anti-rotation | the key or tab that keeps the body from turning in the cut-out | NOT ON FILE (B): toolkit/std22.py and lib/standards/holes.csv give the Ø22.5 cut-out only, not the notch (width, depth, clocking) a 22 mm device keys into; no tab is modelled, so in 1.0 the latch's clamping alone holds the body and keeps the fork's plane vertical |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screw's thread and torque | NOT ON FILE (B): a fit with the wire element; the clamp's connecting capacity is set by IEC 60947-1 (terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| overall | 30.0 × 96.5 (y −54.0 … 42.5) × 56.0 (z −38.5 … 17.5) at panel_t 3.0 | from the parts above |

Terminal marks follow the function-number convention of IEC 60947-1 (13-14 the first N.O. contact, 23-24 the second); the marks are labels, a design choice; the standard itself is not on file.

## Named nodes
`self` (rotate about +x through the hub's axis (0, −9.5, 0), −20 … +20°: the lever with its hub, rod, knob and cap; −20 = up, 0 = released, +20 = down; spring return to 0) · ports `t-13`, `t-14`, `t-23`, `t-24` (kind port, unit screw, gender none: a screw clamp, PIN-002; axis +y). The twin tilts `self` to the direction it reads and closes that direction's contact by the switching program; pins.csv names what each terminal carries.

## Materials by layer
`M-BLACK-PA` legend plate, lever, body, latch and contact blocks · `M-ZINC` front ring, fork and terminal screws · `M-GASKET` the ring's bore and the wire entries

## Decals (Blender)
On the legend plate: an up arrow above the ring and a down arrow below it, and "complexes.org generic". On a contact block's side face: "joystick-22", "13-14 up, 23-24 down", "AC-21 400 V 6 A". Terminal marks beside each screw. No maker's name, logo or approval mark.

## Notes and open figures
- Two fits are open, both class B: the anti-rotation feature and the clamps' conductor range (the Dimensions rows above). Everything else this element meets is on file (the cut-out, legend plate, front ring, latch and blocks of std22), and every other size is a design choice; nothing is guessed and shown as sourced.
- The return spring, the hub's bearing pin and the linkage from the lever to the contact blocks are inside or behind the ring and are not modelled in 1.0; the hub rides on its pivot (MOT-010 sweeps the lever through ±20° clear of the fork and the ring).
- Not a safety-function device: a jog or hoist command, not an enabling device or an emergency stop; no safety function rests on it here.

## Outputs (out/)
`joystick-22.lsp` · `.glb` (pivots on the lever and the four ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at 1.1 (lane round elec-r19).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000632), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07, round 2) |
| 1.1 | ratings.csv: the four class-value rows to status "generic design" and source "ETIM 10.0 EC000632 class value: <feature> (EFnnnnnn)", OPERATING.md 12's form (review cloud-elec 2026-11-07 r2, finding 1); no shape, node or figure change; gated on the PC (elec-r19, 2026-11-08) |
