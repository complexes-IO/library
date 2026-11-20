# reel-cable-630 · v1.0 · cable storage and transport reel, generic, wooden flanges Ø630 x 25 on a barrel Ø315, 500 wide over the flanges, arbor bore Ø50

**What** A cable storage and transport reel: cable is wound on a barrel between two flanges, and the reel turns on an axle through its
arbor bore as the cable is paid out. Two wooden flanges Ø630 × 25 sit on the ends of a wooden barrel Ø315 × 450; a Ø50 arbor bore runs
through the flanges and the barrel on the reel's axis, and each flange has one Ø30 drive-pin hole at a radius of 220 for a winding
machine's drive pin. It is the reel that rack-cable-drum-1000 1.0 carries on its Ø40 axles. The cable, the barrel's staves and spokes,
and the flanges' bolts are not drawn: the barrel is drawn as one solid.
**Class** furniture · **Baseline** our own design: generic storage/transport reel (ETIM 10.0 EC004844 Storage/transport reel),
OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by
name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r168.md), and EC004844 is a class not yet built; its shape no dimensional
standard on file fixes. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the reel's axis, midway between the flanges' outer faces: x along the axis (the flanges' outer faces
x −250 and 250), y and z across it. On rack-cable-drum-1000 the origin goes on an axle's axis (y 0, z 450 or 1200, the reel between the
side frames); standing on the floor, at z = 315 (the flanges' rims on the floor). Extents x −250 to 250, y −315 to 315, z −315 to 315.
**Built with** toolkit 1.3 · AutoLISP command `RLCB630` · no parameter · places no element; reads rack-cable-drum-1000 1.0 with
library.load.

## Class values (ETIM 10.0 EC004844)
Design inputs. EC004844 Storage/transport reel (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 4
features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are
on file this table gives the values the reel is designed to under plain names, as rack-cable-drum-1000 1.0 does (requests mech-8 and
mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the design has
no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | wood (the `M-BROWN` layer); the species and grade not stated |
| flange diameter | 630 |
| width | 500 over the flanges; traverse 450 between them |
| barrel diameter | 315 |
| arbor bore | Ø50 |
| load capacity | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load or mass figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| rack-cable-drum-1000 1.0's largest drum | Ø700 × 960: the reel's Ø630 × 500 is inside both (asserted), and 500 < the frames' 1000 clear | library.load("rack-cable-drum-1000", "1.0"): `D_MAX`, `W_MAX`, `XI` |
| its axle | Ø40 (`RA` 20): the Ø50 bore clears it by 5 all round, so the reel turns on the axle (asserted ≥ 2) | library.load: `RA` |
| its tiers | on the lower axle (z 450) the rim's bottom 135 is above the floor tie's top 50 (asserted 315 ≤ 400); one reel on each axle (750 apart) clear each other by 120 (asserted 750 ≥ 630) | library.load: `ZA`, `UP` |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| flanges | Ø630 × 25, x −250 to −225 and 225 to 250 | 35 under the rack's largest drum's radius; 25 thick, so every edge is 25 or more (none in the 3 to 7 fillet trap) |
| barrel | Ø315 × 450, x −225 to 225, one solid | half the flange's diameter: the cable's smallest wrap; drawn solid, its staves and spokes not drawn |
| arbor bore | Ø50 through both flanges and the barrel (features.csv kind own; three coaxial holes, one per part) | turns on the rack's Ø40 axle, 5 clear all round |
| drive-pin holes | Ø30 through each flange at r 220, above the axis (features.csv kind own) | 47.5 outside the barrel and 80 inside the rim (asserted), for a winding machine's drive pin |
| width | 500 over the flanges | a mid-size reel; 460 less than the rack's largest drum, so two side by side on one axle (2 × 500 = 1000) do not fit: one reel an axle |

## Mechanism
None. One fixed body, no node: the reel turning on an axle, the cable wound on it and its fixing to a winder are the host's assembly, not
a motion (behaviour.csv: the header only).

## Named nodes
None. Collider, an axis-aligned box: `reel` (the reel's envelope, x −250 to 250, y and z −315 to 315).

## Materials by layer
`M-BROWN` the flanges and the barrel (wood).

## Decals (Blender)
No label: `M-BROWN` is not a printed layer of the Blender gate (its default printed layers are `M-WHITE-PA` and `M-BLACK-PA`; review
mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Volume by hand (asserted in element.py): the flanges 2 × π × 315² × 25 ≈ 15586227, the barrel
π × 157.5² × 450 ≈ 35069010, less the bore π × 25² × 500 ≈ 981748 and the two drive-pin holes 2 × π × 15² × 25 ≈ 35343, so about
49638146 mm³. Every bounding-box extreme lies on an uncut face: x ±250 the flanges' outer faces (the bore and the drive holes lie inside
them), y and z ±315 the flanges' rims. No mass is stated: lib/materials.csv gives no density. Not drawn: the cable, the barrel's staves
and spokes, the flanges' bolts.

## Outputs (out/)
`reel-cable-630.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004844), our own design (mech-r168, unattended, 2026-11-13): two wooden flanges Ø630 × 25 on a barrel Ø315 × 450, 500 wide, a Ø50 arbor bore and two Ø30 drive-pin holes, sized to ride on rack-cable-drum-1000 1.0's Ø40 axle |
