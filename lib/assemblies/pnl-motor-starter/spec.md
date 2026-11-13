# pnl-motor-starter · v0.14 · the motor-starter panel for mc-motor-1

**What** The control panel of the motor bench mc-motor-1, built by the panel shop to the bench's controls spec
(lib/assemblies/mc-motor-1/controls.csv, 17 points) and shipped as one unit: the machine places it and pins its version, and
never models what is inside (lib/panel-shop.md).
**Type** motor-starter (lib/panel-types.csv): one motor branch (disconnect, branch breaker, contactor, thermal overload), 24 V DC
control, a safety relay, a small controller; four rails (safety and controller; control; power; terminals), horizontal ducts
between them, strip X1 and the PE blocks on the bottom rail.
**Baseline** our own design (complexes.org): the arrangement starts from pm-motor-starter 1.0, the panel the core laid out by hand
on 2026-11-03, with every element at the version on file on 2026-11-10.
**Units / frame** mm, Z up. Origin: the cabinet's (enc-1): floor anchors at the origin, doors toward -y. The same origin and
wall ports as pm-motor-starter, so dm-motor-starter-cell can swap one unit for the other.
**Built with** toolkit 1.3 · `assembly.py` from `bom.csv` (library.read_bom, place_on_hosts; P.assembly = True; no geometry of
its own) · AutoLISP command `PNLMS`.

