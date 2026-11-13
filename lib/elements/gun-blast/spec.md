# gun-blast · v1.0 · generic suction blast gun for a blast cabinet, 10 bar, female NPT 1/4 air inlet, rear abrasive hose nipple

**What** the hand-held blast gun inside a suction blast cabinet: the operator holds it through the cabinet's glove ports and aims
it at the part. Air from the cabinet's line enters `port-1`, a female NPT 1/4 bore in the collar under the grip; the air jet in the
head draws the abrasive by suction through a hose from the hopper below the cabinet (hopper-abrasive), into the nipple at the rear,
and drives it out through the nozzle at the front. The air is switched upstream by the cabinet's foot control (lib/machines-factory.txt
line 106 lists a foot switch for the sandblaster), not at the gun, so the gun has no trigger. lib/inventory.csv row `gun-blast`
(own_design generic, "blast gun"; 1 system: sandblaster, with cabinet-blast, hopper-abrasive, nozzle-blast, compressor-air, frl and
valve-air-shutoff).
**Class** device · **Baseline** our own design: generic sand blasting gun (compressed air) (ETIM 10.0 EC004036, synonyms "Compressed
air pistol", "Compressed air tool"), as OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic)
say. No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its air
inlet takes its thread from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and its number from ISO 11727
(pneu.NODES). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the inlet collar's face z = 0 on the inlet's axis; the air hose below (−z), the blast toward +x.
The port follows pneu.py's port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `GUN-BLAST` · no parameters.

The class: the inventory row names none. EC004036 "Sand blasting gun (compressed air)" (tier 1, group EG020014 "Compressed air tools
and accessories", 13 features on file) is the class lib/standards/etim/classes.csv gives for a compressed air blast gun, and its
features (nozzle bore, granulation, air volume required, material volume regulation, dust free) are a blast gun's, so it fits the
row's one system. EC004148 "Sand blasting device" (the whole blasting system) and EC004088 "Sand blasting coupling" are other things.

## Class values (ETIM 10.0 EC004036, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF014480 Nozzle bore | not stated (the nozzle is its own element, inventory nozzle-blast, mech's; its bore is that element's figure, and the holder takes it in a later version) |
| 2 | EF000176 Reservoir volume | not stated (suction fed: the gun holds no abrasive; it draws it by hose from the cabinet's hopper) |
| 3 | EF004854 Granulation | not stated (the abrasive is the cabinet's) |
| 4 | EF020449 Max. operating pressure | 10 bar (1000 kPa gauge, about 145 psig); in ratings.csv as p_max, status "generic design" |
| 5 | EF011396 Max. operating pressure (psi) | 145 psi (class value 4 in psi) |
| 6 | EF020609 Air volume required | not stated (it follows from the nozzle's bore, class value 1) |
| 7 | EF011398 Air inlet device-sided | female thread NPT 1/4 (`port-1`; pneu.py D1) |
| 8 | EF014273 Material volume regulation | no |
| 9 | EF025906 Dust free | no (the dust is held by the cabinet and its dust collector, not by the gun) |
| 10 | EF001438 Length | 165 mm (the hose nipple's end to the nozzle holder's front, along the blast axis; element.py envelope()) |
| 11 | EF000008 Width | 36 mm (across the nozzle holder) |
| 12 | EF000040 Height | 164 mm (inlet face to the head's top) |
| 13 | EF001951 Machine weight | not stated |

The pressure (class value 4) is a generic design value (OPERATING.md 12), not a tested rating. 1000 kPa is above P_SUPPLY (689.5
kPa, 100 psig; pneu.py D3), so PNE-003 passes it on a bench line; element.py asserts it. The blast pressure the cabinet sets at its
regulator is the cabinet's figure, not the gun's.

**No safety claim.** Abrasive blasting is done inside the cabinet, which holds the dust and the rebound; the cabinet's and the
blasting codes are the machine's. This gun is pneumatic, carries no electrical part and claims no safety function (OPERATING.md 12).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| inlet collar | Ø22 × 16 under the grip, its face on z = 0 | carries the NPT 1/4 bore with 4.2 mm of wall (asserted ≥ 3) and 4.1 round the pipe OD (13.7 mm, pneu.NPT; asserted ≥ 3); gun-spray 1.0's collar |
| inlet bore | Ø13.616 × 12.205, blind, up the collar's axis from its face | Ø = E1 + h of NPT 1/4 from pneu.NPT, the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 and < the collar's 16. Role in features.csv (HOLE-010) |
| grip | 28 (x) × 22 (y), x −14 to 14, from the collar (0.5 into it) up into the head | a gloved hand's grip; upright, the inlet on its axis, so the air hose hangs down out of the way of the abrasive hose |
| head | 100 (x) × 32 (y) × 44 (z), x −45 to 55, z 120 to 164 | the mixing chamber where the air jet meets the abrasive; the blast axis at z 142; the jet and passages inside are not modelled |
| nozzle holder | Ø36 × 30 in front of the head (0.5 into it), x 54.5 to 85, on the blast axis; solid | the nut that holds the nozzle; the nozzle and its seat are not drawn: the nozzle is nozzle-blast (mech's), placed in a later version (OPERATING.md 12: a host doesn't model holes now for a part it will place later) |
| abrasive hose nipple | Ø16 × 35 at the head's rear (0.5 into it), x −44.5 to −80, on the blast axis | the abrasive hose from the hopper pushes over it; its bore and barbs are not drawn |
| overall | envelope x −80 to 85, y −18 to 18, z 0 to 164 | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | the inlet collar's face z = 0, axis −z | the air inlet; ISO 11727 number 1 as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1); NPT 1/4 the bench's drop size, so fitting-pushin 2.0 screws in |

PNE-002 pairs it with a male NPT 1/4 (sealant on the male, D1). The cabinet's assembly places fitting-pushin 2.0 and a tube-pneu
(or its own hose) from its line; this element places nothing. The abrasive hose nipple is drawn with no port node: no abrasive hose
element and no port unit for one is on file (toolkit/pneu.py holds the compressed air units only). A node there is a later major,
when the cabinet's hose is an element.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (the inlet collar): kind port, fixed (range 0). No moving node: the air is switched at the cabinet's foot control.

## Materials by layer
`M-ALU-ANOD` head, inlet collar · `M-BLACK-PA` grip · `M-SILVER` nozzle holder, abrasive hose nipple

## Decals (Blender)
None in 1.0 (the "generic" label is a later version). No vendor names, no approval marks.

## Notes
- The nozzle (inventory nozzle-blast, a mech row, unbuilt) is placed in the holder in a later version, once it is past station 6
  (OPERATING.md 12, quality at the source); the holder is then bored for it (a changed cut-out: a major).
- The air and abrasive paths are not modelled; the twin reads no moving part.

## Outputs (out/)
`gun-blast.lsp` · `.glb` (port pivot, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004036), pneu-r71 (unattended): grip on a female NPT 1/4 inlet collar `port-1` bored at E1 + h, head (mixing chamber), solid nozzle holder, rear abrasive hose nipple; no trigger (air switched at the cabinet); 10 bar p_max as a class value; nothing placed |
