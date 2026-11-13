# rack-cantilever · v1.0 · cantilever rack, generic, single-sided, 2 columns 1500 apart, 4 arm levels 1000 long, 2400 high, 4 × M12 anchor holes

**What** A cantilever rack for the steel store and the storage racks (lib/machines-factory.txt lines 121 and 122: racks-storage
and storage-steel place it): long stock lying flat (bars, tubes, profiles, bundles) rests across the arms of two columns and is
taken out from the front with nothing in the way, since the arms have no front post. Bars that stand on end go on rack-bar, sheet
on rack-sheet-vertical. Single-sided: arms on one side only, the columns' backs toward a wall or an aisle. One fixed body.
**Class** furniture · **Baseline** our own design: generic cantilever rack (ETIM 10.0 EC004068), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07); lib/inventory.csv marks the row own_design "generic". No product was matched and no vendor file was
opened. The class values below are the design inputs; the holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0, midway between the two columns x = 0, the columns' front faces (the
faces the arms spring from) y = 0. The arms and the loading side are toward −y; the columns' backs toward +y.
**Built with** toolkit 1.3 · AutoLISP command `RACKCANT` · no parameters.

## Class values (ETIM 10.0 EC004068)
Design inputs. EC004068 Cantilever rack (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, 7 features)
is a tier-2 class on no inventory row yet, so lib/standards/etim/class-features.csv (the tier-1 classes and the classes the
inventory uses) does not list its features, and none is written from memory. Request mech-8 asks the core to give the inventory
row its class, which brings them in (as request pneu-4 for tube-pneu). Until then this table gives the values the rack is designed
to under plain names; the next minor version restates them in ETIM's order with their EF codes, "not stated" where the design has
no value.

| value | this element |
|---|---|
| sides | single-sided: arms toward −y only |
| columns | 2, 1500 apart centre to centre |
| arm levels | 4 on each column (8 arms); the bases' top faces make a fifth, lowest level |
| arm length | 1000 mm, the column's front face to the arm's end |
| height | 2400 mm, the floor to the columns' tops |
| width over all | 1780 mm over the anchor plates (1620 over the columns) |
| depth over all | 1300 mm, the bases' front ends to the columns' backs |
| material | steel, painted (layer M-STEEL-7035) |
| load per arm, load per column | not stated: no load is designed or claimed |

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the anchor plates at 1700 × 1140 (x ±850, y 120 and −1020) | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice. The anchors (anchor-bolt, a separate element on the same lines of machines-factory.txt) are the assembly's; nothing is placed in the holes |
| floor | the bases' and anchor plates' undersides, z = 0 | a flat floor; the floor is the assembly's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the columns' front faces) and C
(the plane midway between the columns) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| columns | 2, section 120 (x) × 200 (y 0 to 200), from the bases' tops (z 160) to z 2400, centred on x ±750 | each carries four arms on its front face |
| floor bases | 2, 120 × 1300 × 160 (y −1100 to 200, z 0 to 160), one under each column, the column on the rear end | the base runs forward under the arms and 100 beyond their ends; its top face is the lowest storage level |
| arms | 8, 100 wide × 1000 long × 100 deep (y −1000 to 0), plain and level, their top faces at z 700, 1200, 1700 and 2200 | four levels 500 apart, 400 clear between an arm's top and the next arm's underside; each arm 10 inside the column's side faces. Level and of one depth: no taper, no upturned end, no end stop is drawn |
| ties | 3, 80 × 80, between the columns' inner faces (x ±690), y 60 to 140, undersides at z 300, 1250 and 2200 | hold the columns apart and in line. Horizontal ties only: no diagonal brace is drawn |
| anchor plates | 4, 80 × 120 × 20 (z 0 to 20), on the outer side of each base at its rear (y 60 to 180) and front (y −1080 to −960), one Ø13.5 hole in each plate's centre | fix the rack to the floor; 20 thick |
| the stock | not drawn | the store's, not the rack's |

## Mechanism
None: one fixed body, no node. The arms are fixed at their heights in this model; stock laid on the arms is the store's.

## Named nodes
None. Colliders, one per member, so stock on an arm meets that arm and not an envelope: `base-l`, `base-r`, `column-l`,
`column-r`, `arm-l1` to `arm-l4` and `arm-r1` to `arm-r4` (1 the lowest), `tie-1` to `tie-3` (1 the lowest), `anchor-lb`,
`anchor-lf`, `anchor-rb`, `anchor-rf` (l / r the −x / +x side, b / f rear / front).

## Materials by layer
`M-STEEL-7035` every member (painted steel, RAL 7035).

## Decals (Blender)
"complexes.org generic" on the +x column's outer side face.

## Notes
No vendor names, part numbers or marks. No load rating, no stability claim and no safety claim: no stock's mass is on file, no
calculation or test of the model is on file, and the rack is not sized against a load. The class values are the figures this
design is meant to meet. Not drawn: arm end stops, adjustable arm fixings (holes or slots up the column), diagonal bracing, a
second side of arms. The anchor holes are on file; the anchors are the assembly's.

## Outputs (out/)
`rack-cantilever.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004068), our own design (mech-r87, unattended, 2026-11-10) |
