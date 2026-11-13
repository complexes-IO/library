# spring-plate-qt-6 · v1.0 · spring plate for a quarter-turn fastener, generic, for a Ø6 stud with a Ø3 × 12 cross pin, pressed spring steel 1.2, hat section 52 × 14 × 10.2, keyhole in the bridge, 2 × M3 rivet holes in the tabs

**What** The spring plate of a quarter-turn fastener: a one-piece pressed spring-steel bridge riveted behind a frame's flange that a
removable panel's stud locks under. Two tabs 14 × 14 × 1.2 lie against the flange's underside, two legs carry a bridge 21.6 × 14 × 1.2
10.2 below the flange; the bridge has a keyhole (a Ø7 bore for the stud's Ø6 shank and a 13 × 4 slot along x for its Ø3 × 12 cross pin),
and each tab a Ø3.4 hole for an M3 rivet or screw. The stud goes in with its pin in line with the slot (90 degrees), a quarter turn puts
the pin across it (0 degrees), 0.5 under the bridge, and the panel is held. It is the other form of the receptacle beside
receptacle-clip-qt-6: a hat section with its tabs outside the legs, so nothing lies under the flange's hole and the rivets sit clear of the
stud's path. Every stud figure is read from latch 1.0 (`library.load("latch")` in element.py), so the stud and the plate cannot drift
apart.
**Class** connector-part · **Baseline** our own design: generic spring plate (ETIM 10.0 EC011978, Spring plate (quarter turn fastener);
synonyms rivet spring plate, spring bracket, slip-on spring receptacle, weld spring plate), OPERATING.md 12 "Generic elements" (EM,
2026-11-07). No inventory row names it: the lane's tier-1 ETIM groups are done (lib/rounds/mech/r143.md), and EC011978 is the next class
of group EG021006 in lib/toolkit/generic.py's mech order that the lane builds after threaded-sleeve-m8 (lib/rounds/mech/r146.md, Proposed
next); its shape no dimensional standard fixes and it needs no safety rating. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the tabs' top face (their seat against the flange's underside) z = 0, on the stud's axis; −z goes
into the plate, the bridge at the bottom. The keyhole's slot and the rivet holes lie along x. Extents x ±26, y ±7, z −10.2 to 0. In
latch 1.0's frame the plate's z = 0 is latch's z −4 (a 2.0 panel on a 2.0 flange), as receptacle-clip-qt-6's.
**Built with** toolkit 1.3 · AutoLISP command `SPRQT6` · no parameter.

## Class values (ETIM 10.0 EC011978)
Design inputs. EC011978 Spring plate (quarter turn fastener) (lib/standards/etim/classes.csv: group EG021006 Accessories/components for
fasteners and anchoring systems, tier 2, 6 features) is a class whose features lib/standards/etim/class-features.csv does not list, and
none is written from memory. Until they are on file this table gives the values the plate is designed to under plain names, as
receptacle-clip-qt-6 1.0 and rack-cantilever 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates
them in ETIM's order with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | spring steel (lib/materials.csv `steel-spring`; the grade not stated) |
| surface | bright (the `M-SILVER` layer); no plating stated |
| form | rivet spring plate: hat section, tabs outside the legs |
| the stud it takes | Ø6 shank with a Ø3 × 12 cross pin: latch 1.0's stud |
| the stack it is built for | a 2.0 panel on a 2.0 flange (latch 1.0's Length 21) |
| fixing | 2 × M3 rivets or screws through Ø3.4 holes at 38 pitch (ISO 273 medium); the rivets are the host's |

No ratings.csv: no rating the checks read, and no load, holding force or locking figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the stud | Ø6 shank through the Ø7 bore (0.5 clear round it); the Ø3 × 12 cross pin through the 13 × 4 slot at 90 degrees, across it at 0, its top 0.5 under the bridge's underside (z −10.7); its turn (r 6) clear of the legs' inner faces (x ±10.8) | latch 1.0 (element.py SHANK_R, PIN_R, PIN_L, PIN_Z, REC_SLOT; read with library.load) |
| the frame's flange | the tabs' top against the flange's underside; the flange's own hole for the pin (Ø14 or a 14 × 4 slot along x) is cut by the frame's element and lies between the legs (x ±10.8 clear) | latch 1.0 (spec.md What it meets, the frame's flange) |
| the fixing | 2 × Ø3.4 at x ±19, M3 clearance medium, position Ø0.4 at MMC (features.csv) | ISO 273 medium (lib/standards/holes.csv); ASME Y14.5 floating fastener |

## Its own sizes (design choices; the stud's figures read from latch 1.0)
| item | value | why |
|---|---|---|
| bridge | 21.6 × 14 × 1.2, z −10.2 to −9.0 | latch's receptacle depth (REC_TOP, CAM_TOP, REC_T) and width (REC_Y); its span between the legs, 21.6, clears the pin's 12 turn by 4.8 a side (asserted) |
| legs | 1.2 × 14 × 10.2 at x ±10.8 to ±12, z −10.2 to 0 | the hat's sides, the full depth, so no edge of the part falls between 3 and 7 long (the gate's fillet trap; asserted) |
| tabs | 14 × 14 × 1.2 at x ±12 to ±26, z −1.2 to 0 | outside the legs, square on the plate's width; a rivet on each tab's centre |
| keyhole | Ø7 bore + a 13 × 4 slot along x in the bridge | the shank 0.5 clear; the pin 0.5 clear at each end and side (asserted in element.py) |
| rivet holes | 2 × Ø3.4 at x ±19 | on the tabs, clear of the legs (17.3 > 12) and of the tabs' ends (20.7 < 26), asserted |
| cam ramps, spring take-up | not drawn: the bridge is flat | the 0.5 under the bridge is where a real plate's spring takes up; appearance and mechanism the twin doesn't read |

## Mechanism
None in the plate: one fixed body, no moving node, no port. The stud that turns in it is latch's node `stud` (0 to 90 degrees);
riveting it behind a flange is the host's assembly. behaviour.csv is the header only.

## Named nodes
None. One collider, an axis-aligned box: `plate` (x ±26, y ±7, z −10.2 to 0), named apart from any node.

## Materials by layer
`M-SILVER` the whole plate (bright spring steel).

## Decals (Blender)
No label: the plate's one layer, `M-SILVER`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as a bridge (a box less a hole and a cut, the keyhole), two leg boxes and two tab boxes
(each less a rivet hole). Volume by hand: the bridge 21.6 × 14 × 1.2 = 362.88 less the keyhole 76.91 (the slot's 52 mm² and the Ø7
bore's 38.48 less their overlap 26.39, so 64.09 mm² × 1.2, as receptacle-clip-qt-6's) = 285.97; the legs 2 × 1.2 × 14 × 10.2 = 342.72;
the tabs 2 × 14 × 14 × 1.2 = 470.40 less 2 × π × 1.7² × 1.2 = 21.79, so 448.61; in all 1 077.3 mm³.
Not drawn: the cam ramps and spring take-up, the rivets, the flange, the stud.

## Outputs (out/)
`spring-plate-qt-6.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011978), our own design (mech-r147, unattended, 2026-11-13): a hat-section spring plate for latch 1.0's stud, every stud figure read from latch; bridge 21.6 × 14 × 1.2 with the keyhole, 10.2 deep, legs to full depth, tabs 14 × 14 outside them with 2 × M3 rivet holes at 38 pitch |
