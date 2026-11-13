# valve-sol-52-sr · v2.1 · four-way solenoid valve 5/2, generic, single solenoid, spring return, 24 V DC, body ported NPT 1/4

**What** a four-way, two-position (5/2) directional valve for a double-acting cylinder: single solenoid, spring return, pilot
operated from its own supply, with a locking manual override and a coil LED. Body ported: every port is on the body's front face,
and two M4 screws hold its back face on a panel. Unpowered (spring), port-1 feeds port-2 and port-4 exhausts through port-5; with
the coil (14) on, port-1 feeds port-4 and port-2 exhausts through port-3 (ISO 11727 numbering, pneu.py D6). It is our own
vendor-neutral design of the ETIM class below (OPERATING.md 12, generic elements, EM 2026-11-07): the class values it is designed
to are listed under Class values. No maker's datasheet or CAD was opened or measured.
**Class** device · **Baseline** our own design: generic four-way solenoid valve (ETIM 10.0 EC010304). What it meets takes its
figures from the pneumatic contract, `toolkit/pneu.py` (D1 threads and the NPT table, D6 coil voltage and connector, D7 names) or
from ISO 273 for its fixing holes (lib/standards/holes.csv); every other size is a design choice (below).
Body ported on purpose: the valve-bank row's valves sit on ISO 15407-1 18 mm sub-bases (pneu.py D6), whose interface face is not on
file (pneu.ISO15407_18 is empty). A body-ported valve takes no interface face, so nothing in its shape waits on that standard.
**Units / frame** mm, Z up. Origin: surface mount (lib/README.md): back face on the panel y = 0, the left fixing hole's centre at
x = 0, z = 0; body toward −y, ports on the front face (−y), spool along +x, the solenoid at the left end. Ports follow pneu.py's
port frame: the pivot on the port's number field's outer face (y = −30.2; 2.0), its axis out of the body toward the counterpart,
so a placed male's hex seats on the field.
**Built with** toolkit 1.3 · AutoLISP command `VALVE-SOL-4WAY` · no parameters.

## Class values
ETIM 10.0 EC010304 "Four-way solenoid valve" (group EG020069), every feature in ETIM's order
(lib/standards/etim/class-features.csv). These are the values this element is designed to: they define it as a member of the
class, and they are design inputs. ETIM's features for this class are written for piped valves; a feature a body-ported air valve
has no use for is "not stated".

