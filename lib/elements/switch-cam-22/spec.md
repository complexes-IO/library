# switch-cam-22 · v1.1 · control switch 1-0-2, 2 poles, 10 A, knob on a 48 × 48 front shield, 22.5 mm front mounting (complexes.org generic)

**What** Control switch (cam switch) for control circuits: a knob with three maintained positions, 1-0-2, on a 48 × 48 front shield, mounted from the front through the 22.5 mm cut-out, with a stack of two contact chambers behind the panel (one pole each) and screw terminals. Position 1 closes 1-2 and 5-6, position 2 closes 3-4 and 7-8, position 0 leaves every contact open: a hand-off-auto or forward-off-reverse selection in a control circuit. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002611, built to the class values below; no maker's datasheet and no product is matched.
**Class** operator-22 · **Baseline** our own design: generic Control switch (ETIM 10.0 EC002611). The class values are this element's definition (design inputs); the Ø22.5 cut-out and the Ø30 × 8 mounting latch are the library's 22 mm contract (toolkit/std22.py `CUTOUT`, `LATCH`; the cut-out window Ø22.3 … 22.7 in lib/standards/holes.csv, "22.5 operator cut-out"); every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: panel device: the cut-out centre on the panel's front face; the panel occupies 0 ≤ y ≤ panel_t; the knob toward −y (the std22 operator frame). The host cuts the Ø22.5 hole (`CUTOUT`, library.mount).
**Built with** toolkit 1.3 · AutoLISP command `SWCAM` · parameters `panel_t` (3.0: the panel the body passes through), `position` (0: the knob at 0; 1 or 2 build it turned to that position).

## Class values
ETIM 10.0 EC002611 "Control switch", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Type of switch (EF003496) | changeover switch, 1-0-2 (control switch) |
| 2 | Number of poles (EF001391) | 2 (one contact chamber each; each pole has a contact for position 1 and one for position 2) |
| 3 | Max. rated operation voltage Ue AC (EF007355) | 440 V |
| 4 | Rated permanent current Iu (EF001389) | 10 A (each contact) |
| 5 | Number of switch positions (EF000231) | 3 (1, 0, 2) |
| 6 | With zero (off) position (EF001416) | yes (position 0: every contact open) |
| 7 | With retraction in 0-position (EF002428) | no (maintained in every position) |
| 8 | Device construction (EF008240) | built-in device, front mounting through a Ø22.5 hole |
| 9 | Width in number of modular spacings (EF002950) | not stated (not a distribution-board device) |
| 10 | Suitable for floor mounting (EF025108) | no |
| 11 | Suitable for front mounting (EF020288) | yes |
| 12 | Suitable for distribution board installation (EF007262) | no |
| 13 | Suitable for intermediate mounting (EF007264) | no |
| 14 | Complete device in housing (EF007317) | no |
| 15 | Type of control element (EF006976) | knob with thumb grip and pointer |
| 16 | Front shield size (EF007176) | 48 × 48 mm |
| 17 | Degree of protection (IP), front side (EF003118) | not stated (no front seal is designed or tested in 1.0) |
| 18 | Degree of protection (NEMA), front side (EF011961) | not stated (as 17) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design", source "ETIM 10.0 EC002611 class value" with the feature code, OPERATING.md 12); `pins.csv` gives each terminal its role.

## Switching program
| position | knob angle (about +y, clockwise seen from the front) | closed | open |
|---|---|---|---|
| 1 | −45° (pointer at 10:30) | 1-2, 5-6 | 3-4, 7-8 |
| 0 | 0° (pointer up) | none | all |
| 2 | +45° (pointer at 1:30) | 3-4, 7-8 | 1-2, 5-6 |

Odd terminals are each contact's line side (`sw-com`), even terminals its load side (`sw-no`: open at 0). A common feed to both contacts of a pole is a jumper the panel wiring adds (1 to 3, 5 to 7). The 45° step is a design choice.

