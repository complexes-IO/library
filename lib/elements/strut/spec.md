# strut · v1.0 · strut channel, generic, 41 x 41 x 2.5 C-profile with inturned lips, 22 opening, slotted back 13.5 x 28 at 50, cut to length

**What** A slotted strut channel: the mounting rail a process skid (process-skid) carries its instruments, valves and small
supports on. A cold-formed steel C-profile 41 wide × 41 high, wall 2.5, whose two top edges return inward as lips 9.5 wide and
hook down 10, leaving a 22 opening along the run where a channel nut sits behind the lips; the back carries a row of slotted holes
13.5 × 28 on a 50 pitch for M12 bolts into the frame. One straight length, cut to length by the `length` parameter (default 1000; a
parameter stays out of the id, OPERATING.md 6). lib/inventory.csv row `strut` (own_design generic, etim EC000386; 1 system:
process-skid).
**Class** rail · **Baseline** our own design: generic mounting rail/-profile (ETIM 10.0 EC000386), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07); the inventory row is own_design "generic" with its class on file (24 features,
lib/standards/etim/class-features.csv). No product was matched and no vendor file was opened: the folder's reference record (an
inch-sized catalogue channel and its corner bracket, references/source.txt) is not what this element is built from. What it meets
takes its figures from the standards on file (the slots' width at M12's ISO 273 clearance); the section properties are computed
from the drawn section; every other size is a design choice.
**Units / frame** mm, Z up. Origin: run start x = 0, the channel's centre line y = 0, the back's outer face z = 0 (the mounting
face, on the frame). The run goes along +x, the open side (the lips) is up at z 41. Extents x 0 to `length`, y ±20.5, z 0 to 41.
**Built with** toolkit 1.3 · AutoLISP command `STRUTCH` · parameter `length` (mm, default 1000).