| # | feature | value | note |
|---|---|---|---|
| 1 | Housing material | aluminium | anodised body; pilot head, end cap and coil housing black polyamide |
| 2 | Material quality | not stated | |
| 3 | Nominal diameter | not stated | threaded ports; no DN is claimed |
| 4 | Outer pipe diameter connection 1 | not stated | a threaded port, no pipe end |
| 5 | Connection 1 | female thread NPT 1/4 | port-1, supply (pneu.py D1) |
| 6 | Outer pipe diameter connections 2, 3, 4 | not stated | threaded ports, no pipe ends |
| 7 | Connections 2-3-4 | female thread NPT 1/4 | port-2 and port-4 work, port-3 and port-5 exhaust (a 5/2 valve has four ports besides 1) |
| 8 | Valve bore | 6 mm | the spool's flow section; the internal passages are not modelled in 1.0 |
| 9 | Max. pressure difference for AC model | not stated | DC coil only |
| 10 | Max. pressure difference for DC model | 10 bar | |
| 11 | Min. pressure difference | 2 bar | internal pilot from port-1: the spool shifts only with 2 bar or more at port-1 |
| 12 | Medium temperature (continuous) | −5 to 50 °C | filtered compressed air, unlubricated (pneu.py D4: no lubricator) |
| 13 | Max. ambient temperature | 50 °C | |
| 14 | Indirect effect | yes | pilot operated: the solenoid opens a pilot, the pilot air shifts the spool |
| 15 | Switch-on duration | 100 % | continuous duty |
| 16 | Electrical connection | M12 plug, A-coded, male | pneu.py D6: pin 4 switched +24 V, pin 3 0 V, pins 1, 2 and 5 not connected; the receptacle is placed in a later version (Notes) |
| 17 | Connection voltage | 24 V | pneu.py D6 (COIL_V) |
| 18 | Voltage type | DC | |
| 19 | Frequency | not stated | DC |
| 20 | Degree of protection (IP) | IP65 | with the M12 cordset fitted; IEC 60529 code, the design target |
| 21 | Explosion safety | none | not for explosive atmospheres |
| 22 | Kvs value | not stated | |
| 23 | Max. viscosity | not stated | a gas valve |
| 24 | Length of connection 1 | 10.2 mm | NPT 1/4's thread length L2 (pneu.NPT, 10.205); the bore is L2 + 2 deep |
| 25 | Working length connection 1 | not stated | ETIM's working length is a piped valve's face-to-centre length; a body-ported valve has none of its own |
| 26 | Length of connection 2 | 10.2 mm | as 24 |
| 27 | Working length connection 2 | not stated | as 25 |
| 28 | Length of connection 3 | 10.2 mm | as 24 |
| 29 | Working length connection 3 | not stated | as 25 |
| 30 | Length of connection 4 | 10.2 mm | as 24 |
| 31 | Working length connection 4 | not stated | as 25 |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| body | 80 (x) × 30 (y) × 44 (z), anodised aluminium, x from −6 to 74, centred on z = 0 | holds five ports on one face with room for their fittings |
| fixing holes | 2 × Ø4.5 through y, at x = 0 and 68, z = 0 | M4 clearance, medium (ISO 273 H13, 4.5 to 4.68; lib/standards/holes.csv). The screw (screw-iso4762, not built yet) is placed in a later version (OPERATING.md 12) |
| fixing-hole position | Ø0.4 to A (back face), B (left end), C (bottom face); features.csv | design choice within the floating-fastener limit H − F = 0.50 (ASME Y14.5); ISO 2768-m alone gives Ø0.85 over 68 mm (GDT-010) |
| port places | lower row z = −10: port-5 x = 14, port-1 x = 34, port-3 x = 54; upper row z = +10: port-4 x = 24, port-2 x = 44 | 20 between neighbours in a row; 4 above 5 and 2 above 3, as the symbol reads |
| port bores | Ø13.616 plain (E1 + h of NPT 1/4), 12.205 deep (L2 + 2), blind, into the front face (2.0) | the thread drawn plain at the male stub's own diameter (fitting-pushin 2.0), so a placed male meets the bore face to face (tank 2.0's rule; review valve-sol-4way-1.0.md finding 1); deeper than a male's make-up L1 + L3 (10.02); 17.8 of body behind each floor; 5.19 of wall to the top and bottom faces, 6.38 between neighbours in a row, 8.75 across the rows, 8.1 to the fixing holes (element.py asserts at least 10 behind and 5 of wall). Declared in features.csv |
| port-number fields | 18 × 18, 0.2 proud, centred on each bore, the bore through it (2.0: 16 → 18, a ring round the wider bore) | the ISO 11727 number is a decal; 0.2 proud for GEO-050; each port's pivot on its outer face (2.0); 2 between neighbouring fields in a row and across the rows, 3 to the top and bottom faces, 2.75 (x) to the fixing holes |
| pilot head | 12 (x) × 28 (y) × 42 (z), left of the body, 1 inside its faces | carries the manual override |
| coil | 30 (x) × 26 (y) × 36 (z), left of the pilot head | its left end face (x = −48) is where receptacle-m12 stands in a later version |
| end cap | 6 (x), the pilot head's section, right end | the spring-return side (12) |
| manual override | Ø6, 1.5 proud, centre of the pilot head's front face; turns 90° to lock on | locking override, as pneu-1 asked for the valve-bank |
| LED | Ø3 lens, 0.6 proud, on the coil's front face, upper right | lit while the coil is on |
| label field | 60 × 14, 0.2 proud, centred on the body's top face | "complexes.org generic", the ISO 1219 symbol and "24 V DC" decals |

## Ports (toolkit/pneu.py)
| node | unit | gender | role | basis |
|---|---|---|---|---|
| `port-1` | NPT1/4 | female | supply | pneu.py D1 (NPT, ASME B1.20.1), D6 and D7 (ISO 11727 numbers) |
| `port-2`, `port-4` | NPT1/4 | female | work | as above |
| `port-3`, `port-5` | NPT1/4 | female | exhaust | as above; PNE-005 asks a silencer on each in an assembly |

NPT 1/4 is our choice within pneu.THREADS. The ports are female and take sealant on the male (PNE-002).

