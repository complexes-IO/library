# frl · v2.0 · generic air service unit, shut-off and dump valve and filter-regulator, female NPT ports

**What** the bench's air service unit, the first part of every compressed air circuit on a bench (a pneumatic trainer, a test
bench, a booth, a pick-and-place cell). Supply air enters `port-1` on the inlet boss at the left and meets the 3/2 shut-off and dump
valve: a quarter turn of its red `handle` opens the line; closed, it shuts the supply and vents the line downstream through
`port-3` under the valve block, and a padlock through the handle's hasp and the shelf under it holds it there. The air then passes the filter-regulator: the clear bowl below collects the water and dirt the
filter takes out (a manual drain at its foot), the diaphragm regulator reduces it to the pressure set with the adjusting `knob` on
the bonnet, and it leaves through `port-2` on the right. `port-g` on the regulator's front face, downstream of the seat, is the
gauge port (gauge-p, 0 to 160 psig).
lib/inventory.csv row `frl` (own_design generic, ETIM EC010122; 14 systems: booth-paint, booth-powder, booth-spray-paint, cmm,
laser-cutter-fiber, plasma-cutter-cnc, pneumatic-pick-and-place, pneumatic-trainer, powder-coating-system, riveter, sandblaster,
test-bench-pneumatic, welder-spot, workbench-assembly).
**Class** device · **Baseline** our own design: generic pressure reducing valve, air service unit (ETIM 10.0 EC010122), as
OPERATING.md 12 (generic elements, EM 2026-11-07), lib/inventory.csv (own_design generic) and request pneu-6's answer (core watch
2026-11-09) say. No vendor file was opened or measured: the vendor file in this folder's references/ is reference only, never used
here (inventory note). The class values below are its design inputs; its sizes are design choices; its ports take their thread
from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and their numbers from ISO 11727 (pneu.NODES). No vendor names;
"generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of `port-1`'s joint plane on the inlet boss's left face (where the supply fitting
meets it); the air flows in along +x, the gauge port faces −y. Ports follow pneu.py's port frame: the pivot on the joint plane, its
axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `FRL` · no parameters.

The class: EC010122 "Pressure reducing valve" (tier 2, group EG015810, 33 features on file). Request pneu-6 (pneu-r61) found the
row's first class, EC011249 "Air filter unit", is a ventilation duct filter; the core's answer moved the row to EC010122, the
class of the part the PNE checks read (the regulator: PNE-003 its inlet rating, PNE-007 the setting, PNE-009 the gauge in
`port-g`). The filter half is not a second class: its EC004033 "Compressed air filter" values are notes under the table. regulator
1.0 is the same class as a bare inline regulator; this element adds the shut-off and dump valve and the filter and places none of
regulator's parts (they share the same design choices for bosses and bores, not geometry).

