# separator-oil-water · v1.1 · oil-water separator for compressor condensate, generic, static (gravity and adsorption), vented tank, two NPT 1/4 inlets, NPT 3/8 water outlet

**What** a static oil-water separator for the condensate of a compressed-air plant. The drains (drain-auto on the receiver, the
dryer and the filters) blow their condensate through hoses into the two inlets on top of the steel expansion chamber, where its
pressure is let off to atmosphere and the oil mist settles. The condensate runs down into the vented settling tank: free oil rises
and runs over into the oil container hung on the tank's front; the water passes two adsorption filter cartridges (their screw caps
on the lid) and leaves by the clean-water outlet low on the right end, to the sewer. It stands on the floor beside the compressor.
lib/inventory.csv row `separator-oil-water` (own_design generic, "oil-water separator (condensate)"; 2 systems: compressor-station,
compressors-plant).
**Class** device · **Baseline** our own design: generic oil-/water separator static (ETIM 10.0 EC012068), as OPERATING.md 12
(generic elements, EM 2026-11-07) and the inventory row say. No vendor file was opened or measured. Its ports take their sizes from
the pneumatic contract (`toolkit/pneu.py` D1 and its NPT table, ASME B1.20.1 by its formulas); every other size is a design choice.
No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the tank's bottom face (the floor contact plane z = 0); length along x, width
along y. The inlets on the expansion chamber's top (−x half), the water outlet on the right end (+x), the oil container on the front
(−y).
**Built with** toolkit 1.3 · AutoLISP command `SEPARATOR-OIL-WATER` · no parameters.

The class: the inventory row names none. EC012068 "Oil-/water separator static" (group EG015140 Filters/separators, tier 2) is the
class lib/standards/etim/classes.csv gives for a separator that works by settling and adsorption with no pump or power (synonyms
"Oily water separator", "Oil filter (water separator)"); EC012200 "Oil-/water water separator dynamic" is the powered kind. A
compressor plant's condensate separator works by gravity and adsorption, so the static class fits the row's two systems.

## Class values (ETIM 10.0 EC012068)
Design inputs. EC012068 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (tier-1 classes and the
classes the inventory uses) does not list its 5 features: the case request pneu-4 raised for tube-pneu, which the core answered
(lib/requests/core/pneu-4-answer.md): the features come with an attended core session and EM's ETIM download, and the element is
built meanwhile with its design values under plain names (as tube-pneu 1.0 and pump-hand-hyd 1.0). When they are on main, a minor
version restates this table in ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| principle | static: pressure relief in the expansion chamber, gravity settling, adsorption filters; no pump, no power |
| medium | condensate of a compressed-air plant (water with compressor oil) |
| material | settling tank, lid and oil container polyethylene; expansion chamber steel; port bosses galvanised steel; filter caps polyamide |
| tank volume | about 73 l gross (`volume_l()`: 490 × 290 × 515 inside, 5 mm walls not modelled) |
| connections | two condensate inlets female NPT 1/4; one clean-water outlet female NPT 3/8 (Ports) |
| max. inlet pressure | not stated: a rating with no source on file (Open figures, class A); no p_max row in ratings.csv |
| compressor capacity served, residual oil content | not stated: no feature on file gives either, and no check reads them; no claim is made about the water discharged |

What the water may carry to the sewer is the local authority's rule, not on file here: the element claims no residual oil content,
and an assembly that discharges its water needs that rule first.

