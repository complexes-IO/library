# rail-suspension-shelving-1000 · v1.0 · suspension rail for the back of a 1000 wide steel shelving bay, generic, painted steel sheet 2.0, a hook profile 20 x 80 between two end plates on the rear uprights

**What** A suspension rail that spans a steel shelving bay between the inner faces of its two rear uprights, above one of its shelves,
so open-fronted bins hang on it by their rear hooks in front of the bay's back. The rail is one painted steel sheet 2.0 formed to a
hook profile 20 deep and 80 high: a web in the plane of the bay's back (y 488 to 490) and, along its top front edge, a channel open on
top, 16 wide and 13 deep, whose floor is the sheet turned forward and whose front lip is the sheet turned up again; a bin's hook drops
into the channel behind the lip. Two end plates 3 × 40 × 80 close the rail's ends and stand against the rear uprights' inner faces:
one fixed body. The rail's top stands 30 under the shelf above, so a hook lifts out over the lip. Every bay figure is read from
shelving-steel 1.0 (`library.load("shelving-steel")` in element.py); the bay is placed, never redrawn. The end plates' fixing to the
uprights is the host's assembly: none is drawn and no hole is modelled (shelving-steel's uprights carry none).
**Class** furniture · **Baseline** our own design: generic suspension rail (ETIM 10.0 EC004080 Suspension rail (rack element)),
OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by
name from lib/toolkit/generic.py's mech order (lib/rounds/mech/r160.md, Proposed next), and EC004080 is a class not yet built that meets
an element on file (shelving-steel's rear uprights and shelves); its shape no dimensional standard fixes. No product was matched and no
vendor file was opened.
**Units / frame** mm, Z up. Origin: shelving-steel's own x and y, at the height of the top face of the shelf below the rail, so the
host places the rail at the bay's origin raised to that shelf's top (z 150, 600, 1050 or 1500 in shelving-steel 1.0; the top shelf at
1950 has no shelf above it and no rear upright over 2000): that shelf's top face z = 0, the middle of the bay's width x = 0, the front
uprights' front faces y = 0; the bay's depth toward +y, its back at y = 500; bins hang on the rail's front, toward −y.
Extents x −450 to 450, y 455 to 495, z 300 to 380.
**Built with** toolkit 1.3 · AutoLISP command `RSUS1000` · no parameter.

## Class values (ETIM 10.0 EC004080)
Design inputs. EC004080 Suspension rail (rack element) (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems,
tier 2, 4 features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory.
Until they are on file this table gives the values the rail is designed to under plain names, as shelf-pullout-shelving-1000 1.0 and
door-shelving-1000 1.0 do (requests mech-8 and mech-9, the core's answers); a later minor version restates them in ETIM's order with
their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel, painted (the `M-STEEL-7035` layer, shelving-steel's; the grade not stated) |
| the rack it fits | shelving-steel 1.0: bay 1000 × 500 × 2000 over 50 × 50 uprights, between its rear uprights over any of its lower four shelves |
| length | 900 over the end plates (the uprights' inner faces); the rail 894 between them |
| profile | hook profile 20 deep × 80 high, sheet 2.0, an open channel 16 wide and 13 deep along its top front edge |
| load capacity | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the rear uprights | inner faces x ±450 at y 450 to 500; the end plates' outer faces on them, y 455 to 495, 5 inside each upright's front and back faces | shelving-steel 1.0 (element.py W, D, UP) |
| the shelf below | its top face z 0; the rail's bottom 300 above it, so a bin up to 300 high hangs clear of it | shelving-steel 1.0 (element.py SH_TOPS) |
| the shelf above | its underside 410 above the shelf below (450 apart, 40 deep); the rail's top at 380 leaves 30, more than twice the channel's 13 depth, so a hook lifts out over the lip (asserted) | shelving-steel 1.0 (element.py SH_TOPS, SH_T) |

## Its own sizes (design choices; the bay's figures read from shelving-steel 1.0)
| item | value | why |
|---|---|---|
| sheet | 2.0 | a formed rail, not a frame member; under 3, so every section edge is thin to the gate's fillet check |
| web | y 488 to 490, z 300 to 380 | in the plane of the bay's back, 5 in front of the end plates' back edges |
| channel | floor y 470 to 488 at z 360 to 362; clear width 16 (y 472 to 488), 13 deep to the lip's top at z 375 | takes a bin's rear hook up to 16 thick |
| lip | y 470 to 472, z 360 to 375 | holds the hook behind it; 5 under the web's top so the hook rides on the web |
| end plates | 3 × 40 × 80, x ±447 to ±450, y 455 to 495, z 300 to 380 | close the rail's ends against the uprights; carry it as one body |
| height | the rail's bottom 300 above the shelf below | the room under it for a hanging bin; the top 30 under the shelf above |
| folds | drawn sharp (one box less three cutboxes) | no bend radius is claimed |

## Mechanism
None. One fixed body, no node: hanging a bin on the rail and fixing the rail to the bay are the host's assembly, not a motion
(behaviour.csv: the header only).

## Named nodes
None. Colliders, axis-aligned boxes: `hook-rail` (the profile's envelope: x −447 to 447, y 470 to 490, z 300 to 380), `end-l`
(x −450 to −447, y 455 to 495, z 300 to 380), `end-r` (x 447 to 450).

## Materials by layer
`M-STEEL-7035` the rail and its end plates (painted steel, shelving-steel's layer).

## Decals (Blender)
No label: the one layer, `M-STEEL-7035`, is not a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. The rail is one box (894 × 20 × 80) less three cutboxes: the channel's opening (16 × 18 over
the floor), the room in front of the web under the floor (18 × 60) and the corner above the lip (2 × 5), which leave the web, the
floor and the lip as one solid of section 1600 − 288 − 1080 − 10 = 222 mm²; each end plate one box. Volume by hand (asserted in
element.py): the rail 894 × 222 = 198468 mm³; an end plate 3 × 40 × 80 = 9600; in all 217668 mm³. Every bounding-box extreme lies on
an end plate's uncut faces (x ±450, y 455 and 495, z 300 and 380). Not drawn: the bay, its uprights and shelves, the bins, any
fixing.

## Outputs (out/)
`rail-suspension-shelving-1000.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004080), our own design (mech-r161, unattended, 2026-11-13): a painted steel sheet 2.0 hook profile 20 × 80 between two end plates on the inner faces of shelving-steel 1.0's rear uprights, its open channel taking bins' rear hooks, its top 30 under the shelf above; every bay figure read from shelving-steel |