## Class values (ETIM 10.0 EC010122, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | aluminium, anodised (valve block, coupling, body, bosses and bonnet); the bowl clear polycarbonate; knob and drain black polyamide, handle red polyamide |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000139 Surface protection | anodised |
| 4 | EF023193 Nominal diameter connection 1 | 1/4 (NPT, ASME B1.20.1) |
| 5 | EF020122 Outer pipe diameter connection 1 | 13.7 mm (NPT 1/4 pipe OD D = 0.540 in, pneu.NPT) |
| 6 | EF000321 Connection 1 | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1) on the inlet boss's left face, `port-1` |
| 7 | EF013560 Contour code connection 1 | not stated |
| 8 | EF021872 With coupling connection 1 | no: a fitting is placed in `port-1` |
| 9 | EF020151 Length of connection 1 | not stated |
| 10 | EF020153 Working length connection 1 | not stated |
| 11 | EF020052 Nominal diameter connection 2 | 1/4 (NPT, ASME B1.20.1) |
| 12 | EF020123 Outer pipe diameter connection 2 | 13.7 mm (as connection 1) |
| 13 | EF000322 Connection 2 | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1) on the outlet boss's right face, `port-2` |
| 14 | EF013561 Contour code connection 2 | not stated |
| 15 | EF021873 With coupling connection 2 | no: a fitting is placed in `port-2` |
| 16 | EF020152 Length of connection 2 | not stated |
| 17 | EF020154 Working length connection 2 | not stated |
| 18 | EF020007 Article compression class | not stated |
| 19 | EF020149 Flange compression class | not stated (no flange) |
| 20 | EF020100 Max. inlet pressure | 10 bar (1000 kPa gauge, about 145 psig); in ratings.csv as p_max, status "generic design" |
| 21 | EF024003 Reduced pressure | 0.5 to 7 bar (50 to 700 kPa gauge, about 7 to 102 psig): the outlet's setting range, set with `knob` |
| 22 | EF022466 Kvs value | not stated |
| 23 | EF023182 Medium temperature (continuous) | not stated |
| 24 | EF001776 Sealing | not stated |
| 25 | EF002223 With pressure gauge | no: `port-g` (female NPT 1/4, role gauge) takes gauge-p, placed, never redrawn (a later version) |
| 26 | EF021587 With siphon | no |
| 27 | EF007245 Suitable for liquids | no |
| 28 | EF020335 Suitable for steam | no |
| 29 | EF007249 Suitable for gases | yes: compressed air to ISO 8573-1 [7:4:4] (pneu.py D3) |
| 30 | EF000040 Height | 184 mm (bowl foot with drain 98, body 40, bonnet 30, knob 16) |
| 31 | EF020158 Spindle angle | not stated |
| 32 | EF022259 Wrench width union nut | not stated (no union nut on this element) |
| 33 | EFSE0002 Type approval according to BBR/EKS | no |

The filter half, as notes from EC004033 "Compressed air filter" (request pneu-6's answer: not a second class, so not checked by
GEN-010): thread size NPT 1/4 (the same ports); depositional particle size not stated (the outlet air is to ISO 8573-1 [7:4:4],
pneu.py D3, the bench contract; this design gives no filter element rating); max. flow rate not stated. No flow figure is given or
checked anywhere in 1.0.

The pressures (class values 20 and 21) are generic design values (OPERATING.md 12), not tested ratings. 1000 kPa is above
P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it on a bench line; the setting range's top, 700 kPa, is above
P_WORK_MAX (551.6 kPa, 80 psig), the bench regulator's highest setting, so the range covers it. element.py asserts both. The twin
reads no pressure from the knob in 1.0.

