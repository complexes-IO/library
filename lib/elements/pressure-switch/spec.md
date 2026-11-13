# pressure-switch · v1.0 · pressure switch for hydraulic oil, 1 change-over, 24 V DC, 20-200 bar (complexes.org generic)

**What** Pressure switch for a hydraulic line: oil at the stem's port pushes a piston against a set spring; as the pressure rises past the setting the change-over contact moves from 11-12 to 11-14, and it moves back once the pressure has fallen by the fixed differential. Rated 24 V DC; setting range 20 … 200 bar on rising pressure, maximum operating pressure 250 bar. The press-hydraulic machine's "pressure ok" switch (lib/assemblies/press-hydraulic/controls.csv row press_ok, a 24 V DC N.O. into an IEC 61131-2 type 3 input; hydraulic.csv: it tees off the P line at the HPU's gauge port, beside the gauge). A hex stem whose seat face meets the host's gauge port, a round sensing body, and a switch head with three screw clamps behind a front cover, an M20 × 1.5 cable entry in its side and a sealed cap over the setting screw on top. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000243 "Pressure switch", built to the class values below; no maker's datasheet and no product is matched (lib/inventory.csv row `pressure-switch`, own_design generic, pin 12).
**Class** device · **Baseline** our own design: generic Pressure switch (ETIM 10.0 EC000243). The class values are this element's definition (design inputs); the stem meets a host's gauge port as hyd-gauge 1.1's does (unit "hyd-port", its thread open, Notes); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1), as limit-switch 1.0's; the body, head and cap sizes are design choices, said so below.
**Units / frame** mm, Z up. Origin: the joint plane, the hex's seat face z = 0 on the stem's axis (x = y = 0); the host's port toward −z, the switch head up, its front cover toward −y (in a BOM: the host's gauge port node, the stem's axis along the port's).
**Built with** toolkit 1.3 · AutoLISP command `PRESSSW` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC000243 Pressure switch)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Suitable as guard (EF007239) | no |
| 2 | Suitable as 2-point controller (EF007226) | no (a fixed differential, no second setting) |
| 3 | Suitable as limiter (EF007228) | no |
| 4 | Max. operating pressure (EF020449) | 250000 hPa (250 bar) |
| 5 | Engaging pressure (EF007124) | 20 … 200 bar, set by the screw under the cap (the machine's setting is its own: press-hydraulic controls.csv) |
| 6 | Initial setting (EF001410) | not stated |
| 7 | Switch off pressure (EF007008) | 10 … 190 bar (the setting less the differential) |
| 8 | End setting (EF001411) | not stated |
| 9 | Pressure-switching differential (EF008261) | 10 bar, fixed |
| 10 | Max. test pressure (EF007365) | not stated |
| 11 | Bursting pressure (EF007080) | not stated |
| 12 | Medium temperature (EF007369) | −20 … +80 °C (hydraulic mineral oil, as press-hydraulic's HM 46) |
| 13 | Connection (EF000443) | male stem with a hex, into a host's gauge port |
| 14 | Thread size (EF022694) | not stated (open: Notes) |
| 15 | Rated voltage Ue at AC 50 Hz (EF007029) | not stated (no AC rating) |
| 16 | Rated voltage Ue at AC 60 Hz (EF007030) | not stated (no AC rating) |
| 17 | Rated voltage Ue at DC (EF007031) | 24 V |
| 18 | Initial value measuring range pressure (EF006812) | not stated (a switch, no measuring range) |
| 19 | End value measuring range pressure (EF007134) | not stated |
| 20 | Rated operation power at AC-3, 400 V (EF001364) | not stated |
| 21 | Switching capacity at AC-3, 240 V (EF001409) | not stated |
| 22 | Rated operation current Ie at AC-1, 400 V (EF001393) | not stated |
| 23 | Rated operation current Ie at AC-3, 400 V (EF001392) | not stated |
| 24 | Number of auxiliary contacts as normally open contact (EF001376) | 0 |
| 25 | Number of auxiliary contacts as normally closed contact (EF001377) | 0 |
| 26 | Number of auxiliary contacts as change-over contact (EF003531) | 1 (11-12 / 11-14) |
| 27 | Type of electric connection (EF003961) | screw connection, cable entry M20 × 1.5 |
| 28 | Number of normally closed contacts as main contact (EF001375) | 0 |
| 29 | Number of normally open contacts as main contact (EF001374) | 0 |
| 30 | Adjustable current range (EF008211) | not stated |
| 31 | With hand operation (EF007378) | no |
| 32 | With manual on/off switch (EF001408) | no |
| 33 | Electronic version (EF007132) | no (a piston, a spring and a microswitch) |
| 34 | With display (EF000458) | no |
| 35 | Explosion-proof (EF004663) | no |
| 36 | Degree of protection (IP) (EF005474) | not stated (no cover or entry seal is modelled) |
| 37 | Degree of protection (NEMA) (EF011959) | not stated |
| 38 | Height (EF000040) | 86 mm (seat face to the cap's top) |
| 39 | Width (EF000008) | 44 mm (the head) |
| 40 | Diameter (EF000551) | 32 mm (the sensing body) |
| 41 | Depth (EF000049) | 40.6 mm (the head with its label field) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the ones the checks may read (status "generic design", source "ETIM 10.0 EC000243 class value"); `pins.csv` gives each terminal its role.

## Switching program
| pressure at port-p | 11-12 | 11-14 |
|---|---|---|
| below the setting (and, falling, until the setting less 10 bar) | closed | open |
| risen past the setting | open | closed |

The contact's current is no class feature of EC000243: 2 A at 24 V DC, utilization category DC-13, is the design's figure (ratings.csv `ie_dc13_24v`, status "design"), the rating limit-switch 1.0's contacts carry; IEC 60947-5-1, which defines the category, is named and not on file. The PLC's input draws far less (IEC 61131-2 type 3, controls.csv). The twin reads the two states only (behaviour.csv): the electrical solver computes no pressure, so "above" is a manual toggle until the circuit model gives the pressure at the port, as hyd-gauge 1.1's pointer.

## Dimensions
| item | value | source |
|---|---|---|
| hex | 15 across flats × 9 (z 0 … 9), corners turned to 1.12 × AF (Ø16.8); zinc-plated steel; the node `port-p` | design choice, hyd-gauge 1.1's; Ø16.8 sits inside the Ø24 spot face of hpu-7.5kw's and hyd-cylinder-da-40's ports (asserted in element.py) |
| stem below the seat face | not drawn (Notes) | its thread and length are open, as hyd-gauge 1.1's |
| neck | Ø12 (z 8.5 … 13.5) | design choice |
| sensing body | Ø32 (z 13 … 42.5, 0.5 into the head) | design choice; the piston and spring inside are not modelled |
| switch head | 44 × 40 × 38 (x ±22, y ±20, z 42 … 80): bottom plate z 42 … 48, top plate z 74 … 80, side walls 4 (−x) and 8 (+x), back wall y 16 … 20, front cover y −20 … −17; the terminal compartment x −18 … 14, y −17 … 16, z 48 … 74 | design choice |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis along x at y 0, z 61, through the +x wall (x 14 … 22) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| terminals | three screw clamps on the back wall's front face (y 16): heads Ø4.4 × 1.2, 11 at (x −2, z 66), 12 at (−9, 55), 14 at (5, 55); conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions a design choice; the marks a design choice (a change-over's common 11, N.C. 12, N.O. 14, as the two-digit marks of limit-switch 1.0); the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| cap | Ø16 × 6 on the top plate (z 79.5 … 86), sealed over the setting screw | design choice |
| label field | 0.6 × 28 × 18 on the cover (x ±14, y −20.6 … −20, z 52 … 70) | design choice |
| overall | 44.0 × 40.6 (y −20.6 … 20) × 86.0 (z 0 … 86) | from the parts above |

## Named nodes
`port-p` (the hex: kind port, fixed, unit "hyd-port", gender male, role gauge, at the seat face z = 0, axis −z; as hyd-gauge 1.1's `port-1`, the host's gauge port `port-g` female) · ports `t-11`, `t-12`, `t-14` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries. Nothing moves.

## Materials by layer
`M-ZINC` hex and terminal screw heads · `M-SILVER` neck and sensing body · `M-GREY-PA` switch head (plates, walls, cover) · `M-BLACK-PA` cap · `M-WHITE-PA` label field (the entry is a cut, no layer of its own)

## Decals (Blender)
On the label field: "complexes.org generic", "pressure-switch", "1 CO 11-12 / 11-14 · 24 V DC 2 A", "20-200 bar · max. 250 bar". The change-over symbol beside the marks. No maker's name, logo or approval mark.

## Notes
- The stem's thread, size and length: NOT ON FILE (B): no hydraulic port standard, such as an ISO 6149 or SAE straight-thread port, is in lib/standards/sources.csv (as hyd-gauge 1.1's and hpu-7.5kw's ports), asked for once in lib/standards/wanted.md. No stub is drawn below the seat face; the seat face meets the host's port face to face. A major adds the stub once the standard is on file.
- The screw clamps' conductor range and torque: class B, IEC 60947-1 (Dimensions; behaviour.csv). Every rating is a class value (design input) or, for the contact's current, the design's figure; every size a design choice; the entry thread derived. Nothing is guessed and shown as sourced.
- Not a safety-function device: the PLC reads it as a process signal ("pressure ok"). A pressure monitor in a safety function needs a safety-class element and EM's sign-off.
- Not placed (OPERATING.md 12, quality at the source): the inventory row lists receptacle-m12 and led as its parts; neither is past station 6, so this version is the cable-entry form with screw clamps (as limit-switch 1.0), with no M12 receptacle and no switching LED. A later version may place them (a major: the terminals become the receptacle's contacts). The installer's cable gland in the M20 entry, and the piston, spring and microswitch inside, are not modelled.
- The id: the inventory's row is `pressure-switch`; the id convention (OPERATING.md 6) would add the medium and the contact (pressure-switch-hyd-1co). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r42.

## Outputs (out/)
`pressure-switch.lsp` · `.glb` (pivots on port-p and the three terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r42 (lib/rounds/elec/r42.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r42 (2026-11-12, unattended): first build, generic ETIM 10.0 EC000243, our own design; inventory elec pinned 12 |
