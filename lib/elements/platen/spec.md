# platen · v1.0 · belt grinder platen: face 60 × 250 × 10, stand-off 30, mounting flange 130 × 80 × 10 with 2 × M8 holes

**What** The platen of a belt grinder: the flat plate the abrasive belt runs over between the contact wheel and the idler. The work
is pressed against the belt where the platen backs it, so the belt grinds a flat face instead of following the work. It is the
platen of grinder-belt (lib/machines-factory.txt line 111: frame-welded (own), motor-iec, belt-abrasive (new), platen (own),
wheel-contact (new), tensioner-belt, guard-panel (own), pbs-6h-22, op-estop-22-2nc, dust-collector (new)). The machine's frame carries
it between the wheels; a BOM places it with its flange's back face on the frame.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks platen own_design "yes").
No product was matched and no vendor file was opened. The mounting holes are on file (ISO 273); every other size is a design
choice.
**Units / frame** mm, Z up. Origin: the mounting flange's back face y = 0 (the grinder frame's face) at the flange's centre x = 0,
z = 0. The belt runs along z over the face plate's front face at y = −50; x is across the belt. Extents x −65 to 65, y −50 to 0,
z −125 to 125.
**Built with** toolkit 1.3 · AutoLISP command `PLATEN` · no parameters.

## Mechanism
No moving part. The whole platen is the fixed body; the belt slides over its front face.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| mounting holes | 2 × M8, Ø9 through the flange (y −10 to 0), at x ±50, z 0 (100 apart) | ISO 273 medium (H13), lib/standards/holes.csv. The screws are the assembly's: placed by it, not built here |
| the belt | runs over the face plate's front face, y −50, x −30 to 30, z −125 to 125 | belt-abrasive is not built yet and no belt-size standard is on file: the face is sized for a belt up to 50 wide as a design choice, and the fit is checked when the belt is on file |
| the grinder frame | the flange's back face, 130 × 80, at y 0 | frame-welded's grinder-belt variant is not drawn yet; the frame's holes are drilled to the flange's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The two mounting holes carry a declared position tolerance Ø0.8 at MMC to A, the flange's back face (the frame's face), the holes
located to each other (features.csv; H − F = 9 − 8 = 1.0). Their 100 spacing under ISO 2768-m (±0.3, lib/standards/general-
tolerances.csv row m 30-120; a Ø0.6 zone) stays inside it.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| face plate | 60 (x) × 250 (z) × 10 (y), y −50 to −40 | wide enough for a belt up to 50 wide with 5 to spare a side; 250 long to back the belt over a work length between two wheels; 10 thick so it stays flat in grinding (no flatness claim is made) |
| face plate ends | plain, square | a lead-in radius or chamfer where the belt comes on is left to a later version; the belt's run-on is set by the wheels' positions in the assembly |
| stand-off block | 40 (x) × 70 (z) × 30 (y), y −40 to −10 | holds the face 30 in front of the flange, so the belt clears the flange's screws |
| mounting flange | 130 (x) × 80 (z) × 10 (y), y −10 to 0 | wider than the face plate, so the two screws sit outside the face's outline and a key reaches them from the front |
| mounting holes | x ±50, z 0 | 20 clear of the face plate's sides (x ±30) and 15 in from the flange's ends |
| finish | face plate bare ground steel; stand-off and flange painted | the face is where the belt rubs; the bracket is painted like the frame |

## Named nodes
None (fixed body only). Colliders `face` (the face plate) and `bracket` (stand-off and flange).

## Materials by layer
`M-SILVER` the face plate (bare ground steel, the library's bright-metal layer). `M-STEEL-7035` the stand-off and flange (painted
RAL 7035).

## Notes
No load, wear, flatness or stiffness claim: no grinding force, belt tension or belt speed is on file. No wear liner (a hard or glass
liner on the face) is drawn. No guard function: the platen is not a guard; grinder-belt's guards are guard-panel. No vendor names,
no label.

## Outputs (out/)
`platen.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r78, unattended) |
