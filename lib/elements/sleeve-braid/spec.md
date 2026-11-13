# sleeve-braid · v1.0 · generic braided protective sleeve, polyester, for 1/4 in tube, 500 long

**What** a straight length of braided protective sleeve: a tubular polyester braid pulled over an air tube where the tube runs over
an edge, through a bundle or past a moving part, so the braid takes the wear instead of the tube's wall. Its use in the lane: over
tube-pneu (the contract's inch tube, toolkit/pneu.py D2) on a machine's air runs. The default build is 500 long, for 1/4 in tube.
**Class** connector-part · **Baseline** our own design: generic braiding for hose (ETIM 10.0 EC011215), as OPERATING.md 12 (generic
elements, EM 2026-11-07) says: the next ETIM class in generic.next_classes' order that builds. The Fittings group (EG015540) closed
with pneu-r115; the Hoses group (EG015510) is next, and its first two classes were passed over (lib/rounds/pneu/r116.md section 2).
No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices or read from the
contract; no vendor names; "generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic, whether that standard is on
file or not. A braided sleeve is sold by the size of the hose or tube it fits and cut from a reel; the lane knows of no dimensional
standard that fixes its section the way ISO 4017 fixes a screw's. Whether such a sleeve, like the seal tapes, falls under that list
is the question already with EM (lib/needs-em/pneu.md r108 (c)); if he rules that a standard shapes it, its wall becomes a "source
wanted" line and the element waits for that document.
**Units / frame** mm, Z up. Origin: the centre of the sleeve's end face a (y = 0) on its axis; the sleeve along +y to end b at
y = length.
**Built with** toolkit 1.3 · AutoLISP command `SLEEVE-BRAID` · `tube` (1/4; 5/32, 1/4, 3/8 in, pneu.TUBES_IN) · `length` (500; 50
to 10000 mm).

## Class values (ETIM 10.0 EC011215)
Design inputs. EC011215 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its two features (the pneu-4 answer's case, tube-pneu 1.0's and seal-tape-ptfe 1.0's way).
Until they are on file this table gives the values this sleeve is designed to under plain names; a later minor restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| material | polyester (PET) monofilament braid, grey |
| form | tubular braid, cut square at both ends, ends not finished |
| nominal size (the hose or tube it fits) | 1/4 in tube (parameter `tube`: 5/32 or 3/8 in), the contract's series |
| length | 500 mm (parameter `length`, 50 to 10000 mm) |
| temperature range | not stated |
| flame behaviour | not stated: no flame-retardant claim |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv: the sleeve holds no pressure (the tube inside it does) and no check reads a
figure of it.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| bore | Ø6.35 for 1/4 in tube (Ø3.97 for 5/32, Ø9.525 for 3/8) | read from the contract: pneu.TUBES_IN, the tube's OD (D2), so tube-pneu sits in it face to face (bore_d() in element.py). A braid expands and closes on the tube; drawn at the tube's OD |
| wall | 1.5 radial | design choice: the braid's thickness as drawn, its strands and their crossings as one annulus; at least 2.5 × the AutoCAD gate's 0.5 fillet (1.25, asserted) |
| outside | Ø9.35 for 1/4 in tube (Ø6.97 for 5/32, Ø12.525 for 3/8) | bore + 2 × wall |
| length range | 50 to 10000 | design choices: the shortest guard built, and one cut from a reel; a longer run is two sleeves |
| envelope | Ø9.35 × 500 (default) | along +y |

## Ports (toolkit/pneu.py)
None. The sleeve joins nothing: the tube inside it keeps its own ends and ports (tube-pneu's `port-a`, `port-b`).

## Open figures
None. Every figure is a class value, a design choice above, or read from the contract (the bore).

## Named nodes
None. Nothing moves; the sleeve is the fixed body.

## Materials by layer
`M-GREY-PA` the braid (the grey plastic on file closest to polyester's look; not M-BLACK-PA or M-WHITE-PA, the Blender gate's
printed materials, pneu-r113)

## Decals (Blender)
None in 1.0. No vendor names.

## Outputs (out/)
`sleeve-braid.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011215), pneu-r116 (unattended): a straight braided sleeve as one annulus, its bore the contract's tube OD (pneu.TUBES_IN), wall 1.5; parameters `tube` and `length`; no port, no node, no ratings |
