# limit-switch · v1.1 · end switch, roller lever, 1 N.C. + 1 N.O., AC-15 3 A 230 V (complexes.org generic)

**What** End (position) switch for a machine's end of travel: a roller lever on a rotary head swings ±45° in the front plane when a cam or dog on the moving part runs onto its roller; past its operating point the N.C. contact 11-12 opens and the N.O. contact 23-24 closes (slow action, break before make), and a return spring brings the lever back to rest. Rated AC-15 3 A at 230 V and DC-13 2 A at 24 V each contact. A plastic housing 30 × 30 × 80 with two M5 fixing holes, a terminal compartment with four screw clamps behind a front cover, and an M20 × 1.5 cable entry in its base. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000030 "End switch", built to the class values below; no maker's datasheet and no product is matched (the folder's earlier stub was not used: references/source.txt).
**Class** device · **Baseline** our own design: generic End switch (ETIM 10.0 EC000030). The class values are this element's definition (design inputs); the fixing holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1); the housing, head and lever sizes are design choices, said so below. The standard form of a position switch's housing and fixing pattern (EN 50047) is not in lib/standards/sources.csv and nothing is taken from it: this element claims no interchangeability with that form.
**Units / frame** mm, Z up. Origin: the housing's back (mounting) face y = 0, x = 0 the centreline, z = 0 the base's bottom face (cable entry), body toward −y (in a BOM, the machine's mounting face at y = 0 and the lever toward the moving part's cam).
**Built with** toolkit 1.3 · AutoLISP command `LIMITSW` · no parameters · places no element (the cable gland is the installer's: Notes).

## Class values (ETIM 10.0 EC000030 End switch)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Width sensor (EF007094) | 30 mm (the housing; the lever and roller stay inside it at rest) |
| 2 | Diameter sensor (EF007111) | not stated (a rectangular housing) |
| 3 | Height of sensor (EF007283) | 111 mm with the lever at rest (housing and head 80, lever and roller above) |
| 4 | Length of sensor (EF007334) | 48 mm (30 housing, 18 shaft, arm and roller in front of it) |
| 5 | Rated operation current Ie at AC-15, 24 V (EF007084) | not stated |
| 6 | Rated operation current Ie at AC-15, 125 V (EF007082) | not stated |
| 7 | Rated operation current Ie at AC-15, 230 V (EF001385) | 3 A, each contact |
| 8 | Rated operation current Ie at DC-13, 24 V (EF007087) | 2 A, each contact |
| 9 | Rated operation current Ie at DC-13, 125 V (EF007085) | not stated |
| 10 | Rated operation current Ie at DC-13, 230 V (EF001386) | not stated |
| 11 | Switching function (EF000189) | slow-action contacts, break before make |
| 12 | Switching function latching (EF007447) | no (the lever springs back) |
| 13 | Output electronic (EF006987) | no |
| 14 | Forced opening (EF006694) | no (no positive opening is claimed) |
| 15 | Number of safety auxiliary contacts (EF006940) | 0 |
| 16 | Number of contacts as normally closed contact (EF008255) | 1 (11-12) |
| 17 | Number of contacts as normally open contact (EF008256) | 1 (23-24) |
| 18 | Number of contacts as change-over contact (EF008257) | 0 |
| 19 | Type of interface (EF006977) | none (contacts only) |
| 20 | Type of interface for safety communication (EF003956) | none |
| 21 | Construction type housing (EF004008) | rectangular, own design layout (Dimensions) |
| 22 | Housing material (EF001596) | plastic (glass-fibre-reinforced polyamide) |
| 23 | Coating housing (EF001601) | none |
| 24 | Type of control element (EF006976) | roller lever |
| 25 | Alignment of the control element (EF008793) | on top of the head, swinging in the front plane, either way |
| 26 | Type of electric connection (EF003961) | screw connection, cable entry M20 × 1.5 |
| 27 | With status indication (EF001602) | no |
| 28 | Suitable for safety functions (EF001597) | no |
| 29 | Explosion safety category for gas (EF003997) | none |
| 30 | Explosion safety category for dust (EF003998) | none |
| 31 | Ambient temperature during operating (EF007515) | −25 … +70 °C |
| 32 | Degree of protection (IP) (EF005474) | not stated (no cover or entry seal is modelled) |
| 33 | Degree of protection (NEMA) (EF011959) | not stated |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones the checks may read (status "generic design", source "ETIM 10.0 EC000030 class value"); `pins.csv` gives each contact its role.

## Switching program
| lever | 11-12 (N.C.) | 23-24 (N.O.) |
|---|---|---|
| at rest, 0° (upright) | closed | open |
| actuated, past the operating point either way (up to ±45°) | open | closed |

The operating point's angle, the differential travel and the operating force are not class values here: not stated, and the twin reads only the two states (behaviour.csv). The lever's ±45° travel is a design choice.

## Dimensions
| item | value | source |
|---|---|---|
| housing | 30.0 × 30.0 × 60.0 (x ±15, y −30 … 0, z 0 … 60), back face y 0 the mounting face | design choice |
| base | z 0 … 10, full section; the cable entry up through it | design choice |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis at x 0, y −15, through the base (z 0 … 10) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| terminal compartment | x ±11, y −27 … −4, z 10 … 48, between two 4.0 side walls, a 4.0 back wall and a 3.0 front cover (y −30 … −27) | design choice |
| terminals | four screw clamps on the back wall's front face (y −4): heads Ø4.4 × 1.2, 11 at (x −5, z 36), 12 at (−5, 22), 23 at (5, 36), 24 at (5, 22); conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions a design choice; the marks a design choice (the N.C. contact 11-12, the N.O. contact 23-24, line side odd); the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| top block | z 48 … 60, full section | design choice |
| fixing holes | two Ø5.5 through the top block (y 0 … −30) at x ±8, z 54; position Ø0.5 to A (back face), B and C (the holes) | ISO 273 medium clearance for M5 (lib/standards/holes.csv); pattern and tolerance design choices; Ø0.5 ≤ H − F = 5.5 − 5.0 (GDT-010, features.csv) |
| rotary head | 30.0 × 30.0 × 20.0 (z 60 … 80) | design choice |
| lever | shaft Ø6 out of the head's front face (y −30 … −36) at z 70; arm 8 × 4 (x ±4, y −40 … −36, z 64 … 102); roller Ø18 × 8 (y −48 … −40) on the arm's front face, axis at z 102; swings ±45° about the shaft | design choice |
| label field | 0.6 × 20 × 16 on the cover (x ±10, y −30.6 … −30, z 28 … 44) | design choice |
| overall | 30.0 × 48.0 (y −48 … 0) × 111.0 (z 0 … 111) | from the parts above |

## Named nodes
`lever` (rotate −45 … +45° about the y axis at the head's shaft, (0, −30, 70): the shaft, arm and roller) · ports `t-11`, `t-12`, `t-23`, `t-24` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing, base, walls, cover, top block · `M-BLACK-PA` rotary head and roller · `M-ZINC-CAST` lever arm · `M-SILVER` lever shaft · `M-ZINC` terminal screw heads · `M-WHITE-PA` label field (the holes are cuts, no layer of their own)

## Decals (Blender)
On the label field: "complexes.org generic", "limit-switch", "1 NC 11-12 · 1 NO 23-24", "AC-15 3 A 230 V · DC-13 2 A 24 V". The contact symbols (one N.C., one N.O.) beside the marks. No maker's name, logo or approval mark.

## Notes
- The one open line is class B: the screw clamps' conductor range and tightening torque, a standard's table not on file (IEC 60947-1), asked for once in lib/standards/wanted.md. Every rating is a class value (design input), every size a design choice, the holes ISO 273 on file, the entry thread derived. Nothing is guessed and shown as sourced.
- Not a safety-function device: no forced (positive) opening of the N.C. contact is claimed (Class values 14 and 28). A guard interlock or an over-travel switch in a safety function needs a safety-class element and EM's sign-off.
- Not placed: the installer's cable gland in the M20 entry, and the contact block (springs, bridges, plunger) inside the head and the compartment. Nothing is modelled that a later element will place.
- The housing's form and fixing pattern follow no standard on file: EN 50047 (the small standard form of a position switch) is not in lib/standards/sources.csv. Claiming that form needs the standard, then a major version.
- The id: the inventory's row is `limit-switch`; the id convention (OPERATING.md 6) would add the form and the contacts (limit-switch-roller-1no1nc). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r40.
- The folder's earlier stub: references/source.txt keeps its record verbatim as the end block (its earlier source.txt and metadata.json, from git 4c33533a; OPERATING.md 6, DOC-007; review limit-switch-1.0 finding 1). The stub's validation.json stays in the folder: removing or moving a tracked file is refused to an unattended run (lib/needs-em/elec.md r47, r50).

## Outputs (out/)
`limit-switch.lsp` · `.glb` (pivots on the lever and the four terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r40 (lib/rounds/elec/r40.md); 1.1 in elec-r50 (lib/rounds/elec/r50.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r40 (2026-11-12, unattended): first build, generic ETIM 10.0 EC000030, our own design; inventory elec pinned 13 |
| 1.1 | elec-r50 (2026-11-13, unattended): text only (review limit-switch-1.0 / elec-r40 finding 3): references/source.txt keeps the earlier stub's record verbatim as its end block (source.txt and metadata.json from 4c33533a, joined unread); the stub's validation.json left in place (needs-em). Nodes, origin and cut-outs as 1.0 |
