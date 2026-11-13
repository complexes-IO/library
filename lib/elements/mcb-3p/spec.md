# mcb-3p · v1.1 · miniature circuit breaker, 3-pole

**What** A 3-pole miniature circuit breaker on the 35 mm rail: three poles on one handle and one trip, so all three open together. In the press-hydraulic panel it is q3, the HPU motor's branch breaker on 480 V three-phase (request panel-6 item 1b; inventory row mcb-3p, own_design generic by request elec-13, the core's answer of 2026-11-13). The family's maker-measured size, mcb-3p-c10 (10 A), is below the motor's full-load current (hpu-7.5kw: 12.08 A derived); this element is the family's generic 3-pole body, its size chosen later.
**Class** device · **Baseline** our own design: generic Miniature circuit breaker (ETIM 10.0 EC000042). Its body, pole pitch, terminals, rail clip, toggle and pole indicators are the mcb family's on file (mcb-3p-c10 1.5, read at build time), three poles of it, as mcb-2p is two; no vendor names; complexes.org on the label.
**Units / frame** mm, Z up. Origin: rail device: back face on the rail crown y = 0, rail centreline z = 0, left face of pole 1 x = 0, body toward −y.
**Built with** toolkit 1.3 · AutoLISP command `MCB3G` · no parameters (the rated current is not chosen: see Notes).

