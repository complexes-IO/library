# The behaviour spec · every element (EM, 2026-11-09)

EM, 2026-11-09 02:04: "this should emerge from the elements properties themselves ... if we're creating the set elements from the
sub elements then the behaviors should emerge from the complete set"; 02:08: "every electrical and mechanical element gets a
behaviour spec". So a machine's behaviour is never written at the machine: the twin's `rules` block (lib/toolkit/twin/scenes/) goes
away. Each element says what it does at its own terminals and joints, in a machine-readable file; the assembly says only where
things sit and which pin is wired to which (bom.csv, wires.csv); the solver (lib/toolkit/nets.py) runs the wired set and the twin
reads the result. Seal-in, interlocks, a motor that single-phases, a loose terminal that drops voltage: none of it is written
anywhere; it falls out of the elements and the wiring, the way it does in the field.

## The file: lib/elements/<id>/behaviour.csv

Beside `behaviour.md` (the prose EM reviews: states, transitions, failure modes, grading hooks; unchanged) and `parts.csv` (the
sub-elements and their physics models, lib/models.md). The csv is the part the solver runs. Every figure cites its document or is
NOT ON FILE (OPERATING.md 6); a figure the twin reports is class A (OPERATING.md 12).

    kind,a,b,part,when,value,unit,source,note

