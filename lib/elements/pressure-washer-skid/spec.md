# pressure-washer-skid · v1.0 · pressure washer, stationary cold water, motor and triplex plunger pump on a skid, unloader, NPT 3/8 inlet and outlet

**What** a stationary cold-water pressure washer for a parts-cleaning cell (lib/inventory.csv row `pressure-washer-skid`, "pressure
washer", own_design yes, 1 system: the industrial cleaner of lib/machines-factory.txt, beside the parts washer, pump, oven, tank
and industrial vacuum). A skid plate on four rubber feet carries a horizontal three-phase motor close-coupled through a bell flange
to a triplex plunger pump; the pump's manifold head takes the water in at `port-in` (the front) and delivers it at `port-out` (the
+x end) to the cell's high-pressure hose and lance; the unloader valve on the head returns the flow to the inlet side when the lance
is shut (its knob is fixed in 1.x).
**Class** device · **Baseline** our own design (OPERATING.md 12, own designs; the inventory row's own_design yes: core watch
2026-11-11, request pneu-11's answer item 1, "no ETIM class and no standard on file: no ratings of its own until one is"). No vendor
file was opened or measured. What it meets takes its figures from the pneumatic contract's threads on file, `toolkit/pneu.py` (D1;
pneu.NPT, ASME B1.20.1 by its formulas, for the bores); every size the contract and the standards on file don't fix is a design
choice (below). No vendor names; "complexes.org" on its label in a later version.
**Units / frame** mm, Z up. Origin: the centre of the skid plate in x and y, on the feet's underside (the floor, z = 0); the motor
toward −x, the pump head and `port-out` toward +x, `port-in` on the head's front (−y) face, the unloader up (+z). Ports follow
pneu.py's port frame: the pivot on the port's field's outer face (0.2 out from the end face, where a placed male's hex seats), its
axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `PRESSURE-WASHER` · no parameters.

The motor is the unit's own body, not the inventory's motor-iec71-370w placed (the row has no made_of, and a washer's pump wants
more than 0.37 kW); no IEC frame figure is used (IEC 60072-1 is not in sources.csv) and no measured motor is copied. It has no
electrical port in 1.0: a motor rating (power, voltage, current) is what the core's answer rules out for this row until a standard
is on file, there is no ratings.csv, and an unrated `pwr` port would make the ELR checks read a current the file doesn't hold
(hpu-0.37kw's `pwr` carries fla from a motor on file; here none is). The terminal box is drawn; the cable entry, `pwr` and pins.csv
come with the rated version (a new node: a major), once EM chooses the standard (lib/needs-em/pneu.md r86).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| skid plate | 560 (x) × 300 (y) × 8, painted steel, z 19.5 to 27.5, centred | carries the motor and the pump; no anchor or lifting holes in 1.0 |
| rubber feet | four, Ø30 × 20 under the plate, 30 in from its corners (x ±250, y ±120), z 0 to 20 (the plate 0.5 into them); black | stand the skid on the cell's floor; set in so no face is flush with the plate's edge (GEO-050) |
| motor foot block | 220 (x, −230 to −10) × 120 (y) × 32 on the plate, z 27 to 59; blue | the motor's feet, one block |
| motor body | Ø160, x −240 to 20, axis y = 0, z = 138.5 (0.5 into the foot block); blue | a three-phase motor's envelope as drawn here is our own (no frame figure used) |
| fan cowl | Ø150 × 40 on the motor's −x end (x −279.5 to −239.5) | the fan, air drawn in from −x |
| terminal box | 70 (x, −160 to −90) × 60 (y) × 50 on the motor's top, z 218 to 268; blue | the motor's terminals; no entry drawn in 1.0 (Notes) |
| bell flange | Ø130 × 24 on the motor's +x end (x 19.5 to 43.5), aluminium | the close coupling: the pump's crankcase bolts to it; the shaft and coupling inside are not modelled |
| crankcase | 120 (x, 43 to 163) × 110 (y) × 110 (z), centred on the axis, aluminium | the triplex pump's crank and plungers inside, not modelled |
| manifold head | 50 (x, 162.5 to 212.5) × 130 (y) × 120 (z), centred on the axis, brass | the pump's valve head; carries the two ports and the unloader |
| port bores | Ø17.055 plain (E1 + h of NPT 3/8), 12.358 deep (L2 + 2), blind: `port-in` into the head's front face (y = −65) at x = 187.5, z = 138.5; `port-out` into the head's +x end face (x = 212.5) at y = 0, z = 138.5 | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0; tank 2.0's rule); deeper than a male's make-up L1 + L3; 37.6 of floor under `port-out`, 52.6 under `port-in` (asserted ≥ 10), 51 of wall round each (asserted ≥ 5). Declared in features.csv |
| port fields | 22 × 22, 0.2 proud, centred on each bore, the bore through it; `M-WHITE-PA` | each port's name is a decal; 0.2 proud for GEO-050; each port's pivot on its outer face (filter-air 3.0's rule) |
| unloader | cartridge Ø32 × 40 up from the head's top (z 198 to 238.5) at x = 187.5, its knob Ø36 × 16 on it (to z 254.5); silver, black knob | the unloader valve; the knob is fixed in 1.x (the setting is the cell's) |
| overall | envelope 560 × 300 × 268 (x −280 to 280, y −150 to 150, z 0 to 268; the terminal box's top) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-in` | NPT3/8 | female | none | pneu.py D1 (NPT, ASME B1.20.1); pivot at y = −65.2 (the field's outer face), axis −y. Water in from the cell's supply: a liquid port on the thread contract on file, as coolant-pump's, tank's and hyd-cooler's water ports (no role; an assembly leaves it out of its air joints). The garden-hose thread of the trade (ASME B1.20.7) is not on file: a hose adapter is the cell's |
| `port-out` | NPT3/8 | female | none | as above; pivot at x = 212.7, axis +x. The high-pressure water out to the hose and lance; the trade's M22 hose coupling is not on file, so the outlet is a plain NPT 3/8 port and the adapter is the hose's (no figure claimed) |

NPT 3/8 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002). pneu.NPT holds NPT 3/8's
figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 17.055 (the bore), L2 = 10.358 (the bore is
L2 + 2 deep). The helix is not modelled: the bore is the thread drawn plain. A male seated on the field's face reaches L2 − 0.2
past the end face, inside the bore.

