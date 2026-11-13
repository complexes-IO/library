# hyd-pump · v1.0 · hydraulic gear pump, generic, external gear, two-bolt flange mounted, side ports

**What** an external gear pump for a hydraulic power unit: the motor turns the shaft through a coupling; the drive gear on the shaft
and the driven gear below it carry oil round the outside of their teeth from the suction port `port-s` (+y side) to the pressure
port `port-p` (−y side), turning clockwise seen on the shaft end. It is flange mounted: its two-bolt flange and pilot go on a bell
housing (the motor bracket) with two M10 screws, and the oil comes in from the reservoir and goes out to the valves through hoses or
tubes on the two side ports. lib/inventory.csv row `hyd-pump` (own_design generic, "hydraulic pump (gear or piston)"; 1 system:
hpu-assembly-station, whose line in lib/machines-factory.txt places it with hyd-tank, motor-iec, hyd-valve-d03, hyd-filter-return,
hyd-cooler, accumulator and hyd-gauge).
**Class** device · **Baseline** our own design: generic gear pump (ETIM 10.0 EC012031), as OPERATING.md 12 (generic elements, EM
2026-11-07) and the inventory row say. No vendor file was opened or measured. Its sizes are design choices; the flange's holes take
their size from ISO 273 (lib/standards/holes.csv). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the mounting face, the flange's front face (x = 0); y = 0 and z = 0 on the shaft's axis. The
pilot and the shaft toward −x, the body and the rear cover toward +x; the suction port on +y, the pressure port on −y.
**Built with** toolkit 1.3 · AutoLISP command `HYD-PUMP` · no parameters.

