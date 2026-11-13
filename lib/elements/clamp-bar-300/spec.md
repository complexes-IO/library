# clamp-bar-300 · v1.1 · bar clamp, generic, chucking range 1 to 300, overhang 90, bar 25 × 10 × 380, sliding arm with screw, pad Ø24 and wooden handle

**What** A bar clamp: the F-style screw clamp a fitter or joiner sets across work to hold it while glue sets, or while it is drilled
or welded. A steel bar with a fixed cast arm at its end; a sliding cast arm runs along the bar and carries the screw spindle, its
pressure pad and its wooden handle. The work is held between the fixed arm's clamping face and the pad. The sliding arm is the
mechanism: the twin opens and closes the clamp by name. The first element of ETIM's "Glue clamp" class in the library (its synonyms
name the bar clamp and the screw clamp; `python lib/build.py inventory mech` lists the class to build generic once no inventory row
builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic glue clamp (ETIM 10.0 EC002200), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its thirteen features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was
matched and no vendor file was opened. The class values below are the design inputs; it meets no fixed interface; every size is a
design choice.
**Units / frame** mm, Z up. Origin: the fixed arm's clamping face at x = 0, the bar's underside at z = 0, the clamp's centre plane
at y = 0. The bar runs along +x above the origin; both arms hang down to z −110; the screw's axis at z −90. The sliding arm opens
toward +x. Extents x −20 to 380, y −13 to 13, z −110 to 35.
**Built with** toolkit 1.3 · AutoLISP command `CLAMPBAR` · no parameters.

## Class values
ETIM 10.0 class EC002200 Glue clamp (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Chucking range (EF002391) | 1 to 300 mm: the pad's face from the fixed arm's clamping face, 1 at rest + 299 of travel |
| 2 | Jaw length (EF005953) | 110 mm: the arms' clamping faces below the bar, z −110 to 0 |
| 3 | Jaw width (EF005637) | 26 mm: the fixed arm across y (the pad Ø24 opposite it) |
| 4 | Total length (EF000369) | 400 mm: the whole clamp at rest, x −20 to 380 (the fixed arm 20 and the bar 380), the element's own extents (1.1: 1.0 gave the bar's 380) |
| 5 | Overhang length (EF000303) | 90 mm: the screw's axis below the bar's underside (the reach from the bar to the clamping point) |
| 6 | Max. angle (EF025752) | not stated: the pad is drawn fixed on its spindle (it does not swivel in this design) |
| 7 | One hand control (EF006517) | no: the arm is slid and the handle turned |
| 8 | Type of clamping mechanism (EF015119) | screw spindle through the sliding arm |
| 9 | Fixator (EF001827) | no |
| 10 | With antislip facility (EF025068) | no: plain pad and jaw faces |
| 11 | Material jaws (EF015118) | cast iron arms, steel pad |
| 12 | Material handle (EF006500) | wood |
| 13 | Weight (EF000167) | not stated (lib/materials.csv gives no densities) |

No clamping force is designed or claimed (the class states none, and the spindle's thread and the handle's torque are not drawn or
rated).

## What it meets
| figure | value | source |
|---|---|---|
| the work | held between the fixed arm's face (x = 0) and the pad, 1 to 300 apart, at 90 below the bar | design: the chucking range and the reach are this design's (OPERATING.md 12, an own size) |
| the bench or the work's support | none: the clamp is a loose tool, no fixing hole | design: a hand tool that rests on the work it holds (OPERATING.md 12) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| bar | 25 × 10 (y ±5, z 0 to 25), x 0 to 380, steel | its −x end face on the fixed arm's +x face; open, it still runs 15 beyond the sliding arm |
| fixed arm | 20 × 26 × 145 (x −20 to 0, y ±13, z −110 to 35), cast iron | its +x face below the bar is the fixed jaw; its x / y / z extremes are the element's (an uncut box) |
| sliding arm | 25 × 22 × 145 (x 41 to 66 at rest, y ±11, z −110 to 35), cast iron, with a channel 12 × 27 right through it along x (y ±6, z −1 to 26) | runs on the bar 1 clear on every side; the channel's side walls 5, its roof 9 |
| pressure pad | Ø24 × 10 on the screw's axis, x 1 to 11 at rest | its face 1 from the fixed jaw when closed, so the solids never touch |
| spindle | Ø12, x 11 to 41 at rest (the 30 showing between the pad and the arm) | the thread inside the sliding arm is not drawn |
| handle | Ø24 × 80 behind the sliding arm (x 66 to 146 at rest), wood | a bar clamp's handle is on its screw and travels with the sliding arm |
| layers | arms `M-CAST-BLUE`; bar, pad and spindle `M-SILVER` (bright steel); handle `M-BROWN` | a design choice, no finish claim |

## Mechanism
`jaw` (translate along +x, 0 to 299, pivot (1, 0, −90) on the pad's face): 0 is closed, as built (the pad 1 from the fixed jaw); 299
is open (300 apart). The node carries the sliding arm, the pad, the spindle and the handle. MOT-010 sweeps it through the full range:
the bar runs in the sliding arm's channel (1 clear on every side), and nothing else is in its path.
Not drawn (internal mechanism the twin doesn't read): the sliding arm's lock on the bar (a real one tilts and grips), the screw's own
stroke through the arm and the handle's turning; the node's travel stands for the whole chucking range. A workpiece between the jaws
sets the real stop in an assembly.

## Named nodes
`jaw` (translate). Colliders `fixed-arm`, `bar` (axis-aligned boxes).

## Materials by layer
`M-CAST-BLUE` fixed arm, sliding arm · `M-SILVER` bar, pad, spindle · `M-BROWN` handle.

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default
M-WHITE-PA, M-BLACK-PA); this part's layers are M-CAST-BLUE, M-SILVER and M-BROWN, so no tool on file carries the "complexes.org
generic" label 1.0 named (review mech-r126 finding 2; needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force claim. The class values are the figures this design is
meant to meet; no calculation or test of the model is on file. No open figure: it meets no interface a standard fixes. The gate's
fillet rule (r 0.5 for a device): every box edge is 10 or longer; the channel's edges are cut edges, skipped. Every bounding-box
extreme is on an uncut box (the fixed arm, the bar). Not drawn: the screw's thread, a swivel pad, the bar's end stop, serrations.
Hand volume: fixed arm 75 400, bar 95 000, sliding arm 79 750 − 8 100 = 71 650, pad 4 523.9, spindle 3 392.9, handle 36 191.2;
286 158.0 mm³ in all. lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`clamp-bar-300.lsp` · `.glb` (pivot on `jaw`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002200), our own design (mech-r126, unattended, 2026-11-12): a bar 25 × 10 × 380 with a fixed arm, a sliding arm carrying the screw, pad and handle, chucking range 1 to 300, overhang 90 |
| 1.1 | text only (review mech-r126 findings 3 and 2): class value Total length 400, the whole clamp (x −20 to 380, the element's extents), not the bar's 380; Decals "No label" (no printed layer). The part unchanged; a minor (mech-r143, unattended, 2026-11-13) |
