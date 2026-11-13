# damping-rod-angle · v1.1 · angle damping rod, generic, rubber-metal slanting rail, 140 × 160 × 80, 90-degree V, 4 × M10 base holes, 2 × M10 tapped

**What** An angle damping rod: a rubber-metal slanting rail, the rail-shaped machine mount that carries a machine, a frame, a
compressor skid or a cabinet on rubber, so the floor or the frame under it takes less of its vibration. A steel base with four M10
bolt holes carries a holder with a 90-degree V-groove along the rail; two rubber layers lie on the groove's two faces, and a steel
wedge rests on them, its ridge down in the groove. The machine's foot is screwed to the wedge's top face through two M10 tapped
holes. A vertical load presses the wedge into the V, so each rubber layer works in compression and in shear at once (that is what
the slanting form is for); a side load across the rail meets one layer face-on. It is the first element of ETIM's
"Angle damping rod" class in the library (`python lib/build.py inventory mech` lists the class as the next mech class to build
generic once no inventory row builds unattended); no inventory row or system names it yet.
**Class** device · **Baseline** our own design: generic angle damping rod (ETIM 10.0 EC003741), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07). The class and its five features are on file (lib/standards/etim/classes.csv, class-features.csv). No product was
matched and no vendor file was opened. The class values below are the design inputs; the base holes are ISO 273's; the tapped
holes' thread is derived (What it meets); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face (the base's underside, z = 0) at the rail's centre. y runs along the rail (the
groove's line), x across it. Extents x −70 to 70 (the base), y −80 to 80 (the base, the holder and the wedge), z 0 to 80 (the
wedge's top face, where the machine's foot seats).
**Built with** toolkit 1.3 · AutoLISP command `DAMPRODANG` · no parameters.

## Class values
ETIM 10.0 class EC003741 Angle damping rod (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md; classes.csv describes it
as "Rubber-metal slanting rail"), every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element
is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Total width (EF022578) | 140 mm: the base across the rail (x); the holder 84, the wedge 64 |
| 2 | Total height (EF001761) | 80 mm: the mounting face to the wedge's top face, unloaded |
| 3 | Length (EF001438) | 160 mm: along the rail (y); the rubber layers 150 |
| 4 | Rubber quality (EF014147) | NR (natural rubber), bonded to the steel |
| 5 | Shore hardness (EF022944) | 55 Shore A |

The class has no stiffness, load or deflection feature, so none is designed to or claimed: the mount carries what its host's
design gives it, and the twin draws it unloaded.

## What it meets
| figure | value | source |
|---|---|---|
| the floor or frame it bolts to | 4 × Ø11 through the base at x ±56, y ±60 | M10 clearance, ISO 273 medium H13 (lib/standards/holes.csv); the spacing is this design's choice. Position Ø0.5 at MMC ≤ H − F = 1.0 to A the mounting face, B the plane x 0, C the plane y 0 (ASME Y14.5 floating fastener, features.csv); the bolts and the host's holes are the host's |
| the machine's foot | 2 × M10 tapped holes, 15 deep, in the wedge's top face at x 0, y ±45 | the thread, derived: M10 × 1.5 coarse, internal tolerance class 6H: minor Ø D1 8.3762 to 8.6817, pitch Ø D2 9.0257 to 9.2016 (basic: H 1.299, tap drill 8.5); derived: derive.thread(10.0, 1.5) (ISO 68-1 basic profile; ISO 965-1 clause 10 formulas, 6H; ISO 261 pitch). Drawn as plain bores at D1 8.3762 (features.csv kind `own`); the thread form is not drawn. The foot's screws and their length are the host's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base | 140 × 160 × 10, steel, zinc-plated (`M-ZINC`) | carries the holder and the four bolt holes; each hole 8.5 from the base's edge and 8.5 from the holder's side |
| holder | 84 × 160, from the base to z 50, 0.5 into the base (one solid) | the V-groove's body: 8 of steel under the groove's bottom line (z 18 against the base's top 10) and a 10 lip each side of the groove's mouth |
| V-groove | 90 degrees (each face 45 degrees to the floor), its bottom line at z 18, 64 wide at the holder's top | the slanting form: a vertical load shares out into compression and shear of the layers |
| rubber layers | two, 10 thick, 150 along the rail (y ±75, 5 short of each steel end), each from 12 up its face (along the slope) to the groove's mouth, 33.25 along the slope | bonded on the groove's faces and under the wedge's; they stop short of the bottom line, so the two never meet |
| wedge | 64 × 160, a 90-degree ridge down at z 32.14 (each face 10 off its groove face, so 14.14 higher at any x), top face at z 80 | rests on the two layers only; its lower corners (x ±32, z 64.14) stand 14.14 over the holder's lips, so it never touches the holder |
| tapped holes | 2 × M10, 15 deep, y ±45 | in the wedge's full width (they end at z 65, over the corners at 64.14) |
| load, stiffness, deflection, natural frequency, damping, temperature range | not claimed | no feature of this class states one; no calculation or test is on file |

## Mechanism
None: one fixed body, no moving node, no port. The wedge and the rubber are drawn unloaded; with no stiffness or load figure in the
class or on file, a loaded pose (the wedge sunk into the V) has no figure to come from, so none is drawn. behaviour.csv is the
header only.

## Named nodes
None. Colliders, axis-aligned boxes: `body` (the base and the holder, x ±70, y ±80, z 0 to 50) and `wedge` (x ±32, y ±80, z 32.14
to 80).

## Materials by layer
`M-ZINC` the base, the holder and the wedge (steel, zinc-plated) · `M-GASKET` the rubber layers (black).

## Decals (Blender)
No label. The Blender gate puts a decal island only on its printed layers (toolkit/blender/gate.py `--printed`: M-WHITE-PA,
M-BLACK-PA), and this part's layers are M-ZINC and M-GASKET, so no tool on file carries one.

## Notes
No vendor names, part numbers or marks. No load, stiffness, deflection or safety claim. The drawn volume is about 918 530 mm³ of
steel (base 224 000 less four holes 3 801; holder 84 × 160 × 40 = 537 600 less the groove 1 024 × 160 = 163 840; wedge (64 × 47.858
− 1 024) × 160 = 326 227 less two tapped holes 1 653) and 99 765 mm³ of rubber (2 × 33.255 × 150 × 10); written as volume only:
lib/materials.csv gives no densities, so no mass is stated. A mesh's polygonal bores remove less than their circles, so a mesh's
steel volume reads a little high. Not drawn: the bolts, the foot's screws, a stop that limits the wedge's travel (a later variant if
a host needs one). An angle damping rod is not a part a dimensional standard shapes, so it is built generic to its ETIM class
(OPERATING.md 12). The gate's fillet rule (r 0.5 for a device): every free-corner edge is 10 or longer (the base's 10, 140 and 160;
the holder's 40 and the lips' 10; the wedge's 15.86 and 64; the rubber's 10, 33.25 and 150); the groove's, the wedge's lower faces'
and the holes' edges are cut edges, skipped. Every bounding-box extreme lies on an axis-aligned box face: the base's x ±70, y ±80 and
z 0, the wedge's top face z 80 (the cuts leave it whole); the rubber's tilted boxes lie inside.

## Outputs (out/)
`damping-rod-angle.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003741), our own design (mech-r117, unattended, 2026-11-12): base with four M10 holes, a 90-degree V holder, two rubber layers, a wedge with two M10 tapped holes |
| 1.1 | text only, the part unchanged (mech-r142, unattended, 2026-11-13; review mech-r120 finding 2, which names this element's same line): Decals now "No label" (no printed layer carries the decal the 1.0 spec named) |