**Status: v0.14 takes two text minors' pins (panel-r28, 2026-11-13): disc-3p-30a 1.7 and term-4mm 1.6 (elec-r48, each at
station 6: same nodes and origin). contactor-9a-1no1nc 1.3 (elec-r51: MOT-020 stops, GEO-070 seats, PIN-002 genders) is on main
but not at station 6 (no AutoCAD gate at 1.3: AutoCAD on the PC has answered no gate since 03:42), so k1's pin stays 1.2
(section 10); the build draws the element as main has it, 1.3. term-jumper's behaviour.csv on main now gives a pin for every
pole the placed build draws (elec-r50, request panel-13 item 2): jmp-3 (2 poles) has p-1 and p-2 only, so the solver carries no
loose pins 3 and 4 any more (review r23 note 2); wires.csv needs no change. The solver reads the loads as v0.13. 63 wires, 45
lengths.**
v0.13 pushes the combs home (panel-r26, 2026-11-13): request panel-13's answer item 1 declared a comb's blade in a
term-4mm block's body as a `seated` contact (lib/contacts.csv, `pnl-*, jmp-*.p-*|M-CU, x1-*.body`), so jmp-1 to jmp-3 stand
with their seating face on the blocks' front face, y 223.6 (212.0 in v0.12); the single-panel check accepts the 10 blade pairs
(GEO-030) and finds no interference (GEO-020, 2081 solids). Pins psu-24v-2a4 1.4, disc-3p-30a 1.6 (elec-r39 to r41's minors,
each at station 6: same nodes and origin). Text, from reviews r18, r20 and r21: section 10 lists the placed elements that are
not at station 6 and what holds each (the panel's own station 6 waits on them); section 8 says the conductors' insulation is
not on file. The solver with core's panel-14 fix reads the loads as before (k1's coil 24 V 0.242 A, the power lamp 0.02 A).
63 wires, 45 lengths.
v0.12 places the bridges of strip X1 (panel-r23, 2026-11-12): term-jumper 2.0 (elec-r36's major, at station 6 on
main since the library's merge of elec-r38) as three combs, jmp-1 (4 poles) on the +24 V group X1:1 to 4, jmp-2 (4 poles) on
the 0 V group X1:5 to 8, jmp-3 (2 poles) on the sensor-supply group X1:15 and 16 (request panel-3 item 1, kept since v0.2).
wires.csv's seven block-to-block stand-in rows become ten joins from each blade to its block (section 8). The combs are drawn
offered up, their blades' tips 0.1 in front of the blocks' front face, not inserted: term-4mm has no jumper channel on file
and its body is solid, so inserted the blades would stand in the blocks (term-jumper spec.md Notes; the same form as the
cordsets' plugs, section 9). Request panel-13 asks the core for the joint (section 7). Pins: term-4mm 1.5, mcb-1p-c6 1.5,
mcb-3p-c10 1.5, disc-3p-30a 1.5 (elec-r37 and r38's text minors, each at station 6: same nodes and origin). 63 wires, 45
lengths.
v0.11 bonds the cabinet's three earth studs (panel-r21, 2026-11-12): enc-fs-1524x1829x305 1.9 (mech-r96's minor,
from request panel-3 item 3) makes its M8 studs port nodes with pins PE1 to PE3, so wires 61 to 63, kept since v0.3, run from
PE:1 to the body's stud and from PE:2 and PE:3 across the hinges to the right and left doors' studs; the solver puts the doors
and the body on the PE net (section 8). xfmr-control pinned 1.1. 63 wires, 45 lengths.
v0.10 placed the controller's supply lead (panel-r18, 2026-11-12): w-pwr, the L-coded open-ended cordset held since
v0.7, now runs from plc-1's port-pwr down into duct-1680, left to riser-l, down to duct-1085 and out under it over X1:3 and
X1:7, through four fingers broken out with duct-40x60 1.3's `breakout` parameter (mech's minor, the answer to request
panel-11 item 1; section 9). Wires 22 and 29 are retired: the cordset's own leads 1 and 3 land on X1:3 and X1:7 (wires.csv's
plug-in and landed rows, as w-eth's). Every BOM row is placed. The two `t1` stand-in rows on q4's poles are gone: the core's
scene names key 4 q4 (q4.on) since its answer to request panel-12. Pins: duct-40x60 1.3 (released), mcb-2p 1.1 (elec-r32's
minor, station 6). Text: section 1's tables name the pinned versions (lib/reviews/panel/r15.md finding 1). 60 wires, 44
lengths.
v0.9 placed the control transformer and its primary breaker (panel-r15, 2026-11-12): t1, xfmr-control 1.0 (250 VA,
480 V to 120 V, generic, elec-r27), screwed to the back panel right of rail-2 (x 1092 to 1208, z 1485 to 1615; rail-2 shortened
from 1200 to 900 for it, section 3), and q4, mcb-2p 1.0 (elec-r28), on rail-2 at the place kept for it since v0.1. Both had
passed station 6 when this host placed them (OPERATING.md 12). Wires 11 to 17, kept since v0.3, are written and 18 added (t1's
frame to PE:6); the `t1` stand-in rows are gone, so the control circuit lives only from q1's load side: with q1 off the
transformer, the PSU, the safety relay and K1 drop (lib/reviews/panel/r11.md note 1; section 8). The spec's control_power row
is served (section 1). Four devices pinned at the minors the build already used, whose pins carry nodes now (q1, q2, q3, g1):
46 of the 62 wires have a length. The twin's scene still named its key 4 `t1`: two stand-in rows closed q4's poles on it
until the core's scene had q4.on (request panel-12; gone in v0.10).
**Gated at v0.12 (panel-r23, unattended, 2026-11-12), each the first run at v0.12:** AutoCAD PASS (gate/pnl-motor-starter-acad.json:
2060 solids as the LISP predicts, 16 more than v0.11's 2044: the three combs; 393 holes, AUDIT 0 errors, extents 1597.7 x 432.0
x 2182.0 unchanged, the DWG saved; PNLMS 85.3 s); Blender PASS (gate/pnl-motor-starter.json: export 227876 triangles); Godot
QA PASS (qa/pnl-motor-starter.json: 225440 triangles, 25 materials, 7 colliders, fail list empty; 1856 draw calls noted); the
twin's smoke run through the godot lock exit 0 (qa/twin.json: 2048 combinations of 11 inputs, 196 probe points, 95 flags at
rest, every step of the scene run). lib/metrics/panel.csv rows by lock.py.
**Gated at v0.9 (panel-r15, unattended, 2026-11-12):** AutoCAD PASS (gate/pnl-motor-starter-acad.json: 2012 solids as the LISP
predicts, 375 holes, AUDIT 0 errors, extents unchanged, the DWG saved; PNLMS 80.5 s); Blender PASS (gate/pnl-motor-starter.json:
368 meshes, every one clean; export 215822 triangles); Godot QA PASS (qa/pnl-motor-starter.json: 213530 triangles, 25 materials,
7 colliders, fail list empty; 1748 draw calls noted); the twin's smoke run exit 0 (qa/twin.json: 2048 combinations, 171 probe
points, 94 flags at rest; "power off" now drops the control circuit). lib/metrics/panel.csv rows by lock.py.
v0.8 was text only (panel-r14, 2026-11-11): two `field` stand-in rows in wires.csv join the I/O block's U_S 0 V (p-x2
pin 3) to p-x4 pin 3 and p-x5 pin 3, so the twin's meters for estop_ok, k1_aux and ol_trip (the core's scene, each against its
port's pin 3) read a net instead of "floating" (lib/reviews/panel/r8.md finding 1, change (a); section 8). The geometry is
v0.7's; Godot QA run at this version with round 30's qa.gd (below). The supply lead w-pwr stays held and the Ethernet plug
offered up: request panel-11's answer (2026-11-11) sends the duct's break-out to mech (a `breakout` parameter of duct-40x60) and
the socket's bore to elec (plc0 places receptacle-m12 once the core re-gates it); both come back as minors of this panel.**
v0.7 places the controller's Ethernet lead, the first cable routed inside a panel: w-eth, a D-coded open-ended
cordset (cordset-m12 1.8 `male-open`, the form core round 29 built for request panel-4's answer item 2) from plc-1's port-eth
down through a slot of duct-1680, along the row, down riser-r and out to p-x1's pigtail, where its four leads are spliced
(section 9). The controller's supply lead w-pwr (the L-coded twin of it, for X1:3 and X1:7) is in the BOM and held: its 9.8
cable passes none of the duct's 8.0 slots (section 2; request panel-11). plc-1 moved 6.5 to the right so its Ethernet socket
stands over a slot. Two modelling limits are written where they stand, for the reviewer: the plug is drawn offered up to the
socket, not inserted (plc0 1.2's socket is a solid with no bore: inserted, GEO-020 found 351 mm³), and the splice to the
pigtail has no place of its own (port-m12-a 1.4's pigtail is a plain sweep).** v0.6 placed the main disconnect q1 (the core's
answer to request panel-2, 2026-11-11: lib/motion.csv's three rows for the door-coupled switch carry the scope
p*-motor-starter, so the motion check leaves q1's body and shaft on the back panel and swings its handle unit with door-r);
with it the spec's supply row is served. The rest is v0.5's: the BOM with its two riser ducts and the three wall ports the
controller's signals leave by, this spec, the terminal plan (section 7) and the wire list, now 54 wires with 28 lengths
(section 8: the four Ethernet conductors are the cordset's). The wires are listed and the solver runs the panel from them;
they are not placed as wire elements yet, no wire has a gauge (the ampacity table: an attended reading, EM's), and 26 have
no length (section 8 says what each waits on). v0.6 also took the library's renames of the safety relay and the overload
(relay-safety-2ch-2no1nc, overload-9a-1no1nc: the same elements and versions, renamed on main in core round 29), the
reviewer's finding on the motor branch's design current (lib/reviews/panel/r1.md finding 1; section 5) and the core's
answers to requests panel-2 item 3 (the enclosure as a design choice; section 3) and panel-5 item 1 (read_bom reads `roll`).
69 BOM rows: 66 placed, 3 not placed (section 2). Pins no machine yet.
**Gated at v0.8 (panel-r14, unattended, 2026-11-11; v0.7's geometry):** Godot QA PASS (qa/pnl-motor-starter.json: triangles
209842, 25 materials, 7 colliders, fail list empty; the draw count, 1589, is noted and not failed since round 30's qa.gd, request
panel-9's answer: the panel's first Godot pass, so all three tools have passed, AutoCAD and Blender at v0.7 below); the twin's
smoke run through the godot lock exit 0 (qa/twin.json: 2048 combinations of 11 inputs, 137 probe points, 92 flags at rest, every
step of the scene run; the meters for estop_ok and ol_trip now read 24 V DC when the signal is on and floating when its contact
is open, where v0.7 read floating throughout: lib/reviews/panel/r8.md finding 1). lib/metrics/panel.csv row by lock.py.
**Gated at v0.7 (panel-r12, unattended, 2026-11-11):** AutoCAD PASS (gate/pnl-motor-starter-acad.json: 1973 solids as the LISP
predicts, the cordset's 38 among them, 371 holes, AUDIT 0 errors, extents unchanged, the DWG saved; PNLMS 76.0 s); Blender PASS
(gate/pnl-motor-starter.json: 328 meshes, every one clean; the swept cable w-eth.body 4868 triangles; export 212098 triangles);
the twin's smoke run through the godot lock (qa/twin.json): 2048 combinations of 11 inputs, 134 probe points (122 at v0.6: the
cordset's contacts and leads), 92 flags at rest, every step of the scene run, exit 0 (its first run stopped in Godot on a layer
the scene toggles, "Ethernet & communication", which the round's first wires.csv had emptied: the eight joint rows carry that
section now; lib/rounds/panel/r12.md). Godot QA not re-run (round 30's qa.gd not on main). lib/metrics/panel.csv
rows by lock.py.
**Gated at v0.6 (panel-r11, unattended, 2026-11-11):** AutoCAD PASS (gate/pnl-motor-starter-acad.json: 1935 solids as the
LISP predicts, 355 holes, AUDIT 0 errors, extents 1597.7 x 432.0 x 2182.0, the DWG saved; PNLMS 70.6 s); Blender PASS
(gate/pnl-motor-starter.json: 321 meshes, every one clean, non-manifold 0, inside-out 0, degenerate 0; export 200050
triangles: the port's D and L needles are gone with cadout.unneedle, request panel-9's answer); the twin's smoke run through
the godot lock (qa/twin.json; request panel-8's answer): 2048 combinations of 11 inputs solved, 122 probe points, 91 flags at
rest, every step of the scene run (rest, power on, doors open, the layer steps, field healthy, run, e-stop pressed and
twisted out, overload trips, reset, power off), exit 0. Godot QA not re-run: qa.gd's draw-call line changes in core round
30 (panel-9's answer, item 2), not on main yet; v0.5's result (1581 draw calls against 400, nothing else) stands until then.
lib/metrics/panel.csv has its first rows (autocad, blender; lock.py writes none for the twin). For the reviewer, from the
twin's "power off" step: with q1 off the 480 V leaves k1's line side, but the control circuit stays up (g1 120 V, k1
operated) because the 120 V secondary is a stand-in source (sources.csv `t1`) and not fed from q1's load side; that is the
stand-in's limit, gone when xfmr-control is on file (wires 11 and 12).
**Gated at v0.5 (panel-r8, unattended, 2026-11-11; the card's r4):** AutoCAD PASS (gate/pnl-motor-starter-acad.json: 1911 solids
as the LISP predicts, 354 holes, AUDIT 0 errors, the DWG saved); Blender FAIL (gate/pnl-motor-starter.json: p-x1.body and
p-x2.body, the D-coded and L-coded port-m12-a 1.4, carry one degenerate triangle each; the four A-coded ports and the other
311 meshes are clean; non-manifold 0, inside-out 0 everywhere; export 197608 triangles); Godot QA FAIL (qa/pnl-motor-starter.json:
1581 draw calls against the web budget of 400 for an assembly; triangles 195472 of 500000, 25 materials all from the library,
6 colliders, 10 lens materials). Neither failure is the shop's to fix: the port is the core's element (its own gates cover the
A-coded and male variants only) and the draw budget is a rule of lib/godot/qa/qa.gd that the core's own cell
dm-motor-starter-cell also fails (458). Request panel-9. The twin waits on a scene file the shop may not write (request panel-8).

## 1. The spec served, point by point (controls.csv, in its order)

"Served" means the device is in the BOM with the rating the row asks for on file. The wires that make each circuit are in
wires.csv since v0.3 (section 8); where a row below says "r3's", read section 8.

| point | kind | served | device and terminal, or what is missing and why |
|---|---|---|---|
| supply | power-in | yes (since v0.6) | q1 (disc-3p-30a 1.6: 3 poles, Ith 30 A on file, against the row's 30 A feeder), line terminals L1 L2 L3; handle on door-r (NFPA 79 5.3, the row's clause); the cable enters at gl-pe. Placed in v0.6 (section 2); the solver's run with q1.on set puts 277.1 V a phase on q1's load side and through q3, k1 and f1 on p-m1 (section 8). Open: the feeder is the row's Assumption (B); the supply cable's diameter is NOT ON FILE (B) (gl-pe takes one cord of 6.1 to 13 mm); q1's rated voltage is not in its ratings.csv (section 5) |
| control_power | transform | yes (since v0.9) | t1 (xfmr-control 1.0: 250 VA, primary 480 V 1U 1V, secondary 120 V 2U 2V on its placed plug, PE its frame) fed across L1 and L2 of q1's load side through q4 (mcb-2p 1.1: two poles on one handle and one trip, so both open together; the core's answer to request panel-1 item 2); 2U to q2 (mcb-1p-c6 1.5, 6 A C) and on to g1.L; 2V, the grounded end, to g1.N and bonded to PE:6 at the transformer (NFPA 79 9.1.1 and 9.1.3, the row's clauses). Wires 11 to 18. The row's 100 VA class (its Assumption (B)) against 250 VA on file: the 120 V load is g1's input, 0.5 A = 60 VA by the solver (section 8). Open (section 5): q4's rated current and q2 as the secondary's protection (NEC 430.72(C) tables), q2's rated voltage (not in its ratings.csv) |
| m1 | load | yes | q3 (mcb-3p-c10 1.5: 10 A C, 3 poles) terminals 1 3 5 / 2 4 6; k1 (contactor-9a-1no1nc 1.2, the id contactor-9a until the library's rename of 2026-11-11: 9 A AC-3 against 0.91 A) 1 3 5 / 2 4 6; f1 (overload-9a-1no1nc 1.1, range=D012, 0.8 to 1.2 A: EM 2026-11-03) T1 T2 T3; p-m1 (port-pwr-480 1.1: 20 A, 480 V) L1 L2 L3 PE. Open lines in section 5 (f1's range rows, the 480 V ratings, NEC 430.52) |
| start | DI | yes, outside the panel | the station's button lands on io-1 X1 A by the bench's cordset; the panel's part is io_link and io_power |
| stop | DI | yes, outside the panel | io-1 X1 B, as start |
| reset | DI | yes, outside the panel | io-1 X2 B, as start. The door's own reset button (enc-1.btn-reset 13-14) still has no way to the controller: the core's answer to request panel-1 names ports for the four signals below and none for the door's reset (X1:21 and 22 stay reserved) |
| estop | safety | in form; the claim is EM's | k-safe (relay-safety-2ch-2no1nc 1.2): S11 and S21 out through the door e-stop's two channels (enc-1.estop-door 11-12, 21-22) and the station's e-stop (p-x3), back on S12 and S22; output 13-14 in K1's coil chain. Stop category 0, PL d / category 3 is the row's Assumption (A): EM's, with his safety sign-off (lib/needs-em/panel.md: one contactor, no feedback loop) |
| estop_ok | DI | yes | k-safe's safety output 2, 23-24 (N.O., closes with the relay on: the row asks for an N.O. monitored output; v0.3 named the N.C. auxiliary 41-42, which closes with the relay off and is what the press's spec calls safety_fb), fed from io-1 port-x3's own U_S (pin 1) and back to io-1 X3 A (pin 4) through the panel's A-coded wall port p-x4 (request panel-1 answer 3.b and 3.c; the point moved from X2 A to X3 A in controls.csv). Wires 50, 51, 69, 70 |
| k1 | DO | yes | k1 coil A1 A2 (24 V DC, 5.8 W on file: the row's coil voltage met). The chain since v0.5: the controller's run output, io-1 X7 A (port-x7 pin 4), comes in by the wall port p-x6 to X1:13 and sources f1 95-96, k-safe 13-14, k1 A1; A2 returns to the 0 V bus (answer 3.a). Open: the output port's return pin is io-1's NOT ON FILE (A) (its spec: the supply pins of X5 to X8), so it is not wired and X1:14 is kept for it |
| ol_trip | DI | yes | f1 97-98 (N.O., closes on a trip) fed from io-1 port-x4's U_S and back to io-1 X4 A (pin 4) through the wall port p-x5; f1 95-96 (N.C.) stays hardwired in K1's coil chain, so a trip drops K1 with no controller in the path (answer 3.d, IEC 60204-1 7.3 as the row cites it; the point was ol_ok on 95-96 until 2026-11-11). Wires 64, 65, 66, 68 |
| k1_aux | DI | yes | k1 13-14 (N.O.) from the same U_S (X1:15 and 16 bridged) back to io-1 X4 B (pin 2) through p-x5 (answer 3.c). Wires 48, 49, 67 |
| h1_run | DO | yes, outside the panel | the station's lamp on io-1 X6 B |
| h2_fault | DO | yes, outside the panel | the station's lamp on io-1 X5 A |
| io_power | field-power | yes | g1 (psu-24v-2a4 1.4: 24 V DC, 60 W) +V and -V to p-x2 (port-m12-a 1.4, L-coded): pins 1 and 4 +24 V (US, UL), 2 and 3 0 V, 5 FE. The load sum is section 4. The controller's own supply, plc-1 port-pwr (L-coded) from X1:3 and X1:7, is the cordset w-pwr (cordset-m12 1.8, L-coded, open-ended; placed since v0.10, section 9): its plug in port-pwr, its leads 1 and 3 landed on X1:3 and X1:7 (wires 22 and 29 to v0.9) |
| io_link | comm | yes (placed since v0.7) | plc-1 (plc0 1.2) port-eth to p-x1 (port-m12-a 1.4, D-coded, IEC 61076-2-101 by the row), pins 1 to 4, by the cordset w-eth (cordset-m12 1.8, D-coded, open-ended: its plug at port-eth, its leads spliced to p-x1's pigtail; section 9). Open: the cordset's conductor size is NOT ON FILE (B) (cordset-m12 spec.md: the D cable's); the plug is drawn offered up, not inserted, and the splice has no place in the model (request panel-11 items 2 and 3) |
| estop_chain | field-power | yes | p-x3 (port-m12-a 1.4, A-coded): pins 1 and 3 out (channels 1 and 2 from the door e-stop), 2 and 4 back to k-safe S12 and S22; pin 5 unused |
| bonding | safety | yes, with an open line | pe-1 to pe-6 (term-4mm 1.5, kind=ground); the bench's bonding cable enters at gl-pe-2 (a second gland-m20: one cord a gland) and lands on PE:2, the supply's PE at gl-pe on PE:1 (section 7). Since v0.11 the cabinet's three M8 earth studs are bonded: wires 61 to 63 from PE:1 to 3 to enc-fs-1524x1829x305 1.9's pins PE1 (pe-body), PE3 (pe-door-r) and PE2 (pe-door-l) (section 8; the solver puts all three on the PE net). Open: the rail as the blocks' common is NOT ON FILE (B) (section 7) |

Count (v0.12, unchanged since v0.9): 16 served (5 of them outside the panel; bonding has an open line; k1 with the return pin's open line), 1 in form
(estop), none not served. v0.6 to v0.8 had 15, 1 and 1 (control_power). v0.5 had 14, 1 and 2 (supply until q1 was
placed); v0.4 had 10, 1, 3 half and 3 not served: the answer to request panel-1 freed estop_ok, k1, ol_trip and k1_aux.

The three ports it took (bom.csv): p-x4, p-x5 and p-x6, port-m12-a 1.4 A-coded on the right wall at z 1450, 1400 and 1350,
the ports' 50 pitch below p-x3 (the wall is bare there: q1 is held and the receptacle p-m1 stands at 1100). One port per
io-1 port served (answer 3.c): p-x4 to io-1 port-x3, p-x5 to port-x4, p-x6 to port-x7. The cordsets between them are the
cell's (dm-motor-starter-cell/connections.csv, when it places this panel: answer 3.c).

## 2. BOM rows not placed

| tag | element | why | what clears it |
|---|---|---|---|
| q1 | disc-3p-30a 1.4 | **placed since v0.6.** v0.1 to v0.5 held it in assembly.py (`HOLD`): its parent is enc-1.door-r (the door gets the handle's cut-out), and MOT-010 swings every child of a moving node with it, the switch body on the back panel too, unless lib/motion.csv says the body stays; its three rows named pm-motor-starter only. The core's answer to request panel-2 (2026-11-11) gave the rows the scope `p*-motor-starter` (fnmatch: pm- and pnl-motor-starter, nothing else on file), unchanged otherwise: (enc-1.door-r, q1) exclude, q1.door-unit and q1.handle follow. They hold while the panel keeps the tags enc-1 and q1, as it does. `HOLD` is empty; the row is as pm-motor-starter's (door-r, x 1250, z 1480, shaft 243.1, door_t 1.9) | cleared |
| t1 | xfmr-control 1.1 | **placed since v0.9** (elec-r27's generic element, station 6 passed): on the back panel, section 3; pinned 1.1 since v0.11 (elec's minor, station 6 passed: same nodes and origin) | cleared |
| q4 | mcb-2p 1.1 | **placed since v0.9** (elec-r28's generic element, station 6 passed): rail-2 x 290; pinned 1.1 since v0.10 (elec-r32's minor, at station 6) | cleared |
| w-pwr | cordset-m12 1.8, L-coded, open-ended | **placed since v0.10** through four breakouts of duct-40x60 1.3 (section 9); `HOLD` is empty. v0.7 to v0.9: **held in assembly.py** (the row is in the BOM at its version, at plc-1's port-pwr, x 305). The L cable is 9.8 across (cordset-m12 element.py CABLE_D, from the cut sheets on file) and duct-40x60's finger slots are 8.0 wide (its SLOT, from the duct's drawing); every way into the duct system is a slot (the rows' walls, the risers' walls) or a riser's open top end at z 1975, so no path from the socket at z 1784.9 to X1 passes GEO-020 (a 9.8 cable through an 8.0 slot overlaps each finger 0.9 deep, about 5 mm³ a side, over the rule's 1 mm³ and 0.2 mm). In the shop a finger is broken out for a cable like this; the element has no parameter for it. Meanwhile wires 22 and 29 stood as single wires, as in v0.6 | cleared: duct-40x60 1.3's `breakout` (request panel-11 item 1) |

## 3. Arrangement and fill

Back panel 1372 x 1676 (enc-fs-1524x1829x305 1.9; 1.8 to v0.10). Four rails at z 1850, 1550, 1250, 950, 1200 long (rail-2 900 since v0.9); five 40 x 60 ducts above,
between and below them. Since v0.4 two risers, the same duct stood on end, join the five rows: riser-l at x 120 to 160 and
riser-r at x 1364 to 1404, both z 790 to 1975 (the bottom row's lower edge to the top row's upper edge), each 2 clear of the
rows' ends (162 and 1362). Design choices of the shop, read against the hosts' own solids: the back panel spans x 76 to 1448
and its four studs stand at x 116 and 1408, z 421.5 and 2017.5 (nut Ø17), below and above the risers; the rails start at
x 162. bom.csv's `roll` column (-90) stands them up; library.read_bom reads it since the core's answer to request panel-5
(2026-11-11; v0.4 and v0.5 converted it in assembly.py). Rail length used, from the elements' envelopes in lib/catalogue.csv (derived: a sum):

| rail | devices | used of 1200 |
|---|---|---|
| rail-1 | k-safe 22, plc-1 90 (at x 246.5 since v0.7, 240 before: its Ethernet socket over duct-1680's slot at x 274 to 282; section 9) | 112 |
| rail-2 (900 since v0.9) | q2 18, g1 32, q4 35.4 (x 290 to 325.4, since v0.9) | 85.4 |
| rail-3 | q3 53, k1 45 (f1 hangs on k1) | 98 |
| rail-4 | end plate 2, X1 24 x 6.0, PE 6 x 5.0, end plate 2 | 178 |

473.4 of 4500 mm, 11 % (438 of 4800 to v0.8).

**The transformer (v0.9).** xfmr-control is a surface-mount device: its brackets' two flanges carry four M5 clearance holes
(ISO 273 medium, its own) at 100 x 110, its origin the lower-left hole, its body 116 wide, 130 high and 108 deep toward the door
(element.py: brackets x -8 to 108, flanges z -10 to 120). It does not clip on a rail, and at 130 high it spans rail-2's z
(1532.5 to 1567.5) wherever it stands in that band, so the row moved from the rail's reserved x 340 to the back panel at
x 1100, z 1495, y 275.6 (the plate's face, as the rails' and ducts' rows): body x 1092 to 1208, z 1485 to 1615, y 167.6 to 275.6.
Design choices of the shop, read against the hosts' solids: rail-2 ends at x 1062 (length 900; 30 clear of the brackets;
its panel screws at the 200 pitch, as before); q1's body on its shaft (x 1250) starts at about 1227.7, so 19.7 clear on the
right; duct-1680 is 65 above the upper flange and duct-1385 60 below the lower one, room for the primary's wires leaving the
top block upward and the secondary's and PE's downward. The single-panel check finds no interference among 2032 solids
(section 8). The four panel screws are the installer's (xfmr-control's spec: not built as elements); the panel has no tapped
holes or studs of its own, as for every device here. **design: enc-fs-1524x1829x305 (the floor cabinet pm-motor-starter 1.0 uses and dm-motor-starter-cell
already places, so the swap from pm-motor-starter moves no port and no cable; the door operators' cut-outs and the cell's
ports are what it meets today, checked by the build; the heat load against what the enclosure sheds comes with round 13's
IEC TR 60890 method, UL 508A's spacings once that document is on file).** The type's row reads "enc-fs-1524x1829x305 or
enc-wm, the shop's design choice" since the core's answer to request panel-2 item 3 (2026-11-11): no fill figure is on file
and none is a standard's (UL 508A sets spacings and wire bending space, not an enclosure size by rail fill). By the 9 %
figure the panel would fit a wall-mount enclosure; the floor cabinet is kept for the reason above. Duct fill is r3's (it
needs the wires). Spacings and wire bending space: UL 508A, NOT ON FILE (B) (to buy, lib/standards/sources.csv).

Strip X1: 24 feed-through blocks (x 192 to 336), 6 ground blocks (336 to 366), an end cover on each open side (190 to 368
over all: between two of rail-4's panel screws, whose heads stand on the crown at x 170 to 179 and 370 to 379; term-endplate
1.0) and one number tag a block (marker-terminal 1.0: X1:1 to X1:24, PE:1 to PE:6). An end stop to hold the strip on the rail is
not on file as an element (term-endplate's spec says so). The terminal plan is section 7.

**The bridges (v0.12).** Three combs of term-jumper 2.0 (bom.csv jmp-1 to jmp-3), each at its group's first block: blade 1 on the
block's centre (x + 3.0, the block's pitch 6.0 from term-4mm's SIZES), at z = rail + 9.2 (term-jumper spec.md: the design
channel's z, clear of clamp 1's screwdriver hole and of the marker tag by 0.2 each). jmp-1 x 195 (cap 192.25 to 215.75),
jmp-2 x 219 (216.25 to 239.75: 0.5 from jmp-1's, as that spec says two combs on neighbouring groups stand), jmp-3 x 279
(2 poles, 276.25 to 287.75). **A modelling limit, not a figure:** term-4mm 1.5 has no jumper channel (its fit is term-jumper's
NOT ON FILE (B), the maker's drawing of the block's bar jumper, an attended download), so a comb pushed home puts its blades in
the blocks' solid bodies. Since v0.13 the combs are pushed home: the seating face on the blocks' front face (268.1 - 44.5 =
223.6), each blade in its block's body, which lib/contacts.csv declares `seated` for every panel (`pnl-*, jmp-*.p-*|M-CU,
x1-*.body`; request panel-13's answer item 1: a modelling simplification, listed by GEO-030 in every report so it stays
visible). The row covers the blades and the block's body only: a cap or bar in a block is still GEO-020. v0.12 drew them offered
up (seating face at y 212.0). The core refused a channel of our own in term-4mm (it is measured from a maker's product); the row
goes when the maker's drawing of the bar jumper is on file. The joint is wires.csv's (blade k to the k-th block's pin 1).

## 4. The 24 V load against g1 (derived: a sum of the elements' ratings.csv)

| load | A | status in its ratings.csv |
|---|---|---|
| k-safe | 0.17 | derived (4 W typical) |
| k1 coil | 0.24 | derived (5.8 W) |
| plc-1 | 0.15 | assumption (own design) |
| enc-1.lamp-power (op-pilot-22) | 0.02 | assumption |
| io-1 US, through p-x2 | 0.14 typical; 1.0 at most with sensor load | on file |
| the station's two lamps, through io-1's outputs (UL) | 0.04 | assumption (2 x 0.02) |
| f1 | 0 | on file (thermal) |

Sum 0.76 A typical, 1.62 A with io-1's US at its 1 A limit. g1: 60 W at 24 V = 2.5 A (derived in its ratings.csv; the spec row
and the element's id say 2.4 A), 2.0 A at the 0.8 loading its ratings.csv carries as an assumption. 1.62 A is within 2.0 A.
The three assumption rows are their elements' (elec's), not the panel's to accept.

## 5. Ratings, open lines

- Motor branch design current: 1.25 x the motor's Table 430.250 current, NOT ON FILE (B): NEC 2023 Table 430.250 (view-only;
  the same attended reading as the ampacity table, request panel-1 item 4). NEC 430.6(A)(1) takes the conductors' ampacity
  and the branch protection's rating from Tables 430.247 to 430.250 by the motor's horsepower, not from the nameplate;
  the nameplate's 0.91 A sizes the overload f1 only (430.6(A)(2); lib/reviews/panel/r1.md finding 1, taken in v0.6). v0.1
  to v0.5 wrote 1.25 x 0.91 A = 1.14 A here and in wires.csv's header; no gauge was chosen from it (none is filled). The
  reviewer's reading of the table (1.1 A for ½ hp at 460 V, so 1.38 A) is not on file and is not written as a figure here;
  the attended reading settles it. For the core: mc-motor-1/controls.csv's m1 row gives the nameplate figure under
  "NEC 430.22 and 430.52" (the same finding).
- q3 as the branch protection of a 0.91 A motor: the largest rating NEC 430.52 allows is a table's figure, NOT ON FILE (B)
  (NFPA 70 is view-only, not read into a table).
- f1: the BOM's range=D012 (0.8 to 1.2 A) covers 0.91 A, but overload-9a-1no1nc's ratings.csv lists one range only (7.0 to 10.0 A) and
  its heat-loss rows are that range's. The D012 range's figures are not in ratings.csv (elec's; lib/rounds/panel/r1.md).
- Rated voltages at 480 V: mcb-3p-c10, mcb-1p-c6, contactor-9a-1no1nc and disc-3p-30a have no rated-voltage row in ratings.csv
  (port-pwr-480 has 480 V; overload-9a-1no1nc has Ui 690 V). So "480 V" is met on file only at p-m1 and f1.
- Short-circuit current rating: NOT ON FILE (B): UL 508A (to buy), and no device's interrupting rating is in its ratings.csv.
  The panel claims none.
- Heat load, from what is on file: k1 coil 5.8 W, k-safe 4 W, plc-1 3.6 W (assumption), lamp 0.48 W (assumption), f1 0.9 to
  1.7 W (the 7 to 10 A range's rows) = 14.8 to 15.6 W. Not in the sum because not on file: g1's own loss (its efficiency), the
  pole losses of q1, q2, q3 and q4, t1's losses. No temperature-rise method is on file, so no rise is claimed.
- q4 (v0.9): mcb-2p 1.0's rated current is not chosen (its spec: NEC 430.72(C) NOT ON FILE), so the transformer primary's
  protection is NOT ON FILE (B): NEC 2023 430.72(C) and 450.3(B) (tables; view-only, not read into lib/standards). The
  primary draws 0.52 A at 480 V (t1's ratings.csv i1, derived from 250 VA).
- q2 as the secondary's protection: 6 A C (mcb-1p-c6) against t1's rated secondary 2.08 A (its ratings.csv i2, derived:
  250 VA / 120 V). Whether 6 A protects that secondary is the same tables' question: NOT ON FILE (B): NEC 2023 430.72(C).
  Not claimed either way.
- The category and PL of the e-stop function: the spec's Assumption (A), EM's.

## 6. What v0.1 changes from pm-motor-starter 1.0

Versions as on file (enc 1.6 to 1.8, duct 1.0 to 1.2, safety relay 1.1 to 1.2, both breakers 1.2 to 1.3, PSU 1.0 to 1.2,
term-4mm 1.0 to 1.4, plc0 1.1 to 1.2, gland 1.1 to 1.3: all minors, same nodes and origin). Added: two end covers and two
marker strips on X1; gl-pe-2; the planned rows t1 and q4. Not placed: q1 (section 2). Positions of everything else unchanged.

## 7. The terminal plan (terminals.csv; role card r2; arrangement: NFPA 79 13.1 as the card cites it)

NFPA 79 is view-only and not read into a table (lib/standards/sources.csv), so the plan quotes none of its wording; the rules
below are the shop's design rules, written as such, and the reviewer reads them against the clause.

- **Two strips on rail-4**: X1 (control, 24 V DC; 24 feed-through blocks) and PE (6 ground blocks). Side 1 of a block (clamp 1,
  the top entry) takes the panel's devices; side 2 (clamp 2, the bottom entry, toward duct-790 and the gland plate) takes what
  leaves the panel.
- **One conductor a clamp** (design: the shop's rule; how many conductors a clamp of term-4mm may take is not in its brief). The
  core's test wiring of pm-motor-starter puts nine wires on x1-1.2 and seven on x1-2.2; this plan has none with more than one.
  A potential with more than two ends is therefore a bridged group of blocks: +24 V on X1:1 to 4 (seven ends, one clamp
  spare), 0 V on X1:5 to 8 (eight ends), and the sensor supply of the port for io-1 X4 on X1:15 and 16. The bridge is
  term-jumper (request panel-3 item 1): since v0.12 term-jumper 2.0, one comb a group (jmp-1, jmp-2 4 poles; jmp-3 2 poles;
  section 3). v0.2 to v0.11 the groups were planned and joined in wires.csv by stand-in rows.
- **What lands on X1** (v0.5: 20 of 24 named, 1 reserved with nothing on it, 3 spare): the 24 V bus and its two door wires
  (X1:1 to 8; X1:4 is the +24 V group's spare since the coil chain's head moved); the four conductors of the e-stop chain's
  port p-x3 (X1:9 to 12); the run output in on X1:13 (the chain's head: f1 95 on side 1, p-x6 pin 4 on side 2); X1:14 kept
  for the output port's return pin (io-1's NOT ON FILE (A)); the sensor-supply group X1:15 and 16 (io-1 port-x4's U_S by p-x5
  pin 1) with k1 13 and f1 97 on side 1; k1_aux and ol_trip back out on X1:17 and 18 (p-x5 pins 2 and 4); estop_ok on X1:19
  and 20 (port-x3's U_S by p-x4 pin 1, k-safe 23-24, back on p-x4 pin 4); the door's reset reserved on X1:21 and 22 (the
  answer names no port for it); 23 and 24 spare.
- **What lands on PE**: the supply's protective conductor on PE:1 and the bench's bonding cable on PE:2 (side 2, from gl-pe and
  gl-pe-2); the receptacle's PE, the PSU's PE, the I/O block's FE, the 0 V bond (one point: X1:8 to PE:5; NFPA 79 8.2.1 as
  pm-motor-starter's wire 20 cites it); the cabinet's three M8 earth studs (body, door-l, door-r: enc-1's spec) on side 1 of
  PE:1 to 3; PE:6 the transformer (v0.9): its grounded secondary end 2V on side 1 (wire 17) and its frame on side 2 (wire 18),
  the one device on a side 2, since side 2 of PE:6 was spare and one conductor a clamp is kept.
- **What has no terminal**: the supply's phases (on q1 L1 L2 L3, the spec's supply row); the motor leads (f1 T1 T2 T3 to the
  receptacle p-m1's own terminals: X1 is the control strip and the BOM has no power strip, a design choice); the Ethernet
  link (p-x1's lead into plc-1 port-eth: a data pair is not broken at a screw terminal, a design choice); the panel's own
  circuits, device to device (the card's r2).
- The wire column (v0.3) carries wires.csv's numbers, side 1's then side 2's; a number in brackets is kept for a wire whose
  other end is not on file. X1:3 and X1:7 name the controller's pins by plc0's own marks (24V-1 and 24V-3: v0.2 wrote L+ and M,
  marks plc0 does not have).

Open lines of the plan:
- The PE blocks are joined only through their bonding feet and rail-4. The rail's rating as that protective conductor:
  NOT ON FILE (B): IEC 60947-7-2 (not in lib/standards/sources.csv; request panel-3 item 2).
- The earth studs are pins of enc-1's behaviour.csv since enc-fs-1524x1829x305 1.9 (PE1 to PE3, mech-r96, from request
  panel-3 item 3): v0.11 wires them (61 to 63), so the solver sees the doors and the body bonded. The back panel and the gland plate have no bonding point on file: the back panel carries rail-4, and with
  it the PE blocks' feet; whether that is its bond is the same standard's question.
- X1 is 24 V DC throughout, so the plan separates no voltages on it. Between the two neighbouring bridged groups (X1:4 on
  +24 V, X1:5 on 0 V) the combs' caps stand 0.5 apart (term-jumper 2.0 spec.md Dimensions, cap) and the insulation between
  them is the blocks' walls round each blade (its Class values 5); whether the block's maker asks for a partition between
  groups is in the maker's drawing that term-jumper names as its document wanted (NOT ON FILE (B)), not on file.
- The combs stand home since v0.13, declared `seated` (section 3; request panel-13's answer item 1). The core's answer to item
  3: X1 is 24 V DC throughout, no partition; the maker's drawing answers it with the channel.

## 8. The wire list (wires.csv, sources.csv; role card r3)

**What is there (v0.9).** 62 numbered wires, each from one pin to one pin by the marks of the elements' behaviour.csv, and 32
rows that are not wires (three plug-in joints of f1 in k1, eight joints of the Ethernet cordset w-eth (its plug's four
contacts in plc-1's port-eth, its four leads spliced to p-x1's pigtail), seven bridges, five rail joints between the PE
blocks, nine stand-ins: section's end). v0.12: the seven bridge stand-ins (block to block) became ten joins from each blade of
the three placed combs to its block (jmp-1.1 to x1-1.1 ... jmp-3.2 to x1-16.1; term-jumper 2.0's own contact rows join the
blades), so the groups are now the elements' own conductors. v0.9 wrote the seven kept numbers 11 to 17 with t1 and q4 placed and added 18 (t1's
frame to PE:6); the transformer's stand-in row (g1.N to pe-6.1) and sources.csv's (120 V on q2.1) went, and two stand-ins for
q4's handle came (below). v0.7 had 54 wires and 29 rows that are not wires. v0.7 retired the four Ethernet conductors 54 to 57 (plc-1.ETH-n to p-x1.n as wires, v0.3 to v0.6):
the link is the cordset, a BOM row, whose conductors are its own contact rows; v0.6 dropped the three stand-ins for q1's poles
with q1 placed. Three numbers were kept (61 to 63) for the wires to the cabinet's earth studs (11 to 17 were kept too until
v0.9); v0.11 writes them with the studs pins of enc-fs-1524x1829x305 1.9 (63 wires). v0.5 added the seven wires of the
answer to request panel-1 (64 to 70: ol_trip's two at f1 97-98 and the five to the new ports) and moved three (23, 25, 26: the
coil chain's head is the run output; 50 and 51 moved from k-safe 41-42 to 23-24).

| section | wires | colour (the card's list, NFPA 79 13.2.4 as it cites it) |
|---|---|---|
| 480 VAC power | 9 (1 to 9) | black |
| control (mains) | 7 (10 to 16) | the primary's four (11 to 14, 480 V) black, a power circuit; 10 and 15, the ungrounded 120 V, red; 16, the grounded 120 V conductor: NOT ON FILE (B): NFPA 79 13.2.4 (the card's list has no line for a grounded AC conductor) |
| control & 24 VDC | 38 (20, 21, 23 to 28, 30, 32 to 53, 64 to 70; v0.10: 22 and 29 retired for the cordset w-pwr's leads 1 and 3, joined by two plug-in and two landed rows without a number) | blue; the 0 V conductors (27, 28, 30, 44, 45, 47) white/blue |
| Ethernet & communication | none since v0.7: the cordset w-eth (bom.csv), joined by eight rows without a number | the cordset's own (M-CABLE-PUR jacket; conductor colours not on file) |
| ground | 9 (17, 18, 31, 58 to 63; v0.11: 61 to 63, the earth studs' bonds) | green/yellow |

- **Gauge: NOT ON FILE (B) on all 63 single wires** (60 in v0.10, 62 to v0.9; the cordsets' conductors are theirs: cordset-m12 spec.md): the conductor ampacity table (NEC 2023 310.16, NFPA 79 chapter 12) is
  view-only and not read into lib/standards/nec-conductors.csv, which has sizes only (request panel-1 item 4; the core's
  answer: an attended reading of NFPA 79 chapter 12 and 13.2 into a standards table, EM's). The design
  currents: the motor branch's is NOT ON FILE (B) (1.25 x the Table 430.250 current, section 5; v0.5 wrote 1.14 A from
  the nameplate); the 24 V feed 2.5 A at most (g1); each other load in section 4.
- **Insulation (v0.13; lib/reviews/panel/r20.md finding 1): NOT ON FILE (B): NFPA 79 13.1.3.** The ducts carry conductors of
  different circuits together: duct-1385, duct-1085, riser-l and duct-1680 carry 480 V (the motor branch 1 to 9, the primary 11
  to 14) and 120 V (10, 15, 16) in the same ducts as 24 V wires (wires.csv's route column). Conductors of different voltages may share a duct when each is insulated for the highest voltage in it, as the
  reviewer reads NFPA 79 13.1.3; that clause is not read into lib/standards/, and the wire element (lib/elements/wire 1.0) states
  no rated voltage (its insulation thickness is an Assumption from an IEC 60227-3 class). So the panel claims no insulation
  voltage and no separation by duct; the wires' rated voltage is the same attended reading as their gauge.
- **Colour** is complete for the single wires but one (16, above). Two are the shop's choice outside the card's list, for the
  reviewer: wire 31, the bond of the 0 V bus to PE:5, and wire 17, the bond of the transformer's grounded end to PE:6, are
  green/yellow (they belong to the bonding circuit); the card names white/blue for the grounded DC conductor and has no line
  for a bond. The transformer's primary (11 to 14) is black as a power circuit at 480 V, the card's "black power". No circuit
  of the panel stays live with the disconnect off, so none is orange: the control transformer is fed from q1's load side
  (wires 11 and 12, written since v0.9).
- **Route** names the ducts a wire runs in, by BOM tag. Since v0.4 the BOM has two risers (section 3): the 27 wires between
  two rows (20 to v0.8; v0.9's 11 to 15, 17 and 18: t1's primary block takes its wires from its top face, toward duct-1680,
  its plug and PE block from below, toward duct-1385, element.py) go by `riser-l` (the devices stand at the left of the rails), and the 19 wires and conductors to the M12 ports and
  the PE of the receptacle on the right wall leave by `riser-r` at the port's height (the three phase wires to the receptacle
  go straight from the row at its height). Nine wires cross the right door's hinge (`door-r`; v0.11 added 62) and one the
  left's (`door-l`, 63): the loom and its fixing are not elements on file.
- **Length: on 45 of the 63, in mm** (v0.11: 61, 1205, from PE:1 along duct-1085 and down riser-l out of its bottom end to the
  body's stud; 62 and 63 cross a hinge, so none; v0.10: 22 and 29 retired, the controller's supply is the cordset w-pwr's own leads,
  section 9; v0.9, 46 of 62: the eight new wires 11 to 18, 1755 to 2152, and ten that had none: 1 to 6, 10,
  20, 27, 59, now that disc-3p-30a 1.4, mcb-3p-c10 1.4, mcb-1p-c6 1.4 and psu-24v-2a4 1.3 give q1, q3, q2 and g1 pin nodes,
  request panel-4 item 1's answer; the BOM pins those minors since v0.9, which the build had already used; 28 of 54 in v0.7
  and v0.8; 32 of 58 in v0.6: the four Ethernet conductors are the cordset's now; 22 and 29 are 6 longer with plc-1 at x 246.5). The card takes it from the route. assembly.py `lengths()` computes it at every build
  and writes out/wire-lengths.csv; wires.csv carries the same figures. The method, the shop's: square legs (x, y and z summed)
  from end A's node into its first duct at the x it stands at, along each duct's centreline, to end B's node. It is the path's
  length and nothing more: no allowance for a service loop or the stripped end (none on file). It is coarse where an element
  has one node for several pins (the overload's `motor` and `aux`, the receptacle's own node). The other 16 have their reason
  in out/wire-lengths.csv: an end on k-safe or a door operator, whose pins have no node in their behaviour.csv yet (elec's
  records; request panel-4 item 1 and its answer: a minor version of each of the eight, asked of elec on 2026-11-11; four
  have come), or through the hinge loom.
- **Not placed.** The card places one wire element (lib/elements/wire) per row through its ducts. The element's `size`
  parameter is the conductor's cross-section, which is the gauge: NOT ON FILE (B) on every wire. So v0.4 places none; a wire
  drawn at a size picked to draw it would be a guessed figure in the model.
- **Duct fill** (section 3) therefore stays open too: it needs gauges.

**What the solver sees** (`python lib/build.py nets pnl-motor-starter ...`, toolkit/nets.py; ideal wires, phase 1):

| inputs set | result |
|---|---|
| none | stable in 1 pass; only q1's line terminals live (277.1 V to ground each); everything else dead |
| v0.9: q1.on q2.on q3.on q4.on field run (180 elements with a spec, 94 rows, 7 passes, stable) | t1 energised: its primary 480.0 V, 0.521 A across q4's load side (L1 and L2); its secondary 120.0 V on q2 and g1.L, 2V at 0 V with PE; g1 on, +24.0 V on the bus, k-safe on, k1 operated (24.0 V, 0.242 A), plc-1 0.15 A, the door lamp 0.02 A; no load over its limit. The same with `t1` in place of q4.on (the twin's key 4, the stand-in rows below): the same figures. With q1 off (q2 q3 t1 field run set): every load 0 V, k1 released: the control circuit now drops with the supply (lib/reviews/panel/r11.md note 1; to v0.8 the stand-in kept g1 at 120 V with q1 off) |
| v0.9: the same with the door e-stop pressed | k1's coil 0 V, k1 released (4 passes, stable) |
| v0.12: q1.on q2.on q3.on q4.on field run, the combs placed (192 elements with a spec, 100 rows, 7 passes, stable) | the same figures as v0.9: +24.0 V on every block of X1:1 to 4 and X1:15 and 16, 0 V on X1:5 to 8, k1 operated (24.0 V, 0.242 A), t1's primary 0.521 A. The solver lists each blade as its own net joined to the next by the bar's 2.07e-5 ohm (term-jumper's contact rows), so a group reads as four nets at one voltage. jmp-3 (2 poles) shows pins 3 and 4 too, at +24 V and joined to nothing else: term-jumper's behaviour.csv is written for the 4-pole build (its spec.md Notes; request panel-13 item 2) |
| v0.8 and before: q1.on q2.on q3.on field run (the panel as it could be built) | the 480 V reaches q3 and k1's line side; g1 off (0 V on its input: no transformer); k-safe dead, k1 released; p-m1 dead |
| v0.8 and before: the same with `t1` (the stand-in for the transformer's 120 V secondary) | g1 on (120.0 V, 0.5 A); +24.0 V on the bus; k-safe powered, input made, outputs on; plc-1 run; the door lamp lit; k1 operated (24.0 V, 0.242 A on the coil); p-m1 L1 L2 L3 at 277.1 V, 0°, -120°, 120°; no load over its limit. v0.5: estop_ok (p-x4 pin 4) and k1_aux (p-x5 pin 2) at 24 V, ol_trip (p-x5 pin 4) floating with f1 not tripped: the three signals read as the spec means them. v0.6: the same figures with q1 placed (169 elements, 79 wires, 6 passes, stable; `q1.on` is now the switch's own contact rows, "q1: handle=on") |
| the same with the door e-stop pressed | k-safe powered, input open, outputs off; k1 released; p-m1 dead (3 passes, stable) |

So the 480 V never reaches the PSU: the fault the solver found on pm-motor-starter (lib/panel-shop.md "First job") is not in
this wiring: the PSU sees the transformer's 120 V. sources.csv's three phases are 277.128 V since v0.9 (480 / √3; 277.13 gave
480.0003 V line to line, which the solver's limit check flagged over t1's rated 480 V primary).

**The stand-ins** (each a `when` row, each named in the file with what it stands for; none is a wire):
- `q1.on`: gone in v0.6. v0.1 to v0.5 stood in for the disconnect's three poles while q1 was held out of the build; the
  input kept the name the placed switch's own state has, so nothing changed for the solver or the twin when the rows went.
- `t1`: to v0.8 the transformer's secondary, 120 V on q2's line side (sources.csv) and its grounded end joined to g1.N and
  PE:6 (wires.csv); gone in v0.9 with t1 placed. In v0.9 the input closed q4's two poles (two rows, q4.1 to q4.2 and q4.3 to
  q4.4) while the twin's scene (the core's) named its key 4 `t1`; gone in v0.10: the scene's key 4 is q4 (input q4.on) since
  the core's answer to request panel-12, so q4's own contact rows carry the circuit.
- `field`: the station's e-stop, jumpered at p-x3 as for a bench test, and (v0.5) io-1's U_S from the panel's own p-x2 pin 1
  to the new ports' pin 1 (what the block does inside while the cordsets are plugged), and (v0.8) its U_S 0 V from p-x2 pin 3
  to p-x4 pin 3 and p-x5 pin 3, the same block-internal path for the return: the twin's scene (lib/toolkit/twin/scenes/
  pnl-motor-starter.json, the core's, from request panel-8) meters p-x4.4 against p-x4.3 and p-x5.4 against p-x5.3, and with
  no row to pin 3 both meters read "floating" in every step (lib/reviews/panel/r8.md finding 1); `run`: the controller's run output,
  io-1 port-x7 pin 4 at the block's UL (p-x2 pin 4) while `run` is set (the spec's io_power row: the block's UL feeds the
  coils). v0.3's `run` row across X1:13 and 14 is gone with the answer.
- The bridges (term-jumper 2.0 since v0.12: each blade to its block) and the rail under the PE blocks are written as joints with no number.

## 9. The cordsets (v0.7; bom.csv w-eth and w-pwr, assembly.py `PATHS` and `HOLD`; request panel-4's answer item 2)

The core's answer decided the controller's two leads: plc0's ports are M12 sockets, not screw terminals, so each lead is an
open-ended cordset (cordset-m12 1.8, `genders=male-open`: a plug at end A, bare leads at end B, each lead a contact node
`lead-<pole>` carrying the pin mark B1 to B5), its plug in the controller's socket and its leads landed inside the panel. No
field-wireable plug, no new inventory row. Both are BOM rows at their version; the route of a placed one is a list of points
and bom.csv's params column carries scalars only (library.parse_params), so the points live in assembly.py `PATHS` in the
panel's frame, and build() turns them into the cordset's own frame (the inverse of the row's rotation) before placing the row.

**Placement.** A cordset's origin is its end A mating face, plugging along its +y into a port whose face looks toward -y.
plc0's sockets are on its bottom face and look down (axis 0 0 -1), so the row's pitch is 90 (prims.rotation_yp: pitch turns
+y onto +z) and its yaw 0: the plug points up into the socket and the cable leaves downward. The socket's mouth (the port
pivot) is at plc-1's x + 31.5 (port-eth) or + 58.5 (port-pwr), y 268.1 - 30 = 238.1, z 1850 - 65.1 = 1784.9.

**Offered up, not inserted (a modelling limit, for the reviewer).** plc0 1.2 models each socket as a solid zinc cylinder
(Ø13.5, 12.6 long) with the coding insert 0.2 proud of its mouth and no bore. A mated plug puts its sleeve 8.9 into the
socket (toolkit/m12.py MALE cordset reach) and its pins 6: the build's overlap check found 351 mm³ between plc-1.body and
w-eth.port-a.nut and eight smaller pairs (GEO-020 FAIL, lib/rounds/panel/r12.md). So the row's z is the mouth less 9.2
(1775.7): the sleeve's front and the pins stop 0.1 short of the socket and the proud insert; the electrical join is wires.csv's
plug-in rows. The real plug is screwed home; mating it in the model needs either a bore in plc0's sockets (elec's element:
its own spec already keeps a 2.0 open for port-pwr's gender) or a declared contact for a plug in a socket (lib/contacts.csv,
the core's; the "seated" kind that file lists for knobs in uncut bores). Request panel-11 item 2.

**w-eth's route** (the points of `PATHS`, after the plug's own straight exit: the cable leaves the overmould 38.6 below the
mating face, OVERALL 47.5 less the reach 8.9, and runs straight 12 more; so from z 1725.1):
1. (278, 238.1, 1712): straight down through the slot of duct-1680's top wall. The duct's fingers are 12 wide at a 20 pitch
   from its x 162 with 8.0 slots between (duct-40x60 element.py SLOT, PITCH), so the slots stand at x 174 + 20 k to 182 + 20 k:
   the one at 274 to 282 is why plc-1 moved from x 240 to 246.5 (port-eth at 278). The D cable is 6.6 across (CABLE_D), 0.7
   clear of each finger when it drops vertically; the wall is z 1718.5 to 1720 and the fingers' zone y 217.9 to 242.9 (the
   wall's solid web is nearer the panel), which y 238.1 ± 3.3 is inside. The 12 straight above (z 1737.1 to 1725.1) and this
   leg give the drop; no bend is needed before the wall.
2. (284, 238.1, 1706): a 45° turn onto the row's run, at z 1706 so the cable meets riser-r's slot (point 4) level.
3. (1384, 238.1, 1706): along duct-1680's cavity (z 1681.5 to 1718.5, y 215.5 to 274.1; the cover's skirts at y 217.9 to 224.3
   are clear of the cable) out of its open right end at x 1362, through riser-r's left wall (x 1364 to 1365.5) at its slot z 1702
   to 1710 (the riser's fingers run at the same pitch from its z 790), to the riser's centre x 1384.
4. (1384, 238.1, 1618): down riser-r's cavity (x 1365.5 to 1402.5).
5. (1394, 238.1, 1606): a 45° turn toward the riser's right wall at the slot z 1602 to 1610.
6. (1416, 238.1, 1606): level out through that wall (x 1402.5 to 1404), 12 clear of it.
7. (1416, 200, 1590) and 8. (1416, 170, 1578): toward the front and down, to where p-x1's pigtail ends: port-m12-a 1.4 draws its
   pigtail as a sweep from its rear body to 142.6 behind the wall and 30 below the port, which for p-x1 (x 1524, z 1600, yaw 90) is
   (1381, 150, 1570). The jacket ends at point 8; the four leads run 50 on along the last leg (lead-1 to lead-4, 6 out from the
   axis), their tips about (1416, 124, 1559), 35 from the pigtail's end: the splice.
The run is about 1340 mm; the open form draws the jacket to the path's end (`length` is not read with a path), so the row's
length=2000 names the catalogue cordset the shop orders (cordset-m12 spec.md: 0.6 / 1 / 2 / 3 / 5 m), the surplus coiled in
the row. Every figure here is the elements' own (plc0, duct-40x60, cordset-m12, port-m12-a element.py) or a design choice of
the shop, said so; none is a rating.

**The splice (a modelling limit, for the reviewer).** The answer describes the port's rear as leads each carrying the port's pin
mark; port-m12-a 1.4 draws one 150 pigtail sweep with no node, and its pins 1 to 5 stand on the receptacle's contacts at the
front. So the joint rows w-eth.B<n> to p-x1.<n> are right for the solver and the twin, and the splice itself has no place in
the model (no element for it: a crimp or solder joint behind the panel). Request panel-11 item 3 says so; nothing is asked
beyond the record.

**w-pwr** (v0.10; held v0.7 to v0.9 because every passage of its route is a slot 8.0 wide and the L cable is 9.8). The row is
as v0.7 wrote it: plc-1's port-pwr (x 246.5 + 58.5 = 305), pitch 90, offered up 9.2 below the mouth (z 1775.7; the L sleeve's
reach is 8.8, toolkit/m12.py, so it stops 0.4 short). duct-40x60 1.3's `breakout` (the answer to request panel-11 item 1)
leaves out the one finger that holds a named position of a wall, joining the slots either side into a gap PITCH + SLOT = 28
wide; the shop names four (bom.csv params), each where the cable passes a wall:
- duct-1680 `b143`: its top wall (b, z 1718.5 to 1720), the finger at run 140 to 152 (x 302 to 314): gap x 294 to 322 for the
  drop at x 305 (305 ± 4.9).
- riser-l `a906`: its right wall (a, x 158.5 to 160: local z 0 is the riser's x 160 with roll -90), the finger at run 900 to 912
  (z 1690 to 1702): gap z 1682 to 1710 for the run at z 1692 (1687.1 to 1696.9) out of duct-1680's open left end.
- riser-l `a306`: the same wall, run 300 to 312 (z 1090 to 1102): gap z 1082 to 1110 for the run at z 1100 into duct-1085.
- duct-1085 `a66`: its bottom wall (a, z 1085 to 1086.5), run 60 to 72 (x 222 to 234): gap x 214 to 242 for the drop at x 228.
**w-pwr's route** (`PATHS`, the panel's frame), at y 229.5 throughout: the fingers' zone is y 217.9 to 242.9 (the walls' solid
web nearer the panel), the cover's skirts inside each wall end at y 224.3 (so 224.6 to 234.4 clears them by 0.3), and w-eth's
run along duct-1680 is at y 238.1 with its 6.6 cable: 4.9 + 3.3 = 8.2 apart is touching, 8.6 here. The cable leaves the plug
straight down; then:
1. (305, 229.5, 1714): through the top wall's gap, stepping 8.6 toward the front.
2. (305, 229.5, 1698): on down past w-eth's run (z 1702.7 to 1709.3 at y 238.1), beside it.
3. (299, 229.5, 1692) and 4. (140, 229.5, 1692): a 45° turn onto the row's run at z 1692 (the cavity is z 1681.5 to 1718.5,
   the bottom skirt z 1681.7 to 1682.9 at y up to 224.3), under the foot of w-eth's drop at x 278 (z 1702.7), out of the row's
   open end at x 162 and through riser-l's right-wall gap to the riser's centre x 140.
5. (140, 229.5, 1106): down riser-l's cavity (x 121.5 to 158.5).
6. (146, 229.5, 1100) and 7. (222, 229.5, 1100): a 45° turn out through the right wall's second gap, right along duct-1085
   (cavity z 1086.5 to 1123.5).
8. (228, 229.5, 1094) and 9. (228, 229.5, 1060): a 45° turn down through the bottom wall's gap; the jacket ends 25 under the
   duct over X1:7 (x 228 to 234). The five leads (L coding) run 50 on along the last leg, 6 out from its axis, so their tips
   stand at about z 1010, 36 over the blocks' top (rail z 950 + 47 / 2 = 973.5).
The model draws the leads straight (cordset-m12: a lead is straight, 50 long), so leads 1 and 3 end over X1:3 and X1:7 and not
in their clamps: the landing is wires.csv's rows w-pwr.B1 to x1-3.1 and w-pwr.B3 to x1-7.1 (a modelling limit, for the
reviewer, as w-eth's splice); leads 2, 4 and 5 are not used (plc0's port-pwr pins 1 and 3 are the only supply marks on file,
24V-1 and 24V-3). The run is about 1020 mm from the mating face (61 down, 165 along duct-1680, 592 down riser-l, 82 along
duct-1085, 40 down) plus the plug; the row's length=1000 (v0.7's) is the catalogue length below it, so the row's figure is
the 2 m cordset now (cordset-m12 spec.md: 0.6 / 1 / 2 / 3 / 5 m), the surplus coiled in the duct; the open form draws the
jacket to the path's end. `python lib/build.py assembly pnl-motor-starter`: GEO-020 no interference among 2065 solids (2032 in
v0.9: the cordset's), MOT-010 101 nodes; `build.py nets`: plc-1 runs at 24.0 V, 0.15 A, its supply through the cordset's
cores 1 and 3. Every figure here is the elements' own (plc0, duct-40x60, cordset-m12, term-4mm) or the shop's choice.

## 10. Placed elements not yet at station 6 (v0.13, checked again in v0.14; lib/reviews/panel/r18.md finding 1, r20 finding 4, r21 finding 1)

OPERATING.md 12 (quality at the source) and lib/panel-shop.md "The line": a panel moves through the stations as an element does,
and a host places common parts that have passed station 6. `python lib/build.py station <id>` on 2026-11-13 (main 0c07f83b; the
pins that moved, again at main 29ddebeb, panel-r28) for
every element this BOM places (and enc-1's own door operators): these are below station 6 at the pinned version, so **the
panel's own station 6 waits on them**. None is the shop's to fix (each is its lane's element); they are placed because the
panel's points need them and no element at station 6 serves those points.

| tag(s) | element · pin | station reached | what holds it |
|---|---|---|---|
| enc-1 | enc-fs-1524x1829x305 1.9 | 1 open | DOC-004: no Stage 0 brief (references/measure.md) on file. Pinned 1.9 since v0.11 for its earth-stud pins PE1 to PE3; 1.8 was at station 0 too (review r18 finding 1), so the pin goes to no lower station |
| enc-1's door: estop-door, btn-reset, lamp-power | op-estop-22-2nc 1.1, op-pb-22-1no 1.1, op-pilot-22 1.0 (enc-fs's own BOM) | 1 open | DOC-004: no Stage 0 brief |
| rail-1 to rail-4 | din-rail-35 1.1 | 1 open | DOC-004: no Stage 0 brief; GEO-070 (its end clamps touch nothing of the body) |
| np-1, tag-k1 | tag-plate 1.0 | 1 open | DOC-008 (a spec figure against the brief's NOT ON FILE) |
| k1 | contactor-9a-1no1nc 1.2 | 2 open | GEO-070, PIN-002 (16 ports without a gender); MOT-020 at station 3. v0.14: 1.3 on main (elec-r51) fixes the three and passes stations 1 to 5, but station 6 is open (its AutoCAD gate is not at 1.3; AutoCAD on the PC answers no gate since 03:42), so the pin stays 1.2 and goes to 1.3 when that gate passes; the build already draws 1.3 (`build.py assembly` warns "BOM pins 1.2, building with 1.3") |
| f1 | overload-9a-1no1nc 1.1 | 2 open | GEO-070 |
| p-x1 to p-x6 | port-m12-a 1.4 | 2 open | GEO-070 (the pigtail's solids 1.9 off the body) |
| p-m1 | port-pwr-480 1.1 | 2 open | PIN-002 (its port without a gender) |
| k-safe | relay-safety-2ch-2no1nc 1.2 | 5 open | BEH-020: no port node for the probe (wires 48 and 49 have no length for it) |
| w-pwr | cordset-m12 1.8, variant `coding=L;genders=male-open` | 6 open | that variant's AutoCAD gate failed (2026-11-11, core round 29). w-eth (D-coded) is not named by the hold |

At station 6 or past it (checked the same day): contactor-18a-1no 1.0 is not placed here; plc0 1.2, psu-24v-2a4 1.4, mcb-1p-c6
1.5, mcb-2p 1.1, mcb-3p-c10 1.5, disc-3p-30a 1.7, xfmr-control 1.1, term-4mm 1.6, term-jumper 2.0, gland-m20 1.3 (station 7
open); duct-40x60 1.3, marker-terminal 1.0, term-endplate 1.0 (released). A pin moved to a version below station 6 is said so in
the round's report (review r21 finding 1).

## History
| version | change |
|---|---|
| 0.14 | pins (panel-r28, unattended, 2026-11-13): disc-3p-30a 1.7, term-4mm 1.6 (elec-r48's text minors, at station 6); k1 stays at 1.2 (1.3 not at station 6: section 10). term-jumper's count pins on main drop jmp-3's loose pins 3 and 4 (review r23 note 2); wires.csv unchanged. 63 wires, 45 lengths; 72 BOM rows, 72 placed. A minor: pins only, nothing moves |
| 0.13 | the combs pushed home (panel-r26, unattended, 2026-11-13; request panel-13's answer item 1): jmp-1 to jmp-3 at y 223.6 (212.0 in 0.12), the seating face on the blocks' front face, declared `seated` by lib/contacts.csv (GEO-030: 10 pairs). Pins psu-24v-2a4 1.4, disc-3p-30a 1.6 (elec-r39 to r41's minors, at station 6). Text (reviews r18 finding 1, r20 findings 1 and 4, r21 finding 1): section 10, the placed elements below station 6; section 8, the conductors' insulation NOT ON FILE (B). 63 wires, 45 lengths; 72 BOM rows, 72 placed. A minor: the combs move 11.6 toward the blocks, nothing else moves |
| 0.12 | the bridges of X1 placed (panel-r23, unattended, 2026-11-12; request panel-3 item 1, kept since 0.2): term-jumper 2.0 (elec-r36's major, at station 6) as three combs, jmp-1 (4 poles, X1:1 to 4, x 195), jmp-2 (4 poles, X1:5 to 8, x 219), jmp-3 (2 poles, X1:15 and 16, x 279), all at y 212.0, z 959.2: drawn offered up, the blades' tips 0.1 in front of the blocks (term-4mm has no channel on file; section 3; request panel-13). wires.csv: the seven block-to-block bridge stand-ins became ten joins from each blade to its block. terminals.csv: the header names the combs. Pins: term-4mm 1.5 (30 rows), mcb-1p-c6 1.5, mcb-3p-c10 1.5, disc-3p-30a 1.5 (elec-r37 and r38's text minors, each at station 6, the build used them already). 63 wires, 45 lengths; 72 BOM rows, 72 placed. A minor: the origin, every rail, device, port and cut-out kept; three parts added |
| 0.11 | the cabinet's earth studs bonded (panel-r21, unattended, 2026-11-12; r14's and r20's next items): enc-fs-1524x1829x305 pinned 1.9 (mech-r96's minor: its three M8 earth studs are port nodes, pins PE1 to PE3, from request panel-3 item 3), wires 61 to 63 written from PE:1 to 3 side 1 to PE1 (pe-body), PE3 (pe-door-r) and PE2 (pe-door-l); 61 is 1205 long, 62 and 63 cross a hinge (no length; assembly.py `lengths()` knows `door-l` now). terminals.csv: PE:1 to 3 side 1 name the pins, their wire numbers unbracketed. xfmr-control pinned 1.1 (text-only minor, the build used it already). 63 wires, 45 lengths; 69 BOM rows, 69 placed. A minor: the origin, every rail, device, port and cut-out kept |
| 0.10 | the controller's supply lead placed (panel-r18, unattended, 2026-11-12): w-pwr, cordset-m12 1.8 L-coded open-ended, held since 0.7, now routed from plc-1's port-pwr through duct-1680, riser-l and duct-1085 to X1:3 and X1:7 by four breakouts of duct-40x60 1.3 (duct-1680 b143, riser-l a906 and a306, duct-1085 a66; section 9; request panel-11 item 1's answer); its row's length 2000 (1000). wires.csv: 22 and 29 retired for two plug-in and two landed rows (60 wires, 44 lengths); the two `t1` stand-ins on q4's poles dropped (the core's scene names key 4 q4: request panel-12's answer). terminals.csv: X1:3 and X1:7 side 1 name the cordset's leads. Pins: duct-40x60 1.3, mcb-2p 1.1. Text: section 1's tables name the pinned versions (lib/reviews/panel/r15.md finding 1). 69 BOM rows, 69 placed. A minor: the origin, every rail, device, port and cut-out kept; four duct fingers left out |
| 0.9 | the control transformer and its primary breaker placed (panel-r15, unattended, 2026-11-12; lib/reviews/panel/r11.md note 1): t1 xfmr-control 1.0 on the back panel at x 1100, z 1495 (moved from the rail's reserved x 340: a surface-mount device 130 high), q4 mcb-2p 1.0 on rail-2 at x 290; rail-2 900 long (1200). wires.csv: 11 to 17 written, 18 added (62 wires, 46 lengths), the `t1` stand-in row dropped and two for q4's handle added (request panel-12); sources.csv: the 120 V stand-in dropped, the phases 277.128 V. terminals.csv: PE:6 t1.2V / t1.PE. Pins at the minors the build used: disc-3p-30a 1.4, mcb-1p-c6 1.4, mcb-3p-c10 1.4, psu-24v-2a4 1.3. 69 BOM rows, 68 placed. A minor: the origin, every port, duct and device position kept but t1's reserved place; one rail shortened |
| 0.8 | text only (panel-r14, unattended, 2026-11-11): two `field` stand-in rows in wires.csv, p-x2.3 to p-x4.3 and p-x2.3 to p-x5.3 (lib/reviews/panel/r8.md finding 1: the twin's meters against the ports' pin 3 read "floating"); 54 wires and 28 lengths unchanged; the geometry is 0.7's. Godot QA at this version with round 30's qa.gd (the draw count noted, not failed) and the twin's smoke run again (section 8); status above |
| 0.7 | the controller's Ethernet lead placed (panel-r12, unattended, 2026-11-11): w-eth, cordset-m12 1.8 D-coded open-ended, from plc-1's port-eth through duct-1680 and riser-r to p-x1's pigtail (section 9; request panel-4's answer item 2); w-pwr, its L-coded twin for X1:3 and X1:7, in the BOM and held (its 9.8 cable passes no 8.0 slot: request panel-11 item 1); plc-1 from x 240 to 246.5 (its Ethernet socket over a slot); wires.csv: the four Ethernet conductors retired for eight joint rows (54 wires, 28 lengths; 22 and 29 recomputed). The plug drawn offered up, 9.2 below the socket's mouth (plc0's socket has no bore: request panel-11 item 2). 69 BOM rows, 66 placed. A minor: the origin, every rail, duct, port and cut-out kept; one device moved 6.5 along its rail |
| 0.6 | the main disconnect placed (panel-r11, unattended, 2026-11-11): request panel-2's answer gave lib/motion.csv's three rows the scope p*-motor-starter, assembly.py's `HOLD` emptied, q1 on door-r as the BOM had it since 0.1; the three stand-in rows for its poles dropped from wires.csv (58 wires, 32 lengths unchanged: q1's pins have no node). 67 BOM rows, 65 placed. Text with it: the motor branch's design current as NOT ON FILE (B), NEC Table 430.250 (lib/reviews/panel/r1.md finding 1; section 5 and wires.csv's header); the enclosure written as a design choice (request panel-2 item 3; section 3); assembly.py's `roll` line dropped (request panel-5 item 1); the renamed ids relay-safety-2ch-2no1nc and overload-9a-1no1nc (the library's, core round 29). A minor: the origin, every rail, duct, device and port position kept; q1 adds its handle cut-out on door-r (pm-motor-starter's since 1.0) |
| 0.5 | request panel-1's answer taken in (panel-r7, unattended, 2026-11-11): three A-coded wall ports p-x4, p-x5, p-x6 (port-m12-a 1.4, the right wall at z 1450, 1400, 1350) for estop_ok (k-safe 23-24, from 41-42), k1 (the run output sources the coil chain from X1:13), ol_trip (f1 97-98; the point ol_ok renamed by the core) and k1_aux; terminals.csv X1:4 and 13 to 20 rewritten; wires.csv 58 wires (seven new, 64 to 70; 23, 25, 26, 50, 51 moved), 32 lengths; k1's id contactor-9a-1no1nc (the library's rename of contactor-9a, the same element and version). 67 BOM rows, 64 placed. A minor: the origin, every rail, duct and device position kept; the ports added on the bare wall. Gated in panel-r8 (2026-11-11), no file of the panel changed: AutoCAD PASS, Blender FAIL (p-x1.body, p-x2.body: one degenerate triangle each, port-m12-a's D and L codings), Godot QA FAIL (1581 draw calls > 400); request panel-9 |
| 0.4 | two riser ducts and the first wire lengths (panel-r4, unattended, 2026-11-11): riser-l and riser-r, duct-40x60 1.2 on end at the rows' two ends (bom.csv `roll` column, 64 rows, 61 placed); wires.csv routes by the risers' tags and a length on 25 of the 51 wires (assembly.py `lengths()`, out/wire-lengths.csv); no gauge, no wire placed (section 8). A minor: the origin, the ports and every other position kept |
| 0.3 | the wire list, wires.csv and sources.csv (panel-r3, unattended, 2026-11-10/11): 51 wires with their ends, sections, colours and duct rows; no gauge and no length yet (section 8); terminals.csv's wire column, and its two controller pins named by plc0's marks. No BOM row and no position changed: the geometry is 0.2's |
| 0.2 | the terminal plan, terminals.csv (panel-r2, unattended, 2026-11-10): strip X1 from 12 to 24 blocks and PE from 2 to 6, the whole strip moved 8 to the left (rail-4 from x 190 to 368, clear of the rail's panel screw at 374.5), the two marker strips to match; 59 placed, 3 not placed. A minor: the origin, the wall ports and every position off rail-4 kept |
| 0.1 | the BOM, assembly.py and this spec (panel-r1, unattended, 2026-11-10); 43 placed, 3 not placed |
