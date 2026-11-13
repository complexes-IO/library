# tag-plate · measure brief

Element `tag-plate`: own element (Complexes), legend plates and label carriers: the institute's panel tag plate and the operator legend plates. No vendor file; the envelope comes from the plate sizes already written in the two released specs. Parametric: `w`, `h`, `t`, `text`, `colour` (black plate / white text, or engraved). Carried by `pbs-6h-22` (lid, lower right), `enc-fs-1524x1829x305` (top-left of the right door) and every operator (legend under the cap).

## Documents on file
- `lib/out/pbs-6h-22-spec.md`: dimensions table (p. 1, line 'legend plates'): 30 x 50 x 1 black, text white (decal), one under each operator except the E-stop; decals line: 'IP66 and the institute's tag plate on the lid, lower right'.
- `lib/operators.py`: `LEGEND = dict(w=30.0, h=50.0, t=1.0)`, placed centred under the operator at 0.65 h below the cut-out centre; `ESTOP plate=(60.0, 60.0, 1.5)` (the yellow E-stop plate, a different element).
- `lib/out/enc-fs-1524x1829x305-spec.md`: decals line: 'the institute's panel tag plate top-left of the right door'; rating label inside the right door; no plate size given.
- No references/ documents (own element, nothing downloaded).

## Figures (mm)
| feature | mm | source |
|---|---|---|
| legend plate W x H x T | 30 x 50 x 1 | pbs-6h-22 spec, dimensions table; operators.py LEGEND |
| legend plate offset below the cut-out centre | 0.65 x 50 = 32.5 to the plate centre | operators.py `_legend` (derived) |
| institute tag plate W x H x T | NOT ON FILE | the enclosure and station specs give the position only |
| E-stop plate (for reference, separate element) | 60 x 60 x 1.5 | operators.py ESTOP; pbs spec |

## STEP read-back (Open CASCADE)
- No vendor STEP. The legend plate exists as primitives inside the pbs-6h-22 build (`operators.py`), not as its own file yet.

## Mounting
Legend plate: clamped between the operator bezel and the panel (operators.py: the plate sits on the panel face, the cut-out passes through it). Tag plate: adhesive or two screws on the door / lid (fixing NOT ON FILE; EM to rule).

## Build notes (own model)
- One generator: box w x h x t with a centred Ø22.3 cut-out when `kind = legend` (operators.py CUT) and none when `kind = tag`; corner radius NOT ON FILE (none in the pbs build).
- Default sizes: legend 30 x 50 x 1; tag plate size to be ruled by EM (NOT ON FILE); text as a decal on the front face (M-BLACK-PA plate, white text per the pbs spec).
- Datum: back face on the panel, lower-left corner.

## Origin
Panel device (README Conventions): back face on the panel y = 0, lower-left corner x = 0, z = 0, plate toward -y.

## Named nodes
- None (fixed plate).

## Ports
None.

## Decals
- The plate is the decal: legend text START / STOP / RESET / RUN / FAULT in white on black (pbs spec), the institute's tag text on the tag plate (text NOT ON FILE: EM to give the tag wording and the asset-tag format), 'IP66' on the station lid.

## Status
Legend plate figures VERIFIED from the released pbs spec (30 x 50 x 1); institute tag plate size, fixing and wording NOT ON FILE; own element, no licence. Stage 0 COMPLETE 2026-11-03 for the legend plate; the tag plate waits on EM's sizes.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