The class: the inventory row names none, and its type says "gear or piston". EC012031 "Gear pump" (group EG020079 Pumps, tier 2,
synonyms "Hydraulic gear pump", "Pump with gears") is the class lib/standards/etim/classes.csv gives for a hydraulic gear pump; no
piston pump class is in the file, and a gear pump is what a small power unit (the row's system) carries. EC010732 "Block pump"
(coolant-pump's) is a liquid transfer pump, not a hydraulic pressure pump. It fits the row's one system.

## Class values (ETIM 10.0 EC012031)
Design inputs. EC012031 is a tier-2 class on no inventory row, so lib/standards/etim/class-features.csv (tier-1 classes and the
classes the inventory uses) does not list its 20 features: the case request pneu-4 raised for tube-pneu, which the core answered
(lib/requests/core/pneu-4-answer.md): the features come with an attended core session and EM's ETIM download, and the element is
built meanwhile with its design values under plain names, as pump-hand-hyd 1.0's. When they are on main, a minor version restates
this table in ETIM's order with their EF codes, "not stated" where the design has no value.

| feature | value |
|---|---|
| pump type | external gear pump, two gears (a drive gear on the shaft, a driven gear below it) |
| material | aluminium body, flange and rear cover; steel shaft |
| direction of rotation | clockwise seen on the shaft end (design choice: it puts the suction port on +y) |
| mounting | flange, two bolts, with a pilot (the interface open: Open figures 1) |
| shaft end | cylindrical, Ø16 (the key or spline open: Open figures 1) |
| connection | two side ports, suction and pressure, their threads open (Open figures 2) |
| displacement | not stated: the gears are not modelled |
| speed range | not stated: no figure on file gives it |
| max. operating pressure | not stated: a rating with no source on file (Open figures 3, class A); no p_max row in ratings.csv |

The pressure is not stated. A power unit's pump pressure decides the force its cylinders make, so it is a rating that decides what
the twin reports: class A, EM's (OPERATING.md 6). No EC012031 feature is on file to carry a value, and no other figure on file gives
one: hpu-7.5kw's 160 bar is that unit's own value, not this pump's (tube-pneu 1.2 dropped a borrowed figure the same way, review
pneu-r62 finding 1). No hydraulic check reads it yet (the PNE rules are for compressed air, toolkit/pneu.py; request pneu-8 proposes
HYD-001..008). The displacement and the speed would give the flow; with neither stated, the element claims no flow.

**No safety claim.** A power unit's pressure relief is its valve block's (hyd-valve-d03's circuit, hpu-0.37kw); the pump has no relief
of its own modelled or claimed, and its coupling's guard is the host's (OPERATING.md 12).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| flange | 10.5 × 116 × 50 (x 0 to 10.5, y ±58, z ±25), 0.5 into the body | a two-bolt flange: wider than the body (y ±35) and inside its height (z −50 to 30), so no face of it is flush with the body's |
| flange holes | 2 × Ø11.0 through, at y = ±45, z = 0 | M10 clearance, medium (ISO 273 H13, holes.csv); position Ø1.0 to A (the mounting face), B (the pilot's axis), C (the flange's top edge) in features.csv (GDT-010: T = H − F = 1.0); 4.5 between each hole's edge and the body's side, room for a nut behind the flange (asserted); 7.5 of plate past each hole (y) |
| pilot | Ø50 × 6 on the mounting face (x −6 to 0.5, 0.5 into the flange) | centres the pump in the bell housing; its size is a design choice, the standard's open (Open figures 1) |
| shaft | Ø16 × 30 out of the pilot (x −36 to −6), seated face to face on the pilot's end; plain, no key drawn | takes the coupling's hub; its key or spline is the standard's (Open figures 1) |
| gear body | 64 × 70 × 80 (x 10 to 74, y ±35, z −50 to 30) | holds the drive gear on the shaft's axis (z = 0) and the driven gear 24 below it (z = −24), neither modelled; the ports at the mesh, z = −12 |
| rear cover | x 73.5 to 86 (0.5 into the body), y ±33, z −48 to 28 | closes the gear chamber; 2 in from the body's sides, top and bottom |
| port spot faces | suction Ø40, pressure Ø32, each 1 proud of its side face (|y| 34.5 to 36, 0.5 into the body), centred x = 42, z = −12 | the joint plane a fitting meets; the suction port the larger, as a pump's inlet is; no bore cut (Open figures 2); 5 or more of face round each (asserted) |
| overall | envelope 122 × 116 × 80 (x −36 to 86, y ±58, z −50 to 30) | |

## Ports
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-s` | hyd-port | female | (none) | the +y side's spot face, y = 36, axis +y | the suction port: from the reservoir (hyd-tank, once built); no role in pneu.ROLES fits a suction line, as hpu-7.5kw's `port-t` |
| `port-p` | hyd-port | female | supply | the −y side's spot face, y = −36, axis −y | the pressure port: hpu-7.5kw's and pump-hand-hyd's delivery port `port-p`, to the valve block |

"hyd-port" is the lane's placeholder unit for a hydraulic port whose thread is open, as hpu-7.5kw 1.1's, hold-down 1.0's and
pump-hand-hyd 1.0's (no hydraulic contract in toolkit/ yet; request pneu-8 proposes SAE J1926-1 ports); it is no air unit, so the PNE
checks don't pair it, and no check pairs or rates a hyd-port joint.

## Open figures
- NOT ON FILE (B): the mounting flange's interface and the shaft end (the pilot's diameter and fit, the bolt pattern, the shaft's
  diameter, length and key or spline: ISO 3019-1 or SAE J744, neither in lib/standards/sources.csv). Drawn as design choices so the
  element has a shape; a host's bell housing and coupling meet them once the standard is on file (a major).
- NOT ON FILE (B): the two ports' threads and sizes (no hydraulic port standard, such as SAE J1926-1 or ISO 6149, is in
  lib/standards/sources.csv; request pneu-8). Each port is a plain spot face with its pivot; the bores are cut once the standard is
  on file (a major).
- NOT ON FILE (A): the max. operating pressure (Class values): no feature of EC012031 and no figure on file gives it; EM's.

## Named nodes
`shaft`: kind rotate about +x on its own axis (origin x = −6, the pilot's end), 0 to 360°, positive clockwise seen on the shaft
end (the pump's turning direction); a cylinder turning about its axis sweeps only itself. `port-s`, `port-p` (the spot faces): kind
port, fixed (range 0).

## Materials by layer
`M-ALU-ANOD` flange, pilot, gear body, rear cover · `M-ZINC` shaft · `M-STEEL-7035` port spot faces

## Decals (Blender)
None in 1.0 (the "generic" label, the rotation arrow and the "S" / "P" port marks are a later version). No vendor names, no approval
marks.

## Notes
- A host places it on a bell housing with motor-iec and a shaft coupling; the bell housing and the coupling are not elements yet,
  and their fit waits on Open figures 1.
- hpu-0.37kw's inventory row (our own assembly) names `pump` (a centrifugal pump, EC010732) among its parts; a hydraulic power unit's
  pump is this element's kind. The row is the core's (needs-em r77).

## Outputs (out/)
`hyd-pump.lsp` · `.glb` (shaft and port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC012031), pneu-r77 (unattended): two-bolt flange with two M10 clearance holes (ISO 273), pilot, `shaft` (rotate, clockwise seen on its end), gear body, rear cover, spot faces `port-s` and `port-p`; the flange and shaft interface and the ports' threads (class B) and the max. operating pressure (class A) left open; the gears, bearings and seals not modelled; nothing placed |
