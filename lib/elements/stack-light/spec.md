# stack-light · v1.0 · signal tower, 3 continuous-light elements green / yellow / red, Ø50, 24 V DC (complexes.org generic)

**What** Signal tower (stack light) that shows a machine's state from across the floor: three light elements Ø50 stacked on a terminal base, green nearest the base, yellow in the middle, red on top, each lit steadily while 24 V DC is across its own terminal (1, 2, 3) and the common C. A plastic base 60 × 60 × 48 stands on the machine's surface on two ears with an M4 fixing hole each; the cable comes up through an M20 × 1.5 entry in the mounting face into a terminal compartment with four screw clamps behind a front cover. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001042 "Signal tower complete", built to the class values below; no maker's datasheet and no product is matched (the folder's earlier stub was not used: references/source.txt).
**Class** device · **Baseline** our own design: generic Signal tower complete (ETIM 10.0 EC001042). The class values are this element's definition (design inputs); the fixing holes are ISO 273 medium clearance for M4 (lib/standards/holes.csv); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1); the base, light element and cap sizes are design choices, said so below.
**Units / frame** mm, Z up. Origin: the base's bottom (mounting) face z = 0, x = 0 and y = 0 the tower's axis (the cable entry's axis), front cover toward −y (in a BOM, the machine's mounting surface at z = 0 and the cover toward the side a person reaches it from).
**Built with** toolkit 1.3 · AutoLISP command `STACKLT` · no parameters · places no element (Notes).

## Class values (ETIM 10.0 EC001042 Signal tower complete)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Number of signal tower elements (EF008260) | 3 |
| 2 | Function flashing light (EF001446) | no (a controller's output may switch an element on and off; the tower has no flasher of its own) |
| 3 | Function continuous light (EF001448) | yes, all three elements |
| 4 | Function revolving light (EF006525) | no |
| 5 | Colour light 1 (EF016679) | green (nearest the base) |
| 6 | Colour light 2 (EF016680) | yellow |
| 7 | Colour light 3 (EF016681) | red (on top) |
| 8 | Colour light 4 (EF016682) | none (three elements) |
| 9 | Colour light 5 (EF016683) | none (three elements) |
| 10 | Voltage type (operating voltage) (EF005294) | DC |
| 11 | Operating voltage AC 50 Hz (EF008206) | none (DC only) |
| 12 | Operating voltage AC 60 Hz (EF008207) | none (DC only) |
| 13 | Operating voltage DC (EF008208) | 24 V |
| 14 | Function acoustic (EF001447) | no |
| 15 | Loudness (EF000144) | none (no acoustic element) |
| 16 | Degree of protection (IP) (EF005474) | not stated (no cover or entry seal is modelled) |
| 17 | Degree of protection (NEMA) (EF011959) | not stated |
| 18 | Height (EF000040) | 176 mm (base 48, three elements of 40, cap 8) |
| 19 | Width (EF000008) | 100 mm (the base 60, an ear of 20 each side) |
| 20 | Depth (EF000049) | 60 mm (the base; the label field stands 0.6 proud of the cover) |
| 21 | Outer diameter (EF000015) | 50 mm (the light elements and the cap) |

These values are what the element claims: they are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the ones the checks may read (status "generic design", source "ETIM 10.0 EC001042 class value"); `pins.csv` gives each terminal its role. Each light element's power, 2.4 W (0.10 A at 24 V, derived; 7.2 W and 0.30 A with all three lit), is not a feature of the class: it is the designer's figure, chosen inside the panel's 24 V DC control supply (psu-24v-2a4's output, the 24 V budget ELR-020), written in ratings.csv as "design".

## Wiring
| terminal | carries | lit |
|---|---|---|
| C | the three elements' common 0 V | |
| 1 | green element +24 V DC | green while a voltage is across 1-C |
| 2 | yellow element +24 V DC | yellow while a voltage is across 2-C |
| 3 | red element +24 V DC | red while a voltage is across 3-C |

