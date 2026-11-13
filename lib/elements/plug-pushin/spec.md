# plug-pushin · v1.0 · generic blanking plug for a push-in port, tube 1/4 in

**What** a blanking plug for a push-in port: a stem of one tube OD under a round head. The stem is pushed into a push-in fitting's
tube port (fitting-pushin's `port-tube`) as a tube end would be, the collet holds it, and the port is closed; pressing the release
sleeve and pulling the head takes it out again. Its use in the lane: a push-in port a circuit leaves unused (a fitting screwed into
a spare manifold or tee port for later, a test point), which request pneu-1's rule "every port connected or plugged" asks to close;
plug-hex-npt closes a female NPT port, this element a push-in one. The default build is tube 1/4 in, fitting-pushin's default.
**Class** connector · **Baseline** our own design: generic plug stop for fitting (ETIM 10.0 EC004547, synonym "Blanking plug"), as
OPERATING.md 12 (generic elements, EM 2026-11-07) says: the next ETIM class of EG015540 in pneu's order (generic.next_classes) that
the lane can build unattended (pneu-r113; the classes before it in that order were passed over for the reasons in
lib/rounds/pneu/r113.md section 2). No vendor file was opened or measured. The class values below are its design inputs; its sizes
are design choices or taken from fitting-pushin; the stem takes its OD from the pneumatic contract `toolkit/pneu.py` (request pneu-1:
D2 inch tube, push-in fittings to ISO 14743). No vendor names; "generic" in its title.
**Why generic** no dimensional standard on file or named in pneu.py shapes a blanking plug: ISO 14743 (pneu.py D2) is the push-in
fitting's standard, and the plug meets it only through its stem, which is a tube end of the contract's OD. The head is the design's.
**Units / frame** mm, Z up. Origin: the head's underside y = 0 on the stem's axis (x = z = 0), the face that meets fitting-pushin's
release sleeve; the stem and the fitting toward −y, the head toward +y. The port follows pneu.py's port frame: the pivot on the joint
plane, its axis toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `PLUG-PUSHIN` · `tube` (1/4; 5/32, 1/4, 3/8).

## Class values (ETIM 10.0 EC004547)
Design inputs. EC004547 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv does not list its 6
features: the case request pneu-4 raised for tube-pneu, which the core answered (lib/requests/core/pneu-4-answer.md): the element is
built with its design values under plain names (as tube-pneu 1.0, separator-oil-water 1.0 and the block fittings). When the features
are on main, a minor version restates this table in ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| model | blanking plug for a push-in port: a plain stem under a round head |
| material | polyamide, grey (fitting-pushin's release-sleeve material) |
| connection | push-in, as a tube end (ISO 14743; pneu.py D2) |
| tube outer diameter | 1/4 in, 6.35 mm (parameter `tube`: 5/32, 1/4, 3/8 in; pneu.TUBES_IN, exact conversions of the size names) |
| length | 24 mm for every tube, stem end to head top (`length()`: stem 16 + head 8) |
| max. operating pressure | not stated: a plug holds the pressure of the fitting it closes; no rating claimed, no ratings.csv |

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| stem | Ø6.35 for tube 1/4 (Ø3.97 for 5/32, Ø9.53 for 3/8), 16 long below the head's underside, 0.5 into the head; part of the `port-a` node | its diameter is the tube OD (pneu.TUBES_IN), so the collet and seal of fitting-pushin's port grip it as they grip tube-pneu; its length is a stand-in for the port's insertion depth, which is not on file (Open figures). The stem's end is square (a lead-in chamfer is not drawn) |
| head | Ø11 for tube 1/4 (Ø9 for 5/32, Ø15 for 3/8), 8 long (y 0 to 8) | as wide as fitting-pushin's release sleeve for the same tube (its body, BODY_D, less SLEEVE_DD, read from that element by `head_d()`), so the head sits on the sleeve's face and overhangs nothing; its rim stands at least 2 proud of the stem all round, and every envelope edge is at least 8 (the AutoCAD gate's fillet pre-flight): element.py asserts both |
| overall | 24 long (16 + 8); envelope Ø11 for tube 1/4 | |

## Ports (toolkit/pneu.py)
| node | unit | gender | at | basis |
|---|---|---|---|---|
| `port-a` | tube-1/4 (parameter `tube`) | male | the head's underside y = 0, axis −y; the stem runs 16 along the axis | pneu.py D2 (inch tube, ISO 14743 push-in); PNE-001 pairs it with a push-in port of the same OD (fitting-pushin's `port-tube`), as it pairs a tube-pneu end |

The port carries no role and no ISO 11727 number (design: plug-hex-npt's way, a plug takes the role of the port it closes; marked by
its node's name). a is the class's one connection.

## Open figures
- NOT ON FILE (B): the push-in port's insertion depth per tube OD (pneu.PUSHIN depth; the fit fitting-pushin's class B line leaves
  open, ISO 14743 named in pneu.py D2). The stem is drawn 16 long as a stand-in; once the depth is on file the stem takes it (a
  minor if only its length changes, since the node, origin and pivot stay). Every other figure is a class value, a design choice
  above, or the contract's tube OD.

## Named nodes
`port-a` (the stem); kind port, fixed (range 0). The head is the fixed body.

## Materials by layer
`M-GREY-PA` head and stem. Not M-BLACK-PA: the Blender gate takes black and white polyamide as printed faces and lays a decal
island on them, and the stem's island (2.88 wide for tube 1/4) is under its 3 mm floor (pneu-r113's first Blender run)

## Decals (Blender)
None: no face on a plug this size carries a legible mark. No vendor names.

## Outputs (out/)
`plug-pushin.lsp` · `.glb` (port pivot, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC004547), pneu-r113 (unattended): a round head as wide as fitting-pushin's release sleeve over a stem of the tube OD, one port pivot, parameter `tube`, grey polyamide; the stem's length a stand-in for the insertion depth (class B); no ratings (none claimed) |
