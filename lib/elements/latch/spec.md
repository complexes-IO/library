# latch · v1.0 · quarter-turn fastener, generic, stud 21 long with knurled slotted knob Ø20, grommet and receptacle, for a 2.0 panel on a 2.0 flange

**What** A quarter-turn fastener: the set that holds a removable panel (a guard, a cover, an access door, a rack's blank plate)
on a frame and lets it off without unscrewing anything. A steel stud with a knurled, slotted knob and a cross pin sits captive in
the removable panel in a grommet; a pressed-steel receptacle riveted under the frame's flange has a keyhole in its base and cam
plates. Pushed in and turned a quarter turn, the pin passes the slots and locks across them under the cam plate; a quarter turn
back frees it and the panel lifts off, stud and grommet with it. The inventory row lists it as "latch / quarter-turn lock" for the
guards, covers and enclosure panels of the machine rows (lib/machines-factory.txt); no system row names it on its own.
**Class** device · **Baseline** our own design: generic quarter-turn fastener stud (ETIM 10.0 EC011966 Stud (quarter turn
fastener)), with its grommet and receptacle, OPERATING.md 12 "Generic elements" (EM, 2026-11-07); lib/inventory.csv marks the row
own_design "yes" with etim EC011966 (the class and its six features are on file, so the element is built generic and states its
class values). No product was matched and no vendor file was opened. The holes it meets are on file (ISO 273); every other size
is a design choice.
**Units / frame** mm, Z up. Origin: the removable panel's outer face plane (z = 0) on the stud's axis. +z is toward the operator
(the knob, z 1 to 9); −z goes into the panel (z 0 to −2), the frame's flange (z −2 to −4) and the receptacle under it (z −4 to
−14.2); the stud's tip is at z −20. Extents x ±20, y ±10, z −20 to 9.
**Built with** toolkit 1.3 · AutoLISP command `LATCHQT` · no parameters.

## Class values
ETIM 10.0 class EC011966 Stud (quarter turn fastener) (ETIM International, ODC-BY 1.0; lib/standards/etim/README.md), every
feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to. These define the
element.

