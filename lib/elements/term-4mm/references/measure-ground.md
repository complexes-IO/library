# term-4mm · ground block variant · measure brief

Element `term-4mm`, variant `ground`: TE Connectivity (Entrelec) 1SNA165488R2700 green/yellow screw-clamp ground terminal block, McMaster-Carr 7641K931, 5 mm pitch, 22-12 AWG, 35 mm rail. One element with the feed-through block (`measure.md`): parameter `kind` = feed-through (6.0 pitch, grey) / ground (5.0 pitch, green/yellow, rail-bonded foot). Control rail: the PE blocks of the terminal strip.

## Documents on file
- `references/ground-7641K931-drawing.pdf`: McMaster 2-D drawing 7641K931, one page (p. 1), text layer: 5 mm, 43.5 mm, 44.5 mm, rail 32 / 35 mm.
- `references/ground-7641K931.step`: McMaster STEP of the ground block (validated as a reference file of term-4mm).
- `references/source.txt`: page specification (ground block green/yellow 5 mm wide 22-12 AWG).
- The feed-through documents are in `measure.md`.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| pitch (width on the rail) | 5.0 | 2-D drawing 7641K931 p. 1 |
| height above the rail datum | 43.5 | 2-D drawing 7641K931 p. 1 |
| length (depth across the rail) | 44.5 | 2-D drawing 7641K931 p. 1 |
| rail | 35 mm top-hat (also 32 mm) | 2-D drawing p. 1 |

## STEP read-back (Open CASCADE)
- ground-7641K931.step: 12 solids, 932 faces, extents 7.0 x 43.5 x 46.95 mm (mm); against the drawing: 5.0 vs 7.0 (2.0, the rail latch and the bonding foot stand proud of the 5.0 pitch, on the tolerance line), 43.5 exact, 44.5 vs 46.95 (2.45 OVER: the foot's rail-contact spring reaches 47.0, the body is 43.0).
- Solids: body 6.4 x 43.7 x 43.0; bonding foot 4.8 x 43.5 x 47.0; an inner 4.5 x 37.8 x 26.9 block and a 2.5 x 28.5 x 23.0 plate (the contact bar); two 4.5 x 8.5 x 13.3 clamp cages; two 3.8 x 3.8 x 11.7 screws; a 4.2 x 27.6 x 2.1 bar; smaller spring parts.
- AutoCAD 2026 import: not run for this reference file (the validator records the main model only).

## Mounting
Snap on 35 mm rail; the foot bonds the block to the rail (PE), no wire to the rail needed (McMaster page: ground block). Stacks in the strip at 5.0 pitch between feed-through blocks (measure.md build notes: strip length).

## Build notes (own model)
- Same generator as the feed-through with `kind = ground`: envelope 5.0 x 43.5 x 44.5, green/yellow body (M-GREEN-YELLOW layer to be added to the writer's table), bonding foot modelled as part of the body; the 7.0 read-back width is the latch, never the pitch.
- Two clamp pockets with screws at the top as the feed-through, 22-12 AWG.
- Datum: rail centreline, block face flush with the rail front, as the feed-through.

## Origin
Rail device (README Conventions, EM 2026-11-03): back face on the rail crown y = 0, rail centreline z = 0, left edge x = 0, body toward -y. Shared with the feed-through variant.

## Named nodes
- None (no state); clamp screws fixed. (Stale since 1.1, said in 1.6, review term-4mm-1.3 finding 6: the two clamps are placed clamp-screw elements, nodes `clamp-1` / `clamp-2` with their turning `screw` nodes, as the feed-through's; spec.md Named nodes holds the current list.)

## Ports
None (screw clamps, 22-12 AWG; PE wires land here, the rail is the PE bus).

## Decals
- Green/yellow body colour is the marking; the earth symbol on the top face (position NOT ON FILE); marker tags as the feed-through.

## Status
Figures: 2 of 3 within 2 mm (43.5 exact, pitch on the tolerance line), length MISMATCH explained (rail spring 47.0); licence McMaster REVIEW. Stage 0 COMPLETE 2026-11-03 as the ground variant of term-4mm.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