## Dimensions
| item | value | source |
|---|---|---|
| cut-out | Ø22.5 in the host panel, cut by the host | toolkit/std22.py `CUTOUT` (lib/standards/holes.csv "22.5 operator cut-out", Ø22.3 … 22.7) |
| front shield | 48.0 × 48.0 (x, z) × 3.0 (y −3.0 … 0), on the panel face | design choice (Class values 16) |
| knob | base Ø32.0 × 4.0 on the shield (y −3 … −7); thumb grip 8.0 × 32.0 × 12.0 deep (y −7 … −19); white pointer inlay 2.0 × 7.0 at the grip's upper end, 0.2 proud | design choice |
| body through the cut-out | Ø22.0 × panel_t (y 0 … panel_t) | design choice: 0.3 under the cut-out's smallest Ø22.3 (holes.csv), so it never bears on the panel |
| mounting latch | Ø30.0 × 8.0 behind the panel (y panel_t … panel_t + 8) | toolkit/std22.py `LATCH` (the library's 22 mm contract) |
| panel thickness | `panel_t`, 3.0 built; 1.0 … 6.0 the latch's design range | design choice, the same range as std22 `PANEL_RANGE` so the hosts' mates (lib/mates.csv) hold for it as for the other 22 mm operators |
| contact chambers | two, each 32.0 (x) × 15.0 (y) × 40.0 (z), stacked behind the latch (y panel_t + 8 … panel_t + 38) | design choice |
| terminals | four screw clamps per chamber, two on the top face and two on the bottom, at x ±8.0, centred on the chamber's depth; screw heads Ø4.4 × 1.2; wire entries 5.0 (y) × 4.0 (z) slots cut 0.5 into the side faces, 4.5 in from the top and bottom | design choice (the shape of toolkit/din.py `terminal_row`, with a port node per terminal) |
| anti-rotation | the key or tab that keeps the body from turning in the cut-out under the knob's torque | NOT ON FILE (B): toolkit/std22.py and lib/standards/holes.csv give the Ø22.5 cut-out only, not the notch (width, depth, clocking) a 22 mm device keys into; no tab is modelled, so in 1.0 the latch's clamping alone holds the body |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, and the screw's thread and torque | NOT ON FILE (B): a fit with the wire element; the clamp's connecting capacity is set by IEC 60947-1 (terminals), which is not on file (lib/standards/sources.csv), so no size is claimed |
| overall | 48.0 × 60.2 (y −19.2 … 41.0) × 48.0 at panel_t 3.0 | from the parts above |

Terminal marks are numbers per contact (odd line, even load), a design choice printed beside each screw; the marking standard (IEC 60947-1) is not on file.

## Named nodes
`self` (rotate about +y through the shield face's centre, −45 … +45°: the knob; −45 = position 1, 0 = position 0, +45 = position 2; maintained, no spring) · ports `t-1` … `t-8` (kind port, unit screw, gender none: a screw clamp, PIN-002; axis +z on the top face, −z on the bottom). The twin turns `self` to the position it reads and closes the contacts by the switching program; pins.csv names what each terminal carries.

## Materials by layer
`M-BLACK-PA` front shield, knob, body and latch · `M-GREY-PA` contact chambers · `M-ZINC` terminal screws · `M-GASKET` wire entries · `M-WHITE-PA` the knob's pointer inlay

## Decals (Blender)
On the front shield, around the knob: "1" at 10:30, "0" at 12:00, "2" at 1:30. On a chamber's side face: "complexes.org generic", "switch-cam-22", "440 V~ 10 A", and the switching program (the table above, as a diagram). Terminal numbers beside each screw. No maker's name, logo or approval mark.

## Notes and open figures
- Two fits are open, both class B: the anti-rotation feature and the clamps' conductor range (the Dimensions rows above). Everything else this element meets is on file (the cut-out, the latch), and every other size is a design choice; nothing is guessed and shown as sourced.
- The cam shaft, cams and contact bridges inside the chambers, the detent and the switching capacity per utilization category are not modelled or stated in 1.0 (no utilization category is a feature of the class); the twin takes the contact state from the knob's position.
- Not a safety-function device: a control-circuit selector, not an emergency stop or an enabling device; no safety function rests on it here.

## Outputs (out/)
`switch-cam-22.lsp` · `.glb` (pivots on the knob and the eight ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at 1.1 (lane round elec-r19).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002611), our own design; built in the cloud by the core chat's builder for lane elec (2026-11-07, round 2) |
| 1.1 | ratings.csv: the four class-value rows to status "generic design" and source "ETIM 10.0 EC002611 class value: <feature> (EFnnnnnn)", OPERATING.md 12's form (review cloud-elec 2026-11-07 r2, finding 1); no shape, node or figure change; gated on the PC (elec-r19, 2026-11-08) |
