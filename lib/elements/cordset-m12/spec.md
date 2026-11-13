# cordset-m12 · v1.8 · M12 cordset, routed cable

**What** M12 cordset, routed cable. Built from the Stage 0 brief `references/measure.md` (figures with their document pages).
**Class** cable · **Baseline** the cordset cut sheets and drawings of the round-4 reference set: cable Ø A 5.0 (22 AWG), D 6.6, L 9.8 (16 AWG); catalogue lengths 0.6 / 1 / 2 / 3 / 5 / 7.5 / 10 / 15 m; bend radius 5 x Ø fixed, 10 x Ø flexing; ends are plug-m12 1.2; own per the 2026-11-03 ruling (A, D and L in one element). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: end A (male) mating face at the origin, plugging along +y into a port that looks toward −y; the cable leaves toward −y and follows `path`.
**Built with** toolkit 1.3 · AutoLISP command `CORD` · `coding` (A | D | L), `length` (1000), `ends` (straight), `path` (list of points for end B's route; default a straight run with a gentle hang), `genders` (male-female; male-open / female-open: end B open-ended), `conditions_a`, `conditions_b`.

## Dimensions
| item | value |
|---|---|
| connectors | coupling nut Ø14.5 × 8, overmould Ø13 × 32; male pin carrier 2 proud, female insert recessed 1.5 |
| cable | swept circle, 12 sides, resampled every 8 mm along the path |
| open end B (genders `*-open`) | no plug: the jacket ends at the path's end (`length` runs to it); one bare lead per pole of the coding, 50 beyond the jacket, fanned to 6 off the axis on the poles' angles (design: own choice, no standard fixes a strip length) |
| lead Ø | the conductor's solid-equivalent Ø, derived: derive by the AWG definition d = 0.127 mm x 92^((36-n)/39) (sources.csv awg): A 22 AWG 0.644, L 16 AWG 1.291 (lib/standards/cables.csv) |

## Named nodes
`port-a`, `port-b` (kind port, unit = coding, mating data in the extras: plug-m12) · `port-a.insert.c<pole>`, `port-b.insert.c<pole>` (contacts) · `port-a.nut`, `port-b.nut` (rotate, 4.35 turns; L 5) · open form: `lead-<pole>` (kind contact, at each lead's tip, axis along the lead; no `port-b`)

## Materials by layer
`M-ZINC` nuts · `M-BLACK-PC` overmould, inserts · `M-CABLE-PUR` cable · `M-CU` open-end leads

## Decals (Blender)
none

## Notes and assumptions
The first routed element: connections.csv will pass `path` from the assembler's port-to-port routing (toolkit 1.3). Every figure marked **Assumption** here was NOT ON FILE in the brief and is set from the usual norm; a document figure replaces it as a minor version.
NOT ON FILE (B): the D cable's conductor size (cordset cut sheet). Assumption (B): the D form's open-end leads are drawn at A's 22 AWG (0.644) until that figure is on file; only the open form draws them.

## Outputs (out/)
`cordset-m12.lsp` · `.glb` (pivots on the moving nodes, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.8 | core round 29 (request panel-4 item 2): the open-ended form, genders male-open / female-open: end B bare leads, each a contact node lead-<pole> with its pin row (behaviour.csv form rows); the default form's nodes and figures unchanged (a minor) |
| 1.7 | round 7 back (2026-11-04): ends are plug-m12 1.6 (the cordset L female's recess takes X04's outline) |
| 1.6 | round 6 back (2026-11-04): ends are plug-m12 1.5 (D keyed as it is; the D and L male nuts and bodies as measured) |
| 1.5 | round 5 back (2026-11-04): ends are plug-m12 1.4 (the A male nut and body as measured; D poles and notches; the L key outlines) |
| 1.4 | round 4 back (2026-11-04): ends are plug-m12 1.3; the A cable's Ø5.0 is the catalogue's PVC figure (the TPE cable's Ø NOT ON FILE) |
| 1.3 | round 4 (2026-11-04): ends are plug-m12 1.2 (a male end's nut is the threaded sleeve, a female end's the threaded bore); cable Ø A 5.0, D 6.6, L 9.8 and the catalogue lengths and bend radii from the cut sheets |
| 1.2 | round 3 (2026-11-04): its ends are plug-m12 1.1 |
| 1.1 | each end is a plug-m12 (coded insert with pin or socket contacts as elements, knurled nut, seal on a female end); `genders` (end A - end B: male-female, male-male, ...) and `conditions_a` / `conditions_b` (a bent or pushed-back pin) as params a connections.csv row passes; the cable leaves each overmould straight and is sampled about 150 times whatever its length |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
