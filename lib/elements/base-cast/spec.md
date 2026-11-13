# base-cast · v1.0 · drill base 900 × 1500 × 270, column seat 600 × 600 with 8 × M12 for column 1.1, work face 700 × 700

**What** A machine base for a drill: a box-section body standing on two runners, a machined column seat at its rear and a machined
work face at its front. The pillar and radial drills of lib/machines-factory.txt (drill-pillar, drill-radial) stand on a base of
this kind; a BOM places the column (column 1.1) on the base's `column-seat` and the work, or a table, on its `work-face`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks base-cast own_design
"yes"). No product was matched and no vendor file was opened. The column seat's bolt holes are on file (ISO 273, and column
1.1's pattern); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 under the column seat's centre x = 0, y = 0; front (the work face)
toward −y. The column seat's top plane, where column 1.1's base flange stands, is at z = 270.
**Built with** toolkit 1.3 · AutoLISP command `BASECST` · no parameters.

## Mechanism and the seats
- `column-seat` (fixed): the machined pad at the rear. Its pivot is the centre of its top face (0, 0, 270) with the axis +z:
  column 1.1 is placed there with its own origin (its base flange's underside at its centre) and no turn, so its eight base holes
  line up with the seat's and its ways face −y, over the work face. A BOM row reads `<tag>.column-seat`.
- `work-face` (fixed): the machined pad at the front. Its pivot is the centre of its top face (0, −700, 270) with the axis +z: the
  work, a vice or a table is placed there. A BOM row reads `<tag>.work-face`.
- The base has no moving part.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| column seat | 600 × 600 (x and y −300 to 300), top at z 270 | column 1.1's base flange, 600 × 600 (lib/elements/column/spec.md, "Its own sizes") |
| column bolts | 8 × M12, Ø13.5 holes through the seat and the body (z 60 to 270), on a 500 × 500 square (x and y −250, 0, 250; the centre left out) | ISO 273 medium (H13), lib/standards/holes.csv; the pattern is column 1.1's (lib/elements/column/features.csv). The bolts pass through both parts and take their nuts under the body, in the space between the runners: clearance holes in both parts with nuts, the floating fastener column 1.1 requires of its mate (column spec.md, "GD&T"). The bolts and nuts are not built; their lengths are not checked (no screw or nut table is on file) |
| the column's ways over the work | column 1.1's ways run from its z 400, so 670 above the floor on this seat: 400 above the work face (z 270) | column 1.1 "Its own sizes" ("the lowest 400 is left for the table or work below the head") |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The eight holes carry a declared position tolerance Ø1.2 at MMC to A, the column seat's top face, the holes located to each other
(features.csv; H − F = 13.5 − 12 = 1.5), the same as column 1.1's flange holes. With nuts on both sides of the joint each part may
take the whole H − F (ASME Y14.5-2018 Appendix B, the floating-fastener case), so Ø1.2 in both parts fits. The ISO 2768-m general
tolerance of the pattern's 707 mm diagonal (±0.8, lib/standards/general-tolerances.csv row m 400-1000; a Ø2.3 zone) would not
hold it, so the seat is drilled in one set-up with its machining. ASME Y14.5 is not a row in lib/standards/sources.csv (the
core's open item, review mech-r47 finding 2); GDT-010 checks the pattern as floating, which is what it is here.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| footprint | 900 wide (x −450 to 450), 1500 long (y −1100 to 400) | the column's 600 seat with 150 to each side and 100 behind it, and 800 in front of it for the work face |
| runners | two, 60 wide (x ±390 to ±450) and 60 high (z 0 to 60), the base's full length, under its long sides | the base stands on them; the 780 × 60 space between them takes the column bolts' nuts. The column is bolted to the base before the base is set in place |
| body | 900 × 1500, from the runners (z 60) to its top face (z 250) | a closed box section; drawn by its outside: a cast base is cored and ribbed inside, not seen. The bolts pass through it, so its holes are drawn the body's full height |
| column seat | 600 × 600 × 20, 20 proud of the body's top (z 250 to 270), 100 from the body's back and 150 from its sides | the machined face the column's flange stands on |
| work face | 700 × 700 × 20 (x ±350, y −1050 to −350, z 250 to 270), 50 from the body's front and 50 from the column seat | the machined face the work stands on; plain: T-slots wait on ISO 299 (not on file) |
| floor fixing, levelling, coolant trough, chip edge | not drawn | the installation's and the machine's; a later version once their parts are on file |

## Named nodes
`column-seat` and `work-face` (fixed, above). Colliders `base` (runners and body), `seat` (the column seat) and `table` (the work
face); none is named like a node.

## Materials by layer
`M-STEEL-7035` the runners and body (painted RAL 7035) · `M-SILVER` the column seat and work face (bare machined steel, shown in
the library's bright-metal layer; the library has no `M-STEEL` render material).

## Notes
No load rating, no stiffness or accuracy claim: no drill's mass, thrust or table tolerances are on file, so the base is not sized
against them. The volume is 284 059 527 mm³ (runners 10 800 000, body 256 500 000 less its eight holes 217 571, column seat
7 200 000 less its eight holes 22 902, work face 9 800 000; written as volume only: lib/materials.csv gives steel no density, so
no mass is stated). No vendor names, no label.

## Outputs (out/)
`base-cast.lsp` · `.glb` (pivots on `column-seat` and `work-face`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r61, unattended) |
