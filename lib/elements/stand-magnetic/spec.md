# stand-magnetic · v1.1 · magnetic indicator stand, switchable base 50 × 60 × 55 with on/off lever, post Ø12 × 200, swivel arm Ø10 on the post's top reaching 185, clamp block with Ø8 bore for the indicator's stem

**What** A magnetic indicator stand: a switchable magnetic base that holds on a steel face (a machine bed, a column, a
workpiece), a post standing on it, and an arm that swings on the post and carries a dial indicator at its end, so the
indicator's stem can be brought to the work for tramming, run-out and alignment checks. The model shows the base block, its
on/off lever (node `switch`), the post, and the arm (node `arm`: a square hub on the post's top, a round boom, a clamp block
with a vertical bore for the indicator's stem). lib/machines-factory.txt lists it with dial-indicator (the dial-indicator row:
the indicator and its stand); the indicator is a separate element, not built yet, and is not placed. The switch and the arm are
the mechanism: the twin sets them by name.
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks stand-magnetic own_design
"yes", "magnetic indicator stand"; request mech-8's answer: no ETIM class on file fits, so an own design as panel-clamp). No
product was matched and no vendor file was opened. Every size is a design choice but one: the clamp bore's fit to the
indicator's stem is a figure a standard tabulates (ISO 463, not on file: class B, source wanted, What it meets).
**Units / frame** mm, Z up. Origin: the base's underside (the pole face that seats on the work) z = 0, on the post's axis
x = 0, y = 0; the base's long sides run along y. The switch lever stands on the −x end face, up at rest (off); the arm points
along +x at rest and turns about z. Extents x −45 (the lever) to 185 (the clamp block), y ±30 (the base), z 0 to 280 (the hub).
**Built with** toolkit 1.3 · AutoLISP command `STANDMAG` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| the work | the base's underside (z = 0, 50 × 60) and its −y side face (60 × 55): the pole faces, flat | a flat steel face of the machine or workpiece; where it stands is the assembly's. The magnet, its rotor and the switch's internals are not drawn and no holding force is claimed |
| the dial indicator | the clamp block's bore along z at x 175, through 24 of block (z 255.5 to 279.5), 10 from the block's faces; drawn Ø8 | **NOT ON FILE (B)**: the indicator stem's diameter and tolerance the bore meets: ISO 463 (mechanical dial gauges; DIN 878 and JIS B 7503 nationally). The stem is a fit that standard tabulates, so the figure is a source wanted (OPERATING.md 6 and 12; review stand-magnetic-1.0 finding 1, mech-r94 finding 1), not this design's: the bore is drawn Ø8 until the document is on file, and then the clamp's fit to the stem is read from it (a later version if the figure differs). The clamp screw is not drawn. dial-indicator is not built (inventory row, generic); when it is, its stem meets this bore (features.csv, kind own) |
| the operator | the lever on the knob (the switch) and the arm's hub (the swivel) | by hand; no torque or force figure |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base block | 50 × 60 × 55 (x ±25, y ±30, z 0 to 55) | a block a hand spans, long along y so the −y side face is a second pole face; the post on its centre |
| on/off knob and lever | knob Ø22 × 12 proud of the −x end face on an axis along x at z 30 (x −37 to −25); lever 8 × 6 × 22 on the knob's outer face, from the axis up to z 52 at rest | the knob turns the magnet's rotor (not drawn); the lever gives the hand a grip and shows the state: up is off, turned down 90 degrees is on. The lever's edges are 6 and over, so the fillet gate rounds them |
| post | Ø12, from the base's top (z 55) to z 255 (200 long), on the base's centre | a plain round post; the arm swivels on its top |
| hub | 30 × 30 × 25 (x, y ±15, z 255 to 280) on the post's top face | square, so the hand can turn it; it carries the boom at its mid-height and is the model's z extreme (an axis-aligned box of a top-level node) |
| boom | Ø10 along +x from the hub's +x face (x 15) to x 165, axis z 267.5 | 150 of plain round arm |
| clamp block | 20 × 20 × 24 (x 165 to 185, y ±10, z 255.5 to 279.5) on the boom's end face | its faces 0.5 inside the hub's top and bottom planes, so no face is coplanar with the hub's; carries the Ø8 bore for the indicator's stem; the model's x extreme |
| swing | the arm −180 to 180 degrees about the post's axis; the lever 0 to 90 about the knob's axis | a full turn each way on the post; a quarter turn for the switch |
| layers | base M-STEEL-7035 (painted steel); post, hub, boom and block M-SILVER (bright steel); knob and lever M-BLACK-PA (moulded) | a design choice, no finish claim |

