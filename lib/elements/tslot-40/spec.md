# tslot-40 · v1.1 · T-slot framing profile 40 x 40, four T-slots 10 wide (undercut 15 x 6.5), centre bore at M8 tapping, cut to length

**What** An aluminium T-slot framing profile, 40 × 40: the bar machine frames, guards, benches and fixtures are built from
(lib/inventory.csv row `tslot-40`, own_design yes, "aluminium T-slot profile, 40 x 40"; 10 systems: gantry-xyz,
guarded-machine-door, machining-station, mechanisms-bench, pneumatic-pick-and-place, pneumatic-trainer, robot-cell,
rotary-index-table, servo-pick-and-place, vision-inspection-station). A square bar with one T-slot along its whole length in each
of its four faces, for slot nuts that brackets, panels and parts bolt to anywhere along it, and a centre bore along its axis that
an end can be tapped in for an end fastening. Cut to length by the `length` parameter.
**Class** rail · **Baseline** our own design (OPERATING.md 12, own designs; request mech-13's answer, core watch 2026-11-12: no
ETIM 10.0 class on file fits a T-slot profile, so the row is own design "yes", built first of the ten). No product was matched and
no vendor file was opened: the folder's reference record (a catalogue rail, references/source.txt) is not what this element is
built from, and no figure was taken from it. The bore's diameter is derived (ISO 68-1, ISO 965-1); every other size is a design
choice.
**Units / frame** mm, Z up. Origin: the run's start (x = 0) on the profile's centre line (y = 0), at its underside face (z = 0).
The run goes along +x; the section is y ±20, z 0 to 40; the centre bore's axis is at (y 0, z 20). Extents x 0 to `length`,
y ±20, z 0 to 40 (at the default 1000: 1000 × 40 × 40).
**Built with** toolkit 1.3 · AutoLISP command `TSLOT40` · parameter `length` (default 1000; any cut length).

## What it meets
| figure | value | source |
|---|---|---|
| the slot nut | each T-slot: an opening 10 wide in the face, a lip 4 thick, an undercut 15 wide × 6.5 high, the floor 10.5 below the face; the lips overhang the undercut 2.5 each side for a nut to bear on | this design's slot (request mech-13's answer: the slot width a design choice). The answer named tslot-nut's figures for it, but tslot-nut had no folder when this profile was built, so the profile defines the slot and the nut is sized to it: tslot-nut 1.0 (mech-r115, generic EC000096) reads this slot by library.load, its body 20 × 14 × 3 under the lips and its neck 20 × 9 × 3 in the 10 opening, 0.5 clear each side |
| the screws through brackets into the slot nuts | an M8 screw's shank (8) passes the 10 opening with 1 each side | this design's choice against the M8 nominal diameter 8 (ISO 261); the nut is tslot-nut 1.0 and the bracket bracket-angle 1.2 (both built, rows below and above); the screws (screw-iso4762, the inventory's made_of, not built yet) are the hosts', placed with the profile in a later version or an assembly |
| the inner-corner bracket | bracket-angle 1.2 reads this profile's face (40) and slot opening (10) by library.load: legs 40 long, 36 wide (2 inside each edge of the 40 face), one Ø9.0 M8 clearance hole (ISO 273 medium) per leg 20 from the inner corner on the face's centre line, over the slot | bracket-angle 1.2 (review mech-r109 finding 1 (c)); the bracket is the host's, placed with the profile in an assembly |
| an end fastening | the centre bore Ø6.6468 through the whole length, plain, so either end can be tapped M8 (6H) at its cut length | derived: `python lib/build.py derive thread M8` (ISO 68-1 basic profile; ISO 965-1 clause 10, internal 6H: D1 6.6468 to 6.9157; ISO 261 pitch 1.25). The tapping and its depth are the host's, at the end it fastens; features.csv kind `own` |

## Section (computed from the drawn section)
The square 40 × 40 less the four slots (each 137.5 mm²: the throat 10 × 4 and the undercut 15 × 6.5) and the bore (34.70 mm²),
by the parallel-axis theorem over exact rectangles (element.py `section()`, asserted against these figures by hand):

| figure | value |
|---|---|
| area | 1015.30 mm² |
| second moment of area, either axis through the centre (the section is the same after a quarter turn) | 150 502 mm⁴ (15.05 cm⁴): 213 333.3 for the square, less 58 412.9 for the two slots across the axis, 4 322.9 for the two along it and 95.8 for the bore |
| section modulus, either axis (I over 20) | 7 525 mm³ (7.53 cm³) |

These are geometry, not a rating: no alloy, temper, allowable stress or deflection limit is on file, so no load, span or stiffness
claim is made.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 40 × 40, square | the inventory row's size; one bar for posts, rails and cross members alike |
| slot opening | 10, centred in each face | an M8 screw's shank passes with 1 each side |
| lip | 4 thick (face to undercut) | the face that a bracket or panel clamps against, with the nut drawn up under it |
| undercut | 15 wide × 6.5 high, its floor 10.5 below the face | 2.5 of lip each side for a slot nut to bear on; neighbouring slots' undercuts keep 2.8 of web between their corners and 6.2 of core round the bore |
| centre bore | Ø6.6468, through | M8's tapping diameter, so an end fastening needs no drilling (What it meets) |
| section | solid apart from the slots and the bore | the model shows what can be seen at a cut end; no cavities are drawn |
| length | the `length` parameter, default 1000 | a profile is cut to the length its host needs; a parameter stays out of the id (OPERATING.md 6) |
| end finish | square, plain | cut ends; end caps are not drawn |

## Named nodes
None: a structural part with no moving part and no port. Collider `profile` (the full 40 × 40 × `length` box, the slots filled).

## Materials by layer
`M-ALU-ANOD` the profile (anodised aluminium; no alloy or temper is claimed).

## Notes
No vendor names, part numbers or marks; no label. No load, stiffness, mass or alloy claim (lib/materials.csv has no density: the
drawn volume at the default length is 1015.30 × 1000 = 1 015 300 mm³). Not drawn: slot nuts, brackets, screws, end caps, slot
covers (the hosts' or later versions'). The gate's fillet rule: this element sets r 0.5 on every primitive (element.py `P.radii`,
mech-r106: the gate reads each primitive's radius); the only free-corner edges are the 4 long edges along the run and, on each end
face, the 8 segments of 15 between a corner and a slot; the slots' and the bore's edges are cut edges, skipped. The bounding box's
extremes lie on the bar's axis-aligned outer faces.

## Outputs (out/)
`tslot-40.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r109, unattended, 2026-11-12; request mech-13's answer): 40 × 40 bar, four T-slots, centre bore at M8 tapping, `length` parameter |
| 1.1 | review mech-r109 finding 1 (c) (mech-r122, unattended, 2026-11-12): What it meets gives bracket-angle 1.2's figures on this profile and tslot-nut 1.0's (built since); text only: the part, origin and holes are 1.0's |
