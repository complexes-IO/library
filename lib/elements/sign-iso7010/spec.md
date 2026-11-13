# sign-iso7010 · v1.0 · safety sign plate 200 x 300 x 2, generic, aluminium, blank symbol and text fields, 4 x Ø4.5 corner holes (M4, ISO 273)

**What** A safety sign plate: the rigid plate screwed to a wall, a rack upright, a door or a guard that carries a safety sign's
symbol above and its supplementary text below. A portrait 200 × 300 × 2 aluminium plate with two printed fields standing 0.1
proud of its face, a 160 × 160 symbol field and a 160 × 60 text field, both blank in this version, and four Ø4.5 clearance holes
at the corners for the host's M4 screws. The inventory row lists it as "sign-iso7010" (safety sign, ISO 7010 / ANSI Z535) for the
racks-storage, storage-steel and safety-equipment systems (lib/machines-factory.txt lines 121 to 123). One fixed body: no moving
node and no terminal.
**Class** plate · **Baseline** our own design: generic warning/signing plate (ETIM 10.0 EC001777 Warning/signing plate),
OPERATING.md 12 "Generic elements" (EM, 2026-11-07); lib/inventory.csv marks the row own_design "yes" with etim EC001777 (the class
and its 22 features are on file, so the element is built generic and states its class values). No product was matched and no
vendor file was opened. The holes it meets are on file (ISO 273); every other size is a design choice. The symbols of ISO 7010 and
the colours of ISO 3864 are not in the standards on file (lib/standards/sources.csv lists iso-7010 as "to get"), so the fields are
blank and the class values Symbol, Literal imprint and Colour are "not stated": this plate carries no safety message until a
version prints one, and claims none.
**Units / frame** mm, Z up: the width runs along x, the height along z, the thickness along y. Origin: the mounting face plane
(y = 0, the wall's face) at the plate's centre, x = 0 on the vertical centre line, z = 0 on the horizontal centre line (a sign is
placed by its centre at the height its system sets). The plate lies toward −y (y −2 to 0, as tag-plate 1.0's plates lie on their
panel); the printed fields stand at y −2.1 to −2. Extents x ±100, y −2.1 to 0, z ±150.
**Built with** toolkit 1.3 · AutoLISP command `SIGNPLATE` · no parameters.

## Class values
ETIM 10.0 class EC001777 Warning/signing plate (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in
ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Shape (EF000051) | rectangular, portrait (200 wide × 300 high) |
| 2 | Model (EF000010) | not stated (a plain rigid plate; the sign's kind, warning, prohibition, mandatory, safe condition or fire, is the print of a later version) |
| 3 | Material (EF002169) | aluminium (lib/materials.csv al-6063; the alloy and temper not stated) |
| 4 | Material quality (EF001257) | not stated |
| 5 | Halogen free (EF000025) | not stated |
| 6 | Waterproof (EF001823) | not stated |
| 7 | With alert-/information symbol (EF006312) | the symbol field is there (160 × 160, blank): a symbol is a later version's print |
| 8 | Symbol (EF025222) | not stated (the field is blank; ISO 7010's symbols are not in the standards on file: lib/standards/sources.csv iso-7010, "to get") |
| 9 | With alert-/information text (EF006313) | the text field is there (160 × 60, blank): text is a later version's print |
| 10 | Literal imprint (EF015918) | not stated (blank) |
| 11 | Language of the imprint (EF015922) | not stated (blank) |
| 12 | Width (EF000008) | 200 mm |
| 13 | Height (EF000040) | 300 mm |
| 14 | Diameter (EF000551) | not stated (a rectangular plate; a round plate is another version) |
| 15 | Thickness (EF000125) | 2 mm |
| 16 | Type of fastening (EF002442) | screws: 4 × Ø4.5 corner holes for M4 (What it meets) |
| 17 | With mounting material (EF006009) | no: the screws are the host's (a common part not built yet) |
| 18 | Foldable (EF000643) | no (a rigid plate) |
| 19 | Colour (EF000007) | not stated: the plate's layer M-ALU-ANOD and the fields' M-WHITE-PA are the model's appearance; the sign colours (ISO 3864-1) are not in the standards on file and no colour is claimed |
| 20 | Fluorescent (EF009518) | no |
| 21 | Photoluminescent (glow in the dark) (EF006058) | no |
| 22 | Mounting method (EF000003) | screwed flat to a surface by its four corner holes (a wall, a rack upright, a door, a guard) |

## What it meets
| figure | value | source |
|---|---|---|
| the screws | 4 × M4, Ø4.5 through the plate at the corners, 10 in from each edge (x ±90, z ±140: pattern 180 × 280) | ISO 273 medium (H13), lib/standards/holes.csv; features.csv position Ø0.25 at MMC to A the mounting face, B the vertical and C the horizontal centre line (ASME Y14.5 floating fastener, T ≤ H − F = 0.5 shared with the host's pattern: Ø0.25 here, Ø0.25 the host's). M4 is this design's choice (a sign plate's usual fixing); the screws and the host's holes or wall anchors are the host's (a screw is a common part not built yet: the holes are modelled, the part placed later) |
| the surface | the plate's back, 200 × 300 in the plane y = 0 | design: any flat face; the plate seats on it face to face |
| the print | the two fields, 160 × 160 and 160 × 60 on the face (y −2), 0.1 proud | design: a printed or applied face, drawn 0.1 proud as tag-plate 1.0 draws its text fields, so the glTF shows the fields; blank in this version |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| plate | 200 × 300 × 2, portrait (x ±100, z ±150, y −2 to 0) | a size a symbol and a line of text read at a few metres; 2 aluminium is rigid at this size and screws flat (its 2 mm end edges are under the gate's 3 mm minimum and skipped; its eight long face edges, 200 and 300, are filleted at r 0.5 and meet the volume rule with room: no free-corner edge of 3 to 7 mm anywhere) |
| symbol field | 160 × 160 (x ±80, z −30 to 130), 20 under the top edge | the square field an ISO 7010-style symbol fills, as wide as the plate less 20 each side; clear of the corner holes (x 87.75 to 92.25, z 137.75 to 142.25) |
| text field | 160 × 60 (x ±80, z −120 to −60), 30 under the symbol field and 30 above the bottom edge | the supplementary text's band; clear of the bottom holes |
| field height | 0.1 proud (y −2.1) | a print, not a part: the same figure tag-plate 1.0 uses; the field's back seats face to face on the plate's face (a seat, not two same-facing faces in one plane) |
| holes | 4 × Ø4.5 at x ±90, z ±140 | 10 in from each edge leaves a 7.75 wall outside each hole; a four-corner pattern holds a plate flat |
| colour, finish, reflectivity, durability | not claimed | no figure is on file for them; the layers show an anodised plate with white fields, appearance only |

## Mechanism
None: the plate and its two fields are one fixed body. behaviour.csv is the header only (no terminal, no state, no pose). MOT-010
has nothing to sweep.

## Named nodes
None. Collider, an axis-aligned box: `sign` (the whole plate with its fields, x ±100, y −2.1 to 0, z ±150).

## Materials by layer
`M-ALU-ANOD` the plate (aluminium, lib/materials.csv al-6063) · `M-WHITE-PA` the two printed fields (a print on the face, drawn as
a layer for appearance; no material of its own).

## Decals (Blender)
"complexes.org generic" on the plate's back (y = 0), near the bottom edge, between the lower holes.

## Notes
No vendor names, part numbers or marks. No safety claim: the fields are blank, no symbol, text or colour is printed, and the plate
carries no message; a sign that does is a later version with the symbol and colours taken from ISO 7010 and ISO 3864 once they are
on file (lib/standards/sources.csv: iso-7010 "to get"; OSHA 1910.144 free to read, its colour figures to be recorded attended into
a standards table). No open figure: the holes it meets are on file (ISO 273), the class values are design inputs and the rest are
design choices. A sign plate is not a part a dimensional standard shapes, so it is built generic to its ETIM class (OPERATING.md
12); a round plate, a self-adhesive foil, a folding sign or a hanging sign is another version or another element.
The gate's fillet rule (fillet r 0.5 for a plate, lib/toolkit/fillet.py): the gate picks the plate's eight long face edges (200
and 300 long: one batch, 107.2 of 107.3 mm³ removed) and skips its 2 mm end edges as short (under 3 mm) and the 0.1 fields' edges
as thin; no free-corner edge of 3 to 7 mm exists (mech-r101's trap). The bounding box's extremes lie on the plate (x ±100, z ±150,
y 0) and the fields (y −2.1), all axis-aligned boxes; no node, nothing nested, nothing tilted.

## Outputs (out/)
`sign-iso7010.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC001777), our own design (mech-r102, unattended, 2026-11-11) |
