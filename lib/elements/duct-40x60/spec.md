# duct-40x60 · v1.3 · slotted wiring duct 40 × 60

**What** slotted wiring duct 40 × 60 with a snap-on cover, PVC, cut to length. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** run (lib/README.md, Conventions, origins: a part cut to length along a run) · **Baseline** reference duct 40 × 60: 2-D drawing p. 1 (40.0 × 60.1 section, 8.0 slots); STEP read-back (base 57.7, cover 8.8). The maker, product and drawing are named only in references/. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: panel face y = 0, run start x = 0, section bottom z = 0; run along +x, 40 across z, 60.1 toward −y.
**Built with** toolkit 1.3 · AutoLISP command `DUCT` · `length` (1000), `cover` (true), `breakout` (none; below).

## Parameters
| parameter | default | what it does |
|---|---|---|
| `length` | 1000 | the run along +x, in mm; the fingers repeat at the 20.0 pitch from x = 0 and the last one is cut at the end |
| `cover` | true | the snap-on cover (node `cover`) built on the fingers; false leaves the base open |
| `breakout` | none ("") | where an installer breaks a finger off for a cable too thick for the 8.0 slots (1.3; lib/requests/core/mech-duct-breakout-2026-11-11.md, from request panel-11 item 1): positions along the run in mm joined by `/`, each optionally prefixed by its finger wall, `a` (the wall at z 0) or `b` (the wall at z 38.5, W − T); a bare position names both walls. The finger whose span holds the position is not drawn, so the slots either side of it join into one gap 28 wide (the pitch 20.0 plus a slot 8.0), centred on the finger's centre; a position in a slot names the nearer of the two fingers beside it (the one before on a tie). A position outside 0 to `length`, or a token that is not a position, stops the build. In a BOM row: `length=1200;cover=true;breakout=278/b305` |

A breakout changes the model only where it is asked for: the default build is 1.2's part. Whether the fingers are scored for breaking is a figure of the
product the brief measured (references/measure.md has none) and is not needed to leave a finger out, so none is stated.

## Dimensions
| item | value | source |
|---|---|---|
| section | 40.0 (z) × 60.1 (−y) | 2-D drawing p. 1 (measure.md:13-14) |
| base | 57.7 off the panel | STEP read-back, base solid (measure.md:22) |
| cover | 8.8 high: lid 2.4 on the finger tops (60.1 − 57.7) and two skirts reaching 6.4 down over the fingers (8.8 − 2.4) | STEP read-back, cover solid and overlap (measure.md:18, :22) |
| slots | 8.0 wide, both walls | 2-D drawing p. 1, 0.315 in (measure.md:16) |
| slot pitch, finger height | 20.0, 25 from the top of the wall | open figure, below |
| walls and fingers | 1.5 thick | open figure, below |
| skirts | 1.2 thick, 0.2 clear inside the walls | open figure, below |
| floor slots | not modelled | open figure, below |
| length | a parameter (1000 default); supplied as 1981.2 and cut to the row (measure.md:15) | 2-D drawing p. 1 |

## Rating
Flammability class UL 94 V-0 (the material's test class, a standard, not an approval mark): product page, `references/source.txt` line 3 and
measure.md:7. A rating of this product, not of the library's PVC; nothing in the library rests on it yet. If a panel's fire case comes
to rest on it, it becomes a class A figure for EM (lib/needs-em/mech.md).

## Named nodes
`cover` (translate −y, away from the panel, 0–40: lifted off)

## Materials by layer
`M-WHITE-PVC` base and cover (1.2): the part is PVC (product page). The layer renders with M-WHITE-PA's white (toolkit/cadout.py,
preview.py; Godot lib/godot/qa/materials/M-WHITE-PVC.tres), as lib/requests/mech/1.md asked and lib/requests/core/mech-1-answer.md
item 2 gave. lib/materials.csv's pvc row holds no flammability class; the duct's stays under Rating, with its source.

## Parts
Each finger is named `part="duct-finger"` (toolkit/prims.py; 1.2, lib/requests/core/mech-idle-2026-11-06.md). The AutoCAD gate keys
its finger exclusion (EM 2026-11-03: counted, never filleted) on that name first (acad-gate.py, round 14 B b), so a changed finger
height can't end the exclusion silently. No output reads the name: layers, census, glTF and previews are 1.1's.

## Decals (Blender)
none (plain white PVC)