## Class values
ETIM 10.0 class EC000386 Mounting rail/-profile (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". These define
the element; they are design inputs.

| # | feature | value |
|---|---|---|
| 1 | Length (EF001438) | the `length` parameter, default 1000 mm (a BOM row sets it) |
| 2 | Width (EF000008) | 41 mm (y, outside) |
| 3 | Height (EF000040) | 41 mm (z, outside, the back's face to the lips' top) |
| 4 | Slit width (EF005247) | 22 mm (the opening between the lips, along the whole run) |
| 5 | Material thickness (EF000386) | 2.5 mm |
| 6 | Profile shape (EF005179) | C-profile (the lips returned inward and hooked down) |
| 7 | Model (EF000010) | single channel, slotted back |
| 8 | Type of perforation (EF004147) | slotted holes in the back: 13.5 × 28, square-ended, on a 50 pitch, centred on the length (20 in a 1000 length, the first at x 25) |
| 9 | Hole width (EF005742) | 13.5 mm (the slots' width across the run: M12 clearance medium H13, ISO 273, lib/standards/holes.csv) |
| 10 | With toothing (EF000571) | no (plain lips) |
| 11 | Snap-off (EF007562) | no |
| 12 | Load bearing capacity (EF002918) | not stated: no allowable stress for the steel is on file (lib/materials.csv steel-mild carries no figures) |
| 13 | Area moment of inertia Iy (EF012513) | 8.35 cm⁴ (83 530 mm⁴) about the centroid's axis parallel to the back (y); the centroid 19.42 above the back's outer face: computed from the drawn section by the parallel-axis theorem over its seven rectangles, element.py `section()` (a definition, no standard's table; the build asserts the figure) |
| 14 | Area of inertia Iz (EF012514) | 10.08 cm⁴ (100 823 mm⁴) about the section's axis of symmetry (z), the same way |
| 15 | Moment of resistance Wy (EF012503) | 3.87 cm³ (Iy over the farthest fibre, 21.58 to the lips' top) |
| 16 | Moment of resistance Wz (EF012504) | 4.92 cm³ (Iz over 20.5, the outer face) |
| 17 | Suitable for circuit integrity (EF007806) | not stated (no fire test or rule on file) |
| 18 | Material (EF002169) | steel |
| 19 | Material quality (EF001257) | not stated (lib/materials.csv steel-mild names no grade) |
| 20 | Surface protection (EF000139) | zinc plated (the `M-ZINC` layer) |
| 21 | Layer thickness surface protection (EF025871) | not stated |
| 22 | Colour (EF000007) | not stated (bright zinc) |
| 23 | RAL-number (EF000116) | not stated |
| 24 | Weight (EF000167) | not stated: lib/materials.csv has no density on file. The section's area is 380 mm² (element.py `section()`), so the mass follows from a density once one is on file |

No ratings.csv: no feature of the class is a rating the checks read, and no load is claimed.

## What it meets
| figure | value | source |
|---|---|---|
| the frame it mounts on | M12 bolts through the back's slots, 13.5 wide (ISO 273 medium H13), 28 long, 50 pitch; their nuts or the frame's tapped holes are the host's | ISO 273 (lib/standards/holes.csv) for the width; the slot's length and pitch are this design's choices. The slots are cut with square ends (two plain cuts, the gate skips cut edges); no position tolerance is declared (a slot locates one way only, and the frame's holes are the host's) |
| channel nuts, brackets and clamps behind the lips | the 22 opening and the lips' 10 return (the nut's hook) | this design's choices: no strut-channel standard or channel-nut element is on file (lib/standards/etim/classes.csv has EC000096 Slide nut, the inventory's tslot-nut, not built); a nut built later takes its figures from this element |
| the process skid's instruments | nothing of theirs is drawn; they clamp to the channel | process-skid places them (lib/machines-from-elements.txt) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| section | 41 × 41 outside, wall 2.5, zinc-plated steel (`M-ZINC`) | the common strut-channel size class in metric figures; 2.5 is a cold-formed sheet the gate skips as "short" at r 0.5 (every 2.5 edge is under MIN_EDGE 3.0) |
| lips | 9.5 wide (from the outer face) × 2.5, returned inward at the top; 22 opening | a nut behind the lips bears on 7 of lip each side (the lip past the wall) |
| returns | 2.5 × 10, hooking down from each lip's inner edge, 0.5 into the lip | the nut's hook; 10 keeps the returns' end edges over the gate's 3 to 7 mm free-corner trap at r 0.5 (mech-r101) |
| slots | 13.5 × 28 at 50, centred on the length; 3 or more of back each side; 22 of back between slots | M12's clearance width; 28 gives 14.5 of adjustment; the row is centred so both ends read alike |
| length | 1000 default, a parameter | the skid's frame sets it per BOM row |
| fillet radius | 0.5 (`FILLET_R`) | the rail class's 1.0 reads 10 mm edges short in the per-edge pass (mech-r69): 0.5 is the right radius for a 2.5 cold-formed section |
| load, grade, finish thickness | not claimed | no allowable stress, grade or plating figure is on file |

## Mechanism
None: one fixed body, no moving node, no port. behaviour.csv is the header only.

## Named nodes
None. Collider, an axis-aligned box: `body` (x 0 to `length`, y ±20.5, z 0 to 41).

## Materials by layer
`M-ZINC` the whole channel (zinc-plated steel).

## Decals (Blender)
"complexes.org generic" on the back's outer face, centred.

## Notes
No vendor names, part numbers or marks. No load rating: the section properties (Class values 13 to 16) are the drawn section's
arithmetic, not a test, and no allowable stress is on file to turn them into a load. A mounting profile is in the ETIM classes on
file and not a part a dimensional standard shapes, so it is built generic to its class (OPERATING.md 12); a back-to-back double
channel, a half-height channel or a slotted-sides channel is another class value or another element. Not drawn: the channel nuts,
brackets, clamps and bolts (the hosts' or later elements'), the frame it bolts to. No open figure: the slots' width is ISO 273's,
the section properties are computed, and the rest are design choices.
The gate's fillet rule (r 0.5, `FILLET_R`): the 2.5 sheet edges are short (skipped); the free-corner edges picked are the lips'
9.5, the returns' 10, the walls' 41 and the run's `length` edges; the slots' edges are cut edges, skipped; the web's long edges and
the returns' top edges lie buried in their neighbours. Every bounding-box extreme lies on an axis-aligned box (the walls' outer
faces y ±20.5, the back z 0, the lips' top z 41, the ends x 0 and `length`); nothing is tilted or nested.

## Outputs (out/)
`strut.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000386), our own design (mech-r105, unattended, 2026-11-11): 41 x 41 x 2.5 C-profile with inturned lips and returns, slotted back, cut to length; section properties computed |
