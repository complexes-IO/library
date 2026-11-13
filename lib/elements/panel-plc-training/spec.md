# panel-plc-training · v1.1 · bench-top PLC training panel 600 × 480, two DIN-rail rows, six 22.5 mm operator cut-outs, two feet

**What** A sheet-steel training panel that stands on a bench: an upright back plate 600 wide and 480 high on two feet, with a rib
behind each foot. The plate carries the fixing holes of two 35 mm DIN rails (a PLC, its I/O modules, the 24 V power supply and the
terminals clip onto them) and, below the rails, a row of six 22.5 mm cut-outs for pushbuttons, pilot lights and an E-stop. Four M6
holes in the feet fix the panel to the bench.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match; lib/inventory.csv marks the row
own_design). No vendor file was opened and no folder record was used: the element is new.
**Units / frame** mm, Z up. Origin: the bench top z = 0, under the plate's front face y = 0, at its left edge x = 0. The devices
mount on the front (−y), where the person stands; the feet reach 150 to each side of the plate.
**Built with** toolkit 1.3 · AutoLISP command `PLCTRN` · no parameters.

## Mechanism
None: the panel has no moving part. Collider `body` (the panel's envelope, feet included).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| rail panel screws | M5, through the rail's slots, a screw every 8th slot (fix_pitch 200 at 25 slot pitch, first slot 12.5 from the rail's end) | din-rail-35 1.1 `SLOT`, `PARAMS["fix_pitch"]` and its build(); element.py loads the rail, so the holes follow the rail's slots |
| rail screw hole | Ø5.5, six, M5 | ISO 273 medium (H13), lib/standards/holes.csv |
| operator cut-out | Ø22.5, six | op-pb-22-1no `CUTOUT` (toolkit/std22.py); lib/standards/holes.csv "22.5 operator cut-out" (22.3 to 22.7) |
| bench screw hole | Ø6.6, four, M6 | ISO 273 medium (H13), lib/standards/holes.csv |

The 2.0 plate lies inside the panel range the 22 mm operators clamp (toolkit/std22.py `PANEL_RANGE`, 1 to 6). The rails, the
devices on them (plc0 1.1, term-4mm) and the operators are not placed in this version: their holes are modelled; a later version
places the elements (EM's rule).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| back plate | 600 wide × 480 high × 2.0, standing on the feet (bottom edge z = 2, top z = 482) | two rail rows and an operator row at a bench-top working height |
| rails | two rows, centrelines z = 260 and 400 (140 apart); each rail 425 long, x = 87.5 to 512.5, centred on the width | a 105 high device on each row leaves 35 between the rows for the wires of devices wired from their top and bottom faces (terminals), and 29.5 above the top row; plc0, whose M12 cordsets leave its bottom face, needs more below it: it goes on the upper row only, with the lower row kept empty under it ("Where plc0 goes", below); 425 = 17 slots, so the 1st, 9th and 17th carry screws (x = 100, 300, 500) and the rail sits symmetric |
| rail capacity (not modelled) | per row 425 less two 8 end clamps = 409. Upper row: plc0 (90) and about 50 feed-through terminals at 6.0 pitch (term-4mm). Lower row: the 90 under plc0 kept empty, so about 50 terminals beside it | the layout the holes are chosen for; the devices are placed in a later version |
| operator cut-outs | x = 100, 180, 260, 340, 420, 500 (80 pitch), z = 110 | 80 pitch leaves room for an E-stop's 60 × 60 plate or a 30 × 50 legend plate at each; below the rails, within reach |
| feet | two, 60 × 300 × 2.0, at x = 30 and 510, y = −150 to 150 | 150 in front of and behind the plate, so the panel stands without a bench screw |
| ribs | 2.0 × 148 × 150, behind the plate on each foot's outer edge (x = 30 and 568) | hold the plate square to the feet; on the outer edge, clear of the bench screws and of the operators' contact blocks (x ≥ 85) |
| bench screw holes | x = 60 and 540, y = −120 and 120 (480 × 240 centres) | on each foot's centre line, 30 from its ends |
| sheet | 2.0 steel, RAL 7035, every part | |

## Where plc0 goes (the cordsets below it)
The row pitch stays 140 (the rail holes are 1.0's). plc0 1.1 takes its two M12 cordsets on its bottom face, so where it may sit is
set by the length below it, all figures from elements on file:

| figure | value | source |
|---|---|---|
| plc0 | 105 high, centred on its rail; sockets on the bottom face standing 12.6 below the body, at 31.5 and 58.5 from its left face, axis 30 in front of the rail crown | plc0 1.1 element.py (`W`, `H`, `D`, the socket loop) |
| rail crown | 7.5 in front of the plate, so the socket axes stand at y = −37.5 | din-rail-35 1.1 (TH35-7.5, `RH`) |
| longest plug on file | 53.8, socket rim to cable exit (L male); D male 47.5, L female 53.0 | plug-m12 spec.md, Dimensions "overall" |
| cable bend | 5 × Ø fixed: 49 for the L cable (Ø9.8), the largest | cordset-m12 spec.md, Baseline |
| below plc0's body | 12.6 + 53.8 + 49 = 115.4 | the three above |

- **Upper row (rail z = 400): plc0 goes here.** Body z 347.5 to 452.5; socket rims at z 334.9; the plugs end by z 281.1 and the bend
  by z 232.1. On the lower row, the 90 under plc0 (its own x span) stays empty: a 105 high device there would reach z 312.5, inside
  that zone. The lower rail itself may run through it: its crown (y −7.5) lies 22.5 behind the L plug's Ø15 overmould (y −30).
  The cordsets turn toward the front (−y) at the bend; a cordset turned sideways along the rail widens the empty span by 49 on
  that side.
- **Lower row (rail z = 260): not for plc0.** There its socket rims are at z 194.9, the plugs end by z 141.1 and the bend reaches
  z 92.1, into the operator row (cut-outs at z 110; an E-stop's 60 × 60 plate spans z 80 to 140).
- Any other device with connectors on its bottom face takes the same sum (its socket, the plug, the bend) below it, from its own
  element, before an assembly places it here.

## GD&T (ISO 273, ASME Y14.5 floating fastener)
- The six Ø5.5 rail holes are one pattern (400 × 140): position Ø0.4 at MMC (features.csv; H − F = 5.5 − 5.0 = 0.5), datum A the
  plate's front face, the holes located to each other. ISO 2768-m alone would give a wider zone over the 400 span (GDT-010).
- The four Ø6.6 bench holes are one pattern (480 × 240): position Ø0.5 at MMC (H − F = 6.6 − 6.0 = 0.6), datum A the feet's undersides.
- The cut-outs are cut-outs, not a fastener pattern.

## Named nodes
None (no mechanism). Collider `body`.

## Materials by layer
`M-STEEL-7035` every part.

## Notes
No load rating, no IP rating and no safety claim: the panel carries training devices, and an E-stop placed in it is the E-stop
element's function, not this panel's. No vendor names; no label in this version.

## Outputs (out/)
`panel-plc-training.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r10, unattended) |
| 1.1 | review panel-plc-training-1.0 finding 1 (lib/reviews/elements/panel-plc-training-1.0.md), its second option: the rows stay 140 apart; the rails row no longer says a plc0 fits on each row; "Where plc0 goes" sets plc0 on the upper row with the lower row empty under it (115.4 below its body: socket 12.6, plug 53.8, bend 49, from plc0 1.1, plug-m12 and cordset-m12), not on the lower row (its bend would reach the operator row). Text only: part, holes, origin and colliders unchanged, a minor (mech-r24, unattended) |
