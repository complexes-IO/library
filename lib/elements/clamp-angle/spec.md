# clamp-angle · v2.0 · angle clamp, generic, 90 degree corner, two screw pads, clamping spread 30, jaws 100 × 40, base 120 × 120

**What** An angle clamp: the corner clamp that holds two workpieces at a right angle while a frame's corner is glued, screwed or
welded. A cast base carries two fences at 90 degrees (the fixed jaws) and two spindle posts. Each workpiece lies on the base against
its fence; a steel pad on a hand-turned screw spindle presses it onto the fence. The two pads are the mechanism: the twin opens and
closes each by name. The first element of ETIM's "Angle clamp" class in the library (`python lib/build.py inventory mech` lists the
class to build generic once no inventory row builds unattended: the first class of group EG020054 Clamping tools whose shape no
dimensional standard fixes, lib/needs-em/mech.md); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic angle clamp (ETIM 10.0 EC002144, whose synonyms name the corner clamp and
the mitre clamp), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). The class and its eight features are on file
(lib/standards/etim/classes.csv, class-features.csv). No product was matched and no vendor file was opened. The class values below
are the design inputs; every size is a design choice.
**Units / frame** mm, Z up. Origin: the base's underside (z = 0) at the jaws' inside corner. Fence a's clamping face is the plane
y = 0 (its workpiece runs along +x), fence b's the plane x = 0 (its workpiece runs along +y). Pad a opens toward +y, pad b toward
+x. Extents x −20 to 100, y −20 to 100, z 0 to 50.
**Built with** toolkit 1.3 · AutoLISP command `CLAMPANG` · no parameters.

## Class values
ETIM 10.0 class EC002144 Angle clamp (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Clamping spread (EF006203) | 30 mm: each pad's face 30 from its fence at the end of its travel (1 at rest + 29 of travel), both pads at once (2.0) |
| 2 | Jaw length (EF005953) | 100 mm: each fence's clamping face from the inside corner (fence a x 0 to 100, fence b y 0 to 100) |
| 3 | Jaw width (EF005637) | 40 mm: each fence's clamping face, z 10 to 50 |
| 4 | Overhang length (EF000303) | not stated |
| 5 | Angle (EF005434) | 90° |
| 6 | Type of clamping mechanism (EF015119) | screw spindle, one per jaw, turned by a T-handle |
| 7 | Material jaws (EF015118) | fences cast iron (with the base); pads steel |
| 8 | Material handle (EF006500) | steel |

No clamping force is designed or claimed (the class states none, and the spindles, their thread and the handles' torque are not
rated).

## What it meets
| figure | value | source |
|---|---|---|
| the workpieces | two, each up to 30 thick, both at once (each pad is clear of the other pad's whole stroke), on the base's top face (z 10) against its fence, meeting at the inside corner | design: a loose bench tool (OPERATING.md 12, an own size); the workpieces and the joint are the host's |
| the bench or welding table | the base's underside, z = 0, 120 × 120 | design: used loose on a flat bench, no fixing hole (OPERATING.md 12) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | 120 × 120 × 10 (x and y −20 to 100, z 0 to 10), cast iron (`M-CAST-BLUE`) | carries both fences and both posts as one body; the workpieces lie on its top face |
| fences | 20 thick, 40 high on the base: a x −20 to 100, y −20 to 0; b x −20 to 0, y 0 to 100 (z 10 to 50) | their faces the two jaws at 90 degrees; they meet behind the corner, so the corner itself is open for the joint |
| posts | 36 × 15 × 40 on the base: a x 42 to 78, y 70 to 85; b x 70 to 85, y 42 to 78 (z 10 to 50), each with a Ø14 bore for its spindle | 2 clear of the other pad's whole stroke (it reaches 40 from its fence), 4 clear of the other spindle (66) and 2 short of the handles |
| pads | steel (`M-SILVER`), 36 × 10 × 30, z 11 to 41 (1 above the base, so they never rub it): a x 42 to 78, y 1 to 11 at rest; b x 1 to 11, y 42 to 78 at rest | each presses its workpiece onto its fence over 36 of its length, 42 to 78 from the corner; each pad's whole stroke (1 to 40 from its fence) stops 2 short of the other pad (42), so both may be open at once (2.0, review mech-r124 finding 1: 1.0's pads at 32 to 68 met once both passed 21) |
| spindles | Ø12, steel, drawn plain: a along y at x 60, z 20, from pad a's back to y 95; b along x at y 60, z 34, from pad b's back to x 95 | the two cross in plan at (60, 60), 2 apart in z, so neither pad's sweep meets the other spindle (each pad's back stops at 40, 14 short of the other spindle) |
| T-handles | Ø10 × 50, steel, at 92 from the fence: a along x (x 35 to 85), b along y (y 35 to 85) | 2 behind the posts at rest; the two handles 2 apart in plan |

