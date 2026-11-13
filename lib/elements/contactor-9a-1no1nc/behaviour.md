principles: e04 e13 e17 e21 a14 m18 m17 x03 x06 x07 x13 x14 x15 x17 x18 x19 (x16 offline)

# contactor-9a-1no1nc · behaviour (as the twin runs it)

Sub-elements and models are in `parts.csv`; models in `lib/models.md`; principles in `lib/principles.csv`. Figures cite `references/interior.md` and its documents (spec = technical-specifications-cwb-series.pdf).

## Inputs
- `coil`: voltage across A1–A2, nominal 24 VDC, operating limits 19.2 to 26.4 V (0.8 to 1.1 x Us, spec p. 6).
- Main circuit: current through 1–2, 3–4, 5–6 (from circuit-ac), for contact wear and heating by utilization category.
- Auxiliary circuits: current through 13–14, 21–22, 53–54, 61–62.

## Outputs
- Main poles closed or open (each a resistance `contact.R_c`, new 2.5 mΩ per pole, spec p. 7).
- Built-in auxiliaries 13–14 (N.O.), 21–22 (N.C.); front block 53–54 (N.O.), 61–62 (N.C.).
- No indicator on the documents (a contact-position window is NOT ON FILE).

## States (sub-node pose in each)
| state | coil | armature / carrier | main poles 1-2 3-4 5-6 | 13-14 / 53-54 | 21-22 / 61-62 | return spring | contact springs |
|---|---|---|---|---|---|---|---|
| released | below drop-out | back stop | open | open | closed | extended | free |
| closing (transient) | above pick-up | travelling; N.C. aux open first | open, then touching | open, then closed | opened | compressing | free, then compressing |
| operated | held above drop-out | on the core | closed | closed | open | compressed | compressed by the over-travel |
| opening (transient) | below drop-out | returning | breaking (arc at AC-3 / AC-4) | opening | closing after 1.5 ms | extending | extending |

## Transitions
- released → operated: coil voltage reaches pick-up, between 12.0 and 19.2 V (0.5 to 0.8 x Us, p. 6). The N.O. contacts close 35 to 45 ms after energising (p. 6); the auxiliary N.C. opens at least 1.5 ms before the auxiliary N.O. closes (p. 8). The DC coil draws 5.8 W closing and holding (p. 6, p. 24): no inrush. Main contacts bounce on closing (bounce time NOT ON FILE).
- operated → released: coil voltage falls to drop-out, between 9.6 and 2.4 V (0.1 to 0.4 x Us, p. 6); the N.O. contacts open 8 to 12 ms later (p. 6), six times longer with a DC suppressor fitted (p. 15). Switching the coil off makes an inductive spike across A1–A2 unless suppressed (x13).
- Breaking load current: at AC-3 the contacts break the motor's running current; at AC-4 (inching, plugging) they break locked-rotor current, which is why the AC-4 rating is 4.4 A against 9 A AC-3 (p. 7).

## Failure modes
| mode | sub-element | parameter it changes | visible symptom (x-ray) | electrical symptom (what viob sees) | how found | spare | source |
|---|---|---|---|---|---|---|---|
| coil open | coil | coil.R = ∞ | carrier stays at the back stop with 24 V on A1–A2 | output on, no auxiliary feedback (13–14 stays open), motor does not start | meter: R across A1–A2 open (about 99 Ω derived) | whole contactor (a spare coil part is NOT ON FILE) | FIELD KNOWLEDGE; R derived from p. 6 |
| low coil voltage | circuit (supply) | coil input V below pull_in_v | carrier hesitates, chatters | auxiliary feedback flickers; motor contacts chatter and burn | meter: voltage at A1–A2 under load (19.2 V minimum, p. 6) | none (supply fault) | spec p. 6 |
| main contacts eroded | pole-1 / pole-2 / pole-3 | contact.R_c ↑; contact.gap ↑ (over-travel used up) | pitted bridges, worn contact faces | phase voltage drop, one phase hot, motor current unbalance | meter: mV drop per pole under load; life 2 million AC-3 operations, B10 1.8 million (p. 6, p. 24) | whole contactor | spec p. 6, p. 24; FIELD KNOWLEDGE |
| welded main contact | pole | contact.welded = true | carrier held part-way; one bridge stuck | motor keeps running (or single-phases) after the coil is off; aux N.C. does not reclose | look: carrier not back; meter across the pole with the coil off | whole contactor | FIELD KNOWLEDGE (the CWB is not stated as mirror-contact rated, p. 17 is the CWBS) |
| AC-4 duty on an AC-3 rating | pole | contact.erosion per operation ↑ | fast erosion | early failure (AC-4 4.4 A against AC-3 9 A, p. 7) | operations counter against the AC-4 rating | whole contactor | spec p. 7 |
| return spring weak or broken | spring-return | spring.k ↓ (k = 0) | carrier slow to return or stays in | contacts stay closed or release late after the coil is off | listen: no drop-out clack; aux feedback stays on | whole contactor | FIELD KNOWLEDGE; mechanical life 10 million (p. 6) |
| contact spring fatigued | spring-contact | spring.k ↓ | bridge touches with little force | high contact resistance, heating at full current | thermal check of the poles; mV drop | whole contactor | FIELD KNOWLEDGE |
| armature not seating (dirt, misalignment) | armature | mass-1d stops not reached (gap ≠ 0) | small gap at the core | DC coil: still holds if above drop-out; contact force low (FIELD KNOWLEDGE) | look: air gap; mV drop on the poles | clean / whole contactor | FIELD KNOWLEDGE |
| low-current auxiliary film | aux-13 / fb-53 | contact.R_c ↑ below I_min | none visible | PLC input from 13–14 reads off or flickers; reliability rated 17 V / 5 mA (p. 8) | meter at low current | none (circuit) | spec p. 8, p. 14 |
| loose terminal | terminal-main / terminal-coil-aux | contact.R_c ↑ at the clamp (torque below 1.7 / 1.0 N-m) | discoloured terminal | heating, voltage drop, intermittent | torque check (p. 9); thermal | re-terminate | spec p. 9; principle x06 |
| front block not latched | front-block | fb-slide not following the carrier | block loose on the front face | 53–54 / 61–62 do not change with the contactor | look; check the block with the carrier operated by hand | re-seat | FIELD KNOWLEDGE |
| DC suppressor fitted with an N.C. front block | suppressor | release time x 6 (p. 15) | none | slow drop-out; the documents forbid it with N.C. front blocks (p. 15) | read the accessory list against p. 15 | remove the suppressor or change the block | spec p. 15 |

## Grading hooks (a diagnosis must include)
1. The coil checked: voltage at A1–A2 with the output on (19.2 V minimum) and resistance across A1–A2 (about 99 Ω, derived).
2. The main poles checked under load: the voltage drop across each of 1–2, 3–4, 5–6, compared pole to pole.
3. The auxiliary feedback compared with the carrier: 13–14 and 21–22 (and 53–54, 61–62) against the commanded state, with the 1.5 ms non-overlap in mind when an N.O. and an N.C. are used as a pair.
