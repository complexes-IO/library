# nipple-bulkhead-npt · v1.0 · generic tank feed-through nipple, male NPT at both ends, locknut

**What** a tank feed-through (bulkhead) nipple: a wrench-hex collar outside a tank or panel wall, a straight threaded shank through a
plain hole in the wall, a locknut that clamps the wall against the collar from the inside, and one male NPT stub at each end. It
takes a line through a wall without a tapped boss: the outside stub into the line's female fitting, the inside stub into a dip tube's
or a fitting's female port. Its uses in the lane: a port through a sheet-metal tank or cabinet wall that has no boss (a tank's
added return or level line, an air line through a panel or guard into a cabinet), the inside end then free for a female fitting. The
default build is NPT 1/4 through a 3 mm wall (tank's and hyd-tank's design wall).
**Class** connector · **Baseline** our own design: generic tank feed-through nipple (ETIM 10.0 EC010488, synonyms "Tank adaptor",
"Tank connector", "Tank feed-through"), as OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next ETIM class of EG015540
in pneu's order (generic.next_classes) that the lane can build unattended (pneu-r114; the classes passed over before it are in
lib/rounds/pneu/r114.md section 2). No vendor file was opened or measured. The class values below are its design inputs; its sizes
are design choices; its NPT threads take their series from the pneumatic contract `toolkit/pneu.py` (request pneu-1: D1 NPT threads,
ASME B1.20.1) and the shank's straight thread its size and pitch from lib/standards/un-threads.csv (ASME B1.1, on file). No vendor
names; "generic" in its title.
**Why generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. No standard on file or named in
pneu.py tabulates a tank feed-through nipple: its only standard figures are its threads, and both are on file (NPT by ASME B1.20.1's
formulas in pneu.NPT; the UNF shank in un-threads.csv). The locknut is the fitting's own, sized to its collar: ASME B18.2.2's hex and
jam nuts are not on file and are not used (a nut of that standard for this shank is a later element if a machine needs one). The
collar, the nut and the lengths are design choices, as on nipple-hex-npt.
**Units / frame** mm, Z up. Origin: the collar's wall face (the face that bears on the wall's outside) y = 0 on the axis (x = z = 0);
the wall and the tank's inside toward +y, port-a's host (outside) toward −y, port-b's host (inside) toward +y. Ports follow pneu.py's
port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `NIPPLE-BULKHEAD-NPT` · `thread` (NPT1/4; NPT1/8, NPT1/4, NPT3/8), both ends the same;
`wall` (3.0; 1.0 to 10.0 mm), the wall's thickness, which sets the locknut's place.

## Class values (ETIM 10.0 EC010488)
Design inputs. EC010488 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv does not list its 23
features: the case request pneu-4 raised for tube-pneu, which the core answered (lib/requests/core/pneu-4-answer.md): the element is
built with its design values under plain names (as tube-pneu 1.0, plug-pushin 1.0 and the block fittings). When the features are on
main, a minor version restates this table in ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| model | straight feed-through nipple: hex collar, straight shank with a locknut, male thread at both ends |
| material | brass |
| connection 1 (outside) | male thread, NPT (ASME B1.20.1; pneu.py D1) |
| connection 2 (inside) | male thread, NPT, the same size as connection 1 |
| size of thread connection (inch) | 1/4 (parameter `thread`: 1/8, 1/4, 3/8) |
| wall thread | straight, UNF: 5/8-18 for NPT 1/4 (1/2-20 for NPT 1/8, 3/4-16 for NPT 3/8; un-threads.csv) |
| wall thickness (clamping range) | 1 to 10 mm (parameter `wall`) |
| seal | not drawn: a flat gasket under the collar, the installer's, sized to the wall's hole (NPT ends seal on their taper with sealant, pneu.py D1) |
| max. operating pressure | not stated: no rating claimed, no ratings.csv; a feed-through carries the pressure of the ports it joins, and the wall's own seal decides what the tank holds |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT male stubs | one at each end, a plain cylinder L2 long, 0.5 into the collar or the shank: Ø13.62 × 10.21 for NPT 1/4 (Ø10.24 × 6.70 for NPT 1/8, Ø17.06 × 10.36 for NPT 3/8) | nipple-hex-npt's stub, from pneu.NPT (calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2 = (0.80D + 6.8)P; diameter E1 + h, the external thread's major diameter at the hand-tight plane. The library draws threads as plain cylinders; the taper and thread form are not drawn |
| collar | hex, 8 long (y −8 to 0), 22 AF for NPT 1/4 (19 for NPT 1/8, 27 for NPT 3/8), corners turned to 1.05 × AF | flats at least the shank's major + 6, so the collar bears 3 or more all round a clearance hole in the wall (element.py asserts it); 1.05 × AF keeps the glb's turned corners within the catalogue envelope's rounding (cap-hex-npt r106's Godot check; asserted). 8 long for the AutoCAD gate's fillet pre-flight |
| shank | Ø15.88 (5/8-18 UNF's major D) for NPT 1/4 (Ø12.70, 1/2-20; Ø19.05, 3/4-16), from the collar's wall face to y = 19 | a straight thread, since an NPT taper can't carry a locknut; the UNF size is the smallest of un-threads.csv whose major clears the stub's largest major diameter E2 + h (asserted), so the stub steps down from the shank. Size and pitch read from un-threads.csv (ASME B1.1, FED-STD-H28/2B on file); drawn plain at its major D. 19 = the thickest wall 10 + nut 6 + 3 of thread past the nut |
| locknut | hex, 6 long, the collar's flats and corners, its wall face at y = `wall` | clamps the wall between itself and the collar; the collar's flats, so one wrench size serves both. Part of the fixed body: its place is the `wall` parameter, not a motion |
| wall's hole | not drawn (the host's): a plain clearance hole for the shank | a host that places this element cuts its own hole; the collar's 3 of bearing allows a hole up to the shank's major + 6 less the gasket's own margin |
| flow bore | not drawn | inside the ports once made up; no check or host reads it (nipple-hex-npt's case) |
| overall | 47.41 long for NPT 1/4 (L2 + 8 + 19 + L2; 40.40 for NPT 1/8, 47.72 for NPT 3/8); envelope 23.1 across the collar's turned corners | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT1/4 (parameter `thread`) | male | the collar's outer face y = −8, axis −y; the stub runs L2 along the axis (`length` in the pivot's data) | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a female NPT port of the same size; sealant on this male (D1) |
| `port-b` | NPT1/4 (parameter `thread`) | male | the shank's inner end y = 19, axis +y; the stub as port-a's | as port-a |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, nipple-hex-npt's way): the
feed-through passes on its line's role from the port it joins. a and b are the class's connections 1 (outside) and 2 (inside).

## Open figures
None. Every figure is a class value, a design choice above, a size read from un-threads.csv, or calculated from ASME B1.20.1's
formulas (pneu.NPT).

## Named nodes
`port-a` (stub a), `port-b` (stub b); kind port, fixed (range 0). The collar, the shank and the locknut are the fixed body.

## Materials by layer
`M-BRASS` collar, shank, locknut and both stubs

## Decals (Blender)
None: no face on a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`nipple-bulkhead-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010488), pneu-r114 (unattended): hex collar, UNF shank from un-threads.csv, locknut at parameter `wall`, a male NPT stub at each end from pneu.NPT, two port pivots, parameter `thread`; no ratings (none claimed); gasket, wall hole and flow bore not drawn |
