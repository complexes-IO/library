# filter-air · v3.0 · compressed air filter, generic, 5 µm, NPT 1/4 in line, clear bowl, manual drain

**What** a general-purpose compressed air filter for a bench drop or a machine's air supply: air enters at port-1, passes a 5 µm
sintered element in a clear bowl, and leaves at port-2; water and particles collect in the bowl and leave by a manual
quarter-turn drain. It is our own vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements, EM
2026-11-07): the class values it is designed to are listed under Class values. No maker's datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic compressed air filter (ETIM 10.0 EC004033). What it meets takes its
figures from the pneumatic contract, `toolkit/pneu.py` (D1 threads, D7 names), or is left open (Open figures); every size the
contract and the standards on file don't fix is a design choice (below).
**Units / frame** mm, Z up. Origin: port-1's face centre, in line: the port axis is the x axis, flow along +x, the bowl hangs
toward −z, the label face toward −y. Ports follow pneu.py's port frame: the pivot on the joint plane (3.0: the number field's
outer face, 0.2 in front of the head's end face), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `FILTER-AIR` · no parameters.

## Class values
ETIM 10.0 EC004033 "Compressed air filter" (group EG020014), every feature in ETIM's order (lib/standards/etim/class-features.csv).
These are the values this element is designed to: they define it as a member of the class, and they are design inputs.

| # | feature | value | note |
|---|---|---|---|
| 1 | Max. flow rate | 1000 l/min | at 6.3 bar inlet pressure and 0.5 bar pressure drop |
| 2 | Thread size inner thread (inch) | 1/4 | NPT 1/4 female, both ports (pneu.py D1, ASME B1.20.1); bored plain at E1 + h from pneu.NPT (Ports) |
| 3 | Depositional particle size | 5 µm | the sintered element's rating |
| 4 | Residual oil aerosol content | not stated | a particulate filter: it claims no oil removal (no coalescing stage) |
| 5 | Residual oil vapor content | not stated | no activated-carbon stage |
| 6 | Diameter | 36 mm | the bowl |
| 7 | Height | 100 mm | head top to the drain's underside: 32 head + 60 bowl + 8 drain |

The 5 µm rating is an element rating, not an ISO 8573-1 purity class: this element does not claim the [7:4:4] that pneu.py D4
requires at the bench regulator's outlet.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| head | 40 (x, along the flow) × 40 (y) × 32 (z), anodised aluminium, centred on the port axis in y and z | carries both ports on its end faces and the bowl underneath |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, on the port axis, one in each end face (2.0) | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0, gauge-p), so a placed male meets the bore face to face (tank 2.0's rule, review pneu-r48 finding 1); deeper than a male's make-up L1 + L3 (10.02); 15.6 of head between the two floors, 9.2 of wall round each (element.py asserts both). Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it (2.0: 16 → 18, a ring round the wider bore); the port's pivot on its outer face (3.0) | the ISO 11727 number is a decal; 0.2 proud for GEO-050. The field's outer face is the joint plane: a placed male's hex (fitting-pushin 2.0's AF 17) meets it face to face, where with the pivot on the head's face (1.0, 2.0) it stood 0.2 into the field's ring (review pneu-r58 finding 1, GEO-020's threshold) |
| bowl | Ø36 × 60, clear polycarbonate, centred under the head (x = 20) | the condensate is seen; class value "Diameter" |
| bowl cavity | Ø30, open to the head, 4 floor | 3 wall; declared in features.csv |
| filter element | Ø16 × 40, sintered bronze, hanging from the head inside the cavity | the 5 µm stage; clear of the bowl wall by 7 |
| drain | Ø12 × 8 knob under the bowl, quarter turn closed to open | manual drain |
| label field | 28 × 10, 0.2 proud, centred on the head's label face (−y) | "complexes.org generic" and "5 µm" decals |
| flow-arrow field | 24 × 8, 0.2 proud, centred on the head's top face | the arrow 1 → 2 |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply (inlet) | x = −0.2 (its field's outer face), axis −x | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727: 1 inlet) |
| `port-2` | NPT1/4 | female | work (outlet) | x = 40.2 (its field's outer face), axis +x | as above (ISO 11727: 2 outlet) |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002). Thread: NPT (ASME
B1.20.1); pneu.NPT holds NPT 1/4's figures as values calculated from its formulas (EM 2026-11-07): E1 + h = 13.616 (the bore), L2 =
10.205 (the bore is L2 + 2 deep), L1 + L3 = 10.02 (a male's make-up). The helix is not modelled: the bore is the thread drawn plain.

## Open figures
None. 1.0's one open figure (the NPT 1/4 thread, while pneu.NPT was empty) is closed in 2.0 by pneu.NPT on file.

Not claimed: a pressure rating. The class has no pressure feature, and an own design states no rating of its own beyond its class
values (OPERATING.md 12), so there is no ratings.csv; in an assembly PNE-003 gives REVIEW (rating not on file) until one is.

## Named nodes
`port-1`, `port-2` (kind port, fixed; range 0) · `drain` (rotate about −z at the bowl's underside, 0 to 90°: closed to open)

## Materials by layer
`M-ALU-ANOD` head · `M-CASE-CLEAR` bowl · `M-BRASS` filter element (sintered bronze) · `M-BLACK-PA` drain · `M-WHITE-PA` fields

## Decals (Blender)
port numbers 1 and 2 on their fields (ISO 11727); the flow arrow 1 → 2 on the top field; "complexes.org generic" and "5 µm" on
the label field. No vendor names, no approval marks.

## Notes
In line: it is carried by its pipework or fittings (fitting-pushin, not built yet, is placed by the assembly). It has no mounting
holes; a bracket is a later element. A bowl guard is not modelled.

## Outputs (out/)
`filter-air.lsp` · `.glb` (port and drain pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004033), cloud-pneu 2026-11-07 (the core chat's cloud builder, the PC being down): head, bores, bowl, element, drain, fields; stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r58 (unattended): each port's bore Ø11.5 × 12 → Ø13.616 (E1 + h) × 12.205 (L2 + 2) from pneu.NPT, its role in features.csv; port-number fields 16 → 18; the thread line closed (pneu.NPT on file); nodes and origin unchanged |
| 3.0 | pneu-r67 (unattended): review pneu-r58 finding 1 (filter-air-2.0.md finding 1): each port's pivot moved 0.2 out, from the head's end face to its number field's outer face (x −0.2 and 40.2), so a placed male's hex meets the field face to face; behaviour.csv added (BEH-010); nodes, origin, bores and envelope unchanged |
