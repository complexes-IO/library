# jbox · v1.1 · junction box 240 × 240 × 120, wall mount, hinged lid, two M20 entries

**What** A sheet-steel junction box for a wall, a machine frame or a panel side: a box 240 wide, 240 high and 120 deep, open at
the front and closed by one flat lid hinged at its left edge. The cables come in from below, through two M20 cable-entry holes in
the bottom; four M6 holes in the back fix the box to the wall. Terminals or a DIN rail inside are not part of this element: an
assembly places them.
**Class** enclosure · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, references/source.txt, validation.json) describes a catalogue box with its sizes; no
figure was taken from it: this box's sizes differ from it and are this lane's choices (below). The record stays as it is.
**Units / frame** mm, Z up. Origin: the box's underside z = 0 at its front-left corner x = 0, y = 0. The back face y = 120 goes
against the wall; the person stands at −y; the lid opens toward −y.
**Built with** toolkit 1.3 · AutoLISP command `JBOX` · no parameters.

## Mechanism
`lid`: rotates about the box's front-left vertical edge (the line x = 0, y = 0, z up), 0 to −110° about +z, so its free (right)
edge swings outward (−y) and round to the left of the box. Closed, it lies over the front edges of the top, the bottom and the
sides (y −2 to 0, the full 240 × 240); through its travel every point of it stays at y ≤ 0 or x ≤ 0, outside the box, and away from
the wall behind the back. The hinge and the latch are not modelled (a hinge and a latch are later own designs on the element list,
next.md #12 and #13; this box places them in a later version).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| cable-entry hole | Ø20.5, two, in the bottom | gland-m20 1.3 `CUTOUT`; lib/standards/holes.csv "M20 x 1.5 entry" (20.2 to 20.7) |
| fixing hole | Ø6.6, four, M6, in the back | ISO 273 medium (H13), lib/standards/holes.csv |

The entry figure is read from the gland element itself (element.py loads gland-m20), so the two cannot drift apart. The 2.0 sheet
of the bottom lies inside the plate range gland-m20 is built for (its `plate_t` 2.0, up to 4.2). The glands are not part of the
box: the entry holes are the box's own feature, and an assembly fits gland-m20 (released, station 8) in the entries its cables use,
as a box is fitted on site. So the box places no gland.

## Mounting (what a fitted gland needs)
The bottom's underside, z = 0, is the face the glands stand on. gland-m20 1.3 has its origin on the plate's outer face, the dome
outward (here −z), the body 27.7 proud of that face and 29.72 across its largest diameter; its locknut (25 AF, 28.87 across the
corners, 6.0 high) is inside the box, on the bottom (z 2.0 to 8.0).

| what | figure | from |
|---|---|---|
| clear space under each entry (x 80 and 160, y 60) | at least Ø29.72, 27.7 deep below z = 0, then the cable's bend | gland-m20 1.3 "largest diameter" 29.72, "body above the seat face" 27.7; the bend radius is the fitted cable's own figure, taken by an assembly from the cable element it routes |
| locknut room inside | 28.87 across the corners at 80 pitch: 51.1 between the two nuts; 45.6 to the inside of the front, 43.6 to the back's inner face; 63.6 to each side's inner face | gland-m20 1.3; this box's entry positions |

So the box hangs with its bottom free: nothing may stand under it closer than the glands and the cables' bends.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| outside | 240 wide × 240 high × 120 deep (with the lid closed: 122 deep) | room for a short DIN rail or a row of terminals behind two cable entries |
| sheet | 2.0 steel, RAL 7035, every panel and the lid | |
| cable entries | x = 80 and 160 (80 pitch, centred on the width), y = 60, the middle of the bottom's depth (0 to 120), bottom only | the cables come up from below; nothing enters from the top |
| fixing holes | x = 30 and 210, z = 30 and 210 (180 × 180 centres) | 28 from each side's inner face, room for an M6 screw head inside |
| lid | 240 × 240 × 2.0, swings 110° | |
| assembly | bottom and top full width and depth; the sides between them; the back between the sides; the lid on the front edges | |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four Ø6.6 fixing holes are one pattern (180 × 180): position Ø0.5 at MMC (features.csv; H − F = 6.6 − 6.0 = 0.6), datum A the
back's outer face, the four holes located to each other. The two entry holes are cut-outs for glands, not a fastener pattern.

## Named nodes
`lid` (rotate, above). Colliders `body` (the box) and `lid`.

## Materials by layer
`M-STEEL-7035` every panel and the lid.

## Notes
No IP rating, no load rating and no safety claim: the lid has no seal or latch in this version. No vendor names; no label in this
version.

## Outputs (out/)
`jbox.lsp` · `.glb` (pivot on `lid`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (drafted by the mech run of 2026-11-07 19:07, finished and gated in mech-r46, unattended; next.md #8) |
| 1.1 | review jbox-1.0 finding 1, text only: the cable entries' y = 60 stated as the middle of the bottom's depth (0 to 120), in spec.md and element.py's comment; no model change (mech-r60, unattended) |
