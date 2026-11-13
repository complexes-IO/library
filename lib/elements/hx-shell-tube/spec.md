# hx-shell-tube · v1.0 · liquid-to-liquid heat exchanger, shell and tube, two tube passes, four NPT 3/8 female ports

**What** a liquid-to-liquid heat exchanger (lib/inventory.csv row `hx-shell-tube`, "heat exchanger", own_design yes, 2 systems:
heat-exchanger-loop and process-skid of lib/machines-from-elements.txt). One liquid enters `port-shell-in`, passes through the
shell round the tubes and leaves through `port-shell-out`; the other enters `port-tube-in` (the lower port on the tube-side
bonnet), runs through the tubes to the far bonnet and back, and leaves through `port-tube-out` (the upper port), so the tubes stay
full. Which liquid is the hot one is the loop's choice: the exchanger works either way, and the two flows run against each other
(the shell liquid toward −x, the tube liquid's first pass toward +x).
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; the inventory row's own_design yes: core watch
2026-11-11, request pneu-11's answer item 3, "EC002515 is the cabinet air/water cooler ... no liquid-to-liquid class or standard is
on file. A shell-and-tube or plate form is your design choice; its ports from the thread or flange contract on file; no ratings
until a standard is"). No vendor file was opened or measured: the folder's references/source.txt holds the reference part's record
(a brazed plate exchanger picked 2026-11-02, moved out of metadata.json by `build.py own hx-shell-tube --write` this round, DOC-007) and is
not used. Every port takes its figures from the thread contract on file (ASME B1.20.1, through toolkit/pneu.py); every size the
contract and the standards on file don't fix is a design choice (below). No vendor names; "complexes.org" on its label in a later
version.
**Units / frame** mm, Z up. Origin: the centre of the two feet's underside (the mounting plane z = 0); the shell's axis along x
at z = 90; the tube-side ports on the −x bonnet's end face, the shell-side ports on the shell's top. Ports follow pneu.py's port
frame: the pivot on each boss's outer face (where a placed male's hex seats), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `HX` · no parameters.

