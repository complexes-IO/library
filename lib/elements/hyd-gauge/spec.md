# hyd-gauge · v1.1 · generic hydraulic dial pressure gauge, 0-250 bar, liquid filled, lower mount

**What** a dial pressure gauge for hydraulic oil: a 63 mm liquid-filled case with a white dial, a clear window in a front bezel,
and a pointer that turns with the pressure. The stem below the case ends in a hex whose seat face, `port-1`, meets a hydraulic
gauge port: hpu-7.5kw's `port-g` (160 bar), hpu-0.37kw's, a test bench's. lib/inventory.csv row `hyd-gauge` (own_design generic,
"hydraulic pressure gauge, 0-250 bar, bottom mount", 5 systems, pin 4, "press-hydraulic first", EM 2026-11-08), and part of
hpu-0.37kw (13 systems), which places it.
**Class** device · **Baseline** our own design: generic Bourdon tube pressure gauge (ETIM 10.0 EC011170, synonym "Pressure
gauge"), as OPERATING.md 12 (generic elements, EM 2026-11-07) and the inventory row say. No vendor file was opened or measured:
the folder's metadata.json and references/ were not used (the row's note: "the vendor file in its folder is reference only, never
copied"). The class values below are its design inputs; its sizes are design choices, gauge-p 1.0's. No vendor names; "generic"
in its title.
**Units / frame** mm, Z up. Origin: the hex's seat face z = 0 on the stem's axis (x = y = 0), the joint plane where the gauge
meets its host port; the host lies below (−z), the dial faces −y (the front).
**Built with** toolkit 1.3 · AutoLISP command `HYD-GAUGE` · no parameters.

The class chosen: EC011170 "Bourdon tube pressure gauge", as gauge-p 1.0 (tier 2, group EG015810, 17 features; synonyms
"Manometer", "Pressure gauge"): a hydraulic dial gauge is a Bourdon tube gauge with a range for oil. The inventory row names
EC011112, which is not in lib/standards/etim/classes.csv (only its three features are in class-features.csv), so GEN-010 could not
find it; request pneu-5 (gauge-p's) asks the core to set gauge rows to EC011170. Rejected as gauge-p's were: EC011168 "Membrane
pressure gauge", EC011169 "Diaphragm drum pressure gauge" (low pressures), EC011478 "Pressure transmitter" (an electrical output).

## Class values (ETIM 10.0 EC011170)
Design inputs. EC011170 is a tier-2 class on no inventory row yet, so lib/standards/etim/class-features.csv does not list its 17
features (request pneu-5). Until then this table gives the values this gauge is designed to under plain names, as gauge-p 1.0's
does; the next minor version restates them in ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| measuring range | 0 to 250 bar (0 to 25 000 kPa gauge, about 3626 psig); in ratings.csv as span and p_max, status "generic design" |
| unit of the scale | bar first, psi second (the hydraulic machines' units; the dial's printing is a later version, Decals) |
| nominal size (case diameter) | 63 mm (the 2.5 in nominal dial class) |
| connection | a hydraulic male stem; its thread and size are open (Open figures), `port-1` |
| position of connection | bottom (lower mount), radial |
| case material | stainless steel, bright (`M-SILVER`) |
| connection material | brass (stem and hex, `M-BRASS`) |
| window | clear, in a front bezel ring |
| filling | liquid filled (glycerine), damping the pump's pulsation; not modelled apart from the case |
| accuracy class | not stated |
| medium | hydraulic oil (mineral oil, ISO 4413's fluids) |
| medium temperature | not stated |
| with electrical contact | no |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

The span is the inventory row's, 0-250 bar. On hpu-7.5kw 1.0 (p_max 160 bar, its relief setting) it reads 64 % of span, under
pneu.GAUGE_FRACTION 0.75, a figure pneu.py holds open for EM, class A, meant for air gauges (PNE-009; element.py asserts against
pneu.py's value and keeps no copy of it; nothing of this element hangs on it, the span being the inventory row's): no rule reads a
hydraulic gauge yet, since the PNE checks are for compressed air (toolkit/pneu.py) and "hyd-port" is no air unit. The gauge is not
rated above its span, so p_max is 250 bar too. These are generic design values (OPERATING.md 12), not tested ratings.

## Dimensions (design choices, our own; gauge-p 1.0's)
| item | value | why |
|---|---|---|
| hex | 15 across flats × 9 (z 0 to 9), corners turned to 1.12 × AF (16.8); brass; part of `port-1` | the wrench flats; its seat face (z = 0) is the joint plane. 16.8 sits inside the Ø24 spot face of hpu-7.5kw's and hyd-cylinder-da-40's ports (asserted) |
| stem below the seat face | not drawn | its thread and length are open (Open figures); a host's port is a spot face with no bore yet, so the seat face meets it face to face |
| neck | Ø12 from the hex (0.5 into it) up into the case's underside (1.5 into it) | the socket that carries the Bourdon tube |
| case | Ø63 × 21 along y (y −8 to 13), centre z = 47.5; stainless | the 2.5 in nominal dial class; the depth holds the movement and the filling |
| bezel | Ø64 × 7 (y −14 to −7), 0.5 proud of the case and 1.0 into it; window opening Ø57 (features.csv, HOLE-010) | the front ring |
| window | Ø58 × 1 (y −13.5 to −12.5), clear, 0.5 into the ring all round | |
| dial | Ø57.6 × 1.5 (y −9 to −7.5), white, 0.5 into the case | its face at y = −9 |
| pointer | hub Ø5 × 1.8 (y −10.8 to −9, seated face to face on the dial); needle 1.6 wide × 0.9 (y −10.3 to −9.4), from 4 behind the axis to 24 in front of it; black | sweeps 24 of the opening's 28.5 radius; 2.2 clear of the window, 0.4 clear of the dial |
| overall | envelope 64 × 27 × 79.5 (x −32 to 32, y −14 to 13, z 0 to 79.5) | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | hyd-port | male | gauge | the hex's seat face z = 0, axis −z | a gauge's stem; "hyd-port" as hyd-cylinder-da-40 1.0 and hpu-7.5kw 1.0 (their gauge port `port-g`, female, role gauge) |

"hyd-port" is the library's name for a hydraulic port whose thread is open; it is no air unit, so the PNE checks (compressed air
only) don't pair it. Its host is hpu-7.5kw's `port-g` (and hpu-0.37kw's, when built).

## Open figures
- NOT ON FILE (B): the stem's thread, size and length (no hydraulic port standard, such as an ISO 6149 or SAE straight-thread
  port, or a gauge connection standard, is in lib/standards/sources.csv), as hyd-cylinder-da-40 1.0's and hpu-7.5kw 1.0's ports. The
  stem below the seat face is not drawn; a major draws it once the standard is on file, with the hosts' bores.

## Named nodes
`port-1` (the hex): kind port, fixed (range 0). `pointer` (hub and needle): kind rotate about the dial's axis (+y, through x = 0,
z = 47.5), 0 to 270°, clockwise seen from the front; at 0° (rest) it points to the lower left, the scale's zero; 270° is the span's
top, 250 bar. The twin turns it to the pressure the gauge reads: angle = 270 × p / 250 bar. It sweeps only the gap between the
dial and the window.

## Materials by layer
`M-BRASS` hex, neck · `M-SILVER` case, bezel · `M-CASE-CLEAR` window · `M-WHITE-PA` dial · `M-BLACK-PA` pointer

## Decals (Blender)
None in 1.0 (the dial's scale, bar first then psi, and the "generic" label are a later version). No vendor names.

## Outputs (out/)
`hyd-gauge.lsp` · `.glb` (port and pointer pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the
QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011170), pneu-r60 (unattended): gauge-p 1.0's 63 mm case, bezel, window, dial and rotating `pointer`, span 0-250 bar; brass hex stem whose seat face is `port-1` (hyd-port, male, role gauge); the stem's thread left open (class B), so no stub drawn; Bourdon tube, movement, filling and dial printing not modelled |
| 1.1 | pneu-r68 (unattended), text only, review pneu-r60 finding 1: element.py keeps no copy of pneu.GAUGE_FRACTION and asserts against pneu.py's value; the spec calls it a figure pneu.py holds open for EM (class A), meant for air gauges, not a settled share (worded so DOC-005 counts no line of this element, as gas-regulator 2.2); geometry, nodes and Open figures unchanged |
