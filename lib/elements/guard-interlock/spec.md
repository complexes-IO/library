# guard-interlock · v1.0 · position switch with guard locking, tongue actuator, 2 N.C. safety contacts, 24 V DC solenoid release (complexes.org generic)

**What** Interlocking device with guard locking for a movable guard (a machine door): the switch is fixed to the machine's frame and its separate tongue actuator to the guard. With the guard shut the tongue sits in the slot of the switch's head; a spring-applied bolt inside the head holds it there (guard locking), and a 24 V DC solenoid A1-A2 pulls the bolt back while it is powered (power to unlock). Two N.C. safety contacts tell the control system where the guard is: 11-12 is closed while the actuator is in, 21-22 while the actuator is in and locked; withdrawing the actuator or releasing the lock opens them. Rated AC-15 2 A at 230 V and DC-13 1 A at 24 V each contact. A plastic housing 40 × 40 × 92 with two M5 fixing holes, a terminal compartment with six screw clamps behind a front cover and an M20 × 1.5 cable entry in its base, under a 30 high head. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002593 "Position switch with guard locking", built to the class values below; no maker's datasheet and no product is matched (the folder's earlier stub was not used: references/source.txt).
**Class** device · **Baseline** our own design: generic Position switch with guard locking (ETIM 10.0 EC002593). The class values are this element's definition (design inputs); the fixing holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1); the housing, head and actuator sizes are design choices, said so below. The interlocking standard (ISO 14119: actuator coding, guard locking principles, the release functions) and the contact standard (IEC 60947-5-1, positive opening in its Annex K) are not in lib/standards/sources.csv: nothing is taken from them and no conformity with either is claimed.
**Safety** A safety-function class (lib/inventory.csv: safety yes). The element is held at station 7 for EM's safety sign-off at this version (OPERATING.md 13); an unattended run builds it and proposes nothing more (lib/needs-em/elec.md r48).
**Units / frame** mm, Z up. Origin: the housing's back (mounting) face y = 0, x = 0 the centreline, z = 0 the base's bottom face (cable entry), body toward −y (in a BOM, the machine's frame at y = 0 and the guard closing toward +y onto the head's front face).
**Built with** toolkit 1.3 · AutoLISP command `GUARDLK` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC002593 Position switch with guard locking)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | With status indication (EF001602) | no (no LED: the led element is not built) |
| 2 | Suitable for safety functions (EF001597) | yes (the class's purpose; held for EM's safety sign-off) |
| 3 | Guard locking force (EF007552) | 1000 N |
| 4 | With escape release (EF007172) | no |
| 5 | Type of guard locking (EF012608) | spring force locking, released by the solenoid (power to unlock) |
| 6 | With auxiliary release (EF011964) | no |
| 7 | Rated control supply voltage magnet drive AC 50 Hz (EF007068) | not stated |
| 8 | Rated control supply voltage magnet drive AC 60 Hz (EF007069) | not stated |
| 9 | Rated control supply voltage magnet drive DC (EF007070) | 24 V |
| 10 | Width sensor (EF007094) | 40 mm (the housing and head; the actuator block 32 inside it) |
| 11 | Height of sensor (EF007283) | 122 mm (housing 92 and head 30) |
| 12 | Length of sensor (EF007334) | 54 mm with the actuator in (housing 40, gap 4, actuator block 10) |
| 13 | Number of safety auxiliary contacts (EF006940) | 0 |
| 14 | Number of contacts as normally closed contact (EF008255) | 2 (11-12, 21-22) |
| 15 | Number of contacts as normally open contact (EF008256) | 0 |
| 16 | Number of contacts as change-over contact (EF008257) | 0 |
| 17 | Type of switching contact (EF003591) | slow action; the N.C. contacts designed to be opened positively by the actuator's withdrawal (no conformity with IEC 60947-5-1 Annex K is claimed: not on file) |
| 18 | Rated operation current Ie at AC-15, 24 V (EF007084) | not stated |
| 19 | Rated operation current Ie at AC-15, 125 V (EF007082) | not stated |
| 20 | Rated operation current Ie at AC-15, 230 V (EF001385) | 2 A, each contact |
| 21 | Rated operation current Ie at DC-13, 24 V (EF007087) | 1 A, each contact |
| 22 | Rated operation current Ie at DC-13, 125 V (EF007085) | not stated |
| 23 | Rated operation current Ie at DC-13, 230 V (EF001386) | not stated |
| 24 | Construction type housing (EF004008) | rectangular, with a separate tongue actuator, own design layout (Dimensions) |
| 25 | Housing material (EF001596) | plastic (glass-fibre-reinforced polyamide) |
| 26 | Coating housing (EF001601) | none |
| 27 | Type of interface (EF006977) | none (contacts only) |
| 28 | Type of interface for safety communication (EF003956) | none |
| 29 | Type of electric connection (EF003961) | screw connection, cable entry M20 × 1.5 |
| 30 | Explosion safety category for gas (EF003997) | none |
| 31 | Explosion safety category for dust (EF003998) | none |
| 32 | Ambient temperature during operating (EF007515) | −20 … +55 °C |
| 33 | Degree of protection (IP) (EF005474) | not stated (no cover or entry seal is modelled) |
| 34 | Degree of protection (NEMA) (EF011959) | not stated |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the ones the checks may read (status "generic design", source "ETIM 10.0 EC002593 class value"), and the solenoid's power as the designer's figure (Notes); `pins.csv` gives each terminal its role.

## Switching program
| guard | actuator | lock (solenoid A1-A2) | 11-12 (N.C.) | 21-22 (N.C.) |
|---|---|---|---|---|
| shut and locked | in | locked (off) | closed | closed |
| shut, lock released | in | released (24 V DC on) | closed | open |
| open | withdrawn | either | open | open |

