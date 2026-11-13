# fan-exhaust · v1.1 · exhaust fan, centrifugal, generic, impeller Ø480, inlet Ø250, discharge 200 x 230 up, motor seat for motor-iec71-370w, 4 × M12 anchor holes

**What** An exhaust (extraction) fan: it draws air out of a paint or powder booth, a dust collector, a fume hood or a ventilated
room and blows it up the exhaust duct. A steel housing on a base plate takes the air in through a round inlet on its −y face and
lets it out through a rectangular discharge straight up from its top; inside, an open impeller with eight radial blades turns on a
horizontal shaft. The shaft runs back through the housing's back wall and a bearing stand to a free end where a coupling meets the
motor; the motor stands on a seat behind, at its own shaft height. lib/machines-factory.txt and lib/machines-from-elements.txt list
it in eight systems (booth-paint, booth-powder, booth-spray-paint, dust-collection-system, fume-extraction-system, hvac-trainer,
powder-coating-system, ventilation-industrial). The impeller is the mechanism: the twin turns it by name.
**Class** machine · **Baseline** our own design: generic centrifugal fan (ETIM 10.0 EC010994), OPERATING.md 12 "Generic elements"
(EM, 2026-11-07); lib/inventory.csv marks the row own_design "generic" (request mech-13's answer, 2026-11-12: generic of EC010994,
built under plain names as conveyor-wheel). No product was matched and no vendor file was opened. The folder held a
catalogue search record from 2026-11-02 (a wall-mount propeller fan, another type), moved to references/source.txt by `build.py own`
(DOC-007); no size is taken from it. The class values below are the design inputs; what it meets is on file (ISO 273, the thread formulas,
motor-iec71-370w); every other size is a design choice.
**Units / frame** mm, Z up. Origin: the floor plane z = 0 (the base plate's underside), x = 0 through the shaft's axis, y = 0 at
the housing's back face. The shaft runs along y at z 420; the inlet opens toward −y, the motor stands at +y, the discharge points
up (+z). Extents x ±350, y −360 to 540, z 0 to 875.
**Built with** toolkit 1.3 · AutoLISP command `FANEXHAUST` · no parameters.

## Class values (ETIM 10.0 EC010994)
Design inputs. EC010994 Centrifugal fan (lib/standards/etim/classes.csv: group EG020066 Fans and ventilators, 56 features) is a
tier-2 class whose features lib/standards/etim/class-features.csv does not list, and none is written from memory. Request mech-13's
answer puts the row's class and its features in the attended ETIM reading (needs-em.md). Until then this table gives the values the
fan is designed to under plain names, as conveyor-wheel 1.0 and rack-cantilever 1.0 do; the next minor version restates them in
ETIM's order with their EF codes, "not stated" where the design has no value.

| value | this element |
|---|---|
| type | centrifugal fan, single inlet, open impeller with radial blades, direct drive through a coupling (the coupling and motor placed later) |
| volume flow at the duty point | 1200 m³/h (ratings.csv `volume_flow`) |
| pressure increase at the duty point | 600 Pa (ratings.csv `pressure_increase`) |
| motor power | 0.37 kW, the output of the motor the seat takes, motor-iec71-370w (ratings.csv `motor_power`) |
| the flow's power at the duty point | 200 W, computed in element.py as volume flow × pressure increase (0.333 m³/s × 600 Pa): below the motor's 370 W |
| speed, efficiency, sound power | not stated: no fan curve, test or calculation of the impeller is on file |
| impeller diameter | 480 mm |
| inlet | round, Ø250, with a collar Ø270 × 60 for the duct |
| outlet | rectangular, 200 × 230 outside (180 × 210 open), vertical (up), with a flange 260 × 290 × 15 and 4 × M8 holes |
| housing material | steel, painted (RAL 7035, layer M-STEEL-7035) |
| impeller material | steel, bright (layer M-SILVER) |
| temperature range, explosion protection, spark-free design | not stated: no figure is designed or claimed; the fan is not for a hazardous area |

## What it meets
| figure | value | source |
|---|---|---|
| anchor holes | 4 × M12, Ø13.5 through the base plate at 620 × 820 (x ±310, y −320 and 500) | ISO 273 medium (H13), lib/standards/holes.csv. M12 is this design's choice. The anchors (anchor-bolt, not built yet) are the assembly's; nothing is placed in the holes |
| floor | the base plate's underside, z = 0 | a flat floor; the floor is the assembly's |
| the exhaust duct | the discharge flange's top face, z 875, opening 180 × 210 (x ±90, y −230 to −20); 4 × M8, Ø9.0 through the flange at x ±115, y −255 and 5 | ISO 273 medium (H13), lib/standards/holes.csv. M8 and the flange's size are this design's choices; the duct and its screws are the assembly's |
| the inlet duct | the collar's outside, Ø270, y −325 to −265, around the Ø250 inlet | NOT ON FILE (B): EN 1506 (circular sheet-metal ducts: their sizes and the slide fit over a spigot). The collar is drawn at the design's Ø270 until that table is on file; the duct and its clamp are the assembly's |
| the motor | the seat's top face at z 349 = 420 − 71, motor-iec71-370w's shaft height (its SH 71, read by library.load), so the motor's shaft lies on the fan's axis; 4 × M6 tapped holes at its foot pattern 112 × 90 (HX, HY, read the same way): x ±56, y 350 and 440, so its shaft end (its drive-end shield face 80 in front of its first foot row, the shaft 30 past it) stands at y 240 | motor-iec71-370w 1.5 (its drawing p. 1 figures, as that element gives them). M6 for its K 7 foot slots; tapped at the minor diameter 4.9175, 12 deep: derived: derive.thread(6.0, 1.0) (ISO 68-1 basic profile; ISO 965-1 clause 10, internal 6H: D1 min; ISO 261 pitch 1), the thread not drawn. The motor is not past station 6, so it is placed in a later version (OPERATING.md 12, quality at the source); its screws are the assembly's |
| the coupling | the fan's shaft end Ø24 at y 200, 40 from the motor's shaft end (Ø14, y 240) | design choices, the fan shaft's Ø24 (drawn at its nominal size) and the 40 gap, facing motor-iec71-370w's shaft end; the coupling (coupling-shaft, not built) is placed in a later version and its two bores are its own |

## GD&T (ISO 273, ASME Y14.5 floating fastener)
The four anchor holes carry a declared position tolerance Ø1.0 at MMC to A (the floor plane), B (the plane x = 0 through the
shaft's axis) and C (the housing's back face, y = 0) (features.csv; T ≤ H − F = 13.5 − 12 = 1.5). The four flange holes carry
Ø1.0 at MMC to D (the flange's top face), B and C (T ≤ H − F = 9.0 − 8 = 1.0).

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| base plate | 700 (x ±350) × 900 (y −360 to 540) × 15 | carries the housing, the bearing stand and the motor seat as one unit, so the fan is set and anchored as one |
| housing | a drum Ø600 × 250 (y −250 to 0) on the shaft's axis, a cavity Ø560 open toward −y, the back wall 15 with a Ø40 way for the shaft | the scroll's envelope: the spiral that widens toward the discharge is not drawn (appearance) |
| housing support | a block 300 (x ±150) × 230 (y −240 to −10) from the base plate to z 125, 5 into the drum's underside (z 120) | sets the drum on the base plate |
| inlet plate | Ø600 × 15 on the drum's rim (y −265 to −250), the inlet Ø250 through it | closes the drum's front; the inlet looks onto the blades' inner part (r 100 to 125) |
| inlet collar | Ø270 × 60 (y −325 to −265), bore Ø250 | the duct's seat, 10 wall |
| discharge duct | 200 (x ±100) × 230 (y −240 to −10) outside, walls 10, from z 701 (in the drum's shell, 1 above the cavity's top at z 700) to z 860; open through | carries the air up; the throat from the scroll into the duct is not drawn (appearance) |
| discharge flange | 260 (x ±130) × 290 (y −270 to 20) × 15 (z 860 to 875), opening 180 × 210 | the exhaust duct's joint |
| impeller | back disc Ø480 × 10 (y −55 to −45), eight radial blades r 100 to 235 × 145 (y −55 to −200) × 3 at 45 degrees, each centred on its radial line (±1.5 either side), hub Ø100 (y −50 to −25), all in M-SILVER | blade tips 45 inside the cavity's wall; the blades' front edges 50 behind the inlet plate; the hub 10 in front of the back wall |
| shaft | Ø24 from the hub (y −40) to its free end at y 200 | through the back wall's Ø40 way and the bearing stand's Ø26 bore, touching neither (the bearings are not drawn) |
| bearing stand | 120 (x ±60) × 80 (y 40 to 120), from the base plate to z 460, bore Ø26 on the axis | where the shaft's bearings go (not drawn); 40 over the axis |
| coupling gap | 40, y 200 to 240 | the coupling's room |
| motor seat | 200 (x ±100) × 200 (y 300 to 500), from the base plate to z 349 | a fabricated pedestal drawn by its outside; its top at the motor's foot plane |
| the motor, coupling, bearings, belt or drive guard, inlet guard, vibration mounts, drain | not drawn | the motor and coupling are placed later; a guard over the coupling is the assembly's (no guard is claimed); the rest is the maker's detail |

## Mechanism
One moving node, `impeller`: the back disc, the blades, the hub and the shaft, rotating about the shaft's axis (along y, through
x 0, z 420), 0 to 360 degrees: a spin, with no stop. The motor, placed later through the coupling, turns it; at rest it stands with a
blade on each axis. It touches nothing as it turns: blade tips and the disc 40 to 45 inside the cavity's wall, the blades 50 behind
the inlet plate, the hub 10 in front of the back wall, the shaft 8 clear of the back wall's way and 1 clear of the bearing stand's
bore. behaviour.csv: state `still` (default) and `running` (manual toggle: the assembly's motor), pose of the impeller at the range
end in `running`.

## Named nodes
`impeller`: rotate about y through (0, −55, 420), range 0 to 360 degrees. Colliders: `base-plate`, `housing` (the drum and the
inlet plate), `inlet` (the collar), `discharge` (the duct and the flange), `support`, `bearing-stand`, `motor-seat` (none is named
like a node).

## Materials by layer
`M-STEEL-7035` the base plate, housing, inlet plate and collar, discharge duct and flange, support, bearing stand and motor seat
(painted steel, RAL 7035) · `M-SILVER` the impeller and its shaft (bright steel).

## Decals (Blender)
"complexes.org generic" on the housing's +x side.

## Notes
No vendor names, part numbers or marks. No flow, pressure, speed, sound or efficiency figure beyond the class values, and no
safety claim: the duty point is the design input the fan is meant to meet, not a tested curve. The fan is not guarded: inlet and
coupling guards (ISO 13857 distances) are the assembly's. Not drawn: the scroll's spiral and throat, the bearings, the motor and
coupling (placed later), a drain, inspection door or vibration mounts. The holes are on file; the anchors, duct screws and motor
screws are the assembly's.

## Outputs (out/)
`fan-exhaust.lsp` · `.glb` (pivot on the impeller) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010994), our own design (mech-r110, unattended, 2026-11-12) |
| 1.1 | review fan-exhaust-1.0 finding 1: each blade's origin offset along the third edge passed to obox (ex × ey), so the eight blades are centred on their radial lines (1.0 stood each 3.0 off it); the node, its pivot, the origin, the cut-outs, extents and colliders unchanged: a minor (mech-r122, unattended, 2026-11-12) |
