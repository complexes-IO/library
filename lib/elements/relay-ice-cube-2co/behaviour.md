principles: e04 e13 e17 m18 m17 x03 x06 x07 x13 x14 x15 (x16 offline)

# relay-ice-cube-2co · behaviour (as the twin runs it)

Sub-elements and their models are in `parts.csv`; models are defined in `lib/models.md`; principle ids in `lib/principles.csv`. Figures cite `references/interior.md` and its documents ("spec" = the maker's relay specification listed there; maker and file names only in references/).

## Inputs
- `coil`: voltage across pins 13 (A1, +) and 14 (A2, −), from the circuit model. Nominal 24 VDC; continuous maximum 26.4 V (110 %, spec p. 3).
- `btn-test`: pressed by the student (manual operation without coil power, spec p. 1).
- `door-lock`: closed or open over the button (spec p. 1).
- Load circuits on each pole: current through common 9 / 12 (from the circuit model), for contact wear and heating.

## Outputs
- Contact states: pole 1 common 9 to N.C. 1 or N.O. 5; pole 2 common 12 to N.C. 4 or N.O. 8 (spec p. 5); each closed contact as a resistance `contact.R_c` in the circuit model.
- `led-coil`: lit while the coil has voltage (spec p. 1).
- `flag`: shows operate in the powered or manual condition (spec p. 1).

## States (sub-node pose in each)
| state | coil | armature | pole-1 / pole-2 | btn-test | door-lock | flag | led-coil |
|---|---|---|---|---|---|---|---|
| released | below drop-out | back stop | 9–1, 12–4 closed | out | open | released | off |
| operated (powered) | at or above pull-in, then held above drop-out | at the core | 9–5, 12–8 closed | out | open | operate | on |
| manual test | any | where the coil leaves it (the button drives the card, not the armature) | 9–5, 12–8 closed | pressed | open | operate | on only if powered |
| locked test | any | where the coil leaves it (the door holds the button, the button the card) | 9–5, 12–8 closed | held | closed | operate | on only if powered |

"At the core" in the model (1.3): the armature plate turns 4.06° about its hinge, the angle set by the 1.2 contact travel at its tip,
and the core's pole face stands where the turned plate meets it (its lower edge; spec.md "Mechanism as built"). In the manual test the
button's stem pushes the card through a tab in line with it (lib/motion.csv btn-test → actuator); the armature is not driven by the
button (request elec-4 answer item 1). The twin takes the state from the coil model and the button, not from the geometry. How the
slider holds the pressed button is not on the specification (spec.md, "Mechanism as built").

## Transitions
- released → operated: coil voltage rises to the pull-in level, at or below 19.2 V (80 % of 24 V, spec p. 3); response time 20 ms (spec p. 3, whether operate or release not stated). The commons leave N.C. before reaching N.O. (break-before-make: FIELD KNOWLEDGE, no figure on file). Contacts bounce on closing (spec p. 7; bounce time NOT ON FILE).
- operated → released: coil voltage falls to the drop-out level; the relay has released by 2.4 V (10 % of 24 V, spec p. 3). The return spring brings the armature back. Switching the coil off makes an inductive spike across 13–14 unless a suppression module is fitted (spec p. 7).
- released → manual test: button pressed (spec p. 1); → locked test: door closed over the pressed button (spec p. 1); back to released when the door is opened and the button returns (button spring: FIELD KNOWLEDGE).

## Failure modes
| mode | sub-element | parameter it changes | visible symptom (x-ray) | electrical symptom (what viob sees) | how found | spare | source |
|---|---|---|---|---|---|---|---|
| coil open | coil | coil.R = ∞ | armature stays at the back stop with 24 V applied; LED state depends on the LED circuit (NOT ON FILE) | the output that drives the coil is on, no contact change; no coil current | meter: R across 13–14 open (new 640 Ω, spec p. 3) | whole relay | FIELD KNOWLEDGE; R from spec p. 3 |
| shorted turns | coil | coil.R ↓, coil.L ↓ | coil runs hot; armature may still pull in | coil current above 24 V / 640 Ω = 37.5 mA; driver may trip | meter: R across 13–14 below 640 Ω (tolerance NOT ON FILE) | whole relay | FIELD KNOWLEDGE |
| low supply | circuit (supply) | coil input V below pull_in_v (19.2 V) | armature does not pull in, or chatters | contacts do not change; contact chatter if the voltage hovers | meter: voltage at 13–14 under load | none (supply fault) | spec p. 3 (pull-in) |
| reversed coil polarity | led / circuit | led polarity (13 + / 14 −, spec p. 5) | relay operates (a coil is not polarised), LED stays dark (FIELD KNOWLEDGE; LED circuit NOT ON FILE) | normal contact change; indicator wrong | look: LED dark while contacts operate | none (wiring fault) | spec p. 5 polarity marks; FIELD KNOWLEDGE |
| contacts pitted / eroded | contact-1-mov, contact-2-mov (and fixed contacts) | contact.R_c ↑, intermittent | darkened, cratered contact faces | voltage drop across a closed contact; intermittent load; heating at high current | meter: mV drop or R across the closed contact under load; electrical life 100,000 operations at rated resistive load (spec p. 3) | whole relay | spec p. 3 (life); FIELD KNOWLEDGE (symptom) |
| contacts welded | contact-1-mov / contact-1-no (or pole 2) | contact state stuck closed (contact.welded = true) | common stays on N.O. with the coil off; armature held near the core | load stays on after the output turns off | look: flag stays at operate with the coil off; meter across N.O. | whole relay | FIELD KNOWLEDGE |
| low-current switching film | contact | contact.R_c ↑ at currents below I_min | none visible | input that the relay feeds reads off or flickers | meter: high R at low current; the circuit switches under 10 mA at 17 VDC (spec p. 3; 'not recommended for low current switching', p. 2) | relay with gold-only contacts (not in this series) or redesign | spec p. 2, p. 3 |
| return spring fatigued | spring-return | spring.k ↓ (broken: k = 0) | armature slow to return or stays near the core | drop-out voltage falls; contacts release late or not at all | listen / look: no release click; flag stays at operate; mechanical life 10,000,000 operations (spec p. 3) | whole relay | spec p. 3 (life); FIELD KNOWLEDGE |
| armature sticking | armature | armature.b ↑ (friction) or residual hold | armature hesitates | operate and release times beyond 20 ms (spec p. 3) | look: flag lags; timer on the input | whole relay | FIELD KNOWLEDGE |
| door left locked | door-lock | latch latched | button held in, flag at operate | contacts operated with the coil off: the machine sees a permanent signal | look: door closed over the button (spec p. 1) | none (operator error) | spec p. 1 |
| loose socket terminal | socket-terminal | contact.R_c ↑ at the terminal (torque below 1.0 N-m) | none, or discolouration at the screw | intermittent, heating under load | meter: mV drop across the terminal; torque check 1.0 N-m (sockets spec p. 1) | re-terminate | sockets spec p. 1; principle x06 |
| no suppression | suppressor (absent) | coil turn-off spike unclamped | none | transient on the driving output; damaged output (spec p. 7) | oscilloscope at 13–14 on turn-off | fit the diode module (spec p. 7) | spec p. 7 |

## Grading hooks (a diagnosis must include)
1. The coil measured: resistance across 13–14 against 640 Ω, and the voltage at 13–14 with the output on (against pull-in 19.2 V).
2. The contact checked under load: which pole and side (9–5 or 12–8 operated, 9–1 or 12–4 released), and the voltage drop or resistance across it.
3. The mechanical evidence: flag and LED compared (flag = armature, LED = coil voltage), and the lock-down door checked before anything is replaced.