**No safety claim.** The shut-off and dump valve isolates and vents the air downstream; whether that is a safety function (energy
isolation in ISO 14118's terms) is EM's question (request pneu-6's answer, lib/needs-em/pneu.md), and the inventory row's
`safety` column is empty. This element claims nothing beyond its class values (OPERATING.md 12). If EM says yes, the row's
column changes and station 7 asks his "Safety sign-off"; the build is the same either way.

**Lockable from 2.0** (review frl-1.0.md finding 2): the handle carries a hasp tab on its +y end and the valve block a fixed shelf
under it, each with a Ø8 padlock hole; the two holes are coaxial only with the handle closed (0°), so a padlock through both holds
the valve shut and the line vented, and the handle cannot turn open. ratings.csv `lockable` yes, status "derived", is read from
that geometry (element.py), not claimed; PNE-008 (toolkit/v_pneu.py; 29 CFR 1910.147(c)(2)(iii), "accepts a lock") reads it, so
frl may be a circuit's dump valve. The padlock itself is no element on file and is not placed. The knob's lock, which the
inventory row also names ("filter-regulator with locking knob"), is still not modelled: 2.0 claims no locked setting, and the twin
reads no pressure from the knob. Whether a lockable dump valve makes frl a safety-function element stays EM's question (above).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| inlet boss | Ø20 × 14 along x, 0.5 into the valve block; `port-1` on its left face x = 0 | at least 3 mm of metal round the NPT 1/4 pipe OD (13.7 mm, pneu.NPT); 14 is at least 2 more than a male's effective thread L2 (10.21) and its make-up depth L1 + L3 (10.02), both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each, for every boss |
| port bores | Ø13.616 × 12.205 deep, blind, one in each boss (inlet, outlet, gauge, exhaust), on the port's axis from its face | Ø = E1 + h of NPT 1/4 from pneu.NPT, the very diameter fitting-pushin 2.0 and gauge-p draw their male stubs at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out, design choice), asserted ≥ the make-up L1 + L3 and < the boss's 14; 3.19 mm of boss wall round each bore (asserted ≥ 3). Role in features.csv (HOLE-010) |
| shut-off valve block | 40 × 40 × 40 (x, y, z), x 14 to 54, centred on the port axis | holds the 3/2 valve's spool |
| exhaust boss | Ø20 × 14 along −z under the valve block, at its centre x = 34; `port-3` at z = −34 | as the inlet boss; downward, so the vented air and any oil mist go to the floor side, away from the operator's face |
| shut-off handle | lever 10 × 40 × 8 on the valve block's top, red, seated face to face (it turns a quarter turn about +z); at rest across the line (along y, closed), open along it (along x, at 90°) | along the line reads open, across it shut: the trade's reading of a quarter-turn lever, valve-air-shutoff's way (review frl-1.0.md finding 1; no standard on file fixes it); its sweep (radius 20.6) stays over the valve block and 11.4 clear of the bonnet (asserted ≥ 5) |
| hasp tab (2.0) | 14 (x) × 16 (y) × 8 (z) on the handle's +y end (y 20 to 36, z 20 to 28: the lever's own height, its underside in the valve block's top plane as the lever's), face to face, part of `handle`; Ø8 padlock hole at y = 29 | 2 over the shelf; opening, it swings to −x over the valve block's top and the inlet boss (z 20 > the boss's 10, asserted), away from the bonnet; 3 of wall round the hole (asserted); 8 thick because a 4 thick tab's corner edges took no fillet at the AutoCAD gate (section History) |
| shelf and support (2.0) | shelf 14 × 14.5 × 6 (y 21.5 to 36, z 12 to 18) on a support plate 12 × 3.5 × 16 (y 19.5 to 23, 0.5 into the valve block's rear face, z 0 to 16); Ø8 padlock hole at y = 29, coaxial with the tab's at 0° | the shelf stays outside the handle's sweep (21.5 > 20.6, asserted); the support 12 wide so no side lies in the shelf's plane; a shackle up to Ø7 passes both holes (design choice: no padlock standard on file) |
| coupling block | 10 × 30 × 30, x 54 to 64, 0.5 into each body | joins the two modules on the port axis |
| filter-regulator body | 40 × 40 × 40, x 64 to 104 | holds the filter element, the seat and the diaphragm |
| outlet boss | Ø20 × 14 along +x on the body's right face; `port-2` at x = 118 | as the inlet boss, on the same axis (inline) |
| gauge boss | Ø20 × 14 along −y on the body's front face, at the body's centre x = 84; `port-g` at y = −34 | as the inlet boss |
| bonnet | Ø36 × 30 on the body's top face, 0.5 into it, z 20 to 50 | the spring housing, under the knob |
| adjusting knob | Ø30 × 16 on the bonnet, black, seated face to face (it turns) | `knob` |
| filter bowl | Ø36 × 90 under the body, 0.5 into it, clear, z −20 to −110 | the operator sees the condensate level through it |
| manual drain | Ø10 × 8 at the bowl's foot, black, z −110 to −118 | fixed in 1.0 (its turn is not modelled) |
| overall | envelope 118 × 70 × 184 (x 0 to 118, y −34 to 36, z −118 to 66) | the hasp adds 16 at +y (2.0) |

All four ports are NPT 1/4, the bench's FRL and gauge size (pneu.py D3; next.md decision 1), so fitting-pushin 2.0's male NPT 1/4
stub fits `port-1` and `port-2`, silencer 1.0 (NPT1/4) fits `port-3`, and gauge-p's stub fits `port-g`.

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | the inlet boss's face x = 0, axis −x | inlet; ISO 11727 number 1 as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1) |
| `port-2` | NPT1/4 | female | work | the outlet boss's face x = 118, axis +x | outlet; ISO 11727 number 2 as pneu.NODES; pneu.py D1 |
| `port-3` | NPT1/4 | female | exhaust | the exhaust boss's face z = −34, axis −z | the dump valve's vent; ISO 11727 number 3 as pneu.NODES; a silencer goes in it in the circuit |
| `port-g` | NPT1/4 | female | gauge | the gauge boss's face y = −34, axis −y | downstream of the seat, so the gauge reads the set pressure (next.md decision 1) |

PNE-002 pairs each with a male NPT of the same size (sealant on the male, D1). gauge-p 1.0 (0 to 160 psig) at `port-g`: PNE-009
judges a gauge at P_SUPPLY (100 psig, 62.5 % of its span, under pneu.GAUGE_FRACTION 0.75), so it passes there. Each face is the
joint plane a placed fitting meets; the bores behind them take the male stubs.

The inventory row's made_of names gauge-p. A host places only common parts already past station 6 (OPERATING.md 12, quality at
the source); gauge-p 1.0 is held at station 5 by BEH-010 today (no behaviour.csv yet), so 1.0 places nothing and leaves `port-g`
open for it. Placing gauge-p in `port-g` adds its nodes, so it is frl 2.0, once gauge-p has passed station 6.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (inlet boss), `port-2` (outlet boss), `port-3` (exhaust boss), `port-g` (gauge boss): kind port, fixed (range 0).
`handle` (the lever and its hasp tab): kind rotate about its own axis (+z, through the valve block's centre line), 0 to 90° (a
quarter turn, closed at 0, open at 90), seated face to face on the valve block's top; the tab sweeps radius 36.7 at z 20 to 28,
over the valve block's top and the inlet boss only. `knob`: kind rotate about its own axis (+z, through the bonnet's centre line),
0 to 1800° (five turns from the spring unloaded to the top of the range, a design choice), seated face to face on the bonnet, so it
sweeps only its own cylinder. The spool, spring and stem they turn are inside and not modelled. behaviour.csv names their states.

