# receptacle-m23 · v1.1 · M23 receptacle (device side), flange mounted, male contacts, power 3 + PE or signal 6 poles (complexes.org generic)

**What** The device side of an M23 circular joint, as a servo motor or a drive carries it: a square flange that sits on the host's outer wall with four M3 screws, an M23 × 1 threaded sleeve in front of it that the cable plug's coupling nut screws onto, an insulating contact carrier in the sleeve's bore with male contacts standing out of it, and a round body behind the flange that passes through the host's wall hole. Two kinds by parameter: `power` (contacts 1, 2, 3 and PE, Ø1.2) and `signal` (contacts 1 … 6, Ø1.0). A common part (lib/inventory.csv: "M23 power / signal receptacle (servo)"): servo-motor's two connector seats wait on it. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC003569 "Circular connector, mounting (without cable)", built to the class values below; no maker's datasheet and no product is matched.
**Class** connector · **Baseline** our own design: generic Circular connector, mounting (without cable) (ETIM 10.0 EC003569). The class values are this element's definition (design inputs); the thread M23 × 1 is derived and the flange holes are ISO 273 on file; the mating face (contact layout, coding, sleeve length) is a design layout, since no standard fixes it (Dimensions); every other size is a design choice, said so below.
**Units / frame** mm, Z up. Origin: the flange's back face (the face that sits on the host's outer wall) y = 0 on the sleeve's axis x = 0, z = 0; the sleeve and the mating plug toward −y, the body behind the flange (inside the host) toward +y. A host places it with its origin on its wall's outer face and the axis along the wall's normal (roll and yaw, toolkit/library.place).
**Built with** toolkit 1.3 · AutoLISP command `M23RCP` · parameter `kind` = `power` (default) or `signal` · places no element.

