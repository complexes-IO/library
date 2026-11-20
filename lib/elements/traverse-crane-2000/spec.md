# traverse-crane-2000 · v1.0 · crane hook traverse (lifting beam), generic, 2000 long, painted steel box beam 100 x 200, a placed lifting lug on top for the hook and two under it 1600 apart for the load

**What** A crane hook traverse, the lifting beam form: one painted steel box beam 2000 long, 100 wide and 200 high (wall 8, both ends
closed by plates 10 thick) hangs from a crane's hook by one lug on its top face at the middle, and carries the load from two lugs under
it, 1600 apart, so the load's two slings hang straight down rather than pulling inward. The three lugs are placed lug-lifting-32 1.0
elements (tags `lug-hook`, `lug-load-l`, `lug-load-r`), never redrawn: the top one stands on the beam's top face as that element is
drawn, the two under it are the same part turned 180° about y, so their feet are on the beam's underside and their eyes hang below it.
Each lug's eye lies along y, in the beam's vertical middle plane. The welds are not drawn; their size is not stated.
**Class** furniture · **Baseline** our own design: generic crane hook traverse (ETIM 10.0 EC004250 Crane hook traverse), OPERATING.md
12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010320 Lifting equipment is walked by name from
lib/toolkit/generic.py's mech order (lib/rounds/mech/r171.md, r172.md, r173.md), and EC004250 is a class not yet built. A lifting beam
that places an element on file (lug-lifting-32 1.0, station 6 passed); its shape no dimensional standard on file fixes. The class's other
forms in its synonyms (a C-hook, a forklift attachment, a cross traverse) are not this element. No product was matched and no vendor file
was opened.
**Units / frame** mm, Z up. Origin: the middle of the beam's underside: x = 0 the beam's middle along its length, y = 0 its
mid-width, z = 0 its underside. Extents x -1000 to 1000, y -50 to 50, z -120 (the load lugs' tops, hanging) to 320 (the hook lug's top).
The hook's eye centre (0, 0, 280); the load eyes' centres (±800, 0, -80).
**Built with** toolkit 1.3 · AutoLISP command `TRVCR2K` · no parameter · places lug-lifting-32 1.0 three times (tags `lug-hook`,
`lug-load-l`, `lug-load-r`) and reads its figures (library.load: W, T, H, ZE, VOL).

## Class values (ETIM 10.0 EC004250)
Design inputs. EC004250 Crane hook traverse (lib/standards/etim/classes.csv: group EG010320 Lifting equipment, tier 2, 5 features,
synonyms C-hook, Conveyor system, Crane traverse, Cross (X), Cross (X) traverse, Cross traverse, Forklift attachment) is a class whose
features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are on file this table gives
the values the traverse is designed to under plain names, as lug-lifting-32 1.0 does (requests mech-8 and mech-9, the core's answers); a
later minor version restates them in ETIM's order with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| form | lifting beam: one hook point on top, two load points under it |
| material | steel, painted (the `M-YELLOW` layer); the grade not stated |
| length | 2000 over the end plates |
| beam section | box 100 wide x 200 high, wall 8 |
| hook point | one lug-lifting-32 1.0, eye Ø32 at (0, 0, 280) |
| load points | two lug-lifting-32 1.0, eyes Ø32 at (±800, 0, -80), 1600 apart |
| load capacity (working load limit) | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load, proof load or mass figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the lugs | three lug-lifting-32 1.0, each foot 120 x 20 on a face of the beam: the hook's on the top face (z 200) at x -60 to 60, the load's on the underside (z 0) at x 740 to 860 and -860 to -740, all at y -10 to 10 | lug-lifting-32 1.0 (element.py W, T, H, ZE; asserted: each foot within its face, 130 short of the end plates) |
| a crane's hook | through the hook lug's eye | design: no hook or crane element is on file, so none is read; no load is claimed |
| the load's slings or shackles | through the load lugs' eyes | design: no sling or shackle element is on file; no load is claimed |

## Its own sizes (design choices; the lug's figures read from lug-lifting-32 1.0)
| item | value | why |
|---|---|---|
| beam | 2000 long (x -1000 to 1000), 100 wide (y -50 to 50), 200 high (z 0 to 200), box section wall 8 | a hollow section stiff about the vertical load, 100 wide so each lug's 20-thick foot lies on its face with 40 each side |
| end plates | 10 thick, the box's full section 100 x 200, at x -1000 to -990 and 990 to 1000 | close the box's ends |
| load lugs' span | 1600 (x ±800) | the slings hang 1600 apart; each lug's foot 130 short of the end plate |
| hook lug | at the middle (x 0) | the hook over the middle of the two load points, so the beam hangs level under an even load |

## Mechanism
None: one fixed beam with three welded lugs. behaviour.csv is the header only (no terminal, no moving node).

## Named nodes
None. Colliders (box): `beam` (the beam's outline, 2000 x 100 x 200) and each placed lug's under its tag: `lug-hook-plate`,
`lug-load-l-plate`, `lug-load-r-plate` (renamed from the lug's own `plate`, so no two colliders share a name, as rack-bins-1000 does
with its placed rails; the turned lugs' colliders written back as axis-aligned boxes, the same corners).

## Materials by layer
`M-YELLOW` the beam, its end plates and the placed lugs (painted steel, the lug's layer; no marking claim).

## Decals (Blender)
No label: `M-YELLOW` is not a printed layer of the Blender gate (its default printed layers are `M-WHITE-PA` and `M-BLACK-PA`; review
mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. The beam drawn as one box less one through cutbox (its hollow) and two end-plate boxes; the
lugs placed, each one box less two oblique cuts and one hole. Volume by hand (asserted in element.py): the box section 100 × 200 −
84 × 184 = 4544 mm² over 1980, two end plates 10 × 100 × 200, three lugs at 235915.0 mm³: 10104865 mm³. Every bounding-box extreme lies
on an uncut face: x ±1000 the end plates, y ±50 the beam's sides, z 320 the hook lug's top, z -120 the load lugs' tops (hanging). No
mass is stated: lib/materials.csv gives no density. Not drawn: the welds, a hook, a shackle, a sling, the load.

## Outputs (out/)
`traverse-crane-2000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004250), our own design (mech-r173, unattended, 2026-11-13): a lifting beam, painted steel box beam 2000 × 100 × 200 (wall 8, end plates 10), one placed lug-lifting-32 1.0 on top for the hook and two under it, turned 180° about y, 1600 apart for the load |
