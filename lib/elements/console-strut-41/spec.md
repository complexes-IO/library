# console-strut-41 · v1.1 · rail console for a 41 × 41 strut channel, generic, zinc-plated steel, wall plate 80 × 160 × 8 with 2 × M12 anchor holes, arm 300 long, inverted U 41 × 80 with a 13.5 slot along its top

**What** A rail console (cantilever arm) for the 41 × 41 strut channel: a zinc-plated steel arm on its own wall plate that carries the
channel laid across its top. The plate, 80 × 160 × 8, goes on the wall with two M12 anchors (Ø13.5, ISO 273 medium) on its centre line,
one above the arm and one below it. The arm, welded square to the plate, reaches 300 from it: an inverted U 41 wide and 80 deep, a top
8 thick on two webs 8 thick, open below with 25 clear between the webs. The top carries a slot 13.5 wide from x 60 to 290. The channel
lies across the arm with its back on the top (z = 0); one M12 through one of the channel's back slots and the top's slot fixes it
anywhere from 66.75 to 283.25 out from the wall, and the nut goes up between the webs. Every channel figure is read from strut 1.0
(`library.load("strut")` in element.py); the channel is placed, never redrawn.
**Class** plate · **Baseline** our own design: generic rail console (ETIM 10.0 EC010933, Rail console; synonyms cantilever arm, clap
console, industry support, rail console set, screw on angle, support for wall rail), OPERATING.md 12 "Generic elements" (EM, 2026-11-07).
No inventory row names it: group EG021005 Mounting systems is walked by name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r149.md
to r151.md), and EC010933 is the next of its classes that meets an element on file (strut); its shape no dimensional standard fixes and it
needs no safety rating. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the plate's wall face x = 0 (the arm runs +x from the wall), the arm's centre plane y = 0, the arm's
top face z = 0 (the seat: the channel's back lies on it, the channel running along y). Extents x 0 to 308, y ±40, z −120 to 40.
**Built with** toolkit 1.3 · AutoLISP command `CNST41` · no parameter.

## Class values (ETIM 10.0 EC010933)
Design inputs. EC010933 Rail console (lib/standards/etim/classes.csv: group EG021005 Mounting systems, tier 2, 14 features) is a class
whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are on file this table
gives the values the console is designed to under plain names, as head-plate-strut-41 1.0 and cap-strut-41 1.0 do (requests mech-8 and
mech-9, the core's answers); the next minor version restates them in ETIM's order with their EF codes, "not stated" where the design has
no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, zinc-plated (the `M-ZINC` layer; the grade not stated) |
| form | cantilever arm, inverted U, welded to a wall plate |
| the profile it carries | strut 1.0: 41 × 41, wall 2.5, slotted back 13.5 × 28 at 50, laid across the arm |
| reach | 300 from the plate's face (308 from the wall face) to the arm's end |
| arm section | 41 × 80, top and webs 8 |
| wall plate | 80 × 160 × 8 |
| anchor holes | 2 × Ø13.5 (M12, ISO 273 medium) |
| fixing to the profile | one M12 through the top's slot and one of the profile's back slots |

No ratings.csv: no rating the checks read, and no load, deflection or pull-out figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the channel's width | 41 across the arm's top (x), as wide as the arm; at the slot's two ends the channel spans x 46.25 to 87.25 and x 262.75 to 303.75, on the arm (asserted) | strut 1.0 (element.py W; read with library.load) |
| the channel's back slots | 13.5 wide on the back's centre line; the top's slot is the same width, so one M12 passes both wherever the channel's slot stands over the top's | strut 1.0 (element.py SLOT_W) |
| the channel's back | its outer face lies on the arm's top face, z = 0 | strut 1.0 (element.py origin: the back's outer face z = 0) |
| the M12 through top and channel | Ø13.5 clearance, ISO 273 medium (lib/standards/holes.csv); the bolt, its nut or channel nut are the host's, not drawn; the nut goes in the 25 between the webs | ISO 273 |
| the anchors | 2 × M12 at Ø13.5, ISO 273 medium; position Ø1.5 at MMC, floating fastener (features.csv); the anchor and its seat in the wall are the host's, not drawn | ISO 273; ASME Y14.5 |

## Its own sizes (design choices; the channel's figures read from strut 1.0)
| item | value | why |
|---|---|---|
| reach | 300 | room for the channel anywhere along 216.5 (bolt at x 66.75 to 283.25), clear of the upper anchor's head (the channel starts 46.25 out at its nearest) |
| arm section | inverted U 41 × 80, top 8, webs 8, 25 clear between them | as wide as the channel; open below so the M12's nut goes up under the top; every edge 8 or more, clear of the gate's 3 to 7 mm trap |
| top slot | 13.5 × 230, x 60 to 290 | the channel's back slot width; 18 of top beyond it at the end |
| wall plate | 80 × 160 × 8, z −120 to 40 | wider than the arm; one anchor 20 above the top and one 20 below the webs, each 13.25 of metal from the arm (room for a washer) and 20 from the plate's end edge |
| weld | the arm runs 0.5 into the plate (one solid joint) | the weld itself is not drawn and no weld size is claimed |

## Mechanism
None: one fixed body, no moving node, no port. Anchoring the plate and bolting the channel to the arm are the host's assembly.
behaviour.csv is the header only.

## Named nodes
None. Two colliders, axis-aligned boxes named apart from any node: `plate` (x 0 to 8, y ±40, z −120 to 40) and `arm` (x 8 to 308,
y ±20.5, z −80 to 0), so the channel's space above the arm stays free.

## Materials by layer
`M-ZINC` the whole console (zinc-plated steel, strut's layer).

## Decals (Blender)
No label: the console's one layer, `M-ZINC`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as two boxes in one material: the plate with two through holes, and the arm with two cuts
(the U's inside, open below and at the end; the top's slot), run 0.5 into the plate. Volume by hand: plate 80 × 160 × 8 − 2 × π × 6.75² × 8
= 102400 − 2290.2 = 100109.8; arm 300.5 × 41 × 80 − 300.5 × 25 × 72 − 230 × 13.5 × 8 = 985640 − 540900 − 24840 = 419900; together
520009.8 mm³ (the arm's 0.5 inside the plate counted, 740).
Not drawn: the channel, the bolt and its nut, the anchors, the weld.

## Outputs (out/)
`console-strut-41.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010933), our own design (mech-r151, unattended, 2026-11-13): a rail console for strut 1.0, a wall plate with two M12 anchor holes and an inverted-U arm 300 long whose top slot takes the channel anywhere along 216.5, every channel figure read from strut |
| 1.1 | review mech-r151 finding 1 (mech-r159, unattended, 2026-11-13; text only, the model unchanged): Class values `reach` reads "300 from the plate's face (308 from the wall face)", as the extents give, and the AL comment in element.py the same |
