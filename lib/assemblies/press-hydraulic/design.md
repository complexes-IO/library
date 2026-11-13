# press-hydraulic · the first whole machine · design (the core, 2026-11-09)

EM 2026-11-08: "this is something the engineer would face in the real world"; 2026-11-09: "I want the engineers to see machines as a
set of elements"; "each machine will have a control panel". This file is the machine as that set, written before its last
elements exist so the panel shop, the lanes and the twin build to one design. bom.csv follows when the pinned elements are on
file; nothing here is geometry.

## The machine, as a person points at it (14 things)

| # | thing | element (lib/inventory.csv) | lane | state 2026-11-09 |
|---|---|---|---|---|
| 1 | frame | frame-welded (own) | mech | 1.1, station 6, waiting on the reviewer |
| 2 | bolster plate | bolster (own) | mech | 1.0, station 6, waiting on the reviewer |
| 3 | power unit | hpu-7.5kw (generic, ISO 4413 values: 160 bar, 22 l/min, 100 l, 7.5 kW 460 V 3~) | pneu | 1.0, station 4 (behaviour.csv) |
| 4 | directional valve | hyd-valve-d03 (4/3, ISO 4401-03 / D03 pattern) | pneu | not started, pin 3 |
| 5 | cylinder | hyd-cylinder-da-40 (generic EC012253: bore 40, rod 22, stroke 200, 160 bar) | pneu | 1.0, station 4 |
| 6 | gauge | hyd-gauge (generic EC011170, 0–250 bar) | pneu | 1.0, station 4 |
| 7 | pressure switch | pressure-switch (generic) | elec | not started, pin 12 |
| 8 | pressure transmitter | pt | elec | not started, pin 11 |
| 9 | ram limits | limit-switch ×2 (top, bottom) | elec | not started, pin 13 |
| 10 | two-hand station | two-hand-control (generic EC001260; op-pb-22-1no ×2, op-estop-22-2nc; ISO 13851) | elec | not started, pin 10 |
| 11 | light curtain | light-curtain (IEC 61496-2 type 4) | elec | not started, pin 8 |
| 12 | e-stop | op-estop-22-2nc | elec | 1.1, station 0 (its brief) |
| 13 | control panel | pnl-press-hydraulic (the panel shop, from controls.csv below; enc-wm, relay-safety-2ch-2no1nc, plc0, hmi-7in and the panel's own devices) | panel | its spec here; enc-wm 1.1 at 6, relay-safety-2ch-2no1nc 1.2 and plc0 1.2 at 4 (behaviour.csv), hmi-7in not started, pin 9 |
| 14 | the machine | press-hydraulic (this assembly: bom.csv places 1–13) | core | this file |

## What the pinned elements make (sizing, from their ratings.csv)

Cylinder bore 40 / rod 22 at 160 bar: piston area 1257 mm², annulus 877 mm²: **20.1 kN pressing (2.05 t), 14.0 kN returning**.
HPU 22 l/min: rod speed 0.29 m/s down, 0.42 m/s up: the 200 mm stroke in 0.7 s. So the press the pins build is a **2-tonne bench
press with a fast ram**, and its 7.5 kW HPU is far larger than its cylinder asks (20 kN × 0.29 m/s ≈ 5.9 kW at full load, less with
a smaller cylinder's flow). It is a true machine and the right first case (one branch, one valve, one cylinder, two safety
functions), and it says what a parametric machine must do later (EM 2026-11-09, "scalable"): tonnage picks the bore, speed picks
the flow, and the frame section follows the force. A 20 t press wants bore 125 at 160 bar; the frame-welded's section is then its
own question (mech). The twin should slow the ram: a flow control in the valve's A line (not in the BOM yet: the pneu lane's call
when the hydraulic circuit is placed) or a smaller pump.

## Sub-assemblies (how bom.csv will group the placements; each a parent for what rides on it)

- **structure**: frame-welded at the origin (floor plane z = 0); bolster on its lower cross-member; the cylinder's mounting plate
  on its upper cross-member; the ram (the cylinder's rod end plate) between the guides.
- **hydraulics**: hpu-7.5kw on the floor beside the frame (its own skid); hyd-valve-d03 on the HPU's manifold (D03 subplate on the
  tank top), blocked-centre spool, and a counterbalance valve in the A line (EM 2026-11-09: decided; its setting derived from the
  ram's mass, p_set = k × W / A_cap, k ≈ 1.3 a design rule; ISO 4413 5.4.6); hyd-gauge and pressure-switch on the P line gauge port; pt on the P line (the HMI's reading); hoses P/T to the valve,
  A/B to the cylinder (hose-hyd and fitting-hyd-iso8434 when placed; hydraulic.csv names the lines).
- **safety**: light-curtain receiver and sender on the frame's front posts (resolution 14 mm, hand protection, mounted at the
  ISO 13855 safety distance: S = 1600 × T + 8 × (d − 14): with d = 14, S = 1600 × T; T = the valve's and ram's stopping time plus
  the relay's response: NOT ON FILE until the elements carry their response times; the twin reports it); two-hand-control on its
  pedestal in front, ISO 13851 type IIIC (synchronous within 0.5 s, both released before a new cycle); op-estop-22-2nc on the two-hand
  station and on the panel door.
- **control panel**: pnl-press-hydraulic (enc-wm wall-mount) on the frame's rear post or the wall; controls.csv is its spec.

## Behaviour the twin must show (from the elements' behaviour.csv once on file; nothing scripted at the machine)

1. Disconnect on → HPU motor starter (panel) runs the pump → P at 160 bar on the gauge and the pt; the pressure switch closes
   above its setting (the PLC's "pressure ok").
2. Curtain clear and both hands on the two-hand station within 0.5 s → the safety relay's outputs close → the PLC's down command
   reaches the valve's solenoid a (A pressurised) → the ram descends until the bottom limit switch → the PLC commands up
   (solenoid b) → the top limit switch → the valve centres (ram held: a P-blocked centre, the cylinder's A and B to tank or
   blocked per the spool the pneu lane gives the element). Releasing either hand mid-stroke: outputs open, the valve centres,
   the ram stops (a stop category 0 on the hydraulic function needs the valve's centre to hold: the spool choice is a safety
   question for EM's sign-off).
3. Curtain broken while the ram descends → outputs open within the relay's response → the valve centres → the ram stops; the
   HMI shows the reason (the relay's 41–42 and the PLC's input).
4. Faults to inject: a stuck solenoid (the ram keeps moving: the curtain stops nothing, which is why the valve's centre matters);
   a loose terminal on the solenoid coil (24 V at the panel, nothing at the coil: the probe finds it); the pressure switch set
   above the relief (never "pressure ok"); a muted curtain (ISO 13849: a fault the PLC must detect through the relay's feedback).

## Files of this assembly

- design.md (this), controls.csv (the panel shop's spec), circuits.csv (the ratings checker's single-line view), hydraulic.csv (the
  hydraulic lines: a pneu lane contract for hydraulics is a request, pneu-7, like air.csv for air; until then the file is the
  design, not a check).
- To come: bom.csv (when hyd-valve-d03, two-hand-control, light-curtain, pressure-switch, pt, limit-switch, hmi-7in are on file),
  assembly.py, wires.csv and sources.csv (the panel shop's, for pnl-press-hydraulic; the machine's field wiring here), the twin
  scene lib/toolkit/twin/scenes/press-hydraulic.json.
