# coupling-clamp-strip · v1.0 · generic clamp strip coupling, plain-end pipe NPS 1/4 (OD 13.72)

**What** a clamp strip coupling (a clamp band coupling): it joins two plain-end pipes of the same outside diameter, or closes a crack
or a pinhole in one, with no thread cut. An EPDM sleeve goes round the two pipe ends where they meet; a stainless band goes round the
sleeve; two lugs on the band are drawn together by two screws, so the band squeezes the sleeve onto the pipes and the sleeve seals
them. A host that runs plain-end pipe places it over the joint; the default build is the coupling for NPS 1/4 pipe.
**Class** connector-part · **Baseline** our own design: generic clamp strip coupling (ETIM 10.0 EC011508), as OPERATING.md 12
(generic elements, EM 2026-11-07) says: the first class of the tier-2 group EG015540 "Fittings, flanges and connectors" in pneu's
order that builds, after the Seals group closed with seal-vring's EC010422 (pneu-r105; the report says why EC010650 was passed over).
No vendor file was opened or measured. The class values below are its design inputs; its sizes are design choices; no vendor names;
"generic" in its title.
**Why it may be generic** OPERATING.md 12 keeps a part a dimensional standard shapes from being generic (pipe and flange sizes among
them). The one figure here a standard fixes is the pipe's outside diameter, and that is on file: D of ASME B1.20.1 Table 2 (pneu.NPT,
the figures EM sent 2026-11-07), the OD of the steel pipe the NPT threads of the lane's contract (D1) are cut on. No standard on file
sizes a band coupling's sleeve, band or lugs (lib/standards/sources.csv has none), so they are the design's.
**Units / frame** mm, Z up. Origin: the coupling's centre on the pipe axis; x along the pipe (the two pipe ends meet at x = 0), the
lugs up (+z).
**Built with** toolkit 1.3 · AutoLISP command `COUPLING-CLAMP-STRIP` · `pipe` (NPS1/4; NPS1/8, NPS1/4, NPS3/8: the plain-end pipe it
fits).

## Class values (ETIM 10.0 EC011508)
Design inputs. EC011508 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (the tier-1 classes and the
classes the inventory uses) does not list its features (the pneu-4 answer's case, tube-pneu 1.0's and the seals' way). Until they are
on file this table gives the values this coupling is designed to under plain names; a later minor restates them in ETIM's order with
their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| type | clamp strip coupling for plain-end pipe: sleeve, band, two lugs, two screws |
| pipe outside diameter | 13.716 mm, NPS 1/4 (parameter `pipe`: NPS 1/8 10.287, NPS 3/8 17.145), derived: pneu.NPT D (ASME B1.20.1 Table 2) |
| pipe material | not stated: any pipe of that OD (steel pipe is what the NPT sizes name; pipe-asme is not built) |
| band material | stainless steel |
| seal material | EPDM, black |
| length | 40 mm (30 and 50 for NPS 1/8 and 3/8) |
| number of screws | 2, M5 (not placed in 1.0: screw-iso4017 is not built) |
| max. pressure | not stated: no rating is claimed |
| temperature range | not stated |
| approval and quality marks | none: no approval marks on our elements (OPERATING.md 6) |

No rating is claimed, so there is no ratings.csv: no check reads a band coupling's figure, and the pipes it joins carry their own.

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| sleeve bore | Ø13.716 (NPS 1/4; Ø10.287, Ø17.145) | the pipe's OD, derived: `pipe_od()` reads D from pneu.NPT (ASME B1.20.1 Table 2, D × 25.4) |
| sleeve | EPDM, 3 wall, 0.5 shorter than the band at each end (39 long for NPS 1/4) | the seal between the pipe ends and the band; a design choice; its ends sit inside the band's so no two end faces share a plane |
| band | stainless, 4 wall over the sleeve, the full length: Ø27.716 outside for NPS 1/4 (Ø24.287, Ø31.145) | stiff enough to carry the two lugs on its top; a design choice; the band's split under the lugs is not drawn (an appearance, class C: the band is drawn as a closed ring) |
| lugs | two, 6 thick (y), a 2 gap between them (y = ±1), 4 shorter than the band (2 in from each end), bottom 0.5 above the sleeve's outside, top 9.5 above the band's outside | each lug's whole bottom face lies inside the band, so lug and band are one solid (asserted for each size); the gap is what the screws close |
| holes | 2 per lug, Ø5.5, on y, at x = ±L/4 (one over each pipe end), axis 4.5 above the band's outside | M5 clearance, medium (ISO 273 H13: 5.5 to 5.68; lib/standards/holes.csv); 1.75 of lug under each hole, 2.25 above it, 2.5 or more to the lug's end (asserted) |
| length | 40 for NPS 1/4 (30, 50) | each pipe end goes in half the sleeve's length, at least one OD (asserted): its grip in the sleeve; a design choice |
| screws | not drawn | the two M5 screws and their nuts are common parts (screw-iso4017, not built): OPERATING.md 12, an own design models the holes and places the part in a later version |
| envelope | 40 × 27.716 × 37.216 (default: x × y × z, the lugs' top 23.358 above the axis) | calculated from the sizes above |

## Ports (toolkit/pneu.py)
None. The pipe passes through: the coupling joins the host's two pipe ends and has no connection of its own. pneu.py's units are
threads and tube ODs; a plain pipe end has none (pipe-asme, the inventory's pipe, is not built).

## Open figures
None. Every figure is a class value, a design choice or derived above.

## Named nodes
None. Nothing moves: the screws close the gap once, at assembly.

## Materials by layer
`M-SILVER` band and lugs (stainless steel) · `M-GASKET` sleeve (EPDM, black)

## Decals (Blender)
None in 1.0. No vendor names.

## Outputs (out/)
`coupling-clamp-strip.lsp` · `.glb` (`-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011508), pneu-r105 (unattended): a clamp strip coupling for NPS 1/8, 1/4 or 3/8 plain-end pipe, the pipe OD from pneu.NPT D; EPDM sleeve, 4 mm stainless band, two lugs with M5 clearance holes (ISO 273), screws not placed; parameter `pipe`; no port, no node, no ratings |
