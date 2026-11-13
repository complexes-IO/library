# contactor-9a-1no1nc · v1.3 · IEC contactor 9 A, 24 V DC coil

**What** IEC contactor 9 A, 24 V DC coil. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** device · **Baseline** maker's datasheet and 2-D drawings (references/measure.md; the reference part's record in references/source.txt): contactor drawing p. 1 (44.8 × 78.4 × 98.5; 70 × 35 pattern); front aux block drawing p. 1 (45 × 46 × 42); series spec p. 6, 9, 17. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0.
**Built with** toolkit 1.3 · AutoLISP command `CONT` · `aux` (true: the front aux block fitted).

## Dimensions
| item | value |
|---|---|
| body | 44.8 × 78.4 × 98.5: rear base 39.2 deep with the terminal shoulders, coil housing 56 high to 98.5 |
| power terminals | L1 L2 L3 top, T1 T2 T3 bottom, 14.0 pitch (interior brief, STEP read-back; 1.0 had 14.5, see Terminal rows below) |
| coil and aux | A1 A2, 13/14, 21/22 on the housing top edge |
| aux block | 45 × 46 × 42 on the coil face, 53/54 and 61/62; fitted depth 140.5 |

## Mechanism (v1.1, built mechanism-first from references/interior.md, parts.csv, behaviour.md)
Fixed E-core (back plate, two outer legs, centre leg) and the 24 V DC coil on the centre leg sit in the base; the armature and the
contact carrier are one moving assembly that travels **+y, toward the mounting plate** (normal to it, consistent with the any-orientation
mounting of spec p. 10). The carrier holds three double-break main bridges on contact springs, the two built-in auxiliary bridges, and
drives the front block's slide through a window in the face. Two return springs between the base and the carrier bring it back.
The carrier meets every bridge it drives (1.3, MOT-020), each stop at z −3 … 3 where no fixed strip runs: a bar across the three main
bridges' +y faces (y −53.6 … −52.6; each contact spring presses its bridge onto it, the bridge stops on its rivets after the 2.0 gap and
the bar runs on by the 1.5 over-travel), a stop across the window on the N.O. aux bridge's +y face, and a pusher on the N.C. aux bridge's
−y face that lifts it off its strips. The front block's slide carries a yoke the same way: a bar on the N.C. bridge's −y face (61-62) and
a post on the N.O. bridge's +y face (53-54). The fixed aux strips, built-in and front block, run to the housing walls (GEO-070).
Coil data, contact ratings, timings and life live in parts.csv as model parameters (coil 5.8 W, ≈ 99 Ω derived; pick-up 12–19.2 V;
drop-out 2.4–9.6 V; close 35–45 ms, open 8–12 ms; 9 A AC-3, 25 A AC-1, 4.4 A AC-4; 2.5 mΩ per pole; 2 million AC-3 operations).

**Assumption (C)**, internal mechanism and walls the twin doesn't read (OPERATING.md 6, class C; none of it is in the brief): contact
gap 2.0 per break and over-travel 1.5 (stroke 3.5) · E-core 28.8 wide, outer legs at z ±14…20, centre leg ±5, legs ending at y −30 ·
armature 5 thick, gap 3.5 released · coil as a block on the centre leg · carrier frame (rear plate, side columns, crossbar at y −60,
front crossbar at −84, stem to the face, the 1.3 stops) · fixed main strips at y −49…−50.5 with rivets Ø3.6, bridges 6 × 24 × 2 · two
return springs Ø2.8, nine turns · contact springs Ø3.2 · housing wall 2.0 · front block slide, yoke and bridges.
**Assumption (B)**, where a wire meets the part (the maker's drawing would give it; it gives none of these): built-in aux 13–14 at
x 36.8 and 21–22 at x 8.0, A1 / A2 at x 22.4 on the top / bottom edges.
**Terminal rows** now at z ±31.5 and 14.0 pitch (interior brief STEP read-back; v1.0 had 14.5 from the Stage 0 brief). The overload's pins are
at 14.5 (its brief): a 0.5 mm disagreement between two read-backs, to be re-measured on both STEPs.

## Named nodes (v1.1)
`coil` (emissive in x-ray) · `armature`, `carrier` (translate +y, 0–3.5) · `pole-1..3` (translate +y, 0–2.0: the bridges stop on the fixed
contacts) · `spring-contact-1..3` (compress 0–1.5: the over-travel) · `spring-return` (compress 0–3.5) · `aux-13` (N.O., closes),
`aux-21` (N.C., opens) (translate with the carrier) · `front-block` (fixed), `fb-slide`, `fb-53`, `fb-61` (translate with the carrier)
· ports `t-1 … t-6` (main), `t-a1`, `t-a2`, `t-13`, `t-14`, `t-21`, `t-22`, `t-53`, `t-54`, `t-61`, `t-62` (kind port, unit screw,
gender none: screw clamps, PIN-002, since 1.3).
Parameters: `aux` (true), `view` (product | cutaway: face and −x walls removed), `operated` (false).

## Named nodes (v1.0, superseded by the list above)
none visible (the armature is internal; state lives in the circuit)

## Materials by layer
`M-GREY-PA` body, block · `M-ZINC` screws · `M-WHITE-PA` label field · `M-GASKET` openings

## Decals (Blender)
terminal marks, 24 VDC coil mark on the label field; no vendor label

## Notes and assumptions
The aux block is a parameter, not a carried element: it has no state and no origin of its own. Every figure classed B or C above is set here, no document on file giving it; a document figure replaces it as a minor version.

## Outputs (out/)
`contactor-9a-1no1nc.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.3 | elec-r51 (unattended), the backlog's checks: MOT-020, the carrier's stops on the main bridges and both built-in aux bridges and the front block slide's yoke on its two bridges, so every follow pair of lib/motion.csv meets within the stroke; GEO-070, the fixed aux strips (built-in and front block) run 0.5 further to the housing walls; PIN-002, gender none on the 16 screw-clamp ports; DOC-006, the maker's and part names out of BASELINE and this spec (references/ only); the open mechanism figures classed C and the aux and coil terminal positions B; the Dimensions pitch row 14.0 as built. Nodes, origin and cut-outs as 1.2 |
| 1.2 | terminal figures and the suite (2026-11-03): the drawing's 98.5 runs from the rail back, so the rail sits in a groove in the base: coil face at −91.0 from the crown, rear lugs either side of the ±18.4 groove down to the mounting plane, a rail latch tongue (was a clip behind a body standing on the crown: 148.0 against 140.5); 70 × 35 screw pattern cut, Ø4.5 (then an assumption: the drawing p. 1 gives it, terminal round 2); clamp entry holes at the lower and upper terminals (the overload's pins come up through them; the dark wire-entry plates are gone); slots for the overload's hooks in the lower lug; window in the carrier's front crossbar for the N.O. aux bridge (GEO-010) and its stop at 2.6; window in the coil face for the front block's slide, which now reaches the stem (MOT-010); front block N.O. stops at 2.0; label field only without the front block |
| 1.1 | mechanism-first: E-core, coil, armature and carrier, three bridges on contact springs, return springs, built-in aux, front-block slide; shells for the housings; terminal ids as port nodes; rows at 14.0 / ±31.5 (interior brief) |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
