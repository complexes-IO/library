# conveyor-guard · v1.0 · conveyor tunnel guard 1000 long, 560 clear inside, 400 high, sheet 2.0, roof window, 6 × M8 flange holes

**What** A fixed tunnel guard over a belt conveyor section: an inverted U of sheet steel that covers the belt for 1000 of its
length, open at both ends so the load passes through, with a clear window in the roof to watch it. Each side wall is bent out at
its foot into a flange that sits on the top face of the conveyor's side frame and is screwed to it. The systems of
lib/machines-from-elements.txt that list it (the guarded machine door, the inbound conveyor, the robot cell and the safety cell)
cover the stretch of belt where a person could reach a pinch point or a moving load; a BOM places one or more along a conveyor.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs: guards; lib/inventory.csv marks conveyor-guard
own_design "yes"). No product was matched and no vendor file was opened. The fixing holes are on file (ISO 273); every other
size is a design choice.
**Units / frame** mm, Z up. Origin: the flanges' underside z = 0 (the face that sits on the conveyor's side frames), x = 0 at the
middle of the guard's length, along the conveyor's travel; y = 0 on the conveyor's centre line. Extents x ±500, y ±322, z 0 to 400.
**Built with** toolkit 1.3 · AutoLISP command `CNVGRD` · no parameters.

## Mechanism
None: a fixed guard has no moving part. It is removed only by undoing its six screws.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| fixing holes | 6 × M8, Ø9.0, three in each flange, at x −400, 0 and 400, y ±302 (800 × 604) | ISO 273 medium (H13), lib/standards/holes.csv |
| the conveyor's side frames | their top faces at z = 0, under the flanges, with a fixing slot or hole under each flange hole | the conveyor's element (conveyor-seg, made of tslot-40: not built yet). The M8 screws (screw-iso4762) and the T-slot nuts (tslot-nut) are standard and common parts, not built yet: the holes are cut and the assembly places them later (OPERATING.md 12, own designs). The inventory row's bracket-angle is not needed: the flanges are bent from the walls |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The six fixing holes carry a declared position tolerance Ø0.8 at MMC to A, the mounting face (the flanges' underside), the holes
located to each other (features.csv; H − F = 9.0 − 8 = 1.0). The flanges are punched flat before bending, as ISO 2768-m over the
pattern's 1002 diagonal (±1.2, lib/standards/general-tolerances.csv row m 1000-2000) would not hold the pattern by itself.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| tunnel | 1000 long (x −500 to 500), 560 clear between the walls (y ±280), 400 from the flanges' underside to the roof's top | covers a belt up to 500 wide with 30 clear each side and a load up to about 350 high; longer runs take two guards end to end |
| sheet | 2.0 everywhere: walls y ±280 to ±282, roof z 398 to 400 across both walls | one bent sheet part, stiff enough at this span without a stiffener |
| flanges | 40 out from each wall's outer face (y ±282 to ±322), 2.0 thick, the full length | they sit on a 40 wide side frame, the holes on its centre line (y ±302) |
| holes | three a flange, 400 apart | one at each end and one in the middle, so the guard lies flat on the frame |
| roof window | cut-out 800 × 360 (x ±400, y ±180), a clear pane 6 thick under the roof lapping 30 round it (z 392 to 398) | the load can be seen without opening anything |
| ends | open | the load passes through; how far the guard reaches past a pinch point is where the assembly places it |
| bends, welds | not drawn: the corners are drawn square | the model shows the part's envelope |

## Where it stands (the assembly's)
The guard's length against a person's reach through its open ends, and the gap between the belt and the walls, are where a BOM
places it, not part of this element: the safety distances of ISO 13857 and the guard requirements of ISO 14120 are not on file,
so this element makes no safety claim and names no distance. The pane's impact resistance is not stated. The assembly that places
it cites them when they are on file.

## Named nodes
None. Colliders `roof`, `side-l`, `side-r` (the walls; the flanges and the pane are left out).

## Materials by layer
`M-YELLOW` the walls, roof and flanges (steel, painted yellow). `M-CASE-CLEAR` the roof pane (clear polycarbonate).

## Notes
No load rating and no safety claim. No vendor names, no label. A hinged or interlocked version (one that opens for cleaning) and
an end-closing mesh are later elements.

## Outputs (out/)
`conveyor-guard.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r52, unattended) |
