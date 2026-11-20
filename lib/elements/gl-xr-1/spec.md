# gl-xr-1 · v2.0 · display glasses (prop)

**What** The institute's own display glasses: a full-rim frame, clear lenses with a display window inside each, a slim brow module with a knurled dial behind each rim, screw hinges, temples that taper to the tip and curve down behind the ear with the institute's mark inlaid in each, nose pads on wire arms. Used on the site's hero and in the virtual campus as the student's eyewear.
**Class** prop · **Baseline** the boxing system of ISO 8624 (measuring system and terminology for spectacle frames) and normal adult ranges (EM's brief, 2026-11-20). The shape is our own: it follows no product. The institute's mark on the temples is the only mark on it; there is no other logo, vendor name or product name.
**Units / frame** mm, Z up. Origin: bridge centre on the front face; lenses in the xz plane, temples toward +y (the wearer's side).
**Built with** toolkit 1.3 (`mesh` primitive throughout: every visible part is a lofted or turned mesh with its edges rounded in the geometry; glTF only, the AutoLISP command `GLXR` builds nothing visible) · parameter `fold` (temple fold angle, 0 open, 90 folded; the left temple stops at 84).

## Dimensions by the boxing system (ISO 8624)
| item | value | adult range (brief) |
|---|---|---|
| horizontal boxed lens size | 52 | 50 to 56 |
| vertical boxed lens size | 40 | |
| distance between lenses (bridge width) | 18 | 16 to 20 |
| boxed centre distance | 70 | |
| overall length of side (temple), hinge axis to tip along the centre line | 145 | 140 to 150 |
| overall width, open | 142.7 | 140 to 148 |
| overall, open | 142.7 wide × 140.1 deep × 47.0 high | |
| overall, folded (`fold` 90) | 140.8 wide × 24.7 deep × 47.0 high | |

The lens outline is scaled to the boxed size exactly, so 52 × 40 is the box that touches the lens shape, and 18 the gap between the two boxes.

## Parts
| part | what it is |
|---|---|
| lenses | a meniscus between two concentric spheres, front radius 350, 2.0 thick, the front vertex 0.2 behind the frame's front plane; `M-LENS-CLEAR`: transmission 0.95, index of refraction 1.5 (the glTF default, written by the element's glb and left implicit by Blender's export), roughness 0, all but colourless: clear glass, what is behind it seen sharply |
| display windows | inside each lens, mid-thickness: a 22 × 13 × 0.3 waveguide area with 1.5 corners, its centre 3 nasal and 1.5 above the boxed centre (pupil distance 64); `M-WAVEGUIDE`, neutral grey, base colour alpha 0.02 (glTF BLEND): off, only a faint outline at a close look |
| rims | 3.5 radial × 4.6 deep, outer edges rounded 1.0, inner lips 0.3; a groove 2.2 wide and 0.95 deep holds the lens edge (0.1 clear each side, 0.15 at the floor) and follows it round the outline, since a meniscus edge is not in one plane |
| bridge | a low arch from rim to rim, 4.4 deep × 4.6 high, edges 1.3 |
| brow modules | a 6.0 deep × 3.4 high bar behind the top of each rim, flush with the rim's top, edges 1.2; a Ø5.4 × 2.0 dial on each with a straight knurl on its rim (40 teeth, 0.22 deep), top edge 0.6 |
| end pieces | 4.4 × 9.0, edges 1.3: out of the rim's temporal side, round a 3.7 corner, back to the butt joint at y 9.45 |
| hinges | axis vertical at x ±64.35, y 9.6, proud of the inner faces: three knuckles Ø3.0 × 2.3 (two on the frame, the middle one on the temple), rims 0.5, each on a tab to a 1.2 leaf on the inner face; a slotted pan-head screw Ø2.1 down the axis, its end showing below |
| temples | 145 by ISO 8624; section 4.4 × 9.0 at the hinge tapering all the way to 2.7 × 5.0 at the tip, edges 1.3 to 1.1; a slight bow out (1.2 at mid length) then in, and a continuous curve down behind the ear from about 88, the tip 33 below the hinge line |
| nose pads | 2.2 × 5.6 × 11 pads, edges 1.0, on Ø1.2 wire arms from the rims' nasal side |
| mark | on the outer face of each temple: see The mark |

Every outer edge is rounded between 0.5 and 1.5, except the dial's knurl (a knurl is sharp by nature), the inner lips of the rim (0.3), the screw head (0.25) and the mark's inlay (0.03 proud): parts too small to carry 0.5. Rounded surfaces are cut finely enough to show no facet: quarter rounds in six segments (15°), the rims' corners in 5° steps, turned parts in 28 segments.

## The mark
The institute's mark, the ring with `0{1}` inside it, as the site draws it. Its outline is not redrawn: `lib/standards/cit-mark.json` holds it for every element (toolkit/mark.py), taken once from the site's own mark (the inline `svg.site-mark` of `templates/nav.html`: a circle of radius 33 with a line of 2 in a 72 box, and the text `0{1}` at font-size 20, centred), the characters' contours being those of the first font that mark names.
| item | value |
|---|---|
| where | the outer face of each temple, centred on the temple's height (8.9 there), its centre 12 behind the hinge axis (y 21.6) |
| ring | outer diameter 6.0, line 0.4 (the brief's; at 6.0 the site's own line would be 0.18) |
| characters | 4.8 wide × 2.0 high, 0.16 clear of the ring; the font's heaviest weight (800), 1.2 times the site's size relative to the ring: main strokes 0.30, the thinnest places 0.28 (at the site's regular weight and size they would be 0.15) |
| how | real geometry, no texture and no decal: six solids a side (the ring, the zero with its counter, the dot in the zero, the two braces, the one) in `M-TI-BRUSHED`, following the temple's face, 0.3 deep into it and 0.03 proud of it, so the two faces are never coplanar (GEO-050) |
| node | `temple-l` / `temple-r`: it folds with the temple |
| reading | upright and left to right on both sides as worn: toward the back on the +x temple, toward the front on the −x temple; neither is the other's mirror image |

## Named nodes
`frame` (rims, bridge, brow modules, end pieces, the frame's hinge knuckles, leaves and screws) · `body` (nose pads and their arms) · `lens-l`, `lens-r` · `display-l`, `display-r` (the display windows: where the site makes the projection come from; in the twin, the screens) · `dial-l`, `dial-r` (turn about z) · `temple-l`, `temple-r` (each with its hinge knuckle and leaf; rotate about the hinge screw's axis, inward: `temple-r` 0 to 90°, `temple-l` 0 to −84°, so the right folds flat first and the left comes to rest over it). Colliders: `front`, `temple-l`, `temple-r`.

## Materials by layer
`M-BLACK-MATTE` frame and temples (base 0.03, roughness 0.85) · `M-TI-BRUSHED` hinges, screws, pad arms, the mark (metallic 1, roughness 0.3) · `M-GREY-PA` dials and nose pads (roughness 0.55) · `M-LENS-CLEAR` lenses · `M-WAVEGUIDE` display windows. The glb carries no texture and no UV of its own, so the brushed finish is the metal's roughness, not a drawn grain.

## Blender gate
`blender --background --python lib/toolkit/blender/gate.py -- lib/elements/gl-xr-1/out/gl-xr-1.glb lib/elements/gl-xr-1 --class prop --bevel-only M-NONE`: smooth by angle, UVs, normals and tangents as for every element, and no Bevel modifier, because the edges are already round in the geometry and a 0.5 bevel would eat the knurl and the rim's lips. The web asset is the gate's `gltf/gl-xr-1.glb`.

## Outputs (out/)
`gl-xr-1.glb` (9 nodes and `body`, 5 materials, about 51 000 triangles; the gated glb is 2.0 MB; the brief's ceiling is 60 000 and 3 MB) · `gl-xr-1.lsp` (nothing visible: meshes are glTF only) · `preview-*.png` (front, three-quarter, side, folded).

## Not redone in 2.0
`dwg/`, `step/` and the AutoCAD gate files are those of 1.2: a mesh element has no solids for AutoCAD to build. The Godot QA scene has not been run on 2.0.

## History
| version | change |
|---|---|
| 2.0 | rebuilt for the home page (EM's brief 2026-11-20): sized by the boxing system (lens 52 × 40, bridge 18, temple 145, width 142.7; was lens 56, bridge 10, width 148); real lenses (2 mm meniscus, clear, in a rim groove) with a display window inside each (new nodes `display-l`, `display-r`); three finishes (`M-BLACK-MATTE`, `M-TI-BRUSHED`, `M-GREY-PA`); every edge rounded in the geometry; three-knuckle screw hinges, the temple turning about the screw's axis (right 90°, left 84°, one over the other); tapered temples curving down behind the ear; nose pads on wire arms; bridge 4.4 × 4.6; the institute's mark inlaid in each temple (`mark.json`). The brow status mark is gone. No longer proportioned to a product's published envelope |
| 1.2 | render fix (GEO-050): the titanium hinge-pin covers were flush with the hinge blocks' inner faces; now 0.2 proud |
| 1.1 | validation suite finding (MOT-010): the temples turned about their centre line, so the inner half folded into the hinge block at 8°; the hinge axis is now the block's inner rear corner (build and pivot); the temples fold to 74°, where they meet the brow housing (was 95°) |
| 1.0 | first build; first element on the `mesh` primitive (toolkit 1.1) |