## Open figures
Each is a figure no document on file gives; a document figure replaces it as a minor version (or a major where it moves a cut-out).
- **Assumption (B)**: slot pitch 20.0 and finger height 25. The drawing's 0.7874 in and 0.9843 in are uncaptioned; "slot pitch, finger height"
  is the brief's reading of the drawing image (measure.md:17), not confirmed. Unblocks: one attended look at drawing p. 1, or the STEP's
  finger count per 1981.2 run (measure.md:29).
- **Assumption (B)**: wall and finger thickness 1.5. The brief's readings 4.5 (0.1772 in) and 6.5 (0.2559 in) for "wall and finger thickness"
  are uncaptioned (measure.md:17); a 4.5 wall would leave 31 of the 40 inside, so the build keeps 1.5 until the drawing look.
- **Assumption (B)**: the cover's skirts sit inside the walls. The brief gives the 6.4 overlap but not the side; both solids read 40.0 wide
  (measure.md:22), so a skirt outside the walls would need a step in the finger tips that nothing on file shows.
- **Assumption (C)**: skirt thickness 1.2 and 0.2 clearance to the wall (a housing wall and the snap's play; the twin reads neither).
- **NOT ON FILE (B)**: the floor slots' size, shape and spacing, and the panel screw they take. The brief says only "screw-on mount,
  through the floor slots" (measure.md:25). 1.1 leaves the back wall plain rather than guess them; adding them adds cut-outs, so it
  comes as a major (2.0) together with a new pin in pm-motor-starter's bom.csv (the core's file; it pins 1.0). The screw is a common
  part (OPERATING.md 12): that version places a screw element; none is drawn here (1.0's discs are gone).
- **Assumption (C)**: cover lift-off travel 40 (motion only; measure.md:37 has no figure for the snap travel).

## Outputs (out/)
`duct-40x60.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build from the Stage 0 brief, toolkit 1.2; rebuilt under toolkit 1.3 with no change to the part |
| 1.1 | the reviewer's 1.0 findings (lib/reviews/elements/duct-40x60-1.0.md): base 57.7 with the cover's skirts 6.4 over the fingers (finding 2); the drawn screw heads removed, the floor slots left out until their figures are on hand (finding 3; no new cut-out, so a minor: nodes, origin and cut-outs as 1.0); open figures marked with class and reason (finding 1); UL 94 V-0 out of the title, kept here as a sourced rating (finding 4); maker and part number out of the spec, code and baseline (finding 6, DOC-006); toolkit 1.3 |
| 1.2 | the reviewer's 1.1 finding 1 (lib/reviews/elements/duct-40x60-1.1.md): metadata.json's verification_status takes the AutoCAD import record of 2026-11-03 (validation.json autocad_import) in place of the 2026-11-02 "not confirmed" note; CLASS run (mech-1-answer.md item 1); the M-WHITE-PVC layer (item 2); the fingers named duct-finger (the core's mech-idle note). The part unchanged: nodes, origin and cut-outs as 1.1, so a minor (pm-motor-starter pins 1.0) |
| 1.3 | the `breakout` parameter (lib/requests/core/mech-duct-breakout-2026-11-11.md; request panel-11 item 1: the motor starter panel's 9.8 supply cordset passes no 8.0 slot): the finger holding each named position is left out of its wall, Parameters above. The default build is unchanged: the same solids, nodes, origin and cut-outs, so a minor (pnl-motor-starter and pnl-press-hydraulic pin 1.2, pm-motor-starter 1.0); the panel shop pins 1.3 in the row the cordset enters (mech-r106, unattended) |

## Deliberate differences
<!-- acad-gate duct-40x60 -->
- AutoCAD gate 2026-11-06 (duct-40x60 1.2, mech-r25): STEP extents [1000.0, 60.1, 40.0] mm; vs glb [0.0, 0.0, 0.0] mm; brief figures (toolkit/figcompare.py, ISO 2768-1 m): 6 not located, as 1.1's run of the same day: the section's 40.0 and 60.1 (equal to the STEP extents' z and y; measure.md's rows start "section", not with an axis word, so figcompare reads them as part figures; the duct's height runs along −y, not z), the 1981.2 supplied length (cut to the run), and the slot 8.0, the 20.0 and the cover 8.8 (gaps or parts the compare does not measure). Fillet r 0.5 on edges > 3 mm: 0 of 18 rejected (0.0 %, 0 on the envelope); 100 fingers excluded by part name (duct-finger).
