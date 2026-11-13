# bracket-angle-strut-41 · v1.0 · 90-degree angle bracket for a 41 × 41 strut channel, generic, zinc-plated steel, two legs 90 × 41 × 8, one M12 clearance hole in each

**What** A 90-degree angle bracket (mounting angle bracket) for the 41 × 41 strut channel: a zinc-plated steel angle that joins one
channel to a second channel, or to a frame, square to it. Two legs, each 41 wide (as wide as the channel, so its edges lie flush with the
channel's walls), 8 thick and 90 long from the outside corner. Each leg has one Ø13.5 hole (M12, ISO 273 medium) on its centre line,
50 out from the outside corner. A leg seats with its outside face on the channel's open side (the lips' face, the bolt into a channel
nut through the 22 opening) or on its back (the bolt through a back slot, 13.5 wide); one M12 through each hole fixes it. Every channel
figure is read from strut 1.0 (`library.load("strut")` in element.py); the channel is placed, never redrawn.
**Class** plate · **Baseline** our own design: generic fastening element for mounting rail/-profile (ETIM 10.0 EC000482; synonyms base
plate, ceiling bracket, clamp piece, floor console, floor plate, mounting angle bracket), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). No inventory row names it: group EG021005 Mounting systems is walked by name from lib/toolkit/generic.py's mech order
(lib/rounds/mech/r149.md to r152.md), and EC000482 is the next of its classes that meets an element on file (strut); its shape no
dimensional standard fixes and it needs no safety rating. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the outside corner; the horizontal leg's seat face z = 0 (it lies on a channel, running +x), the
upright leg's seat face x = 0 (it stands against a second channel or a frame, running +z), the bracket's centre plane y = 0.
Extents x 0 to 90, y ±20.5, z 0 to 90.
**Built with** toolkit 1.3 · AutoLISP command `BRAS41` · no parameter.

## Class values (ETIM 10.0 EC000482)
Design inputs. EC000482 Fastening element for mounting rail/-profile (lib/standards/etim/classes.csv: group EG021005 Mounting systems,
tier 2, 6 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory.
Until they are on file this table gives the values the bracket is designed to under plain names, as console-strut-41 1.0 and
head-plate-strut-41 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order with
their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, zinc-plated (the `M-ZINC` layer; the grade not stated) |
| form | mounting angle bracket, 90 degrees, two legs |
| the profile it joins | strut 1.0: 41 × 41, wall 2.5, lips' opening 22, slotted back 13.5 × 28 at 50 |
| legs | 2 × 90 × 41 × 8 from the outside corner |
| holes | 2 × Ø13.5 (M12, ISO 273 medium), one in each leg, 50 from the outside corner on its centre line |
| fixing to the profile | one M12 through each hole, into a channel nut through the lips' opening or through a back slot |

No ratings.csv: no rating the checks read, and no load, slip or pull-out figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the channel's width | 41; each leg is as wide, so its long edges lie flush with the channel's walls (y ±20.5) | strut 1.0 (element.py W; read with library.load) |
| the lips' opening | 22 on the channel's centre line; the leg's hole, Ø13.5 on y = 0, lies inside it, so a bolt into a channel nut passes | strut 1.0 (element.py OPEN) |
| the channel's back slots | 13.5 wide on the back's centre line; the leg's hole is the same width, so one M12 passes both where the hole stands over a slot | strut 1.0 (element.py SLOT_W) |
| the M12 through each leg | Ø13.5 clearance, ISO 273 medium (lib/standards/holes.csv); position Ø1.5 at MMC, floating fastener (features.csv); the bolt, its nut or channel nut are the host's, not drawn | ISO 273; ASME Y14.5 |

## Its own sizes (design choices; the channel's figures read from strut 1.0)
| item | value | why |
|---|---|---|
| leg length | 90 from the outside corner | a hole 50 out with 33.25 of metal to the leg's end and 35.25 to the other leg's inner face (room for a bolt head and washer) |
| leg width | 41 | as wide as the channel, flush with its walls |
| thickness | 8 | every free edge 8 or more, clear of the gate's 3 to 7 mm trap |
| holes | Ø13.5, 50 from the outside corner on y = 0 | M12 clearance medium; 13.75 of metal beside each hole |
| joint | the upright runs 0.5 into the horizontal leg (one solid) | a formed or welded angle; no bend radius or weld size is claimed |

## Mechanism
None: one fixed body, no moving node, no port. Bolting the bracket to two channels is the host's assembly. behaviour.csv is the header
only.

## Named nodes
None. Two colliders, axis-aligned boxes named apart from any node: `leg-x` (x 0 to 90, y ±20.5, z 0 to 8) and `leg-z` (x 0 to 8,
y ±20.5, z 8 to 90), so the space inside the angle stays free.

## Materials by layer
`M-ZINC` the whole bracket (zinc-plated steel, strut's layer).

## Decals (Blender)
No label: the bracket's one layer, `M-ZINC`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as two boxes in one material, each with one through hole: the horizontal leg, and the upright
run 0.5 into it. Volume by hand: horizontal leg 90 × 41 × 8 − π × 6.75² × 8 = 29520 − 1145.1 = 28374.9; upright 8 × 41 × 82.5
− π × 6.75² × 8 = 27060 − 1145.1 = 25914.9; together 54289.8 mm³ (the upright's 0.5 inside the horizontal leg counted, 164).
Not drawn: the channels, the bolts and their nuts or channel nuts.

## Outputs (out/)
`bracket-angle-strut-41.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000482), our own design (mech-r152, unattended, 2026-11-13): a 90-degree angle bracket for strut 1.0, two legs 90 × 41 × 8 with one M12 clearance hole each, every channel figure read from strut |
