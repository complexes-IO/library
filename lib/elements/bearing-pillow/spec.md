# bearing-pillow · v1.1 · pillow block bearing unit, generic, housing for a 25 shaft insert, base 140 x 40 with 2 x M12 holes at 105, centre height 50

**What** A pillow block bearing unit: the housed bearing a shaft runs in on a frame, the way a roll, an index table, a rotator, a
bender's rolls or a test rig's shaft are carried (bender-section, condition-monitoring-rig, mechanisms-bench, roll-plate,
rotary-index-table, rotator-welding). This version is the housing: a painted cast block on a base with two M12 bolt holes 105
apart, the shaft axis along y at 50 above the mounting face, and the insert bearing's seat drawn as a plain Ø52 bore through the
tower. The insert bearing itself (outer ring with a spherical seat, inner ring with the 25 bore and its set screws) is a part a
dimensional standard shapes (ISO 9628) and is never generic (OPERATING.md 12): it is not drawn, and its seat's figures are a
source wanted (What it meets). lib/inventory.csv row `bearing-pillow` (own_design generic, etim EC012129; 6 systems; a part of
conveyor-seg x4).
**Class** device · **Baseline** our own design: generic bearing (ETIM 10.0 EC012129), OPERATING.md 12 "Generic elements" (EM,
2026-11-07); the inventory row is own_design "generic" with its class on file (eight features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened: the folder's reference record (a
catalogue pillow block for a 20 shaft, references/source.txt) is not what this element is built from. What it meets takes its
figures from the standards on file (the bolt holes at M12's ISO 273 clearance); the seat is drawn at a design figure and marked;
every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face plane (z = 0, the base's underside) under the shaft axis, at the base's
centre. The shaft axis runs along y at z 50 (the centre height); the base's length along x. Extents x ±70, y ±20, z 0 to 90.
**Built with** toolkit 1.3 · AutoLISP command `BEARINGPB` · no parameters.

## Class values
ETIM 10.0 class EC012129 Bearing (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define the element;
they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Model (EF000010) | pillow block (base-mounted housing for an insert bearing with a spherical outer ring); this version the housing only |
| 2 | Material (EF002169) | cast iron housing, painted (the `M-CAST-BLUE` layer); the insert's rings bearing steel (not drawn) |
| 3 | Suitable for shaft diameter (EF026298) | 25 mm |
| 4 | Inner diameter (EF000065) | 25 mm (the insert's bore, the shaft's size; the insert is not drawn) |
| 5 | Outer diameter (EF000015) | 52 mm: the insert's seat, drawn as a plain bore at this design's figure (What it meets: the figure a standard tabulates is a source wanted) |
| 6 | Length (EF001438) | 140 mm (the base's length along x); the insert's width is not stated (it belongs to the seat's open figure) |
| 7 | Max. number of revolutions (EF000250) | not stated: a bearing's speed limit is the insert's, from its standard or a maker's sheet, neither on file |
| 8 | Load bearing capacity (EF002918) | not stated: the dynamic load rating and rating life (ISO 281) are the insert's, not on file; no load is claimed for the housing |

No ratings.csv: no feature of the class is a rating the checks read (no voltage, current, pressure or power), and no load or speed
is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the frame it bolts to | two Ø13.5 holes through the base at x ±52.5 (105 centres), y 0 | ISO 273 medium H13 (lib/standards/holes.csv) for M12; the spacing is this design's choice. Position: the two holes to each other, Ø0.5 at MMC ≤ H − F = 1.5 (ASME Y14.5 floating fastener, features.csv); the frame's holes are the host's |
| the insert bearing | the seat: a plain Ø52 bore through the tower along y at z 50; the housing's width 40 | **NOT ON FILE (B)**: the insert's spherical outer-ring diameter and width for a 25 bore are figures ISO 9628 (insert bearings) tabulates, and the housing's boundary dimensions for that insert (centre height, bolt spacing, base) are ISO 3228's (cast and pressed housings for insert bearings); neither is on file. The seat is drawn Ø52 and the housing at this design's figures until a document is on file; the insert is placed in a later version from its standard |
| the shaft | nothing drawn; it runs along y through the seat's axis at (x 0, z 50) | the host's shaft (25, Class values 3); the insert's set screws or an adapter sleeve hold it, not drawn |
| the grease nipple | not drawn | the insert's (or the housing's), a later version's figure |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | 140 (x) × 40 (y) × 14 (z 0 to 14), painted cast iron (`M-CAST-BLUE`) | 8 or more of iron beside and beyond each bolt hole (x 59.25 to 70 outside the hole, the tower's side 35 to the hole's edge 45.75); 14 thick, its end edges over the gate's 3 to 7 mm free-corner trap at r 0.5 (mech-r101) |
| tower | 70 (x) × 40 (y) × z 14 to 90, 0.5 into the base (one solid) | 9 of wall each side of the Ø52 seat and 14 above it; the tower is a plain block (no rounded crown: every free edge straight, nothing tangent, mech-r105) |
| centre height | 50 above the mounting face | the seat clears the base by 10 (z 24 to 76) |
| bolt holes | 2 × Ø13.5 at 105 centres, round | M12 (ISO 273 medium); round holes rather than slots so the hole checker reads them as the standard size; a slotted base is a later variant if a host needs the adjustment |
| seat | Ø52 through, plain | a design figure (What it meets); the 13.5 each side between the shaft's 25 and the seat is the insert's (its inner ring, rolling elements and outer ring, bearing steel, not drawn), not the housing's iron; the housing's iron is the 9 of wall each side and the 14 above the seat (tower row) |
| load, speed, mass, finish | not claimed | no figure is on file for them (lib/materials.csv has no density; ISO 281 is not on file) |

## Mechanism
None: one fixed body, no moving node, no port. The shaft and its rotation are the host's (the insert's inner ring, not drawn, is
what turns). behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `body` (x ±70, y ±20, z 0 to 90).

## Materials by layer
`M-CAST-BLUE` the housing (painted cast iron).

## Decals (Blender)
"complexes.org generic" on the tower's −y face, above the seat, centred.

## Notes
No vendor names, part numbers or marks. No load, speed or life claim: those are the insert's (ISO 281 for the rating life, not on
file) and nothing is sized against a load. A bearing is in the ETIM classes on file; the housing is not a part a dimensional
standard shapes once the insert's seat is set aside, so the housing is built generic to its class (OPERATING.md 12) and the insert
waits for its standard (never generic: ISO 9628, as ISO 15 for a deep groove ball bearing, the inventory's bearing-ball). A flange
unit, a take-up unit or a two-bolt housing of another centre height is another class value or another element. Not drawn: the
insert bearing (outer ring, inner ring, balls, seals, set screws), the grease nipple, the bolts, the shaft, the frame. One open
figure, class B (What it meets: the insert's seat, ISO 9628 / ISO 3228, a document wanted, lib/standards/wanted.md); the bolt
holes are ISO 273's and the rest are design choices.
The gate's fillet rule (r 0.5 for a device, lib/toolkit/fillet.py): every free-corner edge is 14 or longer (the base's 14, 40 and
140; the tower's 40, 70 and 76); the bolt holes' and the seat's edges are cut edges, skipped; the tower's bottom edges lie buried in
the base. Every bounding-box extreme lies on an axis-aligned box (the base's x ±70 and z 0, the y ±20 faces, the tower's top z 90);
nothing is tilted or nested, no node.

## Outputs (out/)
`bearing-pillow.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012129), our own design (mech-r105, unattended, 2026-11-11): the housing (base with two M12 holes, tower with the Ø52 seat bore at centre height 50); the insert bearing placed later from its standard |
| 1.1 | text only (review bearing-pillow-1.0 finding 1): the seat row says the 13.5 between the shaft and the seat is the insert's, not the housing's iron; geometry unchanged (mech-r117, unattended) |
