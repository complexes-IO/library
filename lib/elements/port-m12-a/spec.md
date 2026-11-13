# port-m12-a · v1.4 · M12 bulkhead socket A / D / L

**What** M12 bulkhead socket A / D / L. Built from the Stage 0 brief `references/measure.md`.
**Class** connector · **Baseline** maker's datasheet: a panel-mount M12 receptacle's 2-D drawing p. 1 (references/measure.md) (18.0 flange, SW17, Ø13.5, 22.6 rear); IEC 61076-2-101; vendor part is front mount, ours rear mount by default (brief). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: cut-out centre: hole centre on the wall's front face y = 0, socket toward −y.
**Built with** toolkit 1.3 · AutoLISP command `PM12` · `coding` (A | D | L), `mount` (rear | front), `panel_t`, `pigtail` · `gender` (female | male), `conditions` (per pole, e.g. '2:spread') · CUTOUT 16.5 (Assumption: M16 clearance).

## Named nodes
`self` (kind port, unit = coding, from receptacle-m12: extras gender, coding, key, thread, seal, torque; coding band A black, D green, L grey) · `insert.c<pole>` (contacts) · `seal` (female)

## Decals (Blender)
insert and pin pattern by coding as a decal; port label from the BOM tag beside the hole

## Notes and assumptions
Figures marked **Assumption** were NOT ON FILE in the brief; a document figure replaces them as a minor version. Exterior only: the interior (mechanism-first ruling) arrives per interior-first-prompt.txt.

## History
| version | change |
|---|---|
| 1.4 | round 4 back (2026-11-04): receptacle-m12 1.3: the female insert is the foremost face, so it stands 12.6 in front of the flange and is the mating plane; the receptacle's body runs to the nut (no second Ø13.5 solid stacked on it) |
| 1.3 | round 4 (2026-11-04): receptacle-m12 1.2 (the thread follows the gender): the female front face stays 12.6 in front of the flange, the mating plane 0.5 behind it; a male port shares the mating plane, its threaded sleeve 8.9 further out |
| 1.2 | round 3 (2026-11-04): its receptacle-m12 1.1 (Ø10.917 sleeve bore, read-back female face, male sleeve over the shroud) |
| 1.1 | the front is a receptacle-m12 (M12 x 1 sleeve, coded insert, socket or pin contacts as elements, face seal), placed as this element's node self, so the port carries its mating data (gender, key, thread, seal, torque) and its contacts; `gender` (female default: the supply side stays touch-safe), `conditions`; the mating plane is the insert face at y = −15.6 (was a decal disc 0.3 proud at −15.9) |
| 1.0 | first build from the Stage 0 brief, toolkit 1.2 |