## Class values
ETIM 10.0 EC000042 "Miniature circuit breaker (MCB)", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Built-in depth (EF000218) | 73 mm (the family's, mcb-3p-c10 1.5) |
| 2 | Release characteristic (EF000889) | not stated (chosen with the rated current) |
| 3 | Number of poles (total) (EF008618) | 3 |
| 4 | Number of protected poles (EF005548) | 3 |
| 5 | Rated current (EF000227) | not stated: sized for the HPU motor's branch (hpu-7.5kw: 7.5 kW, 460 V, FLC 12.08 A derived; its NFPA 70 Table 430.250 current is that element's own open figure, class B) by NEC 430.52, whose Table 430.52 is NOT ON FILE (B): NEC 430.52 (a document wanted); the size goes into the id when chosen (OPERATING.md 6) |
| 6 | Rated voltage (EF000228) | 480 V (the panel's supply, lib/assemblies/press-hydraulic/controls.csv: 480V 3ph 60Hz, the design input) |
| 7 | Rated insulation voltage Ui (EF001366) | not stated |
| 8 | Rated impulse withstand voltage Uimp (EF011980) | not stated |
| 9 | Rated short-circuit breaking capacity Icn according to EN 60898 at 230 V (EF009556) | not stated |
| 10 | Voltage type (EF000187) | AC |
| 11 | Rated short-circuit breaking capacity Icn according to EN 60898 at 400 V (EF009555) | not stated |
| 12 | Rated short-circuit breaking capacity Icu according to IEC 60947-2 at 230 V (EF009557) | not stated |
| 13 | Rated short-circuit breaking capacity Icu according to IEC 60947-2 at 400 V (EF009558) | not stated |
| 14 | Frequency (EF000416) | 60 Hz (the panel's supply, controls.csv) |
| 15 | Power loss (EF005387) | not stated |
| 16 | Current limiting class (EF002568) | not stated |
| 17 | Flush-mounted installation (EF007517) | no (rail mounted) |
| 18 | Concurrently switching neutral conductor (EF005997) | no (all three poles are phases) |
| 19 | Overvoltage category (EF002569) | not stated |
| 20 | Pollution degree (EF002570) | not stated |
| 21 | Additional equipment possible (EF008148) | not stated |
| 22 | Width in number of modular spacings (EF002950) | 3 |
| 23 | Degree of protection (IP) (EF005474) | not stated |
| 24 | Ambient temperature during operating (EF007515) | not stated |
| 25 | Connectable conductor cross section multi-wired (EF007343) | not stated |
| 26 | Connectable conductor cross section solid-core (EF007337) | not stated |
| 27 | Explosion-proof (EF004663) | no |

## Dimensions
| item | value | source |
|---|---|---|
| body | 53.1 wide (3 × 17.7) × 105.0 high (105.2 over the terminal screws) × 73.0 deep, raised 45 front, toggle 3.7 proud | design choice: the family's figures (mcb-3p-c10 1.5: PITCH, H, D, FRONT, DT; where the depth planes are that element's own open figures, class B) |
| terminals | one captive screw per pole top and bottom, 66.0 apart, shoulders 37.5 from the rail crown | design choice: the family's figures (mcb-3p-c10 1.5: TERM, SHOULDER; where the shoulder line is that element's own open figure, class B) |
| port pivots | at each wire entry's mouth on the end face, axis the way the wire goes in | as mcb-3p-c10 1.4 and later |
| rail clip | 35 mm rail | toolkit/din.py rail_clip (EN 60715 TH35-7.5) |
| terminal marks | 1 (line) / 2 (load) on pole 1, 3 / 4 on pole 2, 5 / 6 on pole 3, printed on the label field | design choice (our part's print, as mcb-2p) |
| label | complexes.org and the marks on the white field of each pole | design choice |

## Named nodes
`t-1`, `t-2`, `t-3`, `t-4`, `t-5`, `t-6` (kind port, unit screw, gender none: the terminal screws, the twin's probe points) · `toggle` (rotate about x, −25 to 25°, off to on: the family's toggle, toolkit/din.py; the swing is class C, a handle swing, as the family's) · `indicator-1`, `indicator-2`, `indicator-3` (emissive: the poles' contact-position windows).

## Materials by layer
`M-GREY-PA` body · `M-ZINC` terminal screws · `M-GASKET` wire entries · `M-WHITE-PA` label fields · `M-BLACK-PA` toggle · the indicators as toolkit/din.py draws them.

## Decals (Blender)
Label fields: "complexes.org" and the terminal marks 1 2 / 3 4 / 5 6. No rating is printed (none is chosen).

## Notes and open figures
- The rated current and release characteristic are not chosen. The breaker protects the HPU motor's branch (the press-hydraulic controls spec's m1 row; hpu-7.5kw: 7.5 kW, 460 V, FLC 12.08 A derived, derive.motor_current; its NFPA 70 Table 430.250 current is that element's own open figure, class B: no file on hand gives the 11 A that 1.0 wrote, review mcb-3p-1.0 finding 1) and is sized by NEC 430.52 (Table 430.52, the inverse-time breaker's percentage of the motor's full-load current), which is NOT ON FILE (B): NEC 430.52; when it is on file the size is chosen and goes into the id (OPERATING.md 6: the library's rename, as the core's answer to request elec-13 says). Until then pnl-press-hydraulic's q3 row places the element without a rating, and the twin trips it only as a manual fault.
- Rated voltage 480 V is the panel's design input. IEC 60898-1, which the inventory row names, covers breakers up to 440 V; a 480 V rating is a UL 489 or IEC 60947-2 rating, and neither standard is on file. No rating is claimed beyond the class value (as mcb-2p; lib/needs-em/elec.md, r28).
- The terminal screws' torque is NOT ON FILE (B): IEC 60947-1 (behaviour.csv).
- The magnetic and thermal trips need the circuit model (phase 2 of the solver): until then `tripped` is a manual fault, as in mcb-3p-c10 and mcb-2p.
- The mechanism is trip-free (the poles cannot be held closed against a trip) and the toggle moves to off to reset: Assumption (A), the family's row (mcb-3p-c10 behaviour.csv `reset`, mcb-2p's the same words), behaviour the twin reports and not a class value of EC000042; IEC 60898-1 and IEC 60947-2, which would fix it, are not on file.

## Outputs (out/)
`mcb-3p.lsp` · `.glb` (`env-colonly` collider) · `preview-*.png`.

## History
| version | change |
|---|---|
| 1.0 | first build: generic EC000042, three poles of the mcb family (mcb-3p-c10 1.5), terminal port nodes t-1 to t-6 at the entries' mouths (elec-r41, unattended, 2026-11-12) |
| 1.1 | text only (review mcb-3p-1.0 / elec-r41 findings 1 and 2, note 2; elec-r50, unattended, 2026-11-13): the motor's current as hpu-7.5kw gives it (FLC 12.08 A derived; the table current that element's own open figure), not the 11 A no file gives; the body and terminal rows "design choice: the family's figures"; metadata.json height 105.2 as built. Nodes, origin and cut-outs as 1.0 |
