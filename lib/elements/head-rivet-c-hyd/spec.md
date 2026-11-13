# head-rivet-c-hyd · v1.2 · rivet setting head, own design, C-frame fixture driven by hyd-cylinder-da-40 1.1 placed, daylight 203, throat 60

**What** a rivet setting head, the fixture of the riveter (lib/inventory.csv row `head-rivet-c-hyd`, "pneumatic rivet setting head",
own_design yes, 1 system: riveter of lib/machines-factory.txt line 67: "frame-welded (own), cylinder, valve-sol-4way, frl,
head-rivet-c-hyd (new), footswitch (new), guard-panel (own), op-estop-22-2nc"). A C-frame: a column at the back, a lower arm carrying
the anvil (the lower die), an upper arm that seats the cylinder. The placed cylinder's rod carries the die cup with the upper die
and pushes it down the die axis onto the rivet standing on the anvil; the rod comes back up and the work is taken out of the
throat. The riveter mounts the head on its welded frame (the frame's underside is the mounting plane) and works it from its foot
switch through its valve; the head itself switches nothing.
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; the inventory row's own_design yes: core watch
2026-11-11, request pneu-11's answer item 3: "a cylinder-driven setting head is a fixture, not the hand-held tool EC004037
describes. It places a cylinder that is on file (a common part, OPERATING.md 12) and models its own body; the rivet sizes it
takes are design choices, written as such"). No vendor file was opened or measured; nothing was downloaded. What it meets takes its
figures from the element on file it places (hyd-cylinder-da-40 1.1, read through library.load); every other size is a design choice
(below). No vendor names; "complexes.org" on its label in a later version.
**Units / frame** mm, Z up. Origin: the frame's underside (the mounting plane z = 0) on the die axis (x = y = 0); the column at
−x, the throat open toward +x, the cylinder above with its rod down the die axis and its ports facing +x.
**Built with** toolkit 1.3 · AutoLISP command `HEAD-RIVET` · no parameters.

**The cylinder placed: hyd-cylinder-da-40 1.1** (bom.csv, tag `cyl`, version pinned; OPERATING.md 12, common parts: placed, never
redrawn, and a host places only common parts past station 6: hyd-cylinder-da-40 1.1 passed its three gates in pneu-r65). It is the one
plain double-acting cylinder on file: the riveter's own `cylinder` row (the pneumatic ISO 15552 cylinder) is not built, because
ISO 15552 is not on file (lib/standards/wanted.md), and the lane's two pneumatic cylinders on file are a stopper (conveyor-stop) and
a sheet clamp (clamp-sheet), neither a plain cylinder. So this head is hydraulic where the row says "pneumatic". For the
comparison only, with no claim of what a riveter needs: a Ø40 bore (rod Ø22) pushes 0.75 kN at 6 bar ("derived: derive.cylinder(40.0,
22.0, 6.0) (F = p A; v = Q / A)") and 20.1 kN at 160 bar ("derived: derive.cylinder(40.0, 22.0, 160.0) (F = p A; v = Q / A)",
hyd-cylinder-da-40 1.1's own class value). The riveter's air circuit (frl, valve-sol-52-sr) then drives an
air-over-oil unit or the pneumatic version comes as a sibling element, `head-rivet-c-pneu` (request pneu-13 item 2), with the ISO 15552 `cylinder` placed once ISO 15552 is on file and that cylinder is past station 6. The
choice and the row's word are put to the core and EM (lib/needs-em/pneu.md r87; report r87.md); the head's frame fits either
cylinder's seat as a design choice.

How it sits (every figure read from hyd-cylinder-da-40's element.py, so the seat cannot drift): the cylinder is rolled 90° about its own
y (toolkit/prims.py rotation_yp: its +x, the rod, turns to −z; its +z, the ports, to +x) and placed at z = 651.5 on the die axis.
Its head cap (60 square, its front face at its x = 300) seats flush on the upper arm's top face (z = 351.5: a placed instance
touches its host and never overlaps it, GEO-020; GEO-070 joins what touches); its gland nose (Ø36, its x 300 to 310) stands in the
arm's Ø38 bore (1 clear all round, z 341.5 to 351.5); its rod (Ø22) runs down through the bore to its plain end face at z = 311.5
(its x = 340 at rest, rod out 30), which the die cup's top face meets. No mounting holes or rod-end thread are used: both are
hyd-cylinder-da-40's open figures (ISO 6020-2, class B, its spec.md), so the seat is a face and a bore, and the die cup is pressed on the
rod's plain end (a design choice). The face-and-bore seat is a placeholder: it locates the cylinder and does not retain it. When oil
at `cyl.port-cap` drives the die down, the reaction on the cylinder's body is upward (up to the 20.1 kN above), and nothing in 1.x takes
it: the cylinder's mounting to the upper arm is open (Open figures; review head-rivet-1.0.md finding 1), drawn with the frame's holes
once hyd-cylinder-da-40 2.0 carries its ISO 6020-2 mounting (a major of this element, Notes). The cylinder's two ports `cyl.port-cap` (its x = 17.5: z = 634) and `cyl.port-rod` (its
x = 280: z = 371.5) face +x above the arm; their thread is hyd-cylinder-da-40's open figure (SAE J1926-1 table 1,
class B, its spec.md), not this element's.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| column | x −110 to −60 (50 thick), y ±50, z 0 to 351.5; painted steel (`M-STEEL-7035`) | the C-frame's back; the mounting plane is the frame's underside; no mounting holes in 1.0 (a later version, with features.csv rows) |
| lower arm | x −60.5 to 60 (0.5 into the column), y ±50, z 0 to 40 | carries the anvil holder; the throat is 60 deep from the die axis to the column's face |
| upper arm | x −60.5 to 60, y ±50, z 313.5 to 351.5 (38 thick) | the cylinder's seat: its head cap stands on the top face (5 of arm round the 60 cap, asserted); the Ø38 bore through it on the die axis takes the gland nose (Ø36 + 2 × 1 clearance) and the rod (features.csv, role own) |
| anvil holder | Ø40 × 20 on the lower arm (z 39.5 to 59.5, 0.5 into the arm); zinc-plated (`M-GALV`) | holds the lower die; 5 clear of the throat's end and the column (asserted) |
| anvil (lower die) | Ø16 × 10 (z 59 to 69, 0.5 into the holder), its face at z = 69; bright (`M-SILVER`) | the die the rivet's shop head stands on. Ø16 × 10 dies take solid rivets up to Ø6 by design (a design choice: no rivet size or setting force rating is claimed) |
| die cup | Ø30 × 30 under the rod's end (z 281.5 to 311.5; its top face on the rod's end face, touching), part of the rod's node `cyl.rod`; zinc-plated (`M-GALV`) | pressed on the plain rod end; its top 2 below the arm at rest (asserted ≥ 2) |
| upper die | Ø16 × 10 under the cup (z 272 to 282, 0.5 into the cup), its face at z = 272 at rest, part of `cyl.rod`; bright (`M-SILVER`) | the die that forms the head |
| daylight and gap | die face to anvil face 203 at rest = the stroke 200 + 3 | at full stroke the upper die stops 3 above the anvil (the least set-head height, a design choice): the dies never meet (element.py asserts), and MOT-010 sweeps the node clear; the cup at full stroke (z 81.5) clears the holder (59.5) |
| overall | envelope 170 × 100 × 651.5 (x −110 to 60, y −50 to 50, z 0 to 651.5: the cylinder's rear cap on top) | |

## Ports (toolkit/hyd.py)
The two port nodes are the placed cylinder's own, renamed with its tag (library.place): `cyl.port-cap` and `cyl.port-rod`, unit
hyd-port, female, role work, their spot faces facing +x at z = 634 and 371.5 (x = 31). Their thread, size and marks are
hyd-cylinder-da-40 1.1's open figures (its spec.md Open figures: SAE J1926-1 table 1; the ports' marks the trade's, ISO 9461 not on file)
and stay its: this element adds no figure to them and claims none. Oil into `cyl.port-cap` drives the die down, into `cyl.port-rod`
raises it; the riveter's valve and lines are its own elements. No air port, no electrical port.

## Open figures
- NOT ON FILE (B): the cylinder's mounting to the upper arm, which takes the setting reaction (ISO 6020-2 mounting styles, not on
  file; hyd-cylinder-da-40's open figure). Until it is on file the head as drawn locates the cylinder and does not hold it (How it sits).

Not claimed: a setting force, a rivet size or material, a cycle rate, a pressure. The force available
is the placed cylinder's own figure (hyd-cylinder-da-40 1.1 Class values: 20.1 kN push at 160 bar, derive.cylinder) and the pressure
the riveter's circuit sets; an own design states no rating of its own (OPERATING.md 12), so there is no ratings.csv. The cylinder's
own open figures (rod-end thread and port thread, class B) are its spec's and its board line's, not this element's (a placed
common part is never redrawn); its mounting is also this element's line above, since the head relies on it to hold the cylinder.

