# floor-marking · v1.0 · floor marking tape, generic, one straight strip 50 wide x 1 thick x 1000 long, self-adhesive PVC, one colour, no print

**What** Floor marking tape: the strip stuck to the floor that marks an aisle, a storage bay, a machine's keep-clear zone or a
walkway's edge. One straight strip, 50 wide, 1 thick (its adhesive within that), 1000 long, plain, one colour; strips are placed
end to end from the origin at one end, so a line of any length is a row of them. The inventory row lists it as "floor-marking"
(floor marking tape and signs, ANSI Z535 / ISO 3864) for the safety-equipment and storage-steel systems (lib/machines-factory.txt
lines 122 and 123). One fixed body: no moving node and no terminal.
**Class** plate · **Baseline** our own design: generic warning tape (ETIM 10.0 EC001496 Warning tape), OPERATING.md 12 "Generic
elements" (EM, 2026-11-07); lib/inventory.csv marks the row own_design "yes" with etim EC001496 (the class and its 11 features are
on file, so the element is built generic and states its class values). No product was matched and no vendor file was opened.
Nothing it meets takes a figure from a standard (a tape has no fixing); every size is a design choice. Which colour a marking
carries is the placing system's choice under its colour code: OSHA 1910.144 is in lib/standards/sources.csv as free to read with
its figures to be recorded, ISO 3864 is not on it, and neither's figures are in a standards table yet, so the class value Colour is
"not stated" and the layer M-YELLOW is the model's appearance only; no colour code and no safety message is claimed.
**Units / frame** mm, Z up: the strip runs along x, its width along y, its thickness along z. Origin: the floor plane (z = 0) at
the strip's start end on its centre line; the strip occupies x 0 to 1000, y ±25, z 0 to 1. The next strip of a line is placed at
x 1000. Extents x 0 to 1000, y ±25, z 0 to 1.
**Built with** toolkit 1.3 · AutoLISP command `FLOORTAPE` · no parameters.

## Class values
ETIM 10.0 class EC001496 Warning tape (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every feature in ETIM's
order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the element.

| # | feature | value |
|---|---|---|
| 1 | Imprint (EF000131) | no: a plain strip, one colour |
| 2 | Literal imprint (EF015918) | not stated (none) |
| 3 | Language of the imprint (EF015922) | not stated (none) |
| 4 | Colour (EF000007) | not stated: one colour, the placing system's choice under its colour code (Baseline); the layer M-YELLOW is appearance only |
| 5 | Transparent (EF006243) | no |
| 6 | Material (EF002169) | PVC (lib/materials.csv pvc; the compound not stated) |
| 7 | Self-adhesive (EF000434) | yes: an adhesive-backed floor tape; the adhesive lies within the 1 thickness and is not drawn; no adhesion figure claimed |
| 8 | Resistant to chemicals (EF001074) | not stated |
| 9 | Detectable (EF012253) | no |
| 10 | Width (EF000008) | 50 mm |
| 11 | Length (EF001438) | 1 m: one strip 1000 long (a line of any length is strips end to end) |

## What it meets
| figure | value | source |
|---|---|---|
| the floor | the strip's underside, 50 × 1000 in the plane z = 0 | design: any flat floor; the strip lies on it face to face, held by its adhesive |
| the next strip | the end face at x 1000, 50 × 1 in the plane x = 1000 | design: the next strip's origin is placed there; end faces meet, nothing overlaps |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| width | 50 | a common aisle-marking width a forklift driver reads at a glance; the class value Width |
| thickness | 1, adhesive included (z 0 to 1) | a floor tape's build; under the gate's 2.5 × 0.5 thin limit, so the gate picks no edge on it |
| length | 1000 | the class value Length 1 m: one placeable unit, chained end to end; a roll is many of them |
| colour, adhesion, wear, slip, chemical resistance | not claimed | no figure is on file for them and no colour code is in a standards table yet (Baseline); the layer M-YELLOW is the model's appearance only |

## Mechanism
None: one fixed strip. behaviour.csv is the header only (no terminal, no state, no pose). MOT-010 has nothing to sweep.

## Named nodes
None. Collider, an axis-aligned box: `strip` (the whole strip, x 0 to 1000, y ±25, z 0 to 1).

## Materials by layer
`M-YELLOW` the strip (PVC, lib/materials.csv pvc; the layer's colour is the model's appearance, not a colour code).

## Decals (Blender)
"complexes.org generic" on the strip's underside (z = 0), at the start end.

## Notes
No vendor names, part numbers or marks. No safety claim: the strip carries no print and no colour code; the system that places it
chooses the colour under its code (OSHA 1910.144, ISO 3864-1, ANSI Z535) once that code's figures are recorded in a standards table
(lib/standards/sources.csv: osha-1910.144 "free to read; record the figures used"). No open figure: nothing it meets takes a
standard's figure, the class values are design inputs and the rest are design choices. A warning tape is not a part a dimensional
standard shapes, so it is built generic to its ETIM class (OPERATING.md 12). Later versions: the corner piece (an L, two strips
mitred or butted at a right angle), the T piece, a two-colour hatched strip and a printed strip; a floor sign (a printed disc or
plate stuck to the floor) is sign-iso7010's family, not this one.
The gate's fillet rule (fillet r 0.5 for a plate, lib/toolkit/fillet.py): the strip is 1 thick, under 2.5 × r, so the gate picks
no edge; the bounding box is the one axis-aligned box; no node, nothing nested, nothing tilted.

## Outputs (out/)
`floor-marking.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC001496), our own design (mech-r102, unattended, 2026-11-11) |
