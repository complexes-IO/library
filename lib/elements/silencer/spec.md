# silencer · v1.0 · generic exhaust silencer, sintered, NPT 1/8 or NPT 1/4 male

**What** the exhaust silencer of the pneumatic line (lib/inventory.csv row `silencer`, "exhaust silencer, sintered, NPT 1/8 and
1/4", own_design generic; a common part, pneu-1's `silencer-npt`: the vacuum ejector and manifold-pneu place it, `made_of`). It
screws into a valve's or manifold's exhaust port (pneu.NODES port-3 / port-5) and lets the exhaust air out through a porous sintered
body, so the port is not left open (PNE-004) and the exhaust is silenced (PNE-005: an exhaust joined to a part whose port role is
"silencer" passes).
**Class** connector · **Baseline** our own design: generic exhaust silencer (no ETIM class; ASME B1.20.1 values), as OPERATING.md 12
(generic elements, EM 2026-11-07; a product class ETIM has no class for is generic by the standard its values follow, EM
2026-11-08) and request pneu-3's answer (lib/requests/core/pneu-3-answer.md) say: the subset on file has no pneumatic silencer
class (EC011254 is a fan silencer), so `etim` stays empty. No vendor file was opened or measured. Its one interface takes its
figures from the standard on file (ASME B1.20.1, through toolkit/pneu.py); its sizes are design choices. No vendor names; "generic"
in its title.
**Units / frame** mm, Z up. Origin: the hex's seat face (z = 0) on the stub's axis, the joint plane where the silencer meets its
port; the stub below (toward the host's port, −z), the body up. pneu.py's port frame: the pivot on the joint plane, its axis toward
the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `SILENCER` · parameter `thread` = NPT1/4 (default) or NPT1/8.

## Class values (no ETIM class; ASME B1.20.1 values)
Design inputs (OPERATING.md 12): the quantities an exhaust silencer is chosen by, with the value this one is designed to.

| # | quantity | value |
|---|---|---|
| 1 | connection | male pipe thread, NPT 1/4 (default) or NPT 1/8 (`thread`), ASME B1.20.1 (pneu.THREADS, D1) |
| 2 | stub | Ø E1 + h × L2 from pneu.NPT: 13.616 × 10.205 (NPT 1/4), 10.242 × 6.702 (NPT 1/8); the thread drawn plain (fitting-pushin 2.0's rule) |
| 3 | silencing element | porous sintered bronze, cylindrical, open all round (its pores not modelled) |
| 4 | max. operating pressure | not claimed: no class feature and no standard on file states one (Open figures) |
| 5 | noise reduction | not stated (a maker's tested figure) |
| 6 | flow (exhaust capacity) | not stated (a maker's tested figure) |
| 7 | medium | compressed air, ISO 8573-1 [7:4:4] as the line's (pneu.py D3); exhaust to atmosphere |
| 8 | port role | silencer (pneu.ROLES): PNE-004 counts the joined exhaust port as closed, PNE-005 as silenced |

These are generic design values (OPERATING.md 12), not tested figures or a listing.

## Dimensions (design choices, our own)
| item | NPT 1/4 (default) | NPT 1/8 | why |
|---|---|---|---|
| male stub | Ø13.616 × 10.205, z −10.205 to 0 | Ø10.242 × 6.702 | pneu.NPT: E1 + h and L2 (ASME B1.20.1 by its formulas); meets the library's female bores at E1 + h face to face |
| hex | AF 17 × 6, corners Ø19.04 | AF 14 × 5, corners Ø15.68 | wrench flats wider than the thread's largest major diameter E2 + h (13.892 / 10.405), asserted in element.py; corners turned to 1.12 × AF as fitting-pushin and gauge-p |
| sintered body | Ø16 × 24 | Ø13 × 18 | inside the hex's flats and wider than the stub (asserted), so a wrench reaches the hex past it; 0.5 into the hex |
| chamfer step | Ø12 × 2 on the body's top | Ø9 × 2 | the closed end's turned edge |
| envelope | 19.04 × 17 × 41.205 (z −10.205 to 31) | 15.68 × 14 × 30.702 (z −6.702 to 24) | the hex's corners across x, its flats across y; the collider is the square of the corners |

Materials: `M-BRASS` the stub and hex (brass) and the body (sintered bronze).

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 (or NPT1/8) | male | silencer | the hex's seat face, z = 0, axis −z; `length` = L2 | the only port: into a female exhaust port of the same size (PNE-002 pairs one male and one female of one series and size; sealant on the male) |

## Open figures
- NOT ON FILE (A): the silencer's max. operating pressure. ETIM's subset has no silencer class whose feature would state it, and
  ASME B1.20.1 states no pressure, so ratings.csv holds no p_max; a porous element's rating is a maker's tested figure. In an
  assembly PNE-003 REVIEWs the silencer until EM gives a source or a figure. It sits on an exhaust, which carries the valve's
  outlet pressure for a moment as the valve shifts.

## Named nodes
`port-1` (the stub and the hex); kind port, fixed (range 0). The body is fixed geometry; nothing moves.

## Materials by layer
`M-BRASS` stub, hex, sintered body, chamfer step

## Decals (Blender)
None in 1.0. No vendor names, no approval marks.

## Notes
- A common part (OPERATING.md 12, foundation first): placed, never redrawn, by each host that has an exhaust, version pinned.
  vacuum (a later element) and manifold-pneu 2.0 place it; manifold-pneu 1.1 doesn't (it waits for pneu.ISO15407_18).
- No flow or noise figure is claimed; a valve's exhaust flow is the host's. A silencer chosen for a larger valve is the same
  element at the next thread size (a new parameter value, once NPT 3/8 is wanted: a minor).

## Outputs (out/)
`silencer.lsp` · `.glb` (port pivot, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (no ETIM class; ASME B1.20.1 values), pneu-r61 (unattended): NPT male stub `port-1` (role silencer) from pneu.NPT, hex, sintered body with a chamfer step; `thread` NPT1/4 (default) or NPT1/8; no pressure rating claimed (one class A open figure) |
