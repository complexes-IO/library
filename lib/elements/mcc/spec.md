# mcc · v2.0 · motor control centre section, generic, 600 × 500 × 2300, four bucket doors, vertical wireway, horizontal and vertical bus, PE bar (complexes.org generic)

**What** One vertical section of a motor control centre: a floor-standing sheet-steel section that holds a machine's motor starters, disconnects and drives in plug-in buckets, fed by a horizontal bus along its top and a vertical bus behind the buckets. On the left the unit space, four bucket spaces behind four doors (three of one module, the lowest of two modules for a drive); on the right a vertical wireway behind its own door, where the load cables run down to the pull space; at the top the horizontal bus compartment behind a fixed cover; at the bottom the pull space behind a fixed cover. Behind the buckets an insulating barrier with a row of three stab openings per bucket space; behind it the three vertical phase bars, each rising to its own horizontal phase bar; a protective (PE) bar along the bottom of the back. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000712, built to the class values below; no maker's datasheet and no product is matched. Inventory row mcc, pinned 4 (EM 2026-11-08: "our own generic design of the section (bus, bucket openings, door) holding the starters, MCCBs and VFDs on file").
**Class** enclosure · **Baseline** our own design: generic Empty enclosure for switchgear (ETIM 10.0 EC000712). The class values are this element's definition (design inputs); every size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md). No vendor file was opened: the folder held an acquisition stub (metadata.json, references/source.txt) whose section sizes the inventory row marks as reference only; it was not read. Its record is kept verbatim as the end block of references/source.txt, under this element's own (since 2.0; OPERATING.md 6), and nothing in this element is taken from it.
**Units / frame** mm, Z up. Origin: floor plane z = 0 at the section's front-left corner x = 0, y = 0 (the body's front face; the doors, covers and knobs stand in front of it, y < 0); the back face y = 500 toward the wall; the next section stands against x = 600.
**Built with** toolkit 1.3 · AutoLISP command `MCC` · no parameters (the doors are built closed; their pivots carry the swing).

