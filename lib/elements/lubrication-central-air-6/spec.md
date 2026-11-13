# lubrication-central-air-6 · v1.0 · central lubrication unit, air-operated piston pump, oil reservoir, progressive distributor with 6 outlets, NPT 1/4 air, NPT 1/8 outlets

**What** the central lubrication unit of a machine tool (lib/inventory.csv row `lubrication-central-air-6`, "central lubrication unit
(pump, reservoir, distributor)", own_design yes, 2 systems: the vertical CNC mill and the machining centre of
lib/machines-factory.txt): it oils the ways and ballscrews from one reservoir. An oil reservoir stands on a base plate; the pump
head over it carries an air-operated single-acting piston pump (the air cylinder on top); a progressive distributor block in front
of the reservoir meters each pump stroke to six outlets, one per lubrication point. A pulse of air at `port-air` (the machine's
air line through its own valve, timed by the machine's control) drives the plunger one stroke and the spring returns it; each stroke
pushes a shot through the distributor to every outlet in turn, and the distributor's cycle indicator pin `indicator` steps out once
a cycle (the control can watch it with a sensor; none is placed here).
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; the inventory row's own_design yes: core watch
2026-11-11, request pneu-11's answer item 1, "no ETIM class and no standard on file: no ratings of its own until one is"). No vendor
file was opened or measured. What it meets takes its figures from the pneumatic contract on file, `toolkit/pneu.py` (D1 threads;
pneu.NPT, ASME B1.20.1 by its formulas, for every bore); every size the contract and the standards on file don't fix is a design
choice (below). No vendor names; "complexes.org" on its label in a later version.
**Units / frame** mm, Z up. Origin: the centre of the base plate's underside in x, the reservoir's centre in y, on the mounting
plane (z = 0); the outlets face −y (the front), the air port up (+z), the cycle indicator pin out of the distributor's +x end.
Ports follow pneu.py's port frame: the pivot on the port's field's outer face (0.2 out from the end face, where a placed male's
hex seats), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `LUBRICATION-CENTRAL` · no parameters.

