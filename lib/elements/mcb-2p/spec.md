# mcb-2p · v1.1 · miniature circuit breaker, 2-pole

**What** A 2-pole miniature circuit breaker on the 35 mm rail: two poles on one handle and one trip, so both open together. In the motor starter panel it is q4, the control transformer's primary breaker across two phases of 480 V (request panel-1 item 2; the core's answer of 2026-11-11: a multipole breaker trips all its poles, two single poles side by side do not).
**Class** device · **Baseline** our own design: generic Miniature circuit breaker (ETIM 10.0 EC000042). Its body, pole pitch, terminals, rail clip, toggle and pole indicators are the mcb family's on file (mcb-3p-c10 1.3, read at build time), two poles of it; no vendor names; complexes.org on the label.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face of pole 1 x = 0, body toward −y.
**Built with** toolkit 1.3 · AutoLISP command `MCB2` · no parameters (the rated current is not chosen: see Notes).

## Class values
ETIM 10.0 EC000042 "Miniature circuit breaker (MCB)", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Built-in depth (EF000218) | 73 mm (the family's, mcb-3p-c10 1.3) |
| 2 | Release characteristic (EF000889) | not stated (chosen with the rated current) |
| 3 | Number of poles (total) (EF008618) | 2 |
| 4 | Number of protected poles (EF005548) | 2 |
| 5 | Rated current (EF000227) | not stated: sized against xfmr-control's primary current (0.52 A, its ratings.csv i1) by NEC 430.72(C), whose table is NOT ON FILE (B): NEC 430.72(C) (a document wanted); the size goes into the id when chosen (OPERATING.md 6) |
| 6 | Rated voltage (EF000228) | 480 V (the panel's line-to-line voltage, the design input) |
| 7 | Rated insulation voltage Ui (EF001366) | not stated |
| 8 | Rated impulse withstand voltage Uimp (EF011980) | not stated |
| 9 | Rated short-circuit breaking capacity Icn according to EN 60898 at 230 V (EF009556) | not stated |
| 10 | Voltage type (EF000187) | AC |
| 11 | Rated short-circuit breaking capacity Icn according to EN 60898 at 400 V (EF009555) | not stated |
| 12 | Rated short-circuit breaking capacity Icu according to IEC 60947-2 at 230 V (EF009557) | not stated |
| 13 | Rated short-circuit breaking capacity Icu according to IEC 60947-2 at 400 V (EF009558) | not stated |
| 14 | Frequency (EF000416) | 60 Hz (the cell's supply, mc-motor-1 controls.csv: 480V 3ph 60Hz) |
| 15 | Power loss (EF005387) | not stated |
| 16 | Current limiting class (EF002568) | not stated |
| 17 | Flush-mounted installation (EF007517) | no (rail mounted) |
| 18 | Concurrently switching neutral conductor (EF005997) | no (both poles are phases) |
| 19 | Overvoltage category (EF002569) | not stated |
| 20 | Pollution degree (EF002570) | not stated |
| 21 | Additional equipment possible (EF008148) | not stated |
| 22 | Width in number of modular spacings (EF002950) | 2 |
| 23 | Degree of protection (IP) (EF005474) | not stated |
| 24 | Ambient temperature during operating (EF007515) | not stated |
| 25 | Connectable conductor cross section multi-wired (EF007343) | not stated |
| 26 | Connectable conductor cross section solid-core (EF007337) | not stated |
| 27 | Explosion-proof (EF004663) | no |

## Dimensions
| item | value | source |
|---|---|---|
| body | 35.4 wide (2 × 17.7) × 105.0 high × 73.0 deep, raised 45 front, toggle 3.7 proud | the family's figures, mcb-3p-c10 1.3 (PITCH, H, D, FRONT, DT) |
| terminals | one captive screw per pole top and bottom, 66.0 apart, shoulders 37.5 from the rail crown | mcb-3p-c10 1.3 (TERM, SHOULDER) |
| rail clip | 35 mm rail | toolkit/din.py rail_clip |
| terminal marks | 1 (line) / 2 (load) on pole 1, 3 / 4 on pole 2, printed on the label field | design choice (our part's print) |
| label | complexes.org and the marks on the white field of each pole | design choice |

## Named nodes
`t-1`, `t-2`, `t-3`, `t-4` (kind port, unit screw, gender none: the terminal screws, the twin's probe points) · `toggle` (rotate about x, −25 to 25°, off to on: the family's toggle, toolkit/din.py) · `indicator-1`, `indicator-2` (emissive: the poles' contact-position windows).

## Materials by layer
`M-GREY-PA` body · `M-ZINC` terminal screws · `M-GASKET` wire entries · `M-WHITE-PA` label fields · `M-BLACK-PA` toggle · the indicators as toolkit/din.py draws them.

## Decals (Blender)
Label fields: "complexes.org" and the terminal marks 1 2 / 3 4. No rating is printed (none is chosen).

## Notes and open figures
- The rated current and release characteristic are not chosen. The breaker is sized against xfmr-control's primary current (0.52 A, derived) by NEC 430.72(C), whose table is NOT ON FILE (B): NEC 430.72(C); when it is on file the size is chosen and goes into the id (OPERATING.md 6: the library's rename). Until then pnl-motor-starter's q4 row places the element without a rating, and the twin trips it only as a manual fault.
- Rated voltage 480 V is the panel's design input. IEC 60898-1, which the inventory row names, covers breakers up to 440 V; a 480 V rating is a UL 489 or IEC 60947-2 rating, and neither standard is on file. No rating is claimed beyond the class value (lib/needs-em/elec.md, r28).
- The terminal screws' torque is NOT ON FILE (B): IEC 60947-1 (behaviour.csv).
- The magnetic and thermal trips need the circuit model (phase 2 of the solver): until then `tripped` is a manual fault, as in mcb-3p-c10.
- The mechanism is trip-free (the poles cannot be held closed against a trip) and the toggle moves to off to reset: Assumption (A), the family's row (mcb-3p-c10 1.3 behaviour.csv `reset`), behaviour the twin reports and not a class value of EC000042; IEC 60898-1 and IEC 60947-2, which would fix it, are not on file (review mcb-2p-1.0 finding 1).

## Outputs (out/)
`mcb-2p.lsp` · `.glb` (`env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.1 | elec-r32 (unattended, 2026-11-11): text only, geometry as 1.0. behaviour.csv's `reset` row written as the family's class A line (trip-free, reset by the toggle) with the line in the Notes, so DOC-005 counts it for EM (review mcb-2p-1.0 finding 1, an ESCAPE: a behaviour row's "design choice" named no rule) |
| 1.0 | first build: generic EC000042, two poles of the mcb family (elec-r28, attended, 2026-11-11) |
