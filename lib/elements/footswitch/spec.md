# footswitch · v1.0 · foot switch, guarded, single pedal, 1 N.C. + 1 N.O., AC-15 3 A 230 V (complexes.org generic)

**What** Foot switch for a machine an operator starts or holds with a foot while both hands guide the work (a press brake, a shear, a crimper, a welder's station): a single pedal under a protective hood, which the operator's foot presses 5° toe down; while it is held the N.C. contact 11-12 is open and the N.O. contact 23-24 closed (momentary: the return spring brings the pedal back when the foot lifts). Rated AC-15 3 A at 230 V each contact. A plastic housing 100 × 200 × 130 standing on the floor: base plate, two side walls and a top plate form the hood, open at the toe end for the foot; the heel holds a terminal compartment with four screw clamps and an M20 × 1.5 cable entry in its back wall. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC001258 "Foot switch", built to the class values below; no maker's datasheet and no product is matched (references/source.txt).
**Class** device · **Baseline** our own design: generic Foot switch (ETIM 10.0 EC001258). The class values are this element's definition (design inputs); the cable entry is M20 × 1.5, its minor diameter derived (ISO 68-1 / ISO 965-1); the housing, hood and pedal sizes are design choices, said so below.
**Units / frame** mm, Z up. Origin: the heel's back face y = 0, x = 0 the centreline, z = 0 the base's bottom face (the floor), the toe end and the hood's opening toward −y (in a BOM, set on the floor in front of the operator's station, the opening toward the operator).
**Built with** toolkit 1.3 · AutoLISP command `FOOTSW` · no parameters · places no element (the cable gland is the installer's: Notes).

## Class values (ETIM 10.0 EC001258 Foot switch)
Each feature of the class (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM 10.0) | value |
|---|---|---|
| 1 | Type of command (EF002399) | momentary, single stage (one pedal, one operating position) |
| 2 | With protection hood (EF002400) | yes (side walls and top plate over the pedal, open at the toe end) |
| 3 | With interlocking (EF002401) | no |
| 4 | Material (EF002169) | plastic (glass-fibre-reinforced polyamide) housing, hood and pedal; steel hinge pin |
| 5 | With protective insulation (EF006523) | not stated |
| 6 | Colour (EF000007) | yellow housing and hood, black pedal |
| 7 | Number of switch positions (EF000231) | 2 (rest, pressed) |
| 8 | Number of contacts as normally closed contact (EF008255) | 1 (11-12) |
| 9 | Number of contacts as normally open contact (EF008256) | 1 (23-24) |
| 10 | Number of contacts as change-over contact (EF008257) | 0 |
| 11 | Switching function latching (EF007447) | no (the pedal springs back) |
| 12 | Suitable for safety functions (EF001597) | no |
| 13 | Rated operation current Ie at AC-15, 230 V (EF001385) | 3 A, each contact |
| 14 | Degree of protection (IP) (EF005474) | not stated (no entry seal or contact enclosure is modelled) |
| 15 | Degree of protection (NEMA) (EF011959) | not stated |
| 16 | Width (EF000008) | 100 mm |
| 17 | Height (EF000040) | 130 mm (130.6 with the label field) |
| 18 | Depth (EF000049) | 200 mm |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones the checks may read (status "generic design", source "ETIM 10.0 EC001258 class value"); `pins.csv` gives each contact its role.

## Switching program
| pedal | 11-12 (N.C.) | 23-24 (N.O.) |
|---|---|---|
| at rest, 0° (up) | closed | open |
| pressed, 5° toe down | open | closed |

The operating point's angle, the differential travel and the operating force are not class values here: not stated, and the twin reads only the two states (behaviour.csv). The pedal's 5° travel is a design choice (the toe's underside comes down to z 18.3, clear of the base plate's top at z 12).

## Dimensions
| item | value | source |
|---|---|---|
| base plate | 100.0 × 200.0 × 12.0 (x ±50, y −200 … 0, z 0 … 12), the floor face z 0 | design choice |
| hood | side walls 8.0 thick (x ±42 … ±50, y −200 … 0, z 12 … 122); top plate 100.0 × 200.0 × 8.0 (z 122 … 130); open at the toe end (x ±42, z 12 … 122 at y −200) | design choice |
| heel compartment | x ±42, y −42 … −8, z 12 … 62, between the side walls, an 8.0 back wall (y −8 … 0), an 8.0 front wall (y −50 … −42) and an 8.0 cover (z 62 … 70) | design choice |
| cable entry | M20 × 1.5 tapped, modelled plain at D1 Ø18.376, axis along y at x 0, z 37, through the back wall (y −8 … 0) into the compartment | derived: derive.thread(20.0, 1.5) (ISO 68-1 basic profile, ISO 965-1 clause 10; 6H D1 18.376 … 18.682); features.csv |
| terminals | four screw clamps on the front wall's back face (y −42), toward +y: heads Ø4.4 × 1.2, 11 at (x −10, z 50), 12 at (−10, 30), 23 at (10, 50), 24 at (10, 30); conductor range and tightening torque NOT ON FILE (B): IEC 60947-1 | positions a design choice; the marks a design choice (the N.C. contact 11-12, the N.O. contact 23-24, line side odd); the clamp's figures a standard's table not on file (lib/standards/wanted.md) |
| pedal | 82.0 × 138.0 × 8.0 (x ±41, y −190 … −52, z 30 … 38), 1.0 clear of each side wall; turns 0 … 5° toe down about the hinge pin | design choice |
| hinge pin | Ø8 along x at y −56, z 34, from x −42 to 42, seated on the side walls' inner faces | design choice |
| label field | 60 × 60 × 0.6 on the top plate (x ±30, y −150 … −90, z 130 … 130.6) | design choice |
| overall | 100.0 × 200.0 × 130.6 | from the parts above |

## Named nodes
`pedal` (rotate 0 … 5° about the x axis at the hinge pin, (0, −56, 34): the plate and the pin; positive turns the toe down) · ports `t-11`, `t-12`, `t-23`, `t-24` (kind port, unit screw, gender none: screw clamps, PIN-002), on the terminal screw heads. pins.csv names what each terminal carries.

## Materials by layer
`M-YELLOW-PA` base plate, hood, heel walls and cover · `M-BLACK-PA` pedal · `M-SILVER` hinge pin · `M-ZINC` terminal screw heads · `M-WHITE-PA` label field (the entry is a cut, no layer of its own)

## Decals (Blender)
On the label field: "complexes.org generic", "footswitch", "1 NC 11-12 · 1 NO 23-24", "AC-15 3 A 230 V". The contact symbols (one N.C., one N.O.) beside the marks. No maker's name, logo or approval mark.

## Notes
- The one open line is class B: the screw clamps' conductor range and tightening torque, a standard's table not on file (IEC 60947-1), asked for once in lib/standards/wanted.md. Every rating is a class value (design input), every size a design choice, the entry thread derived. Nothing is guessed and shown as sourced.
- Not a safety-function device (Class values 12): no forced opening of the N.C. contact is claimed. The hood keeps a dropped object or a passing foot off the pedal; it is not a safeguard of the machine. A machine whose standard asks for a safety-rated foot control (an enabling or a three-position foot switch, a press's guarded start) needs a safety-class element and EM's sign-off.
- Not placed: the installer's cable gland in the M20 entry, the pedal's return spring, and the contact block (plunger, springs, bridges) in the heel. Nothing is modelled that a later element will place.
- The id: the inventory's row is `footswitch`; the id convention (OPERATING.md 6) would add the form and the contacts (footswitch-guarded-1no1nc). A rename is the library's on main (`build.py rename`), not the lane's: lib/needs-em/elec.md r46.

## Outputs (out/)
`footswitch.lsp` · `.glb` (pivots on the pedal and the four terminals, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r46 (lib/rounds/elec/r46.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r46 (2026-11-13, unattended): first build, generic ETIM 10.0 EC001258, our own design; inventory elec footswitch (21 systems) |
