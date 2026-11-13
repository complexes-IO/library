# bench-1800 · v1.3 · steel workbench with back-board

**What** steel workbench with back-board. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** furniture · **Baseline** reference workbench: maker's 2-D drawing p. 1 (top 1828.8 × 762.0, 850.9 high, 12 ga, apron 38.1, holes Ø9.5 at 663.6) and STEP read-back (feet 1872.5 overall, leg, rail and stretcher sections). The maker, product and drawing are named only in references/. Back-board: our own design. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: floor machine: floor plane z = 0; x = 0 at the outer edge of the flared left foot; y = 0 on the front anchor-hole line, 49.2 behind the front edge; front toward −y. The origin point is 1.0's; only its description is corrected (1.0 named the front-left foot hole, which lies at x = 71.8). Moving it to the README's front-left base corner (y = −49.2) is a major: lib/requests/mech/2.md.
**Built with** toolkit 1.3 · AutoLISP command `BENCH` · `backboard` (true).

## Dimensions
| item | value | source |
|---|---|---|
| top | 1828.8 × 762.0, sheet 2.67 (12 ga), x 21.8 to 1850.6 | 2-D drawing p. 1 (measure.md:13, :15) |
| worktop height above the floor | 850.9 to the top face; the element's overall height is 1250.9 with the back-board | 2-D drawing p. 1 (measure.md:14); back-board below |
| apron | 38.1 deep including the sheet: four aprons 2.67 thick under the sheet | 2-D drawing p. 1 (measure.md:16) |
| feet | 1872.4 overall: foot plates reach 21.8 outside the top each side | STEP read-back (measure.md:19, :22) |
| anchor holes | 4 × Ø9.5 through the foot plates; y 0 and 663.6 | 2-D drawing p. 1 (measure.md:18) |
| anchor holes, x | 71.8 and 1800.6 (pitch 1728.8, 50 inside the top's ends) | open figure, below |
| foot plates | 171.8 × 762.0 × 8, each reaching 20 past its legs | open figure, below |
| legs | 60 × 60 solid, against the long aprons, from the foot plate to the sheet's underside (848.23); faces 20 inboard of the anchor-hole axes | open figure, below |
| side rails | 23.7 × 82.6 section (measure.md:23), 636.7 long between the legs, top at z 180 | read-back section; length and height in open figures, below |
| stretcher | 120.7 × 19.1 section (measure.md:23), 1652.5 long, on the side rails at mid-depth, z 180 to 199.1 | read-back section; length and height in open figures, below |
| back-board | 1828.8 × 400 × 2.0 along the rear edge, on the top | design choice (OPERATING.md 12), not a ruling; 2.0, not 14 ga |
| PE stud | Ø8 × 12 at x 61.8, z 200, axis −y, on a 40 × 30 × 2.0 tab welded to the rear-left leg | open figure, below |

## Named nodes
`backboard` (fixed: the field devices mount on its front face y = 710.8 in this frame) · `pe` (kind port, unit PE, gender none: the bonding stud; its port face at y 670.8, the axis clear to the front and to the left end)

## Decals (Blender)
none. The institute's tag on the apron comes as a placed tag-plate in a later version (1.0's spec named one; none was built).

## Open figures
Each is a figure no document on file gives; a document figure replaces it as a minor version (or a major where it moves a cut-out).
- **Assumption (A)**: PE stud Ø8 × 12. mc-motor-1 bonds the panel's PE to it, so its size and the conductor it takes decide a
  protective bonding point: EM's. The reviewer names IEC 60204-1 8.2 and 5.2; that standard is not in lib/standards/sources.csv.
- **Assumption (B)**: the anchor holes' x positions (pitch 1728.8). The drawing gives only the 663.6 spacing; the second spacing is
  not on its text layer (measure.md:18). Kept as 1.0 so the cut-outs stay where they were.
- **Assumption (B)**: legs 60 × 60 solid. The read-back gives channel legs 120.8 × 125.3 (measure.md:23), but not their wall, which way
  they open, or where the anchor holes sit relative to them. The legs stand 20 inboard of the hole axes so an anchor and its washer
  pass (review finding 2), and run up to the sheet so the frame holds together (finding 3).
- **Assumption (B)**: the flare's form. The read-back gives 1872.5 overall (the legs 21.8 outside the top each side); how the real legs
  flare is not on file, so the foot plates reach out 21.8 and the legs stand upright. Foot plate 8 thick and 20 past the legs.
- **Assumption (B)**: side rails upright (82.6 high) between the legs, 636.7 long (read-back 752.5), and the stretcher 1652.5 long
  between the rails' outer faces (read-back 1822.5): the read-back gives the sections, our narrower leg stance sets the lengths.
- **Assumption (B)**: the stretcher at z 180, the rails under it. The brief has no height for it (measure.md:30); 180 is 1.0's.
- **NOT ON FILE (B)**: the anchor holes' position tolerance; the drawing marks its figures "for reference only" and no value is
  assumed (features.csv:2 leaves position_tol empty).
- **Assumption (B)**: the stud's position (x 61.8, z 200, axis −y, as 1.0). It is the `pe` port, where mc-motor-1's bonding
  conductor lands (connections.csv), so the twin reads it: a fit, class B (OPERATING.md 6; review mech-r12 finding 1).
- **Assumption (C)**: the stud's tab (40 × 30 × 2.0 off the rear-left leg), a housing part the twin does not read.
- **NOT ON FILE (B)**: what the drawing's 32 in (812.8) dimensions (measure.md:17); the build no longer uses it.

## Outputs (out/)
`bench-1800.lsp` · `.glb` (pivots on the named nodes, `-colonly` colliders) · `preview-*.png`. out/preview-plain.png is 1.0's stale preview; its removal needs `git rm` (lib/needs-em/mech.md).

## History
| version | change |
|---|---|
| 1.0 | first build from the Stage 0 brief, toolkit 1.2; rebuilt under toolkit 1.3 with no change to the part |
| 1.1 | the reviewer's 1.0 findings (lib/reviews/elements/bench-1800-1.0.md): flare built, origin described as built (finding 1; the move is request mech-2); legs off the anchor holes, stud on a tab with its axis clear (2); legs up to the sheet, side rails and the stretcher joined to them, read-back sections (3); open figures marked with class and reason, the brief's open figures carried here (4); back-board a design choice, 2.0 (5); maker and part number out of spec, code and baseline (7); Dimensions table, Decals, history, unused imports (8); `pe` gender none (PIN-002). Nodes, origin and the four anchor holes as 1.0, so a minor (mc-motor-1 pins 1.0) |
| 1.2 | the brief's row measure.md:14 named for what it is, "worktop height above the floor" (lib/requests/core/mech-2-answer.md, "Not in the request"): the 850.9 is the product's worktop, the element is the product plus our back-board (1250.9 overall), so the AutoCAD gate's figure check no longer reads it as the envelope. The part, nodes, origin and cut-outs unchanged: a minor |
| 1.3 | review mech-r12 finding 1 (lib/reviews/mech/r12.md): the stud's position, the `pe` port the twin reads, reclassed from C to B (its tab stays C); the anchor holes' position tolerance relabelled an open figure not on file, class B (no value is assumed). Text only: the part, nodes, origin and cut-outs unchanged, a minor (mc-motor-1 pins 1.0; mech-r24, unattended) |

## Deliberate differences
<!-- acad-gate bench-1800 -->
