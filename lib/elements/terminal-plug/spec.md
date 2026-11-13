# terminal-plug · v2.0 · pluggable terminal block, plug with screw clamps, 5.0 mm pitch, 4 poles (complexes.org generic)

**What** The plug half of a pluggable terminal block: a row of screw clamps in one housing that plugs onto a header on a device (a PLC, an I/O module, a control transformer, a drive), so the device can be changed without undoing its wires. 5.0 mm pitch, 2 to 12 poles by parameter (built with 4), 12 A, 250 V, the clamp screws on the front, the wires in from below, the sockets in the mating face. A common part (lib/inventory.csv: part of 22 devices); a host carries the header and places this element on it, version pinned. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002021, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Terminal block connector (ETIM 10.0 EC002021). The class values are this element's definition (design inputs); every size is a design choice, said so below (no standard on file fixes a plug's pitch or body; the clamps' standard, IEC 60999, is not on file, lib/standards/sources.csv). Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: mating face on the host's header y = 0, body toward −y (away from the host), left face x = 0, poles along +x, z = 0 on the sockets' axis.
**Built with** toolkit 1.3 · AutoLISP command `TERMPLUG` · parameter `poles` (2 … 12; 4 as built and gated).

## Class values
ETIM 10.0 EC002021 "Terminal block connector", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Model (EF000010) | plug (the plug half; the header is the host's) |
| 2 | Connectable conductor cross section (EF008200) | not stated (the clamps' conductor range is open, class B: Dimensions) |
| 3 | Connectable conductor cross section fine-strand without cable end sleeve (EF007341) | not stated (as 2) |
| 4 | Connectable conductor cross section fine-strand with cable end sleeve (EF007339) | not stated (as 2) |
| 5 | Connectable conductor cross section solid-core (EF007337) | not stated (as 2) |
| 6 | Connectable conductor cross section multi-wired (EF007343) | not stated (as 2) |
| 7 | Rated current In (EF008250) | 12 A (each pole) |
| 8 | Rated voltage (EF000228) | 250 V |
| 9 | Total number of poles (without ground contact) (EF006240) | 4 as built; 2 to 12 by the parameter `poles` |
| 10 | Type of electric connection (EF003961) | screw connection |
| 11 | Width (EF000008) | 20.0 mm at 4 poles (poles × 5.0) |
| 12 | Connectable (EF006169) | yes (plugs onto the host's header) |
| 13 | Number of poles (EF001391) | 4 as built (as 9) |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design"); `pins.csv` gives each port its role; `behaviour.csv` what the solver reads (each clamp and its socket one conductor).

## Dimensions
| item | value | source |
|---|---|---|
| housing | (poles × 5.0) × 16.0 × 14.0 (x 0 … 5.0 n, y −16 … 0, z −6 … 8): 20.0 wide at 4 poles | design choice |
| pitch | 5.0 between pole centres (x 2.5, 7.5, 12.5, …) | design choice (class value 11) |
| pull grip | along the top front edge, the housing's width × 4.0 × 1.5 (y −16 … −12, z 8 … 9.5) | design choice |
| screw wells | one per pole in the front face: 3.6 × 3.0 deep × 3.6 high, centre z 3.5 | design choice |
| clamp screws | head Ø3.0 × 0.6 at each well's floor (y −13.0 … −13.6), axis along y | design choice |
| wire entries | one per pole in the bottom face: 3.2 × 3.2 (y −12.1 … −8.9), the dark slot 0.5 deep | design choice (the shape of toolkit/din.py `terminal_row`) |
| sockets | one per pole in the mating face: 2.0 × 2.0 on z = 0, open 6.0 deep (y −6.0 … 0, the engagement depth), the dark floor 0.5 thick at its bottom (y −6.0 … −5.5); each takes a 1.0 × 1.0 square header pin | design choice: this element defines the joint, and a host builds its header to it |
| header pin (the host's) | 1.0 × 1.0 square, centred on its socket (x = 5.0 k − 2.5, z = 0), free length past the mating face at most 5.0 (the socket is open 5.5 above its floor; the pin ends 0.5 short of the floor, so it touches nothing of the plug) | design choice of this joint (2.0, review elec-r22 finding 1); the host models it to these figures |
| conductor range of the clamps | the wire sizes and ferrules each clamp takes, the screws' thread and their torque | NOT ON FILE (B): a fit with the wire element; the clamps' connecting capacity is set by IEC 60999, which is not on file (lib/standards/sources.csv), so no size is claimed |
| overall | 20.0 × 16.0 × 15.5 at 4 poles (x 0 … 20, y −16 … 0, z −6 … 9.5) | from the parts above |

Pole marks 1 … n from the left, a design choice (the plug's legend; no standard on file sets them).

## Named nodes
Ports `t-1` … `t-n` (the clamp screws; kind port, unit screw, gender none: a screw clamp, PIN-002) and `s-1` … `s-n` (the sockets; kind port, unit pin, gender female: each takes a header pin, PIN-002; the node is the socket's dark floor, the pivot stays on the mating face y = 0). No moving node: the clamp cages and the contact springs inside are not modelled.

## Materials by layer
`M-GREEN` housing and grip · `M-ZINC` clamp screws · `M-GASKET` wire entries and sockets

## Decals (Blender)
On the top face behind the grip: the pole marks 1 … n over each pole. On one end face: "complexes.org generic", "terminal-plug", "12 A 250 V", "5.0". No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the clamps' conductor range, thread and torque (class B, above). Everything else is a design choice of this element; nothing is guessed and shown as sourced.
- The plug is held on the header by the sockets' grip alone: no locking flange or screw flange (a host that needs one asks for it at the plug's next version).
- Not a safety-function device. A host whose circuits need touch protection with the plug pulled carries the male pins on its side (the header), as the class's usual form does: the sockets here are female.

## Outputs (out/)
`terminal-plug.lsp` · `.glb` (pivots on the ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot) at 1.0 in elec-r22, at 2.0 in elec-r26 (lib/rounds/elec/r26.md).

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC002021), our own design; elec-r22 (unattended, 2026-11-09) |
| 2.0 | the joint gets a depth (review elec-r22 finding 1, terminal-plug-1.0 finding 1): each socket open 6.0 deep with its dark floor at the bottom (was a flush 0.5 slot), the header pin's free length 5.0 written as a design choice; a cut-out change, so a major. Nodes, origin and ports as 1.0. vfd-0.75kw, the one host, pins 2.0 at its 1.1. elec-r26 (unattended, 2026-11-09) |
