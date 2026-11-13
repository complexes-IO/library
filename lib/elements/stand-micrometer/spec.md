# stand-micrometer · v1.1 · micrometer stand, base 120 × 90 × 20, post Ø16 × 130, fork on the post's top, tilting clamp head 24 × 26 × 60 with an 8 slot for the micrometer's frame

**What** A micrometer stand: a flat base that stands on the bench, a post on it, and a tilting head that clamps an outside
micrometer by its frame, so both hands are free for the work and the thimble. The model shows the base block, the post, a fork
on the post's top, and the head (node `head`: a clamp block between the fork's cheeks with a slot across its top that seats the
micrometer's frame), tilting about a horizontal pin through the cheeks. lib/machines-factory.txt lists it with micrometer (the
micrometer row: the tool and its stand); the micrometer is a separate element (a generic row, not built) and is not placed. The
head is the mechanism: the twin sets its angle by name. stand-magnetic 1.0 (mech-r94) is its sibling: the same base-post-head
pattern with a swivel instead of a tilt.
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks stand-micrometer own_design
"yes", "micrometer stand"; request mech-8's answer: no ETIM class on file fits, so an own design as panel-clamp). No product was
matched and no vendor file was opened. Every size is a design choice except the slot's fit to the micrometer's frame, a figure
ISO 3611 may fix (not on file: class B, source wanted, What it meets).
**Units / frame** mm, Z up. Origin: the base's underside (on the bench) z = 0, on the post's axis x = 0, y = 0; the base's long
sides run along x. The head's tilt axis runs along y through the fork's cheeks at z 180; the head stands upright at rest with
its slot along x on top. Extents x ±60 and y ±45 (the base), z 0 to 228 (the head's top).
**Built with** toolkit 1.3 · AutoLISP command `STANDMIC` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| the bench | the base's underside, z = 0, 120 × 90, flat | it stands on the bench; where it stands is the assembly's. No fixing holes: a stand is moved to the work |
| the micrometer | the head's slot, 8 wide (y ±4), 30 deep from the head's top (z 198 to 228), through the head along x | **NOT ON FILE (B)**: whether a standard fixes the micrometer frame's section where it is clamped: ISO 3611 (outside micrometers; DIN 863-1 nationally) is the one to read. The reviewer reads it as setting metrological characteristics (flatness, parallelism, error limits) and not the frame's section, which would leave the frame free (review stand-micrometer-1.0); that is a reading, not a read clause, and ISO 3611 is not in lib/standards/sources.csv. So the slot's fit to the frame is a source wanted (OPERATING.md 6; DOC-009, the core's note mech-doc009-2026-11-11 item 2), not a figure of this design: the slot is drawn 8 wide, the frame held by a thumb screw not drawn, until the document is on file. Then either ISO 3611 is cited as leaving the frame free and the line closes, or its frame section is read and the slot follows it (a later version if it differs). micrometer is not built (inventory row, generic); when it is, its frame meets this slot or the slot changes |
| the operator | the head (the tilt) and the thumb screw not drawn | by hand; no torque or force figure |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base block | 120 × 90 × 20 (x ±60, y ±45, z 0 to 20) | a flat block heavy enough to stand still under a hand on the thimble (no mass is stated: lib/materials.csv has no densities); the post on its centre; the model's x and y extremes (an axis-aligned, uncut solid) |
| post | Ø16, from the base's top (z 20) to z 150 (130 long), on the base's centre | a plain round post that brings the micrometer to a hand's height above the bench |
| fork | a base block 20 (x) × 40 (y) × 10 on the post's top face (z 150 to 160), and two cheeks 20 × 6 × 30 up from it (z 160 to 190) at y −20 to −14 and 14 to 20, 28 apart inside | carries the tilt pin (not drawn) along y at z 180; the cheeks' edges are 6 and over, so the fillet gate rounds them |
| head | 24 (x ±12) × 26 (y ±13) × 60 (z 168 to 228), between the cheeks, 1 clear of each | the clamp block; its bottom corners lie 17 from the pin's axis, so at any tilt they stay above the fork's base (z 160); its top at z 228 is the model's z extreme (an axis-aligned box of a top-level node) |
| slot | 8 wide (y ±4) × 30 deep (z 198 to 228), through the head along x | seats the micrometer's frame; a cut-out of the head block (features.csv) |
| tilt | −30 to 30 degrees about the pin's axis (0, 0, 180) along y | enough to turn the anvils toward the hand either way |
| layers | base and head M-STEEL-7035 (painted steel); post and fork M-SILVER (bright steel) | a design choice, no finish claim |

## Mechanism
`head` (the clamp block with its slot; rotate about y through (0, 0, 180), −30 to 30 degrees): 0 is upright, as built, the slot
level on top. The block turns between the cheeks on a pin not drawn (internal mechanism the twin doesn't read); at ±30 its
bottom corners, 17 from the axis, reach down to z 163, above the fork's base (z 160), and its faces at y ±13 stay 1 clear of the
cheeks' inner faces (y ±14) at every angle, so the head meets nothing through its travel (MOT-010). The tilt lock and the clamp's
thumb screw are not drawn: this is the plain stand, one tilt.
behaviour.csv: `upright` (default) and `tilted` (manual toggle) for the head, a pose row at the range end.

## Named nodes
`head`: rotate about y through (0, 0, 180), range −30 to 30 degrees. Colliders, axis-aligned boxes: `base` (the base block),
`post`, `fork` (the fork's base and cheeks), `clamp` (the head at rest). None is named like a node.

## Materials by layer
`M-STEEL-7035` the base block and the head (painted steel, RAL 7035) · `M-SILVER` the post and the fork (bright steel). The
layer names say the colour and the kind of material shown; no grade is claimed.

## Decals (Blender)
"complexes.org" on the base's −y side face.

## Notes
No vendor names, part numbers or marks. No load, no stiffness and no accuracy claim: no calculation or test of the model is on
file. Not drawn: the tilt pin and its lock, the clamp's thumb screw, the micrometer. One open figure, class B: the slot's fit to
the micrometer's frame (What it meets); the document is asked for once in lib/standards/wanted.md and the element waits as
"source wanted" (OPERATING.md 6).
Gate note (mech-r92's and r93's lessons): the bounding box's extremes lie on axis-aligned, uncut solids (the base at x ±60, y ±45
and z 0; the head block at z 228: its slot leaves the top face at y ±4 to ±13); no node is nested; no solid is tilted at rest.

## Outputs (out/)
`stand-micrometer.lsp` · `.glb` (pivot on `head`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r95, unattended, 2026-11-11) |
| 1.1 | text only (mech-r108, unattended, 2026-11-12): the slot's fit to the micrometer's frame marked class B, source wanted (ISO 3611), in What it meets, the Baseline, Notes, features.csv and element.py, where 1.0 called it this design's figure with no standard named (DOC-009, the core's note mech-doc009-2026-11-11 item 2; review stand-micrometer-1.0's reading of ISO 3611 recorded, not cited as a read clause). Nodes, origin, sizes and cut-outs unchanged |
