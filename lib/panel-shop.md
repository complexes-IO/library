# The panel shop (lane panel; this file and lib/panel-types.csv are the core's) · EM 2026-11-08: "we should have a panel shop"

A machine's builder writes the controls spec; a panel shop builds the enclosure to it and ships it as its own unit with its own
drawings. That is how it works in the trade, and it is how the library works from today: the panel shop is the fourth lane, and a
control panel is its own assembly (lib/assemblies/pnl-<name>/), built from the spec a machine hands over, never part of the
machine's own assembly. The machine places the panel as one unit and never knows what is inside; the panel shop never knows the
machine beyond its spec. Wiring inside the panel is the shop's product.

## Stock: panel types (lib/panel-types.csv)

A panel type is an enclosure family plus the arrangement rules, not a fixed bill of elements: which rails and ducts, where the
terminals go, which operators the door carries, the clearances. The shop picks the type from the spec; a spec no type fits is a
request to the core (a new type is the core's to add, with EM).

## In: the controls spec (lib/assemblies/<machine>/controls.csv)

One row per point the panel must serve. The machine's lane writes it (today the core, for mc-motor-1); the panel shop reads it and
nothing else about the machine.

| column | meaning |
|---|---|
| point | the point's name, the machine's (start, stop, k1, m1, estop_ok) |
| kind | `DI`, `DO`, `AI`, `AO` (I/O to the controller), `load` (a motor, heater, drive the panel feeds), `safety` (a safety function the panel implements), `power-in` (the supply the panel takes), `comm` (a network link), `field-power` (a supply the panel gives the machine) |
| signal | the electrical form: `24VDC NO`, `24VDC NC`, `4-20mA`, `0-10V`, `480V 3ph`, `24VDC`, `Ethernet`; for a load its voltage and phases |
| rating | the figure the panel must meet: a load's full-load current or kW, a supply's amperes, a safety function's category / PL |
| device | the field element and port the panel's wire reaches (`machine-1.pbs-1.s-x1`, `machine-1.m1.pwr`): where the cable lands |
| section | the wiring section it belongs to (480 VAC power, control & 24 VDC, Ethernet & communication, ground) |
| standard | what fixes the point's form (IEC 61131-2 type 3 input, NFPA 79 9.2.5.4 stop category, NEC 430) |
| note | anything the shop must know and nothing it needn't |

## Out: the panel assembly (lib/assemblies/pnl-<name>/)

- bom.csv: the enclosure, rails, ducts, devices, terminals, door operators, ports, nameplates: every element placed, versions pinned.
- terminals.csv: the terminal plan: strip, terminal number, what lands on each side (device.pin or field point), wire number.
- wires.csv: every wire: number, from device.pin, to device.pin, section, gauge (AWG, per lib/standards/nec-conductors.csv),
  colour (NFPA 79 13.2), the duct route (which ducts it runs in, in order), length, `when` (blank for a real wire; an input name
  for an outside contact the twin's input stands for, lib/behaviour.md). The wire element is placed from it, and the solver
  (toolkit/nets.py) runs the panel from it: `python lib/build.py nets <panel> q1.on=1 ...` shows every net's potential and what
  each device sees before any gate runs. The pins are the elements' behaviour.csv marks (`k1.A1`, `f1.95`).
- sources.csv: what feeds the panel from outside (the incoming supply on the disconnect's line terminals, PE): pin, kind (VAC /
  VDC), value, phase, `when`. pm-motor-starter's is the model.
- assembly.py: builds the panel from the three files through the toolkit (no geometry of its own).
- spec.md: what the panel does, the spec it was built to (the controls.csv rows, by point), the type, the enclosure fill, the
  heat load, the short-circuit current rating it claims, every open figure marked as the elements' are.
- The drawings come later (ROADMAP 4): layout, terminal plan, wire list, from these files with no hand edits.

## Rules the shop builds to (cite the clause; a rule the toolkit checks gets a PNL-0xx code)

- UL 508A (Industrial Control Panels): spacings, wire bending space, SCCR, wiring methods. To buy: lib/standards/sources.csv.
- NFPA 79 (Electrical Standard for Industrial Machinery, 2024): supply disconnect (5.3), overcurrent protection (7), motor
  circuits (7.2), control circuits (9), stop functions and e-stop (9.2.5.4), conductor colours (13.2), wiring practices (13),
  enclosure marking (16). Free to view (NFPA online access): read attended, figures into a standards table with their clause.
- NEC (NFPA 70, 2023): Article 430 (motor branch circuit: 430.52 protection, 430.22 conductors), 409 (industrial control panels),
  Chapter 9 Tables 8 and 5 (lib/standards/nec-conductors.csv).
- IEC 60204-1 where a machine is built for both markets; IEC 61439 for the MCC section.
- NFPA 70 110.26 working space in front of the panel is the machine's (where it stands), not the shop's.
- Checked by the toolkit (toolkit/v_panel.py, request panel-4 4; `python lib/build.py assembly <id>` runs them on one panel):
  PNL-010 every end of a numbered wire is a tag of the assembly and a pin mark of its element's behaviour.csv; PNL-030 the
  terminal plan and the wire list name the same wires on the same sides. PNL-020 (conductors a clamp) waits on term-4mm's brief.

## The line

A panel goes through the same stations as an element (OPERATING.md 13): its spec and sources (station 1: every point of the
controls.csv served, every rating met by a device with that rating on file), static checks (2: fill, clearances, duct fill, every
wire's gauge and colour), the mechanism (3: doors, operators), performance (4), ratings and safety (5: ERC and ELR on its circuits,
SCCR), the real tools (6), the reviewer and EM (7), the tag (8). The machine that ordered it pins its version.

## First job: pnl-motor-starter, from mc-motor-1's spec

lib/assemblies/mc-motor-1/controls.csv is the bench's spec, written by the core from the cell's connections.csv and circuits.csv
and the first lab's channel map. The shop's first round builds pnl-motor-starter to it: it may start from pm-motor-starter's bom.csv
(the panel the core laid out by hand, 2026-11-03), and it adds what that panel never had: terminals.csv and wires.csv, with every
wire routed through the ducts. When pnl-motor-starter passes, dm-motor-starter-cell places it instead of pm-motor-starter, and
pm-motor-starter is retired. What the solver found on pm-motor-starter (2026-11-09, lib/requests/core/needs-em.md): the panel has no
control transformer, so its 85–264 VAC PSU would see 480 V (or 277 V to ground, also over); pnl-motor-starter needs one
(xfmr-control, elec pin 5, not yet built: a request to elec through the core, or the panel waits on it at the spec's
control_power row), fed through a 2-pole control-circuit breaker from two phases, with the 120 V secondary's X2 grounded
(NFPA 79 8.2.1, 9.1.1). The core's pm-motor-starter/wires.csv and sources.csv show the form.

## Coming: routing by the toolkit (EM 2026-11-09, lib/ROADMAP.md)

The route and length columns of wires.csv will be computed: the ducts' graph from the BOM, each terminal to the nearest duct
opening, shortest path, every segment's fill against the standard, lengths with the drop and the strip. Until the tool lands the
shop writes them by hand as the card says; what it writes now becomes the tool's first check.

## Second job: pnl-press-hydraulic, from press-hydraulic's spec

lib/assemblies/press-hydraulic/controls.csv (the core, 2026-11-09; design.md beside it) is the first whole machine's spec: an
HPU motor branch with a control transformer, two valve solenoids through a safety relay's outputs, a two-hand station and a light
curtain as the safety inputs, two limit switches, a pressure switch and a transmitter, the HMI on the door. Type: a wall-mount
(enc-wm) motor-starter-plus-safety panel; if no type in lib/panel-types.csv fits, a new type is a request to the core.

## Ownership (lib/OWNERS.csv is the library terminal's: it adds these rows at the lane's first merge)

```
lib/assemblies/pnl-*/*,panel,the panel shop's control panels (EM 2026-11-08)
lib/assemblies/*/controls.csv,core,a machine's controls spec for the panel shop (the machine's lane writes it: the core today)
lib/rounds/panel/*,panel,
lib/needs-em/panel.md,panel,
lib/requests/panel/*,panel,
lib/metrics/panel.csv,panel,
```
Until then a panel file the owners check flags as nobody's is the panel shop's.
