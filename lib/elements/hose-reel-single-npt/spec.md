# hose-reel-single-npt · v1.0 · generic hose reel, single hose, hand crank, galvanised drum on a red steel stand, female NPT 3/8 swivel inlet, four M10 holes

**What** a hose reel for one hose: a galvanised drum with two flanges, turning on Ø25 axle stubs in the plain bores of two side frames
that stand on a base plate screwed to the floor (or a wall). A crank on the drum's +x end winds the hose in; drawing the hose off turns
the drum the other way. On the -x end a brass swivel boss, fixed to the frame on the drum's axis, takes the supply line in a female
NPT 3/8 inlet while the drum turns: the air goes through the swivel into the hose wound on the drum. Its use in the lane: a bench or
machine air drop, with hose-flex-npt or tube-pneu as the hose. The drum turns about x; the hose pays out along y.
**Class** device · **Baseline** our own design: generic hose reel, single hose (ETIM 10.0 EC010439, synonyms "Hose car", "Hose
wagon"), as OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next ETIM class in generic.next_classes' order that builds,
after EC010745 (hose-guide-roller, pneu-r119) (lib/rounds/pneu/r120.md section 2). No vendor file was opened or measured. The class
values below are its design inputs; its sizes are design choices or from a standard on file (the inlet thread, the mounting holes);
no vendor names; "generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic. The lane knows of no
standard that fixes a hose reel's stand, drum or crank; the interfaces it meets are the supply line's male NPT (ASME B1.20.1 through
pneu.NPT) and the screws that hold it down (ISO 273 clearance, lib/standards/holes.csv).
**Units / frame** mm, Z up. Origin: the centre of the base's underside (the mounting face, z = 0); the drum's axis along x at
z = 176, the crank on +x, the inlet on -x; the hose pays out along y.
**Built with** toolkit 1.3 · AutoLISP command `HOSE-REEL-SINGLE-NPT` · no parameters.

## Class values (ETIM 10.0 EC010439)
Design inputs. EC010439 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its 13 features (the pneu-4 answer's case, tube-pneu 1.0's and hose-guide-roller 1.0's
way). Until they are on file this table gives the values this reel is designed to under plain names; a later minor restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| number of hoses | 1 |
| form | a drum between two side frames on a base plate, fixed (no wheels: not a cart) |
| drive | hand crank, on the drum's +x end |
| rewind spring | none |
| hose the drum is sized for | 3/8 in air hose, 16 outside diameter: 4 layers of 7 turns, 18.8 m (calculated in element.py `capacity()`), so 15 m with room |
| hose supplied | no: the hose is its own element (hose-flex-npt or tube-pneu) |
| inlet connection | NPT 3/8 female (toolkit/pneu.py D1, ASME B1.20.1), on a swivel on the drum's axis |
| outlet connection | the hose's own end |
| max. operating pressure | not stated: Open figures below |
| drum material | steel, galvanised |
| stand material | steel, red powder coat |
| mounting | four M10 screws through the base (holes ISO 273 medium), floor or wall |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| base plate | 220 (x) × 280 (y) × 6, centred on the origin in plan | design choice: room for the frames and a screw at each corner |
| mounting holes | 4 × Ø11 through, at (±90, ±120) | M10 clearance, medium (ISO 273 H13, lib/standards/holes.csv: 11.0 to 11.27); position Ø1.0 to A B C (features.csv: floating fastener T = H − F); 14.5 of plate to the base's ends and sides, 11.5 to the frames (room for an M10 head) |
| side frames | 2 × 6 thick, 120 deep (y), from the base's top (z = 6) to z = 216; inner faces at x = ±67 | design choice: 27.5 of steel above each axle bore and 47.5 beside it (asserted) |
| axle bores | Ø25 through each frame on the drum's axis (y = 0, z = 176) | design choice: a plain bore the drum's axle stub turns in, face to face |
| drum axis | z = 176 above the mounting face | design choice: 10 between the flanges and the base plate (asserted) |
| hub | Ø150 × 120 (x = −60 to 60) | design choice: the hose's core; Ø150 keeps a 3/8 in hose's bend radius above 75 |
| flanges | 2 × Ø320 × 4 (x = ±60 to ±64) | design choice: 85 above the hub, 4 layers of a 16 OD hose with 10 left below the rim (asserted); 3 of running clearance to each frame |
| axle stubs | 2 × Ø25, from each flange's outer face (x = ±64) to the frame's outer face (x = ±73) | design choice: they turn with the drum in the frames' bores and end flush with the frames |
| crank | hub Ø40 × 10 (x = 73 to 83), arm 8 × 24 reaching 134 from the axis (pointing up at rest), handle Ø25 × 80 along +x, its axis 120 from the drum's | design choice: it turns with the drum and stays below the flanges' top (asserted) |
| swivel boss | Ø40 × 30 (x = −73 to −103), brass, fixed to the -x frame | design choice: the inlet bore's 12.2 sits inside its 30 with 17.8 to the frame (asserted) |
| inlet bore | Ø17.055 (E1 + h), 12.2 deep (L2 + 2), through a Ø26 land 0.2 proud of the boss's end | pneu.NPT (ASME B1.20.1 by its formulas), tank 2.0's rule; the land is the port node (cap-hex-npt's) |
| envelope | 281 (x) × 320 (y) × 336 (z) | the base's −x end (x = −110, beyond the land's face at −103.2) to the handle's end (x = 171); the flanges' Ø; the flanges' top at z = 336 |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-1` | NPT3/8 | female | the land's outer face, x = −103.2, on the drum's axis (y = 0, z = 176), axis −x | pneu.py D1 (NPT, ASME B1.20.1); role supply (ISO 11727 number 1, pneu.NODES); PNE-002 pairs it with a male NPT of the same size |

The hose's inner end joins the drum inside the hub, through the swivel; that joint is not drawn in 1.0 and is no port of the reel.

## Open figures
One open figure, class A (a rating; OPERATING.md 6), EM's.
- NOT ON FILE (A): the reel's max. operating pressure (its swivel's and inlet's, a rating PNE-003 reads). EC010439's features are not
  on file and no standard on file rates a hose reel's swivel. EM's: a figure with its source, or a rating he accepts, closes it.
Every other figure is a class value or a design choice above, or from a standard on file (the inlet thread, the clearance holes).

## Named nodes
| node | kind | axis | range | what |
|---|---|---|---|---|
| `drum` | rotate | +x, through (0, 0, 176) | 0 to 360° | the hub, both flanges, both axle stubs and the crank turn as one in the frames' bores; turned by the crank or by the hose drawn off |
| `port-1` | port | −x | fixed | the inlet land on the swivel boss |

## Materials by layer
`M-RED` the stand (base and side frames, red powder-coated steel) · `M-GALV` the drum (hub, flanges) and the crank's hub and arm ·
`M-SILVER` the axle stubs (bright steel) · `M-BRASS` the swivel boss and its land · `M-GREY-PA` the crank handle (polyamide; not
M-BLACK-PA or M-WHITE-PA, the Blender gate's printed materials, pneu-r113)

## Decals (Blender)
None in 1.0. No vendor names.

## Outputs (out/)
`hose-reel-single-npt.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010439), pneu-r120 (unattended): a hand-crank drum on Ø25 axle stubs in two side frames on a base, the `drum` node rotating about +x; a female NPT 3/8 swivel inlet `port-1`; four M10 clearance holes (ISO 273 medium); one open figure (the max. operating pressure, class A) |
