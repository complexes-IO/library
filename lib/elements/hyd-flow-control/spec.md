# hyd-flow-control · v1.2 · hydraulic one-way flow control valve, generic, inline, throttle with bypass check, 160 bar, knob set, lock nut

**What** an inline hydraulic one-way flow control valve: oil from `port-1` to `port-2` passes an adjustable throttle; oil from
`port-2` to `port-1` lifts a check and passes free. Placed in a cylinder line it slows the stroke that pushes oil out through the
throttle (meter-out) and leaves the other stroke at full speed. The press-hydraulic design (lib/assemblies/press-hydraulic/design.md,
"the twin should slow the ram"; hydraulic.csv line A) asks for one, and the core's request
(lib/requests/core/pneu-hydraulic-2026-11-09.md item 4) asks the pneu lane for the element. The knob on top sets the throttle; the
lock nut under it holds the setting. No inventory row names it yet: request pneu-8 asks the core for a gap row (OPERATING.md 12).
**Class** device · **Baseline** our own design: generic regulating valve (ETIM 10.0 EC011463), as OPERATING.md 12 (generic
elements, EM 2026-11-07) says. No vendor file was opened or measured. The class values below are its design inputs; its sizes are
design choices. No standard on file shapes it: its ports' standard is not in lib/standards/sources.csv (Open figures), and an inline
flow control has no mounting face standard. No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: port-1's face, the inlet spot face's outer face on the flow axis (x = 0); the flow axis along +x
to port-2, the knob up (+z).
**Built with** toolkit 1.3 · AutoLISP command `HYD-FLOW-CONTROL` · no parameters.

