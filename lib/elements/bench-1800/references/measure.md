# bench-1800 · measure brief

Element `bench-1800`: steel workbench, 72 x 30 in top (1828.8 x 762.0), 33-1/2 in (850.9) high, 12 ga powder-coated steel top, 14 ga frame, four 3/8 in floor mounting holes, McMaster-Carr 9054T14 (maker not stated); the back-board is our own addition (McMaster lists a backstop 9054T54, not on disk). The machine's bench bench-1 (mc-motor-1 BOM, planned) carrying the motor, the station and the I/O block.

## Documents on file
- `references/dimensional-drawing.pdf`: McMaster 2-D drawing 9054T14, one page (p. 1), text layer: 32 in, 1.5 in, 72 in, 30 in, 33.5 in, 0.105 in, 26.125 in, '4X 0.375 in Mounting Hole Diameter'; 'Frame Material Gauge: 14, Table Top Material Gauge: 12'.
- `references/source.txt`: product-page specification (72 x 30 in, 33-1/2 in high, 1,800 lb, knockouts for duplex outlets, unassembled; options backstop / end stop 9054T54, upper shelf 9054T64, drawer 9054T18).
- `model.step`: McMaster STEP (inch), 68 solids.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| top W x D | 1828.8 x 762.0 (72 x 30 in) | 2-D drawing p. 1; page |
| worktop height above the floor | 850.9 (33.5 in) | 2-D drawing p. 1; page |
| top sheet | 2.67 (0.105 in, 12 ga) | 2-D drawing p. 1 |
| top lip / apron | 38.1 (1.5 in) | 2-D drawing p. 1 |
| leg stance (inside?) | 812.8 (32 in) | 2-D drawing p. 1 (the figure's reference edges are not captioned: assigned at Stage 1 against the STEP) |
| mounting holes | 4 x Ø9.5 (0.375 in) at 663.6 (26.125 in) spacing | 2-D drawing p. 1 (the second spacing is not on the text layer: NOT ON FILE) |
| overall width with the flared legs | 1872.5 | STEP read-back (the legs stand 21.8 outside the top each side) |

## STEP read-back (Open CASCADE)
- model.step: 68 solids, 3946 faces, extents 1872.456 x 850.9 x 762.0 mm (declared inch); datasheet check 762.0 exact, 850.9 exact; 1828.8 (top) vs 1872.5 overall explained by the flared legs.
- Largest solids: the top 1830.9 x 762.0 x 38.6 (sheet plus the 1.5 in lip); four legs 120.8 wide x 811.5 tall x 125.3 (channel legs, one 116.8); a lower stretcher 1822.5 x 120.7 x 19.1; two side rails 82.6 x 23.7 x 752.5; the rest are gussets, feet plates and fasteners.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
Floor: four 3/8 in holes in the foot plates (drawing p. 1), anchors per the lab floor; the bench is the machine's base, so the motor, station and I/O block mount on its top and the back-board.

## Build notes (own model)
- Top 1828.8 x 762.0 with a 38.1 apron, 2.67 sheet; four channel legs 120.8 x 125.3 section, 811.5 tall (850.9 less the top), flared so the feet stand 1872.5 overall; lower stretcher 1822.5 x 120.7 x 19.1 at the drawing's height (NOT ON FILE on the text layer: from the STEP); foot plates with Ø9.5 holes at 663.6 across.
- Back-board (own): a vertical panel along the rear edge of the top for the station pbs-1 and the I/O block io-1; height and thickness are ours (EM to rule; proposal 400 high x 2 thick, 14 ga), not a McMaster figure.
- Knockouts for duplex outlets on the apron (page) as decals only.
- Datum: the floor plane and the front-left foot hole (as written 2026-11-03; the build's origin is as "Origin" below says).

## Origin
Floor machine class (README Conventions): floor plane z = 0, front-left anchor hole x = 0, y = 0, top toward +z, front edge toward -y.
Correction (mech-r12, review bench-1800-1.0 finding 1): 1.0 and 1.1 put x = 0 at the outer edge of the flared left foot and y = 0 on
the front anchor-hole line (the front-left hole is at x = 71.8). The README's front-left base corner is a major: request mech-2.

## Named nodes
- None that moves (a fixed bench); `node:pe` = the frame bonding point for connections.csv (panel-1.gl-pe -> machine-1.bench-1.pe), kind port, unit PE.

## Ports
- `pe` only (ground section); the duplex knockouts are not modelled as ports.

## Decals
- None on the vendor part; the institute's tag plate (tag-plate kind=device) on the apron, position ours.

## Status
Figures VERIFIED (2 of 2 exact; top width explained); the drawing's 32 in and the second hole spacing need assigning at Stage 1; back-board figures are ours (NOT ON FILE); licence McMaster REVIEW. Stage 0 COMPLETE 2026-11-03.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