| # | feature | value |
|---|---|---|
| 1 | Material (EF002169) | steel (lib/materials.csv steel-mild; the grade not stated): the stud, the grommet and the receptacle |
| 2 | Surface protection (EF000139) | zinc-plated (the stud and the grommet); the receptacle bright spring steel |
| 3 | Screwing system (EF000013) | slot (a 14 × 2 slot across the knob's top, 2 deep, for a screwdriver or a coin), and the knurled knob by hand |
| 4 | Knurled knob (EF025824) | yes |
| 5 | Length (EF001438) | 21 mm: the knob's underside (its seat on the grommet) to the tip; sized for a 2.0 panel on a 2.0 flange with the receptacle under it (What it meets) |
| 6 | Head diameter (EF001001) | 20 mm, over the knurl ridges (the knob's core Ø18) |

## What it meets
| figure | value | source |
|---|---|---|
| receptacle fixing holes | 2 × M3, Ø3.4 through the base plate at 28 pitch (x ±14) | ISO 273 medium (H13), lib/standards/holes.csv. M3 is this design's choice; rivets or screws and the holes in the frame's flange are the host's (a screw is a common part not built yet: the holes are modelled, the part placed later) |
| the removable panel | 2.0 thick, z 0 to −2, with a hole for the grommet's Ø9 tube | design: the stack this build sits at (the Length class value follows it). The panel's hole, Ø9.2 (0.1 clear round the tube), is cut by the panel's element; the grommet's retaining spring that holds it in that hole is not drawn |
| the frame's flange | 2.0 thick, z −2 to −4, under the panel, with a hole the pin passes | design: the stack; the flange's hole, Ø14 or a 14 × 4 slot along x (the pin is 12 long), is cut by the frame's element. The receptacle's base plate sits against the flange's underside (z −4) |
| the grommet's bore, the plates' bores | Ø7 (0.5 clear round the Ø6 shank), features.csv kind `own` | design choice: the stud turns free in them; no fastener and no standard size |
| the pin's way | a 13 × 4 slot along x through the base plate and the cam plate, on the bore | design choice: the Ø3 × 12 pin passes the slots in line with them (open, 90) and locks across them under the cam plate (closed, 0), 0.5 clear each end and each side |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| knob | core Ø18 × 8 (z 1 to 9), 24 straight knurl ridges 1.2 wide standing 1.0 proud (Ø20 over them), each 7 long (z 1.5 to 8.5), at 15° pitch offset 7.5° so none lies on an axis; slot 14 × 2 × 2 deep along y across the top, inside the core | a knob a hand turns a quarter turn; the ridges stop short of the knob's faces so no two faces lie in one plane (GEO-050); the slot stays inside the core (the ridges begin at r 8.4) so no ridge enters it; the ridges are pressed, not a cut knurl (appearance) |
| shank | Ø6 plain, z −20 to 1 | no thread: a quarter-turn stud is not screwed; the pin does the holding |
| cross pin | Ø3 × 12 along y through the shank, its axis at z −16.2 (its top at −14.7, 0.5 under the cam plate's underside at −14.2) | the locking member; at rest it lies across the slots. The 0.5 is the spring take-up of a real receptacle, not drawn |
| grommet | flange Ø14 × 1 on the panel's outer face (z 0 to 1), tube Ø9 × 2 through the panel (z −2 to 0), bored Ø7 | keeps the stud in the removable panel; the knob seats on its flange (face to face at z 1). Its retaining spring is not drawn |
| receptacle | base plate 40 × 14 × 1.2 (z −5.2 to −4), two legs 1.2 × 14 × 7.8 at its ends (x ±18.8 to ±20, z −13 to −5.2), cam plate 40 × 14 × 1.2 (z −14.2 to −13); keyhole (Ø7 bore + 13 × 4 slot along x) in both plates; 2 × Ø3.4 rivet holes in the base plate | a pressed stirrup riveted under the flange whose cam plate the pin locks behind; 1.2 sheet (thinner than 2.5 × the gate's 0.5 fillet radius, so the gate picks no edge on it and no 1.2 free-corner edge meets its volume rule). The cam ramps that pull the stud in are not drawn: the plate is flat |
| stack | panel 2.0 + flange 2.0, the receptacle 10.2 deep under them | a common guard-sheet stack (guard-panel and the booths are 2.0 sheet); another stack is another Length, a parameter of a later version |
| holding force, torque to turn, vibration resistance | not claimed | no ETIM feature of this class states one; no calculation or test of the model is on file; no locking claim |

## Mechanism
One moving node, `stud` (the knob with its ridges and slot, the shank and the cross pin, one part): rotate about its axis (z)
through the knob's seat (0, 0, 1), range 0 to 90 degrees. At 0 (closed, the rest position as modelled) the pin lies along y,
across the receptacle's slots (which run along x) and 0.5 under the cam plate: the stud can't lift, the panel is held. At 90
(open) the pin lies along x, in line with both slots: the stud lifts out through them with the panel and its grommet. Through the
turn the pin sweeps under the cam plate (0.5 clear), the shank turns in the Ø7 bores (0.5 clear) and the knob turns on the
grommet's flange face to face; nothing else is in its way (the legs are at x ±18.8, the pin's ends at r 6). The axial pull-in a
real cam gives is not drawn. behaviour.csv: state `closed` (default) and `open` (manual toggle: a hand on the knob or a screwdriver
in the slot), pose of `stud` at the range end in `open`.

## Named nodes
`stud`: rotate about z through (0, 0, 1), range 0 to 90 degrees. Colliders: `head` (the knob, x, y ±10, z 1 to 9), `grommet`
(x, y ±7, z −2 to 1), `receptacle` (x ±20, y ±7, z −14.2 to −4); none is named like the node.

## Materials by layer
`M-ZINC` the stud (knob, ridges, shank, pin) and the grommet (steel, zinc-plated) · `M-SILVER` the receptacle (bright spring
steel).

## Decals (Blender)
"complexes.org generic" on the receptacle's base plate underside, beside one rivet hole.

## Notes
No vendor names, part numbers or marks. No load, torque, vibration or locking claim: no figure is on file for them and the
element is not sized against a load. The class values are the figures this design is meant to meet; no calculation or test of
the model is on file. Not drawn: the receptacle's cam ramps and spring, the grommet's retaining spring, the rivets, the panel and
the flange (the hosts'). No open figure: the holes it meets are on file (ISO 273) and the rest are design choices. A quarter-turn
fastener is not a part a dimensional standard shapes (no ISO or DIN sheet for it is on file), so it is built generic to its ETIM
class (OPERATING.md 12); a toggle latch, a slam latch or a swing-handle lock is another class and another element.

## Outputs (out/)
`latch.lsp` · `.glb` (pivot on `stud`) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011966), our own design (mech-r98, unattended, 2026-11-11) |