Shell and tube, not plate: a design choice (the answer leaves the form to the lane). The shell-and-tube form is hyd-cooler 1.0's,
already gated, with the oil side's spot faces replaced by two more NPT bosses: so the four ports are of one kind, the exchanger
stands on the same feet, and a loop joins it with the fittings on file (fitting-pushin 2.0 with an NPT 3/8 stub, or the piping the
skid chooses). A brazed plate form would be a sibling (OPERATING.md 6: the form in the id) if a machine asks for one.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| shell | Ø100 × 400 along x (x −200 to 200), its axis at z = 90; painted steel (`M-STEEL-7035`) | holds the tube bundle; the shell liquid passes round the tubes |
| bonnets | Ø110 × 40 on each end (x −240 to −199.5 and 199.5 to 240, 0.5 into the shell); cast (`M-ZINC-CAST`) | the −x one takes the tube liquid in and out (divided inside for the two passes), the +x one turns it round; 35 above the mounting plane (asserted ≥ 30) |
| shell-side port bosses | Ø28 on the shell's top at x = +130 (`port-shell-in`) and −130 (`port-shell-out`), y = 0, from z 136 (inside the shell across their whole width: the shell's surface is at z 138 under a boss's edge) to z 160, 20 above the shell's crown (z 140); `M-GALV` | a flat face for each shell-side port; 56 in from the shell's ends (asserted ≥ 20) |
| tube-side port bosses | Ø28 × 16 along −x on the −x bonnet's end face (x −256 to −239.5, 0.5 into the bonnet), at z = 65 (`port-tube-in`) and 115 (`port-tube-out`), y = 0; `M-GALV` | 22 apart and 16 in from the bonnet's edge (asserted ≥ 20 and ≥ 10); the inlet below so the liquid rises through the tubes |
| port bores | four, Ø17.055 × 12.358 deep, blind, one in each boss from its outer face | Ø = E1 + h of NPT 3/8 from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up (10.02) and 3 short of the boss's 16; a shell-side bore's floor (z 147.6) 7.6 above the shell's crown (asserted ≥ 3); 5.47 of boss wall (asserted ≥ 5). Role in features.csv (HOLE-010) |
| feet | two saddles 30 × 120 × 45 high under the shell at x = −150 and +150; black (`M-BLACK-PA`) | carry the shell 40 above the mounting plane; each holds the shell over 40 of its width (asserted); wider than the bonnets |
| tubes, tube sheets, baffles | not modelled | inside the shell |
| overall | envelope 496 × 120 × 160 (x −256 to 240, y −60 to 60, z 0 to 160) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-shell-in` | NPT3/8 | female | none (a liquid port) | the +x shell boss's top face, x = 130, z = 160, axis +z | pneu.py D1 (NPT, ASME B1.20.1); NPT 3/8 as coolant-pump's, chiller's and hyd-cooler 1.0's liquid ports; named by its function, no ISO 11727 number (that numbering is for pneumatic ports) |
| `port-shell-out` | NPT3/8 | female | none (a liquid port) | the −x shell boss's top face, x = −130, z = 160, axis +z | as `port-shell-in` |
| `port-tube-in` | NPT3/8 | female | none (a liquid port) | the lower bonnet boss's face, x = −256, z = 65, axis −x | as `port-shell-in` |
| `port-tube-out` | NPT3/8 | female | none (a liquid port) | the upper bonnet boss's face, x = −256, z = 115, axis −x | as `port-shell-in` |

NPT 3/8 is our choice within pneu.THREADS (D1). The ports are female and take sealant on the male (PNE-002). pneu.NPT holds the
size's figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 17.055, L2 = 10.358; each bore L2 + 2
deep. The helix is not modelled: each bore is the thread drawn plain. A male seated on a boss's face reaches L2 − 0.2 past the
face, inside the bore. No role: toolkit/pneu.py's roles are air roles, and an assembly leaves liquid ports out of its air joints
(hyd-cooler 1.0's water ports, lubrication-central-air-6 1.0's outlets).

## Open figures
None. Not claimed: a pressure (either side), a flow, a pressure drop, a heat transfer capacity or a temperature. An own design
states no rating of its own (OPERATING.md 12; request pneu-11's answer item 3, "no ratings until a standard is"), so there is no
ratings.csv; a rated version waits for the standard EM chooses in lib/standards/sources.csv (lib/needs-em/pneu.md r87). The
systems that place it size it from their heat load, which is each machine's figure.

## Named nodes
`port-shell-in`, `port-shell-out`, `port-tube-in`, `port-tube-out` (the bosses): kind port, fixed (range 0). Nothing moves.

## Materials by layer
`M-STEEL-7035` shell · `M-ZINC-CAST` bonnets · `M-GALV` port bosses · `M-BLACK-PA` feet

## Decals (Blender)
None in 1.0 (the flow arrows, the port names and "complexes.org" are a later version). No vendor names, no approval marks.

## Notes
- No mounting holes: the feet are plain in this version; their holes, with a clearance from lib/standards/holes.csv and a
  features.csv row, are a later version (a new cut-out, so a major).
- No drain or vent plug on the bonnets in this version.
- The twin reads no temperature from it: the liquids' temperatures come with a hydraulic and thermal model (behaviour.csv).
- The id is the inventory's; under OPERATING.md 6's convention it would carry its form (hx-shell-tube); it rides with request
  pneu-12 (the lane's ids), as lubrication-central-air-6's and pressure-washer-skid's do.
- No safety function (inventory.csv's `safety` column is empty for this row).
- Two systems carry it: heat-exchanger-loop and process-skid; both join it by its NPT ports to the piping they choose.

## Outputs (out/)
`hx-shell-tube.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design, pneu-r87 (unattended; request pneu-11's answer item 3): shell-and-tube liquid-to-liquid exchanger, shell Ø100 × 400 on two saddle feet, two bonnets; `port-shell-in` / `port-shell-out` on bosses on the shell's top and `port-tube-in` / `port-tube-out` on the −x bonnet, all female NPT 3/8 bored Ø (E1 + h) × (L2 + 2) deep, blind in their bosses; no ratings.csv; tubes, tube sheets and baffles not modelled; nothing placed; the reference part's record moved to references/source.txt (DOC-007) |