## Class values
ETIM 10.0 EC000712 "Empty enclosure for switchgear", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Housing material (EF001596) | sheet steel (body, doors, covers 2.0; plinth 3.0), RAL 7035; galvanised steel shelves, partition and compartment floor; insulating barrier and bus supports |
| 2 | Width (EF000008) | 600 mm |
| 3 | Height (EF000040) | 2300 mm (the plinth's 100 included) |
| 4 | Depth (EF000049) | 500 mm (the body; 518 with the doors and their latch knobs) |
| 5 | With transparent cover (EF001094) | no |
| 6 | Suitable for emergency stop (EF001433) | no |
| 7 | Model (EF000010) | floor-standing section, front access, one unit column and one vertical wireway |
| 8 | Degree of protection (IP) (EF005474) | not stated: the doors have no seal in this version |
| 9 | Degree of protection (NEMA) (EF011959) | not stated |

These values are what the element claims: no rating, certification or approval mark. The class has no electrical feature, so there is no ratings.csv: the bus is modelled as copper with no current, short-circuit or voltage rating claimed (Notes).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 600 × 500 × 2200 (z 100 … 2300), 2.0 sheet: bottom and top full, the sides between them, the back between the sides | one unit column of 400 and a wireway of 200 side by side |
| splice openings | in each side sheet (x 0 … 2 and 598 … 600), two: one for the three phase bars, y 330 … 420, z 2090 … 2260; one for the PE bar, y 476 … 496, z 140 … 200; each 10 clear round the bar ends it serves | a splice plate passes from this section's bar end through the openings of both side sheets to the next section's bar, reached from the bus compartment (phases) or the pull space (PE) with the fixed cover off (since 2.0) |
| plinth | four 3.0 plates round the footprint, 100 high (z 0 … 100) | lifts the section's floor off the floor plane for the cables entering below |
| zones (z) | pull space 100 … 300; unit space 300 … 2000 (five modules of 340); horizontal bus compartment 2000 … 2300 | |
| unit space | x 2 … 398, y 0 … 300 (the bucket depth); shelves 2.0 galvanised at z 300, 980, 1320, 1660 (each door's bottom line); bucket spaces of 340, 340, 340 and 680 high (top to bottom) | a starter bucket in one module; the lowest space two modules for a drive (vfd-0.75kw is 72 × 144 × 140 on the rail) |
| partition | x 398 … 400, y 0 … 300, z 300 … 2000, galvanised | separates the buckets from the wireway |
| bus compartment floor | x 2 … 598, y 0 … 300, z 2000 … 2002, galvanised | the line above the doors |
| barrier | insulating, x 2 … 400, y 300 … 303, z 302 … 2000; stab openings 20 × 40 at x 110 … 130, 190 … 210, 270 … 290, one row per bucket space at its mid-height (z 640, 1150, 1490, 1830) | the bars are reached only through the openings a bucket's stabs enter |
| doors | 2.0 leaves over the front edges (y −2 … 0); bucket doors x 0 … 397 hinged at x = 0: `door-1` z 1662 … 1998, `door-2` 1322 … 1658, `door-3` 982 … 1318, `door-4` 302 … 978; wireway door `door-ww` x 401 … 600, z 302 … 1998, hinged at x = 600; the hinge edges flush with the body's sides (x 0 and 600), 4 clear between two doors and between a door and a cover (2 from each module line), 4 between the bucket doors' free edge and the wireway door | |
| latch knobs | 24 × 16 × 60 (x, y, z), one per door, 25 in from its free edge, at its mid-height, y −18 … −2 | a quarter-turn latch's knob; the latch itself is not modelled. Its edges are 8 or more, for the AutoCAD gate's fillet pre-flight (term-jumper 1.0's lesson) |
| covers | pull space x 0 … 600, z 100 … 298; bus compartment x 0 … 600, z 2002 … 2300; both 2.0 at y −2 … 0, fixed | bolted covers; the bolts are not modelled |
| vertical phase bars | 30 × 10 copper, L1 at x 105 … 135 / y 340 … 350, L2 at x 185 … 215 / y 370 … 380, L3 at x 265 … 295 / y 400 … 410, from z 320 up to their own horizontal bar | each phase at its own depth, so no bar crosses another's |
| horizontal phase bars | 30 × 10 copper (z × y), x 20 … 580: L1 z 2100 … 2130 at y 340 … 350, L2 z 2160 … 2190 at y 370 … 380, L3 z 2220 … 2250 at y 400 … 410 | each vertical bar's top face is its horizontal bar's bottom face |
| bus supports | insulating blocks from each bar's back face to the back sheet (y 498): three per vertical bar (40 high at z 600, 1200, 1800), two per horizontal bar (x 30 … 60 and 540 … 570) | |
| PE bar | 6 × 40 copper, x 20 … 580, y 486 … 492, z 150 … 190, on two steel brackets (x 30 … 60, 540 … 570) to the back sheet | along the bottom of the back, where the cables' protective conductors land |

Buckets (their slide-in frames, stabs, doors' operators) and the devices in them are not part of this element: disc-3p-30a, contactor and overload, vfd-0.75kw are elements on file that a bucket or an assembly places; a moulded-case breaker (the inventory's mccb) is not built. The splice plates to a next section and the incoming cable lugs are not modelled: a splice is bolted to the bar ends' faces through the splice openings (a placed part, later), and a first section's incoming cables land on its bars' right ends the same way, from the bus compartment.

## Mechanism
`door-1` … `door-4`: rotate about the vertical line x = 0, y = 0 (their hinge edge), 0 to −110° about +z, so the free edge swings outward (−y). `door-ww`: about x = 600, y = 0, 0 to +110°, also outward. Closed, each leaf lies over the front edges; through its travel it stays at y ≤ 0 or outside x 0 … 600, clear of the body and of the other doors (they are separated in z). Each knob rides on its door's node. The hinges and latches are not modelled. Every other part is fixed.

## Named nodes
`door-1`, `door-2`, `door-3`, `door-4`, `door-ww` (rotate) · ports `bus-l1`, `bus-l2`, `bus-l3` (kind port, unit bus, gender none: a bolted bar end, PIN-002) and `pe-bus` (kind port, unit PE, gender none), each the whole bar, its port face at the bar's right end (x 580, facing +x, 18 inside the right side sheet's splice opening; the next section stands against x = 600). Until 1.x the port faces were at the left ends (x 20, facing −x) against the closed side sheet, where no joint could be made (review mcc-1.0 finding 1): moved in 2.0, a major (the nodes' port points move; names unchanged). Colliders `body` (the section) and one per door with its knob.

## Materials by layer
`M-STEEL-7035` body, plinth, covers, doors, PE bar brackets · `M-GALV` shelves, partition, compartment floor · `M-GREY-PA` barrier and bus supports · `M-CU` phase bars and PE bar · `M-BLACK-PA` latch knobs

## Decals (Blender)
On the bus compartment cover: "complexes.org generic", "mcc". Bucket numbers 1 to 4 on the doors. A warning label is a later version's (its wording is a standard's, not chosen here). No maker's name, logo or approval mark.

## Notes
- No rating is claimed: the class has no electrical feature, and a section's bus ratings (continuous current, short-circuit withstand) and its clearances are properties a standard verifies by test or design rule (IEC 61439-1 / -2; UL 845), neither in lib/standards/sources.csv. The bar sections and spacings are design choices for the model's shape, not a rated design; an assembly that feeds this section takes its ratings from a verified design, not from this element.
- The four bus port nodes give the twin a place to probe the bus and an assembly a place to land its incoming conductors; behaviour.csv lists them with their torque `not claimed` (the lug or splice bolt is not part of this element, lib/behaviour.md pin).
- Not a safety-function device; no emergency-stop function (class value 6).

## Outputs (out/)
`mcc.lsp` · `.glb` (pivots on the five doors and the four bus ports, `body-colonly` and the doors' colliders) · `preview-*.png`. Gates (AutoCAD, Blender, Godot): run on the PC at this version (lane round elec-r49; 1.0's in elec-r36).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000712), our own design (elec-r36, unattended, 2026-11-12): the inventory row pinned 4; the folder's acquisition stub replaced, unread |
| 2.0 | review mcc-1.0 finding 1 (elec-r49, unattended, 2026-11-13): the four bus port nodes moved to the bars' right ends (x 580, facing +x) and a splice opening for the phase bars and one for the PE bar cut in each side sheet, so a splice to the next section can be made (a major: the port points move; node names, origin, zones, bars and doors as 1.0); finding 2: the stub's record kept verbatim as references/source.txt's end block; note 2: the doors row's clearances as built |
