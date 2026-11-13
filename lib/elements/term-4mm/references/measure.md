# term-4mm · measure brief

Element `term-4mm`: screw-clamp feed-through DIN-rail terminal block, TE Connectivity (Entrelec) 1SNA115116R0700 via McMaster-Carr 7641K21, 6 mm pitch, 22-10 AWG (4 mm2 class), 1000 V / 32 A; with the green/yellow ground block 1SNA165488R2700 (McMaster 7641K931), 5 mm pitch. Control rail: the terminal strip at the rail's right end (field wiring in, 24 V distribution).

## Documents on file
- `references/dimensional-drawing.pdf`: McMaster 2-D drawing 7641K21, one page (p. 1), text layer: 6 mm, 44.5 mm, 47 mm, rail 32 / 35 mm.
- `references/ground-7641K931-drawing.pdf`: McMaster 2-D drawing 7641K931, one page (p. 1), text layer: 5 mm, 43.5 mm, 44.5 mm, rail 32 / 35 mm.
- `references/ground-7641K931.step`: the ground block's STEP (validated as a reference file).
- `references/source.txt`: page specification tables; end stop 7641K35, end cover 7641K31 and bar jumper 7641K15 listed, not downloaded (no figures on file for them).
- `model.step`: McMaster STEP of the feed-through block.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| feed-through block pitch (width on the rail) | 6.0 | 2-D drawing 7641K21 |
| feed-through block height above the rail datum | 44.5 | 2-D drawing 7641K21 |
| feed-through block length (depth across the rail) | 47.0 | 2-D drawing 7641K21 |
| ground block pitch | 5.0 | 2-D drawing 7641K931 |
| ground block height | 43.5 | 2-D drawing 7641K931 |
| ground block length | 44.5 | 2-D drawing 7641K931 |
| rail | 35 mm top-hat, EN 60715 TH 35-7.5 | page: 'for DIN 1 (32 mm), DIN 3 (35 mm) rail'; mounting map section 1 |

## STEP read-back (Open CASCADE)
- model.step: 6 solids, 868 faces, extents 7.975 x 46.95 x 44.65 mm (unit mm); datasheet check 6.0 vs 7.975 (the model's width includes the rail latch / foot, 2 mm over, within tolerance), 44.5 vs 44.65, 47.0 vs 46.95.
- Solids: body 8.0 x 47.0 x 44.7; two clamp cages 5.1 x 10.4 x 7.5 at the two terminals; two screw heads 4.0 x 8.9 x 4.0; one 5.2 x 1.7 x 23.4 bar (the current bar between the clamps).
- ground-7641K931.step: 12 solids, extents 6.4 x 43.5 x 47.0 (body 6.4 x 43.5 x 43.0 plus a 4.8 x 43.5 x 47.0 foot, clamp parts 4.5 x 8.5 x 13.3).
- AutoCAD 2026 import VERIFIED for model.step, extents match.

## Mounting
Snap on 35 mm rail (page); blocks stack at the pitch (6.0 feed-through, 5.0 ground), closed by an end stop and end cover (not on file). Mounting map: 'fits the 35 mm rail: yes (per McMaster)'.

## Build notes (own model)
- Own block: 6.0 x 44.5 x 47.0 envelope per the drawing, two clamp pockets with screws at the top, rail foot cut for TH 35-7.5; the model's 8.0 width is the latch and must not be used as the pitch, otherwise a 20-block strip grows by 40 mm.
- Ground block the same at 5.0 x 43.5 x 44.5, green/yellow.
- Strip length = n x 6.0 + m x 5.0 + end stop + end cover; the last two have no figure on file (NOT ON FILE: add the McMaster pages for 7641K35 / 7641K31 if the strip length matters).
- Datum: rail centreline, block face flush with the rail front.

## Origin
Rail device: back face on the rail contact plane y = 0, rail centreline z = 0, left face of the block x = 0 (blocks stack along +x at the pitch). Convention: lib/README.md states mm, Z up, right-handed; the two released specs give the examples (floor machine: floor plane, front-left anchor hole; panel device pbs-6h-22: back face, lower-left mounting hole; operators: panel face y = 0 at the cut-out centre). A DIN-rail device has no mounting hole, so the origin proposed here is the rail class of 'panel device': back face on the rail contact plane (y = 0), rail centreline z = 0, left edge of the module x = 0. Not yet written in the README; EM to confirm before Stage 1. (Since: EM's README Conventions of 2026-11-03 carry the rail device's origin, as measure-ground.md's Origin cites, and every DIN-rail element on file uses it; this line is history, said in 1.6, review term-4mm-1.3 finding 6.)

## Named nodes
- None: the clamp screws turn but the twin does not read them (no state). No lamp, nothing pressed. (Stale since 1.1, said in 1.6, review term-4mm-1.3 finding 6: the clamps are placed clamp-screw elements, nodes `clamp-1` / `clamp-2` and their `screw` nodes; spec.md Named nodes holds the current list.)

## Ports
None (screw clamps, 22-10 AWG; the field wiring lands here).

## Decals
- Marker tags on the top face (terminal numbers from the milestone-1 architecture); tag carrier figure NOT ON FILE (TE marker strip not downloaded).
- Ground block: green/yellow body, no print.

## Status
Figures VERIFIED (3 of 3 within 2 mm, width on the tolerance line because of the latch); end stop / cover figures NOT ON FILE; licence McMaster REVIEW (TE datasheet not on file).

---
2026-11-03, extended the same day to Stage 0 of lib/element-qa-checklist.txt (EM's file of 2026-11-03): identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the library convention, named nodes (kind and range), ports, decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
