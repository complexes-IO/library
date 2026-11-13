# drain-auto · v2.0 · generic automatic condensate drain, float type, female NPT inlet and drain

**What** an automatic condensate drain (a float drain) for compressed air. It hangs below the drain point of a receiver, a
filter's bowl or a dryer: condensate (water with a little oil) runs in through `port-1` on the head's top face and collects in the
bowl; a float inside opens the drain valve when the bowl fills and closes it again before air escapes, so the line keeps its
pressure. `port-drain` under the bowl discharges the condensate to a collector (an oil-water separator, in an assembly).
lib/inventory.csv row `drain-auto` (own_design generic; compressor-station, compressors-plant, dryers-air).
**Class** device · **Baseline** our own design: generic condensate separator (compressed air) (ETIM 10.0 EC004031, synonym
"Condensate trap (compressed air)"), as OPERATING.md 12 (generic elements, EM 2026-11-07) and lib/inventory.csv (own_design generic)
say. No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; its ports
take their thread from the standard on file (ASME B1.20.1, through toolkit/pneu.py) and the inlet its number from ISO 11727
(pneu.NODES). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the head's top face, which is `port-1`'s joint plane (where the drain hangs from
its vessel); the body hangs below z = 0. Ports follow pneu.py's port frame: the pivot on the joint plane, its axis toward the
counterpart.
**Built with** toolkit 1.3 · AutoLISP command `DRAIN-AUTO` · no parameters.

The class chosen: EC004031 (group EG020014 "Compressed air tools and accessories", domain fluid), not EC002009 "Condensate drain
(enclosure/cabinet)", which is a switchgear cabinet's drain (group EG000011 "Enclosures/cabinets"). The inventory row is on the
compressed-air line (compressor station, dryers), so EC004031 is the class it belongs to.

## Class values (ETIM 10.0 EC004031, lib/standards/etim/class-features.csv)
Design inputs, in ETIM's order. "not stated": the class feature has no value in this design.

| # | feature | value |
|---|---|---|
| 1 | EF000010 Model | automatic float drain, normally closed (the float opens it when the bowl fills) |
| 2 | EF014264 Max. compressor power | not stated (no capacity is designed to; the bowl holds about 0.11 l) |
| 3 | EF025498 Operating pressure | 0.5 to 10 bar (50 to 1000 kPa gauge, about 7 to 145 psig); the upper end is in ratings.csv as p_max, status "generic design" |
| 4 | EF020488 Air supply connection | female thread NPT 1/4 (ASME B1.20.1; pneu.py D1) on the head's top face, `port-1` |
| 5 | EF001438 Length | 50 mm (the head, along x) |
| 6 | EF000008 Width | 50 mm (the head, along y) |
| 7 | EF000040 Height | 130 mm (head 30, bowl 90, drain boss 10) |

Medium: condensate from compressed air (pneu.py D4: the air is to ISO 8573-1:2010 class [7:4:4] only at the bench regulator's
outlet, and a drain sits upstream of it, where the water is). The pressure range (class value 3) is a generic design value
(OPERATING.md 12), not a tested rating: 1000 kPa is above P_SUPPLY (689.5 kPa, 100 psig; pneu.py D3), so PNE-003 passes it on any
bench line. Its lower end (0.5 bar) is the pressure the float valve is designed to seal from; nothing checks it yet.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| head | 50 × 50 square, 30 high; anodised aluminium; `port-1` on its top face | holds the float valve's seat. 50 leaves at least 3 mm of metal round the NPT 1/4 pipe OD (13.7 mm, pneu.NPT); 30 is at least 2 more than a male's effective thread L2 (10.21) and its make-up depth L1 + L3 (10.02), both from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07): element.py asserts each |
| bowl | Ø46 × 90 under the head, 0.5 into it; anodised aluminium | the float chamber, about 0.11 l inside with 3 mm walls (walls not modelled); inside the head's square, asserted |
| drain boss | Ø20 × 10 under the bowl, 0.5 into it; bare brass; `port-drain` on its bottom face | at least 3 mm of metal round the NPT 1/8 pipe OD (10.3 mm, pneu.NPT), asserted; 10 is at least 2 more than the drain's make-up depth L1 + L3 (6.92), in the boss alone (asserted from 2.0, review finding 3) |
| port bores | `port-1`: Ø13.616 × 12.205 deep, blind in the head's top face; `port-drain`: Ø10.242 × 8.702 deep, blind in the boss's bottom face; both on the z axis | the thread drawn plain at the male stub's own diameter E1 + h, so a placed fitting-pushin 2.0 or gauge-p stub touches the bore and does not overlap the solid (tank 2.0's rule); depth L2 + 2, a run-out past the male's effective thread; both from pneu.NPT (ASME B1.20.1 by its formulas, EM 2026-11-07). Each bore is deeper than the make-up L1 + L3, blind inside its head (30) or boss (10), with at least 3 mm of metal round it: asserted. Roles in features.csv (HOLE-010) |
| overall | envelope 50 × 50 × 130 | |