## Named nodes
`cyl.rod` (the cylinder's rod with the die cup and upper die on it): kind translate along −z, 0 to 200 (the stroke), at rest 0
(the die up, 203 above the anvil). `cyl.port-cap`, `cyl.port-rod` (the cylinder's spot faces): kind port, fixed (range 0). The
cylinder's other solids (caps, barrel, tie rods, gland) are the body's, seated on the arm. All three nodes are the placed part's:
their states and pose rows are hyd-cylinder-da-40 1.1's behaviour.csv, carried by the placed part (toolkit/behaviour.py: a placed element
carries its own spec; this element's behaviour.csv holds only the two pin rows that say what the ports do here).

## Materials by layer
`M-STEEL-7035` column, arms (and the cylinder's spot faces) · `M-GALV` anvil holder, die cup · `M-SILVER` dies (and the cylinder's
rod) · `M-CAST-BLUE` the cylinder's caps, barrel, gland · `M-ZINC` the cylinder's tie rods

## Decals (Blender)
None in 1.0 ("complexes.org" and a die-size mark are a later version). No vendor names, no approval marks.

## Notes
- A fixture, not a tool: the head switches nothing and holds no control; the foot switch, the valve, the guard and the e-stop are
  the riveter's elements (machines-factory.txt line 67). No safety function is claimed (the inventory row's `safety` column is
  empty); the pinch point between the dies is covered by the riveter's guard-panel, the machine's codes not on file.
- The placed cylinder's version is pinned in bom.csv (1.1); a hyd-cylinder-da-40 2.0 (its mounting and ports cut once ISO 6020-2 and
  SAE J1926-1 are on file) changes the seat here: a major of this element.
