# conveyor-stop · v1.0 · pneumatic conveyor stop, generic, single acting spring extended, bore 32, stroke 25, NPT 1/8 female

**What** a roller conveyor's stop (a stopper cylinder): a square cylinder body hung under the conveyor frame by its top flange, with
a rod and a stop head that stand up between two rollers and hold a pallet or a package back. Single acting, spring extended: at
rest the spring inside holds the head up (the stop closed); air into `port-rod` pulls the head down below the rollers and the load
passes; when the air is let out, the spring raises it again for the next load. lib/inventory.csv row `conveyor-stop` (own_design
generic, "pneumatic conveyor stop (stopper cylinder)"; 1 system: conveyor-types-bench, lib/machines-from-elements.txt), placed by
the conveyor that needs it.
**Class** actuator · **Baseline** our own design: generic Pneumatic cylinder (ETIM 10.0 EC011632), as OPERATING.md 12 (generic
elements, EM 2026-11-07) and the inventory row say. No vendor file was opened or measured; this folder's metadata.json and
references/ (a product picked 2026-11-02) were not used, and every size below is our own. The class values below are its design
inputs; its sizes are design choices; its air port takes its thread from the standard on file (ASME B1.20.1, through
toolkit/pneu.py). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the mounting plane, the flange's top face (z = 0), on the rod's axis (x = y = 0); the body
hangs below (−z), the rod and its stop head stand up (+z), the port faces +x. The load comes along the conveyor; which side of the
head it meets is the conveyor's placement (the head is square to x and y).
**Built with** toolkit 1.3 · AutoLISP command `CONVEYOR-STOP` · no parameters (one size).

The class: the inventory row names none. EC011632 "Pneumatic cylinder" (group EG015640, 3 features on file) is the class
classes.csv gives the lane's cylinder rows (cyl-iso15552, cyl-iso6432, cylinder); a stopper is a pneumatic cylinder whose rod end
is a stop head. Not an ISO cylinder: OPERATING.md 12 never builds a part generic whose shape a dimensional standard fixes (ISO
cylinder interfaces), and this element uses none of them: its flange, body and head are no ISO 15552 or ISO 6432 mounting
interface or rod-end thread (pneu-1 D5), and lib/standards/sources.csv holds no standard for stop cylinders. So its shape is a
design choice, said so below.

