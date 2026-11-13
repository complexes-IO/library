# cap-strut-41 · v1.0 · end cap for a 41 × 41 strut channel, generic, grey polyamide, plate 41 × 41 × 2 flush with the channel's outline, plug 35.6 × 25.6 × 12 into the lower chamber 0.2 clear

**What** The end cap of the 41 × 41 strut channel: a grey polyamide plate 41 × 41 × 2 that closes the channel's cut end, flush with its
outline, and a plug 35.6 × 25.6 × 12 that enters the channel's lower chamber: between the two walls, over the slotted back, under the
lips' returns, 0.2 clear of each. It covers the sharp cut edges and keeps dirt out of the channel. Every channel figure is read from
strut 1.0 (`library.load("strut")` in element.py), so the cap and the channel cannot drift apart.
**Class** connector-part · **Baseline** our own design: generic protective cap/cover for mounting rail/-profile (ETIM 10.0 EC000475,
Protective cap/cover for mounting rail/- profile; synonyms end cap, end cap/cover for support/profile rail, profile rail cover cap),
OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG021006 is walked by name (lib/rounds/mech/r149.md),
and EC000475 is the class of the next group in lib/toolkit/generic.py's mech order, EG021005 Mounting systems, that fits an element on
file (strut, process-skid's channel); its shape no dimensional standard fixes and it needs no safety rating. No product was matched and
no vendor file was opened.
**Units / frame** mm, Z up. Origin: strut's own frame at its run start, so the cap goes on with no transform: the channel's end face
x = 0 (the cap's seat), the centre line y = 0, the back's outer face z = 0; the plug goes +x into the channel, the plate lies at −x, the
open side (the lips) up. Extents x −2 to 12, y ±20.5, z 0 to 41. At the run's far end the host turns it 180° about z and moves it to
x = length.
**Built with** toolkit 1.3 · AutoLISP command `CAPST41` · no parameter.

## Class values (ETIM 10.0 EC000475)
Design inputs. EC000475 Protective cap/cover for mounting rail/- profile (lib/standards/etim/classes.csv: group EG021005 Mounting
systems, tier 2, 7 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from
memory. Until they are on file this table gives the values the cap is designed to under plain names, as compensator-ring-qt-6 1.0 and
spring-plate-qt-6 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order with
their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | polyamide, grey (the `M-GREY-PA` layer; the grade not stated) |
| form | end cap: a plate over the end face and a plug into the channel |
| the profile it fits | strut 1.0: 41 × 41, wall 2.5, inturned lips with 10 returns |
| outside size | 41 × 41, flush with the profile's outline |
| plug | 35.6 × 25.6 × 12, 0.2 clear all round |

No ratings.csv: no rating the checks read, and no retention force, impact or fire figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the channel's outline | 41 × 41: the plate covers the end face and does not stand past it | strut 1.0 (element.py W, H; read with library.load) |
| the lower chamber | between the walls' inner faces (y ±18), over the back (z 2.5), under the returns (z 28.5): the plug 0.2 clear of each, asserted | strut 1.0 (element.py W, T, H, RET) |
| the returns | at y ±11 to ±13.5, z 28.5 to 38.5: over the plug, not touched | strut 1.0 (element.py LIP, T, RET) |
| the back's slots | under the plug, through the back only: the plug does not enter them | strut 1.0 (element.py SLOT_W, SLOT_L) |

## Its own sizes (design choices; the channel's figures read from strut 1.0)
| item | value | why |
|---|---|---|
| plate | 41 × 41 × 2 | flush with the channel's outline; 2 thick so the gate skips its edges ("short") |
| plug depth | 12 | enough to seat it square in the channel; over the gate's 3 to 7 mm free-corner trap |
| clearance | 0.2 all round | a push fit drawn clear, so no solid overlaps the channel in an assembly; ribs that would grip are not drawn and no retention is claimed |

## Mechanism
None in the cap: one fixed body, no moving node, no port. Pushing it into the channel is the host's assembly. behaviour.csv is the
header only.

## Named nodes
None. Two colliders, axis-aligned boxes named apart from any node: `plate` (x −2 to 0, y ±20.5, z 0 to 41) and `plug` (x 0 to 12,
y ±17.8, z 2.7 to 28.3), so the channel's inside stays free.

## Materials by layer
`M-GREY-PA` the whole cap (grey polyamide).

## Decals (Blender)
No label: the cap's one layer, `M-GREY-PA`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as two boxes in one material: the plate, and the plug run 0.5 into it (one solid joint).
Volume by hand: 41 × 41 × 2 + 35.6 × 25.6 × 12 = 3362 + 10936.3 = 14298.3 mm³.
Not drawn: the channel, the grip ribs.

## Outputs (out/)
`cap-strut-41.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000475), our own design (mech-r149, unattended, 2026-11-13): an end cap for strut 1.0, a plate 41 × 41 × 2 flush with its outline and a plug into its lower chamber 0.2 clear, every channel figure read from strut |
