# cable-pwr-480 · v1.4 · motor branch cable 3P+E 480 V

**What** The panel-to-motor cable of the cell: a 3P+E pin-and-sleeve plug for port-pwr-480, a 14/4 SOOW 600 V cord, and at the motor end the cores out of the jacket as wire elements with prepared ends for the motor's terminals.
**Class** cable · **Baseline** see element.py BASELINE; nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: end A (plug) mating face at the origin, plugging along +y into a receptacle that looks toward −y; the jacket leaves toward −y and follows `path`.
**Built with** toolkit 1.3 · AutoLISP command `C480` · `length` (4000), `path`, `size` (mm² per core: 2.08 = 14 AWG, the one size whose cord OD is on file; any other size stops the build), `cores` (colours L1/L2/L3/PE: black / white / red / green, as the cord comes), `strip`, `ferrule` (true), `conditions` ('L1:a:under-stripped': pole, wire end, condition).

## Dimensions
| item | value |
|---|---|
| plug | Ø48 x 60 body + Ø38 x 45 grip, envelope Ø48 x 105 (Assumption (B): fits and envelope, OPERATING.md 6; sized to mate port-pwr-480 1.1's Ø44 socket face (its element.py, the socket face radius 22.0), a modelled size that element gives no source for and does not yet mark open; a source wanted: the IEC 60309-2 plug's standard sheet or a plug's drawing) |
| cord | 14/4 SOOW, OD 14.48, swept along the route |
| cores | four wire elements, 90 out of the jacket, ferruled by default |

## Figures and their sources
| figure | value | source |
|---|---|---|
| conductor size | 14 AWG (2.08 mm²) | chosen by the standards (below), not a preference |
| current rating | 15 A (14 AWG cord, three current-carrying) | NEC Table 400.5(A)(1) column A |
| what it must carry | ≥ 1.38 A: 125 % of the motor's 1.1 A table current | NEC 430.22; 430.6(A)(1); Table 430.250 (1/2 hp, 460 V) |
| what must protect it | the 10 A branch breaker q3 (C10): 15 A ≥ 10 A | NEC 240.4 / IEC 60364-4-43 (ELR-013) |
| smallest power conductor | 14 AWG | NFPA 79 minimum conductor size for power circuits (read from two secondary sources, named in references/source.txt; the clause and edition are not cited yet, review cable-pwr-480-1.1 finding 4) |
| voltage drop, 4 m at 1.1 A | about 0.08 V (0.02 %) | 14 AWG 3.14 Ω/kft at 75 °C (NEC Chapter 9 Table 8): negligible |
| cord type, voltage, temperature | SOOW, 600 V, 90 °C, oil- and water-resistant | maker's datasheet (references/source.txt) |
| core colours | black, white, red (phases), green (equipment ground) | maker's datasheet (references/source.txt); a white core in a flexible cord may carry a phase (NEC 200.7(C)) |
| cord OD | 14.48 (0.570 in) | maker's datasheet (references/source.txt); the only row of element.py `JACKET_OD` (1.2) |
| plug envelope | Ø48 x 105 | the Dimensions table's plug row, classed there (one line for EM) |

## Named nodes
`port-a` (kind port, unit 480V-3P+E, gender male) · `port-b` (kind port, gender none: the jacket end in the motor's gland) · `core-l1/l2/l3/pe` with `.end-a` (at the motor terminal) and `.end-b` (contacts)

## Materials by layer
`M-RED-PA` plug · `M-BLACK-PA` grip · `M-CABLE-GREY` jacket · cores black / white / red / green (the US cord as it comes; an IEC cable would be brown / black / grey / green-yellow, IEC 60445)

## Decals (Blender)
none

## Notes and assumptions
The conductor size follows from the standards: the breaker that protects the cord (ELR-013) and 125 % of the motor current (ELR-016) both pass with 14 AWG, and 14 AWG is the smallest power conductor NFPA 79 allows. A bigger motor on this branch re-runs both checks. The plug's pins (IEC 60309 contacts) are not elements yet. The earth contact's clock position is on file: 7 h, the 3P+E 480 V keying of IEC 60309-2, from port-pwr-480's brief (its references/measure.md, the identity line and "Ports", from the receptacle's 2-D drawing p. 1), so the plug is the 7 h plug that mates it. The contacts' sizes and pin positions are NOT ON FILE (B): a fit, not behaviour, since the twin takes which core is PE from the node `core-pe` and the pole order L1 / L2 / L3 / PE, not from a contact's position (OPERATING.md 6; review cable-pwr-480-1.2 finding 1). A source wanted: the IEC 60309-2 standard sheet for the 3P+E 480 V configuration.

## Outputs (out/)
`cable-pwr-480.lsp` (solids only: the swept insulation or jacket is glTF only) · `.glb` (contact and port data in the node extras, `-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.4 | 2026-11-08 (elec-r17, unattended): review elec-r15 findings 2 and 3 (cable-pwr-480-1.3 findings 1 and 2): the plug row's reason now says port-pwr-480's Ø44 socket face is a modelled size with no source and no open-figure mark in that element (it had called it an open figure there); the earth contact's 7 h clock position is cited from port-pwr-480's brief (receptacle drawing p. 1, IEC 60309-2), and the contacts' open line, still class B, covers their sizes and pin positions only. Text only: same nodes, origin, shapes and default build |
| 1.3 | 2026-11-07 (elec-r15, unattended): review cable-pwr-480-1.2 finding 1: the plug envelope is one open line, class B (fits and envelope), and the contacts' open line class B, each with its reason (the Dimensions plug row; Notes); finding 2: the 15 A has one source, NEC Table 400.5(A)(1) column A (it leaves the BASELINE's datasheet list). Text only: same nodes, origin, shapes and default build |
| 1.2 | 2026-11-06 (elec-r11, unattended): SRC-010: the cord OD is looked up as `JACKET_OD[size]`, and a size the table lacks stops the build naming the table (role card, wire and cable to the NEC, a); the unsourced 1.5 / 2.5 / 4 / 6 mm² rows are gone (review finding 6). PIN-002: `port-b` declares gender none (a gland, OPERATING.md 6). DOC-006: the maker's name and part number and the trade sources move to references/source.txt (review finding 1). The default build (2.08 mm²) is unchanged: same nodes, origin and shapes |
| 1.1 | 2026-11-04: conductor 14 AWG 14/4 SOOW 600 V, chosen by NEC 240.4 / 400.5(A)(1) / 430.22 and the NFPA 79 minimum; OD 14.48 and core colours from the cord's datasheet |
| 1.0 | first build: the element layer reaches the wire and its termination (2026-11-03), toolkit 1.3 |
