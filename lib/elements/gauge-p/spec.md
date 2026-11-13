# gauge-p · v1.0 · generic dial pressure gauge, 0-160 psig, NPT 1/4 male lower mount

**What** a dial pressure gauge for compressed air: a 63 mm case with a white dial, a clear window in a front bezel, and a pointer
that turns with the pressure. The stem below the case ends in a hex and a male NPT 1/4 stub, `port-1`, that screws into any
female NPT 1/4 gauge port on an air line: the bench FRL's `port-g` (next.md decision 1), a receiver or a manifold.
lib/inventory.csv row `gauge-p` (own_design generic, "pressure gauge, 0-100 psig, NPT 1/4 lower mount (pneu-1 D3)", 7 systems,
and part of frl, 14 systems). Built before frl because frl places it (OPERATING.md 12, foundation first).
**Class** device · **Baseline** our own design: generic Bourdon tube pressure gauge (ETIM 10.0 EC011170, synonym "Pressure
gauge"), as OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was
opened or measured (the folder's metadata.json and references/ were not used). The class values below are its design inputs;
its sizes are design choices; its stub takes its figures from the standard on file (ASME B1.20.1, through toolkit/pneu.py). No
vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the hex's seat face z = 0 on the stem's axis (x = y = 0), the joint plane where the gauge
meets its host port; the stub runs down (−z) into the host, the dial faces −y (the front).
**Built with** toolkit 1.3 · AutoLISP command `GAUGE-P` · no parameters.

The class chosen: EC011170 "Bourdon tube pressure gauge" (tier 2, group EG015810, 17 features; synonyms "Manometer", "Pressure
gauge"), the dial gauge with a C-shaped Bourdon tube that bench gauges are. The inventory row names EC011112, which is not in
lib/standards/etim/classes.csv (only its three features, diameter, colour and material, are in class-features.csv), so GEN-010
could not find it; request pneu-5 asks the core to set the row to EC011170. Rejected: EC011168 "Membrane pressure gauge" and
EC011169 "Diaphragm drum pressure gauge" (for low pressures and aggressive media, not a 100 psig air line), EC011478 "Pressure
transmitter" (an electrical output, a different element).

## Class values (ETIM 10.0 EC011170)
Design inputs. EC011170 is a tier-2 class on no inventory row yet, so lib/standards/etim/class-features.csv (tier-1 classes and
the classes the inventory uses) does not list its 17 features; request pneu-5 asks the core to give the inventory row this class,
which brings them in (as request pneu-4 asks for tube-pneu's). Until then this table gives the values this gauge is designed to
under plain names, and the next minor version restates them in ETIM's order with their EF codes, "not stated" where the design
has no value.

| feature | value |
|---|---|
| measuring range | 0 to 160 psig (0 to 1103 kPa gauge); in ratings.csv as span and p_max, status "generic design" |
| unit of the scale | psig first, kPa second (pneu.py D3: "psig first on labels"); the dial's printing is a later version (Decals) |
| nominal size (case diameter) | 63 mm (the 2.5 in nominal dial class) |
| connection | male thread NPT 1/4 (ASME B1.20.1; pneu.py D1), `port-1` |
| position of connection | bottom (lower mount), radial |
| case material | stainless steel, bright (`M-SILVER`) |
| connection material | brass (stem, hex and stub, `M-BRASS`) |
| window | clear, in a front bezel ring |
| filling | none (dry case) |
| accuracy class | not stated |
| medium | compressed air, ISO 8573-1:2010 class [7:4:4] (pneu.py D4) |
| medium temperature | not stated |
| with electrical contact | no |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

The span is the library's own choice, by its gauge rule: PNE-009 (toolkit/v_pneu.py) FAILs a gauge whose span is under the
pressure that can reach it and REVIEWs one read above 75 % of its span (pneu.GAUGE_FRACTION). On a bench line that pressure is
P_SUPPLY, 100 psig (689.5 kPa; pneu.py D3): 0-160 psig reads it at 62.5 %, so PNE-009 passes, and it still passes without the 75 %
line (100 is under 160). A 0-100 psig gauge, the inventory row's wording, would be read at 100 % on every bench line (REVIEW,
EM's), so it is not used; request pneu-5 asks the core to change the row's text to 0-160. The selftest plants the same three
cases (160, 100, 60 psig: PASS, REVIEW, FAIL). The gauge is not rated above its span, so p_max is 160 psig too: PNE-003 compares
it with P_SUPPLY and passes. These are generic design values (OPERATING.md 12), not tested ratings.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT 1/4 male stub | Ø13.616 × 10.205 below the seat face (z −10.205 to 0), 0.5 into the hex; brass; part of `port-1` | pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): Ø = E1 + h, the external thread's major diameter at the hand-tight plane; length L2, the effective thread. Drawn plain, as fitting-pushin 2.0's stub: the 1:16 taper and the thread form are not drawn. A female port bored at E1 + h (tank 2.0) meets it face to face |
| hex | 15 across flats × 9 (z 0 to 9), corners turned to 1.12 × AF; brass; part of `port-1` | the wrench flats; 15 clears the thread's largest major diameter E2 + h = 13.892 (element.py asserts it) |
| neck | Ø12 from the hex (0.5 into it) up into the case's underside (1.5 into it) | the socket that carries the Bourdon tube |
| case | Ø63 × 21 along y (y −8 to 13), centre z = 47.5; stainless | the 2.5 in nominal dial class; the depth holds the movement |
| bezel | Ø64 × 7 (y −14 to −7), 0.5 proud of the case and 1.0 into it; window opening Ø57 (features.csv, HOLE-010) | the front ring |
| window | Ø58 × 1 (y −13.5 to −12.5), clear, 0.5 into the ring all round | |
| dial | Ø57.6 × 1.5 (y −9 to −7.5), white, 0.5 into the case | its face at y = −9 |
| pointer | hub Ø5 × 1.8 (y −10.8 to −9, seated face to face on the dial); needle 1.6 wide × 0.9 (y −10.3 to −9.4), from 4 behind the axis to 24 in front of it; black | sweeps 24 of the opening's 28.5 radius; 2.2 clear of the window, 0.4 clear of the dial |
| overall | envelope 64 × 27 × 89.7 (x −32 to 32, y −14 to 13, z −10.205 to 79.5) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | male | gauge | the hex's seat face z = 0, axis −z; length 10.205 (L2) | pneu.py D1 (NPT, ASME B1.20.1); D3 (the bench's gauge size NPT 1/4) |

PNE-002 pairs it with a female NPT 1/4 (sealant on this male, D1). Its host is an air line's gauge port, frl `port-g` when
built. Not gas-regulator's `port-g`: that reads cylinder pressure (300 bar), far over this span, and PNE-009 would FAIL it there.
A host's port bored at E1 + h (tank 2.0, gas-regulator 2.0) meets the stub face to face.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (stub and hex): kind port, fixed (range 0). `pointer` (hub and needle): kind rotate about the dial's axis (+y, through
x = 0, z = 47.5), 0 to 270°, clockwise seen from the front; at 0° (rest) it points to the lower left, the scale's zero; 270° is
the span's top, 160 psig. The twin turns it to the pressure the gauge reads: angle = 270 × p / 160 psig. It sweeps only the gap
between the dial and the window.

## Materials by layer
`M-BRASS` stub, hex, neck · `M-SILVER` case, bezel · `M-CASE-CLEAR` window · `M-WHITE-PA` dial · `M-BLACK-PA` pointer

## Decals (Blender)
None in 1.0 (the dial's scale, psig first then kPa, and the "generic" label are a later version). No vendor names.

## Outputs (out/)
`gauge-p.lsp` · `.glb` (port and pointer pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011170), pneu-r56 (unattended): 63 mm stainless case, bezel, window, white dial, rotating `pointer`, brass hex stem with the male NPT 1/4 stub `port-1` (pneu.NPT: E1 + h, L2); span 0-160 psig by PNE-009 at P_SUPPLY; the Bourdon tube, movement and dial printing not modelled |
