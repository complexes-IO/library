# clamp-girder-200 · v1.0 · beam clamp (girder clamp), generic, for an I-beam's bottom flange 200 x 20, two painted steel C-jaws, the +y jaw wound out 0 to 40, load plate with a Ø30 eye

**What** A beam clamp for the workshop: it grips the bottom flange of an I-beam and gives a fixed point under it to hang a chain hoist
from. Two painted steel C-jaws 80 wide hook over the flange's edges, their lips bearing on the flange's top face; a plain bright-steel
spindle Ø20 runs across under the flange through Ø22 bores in both jaws' lower parts and through a load plate 20 thick hanging midway
between them, whose Ø30 eye takes the hoist's hook or shackle. A T-handle on the spindle's +y end turns it. The -y jaw stays on the
spindle; the +y jaw (node `jaw`) is wound out along +y to pass the flange's edge when the clamp is fitted or taken off, and wound in to
grip.
**Class** furniture · **Baseline** our own design: generic beam clamp for workshop (ETIM 10.0 EC004751 Beam clamp for workshop),
OPERATING.md 12 "Generic elements" (EM, 2026-11-07). No inventory row names it: group EG010320 Lifting equipment is walked by name from
lib/toolkit/generic.py's mech order after group EG010340 (lib/rounds/mech/r171.md), and EC004751 is a class not yet built; its shape no
dimensional standard on file fixes. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: beam-runway's frame: the flange's underside z = 0 on the beam's centre line y = 0, the clamp's middle
x = 0; the beam's length along x; the jaws' lips rest on the flange's top face z = 20. A host places it at the beam's own origin moved
along x, where no trolley runs. Extents x -40 to 40, y -134 to 184 (the spindle's ends), z -120 to 36.
**Built with** toolkit 1.3 · AutoLISP command `CLGIR200` · no parameter · places no element; reads beam-runway 1.1 (library.load:
FLG_W, FLG_T, WEB_T).

## Class values (ETIM 10.0 EC004751)
Design inputs. EC004751 Beam clamp for workshop (lib/standards/etim/classes.csv: group EG010320 Lifting equipment, tier 2, 3 features,
synonyms Beam clamp, Beam lifting clamp, Chain hoist flange clamp, Girder clamp, Scissor clamp) is a class whose features
lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they are on file this table gives the
values the clamp is designed to under plain names, as ramp-loading-150 1.0 does (requests mech-8 and mech-9, the core's answers); a
later minor version restates them in ETIM's order with their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | steel: the jaws and the load plate painted (the `M-YELLOW` layer), the spindle bright (`M-SILVER`); the grades not stated |
| flange width | 200 (one size: beam-runway 1.1's bottom flange) |
| flange thickness | 20 |
| adjustment | the +y jaw wound out 0 to 40 along the spindle |
| suspension point | an eye Ø30 in the load plate, its centre 95 under the flange's underside |
| load capacity (working load limit) | not stated (no load claim) |

No ratings.csv: no rating the checks read, and no load, proof load or mass figure is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the beam's bottom flange | 200 wide (y -100 to 100), 20 thick (z 0 to 20) | beam-runway 1.1 (FLG_W, FLG_T, read with library.load; asserted in element.py) |
| the beam's web | 20 thick (y -10 to 10) on the flange's top | beam-runway 1.1 (WEB_T): the lips' inner edges at y ±76 stay 66 clear of it |
| the hoist | its hook or shackle in the Ø30 eye | design: no hoist element is on file, so none is read; no load is claimed |

beam-runway's bottom flange is also its trolley's running track (node `track`): a host clamps this element where no trolley runs, or on
a beam of the same flange used as a fixed beam.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| jaws | 80 wide (x -40 to 40), 48 across (y ±76 to ±124), 96 high (z -60 to 36) at rest, each a C open toward the beam | one box less one cut each |
| side walls | 16 thick, their inner faces y ±108, 8 clear of the flange's edges | room to fit the clamp over a flange edge that is not dead straight |
| lips | 16 thick on the flange's top (z 20 to 36), 24 in from its edges (to y ±76) | they carry the load onto the flange's top face |
| opening | y ±76 to ±108, z -24 to 20 | the flange (20) and 24 clear under it |
| lower parts | 36 deep (z -60 to -24) | the spindle's bore in their middle, 7 of wall round it |
| spindle | Ø20 plain, y -134 to 184 on the axis x 0, z -42 | drawn plain: its thread is not modelled and no thread is claimed |
| bores | Ø22 in both jaws and in the load plate | 1 clear all round the spindle |
| travel | the +y jaw 0 to 40 along +y | wound out, its lip's inner edge (y 116) clears the flange's edge (100) by 16 |
| load plate | 80 x 20 x 100 (y -10 to 10, z -120 to -20) on the spindle midway | 20 under the flange; 11 of plate over its bore |
| eye | Ø30 along y at z -95 | 10 of plate under it, 31 between it and the bore |
| T-handle | Ø12 x 80 along z at y 176 | 6 clear of the +y jaw wound fully out (its outer face y 164) |

## Mechanism
Node `jaw` (the +y C-jaw with its bore), translate along +y, 0 to 40 mm, pivot at its lip's inner lower edge (0, 76, 20). At 0 (the
default, "gripping") its lip lies 24 over the flange's top; at 40 ("open") it clears the flange's edge by 16. The spindle that drives it
turns by hand; the twin sets the jaw as the operator's input (behaviour.csv: states gripping / open, one pose row). The -y jaw, the load
plate, the spindle and the handle are the fixed body.

## Named nodes
`jaw` (translate +y, 0 to 40). Colliders (fixed parts only, boxes): `jaw-fixed` (the -y jaw's outline), `load-plate`, `spindle` (the
spindle's bounding box, y -134 to 184).

## Materials by layer
`M-YELLOW` the jaws and the load plate (painted steel, beam-runway's colour; no marking claim) · `M-SILVER` the spindle and the T-handle
(bright steel).

## Decals (Blender)
No label: neither `M-YELLOW` nor `M-SILVER` is a printed layer of the Blender gate (its default printed layers are `M-WHITE-PA` and
`M-BLACK-PA`; review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. Drawn as two boxes less one cut and one bore each (the jaws), one box less two bores (the load
plate) and two cylinders (the spindle and the handle crossing it). Volume by hand (asserted in element.py): a jaw 80 × 48 × 96 less its
opening 80 × 32 × 44 less its bore Ø22 × 48, 237753.6 mm³; the load plate 80 × 20 × 100 less its bore Ø22 × 20 and its eye Ø30 × 20,
138260.2 mm³; so 613767.4 mm³ painted. Every bounding-box extreme lies on an uncut face: x ±40 the jaws' and the plate's sides, y -134 and
184 the spindle's ends, z -120 the load plate's underside, z 36 the jaws' tops. No mass is stated: lib/materials.csv gives no density.
Not drawn: the spindle's thread and its nut in the moving jaw, the load plate's centring spacers, the spindle's retention, a hoist.

## Outputs (out/)
`clamp-girder-200.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004751), our own design (mech-r171, unattended, 2026-11-13): beam clamp for beam-runway 1.1's bottom flange 200 × 20, two painted steel C-jaws 80 wide (the +y jaw a translate node 0 to 40), plain spindle Ø20 through Ø22 bores, load plate with a Ø30 eye 95 under the flange |