## Class values (ETIM 10.0 EC011632, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF000065 Inner diameter | 32 mm (the piston's bore, not modelled) |
| 2 | EF021866 Stroke length | 25 mm (the head's travel from up to down) |
| 3 | EF022580 Dual-action | no: single acting, spring extended (air pulls the rod in, the spring pushes it out) |

The pull-in force at P_WORK_MAX (80 psig, 551.6 kPa, pneu.py D3) on the piston's rod-side annulus, π (32² − 16²) / 4 = 603.2 mm²,
is 333 N (element.py retract_n; theoretical, the spring's force and friction not deducted): a generic design value, not a tested
rating, and no check reads it.

**No load claimed.** How heavy a load the head stops, and at what conveyor speed, is a maker's tested figure that no class feature
and no standard on file gives: this design claims none (as vacuum 1.0 claims no holding force). A conveyor that places it
sizes the stop for its loads.

**No safety claim.** The head rising under a load and a load stopped against it are the conveyor's hazards and guarding (its
codes, not on file here). Spring extended means the stop closes when the air is lost: a design choice for holding the line, not a
safety function this element claims (OPERATING.md 12; inventory `safety` empty).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| top flange | 70 (x) × 90 (y) × 10 (z −10 to 0), zinc-plated steel | screwed under the conveyor frame's cross member; its top face is the mounting plane; the fixing holes are not cut (Notes) |
| body | 50 × 50 square, z −100 to −9.5 (0.5 into the flange), anodised aluminium | holds the piston Ø32 (9 of wall, asserted ≥ 6) and the spring below it |
| rod guide | Ø28 × 10.5 on the flange's top (z −0.5 to 10) | the rod's guide above the flange: 5.5 of wall round its bore |
| rod bore | Ø17 down the guide, through the flange and into the body to z = −61, blind (features.csv; one hole per solid) | 0.5 clear round the rod (it never touches the guide at rest or through its travel) |
| piston rod | Ø16, z −30 to 45.5 at rest, chromed (`M-SILVER`) | 40 in its bore at rest (asserted ≥ 2 × Ø); at full stroke its lower end at −55, 6 above the bore's floor (asserted ≥ 5) |
| stop head | 20 (x) × 36 (y) × 15 (z 45 to 60 at rest), the rod 0.5 into it; grey steel | the face a load meets; retracted (z 20 to 35) it stays 10 above the guide (asserted ≥ 5) |
| stroke | 25 | class value 2 |
| port boss | Ø20 × 3 on the body's +x face (x 24.5 to 28), at z = −25; zinc-plated steel; the `port-rod` node | a spot face a male NPT 1/8 hex (AF 14, corners Ø15.68) seats on; its top (z −15) 5 below the flange (asserted ≥ 3) |
| port bore | Ø10.242 (E1 + h) × 8.702 (L2 + 2) deep from the boss face x = 28 to 19.3, blind, through the boss into the body (features.csv) | the thread drawn plain at the male stub's own diameter (tank 2.0's rule); its floor 10.8 clear of the rod's bore (asserted ≥ 3) |
| overall | envelope 70 × 90 × 160 (x −35 to 35, y −45 to 45, z −100 to 60) at rest | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-rod` | NPT1/8 | female | work | the boss face (28, 0, −25), axis +x | pneu.NODES cylinder end ("port-rod": air in drives the piston in, here the head down); the only port (single acting); NPT 1/8, pneu.py D1 (ASME B1.20.1), the smallest of pneu.THREADS, as clamp-sheet's |

pneu.NPT holds NPT 1/8's figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 10.242 (the bore),
L2 = 6.702 (the bore is L2 + 2 deep), L1 + L3 = 6.925 (a male's make-up). The helix is not modelled. PNE-002 pairs it with a male
NPT 1/8 (sealant on the male, D1); a 3/2 valve's work port feeds it, and its exhaust lets the spring raise the head. The body
breathes through its spring side (a vent, not modelled).

## Open figures
- NOT ON FILE (A): the stop's max. operating pressure. EC011632 has no pressure feature (its three are above), and ASME B1.20.1
  states no pressure, so ratings.csv holds no p_max; it is a maker's tested figure. In an assembly PNE-003 REVIEWs the stop until EM
  gives a source or a figure (clamp-sheet 1.0's case). It sits on a valve's work port, which carries up to P_SUPPLY (100 psig,
  pneu.py D3).

Every other figure is a design choice, a class value above, or from the standard on file.

## Named nodes
`rod` (the stop head and its rod): kind translate along −z, 0 to 25 (the stroke), at rest up (the stop closed); the twin moves it
by the stroke it reads. Through its travel the rod stays in its Ø17 bore (0.5 clear) and the head 10 or more above the guide.
`port-rod` (the port boss): kind port, fixed (range 0).

## Materials by layer
`M-ALU-ANOD` body, rod guide · `M-GALV` top flange, port boss · `M-SILVER` piston rod · `M-STEEL-7035` stop head

## Decals (Blender)
None (the "generic" label is a later version). No vendor names, no approval marks.

## Notes
- The flange's fixing holes (to the conveyor frame) are not cut: holes need their features.csv roles (HOLE-010) and the screws that
  pass them (screw-iso4017) are common parts not yet built. Cutting them is a major version, once the screws are past station 6.
- The piston, the spring, the seals and the vent inside the body are not modelled; the piston's Ø32 sets only the pull-in force.
- No sensor slot: a stop's "load present" or "head down" sensing is the conveyor's (a later version, with a sensor element on file).
- The head is a plain block (no roller, no damper): a damped or roller head is another design, not this one.

## Outputs (out/)
`conveyor-stop.lsp` · `.glb` (rod and port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011632), pneu-r73 (unattended): square body under a top flange, rod guide, `rod` (stop head and rod, translate −z, stroke 25, spring extended at rest), port boss `port-rod` female NPT 1/8 bored at E1 + h × (L2 + 2); single acting, 333 N pull-in at P_WORK_MAX; the max. operating pressure one open class A line; no load claimed; the piston, spring and seals not modelled; no fixing holes; nothing placed |
