# enc-wm · v1.4 · wall-mount enclosure, generic, 600 × 800 × 250, one door, mounting plate, two M20 entries

**What** A sheet-steel wall-mount enclosure for a machine's control panel: a box 600 wide, 800 high and 250 deep, open at the
front and closed by one flat door hinged at its left edge. Inside, a galvanised mounting plate on four studs carries the DIN rails,
ducts and devices a panel places. The cables come in from below, through two M20 cable-entry holes in the bottom; four M8 holes in
the back fix the box to the wall or a machine frame. Three M8 earth studs (1.3) are the ports where a panel's protective
conductors land: `pe-body` on the bottom's inner face beside the cable entries, `pe-door` on the door's inner face (it swings
with the door), `pe-plate` on the mounting plate's front face. Rails, ducts, devices and door operators are not part of this element: the
panel shop's assembly places them (OPERATING.md 14; lib/panel-types.csv names enc-wm for the motor-starter, vfd and plc-control
types).
**Class** enclosure · **Baseline** our own design: generic wall-mount enclosure (ETIM 10.0 EC000261), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07; the inventory row turned generic by the core on 2026-11-08). No product was matched and no vendor file
was opened. The folder's acquisition record (metadata.json, references/source.txt, validation.json) describes a catalogue box with
its inch sizes; no figure was taken from it: this box's sizes differ from it and are this lane's choices (below). The record stays
as it is.
**Units / frame** mm, Z up. Origin: the box's underside z = 0 at its front-left corner x = 0, y = 0. The back face y = 250 goes
against the wall; the person stands at −y; the door opens toward −y.
**Built with** toolkit 1.3 · AutoLISP command `ENCWM` · parameter `swing` (degrees, 0 by default, 0 to 110): the door and
what rides on it (its stud `pe-door`) built turned open by that angle, so an assembly can render and check the panel with its
door open (as enc-fs-1524x1829x305's swing_l / swing_r; request panel-7, lib/requests/core/mech-enc-wm-2026-11-11.md). The
default build (swing 0) is the 1.2 model with the three studs added.

## Class values
ETIM 10.0 class EC000261 Enclosure/cabinet (empty) (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Width (EF000008) | 600 mm (outside) |
| 2 | Height (EF000040) | 800 mm (outside) |
| 3 | Depth (EF000049) | 250 mm (outside, the door not included; 252 with the door closed) |
| 4 | Material (EF002169) | sheet steel, 2.0; the mounting plate galvanised steel, 2.5 |
| 5 | Material quality (EF001257) | not stated |
| 6 | Surface finishing (EF006569) | painted (body and door); the mounting plate zinc-coated |
| 7 | Colour (EF000007) | grey |
| 8 | RAL-number (EF000116) | 7035 |
| 9 | Freestanding (EF020363) | no |
| 10 | Floor standing wall model (EF015208) | no |
| 11 | Suitable for wall mounting (EF000664) | yes: four M8 fixing holes in the back |
| 12 | Corner model (EF020814) | no |
| 13 | Intermediate mounting (EF022994) | no |
| 14 | Couplable (EF001229) | no |
| 15 | With mounting plate (EF000118) | yes: 500 × 700 × 2.5 |
| 16 | Mounting plate depth-adjustable (EF006054) | no |
| 17 | Suitable for wall built-in (EF007536) | no |
| 18 | Pole fastening (EF009582) | no |
| 19 | With door (EF009169) | yes |
| 20 | Number of doors (EF000122) | 1 |
| 21 | With glazed door (EF001089) | no |
| 22 | With ventilation door (EF006279) | no |
| 23 | With rear door (EF007381) | no |
| 24 | Number of locks (EF000123) | 0 in this version (a latch is a later own design) |
| 25 | With cover (EF007965) | no |
| 26 | Transparent cover (EF011401) | no |
| 27 | Suitable for metrical mounting (EF005823) | not stated |
| 28 | Suitable for outdoor installation (EF011885) | no |
| 29 | Pitched roof (EF009278) | no |
| 30 | Number of connector holes (EF005554) | 2 (M20 cable entries, in the bottom) |
| 31 | Pre-stamping (EF001039) | no |
| 32 | EMC-version (EF001062) | no |
| 33 | Impact strength (EF004293) | not stated |
| 34 | Degree of protection (IP) (EF005474) | not stated: the door has no seal or latch in this version |
| 35 | Degree of protection (NEMA) (EF011959) | not stated |
| 36 | Thermal dissipation (Delta T = 20 K) according to IEC/TR 60890 (EF014986) | not stated |
| 37 | Max. permitted load of the enclosure according to IEC 62208 (EF014987) | not stated |
| 38 | Max. permitted load of the door(s) according to IEC 62208 (EF014988) | not stated |
| 39 | Max. permitted load of the mounting plate according to IEC 62208 (EF014989) | not stated |

## Mechanism
`door`: rotates about the box's front-left vertical edge (the line x = 0, y = 0, z up), 0 to −110° about +z, so its free (right)
edge swings outward (−y) and round to the left of the box. Closed, it lies over the front edges of the top, the bottom and the
sides (y −2 to 0, the full 600 × 800); through its travel every point of it stays at y ≤ 0 or x ≤ 0, outside the box, and away from
the wall behind the back. It is a host (2.0): door operators an assembly places cut through it. The hinge and the latch are not
modelled (later own designs; this box places them in a later version).
`back-panel`: the mounting plate, fixed. Origin its front-left-bottom corner (50, 230.5, 50). It is a host (2.5): what the panel
places is mounted on its front face, y = 230.5.
`swing` (parameter, 1.3): with swing > 0 the door is built as the same plate turned open by that angle about the hinge edge
(toward −y), its collider the axis-aligned box of that position, and `pe-door` turned with it; the `door` pivot and its range
(0 to −110 from the closed door) are the same at every swing, so the twin's door state is read from the closed position as
before. Operators an assembly places cut through the door in its closed build (swing 0), as enc-fs-1524x1829x305 does.
Port nodes (1.3, PIN-002 gender none, unit PE): `pe-body`, a stud up from the bottom's inner face at (100, 100), z 2 to 14, its
port face at the tip (z 14); `pe-door`, a stud into the box from the door's inner face at x 50, z 700, y 0 to 12 (a child of
`door`: it swings with the door and keeps its own pivot, as tensioner-belt 2.0's roll); `pe-plate`, a stud out of the plate's
front face at x 300, z 75, y 230.5 to 218.5 (a top-level node: the plate is fixed, so a child of it would move no differently;
the core's note asked for it inside `back-panel`, and the AutoCAD gate's glb reader places a nested node's mesh relative to its
parent's origin, request mech-12, which read this stud 12 outside the box: FAIL on the first run of 1.3). Each stands clear of
the others, of the entries' locknuts (28.87 across the corners at x 200 and 400) and of the plate; `pe-door` at x 50 is 48 from
the left side's inner face and sweeps outward with the door, meeting nothing (MOT-010). `pe-door` sits above the door pivot's
origin (z 400) for the same reader: a stud below it reads below the box (the first run read z −304 with the stud at z 100).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| cable-entry hole | Ø20.5, two, in the bottom | gland-m20 1.3 `CUTOUT`; lib/standards/holes.csv "M20 x 1.5 entry" (20.2 to 20.7) |
| wall-fixing hole | Ø9.0, four, M8, in the back | ISO 273 medium (H13), lib/standards/holes.csv. The four M8 hexagon socket head cap screws (ISO 4762) the inventory row names go here; screw-iso4762 is not built yet, so this version places none (OPERATING.md 12: model the holes, place the part in a later version) |
| mounting-plate hole | Ø9.0, four, M8, over the studs | ISO 273 medium (H13), lib/standards/holes.csv |
| stud thread (four studs) | M8, 12 beyond the plate's front face | the thread, derived: M8 × 1.25 coarse, tolerance class 6g: major Ø 7.7652 to 7.9713, pitch Ø 7.0382 to 7.1594, minor Ø d3 max 6.4377 (basic: H 1.0825, d2 7.1881, d3 6.4664); derived: derive.thread(8.0, 1.25) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6g; ISO 261 pitch). The nut that holds the plate meets it. The studs are modelled plain at the nominal Ø8 (the thread form is not drawn; the model is unchanged). The nuts (nut-iso4032, not built) are placed in a later version |
| earth studs (three, 1.3) | M8, welded, 12 proud of their face: `pe-body`, `pe-door`, `pe-plate` | the same derived thread as the plate studs (above); modelled plain at Ø8; their steel class is the welded stud's standard's (the torque row below). The nut that holds a panel's earth lug or bonding lead on each meets it (nut-iso4032, not built: placed by the panel). The bonding itself (which conductor, which stud) is the panel's (NFPA 79 8.2; IEC 60204-1 8.2; neither in lib/standards/sources.csv: the reviewer reads the clause); this element claims no bonding figure |
| earth stud tightening torque | not given in this version: it waits for the studs' property class. The studs are welded to the 2.0 sheet, the 2.5 plate and the door, so they are studs for arc stud welding, a standard's product whose steel class that standard gives; a quenched and tempered class (8.8) is not one a welded stud is made of, so no class is chosen here. Once the class is on file the torque is derived as the thread's figure (an upper bound: the weld is not rated) | NOT ON FILE (B): ISO 13918 (studs for arc stud welding: the stud's property class, the input the torque needs; not in lib/standards/sources.csv). The derivation then: derive.torque(8, 1.25, '<class>', mu_G=0.12, mu_K=0.12, nu=0.7, d_w=13, d_h=9) (M_A = F_M (0.16 P + 0.58 mu_G d2 + mu_K D_Km / 2), ISO 16047 / VDI 2230 Part 1; F_M = nu R_eL,nom A_s, ISO 898-1 clause 4 designation and stress area); d_w 13 is the bearing face of the nut and lug on the stud (design: the nut's standard, ISO 4032, is in lib/standards/wanted.md); nu 0.7 and mu_G / mu_K 0.12 are design choices (derive's defaults); d_h 9 is the M8 medium clearance hole (ISO 273, lib/standards/holes.csv). behaviour.csv's three `pin` rows carry the same open figure (enc-fs-1524x1829x305 1.9 writes its earth studs' torque open the same way) |

The entry figure is read from the gland element itself (element.py loads gland-m20), so the two cannot drift apart. The 2.0 sheet
of the bottom lies inside the plate range gland-m20 is built for (its `plate_t` 2.0, up to 4.2). The glands are not part of the
box: an assembly fits gland-m20 (released) in the entries its cables use, as a box is fitted on site.

## Mounting (what a fitted gland needs)
gland-m20 1.3 has its origin on the plate's outer face, the dome outward (here −z), the body 27.7 proud of that face and 29.72
across its largest diameter; its locknut (25 AF, 28.87 across the corners, 6.0 high) is inside the box, on the bottom (z 2.0 to
8.0).

| what | figure | from |
|---|---|---|
| clear space under each entry (x 200 and 400, y 100) | at least Ø29.72, 27.7 deep below z = 0, then the cable's bend | gland-m20 1.3; the bend radius is the fitted cable's own figure, taken by an assembly from the cable element it routes |
| locknut room inside | 28.87 across the corners: 171.1 between the two nuts; 85.6 to the closed door's inner face (y 0); 116.1 to the plane of the mounting plate's front face (y 230.5); 42.0 below the plate's bottom edge (z 50) | gland-m20 1.3; this box's entry positions |

So the box hangs with its bottom free: nothing may stand under it closer than the glands and the cables' bends.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| outside | 600 wide × 800 high × 250 deep (with the door closed: 252 deep) | room on the plate for three or four rows of DIN rail and duct, and the depth for a small drive or a contactor with its overload |
| sheet | 2.0 steel, RAL 7035, every panel and the door | |
| mounting plate | 500 × 700 × 2.5 galvanised, centred: x 50 to 550, z 50 to 750, front face y 230.5 | 48 clear of each wall's inner face, for wiring round its edge |
| plate standoffs | four, Ø16 × 15, welded to the back's inner face (y 233 to 248) | the plate stands 15 off the back, so a screw a device puts through the plate has room behind it |
| studs | four, M8 (plain at Ø8), from the standoffs' faces through the plate, 12 beyond its front face; centres 25 in from the plate's edges (x 75 and 525, z 75 and 725: 450 × 650) | a nut on each holds the plate |
| cable entries | x = 200 and 400 (200 pitch, centred on the width), y = 100, bottom only | the cables come up from below; nothing enters from the top |
| wall-fixing holes | x = 25 and 575, z = 25 and 775 (550 × 750 centres) | 23 from the walls' inner faces, room for an M8 screw head inside; outside the mounting plate, so the box is fixed with the plate in place |
| door | 600 × 800 × 2.0, swings 110° | |
| earth studs | three, M8 (plain at Ø8) × 12: `pe-body` up from the bottom's inner face at x 100, y 100; `pe-door` into the box from the door's inner face at x 50, z 700; `pe-plate` out of the plate's front face at x 300, z 75 | one per bonded part (the body, the door, the plate: request panel-7); the body's beside the entries where the supply's earth comes in, the door's at the top hinge corner (50 from the hinge, 100 below the top) so its lead is short and clear of the operators a panel cuts lower down, the plate's at its bottom edge centre, 25 in as the plate studs, below the rows a panel lays out |
| assembly | bottom and top full width and depth; the sides between them; the back between the sides; the door on the front edges | jbox 1.0's construction |

## GD&T (ISO 273, ASME Y14.5)
The four Ø9.0 wall-fixing holes are one pattern (550 × 750): position Ø0.5 at MMC (features.csv; floating fastener H − F = 9.0 −
8.0 = 1.0), datum A the back's outer face. The four Ø9.0 mounting-plate holes are one pattern over fixed studs (450 × 650):
position Ø0.5 at MMC (fixed fastener (H − F) / 2 = 0.5), datum A the plate's back face. The four welded studs that pass through
them are the other half of that fixed-fastener pair: one pattern (450 × 650), position Ø0.5 at MMC of the stud (Ø8), the four
located to each other, datum B the back's inner face (y 248). So H = F + T1 + T2: 9.0 = 8.0 + 0.5 (plate holes) + 0.5 (studs),
ASME Y14.5 fixed-fastener case. features.csv lists holes only, so the stud pattern's tolerance is stated here; GDT-010 reads
the holes' share. The two entry holes are cut-outs for glands, not a fastener pattern.

## Named nodes
`door` (rotate, a host) · `back-panel` (fixed, a host) · `pe-body`, `pe-door` (a child of `door`), `pe-plate`: the earth
studs, kind port, unit PE, gender none, their port face at the stud's tip; behaviour.csv marks them PE1, PE2, PE3 (a mark per
pin row; a label is not drawn in this version). Colliders `body` (the box),
`back-panel` and `door` (none for the studs: they sit inside the box's collider).

## Materials by layer
`M-STEEL-7035` every panel and the door · `M-GALV` the mounting plate · `M-ZINC` standoffs and studs, the earth studs too.

## Notes
No vendor names, part numbers or marks; no label in this version. No IP rating, no load rating, no thermal figure and no safety
claim: the door has no seal or latch in this version, and the class values above leave those "not stated". The three earth studs
(1.3) are where the panel shop asked for them (request panel-7); the protective bonding of the door and the plate (NFPA 79 8.2,
IEC 60204-1 8.2) stays the panel's: it lands its conductors on the studs and names the clause. A gland plate in the bottom that is
a host (the same request's item 3) is a major, 2.0, a later round: the two fixed M20 entries stay in this version. The stud thread
is derived (What it meets); the earth studs' torque waits for the welded stud's class (What it meets, one open figure, class B, a
document wanted). The rest are design choices.

## Outputs (out/)
`enc-wm.lsp` · `.glb` (pivots on `door`, `back-panel`, `pe-body`, `pe-door`, `pe-plate`) · `preview-*.png`. Terminal: dwg/, step/,
gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000261), our own design (mech-r56, unattended; EM's inventory pin 2, press-hydraulic first) |
| 1.1 | text only (mech-r63, review enc-wm-1.0 finding 1): "GD&T" now tolerances the four welded studs, the fixed-fastener pair's other share (position Ø0.5 at MMC of the stud, the four located to each other, datum B the back's inner face; 9.0 = 8.0 + 0.5 + 0.5). Model unchanged |
| 1.2 | text only (mech-r89, review mech-r85 finding 1): element.py's header, BASELINE and the STUD_D comment say the M8 stud thread is derived (derive.thread, ISO 68-1 / ISO 965-1), as "What it meets" has had it since mech-r85; Notes no longer call it open. Model unchanged |
| 1.3 | a minor (mech-r95, the core's lib/requests/core/mech-enc-wm-2026-11-11.md items 1 and 2, from requests panel-6 and panel-7): three M8 earth studs as port nodes pe-body, pe-door (a child of door), pe-plate (top-level, the plate being fixed), gender none, each a `pin` row in behaviour.csv with the derived torque; parameter `swing` builds the door turned open. Nodes added, none moved; origin and cut-outs unchanged. Item 3 (a gland plate host) is 2.0, later |
| 1.4 | text only (DOC-009, review enc-wm-1.3 finding 1, lib/requests/core/mech-doc009-2026-11-11.md item 1): the earth studs are welded, so their property class is the welded stud standard's (ISO 13918, a document wanted), not 8.8 by choice; the torque on the three `pin` rows (behaviour.csv PE1 to PE3) and in What it meets now waits for that class, one open figure, class B, as enc-fs-1524x1829x305 1.9 writes its earth studs. Model, nodes, origin and cut-outs unchanged (mech-r107, unattended) |