The class: classes.csv has no class named for a hydraulic flow control. EC011463 "Regulating valve" (group EG020069 "Flow control
valves", 45 features on file) lists "Manual throttle" and "Throttle" among its synonyms and carries the features a throttle valve
is chosen by (max. operating pressure, manual operation, preset lockable, the operating element's size). EC010238 "Needle valve"
(valve-needle 1.0's class) was the other candidate: it has no operating pressure feature, so the element's 160 bar would be an open
class A line with no class value behind it; EC011463 states it. The bypass check is part of the valve (a one-way flow control is
one product), not a second element.

## Class values (ETIM 10.0 EC011463)
Design inputs, in ETIM's order (lib/standards/etim/class-features.csv). "not stated": the design has no value for the feature.

| # | feature | value |
|---|---|---|
| 1 | EF001596 Housing material | steel, zinc plated |
| 2 | EF001257 Material quality | not stated |
| 3 | EF000139 Surface protection | zinc plated (the body) |
| 4 | EF023191 Nominal diameter | not stated: the ports' size waits on the port standard (Open figures) |
| 5 | EF006272 Outer pipe diameter | not stated: hose or tube joins through port fittings, not on the body |
| 6 | EF000321 Connection 1 | hydraulic straight-thread port, female, `port-1` (thread and size: Open figures) |
| 7 | EF021872 With coupling connection 1 | no |
| 8 | EF000322 Connection 2 | hydraulic straight-thread port, female, `port-2` (thread and size: Open figures) |
| 9 | EF021873 With coupling connection 2 | no |
| 10 | EF020007 Article compression class | not stated |
| 11 | EF020149 Flange compression class | not stated: no flange |
| 12 | EF021265 Suitable for tap water | no: mineral hydraulic oil ISO VG 46 (ISO 11158 HM) |
| 13 | EF021195 Suitable for hot tap water | no |
| 14 | EF021280 Suitable for central heating water | no |
| 15 | EF020150 Max. pressure difference at 20 °C | not stated |
| 16 | EF020449 Max. operating pressure | 160 bar (hpu-7.5kw 1.1's pressure and its relief setting, hydraulic.csv); in ratings.csv as p_max, status "generic design" |
| 17 | EF023182 Medium temperature (continuous) | not stated |
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
| 36 | EF020151 Length of connection 1 | not stated |
| 37 | EF020153 Working length connection 1 | not stated |
| 38 | EF020152 Length of connection 2 | not stated |
| 39 | EF020154 Working length connection 2 | not stated |
| 40 | EF022273 Height operating element | 32 mm: the body's top face (z = 20) to the knob's top (z = 52) (element.py knob_height) |
| 41 | EF010484 Length operating element | not stated |
| 42 | EF010682 Diameter handwheel | 28 mm (the knob) |
| 43 | EF020158 Spindle angle | 90°: the spindle square to the flow axis |
| 44 | EF021057 With insulation | no |
| 45 | EF014592 Venturi nozzle | not stated |

The pressure is a generic design value (OPERATING.md 12), not a tested rating. No hydraulic check reads it yet (the PNE rules are for
compressed air, toolkit/pneu.py; request pneu-8 proposes HYD rules). The flow it passes at a knob setting is not modelled: the twin
reads no flow from the knob in 1.0. The press's line carries 22 l/min (hpu-7.5kw 1.1); the body is sized for a 1/2 in line (the
hose hydraulic.csv names), a design choice.

**No safety claim.** A throttle that slows a ram is not a safety function: a ram's stop is the directional valve's centre and the
press's safety relay (design.md, EM's sign-off). This element claims no safety function (OPERATING.md 12).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| body | 70 long (x 1 to 71) × 40 × 40, the flow axis through its centre (y = 0, z = 0); zinc plated steel (`M-ZINC`) | holds the throttle, the check and both ports in line |
| port spot faces | Ø26 × 1 proud on each end face, on the flow axis (x 0 to 1.5 and 70.5 to 72, 0.5 into the body) | the joint plane a port fitting meets; 7 of end face round each; no bore cut (Open figures) |
| bonnet | Ø22, from the body's top face to z = 32 (0.5 into the body), over the body's centre (x = 36) | carries the throttle's spindle; 23.5 clear of each spot face in x (x 25 to 47; the spot faces end at 1.5 and start at 70.5; element.py asserts) |
| lock nut | Ø30 × 6 on the bonnet's top (z 31.5 to 38, 0.5 into the bonnet); `M-SILVER` | holds the knob's setting (class value 19) |
| knob | Ø28 × 14 on the lock nut, face to face (z 38 to 52); `M-BLACK-PA` | the operator's setting, five turns shut to open |
| throttle needle, check poppet, spring | not modelled | inside the body |
| overall | envelope 72 × 40 × 72 (x 0 to 72, y −20 to 20, z −20 to 52) | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-1` | hyd-port | female | work | the inlet spot face, x = 0, axis −x | design: 1 the throttled way's inlet, as the pneumatic numbering does; ISO 9461 (hydraulic port identification) not on file. The throttled way runs 1 to 2 |
| `port-2` | hyd-port | female | work | the outlet spot face, x = 72, axis +x | design: 2 the throttled way's outlet, as the pneumatic numbering does; ISO 9461 not on file. The free way runs 2 to 1 through the check |

For meter-out, the cylinder's port joins `port-1` and the directional valve's port joins `port-2`: the oil leaving the cylinder is
throttled, the oil going in passes the check. "hyd-port" is the lane's placeholder unit for a hydraulic port whose thread is open, as
hold-down 1.0's and hyd-cylinder-da-40 1.1's (no hydraulic contract in toolkit/ yet; request pneu-8 proposes one); it is no air unit, so
the PNE checks don't pair it, and no check pairs or rates a hyd-port joint.

## Open figures
- NOT ON FILE (B): the ports' thread and size (no hydraulic port standard, ISO 6149 or SAE J1926, is in lib/standards/sources.csv;
  request pneu-8 proposes SAE J1926-1). The ports are plain spot faces with their pivots; the bores are cut once the standard is on
  file (a major).
- NOT ON FILE (B): ISO 9461, the ports' marks (toolkit/hyd.py H11, request pneu-10's answer item 2: hydraulic port identification;
  lib/standards/sources.csv iso-9461, wanted). The ports are named by their function (1 the throttled way's inlet, 2 its outlet, the
  design's own numbers) and claim no mark of the standard's; when it is on file, hyd.PORT_MARKS takes the marks with their clause
  and a text minor marks these ports from it (hpu-0.37kw 1.0's line).

## Named nodes
`knob` (the adjusting knob): kind rotate about +z at x = 36, 0 to 1800° (five turns), at rest 0 (the throttle shut, a design
choice: the setting is the commissioning engineer's). `port-1`, `port-2` (the spot faces): kind port, fixed (range 0).

## Materials by layer
`M-ZINC` body, bonnet · `M-STEEL-7035` port spot faces · `M-SILVER` lock nut · `M-BLACK-PA` knob

## Decals (Blender)
None in 1.0 (the flow arrow and the "generic" label are a later version). No vendor names, no approval marks.

## Outputs (out/)
`hyd-flow-control.lsp` · `.glb` (knob and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the
QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC011463), pneu-r74 (unattended): inline one-way flow control (throttle 1 to 2, check 2 to 1), 160 bar; body, bonnet, lock nut, `knob` (rotate, five turns), spot faces `port-1` / `port-2`; the ports' thread left open (class B); throttle, check and spring not modelled; nothing placed |
| 1.1 | review pneu-r74 findings 1 and 2, pneu-r80 (unattended): the ports' numbers are a design choice (the pneumatic numbering's way; ISO 9461 not on file) in Ports and behaviour.csv's two pin rows; the bonnet's x gap to each spot face is 23.5, and element.py asserts that gap; class value 12 names the oil "ISO VG 46 (ISO 11158 HM)". Text and an assert only: a minor |
| 1.2 | text only, pneu-r87 (unattended; request pneu-10's answer item 2): the ports' marks added to Open figures as a class B line, ISO 9461 a document wanted (toolkit/hyd.py H11: the ports named by their function, no mark of the standard's claimed; the line lists the standard once in lib/standards/wanted.md). No shape, node, origin or cut-out change |
