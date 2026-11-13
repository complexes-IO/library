# guard-panel · v1.0 · fixed guard panel 1000 × 800, square tube 30 frame, plain sheet infill 1.5, 4 × M8 fixing lugs

**What** A fixed guard panel for a machine: a welded frame of square tube with a plain sheet infill, bolted by four lugs against
the frame of the machine it guards. The machines of lib/machines-factory.txt (belt grinders, ironworkers, horizontal mills,
notchers, pipe cutters, presses, riveters, plate rolls, cold saws, the hydraulic test bench and the hose crimper) close their
sides with panels of this kind; a BOM places one on a machine frame's face.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs: guards; lib/inventory.csv marks guard-panel
own_design "yes"). No product was matched and no vendor file was opened. The fixing holes are on file (ISO 273); every other
size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting face y = 0 (the back faces of the frame and the lugs, which bear on the machine
frame), x = 0 at the panel's centre, z = 0 at its lower edge. The panel's front, the side a person stands on, faces −y.
**Built with** toolkit 1.3 · AutoLISP command `GRDPNL` · no parameters.

## Mechanism
None: a fixed guard has no moving part. It is removed only by undoing its four screws.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| fixing holes | 4 × M8, Ø9.0, one in each lug, at 1040 × 600 (x ±520, z 100 and 700) | ISO 273 medium (H13), lib/standards/holes.csv. The screws, nuts and the matching holes in the machine frame are the assembly's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four fixing holes carry a declared position tolerance Ø0.8 at MMC to A, the mounting face, the holes located to each other
(features.csv; H − F = 9.0 − 8 = 1.0). The lugs are drilled in a fixture after welding, as the frame's ISO 2768-m general
tolerance over the pattern's 1201 diagonal (±1.2, lib/standards/general-tolerances.csv row m 1000-2000) would not hold the
pattern by itself.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| frame outside | 1000 wide × 800 tall × 30 deep | one panel closes a machine side of the factory list's size; larger sides take two |
| frame | square tube 30 × 30: two uprights full height, a top and a bottom rail between them | stiff enough to carry the sheet without a middle rail at this size |
| infill | plain sheet 1.5, centred in the frame's depth (y −15.75 to −14.25), welded inside the frame | no opening: nothing reaches through it |
| lugs | 4, 40 × 10 × 50, welded to the uprights' outer faces, flush with the back face, centres 100 above the lower edge and 100 below the top | the panel bolts flat against a machine frame's face; each hole's edge 15.5 clear of the upright, room for a nut |
| tubes | drawn by their outside: every tube end is welded shut against another tube, so no bore shows | the model shows what can be seen |
| welds | not drawn | |

## Where it stands (the assembly's)
The panel's height, its distance from the hazard and the gap under it are where a BOM places it, not part of this element: the
safety distances of ISO 13857 and the guard requirements of ISO 14120 are not on file, so this element makes no safety claim and
names no distance. The assembly that places it cites them when they are on file.

## Named nodes
None. Collider `panel` (the frame and the sheet; the lugs are left out).

## Materials by layer
`M-YELLOW` the frame and the lugs (steel, painted yellow). `M-STEEL-7035` the infill sheet (steel, painted RAL 7035).

## Notes
No load rating and no safety claim. No vendor names, no label. A mesh or windowed variant, and the hinged guard, are later
elements.

## Outputs (out/)
`guard-panel.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r48, unattended) |
