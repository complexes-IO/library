# hyd-tank · v1.0 · hydraulic reservoir, generic, rectangular, pressureless, 59 l, on two foot rails, suction and return ports on the cover, NPT 3/8 drain

**What** a hydraulic reservoir (lib/inventory.csv row `hyd-tank`, "hydraulic reservoir", own_design generic, 1 system:
hpu-assembly-station, where it is the tank a power unit is built on). It holds the circuit's oil at atmospheric pressure: the
filler-breather on the cover vents it. The pump draws through `port-suction`; the return oil (through the return-line filter and
the cooler, hyd-filter-return and hyd-cooler) comes back through `port-return` at the other end of the cover, so the oil crosses the
tank's length before it is drawn again; `port-drain` empties it; a round clean-out cover closes the suction end; the level gauge
on the front shows the level.
**Class** device · **Baseline** our own design: generic storage tank (ETIM 10.0 EC010413), as OPERATING.md 12 (generic elements,
EM 2026-11-07) and the inventory row (own_design generic) say. No vendor file was opened or measured. The class values below are
its design inputs; its sizes are design choices. Its drain takes its figures from the standard on file (ASME B1.20.1, through
toolkit/pneu.py); its oil ports' standard is not in lib/standards/sources.csv (Open figures). No vendor names; "generic" in its
title.
**Units / frame** mm, Z up. Origin: the centre of the two foot rails' underside (the mounting plane z = 0); length along x, width
along y; the suction end at +x, the return and drain end at −x.
**Built with** toolkit 1.3 · AutoLISP command `HYD-TANK` · no parameters (one size).

