# head-plate-strut-41 · v1.0 · head plate for a 41 × 41 strut channel, generic, zinc-plated steel, plate 120 × 120 × 8 with 4 × M12 anchor holes, tab 75 × 41 × 8 under the channel's back with a 13.5 slot

**What** The head plate of the 41 × 41 strut channel: a zinc-plated steel plate that stands the channel on a floor or hangs it from a
ceiling. A square plate 120 × 120 × 8 lies across the channel's end, centred on its outline, with four M12 anchor holes (Ø13.5, ISO 273
medium) on an 80 square pitch, all outside the channel. A tab 75 × 41 × 8 is welded square to the plate under the channel's back, as wide
as the channel. The tab carries a slot 13.5 wide from x 18 to 57. Wherever strut is cut, its first back slot's centre falls between x 25
and 50 (strut's slots are centred on the length at a 50 pitch), so one M12 passes the channel's first slot and the tab's slot together at
any length. Every channel figure is read from strut 1.0 (`library.load("strut")` in element.py), so the plate and the channel cannot drift
apart.
**Class** plate · **Baseline** our own design: generic head plate for mounting rail/-profile (ETIM 10.0 EC001567, Head plate for mounting
rail/-profile; synonyms head plate for profile rail, head plate for support, floor plate, ceiling bracket), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: group EG021005 Mounting systems is walked by name from lib/toolkit/generic.py's mech
order (lib/rounds/mech/r149.md, r150.md), and EC001567 is the next of its classes that meets an element on file (strut, process-skid's
channel); its shape no dimensional standard fixes and it needs no safety rating. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: strut's own frame at its run start, so the channel goes on with no transform: the channel's end face
x = 0 (on the plate's face), the centre line y = 0, the back's outer face z = 0 (on the tab's top face); the channel runs +x from the plate,
the plate's outer face (on the floor or ceiling) at x = −8. Extents x −8 to 75, y ±60, z −39.5 to 80.5. A host that stands the channel
upright turns the whole set so +x points up.
**Built with** toolkit 1.3 · AutoLISP command `HPST41` · no parameter.

## Class values (ETIM 10.0 EC001567)
Design inputs. EC001567 Head plate for mounting rail/-profile (lib/standards/etim/classes.csv: group EG021005 Mounting systems, tier 2,
10 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are
on file this table gives the values the plate is designed to under plain names, as cap-strut-41 1.0 and compensator-ring-qt-6 1.0 do
(requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order with their EF codes, "not stated"
where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, zinc-plated (the `M-ZINC` layer; the grade not stated) |
| form | square head plate with a welded tab |
| the profile it fits | strut 1.0: 41 × 41, wall 2.5, slotted back 13.5 × 28 at 50 |
| plate | 120 × 120 × 8 |
| anchor holes | 4 × Ø13.5 (M12, ISO 273 medium), 80 square pitch |
| fixing to the profile | one M12 through the tab's slot and the profile's first back slot |

No ratings.csv: no rating the checks read, and no load, pull-out or fire figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the channel's outline | 41 × 41, centred on the plate (z 0 to 41, y ±20.5); the anchor holes stand outside it (\|y\| ≥ 33.25 at their edge) | strut 1.0 (element.py W, H; read with library.load) |
| the channel's back slots | 13.5 × 28 at a 50 pitch, centred on the length: the first slot's centre lies at x 25 to 49.75 for every length of 50 or more (computed for 50 to 1049.5 in 0.5 steps, asserted); the tab's slot, x 18 to 57, holds an M12's Ø13.5 clearance at any of them | strut 1.0 (element.py SLOT_W, SLOT_L, SLOT_PITCH and build()'s slot rule) |
| the channel's back | its outer face z = 0 lies on the tab's top face, its end face x = 0 on the plate | strut 1.0 (element.py origin) |
| the M12 through tab and channel | Ø13.5 clearance, ISO 273 medium (lib/standards/holes.csv); the bolt, its nut or channel nut are the host's, not drawn | ISO 273 |
| the anchors | 4 × M12 at Ø13.5, ISO 273 medium; position Ø1.5 at MMC, floating fastener (features.csv); the anchor and its seat in the floor or ceiling are the host's, not drawn | ISO 273; ASME Y14.5 |

## Its own sizes (design choices; the channel's figures read from strut 1.0)
| item | value | why |
|---|---|---|
| plate | 120 × 120 × 8 | room for four M12 anchors outside the channel with a washer; 8 thick so its edges clear the gate's 3 to 7 mm trap |
| anchor pitch | 80 square, round the channel's centre | 20 from the hole's centre to each edge (13.25 of metal), the holes' edges 12.75 outside the channel's walls |
| tab | 75 × 41 × 8, welded square to the plate | as wide as the channel; long enough for the slot and 18 of metal beyond it |
| tab slot | 13.5 × 39, x 18 to 57 | the channel's back slot width; long enough for the first slot at any length (above) |
| weld | the tab runs 0.5 into the plate (one solid joint) | the weld itself is not drawn and no weld size is claimed |

## Mechanism
None: one fixed body, no moving node, no port. Anchoring the plate and bolting the channel to the tab are the host's assembly.
behaviour.csv is the header only.

## Named nodes
None. Two colliders, axis-aligned boxes named apart from any node: `plate` (x −8 to 0, y ±60, z −39.5 to 80.5) and `tab` (x 0 to 75,
y ±20.5, z −8 to 0), so the channel's space above the tab stays free.

## Materials by layer
`M-ZINC` the whole plate (zinc-plated steel, strut's layer).

## Decals (Blender)
No label: the plate's one layer, `M-ZINC`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as two boxes in one material: the plate with four through holes, and the tab with its slot
(one cut), run 0.5 into the plate. Volume by hand: plate 120 × 120 × 8 − 4 × π × 6.75² × 8 = 115200 − 4580.4 = 110619.6; tab 75 × 41 × 8 −
39 × 13.5 × 8 = 24600 − 4212 = 20388; together 131007.6 mm³ (the 0.5 joint not counted).
Not drawn: the channel, the bolt and its nut, the anchors, the weld.

## Outputs (out/)
`head-plate-strut-41.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC001567), our own design (mech-r150, unattended, 2026-11-13): a head plate for strut 1.0, a 120 × 120 × 8 plate with four M12 anchor holes and a tab whose slot meets the channel's first back slot at any length, every channel figure read from strut |