## Materials by layer
`M-ALU-ANOD` inlet boss, valve block, exhaust boss, coupling, body, outlet boss, gauge boss, bonnet, hasp shelf and support ·
`M-CASE-CLEAR` filter bowl · `M-BLACK-PA` adjusting knob, manual drain · `M-RED-PA` shut-off handle and its hasp tab

## Decals (Blender)
None in 1.0 (flow arrow, the handle's open and closed marks and the "generic" label are a later version). No vendor names.

## Outputs (out/)
`frl.lsp` · `.glb` (port, handle and knob pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010122, request pneu-6), pneu-r64 (unattended): shut-off and dump valve block with the inlet `port-1`, exhaust `port-3` and the quarter-turn `handle`; coupling; filter-regulator body with the outlet `port-2`, gauge port `port-g`, bonnet and adjusting `knob`, clear bowl and drain below; four female NPT 1/4 ports bored at E1 + h; behaviour.csv with the handle's and knob's states; gauge-p not yet placed |
| 1.1 | pneu-r68 (unattended), review frl-1.0.md: the handle reads the trade's way, across the line at rest (closed) and along it at 90° (open), HANDLE 10 × 40 × 8 (finding 1; no node, origin, range or cut-out moves, so a minor); a spec line that 1.1 is not lockable and fails PNE-008 as a circuit's dump valve until frl 2.0's hasp (finding 2); behaviour.csv's closed note says what vents through 3 (note 1) |
| 2.0 | pneu-r70 (unattended), review frl-1.0.md finding 2: the padlock hasp, a tab on the handle's +y end and a fixed shelf on a support plate on the valve block's rear face, each with a Ø8 padlock hole, coaxial at 0° (closed); the tab 8 thick (the lever's height; the round's first AutoCAD run, with a 4 thick tab, rejected its four short corner fillets); new cut-outs, so a major; ratings.csv `lockable` yes (derived from the hasp modelled) for PNE-008; envelope y to 36; gauge-p still not placed in `port-g` |
