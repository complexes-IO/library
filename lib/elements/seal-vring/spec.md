# seal-vring · v1.0 · generic V-ring seal, NBR, for a 40 mm shaft

**What** an all-rubber V-ring seal: a ring stretched onto a rotating shaft (a pump's, a gearbox's, a motor's, a conveyor roller's), so
it grips the shaft and turns with it, while its conical lip runs against a counterface across the shaft (a housing's face, a bearing
cover, a shoulder). It keeps splash, dust and grit out of a bearing and the grease in: an axial seal, not a pressure seal; it holds no
fluid under pressure and claims none. A host that seals a shaft with it places the ring on the shaft; the default build is the ring
for a 40 mm shaft.
**Class** connector-part · **Baseline** our own design: generic V-ring seal (ETIM 10.0 EC010422), as OPERATING.md 12 (generic
elements, EM 2026-11-07) says: the next ETIM class in the Seals group's order that builds, after seal-tape-epdm's EC003185 (pneu-r104;
why the classes between them were passed over is in lib/rounds/pneu/r104.md section 2). No vendor file was opened or measured. The
class values below are its design inputs; its sizes are design choices; no vendor names; "generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic (O-rings among them). A V-ring's
section and its stretch on the shaft are fixed by no standard on file (lib/standards/sources.csv has none for it), unlike an O-ring's
(ISO 3601) or a rotary lip seal's (ISO 6194-1), so its sizes are the design's.
**Units / frame** mm, Z up. Origin: the centre of the body's back face (z = 0) on the shaft axis; the ring lies flat, its axis along
+z, the lip toward +z (toward the counterface).
**Built with** toolkit 1.3 · AutoLISP command `SEAL-VRING` · `shaft` (40; 30, 40, 50: the shaft diameter in mm it is made for).

## Class values (ETIM 10.0 EC010422)
Design inputs. EC010422 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, tube-pneu 1.0's and the three seal rolls' way). Until
they are on file this table gives the values this ring is designed to under plain names; a later minor restates them in ETIM's order
with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| material | NBR (nitrile rubber), black |
| shape | V-ring: a body gripping the shaft and a conical lip sealing axially against a counterface |
| shaft diameter | 40 mm (parameter `shaft`: 30 or 50) |
| inner diameter | 36 mm free, stretched onto the shaft (0.90 × the shaft) |
| outer diameter | 54 mm free (the lip's tip) |
| width | 11 mm free (body 5 + lip 6) |
| temperature range | not stated |
| max. circumferential speed | not stated |
| max. pressure | not stated: an axial splash and dust seal, not a pressure seal; it rates no pressure and claims none |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv: no check reads a V-ring's figure, and the shaft and housing it seals carry their own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| bore | 0.90 × the shaft: Ø36 for a 40 shaft (Ø27, Ø45 for 30, 50) | stretched about 11 % onto the shaft, the ring grips it and turns with it without a clamp; the design's choice (bore() in element.py) |
| body | 5 radial × 5 axial, from the bore out | the ring's grip on the shaft; the same section for the three shafts, a design choice |
| lip | two rings stepped outward over the body's front face: the root ring r +3.0 to +6.5 over the bore radius, 3 wide; the tip ring r +5.5 to +9.0, 3 wide | the lip's flare, drawn as two steps because the toolkit's primitives have no cone (an appearance, class C: the lip's true conical line is not drawn); each ring stands on the last face to face, and every wall is at least 3 so each edge passes the AutoCAD gate's fillet pre-flight (element.py asserts both) |
| outside | Ø54 × 11 wide for a 40 shaft (Ø45 × 11, Ø63 × 11 for 30, 50) | calculated from the bore and the section |
| mounting | not drawn | the counterface's distance and the lip's deflection on it belong to the host that places the ring; nothing places it yet |
| envelope | Ø54 × 11 (default) | the ring lies flat |

## Ports (toolkit/pneu.py)
None. The ring joins nothing: it sits on the host's shaft and seals against the host's face.

## Open figures
None. Every figure is a class value or a design choice above, or calculated from them.

## Named nodes
None. The ring turns only with the shaft that carries it; it has no moving part of its own.

## Materials by layer
`M-GASKET` the ring (black rubber)

## Decals (Blender)
None in 1.0. No vendor names.

## Outputs (out/)
`seal-vring.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010422), pneu-r104 (unattended): an NBR V-ring for a 30, 40 or 50 shaft, a 5 × 5 body on a bore 0.90 × the shaft and a lip drawn as two rings stepped outward; parameter `shaft`; no port, no node, no ratings |
