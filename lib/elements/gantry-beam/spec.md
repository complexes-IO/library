# gantry-beam · v1.1 · gantry beam 2200 × 200 × 300 on two end saddles 250 × 400 × 30, two flat front ways 40 high, 1600 long

**What** A gantry beam: the cross beam that carries the cutting head's axis across the bed. A welded box-section beam on a
saddle plate at each end, with two flat machined ways along its front face. The fibre laser, sheet laser and CNC plasma cutters
of lib/machines-factory.txt carry their head on a beam of this kind; the machine's side carriages carry the beam along the bed
on its saddles, and a BOM places the head carriage on the beam's `ways`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks gantry-beam own_design
"yes"). No product was matched and no vendor file was opened. The beam has no hole, thread or standard interface; every size
is a design choice.
**Units / frame** mm, Z up. Origin: the saddles' underside z = 0 at the beam's centre x = 0, y = 0; the beam's length along x;
front (the ways) toward −y. The ways' front plane, the head carriage's seat, is at y = −115.
**Built with** toolkit 1.3 · AutoLISP command `GANTRYBEAM` · no parameters.

## Mechanism and the head carriage's seat
`ways` (fixed): the two flat ways. Its pivot is the centre of the ways' front plane (0, −115, 180) with the axis −y: a head
carriage element is placed there with its own base origin and moves along x on its own nodes, so a BOM row reads
`<tag>.ways`. The beam itself has no moving part; its own travel along the bed belongs to the machine's carriages.

## What it meets
| what | how |
|---|---|
| the machine's side carriages | the beam stands on its two saddles' undersides (z = 0, x ±850 to ±1100). How a carriage locates and holds a saddle (pins, bolts, keys) belongs to that machine, so the saddles have no hole for it |
| the head carriage | sits on the ways' front plane (y = −115) and moves along x on its own nodes. The guide it runs on (flat ways, or profile rails and their carriages) comes with that machine's own version of the beam |
| bed-slat 1.0 | the beam's 2200 length spans the bed's 1600 width; the saddles' inner edges (x ±850) stand 50 outside the bed's long rails (±800) when the beam's x lies along the bed's y |
| the drive (rack, belt or screw), cable chain, covers | belong to the machine: not built |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| beam | box section 200 deep (y −100 to 100) and 300 high (z 30 to 330), 2200 long (x −1100 to 1100) | a closed box section for the 1500-wide cutters of the factory list; 300 high carries two ways 200 apart |
| saddles | 250 along the beam, 400 across it (y −200 to 200), 30 thick (z 0 to 30), one under each end, flush with the beam's ends (x ±850 to ±1100) | 100 each side of the beam to seat on a carriage |
| ways | 2, flat, 40 high, 15 proud of the beam's front face (y −100 to −115), centres at z 80 and 280 (200 apart), from x −800 to 800 | flat ways carry a head carriage on both; 1600 long, 300 short of each end: a design choice. The head's stroke over the sheet depends on the head carriage's length, and no carriage is on file, so the ways are not sized to a reach; that belongs to the machine's own version of the beam |
| body | drawn by its outside: a welded box section is closed at its ends, its webs and ribs are not seen | the model shows what can be seen |
| webs, ribs, scraping of the ways, the drive, cable chain, covers, lifting eyes | not drawn | they belong to the machine that is built on the beam |

## Named nodes
`ways` (fixed, above). Colliders `saddle-a` and `saddle-b` (the end saddles), `beam` (the box beam) and `ways` (the two ways and
the gap between them).

## Materials by layer
`M-STEEL-7035` the saddles and beam (painted RAL 7035) · `M-SILVER` the ways (bare machined steel, shown in the library's
bright-metal layer).

## Notes
No load rating, no stiffness, deflection or accuracy claim: no head mass, acceleration or way tolerance is on file, so the beam
is not sized against them. The guide profile a given machine needs and how its carriages hold the saddles come with that
machine's own version of the beam. No vendor names, no label.

## Outputs (out/)
`gantry-beam.lsp` · `.glb` (pivot on `ways`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r55, unattended) |
| 1.1 | text only (mech-r63, review gantry-beam-1.0 finding 1): the ways' 1600 is a design choice, no longer justified by the head's reach (no head carriage on file); the title says the ways are 40 high, as the body and the model have them. Model unchanged |
