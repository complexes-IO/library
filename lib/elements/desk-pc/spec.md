# desk-pc · v1.0 · workstation desk 1400 × 700 × 740, CPU bay, cable tray under, one drawer

**What** A computer workstation desk for the lab (lab-bench and reverse-engineering-station, lib/machines-from-elements.txt): a 25
top on two steel side frames, a back (modesty) panel, a cable tray hung under the top's back edge, a CPU bay on the floor at the
right and one drawer under the top at the left. The drawer is the mechanism: the twin opens it by name.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match; lib/inventory.csv marks desk-pc
own_design). No vendor file was opened. The folder's acquisition record (metadata.json, references/source.txt, validation.json)
describes a catalogue desk; this element is not built from it and takes no figure from it.
**Units / frame** mm, Z up. Origin: the floor plane z = 0; x = 0, y = 0 at the top's front-left corner, seen from above. The person
sits at −y; the drawer opens toward −y; the CPU bay is on the right (+x).
**Built with** toolkit 1.3 · AutoLISP command `DESKPC` · no parameters.

## Mechanism
`drawer`: translate along −y, 0 to 300. The node carries the drawer's front, its tray (bottom, two sides, back) and its handle. The
tray runs 10 inside each side of the fixed housing (the room drawer slides take; the slides are not modelled), 3.5 above the
housing's bottom and 15 below the top, so the drawer at any travel clears the housing and the top. At 300 out, 100 of the 400 tray
stays inside. Handle as cabinet-tool's, with a shorter bar.

## What it meets
Nothing outside itself: no screw, rail, port or placed element. The frame's fixings, drawer slides and levelling feet are not
modelled; a later version that adds levelling feet places feet-leveling (lib/rounds/mech/next.md #15) once it is built.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| top | 1400 × 700 × 25, its surface z 740, underside z 715 | a single-person workstation with a monitor, keyboard and papers |
| side frames | at x 30 to 80 and 1320 to 1370; each a foot 50 × 660 × 40 (20 in from the front and back edges), two legs 50 × 50 from the foot to the top (y 40 to 90 and 610 to 660), a top rail 50 × 50 between the legs under the top | an open knee space between the frames, 1240 wide |
| back (modesty) panel | 1.5 sheet, x 80 to 1320, its front face at y 633.5, z 300 to the top's underside | closes the back above the floor cables |
| cable tray | 1.5 sheet U along x, 1240 long, 150 wide (y 483.5 to 633.5), underside z 595; front wall 80 high; its back wall rises to the top's underside (the tray hangs from the top by it) and stands against the back panel | keeps monitor and PC cables off the floor |
| drawer housing | 1.5 sheet, x 100 to 560, y 0 to 440, z 595 to 715 (bottom, two sides, back), hung under the top | ahead of the cable tray (y 440 < 483.5) |
| drawer | front 460 × 20 × 114 (z 598 to 712), proud of the top's front edge; tray 437 × 400, sides 98.5 high, 1.5 sheet; pull-out 300 | |
| drawer handle | bar 200 × 12 × 12 on two 12 × 15 × 12 standoffs, 27 proud of the front, centred on it | cabinet-tool's handle, shorter |
| CPU bay | at the right, between its side panel (1.5 sheet, x 1018.5 to 1020, 560 high, on the floor) and the right side frame; a floor plate 300 × 520 × 3.0 at z 60 to 63 on two runners 30 × 60 along y | the PC stands off the floor, 300 wide |
| colours | top brown, frame, panels, tray and housing RAL 7035, drawer front blue, handle zinc | as cabinet-tool, a wood-look top |

## Named nodes
`drawer` (translate, above). Colliders `top`, `frame-left`, `frame-right`, `back-panel`, `cable-tray`, `drawer-housing`, `cpu-bay`
and `drawer`.

## Materials by layer
`M-BROWN` top · `M-STEEL-7035` side frames, back panel, cable tray, drawer housing, drawer tray, CPU bay · `M-BLUE` drawer front ·
`M-ZINC` drawer handle.

## Notes
No load rating and no ergonomic or safety claim (no desk or drawer capacity, no seated-height or knee-space claim, no tipping
claim). Drawer slides, a lock, levelling feet, cable grommets and the frame's fixings are not modelled. No vendor names; no label
in this version.

## Outputs (out/)
`desk-pc.lsp` · `.glb` (pivot on the drawer) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r34, unattended; lib/rounds/mech/next.md #7) |
