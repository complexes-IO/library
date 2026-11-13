# io-block-m12-8di8do · v1.10 · 8DI/8DO IP67 I/O block, M12

**What** 8DI/8DO IP67 I/O block, M12. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** device · **Baseline** maker's datasheet (the brief names the product): techdata p. 1-4 (60 × 31 × 200, 2-hole M4 mount 190.5 apart, port pitch 27); manual p. 12 / 20 / 26 / 32 / 33 / 35 / 39 / 159 pinouts, FE, switches, LEDs; the STEP read with Open CASCADE (rounds 4 and 5). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: frame device: back face on the mounting surface y = 0, first mounting hole x = 0, z = 0; body toward −y, length along +z.
**Built with** toolkit 1.3 · AutoLISP command `IOBLOCK8` (1.9; the command before it named the maker's product family) · `conditions` (per port and pole for fault scenarios: 'x1:2:spread/x5:4:corroded').

## Dimensions (the STEP read with Open CASCADE, round 5: figures.md 4.1)
| item | value |
|---|---|
| body | x ±29.79 (59.59), z −4.50 to 195.30, the housing face 17.6 off the back (y −17.6); the inserts stand 3.4 proud (−21.0), X03's sleeve to −30.7 |
| power end | the housing face runs to the end; three pockets: the first slot's seat and the FE's seat 10.0 off the back, open at the end, sides leaning 10°, closed by R5.0 / R4.5 arcs about z 0.504; the label plate's pocket 13.4 off the back (x −25.70 to the seat, to z 4.80), the plate on its floor |
| far end | a seat 10.0 off the back: an R4.5 arc about (0, 190.303), its sides leaning 10° out to the end |
| not modelled | the face's R5 roll-over into the end faces (the gate's rounds stand for it); the back face's 1.0 recess and its bosses (against the mounting surface) |
| mounting | slots 4.5 × 6.0: across x at the first hole (x 0, z 0), along z at the far one (centre z 191.05); the mounting pattern 190.5 (drawing), the screws there; M4 pan heads on the seats (Ø7 × 2.8: Assumption (C), appearance: the screws are the installer's) |
| mounting position tolerance | Ø0.5 on the pattern's Ø4.5 holes (features.csv position_tol): Assumption (B): the maker's position tolerance is NOT ON FILE (B); Ø0.5 = H − F (4.5 − 4.0) lets a floating M4 pass (ASME Y14.5 floating fastener, the GDT-010 rule; ISO 273 medium Ø4.5); the slots' 6.0 length adds 1.5 along each slot |
| I/O ports | rows at x ±15: X1 / X5 z 174, X2 / X6 147, X3 / X7 120, X4 / X8 93 (X1 to X4 left, inputs; X5 to X8 right, outputs) |
| Ethernet | X01 (x −15), X02 (x +15) D-coded at z 39 |
| power | X03 in (x −15, male), X04 out (x +15) L-coded at z 12 |
| clocking | looking at the housing face, clockwise from the far end: X1–X4 keyway 0°, X5–X8 −90°, X01 0°, X02 −89.6°, X03 key block +45°, X04 recess −45.0° (a placement roll) |
| channel LEDs | Ø3.6, 0.1 proud, x −5 (X1–X4) / +5 (X5–X8): A (pin 4) at port z + 3 yellow, B (pin 2) at z − 3 white |
| status LEDs | 7 at z 77.8, x −17.4 to 17.4 at 5.8: P1 / P2 Lnk/Act (X01 / X02), MS / DIA, NS / BF, the 5th (name and colour NOT ON FILE (C): appearance, a clear lens the twin does not light), U_L, U_S (the actuator and the module supply) |
| switches | x100 / x10 / x1 at x −20.7 / −6.9 / 6.9, z 66.2: knob Ø6.1 in a Ø6.3 bore, a Ø7.2 pocket 1.3 to 4.0 deep, a pointer slot; no cover |
| cap | Ø12.3 flush at x 20.7, z 66.2: what it covers is NOT ON FILE (C) (the twin doesn't read it; the cap is modelled fixed) |
| FE | M4 threaded hole (plain Ø4.0) through the power-end lug at x 20.0, z 0.5, Ø4.5 above it, a Ø6.4 × 1.0 counterbore at the back (manual p. 26) |
| label plates | 13 clip-in plates 19.24 × 7.29 tops flush, 1.0 deep (techdata: 15x; where the other 2 go is NOT ON FILE (C): appearance) |

## Named nodes
`port-x1..x8` (A), `port-x01/x02` (D), `port-x03/x04` (L): kind port, unit = coding, each a receptacle-m12 flush in the housing face, clocked as on the part, its insert 3.4 proud (X03's sleeve 13.1) (mating data in the extras; X03 Power In male, the rest female: manual p. 32-34, the STEP agrees) · `port-<x>.insert.c<pole>` (contacts) · `port-<x>.seal` · `led-x1a..x8b` (channel LEDs: a yellow, b white) · `led-p1`, `led-p2` (green), `led-dia`, `led-bf` (red), `led-s5` (name and colour NOT ON FILE (C): a clear lens, dark), `led-ul`, `led-us` (green) · `sw-x100/x10/x1` (rotate) · `cap`

## Materials by layer
`M-ZINC-CAST` body · coding colour inserts (A black, D green, L grey) · `M-GOLD` contacts · `M-LENS-*` LEDs · `M-GREY-PA` switch knobs · `M-BLACK-PC` cap · `M-WHITE-PA` label plates · `M-ZINC` screws

## Decals (Blender)
X1–X8, X01/X02, X03/X04 on the label plates; FE at the threaded hole; no maker's marks

## Notes and assumptions
LED colours from manual p. 159 / 160 (Table 47), the status row's labels read by eye off the techdata drawing. The back face's 1.0 deep recess is not modelled. Pinouts in the brief are the connection list's source. Every figure marked **Assumption** here was on no page read and is set from the usual norm; a document figure replaces it as a minor version.

## Behaviour (behaviour.csv, elec-r25)
Pins are the receptacles' contacts, marked `<port>-<pole>` (X03-4 = U_L +24 V, manual p. 33). X03 power in carries on to X04 (one pinout);
U_S feeds pins 1 and 3 of the input ports X1 to X4 (manual p. 20: DI type 3 with U_S); pin 5 of every port is the one FE. Each output channel
is a source between its pin (4 = Ch. A, 2 = Ch. B) and pin 3, switched by a manual state the twin sets (the bus and the program are
phase 5), rated 2 A (manual p. 20). Open figures the twin reports:
- the module's supply thresholds: U_S and U_L count as present from 18 V: Assumption (A): the low end of the 18-30 V supply range in metadata.json (the catalogue entry read 2026-11-02, no brief page); the undervoltage threshold is not on any page read
- the input ON level: 11 V: Assumption (B): IEC 61131-2 type 3 (manual p. 20 names type 3); the level is the standard's table, and IEC 61131-2 is not in lib/standards/sources.csv (a document wanted, as behaviour.csv writes it)
- the output voltage drop (behaviour.csv's sources give U_L's nominal 24 V) and which faults raise the DIA state: NOT ON FILE (A), the maker's figures on pages not read (a reading attended)
- which supply and ground feed pins 1 and 3 of the output ports X5 to X8: NOT ON FILE (A) (no contact rows there)
- the sensor supply's short-circuit protection (U_S to pin 1 of the input ports X1 to X4, behaviour.csv's `us-bus` contact rows): NOT ON FILE (A), a maker's rating on a page not read; none is modelled, so the twin shows no sensor-supply fault (a reading attended, as the two above)

## Outputs (out/)
`io-block-m12-8di8do.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.10 | elec-r33 (unattended, 2026-11-12): text only, geometry as 1.9. The sensor supply's short-circuit protection in the Behaviour list as NOT ON FILE (A), as behaviour.csv's `us-bus` row note has carried it since 1.9, so DOC-005 counts it on EM's page (review io-block-m12-8di8do-1.9 finding 1) |
| 1.9 | elec-r32 (unattended, 2026-11-11): text only, geometry as 1.8. AutoLISP command `IOBLOCK8` (the command before it named the maker's product family, which DOC-006's case-sensitive pattern let through: review io-block-m12-8di8do-1.8 finding 1, an ESCAPE); the input ON level class B here as in behaviour.csv (finding 2); every bare open-figure marker classed in this spec, the brief and behaviour.csv (finding 3: the 5th LED, the cap, the label plates and the ports' thread length class C; the output drop and the DIA faults class A) |
| 1.8 | elec-r25 (unattended, 2026-11-09): text only, geometry as 1.7. The maker's and product names out of BASELINE and this spec (DOC-006; they stay in references/); the status LEDs U_L / U_S written as the supplies they show; the mounting pattern's position tolerance Ø0.5 in features.csv (GDT-010; a class B line for EM); the pan heads, the cap and the two missing label plates classed C; behaviour.csv written from the brief's pinouts (two class A thresholds and the output ports' supply pins for EM) |
| 1.7 | round 7 back (2026-11-04): receptacle-m12 1.6 (X03's key tolerance against the cordset female's new recess, 1.759°) |
| 1.6 | round 6 back (2026-11-04): no lug face: the end pockets as measured (seats at 10.0, the label pocket at 13.4, the far seat); X04 clocked −45.0°; receptacle-m12 1.5 |
| 1.5 | round 5 back (2026-11-04): the face as measured: housing face 17.6 off the back (1.4: 30.7, every port 13.1 too far out); ports at x ±15, power at the FE end, Ethernet next, X1 to X4 from the far end; each port clocked as on the part; 16 channel LEDs (A yellow, B white) and 7 status LEDs; switches with no cover and the cap; FE an M4 hole in the power-end lug; mounting slots; 13 label plates |
| 1.4 | round 4 back (2026-11-04): receptacle-m12 1.3 flush in one flat housing face (OCC: no receptacle body proud, no Ø13.5 bore); the female inserts stand 3.4 proud, X03's sleeve 13.1. The STEP has X01 / X02 next to X03 / X04: the face layout waits for its figures |
| 1.3 | round 4 (2026-11-04): receptacle-m12 1.2 (female threaded bores; X03 a male threaded sleeve): each receptacle sits in a Ø13.5 bore of the housing, female front faces 1.5 proud, the mating plane 1.0 out; the pocket for the nut is gone (the male nut's knurl stays outside the housing) |
| 1.2 | round 3 (2026-11-04): genders on file (manual p. 32-34: X03 Power In male, the rest sockets; the STEP agrees); receptacles 1.1 to the STEP read-back of these very ports |
| 1.1 | every port is a receptacle-m12 (sleeve, coded insert, socket contacts, seal; X03 power IN a male inlet) in a pocket of the body that leaves room for the nut, 1.5 proud of the face (the STEP's rims stand 1.7 proud): a cable's pins meet these contacts; `conditions` per port and pole; own triangle budget 24000 (TRIANGLES) for the 12 receptacles |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
