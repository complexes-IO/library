# receiver-air · v2.0 · generic compressed air receiver, vertical, 50 l, female NPT ports

**What** a vertical compressed air receiver for a compressor station: the vessel between the compressor and the air line. It
stores air, so the compressor starts and stops less often and the line sees a steadier pressure, and it lets the condensate the
compressed air carries settle at its foot. Air from the compressor (or its aftercooler) enters `port-1` low on the left side and
leaves through `port-2` high on the right side, so the water drops out before the air leaves. `port-drain` under the bottom end
takes a drain valve (drain-auto, or a manual valve); `port-g` on the top end takes a gauge (gauge-p); `port-relief` on the top end
takes a pressure relief valve.
lib/inventory.csv row `receiver-air` (own_design generic, "compressed air receiver"; 2 systems: compressor-station,
compressors-plant).
**Class** device · **Baseline** our own design: generic pressured air vessel (ETIM 10.0 EC012187, synonyms "Compressed air
reservoir", "Compressed air tank"), as OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design
generic) say. No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices;
its ports take their thread from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and inlet and outlet their numbers
from ISO 11727 (pneu.NODES). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the floor contact plane z = 0 on the vessel's axis; the inlet faces −x, the outlet +x. Ports
follow pneu.py's port frame: the pivot on the joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `RECEIVER-AIR` · no parameters.