- The id head-rivet-c-hyd is OPERATING.md 6's (form C-frame, the hydraulic drive; request pneu-13 item 2, core round 31's rename
  of head-rivet). The row's type "pneumatic" and this head's hydraulic drive are put to EM in lib/needs-em/pneu.md r87.
- No mounting holes in 1.0 (the frame's underside is plain; a later version with features.csv rows, a major).

## Outputs (out/)
`head-rivet-c-hyd.lsp` · `.glb` (the rod node with its dies, the port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/,
step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design, pneu-r87 (unattended; request pneu-11's answer item 3): C-frame (column, lower arm with anvil holder and lower die, upper arm with the cylinder's seat bore Ø38), hyd-cylinder-da-40 1.1 placed (bom.csv tag `cyl`, z 651.5, rolled 90°, rod down the die axis, head cap flush on the upper arm), die cup and upper die under the rod's end face as part of `cyl.rod` (translate −z, 0 to 200), daylight 203, the dies 3 apart at full stroke; no ratings.csv; the cylinder's ports `cyl.port-cap` / `cyl.port-rod` and its rod's states and poses its own |
| 1.1 | text only, pneu-r90 (unattended; review head-rivet-1.0.md findings 1 (ESCAPE) and 2, pneu/r87.md): the cylinder's mounting to the upper arm written in Open figures as a class B line on ISO 6020-2 (hyd-cylinder-da-40's open figure the head relies on), "How it sits" and the docstring say the face-and-bore seat locates the cylinder and does not retain it; the Baseline's unsourced riveter force clause dropped, the Ø40 forces at 6 and 160 bar written as derived (derive.cylinder, the new source string); the id note read for the rename; valve-sol-4way read valve-sol-52-sr. No shape, node, origin or cut-out change |
| 1.2 | text only, pneu-r100 (unattended; review head-rivet-c-hyd-1.1.md finding 1, from head-rivet-c-hyd-1.0.md finding 3): the pneumatic sibling named `head-rivet-c-pneu` (request pneu-13 item 2), where the rename's retoken had made the sentence name this element. No shape, node, origin or cut-out change |
