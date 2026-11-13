# damper · v1.0 · rectangular air damper, own design, for fan-exhaust 1.0's discharge: 200 × 230 casing, flanges with 4 × M8 at its pattern, three blades turning 0 to 90 degrees

**What** A rectangular multi-blade air damper: it sits on the exhaust fan's discharge flange and sets how much air the fan pushes up the
exhaust duct. A short casing the size of the fan's discharge duct carries a flange at each end, the bottom one drilled to the fan's
flange, the top one the same for the exhaust duct; inside, three flat blades, each on its own axle across the casing, turn together
from closed (flat across the airway) to open (on edge along the flow). It is the damper of hvac-trainer and ventilation-industrial
(lib/inventory.csv, 2 systems; request mech-13's answer: "our own design ... no air damper class on file (EC003372 Flap valve is a
fluid valve); no airflow or leakage rating claimed").
**Class** machine · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks damper own_design "yes", core watch
2026-11-12). No product was matched and no vendor file was opened; the folder's catalogue record (another maker's round motorized duct
damper, references/source.txt) is not what this element is, and no size is taken from it. The casing's section, both flanges and their
hole pattern come from fan-exhaust 1.0 (read with library.load, so the two cannot drift apart); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the bottom flange's underside (z = 0) at the airway's centre; the axles run along x, the blades sit
side by side along y, the air flows along +z. Placed on fan-exhaust, this origin goes to (0, −125, 875) in the fan's frame (its
discharge flange's top face over its duct's centre line). Extents x −130 to 130, y −145 to 145, z 0 to 150.
**Built with** toolkit 1.3 · AutoLISP command `DAMPER` · no parameters.

## Mechanism
`blade-1`, `blade-2`, `blade-3` (each rotate about its own axle along x, axis +x through (0, y, 75) at y −70, 0 and 70; 0 to 90 degrees):
each blade 176 × 64 × 2 on an axle Ø10. At 0, as built, the blades lie flat across the airway (closed), 6 apart edge to edge and 3 from
the casing's y walls; at 90 they stand on edge along the flow (open). A blade's corners turn on a radius of 32.02 about its axle: 5.98
clear of a closed neighbour's edge, far clear of an open one's face, 2.98 clear of the casing's y walls, and inside the casing's height
(z 42.98 to 107.02); its ends stay 2 from the x walls and its axle turns in a Ø12 bore, so no blade meets anything over its whole turn
whatever the others do (MOT-010 sweeps each node with the rest still). In service the three turn together; the linkage that couples
them (crank arms on the axles' +x stubs and a link bar) and the actuator that turns them come in a later version once their elements are
on file: none is drawn here, so each blade turns on its own in the model.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| fan-exhaust 1.0, its discharge | the casing 200 × 230 outside with 10 walls, the airway 180 × 210, as the fan's discharge duct; the bottom flange 260 × 290 × 15 on the fan's flange of the same size, the airways in line | fan-exhaust's DUCT_X, DUCT_Y0, DUCT_Y1, DUCT_W, FL_X, FL_Y0, FL_Y1, FL_T (library.load); the assembly places this origin at (0, −125, 875) in the fan's frame |
| the screws to the fan and to the exhaust duct | 4 × Ø9 in each flange at x ±115, y ±130 (fan-exhaust's pattern) | M8 clearance, ISO 273 medium H13 (lib/standards/holes.csv); the pattern from fan-exhaust's FL_HOLE_X, FL_HOLE_Y (library.load); position Ø1.0 at MMC to A the bottom flange's underside, B and C the planes x = 0 and y = 0 (ASME Y14.5 floating fastener, T ≤ H − F = 1.00; features.csv). The screws, and any gasket between the flanges, are the assembly's |
| the exhaust duct | the top flange the same 260 × 290 with the same 4 × Ø9 as fan-exhaust's discharge flange | the duct is the assembly's; it meets this flange as it would meet fan-exhaust's (fan-exhaust 1.0, library.load) |
| the linkage and the actuator | none in this element; the axles stand 20 out of the casing's +x wall for them | placed in a later version once their elements are on file (OPERATING.md 12: a host doesn't model holes for a part it places later) |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| height | 150: flange 15, casing 120 (z 15 to 135), flange 15 | room for the blades' turn (z 42.98 to 107.02) inside the casing |
| blades | three, 176 × 64 × 2, axles at y −70 / 0 / 70 (pitch 70), z 75 | three across the 210 airway; each 64 wide so it turns clear of its neighbours and the walls; 2 thick sheet |
| axles | Ø10, from 0.5 proud of the −x wall to 20 out of the +x wall, in Ø12 bores through both x walls | 1 radial clearance; the +x stubs carry the linkage later; no bearing drawn |
| turn | 0 (closed) to 90 degrees (open) | flat across the airway to on edge along the flow |
| finish | casing and flanges galvanized steel; blades and axles zinc-plated | appearance only |

## Named nodes
`blade-1`, `blade-2`, `blade-3` (rotate, above). Colliders `flange-bottom`, `casing`, `flange-top`.

## Materials by layer
`M-GALV` the flanges and casing · `M-ZINC` the blades and axles.

## Notes
No airflow, pressure drop, leakage class, torque or temperature rating: no air figure for the damper and no actuator are on file, so it
is not sized against them, and the 6 between closed blades is open area, not a seal. The volume by part: each flange 560 183 mm³
(564 000 less four Ø9 holes 3 817), the casing 977 214 mm³ (984 000 less six Ø12 bores through the 10 walls 6 786), each blade 22 528
mm³, each axle 17 319 mm³ (a little of it inside its blade); written as volume only: lib/materials.csv gives no densities, so no mass is
stated. No vendor names, no label.

## Outputs (out/)
`damper.lsp` · `.glb` (pivots on `blade-1` to `blade-3`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r114, unattended) |