**No safety claim.** The expansion chamber lets the drains' pressure off to atmosphere; the element claims no pressure rating
(Open figures) and is not a pressure vessel. Nothing in it is a safety function.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| settling tank | 500 × 300 × 520 (x −250 to 250, y ±150, z 0 to 520); grey polyethylene | about 73 l for the condensate of a small plant's compressor, receiver, dryer and filters (compressor-station) |
| lid | 520 × 320 × 10, on the tank (z 519.5 to 530), 10 over each side | carries the expansion chamber and the filter caps; no face flush with the tank's |
| expansion chamber | Ø120, z 529.5 to 700, its axis at x = −150, y = 0; steel | takes the drains' blow-down and vents it; its edge 50 in from the lid's left end (40 from the tank's) |
| filter caps | 2 × Ø100 × 20 (z 529.5 to 550) at x = 20 and 160 | the two adsorption cartridges' screw caps (the cartridges inside not modelled); 60 from the chamber, 40 between them |
| inlet bosses | 2 × Ø24 × 16 proud of the chamber's top (z 699.5 to 716), at y = −30 and +30 | 36 between the bosses, room for two push-in fittings' hexes (fitting-pushin 2.0, 19.04 across corners); 18 in from the chamber's edge (30 + 12 = 42 from the axis of a Ø120 chamber; asserted ≥ 10); tall enough that each bore is blind in its own boss (the condensate's way on into the chamber not modelled) |
| inlet bores | Ø13.616 (E1 + h of NPT 1/4) × 12.205 deep (L2 + 2), blind in the boss, its floor 3.8 above the chamber's top | the thread drawn plain at the male stub's own diameter, so a placed male meets the bore face to face (tank 2.0's rule); deeper than a male's make-up (10.02); 5.19 of boss wall. Declared in features.csv |
| outlet boss | Ø28 × 6 proud of the right end face (x 249.5 to 256), its axis at z = 80, y = 0 | low, so the tank drains to it; its underside 66 above the floor, room for a fitting and a hose |
| outlet bore | Ø17.055 (E1 + h of NPT 3/8) × 12.358 deep (L2 + 2), through the boss into the tank | as the inlets; 5.47 of boss wall. Declared in features.csv |
| oil container | 160 × 80 × 220 (x 60 to 220, y −230 to −149.5, z 260 to 480), 0.5 into the tank's front face; white polyethylene | collects the oil that runs over; its top 39.5 under the lid's overhang, so it lifts off for emptying |
| label field | 160 × 120 (x −200 to −40, z 300 to 420), 0.2 proud of the front face | "complexes.org generic", "condensate in", "oil", "water out" decals |
| overall | envelope 520 × 390 × 716 (x −260 to 260, y −230 to 160, z 0 to 716) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-in-1` | NPT1/4 | female | none | the chamber's top boss face z = 716, x = −150, y = −30, axis +z | pneu.py D1 (NPT, ASME B1.20.1); NPT 1/4 so a push-in fitting (fitting-pushin) takes a drain's hose |
| `port-in-2` | NPT1/4 | female | none | as port-in-1, y = +30 | as above; a second drain without a tee |
| `port-out` | NPT3/8 | female | none | the right end's boss face x = 256, z = 80, axis +x | the liquid ports' size (tank, coolant-pump); clean water to the sewer |

A condensate port has no ISO 11727 number and no role in pneu.ROLES (supply, work, exhaust, ...): it carries liquid, as tank's and
drain-auto's `port-drain`. The ports are female and take sealant on the male (PNE-002).

## Open figures
- NOT ON FILE (A): the max. inlet pressure, the highest pressure a drain may blow into the expansion chamber. No feature of
  EC012068 is on file and no figure on file gives it; it is a rating, EM's. ratings.csv holds no p_max, so PNE-003 reports the
  inlets REVIEW in an assembly that pipes a drain to them.

## Named nodes
`port-in-1`, `port-in-2`, `port-out` (kind port, fixed; range 0). Nothing moves.

## Materials by layer
`M-GREY-PVC` settling tank and lid (the library's grey plastic; the design material is polyethylene) · `M-STEEL-7035` expansion
chamber · `M-GALV` port bosses · `M-BLACK-PA` filter caps · `M-WHITE-PVC` oil container · `M-WHITE-PA` label field

## Decals (Blender)
"complexes.org generic", "condensate in" by the inlets, "oil" on the container, "water out" by the outlet, on the label field. No
vendor names, no approval marks.

## Outputs (out/)
`separator-oil-water.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012068), pneu-r76 (unattended): settling tank, lid, expansion chamber with two female NPT 1/4 inlets, two filter caps, oil container, label field, female NPT 3/8 water outlet, each port bored at E1 + h × L2 + 2 from pneu.NPT; the max. inlet pressure left open (class A); the filters and the liquid inside not modelled; nothing placed |
| 1.1 | text, pneu-r81 (unattended; review pneu-r76 finding 2, separator-oil-water-1.0.md finding 1): Dimensions, the inlet bosses 18 in from the chamber's edge (not 10, the assert's floor) and the chamber's edge 50 in from the lid's left end, 40 from the tank's (not 60); element.py's comment the same; no geometry, node, origin or cut-out changed |