## Mechanism
`switch` (the knob and its lever; rotate about the knob's axis, along x through (−25, 0, 30), 0 to 90 degrees): 0 is off,
as built, the lever up; 90 is on, the lever turned down toward −y. The lever sweeps a quarter circle of radius 22 beside the
base's −x end face, meeting nothing: the base starts at x −25 and the lever lies at x −45 to −37. The magnet's rotor it turns
is not drawn (internal mechanism the twin doesn't read); the holding force is not on file and not claimed.
`arm` (the hub, the boom and the clamp block; rotate about z through (0, 0, 255), −180 to 180 degrees): 0 is the boom along
+x, as built. The hub rests face to face on the post's top (z 255) and turns on it; the boom and block stay at z 255.5 to 280,
200 above the base's top, so the arm meets nothing through its full turn. The hub's clamp on the post, the elbow and fine
adjuster a stand may have, and the clamp screw at the block are not drawn: this is the plain stand, one swivel.
behaviour.csv: `off` (default) and `on` (manual toggle) for the switch, `home` (default) and `swung` (manual toggle) for the
arm, a pose row each at the range end. MOT-010 sweeps both nodes through their ranges.

## Named nodes
`switch`: rotate about x through (−25, 0, 30), range 0 to 90 degrees; `arm`: rotate about z through (0, 0, 255), range −180 to
180 degrees. Colliders, axis-aligned boxes: `base` (the base block), `post`, `lever-knob` (the knob and lever at rest), `boom`
(the arm at rest: hub, boom and clamp block). None is named like a node.

## Materials by layer
`M-STEEL-7035` the base block (painted steel, RAL 7035) · `M-SILVER` the post, hub, boom and clamp block (bright steel) ·
`M-BLACK-PA` the knob and its lever (moulded). The layer names say the colour and the kind of material shown; no grade is
claimed.

## Decals (Blender)
"complexes.org" on the base's +y side face.

## Notes
No vendor names, part numbers or marks. No holding force, no load, no deflection or accuracy claim: no magnet is sized and no
calculation or test of the model is on file. Not drawn: the magnet and its rotor, the switch's internals, the base's V groove
for round work, the hub's clamp on the post, an elbow joint and a fine adjuster, the clamp screw at the block, the dial
indicator. One open figure, class B (What it meets): the indicator stem's diameter and tolerance the clamp bore meets, a
figure ISO 463 tabulates; the document is asked for once in lib/standards/wanted.md and the element waits as "source wanted"
(not EM's page). Every other size is a design choice.
Gate note (mech-r92's and r93's lessons): the bounding box's extremes lie on axis-aligned solids of top-level nodes (the lever
box at x −45, the clamp block at x 185, the base at y ±30 and z 0, the hub at z 280); no node is nested.

## Outputs (out/)
`stand-magnetic.lsp` · `.glb` (pivots on `switch` and `arm`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r94, unattended, 2026-11-11) |
| 1.1 | text only (mech-r100, unattended, 2026-11-11): the clamp bore's fit to the indicator's stem marked class B, source wanted (ISO 463), in What it meets, features.csv and element.py, where 1.0 called it a design choice (review stand-magnetic-1.0 finding 1; mech-r94 finding 1, the ESCAPE). Nodes, origin, sizes and cut-outs unchanged |