Each element is switched by itself (a controller's sourcing output per colour); any of them may be lit together. What each colour tells the operator is the machine's to define, not this element's (the colour code of indicators, IEC 60073, is not in lib/standards/sources.csv and nothing is taken from it); the order green, yellow, red from the base up is a design choice. The least voltage an element lights at is not a class value here: not stated, and the twin reads any voltage across an element as lit (behaviour.csv).

## Dimensions
| item | value | source |
|---|---|---|
| base | 60.0 × 60.0 × 48.0 (x ±30, y ±30, z 0 … 48), bottom face z 0 the mounting face | design choice |
| floor block | z 0 … 8, full section; the cable entry up through it on the tower's axis | design choice |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis at x 0, y 0, through the floor block (z 0 … 8) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| fixing ears | two, 20 × 60 × 8 (x ±30 … ±50, y ±30, z 0 … 8), one each side of the floor block | design choice |
| fixing holes | two Ø4.5 through the ears (z 0 … 8) at x ±40, y 0; position Ø0.5 to A (mounting face), B and C (the holes) | ISO 273 medium clearance for M4 (lib/standards/holes.csv); pattern and tolerance design choices; Ø0.5 ≤ H − F = 4.5 − 4.0 (GDT-010, features.csv) |
| terminal compartment | x ±26, y −27 … 26, z 8 … 40, between two 4.0 side walls, a 4.0 back wall (y 26 … 30) and a 3.0 front cover (y −30 … −27) | design choice |
| terminals | four screw clamps on the back wall's front face (y 26) at z 24: heads Ø4.4 × 1.2, C at x −15, 1 at −5, 2 at 5, 3 at 15; conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions and marks a design choice; the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| top block | z 40 … 48, full section; the light elements stand on it | design choice |
| light elements | three, Ø50 × 40 each, on the tower's axis: green z 48 … 88, yellow z 88 … 128, red z 128 … 168 | design choice |
| cap | Ø50 × 8 (z 168 … 176) | design choice |
| label field | 0.6 × 40 × 20 on the cover (x ±20, y −30.6 … −30, z 14 … 34) | design choice |
| overall | 100.0 (x ±50) × 60.6 (y −30.6 … 30) × 176.0 (z 0 … 176) | from the parts above |

## Named nodes
`lamp-green`, `lamp-yellow`, `lamp-red` (emissive 0 … 1: each light element's lens, lit by its own terminal) · ports `t-C`, `t-1`, `t-2`, `t-3` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries. Nothing moves.

## Materials by layer
`M-GREY-PA` base (floor block, ears, walls, cover, top block) · `M-LENS-GREEN`, `M-LENS-YELLOW`, `M-LENS-RED` the light elements · `M-BLACK-PA` cap · `M-ZINC` terminal screw heads · `M-WHITE-PA` label field (the holes are cuts, no layer of their own)

## Decals (Blender)
On the label field: "complexes.org generic", "stack-light", "24 V DC · C 0 V · 1 green · 2 yellow · 3 red". No maker's name, logo or approval mark.

## Notes
- The one open line is class B: the screw clamps' conductor range and tightening torque, a standard's table not on file (IEC 60947-1), asked for once in lib/standards/wanted.md. Every rating is a class value (design input), every size a design choice, the holes ISO 273 on file, the entry thread derived. Nothing is guessed and shown as sourced.
- Not a safety-function device: a signal tower informs, it guards nothing, and no rule on file reads its state as a safeguard.
- Not placed (OPERATING.md 12, quality at the source): the inventory's parts receptacle-m12 (not past station 6) and led (not built), so this is the cable-entry form with screw clamps and each light element is one lit node; screw-iso7380 (not built), so the two fixing holes stand open; the installer's cable gland or conduit fitting in the M20 entry. A later major can place the receptacle and the LEDs.
- No pole or tube between the base and the elements, no flashing or acoustic element: other members of the class, each its own element or a later parameter.
- The id: the inventory's row is `stack-light`; the id convention (OPERATING.md 6) would add the form and the size (for example stack-light-3-50-24vdc). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r55.
- The folder's earlier stub: references/source.txt keeps its record verbatim as the end block (its earlier source.txt and metadata.json, joined unread; OPERATING.md 6, DOC-007). The stub's validation.json stays in the folder: removing or moving a tracked file is refused to an unattended run (lib/needs-em/elec.md r47, r50).

## Outputs (out/)
`stack-light.lsp` · `.glb` (pivots on the three light elements and the four terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: Blender and Godot in elec-r55 (lib/rounds/elec/r55.md); the AutoCAD gate waits for AutoCAD to be opened on the PC (the lane's gate queue).

## History
| version | change |
|---|---|
| 1.0 | elec-r55 (2026-11-20, unattended): first build, generic ETIM 10.0 EC001042, our own design; inventory elec, 7 systems |
