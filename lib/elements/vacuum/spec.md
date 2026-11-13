# vacuum · v2.0 · generic vacuum gripper: inline ejector with a flat round suction cup, female NPT 1/8 ports

**What** a vacuum gripper for pick and place (a cobot bench, a pneumatic pick-and-place cell, the pneumatic trainer): a compact
inline ejector (a venturi: no pump, no motor) with a flat round suction cup below it. Supply air enters `port-1` on the body's left
end face, passes the nozzle and leaves through `port-3` on the right end face, where the silencer goes; the flow draws the air
out of the cup, which then holds the part. Air into `port-blow` on the top face, over the cup, blows the vacuum off and releases
the part. lib/inventory.csv row `vacuum` ("vacuum ejector and suction cup", own_design generic, ETIM EC004675, made of
fitting-pushin x2 and silencer; cobot-bench, pneumatic-pick-and-place, pneumatic-trainer, servo-pick-and-place).
**Class** device · **Baseline** our own design: generic vacuum suction cup (ETIM 10.0 EC004675) on an inline ejector body, as
OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or
measured, and the product figures in this folder's metadata.json (a product picked 2026-11-02, reference only) are not used: every
size below is our own. The class values below are its design inputs; its sizes are design choices; its ports take their thread
from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and supply and exhaust their numbers from ISO 11727
(pneu.NODES). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the body's left end face, on `port-1`'s axis (`port-1`'s joint plane, its
number field's outer face, is 0.2 to −x); the air flows in along +x, the cup below (−z). Ports follow pneu.py's port frame: the
pivot on the joint plane, its axis toward the counterpart; the joint plane is each port's number field's outer face (2.0).
**Built with** toolkit 1.3 · AutoLISP command `VACUUM` · no parameters.

The class: EC004675 "Vacuum suction cup" (tier 2, group EG010320 "Lifting equipment", 4 features on file), the class
lib/standards/etim/classes.csv maps inventory row `vacuum` to. ETIM's subset on file has no class for the ejector itself (EC012080
"Jet pump" is a liquid pump in group EG020079 "Pumps"), so the element is the cup's class with the ejector it hangs from, as the
inventory row names them together: one part on a robot's flange, one node set for the twin.

## Class values (ETIM 10.0 EC004675, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF014871 Suction disc diameter | 32 mm (the sealing lip's outer diameter) |
| 2 | EF013335 Holding force | not stated (it follows from the vacuum level the ejector reaches, which this design does not state) |
| 3 | EF000007 Colour | black (the cup, nitrile rubber); the body anodised aluminium |
| 4 | EF002386 Ambient temperature | not stated |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| ejector body | 64 × 20 × 28 (x, y, z), x 0 to 64, centred on the port axis in y and z | carries the three ports and the nozzle; 4.88 mm of wall round each bore across its 20 width (at least 3 mm round the NPT 1/8 pipe OD, 10.287 mm, pneu.NPT: element.py asserts it) |
| port bores | Ø10.242 × 8.702 deep, blind, one in each port's face (`port-1` left end, `port-3` right end, `port-blow` top), on the port's axis | Ø = E1 + h of NPT 1/8 from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), the very diameter fitting-pushin 2.0 and silencer 1.0 draw their male stubs at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ a male's make-up L1 + L3; `port-blow`'s bore is clear of both end bores along x (asserted). Role in features.csv (HOLE-010) |
| port-number fields | 16 × 16, 0.2 proud, centred on each bore, the bore through it; each port's pivot on its field's outer face (2.0) | the port number is a decal; 0.2 proud for GEO-050; the pivot on the field's outer face so a placed male's hex (AF 14, corners Ø15.68, inside the 16 square) meets the field face to face instead of sitting 0.2 into it (review vacuum-1.0.md finding 1, as filter-air 3.0 and valve-gauge 3.0); a male's stub (L2 6.702) then reaches 6.502 past the body face, inside the 8.702 bore |
| blow-off port and cup centre line | x = 40 | over the vacuum chamber, downstream of the nozzle |
| cup stem | Ø12 × 8 below the body, 0.5 into it, z −13.5 to −22 | carries the vacuum channel down to the cup |
| cup back | Ø20 × 4.5 under the stem, black nitrile | |
| sealing lip | Ø32 × 3.5, its face (the suction face) at z = −29 | class value 1 |
| overall | envelope 64.4 × 32 × 43.2 (x −0.2 to 64.2, y −16 to 16, z −29 to 14.2) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/8 | female | supply | its field's outer face x = −0.2, axis −x | supply; ISO 11727 number 1 as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1) |
| `port-3` | NPT1/8 | female | exhaust | its field's outer face x = 64.2, axis +x | the ejector's exhaust; ISO 11727 number 3 as pneu.NODES; takes silencer 1.0 (`thread` NPT1/8), so PNE-005 finds it silenced |
| `port-blow` | NPT1/8 | female | supply | its field's outer face z = 14.2, x = 40, axis +z | the blow-off air from a second valve output; named for what it does (no ISO 11727 number is given to it here) |

