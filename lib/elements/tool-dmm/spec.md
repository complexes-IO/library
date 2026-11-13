# tool-dmm · v1.0 · digital multimeter

**What** Hand-held digital multimeter for the toolbox station: display, rotary dial, four test-lead jacks, and two probes parked in clips on the sides. No measurement category, voltage rating or approval mark is printed on it or claimed for it.
**Class** device · **Baseline** our own design (complexes.org; EM rule 2026-11-05: a part with no product to match is our own design). Its sizes are design choices. What it meets is the 4 mm test plug of its leads: the jack bore and pitch are its one fit figure (Dimensions, jacks).
**Units / frame** mm, Z up. Origin: lying on a bench: the centre of the back face, y = 0; the front faces −y; z up the long side.
**Built with** toolkit 1.3 · AutoLISP command `DMM1` · no parameters.

## Dimensions
| item | value | source |
|---|---|---|
| body | 90 × 40 × 180 (x × y × z), grey | design choice: a one-hand meter |
| display | 70 × 40, 1.0 proud, centre z 55 | design choice |
| dial plate | 70 × 66 × 0.6, black (the positions are printed on it) | design choice |
| dial | Ø44 × 8 with a 4 × 16 pointer ridge, rotates 0–270° (ten positions every 30°; what each selects: the dial positions table below) | design choice (the size and the travel) |
| jacks | four Ø8.0 bores, 12 deep, at z −60, x −30 / −10 / 10 / 30 (COM, V / Ω, mA, A) | **Assumption (B)**: a fit to the leads' 4 mm shrouded test plug, bore Ø8.0 and pitch 20, the usual size for that plug. Reason: no test-lead standard or element is in the library to take the plug's figures from. Source wanted: IEC 61010-031 (hand-held probe assemblies), not held. A figure from it replaces this one as a minor version |

Dial positions: what the dial selects at each angle, and which jacks that position uses. **Assumption (A)**: behaviour the twin reports (the function decides what the display shows), and our own design's choice, with no product or standard on file that fixes a meter's dial order. EM's. The angle is the `dial` pivot's (rotation about −y, the pointer ridge up at 0°).

| angle | function | jacks in use |
|---|---|---|
| 0° | OFF | none (the display dark) |
| 30° | V~ (AC voltage) | COM, V / Ω |
| 60° | V⎓ (DC voltage) | COM, V / Ω |
| 90° | mV | COM, V / Ω |
| 120° | Ω (resistance) | COM, V / Ω |
| 150° | continuity | COM, V / Ω |
| 180° | diode | COM, V / Ω |
| 210° | µA | COM, mA |
| 240° | mA | COM, mA |
| 270° | A | COM, A |
| probes | tip Ø1.2 × 20 (left sharp: thinner than 2.5 × the 0.5 fillet radius), guard Ø12 × 2, grip Ø9 × 108, boot Ø6 × 15; parked tip up at x ±51, y −20, top z 90; pull out 150 along +z | design choice |
| clips | two per probe, 1.5 × 8 × 8, between the side face and the grip, at z −20 and 40 | design choice |
| label | 60 × 12 × 0.6 white, centre z −78 | design choice |

## Named nodes
`display` (emissive) · `dial` (rotate about −y, 0–270°) · `probe-red`, `probe-black` (translate +z, 0–150: out of the clips).

## Materials by layer
`M-GREY-PA` body, dial · `M-LENS-DARK` display · `M-BLACK-PA` dial plate, clips, black probe · `M-RED-PA` red probe · `M-ZINC` probe tips · `M-WHITE-PA` pointer ridge, label · `M-GASKET` jack bores.

## Decals (Blender)
Dial positions (OFF, V~, V⎓, mV, Ω, continuity, diode, µA, mA, A, at the angles of the dial positions table) on the dial plate; jack names (COM, V Ω, mA, A) beside the jacks; `complexes.org` on the label. No category or rating marks, no vendor name.

## Notes and assumptions
- The jack bore and pitch are the one fit figure (Dimensions, jacks, class B). The leads and their plugs come with a later element; the plug's figure, once on file, replaces them as a minor version.
- The dial positions table is the one behaviour figure (class A). Until EM accepts it, the twin should read it as the design's proposal.
- The leads are not modelled: the probes' boots end free. A later version adds the leads and plugs them into the COM and V / Ω jacks.

## Outputs (out/)
`tool-dmm.lsp` · `.glb` (pivots on the moving nodes, `env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (elec-r4, 2026-11-05); before its first commit the probe tips went from Ø2 to Ø1.2, after the AutoCAD gate rejected each tip's end edge on the envelope (2 of 35) |