## Open figures
None. Not claimed: a pressure, a flow, a motor power, voltage or current. An own design states no rating of its own
(OPERATING.md 12; request pneu-11's answer item 1), so there is no ratings.csv; a rated version waits for the standard EM chooses.
No safety function (inventory.csv's `safety` column is empty for this row); the lance's trigger gun is the cell's, not this element.

## Named nodes
`port-in`, `port-out` (kind port, fixed; range 0; each the field with its pivot on the field's outer face). No moving node: the
unloader's knob is fixed in 1.x.

## Materials by layer
`M-STEEL-7035` skid plate · `M-BLACK-PA` rubber feet, unloader knob · `M-CAST-BLUE` motor foot block, motor body, fan cowl,
terminal box · `M-ALU-ANOD` bell flange, crankcase · `M-BRASS` manifold head · `M-SILVER` unloader cartridge · `M-WHITE-PA` port fields

## Decals (Blender)
None in 1.0 ("IN" / "OUT" on the port fields and "complexes.org" on the motor are a later version). No vendor names, no approval
marks.

## Notes
- Nothing placed: the hose, lance, inlet strainer and the motor's cable are the cell's; a fitting (male NPT 3/8) in each port is the
  assembly's. The crank, plungers, valves, the unloader's internals and the water are not modelled.
- Stationary: no wheels or handle (a cart form would be a sibling under OPERATING.md 6's convention, pressure-washer-skid-cart). The id
  is the inventory's; its convention form (pressure-washer-skid) rides with request pneu-12's question on the lane's ids (needs-em
  r86).
- The `pwr` port, pins.csv and ratings.csv (a 480 V three-phase motor on the campus supply, as hpu-0.37kw's) come with the rated
  version; in 1.0 an assembly cannot wire it.

## Outputs (out/)
`pressure-washer-skid.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design, pneu-r86 (unattended; request pneu-11's answer item 1): skid plate on four rubber feet, motor foot block, motor body with fan cowl and terminal box (no electrical port), bell flange, crankcase, manifold head with `port-in` / `port-out` (female NPT 3/8 bored Ø (E1 + h) × (L2 + 2) deep from pneu.NPT, pivots on the fields' outer faces), unloader cartridge and fixed knob; no ratings.csv; nothing moves; nothing placed |
