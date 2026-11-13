# cable-tray · v1.0 · perforated cable tray 300 × 100, flanged sides, cut to length

**What** One straight length of perforated sheet-steel cable tray: a slotted bottom, two sides with an inward return flange at the
top, and two M6 splice holes in each side at each end, so lengths join with splice plates. The network bench places it
(lib/inventory.csv); other systems may place it under benches or along walls.
**Class** furniture · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
folder's acquisition record (metadata.json, validation.json, references/source.txt) describes a catalogue wire-basket tray; this
element is not built from it and takes none of its figures. Cable-tray standards (IEC 61537, NEMA VE 1) are not on file: nothing
is taken from them and no load or earthing-continuity rating is claimed.
**Units / frame** mm, Z up. Origin: the run start x = 0, the tray's centre line y = 0, the underside of the bottom z = 0. The run
goes along +x; the open side faces +z.
**Built with** toolkit 1.3 · AutoLISP command `CTRAY` · parameter `length` (3000).

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| splice screw clearance hole | Ø6.6, M6 | ISO 273 medium (H13), lib/standards/holes.csv |

The splice plates and their screws are not built yet: the holes are modelled; a host or a later version places them.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| outside width | 300 | a bench-width tray for a classroom network bench |
| outside height | 100 | |
| sheet | 1.5, galvanised steel | |
| return flange | 20 inward from each outer face, at the top | stiffens the side edge and covers the sheet edge |
| bottom slots | 50 × 10, three across at y = −90, 0, 90, rows every 100, centred on the length (30 rows at 3000) | drainage and tie points |
| splice holes | 25 and 75 from each end, 50 above the underside, both sides | two screws per side per joint |
| length | 3000 (parameter) | |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The checker takes all eight Ø6.6 holes as one pattern across the length (3 m). Each end's four holes are declared at position
Ø0.5 at MMC (features.csv; H − F = 6.6 − 6.0 = 0.6), with the bottom face as datum A and the run's end as datum B: a splice joins
one end of this length to one end of the next, so the holes at the two ends of one length are not a fit with each other.

## Named nodes
none (nothing moves). Collider `body` (the whole envelope).

## Materials by layer
`M-GALV` bottom, sides and flanges.

## Notes
No load rating, no earthing claim and no safety claim. No open figure in this version: the mating figure is on file, the rest are
design choices. Covers, bends, tees and drop-outs are separate elements if a system needs them.

## Outputs (out/)
`cable-tray.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r5, unattended) |
