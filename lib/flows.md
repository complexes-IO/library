# Flows and layers · electrons, fluid, frames (EM, 2026-11-09 17:50–18:04: "electron flow and fluid flow ... lean and clean"; "view layers ... think how CAD layers work"; "it depends on the machine elements"; "let's do it")

Phase 2's second half (lib/ROADMAP.md). One solver, three flows, layers that exist because an element does.

## One solver

Voltage and pressure are potentials at a node; current and flow are what moves through an edge when there is a difference.
Kirchhoff holds at every node for charge and for oil. toolkit/nets.py already finds the nets and their potentials (phase 1,
ideal). Phase 1.5 gives every edge a conductance and solves the node equations (G·V = I; a sparse linear system, numpy; complex
for AC), so a wire carries a current, a load sees its drop, and a loose terminal (a resistance that jumped) drops the voltage
downstream, derived. Fluid is the same machinery with two nonlinear edge laws and a few Newton steps:

| electricity | hydraulic oil | compressed air |
|---|---|---|
| V, I; V = I·R (Ohm) | p, Q; orifice Q = Cd·A·√(2Δp/ρ) (the valve's Cv/Kv); pipe Δp = f·(L/D)·ρv²/2, f = 64/Re laminar (linear) else Haaland | p, Q; ISO 6358: Q = C·p₁·√(T₀/T₁)·√(1 − ((p₂/p₁ − b)/(1 − b))²), choked below b |
| source holds V | pump Q = Vg·n·η_vol; relief clamps p | compressor and receiver hold p; the regulator clamps it |
| P = V·I | P = Δp·Q | P = Δp·Q |
| capacitor | accumulator p·Vⁿ = const; bulk modulus β | the receiver: p·V = m·R·T |
| load: a resistor | the cylinder: F = p·A, v = Q/A; a leak is a small orifice | the cylinder, and the air compresses |

Data (IT) is the third flow, a scheduler over the same graph rather than a node solve (frames are not conserved): per link a
capacity and a delay, per device what it says and how often (`link`, `talk`, `address` rows). Derived: serialization time = bits /
rate; path latency hop by hop; link load Σ bits/period against capacity (the PLC's RPI fits or not); IEEE 802.3 channel length;
PoE far-end voltage by Ohm's law over the pair resistance; fibre loss budgets in dB; a mask is a number.

Where the figures come from: the elements' behaviour.csv (`load` R, `contact` R, and for fluid `path` Cv, `pump` Q, `relief` p: the
hydraulic contract, request pneu-7; for air the ISO 6358 C and b of each component), the assembly's wires.csv / hydraulic.csv /
air.csv (which pin meets which), and toolkit/derive.py for everything a formula gives. Nothing scripted at the machine.

## Layers (as CAD layers: a name, a visibility, a colour, the discipline that owns it)

A layer exists because the machine's elements carry it: a hydraulic layer because a pump, a valve and a cylinder are joined by
hydraulic.csv; a data layer because two elements' Ethernet pins are wired; a safety layer because a safety relay's inputs and
outputs land somewhere. Take the elements out and the layer goes. The names are the sections already in the files (wires.csv
`section`: 480 VAC power, control & 24 VDC, Ethernet & communication, ground; hydraulic.csv lines; air.csv) plus structure,
mechanism, safety and instruments. Colours are the real wire and line colours (NFPA 79 13.2.4, ISO 1219), so the twin's layer
colours are the panel's. A lesson is a saved view: a named set of layers on, instruments ready. The layer list of a machine is
itself a reading of it (the press: power, control, safety, hydraulic, data; no pneumatic). Few layers, nameable by a student.

A layer toggle is a visibility flag on a group; the solver computes everything and the layers decide what is shown, so a layer can
never show a flow the solver doesn't compute, and the solver never computes a flow no element carries.

## What the student sees, and what we refuse to show

Dots along the wires' and hoses' polylines (wires.csv routes through the ducts, once the panel shop places the wire element):
speed from the solved current or flow, direction from its sign, colour from the potential at that point; they slow and the colour
steps down across a drop (a loose terminal, the overload's heaters, an orifice); in x-ray a conductor glows with its I²R (the
thermal model's heat later). The layer is **current**, drawn as current: a rate and a direction, oscillating on AC, never
"electrons" moving fast (they drift at mm/s; the field is what moves; the HUD says so once). Air dots slow and bunch where it
compresses. Frames are bursts every cycle, link LEDs blink at the solved rate. The instruments are the engineer's: multimeter and
clamp meter, pressure gauge and flow meter, cable tester and ping; each reads the solver's table for the layer it touches.

## The order (lean: in this order, and no further than a lesson needs)

1. Steady state: the nodal solve with drops; meters read; layers toggle; a planted loose terminal on the motor starter's 480 V
   branch and the press's P–A line with its orifice are the first two cases (the planted cases of the selftest).
2. Motion: flow integrates into the ram's position, current into the coil's armature (parts.csv `mass-1d`, `spring`, `coil`).
3. Transients (inductive spikes, water hammer) only when a lesson asks.
4. Faults designed beside the flows, not after: the fault library is the course (ROADMAP 6).
5. A bench: the motor starter cell as metal, EM's Fluke on K1's terminals, the twin's reading against it. The solver is consistent
   long before it is true; the bench is where field experience is not replaceable by a formula.

## The analogy's edges are lessons, not footnotes

Oil is square-root, air chokes and compresses (hydraulics behaves like DC: instant and stiff; pneumatics like an RC circuit:
pressure builds and a cylinder moves soft), data is not conserved (a switch drops frames; the potential is a queue). The picture is
a doorway, not the room.