The inlet is NPT 1/4, the size of the bench's FRL and gauge ports (pneu.py D3; next.md decision 1). The drain is NPT 1/8, one
size down in pneu.THREADS: condensate flow is small, and a smaller outlet takes the tube to the collector. How the inlet meets its
vessel is open (Open figures): every drain point on file is female, as `port-1` is, so the two need a male-male nipple between
them, and no such part is on file.

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | the head's top face z = 0, axis +z | inlet; ISO 11727 number 1 (the side under supply pressure) as pneu.NODES; pneu.py D1 (NPT, ASME B1.20.1) |
| `port-drain` | NPT1/8 | female | none | the drain boss's bottom face z = −130, axis −z | condensate outlet; named, not numbered, as tank's `port-drain`: ISO 11727's numbers (pneu.NODES) name air ports, and this one carries water and oil; it takes no pneu.ROLES role (it is not an air exhaust, so no silencer goes on it) |

PNE-002 pairs each with a male NPT of the same size (sealant on the male, D1). Each face is the joint plane a placed fitting
meets; from 2.0 the port bore behind it takes the male's stub (Dimensions, port bores). Cutting them changed the cut-outs, so 2.0
is a major version, as for tank and check-valve.

## Open figures
| class | figure | why open |
|---|---|---|
| B | NOT ON FILE (B): the nipple between the vessel's drain point and `port-1` | a fit (OPERATING.md 6, class B, EM's). Every drain point on file is female (tank 2.0's `port-drain` NPT 3/8; receiver-air is not built) and so is `port-1`, so the drain hangs from a male-male nipple (a reducing one under tank). A pipe nipple is a part a dimensional standard shapes (OPERATING.md 12: never generic), and none is on file. Review drain-auto-1.0.md finding 2's other choice, a male NPT 1/4 stub for `port-1`, is a major that changes the node's gender; it is left to EM (lib/needs-em/pneu.md). The hosts (filter-air, dryer-air, receiver-air) also need a drain port before drain-auto can be placed |

Every other figure is a design choice, a class value above, or from the standards on file.

## Named nodes
`port-1` (the head), `port-drain` (the drain boss); kind port, fixed (range 0). The float and its valve are inside and not modelled:
nothing moves outside the body.

## Materials by layer
`M-ALU-ANOD` head and bowl · `M-BRASS` drain boss

## Decals (Blender)
None in 1.0 (a flow arrow and the "generic" label on the head are a later version). No vendor names.

## Outputs (out/)
`drain-auto.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004031), pneu-r53 (unattended): square head with the female NPT 1/4 inlet `port-1` on top, round bowl, brass drain boss with the female NPT 1/8 `port-drain` below; port bores, float and valve not modelled |
| 2.0 | pneu-r60 (unattended), review drain-auto-1.0.md findings 1 to 3: a blind port bore in the head and in the drain boss, Ø E1 + h × L2 + 2 from pneu.NPT (13.616 × 12.205 at NPT 1/4, 10.242 × 8.702 at NPT 1/8), roles in features.csv; the fit to the vessel (a nipple) is now an open class B line; the boss's make-up assert reads the boss alone |
