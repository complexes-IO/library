# wire · behaviour (as the twin runs it)

Each end is decided with the clamp it is in by `toolkit/contact.py` `terminate()`.

## Failure modes (condition → parameter it changes → symptoms)
| condition (per end) | parameter | visible | electrical | how found |
|---|---|---|---|---|
| under-stripped | bare length 0.4 x strip | insulation into the clamp | marginal: the clamp grips insulation, high resistance, heat, intermittent | pull test; a warm terminal |
| over-stripped | bare length 1.8 x strip | bare copper outside the terminal | made, but a touchable live conductor (and a short to the neighbour) | look |
| nicked | conductor Ø 0.6 x over a short length | a notch | high-r: heats at the nick under load, breaks with vibration | inspection after stripping |
| strands-out | four strands splayed | stray strands | made, a short to the next terminal waiting | look; a ferrule prevents it |
Source: FIELD KNOWLEDGE; figures Assumption.
