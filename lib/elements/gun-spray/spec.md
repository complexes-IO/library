# gun-spray · v1.0 · generic paint spray gun, gravity cup 600 ml, nozzle 1.4 mm, female NPT 1/4 air inlet

**What** a hand-held compressed air paint spray gun for the paint booths: the paint runs down from a cup on top into the head, and
air from the booth's line, entering under the handle, atomises it at the air cap in front. Pulling the trigger opens the air valve
and draws the fluid needle back from its seat, so the gun sprays; releasing it lets the spring shut both. The air enters `port-1`, a
female NPT 1/4 bore in the collar under the handle, which takes fitting-pushin 2.0 (male NPT 1/4) and a tube-pneu from the booth's
frl. lib/inventory.csv row `gun-spray` (own_design generic, "paint spray gun"; 2 systems: booth-paint, booth-spray-paint).
**Class** device · **Baseline** our own design: generic spray gun (compressed air) (ETIM 10.0 EC004054, synonyms "Compressed air
pistol", "Compressed air tool"), as OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic)
say. No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its air
inlet takes its thread from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and its number from ISO 11727
(pneu.NODES). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the inlet collar's face z = 0 on the inlet's axis; the hose below (−z), the spray toward +x.
The port follows pneu.py's port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `GUN-SPRAY` · no parameters.

The class: the inventory row names none. EC004054 "Spray gun (compressed air)" (tier 1, group EG020014 "Compressed air tools and
accessories", 16 features on file) is the class lib/standards/etim/classes.csv gives for a compressed air spray gun, and its
features (reservoir volume, nozzle diameter, round and wide stream, air volume required, max. viscosity, discharge) are a paint
gun's, so it fits both of the row's systems, each a paint booth whose gun it is. The electrostatic powder gun (row `gun-powder`)
is another element.

## Class values (ETIM 10.0 EC004054, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF015068 Colour lead | not stated |
| 2 | EF000176 Reservoir volume | 600 ml (the gravity cup; 627 ml inside a 2 mm wall by element.py's cup_ml, asserted ≥ 600) |
| 3 | EF015067 Nozzle diameter | 1.4 mm (the fluid nozzle's orifice; stated, not drawn: the paint path is not modelled) |
| 4 | EF015070 Round stream | yes (the fan closed) |
| 5 | EF015069 Wide stream | yes (the fan open) |
| 6 | EF015072 Swivelling nozzle | no |
| 7 | EF020449 Max. operating pressure | 10 bar (1000 kPa gauge, about 145 psig); in ratings.csv as p_max, status "generic design" |
| 8 | EF011396 Max. operating pressure (psi) | 145 psi (class value 7 in psi) |
| 9 | EF015071 Pressure display | no (the booth's frl carries the gauge) |
| 10 | EF020609 Air volume required | not stated |
| 11 | EF025190 Max. viscosity | not stated |
| 12 | EF011233 Max. discharge efficiency | not stated |
| 13 | EF001438 Length | 153 mm (needle knob to nozzle tip, along the spray axis) |
| 14 | EF000008 Width | 94 mm (across the cup's lid) |
| 15 | EF000040 Height | 293 mm (inlet face to the lid's top) |
| 16 | EF001951 Machine weight | not stated |

The pressure (class value 7) is a generic design value (OPERATING.md 12), not a tested rating. 1000 kPa is above P_SUPPLY (689.5
kPa, 100 psig; pneu.py D3), so PNE-003 passes it on a bench line; element.py asserts it. The spray pressure the booth sets at its
regulator is lower; it is the booth's figure, not the gun's.

**No safety claim.** A paint gun works in a booth whose spray area is a hazardous location (the booth's codes, not on file here).
This gun is pneumatic and carries no electrical part; it claims no rating for a hazardous location and no other safety function
(OPERATING.md 12).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| inlet collar | Ø22 × 16 under the grip, its face on z = 0 | carries the NPT 1/4 bore with 4.2 mm of wall (asserted ≥ 3) and 4.1 round the pipe OD (13.7 mm, pneu.NPT; asserted ≥ 3) |
| inlet bore | Ø13.616 × 12.205, blind, up the collar's axis from its face | Ø = E1 + h of NPT 1/4 from pneu.NPT, the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 and < the collar's 16. Role in features.csv (HOLE-010) |
| grip | 28 (x) × 22 (y), x −14 to 14, from the collar (0.5 into it) up into the head | a hand's grip; upright, the inlet on its axis |
| head | 110 (x) × 28 (y) × 40 (z), x −40 to 70, z 120 to 160 | carries the air valve, the fluid needle and the cup; the spray axis at z 140 |
| air cap | Ø30 × 20 in front of the head (0.5 into it), on the spray axis | the ring that holds the air cap; its horns are not drawn |
| fluid nozzle tip | Ø6, 5 out of the air cap | where the paint leaves; its 1.4 mm orifice is class value 3, not drawn |
| needle knob | Ø16 × 18 at the head's rear (0.5 into it), on the spray axis | the fluid needle's stop; fixed in 1.0 (no node) |
| cup | neck Ø14 × 15 on the head's top at x = 30; cup Ø90 × 110 from z 175; lid Ø94 × 8 | 627 ml inside a 2 mm wall (asserted ≥ 600); the cup's foot (z 175) clears the air cap's top (155), asserted |
| trigger | 6 (x) × 18 (y), x 34 to 40, z 42 up to the head's underside (face to face) | pulled 10° about its top rear edge; fully pulled its lowest rear corner stands at x 20.5, 6.5 clear of the grip's front (asserted > 5) |
| overall | envelope x −58 to 95, y −47 to 47, z 0 to 293 | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | the inlet collar's face z = 0, axis −z | the air inlet; ISO 11727 number 1 as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1); NPT 1/4 the bench's drop size, so fitting-pushin 2.0 screws in |

PNE-002 pairs it with a male NPT 1/4 (sealant on the male, D1). A quick coupler for the hose is no element on file; the booth's
assembly places fitting-pushin 2.0 and a tube-pneu, and this element places nothing.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (the inlet collar): kind port, fixed (range 0) · `trigger` (rotate about +y at its top rear edge, x 34, z 120; 0 at rest
to 10° fully pulled, the lower end toward the grip).

## Materials by layer
`M-ALU-ANOD` head, inlet collar · `M-BLACK-PA` grip, needle knob, lid · `M-SILVER` air cap, nozzle tip, cup neck, trigger ·
`M-CASE-CLEAR` cup

## Decals (Blender)
None in 1.0 (the "generic" label is a later version). No vendor names, no approval marks.

## Outputs (out/)
`gun-spray.lsp` · `.glb` (port and trigger pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004054), pneu-r69 (unattended): grip on a female NPT 1/4 inlet collar `port-1` bored at E1 + h, head with air cap, nozzle tip and needle knob, 600 ml gravity cup with lid, `trigger` rotating 0 to 10°; 10 bar p_max as a class value; nothing placed |