Air-operated, not motor-driven: the inventory row names a pump, a reservoir and a distributor and no drive. The air contract is on
file (pneu.py) and a motor's rating is what the core's answer rules out for this row until a standard is in sources.csv, so the
pump is driven by the machine's compressed air (a single-acting air piston on an oil plunger: one air port, no electrical port,
nothing the ELR checks read). A motor-driven sibling with a `pwr` port is a later rated version or a sibling element, once a
standard is on file (EM's document choice, lib/needs-em/pneu.md r86).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate | 200 (x, −100 to 100) × 160 (y, −95 to 65) × 10, painted steel, z 0 to 10 | carries the reservoir and the distributor; the mounting plane is its underside; no anchor holes in 1.0 (a later version, with features.csv rows) |
| reservoir | 120 (x) × 100 (y) × 160 (z), clear polymer (`M-CASE-CLEAR`), centred on x = 0, y = 0, z 9.5 to 169.5 (0.5 into the plate) | 1.92 l gross; the oil level is seen through it; the oil, the suction strainer and the level float are not modelled |
| pump head | 136 × 116 × 40 over the reservoir (8 overhang all round), aluminium, z 169 to 209 | holds the plunger pump (inside, not modelled), the filler and the air cylinder |
| air cylinder | Ø50 × 70 on the head's top, centred, aluminium, z 208.5 to 278.5 | the single-acting air piston that drives the plunger; its cap carries `port-air` |
| `port-air` bore | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, down the cylinder's axis from its cap face (z = 278.5) | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0; tank 2.0's rule), deeper than a male's make-up L1 + L3 (10.02); 18.19 of wall round it; 57.8 of cylinder under its floor (element.py asserts ≥ 10). Declared in features.csv |
| filler cap | Ø30 × 14 on the head's top at x = 48, y = 30; black | fills the reservoir; a breather in it is not modelled |
| distributor block | 110 (x, −55 to 55) × 26 (y, −88 to −62) × 46 (z 9.5 to 55.5), zinc-plated steel, on the plate in front of the reservoir (12 clear of it) | the progressive metering block; its pistons and the pump's feed line into it are not modelled |
| outlet bores | six, Ø10.242 plain (E1 + h of NPT 1/8), 8.702 deep (L2 + 2), blind, into the block's front face (y = −88) at x = −40, −24, −8, 8, 24, 40 (pitch 16), z = 32.75 | one per lubrication point; 5.76 of wall between bores, 17.88 above and below, 17.3 of floor (asserted ≥ 5). Declared in features.csv |
| port fields | 18 × 18 on the cylinder's cap round `port-air`; 14 × 14 round each outlet; 0.2 proud, the bore through each; `M-WHITE-PA` | each port's number is a decal; 0.2 proud for GEO-050; each port's pivot on its outer face (filter-air 3.0's rule) |
| cycle indicator pin | Ø6 × 8 on the block's +x end face (x = 55), at y = −75, z = 32.75, face to face; silver | `indicator`, translate +x 0 to 4 once a cycle |
| overall | envelope 200 × 160 × 278.7 (x −100 to 100, y −95 to 65, z 0 to 278.7) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-air` | NPT1/4 | female | work | pneu.py D1 (NPT, ASME B1.20.1); pivot at z = 278.7 (the field's outer face), axis +z. The pump's air pulse comes from the machine's valve: a working line (role work, as clamp-sheet's `port-cap`), never the supply itself |
| `port-out-1` … `port-out-6` | NPT1/8 | female | none | pneu.py D1; pivots at y = −88.2 (the fields' outer faces), axis −y. Oil, not air: a fitting-pushin (NPT 1/8 stub, 5/32 tube) screws into each and the oil tube runs to its point; NPT is the thread contract on file for the lane's liquid ports too (tank, coolant-pump, hyd-cooler's water ports), so the unit reads as the thread, and an assembly leaves these outlets out of its air joints |

NPT 1/4 and NPT 1/8 are our choices within pneu.THREADS. The ports are female and take sealant on the male (PNE-002). pneu.NPT holds
each size's figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): NPT 1/4 E1 + h = 13.616, L2 = 10.205;
NPT 1/8 E1 + h = 10.242, L2 = 6.702; each bore L2 + 2 deep. The helix is not modelled: each bore is the thread drawn plain. A male
seated on a field's face reaches L2 − 0.2 past the end face, inside the bore.

## Open figures
None. Not claimed: a pressure, a shot volume, a cycle rate, a flow or an outlet count per class. An own design states no rating of
its own (OPERATING.md 12; request pneu-11's answer item 1), so there is no ratings.csv, and in an assembly PNE-003 gives REVIEW
(rating not on file) for `port-air` until a figure for our unit is on file. The air pulse the pump needs is below the bench
regulator's range by design (a single-acting piston works from any line pressure the contract allows); no figure is written.

## Named nodes
`indicator` (the distributor's cycle indicator pin): kind translate along +x at the block's +x end face, 0 to 4, at rest 0 (seated:
a cycle not yet complete). `port-air`, `port-out-1` to `port-out-6` (kind port, fixed; range 0; each the field with its pivot on the
field's outer face).

## Materials by layer
`M-STEEL-7035` base plate · `M-CASE-CLEAR` reservoir · `M-ALU-ANOD` pump head, air cylinder · `M-BLACK-PA` filler cap · `M-GALV`
distributor block · `M-SILVER` cycle indicator pin · `M-WHITE-PA` port fields

## Decals (Blender)
None in 1.0 (the outlet numbers 1 to 6, "AIR" on the cylinder's cap, the oil level marks and "complexes.org" are a later version).
No vendor names, no approval marks.

## Notes
- One element: the pump, the reservoir and the distributor are one unit on one plate (the inventory row's three parts), as the
  machines list one `lubrication-central-air-6` each. A machine with more points places a second distributor: a later version or a
  sibling.
- Nothing placed: fitting-pushin screws into each outlet in the assembly (made_of is empty on the row; the fitting is the
  machine's); a sensor for the indicator pin, a low-level switch and a solenoid valve for the air pulse are the machine's elements.
- Inside nothing is modelled: the plunger, spring, check valves, the suction strainer, the metering pistons, the feed line, the oil.
- The id is the inventory's; under OPERATING.md 6's convention it would carry its drive and outlet count (lubrication-central-air-6);
  request pneu-12 asks the core about the lane's ids and this one rides with it (needs-em r86).
- No safety function (inventory.csv's `safety` column is empty for this row).

## Outputs (out/)
`lubrication-central-air-6.lsp` · `.glb` (indicator and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/,
gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design, pneu-r86 (unattended; request pneu-11's answer item 1): base plate, clear reservoir, pump head, air cylinder with `port-air` (female NPT 1/4 bored Ø (E1 + h) × (L2 + 2) deep from pneu.NPT), filler cap, progressive distributor with `port-out-1` to `port-out-6` (female NPT 1/8 bored the same way), cycle indicator pin `indicator` (translate, 4 mm); no ratings.csv; plunger, spring, metering pistons and oil not modelled; nothing placed |
