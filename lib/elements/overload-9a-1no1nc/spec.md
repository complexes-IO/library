# overload-9a-1no1nc · v1.2 · thermal overload relay, class 10, range by parameter

**What** Three-pole bimetallic thermal overload relay, trip class 10, 1 N.O. (97-98) + 1 N.C. (95-96), direct mount under the 9 A contactor; built mechanism-first from the Stage 0b brief `references/interior.md`, `parts.csv`, `behaviour.md` and the Stage 0 brief `references/measure.md` (mate with the contactor measured on both STEPs, 2026-11-03).
**Class** device · **Baseline** maker's datasheet and 2-D drawing (references/measure.md, references/interior.md, references/source.txt): drawing p. 1 (45.0 × 71.7 × 83.7; pins Ø2.5 at 14.0; motor terminals at 14.5; install dimension A = 136.4 with the 9 A contactor, contactor-9a-1no1nc); spec p. 2 (mechanism, RESET/TEST positions), p. 3 (ranges), p. 5–8 (aux ratings, terminals, curve). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: carried: back face on the contactor's mounting plane, x = 0 at the left face, z = 0 at the top of the upper housing (the contactor's rail centre line − 39.2, 0.4 below its bottom on the STEP); body toward −y, hanging toward −z.
**Built with** toolkit 1.3 · AutoLISP command `OVLD` · `range` (D012), `view` (product | cutaway), `tripped` (false), `mode` (H | HAND | AUTO | A).

## Range (maker's spec p. 3; the same body for every range)
`range` picks the setting range and the maximum fuse; the ratings checker reads them through `ratings_for()`: D004 0.28–0.40 · D008 0.56–0.80 · **D012 0.8–1.20** · D018 1.2–1.80 · D028 1.8–2.80 · U004 2.8–4 · D063 4–6.30 · U008 5.6–8 · U010 7–10 · D125 8–12.5 A. The motor-starter cell uses D012 for its 0.91 A motor (EM 2026-11-03; ELR-010).

## Dimensions
| item | value | source |
|---|---|---|
| housing | 45.0 wide; full-depth body 47.0 tall × 77.0 deep; upper housing 60 deep to 57.6 above the bottom; 6.7 front projection (83.7 overall) | drawing p. 1; STEP |
| pins L1 L2 L3 | Ø2.5 × 22, pitch **14.0**, x 5.3 / 19.3 / 33.3 (3.2 left of centre); tips 71.7 above the bottom; Ø4.4 sleeves to 60.9 | drawing p. 1; STEP |
| pin row depth | y −42.0 under the contactor's lower clamps | Assumption (B): where the pins meet the contactor; not on the drawing pages read (the maker's drawing would give it) |
| motor terminals T1 T2 T3 | pitch 14.5 at x 8.0 / 22.5 / 37.0; clamps 7.8 × 9.2 × 15.2; screws on the front | drawing p. 1; STEP |
| aux terminals 95 96 97 98 | x 6.75 / 17.25 / 27.75 / 38.25 at 10.5 pitch, front, upper row, screw heads 0.2 inside counterbores; which mark is which block: Assumption (B), the order 95 96 97 98 from the left (the maker's terminal page would give it) | STEP; spec p. 2 |
| rear hooks | two Ø4 hooks to 67.3 above the bottom, into the contactor's lower lug slots | STEP (positions); form round: Assumption (B), the fit into the contactor's slots |
| RESET / TEST and dial | button Ø10 red at x 8 (front left), dial Ø12 at x 34 (front right), both at z −30.6, faces 0.2 inside their counterbores (the 83.7 depth); button 2.0 press | STEP (positions); travel Assumption (C): a motion the twin reads at its two ends only |
| wall | 1.5 | Assumption (C): a housing wall |

## Mechanism (positions not in the brief, set here: Assumption (C), internal mechanism the twin doesn't read; 1.2 made each driver meet its follower)
Each phase: pin → heated bimetal strip (`bimetal-1..3`, 4 × 0.8, root z −14 to free end −40, bends 2.5° toward −y at trip) → copper link under the trip slide → motor terminal clamp. `bimetal-2`'s tip rests on the `differential` slide (−y, 1.0; 1.2 in front of the free ends, so `bimetal-1` and `-3`, whose 2.5° swings their ends 1.13, clear it in this model); the differential rests on the `trip-slide` (−y, 1.5) beside the ambient `comp-bimetal` (hung from the upper housing's top on a post); the latch's tooth is held on the trip slide's +y face, so the slide moving −y releases the `latch` (rotate 12°), whose pushers rest on the auxiliaries' bridges: `aux-95` (N.C.) is pushed off its strips, `aux-97` (N.O.) onto its strips after its 1.0 gap. `btn-reset` presses 2.0 (reset in H / HAND, test in HAND / AUTO, spec p. 2); `dial-fla` turns 270° over the range (the angle span: Assumption (C), appearance). Couplings in `lib/motion.csv` (bimetal-2 → differential → trip-slide → latch → aux-95, aux-97). The behaviour (trip time from the class 10 limits, thermal memory, phase-loss and ambient compensation) is in `behaviour.md` and principles x20–x22.

