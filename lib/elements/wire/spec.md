# wire · v1.0 · single insulated conductor with prepared ends

**What** One conductor as a part, so an end stripped too short, a nicked conductor, stray strands or a missing ferrule are properties of this wire, and `toolkit/contact.py` `terminate()` decides what a clamp makes of them.
**Class** wire · **Baseline** see element.py BASELINE; nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: end A's conductor tip on the wire axis, inserted along +y; the wire leaves toward −y and follows `path`.
**Built with** toolkit 1.3 · AutoLISP command `WIRE` · `size` (mm², 1.5), `colour` (a material: M-BLUE, M-BROWN, M-BLACK-PA, M-GREY-PA, M-GREEN-YELLOW, ...), `length` (150), `path`, `strip` (10), `ferrule` (false), `conditions` ('a:under-stripped/b:strands-out': end, condition).

## Dimensions
| item | value |
|---|---|
| conductor | area-equivalent Ø from `size` (1.5 mm²: Ø1.38) |
| insulation | conductor + 2 x thickness + 0.2 (lay) |
| stripped end | bare copper `strip` long; under-stripped 0.4 x, over-stripped 1.8 x; nicked: Ø0.6 x over a tenth of the strip; strands-out: four splayed strands |
| ferrule | tinned sleeve (8 / 10 / 12 by size) + plastic collar 2.0 |

## Figures and their sources
| figure | value | source |
|---|---|---|
| insulation thickness 1.5 / 2.5 / 4 / 6 / 10 mm² | 0.7 / 0.8 / 0.8 / 0.8 / 1.0 | Assumption (IEC 60227-3 class) |
| ferrule sleeve length 0.5-2.5 / 4 / 6-10 mm² | 8 / 10 / 12 | Assumption (DIN 46228-4 class) |
| strip length | 10 default | Assumption: the clamp's maker states it (NOT ON FILE) |

## Named nodes
`end-a`, `end-b` (kind contact: origin the tip, axis the way it goes into a clamp, range (0, bare or sleeve length); extras gender wire, size, d, ferrule, strip, condition)

## Materials by layer
`M-CU` bare conductor · `M-SILVER` ferrule sleeve · insulation and collar: `colour`

## Decals (Blender)
none

## Notes and assumptions
Conductor sizes, insulation thickness and ferrule lengths are Assumption (IEC 60227-3 / DIN 46228-4 class, not on file). The insulation is a swept mesh (glTF only), like the cordset's cable.

## Outputs (out/)
`wire.lsp` (solids only: the swept insulation or jacket is glTF only) · `.glb` (contact and port data in the node extras, `-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.0 | first build: the element layer reaches the wire and its termination (2026-11-03), toolkit 1.3 |