The class: the inventory row names none. EC012187 "Pressured air vessel" (tier 1, group EG020014 "Compressed air tools and
accessories", 15 features on file) is the class lib/standards/etim/classes.csv gives for a compressed air tank or reservoir, and it
fits the row's two systems: both are compressor stations, whose receiver it is. tank 2.1 (EC010413) is a pressureless liquid
reservoir and compressor-air 1.0 carries its own 24 l receiver; this element shares no parts with either.

## Class values (ETIM 10.0 EC012187, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel, painted grey (shell, ends, legs); the port bosses galvanised steel half couplings |
| 2 | EF000010 Model | vertical |
| 3 | EF000003 Mounting method | floor standing on four legs |
| 4 | EF023191 Nominal diameter | 3/8 (NPT, ASME B1.20.1): the inlet and the outlet |
| 5 | EF002222 With safety valve | no: `port-relief` (female NPT 1/4) takes one; no relief valve is an element yet (needs-em r68) |
| 6 | EF002223 With pressure gauge | no: `port-g` (female NPT 1/4, role gauge) takes gauge-p, placed, never redrawn |
| 7 | EF000364 Capacity | 50 l (the inner volume, 50.7 l, by element.py's volume_l with a 3 mm wall; asserted ≥ 50) |
| 8 | EF020449 Max. operating pressure | 11 bar (1100 kPa gauge, about 160 psig); in ratings.csv as p_max, status "generic design" |
| 9 | EF000008 Width | 376 mm (across the legs) |
| 10 | EF000049 Depth | 376 mm (across the legs) |
| 11 | EF000040 Height | 1014 mm (floor to the top bosses' faces) |
| 12 | EF000551 Diameter | 300 mm (the shell) |
| 13 | EF000167 Weight | not stated |
| 14 | EF019381 PED (Pressure Equipment Directive) compliant (2014/68/EU) | no: no compliance or approval is claimed (OPERATING.md 6) |
| 15 | EF019382 SPVD (Simple Pressure Vessels Directive) compliant (2014/29/EU) | no: as 14 |

The pressure (class value 8) is a generic design value (OPERATING.md 12), not a tested or code-stamped rating. 1100 kPa is above
P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it on a bench line, and above compressor-air 1.0's 8 bar, the
station's compressor. element.py asserts it. No pressure-vessel design code (ASME BPVC Section VIII, EN 286-1, EN 13445) is on file
(lib/standards/sources.csv), so the shell's wall is not designed to one: it is a design figure for the capacity only, and the
vessel is modelled solid.

**No safety claim.** A receiver is protected in service by a pressure relief valve; this element has the port for it and claims
nothing (OPERATING.md 12: no ratings or safety claims of its own beyond the class values). No relief valve element exists in the
inventory; whether the receiver must carry one, and which element it is, is EM's question (needs-em r68).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| shell | Ø300, z 260 to 960 (700 high) | with the two ends, 50.7 l inside a 3 mm wall: the nominal 50 l (asserted) |
| dished ends | Ø240 × 40 below (z 220 to 260) and above (z 960 to 1000), each 0.5 into the shell | a stepped stand-in for a dished head (the toolkit draws boxes and cylinders); appearance only, not a head shape to any code |
| legs | four, 40 × 40, on the ±x and ±y axes, floor to z 340, each 2 into the shell | the shell's foot 260 above the floor leaves room for the drain stack under the bottom end (the drain boss row); the legs clear the bottom end (inner face at r 148 > 120) |
| inlet boss | Ø28 on the −x side at z 400, 14 proud of the shell, 10 into it; `port-1` at x = −164 | low, so the air enters below the outlet; at least 3 mm of metal round the NPT 3/8 pipe OD (17.1 mm, pneu.NPT); 14 is more than the bore's 12.36 |
| outlet boss | Ø28 on the +x side at z 860, as the inlet; `port-2` at x = 164 | high, so the condensate stays below it |
| gauge and relief bosses | Ø20 on the top end at x = −60 (`port-g`) and x = +60 (`port-relief`), 14 proud, 0.5 into it; faces at z = 1014 | upright, so a gauge reads from the front and the relief valve vents upward |
| drain boss | Ø20 under the bottom end on the axis, 14 proud, 0.5 into it; `port-drain` at z = 206 | at the lowest point, where the condensate gathers; 206 above the floor, asserted ≥ the drain stack's 193.5 (next row), 12.5 to spare |
| drain stack (below `port-drain`, not part of this element) | 10 + 130 + 23.5 + 30 = 193.5 | 10: the gap a male-male NPT 1/4 nipple's hex keeps between this face and drain-auto's inlet face (an allowance, design choice: both ports are female and no nipple is an element yet); 130: drain-auto 2.0's height, read from its element (`height()`), not copied; 23.5: a fitting-pushin 2.0 in drain-auto's own `port-drain`, read from its element (`length()`); 30: room for the tube's bend (an allowance, design choice). element.py `drain_stack()` |
| port bores | NPT 3/8: Ø17.055 × 12.36; NPT 1/4: Ø13.616 × 12.205; blind, one in each boss, on the port's axis from its face | Ø = E1 + h of the size from pneu.NPT, the diameter fitting-pushin 2.0 and gauge-p draw their male stubs at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 and < the boss's 14; 5.47 / 3.19 mm of boss wall (asserted ≥ 3). Role in features.csv (HOLE-010) |
| overall | envelope 376 × 376 × 1014 (x and y −188 to 188, z 0 to 1014) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT3/8 | female | supply | the inlet boss's face x = −164, z = 400, axis −x | inlet; ISO 11727 number 1 as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1); NPT 3/8 the largest size on file (tank's, coolant-pump's) |
| `port-2` | NPT3/8 | female | work | the outlet boss's face x = 164, z = 860, axis +x | outlet; ISO 11727 number 2 as pneu.NODES; pneu.py D1 |
| `port-g` | NPT1/4 | female | gauge | the top boss's face x = −60, z = 1014, axis +z | the bench's gauge size (lib/rounds/pneu/next.md decision 1), so gauge-p's stub fits |
| `port-relief` | NPT1/4 | female | none | the top boss's face x = 60, z = 1014, axis +z | for a pressure relief valve; pneu.ROLES has no relief role, so none (as drain-auto's `port-drain`) |
| `port-drain` | NPT1/4 | female | none | the drain boss's face z = 206, axis −z | for a drain valve; drain-auto 2.0's inlet is NPT 1/4 female too (its `port-1`), so it hangs here only through a male-male NPT 1/4 nipple, which is no element yet (drain-auto's open class B line names the same fit); the 206 leaves room for the stack (Dimensions) |

PNE-002 pairs each with a male NPT of the same size (sealant on the male, D1). gauge-p 1.0 (0 to 160 psig) at `port-g`: PNE-009
judges a gauge at P_SUPPLY (100 psig, 62.5 % of its span), so it passes there. Each face is the joint plane a placed fitting meets;
the bores behind them take the male stubs. This element places nothing (gauge, relief valve and drain valve are the station's
assembly's, as regulator's gauge-p).

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (inlet boss), `port-2` (outlet boss), `port-g` (gauge boss), `port-relief` (relief boss), `port-drain` (drain boss): kind
port, fixed (range 0). No moving part.

## Materials by layer
`M-STEEL-7035` shell, dished ends, legs · `M-GALV` the five port bosses

## Decals (Blender)
None (the "generic" label and the flow marks are a later version). No vendor names, no approval or code marks.

## Outputs (out/)
`receiver-air.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012187), pneu-r68 (unattended): vertical 50 l shell on four legs with stepped dished ends; female NPT 3/8 inlet `port-1` (low, −x) and outlet `port-2` (high, +x), female NPT 1/4 `port-g` and `port-relief` on the top end and `port-drain` under the bottom end, each bored at E1 + h; 11 bar p_max as a class value; nothing placed |
| 2.0 | pneu-r79 (unattended; review receiver-air-1.0.md findings 1 and 2, pneu-r68 finding 1): the vessel 100 higher on longer legs (shell z 160 to 860 → 260 to 960, legs to z 240 → 340), so `port-drain`'s face stands at z 206 (was 106): above the drain stack's 193.5 (a nipple's gap, drain-auto's height and a fitting-pushin's length read from their own elements, the tube's bend), asserted; the old assert against 50 gone. Every port node 100 higher (`port-1` z 400, `port-2` z 860, `port-g` and `port-relief` z 1014): a major. Envelope 376 × 376 × 914 → 1014. Text: `port-drain` says a nipple is needed (both ports female); `port-g`'s basis cites next.md decision 1 alone |
