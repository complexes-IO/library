# hook-rack · v1.0 · hanging rack for powder coating, spine 1530 with a Ø18 hang eye, four cross-bars 800 wide, 32 L-pins Ø8

**What** A hanging rack that carries small parts through a powder coating line: hung by its eye from the overhead conveyor's hook,
it takes the parts through the booth and the cure oven. Each part hangs by a hole on one of the pins; the pin's upturned tip keeps
it from sliding off. It is the rack of the powder-coating system (lib/machines-factory.txt line 69: booth-powder (own), gun-powder,
hopper-powder, fan-exhaust, filter-cartridge, compressor-air, frl, oven-cure (own), heater-oven, thermostat-enc, tt-rtd,
conveyor-overhead, hook-rack (own), plc0, hmi-7in, enc-wm, op-estop-22-2nc).
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks hook-rack own_design
"yes"). No product was matched and no vendor file was opened. Every size is a design choice.
**Units / frame** mm, Z up. Origin: the hang point, the centre of the hang eye, x = 0, y = 0, z = 0. The rack hangs toward −z; the
cross-bars run along x; the pins stand out toward −y and +y. Extents x −400 to 400, y −64 to 64, z −1500 to 30.
**Built with** toolkit 1.3 · AutoLISP command `HOOKRACK` · no parameters.

## Mechanism
None: one fixed body, no node. On the line the whole rack swings on the conveyor's hook; that is the assembly's motion, not the
rack's.

## What it meets (figures from files on hand)
| figure | value | source |
|---|---|---|
| the overhead conveyor's hook | the Ø18 hang eye through the spine along y, centre at the origin, 21 of bar above it | conveyor-overhead is not built yet (machines-factory.txt line 69 lists it as new): how the eye fits its hook is checked when that element is on file |
| booth-powder's open front | 2000 × 2200 | booth-powder 1.0 (TITLE): the rack's 800 × 1530 is smaller; how high the conveyor runs is the assembly's |
| oven-cure's door opening | 1800 × 2100 | oven-cure 1.1 (TITLE): the same |
| the parts | none in this element | they hang by their own holes on the pins; they are the line's work, not the rack's |

No fastener hole is cut: the rack hangs, it is not fixed.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| spine | 50 × 20 bar, x ±25, y ±10, z −1500 to 30 | carries the cross-bars; 21 of bar above the eye |
| hang eye | Ø18 along y at z 0 | one hang point on the spine's axis, so the rack hangs plumb when its load is even |
| cross-bars | four levels, centres at z −350, −700, −1050 and −1400; each two halves 375 × 20 × 40 from the spine's sides to x ±400 | the halves abut the spine (one welded body); 350 between levels leaves room for parts hanging from the level above |
| pins | per cross-bar, four out of each face at x −300, −100, 100 and 300: an arm Ø8 straight out 50 from the face (starting 2 inside it), and a tip Ø8 turned up from the arm's axis to 20 above it, the arm ending on the tip's axis | 32 pins in all; the tip keeps a hanging part on the pin |
| rod and bar | bare steel | a design choice: the rack is stripped and reused; no earthing is claimed |

## Named nodes
None. Colliders `spine` and `bar-1` to `bar-4` (each cross-bar with its pins' envelope, y ±64).

## Materials by layer
`M-SILVER` every member (bare steel).

## Notes
No load rating: no part's mass is on file, so the rack is not sized against one. No earthing claim (an electrostatic line earths
the parts through the hook and conveyor; nothing here is claimed for it) and no safety claim. The volume without the pins is about 3 925 000 mm³
(spine 1 530 000 less the eye 5 090, cross-bars 8 × 300 000; lib/materials.csv gives steel no density, so
no mass is stated). No vendor names, no label.

## Outputs (out/)
`hook-rack.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r76, unattended) |
