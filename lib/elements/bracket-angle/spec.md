# bracket-angle · v1.2 · angle bracket 40 for T-slot profile, 2 × M8

**What** Inner-corner angle bracket that joins two 40 × 40 T-slot profiles (tslot-40) at 90°: one leg on each profile face, one M8
screw per leg into the profile's slot. A common part: frames, guards and machine bases place it, never redraw it.
**Class** plate · **Baseline** our own design (EM's r4 rule, 2026-11-05: no product to match). No vendor file was opened. The
profile it meets is tslot-40 1.0 (our own design, built and released in mech-r109): its face width and slot opening are read from
it with library.load, one home for each figure.
**Units / frame** mm, Z up. Origin: the inner corner, where the two profile faces meet, at the bracket's mid-width. Leg H lies on
the face z = 0 and runs toward +x; leg V lies on the face x = 0 and runs toward +z; the width is along y (the profiles' slots run
along x and z, centred on y = 0).
**Built with** toolkit 1.3 · AutoLISP command `BRKA` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| profile face width | 40 × 40, slot centred on each face | tslot-40 1.0 (library.load: S 40; its slots centred on each face). The bracket's legs, width and hole line are laid out on it |
| profile slot opening | 10 | tslot-40 1.0 (library.load: THROAT 10). The bracket takes no figure from it but the screw size below. Until 1.1 this row read 8 from a catalogue record in tslot-40's folder; tslot-40 was built with 10 (its own design), and the bracket's part did not depend on the figure |
| screw clearance hole | Ø9.0, M8 | ISO 273 medium (H13), lib/standards/holes.csv |
| screw size | M8 | the slot opening 10 passes an M8 shank (6g, just under 8) with about 1 each side, as tslot-40 1.0 lays it out; the nut is tslot-nut 1.0 (sized to tslot-40's slot), placed with the screws by a later version or by the host |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| leg length | 40 each | one profile width, so the bracket stays inside the face of a 40 profile |
| width | 36 | 2 inside each edge of the 40 face |
| thickness | 6 | a cast bracket's wall; no load rating is claimed |
| hole centre | 20 from the inner corner, on the centre line | mid-leg: the screw head clears the other leg |
| material | anodised aluminium | |

## Named nodes
none (nothing moves). Collider `body`.

## Materials by layer
`M-ALU-ANOD` both legs.

## Notes
No ratings and no safety claims. No open figure: the profile's face and slot come from tslot-40 1.0, the screw clearance from
ISO 273; the rest are design choices.
GD&T: each leg has one hole, so neither is a pattern (GDT-010 checks Ø9.0 for M8: H − F = 1.0).

## Outputs (out/)
`bracket-angle.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r4). Legs 6 thick: built at 4 first, the AutoCAD gate rejected the four 3.95 mm corner edges of the lower leg (each fillet removed 85 to 88 % of its expected volume, where three fillets meet; the gate wants 90 %) |
| 1.1 | review bracket-angle-1.0 finding 1 (mech-r19): the profile's face width and slot width marked as open figures, class B (only a catalogue record behind them); "no open figure" withdrawn; the slot-clears-the-shank claim made conditional. Text only: the part, nodes, origin and holes are 1.0's |
| 1.2 | review mech-r109 finding 1 (a) (mech-r121, unattended): tslot-40 1.0 is built, so the face (40) and the slot opening (10, not the catalogue record's 8) are read from it with library.load and cited; the two class B lines EM accepted at 1.1 close with it (the figure changed, autopilot.md 2 a3). Text only: the part, nodes, origin and holes are 1.0's |
