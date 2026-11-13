# box-assortment-340x240 · v1.0 · assortment box for small parts, empty, generic, grey plastic case 340 × 240 × 50 with 12 fixed compartments, clear lid hinged at the rear top edge, 0 to 110 degrees

**What** An empty assortment box for small parts (screws, nuts, washers, terminals, ferrules) kept on a bench, in a drawer or on a
shelf: a grey plastic case 340 wide, 240 deep and 50 high, walls and bottom 2.0, divided into twelve fixed compartments, four across
and three deep, each 82.875 × 77.667 inside, by 1.5 dividers that stand on the bottom and stop 2 under the rim. A clear plastic lid 2.0
lies on the rim and turns up about the case's rear top edge, 0 to 110 degrees, so the compartments are seen through it when shut and
reached from the front when open. The dividers stop under the rim, so the lid closes on the rim alone. The hinge knuckles and the catch
are not modelled: the lid's turn is about the rear top edge itself. The box stands on its own and meets no element on file.
**Class** furniture · **Baseline** our own design: generic assortment box, empty (ETIM 10.0 EC003616), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07). No inventory row names it: group EG010340 Storage and racking systems is walked by name from
lib/toolkit/generic.py's mech order (lib/rounds/mech/r158.md), and EC003616 is a class not yet built; its shape no dimensional standard
fixes. No product was matched and no vendor file was opened.
**Units / frame** mm, Z up. Origin: the case's underside z = 0 at its front-left corner x = 0, y = 0; the width along +x, the depth
along +y. The lid's hinge line is the case's rear top edge (y 240, z 50); it opens upward toward the back. Extents x 0 to 340, y 0 to
240, z 0 to 52 (the lid shut).
**Built with** toolkit 1.3 · AutoLISP command `BOXASRT` · no parameter.

## Class values (ETIM 10.0 EC003616)
Design inputs. EC003616 Assortment box empty (lib/standards/etim/classes.csv: group EG010340 Storage and racking systems, tier 2, 4
features) is a class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Until they
are on file this table gives the values the box is designed to under plain names, as basin-bulk-shelving-440 1.0 and
wall-side-shelving-500 1.0 do (requests mech-8 and mech-9, the core's answers); the next minor version restates them in ETIM's order with
their EF codes, "not stated" where the design has no value (lib/needs-em/mech.md).

| value | this element |
|---|---|
| material | plastic: the case grey (`M-GREY-PA`), the lid clear (`M-CASE-CLEAR`); the grade not stated |
| outside size | 340 wide × 240 deep × 52 high with the lid shut (the case 50, the lid 2.0) |
| compartments | 12, fixed: 4 across × 3 deep, each 82.875 × 77.667 inside and 46 deep (the dividers' height) |
| lid | clear, hinged at the rear top edge, opens 0 to 110 degrees |
| contents | none (an empty box) |
| capacity | not stated (no load or volume of goods is claimed) |

No ratings.csv: no rating the checks read, and no load figure is claimed.

## What it meets
Nothing on file: it stands on any flat face (a bench top, a shelf, a drawer's bottom) by its own weight. No fixing is drawn and no
hole is modelled.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| case | 340 × 240 × 50 | a box carried in one hand, set two deep on a 500 shelf |
| walls and bottom | 2.0 | a moulded case's wall; under 3, so every wall edge is thin to the gate's fillet check |
| compartments | 4 × 3, the dividers 1.5 thick | twelve sorts of small parts; every compartment's side 77 or more, so a hand's fingers reach the bottom |
| dividers' height | 46, from the bottom (z 2) to 2 under the rim (z 48) | the lid closes on the rim alone and never on a divider |
| lid | 2.0, clear, the whole top | the compartments are seen with the lid shut |
| lid's turn | 0 to 110 degrees about the rear top edge | past upright, so it stays open by its own weight leaning back; at every angle the lid lies behind the back wall's outer face (y 240) or above the rim (z 50) |
| folds and corners | drawn sharp (one box less one cutbox) | no moulding radius or draft is claimed |

## Mechanism
One moving node, `lid`: rotate about the x axis through (170, 240, 50), the case's rear top edge, range 0 to −110 degrees (0 shut on the
rim; a negative angle turns the lid's front edge up and over toward the back). Turned by hand (behaviour.csv: `shut` default, `open`
manual toggle, pose at the range's end). The case and its dividers are the fixed body. No hinge knuckle, catch or lock is modelled, so
there is no latched state.

## Named nodes
`lid` (the clear lid plate). Two colliders, axis-aligned boxes named apart from the node: `case` (x 0 to 340, y 0 to 240, z 0 to 50) and
`lid-plate` (x 0 to 340, y 0 to 240, z 50 to 52, on the node).

## Materials by layer
`M-GREY-PA` the case and its dividers (grey plastic) · `M-CASE-CLEAR` the lid (clear plastic).

## Decals (Blender)
No label: neither layer, `M-GREY-PA` nor `M-CASE-CLEAR`, is a printed layer of the Blender gate (review mech-r125 finding 2's reading).

## Notes
No vendor names, part numbers or marks. The case is drawn as one box (340 × 240 × 50) less one cutbox from the top (336 × 236 inside it,
from 2.0 above the bottom up through the rim), which leaves the bottom and the four walls as one solid. The three long dividers run the
inside's whole depth, front wall to back wall; the eight cross dividers stand between two long dividers or a long divider and a side
wall, so no two dividers overlap (each meets the next face to face). Volume by hand (asserted in element.py): the case 4080000 −
336 × 236 × 48 = 4080000 − 3806208 = 273792 mm³; the long dividers 3 × 1.5 × 236 × 46 = 48852 mm³; the cross dividers 8 × 82.875 × 1.5
× 46 = 45747 mm³; the fixed body 368391 mm³; the lid 340 × 240 × 2.0 = 163200 mm³. Every bounding-box extreme lies on a face the cutbox
leaves whole (x 0 and 340 on the side walls' outer faces, y 0 and 240 on the front and back walls', z 0 on the bottom) or on the lid's
top face (z 52). Not drawn: the hinge knuckles, the catch, any label, the parts the box holds.

## Outputs (out/)
`box-assortment-340x240.lsp` · `.glb` (`-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC003616), our own design (mech-r158, unattended, 2026-11-13): a grey plastic case 340 x 240 x 50, walls and bottom 2.0, twelve fixed compartments (4 x 3) from 1.5 dividers stopping 2 under the rim, a clear lid 2.0 turning 0 to 110 degrees about the rear top edge; meets no element on file |
