# tslot-nut · v1.0 · slide nut M8 for tslot-40's T-slot, generic, 20 long, body 14 x 3 under the lips, neck 9 x 3 in the opening

**What** A slide nut for the T-slot of tslot-40, the library's 40 × 40 framing profile: the nut that a bracket, a guard panel, a
sensor bracket or any part is screwed to anywhere along the profile. It slides into the slot from the profile's cut end; an M8
screw through the host's part is turned into it and draws its body up against the undercut side of the slot's lips, clamping the
part on the profile's face. A neck in the slot's opening keeps it from turning while the screw is started. The inventory row lists
it as a common part ("T-slot nut for 40 mm profile"), the made_of of tslot-40 and so of every frame, guard and bench built from it.
**Class** connector-part · **Baseline** our own design: generic slide nut (ETIM 10.0 EC000096 Slide nut), OPERATING.md 12
"Generic elements" (EM, 2026-11-07); lib/inventory.csv marks the row own_design "generic" with etim EC000096 (the class and its 15
features are on file, so the element is built generic and states its class values). No product was matched and no vendor file was
opened. The slot it runs in is tslot-40 1.0's, read with library.load; the thread's figures are derived; every other size is a
design choice.
**Units / frame** mm, Z up. Origin: the nut's bearing face (the body's top, the face the screw draws against the lips) on the
thread's axis. x runs along the slot; +z points out of the slot toward the profile's face (the neck). Extents x ±10, y ±7, z −3 to
3. In tslot-40's frame, in its top slot at a position x0 along the run, the nut's origin sits at (x0, 0, 36): the lips' underside.
**Built with** toolkit 1.3 · AutoLISP command `TSLOTNUT` · no parameters.

## Class values
ETIM 10.0 class EC000096 Slide nut (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | steel (lib/materials.csv steel-mild; the grade not stated) |
| 2 | Surface protection (EF000139) | zinc-plated |
| 3 | Layer thickness surface protection (EF025871) | not stated: no plating standard is in lib/standards/sources.csv, so no thickness is designed to |
| 4 | Length (EF001438) | 20 mm, along the slot |
| 5 | Head width (EF006645) | 14 mm: the body across the slot, under the lips (the neck 9) |
| 6 | Thread size (metric) (EF003563) | M8 |
| 7 | Thread size (imperial) (EF003715) | none: a metric thread |
| 8 | Thread type (EF001758) | ISO metric coarse, M8 × 1.25 (ISO 261), internal tolerance class 6H (ISO 965-1) |
| 9 | With spring (EF001261) | no |
| 10 | With washer (EF005076) | no |
| 11 | With clamping plate (EF016078) | no |
| 12 | With hexagonal nut (EF009516) | no |
| 13 | With thread end (EF021036) | no |
| 14 | Clickable (EF006591) | no: it slides in from the profile's cut end |
| 15 | Material click-mount element (EF016075) | none: not clickable |

## What it meets
| figure | value | source |
|---|---|---|
| the slot it runs in | tslot-40's T-slot: an opening 10 wide, lips 4 thick, an undercut 15 wide × 6.5 high under them | tslot-40 1.0 (element.py THROAT, LIP, UNDER_W, UNDER_H, read with library.load, so the two cannot drift apart) |
| its fit in the slot | body 14 wide in the 15 undercut, neck 9 wide in the 10 opening: 0.5 clear each side; the body 3 high under the lips leaves 3.5 below it; the neck's top 1.0 under the profile's face | design: the clearances are this design's, sized to tslot-40's slot so the nut slides along it freely and the host's part clamps on the profile's face (tslot-40 1.0), never on the nut |
| the lips it bears on | 2.0 each side: the body's 14 over the opening's 10 | design: from tslot-40 1.0's figures; the bearing area is geometry, not a rating |
| the screw | M8 internal thread through the body and the neck, 6 long (z −3 to 3), on the nut's axis; drawn as a plain bore Ø6.6468 (D1 min), features.csv kind `own` | derived: `python lib/build.py derive thread M8` (ISO 68-1 basic profile; ISO 965-1 clause 10, internal 6H: D1 6.6468 to 6.9157, D2 7.1881 to 7.348; ISO 261 pitch 1.25). The screw (screw-iso4762, tslot-40's made_of, a common part not built yet) and its length are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| length | 20 along the slot | twice the slot's opening, so the nut sits square in the slot while the screw is started |
| body | 20 × 14 × 3 (z −3 to 0) | wider than the opening, so it can't pull through and bears 2.0 on each lip; 3 high, its short edges 3.0 so the gate's fillet rule skips them (mech-r101: free-corner edges ≤ 3 or ≥ 8 at r 0.5) |
| neck | 20 × 9 × 3 (z 0 to 3) | in the opening, so the nut can't turn in the slot; together with the body it gives the thread 6 of length |
| thread | M8 through, on the axis | an M8 screw's shank passes tslot-40's 10 opening with 1 each side (tslot-40 1.0's choice) |
| edges | square; no chamfer or lead-in drawn | the slot ends and the nut's ends are cut square |
| holding force, tightening torque, slip load | not claimed | no ETIM feature of this class states one; the nut is not sized against a load; the screw's torque is the host's joint |

## Named nodes
None: a structural part with no moving part and no port. Collider `nut` (x ±10, y ±7, z −3 to 3, the neck's sides filled).

## Materials by layer
`M-ZINC` the nut (steel, zinc-plated).

## Notes
No vendor names, part numbers or marks; no label (too small). No load, torque, slip or mass claim (lib/materials.csv has no
density: the drawn volume is 20 × 14 × 3 + 20 × 9 × 3 less the bore through 6, 1380 − 208.2 = 1171.8 mm³). A profile's slide nut
is shaped by the profile's slot, which here is this library's own design (tslot-40), so no dimensional standard shapes it and it is
built generic to its ETIM class (OPERATING.md 12); a nut a standard shapes (ISO 4032 and its family) is another element. Not drawn:
the thread, a spring or ball that would hold it in place in a vertical slot (a later variant), the screw. The gate's fillet rule:
the default r 0.5 of class connector-part; every edge of the body and the neck is 20, 14 or 9 long (picked) or 3.0 (short,
skipped); the bore's edges are cut edges. The bounding box's extremes lie on the two boxes' axis-aligned faces.

## Outputs (out/)
`tslot-nut.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000096), our own design (mech-r115, unattended, 2026-11-12): body and neck sized to tslot-40 1.0's slot, M8 through |
