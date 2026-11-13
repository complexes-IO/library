# gland-m20 · v1.3 · M20 × 1.5 nylon cable gland

**What** M20 × 1.5 nylon cable gland with locknut, for 6.1 to 13 mm cord. Built from the Stage 0 brief `references/measure.md`.
**Class** connector · **Baseline** reference gland, 2-D drawing p. 1 and STEP read-back (references/measure.md). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: cut-out centre: knockout centre on the plate's outer face y = 0, dome toward −y, locknut toward +y.
**Built with** toolkit 1.3 · AutoLISP command `GLND` · `plate_t` (2.0; up to 4.2, the locknut's 6.0 on the 10.2 thread) · CUTOUT 20.5.

## Dimensions
| feature | mm | where in the build | source |
|---|---|---|---|
| largest diameter | 29.72 | the body / dome nut hex's corners, turned to it | drawing p. 1 (1.17 in) |
| body above the seat face | 27.7 | y 0 to −27.7 | drawing p. 1 (1.09 in) |
| thread length from the seat face | 10.2 | y 0 to +10.2 | drawing p. 1 (0.4 in) |
| overall | 37.9 | y −27.7 to +10.2 | 27.7 + 10.2; the drawing's 38.1 (1.5 in, printed to one decimal: 1.45 to 1.55 in) |
| thread | M20 × 1.5, Ø20 envelope | plain cylinder, no thread form | drawing p. 1; ISO 261 metric fine series (the standard's text is not in the library: no tolerance class claimed) |
| body and dome nut hex | 27 AF | one profile, y 0 to −27.7 | drawing p. 1 gives 25 and 27; 27 to the body and the dome nut by the STEP read-back (both 27.6 AF, measure.md): Assumption (B), the drawing's label for each hex not yet read |
| locknut hex | 25 AF × 6.0, sharp corners (28.87) | y plate_t to plate_t + 6.0, inside | 25 from drawing p. 1 (read-back 29.7 across corners, ≈ 25.7 AF); 6.0 from the read-back |
| hex turn about the axis | body 15° (a corner 15° off x and off z); locknut 0° (a flat facing x) | each hex | a design choice (no figure sets it; a gland and its locknut sit at any turn). Body at 0° would put a flat on x: the glb measures 27.0 there while the catalogue's size, which does not apply cuts, reads 30, and Godot QA fails at > 2 mm; at 15° both read 29.3. The locknut at 0° shows its 25 AF on x, where the AutoCAD gate's brief check finds it |
| dome end | square | y −27.7 | the crown's rounding is not in the brief: built square, Assumption (C) |
| seal insert | Ø13 × 0.8, 0.2 proud of the dome end | node `self`, y −27.9 to −27.1 | Ø13 = the largest cord (product page, 0.51 in); 0.2 proud for GEO-050 |
| cut-out | Ø20.5 | CUTOUT | lib/standards/holes.csv:27, M20 × 1.5 entry 20.2 to 20.7 (manufacturer practice, not in EN 62444); 20.5 a design choice inside that range |
| tightening torque | NOT ON FILE (B) | behaviour.csv, pin `cable` (node `self`) | the maker's sheet, not in the brief; a fit figure, so class B (OPERATING.md 6), EM's. Not modelled; the twin reads it as text only |

## Named nodes
`self` (kind port, unit cable, gender none: the pass-through a connections.csv row names; its pivot at the dome end, y −27.7.
A gland declares gender none, OPERATING.md 6 / PIN-002)

## Decals (Blender)
none

## Notes and assumptions
Figures marked **Assumption** were NOT ON FILE in the brief; a document figure replaces them as a minor version. Exterior only: the interior (mechanism-first ruling) arrives per interior-first-prompt.txt.
The hexes are solids (a cylinder with six flats cut, as nut-m12), so the DWG and STEP carry the whole gland. The body hex and the dome nut share one profile and are built as one solid; the parting line between them (the dome nut 15.9 long in the read-back) is not modelled. No rating is stated (the brief's IP figures are the product page's, not this element's).

## History
| version | change |
|---|---|
| 1.3 | PIN-002 (mech-r14): the `self` port declares gender none (a gland, OPERATING.md 6, EM 2026-11-05); the part, nodes, origin and cut-out unchanged. Correction to 1.2's row: out/preview-outside.png is not removed yet; it is no longer written, and its `git rm` waits for an attended session (lib/needs-em/mech.md item 17) |
| 1.2 | review gland-m20-1.1 (mech-r8): the body stands 27.7 proud of the seat face and the thread runs 10.2 from it (1.1 built 38.1 + 12.2 = 50.5, the thread counted twice); the hexes are solids, not glTF-only meshes, within the drawing's 29.72 (1.1 used 27 AF sharp, 31.18 across corners); hex sizes per the STEP read-back (27 body and dome nut, 25 locknut); the Ø24 dome and Ø27 skirt with no source removed; neutral baseline; Dimensions table; stale out/preview-outside.png removed |
| 1.1 | render fix (GEO-050): the seal insert's face was flush with the dome end; now 0.2 proud |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
