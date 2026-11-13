# panel-operator · v1.1 · operator console box 300 × 200, sloped face, four 22.5 mm cut-outs, gland plate, rear cover

**What** A sheet-steel operator console for a machine or a training bench: a box 300 wide and 200 deep, 60 high at the front and
160 at the back, whose top is one sloped operator face with four 22.5 mm cut-outs for pushbuttons, an E-stop or pilot lights. The
cables come in from below, through a gland plate with two M20 cable-entry holes; four M6 holes in the same plate fix the box to a
bench top, a pedestal or a bracket that has an opening under the cable entries (see "Mounting": with its glands fitted the box
cannot sit on a flat, unbroken top). The back is a cover hinged at its bottom edge, so the wiring behind the operators can be
reached.
**Class** enclosure · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened and
no folder record was used: the element is new.
**Units / frame** mm, Z up. Origin: the underside of the gland plate z = 0 at the box's front-left corner x = 0, y = 0. The person
stands at −y; the operator face slopes up toward +y; the rear cover opens toward +y.
**Built with** toolkit 1.3 · AutoLISP command `OPCONS` · no parameters.

## Mechanism
`door` (the rear cover): rotates about its bottom edge (the hinge line x across the box at y = 200, z = 2.5), 0 to −90° about +x,
so its top swings outward (+y) and down until the cover lies flat behind the box. Closed, it sits between the two sides with 0.5
clear at each side, 0.5 above the gland plate and 1 below the sloped face; through its travel it moves only outward, behind the
box. The hinge and the cover's fixing screws are not modelled.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| operator cut-out | Ø22.5, four | op-pb-22-1no / op-estop-22-2nc / op-pilot-22 `CUTOUT` (toolkit/std22.py); lib/standards/holes.csv "22.5 operator cut-out" (22.3 to 22.7) |
| cable-entry hole | Ø20.5, two | gland-m20 1.2 `CUTOUT`; lib/standards/holes.csv "M20 x 1.5 entry" (20.2 to 20.7) |
| fixing hole | Ø6.6, four, M6 | ISO 273 medium (H13), lib/standards/holes.csv |

Both cut-out figures are read from the elements themselves (element.py loads op-pb-22-1no and gland-m20), so they cannot drift apart.
The 2.0 sheet of the operator face lies inside the panel range the 22 mm operators clamp (toolkit/std22.py `PANEL_RANGE`, 1 to 6).
The operators and the glands are not placed in this version: the holes are modelled; a later version places the elements
(EM's rule).

## Mounting (what the surface under the box needs)
The gland plate's underside, z = 0, is the mounting face. A gland fitted in a cable entry stands below it: gland-m20 1.3 has its
origin on the plate's outer face, the dome outward (here −z), the body 27.7 proud of that face and 29.72 across its largest
diameter; the locknut is inside the box (z 2.0 to 8.0). So the surface the box is fixed to needs, under each entry:

| what | figure | from |
|---|---|---|
| a clear opening centred under each entry (x 100 and 200, y 140) | at least Ø29.72, or one slot under both of at least 129.72 × 29.72 (x 85.14 to 214.86, y 125.14 to 154.86) | gland-m20 1.3 "largest diameter" 29.72; the entries' 100 pitch (element.py GLAND_XY) |
| clear depth below z = 0 | 27.7 for the gland, then the cable's bend below it | gland-m20 1.3 "body above the seat face" 27.7; the bend radius is the fitted cable's own figure, not this box's: an assembly that places the box takes it from the cable element it routes |

The opening lies inside the fixing pattern (x 25 to 275, y 25 to 175) and at least 60 from every fixing hole's centre (the slot's corner nearest a hole: 60 in x, 20 in y, 63 apart), so the four
M6 holes still bear on the surface around it. A bench top with a cut-out, a pedestal or bracket open under the entries, or a frame
across the two short sides all meet it. Feet or standoffs under the plate would change the outside and the origin's surface: a
major version, not this one (OPERATING.md 7).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| outside | 300 wide × 200 deep; 60 high at the front, 160 at the back (to the sloped face's underside) | four operators side by side, room behind them for their latches and contact blocks |
| operator face slope | 100 rise over 200 run (26.6°), face 223.6 long | the face turns toward a standing or seated person |
| sheet | 2.0 steel, RAL 7035, every panel | |
| operator cut-outs | x = 52.5, 117.5, 182.5, 247.5 (65 pitch), half-way up the slope (111.8 from the face's front edge) | 65 pitch leaves room for an E-stop's 60 × 60 plate or a 30 × 50 legend plate at each |
| cable entries | x = 100 and 200, y = 140 | toward the back, under the deepest part of the box |
| fixing holes | x = 25 and 275, y = 25 and 175 (250 × 150 centres) | |
| rear cover | 295 × 155.5 × 2.0, swings 90° | |
| assembly | gland plate under everything; the sides stand on it, cut along the face's underside; the front stands between the sides; the sloped face lies on the sides and the front | |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four Ø6.6 fixing holes are one pattern (250 × 150): position Ø0.5 at MMC (features.csv; H − F = 6.6 − 6.0 = 0.6), datum A the
gland plate's underside, the four holes located to each other. The cut-outs are cut-outs, not a fastener pattern.

## Named nodes
`door` (rotate, above). Colliders `body` (the box less the cover) and `door`.

## Materials by layer
`M-STEEL-7035` every panel and the rear cover.

## Notes
No IP rating, no load rating and no safety claim: the box is a housing for operators, and an E-stop placed in it is the E-stop
element's function, not this box's. No vendor names; no label in this version.

## Outputs (out/)
`panel-operator.lsp` · `.glb` (pivot on `door`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.1 | review panel-operator-1.0 finding 1 (mech-r23, unattended): "What" no longer says the box stands on a bench on its four M6 holes as if the top were flat; a "Mounting" section states what the surface needs under the cable entries with glands fitted (an opening of at least Ø29.72 per entry, 27.7 deep, then the cable's bend), from gland-m20 1.3. Text only: the part, nodes, origin, colliders and cut-outs unchanged (a minor) |
| 1.0 | first build, our own design (mech-r9, unattended) |