A control system starts the machine's hazardous motion only with both contacts closed and powers the solenoid only when the motion has stopped; that logic is the machine's (a safety relay or a safety controller), not this element's. The actuator's travel to the contacts' operating points is not stated: the twin reads only the states (behaviour.csv). The 40 mm withdrawal modelled is a design choice, the tongue then clear of the head.

## Dimensions
| item | value | source |
|---|---|---|
| housing | 40.0 × 40.0 × 92.0 (x ±20, y −40 … 0, z 0 … 92), back face y 0 the mounting face | design choice |
| base | z 0 … 10, full section; the cable entry up through it | design choice |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis at x 0, y −20, through the base (z 0 … 10) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| terminal compartment | x ±16, y −37 … −4, z 10 … 80, between two 4.0 side walls, a 4.0 back wall and a 3.0 front cover (y −40 … −37) | design choice |
| terminals | six screw clamps on the back wall's front face (y −4): heads Ø4.4 × 1.2, 11 at (x −8, z 66), 12 at (−8, 46), 21 at (0, 66), 22 at (0, 46), A1 at (8, 66), A2 at (8, 46); conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions a design choice; the marks a design choice (the safety contacts 11-12 and 21-22, line side odd; the solenoid A1-A2); the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| top block | z 80 … 92, full section | design choice |
| fixing holes (switch) | two Ø5.5 through the top block (y 0 … −40) at x ±12, z 86; position Ø0.5 to A (back face), B and C (the holes) | ISO 273 medium clearance for M5 (lib/standards/holes.csv); pattern and tolerance design choices; Ø0.5 ≤ H − F = 5.5 − 5.0 (GDT-010, features.csv) |
| head | 40.0 × 40.0 × 30.0 (z 92 … 122) | design choice |
| actuator slot | 14 × 8 (x ±7, z 103 … 111) in the head's front face, 25 deep (y −40 … −15) | design choice (1 clear of the tongue each side, 2 at its floor) |
| actuator | tongue 12 × 6 (x ±6, z 104 … 110) from the block's back face (y −44) to its tip at y −17; mounting block 32 × 10 × 18 (x ±16, y −54 … −44, z 98 … 116), 4 in front of the head with the guard shut; slides 0 … 40 toward −y as the guard opens | design choice |
| fixing holes (actuator) | two Ø5.5 through the block (y −44 … −54) at x ±11, z 107, into the guard's tapped holes; an M5 ISO 4762 head (Ø8.5) seats beside the tongue (x 6.75 … 15.25); position Ø0.5 as the switch's pair | ISO 273 medium clearance for M5 (lib/standards/holes.csv); pattern and tolerance design choices (GDT-010, features.csv) |
| label field | 0.6 × 24 × 18 on the cover (x ±12, y −40.6 … −40, z 20 … 38) | design choice |
| overall | 40.0 × 54.0 (y −54 … 0) × 122.0 (z 0 … 122), actuator in | from the parts above |

## Named nodes
`actuator` (translate 0 … 40 toward −y from (0, −44, 107): the tongue and its mounting block, fixed to the guard) · ports `t-11`, `t-12`, `t-21`, `t-22`, `t-A1`, `t-A2` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries.

## Materials by layer
`M-GREY-PA` housing, base, walls, cover, top block · `M-YELLOW-PA` head · `M-SILVER` tongue · `M-ZINC-CAST` actuator's mounting block · `M-ZINC` terminal screw heads · `M-WHITE-PA` label field (the holes and the slot are cuts, no layer of their own). The head's yellow is an appearance choice (class C), no colour code is claimed.

## Decals (Blender)
On the label field: "complexes.org generic", "guard-interlock", "2 NC 11-12 · 21-22", "A1-A2 24 V DC unlock", "AC-15 2 A 230 V · DC-13 1 A 24 V". The contact symbols (two N.C.) beside the marks. No maker's name, logo or approval mark.

## Notes
- Two open lines of the element's own, both class B under one document (lib/standards/wanted.md), not EM's: the screw clamps' conductor range and tightening torque (Dimensions), and the solenoid's operating limits, pick-up and drop-out, NOT ON FILE (B): IEC 60947-1 (behaviour.csv's `released` row reads any solenoid voltage as released until it is on file). Every rating is a class value (design input), every size a design choice, the holes ISO 273 on file, the entry thread derived. Nothing is guessed and shown as sourced.
- The solenoid's power, 6 W at 24 V DC (0.25 A), is not a class feature: the designer's figure for the panel's 24 V budget (ELR-020), in ratings.csv (coil_p design, load_i derived) and behaviour.csv's load row A1-A2.
- Safety: the class's purpose is a safety function, and what makes this a safety-rated device (the actuator's coding, the guard locking principle and its monitoring, positive opening, the release functions) is ISO 14119's and IEC 60947-5-1's, neither on file. The element claims the class values above and the switching program, nothing more; EM's safety sign-off is asked in lib/needs-em/elec.md r48.
- Not placed: receptacle-m12 (the inventory's made_of; built but not past station 6, so this version has the cable-entry form, as limit-switch; a connector version is a later major), the four screw-iso4762 (not built: the holes are modelled), the installer's cable gland in the M20 entry, and the mechanism inside the head (the bolt, the solenoid, the contact block). Nothing is modelled that a later element will place.
- The id: the inventory's row is `guard-interlock`; the id convention (OPERATING.md 6) would add the form and the contacts (guard-interlock-lock-2nc). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r48.

## Outputs (out/)
`guard-interlock.lsp` · `.glb` (pivots on the actuator and the six terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r48 (lib/rounds/elec/r48.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r48 (2026-11-13, unattended): first build, generic ETIM 10.0 EC002593, our own design; inventory elec 15 systems |
