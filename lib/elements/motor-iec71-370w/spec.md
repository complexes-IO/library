# motor-iec71-370w · v1.5 · 3-phase motor 0.37 kW IEC 71 B3

**What** 3-phase motor 0.37 kW IEC 71 B3. Built from the Stage 0 brief `references/measure.md`.
**Class** machine · **Baseline** maker's 2-D dimension drawing p. 1 (250.5 overall, shaft height 71, fan cover Ø138, feet 136 × 90 / holes 112 × 90, slots 7.0 along the shaft × 10.5 across (K = 7), shaft Ø14 × 30 key 5 × 5 × 25, terminal box 81 × 110, M20 entry) and cutsheet p. 1; IEC 60072-1 frame 71 (K = 7). The maker, product and documents are named only in references/. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: bench machine: foot plane z = 0, front-left foot hole x = 0, y = 0; shaft axis z = 71 toward −y.
**Built with** toolkit 1.3 · AutoLISP command `MOTOR` · no parameters.

## Dimensions
| item | value | source |
|---|---|---|
| overall length | 250.5: shaft end y −110 to fan cover end y 140.5 | drawing p. 1 (measure.md:16) |
| shaft height | 71.0 | drawing p. 1 (measure.md:17) |
| overall height | 175.5 (terminal box top) | drawing p. 1, 71.0 + 104.5 (measure.md:18, :19) |
| fan cover | Ø138 × 72, a 1.5 shell with its end face | drawing p. 1 (Ø); STEP read-back (length, measure.md:30); shell 1.1 |
| feet | 136 across, 8 thick, 24 wide each | drawing p. 1 (measure.md:21, :22) |
| foot length | 110: 10 past each hole centre | open figure, below |
| foot holes | 112 × 90; slots 7.0 along the shaft × 10.5 across, built as three Ø7 holes (the writer cuts round holes only) | drawing p. 1 (measure.md:21); IEC 60072-1 K = 7 (features.csv) |
| shaft | Ø14 × 30 from the shield face | drawing p. 1, cutsheet p. 1 (measure.md:23) |
| key | 5 × 5 × 25 (wide × high × long); built 5 wide × 25 long × 2.5 high, its top at the shaft's top line (z SH + 7) | drawing p. 1 (measure.md:23); the built 2.5 and the height above the axis: open figures, below |
| shield face to first hole row | 80 (shaft end 110 from the row) | open figure, below |
| terminal box | 81 × 110 in plan, top at 175.5, on the frame top (F3) | drawing p. 1 (measure.md:25); cutsheet p. 1 (F3); see review finding 2 (lib/needs-em/mech.md 22) |
| M20 entry | M20 × 1.5 on the box's right side; built Ø20 × 11.5 | drawing p. 1 (measure.md:25); its place: open figure, below |
| frame | Ø124 between the drive-end shield and the fan cover | open figure, below |

## Named nodes
`shaft` (rotate about −y, continuous) · `fan` (rotate, same speed) · `pwr` (kind port, unit 480V-3P+E, gender none: the M20 cable entry to the ring-lug terminals U1 / V1 / W1 and PE, PIN-002)

## Decals (Blender)
nameplate field on the frame side; rotation arrow on the fan cover (positions: open figures, below)

## Left out
- The shaft end's M5 tapped centre hole (drawing p. 1, detail A, measure.md:24): its depth and centre-hole form are not in the brief, and nothing in the library mates with it yet. It comes as a minor version with those figures.
- The interior (mechanism-first ruling): it arrives per interior-first-prompt.txt.

