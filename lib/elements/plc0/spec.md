# plc0 · v1.2 · plc0 controller box

**What** plc0 controller box. Built from the Stage 0 brief `references/measure.md`.
**Class** device · **Baseline** own design (2026-11-03): 90 × 105 × 60, 35 mm rail, RUN / FAULT, M12 D Ethernet and M12 L power on the bottom at 27 pitch; port pinouts as io-block-m12-8di8do X01 / X03. Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0.
**Built with** toolkit 1.3 · AutoLISP command `PLC0` · no parameters.

## Named nodes
`led-run` (green), `led-fault` (red): emissive · `port-eth` (D), `port-pwr` (L): kind port, gender female (sockets, as built; PIN-002). Review plc0-1.1 finding 3 asks for `port-pwr` male L, as io-block-m12-8di8do X03 (IEC 60204-1 13.4.5): a node and geometry change, so a 2.0, still open

## Decals (Blender)
plc0, tag, RUN / FAULT, ETH / 24 V; no vendor marks

## Notes and assumptions
Figures marked **Assumption** were NOT ON FILE in the brief; a document figure replaces them as a minor version. Exterior only: the interior (mechanism-first ruling) arrives per interior-first-prompt.txt.

## History
| version | change |
|---|---|
| 1.2 | elec-r21 (2026-11-09, unattended): PIN-002 (EM 2026-11-05): `port-eth` and `port-pwr` declare gender female, the sockets as built; DOC-006 (OPERATING.md 6): the reference controller's maker left BASELINE ("a reference controller on file", references/measure.md). No shape change: nodes, origin and cut-outs as 1.1 |
| 1.1 | render fix (GEO-050): the M12 coding inserts were flush with the socket rims; now 0.2 proud |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |

## Deliberate differences
<!-- acad-gate plc0 -->
- AutoCAD gate 2026-11-05 (plc0): STEP extents [90.0, 67.8, 117.8] mm; vs glb [0.0, 0.0, 0.0] mm; brief figures not found within 2 mm: 'our box W x H x D (proposal)' [90.0, 105.0, 60.0] (nearest overall extent [90.0, 105.0, 67.8]); 'rail clip' [22.5, 50022.0, 35.0, 7.5] (nearest overall extent [20.5, 117.8, 67.8, 7.5]); 'reference controller H x W x D' [143.97, 98.1, 136.81] (nearest overall extent [117.8, 99.0, 117.8]); 'reference I/O module per slot' [144.6, 22.0, 105.4] (nearest overall extent [117.8, 20.5, 105.0]); 'clearance around the box' [50.8, 25.0] (nearest overall extent [67.8, 67.8]). Fillet r 0.5 on edges > 3 mm: 0 of 18 rejected (0.0 %, 0 on the envelope).
