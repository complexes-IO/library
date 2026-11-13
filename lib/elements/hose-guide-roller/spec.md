# hose-guide-roller · v1.0 · generic hose guide roller, flanged polyamide spool on a zinc-plated steel U-bracket, for hose to Ø25, two M6 holes

**What** a hose guide roller: a flanged spool roller turning between the two cheeks of a U-bracket that is screwed down on a
machine's frame. Where an air or coolant hose turns over an edge, or runs out to a moving part, the hose lies in the spool's channel
and rolls over it instead of rubbing on the edge; the two flanges keep it on the roller. Its use in the lane: under hose-flex-npt,
tube-pneu in sleeve-braid, or a coolant hose where the run turns. The roller turns about x; the hose runs over it along y.
**Class** device · **Baseline** our own design: generic hose guide (ETIM 10.0 EC010745, synonym "Hose guide roller"), as OPERATING.md
12 (generic elements, EM 2026-11-07) says: the next ETIM class in generic.next_classes' order that builds, after EC004090
(hose-flex-npt, pneu-r118) and the three Hoses classes passed over (lib/rounds/pneu/r119.md section 2). No vendor file was opened or
measured. The class values below are its design inputs; its sizes are design choices or from a standard on file (the mounting
holes); no vendor names; "generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. The lane knows of no
standard that fixes a hose guide's bracket, roller or channel; the only interface it meets is the screw that holds it down, whose
clearance hole ISO 273 gives (lib/standards/holes.csv).
**Units / frame** mm, Z up. Origin: the centre of the bracket's underside (the mounting face, z = 0); the roller's axis along x at
z = 35; the hose runs over the roller along y.
**Built with** toolkit 1.3 · AutoLISP command `HOSE-GUIDE-ROLLER` · no parameters.

## Class values (ETIM 10.0 EC010745)
Design inputs. EC010745 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its two features (the pneu-4 answer's case, tube-pneu 1.0's and sleeve-braid 1.0's way).
Until they are on file this table gives the values this guide is designed to under plain names; a later minor restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| form | single flanged roller between two cheeks of a U-bracket, base-mounted |
| largest hose outside diameter | 25 mm (the channel: 30 wide between the flanges, the flanges 10 above the hub) |
| roller material | polyamide (PA), grey |
| bracket material | steel, zinc plated |
| mounting | two M6 screws through the base, 70 apart (holes ISO 273 medium) |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv: the guide holds no pressure (the hose over it does), and no check reads a figure
of it. Its load (the hose's pull) is not claimed either.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| base plate | 90 × 50 × 6, centred on the origin in plan | design choice: room for the cheeks and a screw at each end |
| mounting holes | 2 × Ø6.6 through, at x = ±35, y = 0 | M6 clearance, medium (ISO 273 H13, lib/standards/holes.csv: 6.6 to 6.82); position Ø0.6 to A B C (features.csv: floating fastener T = H − F); 6.7 of plate to the base's end and to the cheek (room for an M6 head) |
| cheeks | 2 × 5 thick, 40 deep (y), from the base's top (z = 6) to z = 50; inner faces at x = ±20 | design choice: 10 of steel above each axle bore and 15 beside it (asserted) |
| axle bores | Ø10 through each cheek on the roller's axis (y = 0, z = 35) | design choice: a plain bore the roller's axle stub turns in, face to face |
| roller axis | z = 35 above the mounting face | design choice: 4 between the flanges and the base plate (asserted) |
| hub | Ø30 × 30 (x = −15 to 15) | design choice: the channel's floor; its width takes a hose to Ø25 |
| flanges | 2 × Ø50 × 4 (x = ±15 to ±19) | design choice: they rise 10 above the hub, over a third of the largest hose's Ø (asserted); 1 of running clearance to each cheek |
| axle stubs | 2 × Ø10, from each flange's outer face (x = ±19) to the cheek's outer face (x = ±25) | design choice: they turn with the roller in the cheeks' bores and end flush with the cheeks |
| envelope | 90 (x) × 50 (y) × 60 (z) | the base's plan; the flanges' top at z = 60 |

## Ports (toolkit/pneu.py)
None. The guide carries no fluid: the hose over it keeps its own ends and ports.

## Open figures
None. Every figure is a class value or a design choice above, or from a standard on file (the clearance holes, ISO 273).

## Named nodes
| node | kind | axis | range | what |
|---|---|---|---|---|
| `roller` | rotate | +x, through (0, 0, 35) | 0 to 360° | the hub, both flanges and both axle stubs turn as one in the cheeks' bores; turned by the hose drawn over it |

## Materials by layer
`M-ZINC` the bracket (base and cheeks, zinc-plated steel) · `M-GREY-PA` the roller's hub and flanges (polyamide; not M-BLACK-PA or
M-WHITE-PA, the Blender gate's printed materials, pneu-r113) · `M-SILVER` the axle stubs (bright steel)

## Decals (Blender)
None in 1.0. No vendor names.

## Outputs (out/)
`hose-guide-roller.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010745), pneu-r119 (unattended): a flanged spool roller on Ø10 axle stubs in a U-bracket's cheeks, the `roller` node rotating about +x; two M6 clearance holes (ISO 273 medium); no port, no ratings |
