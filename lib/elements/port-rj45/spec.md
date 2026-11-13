# port-rj45 · v1.0 · RJ45 (8P8C) Ethernet socket, unshielded, 8 female contacts, front opening (complexes.org generic)

**What** The device side of a twisted-pair Ethernet joint, as an HMI, an industrial PC, a DIN-rail switch or a gateway carries it behind its wall: an insulating housing whose front face carries the plug's opening with the latch slot under it, and eight female spring contacts on the opening's top face that the plug's blades press against. A common part (lib/inventory.csv row `port-rj45`, own_design generic, "RJ45 Ethernet socket (IEC 60603-7)"): hmi-7in, ipc, eth-switch-din, power-meter, ups-rack and gateway-fieldbus list it in their made_of. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of ETIM 10.0 EC001121 "Modular connector", built to the class values below; no maker's datasheet and no product is matched.
**Class** connector · **Baseline** our own design: generic Modular connector (ETIM 10.0 EC001121). The class values are this element's definition (design inputs); the mating face (opening, latch slot, contact pitch and order) is not on file (Notes); every other size is a design choice, said so below.
**Units / frame** mm, Z up. Origin: the housing's front face y = 0 (the face that sits on the host's wall's outer face), x = 0 and z = 0 on the housing's centre; the mating plug toward −y, the housing (inside the host) toward +y. A host places it with its origin on its wall's outer face and its −y along the wall's outward normal (toolkit/library.place), and cuts the wall's 16 × 14 opening itself (the host's figure).
**Built with** toolkit 1.3 · AutoLISP command `RJ45P` · no parameters · places no element.

## Class values
ETIM 10.0 EC001121 "Modular connector" (lib/standards/etim/classes.csv, group EG000037 Installation material for data and telecommunication networks). The class's features are not in the subset on file: lib/standards/etim/class-features.csv has no EC001121 rows (request elec-14 asks the core for them and for the inventory row's etim cell). Until they come, the values this element is designed to, under the names the class's synonyms and the inventory row use; they define the element: design inputs, not open figures (OPERATING.md 12; GEN-010 does not judge a class whose features are not on file, request pneu-4).

| # | feature | value |
|---|---|---|
| 1 | Type of connector | socket (jack), female contacts |
| 2 | Number of positions / contacts | 8 / 8 (8P8C, "RJ45") |
| 3 | Shielded | no (no metal shield, no shield contact) |
| 4 | Mounting method | built into a device behind its wall (the contacts' tails to the host's board are not modelled) |
| 5 | Plug-in direction | straight, along the wall's normal |
| 6 | Housing material | polyamide, black |
| 7 | Material of contact surface | gold |
| 8 | Transmission category | not stated |
| 9 | Rated voltage, rated current per contact | not stated (no rating is claimed: a pass-through; the host's pins.csv says what each contact carries) |
| 10 | Degree of protection (IP) | not stated (no seal) |
| 11 | With LED | no |

No approval mark is shown and no transmission performance is claimed.

## Dimensions
| item | value | source |
|---|---|---|
| housing | 16.0 × 21.0 × 14.0 (x ±8, y 0 … 21, z ±7), one solid | design choice |
| opening | 11.8 wide (x ±5.9) × 8.0 high (z −3.0 … 5.0), 15.0 deep from the front face (y 0 … 15) | design layout (the mating face, Notes) |
| latch slot | 6.0 wide (x ±3.0) × 2.5 high (z −5.5 … −3.0), under the opening and open into it, 15.0 deep | design layout (the mating face, Notes) |
| back wall | 6.0 (y 15 … 21) | design choice |
| contacts | eight, 0.5 wide × 0.6 thick × 8.0 long (y 5 … 13), on the opening's top face (z 4.4 … 5.0), at a 1.0 pitch: contact 1 at x −3.5 (left, seen from the front with the latch slot down) to contact 8 at x +3.5 | design layout (the mating face, Notes) |
| overall | 16.0 × 21.0 × 14.0 | the housing |

The mating face, the plug's side of the joint: the opening, the latch slot, the contacts' pitch, their order and their reach into the opening are the 8-way modular connector's mating interface, and its standard is not on file: NOT ON FILE (B): IEC 60603-7 (lib/standards/sources.csv lists no row for it). Drawn to the design layout above, so two of these elements mate each other's plugs only as this design; a maker's RJ45 plug is not claimed to fit.

## Named nodes
Contacts `c-1` … `c-8`, each a port (kind port, unit rj45, axis −y, at the contact's front tip, gender female). The housing is the `body` node: nothing moves. pins.csv says what each contact passes; the host's pins.csv says what it carries.

## Materials by layer
`M-BLACK-PA` housing · `M-GOLD` contacts (the opening and the latch slot are cuts, no layer of their own)

## Decals (Blender)
None: the front face carries no field big enough for a legend; the host's legend names the port. No maker's name, logo or approval mark.

## Notes
- One open figure: the mating face's line under Dimensions (class B, a fit: a document wanted, lib/standards/wanted.md, not EM's). Every other size is a design choice; no rating is claimed.
- Not modelled: a metal shield (this design is unshielded), the contacts' tails and the board-lock pegs (the host's board is not modelled), link / activity LEDs (led is not built: OPERATING.md 12, quality at the source; a later version may add the light pipes), a dust cover.
- hmi-7in 1.0 draws no Ethernet socket yet (its spec.md Notes): it places this element at its next version, once this is past station 6.
- Not a safety-function device.

## Outputs (out/)
`port-rj45.lsp` · `.glb` (a port pivot on every contact, `env-colonly` collider) · `preview-*.png`. Gates through the lock: 1.0 in elec-r44 (lib/rounds/elec/r44.md).

## History
| version | change |
|---|---|
| 1.0 | elec-r44 (2026-11-12, unattended): first build, generic ETIM 10.0 EC001121, our own design; common part for the Ethernet ports of hmi-7in and the inventory's other hosts |
