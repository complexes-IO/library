# jack-screw · v1.1 · screw jack, generic, base Ø50, bearing face 80 to 110, wrench width 24, plug-in peg Ø10

**What** A screw jack: the workpiece support a machinist sets under an overhanging part on a machine table, then winds up until its
bearing face meets the part, so the clamping or the cut doesn't bend it. A round cast base standing loose on the table, and one
moving node: the screw, its collar with two spanner flats (the collar's top is the bearing face) and a plug-in peg on top that takes
a pad or a prism head. The moving screw is the mechanism: the twin sets the jack's height by name. The first element of ETIM's "Bolt
block" class in the library (`python lib/build.py inventory mech` lists the class to build generic once no inventory row builds
unattended: group EG020054 Clamping tools, lib/needs-em/mech.md); no inventory row or system names it yet. vise-machine, clamp-toggle
and claw-clamping hold a part down; this one holds it up.
**Class** device · **Baseline** our own design: generic bolt block (ETIM 10.0 EC003406), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its five features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; every size is a design choice.
**Units / frame** mm, Z up. Origin: the base's underside (its seat on the machine table) at z = 0, on the screw's axis (x = y = 0).
The screw winds up along +z. The bearing face at z = 80 at rest, 110 at the end of the travel. Extents x −25 to 25, y −25 to 25 (the
base), z 0 to 92 at rest (the peg's top).
**Built with** toolkit 1.3 · AutoLISP command `JACKSCRW` · no parameters.

## Class values
ETIM 10.0 class EC003406 Bolt block (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Outer diameter (EF000015) | 50 mm: the base |
| 2 | Height (EF005454) | 80 to 110 mm: the bearing face above the table, from the screw wound down (0) to the end of its travel (30) |
| 3 | Wrench width (EF000177) | 24 mm: the two flats across the collar (y ±12) |
| 4 | Load bearing capacity (EF002918) | not stated |
| 5 | Diameter of plug-in peg (EF011326) | 10 mm: the peg on the bearing face, 12 high |

No load bearing capacity is designed or claimed: the screw's thread, the base's nut thread and their engagement are not drawn or rated.

## What it meets
| figure | value | source |
|---|---|---|
| the machine table | the base's underside, z = 0, Ø50; loose, no fixing hole | design: a loose support set by hand under the work (OPERATING.md 12, an own size); the table is the host's (bed-cast, table-slotted are such tables) |
| the work | the bearing face Ø30 less its flats, z 80 to 110 | design: wound up by hand to meet the work (OPERATING.md 12, an own size) |
| a pad or a prism head | the plug-in peg Ø10 × 12 on the bearing face | design: the peg's diameter is this design's class value (OPERATING.md 12); no head is on file, so none is placed |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | Ø50 × 55 (z 0 to 55), a bore Ø18 from z 6 up through its top | a wide foot for a 30 high travel; the bore 1 clear of the screw each side and 2 under its foot, so the drawn solids never touch |
| screw | Ø16, z 8 to 57 at rest, drawn plain | at the top of the travel 17 of it is still in the base; its thread and the base's nut thread are internal mechanism, not drawn |
| collar | Ø30 × 24 (z 56 to 80 at rest), two flats 24 apart across y | 1 above the base at rest, rising away from it; the flats take an open-ended spanner |
| plug-in peg | Ø10 × 12 on the bearing face (z 80 to 92 at rest) | takes a pad or a prism head |
| layers | base `M-CAST-BLUE`; screw, collar and peg `M-SILVER` (bright steel) | a design choice, no finish claim |

## Mechanism
`screw` (translate along +z, 0 to 30, pivot (0, 0, 80) on the bearing face): 0 is wound down, as built (the bearing face at 80); 30 is
the end of the travel (the bearing face at 110). The node carries the screw, the collar and the peg. MOT-010 sweeps it through the full
range: the screw rises in the base's bore (1 clear each side) and the collar rises away from the base's top, so nothing is in its path.
The thread that turns the screw's rotation into its rise is not drawn (internal mechanism the twin doesn't read); the model shows the
rise only. The work set on the bearing face sets the real stop in the assembly.

## Named nodes
`screw` (translate). Collider `base` (an axis-aligned box round the base).

## Materials by layer
`M-CAST-BLUE` base · `M-SILVER` screw, collar, peg.

## Decals (Blender)
No label. The Blender gate makes a decal island only on its printed layers (toolkit/blender/gate.py `--printed`, default
M-WHITE-PA, M-BLACK-PA); this part's layers are M-CAST-BLUE and M-SILVER, so no tool on file carries the "complexes.org generic"
label 1.0 named (review mech-r125 finding 2; needs-em 218 asks the core for the rule).

## Notes
No vendor names, part numbers or marks. No safety claim, no load claim. The class values are the figures this design is meant to meet;
no calculation or test of the model is on file. No open figure. The gate's fillet rule (r 0.5 for a device): every edge is a circle
of Ø10 or more, or a cut edge (the bore, the flats), skipped. Every bounding-box extreme is on an uncut solid (the base's x / y and z 0,
the peg's top). Not drawn: the thread, a locking nut, a swivel or prism head, knurling. Hand volume: the base 95 523.3 mm³ (Ø50 × 55
less the Ø18 bore 49 deep). lib/materials.csv gives no densities, so no mass is stated.

## Outputs (out/)
`jack-screw.lsp` · `.glb` (pivot on `screw`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003406), our own design (mech-r125, unattended, 2026-11-12): a round base, a screw with a flatted collar and a plug-in peg, the bearing face 80 to 110 |
| 1.1 | text only (review mech-r125 finding 2): Decals "No label" (no printed layer). The part unchanged; a minor (mech-r144, unattended, 2026-11-13) |