## Mechanism
`pad-a` (translate along +y, 0 to 29, pivot (60, 1, 20) on pad a's clamping face) and `pad-b` (translate along +x, 0 to 29, pivot
(1, 60, 34) on pad b's): 0 is closed, as built (each pad 1 off its fence, so the solids never touch); 29 is open (30 between pad
and fence). Each node carries its pad, its spindle and its T-handle; the spindle runs through its post's Ø14 bore (1 clear) over
the whole travel. MOT-010 sweeps each node through its full range with the other at rest: the pads move over the base without
touching it, and each pad's back stops 14 short of the other spindle. The two nodes are independent (two manual toggles in
behaviour.csv), so every pair of their positions is reachable; element.py asserts what MOT-010 alone does not pose: each pad's
whole stroke (1 to 40 from its fence) ends 2 short of the other pad and of the other post (42), and the spindles cross 2 apart in
z, the handles 4 apart, so with both pads at any setting no two parts meet (by hand at both ends: pad a x 42 to 78, y 30 to 40;
pad b x 30 to 40, y 42 to 78; 2 apart in x and in y).
The spindles' thread and their nuts in the posts are not drawn (internal mechanism the twin doesn't read); a spindle swivel pad
is drawn as a fixed block on its spindle. A workpiece between pad and fence sets the real stop in the assembly.

## Named nodes
`pad-a`, `pad-b` (translate). Colliders `base`, `fence-a`, `fence-b`, `post-a`, `post-b` (axis-aligned boxes, named apart from the
nodes).

## Materials by layer
`M-CAST-BLUE` base, fences, posts · `M-SILVER` pads, spindles, handles.

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default
M-WHITE-PA, M-BLACK-PA); this part's layers are M-CAST-BLUE and M-SILVER, so no tool on file carries the "complexes.org generic"
label 1.0 named (review mech-r125 finding 2; needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. No safety claim, no clamping force, no accuracy (squareness) claim. The class values are the
figures this design is meant to meet; no calculation or test of the model is on file. No open figure: nothing it meets is a
standard's figure, and it is used loose. The gate's fillet rule (r 0.5 for a device): every box edge is 10 or longer (base 10
thick, pads 10 thick, posts 15); the bores' edges are cut edges, skipped. Every bounding-box extreme lies on an uncut axis-aligned
box face: the base's x −20 / 100, y −20 / 100 and z 0, the fences' and posts' top z 50. Not drawn: the spindles' thread, the
swivel joint between spindle and pad, the nuts in the posts. lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`clamp-angle.lsp` · `.glb` (pivots on `pad-a`, `pad-b`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002144), our own design (mech-r124, unattended, 2026-11-12): a cast base with two fences at 90 degrees, two screw pads with a clamping spread of 30 |
| 2.0 | review mech-r124 finding 1 (ESCAPE, MOT-010): 1.0's two pads met once both were opened past 21. The pads, spindles and posts move out to 42 to 78 from the corner (spindles on 60), so each pad's whole stroke ends 2 short of the other pad and post; T-handles 70 → 50 long; new asserts for pad against pad and post against pad; Decals "No label" (review mech-r125 finding 2). A major (OPERATING.md 7: the nodes' pivots and the bores move); nothing places clamp-angle. Extents, nodes and class values unchanged (mech-r143, unattended, 2026-11-13) |
