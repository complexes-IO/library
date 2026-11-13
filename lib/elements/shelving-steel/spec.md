# shelving-steel · v1.0 · steel shelving bay, generic, 1000 × 500 × 2000, 5 shelves 900 × 500, 4 × M12 anchor holes

**What** One bay of steel shelving for the storage racks (lib/machines-factory.txt line 121: racks-storage places it): boxed and
loose goods, bins and small parts are put on its shelves and taken off by hand from the front. Pallets go on pallet-rack, long
stock lying flat on rack-cantilever, bars on end on rack-bar, sheet on rack-sheet-vertical. One fixed body.
**Class** furniture · **Baseline** our own design: generic steel shelving bay (ETIM 10.0 EC004064), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07); lib/inventory.csv marks the row own_design "generic". No product was matched and no vendor file was
opened. The class values below are the design inputs; the holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0, the middle of the bay's width x = 0, the front uprights' front faces
y = 0. The bay's depth runs toward +y, its back at y = 500; goods go in and out at the front, from −y.
**Built with** toolkit 1.3 · AutoLISP command `SHELVSTEEL` · no parameters.

## Class values (ETIM 10.0 EC004064)
Design inputs. EC004064 Shelf rack (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, 9 features) is a
tier-2 class on no inventory row yet, so lib/standards/etim/class-features.csv (the tier-1 classes and the classes the inventory
uses) does not list its features, and none is written from memory. Request mech-9 asks the core to give the inventory row its class,
which brings the features in (as request mech-8 for rack-cantilever and pneu-4 for tube-pneu). Until then this table gives
the values the bay is designed to under plain names; the next minor version restates them in ETIM's order with their EF codes,
"not stated" where the design has no value.

| value | this element |
|---|---|
| width over all | 1000 mm, over the uprights |
| depth over all | 500 mm, the front uprights' front faces to the rear uprights' backs |
| height | 2000 mm, the floor to the uprights' tops |
| shelves | 5, each 900 × 500, their top faces at 150, 600, 1050, 1500 and 1950 above the floor |
| shelf spacing | 450 mm top face to top face, 410 clear between a shelf and the underside of the next |
| uprights | 4, one at each corner |
| material | steel, painted (layer M-STEEL-7035) |
| load per shelf, load per bay | not stated: no load is designed or claimed |

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the anchor plates at 950 × 300 (x ±475, y 100 and 400) | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice. The anchors (anchor-bolt, a separate element on the same line of machines-factory.txt) are the assembly's; nothing is placed in the holes |
| floor | the uprights' and anchor plates' undersides, z = 0 | a flat floor; the floor is the assembly's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the front uprights' front
faces) and C (the plane at the middle of the bay's width) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| uprights | 4, section 50 × 50, z 0 to 2000, at the corners of the 1000 × 500 footprint (x −500 to −450 and 450 to 500; y 0 to 50 and 450 to 500) | carry the shelves; drawn as plain square members (a slotted or perforated angle's holes are not drawn) |
| shelves | 5, 900 (x −450 to 450) × 500 (y 0 to 500) × 40, between the uprights' inner side faces, their ends against those faces | 40 is a folded panel's edge height, drawn solid; top faces at z 150, 600, 1050, 1500 and 1950, so the lowest shelf's underside is 110 above the floor and the top shelf's face 50 below the uprights' tops |
| anchor plates | 4, 50 × 100 × 20 (z 0 to 20), inside the footprint: behind each front upright (y 50 to 150) and in front of each rear upright (y 350 to 450), the upright's width, one Ø13.5 hole in each plate's centre | fix the bay to the floor without anything standing out of the footprint, so bays stand side by side and back to back; 90 below the lowest shelf's underside |
| the goods | not drawn | the store's, not the bay's |

## Mechanism
None: one fixed body, no node. The shelves are fixed at their heights in this model; goods on a shelf are the store's.

## Named nodes
None. Colliders, one per member, so goods on a shelf meet that shelf and not an envelope: `upright-lf`, `upright-lb`,
`upright-rf`, `upright-rb` (l / r the −x / +x side, f / b front / back), `shelf-1` to `shelf-5` (1 the lowest), `anchor-lf`,
`anchor-lb`, `anchor-rf`, `anchor-rb`.

## Materials by layer
`M-STEEL-7035` every member (painted steel, RAL 7035).

## Decals (Blender)
"complexes.org generic" on the +x front upright's outer side face.

## Notes
No vendor names, part numbers or marks. No load rating, no stability claim and no safety claim: no goods' mass is on file, no
calculation or test of the model is on file, and the bay is not sized against a load. The class values are the figures this
design is meant to meet. Not drawn: the uprights' fixing holes or slots and the shelves' adjustment along them, shelf clips or
bolts, diagonal bracing, back and side cladding, the joining of bays in a row. The anchor holes are on file; the anchors are the
assembly's.

## Outputs (out/)
`shelving-steel.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004064), our own design (mech-r89, unattended, 2026-11-10) |
