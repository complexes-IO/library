# clamp-screw · behaviour (as the twin runs it)

A wire end's state in the clamp is decided by `toolkit/contact.py` `terminate()`: insertion depth, strip length, wire size against the range (on file for term-4mm: 22-10 AWG feed, 22-12 AWG ground), screw torque against its window (Assumption 0.5-0.8 N m).

## Failure modes (condition or situation → symptoms)
| situation | state | symptom |
|---|---|---|
| screw never tightened | open | the wire pulls out; channel dead |
| torque under the window | marginal | works loose with vibration and thermal cycling; heats under load |
| torque over the window | high-r | strands crushed; heats, then breaks |
| wire over the range | blocked | it does not go in |
| wire under the range | marginal | not gripped |
| insulation under the clamp | marginal or open | high resistance or no contact at all |
| corroded (condition) | high-r | volt drop, heat |
Source: FIELD KNOWLEDGE; figures Assumption except the wire range.
