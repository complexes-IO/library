# contact-m12-pin · behaviour (as the twin runs it)

The pin's state is decided with its socket by `toolkit/contact.py` `mate()` from where both parts sit; figures in `toolkit/m12.py` (Assumption until a maker drawing is on file).

## Inputs
- where its socket is (insertion depth from the plug's gap: nut turns x 1.0 mm), the key, the nut torque; current through it (the binder's net).

## Outputs
- pole state: made (overlap with the socket's springs ≥ 0.5 mm, 5 + 5 mΩ) · marginal (0 < overlap < 0.5) · open · high-r · blocked.

## Failure modes (condition → parameter it changes → symptoms)
| condition | parameter | visible (x-ray) | electrical (what viob sees) | how found |
|---|---|---|---|---|
| bent | the exposed shank leans 12°: the tip 0.94 off its socket's axis | a leaning pin in the plug face | the plug stops 3.45 mm short: every pole open, the nut will not run home | look at the face; the nut stops after one turn |
| pushed-back | the pin 2.0 deeper in its carrier | one pin shorter than the rest | that pole marginal at the seat: works on the bench, drops out under vibration or heat | intermittent channel; measure pin height |
| broken | a 0.6 stub | a missing pin | that pole open | one channel dead, the rest fine |
| corroded | contact resistance x 100 | a green pin | that pole high-r: volt drop, a sensor flickers under load | volt drop across the joint |
Source: FIELD KNOWLEDGE (EM, 2026-11-03: connectors not seated well in the field); figures Assumption.