| kind | a | b | part | when | value / unit | what it says |
|---|---|---|---|---|---|---|
| `pin` | the mark printed on the part (1, 2, A1, 13, L1, +, S11) | the port node the probe touches (`t-a1`; a multi-pin port by its node, `main`) | the terminal in parts.csv | | tightening torque, `N·m` (NOT ON FILE allowed; `not claimed`; see below) | a terminal: its mark, where it is, its screw's torque. A pin with no port node is a REVIEW (BEH-020): the twin can't probe it until the lane adds the node |
| `contact` | pin | pin | the contact in parts.csv | a state name or an expression | R closed, `ohm` | a–b are one conductor while `when` holds, open otherwise; `always` for a pass-through (an overload's heater path, a terminal block's two sides) |
| `load` | pin | pin | the load in parts.csv | optional | R `ohm`, or P `W` at the load's rated V | a–b is a load (coil, lamp, PSU input, winding); the solver gives it V and I |
| `source` | + pin | − pin | the source in parts.csv | optional | V, `VDC` or `VAC` | a–b supply V while `when` holds (a PSU's output once its input is up). Three-phase supplies live at the assembly (sources.csv), not in an element |
| `state` | state name | | the thing that holds the state (magnet-system, latch, door) | expression, or `default`, or `hold`, or `manual [toggle|latch|momentary] [cleared by <state>]` | | the element's states. Rows of one part are tried in order each solver pass; the first true row wins, so a fault row (tripped) goes above a command row (on); none true: the machine rests at its `default`, unless the part has a `hold` row (a blank name, `when` = hold): then it keeps its previous state (declared hysteresis: the contactor operates at 19.2 V, releases at 9.6 V, holds between). `manual` is an operator's action: the twin exposes it as an input |
| `pose` | node, or several separated by spaces, or `*` (every moving node) | | | a state name or expression | amount in the pivot's unit, or `end` (the pivot's range end) | how the geometry sits in that state; nodes not named sit at rest (0). Emissive nodes light with 1 |
| `link` | state of this element | a state of the element it is mounted on or coupled to | | | | a's state follows b's (a disconnect body's shaft follows the door handle it is coupled to) |
| `limit` | node or part | | | | the figure and unit | a mechanical limit the twin enforces or reports: a door's load, a screw's stroke, a cylinder's force (later phases) |

A `pin` row's torque (request mech-10, core watch 2026-11-11). The value is the figure of the thread or clamp at the pin, by
definition: the screw's own torque for its size and property class (derive.torque, ISO 16047 / VDI 2230 Part 1, the screw taken as
the weakest member), or the terminal's tabulated figure. It is an upper bound the element is never tightened past; when something
of the element's own is weaker than the screw (a stud held by a tube end, an insert bonded to rubber) and nothing on file rates it,
the note says so ("the stud's thread at 8.8: an upper bound; the tube end is not rated"), and a rated figure for that part, when one
comes, is a `limit` row on the part, not a change to the pin's value. When the element has no seat of its own to tighten against (a
body threaded its whole length, set by the host's lock nut or stop; a plug-in contact with no screw), the value is `not claimed` and
the source says who sets it ("not claimed: the host's lock nut sets it (lib/behaviour.md, pin)"): no figure, so BEH-010 takes it and
DOC-005 counts nothing (validate.behaviour_open reads only a value marked NOT ON FILE or Assumption). `NOT ON FILE (B)` is kept for
a torque a standard does tabulate and is not on file (a terminal's IEC 60947-1 torque); a blank value is an older row not yet filled.
Three cases by name (request pneu-13 1, core watch 2026-11-12), each `not claimed` because the pin has no torque of its own to claim:
a tapered pipe thread (NPT) is made up by turns, not torque: `not claimed: made up by turns past hand-tight, not torque (ASME B1.20.1;
pneu.NPT L1 + L3)`; a straight-thread O-ring port (SAE J1926-1) is tightened by the fitting screwed into it, whose stud end carries
the torque: `not claimed: the fitting's stud end sets it (SAE J1926-2 / -3)`, the port's own open thread staying the spec's one
NOT ON FILE (B) line; a terminal the element draws but does not model (a placed motor's box drawn as one solid) names the element
that will carry it: `not claimed: the terminal is not modelled; a placed <id> carries its own (IEC 60947-1)`; when no element of
that kind is on file it names the kind instead (request pneu-15 1, core watch 2026-11-13: chiller's supply terminals),
`not claimed: the terminal is not modelled; the cabinet's terminal block carries its own (IEC 60947-1)`.
A fourth case (request pneu-15 3): a tube end held by a push-in fitting's collet has no thread and nothing is tightened,
`not claimed: held by the fitting's collet, no thread (ISO 14743 push-in)`, on the fitting's tube port and on the tube's ends.
Not a case (request pneu-15 2): a male stud end that IS the element's own pin (a gauge's stem screwed into a host's O-ring port)
has a torque of its own, which SAE J1926-2 / -3 tabulate; it is `NOT ON FILE (B): SAE J1926-2 / -3`, never `not claimed`.
`not claimed` says the pin has no torque to claim, and a stud end has one. The line sits under the same document as the thread's
open line (lib/standards/wanted.md groups by document): it adds no hold the element does not have already, and clears with it.

A `pin` row's `when` names a form of the element, and nothing else (core round 29, request panel-4 item 2): `form <param>=<value>[|<value>]`,
as `form genders=male-open|female-open` in cordset-m12. The element's default row for the same mark stays; in a build whose param has
one of the values the mark sits at this row's node instead (cordset-m12's B1 at `lead-1` in the open-ended form, at
`port-b.insert.c1` with a plug). A form moves a pin; it adds none, so the marks a wire list may end on are the same in every form.
BEH-020 reads each form's nodes in a build of that form (the param set to its first value); the solver joins by mark, and a probe
on a form's node finds its mark (nets.pins_at, twin's probes).
A pin that follows a parameter is a count, not a form (request panel-13 2, core watch 2026-11-13): `count <param>>=<k>` in the pin
row's `when`, as `count poles>=5` on term-jumper's blade 5. The mark has no other row; it is a pin only in a build whose param is at
least k. A comb's blades: pins 1 and 2 plain (the least `poles` builds), 3 to 12 each `count poles>=<k>`, and every contact k to k+1
plain: in an assembly the solver keeps a count pin where the placed build has its node, and drops a contact, load or source that
names a count pin the build lacks (nets.elements), so a 2-pole comb has blades 1 and 2 and contact 1-2, a 7-pole comb 1 to 7.
BEH-020 reads a count pin's node in a build at its k; a wire list may end on any count mark (PNL-010).
A pin that is there for some values of a word parameter is an `only` (request elec-15, core watch 2026-11-13: receptacle-m23's
`kind`, power with 1, 2, 3, PE and signal with 1 to 6): `only <param>=<value>[|<value>]` in the pin row's `when`, as
`only kind=signal` on marks 4 to 6 and `only kind=power` on PE, marks 1 to 3 plain. The mark has no other row; it is a pin only in a
build whose param has one of the values. The solver keeps it where the placed build has its node and drops what names it where
not, as for a count; BEH-020 reads its node in a build at its first value; a wire list may end on it (PNL-010). Two kinds whose
pins differ stay one element when one build makes both (one code, one parameter); a host places the kind it needs.
A form moves a pin, a count adds one for a number and an `only` for a word; nothing else changes the marks.

Expressions (`when`): the element's own state names; `<part>.V`, `<part>.I` for a load or contact named in `part`; `V(a,b)` the
voltage between two of its pins; `and`, `or`, `not`, comparisons, numbers. Nothing else: an element knows only itself. What
another element does reaches it through the wires, as a voltage on its pins.

## What the assembly adds (and nothing more)

- `wires.csv`: `wire,from,to,section,gauge,colour,route,length,when,source,note` with `from`/`to` as `<tag>.<pin mark>` (the panel
  shop's file, lib/panel-shop.md; a cell's cables go through connections.csv and the cable's wiring map as today). `when` names an
  operator's input the wire stands for: an outside contact (a controller's output in another assembly, a field device jumpered at
  the bench test) closed while that input is set; blank is a real wire.
- `sources.csv`: `pin,kind,value,phase,when,source,note`: what feeds the assembly from outside (the incoming 480 V three-phase
  on the terminals, as `L1`/`L2`/`L3` at 277.13 V to ground, phase 0 / −120 / 120; the 0 V of a 24 V supply from another panel).
  `kind` VAC or VDC. `when` names an operator's input the source stands for (a controller's run output that lives in another
  assembly: present while the twin's `run` is set); blank means always present.
- The twin's scene names which manual states it shows and the camera. No rules.
- `python lib/build.py nets <aid> [<tag>.<state>=1 ...]` prints the nets with their potentials, every element's states and what each
  load sees, for one set of inputs.

## The solver (lib/toolkit/nets.py)

Pins joined by wires and by closed contacts are one net. Sources give nets their potential (AC as a phasor, DC as a number);
a load between two nets sees their difference; every element's state rows are evaluated on what its loads see; contacts follow
the states; nets are rebuilt; until nothing changes (a fixpoint, bounded). The meter reads two nets. Phase 1 is ideal (a closed
contact drops nothing, a load draws its rated current); series drops (a loose screw, a long wire) come with the circuit model.

## The twin (lib/toolkit/twin, toolkit/twin.py)

The scene names which of the solver's inputs the operator works (`solver`: `<tag>.<state>` of a manual state, or a `when` name of
sources.csv / wires.csv), with a key and a short label; nothing else. `build.py twin` solves every combination of those inputs
(toolkit/twin.solved) into res://out/<id>-solved.json: poses, flags, each net's potential, the probe points (every pin with a port
node); Godot reads the table and drives the parts; P then two clicks on terminals reads the meter (VAC, VDC, floating). The table is
memoryless: a machine whose behaviour depends on history (a seal-in: the button released, the contactor held through its own
auxiliary) needs the solver live beside Godot, the next step; pm-motor-starter has no such path (the controller holds the command).

