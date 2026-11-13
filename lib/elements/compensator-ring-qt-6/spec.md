# compensator-ring-qt-6 · v2.0 · tolerance compensator ring for a quarter-turn fastener, generic, for a Ø6 stud with a Ø3 × 12 cross pin, zinc-plated steel, Ø40 × Ø14 × 1.0 with the receptacle's 2 rivet holes, takes up a 1.0 thinner stack

**What** The tolerance compensator of a quarter-turn fastener: a flat zinc-plated steel ring Ø40 × Ø14 × 1.0 that sits round the stud
between the frame flange's underside and the receptacle's base plate, with the receptacle's two rivet holes (Ø3.4 at x ±14) in it.
latch 1.0's stud (Length 21) is built for a 4.0 stack (a 2.0 panel on a 2.0 flange); on a stack of 3.0 (a 1.0 panel or a 1.0 flange)
the receptacle would sit 1.0 higher and the cross pin 1.5 under the cam plate. The ring takes up that 1.0, so the cam plate lies where
latch puts it and the pin locks 0.5 under it again. The receptacle's rivets pass the flange, the ring and the base plate, so they clamp
the three as one solid stack (review mech-r148 finding 1: 1.0's Ø20 ring lay inside the rivets, which then pulled the plate's ends 1.0
up into the gap). Its Ø14 bore is latch's flange hole: the Ø6 shank and the Ø3 × 12 cross pin pass it at any angle. Every stud and
receptacle figure is read from latch 1.0 (`library.load("latch")` in element.py), so the ring and the stud cannot drift apart.
**Class** connector-part · **Baseline** our own design: generic tolerance compensator (ETIM 10.0 EC011999, Tolerance compensator
(quarter turn fastener); synonyms compensator ring, protective cup, tolerance ring), OPERATING.md 12 "Generic elements" (EM, 2026-11-07).
No inventory row names it: the lane's tier-1 ETIM groups are done (lib/rounds/mech/r143.md), and EC011999 is the next class of group
EG021006 in lib/toolkit/generic.py's mech order that the lane builds after spring-plate-qt-6 (lib/rounds/mech/r147.md, Proposed next);
its shape no dimensional standard fixes and it needs no safety rating. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the ring's top face (its seat against the frame flange's underside) z = 0, on the stud's axis, x
along the receptacle's rivet line; −z goes into the ring, the receptacle's base plate under it. Extents x ±20, y ±20, z −1.0 to 0. In
latch 1.0's frame, on a 3.0 stack the ring's z = 0 is latch's z −3 and its underside latch's z −4, the receptacle base plate's top.
**Built with** toolkit 1.3 · AutoLISP command `CMPRQT6` · no parameter.

## Class values (ETIM 10.0 EC011999)
Design inputs. EC011999 Tolerance compensator (quarter turn fastener) (lib/standards/etim/classes.csv: group EG021006
Accessories/components for fasteners and anchoring systems, tier 2, 4 features) is a class whose features
lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are on file this table gives the values
the ring is designed to under plain names, as receptacle-clip-qt-6 1.0 and spring-plate-qt-6 1.0 do (requests mech-8 and mech-9, the
core's answers); a later minor version restates them in ETIM's order with their EF codes, "not stated" where the design has no value
(lib/needs-em/mech.md 230).

| value | this element |
|---|---|
| material | steel, zinc-plated (the `M-ZINC` layer, as latch's grommet; the grade not stated) |
| form | flat ring with two rivet holes |
| the stud it takes | Ø6 shank with a Ø3 × 12 cross pin: latch 1.0's stud |
| take-up | 1.0: a stack of 3.0 (a 1.0 panel or flange) under latch 1.0's 4.0 stud |
| outside / inside diameter | Ø40 / Ø14 |

No ratings.csv: no rating the checks read, and no load, holding force or locking figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the stud | Ø6 shank and the Ø3 × 12 cross pin through the Ø14 bore at any angle (the pin 1.0 clear at either end) | latch 1.0 (element.py SHANK_R, PIN_L, BORE_R; read with library.load) |
| the frame's flange | the ring's top against the flange's underside, its bore on the flange's own Ø14 hole, its rivet holes on the flange's | latch 1.0 (spec.md What it meets, the frame's flange: Ø14 or a 14 × 4 slot); the flange's rivet holes are the host's |
| the receptacle | latch 1.0's base plate (x ±20, y ±7) under the ring: the ring's Ø40 spans the plate's 40 length and covers its 14 width; its 2 × Ø3.4 holes at x ±14 lie on the plate's rivet holes, so the receptacle's rivets or screws pass flange, ring and plate and clamp them as one stack | latch 1.0 (element.py REC_X, REC_Y, RIVET_X, RIVET_D); ISO 273 medium (lib/standards/holes.csv) for the rivet holes |

## Its own sizes (design choices; the stud's and receptacle's figures read from latch 1.0)
| item | value | why |
|---|---|---|
| thickness | 1.0 | the take-up from a 3.0 stack to latch's 4.0 (one panel or flange a gauge thinner); 1.0 sheet, so the gate skips its edges |
| bore | Ø14 | latch's flange hole: the pin (12 long) 1.0 clear at either end, so the bore needs no keyhole |
| outside | Ø40 | the receptacle base plate's length (2 × REC_X): the rivet holes lie 4.3 inside the rim (20 − 15.7) and 5.3 outside the bore (12.3 − 7), both asserted in element.py |
| rivet holes | 2 × Ø3.4 at x ±14 | the receptacle's own (M3 clearance medium, ISO 273), position Ø0.4 as latch's (features.csv); the ring is placed with them on the receptacle's rivet line |

## Mechanism
None in the ring: one fixed body, no moving node, no port. The stud that turns through it is latch's node `stud` (0 to 90 degrees);
fitting it between the flange and the receptacle, and the rivets that clamp the stack, are the host's assembly. behaviour.csv is the
header only.

## Named nodes
None. One collider, an axis-aligned box: `ring` (x ±20, y ±20, z −1.0 to 0), named apart from any node.

## Materials by layer
`M-ZINC` the whole ring (zinc-plated steel).

## Decals (Blender)
No label: the ring's one layer, `M-ZINC`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as one cylinder Ø40 × 1.0 less a through hole Ø14 and two through holes Ø3.4 at x ±14.
Volume by hand: π × (20² − 7² − 2 × 1.7²) × 1.0 = π × (400 − 49 − 5.78) = π × 345.22 = 1084.5 mm³.
Not drawn: the flange, the receptacle, the rivets, the stud.

## Outputs (out/)
`compensator-ring-qt-6.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011999), our own design (mech-r148, unattended, 2026-11-13): a flat ring Ø20 × Ø14 × 1.0 between the frame flange and latch 1.0's receptacle that takes up a stack 1.0 thinner than latch's 4.0, every stud figure read from latch |
| 2.0 | review mech-r148 finding 1 (mech-r159, unattended, 2026-11-13): the Ø20 ring lay inside the receptacle's rivets, so they could not clamp the stack it is for; now Ø40 (the base plate's length) with the receptacle's 2 × Ø3.4 rivet holes at x ±14, so the rivets pass flange, ring and plate. A major: the outline and the cut-outs change; nothing places it |
