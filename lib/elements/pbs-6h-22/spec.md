# pbs-6h-22 · v1.7 · six-hole 22.5 mm pushbutton station

**What** Six-hole 22.5 mm pushbutton station, horizontal, IP66, die-cast body and lid, RAL 7035; the operator station of the motor-starter cell and the standard station for every panel in the set.
**Class** station · **Baseline** the six-hole die-cast station class (AutomationDirect / Rockwell 800F-6H, measured, not shipped); operators per the 22.5 mm standard (IEC 60947-5-1 cut-out Ø22.5, bezel Ø29.7, E-stop mushroom Ø40 per ISO 13850).
**Units / frame** mm, Z up. Origin: back face, lower-left mounting hole; the body extends toward −y (toward the student).
**Built with** toolkit 1.3 · AutoLISP command `PBS` · no parameters.

## Dimensions
| item | value |
|---|---|
| back box | 340 × 90 × 50, 3 mm wall, gasket on the rim |
| lid | 22 deep, 3 mm, overlaps the rim 1.5 all round, four captive M4 screws at the corners; total depth 72 |
| cut-outs | six Ø22.5 at 50 pitch, first at 45 from the left edge, on the lid's centre line (z = 35 from the origin) |
| mounting | four Ø5.5 through the back, 320 × 70 centres (10 in from each edge); position Ø0.5 at MMC to A, the back face (features.csv) |
| gland | M20 on the bottom face, 40 from the left end |

## Carries (bom.csv)
Left to right on `lid-1`: `btn-start` = op-pb-22-1no 1.0 (M-GREEN) · `btn-stop` = op-pb-22-1no 1.0 (M-RED) · `btn-reset` = op-pb-22-1no 1.0 (M-BLUE) · `estop-1` = op-estop-22-2nc 1.0 · `lamp-run` = op-pilot-22 1.0 (M-LENS-GREEN) · `lamp-fault` = op-pilot-22 1.0 (M-LENS-RED). The station is the box, the lid and six cut-outs; what sits in them is the BOM.

## Field connection (v1.1)
The station is a field device: its operators are wired inside to five A-coded M12 bulkhead sockets (`port-m12-a`, rear mount, BOM rows) through its end walls, and cables land on those, never on the operators. Right end: `s-x1` (start pin 4 + stop N.C. pin 2 → I/O X1), `s-x2` (reset → X2 B), `s-x3` (run light ← X6 B, an output). Left end: `s-x5` (fault light ← X5 A), `s-es` (E-stop dual channel → panel p-x3, 440R S12 / S22). Internal wiring from the contact blocks to the sockets is a decal-level detail for now. The pinout checker found the gap: the cell's connection list had cables landing on buttons and lamps.

**Port gender (settled 2026-11-04 by the standards):** the five ports are male (pins in a threaded sleeve). IEC 60204-1 13.4.5 a): the part of a plug/socket combination that stays live after it is pulled apart must be finger-safe (IP2X / IPXXB), so the side that supplies the voltage carries the sockets. Every circuit on these ports is supplied from the other end: the I/O block feeds 24 V to the buttons and drives the lamps, and the panel's safety relay feeds the E-stop channels. The station is the load, so it carries the pins, as a sensor does (an M12 sensor carries a male connector, IEC 60947-5-2 Annex D class) and as the I/O block's own power inlet X03 does (LioN-X manual p. 32-34). The cordsets are female at the station, male at the I/O block and the panel.

## Named nodes
`lid-1` (the front plate with everything mounted on it; removable) and the six operator tags above (caps press 4 mm along +y; the E-stop head presses 6 mm and latches, twist 45° to release; lenses are emissive when the output is on).

## Channel map (fixture 1)
btn-start X1 A · btn-stop X1 B (NC) · btn-reset X2 B · estop-1 feeds the 440R (its monitored output is X2 A) · lamp-run X3 B · lamp-fault X5 A.

## Materials by layer
`M-ALU-7035` body, lid · `M-ZINC` lid screws, gland nut · `M-BLACK-PA` gland insert · `M-GASKET` rim gasket · operator materials per their own specs.

## Decals (Blender)
Legend text START / STOP / RESET / RUN / FAULT in white on the black plates; EMERGENCY STOP around the mushroom on the yellow plate; IP66 and the institute's tag plate on the lid, lower right.

## Outputs (out/)
`pbs-6h-22.lsp` (AutoCAD solids, mm; cut-outs, bezels and mounting holes are real SUBTRACTs) · `.glb` (8 nodes, 10 materials, metres, indexed, no normals) · `-drawing.svg` · `preview-*.png`. Terminal builds in `dwg/`, `step/`, `blend/`, `gltf/`.
Still to do: 0.5 mm radii on the die-cast edges (Bevel), the mushroom's true dome, legend decals.

## History
| version | was | change |
|---|---|---|
| 1.7 | GDT-010 (r0) | the mounting pattern gets a position tolerance: Ø0.5 at MMC to the back face, which is the floating-fastener limit T = H − F = 5.5 − 5.0 (ASME Y14.5 floating fastener; Ø5.5 is ISO 273's medium series, H13, for M5). Without it the pattern fell to ISO 2768-m ±0.5 over 328 mm, a Ø1.41 zone. Kept Ø5.5 rather than the coarse Ø5.8: its T = 0.80 would still not cover the general tolerance, and the holes stay as they are. Geometry, nodes and origin unchanged |
| 1.6 | round 4 gate | the die-cast box and the lid are one solid each (a box hollowed by one cut): as separate wall and skirt boxes their edges lay a few mm apart on one outline and AutoCAD picked the neighbour's ('Cannot fillet multiple bodies', 26 rejects); ports port-m12-a 1.4 |
| 1.5 | — | its ports are port-m12-a 1.3 (male receptacles 1.2: the pins inside a fixed threaded sleeve with its O-ring) |
| 1.4 | — | its ports are port-m12-a 1.2 (male receptacles 1.1: the sleeve covers the shroud, pins recessed) |
| 1.3 | — | the five M12 ports are male receptacles (port-m12-a 1.1, gender=male: pins in a shroud, as a device carries; the I/O block and the panel, the supply side, keep the sockets); each is built from receptacle-m12 with its contacts |
| 1.2 | validation suite findings (GEO-010, GEO-020): the lid skirt ran 4 mm into the walls and the rim gasket was a solid plate the contact blocks passed through; the skirt now ends on a 2 mm gasket ring; operators op-pb-22-1no 1.1 and op-estop-22-2nc 1.1 (latch bore, E-stop skirt recess); run light socket now fed from I/O X6 B (X3 is an input port: ERC-005) |
| 1.1 | — | five A-coded M12 ports through the end walls (BOM rows), so cables land on ports; the operators are unchanged |
| 1.0 | rev A | first build; restructured as an element with its operators in bom.csv (same geometry, nodes and origin) |
