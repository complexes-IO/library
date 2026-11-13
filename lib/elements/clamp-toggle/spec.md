# clamp-toggle · v1.0 · toggle clamp, generic, vertical hold-down, 2.5 kN, flanged base 4 × M5, spindle hole M8

**What** A vertical hold-down toggle clamp: screwed down beside a fixture, it presses a workpiece down with a spindle at the end of
its arm, and its handle swings the arm clear to load the next part. A flanged base with four M5 holes, a two-plate frame, and
one lever (the arm with its handle) on a pivot through the frame. The lever is the mechanism: the twin opens and closes the
clamp by name.
**Class** device · **Baseline** our own design: generic machine toggle clamp (ETIM 10.0 EC003935), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No product was matched and no vendor file was opened. The class values below are the design inputs;
the holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face (the base's underside) at z = 0, the centre of the base's four-hole pattern
at x = 0, y = 0. Clamped, the arm reaches toward +x and the handle stands up (+z); opening swings the arm up and the handle back
toward −x.
**Built with** toolkit 1.3 · AutoLISP command `TOGCLAMP` · no parameters.

## Class values
ETIM 10.0 class EC003935 Machine toggle clamp (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Clamping spread (EF006203) | not stated: the spindle sets it, and the spindle (a screw) is placed in a later version |
| 2 | Clamping height (EF005936) | 26 mm: the arm's underside at the spindle axis, clamped, above the mounting face; the spindle reaches below it to the work |
| 3 | Max. clamping force (EF021596) | 2.5 kN at the spindle, clamped: the force the closed clamp is designed to hold |
| 4 | Clamp- and release automatic (EF015038) | no: operated by hand |
| 5 | Total length (EF000369) | 94 mm clamped: the base's rear edge to the arm's tip |
| 6 | Total height (EF001761) | 102 mm clamped: the mounting face to the top of the grip |
| 7 | Overhang length (EF000303) | 30 mm clamped: the arm's tip beyond the base's front edge (the spindle axis 18 beyond it) |
| 8 | Type of profile rail (EF006796) | not stated: it is screwed down through its base, on no profile rail |

## What it meets
| figure | value | source |
|---|---|---|
| base screws | 4 × M5, Ø5.5 holes at 48 × 28 (x ±24, y ±14) | ISO 273 medium (H13), lib/standards/holes.csv. The screws are not built; the host places them |
| spindle | M8, a Ø9.0 hole through the arm, 50 from the pivot | ISO 273 medium (H13), lib/standards/holes.csv. The spindle (a hex-head screw with a pressure cap) and its two lock nuts are standard parts, never generic (OPERATING.md 12): the hole is cut, and they are placed in a later version once the screw and nut elements are built |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four base holes carry a declared position tolerance Ø0.4 at MMC to A (the mounting face), B (the base's rear edge) and C (its
left edge) (features.csv; H − F = 5.5 − 5 = 0.5). The ISO 2768-m general tolerance of their 55.6 mm diagonal (±0.3, a Ø0.85
zone) would not hold the pattern. The spindle hole is one hole, not a pattern (Ø9.0 for M8: H − F = 1.0).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | 64 × 44 × 3, flanged, zinc-plated steel | the hole centres stand 12 beyond the frame plates' ends (x ±24 against ±12), room for the screw heads |
| frame | two plates 24 × 35 × 3 on the base, x −12 to 12, inner faces at y ±8.5 | 0.5 clear of the 16-wide arm each side |
| pivot | a Ø6 journal along y at x 0, z 30, through both plates, riveted heads Ø10 × 1.5 outside | the arm's hub turns on it in a Ø6.2 bore (features.csv) |
| arm | hub Ø14 × 16; bar 57 × 16 × 8 from inside the hub to x 62, its centre line level with the pivot | the spindle hole at x 50 leaves 7.5 to the tip and 3.5 each side |
| handle | bar 8 × 10 up to z 100; grip Ø14 × 40 from z 62 to 102 | the grip clear above the frame plates (z 38) |
| opening | 95° | the arm just past vertical, so the open clamp stays open |

## Mechanism
`arm` (rotate about the pivot (0, 0, 30), axis −y, 0 to 95°): 0 is clamped, as built (arm level, handle up); 95 is open (arm
just past vertical, handle back toward −x). The node carries the hub, the arm bar, the handle and the grip. MOT-010 sweeps it
through the full range: the hub, arm and handle pass between the frame plates, and the lever's lowest point (the grip's edge, at
95°) stays 13.75 above the base's top face (z 16.75).
In this model the handle and the arm are one lever on one pivot, so the twin opens the clamp by one angle. A real toggle clamp
couples them through a link and a second pivot that lock it over centre; that linkage is not drawn in 1.0. Drawing it needs the
twin to move two nodes together (a lib/motion.csv row, the core's), so it is a question for a later version, not a figure.

## Named nodes
`arm` (rotate). Colliders `body` (the base), `frame` (the plates and pivot), `arm` (hub and bar), `handle` (handle and grip).

## Materials by layer
`M-ZINC` base, frame, pivot, arm and handle bar (zinc-plated steel) · `M-RED-PA` grip.

## Decals (Blender)
"complexes.org generic" on the +y frame plate's outer face, below the pivot.

## Notes
No vendor names, part numbers or marks. No safety claim. The class values are the figures this design is meant to meet; no
calculation or test of the model is on file. No open figure: both holes are on file, and the spindle, its nuts and the base
screws are standard parts placed later.

## Outputs (out/)
`clamp-toggle.lsp` · `.glb` (pivot on `arm`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003935), our own design (cloud-mech, 2026-11-07); stations 1 to 5; the gates (AutoCAD, Blender, Godot) run on the PC in the lane's next round |
