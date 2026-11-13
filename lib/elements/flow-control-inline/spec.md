# flow-control-inline · v1.0 · pneumatic one-way flow control valve, generic, in line, NPT 1/4, throttle with bypass check, 10 bar, knob set, lock nut

**What** an in-line pneumatic one-way flow control valve (a speed controller): air from `port-1` to `port-2` passes an adjustable
throttle; air from `port-2` to `port-1` lifts a check and passes free. Placed between a directional valve and a cylinder port it
slows the stroke whose air passes the throttle and leaves the other stroke at full speed. The knob on top sets the throttle; the
lock nut under it holds the setting. It is the lib/inventory.csv row `flow-control-inline` ("flow control valve, inline / banjo",
own_design generic, made_of fitting-pushin x2): this is the in-line form; the banjo form (a swivel body screwed into a cylinder
port) is not built. valve-needle 2.0 is the sibling without the check: it throttles both ways.
**Class** device · **Baseline** our own design: generic regulating valve (ETIM 10.0 EC011463), as OPERATING.md 12 (generic
elements, EM 2026-11-07) says. No vendor file was opened or measured. The class values below are its design inputs. What it meets
takes its figures from the pneumatic contract, `toolkit/pneu.py` (D1 threads, D7 names, pneu.NPT for the bores); every size the
contract and the standards on file don't fix is a design choice (below). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: port-1's end face centre on the port axis, in line: the port axis is the x axis, the throttled
way along +x, the knob toward +z, the label face toward −y. Ports follow pneu.py's port frame: the pivot on the port's number
field's outer face (0.2 out from the end face, where a placed male's hex seats), its axis out of the body toward the counterpart.
**Built with** toolkit 1.3 · AutoLISP command `FLOW-CONTROL` · no parameters.

The class: the inventory row names none. classes.csv has no class named for a pneumatic flow control. EC011463 "Regulating valve"
(group EG020069 "Flow control valves", 45 features on file) lists "Manual throttle" and "Throttle" among its synonyms and carries
the features a throttle valve is chosen by (max. operating pressure, manual operation, preset lockable, the operating element's
size); hyd-flow-control 1.1 is the same class for oil. EC010238 "Needle valve" is valve-needle's class and has no operating
pressure feature; EC010590 "Compressed air valve" (synonyms "Air cock", "Air tap") is a shut-off cock, valve-air-shutoff's kind.
The bypass check is part of the valve (a one-way flow control is one product), not a second element.

