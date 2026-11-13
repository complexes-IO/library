# gl-xr-1 · v1.2 · display glasses (prop)

**What** The institute's own display glasses: a wayfarer-style frame with thick temples (the electronics housing), a brow status mark, and dark lenses the twin treats as screens. Used on the site's hero (the lab seen through the lenses) and in the virtual campus as the student's eyewear.
**Class** prop · **Baseline** the published envelope of a current display-glasses product (spec sheet, not a CAD file): 155.0 × 50.1 × 56.5 mm folded, 79 g, IPD 64 ± 6 mm, 52° diagonal field, built-in diopter dials, magnetic nose pads. The envelope and the feature list are from the spec; the frame shape is our own.
**Units / frame** mm, Z up. Origin: bridge centre on the front face; lenses in the xz plane, temples toward +y (the wearer's side).
**Built with** toolkit 1.3 (`mesh` primitive, swept sections) · AutoLISP command `GLXR` (frame and temples are swept meshes: glTF only; the LISP carries only the boxes) · parameter `fold` (temple fold angle, 0 open, 95 folded).

## Dimensions
| item | value |
|---|---|
| lens (each) | 56 × 42, wayfarer outline: outer-top corner highest, bottom narrower and rounder; centres at ±33 (IPD 66) |
| frame rim | 5.5 radial × 4.5 deep rounded section, 3 mm outside the lens outline |
| bridge | 10 between lenses, arch 20 high, 5.5 × 4.5 section |
| brow housing | the optics housing: 12 deep × 8 high bar along the top of each rim, a Ø7 diopter dial on each, the status mark on the right |
| temples | 150 long, 4 × 8 section, housing 9 × 12 over the first 38, bend down behind the ear at 112–143 |
| hinges | 5 × 9 × 12 block at the outer rim, titanium pin cover |
| overall | 148 wide × 52 high × 156 deep open; folded at 74° (the temples meet the brow housing) |
| lenses | 1.5 thick plates 1 mm behind the front face, `M-LENS-DARK` (base colour alpha 0.6, glTF BLEND) |
| nose pads | 2.5 × 3 × 9 grey PA on 1.6 Ø arms |

## Named nodes
`frame` (rims, brow housings, bridge, hinges) · `dial-l`, `dial-r` (diopter dials, turn about z) · `lens-l`, `lens-r` (the screens: in the twin a viewport texture, on the site a clip-path over the live video and ladder) · `temple-l`, `temple-r` (fold about the hinge).

## Deliberate differences from the spec
Width 148 against 155 (ours has no hinge overhang; +3.5 each side is a one-line change); height 52 against 50.1 (our rim is 3 mm all round). The spec's folded depth of 56.5 is not reproduced: our temples fold flat (21); the product's likely stop short, which the spec does not say. No unfolded dimensions, lens size or temple length are published, so those are eyewear norms.

## Materials by layer
`M-BLACK-PA` frame and temples (matte, slight gloss in Blender) · `M-LENS-DARK` lenses · `M-TITANIUM` hinge covers, brow mark · `M-GREY-PA` nose pads.

## Blender render (for the hero)
Camera front three-quarter, az 238 / el 14 as the preview; 2400 px wide, transparent background; lenses rendered opaque black at alpha 0 so the PNG has holes where the lenses are (the site shows the live video through them); a soft rim light on the top edge. Bevel 0.4 mm on the housing boxes; the swept parts need none.

## Outputs (out/)
`gl-xr-1.glb` (6 nodes, 4 materials, ~14 k triangles) · `gl-xr-1.lsp` (hinge and pad boxes only) · `preview-*.png` (front, three-quarter, side, folded).

## History
| version | change |
|---|---|
| 1.2 | render fix (GEO-050): the titanium hinge-pin covers were flush with the hinge blocks' inner faces; now 0.2 proud |
| 1.1 | validation suite finding (MOT-010): the temples turned about their centre line, so the inner half folded into the hinge block at 8°; the hinge axis is now the block's inner rear corner (build and pivot); the temples fold to 74°, where they meet the brow housing (was 95°) |
| 1.0 | first build; proportioned to a published display-glasses envelope; first element on the `mesh` primitive (toolkit 1.1) |
