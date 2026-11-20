# corner-stacking-1000 · v1.0 · stacking corner for a block pallet, generic, painted steel, 1000 clear between the pallets, angle post 60 x 60 x 8 between lipped plates 120 x 120

**What** A stacking corner: four of them, one at each corner of a loaded pallet, carry a second loaded pallet above it, so the loads
are stacked without the upper pallet resting on the lower load. A painted steel foot plate stands on the lower pallet's corner deck
board, two lips turned down over the deck's outer edges locating it; an angle post of two legs 60 × 8 rises at the outer corner; a top
plate carries the upper pallet's corner, two lips turned up over its bottom board's outer edges locating it. The part is symmetric about
its diagonal, so one part serves all four corners, turned 90, 180 and 270 degrees about z. It is sized on pallet 1.2.
**Class** furniture · **Baseline** our own design: generic stacking corner (ETIM 10.0 EC003948 Stacking corner), OPERATING.md 12
"Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by name from
lib/toolkit/generic.py's mech order (lib/rounds/mech/r169.md), and EC003948 is a class not yet built; its shape no dimensional standard
on file fixes. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the lower pallet's outer corner on its deck top: x and y along the pallet's outer edges (the pallet
at x ≥ 0, y ≥ 0), z = 0 the lower pallet's deck top, z = 1000 the upper pallet's underside. On pallet 1.2 the origin goes at its corner
(0, 0, 144); the other three corners take the same part turned about z. Extents x −8 to 120, y −8 to 120, z −16 to 1016.
**Built with** toolkit 1.3 · AutoLISP command `CRST1000` · no parameter · places no element; reads pallet 1.2 with library.load.

## Class values (ETIM 10.0 EC003948)
Design inputs. EC003948 Stacking corner (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 3 features)
is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are on file
this table gives the values the corner is designed to under plain names, as reel-cable-630 1.0 does (requests mech-8 and mech-9, the
core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the design has no value
(lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer); the grade not stated |
| stacking height | 1000 clear, the lower pallet's deck top to the upper pallet's underside |
| pallet it fits | pallet 1.2, a block pallet 1219 × 1016 × 144 |
| load capacity | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load or mass figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| pallet 1.2's corner deck board | 120 wide (x 0 to 120) over the corner block 145 × 145: the foot plate's bearing square 120 × 120 lies on it (asserted `S` ≤ `DECK_W` and ≤ `B`) | library.load("pallet", "1.2"): `DECK_W`, `B` |
| its deck boards' thickness | 20: the foot lips reach 16 below the deck top, so they cover the deck's edges and never reach the stringer board (asserted 16 < 20) | library.load: `DECK` |
| the upper pallet's corner bottom board | 145 wide (x 0 to 145), 18 thick: the top plate's 120 × 120 lies under it, its lips reach 16 up its edges (asserted 120 ≤ 145, 16 < 18) | library.load: `BOT_W`, `BOT` |
| its footprint | 1219 × 1016: four corners, 120 each, never meet (asserted 240 < 1016). The footprint is pallet's own open figure (its spec.md, ISO 6780 not on file); this fit holds for any footprint over 240 a side, so the corner does not depend on it | library.load: `LX`, `LY` |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| clear height | 1000 between the pallets | the upper pallet's deck stands at 2 × 144 + 1000 = 1288 above the floor; a lower load clears the upper pallet if under 1000, and under 992 where it reaches the plates' 120 × 120 corners |
| plates | 128 × 128 × 8 each (x and y −8 to 120): the bearing square 120 × 120 on the pallet and the lips' 8 outside it | 8 thick so every edge is 8 or more (none in the 3 to 7 fillet trap) |
| foot lips | two, 8 thick, z −16 to 0 along the pallet's x = 0 and y = 0 edges, meeting at the corner | locate the corner on the deck: they cover the deck board's side and the deck boards' ends |
| top lips | two, 8 thick, z 1000 to 1016 along the same edges | locate the upper pallet: they cover its bottom board's side and the bottom boards' ends |
| post | an angle of two legs 60 × 8 at the outer corner (x 0 to 60 by y 0 to 8, x 0 to 8 by y 0 to 60), z 8 to 992 | at the corner, outside the load's space: a load set 60 in from the pallet's edges clears it |
| joints | each lip and post leg 0.5 into its plate (welded) | one body |

## Mechanism
None. One fixed body, no node: the pallets it stands on and carries are the host's assembly, not a motion (behaviour.csv: the header
only).

## Named nodes
None. Colliders, axis-aligned boxes: `foot` (the foot plate and its lips, x and y −8 to 120, z −16 to 8), `post-x` and `post-y` (the
post's two legs, z 8 to 992), `top` (the top plate and its lips, z 992 to 1016).

## Materials by layer
`M-STEEL-7035` the plates, lips and post (painted steel).

## Decals (Blender)
No label: `M-STEEL-7035` is not a printed layer of the Blender gate (its default printed layers are `M-WHITE-PA` and `M-BLACK-PA`;
review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Volume by hand (asserted in element.py, the union): two plates 2 × 128 × 128 × 8 = 262144, two
L-shaped lips 2 × (8 × 128 + 120 × 8) × 16 = 63488, the post's L section 896 over 984 = 881664, so 1207296 mm³. Every bounding-box
extreme lies on an uncut face: x and y −8 the lips' outer faces, 120 the plates' edges, z −16 the foot lips' lower edges, 1016 the top
lips' upper edges. No mass is stated: lib/materials.csv gives no density. Not drawn: the welds.

## Outputs (out/)
`corner-stacking-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003948), our own design (mech-r169, unattended, 2026-11-13): painted steel foot and top plates 128 × 128 × 8 with lips 16 over the pallets' edges, an angle post 60 × 60 × 8 between them, 1000 clear between the pallets, sized on pallet 1.2 |