## Open figures
Each is a figure the brief does not give; a document figure replaces it as a minor version (or a major where it moves the body against the origin hole).
- **Assumption (B)**: FOOT_END 10, the foot's length past each hole centre (110 along the shaft). The brief's "foot length 90" equals the hole pitch, which would put the slots on the foot's ends (HOLE-020). Only the foot's outline depends on it.
- **Assumption (B)**: the drive-end shield face 80 from the first foot-hole row (shaft end 110). The drawing's 45.0 and 75.0 (measure.md:26) are not yet assigned; the reviewer reads them as IEC 60072-1's C = 45 and E + C = 75, which is not on file here. Moving the body is a major (2.0): lib/needs-em/mech.md 22.
- **Assumption (B)**: the M20 entry's place on the box side, y 45 and 16 above the box floor; a cable lands there.
- **NOT ON FILE (B)**: the key's height above the axis (GA) and the keyway depth. Neither IEC 60072-1 (GA) nor DIN 6885-1 (t1) is on file.
- **Assumption (B)**: the key built 2.5 high (of its 5 × 5 section, drawing p. 1), its top at the shaft's top line (z SH + 7, from SH + 4.5), so it stays inside the shaft's envelope (its bounding box) and adds nothing to it; its two top edges, at x ± 2.5, stand 0.46 outside the round Ø14 surface (√(7² − 2.5²) = 6.54) along its 25 length; how far the 5 high key stands above the shaft is GA, the figure above. A fit (a coupling hub's keyway meets it), so class B. GA or t1 on file replaces it as a minor: the key keeps its node (`shaft`).
- **Assumption (C)**: the frame radius 62 inside the fan cover radius (a housing wall).
- **Assumption (C)**: ten cooling fins, 6 × 2.5, from 20° at 14° steps on R + 3 (appearance).
- **Assumption (C)**: the drive-end shield, 12 long at R − 4 (a housing wall).
- **Assumption (C)**: the fan, Ø124 × 2, 60 inside the cover end (internal; the twin reads only its rotation).
- **Assumption (C)**: the webs from foot to frame, 16 × 70 × 29 (housing).
- **Assumption (C)**: the terminal box lid, 84 × 114 × 3 (appearance).
- **Assumption (C)**: the nameplate field, 0.6 × 50 × 30 on the frame side (a decal carrier).
- **NOT ON FILE (C)**: the rotation-arrow and 'M20' decal positions (Blender decals only, no geometry).

## History
| version | change |
|---|---|
| 1.5 | the reviewer's 1.4 finding 1 (lib/reviews/elements/motor-iec71-370w-1.4.md, lib/reviews/mech/r25.md), text only, the part unchanged: the key's top is at the shaft's top line (z SH + 7), inside the shaft's envelope; "stays inside the Ø14 shaft" withdrawn, since its top edges at x ± 2.5 stand 0.46 outside the round surface. Nodes, origin and cut-outs as 1.4, so a minor (mc-motor-1 pins 1.2) |
| 1.4 | the reviewer's 1.3 finding 1 (lib/reviews/elements/motor-iec71-370w-1.3.md), text only, the part unchanged: the Dimensions row gives the drawing's 5 × 5 × 25 key and the built 2.5 height; the 2.5 is an open figure of class B, with its reason, in the open figures and in element.py. Nodes, origin and cut-outs as 1.3, so a minor (mc-motor-1 pins 1.2) |
| 1.3 | the reviewer's 1.2 findings (lib/reviews/elements/motor-iec71-370w-1.2.md), the part unchanged: the brief and baseline give the foot holes as 7.0 × 10.5 slots, K = 7 (3); the key described as built, flush, its height an open figure, the M5 centre hole listed as left out (4); every figure not from the brief marked with its class in the open figures and in element.py (5); maker and part number out of spec, code and baseline, ratings.csv's source a page (6); ratings.csv's unused eta_pf_min row removed, FLA on file (7); pins.csv pages; `pwr` gender none (PIN-002). Findings 1 and 2 need the drawing or IEC 60072-1 (lib/needs-em/mech.md 22). Nodes, origin and cut-outs as 1.2, so a minor (mc-motor-1 pins 1.2) |
| 1.2 | terminal figures 2026-11-03: foot holes are 7.0 along the shaft × 10.5 across slots (drawing p. 1; K = 7 per IEC 60072-1), built as three Ø7 holes (the writer cuts round holes only); the feet were 90 long with the holes on their ends (HOLE-020): now 110, 10 past each hole centre (FOOT_END, an open figure of class B, above); FLA 0.91 A at 460 V on file |
| 1.1 | validation suite finding (GEO-010): the fan cover was a solid cylinder with the fan inside it; now a 1.5 shell with its louvred end face, fan Ø124 clear of the terminal box |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |

## Deliberate differences
<!-- acad-gate motor-iec71-370w -->
- AutoCAD gate 2026-11-06 (motor-iec71-370w 1.5, mech-r32): STEP extents [138.0, 250.5, 175.5] mm; vs glb [0.0, 0.0, 0.0] mm; brief figures (toolkit/figcompare.py, ISO 2768-1 m): 2 found (the overall length 250.5 and height 175.5 on their own axes), 10 not located (part figures the compare does not measure since round 12; 1.3's "10 found" counted matches to unrelated solids, escape group 6). Fillet r 0.5 on edges > 3 mm: 2 of 91 rejected (2.2 %, 0 on the envelope): two 6.0 fin edges (M-CAST-BLUE, at y 64.5) that 1.4's run on the same part filleted (0 of 91).
