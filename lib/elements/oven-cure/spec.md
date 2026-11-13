# oven-cure · v1.1 · powder cure oven, batch, outside 2400 × 3200 × 2400, insulated panels 100, door opening 1800 × 2100, roof circulation housing, exhaust Ø150

**What** The body of a batch powder cure oven: parts coated in the powder booth are rolled in on a cart, the door is closed and
the powder is cured by hot air circulated through the oven. Two side walls, a back wall, a front wall and a roof of insulated
panels stand on the floor; the front wall has the door opening at floor level. On the roof at the back stands the circulation
housing, over two openings in the roof (return and supply), where the circulation fan and the heaters go; on the roof at the
front, an exhaust collar. The door, the fan, its motor and the heaters are other elements of the inventory (door-oven,
fan-circulation, motor-iec, heater-oven), placed by the system; this element draws none of them. The systems of
lib/machines-factory.txt that list it (oven-cure and powder-coating-system) place it with them.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks oven-cure own_design
"yes", "powder cure oven (insulated panels)"). No product was matched and no vendor file was opened. Every size is a design
choice.
**Units / frame** mm, Z up. Origin: the floor z = 0 under the middle of the door opening, in the front wall's outer face; x = 0
across the oven's width, y = 0 the front wall's outer face, the oven toward +y. Extents x ±1200, y 0 to 3200, z 0 to 3000 (the
housing's top).
**Built with** toolkit 1.3 · AutoLISP command `CUREOVEN` · no parameters.

## Mechanism
None: the body has no moving part. The door is door-oven's, a later element, with its own hinge or lift; the twin reads nothing
here.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the floor | the four walls and nothing else stand on z = 0; the oven has no floor panel, so a cart rolls in at floor level | its fixing to the floor and the floor's own insulation are where a BOM places it (no anchor in this element) |
| the door (door-oven) | the opening 1800 wide × 2100 high (x ±900, z 0 to 2100) in the front wall (y 0 to 100); the door covers it from the front face y = 0 | door-oven is not built yet: the opening is modelled and the door placed in a later version (OPERATING.md 12, own designs) |
| the fan, motor and heaters | inside and on the circulation housing, over the return opening (x −500 to −100) and the supply opening (x 100 to 500) | fan-circulation, motor-iec and heater-oven are the system's; not drawn |
| the exhaust duct | Ø150 bore of the collar on the roof, axis at (0, 600), the collar's top at z 2600 | a design choice (features.csv kind `own`): the duct and its clamp are the system's |
| the parts cured | through the door opening, on a cart; the inside is 2200 wide, 3000 deep, 2300 high | the cart and the hangers are the system's |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| oven | 2400 wide (x ±1200), 3200 deep (y 0 to 3200), 2400 high, outside | a batch oven for a cart of parts from the powder booth (booth-powder's work opening is 1200 × 1000) |
| panels | 100 thick, drawn by their outside: side walls x ±1100 to ±1200 under the roof, roof z 2300 to 2400 across them, front wall y 0 to 100 and back wall y 3100 to 3200 between them | an insulated panel of two skins and the insulation between, shown as one solid; the skins, the insulation, its grade and the panel joints are not drawn |
| inside | 2200 × 3000 × 2300 (x ±1100, y 100 to 3100, z 0 to 2300) | 2200 × 3000 × 2300: a design choice; whether a cart and the air gap round it fit is checked when the cart is on file |
| door opening | 1800 × 2100, at floor level, centred | the cart's way in; door-oven's frame laps it |
| circulation housing | 1400 × 1200 × 600 (x ±700, y 1900 to 3100, z 2400 to 3000), a top and four sides of 50 thick panels, the roof its floor; inside 1300 × 1100 × 550 | the fan and the heaters' place, on the roof at the back, outside the work space |
| return and supply openings | two, 400 × 800 through the roof under the housing (x −500 to −100 and 100 to 500, y 2100 to 2900) | the air goes up through one and down through the other; the ducts and baffles inside the oven are the fan's later version |
| exhaust collar | Ø150 bore, 2.0 wall (Ø154 outside), 200 high (z 2400 to 2600), on the roof at the front (axis x 0, y 600), through a Ø150 opening in the roof | the oven's exhaust connection |
| door, fan, motor, heaters, floor, frame, controls | not drawn | other elements of the inventory and the system's; the twin reads none of them here |

## Where it stands (the system's)
The cure temperature, the insulation's thermal value and the outside skin temperature, the heat input and the air rate, the
exhaust rate that keeps the solvent and powder vapours down, and the fire and explosion protection of an oven are figures of the
system and its standards, none of which is on file (lib/standards/sources.csv lists no oven standard). This element makes no
temperature, thermal, airflow, fire, explosion or safety claim and names no such figure; the system that places it cites them
when they are on file.

## Named nodes
None. Colliders `roof`, `wall-l`, `wall-r`, `wall-back`, `jamb-l`, `jamb-r`, `lintel` (the front wall round the opening, which
stays clear), `housing`, `stack`.

## Materials by layer
`M-STEEL-7035` the panels and the circulation housing (painted sheet skins, light grey). `M-GALV` the exhaust collar
(galvanised).

## Notes
No load rating and no safety claim. No vendor names, no label. The door (door-oven), a conveyor oven with end openings and the
inside ducts and baffles are later elements or versions.

## Outputs (out/)
`oven-cure.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r64, unattended) |
| 1.1 | text only, the part unchanged (mech-r73, unattended; review mech-r64 finding 1): the inside's "why" cell written as a design choice, with no fit claimed for a cart or air gap not on file |
