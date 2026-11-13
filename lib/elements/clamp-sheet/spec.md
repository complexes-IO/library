# clamp-sheet · v1.0 · pneumatic sheet clamp, generic, turret punch, single acting, jaw opening 8, NPT 1/8 female

**What** a turret punch's sheet clamp: a C-shaped body whose back face is screwed to the punch's carriage, a fixed lower jaw the
sheet's edge rests on, and an upper jaw that a single-acting piston in the upper arm presses down onto the sheet. Air into
`port-cap` (on the arm's top) closes the jaw; when the air is let out, a spring inside lifts it. The carriage then moves the sheet
under the punch by its clamped edge. The punch carries three of them (lib/machines-factory.txt, punch-turret: "clamp-sheet (x3)"),
each placed by the machine. lib/inventory.csv row `clamp-sheet` (own_design generic, "pneumatic sheet clamp (turret punch)"; 1
system: punch-turret).
**Class** actuator · **Baseline** our own design: generic Gripper (pneumatic/hydraulic) (ETIM 10.0 EC004755), as OPERATING.md 12
(generic elements, EM 2026-11-07) and the inventory row say. No vendor file was opened or measured. The class values below are its
design inputs; its sizes are design choices; its air port takes its thread from the standard on file (ASME B1.20.1, through
toolkit/pneu.py). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the clamping plane, the fixed lower jaw's top face (z = 0) at its front edge (x = 0), centred
across the clamp (y = 0); the body behind (−x), the mouth open toward +x (the sheet's edge enters from +x), the port up (+z).
**Built with** toolkit 1.3 · AutoLISP command `CLAMP-SHEET` · no parameters (one size).

The class: the inventory row names none (next.md asked to check EG020054 "Clamping tools" first). EC004755 "Gripper
(pneumatic/hydraulic)" is the one class of that group with a pneumatic drive (its synonyms "Pneumatic gripper", "Hydraulic
gripper"; 3 features on file): a powered jaw that holds a workpiece, which a turret punch's sheet clamp is. The group's other
clamps are hand tools (toggle, screw, spring and glue clamps, vices) with no drive. It is the class mech's gripper row uses for a
robot's parallel gripper; the class covers both, and the class values say which this is.

## Class values (ETIM 10.0 EC004755, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF001422 Type of drive | pneumatic, single acting, spring return (air closes the jaw, the spring opens it) |
| 2 | EF009111 Number of arms | 2: the fixed lower jaw and the moving upper jaw |
| 3 | EF013335 Holding force | 444 N: P_WORK_MAX (80 psig, 551.6 kPa, pneu.py D3) on the Ø32 piston's 804.2 mm² (element.py hold_n; theoretical, the spring's force and friction not deducted) |

The holding force is a generic design value (OPERATING.md 12), not a tested rating; it is taken at the bench regulator's highest
setting, the most air a circuit on the library's benches gives it. No check reads it (behaviour.csv carries it as a limit row).

**No safety claim.** The jaw closing on the sheet is a pinch point at the punch's carriage; guarding it is the punch's (its guard
and its codes, not on file here). This element claims no safety function (OPERATING.md 12; inventory `safety` empty).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| back column | 30 (x, −70 to −40) × 50 (y) × 90 (z, −30 to 60) | its back face (x = −70) meets the carriage; the fixing holes are not cut (Notes) |
| fixed lower jaw | 40.5 × 50 × 30 (x −40.5 to 0, z −30 to 0), 0.5 into the column | its top face is the clamping plane the sheet rests on |
| upper arm | 40.5 × 50 × 30 (x −40.5 to 0, z 30 to 60), 0.5 into the column | holds the piston Ø32 (not modelled; 9 of wall across y, at least 4 along x, asserted ≥ 3) and the rod's bore |
| rod bore | Ø13 up the arm from its underside to z = 56, blind, on x = −20 (features.csv) | 0.5 clear round the rod (it never touches the arm at rest or through its travel) |
| piston rod | Ø12, z 19.5 to 55 at rest, on x = −20; chromed (`M-SILVER`) | 25 in the bore at rest, 17.5 at full stroke (≥ 1 × Ø, asserted) |
| upper jaw | 26 (x −33 to −7) × 30 (y −15 to 15) × 12 (z 8 to 20 at rest), the rod 0.5 into it; grey steel | its face 8 above the plane at rest: the mouth's opening |
| stroke | 7.5 | the jaw stops 0.5 above the lower jaw: it holds sheet from 0.5 to 8 thick (asserted: never reaches the lower jaw) |
| port boss | Ø18 × 12 proud on the arm's top (z 59.5 to 72), on x = −20 | a half coupling for a female NPT 1/8: 3.9 of metal round the pipe OD (10.3), 12 proud, more than a male's make-up (L1 + L3, 6.9) plus 2 (asserted) |
| port bore | Ø10.242 (E1 + h) × 8.702 (L2 + 2) deep, blind, from the boss face z = 72 down to 63.3 (features.csv) | the thread drawn plain at the male stub's own diameter (tank 2.0's rule), so silencer 1.0's or another male NPT 1/8 stub meets it face to face; 3.88 of wall |
| overall | envelope 70 × 50 × 102 (x −70 to 0, y −25 to 25, z −30 to 72) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-cap` | NPT1/8 | female | work | the boss face (−20, 0, 72), axis +z | pneu.NODES cylinder end ("port-cap": air in drives the piston out, here the jaw down); the only port (single acting); NPT 1/8, pneu.py D1 (ASME B1.20.1), the smallest of pneu.THREADS, as vacuum's ports |

pneu.NPT holds NPT 1/8's figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 10.242 (the bore),
L2 = 6.702 (the bore is L2 + 2 deep), L1 + L3 = 6.925 (a male's make-up). The helix is not modelled. PNE-002 pairs it with a male
NPT 1/8 (sealant on the male, D1); a 3/2 valve's work port feeds it, and its exhaust lets the spring open the jaw.

## Open figures
- NOT ON FILE (A): the clamp's max. operating pressure. EC004755 has no pressure feature (its three are above), and ASME B1.20.1
  states no pressure, so ratings.csv holds no p_max; it is a maker's tested figure. In an assembly PNE-003 REVIEWs the clamp until EM
  gives a source or a figure (vacuum 1.0's case). It sits on a valve's work port, which carries up to P_SUPPLY (100 psig, pneu.py D3).

Every other figure is a design choice, a class value above, or from the standard on file.

## Named nodes
`jaw` (the upper jaw and its rod): kind translate along −z, 0 to 7.5 (the stroke), at rest open; the twin moves it by the stroke it
reads. Through its travel the rod stays in its Ø13 bore (0.5 clear) and the jaw stays 0.5 above the lower jaw. `port-cap` (the
boss): kind port, fixed (range 0).

## Materials by layer
`M-CAST-BLUE` column, lower jaw, upper arm · `M-STEEL-7035` upper jaw · `M-SILVER` piston rod · `M-GALV` port boss

## Decals (Blender)
None in 1.0 (the "generic" label is a later version). No vendor names, no approval marks.

## Notes
- The body's fixing holes (to the carriage) are not cut: holes need their features.csv roles (HOLE-010) and the screws that pass
  them (screw-iso4017) are common parts not yet built. Cutting them is a major version, once the screws are past station 6.
- The jaws' faces are plain (no serrations or inserts): appearance and grip the twin doesn't read.
- The piston, the spring and the seals inside the arm are not modelled; the piston's Ø32 sets only the holding force.

## Outputs (out/)
`clamp-sheet.lsp` · `.glb` (jaw and port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004755), pneu-r72 (unattended): C-shaped body (column, fixed lower jaw, upper arm), `jaw` (upper jaw and rod, translate −z, stroke 7.5), port boss `port-cap` female NPT 1/8 bored at E1 + h × (L2 + 2); single acting, spring return, 444 N at P_WORK_MAX; the max. operating pressure one open class A line; the piston, spring and seals not modelled; no fixing holes; nothing placed |
