# dryer-air · v2.0 · compressed air dryer, generic, adsorption (desiccant), point of use, NPT 1/4 in line, clear bowl

**What** a point-of-use adsorption dryer for a bench drop or a machine's air supply: air enters at port-1, passes through a
replaceable desiccant cartridge in a clear bowl, and leaves dried at port-2. The desiccant changes colour as it takes up water, and
is seen through the bowl; the cartridge is changed when it has turned. It does not regenerate itself and has no drain, so a filter
(filter-air) stands upstream to keep liquid water and particles out of it. It is our own vendor-neutral design of the ETIM class
below (OPERATING.md 12, generic elements, EM 2026-11-07): the class value it is designed to is listed under Class values. No maker's
datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic dryer for compressed air system (ETIM 10.0 EC004030). What it meets takes its
figures from the pneumatic contract, `toolkit/pneu.py` (D1 threads, D7 names, the NPT table); every size the contract and the
standards on file don't fix is a design choice (below). Nothing in its shape is fixed by a dimensional standard.
**Units / frame** mm, Z up. Origin: port-1's face centre, in line: the port axis is the x axis, flow along +x, the bowl hangs
toward −z, the label face toward −y. Ports follow pneu.py's port frame: the pivot on the joint plane (from 2.0 the number
field's outer face, 0.2 in front of the head's end face), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `DRYER-AIR` · no parameters.

## Class values
ETIM 10.0 EC004030 "Dryer for compressed air system" (group EG020014), every feature in ETIM's order
(lib/standards/etim/class-features.csv): the class has one. This is the value this element is designed to: it defines it as a member
of the class, and it is a design input.

| # | feature | value | note |
|---|---|---|---|
| 1 | Model | adsorption dryer | a desiccant cartridge, point of use, not regenerating; ETIM's value list is not on file, and the class's synonyms on file (lib/standards/etim/classes.csv) name adsorption, membrane and refrigeration dryers |

Not claimed: a pressure dew point, a flow rate or an ISO 8573-1 water class. None is a feature of the class, and this element states
nothing beyond its class value (pneu.py D4's [7:4:4] is required at the bench regulator's outlet; this dryer does not claim it).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| head | 48 (x, along the flow) × 48 (y) × 32 (z), anodised aluminium, centred on the port axis in y and z | carries both ports on its end faces and the bowl underneath |
| port bores | Ø (E1 + h) × (L2 + 2) deep = Ø13.616 × 12.205, plain, blind, on the port axis, one in each end face | pneu.NPT (ASME B1.20.1 by its formulas): the male stub's own diameter (fitting-pushin 2.0, gauge-p) and its effective thread length plus a 2 run-out (tank 2.0's rule), so a placed male touches the bore and never cuts into the head; the thread is drawn plain. 23.6 of head between the two floors, 9.2 of wall above and below each bore (element.py asserts). Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it | the ISO 11727 number is a decal; 0.2 proud for GEO-050; 18 leaves a 2.19 ring round the bore (filter-air 2.0's size). The port pivot sits on the field's outer face |
| bowl | Ø44 × 110, clear polycarbonate, centred under the head (x = 24) | the desiccant's colour is seen through it |
| bowl cavity | Ø38, open to the head, 4 floor | 3 wall; declared in features.csv |
| desiccant cartridge | Ø32 × 96, hanging from the head inside the cavity, orange (dry) | node `desiccant`: the twin shows its state by its colour; clear of the bowl wall by 3 and of its floor by 10 |
| label field | 32 × 10, 0.2 proud, centred on the head's label face (−y) | "complexes.org generic" and "DRYER" decals |
| flow-arrow field | 24 × 8, 0.2 proud, centred on the head's top face | the arrow 1 → 2 |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply (inlet) | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727: 1 inlet) |
| `port-2` | NPT1/4 | female | work (outlet) | as above (ISO 11727: 2 outlet) |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002).

## Open figures
None. 1.0's one open figure (the NPT 1/4 thread, written while pneu.NPT was empty) is closed in 2.0 by pneu.NPT on file: each port
is bored at the male stub's own diameter and depth (Its own sizes), the thread drawn plain.

Not claimed: a pressure rating. The class has no pressure feature, and a generic element states no rating beyond its class values
(OPERATING.md 12), so there is no ratings.csv; in an assembly PNE-003 gives REVIEW (no rating to read) until a version states one.

## Named nodes
`port-1`, `port-2` (kind port, fixed; range 0) · `desiccant` (fixed: the cartridge, whose colour the twin sets, dry to saturated)

## Materials by layer
`M-ALU-ANOD` head · `M-CASE-CLEAR` bowl · `M-ORANGE-PA` desiccant cartridge · `M-WHITE-PA` fields

## Decals (Blender)
port numbers 1 and 2 on their fields (ISO 11727); the flow arrow 1 → 2 on the top field; "complexes.org generic" and "DRYER" on
the label field. No vendor names, no approval marks.

## Notes
- In line: it is carried by its pipework or fittings (fitting-pushin 2.0's NPT 1/4 stub fits either bore; the assembly places it). It has no mounting
  holes; a bracket is a later element. A bowl guard is not modelled.
- The cartridge's change (unscrewing the bowl) is not modelled as motion: the bowl is fixed to the head.
- Where it stands: after filter-air (it takes no liquid water) and before the regulator.

## Outputs (out/)
`dryer-air.lsp` · `.glb` (port and desiccant pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004030), cloud-pneu r3 2026-11-07 (the core chat's cloud builder, the PC being down): head, bores, fields, clear bowl, desiccant cartridge; stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r78 (unattended; review dryer-air-1.0.md finding 1): each port's bore Ø11.5 × 12 → Ø (E1 + h) × (L2 + 2) deep = Ø13.616 × 12.205 from pneu.NPT, its role in features.csv; port-number fields 16 → 18; each port pivot on its field's outer face (filter-air 3.0's fix); the thread line closed (pneu.NPT on file); nodes and envelope unchanged; no ratings.csv (the class states no pressure) |
