# enc-fs-1524x1829x305 · v1.9 · floor-standing two-door control cabinet

**What** Floor-standing two-door control cabinet, dust-tight, NEMA 12 / IP55, powder-coated steel, key lock, floor stand.
**Class** enclosure · **Baseline** the 60 × 72 × 12 in class (the maker's catalogue drawing and STEP; the product is named only in references/source.txt); measured from them, rebuilt here. Nothing of the vendor file is shipped.
**Units / frame** mm, Z up, right-handed. Origin: floor plane, front-left anchor hole of the left front leg; doors face −y.
**Built with** toolkit 1.3 · AutoLISP command `ENC` · parameters `swing_l`, `swing_r` (door swing in degrees, 0 closed; operators are cut only in the closed frame).

## Dimensions
| item | value |
|---|---|
| body W × H × D (outside) | 1524 × 1829 × 305 |
| sheet | 14 ga (1.9 mm) body and doors |
| doors | two, 757.5 wide each (left door carries a 20 mm astragal over the meeting edge), 3 mm gaps, 13 mm margins top and bottom (door height 1803), 25 mm returns, continuous hinges on the outer edges |
| handle | 3-point latch, 25 wide escutcheon, key cylinder, right door, its edge 50 from the meeting edge, centre 1180 above the floor |
| floor stand | two channel legs 206 wide × full depth × 305 high, flush with the body sides, 3 mm sheet; 60 mm floor flange front and back with a Ø11.1 anchor hole each (7/16 in, since 1.6); anchor centres 1318 apart |
| back panel | 1372 × 1676 × 2.5 galvanised, on four M10 studs 25 off the back wall; stud holes Ø11 (M10 clearance, medium, ISO 273; lib/standards/holes.csv:20), 40 in from the panel corners, 1292 × 1596 apart; position Ø0.5 at MMC to datums A (the panel's rear face), B (its left edge), C (its bottom edge), features.csv. The studs are fixed in the back wall, so H − F = 1.0 is shared between the hole positions and the stud positions; our design choice is an even split, Ø0.5 each (it also passes GDT-010's floating-fastener check, Ø0.5 ≤ 1.0) |
| gland plate | 1050 × 200 × 2 galvanised, removable, 8 × M5, in the floor of the body, clear of the leg channels |
| lifting eyes | two, M12, at 1/4 and 3/4 of the width, bar centre 42 above the body top, top at 48 |
| earth studs | three, M8, brass, Ø8 plain: one on the body (inside the back wall, lower left: x 60, z 365, 20 proud) and one on each door (inside, hinge side, low: 50 from the hinge axis, z 378, 18 proud). Since 1.9 each is a port node of gender none (`pe-body`, `pe-door-l`, `pe-door-r`; the door ones swing with their doors), where a panel's protective conductor lands (behaviour.csv pins PE1 to PE3); the nut's tightening torque is NOT ON FILE (B): IEC 60947-1 (no torque in the maker's files on hand; a brass stud has no property class to derive one from). No bonding point on the back panel or the gland plate: none is on file |

## Carries (bom.csv)
Door operators on `door-r` at 1500 above the floor, 60 pitch, handle side, left to right: `estop-door` = op-estop-22-2nc · `btn-reset` = op-pb-22-1no (M-BLUE) · `lamp-power` = op-pilot-22 (M-LENS-WHITE); their versions are the ones bom.csv pins (one home for a figure). Each row is a Ø22.5 cut-out through the door skin; the operator's latch and contact blocks sit behind it. Changing the fit-out is editing bom.csv.

## Deliberate differences from the reference
Body depth 305 with 25 mm proud doors (reference: 329 body, near-flush doors): ours keeps the nominal 12 in body and shows the door return, the more common construction for this class. Door widths 757.5 (reference 761/784): within the 3 mm gap convention. Everything else is within 5 mm of the reference or follows it.
<!-- acad-gate enc-fs-1524x1829x305 -->
- AutoCAD gate 2026-11-05 (enc-fs-1524x1829x305): STEP extents [1526.0, 432.0, 2182.0] mm; vs glb [0.0, 0.0, 0.0] mm; every brief figure found in the build within 2 mm (overall or on a solid). Fillet r 1.0 on edges > 3 mm: 0 of 51 rejected (0.0 %, 0 on the envelope).

## Named nodes
`door-l`, `door-r` (hinge axes on the outer edges, open outward to 110°), `handle-1` (latch handle with key cylinder), `gland-plate`, `back-panel`, `hinge-l`, `hinge-r` (fixed: the hinge pins the doors turn on); `pe-body`, `pe-door-l`, `pe-door-r` (1.9: the earth studs as port nodes, gender none, the port face at each stud's tip; `pe-door-l` and `pe-door-r` are children of their doors and move with them; a panel's wires.csv names them `enc-1.pe-body`, `enc-1.pe-door-l`, `enc-1.pe-door-r`); from the BOM: `estop-door` (press 6 mm and latch, twist to release), `btn-reset` (press 4 mm), `lamp-power` (emissive when control power is on). Placed in an assembly under tag `enc-1`, these read `enc-1.door-r`, `enc-1.estop-door`, …

## Wiring of the door operators (fixture 1)
`estop-door` in series with the station's `estop-1` into the safety relay's circuit (element relay-safety-2ch-2no1nc); `btn-reset` in parallel with the station's reset on X2 B; `lamp-power` across the 24 V control supply, not a PLC output (power-on lights are wired that way in the field, so they show the panel is live even when the controller is not).

## Layer names on disk
Spec form `node:<name>|M-<material>`; AutoCAD cannot take a colon or a bar in a layer name, so the files carry `node-<name>_M-<material>` (e.g. `node-door-r_M-STEEL-7035`). The glTF writer reads the same prefix and emits node `door-r` with material `M-STEEL-7035`.

## Materials by layer
`M-STEEL-7035` body, doors, legs, feet (RAL 7035 powder coat) · `M-GALV` back panel, gland plate · `M-GASKET` door gasket (EPDM, black) · `M-ZINC` hinges, handle body, latch tongues, studs, screws · `M-BLACK-PA` handle grip, lock cylinder · `M-BRASS` earth studs · operator materials per their own specs.

## Decals (Blender)
Rating label inside the right door (NEMA 12 / IP55, 60 × 72 × 12), warning label "Disconnect power before opening" on the door front near the handle, the institute's panel tag plate top-left of the right door, earth symbols at the studs.

## Not modelled (by design)
Interior wiring and devices (their own elements, placed on `back-panel` by an assembly BOM), gasket compression, hinge pin internals, key.

## Outputs (out/)
`enc-fs-1524x1829x305.lsp` (AutoCAD solids, mm; anchor holes and operator cut-outs are real SUBTRACTs) · `.glb` (glTF 2.0, metres, Y-up, one node per named part plus `body`, one material per `M-` layer, indexed, no normals, base colours and emissive lenses) · `-drawing.svg` (front, side, top, dimensioned) · `preview-*.png`. The terminal's DWG / STEP (with the 1 mm FILLETEDGE pass) and the Blender bevel pass go in `dwg/`, `step/`, `blend/`, `gltf/`.
Still to do: lifting eyes as true rings, the continuous hinge as knuckles, legend decals.

## History
| version | was | change |
|---|---|---|
| 1.9 | rev J | the three M8 earth studs are port nodes `pe-body`, `pe-door-l`, `pe-door-r` (gender none; the door ones children of their doors), with a `pin` row each (PE1 to PE3) in behaviour.csv so a panel's protective conductors can land on them (lib/requests/core/mech-earth-studs-2026-11-11.md, from request panel-3 item 3); the stud count settled at three in spec.md and behaviour.csv; the studs themselves unchanged in place and size, so a minor (nodes added, none moved; origin and cut-outs kept; pnl-motor-starter pins 1.8 and moves when the shop chooses). Not gated in AutoCAD this round: the gate's glb extents reader places a nested node relative to its parent's origin (request mech-12; the fix, cadout.glb_extents, lands with core round 30), so `pe-door-r` would read at x −50 and fail for no defect (mech-r96, unattended) |
| 1.8 | rev I | text only, the part unchanged (a minor: nodes, origin, cut-outs kept): the safety relay named by its element id, not the maker's part-number family, here and in bom.csv (OPERATING.md 6); the Carries section points to bom.csv for the operators' versions (it said 1.0 where bom.csv pins 1.1); the back panel's four Ø11 stud holes declared in features.csv, position Ø0.5 at MMC, half of H − F (GDT-010; ISO 273 medium); review mech-r15 findings 1 to 3 (mech-r21, unattended) |
| 1.7 | rev H | text only, the part unchanged (a minor: nodes, origin, cut-outs kept; pm-motor-starter's 1.6 pin builds it): vendor and part names out of BASELINE, spec and features.csv (DOC-006, OPERATING.md 6: they live only in references/); the Dimensions row's anchor hole corrected to Ø11.1, as built since 1.6 (mech-r15, unattended) |
| 1.6 | rev G | anchor holes 14 → 11.1 (7/16 in, the maker's STEP's floor holes, terminal 2026-11-03) |
| 1.5 | rev F | validation suite findings (GEO-010): gland plate 1200 → 1050 so its flange clears the leg channel walls; the active door's meeting return stops 2.5 short so it closes in front of the astragal, astragal shortened to clear the top / bottom returns; latch keepers, door stay, earth stud and lock cylinder moved into the door nodes (they swing with the door in the twin); hinge pins are nodes `hinge-l` / `hinge-r`; the sub-panel has holes for its four studs; **door swing direction corrected (MOT-010): both doors opened into the cabinet since 1.0** (the build's swing and the pivot range were inverted; the open preview hid it behind the side walls); key cylinder moved into `handle-1` (it turns with the lever) |
| 1.4 | rev E | (rebuilt on toolkit 1.1, no change) lifting-eye bar centre 42 above the top (top at 48); writer binds every SUBTRACT target; glTF colours and emissive lenses; **restructured as an element: door operators moved to bom.csv, built on toolkit 1.0** (same geometry, nodes and origin) |
| 1.3 | rev D | door-mounted operators on the right door at 1500: E-stop, reset, power-on light, 60 pitch |
| 1.2 | rev C | handle escutcheon 25 wide; lifting-eye ring geometry |
| 1.1 | rev B | terminal's measurements of the reference taken in: two full-depth channel legs, handle 50 from the meeting edge at 1180, 13 mm door margins, no drip shield, eyes 48 above the top; kit fixes (left-handed oriented boxes, real anchor holes, indexed glTF) |
| 1.0 | rev A | first build |