## Named nodes
`bimetal-1..3` (rotate) · `comp-bimetal` (fixed) · `differential`, `trip-slide` (translate −y) · `latch` (rotate) · `aux-95`, `aux-97` (translate −y) · `btn-reset` (translate +y) · `dial-fla` (rotate) · ports `main` (pins, unit pin), `motor` (T1–T3, screw), `aux` (95–98, screw); pins.csv lists every pin.

## Materials by layer
`M-GREY-PA` housing, sleeves · `M-CU` pins, links, clamps, contacts · `M-STEEL-7035` bimetals · `M-WHITE-PA` slides, dial, scale field · `M-BLACK-PA` latch · `M-RED-PA` button · `M-ZINC` screws

## Decals (Blender)
dial scale for the range (D012: 0.8–1.2 A), A / AUTO / HAND / H, 95-96-97-98; no vendor label

## Deliberate differences
The STEP is exterior only: the interior is our own construction from the documented behaviour. The 4 W-class heater and bimetal are one solid per phase. The tripping curve (spec p. 8) is an image and is not digitised.
<!-- acad-gate overload-9a-1no1nc -->
- AutoCAD gate 2026-11-05 (overload-9a-1no1nc): STEP extents [45.0, 84.9, 71.7] mm; vs glb [0.0, 0.0, 0.0] mm; every brief figure found in the build within 2 mm (overall or on a solid). Fillet r 0.5 on edges > 3 mm: 0 of 30 rejected (0.0 %, 0 on the envelope).
<!-- acad-gate overload-9a-1no1nc-cutaway -->
- AutoCAD gate 2026-11-05 (overload-9a-1no1nc-cutaway): STEP extents [45.0, 84.2, 71.7] mm; vs glb [0.0, 0.0, 0.0] mm; every brief figure found in the build within 2 mm (overall or on a solid). Fillet r 0.5 on edges > 3 mm: 0 of 68 rejected (0.0 %, 0 on the envelope).

## Outputs (out/)
`overload-9a-1no1nc.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png` (front, top pins, cutaway, tripped cutaway). Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.2 | the backlog's checks, nodes and origin as 1.1: MOT-020 x4, each driver meets its follower at rest (bimetals bend toward −y, bimetal-2's tip on the differential, the differential on the trip slide, the latch's tooth on the trip slide's +y face, the latch's riser, pushers, cross bar and finger on both aux bridges); GEO-070 x7, the aux strips seated under the body's top, the heater links run to the motor clamps' back faces, the compensation bimetal on a post from the upper housing's top; PIN-002, genders on main (male), motor and aux (none); DOC-006, the maker's and part names out of TITLE, BASELINE, spec.md and ratings.csv; the depth, 83.9 with the legend field (aux screws, button and dial inside the face; the brief's 83.7 to the face); the spec's open lines classed B or C |
| 1.1 | mechanism-first from the Stage 0b brief; pin pitch 14.5 → **14.0** (the 14.5 is the motor-terminal pitch; MATE-010), Ø2.5 round pins and sleeves in a 3.2 off-centre row (were 7.8 × 9.2 blocks), body 47 + upper housing 10.6 (was 65; GEO-020), seat at rail − 39.2 as measured; rear hooks; `range` parameter over the maker's setting ranges (default D012); views product / cutaway, tripped, mode |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
