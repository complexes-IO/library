# caster · v1.0 · swivel plate caster, own design, plate 100 x 85 with 4 x Ø9.0 holes on 80 x 60 (M8, ISO 273 medium), fork trailing 25, wheel Ø100 x 32, 140 high

**What** A swivel plate caster: the wheel a cart, a roll cabinet, a tool trolley or a machine stand rolls on, screwed under it by
a square plate with four holes. A fork hangs from the plate and turns freely about the plate's centre, and the wheel turns on the
fork's axle, which trails behind the swivel axis so the wheel follows the push. The inventory row lists it as "caster" (own_design
yes, made of four hexagon head screws, screw-iso4017) for the welding table and the carts and cabinets of the machine rows
(lib/machines-factory.txt); tb-rollcab 1.0 already carries this plate's hole pattern in its bottom pads. Two moving nodes, the fork
(`swivel`) and the wheel (`wheel`, a child of the fork); no terminal.
**Class** device · **Baseline** our own design, OPERATING.md 12 "Own designs" (EM, 2026-11-05): casters are in the next.md list and
lib/inventory.csv marks the row own_design "yes". No ETIM 10.0 class on file is a caster and no caster standard is in
lib/standards/sources.csv, so there are no class values and no standard's figures to follow: the holes it carries are ISO 273's
and every other size is a design choice. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up: the plate lies in the plane z = 0, the swivel axis is z, the axle runs along y at rest. Origin: the
plate's top face (the mounting face, the host's underside) on the swivel axis, x = 0, y = 0; +z up, so the whole caster lies
below the origin and the floor is the plane z = −140 at rest. At rest the fork trails toward +x (the axle at x 25). Extents x −50
to 75, y ±42.5, z −140 to 0.
**Built with** toolkit 1.3 · AutoLISP command `CASTERSW` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| the screws | 4 × Ø9.0 clearance holes through the plate on 80 (x) × 60 (y) centres (x ±40, y ±30), M8 | ISO 273 medium (H13), lib/standards/holes.csv. M8 is this design's choice (the inventory's made_of is screw-iso4017 x4, hexagon head screws, a common part not built yet: the holes are modelled, the part placed later). Position Ø0.5 at MMC (features.csv): T ≤ H − F = 9.0 − 8.0 = 1.0, ASME Y14.5 floating fastener (the host's pattern takes the other Ø0.5) |
| the host | the plate's top face, 100 × 85, flat against the host's underside; its hole pattern 80 × 60 | design: the pattern tb-rollcab 1.0 cut in its four bottom pads (lib/elements/tb-rollcab/spec.md, "caster plates": four Ø9.0 holes on 80 × 60 centres per plate), so that cabinet places this caster without a change; any other host cuts the same pattern. The host's underside carries the whole plate (the swivel load path is the plate's centre, inside the hole pattern) |
| the floor | the tread's bottom line, Ø100 wheel, 32 wide, 140 below the mounting face | by hand; no load rating, no speed, no floor (hardness, threshold) figure |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| top plate | 100 (x) × 85 (y) × 3, zinc-plated pressed steel; z −3 to 0 | 10 past each hole centre along x and 12.5 along y leaves a 5.5 to 8 wall round each Ø9.0 hole; 3 is a pressed plate's gauge, and at 3 the plate's corner edges fall at the gate's short-edge limit, so the fillet pre-flight skips them (below) |
| swivel head | a Ø60 disc, 10 thick, face to face under the plate (z −13 to −3), concentric with the swivel axis | the ball race between the plate and the head is not drawn: the head turns on the plate's underside; Ø60 keeps the head 20 clear of every hole centre (the hole circle is Ø100) |
| crown plate | 60 (x −10 to 50) × 46 (y ±23) × 3, under the head (z −16 to −13) | joins the head to the two legs and carries the trail: it reaches 20 past the head's edge toward +x, where the legs hang |
| legs | two, 50 (x 0 to 50) × 3 thick × 94 high (z −110 to −16), their outer faces at y ±23 and inner faces at y ±20, their top faces wholly on the crown's underside | the axle at the legs' middle (x 25) with 25 of leg each side of it; 20 of leg below the axle; 3 pressed steel as the plate, so no edge of theirs is in the fillet trap |
| trail | the axle 25 behind the swivel axis (x 25) | a swivel caster's offset, so the wheel swings to trail the push; a quarter of the wheel's diameter |
| axle | Ø12 along y, y ±24 (1 proud of each leg's outer face), at z −90 | pressed through the legs; its head and nut are not drawn; 1 proud so its ends show as faces and nothing lies flush |
| wheel | tread Ø100, 32 wide (y ±16), black polyamide; hub Ø30, 36 wide (y ±18), zinc-plated steel, bored Ø13 on the Ø12 axle | Ø100 is a common size for a lab cart; 4 clear of each leg's inner face at the tread, 2 at the hub; the hub 2 proud of the tread each side so the tread never rubs the legs; 0.5 radial clearance on the axle (the bearing is not drawn), as hinge 1.0's moving knuckle |
| height | 140 from the floor to the plate's top face | the axle 90 below the plate plus the tread's radius 50 |
| swivel range | −180 to 180 about z; the wheel 0 to 360 about the axle | free in both: nothing stops the fork or the wheel |
| load rating, speed, finish | not claimed | no figure is on file for them and the element is not sized against a load; the layers show zinc-plated steel and a black tread, no grade is claimed |

## Mechanism
Two moving nodes. `swivel` (the head disc, the crown plate, the two legs and the axle) turns about the swivel axis z at the
plate's underside (pivot (0, 0, −3), −180 to 180): the push on the host swings it so the wheel trails. `wheel` (the tread and the
hub) turns about the axle along y (pivot (25, 0, −90), 0 to 360) and rides the fork (P.parents: a child of `swivel`, so when the
fork turns the wheel goes with it, as turntable's rollers ride its deck). At rest the fork trails toward +x. The top plate is the
fixed body. behaviour.csv: a default state and a `manual toggle` state with its pose for each node (the twin has no drive to
read: the host's push moves both). The swivel's sweep below the plate (a Ø150 circle, the wheel's far edge at 75 from the axis)
meets nothing of this element; the wheel's sweep lies inside the fork, 4 clear of the legs. No load path is checked: no rating.

## Named nodes
`swivel` (pivot (0, 0, −3), rotate about z, −180 to 180) · `wheel` (pivot (25, 0, −90), rotate about y, 0 to 360; child of
`swivel`). Colliders, axis-aligned boxes at rest: `plate` (the top plate, x ±50, y ±42.5, z −3 to 0), `fork` (the head, crown,
legs and axle, x −10 to 50, y ±23, z −110 to −3), `tyre` (the tread and hub, x −25 to 75, y ±18, z −140 to −40).

## Materials by layer
`M-ZINC` the top plate, the fork (head, crown, legs, axle) and the wheel's hub (zinc-plated steel) · `M-BLACK-PA` the tread.

## Decals (Blender)
"complexes.org" on the +y leg's outer face (y = 23, 50 × 94), reading along x.

## Notes
No vendor names, part numbers or marks. No load rating, speed or floor claim: no figure is on file for them and the element is not
sized against a load. Not drawn: the screws (placed later from screw-iso4017), the swivel's ball race, the wheel's bearing, the
axle's head and nut, the host and its holes. No open figure: the plate's holes are ISO 273's, the host's pattern is tb-rollcab's,
and the rest are design choices. A caster is in the own-design list (lib/rounds/mech/next.md #14; OPERATING.md 12: carts, cabinets)
and no dimensional standard for one is on file, so it is built as our own design with no class values. A fixed (rigid) fork, a
brake (a pedal on the fork that locks the wheel and the swivel), a bolt-hole (stem) fitting instead of the plate, other wheel
sizes and treads are other versions or elements; the inventory row names "swivel and fixed, with brake", and this first version is
the plain swivel caster: the brake and the fixed fork follow when a machine row asks for them (lib/needs-em/mech.md).
The gate's fillet rule (fillet r 0.5 for a device, lib/toolkit/fillet.py): the plate, the crown and the legs are 3 thick, so
their end and corner edges are 3 long, at the pre-flight's short-edge limit (MIN_EDGE 3.0: an edge is picked only when longer),
and are skipped as "short"; their long edges (46 to 100) and the circular edges (head Ø60, axle Ø12, hub Ø30, tread Ø100) are
filleted; the head's top face is buried against the plate, the legs' top faces against the crown; the bores are cut edges,
skipped. Why: the first gate run of this version had the plate and crown 5 thick, and its per-edge pass held each 5 mm edge with
two free corners at 88 % of its fillet volume (the 90 % rule), four of them on the envelope: a REJECT (the same ratio mech-r69 saw
on 10 mm edges at r 1.0). The 3 mm pressed sheet is bed-slat 1.0's way round it (its 2.5 slats) and a caster's usual gauge.
Gate note (mech-r92 and r93's lessons; request mech-12's answer in core round 30): the bounding box's extremes lie on the top
plate (x −50, y ±42.5, z 0: an axis-aligned uncut box) and on the wheel's tread (x 75, z −140: a cylinder, a nested node); the
AutoCAD gate's glb reader now walks the node tree with every parent's transform (cadout.glb_extents), so the nested wheel reads
where it stands (enc-fs 1.9's port nodes under the door pivots passed the same way in r100). Nothing is tilted.

## Outputs (out/)
`caster.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r101, unattended, 2026-11-11) |
