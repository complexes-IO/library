# conveyor-incline · v1.1 · cleated belt incline conveyor section, 500 between frames, 1500 long, 30 degrees, belt 490 wide with 6 cleats, belt top 750 at the tail rising to 1558 at the head, head and tail pulleys, floor rails with 4 × M12 anchor holes

**What** A cleated belt incline conveyor, one straight sloped section: goods ride up a belt whose cross cleats keep them from
sliding back, from a tail end at the horizontal sections' track height to a head end about 800 higher. The model shows the
belt's top run at rest (one sloped plate with six cleats standing on it, on a slider bed plate), the two pulleys (a drum with
its shaft) that the belt would run round, the two sloped side frames and the two supports standing on two floor rails that
carry the anchor holes. The belt's wrap round the pulleys, its return run and the drive are not drawn.
lib/machines-from-elements.txt lists it in conveyor-types-bench (one section of every conveyor type), beside conveyor-roller,
conveyor-slat and conveyor-mattop, whose track width, plan length and anchor pattern it shares and whose track height its tail
end meets. The pulleys are the mechanism: the twin turns them by name.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks conveyor-incline
own_design "yes": "cleated belt incline conveyor section (our own build)"). No product was matched and no vendor file was
opened. The holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the centre of the section's plan, x = 0 midway between the side
frames, y = 0 midway along the floor rails. Goods travel up the slope toward +y, the head end. The belt's top line passes z 750
over the tail end of the plan (y −750) and rises at 30 degrees; the frames run 1630 along the slope from there, their sloped
ends inside the rails' plan. Extents x ±375, y ±750 (the floor rails), z 0 to 1558.3 (the belt plate's upper corner).
**Built with** toolkit 1.3 · AutoLISP command `CONVINCL` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the floor rails at 680 × 900 (x ±340, y −400 and 500), one beside each post | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice, the pattern of conveyor-roller 1.0's foot plates (680 across; here 900 apart). The anchors (anchor-bolt, not built yet) are the assembly's; nothing is placed in the holes |
| floor | the floor rails' undersides, z = 0 | a flat floor; the floor is the assembly's |
| the section that feeds it | the tail end: the belt's top line at z 750 over y −750, the track 500 wide between the side frames | element:conveyor-roller 1.0 (W, TOP): a horizontal section's track top is at z 750, so goods pass from it onto the belt. The gap between the two (the horizontal section's last roller to the belt's tail end at y −738.4) and any transfer plate are the assembly's |
| what it feeds | the head end: the belt plate's upper corner at y 650, z 1558.3 | none on file: what receives the goods (a chute, a hopper, a higher section) is the assembly's |
| the drive | the head pulley, node `pulley-head`, shaft Ø40, its end faces at x ±245 inside the side frames | none on file: no gearmotor or reducer is placed and no shaft end, key or bore is drawn. What turns the pulley, and how it joins it, is the assembly's and a later version's |
| the goods | the belt's top, between the cleats (50 high, 250 apart along the slope), 10 above the side frames' tops | none on file: goods up to 490 wide ride between the frames' lines; the cleats carry them up the slope |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane midway between the
side frames) and C (the plane midway between the two supports, y = 50) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5).

