# carriage · v1.0 · lathe carriage 400 × 600 × 380, two shoes on bed-cast's ways, apron, cross slide 200 × 220 with 200 of travel

**What** The carriage of a conventional lathe (lib/machines-factory.txt: lathe-conventional places bed-cast, headstock,
tailstock, carriage, leadscrew and tool-post): the part that runs along the bed and carries the tool. Two way shoes sit on
bed-cast's two flat ways and carry a saddle plate across the bed; an apron hangs from the saddle's front edge in front of the bed;
the cross slide on the saddle's top face moves across the bed and carries the tool post. A BOM places the tool post on the
carriage's `cross-slide`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks carriage own_design
"yes"). No product was matched and no vendor file was opened. The shoes' spacing and width come from bed-cast 1.0; every other
size is a design choice.
**Units / frame** mm, Z up. Origin: bed-cast's ways' top plane z = 0 (the carriage's seat) at the carriage's centre x = 0, y = 0;
the carriage slides along x, the bed's length; front (the operator's side, where the apron hangs) toward −y. The cross slide's top
face, the tool post's seat, is at z = 160.
**Built with** toolkit 1.3 · AutoLISP command `CARRIAGE` · no parameters.

## Mechanism
`cross-slide` (translate, axis +y, 0 to 200 mm): the cross slide. At rest (0) it stands fully toward the operator, y −240 to −20;
at 200 it stands at y −40 to 180. Its pivot is the centre of its top face at rest, (0, −130, 160): the tool post element is
placed there with its own base origin, so a BOM row reads `<tag>.cross-slide` and the tool post moves with the slide. The slide
sits on the saddle's top face (z 100) through its whole travel and stays inside the saddle's y −280 to 280; MOT-010 sweeps it.
The carriage's travel along the bed (x) is the machine's, between the elements (its leadscrew, a placed element), so the carriage
has no node for it, as saddle and gantry-beam.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the bed's ways | two flat ways 80 wide, centres at y ±170 (340 apart), their top plane the carriage's seat | bed-cast 1.0 (`WAY_W`, `WAY_Y`, read by library.load("bed-cast")); its seat at z = 430 above the floor |
| the bed's body | 500 wide (y ±250), its top 400 above the floor; base plate 660 wide, 25 thick | bed-cast 1.0 (spec.md, element.py): what the saddle and apron must clear |

Placed on bed-cast at (x, 0, 430), the shoes cover the bed's ways exactly in y; the saddle plate (from z 40, 470 above the floor)
stands 70 over the bed's body; the apron's back face (y −280) stands 30 in front of the body's front face (y −250), and its
underside (210 above the floor) 185 over the base plate. The carriage's x travel on the bed is the machine's: from bed-cast's
1960 long ways and the shoes' 300, at most 1660 with the shoes fully on the ways; the headstock and tailstock on the same ways
take their own share of it.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| way shoes | 2, 300 × 80 × 40 (x ±150, z 0 to 40), at y ±170 | one on each of bed-cast's ways, as wide as the way; 300 along the bed is a design choice |
| saddle plate | 300 along the bed (x ±150), 560 across (y −280 to 280), 60 thick (z 40 to 100) | a design choice: it spans both ways and overhangs the bed's 500 body by 30 at each side |
| apron | 400 along the bed (x ±200), 40 thick (y −320 to −280), from z −220 to the saddle's top (z 100) | a design choice: the plate in front of the bed that would carry the handwheels and the leadscrew's nut; drawn by its outside |
| cross slide | 200 along the bed (x ±100), 220 across (y), 60 high (z 100 to 160) | a design choice |
| cross slide travel | 200 along +y from its rest at the operator's side | a design choice within the saddle's 560; whether a tool post on it reaches a given work diameter is checked when the tool post and tailstock elements are on file |
| saddle, apron | drawn by their outsides: cores, ribs and the apron's gear box are not seen | the model shows what can be seen |
| the apron's gears, handwheels, half nut, the cross slide's screw, dovetail and gib, the compound rest, way wipers | not drawn | they belong to the machine's own version, or to later elements (leadscrew, tool-post) |

## Named nodes
`cross-slide` (translate, above). Colliders `carriage` (the shoes and the saddle plate, the space between the shoes included) and
`apron`; neither is named like a node. The moving slide has no collider of its own.

## Materials by layer
`M-STEEL-7035` the shoes, saddle plate and apron (painted RAL 7035) · `M-SILVER` the cross slide (bare machined steel, the
library's bright-metal layer, as bed-cast's ways).

## Notes
No load rating, no stiffness or accuracy claim: no machine's mass, cutting forces or way tolerances are on file, so the carriage
is not sized against them. The volume is 19 760 000 mm³ (shoes 2 × 960 000, saddle plate 10 080 000, apron 5 120 000, cross
slide 2 640 000; written as volume only: lib/materials.csv gives steel no density, so no mass is stated). No hole: the tool
post's fixing (a T-slot), the leadscrew's nut and the gib screws come with the parts they hold (OPERATING.md 12: a host doesn't
model holes for a part it places later). No vendor names, no label.

## Outputs (out/)
`carriage.lsp` · `.glb` (pivot on `cross-slide`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r67, unattended) |
