# diverter · v1.0 · swing-arm diverter, own design, for a conveyor-roller 1.1 section: post on a 160 × 160 base with 4 × M12 anchor holes, arm 800 turning 0 to 45 degrees over the rollers

**What** A swing-arm diverter: it stands on the floor beside a roller conveyor section, outside its left side frame near the
section's upstream end, and sends the goods passing along the line over to its right-hand side. A base plate anchored to the floor
carries a post; on the post's top turns the arm, a hub with an 800 long, 100 high face. At rest the arm lies along the track outside
the left frame and the goods pass straight on; turned 45 degrees it lies across the track, and the goods running into its face slide
along it to the right-hand side, where the assembly places the branch line. It is the diverter of conveyor-types-bench, sorting-line,
outbound-conveyor, check-weigh-station and vision-inspection-station (lib/inventory.csv, 5 systems; request mech-13's answer: "an arm on
a pivot node on conveyor-roller's track; the cylinder placed in a later version").
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks diverter own_design "yes", core
watch 2026-11-12: no diverter class on file). No product was matched and no vendor file was opened; the folder's catalogue record (another
maker's right-angle transfer module, references/source.txt) is not what this element is, and no size is taken from it. The arm's place
and height come from conveyor-roller 1.1 (read with library.load, so the two cannot drift apart); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 at the conveyor section's centre (conveyor-roller's origin): x across the
conveyor, y along it, the goods travelling along +y. The pivot axis is vertical at x −340, y −650. Extents at rest x −420 to −260,
y −730 to 150, z 0 to 860.
**Built with** toolkit 1.3 · AutoLISP command `DIVERTER` · no parameters.

## Mechanism
`arm` (rotate about the vertical axis through (−340, −650), axis −z, 0 to 45 degrees, so it turns toward +x): the hub Ø80 (z 750 to
860) resting on the post's top, and the arm 10 × 800 × 100 (z 760 to 860) along +y from the pivot at rest. At 0 the arm's face is at
x −335, 35 outside the left frame's outer face (x −300): the track is clear. At 45 its tip's outer corner stands at x 229.2, y −87.9,
21 inside the right frame's inner face (x 250), and the arm lies across the whole track. Over the whole turn the arm's underside stays
at z 760, 10 above the rollers' tops (750) and 20 above the frames' tops (740), so it never meets the section; nothing of this element
lies in its path (MOT-010 sweeps it). The cylinder that turns it (its rod on a lug of the hub, its body on a bracket of the post), the
valve, and the sensors that read its two positions are placed in a later version once their elements are on file: none is drawn here,
so the arm turns without a visible actuator in the model.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| conveyor-roller 1.1 | the pivot axis 40 outside the left frame's outer face (x −300) and 100 from the section's upstream end (y −750); the post (x −370 to −310) 10 clear of the frame; the base plate (y −730 to −570) 20 clear of the section's foot plates (y −550) and inside its end; the arm's underside 10 above the rollers' tops (750) and 20 above the frames' tops (740); turned 45 its tip 21 inside the right frame's inner face (250) | conveyor-roller's TOP, W, FR_W, L, SUP_Y and PL_L (library.load); the section is placed by the assembly with its centre on this origin; element.py asserts both clearances |
| the floor | 4 × Ø13.5 holes in the base plate at 110 × 110 about the pivot axis | M12 clearance, ISO 273 medium H13 (lib/standards/holes.csv); position Ø1.0 at MMC to A the floor plane, B and C the planes through the pivot axis (ASME Y14.5 floating fastener, T ≤ H − F = 1.50; features.csv). The anchors are the assembly's |
| the branch line | none in this element | where the diverted goods leave the section (over the right frame, whose top is 10 under the rollers', or onto a line the assembly places there) is the assembly's |
| the cylinder | none in this element | the air cylinder, its mounting and ports come with the cylinder element, placed in a later version (OPERATING.md 12: a host doesn't model holes for a part it places later) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate | 160 × 160 × 12 (x −420 to −260, y −730 to −570, z 0 to 12), 4 × Ø13.5 anchor holes at 110 × 110 | the post's footing; the holes 25 from the plate's edges and clear of the post |
| post | 60 × 60, centred on the pivot axis, z 12 to 750 | carries the arm with its hub at the rollers' top height; the bearing inside the hub is not drawn |
| hub | Ø80, z 750 to 860 | the arm's root, resting on the post's top |
| arm | 10 thick, 800 from the pivot axis, face z 760 to 860 (100 high) | long enough that, turned 45, it spans the track; 10 above the rollers so it clears them; 100 high to guide goods taller than 10 |
| turn | 45 degrees toward +x | the arm across the whole track at an angle the goods slide along |
| finish | base and post painted; hub and arm safety yellow | appearance only: the yellow marks the moving part; no safety claim |

## Named nodes
`arm` (rotate, above). Colliders `base` (the base plate), `post`, `paddle` (the hub and arm as one box, at rest).

## Materials by layer
`M-STEEL-7035` the base plate and post (painted RAL 7035) · `M-YELLOW` the hub and arm.

## Notes
No load rating, no speed, force or cycle time: no goods mass, no air pressure and no cylinder figure are on file, so the diverter is not
sized against them. The volume is 4 310 049 mm³ by part (base 307 200 less four holes 6 871, post 2 656 800, hub 552 920, arm 800 000,
whose first 40 lie inside the hub; written as volume only: lib/materials.csv gives no densities, so no mass is stated). No vendor names,
no label.

## Outputs (out/)
`diverter.lsp` · `.glb` (pivot on `arm`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r113, unattended) |
