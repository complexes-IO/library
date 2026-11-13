# teach-pendant · v1.0 · robot teach pendant (simulation only)

**What** Hand-held teach pendant for the robot cell: a 7 in class screen, an E-stop mushroom, 16 keys and an enabling bar, cabled at the bottom. Printed on the part: **SIMULATION ONLY. NOT A SAFETY DEVICE**. It carries no ratings and makes no safety claim: the E-stop and the enabling bar are simulation inputs to the twin, never a safety function.
**Class** device · **Baseline** our own design (complexes.org; EM rule 2026-11-05: a part with no product to match is our own design). Its sizes are design choices; what it meets takes its figures from the library: the E-stop mushroom and collar from `toolkit/std22.py` (`ESTOP`), the cable entry from `lib/standards/holes.csv` (M20 × 1.5 entry, 20.2–20.7).
**Units / frame** mm, Z up. Origin: hand-held: the centre of the back face, y = 0; the screen faces −y; z up the long side.
**Built with** toolkit 1.3 · AutoLISP command `TPND` · no parameters.

## Dimensions
| item | value | source |
|---|---|---|
| body | 240 × 55 × 300 (x × y × z), grey | design choice: two-hand grip, the screen above 16 keys |
| screen | 155 × 87 × 1.0 proud, centre (−27.5, 78.5) | design choice: 7 in diagonal at 16:9 (177.8 → 155.0 × 87.2) |
| E-stop | Ø40 mushroom, Ø32 crown, Ø32 × 6 yellow collar, centre (85, 95), press 6 and latch | toolkit/std22.py `ESTOP` |
| keys | 16, 36 × 18, 3.0 thick (0.5 in a 1.5 deep pocket with 0.2 side clearance), travel 1.0; columns x −75 / −25 / 25 / 75, rows z 5 / −21 / −47 / −73 | design choice |
| enabling bar | 3.5 × 24.6 × 79.6 on the left side in a 3.0 deep pocket, travel 1.5 (released 0, enabled about 0.75, pressed through 1.5) | design choice |
| label | 200 × 18 × 0.8 white, centre z −133 | design choice |
| cable entry | Ø20.5 in the bottom face, 16 deep, at y −27.5 | lib/standards/holes.csv M20 × 1.5 entry |

## Named nodes
`screen` (emissive) · `estop` (translate +y, 0–6) · `key-1` … `key-16` (translate +y, 0–1.0; numbered left to right, top row first) · `enable` (translate +x, 0–1.5).

## Materials by layer
`M-GREY-PA` body · `M-LENS-DARK` screen · `M-YELLOW` collar · `M-RED` mushroom · `M-BLACK-PA` keys, enabling bar · `M-WHITE-PA` label · `M-GASKET` pockets, recess, cable entry.

## Decals (Blender)
On the white label: **SIMULATION ONLY. NOT A SAFETY DEVICE** (the standing rule, OPERATING.md 6) and `complexes.org`. Key legends (J1− … J6+, F1 … F4) on the keys. No vendor name, no approval or rating marks.

## Notes
- The gland and the pendant cable to robot-controller are not built yet: the M20 entry is modelled, and the cable is placed in a later version (EM rule 2026-11-05).
- The red-on-yellow E-stop is the look of the class, so the twin's operator sees what they expect; the label says what it is.

## Outputs (out/)
`teach-pendant.lsp` · `.glb` (pivots on the moving nodes, `env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (elec-r4, 2026-11-05) |
