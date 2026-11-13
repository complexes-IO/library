# bed-slat · v1.1 · slat bed 3100 × 1600 × 200 for a 3000 × 1500 sheet, 30 replaceable flat slats 2.5 × 100 at a 100 pitch

**What** A slat bed for thermal cutting: a welded frame of flat-bar rails round the cutting area, a support ledge inside each
long rail, and replaceable flat slats standing on the ledges, across the bed. The sheet lies on the slats' top edges; the beam
or arc cuts through the sheet between and into the slats, and the slag falls through between them. The fibre laser, sheet
laser and CNC plasma cutters of lib/machines-factory.txt carry a bed of this kind in their frame or shuttle table; a BOM places
the sheet on the bed's `slats`.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks bed-slat own_design
"yes"). No product was matched and no vendor file was opened. The bed has no hole, thread or standard interface; every size
is a design choice.
**Units / frame** mm, Z up. Origin: the frame's underside z = 0 at the bed's centre x = 0, y = 0; the bed's length along x; the
slats run across it along y. The slats' top plane, the sheet's seat, is at z = 200.
**Built with** toolkit 1.3 · AutoLISP command `BEDSLAT` · no parameters.

## Mechanism and the sheet's seat
`slats` (fixed): the 30 slats as one node. Its pivot is the centre of the slats' top plane (0, 0, 200) with the axis +z: a
sheet or workpiece is placed there, so a BOM row reads `<tag>.slats`. Nothing in the bed moves. A worn slat is lifted out of
the bed and a new one dropped in (each slat stands free on the two ledges, 2 clear of the long rails at each end); the twin
does not read it, so the node carries no travel.

## What it meets
| what | how |
|---|---|
| the machine's frame or shuttle table | the bed stands on its frame's underside (z = 0). How the machine locates and holds it (pins, stops, clamps, the shuttle's rails) belongs to that machine, so the bed has no hole for it |
| the sheet | lies on the slats' top edges at z = 200, 50 above the frame's top (z 150), so the sheet bears on the slats only |
| the slag tray or extraction under the bed | belongs to the machine: not built |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| inner opening | 3000 × 1500 (x −1500 to 1500, y −750 to 750) | the 3000 × 1500 sheet, the size the factory list's cutters take |
| frame rails | flat bar 50 thick, 150 high: two long rails the full 3100 length (y ±750 to ±800), two end rails 1500 long between them (x ±1500 to ±1550) | a welded frame, so the bed lifts out as one piece; not sized against a mass (no sheet or bed mass, no lifting point on file) |
| support ledges | 40 × 10 flat bar, 3000 long, inside each long rail (y ±710 to ±750), top at z 100 | the slats stand on them; 50 of the rail stays above the ledge to hold the slats' ends in line |
| slats | 30, flat, 2.5 thick, 100 high, 1496 long (y −748 to 748), centres at x −1450 to 1450 on a 100 pitch (the first and last 50 from the end rails), from z 100 to 200 | a thin slat takes the least of the beam's heat; the 100 pitch is a design choice, and the pitch for a given gauge comes with that machine's own version of the bed; 38 of each end bears on its ledge |
| slat ends | 2 clear of each long rail's inner face | the slat drops in and lifts out by hand |
| slats' top edge | plain, no teeth | a toothed (serrated or pointed) top edge is a later version, once a machine asks for it |
| welds, lifting eyes, a slat comb or slots in the rails | not drawn | the model shows the rails, ledges and slats |

## Named nodes
`slats` (fixed, above). Colliders `rail-a` and `rail-b` (the long rails), `end-a` and `end-b` (the end rails), and `slats`
(the slat field, slats and gaps between them).

## Materials by layer
`M-STEEL-7035` the frame rails and ledges (painted RAL 7035) · `M-SILVER` the slats (bare steel, shown in the library's
bright-metal layer).

## Notes
No load rating and no claim about the cutting process: no sheet mass, beam power or slat life is on file, so the bed is not
sized against them. Slat material, thickness and pitch for a given process (fibre laser or plasma, the sheet's gauge) come with
that machine's own version of the bed. No vendor names, no label.

## Outputs (out/)
`bed-slat.lsp` · `.glb` (pivot on `slats`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r54, unattended) |
| 1.1 | text only (mech-r63, review bed-slat-1.0 finding 1): the frame rails' and slats' "why" cells no longer claim what the bed carries or how stiff it is; both are design choices, not sized against a mass. Model unchanged |
