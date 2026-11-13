# tank · v2.2 · generic storage tank, rectangular, pressureless

**What** a small rectangular storage tank for a liquid: hydraulic oil as the reservoir of a small hydraulic power unit (hpu-0.37kw,
hydraulic-trainer), or process water (lib/inventory.csv row `tank`: 4 systems, cleaner-industrial, heat-exchanger-loop,
process-skid and test-bench-hydraulic, as recounted on main 66e237e).
It holds the liquid at atmospheric pressure: the filler-breather on the cover vents it. Liquid leaves by `port-out`, comes back by
`port-return` and is emptied by `port-drain`; the sight gauge on the front shows the level.
**Class** device · **Baseline** our own design: generic storage tank (ETIM 10.0 EC010413), as OPERATING.md 12 (generic elements, EM
2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or measured. The class values below are its
design inputs; its sizes are design choices; its ports take their thread from the standard on file (ASME B1.20.1, through
toolkit/pneu.py). No vendor names.
**Units / frame** mm, Z up. Origin: the centre of the bottom face, on the floor (z = 0); length along x, width along y. Ports follow
pneu.py's port frame: the pivot on the joint plane (the boss face), its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `TANK` · no parameters (one size).

## Class values (ETIM 10.0 EC010413, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF002169 Material | steel, painted light grey (body, cover); zinc-plated steel port bosses |
| 2 | EF000051 Shape | rectangular (a cuboid with a cover plate) |
| 3 | EF000010 Model | reservoir with cover plate, filler-breather and sight gauge |
| 4 | EF025939 Number of reservoirs | 1 |
| 5 | EF004752 Total volume | 22.8 l (gross: the body's inner size with 3 mm walls and bottom, 394 × 244 × 237) |
| 6 | EF021376 Installation | free-standing on the floor or on a base frame |
| 7 | EF021672 Suitable for oil | yes (hydraulic oil) |
| 8 | EF025941 Suitable for wastewater | no |
| 9 | EF025942 Suitable for fresh water | not stated |
| 10 | EF022633 Outer diameter, in/outlet | 17.1 mm: the NPT 3/8 pipe OD D = 0.675 in (pneu.NPT, ASME B1.20.1); the ports are female threads |
| 11 | EF022634 Outer diameter, connecting pipe | 17.1 mm (NPT 3/8 pipe, as 10) |
| 12 | EF022635 Outer diameter, de-aerator | not stated (the filler-breather is a cap, not a pipe) |
| 13 | EF022631 With support strap | no |
| 14 | EF022632 With manhole | no |
| 15 | EF001229 Couplable | no |
| 16 | EF001438 Length | 420 mm (the cover; the body 400) |
| 17 | EF000008 Width | 270 mm (the cover; the body 250) |
| 18 | EF000040 Height | 248 mm to the cover's top; 278 to the filler-breather's top |
| 19 | EF000551 Diameter | not stated (rectangular) |
| 20 | EF022185 With legs | no |
| 21 | EF023164 Height including legs | not stated (no legs) |
| 22 | EF022955 Diffusion-proof | not stated |
| 23 | EF001207 Corrosion resistant | no (painted carbon steel) |
| 24 | EF025145 With built-in leak detection | no |
| 25 | EF014491 With level indicator | yes: a sight gauge on the front face |
| 26 | EF025155 Net weight | not stated |

Pressure: EC010413 has no pressure feature; the class is a pressureless storage tank by its synonyms ("Pressureless storage
tank", "Storage tank, pressureless"), and the filler-breather vents it. ratings.csv holds p_max 0 bar (gauge), status "generic
design", its source a design choice from the class (2.0: review pneu-r48 finding 3; 1.0's source called it a class value), so
PNE-003 refuses it on any line that carries pressure: a pump's suction and a return line at atmospheric pressure only. A generic
design value (OPERATING.md 12), not a tested rating.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| body | 400 × 250 × 240 (x, y, z), z 0 to 240; painted steel | about 20 l usable for a 0.37 kW unit (hpu-0.37kw's motor-iec71-370w); walls (3 mm) not modelled, used for the volume only |
| cover plate | 420 × 270 × 8, on the body (z 240 to 248), 10 over each side | a lid for the parts a power unit carries on top |
| filler-breather | Ø40 × 30 on the cover at x = −120; black polyamide | fills the tank and vents it to atmosphere (pressureless) |
| port bosses | Ø28, 6 proud of their faces; zinc-plated steel | a half coupling for an NPT 3/8 female thread: at least 3 mm round the pipe OD (17.1), asserted in element.py |
| port bores | Ø17.055 plain, 12.358 deep from the boss face (L2 10.358 + 2), through the boss into the body (ends) or the cover (top) | Ø = E1 + h from pneu.NPT (ASME B1.20.1 by its formulas): the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap; the 2 mm past L2 is a design choice (a run-out, so the stub never bottoms); 5.5 mm of boss wall round it |
| sight gauge | frame 36 wide × 6 deep, z 40 to 210, on the front face (y = −125); clear window 20 wide, 1 proud of the frame, z 48 to 202 | the level shown over most of the height |
| envelope | 420 × 270 × 278 | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-out` | NPT3/8 | female | the right end's boss face x = 206, z = 40, axis +x | outlet (pump suction), low so the liquid reaches it |
| `port-return` | NPT3/8 | female | the cover's boss face z = 254, x = 120, axis +z | return, on the cover, on the outlet's half (80 in x from the outlet's face); see Open figures |
| `port-drain` | NPT3/8 | female | the left end's boss face x = −206, z = 20, axis −x | drain, low on the left end (its bore's lower edge at z = 20 − 17.055 / 2 = 11.47, 8.47 above the inner floor at z = 3, so 394 × 244 × 8.47 = about 0.8 l stays in); see Open figures |

Thread: NPT (ASME B1.20.1; pneu.NPT holds NPT 3/8's figures as values calculated from its formulas, EM 2026-11-07). NPT 3/8 is the
largest size the lane has on file (pneu.THREADS). The ports carry no role: a tank is not on the air line. PNE-002 pairs each with a
male NPT 3/8 of the same size (sealant on the male). Each boss face is the joint plane a placed fitting meets; 2.0 cuts the bores
behind it (their role in features.csv, HOLE-010), a major because the cut-outs changed (OPERATING.md 7). The thread is drawn
plain at one diameter for both halves, E1 + h, as the library draws M12 and gland threads; which diameter every pneumatic host
and male share is the core's to fix in pneu.py (review tank-1.0 note 1); this element uses the one fitting-pushin 2.0 uses.

## Open figures
- NOT ON FILE (B): the hydraulic reservoir rules (ISO 4413, hydraulic fluid power, general rules) are not in
  lib/standards/sources.csv, so where the return and the drain sit for a hydraulic use (return apart from the suction, full
  drainage; review pneu-r48 finding 2) has no clause on file. As drawn, port-return is on the outlet's half and the drain leaves
  about 0.8 l. Moving them is a later version (one geometry finding a round, autopilot.md 2a); the clause comes with ISO 4413.
Every other figure is a design choice, a class value above, or from the standard on file.

## Named nodes
`port-out`, `port-return`, `port-drain` (the bosses); kind port, fixed (range 0)

## Materials by layer
`M-STEEL-7035` body and cover · `M-GALV` port bosses · `M-BLACK-PA` filler-breather and sight-gauge frame · `M-CASE-CLEAR` gauge window

## Decals (Blender)
None (1.0 to 2.1; a "generic" label and port names are a later version). No vendor names.

## Outputs (out/)
`tank.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010413), pneu-r48 (unattended): body, cover, filler-breather, three NPT 3/8 port bosses with pivots, sight gauge |
| 2.0 | pneu-r55 (unattended), review pneu-r48: the three port bores cut, Ø E1 + h, L2 + 2 deep, roles in features.csv (finding 1); ratings.csv's source reworded, EC010413 has no pressure feature (finding 3); the ports' text says where port-return and the drain are drawn, and the hydraulic reservoir rules wait on ISO 4413 as a class B line (finding 2, its move a later version) |
| 2.1 | text only, pneu-r65 (unattended; review tank-2.0.md findings 1 and 2, pneu-r55 finding 3): the drain leaves about 0.8 l (0.81, from the 2.0 bore's lower edge), the Decals line no longer says 1.0, the inventory row's 4 systems; behaviour.csv added (BEH-010). No shape change |
| 2.2 | text only, pneu-r73 (unattended; review tank-2.1.md finding 1, pneu-r65 finding 1): element.py's docstring names the inventory row's four `used_by` systems (cleaner-industrial, heat-exchanger-loop, process-skid, test-bench-hydraulic), as the What line does, no longer the pre-recount list. No shape change |
