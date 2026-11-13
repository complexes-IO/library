# holder-workpiece · v1.1 · workpiece holder, generic, helping hand, two swivelling arms with clips on a cross bar, cast base 150 × 100, height 190

**What** A workpiece holder: the bench "helping hand" that holds a small part, a board or two wires in its clips while both of the
worker's hands solder, glue or inspect it. A cast base stands on the bench; a steel post rises from it to a head block, and a cross
bar is pressed through the head. At each end of the bar an arm (nodes `arm-left`, `arm-right`): a swivel boss that turns round the
bar, a rod and a plastic clip block. Each arm swings down about the bar to bring its clip to the work. The twin sets each arm by
name. The first element of ETIM's "Workpiece holder" class in the library (`python lib/build.py inventory mech` lists the class to
build generic once no inventory row builds unattended: group EG020054 Clamping tools, lib/needs-em/mech.md); no inventory row or
system names it yet.
**Class** device · **Baseline** our own design: generic workpiece holder (ETIM 10.0 EC004363), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its five features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; every size is a design choice.
**Units / frame** mm, Z up. Origin: on the base's underside (z = 0, the face that stands on the bench), at its centre. The post at
x = −50, y = 0; the cross bar's axis is the line x = −50, z = 180 along y; the arms point toward +x. Extents x −75 to 80 (the base's
back to the clips' tips), y −100 to 100 (the cross bar's ends), z 0 to 190 (the head block's top).
**Built with** toolkit 1.3 · AutoLISP command `HOLDWP` · no parameters.

## Class values
ETIM 10.0 class EC004363 Workpiece holder (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | With magnifier (EF014714) | no |
| 2 | With lighting (EF003829) | no |
| 3 | Width (EF000008) | 200 mm: the cross bar's length (y −100 to 100) |
| 4 | Height (EF000040) | 190 mm: the base's underside to the head block's top |
| 5 | Length (EF001438) | 155 mm: the base's back (x −75) to the clips' tips (x 80), the arms level |

No holding force is designed or claimed (the class states none, and the clips' springs are not drawn or rated).

## What it meets
| figure | value | source |
|---|---|---|
| the work | held in the clips, x 60 to 80 at z 172 to 188 with the arms level, down to z 63.4 (the clip's far lower corner) with them turned 60 degrees | design: a bench tool's reach (OPERATING.md 12, an own size); nothing is placed in it |
| the bench | the base's underside z = 0, 150 × 100 | design: a bench tool standing on a worktop (OPERATING.md 12, an own size); nothing is placed under it |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base (fixed) | 150 × 100 × 20 (x ±75, y ±50, z 0 to 20), cast | the weight that keeps the holder standing; the extents' back |
| post (fixed) | Ø12, z 20 to 170, at x −50, y 0 | carries the head toward the base's back, so the arms reach over the bench in front |
| head block (fixed) | 20 × 20 × 20 (x −60 to −40, y ±10, z 170 to 190), bored Ø8 along y on the bar's axis | the cross bar is pressed in it (features.csv, kind own); the extents' top |
| cross bar (fixed) | Ø8 × 200 (y ±100), axis z 180 | the arms' bearing; its ends 2 proud of the bosses |
| swivel bosses (nodes) | 16 × 14 × 16 (x −58 to −42, y ±84 to ±98, z 172 to 188), each bored Ø10 | 1 clear round the bar (features.csv, kind own), so each arm turns free |
| rods (nodes) | Ø6, x −42 to 60, at y ±91, z 180 | carry the clips 110 in front of the bar |
| clip blocks (nodes) | 20 × 10 × 16 (x 60 to 80, y ±86 to ±96, z 172 to 188) | the clip's body; its jaws and spring not drawn |
| travel | 60 degrees down, each arm on its own | the clip block then spans z 63.4 to 88.7 and x −1.9 to 21.9: its far lower corner (130, −8 from the bar's axis) at z 180 − (130 · sin 60° + 8 · cos 60°) = 63.4, 43.4 above the base's top (element.py `Z_LOW`, asserted); 49.8 is only the bound element.py also asserts, that corner straight below the bar (86.5 degrees), which the arm never reaches; the arms hang outside the base's sides (y ±84 and beyond, the base ±50), so they never meet it |
| layers | base `M-CAST-BLUE` (painted cast iron); post, bar, rods `M-SILVER` (bright steel); head, bosses `M-ZINC` (zinc-plated steel); clips `M-BLACK-PA` (plastic) | a design choice, no finish claim |

## Mechanism
`arm-left` (y −98 to −84) and `arm-right` (y 84 to 98), each a rotate about axis (0, 1, 0), 0 to 60 degrees, pivot (−50, 0, 180) on
the cross bar's axis: 0 is level, as built (the rods along +x); 60 turns the clip down toward the bench. Each node carries its swivel
boss, its rod and its clip block. MOT-010 sweeps each arm through its full range with the other at rest: the boss turns round the bar
(1 clear), its corners (radius 11.3) stay inside its own y band, which holds no fixed solid but the bar; the rod and clip stay outside
the base's sides and above z 63.4 (at 60 degrees, the range's end). The arms are 168 apart, so they never meet.
Not drawn (internal mechanism the twin doesn't read): the friction that holds an arm where it is set, the clips' jaws and springs, a
ball joint on the clip.

## Named nodes
`arm-left`, `arm-right` (rotate). Collider `base` (an axis-aligned box).

## Materials by layer
`M-CAST-BLUE` base · `M-SILVER` post, cross bar, rods · `M-ZINC` head block, swivel bosses · `M-BLACK-PA` clip blocks.

## Decals (Blender)
"complexes.org generic" on the two clip blocks (`M-BLACK-PA`), the only printed layer of the part (toolkit/blender/gate.py `--printed`,
default M-WHITE-PA, M-BLACK-PA), where the Blender gate places its decal islands; the base (`M-CAST-BLUE`) is not printed (review
holder-workpiece-1.0 note 2, mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. No safety claim, no holding force. The class values are the figures this design is meant to
meet; no calculation or test of the model is on file. No open figure. The gate's fillet rule (r 0.5 for a device): the base is 20
thick and every block 10 or more on every edge; the bores' edges are cut edges. Not drawn: the clips' jaws, a magnifier, a lamp.
lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`holder-workpiece.lsp` · `.glb` (pivots on `arm-left`, `arm-right`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004363), our own design (mech-r129, unattended, 2026-11-12): a helping hand, two arms with clips each turning 60 degrees about the cross bar |
| 1.1 | text only, the part unchanged (mech-r145, unattended, 2026-11-13): review mech-r129 finding 1, the clips at 60 degrees reach down to z 63.4 (43.4 above the base's top; element.py `Z_LOW`, asserted), not 49.8, which is the bound for the corner straight below the bar; note 2, the Decals line names the clip blocks, the part's printed layer |