## Class values
ETIM 10.0 EC003569 "Circular connector, mounting (without cable)", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to, or "not stated". They define the element: design inputs, not open figures (OPERATING.md 12).

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Type of plug-in contact, outer side (EF005528) | pin (male contacts) |
| 2 | Mounting method (EF000003) | flange mounting, front, four screws M3 |
| 3 | Screw-in thread (EF012303) | M23 × 1 (the sleeve's outside, for the plug's coupling nut) |
| 4 | With shield connection (EF002535) | no |
| 5 | Number of poles (EF001391) | power: 4 (3 + PE); signal: 6 |
| 6 | Number of control contacts (EF012217) | 0 (power: no control contacts; signal: its 6 poles are the contacts) |
| 7 | With PE-connection (EF005600) | power: yes (contact PE, at the centre); signal: no |
| 8 | Housing material (EF001596) | zinc die-cast |
| 9 | Coating housing (EF001601) | not stated |
| 10 | Material of contact surface (EF004020) | power: silver; signal: gold |
| 11 | Pollution degree (EF006786) | not stated |
| 12 | Inflammability class of insulation material according to UL94 (EF002521) | not stated |
| 13 | Min. number of insertion cycles (EF012212) | not stated |
| 14 | Degree of protection (IP), mounted (EF007466) | not stated (no seal is modelled) |
| 15 | Ambient temperature (EF002386) | not stated |
| 16 | Operating temperature (EF002393) | not stated |
| 17 | Rated voltage (EF000228) | power: 630 V; signal: 60 V |
| 18 | Rated current In (EF008250) | power: 10 A per contact; signal: 8 A per contact |
| 19 | Connectable conductor cross section (EF008200) | not stated (the contacts' crimp or solder ends behind the body are not modelled) |
| 20 | With thread (EF003723) | yes |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. Clearance and creepage between the contacts are not claimed (no insulation-coordination standard is on file). `ratings.csv` carries the ratings the checks may read (status "generic design", source "ETIM 10.0 EC003569 class value"); `pins.csv` gives each contact its role.

## Dimensions
| item | value | source |
|---|---|---|
| flange | 30.0 × 3.0 × 30.0 (x, z ±15, y −3 … 0), back face y 0 on the host's wall | design choice |
| flange holes | four Ø3.4 through the flange at x, z = ±11.0 (15.56 from the axis, 4.07 outside the sleeve: a screw head up to Ø8.1 seats clear of it; the head's size is not on file); position Ø0.4 to A (the flange's back face), B (the sleeve's axis), C (the upper-right hole) | ISO 273 medium clearance for M3 (lib/standards/holes.csv); pattern and tolerance design choices; Ø0.4 ≤ H − F = 3.4 − 3.0 (GDT-010, features.csv) |
| sleeve | Ø22.974 × 12.0 out of the flange's front face (y −3 … −15) | the outside: derived, the 6g major diameter's maximum of M23 × 1 (derive.thread(23.0, 1.0): d 22.797 … 22.974; ISO 68-1 basic profile, ISO 965-1 clause 10); the thread's form is not modelled; the length a design choice |
| sleeve bore | Ø19.0, through the sleeve to the flange's front face | design choice |
| contact carrier | Ø18.9 × 4.0 in the bore (y −3 … −7), its back on the flange's front face, 0.05 clear of the bore | design choice |
| contacts, power | Ø1.2 × 5.0 out of the carrier face (y −7 … −12): 1, 2, 3 on a Ø11.0 circle at 90°, 210°, 330° (from +x toward +z), PE on the axis | design layout (the mating face, Notes) |
| contacts, signal | Ø1.0 × 5.0 out of the carrier face (y −7 … −12): 1 … 6 on a Ø10.0 circle, 1 at 90°, then every 60° toward +x | design layout (the mating face, Notes) |
| body | Ø21.0 × 18.0 behind the flange (y 0 … 18), through the host's Ø22 wall hole | design choice |
| overall | 30.0 × 33.0 (y −15 … 18) × 30.0 | from the parts above |

The mating face, the plug's side of the joint: the contact layout, the coding key and the sleeve's length. design: the layout above (no standard on file fixes it: lib/standards/sources.csv lists no M23 mating-face document, and none of the standards on file tabulates one; OPERATING.md 12, a size no standard fixes is the designer's). So two of these elements mate each other's plugs only as this design; a maker's M23 plug may not. If a standard that tabulates an M23 face reaches lib/standards/, the layout follows it in a new version.

## Named nodes
Contacts, each a port (kind port, axis −y, at the contact's tip, gender male): power `c-1`, `c-2`, `c-3`, `c-pe` (unit m23-power); signal `c-1` … `c-6` (unit m23-signal). The flange, sleeve, carrier and body are not nodes: nothing moves. pins.csv says what each contact passes; the host's pins.csv says what it carries.

## Materials by layer
`M-ZINC` flange, sleeve and body · `M-BLACK-PA` contact carrier · `M-SILVER` power contacts · `M-GOLD` signal contacts (the holes and the bore are cuts, no layer of their own)

## Decals (Blender)
None: the flange carries no field big enough for a legend. The contact numbers are not printed (a design choice; the host's legend names the connection). No maker's name, logo or approval mark.

## Notes
- No open figure (1.1): the mating face is a design layout (the line under Dimensions; review receptacle-m23-1.0 finding 3). Every rating is a class value (design input), the thread derived, the holes ISO 273 on file, every other size a design choice.
- The two kinds differ in their contacts (power c-1 c-2 c-3 c-pe; signal c-1 … c-6). behaviour.csv's rows for one kind only read `only kind=<value>` (PE `only kind=power`, 4 to 6 `only kind=signal`; the core's answer to request elec-15, lib/behaviour.md pin; review finding 2): the checks read each such pin in a build of its kind, the solver keeps it where the placed build has its node.
- Not modelled: the coding key (the mating face's), the thread's form, the seal between the flange and the wall, the contacts' crimp or solder ends and the cable side behind the body, a protective cap.
- The host places it on its wall and models the Ø22 wall hole and the four M3 tapped or clearance holes itself (the host's figures). servo-motor's seats (Ø23 × 8, port-pwr and port-enc) are replaced by this element at its next major.
- Not a safety-function device.

## Outputs (out/)
`receptacle-m23.lsp` · `.glb` (a port pivot on every contact, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r39 (lib/rounds/elec/r39.md), the default `power` and the `signal` kind; 1.1 in elec-r50.

## History
| version | change |
|---|---|
| 1.0 | elec-r39 (2026-11-12, unattended): first build, generic ETIM 10.0 EC003569, our own design; common part for servo-motor's connector seats; kinds power and signal |
| 1.1 | elec-r50 (2026-11-13, unattended): text only (review receptacle-m23-1.0 / elec-r39 findings 1 and 3): the mating face a design layout (no standard fixes the M23 face), so the element's one class B line goes; behaviour.csv's contact torques `not claimed` (lib/behaviour.md, pin); the signal kind's rows put to the core (request elec-15); pins.csv says contacts 1 to 3 carry 8 A in the signal kind (review finding 2's note). Nodes, origin and cut-outs as 1.0 |
