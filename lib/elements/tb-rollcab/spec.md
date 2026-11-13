# tb-rollcab · v1.0 · roll cabinet 680 × 460 × 800, five drawers, caster plate holes

**What** A rolling tool cabinet (toolbox station) for the lab: a sheet-steel carcass with five pull-out drawers, a push bar on its
right side, and the fixing holes of four caster plates in its bottom. The drawers are the mechanism: the twin opens them by name.
The casters themselves are not built yet (lib/rounds/mech/next.md #14): as EM's rule for own designs says, the holes are modelled
and a later version places the part.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, references/source.txt) marks it "own design (planned)", EM 2026-11-03; it holds no
figure.
**Units / frame** mm, Z up. Origin: the carcass underside z = 0 at its front-left corner x = 0, y = 0. The person stands at −y;
the drawers open toward −y; the push bar is on the right (+x). The casters go under z = 0: with them placed, the floor lies one
caster height below the origin, and the origin stays where it is.
**Built with** toolkit 1.3 · AutoLISP command `ROLLCAB` · no parameters.

## Mechanism
`drawer-1` (bottom) to `drawer-5` (top): translate along −y, 0 to 320 each. Each drawer node carries its front, its tray (bottom,
two sides, back) and its handle. The trays run 12.5 inside each carcass side (the room drawer slides take; the slides are not
modelled) and inside their own front's height band, so a drawer at any travel clears the carcass and the other drawers. At 320
out, 100 of the 420 tray stays inside. As cabinet-tool's drawers.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| caster plate fixing hole | Ø9.0, four per plate, four plates, M8 | ISO 273 medium (H13), lib/standards/holes.csv |

The M8 screws and the casters are not placed (no fastener element and no caster element is built yet; EM's rule: the holes are
modelled, a later version places the part). The plate pattern (below) is this cabinet's design choice; the caster element (#14)
takes it, or a later version of this one moves the holes (cut-outs: a major).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| carcass | 680 × 460 × 800 outside; sides, back and top 1.5 sheet; bottom 3.0; sides and back stand on the bottom, the top over them | a drawer width for the lab's hand tools; the bottom carries the caster screws |
| bottom | seven 3.0 plates in one plane: a 140 × 140 pad at each corner (the caster plate's holes), a 400 × 460 middle plate and two 140 × 180 plates between the pads | each pad carries one caster plate's four holes |
| caster plates | four, centred 70 in from each side, front and back: (70, 70), (610, 70), (70, 390), (610, 390); four holes each on 80 (x) × 60 (y) centres | |
| drawer fronts | 20 thick, full width (over the carcass edges), heights 240, 180, 150, 110, 100 from the bottom, 3 apart, z 4.5 to 796.5 | deepest drawer at the bottom |
| trays | 652 wide (12.5 clear each side), 420 deep, 1.5 sheet; bottom 10 above the lower edge of their front, sides 20 below its top | as cabinet-tool |
| pull-out | 320 | |
| drawer handles | bar 300 × 12 × 12 on two standoffs, 27 proud of the front, centred on each front | cabinet-tool's handle |
| push bar | bar 12 × 340 × 12 on two 15 × 12 × 12 standoffs on the right side, 27 out from it, centred at z 700, 60 in from the front and back | to push the cabinet by |
| colours | carcass and trays RAL 7035, fronts blue, handles and push bar zinc | as cabinet-tool |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
Each caster plate's four Ø9.0 holes are one pattern (80 × 60): position Ø0.5 at MMC (features.csv; H − F = 9.0 − 8.0 = 1.0), datum
A the bottom's underside, the four holes located to each other.

## Named nodes
`drawer-1` … `drawer-5` (translate, above). Colliders `body` (the carcass and the push bar, 707 × 460 × 800) and one per drawer
(`drawer-<n>`).

## Materials by layer
`M-STEEL-7035` carcass, bottom plates, trays · `M-BLUE` drawer fronts · `M-ZINC` drawer handles, push bar.

## Notes
No load rating and no safety claim (no drawer capacity, no tipping or rolling load, no brake claimed). Drawer slides, locks, the
casters and their screws are not modelled. No vendor names; no label in this version.

## Outputs (out/)
`tb-rollcab.lsp` · `.glb` (pivots on the five drawers) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r33, unattended; lib/rounds/mech/next.md #6); the casters placed as holes until caster (#14) is built |