The class chosen: EC010413 "Storage tank" (group EG015120 "Storage tanks/vessels"; 26 features on file). Its synonyms in
lib/standards/etim/classes.csv are "Oil storage tank; Pressureless storage tank; Storage tank, pressureless; Water tank": a
hydraulic reservoir is a pressureless oil tank, so the class fits the row and its system. It is the class tank 2.2 is built to
(the inventory's `tank` row, a small three-port tank for oil or process water with NPT ports). hyd-tank is its hydraulic
sibling, a different element, not a size of it: its suction and return are hydraulic ports on the cover (unit "hyd-port",
toolkit/hyd.py), it stands on foot rails so the drain can be reached, and it has a clean-out cover. EC012187 "Pressured air
vessel" and EC003996 "Plunge reservoir (industry)" are the other reservoir classes on file: a pressure vessel and a parts
cleaning basin, neither this.

## Class values (ETIM 10.0 EC010413, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel, painted light grey (body, cover, port blocks, clean-out cover); zinc-plated steel drain boss |
| 2 | EF000051 Shape | rectangular (a cuboid with a cover plate) |
| 3 | EF000010 Model | hydraulic reservoir with cover plate, filler-breather, level gauge and clean-out cover |
| 4 | EF025939 Number of reservoirs | 1 |
| 5 | EF004752 Total volume | 59.0 l (gross: the body's inner size with 3 mm walls and bottom, 494 × 344 × 347 = 58.97 l; element.py asserts) |
| 6 | EF021376 Installation | free-standing on its two foot rails, on the floor or on a base frame |
| 7 | EF021672 Suitable for oil | yes (mineral hydraulic oil ISO VG 46, ISO 11158 HM; toolkit/hyd.py H7) |
| 8 | EF025941 Suitable for wastewater | no |
| 9 | EF025942 Suitable for fresh water | no |
| 10 | EF022633 Outer diameter, in/outlet | not stated: the suction and the return are port faces whose size is open (Open figures), not pipes |
| 11 | EF022634 Outer diameter, connecting pipe | not stated (as 10); the drain is a female NPT 3/8, pipe OD 17.1 mm (D = 0.675 in, pneu.NPT, ASME B1.20.1) |
| 12 | EF022635 Outer diameter, de-aerator | not stated (the filler-breather is a cap, not a pipe) |
| 13 | EF022631 With support strap | no |
| 14 | EF022632 With manhole | no (the Ø200 clean-out cover on the suction end is a hand hole) |
| 15 | EF001229 Couplable | no |
| 16 | EF001438 Length | 520 mm (the cover; the body 500; 526 over the drain boss) |
| 17 | EF000008 Width | 370 mm (the cover; the body 350) |
| 18 | EF000040 Height | 358 mm without the foot rails (the body 350 and the cover 8) |
| 19 | EF000551 Diameter | not stated (rectangular) |
| 20 | EF022185 With legs | yes (two foot rails, 50 high) |
| 21 | EF023164 Height including legs | 408 mm to the cover's top; 421 to the port faces; 448 to the filler-breather's top |
| 22 | EF022955 Diffusion-proof | not stated |
| 23 | EF001207 Corrosion resistant | not stated (painted steel) |
| 24 | EF025145 With built-in leak detection | no |
| 25 | EF014491 With level indicator | yes (the level gauge on the front, read by eye; no switch) |
| 26 | EF025155 Net weight | not stated |

These are generic design values (OPERATING.md 12), not tested ratings. The class has no pressure feature and the reservoir is at
atmosphere, vented by the filler-breather: it carries no pressure rating, so there is no ratings.csv and HYD-003 (toolkit/v_hyd.py)
has nothing to judge on it. The 10 bar of toolkit/hyd.py P_TANK is the return line's figure, the pressure that line's parts
(hyd-filter-return, hyd-cooler) are rated against; the tank itself is where that line ends.

**No safety claim.** A reservoir stores oil; it is no protective device, and this element claims no safety function (OPERATING.md
12; the inventory row's `safety` column is empty). It has no level or temperature switch: those are the circuit's, separate
elements.

## Dimensions (design choices, our own, but the drain bore)
| item | value | why |
|---|---|---|
| body | 500 × 350 × 350 (x −250 to 250, y −175 to 175, z 50 to 400); painted steel (`M-STEEL-7035`); 3 mm walls and bottom, used for the volume only | 59 l gross; the inside (the baffle between the return and the suction halves, the suction strainer, the return pipe) not modelled |
| foot rails | two, 40 × 330 × 50 high across the tank at x = −180 and +180 (0.5 into the body); black (`M-BLACK-PA`) | lift the tank 50 off the mounting plane so the drain can be reached and air passes under it; set in 10 from the body's sides and 50 from its ends (asserted) |
| cover plate | 520 × 370 × 8 (z 399.5 to 408, 0.5 into the body), 10 over the body on each side; painted steel | carries the ports and the filler-breather, as tank's |
| oil port blocks | 44 × 44 × 12 on the cover (z 407.5 to 420), at x = +150 (`port-suction`) and −150 (`port-return`), y = 0; painted steel | a flat face for each oil port; 256 between them (asserted ≥ 200) so the return oil crosses the tank; 78 in from the body's ends |
| oil port spot faces | Ø32 × 1 proud on each block's top (z 419.5 to 421, 0.5 into the block); `M-SILVER` | the joint plane a port fitting meets (hyd-filter-return 1.0's and hyd-cooler 1.0's pattern); 6 of block face round each (asserted); no bore cut (Open figures) |
| filler-breather | cap Ø50 × 40 on the cover at x = 0, y = +90 (z 407.5 to 448); black | fills and vents the tank; 43 clear of the blocks' row and 60 in from the body's side (asserted ≥ 20 each) |
| clean-out cover | Ø200 × 6 proud of the suction end (x 249.5 to 256), its centre at z = 225 (the body's mid height), y = 0; painted steel | a hand hole to clean the tank; 75 in from the end face's edges (asserted ≥ 50); inside the cover plate's 10 overhang; its bolts not modelled |
| drain boss | Ø28 × 16 along −x on the return end (x −266 to −249.5, 0.5 into the body), its axis at z = 70, y = 0; `M-GALV` | 20 above the body's underside, tank's figure; the boss wholly above the 3 mm floor plate (asserted) |
| drain bore | Ø17.055 × 12.358 deep, blind, in the boss from its face | Ø = E1 + h of NPT 3/8 from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up and 3 short of the boss's 16; 5.47 of boss wall (asserted ≥ 5). Role in features.csv (HOLE-010) |
| level gauge | frame 36 × 6 × 220 on the front face (y −181 to −174.5, z 150 to 370), black; clear window 20 × 2 × 204, 1 proud of the frame (`M-CASE-CLEAR`) | shows the level; 30 below the cover (asserted ≥ 20); tank's pattern |
| overall | envelope 526 × 370 × 448 (x −266 to 260, y −185 to 185, z 0 to 448) | |

## Ports (toolkit/hyd.py, toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-suction` | hyd-port | female | none | the spot face on the +x block, x = 150, z = 421, axis +z | design: named by its function (as hyd-filter-return 1.0's and hyd-cooler 1.0's ports); the hydraulic port marking standard (ISO 9461) is not on file, so no letter or number is claimed |
| `port-return` | hyd-port | female | none | the spot face on the −x block, x = −150, z = 421, axis +z | as `port-suction`; the tank line ends here |
| `port-drain` | NPT3/8 | female | none (a liquid port) | the boss's face, x = −266, z = 70, axis −x | pneu.py D1 (NPT, ASME B1.20.1); NPT 3/8 as tank's and coolant-pump's liquid ports; named by its function, no ISO 11727 number (that numbering is for pneumatic ports) |

"hyd-port" is toolkit/hyd.py's unit for a hydraulic port whose dash size is open (H1); HYD-001 reads a joint on it as REVIEW until
the size is stated, and HYD-002 wants every oil port joined or plugged in an assembly. No role: toolkit/pneu.py's roles are air
roles, and no HYD check reads one but `plug`. The drain is closed by a plug or a drain valve in the assembly (a male NPT 3/8 stub
screws in face to face).

## Open figures
- NOT ON FILE (B): SAE J1926-1 table 1, the suction and return ports' dash size, thread, spot face and depth (toolkit/hyd.py H1
  and H4: every cell of DASH is open; the standard is not in lib/standards/sources.csv). The two oil ports are plain spot faces
  with their pivots; the bores are cut once the table is on file (a major).

## Named nodes
`port-suction`, `port-return` (the spot faces), `port-drain` (the boss): kind port, fixed (range 0). Nothing moves.

## Materials by layer
`M-STEEL-7035` body, cover plate, oil port blocks, clean-out cover · `M-SILVER` oil port spot faces · `M-GALV` drain boss ·
`M-BLACK-PA` foot rails, filler-breather, level gauge frame · `M-CASE-CLEAR` level gauge window

## Decals (Blender)
None (the level marks, the port names and the "generic" label are a later version). No vendor names, no approval marks.

## Notes
- No mounting holes: the foot rails are plain in this version; their holes, with a clearance from lib/standards/holes.csv and a
  features.csv row, are a later version (a new cut-out, so a major).
- The suction and the return are at opposite ends of the cover with a baffle between them inside (not modelled): a design choice,
  so the return oil settles and cools before it is drawn again. No standard's clause is cited for it (ISO 4413 is not on file).
- A pump and motor on the cover (a power unit) are an assembly's, not this element's: hpu-7.5kw 1.1 is its own element with its
  tank built in, and hpu-0.37kw is an assembly of the lane's parts.
- The twin reads no level from it: the level comes with a hydraulic model (behaviour.csv).

## Outputs (out/)
`hyd-tank.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010413), pneu-r81 (unattended): rectangular pressureless hydraulic reservoir, body 500 × 350 × 350 (59 l gross) on two foot rails, cover plate; oil ports `port-suction` / `port-return` as spot faces on two blocks on the cover (hyd-port, the thread left open, class B); `port-drain` female NPT 3/8 low on the return end, bored Ø (E1 + h) × (L2 + 2) deep, blind in its boss; filler-breather, clean-out cover and level gauge; the baffle and the pipes inside not modelled; no pressure rating; nothing placed |
