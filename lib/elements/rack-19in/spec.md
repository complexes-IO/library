# rack-19in · v1.1 · rack frame 600 × 800 × 2000 for 19-inch equipment, plain rails, front door

**What** A floor-standing rack frame for the lab's 19-inch equipment (servers, switches, patch panels, a rack UPS): a plinth, a
frame of 40 × 40 members, side and rear panels, a roof, four vertical mounting rails, and a front door. The door is the
mechanism: the twin opens it by name. The rails are plain in this version: the 19-inch figures are not on file (open figures).
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, references/source.txt) asks for a build from EIA-310 and a cabinet spec sheet; neither
is on file here (lib/standards/sources.csv row eia-310: "to buy"), so this element is not built from it.
**Units / frame** mm, Z up. Origin: the plinth underside z = 0 at its front-left corner x = 0, y = 0. The person stands at −y; the
door opens toward −y; the rear panel's outer face is y = 800.
**Built with** toolkit 1.3 · AutoLISP command `RACK19` · no parameters.

## Mechanism
`door-front` rotates about the frame's front-left vertical edge (x 0, y 0), 0 to −110° about +z: its free edge swings outward toward
−y and left. Closed, the door lies in front of the frame (y −20 to 0), from the plinth's top (z 100) to the roof's top (z 2000); its
handle stands 27 proud. Through its travel every point of it stays outside the frame (x < 0 once it has left y < 0). Hinges and
the catch are not modelled.

## What it meets (figures from files on hand)
Nothing outside itself in this version. The 19-inch equipment's fit to the rails is the open figure below; no floor fixing is
modelled (the rack stands on its plinth; anchors come with a version that has a fastener table on file).

## Open figures
- **NOT ON FILE (B)**: the 19-inch rail figures: the panel opening between the rails, the rail hole pitch and the unit height
  (IEC 60297-3-100 / EIA-310, sources.csv row eia-310, not on file). The rails are plain bars with no holes, placed by this frame
  (their inner edges 470 apart, the front pair's front face at y 98, the rear pair's at y 658), not at the standard's figures. A
  version with the standard on file moves them and cuts their holes (a major: cut-outs).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| overall | 600 × 800 × 2000 (door shut, handle aside: y −47 to 800) | the depth gives 560 between the front and rear rails, 98 in front of the front rails and 140 behind the rear rails (cables) |
| plinth | 600 × 800 × 100, built solid | lifts the frame off the floor; built solid under the whole footprint, so this version models no cable entry |
| frame | 40 × 40 members, built solid: four corner posts z 100 to 1998.5; side, front and rear members at the bottom (z 100 to 140) and top (z 1958.5 to 1998.5) | the frame's top 1998.5 is the roof sheet's underside (2000 − 1.5) |
| rail cross-bars | four, 520 × 40 × 40, between the side members at the bottom and top, front faces at y 100 and 660 | carry the rails; 560 between the front and rear rails' faces |
| rails | four, 25 × 2.0 sheet, z 100 to 1998.5, on the cross-bars' front faces: x 40 to 65 and 535 to 560 | plain (open figures) |
| side and rear panels | 1.5 sheet, in the posts' outer and rear faces, between the bottom and top members | |
| roof | 600 × 800 × 1.5, z 1998.5 to 2000, on the frame's top | |
| door | 600 × 20 × 1900 (double wall), z 100 to 2000; swing 0 to 110° | |
| handle | vertical bar 12 × 12 × 200 on two 12 × 15 × 12 standoffs, 27 proud of the door, centred at z 1050, 40 from the free edge | hardware-cabinet's handle |
| colours | frame, panels, plinth and roof RAL 7035, door blue, rails galvanised, handle zinc | as hardware-cabinet |

## Named nodes
`door-front` (rotate, above). Colliders `body` (the frame, 600 × 800 × 2000) and `door-front` (the door and its handle).

## Materials by layer
`M-STEEL-7035` plinth, frame, cross-bars, panels, roof · `M-GALV` rails · `M-BLUE` door · `M-ZINC` handle.

## Notes
No load rating (no shelf, rail or tipping load is claimed) and no safety claim; no lock, no earthing point in this version. No
vendor names; no label in this version.

## Outputs (out/)
`rack-19in.lsp` · `.glb` (pivot on the door) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r32, unattended; lib/rounds/mech/next.md #5); the rails plain, their 19-inch figures open (class B) |
| 1.1 | text only (lib/reviews/elements/rack-19in-1.0.md finding 1, mech-r38, unattended): "Its own sizes" gives the built top, posts, rails and top members to z 1998.5, roof z 1998.5 to 2000 (1.0's table said 40 low); the plinth row no longer claims a cable entry from below (review note). Part unchanged |
