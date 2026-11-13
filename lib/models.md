# Shared behaviour models · v0.1 (2026-11-03)

The physics layer under the library. A sub-element in `parts.csv` names one model in its `model` column and supplies its
parameters; a device's behaviour is its sub-elements wired together, as `behaviour.md` describes. `principles.csv` maps every
principle to the model that implements it and the elements that teach it.

Where each model runs: **viob** (the PLC scan, discrete) · **solver** (server, fixed step 1 ms, lumped models) · **godot**
(visible motion, 60 Hz, reads the solver's states) · **twin-api** (the boundary; latency, cycle and sync rules live there once).

| model | state | parameters (each cited in parts.csv or NOT ON FILE) | used by | fault = a parameter change |
|---|---|---|---|---|
| `mass-1d` | x, v | m, b, end stops, preload | armature, plunger, valve spool, cylinder rod | friction ↑ (sticky), end stop worn |
| `spring` | x | k, free length, preload, cycles to fatigue | return springs, contact springs, button springs | k ↓ (fatigued), broken (k = 0) |
| `rot-mass` | ω, θ | J, b (viscous), T_c (Coulomb), load torque | motor rotor, fan, pump, drum, shaft | b ↑ (bearing wear), seized |
| `gear-stage` | — | i, η, backlash, J_reflected | gear-reducer, planetary, belt stage | backlash ↑, η ↓ |
| `coil` | i | R, L, N, pull-in V, drop-out V, F(gap) curve; P_nom, V_max (continuous), t_operate / t_release (added 2026-11-03, relay brief); P_closing (inrush) (contactor brief) | relay, contactor, solenoid valve, breaker magnetic trip | open (R = ∞), shorted turns (R ↓, L ↓), low voltage |
| `contact` | closed / open, R_c | gap, material, R_c new, erosion per operation, rating; I_min at V_min (dry-circuit threshold), t_bounce, U_open (dielectric, offline) (added 2026-11-03, relay brief); over-travel, I by utilization category (AC-1 / AC-3 / AC-4, AC-15 / DC-13), I_make, I_break, t_nonoverlap N.O. / N.C. (contactor brief) | relay and contactor contacts, switches, terminals | welded, pitted (R_c ↑, intermittent), loose (R_c ↑ → heat) |
| `circuit` | node voltages, branch currents | R per branch, sources | every wired path (from connections.csv) | open wire, short, high-resistance joint |
| `circuit-ac` | phasors per line | V_L, f, phase order | 480 V branch, transformer primary | phase loss, phase reversal, unbalance |
| `rc` | v | R, C | PSU output, analog input filter, debounce | C ↓ (aged caps → ripple ↑) |
| `thermal` | T | R_th, C_th, heat in (I²R, losses), ambient, trip T | bimetal, motor winding, terminal, PSU | R_th ↑ (blocked fan), ambient ↑ |
| `induction-motor` | ω, i, T | P_n, V_n, f_n, poles, slip_n, I_start/I_n, T_start/T_n, J | motor-iec71-370w | phase loss (single-phasing), bearing (→ rot-mass), winding heat |
| `pneu-chamber` | p | volume, orifice Cv, supply p | cylinder, valve-bank, vacuum | leak (orifice to atmosphere), low supply |
| `hyd-chamber` | p | volume, bulk modulus, orifice, relief p | hyd-cylinder-da-40, hpu-0.37kw | internal leak, relief stuck |
| `transfer` | output | range, transfer curve, hysteresis, response time, noise σ, resolution | prox, photo-eye, pressure, temperature, flow, level | drift (offset), dirty lens (gain ↓), stuck output |
| `encoder` | count | ppr, channels, max frequency | encoder, servo feedback | lost counts, channel B dead |
| `wear` | cycles, hours | life (L10, operations), rate; B10, B10d (IEC 60947-4-1 Annex K) (added 2026-11-03, contactor brief) | bearings, springs, contacts | life consumed → parameter of the host model changes |
| `vib` | velocity RMS by order | imbalance, misalignment, bearing defect frequencies | motor, pump, coupling | each defect adds its order |
| `latch` | latched / free | trip force, reset force (also the relay's lock-down door, 2026-11-03) | breaker trip-free latch, E-stop head, overload reset | won't latch, won't reset |

Not models (they live in viob, not the solver): PLC logic, sequencing, interlocks, state machines, alarms, PID, motion profiles.
Offline only (checked when designing, not simulated live): stress, material strength, tolerances, load distribution, safe distance, IP rating.
