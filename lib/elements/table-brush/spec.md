# table-brush · v1.0 · brush table 2000 × 1250, work plane at 920, nineteen brush strips across a top frame on four legs

**What** The brush table of a turret punch's sheet feed: the sheet lies on a field of upright brush strips, so the clamps can
push it in any direction without scratching it, and slugs and small parts fall through between the strips. It is the table-brush
of punch-turret (lib/machines-factory.txt line 64: frame-welded (own), turret-punch, punch-die-set, ram (own), servo motors and
drives, ballscrews, linear guides, clamp-sheet, table-brush (own), hpu-0.37kw, cnc-controller, hmi-7in, light-curtain,
op-estop-22-2nc, relay-safety-2ch-2no1nc, enc-fs-1524x1829x305). A BOM places one or more beside the punch, the brushes' tops level with its table.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks table-brush own_design
"yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the table's footprint, x = 0, y = 0. The table's
length runs along x; the side toward the punch is +y. The brushes' tops, the work plane (the sheet's underside), are at z = 920.
Extents x −1000 to 1000, y −625 to 625, z 0 to 920.
**Built with** toolkit 1.3 · AutoLISP command `BRUSHTABLE` · no parameters.

## Mechanism
No moving part. The whole table is the fixed body; a sheet sliding over the brushes is the assembly's.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the punch's table | the work plane z 920 | punch-turret and turret-punch are not built and no table height is on file: 920 is a design choice, and the match is checked when the punch is on file (the assembly sets the table's height, or a later version takes the figure) |
| the floor | four legs, 60 × 60, at the footprint's corners | the table's fixing to the floor (anchor-bolt, a separate element) is the assembly's, so the table has no hole (OPERATING.md 12: a host doesn't model holes for a part it places later) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| footprint | 2000 × 1250 (x ±1000, y ±625) | a design choice |
| top frame | one solid: 2000 × 1250 × 60 (z 820 to 880), cut open inside to 1880 × 1130, so a rim 60 wide | carries the strips on its two long rails; one cut solid, not four boxes (rack-bar 1.0's fillet lesson) |
| legs | 4, 60 × 60, z 0 to 820, under the frame's corners | a design choice |
| stretchers | 2, 40 × 40 × 1880 along x between the legs, z 150 to 190, at y ±595 | tie each pair of legs |
| brush strips | 19 at a pitch of 100 along x (x −900 to 900), each 1230 long (y −615 to 615) across the frame's long rails | 76 clear between bristle blocks, so slugs and small parts drop through; the strips' ends rest 50 on each rail and stop 10 short of the frame's faces |
| strip holder | aluminium, 30 wide × 20 high (z 880 to 900) | a design choice |
| bristle block | nylon, 24 wide × 20 high (z 900 to 920), 1210 long (y −605 to 605) | drawn as one block per strip (the bristles themselves are not drawn); 3 in from the holder's sides and 10 in from its ends, so no face is flush with another material's |
| finish | frame, legs and stretchers painted; holders anodised; bristles black | a design choice |

## Named nodes
None (fixed body only). Colliders `brushes` (the brush field, z 880 to 920), `frame` (the top frame) and `leg-lf`, `leg-rf`,
`leg-lb`, `leg-rb`.

## Materials by layer
`M-STEEL-7035` the frame, legs and stretchers (painted RAL 7035). `M-ALU-ANOD` the strip holders (anodised aluminium).
`M-BLACK-PA` the bristle blocks (nylon).

## Notes
No load rating, no bristle stiffness, wear or scratch claim: no sheet mass, feed force or brush figure is on file, so the table is
not sized against them. Ball transfer units, a slug chute and a height adjustment are not drawn; a later version takes them if a
machine needs them. The volume is 65 417 200 mm³ (top frame 22 536 000, legs 4 × 2 952 000, stretchers 2 × 3 008 000, holders 19 ×
738 000, bristle blocks 19 × 580 800; written as volume only: lib/materials.csv gives no densities, so no mass is stated). No
vendor names, no label.

## Outputs (out/)
`table-brush.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r79, unattended) |
