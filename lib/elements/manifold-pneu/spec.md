# manifold-pneu · v1.1 · valve manifold sub-base, sized for 18 mm valve stations, NPT ports

**What** a panel-mounted valve manifold (sub-base) meant for 5/2 valves of the ISO 15407-1 18 mm size class: one supply port, two
common exhaust ports, and two work ports per station. The 18 mm valve face is open in 1.x (Open figures), so "18 mm" and the 25
pitch are design intent, not yet tested against the standard; 2.0 cuts the face and first settles which interface it is (ISO
15407-1, or ISO 5599-1, which lib/inventory.csv also names for this row; lib/needs-em/pneu.md, pneu-r7 item (c)). lib/inventory.csv lists it as made of fitting-pushin x4 and silencer x2
(placed in a later version, once they are built). Whether valve-bank and manifold-pneu are one element is still EM's question
(lib/needs-em/pneu.md, pneu-r2 item 3 (iii)).
**Class** device · **Baseline** our own design (OPERATING.md 12: manifolds; lib/inventory.csv own_design yes). No vendor file
was opened or measured; nothing of a vendor file ships. Its sizes are design choices (below). What it meets takes its figures
from the pneumatic contract, `toolkit/pneu.py` (request pneu-1, answered 2026-11-05), or is left open (Open figures, below).
**Units / frame** mm, Z up. Origin: back face on the panel y = 0, left end x = 0, bottom face z = 0; stations along +x, the
valve face toward −y. Ports follow pneu.py's port frame: the pivot on the face, its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `MANIFOLD-PNEU` · `stations` (4; 1 to 10).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| body | (2 × 20 + 25 n) × 36 × 50: 140 × 36 × 50 at 4 stations; anodised aluminium | own block; 20 end zones carry the fixing holes and end ports |
| station pitch | 25.0 | design choice, wider than the 18 mm size class (pneu.py D6); the ISO 15407-1 face is checked against it in 2.0 |
| fixing holes | 2 × Ø5.5 through, at x = 10 and L − 10, z = 25 | M5 clearance, medium (ISO 273 H13, 5.5 to 5.68; lib/standards/holes.csv). The screw (screw-iso4762, not built yet) is placed in a later version (OPERATING.md 12) |
| fixing-hole position | Ø0.4 to A (back face), B (bottom), C (left end); features.csv | design choice within the floating-fastener limit H − F = 0.50 (ASME Y14.5); ISO 2768-m alone gives Ø0.85 over 120 mm (GDT-010) |
| port-1 (supply) | left end, y = −18, z = 38 | |
| port-3, port-5 (exhaust) | right end, y = −18, z = 38 and z = 12 | both clear of the fixing hole's line at z = 25 |
| st*k*-port-2, st*k*-port-4 (work) | bottom face, x = 20 + 25 (k − 0.5), y = −27 (2) and −9 (4) | |
| port-number fields | 6 × 6, 0.2 proud, centred on each port's axis | the ISO 11727 number is a decal; 0.2 proud for GEO-050 |
| station-number fields (1.1) | 6 × 6, 0.2 proud, on the top face (z = 50) at each station's x, y = −18 | the station number is a decal; on the top face because the valves cover the valve face (−y) |
| complexes.org field (1.1) | 16 × 8, 0.2 proud, on the top face's left end zone, centred x = 10, y = −18 | the mark is a decal; same reason |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727 numbers) |
| `port-3`, `port-5` | NPT1/4 | female | exhaust | as above; PNE-005 asks a silencer on each in an assembly |
| `st<k>-port-2`, `st<k>-port-4` | NPT1/8 | female | work | as above; NPT1/8 is pneu.ISO15552[32]'s port, so one fitting size serves both ends of a cylinder's line |

The sizes 1/4 and 1/8 are our choices within pneu.THREADS. Ports are female and take sealant on the male (PNE-002).

## Open figures
Both are class B (fits; OPERATING.md 6), set by the lane in pneu-r9; each wants a source and EM's line.
- NOT ON FILE (B): the NPT port bores (tap size, depth, engagement; ASME B1.20.1 table). pneu.NPT is empty, so no bore is cut in
  1.x; each port is a pivot on its axis with its number field. The bores are cut in 2.0 (a new cut-out: a major version).
- NOT ON FILE (B): the ISO 15407-1 18 mm valve interface face (port holes, screw pattern, seal). pneu.ISO15407_18 is empty, so the
  valve face is plain in 1.x and has no internal passages. It is cut in 2.0, and the pitch is checked against it then.

Proposed by the lane (pneu-r9; OPERATING.md 8.c: EM approves by adding "· EM <date>"; until then they clear nothing):
- REVIEW accepted: the NPT port bores left uncut in 1.x (pivots and number fields only), to be cut in 2.0 once pneu.NPT is on file
- REVIEW accepted: the 18 mm valve face left plain in 1.x, to be cut in 2.0 once pneu.ISO15407_18 (or the ISO 5599-1 choice) is on file
- Not claimed: a pressure rating. An own design states no rating of its own (OPERATING.md 12), so there is no ratings.csv,
  and in an assembly PNE-003 gives REVIEW (rating not on file) until a figure for our block is on file.

## Named nodes
`port-1`, `port-3`, `port-5`, `st1-port-2` … `st<n>-port-4` (kind port, fixed; range 0)

## Materials by layer
`M-ALU-ANOD` body · `M-WHITE-PA` port-number fields

## Decals (Blender)
port numbers 1, 2, 3, 4, 5 on their fields (ISO 11727); from 1.1 the station numbers 1 … n on their top-face fields and
complexes.org on the top face's left end field, where no valve covers them and they stay legible in service (review
manifold-pneu-1.0 finding 1; ISO 4414 on identification, clause to be cited once the text is on file). No vendor names.

## Outputs (out/)
`manifold-pneu.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design, pneu-r7 (unattended): block, fixing holes, port pivots and fields; bores and valve face left open (Open figures) |
| 1.1 | pneu-r9 (unattended), review manifold-pneu-1.0 findings 1 and 2: station-number and complexes.org fields on the top face (were planned on the valve face, which the valves cover); TITLE and What say the 18 mm face is still open; open figures classed B, two sign-off lines proposed. Nodes, origin and cut-outs unchanged (a minor) |
