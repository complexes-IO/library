# thermostat-enc · v1.1 · enclosure thermostat

**What** Enclosure thermostat on the 35 mm rail: a housing with a setpoint dial on its front and two screw terminals at its bottom. It switches an enclosure heater or fan in a panel. No switching rating, contact type, temperature range or approval mark is printed on it or claimed for it.
**Class** device · **Baseline** our own design (complexes.org; EM rule 2026-11-05: a part with no product to match is our own design). Its housing and dial sizes are design choices. What it meets is the 35 mm rail and the wires: the rail clip and the screw terminals are the toolkit's rail-device parts (toolkit/din.py `rail_clip`, `terminal_row`), on file.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward −y (toolkit/din.py).
**Built with** toolkit 1.3 · AutoLISP command `TSTE` · no parameters.

## Dimensions
| item | value | source |
|---|---|---|
| housing | 35 × 40 × 60 (x wide, y off the rail crown, z tall), grey | design choice: two narrow rail modules |
| rail clip | upper and lower lips (w − 2) × 7.5 × 2.0 behind the crown at z 17.5 and −19.5, release tab 6 × 3 × 8 at z −27 | toolkit/din.py `rail_clip` |
| setpoint scale | 26 × 26 × 0.6 white, centred on the dial (z 6) | design choice |
| dial | Ø20 × 6, centre x 17.5, z 6; pointer ridge 2 × 1.5 × 7 from the centre; rotates 0–270° | design choice |
| terminals | two screw terminals at the bottom, pitch 12 (x 11.5 and 23.5): screw heads Ø4.4 × 1.2 on the front face at z −24, wire entries 3.6 × 9.0 cut 0.5 deep into the bottom face (inside the 60 housing) | pitch: design choice; head and entry: toolkit/din.py `terminal_row` with `target` (request elec-2) |
| label | 25 × 8 × 0.2 white, centre z 23 | design choice |
| terminal legend | 25 × 4 × 0.2 white, centre z −18 (z −20 to −16, above the screw heads at z −26.2 to −21.8) | design choice (1.1: the numbers had no printed face) |

## Named nodes
`dial` (rotate about −y, 0–270°: the setpoint; what each angle stands for is in the behaviour table under Notes).

## Materials by layer
`M-GREY-PA` housing, rail clip · `M-BLACK-PA` dial · `M-WHITE-PA` setpoint scale, pointer ridge, label, terminal legend · `M-ZINC` terminal screws · `M-GASKET` wire entries.

## Decals (Blender)
Setpoint marks on the scale (ticks only, no temperatures); terminal numbers 1 and 2 on the legend field, each above its screw (x 11.5 and 23.5); `complexes.org` on the label. No rating, no approval mark, no vendor name.

## Notes and assumptions
- The geometry has no open figure: the rail clip and terminals are the toolkit's figures (toolkit/din.py), and the housing, scale, dial and label sizes are design choices.
- The thermostat's behaviour is open (review thermostat-enc-1.0 finding 2). These three figures decide what the twin reports when an assembly wires the part, so they are class A, EM's (OPERATING.md 6). As our own design the part claims no rating (OPERATING.md 12), and no standard or element on file gives them, so none is set:

  | behaviour | status | reason |
  |---|---|---|
  | contact form: the contact opens or closes on rising temperature (a heater's or a fan's thermostat) | NOT ON FILE (A) | no product or standard on file; an assembly that wires it gives the two terminals their roles in its pins.csv |
  | setpoint scale: the temperature each `dial` angle (0–270°) stands for | NOT ON FILE (A) | the printed scale is ticks only, with no temperatures (Decals) |
  | switching differential: the band between switching on and switching off | NOT ON FILE (A) | no product or standard on file |

  Until EM rules on them, 1.0 is geometry only: a twin reads no temperature, switching point or contact state from it. EM accepted the three lines as they read (lib/approvals.csv, 2026-11-06); 1.1 changes no behaviour, so it is geometry only too.
- inventory.csv lists `din-clip-35` as a part of it. That common part is not built yet: the clip is the toolkit's `rail_clip` until it is, and a later version places it (a major: new nodes).

## Outputs (out/)
`thermostat-enc.lsp` · `.glb` (pivot on `dial`, `env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.1 | 2026-11-06 (elec-r11, unattended): the wire entries are cut 0.5 into the housing's bottom face instead of standing 0.5 proud (request elec-2, toolkit/din.py `terminal_row(target=)`): the envelope is 60.0 tall, as the housing; a white terminal legend field above the screws gives the numbers 1 and 2 a printed face (review elec-r10, class C decal position); Blender re-gated with request elec-3's decal tie fix. No node, origin or mounting moves; the behaviour table is unchanged |
| 1.0 | first build, our own design (elec-r6, unattended, 2026-11-05) |
