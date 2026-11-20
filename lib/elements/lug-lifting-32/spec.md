# lug-lifting-32 · v1.0 · lifting lug (pad eye), generic, weld-on, painted steel plate 120 x 20 x 120 with its top corners cut, eye Ø32

**What** A lifting lug of the weld-on form (a pad eye): one painted steel plate 120 wide, 20 thick and 120 high stands on its foot,
which is welded to a host's flat steel surface (a frame, a machine bed, a lifting beam); its two top corners are cut off from 60 up the
sides to a top 60 wide, and a Ø32 eye through the plate takes a shackle's pin or a hook. A host places it on its own top face, as many as
its lifting points need, turned about z so the eye's axis lies where the sling pulls from. The weld is not drawn and its size is not
stated: it is the host's.
**Class** plate · **Baseline** our own design: generic lifting lug (ETIM 10.0 EC012274 Lifting lug), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: group EG010320 Lifting equipment is walked by name from lib/toolkit/generic.py's
mech order (lib/rounds/mech/r171.md, r172.md), and EC012274 is a class not yet built. Its weld-on form no dimensional standard on file
fixes; the class's other forms, an eye bolt or eye nut (shaped by DIN 580 / DIN 582, not on file), are not this element. No product was
matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the foot's middle on the host's surface: x = 0 the plate's middle across its width, y = 0 its
mid-thickness, z = 0 the foot's underside (the host's surface). The plate's faces y = ±10; the eye's axis along y. Extents x -60 to 60,
y -10 to 10, z 0 to 120.
**Built with** toolkit 1.3 · AutoLISP command `LUGLF32` · no parameter · places and reads no element.

## Class values (ETIM 10.0 EC012274)
Design inputs. EC012274 Lifting lug (lib/standards/etim/classes.csv: group EG010320 Lifting equipment, tier 2, 11 features, synonyms
Lashing eye, Lifting eye) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory.
Until they are on file this table gives the values the lug is designed to under plain names, as clamp-girder-200 1.0 does (requests
mech-8 and mech-9, the core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the
design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| form | weld-on plate (pad eye) |
| material | steel, painted (the `M-YELLOW` layer); the grade not stated |
| fixing | welded along its foot to a host's flat steel surface; the weld's size not stated |
| eye | Ø32, its centre 80 over the foot |
| plate | 120 wide, 20 thick, 120 high |
| load capacity (working load limit) | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load, proof load or mass figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the host's surface | flat steel, the foot's 120 x 20 face on it (z 0) | design: any host; the weld that joins them is the host's and is not drawn |
| a shackle's pin or a hook | through the Ø32 eye | design: no shackle or hook element is on file, so none is read; no load is claimed |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| plate | 120 wide (x -60 to 60), 20 thick (y -10 to 10), 120 high (z 0 to 120) | a foot 120 long for the weld, the eye well clear of it |
| corner cuts | from (±60, 60) up to (±30, 120), each face 67.1 long | the top narrows round the eye, and a sling running over it finds no square corner |
| top | 60 wide (x -30 to 30) | 14 of plate each side of the eye |
| eye | Ø32 along y at (0, 80) | 24 of plate over it, 28.7 to each cut face, 44 to each side, 64 under it to the foot (asserted in element.py) |

## Mechanism
None: one fixed plate. behaviour.csv is the header only (no terminal, no moving node).

## Named nodes
None. Collider (box): `plate` (the plate's outline, 120 x 20 x 120).

## Materials by layer
`M-YELLOW` the plate (painted steel, clamp-girder-200's colour; no marking claim).

## Decals (Blender)
No label: `M-YELLOW` is not a printed layer of the Blender gate (its default printed layers are `M-WHITE-PA` and `M-BLACK-PA`; review
mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one box less two oblique cuts (the corners) and one hole (the eye). Volume by hand
(asserted in element.py): the plate 120 × 20 × 120, less two corner triangles 30 × 60 / 2 × 20, less the eye Ø32 × 20: 235915.0 mm³.
Every bounding-box extreme lies on an uncut face: x ±60 the sides under the cuts (z 0 to 60), y ±10 the plate's faces, z 0 the foot, z
120 the top. No mass is stated: lib/materials.csv gives no density. Not drawn: the weld, a shackle, the host.

## Outputs (out/)
`lug-lifting-32.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012274), our own design (mech-r172, unattended, 2026-11-13): weld-on lifting lug, painted steel plate 120 × 20 × 120 with its top corners cut to a top 60 wide, eye Ø32 at 80 over the foot |
