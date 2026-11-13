# damping-rod · v1.1 · damping rod, generic, straight rubber-metal rail, 110 × 200 × 55, rubber block 46 × 190 × 30, 4 × M10 base holes, 2 × M10 tapped

**What** A damping rod: a straight rubber-metal rail, the rail-shaped machine mount that carries a machine, a frame, a pump or
compressor skid or a cabinet on rubber, so the floor or the frame under it takes less of its vibration. A steel base flat with four
M10 bolt holes carries a rubber block bonded on its top; a steel top flat bonded on the rubber takes the machine's foot through two
M10 tapped holes. A vertical load works the rubber in compression, a side load (across or along the rail) in shear. It is the
straight sibling of damping-rod-angle (ETIM EC003741, the slanting rail) and the first element of ETIM's "Damping rod" class in the
library (`python lib/build.py inventory mech` lists the class as the next mech class to build generic once no inventory row builds
unattended; EC012003 Ball joint and EC011971 Cardan joint above it wait for their dimensional standards: lib/needs-em/mech.md); no
inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic damping rod (ETIM 10.0 EC003749), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). The class and its four features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was matched
and no vendor file was opened. The class values below are the design inputs; the base holes are ISO 273's; the tapped holes' thread
is derived (What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face (the base flat's underside, z = 0) at the rail's centre. y runs along the rail,
x across it. Extents x −55 to 55 (the base flat), y −100 to 100 (the base and top flats), z 0 to 55 (the top flat's top face, where
the machine's foot seats).
**Built with** toolkit 1.3 · AutoLISP command `DAMPROD` · no parameters.

## Class values
ETIM 10.0 class EC003749 Damping rod (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's order
(lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Width (EF000008) | 110 mm: the base flat across the rail (x); the top flat 50, the rubber block 46 |
| 2 | Height (EF000040) | 55 mm: the mounting face to the top flat's top face, unloaded (base 10, rubber 30, top 15) |
| 3 | Length (EF001438) | 200 mm: along the rail (y); the rubber block 190 |
| 4 | Rubber quality (EF014147) | NR (natural rubber), bonded to both steel flats |

The class has no stiffness, load, deflection or hardness feature, so none is designed to or claimed: the mount carries what its
host's design gives it, and the twin draws it unloaded.

## What it meets
| figure | value | source |
|---|---|---|
| the floor or frame it bolts to | 4 × Ø11 through the base flat at x ±42, y ±70 | M10 clearance, ISO 273 medium H13 (lib/standards/holes.csv); the spacing is this design's choice. Position Ø0.5 at MMC ≤ H − F = 1.0 to A the mounting face, B the plane x 0, C the plane y 0 (ASME Y14.5 floating fastener, features.csv); the bolts and the host's holes are the host's |
| the machine's foot | 2 × M10 tapped holes, 12 deep, in the top flat's top face at x 0, y ±60 | the thread, derived: M10 × 1.5 coarse, internal tolerance class 6H: minor Ø D1 8.3762 to 8.6817, pitch Ø D2 9.0257 to 9.2016 (basic: H 1.299, tap drill 8.5); derived: derive.thread(10.0, 1.5) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6H; ISO 261 pitch). Drawn as plain bores at D1 8.3762 (features.csv kind `own`); the thread form is not drawn. The foot's screws and their length are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base flat | 110 × 200 × 10, steel, zinc-plated (`M-ZINC`) | carries the rubber and the four bolt holes beside it; 7.5 of steel outside each hole; design: a hexagon head up to Ø18 at x ±42 clears the top flat's side (25) by 8 (a design allowance; screw-head standards not on file) |
| rubber block | 46 × 190 × 30, bonded to both flats | the damping element; 2 inside the top flat's sides and 5 short of each end, so no rubber face lies in a steel face's plane |
| top flat | 50 × 200 × 15, steel, zinc-plated | takes the machine's foot; the tapped holes end 3 over the rubber |
| tapped holes | 2 × M10, 12 deep, y ±60 | blind, in the top flat's full thickness |
| load, stiffness, deflection, natural frequency, damping, hardness, temperature range | not claimed | no feature of this class states one; no calculation or test is on file |

## Mechanism
None: one fixed body, no moving node, no port. The rubber and the top flat are drawn unloaded; with no stiffness or load figure in
the class or on file, a loaded pose (the top flat sunk on the rubber) has no figure to come from, so none is drawn. behaviour.csv is
the header only.

## Named nodes
None. Colliders, axis-aligned boxes: `body` (the base flat and the rubber, x ±55, y ±100, z 0 to 40) and `top` (x ±25, y ±100, z 40
to 55).

## Materials by layer
`M-ZINC` the base and top flats (steel, zinc-plated) · `M-GASKET` the rubber block (black).

## Decals (Blender)
No label. The Blender gate puts a decal island only on its printed layers (toolkit/blender/gate.py `--printed`: M-WHITE-PA,
M-BLACK-PA), and this part's layers are M-ZINC and M-GASKET, so no tool on file carries one.

## Notes
No vendor names, part numbers or marks. No load, stiffness, deflection or safety claim. The drawn volume is about 364 876 mm³ of
steel (base 220 000 less four holes 3 801.3; top 150 000 less two tapped holes 1 322.5) and 262 200 mm³ of rubber (46 × 190 × 30);
written as volume only: lib/materials.csv gives no densities, so no mass is stated. A mesh's polygonal bores remove less than their
circles, so a mesh's steel volume reads a little high. Not drawn: the bolts, the foot's screws, a stop that limits the top flat's
travel (a later variant if a host needs one). A damping rod is not a part a dimensional standard shapes, so it is built generic to
its ETIM class (OPERATING.md 12). The gate's fillet rule (r 0.5 for a device): every free-corner edge is 10 or longer (the base's 10,
110 and 200; the rubber's 30, 46 and 190; the top flat's 15, 50 and 200); the holes' edges are cut edges, skipped. Every bounding-box
extreme lies on an uncut axis-aligned box face: the base's x ±55, y ±100 and z 0, the top flat's top face z 55.

## Outputs (out/)
`damping-rod.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003749), our own design (mech-r120, unattended, 2026-11-12): base flat with four M10 holes, a rubber block 46 × 190 × 30, a top flat with two M10 tapped holes |
| 1.1 | text only, the part unchanged (mech-r142, unattended, 2026-11-13; review mech-r120 findings 2 and 3): Decals now "No label" (no printed layer carries the decal the 1.0 spec named); the bolt-head clearance written as a design allowance (a hexagon head up to Ø18), no longer cited from ISO 4017, which is not on file |