## Checks (toolkit/behaviour.py; BEH rules in toolkit/rules.py; station 5)

- BEH-010: the file is on file and well formed: known kinds, pins declared by `pin` rows before use, states defined before use,
  a source on every row, `when` parses and names only the element's own states, parts and pins. REVIEW while missing (every element
  gets one: EM 2026-11-09; the lanes add them to released elements as backlog); FAIL when malformed.
- BEH-020: every pin names a port node that the element builds (the probe can touch it); a form's pin, in a build of that form.
- BEH-030: every `pose` node is a moving node of the element, `end` only where the pivot has a range.

The core may propose an element's spec in lib/requests/core/behaviour/<id>.csv (its own folder); the toolkit reads it while the
element has none, with BEH-010 REVIEW "proposed by the core": the lane copies it in, checks each figure against its brief and
commits, or writes its own. The core wrote the motor starter's set this way on 2026-11-09.

`python lib/build.py behaviour <id>` prints the element's inputs, states, contacts and loads as the solver reads them;
`python lib/build.py behaviour` lists the elements without a file, by lane.
`python lib/build.py behaviour draft [lane] [--write]` (the core's only) drafts the proposal for every element whose spec its own nodes
settle: no port or contact node, no emissive or compress node, no node in lib/motion.csv; the header alone for a structural part,
and per moving node a manual toggle (`<node>-rest` by default, `<node>-end`) posed at its range end (toolkit/behaviour.draft; core
watch 2026-11-09). The lane renames the states by what they mean when it takes the file in.