PNE-002 pairs each with a male NPT of the same size (sealant on the male, D1). fitting-pushin 2.0 at its defaults (tube 1/4 to
NPT 1/8) fits `port-1` and `port-blow`; silencer 1.0 with `thread` NPT1/8 fits `port-3`. The assembly places them, never redrawn
(regulator 1.0's gauge-p pattern): the element is the gripper itself, and the tube size stays the cell's choice. PNE-004 asks
every one of the three joined in an assembly.

## Open figures
- NOT ON FILE (A): the gripper's max. supply pressure. EC004675 has no pressure feature (its four are above), ETIM's subset has
  no ejector class whose feature would state it, and ASME B1.20.1 states no pressure, so ratings.csv holds no p_max; it is a
  maker's tested figure. In an assembly PNE-003 REVIEWs the gripper until EM gives a source or a figure. It sits on a valve's
  output, which carries up to P_SUPPLY (100 psig, pneu.py D3).

## Named nodes
`port-1`, `port-3`, `port-blow` (the port-number fields): kind port, fixed (range 0), each pivot on its field's outer face. Nothing moves: the cup's lip flexing on a
part is not modelled, and the twin reads the gripper's state from its ports' air, not from a moving node.

## Materials by layer
`M-ALU-ANOD` ejector body, cup stem · `M-GASKET` cup back and sealing lip (black nitrile) · `M-WHITE-PA` port-number fields

## Decals (Blender)
None in 1.0 (the port numbers 1 and 3, "blow" and the "generic" label are a later version). No vendor names, no approval marks.

## Notes
- Mounting: the body has no mounting holes in 1.0; a bracket or a robot flange adapter and its screws come with the cell that
  needs them (a later version, once the screw element is built: OPERATING.md 12, foundation first).
- The nozzle, the diffuser, the check valve that holds the vacuum and the channel down to the cup are inside and not modelled.
  No suction flow, vacuum level, noise or holding force is claimed.

## Outputs (out/)
`vacuum.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004675), pneu-r63 (unattended): inline anodised ejector body with female NPT 1/8 `port-1` (supply), `port-3` (exhaust) and `port-blow` (blow-off), each bored at E1 + h with its number field; cup stem, cup back and a Ø32 flat sealing lip below; one class A open figure (max. supply pressure) |
| 2.0 | pneu-r73 (unattended): review vacuum-1.0.md finding 1 (pneu-r66 finding 2): each port's pivot moved 0.2 out, from the body's face to its number field's outer face (`port-1` x −0.2, `port-3` x 64.2, `port-blow` z 14.2), so a placed male's hex meets the field face to face (filter-air 3.0's fix); the origin is the body's left end face centre, as before, now said so; nodes, bores and envelope unchanged |
