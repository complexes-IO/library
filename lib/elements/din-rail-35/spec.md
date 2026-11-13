# din-rail-35 · v1.1 · 35 × 7.5 top-hat DIN rail

**What** Mounting rail for every DIN-clip device in the set (breakers, supply, contactor, relays, terminals, I/O block): 35 × 7.5 top-hat section to EN 60715 (TH35-7.5), slotted, zinc-plated steel, cut to length, with two screw-type end clamps and M5 panel screws.
**Class** rail · **Baseline** EN 60715 TH35-7.5 section, the common perforated pattern (6.2 × 18 slots at 25 pitch). A standard, so no vendor file; the terminal's comparison is against the EN figure.
**Units / frame** mm, Z up. Origin: on the panel (back face), the centre of the first slot. The rail runs +x; its 35 mm height is along z (horizontal rail on a vertical panel); the crown stands 7.5 toward −y. For a vertical rail, place with yaw 0 and the rail still runs +x — rotate the host instead; a vertical-rail variant is a later parameter.
**Built with** toolkit 1.3 · AutoLISP command `RAIL` · parameters `length` (1000), `clamps` (true), `fix_pitch` (200: panel screws at the nearest slot every 200).

## Dimensions
| item | value |
|---|---|
| section | 35 overall × 7.5 deep, crown 27 wide, flanges 4 each side, 1.0 sheet |
| slots | 6.2 × 18 on the crown centre line, 25 pitch, first centre 12.5 from the end; as many as fit |
| end clamps | 8 wide × 35 × 14 deep, grey PA, M4 screw on the front, 2 from each end |
| panel screws | M5 pan head Ø9 × 3, through a slot, every `fix_pitch` |
| cut lengths in the cell | 1200 (four rails on the back panel) |

## Named nodes
none (nothing moves or lights). Devices clip to it: a DIN device's origin sits on the rail's crown centre line, so in a BOM its y is the rail's y − 7.5 and its z the rail's z.

## Materials by layer
`M-GALV` rail · `M-GREY-PA` end clamps · `M-ZINC` screws.

## Modelling note
The slots are real openings: the crown is two strips and the bridges between slots, so the glTF carries them without booleans and AutoCAD builds the same solids (UNION them in the FILLETEDGE pass if a single body is wanted). Slot ends are square (true slots have Ø6.2 ends): within 0.5 mm of area, invisible at lab scale.

## Outputs (out/)
`din-rail-35.lsp` · `.glb` (1 node, 3 materials) · `-drawing.svg` (300 mm front sample, section at 4×) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.1 | render fix (GEO-050): the end clamps' back faces shared the mounting plane and their ends the rail's edges; now 0.1 inside both |
| 1.0 | first build |
