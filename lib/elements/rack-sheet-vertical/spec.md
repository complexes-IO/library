# rack-sheet-vertical · v1.1 · vertical sheet rack 1600 × 1200 × 1500, base plate 20, nine upright dividers, eight slots 155 wide, sheets stood on edge

**What** A vertical sheet storage rack for the steel store (lib/machines-factory.txt line 122: storage-steel places rack-cantilever,
rack-sheet-vertical, rack-bar, anchor-bolt, sign-iso7010 and floor-marking). Sheets stand on edge on a base plate, one size or
grade to a slot, each leaning on an upright divider, so one sheet is taken out from the front or lifted out from above without
moving the others. Bars and tubes go on rack-bar; long stock lying flat on rack-cantilever.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks rack-sheet-vertical
own_design "yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the rack's footprint, x = 0, y = 0. The front, the side
a sheet goes in from, is toward −y; the slots follow one another along x, each sheet's face in a y-z plane.
**Built with** toolkit 1.3 · AutoLISP command `SHEETRACK` · no parameters.

## Mechanism
None: one fixed body, no node. A sheet placed in the rack is the store's, not the rack's.

## What it meets (figures from files on hand)
Nothing on file: it stands on the floor and holds loose stock. Its fixing to the floor (anchor-bolt, a separate element on the
same line of machines-factory.txt) is the assembly's, so the rack has no hole (OPERATING.md 12: a host doesn't model holes for a
part it places later). No sheet format table is on file, so the rack is not sized to one: the slot depth between the front and
back posts is 1080 and the dividers stand 1480 above the base plate; a sheet longer than the rack is deep stands out of the front.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| footprint | 1600 × 1200 (x ±800, y ±600) | a design choice; eight slots side by side |
| base plate | 1600 × 1200 × 20 (z 0 to 20) | the sheets' edges stand on it. 20 thick, not 10: a 10 mm edge between two free corners read 89 % of the fillet gate's expected volume in rack-bar 1.0's first AutoCAD run |
| dividers | 9, each 40 thick (x), at a pitch of 195; the outer two flush with the plate's ends (x ±800) | each a frame: a front post (y −600 to −560) and a back post (y 520 to 560), 40 × 40, from the plate (z 20) to z 1500; a middle bar (z 720 to 760) and a top bar (z 1460 to 1500), 40 × 40, from post to post |
| slots | 8, each 155 clear (x) between dividers | a sheet, or a stack of a few, leans on the divider beside it |
| back rails | 2, 40 × 40 × 1600, behind the back posts (y 560 to 600): one low (z 240 to 280), one at the top (z 1460 to 1500) | tie the nine dividers along x; the front stays open so a sheet slides in |
| height | dividers' top at 1500 | a design choice (no reach or anthropometric table is on file, so no ergonomic claim is made) |
| the sheets themselves | not drawn | the store's stock, not the rack |

## Named nodes
None. Colliders: `base`, `divider-1` to `divider-9` (each spans its divider's posts and bars, the plane a sheet leans on),
`rail-low`, `rail-top`.

## Materials by layer
`M-STEEL-7035` every member (painted steel, RAL 7035).

## Notes
No load rating and no stability claim: no sheet's mass or lean angle is on file, so the rack is not sized against them, and
whether it needs fixing to the floor is decided where it is placed. The volume is 117 248 000 mm³ (base plate 38 400 000, posts
18 × 2 368 000, bars 18 × 1 728 000, back rails 2 × 2 560 000; written as volume only: lib/materials.csv gives steel no density,
so no mass is stated). No vendor names, no label.

## Outputs (out/)
`rack-sheet-vertical.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r70, unattended) |
| 1.1 | text only (review rack-sheet-vertical-1.0 finding 1): the footprint is a design choice, eight slots side by side; the reach claim is gone; no geometry change (mech-r79, unattended) |
