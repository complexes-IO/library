# thermowell-npt · v1.0 · generic thermowell, male NPT 3/8 process, female NPT 1/4 instrument

**What** a thermowell (temperature sensor fitting): a closed-ended protective tube that goes into the medium through a line's or a
vessel's female port, so a thermometer's or a sensor's stem reads the medium's temperature without touching it, and can be taken out
without opening the line or draining it. A wrench hex; below it a male NPT 3/8 stub into the host's port (the process connection) and
the well tube, closed at its tip; on top a female NPT 1/4 port (the instrument connection) with a bore down the well. It is made for
gauge-t (the lane's bimetal dial thermometer, NPT 1/4 male back connection, Ø6.35 × 100 stem): gauge-t screws into the top port and
its stem hangs in the bore, 2 clear of the floor. Its uses in the lane: gauge-t on the liquid lines of the process skids, the
coolant loop (chiller, coolant-pump) and the heat-exchanger loop (hx-shell-tube), and on tanks (tank, hyd-tank), wherever the
thermometer must come out without a drain-down. It needs a host whose bore past the port takes the Ø12.7 well and whose line or vessel
is deeper than the 92.8 insertion (a tank's or a vessel's side, a large line's tee branch); a small tee would meet the well (Ports).
**Class** connector · **Baseline** our own design: generic temperature sensor fitting (ETIM 10.0 EC004716, synonym "Temperature
measuring fitting"), as OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next ETIM class of EG015540 in pneu's order
(generic.next_classes) that the lane can build unattended (pneu-r115). No vendor file was opened or measured. The class values below are
its design inputs; its sizes are design choices; its threads take their series from the pneumatic contract `toolkit/pneu.py` (request
pneu-1: D1 NPT threads, ASME B1.20.1), and its instrument port, stem bore and well length are read from gauge-t on file. No vendor
names; "generic" in its title.
**Why generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. No standard on file or named in
pneu.py tabulates a thermowell; its only standard figures are its two NPT threads, both from ASME B1.20.1's formulas in pneu.NPT. A
thermowell's strength against the flow's wake frequency and pressure is ASME PTC 19.3 TW's calculation: that code is not on file and
is not claimed here (no rating, Class values), so this element makes no strength or flow-velocity claim. The hex, the well's wall, its
tip and the clearances are design choices.
**Units / frame** mm, Z up. Origin: the hex's seat face (the face that bears on the host's port) z = 0 on the well's axis
(x = y = 0); the host and the medium toward −z, the instrument port up (+z). Ports follow pneu.py's port frame: the pivot on the
joint plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `THERMOWELL-NPT` · no parameters: the well is made for gauge-t's 100 mm stem.

## Class values (ETIM 10.0 EC004716)
Design inputs. EC004716 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv does not list its 13
features: the case request pneu-4 raised for tube-pneu, which the core answered (lib/requests/core/pneu-4-answer.md): the element is
built with its design values under plain names (as tube-pneu 1.0, plug-pushin 1.0, nipple-bulkhead-npt 1.0 and the block fittings).
When the features are on main, a minor version restates this table in ETIM's order with their EF codes, "not stated" where the design
has no value.

| feature | value |
|---|---|
| model | thermowell: a closed protective tube with a process thread and an instrument thread, turned from bar |
| material | stainless steel |
| process connection | male thread, NPT 3/8 (ASME B1.20.1; pneu.py D1) |
| instrument connection | female thread, NPT 1/4 (gauge-t's back connection) |
| insertion length | 92.8 below the seat face (the well's tip) |
| bore for the sensor | Ø7.0, 102 deep below the instrument port's face (takes a Ø6.35 stem 100 long) |
| well outside diameter | Ø12.7 |
| max. operating pressure | not stated: no rating claimed, no ratings.csv (Why generic: ASME PTC 19.3 TW not on file) |
| max. operating temperature | not stated: no rating claimed |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| process stub | male NPT 3/8: a plain cylinder Ø17.06 × 10.36 (L2) below the seat face, 0.5 up into the hex | nipple-hex-npt's stub, from pneu.NPT (calculated from ASME B1.20.1's formulas, EM 2026-11-07): length L2 = (0.80D + 6.8)P; diameter E1 + h, the external thread's major diameter at the hand-tight plane. The library draws threads as plain cylinders; the taper and thread form are not drawn. 3/8 is the largest size of our series (D1), so the Ø12.7 well passes through it |
| hex | 22 AF, 13 long (z 0 to 13), corners turned to 1.05 × AF | flats at least the instrument bore + 2 × 3 of steel and over the process stub (asserted); 1.05 × AF keeps the glb's turned corners within the catalogue envelope's rounding (cap-hex-npt r106's Godot check; asserted). 13 long so the instrument bore is L2 + 2 deep or more, and for the AutoCAD gate's fillet pre-flight (≥ 8) |
| instrument port | female NPT 1/4: a bore Ø13.62 (E1 + h) from the land's face down to the process stub's top, 12.7 deep; a round land Ø19 × 0.2 proud of the hex round it (port-b's node) | cap-hex-npt's port, from pneu.NPT: E1 + h, the male's major diameter at the hand-tight plane, at least L2 + 2 = 12.21 deep (tank 2.0's rule; asserted). gauge-t's stub (the same E1 + h, 10.21 long) fills it face to face and ends 2.5 above its floor (asserted) |
| stem bore | Ø7.0 from the instrument bore's floor down the well to z = −88.8 (blind) | gauge-t's stem Ø6.35 + 0.65 (a slip fit), read from gauge-t; its floor 2 below the end of gauge-t's 100 mm stem (TOP − INSERT_L − 2) |
| well | Ø12.7 (1/2 in) from the stub up 0.5 into it down to the tip z = −92.8; closed tip 4 thick | a wall of 2.85 round the stem bore (≥ 2.5 asserted, for the fillet pre-flight); inside the process stub's diameter so the well passes through the host's port |
| overall | 106.0 long (13.2 above the seat face, 92.8 below); envelope 23.1 across the hex's turned corners | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | NPT3/8 | male | the hex's seat face z = 0, axis −z; the stub runs L2 along the axis (`length` in the pivot's data) | pneu.py D1 (NPT, ASME B1.20.1); PNE-002 pairs it with a female NPT 3/8 port; sealant on this male (D1). The host's bore past its port must take the Ø12.7 well, and its line or vessel must be deeper than the 92.8 insertion |
| `port-b` | NPT1/4 | female | the land's face z = 13.2, axis +z | pneu.py D1; takes gauge-t's `port-1` (male NPT 1/4) face to face, or any male NPT 1/4 instrument stub whose stem is Ø7 or less and 102 or shorter |

The ports carry no role and no ISO 11727 number (design: a fitting's ends are marked by the node's name, nipple-hex-npt's way). No
fluid path joins them: the well is closed, so port-b never sees the medium or its pressure.

## Open figures
None. Every figure is a class value, a design choice above, a figure read from gauge-t, or calculated from ASME B1.20.1's formulas
(pneu.NPT).

## Named nodes
`port-a` (the process stub), `port-b` (the instrument port's land); kind port, fixed (range 0). The hex and the well are the fixed body.

## Materials by layer
`M-SILVER` hex, land, stub and well (stainless steel) · `M-GASKET` the bores' layer (cap-hex-npt's)

## Decals (Blender)
None: no face on a fitting this size carries a legible mark. No vendor names.

## Outputs (out/)
`thermowell-npt.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004716), pneu-r115 (unattended): hex, male NPT 3/8 process stub, closed well Ø12.7 to 92.8 below the seat face, female NPT 1/4 instrument port and a Ø7 stem bore read from gauge-t; two port pivots; no ratings (none claimed) |
