principles: m19 e02 e15 e21 a14 x01 x06 x20 x21 x22

# overload-9a-1no1nc · behaviour (as the twin runs it)

Sub-elements and models are in `parts.csv`; models in `lib/models.md`; principles in `lib/principles.csv`. Figures cite `references/interior.md` and its documents (spec = technical-specifications-rw-series.pdf).

## Inputs
- Motor current through L1-T1, L2-T2, L3-T3 (from circuit-ac): heats the three bimetals (I²R, x01).
- Ambient temperature: compensated from -20 to +60 °C; derated above 60 °C (0.94 at 65, 0.87 at 70, 0.81 at 75, 0.73 at 80 °C, spec p. 8).
- Dial setting I_r: 7.0 to 10.0 A, continuously adjustable (cut sheet p. 1, spec p. 2).
- RESET/TEST button: position A / AUTO / HAND / H, and pressed or not (spec p. 2).

## Outputs
- Auxiliary 95-96 (N.C.): in the contactor's coil circuit; opens on trip.
- Auxiliary 97-98 (N.O.): signals the trip (to a PLC input or a lamp); closes on trip.
- Tripped state visible on the front: the documents do not say whether the button moves on trip, so no indicator is declared (NOT ON FILE).
- The main paths L-T stay closed in every state (FIELD KNOWLEDGE): the overload never breaks the motor current itself.

## States (sub-node pose in each)
| state | bimetals | trip slide / latch | 95-96 | 97-98 | button |
|---|---|---|---|---|---|
| cold, running below I_r | warm to the running current, below the trip point | rest, latched set | closed | open | at its position |
| overload (heating) | bending toward the trip point | moving | closed | open | at its position |
| tripped | at or past the trip point | released | open | closed | at its position |
| cooling (recovery) | returning | released; cannot be reset until cool ('a few minutes', spec p. 2) | open | closed | at its position |
| reset | cool | latched set (H / HAND by pressing; A / AUTO by itself) | closed | open | released |
| test (HAND or AUTO, button pressed) | any | moved by the button | open | closed | pressed |

## Transitions
- running → tripped: at 1.2 x I_r the relay trips within 2 h, at 1.5 x I_r within 4 min, at 7.2 x I_r between 4 and 10 s (class 10 limits, IEC 60947-4-1 table on spec p. 12); the relay's own mean curve is on spec p. 8 (image, 20 °C from cold; about 25 % of those times when warm, p. 8 text). The curve is not digitised: the solver uses the class limits until a digitised curve is on file.
- One phase lost: the differential slide trips faster than a balanced overload (spec p. 2 'phase failure sensitivity'; how much faster is NOT ON FILE).
- tripped → reset: only after the recovery time. In H and HAND the button must be pressed; in A and AUTO the relay resets by itself and the contactor can pull in again without an operator (spec p. 2).
- test: in HAND and AUTO, pressing the button changes both auxiliaries; in H and A the test is blocked (spec p. 2 table).
- Maximum 15 operations per hour (spec p. 7).

## Failure modes
| mode | sub-element | parameter it changes | visible symptom (x-ray) | electrical symptom (what viob sees) | how found | spare | source |
|---|---|---|---|---|---|---|---|
| set above the motor's FLA | dial-fla | thermal trip point I_r ↑ (7-10 A range on a 0.91 A motor) | dial at 7 A or more | motor overloads and overheats without a trip | read the dial against the motor nameplate FLA | an overload of the right range (RW27-2D3-D012, 0.8-1.20 A, spec p. 3) | spec p. 3; motor spec p. 3; IEC 60947-4-1 / NEC 430.32 |
| set below the running current | dial-fla | I_r ↓ | dial below FLA | nuisance trips after minutes of normal running; 97-98 closes | read the dial; clamp-meter the running current | none (set it) | spec p. 2 |
| single-phasing | heater-bimetal (one cold) | phase current = 0 on one leg | one bimetal straight, two bent | fast trip; motor hums and does not start, or slows | meter: voltage on each of T1 T2 T3; current per phase | none (upstream fault) | spec p. 2 |
| ambient above 60 °C | comp-bimetal | thermal ambient ↑ beyond compensation | none | trips at less than I_r (derate 0.87 at 70 °C) | panel temperature against spec p. 8 | ventilation | spec p. 7, p. 8 |
| reset attempted too soon | latch | recovery time not elapsed | button pressed, nothing latches | 95-96 stays open | wait a few minutes, retry | none | spec p. 2 |
| left in A / AUTO | btn-reset | reset mode = automatic | button at A or AUTO | motor restarts by itself after cooling | read the button position | none (set H or HAND) | spec p. 2; FIELD KNOWLEDGE (restart hazard) |
| test disabled | btn-reset | position H or A | button at H or A | pressing the button changes nothing | read the position against the p. 2 table | none | spec p. 2 |
| 95-96 not in the coil circuit | (wiring) | aux-95 bypassed | none | trip closes 97-98 but the contactor stays in | trace the coil circuit through 95-96 | none (wiring) | FIELD KNOWLEDGE |
| aux contact film at low current | aux-95 / aux-97 | contact.R_c ↑ below I_min | none | PLC input from 97-98 flickers; rated 17 V / 5 mA minimum | meter at low current | whole relay | spec p. 5 |
| bimetal fatigued or drifted | heater-bimetal | trip point drifts | none visible | trips early or late against the class limits | test with a known current against p. 12 limits | whole relay | FIELD KNOWLEDGE |
| loose motor terminal | terminal-motor | contact.R_c ↑ (torque below 2.3 N-m) | discoloured terminal | local heating raises the bimetal's temperature: early trip on that phase | torque check (spec p. 6); thermal | re-terminate | spec p. 6; x06 |
| loose pin in the contactor | pin | contact.R_c ↑ at the contactor's lower clamp (1.7 N-m) | pin discoloured | heat into the overload: early trip | torque check of the contactor's lower terminals | re-terminate | contactor spec p. 9; x06 |

## Grading hooks (a diagnosis must include)
1. The dial setting compared with the motor's FLA on the nameplate (0.91 A at 460 V for this cell's motor; the 7-10 A relay cannot be set to it).
2. The state of 95-96 and 97-98 compared with the button position and the trip, with the recovery time respected before a reset.
3. The three phase currents (or voltages at T1 T2 T3) checked for a lost phase before the overload is blamed.
