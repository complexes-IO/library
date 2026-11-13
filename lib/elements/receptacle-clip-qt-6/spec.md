# receptacle-clip-qt-6 · v1.0 · receptacle clip for a quarter-turn fastener, generic, for a Ø6 stud with a Ø3 × 12 cross pin, pressed spring steel 1.2, 40 × 14 × 10.2, keyholes in both plates, 2 × M3 rivet holes

**What** The receptacle of a quarter-turn fastener: the pressed spring-steel stirrup riveted under a frame's flange that a removable
panel's stud locks into. A base plate 40 × 14 × 1.2 lies against the flange's underside, two legs carry a cam plate of the same size
10.2 below the flange; each plate has a keyhole (a Ø7 bore for the stud's Ø6 shank and a 13 × 4 slot along x for its Ø3 × 12 cross
pin), and the base plate two Ø3.4 holes for M3 rivets or screws. The stud goes in with its pin in line with the slots (90 degrees),
a quarter turn puts the pin across them (0 degrees), 0.5 under the cam plate, and the panel is held. It is the receptacle latch 1.0
draws inside itself, made its own element so a host, and a later latch version, places it rather than redraws it (OPERATING.md 12,
common parts). Every figure is read from latch (`library.load("latch")` in element.py), so the stud and the clip cannot drift apart.
**Class** connector-part · **Baseline** our own design: generic receptacle clip (ETIM 10.0 EC011979, Receptacle clip (quarter turn
fastener); synonyms front load receptacle, three part clip), OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row
names it: the lane's tier-1 ETIM groups are done (lib/rounds/mech/r143.md), and EC011979 is the first class of the next group in
lib/toolkit/generic.py's mech order, EG021006, whose shape no dimensional standard fixes and which needs no safety rating
(lib/rounds/mech/r144.md gives the classes passed over). No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the base plate's top face (its seat against the flange's underside) z = 0, on the stud's axis;
−z goes into the clip, the cam plate at the bottom. The keyholes' slots and the rivet holes lie along x. Extents x ±20, y ±7, z −10.2
to 0. In latch 1.0's frame the clip's z = 0 is latch's z −4 (a 2.0 panel on a 2.0 flange).
**Built with** toolkit 1.3 · AutoLISP command `RECQT6` · no parameter.

## Class values (ETIM 10.0 EC011979)
Design inputs. EC011979 Receptacle clip (quarter turn fastener) (lib/standards/etim/classes.csv: group EG021006
Accessories/components for fasteners and anchoring systems, tier 2, 5 features) is a class whose features
lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are on file this table gives the
values the clip is designed to under plain names, as rack-cantilever 1.0 and fan-exhaust 1.0 do (requests mech-8 and mech-9, the
core's answers); the next minor version restates them in ETIM's order with their EF codes, "not stated" where the design has no value
(lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | spring steel (lib/materials.csv `steel-spring`; the grade not stated) |
| surface | bright (the `M-SILVER` layer); no plating stated |
| the stud it takes | Ø6 shank with a Ø3 × 12 cross pin: latch 1.0's stud |
| the stack it is built for | a 2.0 panel on a 2.0 flange (latch 1.0's Length 21) |
| fixing | 2 × M3 rivets or screws through Ø3.4 holes at 28 pitch (ISO 273 medium); the rivets are the host's |

No ratings.csv: no rating the checks read, and no load, holding force or locking figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the stud | Ø6 shank through the Ø7 bores (0.5 clear round it); the Ø3 × 12 cross pin through the 13 × 4 slots at 90 degrees, across them at 0, its top 0.5 under the cam plate's underside (z −10.7) | latch 1.0 (element.py SHANK_R, PIN_R, PIN_L, PIN_Z; read with library.load) |
| the frame's flange | the base plate's top against the flange's underside; the flange's own hole for the pin (Ø14 or a 14 × 4 slot along x) is cut by the frame's element | latch 1.0 (spec.md What it meets, the frame's flange) |
| the fixing | 2 × Ø3.4 at x ±14, M3 clearance medium, position Ø0.4 at MMC (features.csv) | ISO 273 medium (lib/standards/holes.csv); ASME Y14.5 floating fastener |

## Its own sizes (design choices, read from latch 1.0)
| item | value | why |
|---|---|---|
| plates | 40 × 14 × 1.2, base z −1.2 to 0, cam z −10.2 to −9.0 | latch's receptacle (REC_X, REC_Y, REC_T, REC_TOP, CAM_TOP); 1.2 sheet, so every edge of its section is "short" in the gate's fillet pass |
| legs | 1.2 × 14 × 7.8 at the plates' ends (x ±18.8 to ±20, z −9.0 to −1.2) | the stirrup's sides, plate to plate |
| keyholes | Ø7 bore + a 13 × 4 slot along x in both plates | the shank 0.5 clear; the pin 0.5 clear at each end and side (asserted in element.py) |
| rivet holes | 2 × Ø3.4 at x ±14 in the base plate | clear of the legs (x 15.7 < 18.8) and of the slot (12.3 > 6.5), asserted |
| cam ramps, spring take-up | not drawn: the plates are flat | the 0.5 under the cam plate is where a real clip's spring takes up; appearance and mechanism the twin doesn't read |

## Mechanism
None in the clip: one fixed body, no moving node, no port. The stud that turns in it is latch's node `stud` (0 to 90 degrees);
riveting it under a flange is the host's assembly. behaviour.csv is the header only.

## Named nodes
None. One collider, an axis-aligned box: `clip` (x ±20, y ±7, z −10.2 to 0), named apart from any node.

## Materials by layer
`M-SILVER` the whole clip (bright spring steel).

## Decals (Blender)
No label: the clip's one layer, `M-SILVER`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as two plates (each a box less a hole and a cut, the keyhole; the base plate less two
rivet holes) and two leg boxes, latch 1.0's receptacle moved up by 4. Volume by hand: each plate 40 × 14 × 1.2 = 672 less the keyhole
(the Ø7 bore's π × 3.5² = 38.48 and the slot's 13 × 4 = 52 overlap; their union 52 + 38.48 − the bore's part inside the slot, 2 ×
(3.5² × asin(2 / 3.5) + 2 × √(3.5² − 2²)) = 2 × (7.45 + 5.74) = 26.39, so 64.09 mm² × 1.2 = 76.91 mm³) = 595.09; the base plate less
2 × π × 1.7² × 1.2 = 21.79, so 573.30; the legs 2 × 1.2 × 14 × 7.8 = 262.08; in all 1 430.5 mm³.
Not drawn: the cam ramps and spring take-up, the rivets, the flange, the stud.

## Outputs (out/)
`receptacle-clip-qt-6.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011979), our own design (mech-r144, unattended, 2026-11-13): latch 1.0's receptacle as its own part, every figure read from latch; plates 40 × 14 × 1.2, 10.2 deep, keyholes for a Ø6 stud with a Ø3 × 12 pin, 2 × M3 rivet holes |
