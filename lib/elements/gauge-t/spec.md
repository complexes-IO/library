# gauge-t · v1.2 · generic bimetal dial thermometer, 0-120 C, 63 mm case, 100 mm stem, NPT 1/4 male back mount

**What** a dial thermometer for a liquid or air line: a 63 mm case with a white dial facing up, a clear window in a bezel, and a
pointer that turns with the temperature. Below the case, on the dial's axis, a hex and a male NPT 1/4 stub, `port-1`, screw into a
female NPT 1/4 port; under the stub a 100 mm stem carries the bimetal coil into the medium. lib/inventory.csv row `gauge-t`
(own_design generic, ETIM EC011165, 2 systems: calibration-bench, process-skid).
**Class** device · **Baseline** our own design: generic Bimetal thermometer (ETIM 10.0 EC011165, synonym "Thermometer"), as
OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic) say. No vendor file was opened or
measured (the folder's metadata.json and references/ were not used). The class values below are its design inputs; its sizes are
design choices; its stub takes its figures from the standard on file (ASME B1.20.1, through toolkit/pneu.py). No vendor names;
"generic" in its title.
**Units / frame** mm, Z up. Origin: the hex's seat face z = 0 on the stem's axis (x = y = 0), the joint plane where the
thermometer meets its host port; the stub and the stem run down (−z) into the host, the dial faces up (+z, the front).
**Built with** toolkit 1.3 · AutoLISP command `GAUGE-T` · no parameters.

The class: EC011165 "Bimetal thermometer" (tier 2, group EG020094 "Temperature and climate measurement instruments", 12 features
on file; synonyms "Index thermometer", "Thermometer"), the class inventory row `gauge-t` names. Its build follows gauge-p 1.0 (the
same case, bezel, window, dial, pointer and stub sizes), turned so the dial faces up over an axial stem: the "back" connection
that suits a thermometer read from above a pipe or a tank lid.

## Class values (ETIM 10.0 EC011165, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | stainless steel, bright (`M-SILVER`) |
| 2 | EF020571 Material process connection | stainless steel (hex, stub and stem, `M-SILVER`) |
| 3 | EF023949 Size of process connection | NPT 1/4 (pneu.py D1: the NPT series, ASME B1.20.1; the gauge port size from request pneu-1's element list, gauge-p "1/4 NPT lower mount", lib/requests/pneu/1.md, and inventory row gauge-p) |
| 4 | EF000443 Connection | male thread, `port-1` |
| 5 | EF020572 Connection location | back (axial, on the dial's centre line) |
| 6 | EF001836 Measuring range | 0 to 120 °C (32 to 248 °F): coolant, chiller water and hydraulic oil below their boiling or flash points |
| 7 | EF002471 Housing diameter | 63 mm (the 2.5 in nominal dial class, as gauge-p) |
| 8 | EF020279 Insert length | 100 mm, from the seat face to the stem's tip |
| 9 | EF020587 With downcomer | no |
| 10 | EF020577 Accuracy class according to EN | not stated |
| 11 | EF020578 Window pane material | not stated (clear, `M-CASE-CLEAR`) |
| 12 | EF020449 Max. operating pressure | 10 bar (1000 kPa); in ratings.csv as p_max, status "generic design" |

The range and the pressure are generic design values (OPERATING.md 12), not tested ratings. 10 bar is above P_SUPPLY (100 psig,
689.5 kPa; pneu.py D3), so PNE-003 passes the thermometer on any bench line (element.py asserts it), and above coolant-pump's 1 bar (its
ratings.csv); chiller's pressure rating is still open (chiller spec.md, Open figures), so no comparison with it is made here. The range is not a pressure, so ratings.csv has no `span` row (PNE-009 reads `span` as
a pressure). The stem goes straight into the medium (no thermowell): a thermowell is its own later element, and a host that needs
one places it.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| NPT 1/4 male stub | Ø13.616 × 10.205 below the seat face (z −10.205 to 0), 0.5 into the hex; part of `port-1` | pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): Ø = E1 + h, the external thread's major diameter at the hand-tight plane; length L2, the effective thread. Drawn plain, as gauge-p's stub: the 1:16 taper and the thread form are not drawn. A female port bored at E1 + h (tank 2.0's rule) meets it face to face |
| hex | 15 across flats × 9 (z 0 to 9), corners turned to 1.12 × AF; part of `port-1` | the wrench flats; 15 clears the thread's largest major diameter E2 + h = 13.892 (element.py asserts it) |
| stem | Ø6.35 (1/4 in) from the stub's end (0.5 into it) to z = −100 | class value 8; holds the bimetal coil (not modelled); it needs a host whose port bores through into the medium (Ports): the blind NPT 1/4 bores on file (L2 + 2 = 12.205 deep) clear only its first 12.2 mm |
| neck | Ø12 from the hex (0.5 into it) up into the case's underside (1.5 into it), z 8.5 to 13.5 | joins the stem to the case |
| case | Ø63 × 21 along z (z 12 to 33) | class value 7; the depth holds the pointer's shaft |
| bezel | Ø64 × 7 (z 32 to 39), 0.5 proud of the case and 1.0 down into it; window opening Ø57 (features.csv, HOLE-010) | the front ring |
| window | Ø58 × 1 (z 37.5 to 38.5), clear, 0.5 into the ring all round | |
| dial | Ø57.6 × 1.5 (z 32.5 to 34), white, 0.5 into the case | its face at z = 34 |
| pointer | hub Ø5 × 1.8 (z 34 to 35.8, seated face to face on the dial); needle 1.6 wide × 0.9 (z 34.4 to 35.3), from 4 behind the axis to 24 in front of it; black | sweeps 24 of the opening's 28.5 radius; 2.2 clear of the window, 0.4 clear of the dial |
| overall | envelope 64 × 64 × 139 (x −32 to 32, y −32 to 32, z −100 to 39) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | male | gauge | the hex's seat face z = 0, axis −z; length 10.205 (L2) | pneu.py D1 (NPT, ASME B1.20.1); the gauge port size NPT 1/4 from request pneu-1's element list (gauge-p) and inventory row gauge-p; role gauge: pneu.ROLES has no instrument role of its own, and a thermometer takes a gauge port |

PNE-002 pairs it with a female NPT 1/4 (sealant on this male, D1). No host on file takes it yet: its host's port must bore through
into the medium (a process port; pneu.py's docstring says liquid process ports wait for a process section, request pneu-2), or the
host places a thermowell or tee that does, with 100 mm of medium below the port's face. The female NPT 1/4 ports on file are blind
bores (L2 + 2 or 12 deep: regulator 1.0, the cloud elements) or not bored, and tank 2.x's ports are NPT 3/8, so none takes the stem.

## Open figures
None. Every figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (stub and hex): kind port, fixed (range 0). `pointer` (hub and needle): kind rotate about the dial's axis (pivot axis −z,
through x = y = 0), 0 to 270°, clockwise seen from above; at 0° (rest) it points to the lower left (−x, −y), the range's bottom,
0 °C; 270° is its top, 120 °C. The twin turns it to the temperature the thermometer reads: angle = 270 × T / 120 °C. It sweeps only
the gap between the dial and the window.

## Materials by layer
`M-SILVER` stub, hex, stem, neck, case, bezel · `M-CASE-CLEAR` window · `M-WHITE-PA` dial · `M-BLACK-PA` pointer

## Decals (Blender)
None in 1.0 (the dial's scale, °F and °C, and the "generic" label are a later version). No vendor names.

## Outputs (out/)
`gauge-t.lsp` · `.glb` (port and pointer pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011165), pneu-r66 (unattended): gauge-p's 63 mm case, bezel, window, white dial and rotating `pointer` facing up, a stainless hex with the male NPT 1/4 stub `port-1` (pneu.NPT: E1 + h, L2) and a Ø6.35 × 100 stem below; 0 to 120 °C, 10 bar; the bimetal coil and dial printing not modelled |
| 1.1 | review gauge-t-1.0.md finding 1, pneu-r72 (unattended): a, Ports and the stem row say no host on file takes the stem yet (blind bores; tank's are NPT 3/8); b, the pressure line names coolant-pump only, chiller's rating being open; c, the NPT 1/4 gauge size cited to pneu.py D1 and request pneu-1's element list, not D3. Text only: a minor |
| 1.2 | review gauge-t-1.1.md finding 1, pneu-r80 (unattended): the stub row says a female port bored at E1 + h by tank 2.0's rule meets it (tank's own ports are NPT 3/8). Text only: a minor |