## Class values (ETIM 10.0 EC011463)
Design inputs, in ETIM's order (lib/standards/etim/class-features.csv). "not stated": the design has no value for the feature.
ETIM's features for this class are written for piped water valves; a feature an air flow control has no use for is "not stated"
or "no".

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | brass |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000139 Surface protection | none: bare brass |
| 4 | EF023191 Nominal diameter | not stated: threaded ports; no DN is claimed |
| 5 | EF006272 Outer pipe diameter | not stated: tube joins through port fittings, not on the body |
| 6 | EF000321 Connection 1 | female thread NPT 1/4, `port-1` (pneu.py D1) |
| 7 | EF021872 With coupling connection 1 | no |
| 8 | EF000322 Connection 2 | female thread NPT 1/4, `port-2` (pneu.py D1) |
| 9 | EF021873 With coupling connection 2 | no |
| 10 | EF020007 Article compression class | not stated: no PN class is claimed |
| 11 | EF020149 Flange compression class | not stated: no flange |
| 12 | EF021265 Suitable for tap water | no: compressed air |
| 13 | EF021195 Suitable for hot tap water | no |
| 14 | EF021280 Suitable for central heating water | no |
| 15 | EF020150 Max. pressure difference at 20 °C | not stated |
| 16 | EF020449 Max. operating pressure | 10 bar, as fitting-pushin 2.0's, check-valve 2.0's and valve-needle 2.0's; in ratings.csv as p_max, status "generic design" |
| 17 | EF023182 Medium temperature (continuous) | −10 to 60 °C (compressed air; valve-needle 2.0's range) |
| 18 | EF021866 Stroke length | not stated: the throttle needle is not modelled |
| 19 | EF014529 Preset sealable/lockable | yes: the lock nut under the knob holds the setting (modelled, fixed) |
| 20 | EF002978 Suitable for manual operation | yes: the knob |
| 21 | EF022760 Motor-controlled | no |
| 22 | EF020105 Thermostatic | no |
| 23 | EF016118 Hydraulic balance control | not stated |
| 24 | EF014530 Type of actuator | manual knob |
| 25 | EF020078 With drain valve | no |
| 26 | EF002167 With thermometer | no |
| 27 | EF022469 With position indicator | no |
| 28 | EF022471 With measuring nipples | no |
| 29 | EF020104 With extended measuring nipples | no |
| 30 | EF020193 With measuring connector | no |
| 31 | EF001006 Measurement principle | not stated |
| 32 | EF017707 Venturi tube | no |
| 33 | EF020721 With impulse pipe connection | no |
| 34 | EF021251 Kv value | not stated |
| 35 | EF022466 Kvs value | not stated |
| 36 | EF020151 Length of connection 1 | 10.2 mm: NPT 1/4's thread length L2 (pneu.NPT, 10.205); the bore is L2 + 2 deep |
| 37 | EF020153 Working length connection 1 | not stated: ETIM's working length is a piped valve's face-to-centre length; an in-line body threaded at both ends has none of its own |
| 38 | EF020152 Length of connection 2 | 10.2 mm: as 36 |
| 39 | EF020154 Working length connection 2 | not stated: as 37 |
| 40 | EF022273 Height operating element | 29 mm: the body's top face (z = 12) to the knob's top (z = 41) (element.py knob_height) |
| 41 | EF010484 Length operating element | not stated |
| 42 | EF010682 Diameter handwheel | 18 mm (the knob) |
| 43 | EF020158 Spindle angle | 90°: the spindle square to the port axis |
| 44 | EF021057 With insulation | no |
| 45 | EF014592 Venturi nozzle | not stated |

The pressure is a generic design value (OPERATING.md 12), not a tested rating. The flow it passes at a knob setting is not
modelled: the twin reads no flow from the knob in 1.0, and no cylinder speed is claimed.

**No safety claim.** A throttle that slows a cylinder is not a safety function; this element claims none (OPERATING.md 12). The
inventory row's `safety` column is empty.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 44 (x, along the port axis) × 24 (y) × 24 (z), brass (`M-BRASS`), centred on the port axis in y and z | carries both ports on its end faces, the throttle and the check between them; 5.19 of wall round each bore |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, on the port axis, one in each end face | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0, gauge-p), so a placed male meets the bore face to face (tank 2.0's rule); deeper than a male's make-up L1 + L3 (10.02); 19.59 of body between the two floors, 5.19 of wall round each (element.py asserts at least 10 and 5). Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it; `M-WHITE-PA` | the ISO 11727 number is a decal; 0.2 proud for GEO-050; each port's pivot on its outer face (filter-air 3.0's rule) |
| bonnet | Ø16, from the body's top face (z = 12) to z = 22 (0.5 into the body), brass, over the body's centre (x = 22) | carries the throttle's spindle |
| lock nut | Ø20 × 5 on the bonnet's top (z 21.5 to 27, 0.5 into the bonnet); `M-SILVER` | holds the knob's setting (class value 19) |
| knob | Ø18 × 14 on the lock nut, face to face (z 27 to 41); `M-BLACK-PA` | the operator's setting, five turns shut to open (class values 40 and 42) |
| travel | 5 turns shut to open, counter-clockwise seen from above opens | the spindle's rise is not modelled: the knob turns in place |
| label field | 28 × 10, 0.2 proud, centred on the body's label face (−y) | "complexes.org generic" and the throttled way's arrow 1 → 2 |
| throttle needle, check, spring | not modelled | inside the body |
| overall | envelope 44.4 × 24.2 × 53 (x −0.2 to 44.2, y −12.2 to 12, z −12 to 41) | |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | work | pneu.py D1 (NPT, ASME B1.20.1), D7 (ISO 11727: 1); pivot at x = −0.2 (the field's outer face), axis −x. The throttled way runs 1 to 2 (a design choice, hyd-flow-control 1.1's) |
| `port-2` | NPT1/4 | female | work | as above (ISO 11727: 2); pivot at x = 44.2, axis +x. The free way runs 2 to 1 through the check |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002). pneu.NPT holds NPT 1/4's
figures as values calculated from ASME B1.20.1's formulas (EM 2026-11-07): E1 + h = 13.616 (the bore), L2 = 10.205 (the bore is
L2 + 2 deep), L1 + L3 = 10.02 (a male's make-up). The helix is not modelled: the bore is the thread drawn plain. A male seated on
the field's face reaches L2 − 0.2 = 10.0 past the end face, inside the 12.205 bore.

Both ports carry role work: the valve sits in a working line between a directional valve's port 2 or 4 and a cylinder's port,
never on the supply. Which way round is the circuit's choice. Meter-out (the usual way for a double-acting cylinder, a design
note, no standard cited): the cylinder's port joins `port-1` and the directional valve's port joins `port-2`, so the air leaving
the cylinder is throttled and the air going in passes the check. Meter-in: the other way round.

## Open figures
None.

## Ratings (ratings.csv)
p_max 10 bar, status "generic design", source class value 16 (EF020449 Max. operating pressure). 10 bar ≥ P_SUPPLY (689.5 kPa):
PNE-003 passes on a bench line.

## Named nodes
`knob` (the adjusting knob): kind rotate about +z at x = 22, on the lock nut's top face, 0 to 1800° (five turns), at rest 0 (the
throttle shut, a design choice: the setting is the commissioning engineer's). `port-1`, `port-2` (kind port, fixed; range 0; each
the number field with its pivot on the field's outer face).

## Materials by layer
`M-BRASS` body, bonnet · `M-SILVER` lock nut · `M-BLACK-PA` knob · `M-WHITE-PA` fields

## Decals (Blender)
None in 1.0 (the port numbers 1 and 2 on their fields, the throttled way's arrow and "complexes.org generic" on the label field
are a later version). No vendor names, no approval marks.

## Notes
In line: it is carried by its fittings (fitting-pushin 2.0, or another male NPT 1/4, placed by the assembly in each port, as
check-valve 2.0's and vacuum 2.0's are: the tube size stays the cell's choice). It has no mounting holes; a panel nut or the
banjo form is a later version or a sibling. The id is the inventory's; under OPERATING.md 6's convention it would carry its form
and size (request pneu-10 asks the core about the lane's ids).

## Outputs (out/)
`flow-control-inline.lsp` · `.glb` (knob and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the
gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011463), pneu-r83 (unattended): in-line one-way flow control (throttle 1 to 2, check 2 to 1), 10 bar; body, bonnet, lock nut, `knob` (rotate, five turns), female NPT 1/4 `port-1` / `port-2` bored Ø (E1 + h) × (L2 + 2) deep from pneu.NPT, pivots on the number fields' outer faces; throttle, check and spring not modelled; nothing placed |