## Its own sizes (design choices)
Along-the-slope figures (s) are measured from the frames' tail end up the slope; "normal" figures from the belt's top line,
positive out of the belt. A point s along the slope and n out of it is at y = −750 + 0.866 s − 0.5 n, z = 750 + 0.5 s + 0.866 n.
| item | value | why |
|---|---|---|
| plan and slope | floor rails 1500 long (y ±750); the belt rises at 30 degrees from the horizontal; the frames 1630 along the slope (815 of rise), their sloped ends inside the plan | the plan is conveyor-roller's section length, so the section fits the same floor layout; 30 degrees is this design's choice for a cleated belt, which carries loose goods up a slope a plain belt would let them slide down. No standard on file fixes an incline angle. The frames stop 1630 along the slope so that their head end's lower corner (y 746.6) stays inside the rails' end, and the gate's extents fall on the rails (see Notes) |
| belt, top run | one plate 490 (x ±245) × 1603.2 along the slope (s 13.4 to 1616.6) × 10 thick (normal −10 to 0), drawn by its outside; its lower end at y −738.4, z 756.7, its upper corner at y 650.0, z 1558.3 | its ends 13.4 short of the frames' ends, as conveyor-mattop's: the top run drawn as one plate at rest, its wrap round the pulleys (their axes 150 in from the frames' ends) not drawn; 5 clear of each side frame; 10 thick |
| cleats | 6, each 470 (x ±235) × 2.5 thick × 50 high, standing on the belt's top, 250 apart along the slope, centred on the frames' midpoint (s 190, 440, 690, 940, 1190, 1440) | hold the goods on the slope; 10 in from each belt edge; 2.5 thick so the belt and its cleats read as one moulded part |
| slider bed | one steel plate 490 (x ±245) × 1130 along the slope (s 250 to 1380) × 10 (normal −20 to −10) | the belt's top run slides on it; it ends 40 clear of each pulley's drum |
| side frames | 2, section 50 (x) × 160 (normal), 1630 along the slope, their ends square to the slope, drawn by their outside; inner faces at x ±250, normal −170 to −10. Tail end: top corner y −745, z 741.34; underside corner y −665, z 602.78. Head end: top corner y 666.6, z 1556.34; underside corner y 746.6, z 1417.78 | stand either side of the belt and the pulleys; their tops level with the belt's underside, 10 below its top |
| cross members | 2, 500 long (x ±250) × 50 along the slope × 40 (normal −60 to −20), frame to frame, centred where each support's frame underside passes the posts' centres (s 305.99 and 1345.26; centres at y −465.0, z 868.35 and y 435.0, z 1387.99) | carry the slider bed; hold the frames to the track's width |
| pulleys | 2: a drum Ø120 × 420 (x ±210) on a shaft Ø40 × 490 (x ±245), drawn round, the axes along x at normal −90, 150 from each end of the frames along the slope: the tail pulley's axis at y −575.1, z 747.06, the head pulley's at y 576.7, z 1412.06 | the drums' tops 10 below the slider bed, 40 clear of its ends; the shafts 5 clear of each side frame (the bearings are not drawn) |
| floor rails | 2, 150 (x 225 to 375 each side) × 1500 (y ±750) × 20 (z 0 to 20), one under each side's posts, running outward; two Ø13.5 holes in each at y −400 and 500, 40 outside the posts' outer faces and 35 from the rail's outer edge | fix the section to the floor and tie each side's posts together; they run the plan's full length, so the section's footprint is the plan |
| supports | 2, at y −400 and 500: each two posts and a lower tie | 900 apart, under the frames where the slope's underside is 755.8 and 1275.4 above the floor |
| posts | 4, 50 × 50, drawn by their outside, under the side frames (x 250 to 300 each side), from the rail's top (z 20) up to the frame's sloped underside, cut to it (the tail posts 721.3 to 750.2 tall over the rail at their faces, tops at z 741.3 to 770.2; the head posts 1241.0 to 1269.8 tall, tops at z 1261.0 to 1289.8) | each stands on a floor rail and carries a frame; the cut top face lies in the frame's underside plane |
| lower ties | 2, 500 × 50 × 50 (z 150 to 200), post to post | stiffen each support |
| the goods | not drawn | the system's, not the conveyor's |

## Mechanism
Two pulleys, nodes `pulley-head` (the upper end) and `pulley-tail` (the lower end), each a drum and its shaft turning as one
about the shaft's axis (along x), 0 to 360 degrees: a spin, with no stop. In the machine the drive turns the head pulley, the
belt runs up the slider bed with its cleats, round the head pulley, back underneath and round the tail pulley. The model draws
the top run only, at rest, as part of the fixed body: the belt does not move in the twin; the pulleys do. Each pulley's shaft
stands 5 clear of the side frames, its drum 10 below the slider bed and 40 from the bed's ends, clear of the cross members along
the slope (the head drum 49.78 from cross member b), so a pulley touches nothing at rest or as it turns. behaviour.csv: state `still` (default) and
`running` (manual toggle: the drive is the assembly's), pose of both pulleys at the range end in `running`.

## Named nodes
`pulley-head`, `pulley-tail`: rotate about x through their axes, range 0 to 360 degrees. Colliders are axis-aligned boxes, so
each sloped part has six stepping along the slope: `frame-l-1` to `frame-l-6`, `frame-r-1` to `frame-r-6` (l / r the −x / +x
side), `belt-deck-1` to `belt-deck-6` (the belt's top run: what goods ride on); and `rail-l`, `rail-r`, `post-la`, `post-lb`,
`post-ra`, `post-rb` (a / b the −y / +y support), `cross-a`, `cross-b`, `tie-lo-a`, `tie-lo-b`. None is named like a node.

## Materials by layer
`M-STEEL-7035` the side frames, posts, ties, cross members, slider bed and floor rails (painted steel, RAL 7035) · `M-ZINC` the
pulleys' shafts (steel, zinc-plated) · `M-SILVER` the pulleys' drums (bright steel) · `M-BLACK-PA` the belt and its cleats
(black). The layer names say the colour and the kind of material shown; no grade of belt or plastic is claimed.

## Decals (Blender)
"complexes.org" on the +x side frame's outer face.

## Notes
No vendor names, part numbers or marks. No load rating, no speed figure, no incline-capacity figure and no safety claim: no
goods' mass is on file, no calculation or test of the model is on file, and the conveyor is not sized against a load. Not
drawn: the belt's carcass, splice and edges, the turn of the belt round the pulleys, the return run and its supports, the
pulleys' lagging, bores and keys, the bearings, the drive (motor, reducer, the shaft's drive end), belt take-up, side guides or
skirts, guards over the pulleys and the return run, a transfer plate at the tail end, a chute at the head end, joining to the
sections before and after, height adjustment. The anchor holes are on file; the anchors are the assembly's.
Gate note (mech-r92): the AutoCAD gate's r 1.0 fillet on a corner of a tilted box draws the model's extreme in by about 0.4
(the gate allows 0.5 between the STEP and the glb on each axis), so the x and y extremes lie on the floor rails (axis-aligned)
and only the top, the belt plate's upper corner, is such a corner. A first build with sloped frame ends at both ends of the
plan read 0.74 in y and failed the gate; the rails and the shorter frames are the fix, at the same version.

## Outputs (out/)
`conveyor-incline.lsp` · `.glb` (pivots on the two pulleys) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r92, unattended, 2026-11-11) |
| 1.1 | review conveyor-incline-1.0 notes 1 to 3, text only, no figure changed: the posts' heights over the rail (721.3 to 750.2, 1241.0 to 1269.8) beside their top z; the head drum 49.78 from cross member b along the slope; the belt row says its wrap round the pulleys is not drawn (mech-r110, unattended, 2026-11-12) |
