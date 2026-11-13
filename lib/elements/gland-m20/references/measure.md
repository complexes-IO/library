# gland-m20 · measure brief

Element `gland-m20`: M20 x 1.5 nylon liquid-tight cord grip (cable gland), straight, for 6.1 to 13 mm cord, IP66 / IP68 / IP69, McMaster-Carr 7310K33 (maker not stated). The gland plate's PE and supply entry gl-pe (pm-motor-starter BOM; connections.csv section 'ground').

## Documents on file
- `references/dimensional-drawing.pdf`: McMaster 2-D drawing 7310K33, one page (p. 1), text layer: 1.5 in, 0.4 in, 1.09 in, 25 mm, 1.17 in, 27 mm, M20 x 1.5 mm; 'For Knockout Trade Size: M20; For Cord OD: 0.24 in to 0.51 in'.
- `references/source.txt`: product-page specification (nylon, locknut and O-ring included, gray, UL / C-UL / CE / VDE).
- `model.step`: McMaster STEP (inch), 5 solids.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| dome nut, largest diameter | 29.72 (1.17 in) | 2-D drawing p. 1 |
| hex flats | 25 and 27 (which part takes which: not in the text layer; see Corrections) | 2-D drawing p. 1 |
| overall length | 38.1 (1.5 in) | 2-D drawing p. 1 |
| body length | 27.7 (1.09 in) | 2-D drawing p. 1 |
| thread length | 10.2 (0.4 in) | 2-D drawing p. 1 |
| thread | M20 x 1.5 | 2-D drawing p. 1 |
| cord range | 6.1 to 13 | page (0.24 to 0.51 in) |

## STEP read-back (Open CASCADE)
- model.step: 5 solids, 177 faces, extents 29.7 x 29.7 x 37.0 mm (declared inch); datasheet check 29.72 vs 29.7 (0.02) twice, 38.1 vs 37.0 (1.1: the model's dome nut sits 1.1 mm further down than the drawing's overall, within tolerance).
- Solids: dome nut 27.6 across flats x 15.9 long; body hex 27.6 x 15.5; a 23.0 x 13.9 inner (the seal / clamp insert); the locknut 29.7 across corners x 6.0; the M20 thread spigot 17.5 dia x 10.5.
- AutoCAD 2026 import VERIFIED, extents match.

## Corrections (2026-11-05, mech-r8, unattended; review gland-m20-1.1 findings 2 and 5)
- Hex sizes: the text layer lists 25 mm and 27 mm with no part named. This brief's own read-back above gives the dome nut and the
  body hex 27.6 across flats each, and the locknut 29.7 across corners (≈ 25.7 AF). So 1.2 builds 27 AF for the body and dome
  nut, 25 AF for the locknut. The earlier table line ("body / locknut 25 and 27") had them the other way and is withdrawn. An
  attended look at p. 1 confirms or changes this (gland-m20 spec.md carries it as an open figure until then).
- Tolerances: the figures above are as printed (inch, two decimals except 1.5 and 0.4 at one). The drawing's title-block
  tolerance was not read into this brief, and an unattended run does not open the drawing; an attended session adds it.
  "38.1 vs 37.0 within tolerance" (read-back line) names no tolerance: read it as "1.1 mm apart".

## Mounting
Through a Ø20.5 class knockout in the gland plate (M20 trade size, drawing p. 1; the diameter itself is not on the drawing: Ø20.5 is a choice inside lib/standards/holes.csv:27, M20 x 1.5 entry 20.2 to 20.7, manufacturer practice), locknut inside, O-ring under the body hex; the gland plate of enc-fs is 2 mm galvanised (enc spec).

## Build notes (own model)
- (corrected 2026-11-05, mech-r8, review gland-m20-1.1 finding 1) Thread spigot Ø20 x 10.2 from the seat face (plain cylinder); body hex and dome nut 27 AF with the corners turned to Ø29.72, 27.7 above the seat face; locknut 25 AF x 6.0 inside the plate; overall 27.7 + 10.2 = 37.9, the drawing's 38.1 (1.5 in to one decimal). The earlier line here put 38.1 above the plate face and the thread below it, counting the thread twice.
- The cord is a `cordset`-style sweep through the gland, not part of this element.
- Datum: the knockout centre on the gland plate's outer face.

## Origin
Cut-out centre class: knockout centre on the gland plate's outer face y = 0 (the plate lies in the enclosure floor, so the element's -y is downward when placed), dome nut toward -y, locknut toward +y inside.

## Named nodes
- None (the dome nut turns at installation only; no runtime state).

## Ports
- A cable pass-through, not a connector: the twin treats `self` as kind port, unit 'cable' for connections.csv (gl-pe row).

## Decals
- None (grey nylon; thread size moulded, not reproduced).

## Status
Figures VERIFIED (3 of 3 within 2 mm, one at 1.1); hex flats 25 / 27 read from the drawing; licence McMaster REVIEW. Stage 0 COMPLETE 2026-11-03.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