## Open figures
None. 1.0's one open figure (the NPT 1/4 thread, while pneu.NPT was empty) is closed in 2.0 by pneu.NPT on file: each port is
bored at the male stub's own diameter and depth (Its own sizes), the thread drawn plain.

## Ratings (ratings.csv)
p_max 10 bar, p_min 2 bar and coil_v 24 V DC, each status "generic design", the source naming its class value, as review
valve-sol-4way-1.0.md finding 2 asks: class values 10 (EF023852 Max. pressure difference for DC model: with a work port vented,
port-1 carries the whole difference, so the lane reads it as p_max, as valve-sol-32nc-sr 2.0), 11 (EF020189 Min. pressure
difference) and 17 with 18 (EF003625 Connection voltage, EF000187 Voltage type; pneu.py D6 COIL_V). These are the keys PNE-003,
PNE-007 and ELR-021 read: 10 bar ≥ P_SUPPLY (689.5 kPa) and 2 bar ≤ P_WORK_MAX (551.6 kPa), both asserted in element.py.

## Named nodes
`port-1` … `port-5` (kind port, fixed; range 0) · `coil-14` (fixed: the coil the twin switches) · `ovr-14` (rotate about −y at the
pilot head's front face, 0 to 90°: off to locked on) · `led-14` (emissive, 0 to 1)

## Materials by layer
`M-ALU-ANOD` body · `M-BLACK-PA` pilot head, coil, end cap · `M-YELLOW-PA` manual override · `M-LENS-YELLOW` LED ·
`M-WHITE-PA` fields

## Decals (Blender)
port numbers 1 to 5 on their fields (ISO 11727); "14" beside the override and the LED; the ISO 1219-1 symbol of a 5/2 single
solenoid, spring return, pilot operated valve, "24 V DC" and "complexes.org generic" on the label field. No vendor names, no
approval marks.

## Notes
- The coil's connector: pneu.py D6 puts a receptacle-m12 (male, A-coded) on every coil. receptacle-m12 has not passed station 6
  (its AutoCAD gate is at an older version), so 1.0 does not place it (OPERATING.md 12, foundation first). It is placed on the
  coil's left end face in a later version, with a port node and pins.csv (pin 4 switched +24 V, pin 3 0 V); a new node makes that
  version a major one. Until then the valve cannot be wired in an assembly.
- ratings.csv (2.0) carries the class values the checks read (Ratings above), as OPERATING.md 12 asks of a generic element.
- The coil's current is not a feature of the class and is not stated (ELR-020 needs it once the valve is wired); the version that
  places receptacle-m12 and pins.csv writes it as an open class A figure or gives it a basis.
- Two fitting-pushin 2.0 hexes (17 AF, 19.04 across corners) in neighbouring ports of a row, 20 apart, clear each other by 0.96
  (review valve-sol-4way-1.0.md note 1); whether a spanner reaches between them is for the first assembly that places them to show.
- No safety function: the valve is not a safety device; a dump valve upstream (PNE-008) is the assembly's.

## Outputs (out/)
`valve-sol-52-sr.lsp` · `.glb` (port, override and LED pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/
from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC010304), cloud-pneu 2026-11-07 (the core chat's cloud builder, the PC being down): body, fixing holes, five port bores and fields, pilot head, coil, end cap, override, LED; stations 1 to 5; gates pending (AutoCAD, Blender, Godot on the PC) |
| 2.0 | pneu-r76 (unattended; review valve-sol-4way-1.0.md findings 1 and 2): each port's bore Ø11.5 × 12 → Ø13.616 (E1 + h) × 12.205 (L2 + 2) from pneu.NPT, its role in features.csv; port-number fields 16 → 18; each port pivot on its field's outer face (y −30.2; filter-air 3.0's fix); the thread line closed (pneu.NPT on file); class values 24, 26, 28 and 30 the thread length L2, 25, 27, 29 and 31 with their own reason; ratings.csv p_max 10 bar, p_min 2 bar, coil_v 24 V DC (class values 10, 11, 17 and 18); nodes unchanged |
| 2.1 | pneu-r79 (unattended; review valve-sol-4way-2.0.md finding 1, pneu-r76 finding 1): text only. element.py's docstring no longer says the thread form is missing or open (the sentences of 1.0 deleted; the bores have come from pneu.NPT since 2.0). No geometry, node, origin or cut-out changed |
