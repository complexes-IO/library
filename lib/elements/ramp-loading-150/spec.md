# ramp-loading-150 · v1.0 · loading ramp, generic, painted steel, 150 rise at 1 in 10, 1000 wide, 1500 long with a landing 100 deep, hollow underneath

**What** A loading ramp: it stands on the floor against the face of a platform 150 high and takes wheeled loads (a hand pallet truck,
a trolley, a cart) up to it. One welded painted steel body: a nose 10 high at the floor, a deck rising 1 in 10 over 1400, a flat landing
100 deep at 150 whose back face stands against the platform, two closed side walls, three ribs between four bays, open underneath.
**Class** furniture · **Baseline** our own design: generic loading ramp (ETIM 10.0 EC004428 Loading ramp), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by name from
lib/toolkit/generic.py's mech order (lib/rounds/mech/r170.md), and EC004428 is a class not yet built; its shape no dimensional standard
on file fixes. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the nose's lower front corner on the floor: x up the ramp (the landing at x 1400 to 1500), y across
it (0 to 1000), z up from the floor. The landing's back face x = 1500 stands against the platform it serves, whose top is at z = 150.
Extents x 0 to 1500, y 0 to 1000, z 0 to 150.
**Built with** toolkit 1.3 · AutoLISP command `RMPL150` · no parameter · places no element and reads none.

## Class values (ETIM 10.0 EC004428)
Design inputs. EC004428 Loading ramp (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 5 features,
synonym "Access ramp") is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory.
Until they are on file this table gives the values the ramp is designed to under plain names, as corner-stacking-1000 1.0 does
(requests mech-8 and mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated"
where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer); the grade not stated |
| height (rise) | 150, floor to the landing's top |
| length | 1500 overall: the slope's run 1400 and the landing 100 |
| width | 1000 |
| gradient | 1 in 10 (5.71 degrees) |
| load capacity | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load or mass figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the floor | the side walls', ribs' and back walls' lower edges and the nose's underside at z = 0 | design: the ramp stands on the floor; no floor fixing is drawn |
| the platform it serves | its top at z = 150, its face against the landing's back face x = 1500 | design: no platform element is on file, so none is read; a host with a platform of another height takes another ramp |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| gradient | 1 in 10, the deck from z 10 at the nose to z 150 at x 1400 | a gentle slope for a hand-pushed load; no access-ramp gradient rule is on file and none is claimed |
| nose | 10 high at the floor (x = 0), solid to x 100 | the step a wheel climbs onto the deck; 10 so no edge falls in the 3 to 7 fillet trap |
| landing | flat, 100 deep (x 1400 to 1500) at z 150 | the wheel leaves the slope onto a level surface flush with the platform's top |
| width | 1000 | a hand pallet truck's forks and wheels pass inside it |
| steel | 8 thick: the deck and landing (measured square to the surface), the side walls, the ribs, the back walls | every edge 8 or more |
| bays | four, 240 wide each, between the side walls and three ribs (y 8 to 248, 256 to 496, 504 to 744, 752 to 992), open underneath | the deck carried every 248 across its width |
| bays under the deck | x 102 to 1392 at the floor; the front face square to the deck, 12.10 long, its top at x 100.8; the back face square to the deck, 140.46 long, meeting the floor at x 1392 | the nose solid in front of them; a wall 8 thick at the floor (22 at the top) between them and the landing's bays |
| bays under the landing | x 1400 to 1492, z 0 to 142 | the landing 8 thick over them, a back wall 8 thick behind them |

## Mechanism
None. One fixed body, no node: the loads that roll over it are the host's assembly, not a motion (behaviour.csv: the header only).

## Named nodes
None. Colliders, axis-aligned boxes stepping up the slope (the toolkit's colliders are boxes): `step-1` (x 0 to 350, z 0 to 45),
`step-2` (x 350 to 700, z 0 to 80), `step-3` (x 700 to 1050, z 0 to 115), `landing` (x 1050 to 1500, z 0 to 150), each the full width.

## Materials by layer
`M-STEEL-7035` the whole body (painted steel).

## Decals (Blender)
No label: `M-STEEL-7035` is not a printed layer of the Blender gate (its default printed layers are `M-WHITE-PA` and `M-BLACK-PA`;
review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one box 1500 × 1000 × 150 with one oblique cut above the slope, four oblique cuts (the
bays under the deck, their tops on the plane 8 under the slope) and four axis-aligned cuts (the bays under the landing). Volume by hand
(asserted in element.py): the side section 1500 × 150 less 98000 above the slope, 127000 × 1000 = 127000000; less the deck bays, a
trapezoid in section (parallel sides 12.10 and 140.46, 1283.60 apart, 97912.40 mm²) over 4 × 240; less the landing bays 92 × 142 over
4 × 240; so 20462652 mm³. Every bounding-box extreme lies on an uncut face: x 0 the nose's front, 1500 the landing's back, y 0 and 1000
the side walls' outer faces, z 0 the lower edges, z 150 the landing's top. No mass is stated: lib/materials.csv gives no density. Not
drawn: the welds, an anti-slip surface, a floor fixing.

## Outputs (out/)
`ramp-loading-150.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004428), our own design (mech-r170, unattended, 2026-11-13): painted steel ramp 1500 × 1000 rising 150 at 1 in 10 to a landing 100 deep, one welded body 8 thick with four bays open underneath |
