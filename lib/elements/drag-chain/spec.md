# drag-chain · v2.0 · cable guide chain, generic, inner 50 x 25, bending radius 100, 24 links, travel 1000, 2 x M6 at each end

**What** A cable guide chain (a cable carrier, an energy chain): it carries the cables and hoses of a moving axis (a gantry's
carriage, a cutting head, a servo axis) so they bend in one plane at a fixed radius and never drag or kink. Closed tube links,
the cables threaded through them, lie on the machine's mounting surface from the fixed end, turn up through a bend of radius 100
and run back over themselves to the moving end, which bolts under the axis's carriage. lib/machines-factory.txt and
lib/machines-from-elements.txt list it in five systems (gantry-xyz, laser-cutter-fiber, plasma-cutter-cnc, servo-axis-bench,
servo-pick-and-place). The moving end is the mechanism: the twin moves it by name.
**Class** run · **Baseline** our own design: generic cable guide chain (ETIM 10.0 EC002414), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07); lib/inventory.csv marks the row own_design "generic" with etim EC002414 (request mech-13's answer, 2026-11-12:
its 14 features are on file; "links as one bent run with the moving end a node" a design choice). No product was matched and no
vendor file was opened. The folder held a catalogue search record from 2026-11-02 (another maker's open lay-in carrier), moved to
references/source.txt by `build.py own` (DOC-007); no size is taken from it. The class values below are the design inputs; the
holes it meets are on file (ISO 273); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the mounting surface (z = 0) under the fixed end, x = 0 at the fixed end's link face (its
bracket's upright at x 0 to 3), y = 0 on the chain's centre plane. The moving end travels along +x from x −500 to +500 (the fixed end
at the travel's middle); the bend lies toward −x. Drawn at the travel's start: the moving end at x −500, next to the bend, one link
in the upper run. Extents x −667.5 to 40, y ±45, z 0 to 235.
**Built with** toolkit 1.3 · AutoLISP command `DRAGCHAIN` · no parameters.

## Class values
ETIM 10.0 class EC002414 Cable guide chain (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | polyamide (plastic; the grade not stated), layer M-BLACK-PA; the end brackets zinc-plated steel |
| 2 | Inner width (EF006466) | 50 mm |
| 3 | Inner height (EF006588) | 25 mm, through the straight links and the bend alike (the bend's ways, Its own sizes) |
| 4 | Outer width (EF008488) | 66 mm (side walls 8) |
| 5 | Outer height (EF008489) | 35 mm (top and bottom walls 5) |
| 6 | Bending radius (EF023114) | 100 mm, to the chain's centre line (the bend's inner face at r 82.5, its outer at r 117.5) |
| 7 | Max. cantilever length (EF008490) | not stated: no calculation or test of the links' stiffness is on file, and none is claimed |
| 8 | Multi-axial motion (EF008491) | no: the chain bends in one plane (x–z) only |
| 9 | With connection set (EF008324) | yes: a fixed end bracket and a moving end bracket, each with 2 × M6 holes |
| 10 | With partition panel (EF007973) | no |
| 11 | With strain relief (EF000878) | no: the cables' clamps or ties at the ends are the assembly's |
| 12 | Number of links (EF008493) | 24: 12 straight (as drawn, 11 in the lower run and 1 in the upper) and 12 in the bend |
| 13 | Length (EF001438) | 0.914 m on the centre line (2 × 300 straight + π × 100 in the bend), computed in element.py |
| 14 | Opening principle (EF008494) | not openable: closed tube links, the cables threaded through from an end |

## What it meets
| figure | value | source |
|---|---|---|
| fixed end mounting holes | 2 × M6, Ø6.6 through the foot plate at x 25, y ±30 (60 pitch) | ISO 273 medium (H13), lib/standards/holes.csv. M6 is this design's choice; the screws and the surface's tapped holes are the assembly's |
| moving end mounting holes | 2 × M6, Ø6.6 through the top plate at x −475 (25 from its link face, at the travel's start), y ±30, its top face at z 235 under the carriage | ISO 273 medium (H13), lib/standards/holes.csv; the same design choice; the carriage's screws are the assembly's |
| the mounting surface | the foot plate's and the lower run's undersides, z = 0 | ISO 273's screws hold the foot plate; the surface (a machine bed, a trough) is the assembly's |
| the cables and hoses | inside 50 × 25 through every link | cables.csv (lib/standards/) sizes the cables a machine threads; which cables, their fill and their own minimum bending radius (100 or less to suit this chain) are the assembly's |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
Each bracket's two holes carry a declared position tolerance Ø0.6 at MMC to A (the plate's mounting face: the foot plate's
underside, z 0, or the top plate's top, z 235), B (the chain's centre plane y = 0) and C (the fixed end's link face, x = 0)
(features.csv; T ≤ H − F = 6.6 − 6 = 0.6).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| straight links | 12, each 50 long (x), 66 × 35 outside, a 50 × 25 way through each; as drawn the lower run 11 links x −550 to 0, z 0 to 35, the upper run 1 link x −550 to −500, z 200 to 235 | one tube per link, face to face along the run; drawn as plain tubes (the links' pins, side-plate overlaps and stops are not drawn: appearance) |
| bend | 12 links of 15 degrees about the centre (−550, 117.5) on the y axis, each 30.67 long at its outer face (2 × 117.5 × sin 7.5°, its outer corners on the arc r 117.5), 33.99 deep from r 82.5 (117.5 × cos 7.5° − 82.5), 66 wide; a 50 wide way through each from 86.0 to 112.5 normal to its faces (walls 3.5 inner, 4.0 outer at mid-link) | a polygon of links: neighbours share their outer corners and overlap on the inside, as real links' stops hold a bend at its radius. The ways keep the annulus r 87.5 to 112.5 (the straight runs' 25 high way turned about the centre) clear through the whole bend and across its joints with the runs: a point of a link's inner wall lies at most √(86.0² + 15.34²) = 87.36 from the centre, its outer wall at 112.5 or more, so neither the link nor an overlapping neighbour narrows the way (element.py asserts it). 1.0's 6 links of 30 degrees narrowed it to 21 (review mech-r112 finding 2) |
| travel | 1000: the moving end from x −500 to +500, the fixed end at the travel's middle | 600 of straight links = half the travel + two links, so one link stays straight in the upper run at the start (the bend at x −550) and one in the lower run at the end (the bend at x −50) |
| fixed end bracket | foot plate 40 (x 0 to 40) × 90 (y ±45) × 3, upright 3 (x 0 to 3) × 66 × 32 (z 3 to 35) on the lower run's end face, a window 50 (y ±25) × 25 (z 5 to 30) through it | zinc-plated steel; screws down beside the chain. The window is the way's own section, so the cables leave the lower run over the foot plate (2.0, review mech-r112 finding 1: 1.0's solid upright closed the way); 8 of upright each side, 2 below and 5 above it |
| moving end bracket | at the travel's start: upright 3 (x −500 to −497) × 66 × 32 (z 200 to 232) on the upper run's end face, a window 50 × 25 (z 205 to 230) through it, top plate 40 (x −500 to −460) × 90 × 3 (z 232 to 235) | the same bracket upside down, under the carriage; the cables leave the upper run through the window under the top plate; 8 of upright each side, 5 below and 2 above it |
| load, cantilever length, speed, acceleration, fill | not claimed | no figure for them is on file and the links are not sized against one |

## Mechanism
One moving node, `moving-end` (the moving end bracket: its upright and top plate), translating along +x through (−500, 0, 235),
range 0 to 1000 mm (x −500 to +500): the axis's carriage carries it. The links are one fixed run drawn at the travel's start (0);
they do not follow the node. In a real chain the bend rolls half the carriage's travel (from x −550 at the start to −50 at the end)
and links pass from the lower run into the upper; that rolling is not modelled (motion the twin doesn't read: the cables' route,
appearance). Through its range the bracket only moves away from the upper run's end face over the lower run (z 200 to 235 against
the lower run's 0 to 35), so it touches nothing; MOT-010 sweeps it. (A first build drawn at mid-travel with the range −500 to +500
had the bracket's upright entering the drawn upper run toward −x: MOT-010 FAIL, fixed by this pose at the same version.)
behaviour.csv: state `parked` (default) and `travelling` (manual toggle: the assembly's axis), pose of `moving-end` at the range end
in `travelling`.

## Named nodes
`moving-end`: translate along +x through (−500, 0, 235), range 0 to 1000 mm. Colliders: `run-lower`, `run-upper`, `bend`,
`mount-fixed` (none is named like the node; the moving bracket takes no collider, it moves).

## Materials by layer
`M-BLACK-PA` the links (polyamide) · `M-ZINC` both end brackets (zinc-plated steel).

## Decals (Blender)
"complexes.org generic" on the side of the lower run's middle link.

## Notes
No vendor names, part numbers or marks. No load, cantilever, speed or life figure and no safety claim: the class values are the
figures this design is meant to meet; no calculation or test of the model is on file. Not drawn: the links' pins and stops, the
cables, their clamps or ties, a guide trough. A longer travel is another Length and Number of links, a parameter of a later
version. A cable guide chain is not a part a dimensional standard shapes (no ISO or DIN sheet for it is on file), so it is built
generic to its ETIM class (OPERATING.md 12).

## Outputs (out/)
`drag-chain.lsp` · `.glb` (pivot on `moving-end`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002414), our own design (mech-r112, unattended, 2026-11-12) |
| 2.0 | review mech-r112 findings 1 and 2: a 50 × 25 window (the way's section) through each end bracket's upright, so the cables leave at both ends; the bend as 12 links of 15 degrees with ways 86.0 to 112.5, so the 25 high way runs clear through it (1.0: 6 links, a 21 high way). Cut-outs and links changed: a major. Nodes, origin, extents unchanged (mech-r128, unattended, 2026-11-12) |
