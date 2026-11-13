# pnl-press-hydraulic · v0.12 · the control panel of the hydraulic press

**What** The control panel of press-hydraulic, built by the panel shop to the machine's controls spec
(lib/assemblies/press-hydraulic/controls.csv, 21 points; the core, 2026-11-09) and shipped as one unit: the machine places it
and pins its version, and never models what is inside (lib/panel-shop.md, "Second job").
**Type** motor-starter (lib/panel-types.csv), wall-mount: one motor branch, 24 V DC control, safety relays, a small
controller; four rails (safety and controller; control; power; terminals), a horizontal duct above each, strip X1 and the PE
blocks on the bottom rail. The type's row covers "a safety relay" and "a small controller or remote I/O"; this spec asks for
three safety functions and for I/O inside the panel, which the type does not rule out. No new type is asked for.
**Baseline** our own design (complexes.org): the arrangement follows pnl-motor-starter's (rails, ducts, strip), scaled to the
wall-mount's mounting plate, with every element at the version on file on 2026-11-11.
**Units / frame** mm, Z up. Origin: the enclosure's (enc-1): the box's underside at its front-left corner, door toward -y,
back face y = 250 against the wall or the frame's rear post.
**Built with** toolkit 1.3 · `assembly.py` from `bom.csv` (library.read_bom, place_on_hosts; P.assembly = True; no geometry of
its own) · AutoLISP command `PNLPH`.

**Status: v0.12 pins io-2 to plc-aio 1.1 (panel-r29, 2026-11-13).** elec-r46's text minor of the analogue module (review
elec-r33 findings 1 and 4: the IEC 61131-2 threshold counted in its spec, its record moved to references/), at station 6;
the build already drew 1.1 (`build.py assembly` warned "BOM pins 1.0, building with 1.1"). No geometry moves, no wire changes:
57 wires, 30 lengths; 88 BOM rows: 86 placed. Gated at v0.12 in panel-r29, the first AutoCAD gate since v0.9 (AutoCAD on the
PC answered no gate from 03:42 to 10:01 on 2026-11-13).
v0.11 joins every blade of the combs by its own pin (panel-r28, 2026-11-13). term-jumper's behaviour.csv on main
gives a pin for every pole the placed build draws (pins 1 and 2 always, pin k `count poles>=k` to 12; elec-r50, the core's note
on request panel-13 item 2), so wires.csv joins jmp-1's blades 5 to 10 and jmp-2's 5 to 8 to their own blocks as blades 1 to 4
are, and the ten block-to-block stand-in rows of v0.9 and v0.10 are gone (section 8). The solver reads the +24 V group on
jmp-1.1 to .10 and the 0 V group on jmp-2.1 to .8, every load as in v0.10 (section 8). Pins (text minors, each at station 6):
contactor-18a-1no 1.1, which states its main poles' operating voltage up to 480 V AC (ratings.csv `ue_max`, ETIM EF008206 /
EF008207: request panel-15's first half, section 1, m1), disc-3p-30a 1.7, hmi-7in 1.1, term-4mm 1.6. No geometry moves. 57
wires, 30 lengths; 88 BOM rows: 86 placed.
v0.10 pushes the combs home (panel-r26, 2026-11-13). Request panel-13's answer item 1 declared a comb's blade in a
term-4mm block's body as a `seated` contact (lib/contacts.csv, every panel), so jmp-1 and jmp-2 stand with their seating face on
the blocks' front face, y 178.5 (166.9 in v0.9); the single-panel check accepts the 18 blade pairs (GEO-030) and finds no
interference (GEO-020, 1492 solids; w-pwr's leads still pass in front of jmp-1's cap). Blades 5 and up keep their stand-in rows
until elec's count pins for term-jumper reach main (the answer's item 2). Pins psu-24v-2a4 1.4, disc-3p-30a 1.6 (elec-r39 to
r41's minors, at station 6). Text, from reviews r18 and r20: k1's AC-3 18 A is said at 400 V, its rating at 480 V NOT ON FILE
(A) with request panel-15 (finding 2); the duct sentence corrected and the insulation NOT ON FILE (B) (finding 1); port-eth's slot
corrected (finding 3); section 10 lists the placed elements below station 6 (r18 finding 1, r20 finding 4). With core's panel-14
fix the solver reads io-1's DI0 to DI7 off and h1, h2 0 V 0 A (13913 A before); every other load as in v0.9. 57 wires, 30
lengths; 88 BOM rows: 86 placed.
v0.9 lays strip X1 out again, places its bridges and the HMI (panel-r24, 2026-11-12). The +24 V group grows from
X1:1-6 to X1:1-10 and the 0 V group from X1:7-13 to X1:11-18 (X1 36 to 41 blocks; the field blocks renumbered 19 to 41;
section 7), so the four contacts' +24 V commons (k1 13, f1 97, k-safe 41, k-lc 41: wires 70 to 73) and the pressure loop's
AI0- return (55) are written: k1_aux, ol_trip and pressure are served. The groups are bridged by two combs of term-jumper 2.0
(jmp-1 10 poles, jmp-2 8 poles), drawn offered up as on pnl-motor-starter 0.12 (term-4mm has no channel on file; its
behaviour has pins 1 to 4 only, so blades 5 and up are stand-in rows: request panel-13). hmi1 (hmi-7in 1.0, elec-r38) stands
on the door at the place kept for it, fed from X1:7 and X1:18 side 2 and PE:7 (74 to 76); its Ethernet socket is not built
(hmi-7in 1.0), so the link to plc-1 stays open. Pins term-4mm, mcb-1p-c6, disc-3p-30a 1.5. 57 wires, 30 lengths; 88 BOM
rows: 86 placed, 2 not (q3, k-2h).
**Gated at v0.9 (panel-r24, unattended, 2026-11-12), each on v0.9's own out/ written by the round's build, each first pass:**
AutoCAD PASS (1491 solids as the LISP predicts, 261 holes, AUDIT 0 errors, extents 600.0 x 283.5 x 827.9; PNLPH 78.8 s);
Blender PASS (export 166678 triangles); Godot QA PASS (164218 triangles, 24 materials, 5 colliders; 1269 draws noted).
**v0.8 status (panel-r20): v0.8 lays the plate out again and places the motor contactor, its overload, both I/O modules and the controller's
supply cordset (panel-r20, 2026-11-12).** elec's three elements of request panel-6 items 1a and 2 are on main, each at station 6:
k1 is contactor-18a-1no 1.0 (AC-3 18 A at 400 V, its rating at 480 V NOT ON FILE (A) since v0.10: section 1, m1; elec-r35), f1 (overload-9a-1no1nc 1.1, held 0.1 to 0.7) mounts
under it at the place that element's spec gives, io-1 is plc-dio 1.0 (8 DI + 8 DO; elec-r33) and io-2 plc-aio 1.0 (4 AI + 2 AO;
elec-r34). The controller plc-1 moves from rail-1 to rail-3: its two M12 sockets open downward 65.1 under the rail and an
L-coded plug reaches 53.9 below the mouth, and under rail-1 the plug reached through duct-515 (panel-r19: 9.9 between the mouth
and the duct). Only the motor row can be that deep under its rail, and it has to be for the overload anyway, so rail-3 goes up
to z 307 and carries the controller beside k1; the rows between move (duct-365, rail-2 465, duct-525, rail-1 635; the tags
duct-325 and duct-515 to v0.7) and the transformer t1 moves into the motor row's right end (section 4). The supply cordset w-pwr
(cordset-m12 1.8, L-coded, open-ended) is placed as on the first panel: down into duct-145 through a broken-out finger of its
top wall, along the row, out through one of its bottom wall, its leads 1 and 3 landed on X1:4 and X1:10 (wires 23 and 27
retired; section 9). wires.csv writes 18 wires: the solenoid paths' heads (36, 39), the lamps' feeds (43, 44), eight signals
into the I/O (46 to 49, 51 to 54), K1's coil return and its chain's end through f1 95-96 (64, 65), the two modules' supplies
(66 to 69); 49 wires, 27 lengths. Open, and written as such: the head of K1's coil chain (k-safe's two N.O. outputs both stand
in the solenoid paths), io-1's output supply, the contacts' +24 V commons and the loop's AI0- return (no bus block left on X1),
safety_ok (which relay). Pins xfmr-control 1.1 (elec-r35's text minor). 81 BOM rows: 78 placed, 3 not (q3, k-2h, hmi1).
Not a minor in the elements' sense: rails, ducts, the controller and the transformer moved; the origin, the enclosure and its
cut-outs are kept.**
**Gated at v0.8 (panel-r20, unattended, 2026-11-12), each on v0.8's own out/ written by the round's build, each first pass:**
AutoCAD PASS (gate/pnl-press-hydraulic-acad.json: 1395 solids as the LISP predicts, 237 holes, AUDIT 0 errors, extents 600.0 x
283.5 x 827.9, the DWG saved; PNLPH 82.3 s); Blender PASS (gate/pnl-press-hydraulic.json: every mesh clean; export 153996
triangles); Godot QA PASS (qa/pnl-press-hydraulic.json: triangles 151812, 23 materials, 5 colliders, fail list empty; 1138
draws noted).
v0.7 bonds the enclosure (panel-r18, 2026-11-12): wires 61 to 63, kept since v0.2, are written from PE:1, PE:2 and
PE:3 side 1 to the enclosure's three M8 earth studs, enc-wm's pins PE1 (pe-body, the bottom's inner face), PE2 (pe-door, it
swings with the door) and PE3 (pe-plate, the mounting plate's front face): mech-r95's enc-wm 1.3, the core's answer to request
panel-7; the BOM pins enc-wm 1.4 (at station 6; 1.1 to v0.6). 61 and 63 have lengths (546, 212); 62 crosses the hinge (the
loom's `door` token: no length, as the lamps' returns). Pins also duct-40x60 1.3 (released; no breakout here) and mcb-2p 1.1
(at station 6). Text: section 5's motor branch current reads as review r5 had it, with one version range in both files
(lib/reviews/panel/r14.md finding 1), and the q1 lines name disc-3p-30a 1.4 (r16.md finding 1). 33 wires, 17 lengths. A
minor: no position changed.
v0.6 placed the control transformer t1 (xfmr-control 1.0) and its primary breaker q4 (mcb-2p 1.0) (panel-r16,
2026-11-12), as pnl-motor-starter 0.9 did: elec's generic elements, each at station 6 before the panel placed it. t1 is a
surface-mount device 130 high, so it stands on the mounting plate at the right of rail-2, which is 140 shorter for it (section
4); q4 on rail-2 at the place reserved since v0.1. wires.csv writes the seven wires kept since v0.3 (11 to 17, PE:5 for the
grounded secondary end) and adds 18 (t1's frame to PE:6); the `t1` stand-ins go (wires.csv's g1.N to PE:5 row, sources.csv's
120 V on q2.1); the phases are 277.128 V (section 8). The pins of q1, q2 and g1 move to the minors the build already used
(disc-3p-30a 1.4, mcb-1p-c6 1.4, psu-24v-2a4 1.3: their terminals' port nodes), so 12 more wires have a length. f1's open
figure reads "NOT ON FILE (A)" (lib/reviews/panel/r11.md note 2: a maker's rating, unclassed counted as A already). With it
the spec's control_power row is served (section 1). 80 BOM rows: 73 placed, 7 not placed (section 2). A minor: the origin,
every duct, device and cut-out kept, except rail-2's length (400 to 260) and t1's own place (from the x 250 on rail-2 the plan
had reserved). Gated at v0.6: lib/rounds/panel/r16.md. v0.5 placed the main disconnect q1 (panel-r14, 2026-11-11): the core's answer to request panel-10 put this panel's
three rows in lib/motion.csv (scope pnl-press-hydraulic, leader enc-1.door: the body excluded, door-unit and handle follow), so
the motion check leaves the body and shaft on the mounting plate and swings the handle unit with the door; with it the spec's
supply row is served. The body seats on the plate at the right end of rail-1, which is 60 shorter for it (section 4): q1 at
x 465 on the door, shaft 198.4 (bom.csv has the sum). wires.csv drops the three stand-ins for q1's poles (its own contact rows
carry q1.on) and writes the motor branch's design current as NOT ON FILE (B), NEC 2023 Table 430.250, as the first panel does
(lib/reviews/panel/r5.md finding 1 and r7.md finding 1; section 5 and 8); section 8's count of the rows that are not wires
corrected (r7.md's note). 80 BOM rows: 71 placed, 9 not placed (section 2). A minor: the origin, every rail position, duct,
device and cut-out kept, except rail-1's length (400 to 340) and q1's own place (from the x 480 the plan had reserved). Gated
at v0.5: below.** v0.4 is text only (panel-r11, 2026-11-11): the reviewer's finding on f1's range (lib/reviews/panel/r5.md finding 2;
section 1's m1 row and section 5), the terminal plan's count (lib/reviews/panel/r6.md's note; section 7), the library's renames
of the two safety relays and the overload (relay-safety-2ch-2no1nc, overload-9a-1no1nc: the same elements and versions), and
the rows for the door disconnect's motion asked as request panel-10 (section 2). The geometry is v0.2's. v0.3 is the BOM with
its two riser ducts, this spec, the terminal plan (terminals.csv, section 7) and the wire list between the devices on file
(wires.csv and sources.csv, section 8: 22 wires, 3 with a length).** 80 BOM rows: 70 placed, 10 not placed (section 2). Of the spec's 21 points, 1 is served, 4 are in form, 16 not yet (section 1): the motor branch, the
transformer, the controller's I/O, the two-hand relay and the HMI are not elements on file at what this spec asks, and the
shop builds no element (requests panel-1 and panel-6). v0.3 also takes the library's rename of the door e-stop
(op-estop-22-2nc, the same element and version) and the core's rename of the spec's ol_ok point to ol_trip (request panel-1
answer 3.d). Pins no machine.
**Gated at v0.6 (panel-r16, unattended, 2026-11-12), each on v0.6's own out/ written by the round's build:** AutoCAD PASS
(gate/pnl-press-hydraulic-acad.json: 1147 solids as the LISP predicts, 212 holes, AUDIT 0 errors, extents 600.0 x 283.5 x
827.9, the DWG saved; PNLPH 54.2 s); Blender PASS (gate/pnl-press-hydraulic.json: every mesh clean; export 124144 triangles);
Godot QA PASS (qa/pnl-press-hydraulic.json: triangles 122164, 20 materials, 5 colliders, fail list empty; 870 draws noted).
**Gated at v0.5 (panel-r14, unattended, 2026-11-11):** Blender PASS (gate/pnl-press-hydraulic.json: 291 meshes, 22 materials,
non-manifold 0, inside-out 0, degenerate 0 on every mesh, 21 with duplicate vertices which fail nothing; export 120032
triangles); Godot QA PASS (qa/pnl-press-hydraulic.json: triangles 118088 of 500000, 20 materials from the library, 5 colliders,
fail list empty; the draw count, 792, is noted and not failed since round 30's qa.gd, request panel-9's answer); AutoCAD not
run this round (the lock answered busy three times, another lane's long gate; panel-r15 runs it first), so v0.5's geometry has
the build's GEO-020 (1101 solids, no interference) and MOT-010 (100 moving nodes, nothing hit), Blender and Godot, not yet
AutoCAD. The twin waits on a scene (the core's).
**AutoCAD at v0.5 (panel-r15, unattended, 2026-11-12):** PASS (gate/pnl-press-hydraulic-acad.json: 1101 solids as the LISP
predicts, 208 holes, AUDIT 0 errors, extents 600.0 x 283.5 x 827.9, the DWG saved; PNLPH 53.0 s), on v0.5's own out/ written
by r15's build. A first run at 05:37 the same day passed on out/ files a merge had put back to main's v0.4 copies (1080 solids,
no q1): not this version's result (lib/rounds/panel/r15.md section 2). So v0.5 has passed all three tools.
**Gated at v0.3 (panel-r9, unattended, 2026-11-11; the card's step 4, on v0.2's geometry, which v0.3 kept):** AutoCAD PASS
(gate/pnl-press-hydraulic-acad.json: 1077 solids as the LISP predicts, 207 holes, AUDIT 0 errors, extents 600 x 283.5 x 827.9,
the DWG saved); Blender PASS (gate/pnl-press-hydraulic.json: 284 meshes, 21 materials, non-manifold 0, inside-out 0, degenerate 0
everywhere; export 117140 triangles); Godot QA FAIL (qa/pnl-press-hydraulic.json: 772 draw calls against the web budget of 400
for an assembly, the only failing line; triangles 115220 of 500000, 20 materials all from the library, colliders back-panel,
body, door, env, 16 lens materials, the binder test exercised 121 nodes: 88 terminal screws, 16 LEDs, the duct covers, the
door, the e-stop, the pilot lights, two gland ports). This panel places no port-m12-a, so the first panel's
Blender finding (its D and L codings) does not reach it; the draw budget is the rule of lib/godot/qa/qa.gd that every per-node
assembly export fails (request panel-9 item 2; the first panel 1581, dm-motor-starter-cell 458). Not re-run until the core
answers. The twin waits on request panel-8.

## 1. The spec served, point by point (controls.csv, in its order)

"Served" means the device is in the built panel with the rating the row asks for on file. "In form" means the devices are
placed and the claim or a fit is someone else's to settle. The wires that make each circuit come with wires.csv.

| point | kind | served | device, or what is missing and why |
|---|---|---|---|
| supply | power-in | **yes** (v0.5) | q1 (disc-3p-30a 1.6 since v0.10, 1.5 in v0.9, 1.4 before: 3 poles, Ith 30 A on file, against the row's 30 A feeder), handle on the door (NFPA 79 5.3, the row's clause), body on the mounting plate by its long shaft; the cable enters at gl-supply. Held out of the build v0.1 to v0.4 (lib/motion.csv had no rows for this panel; request panel-10, answered 2026-11-11). The feeder is the row's Assumption (B) |
| control_power | transform | **yes** (v0.6) | t1 (xfmr-control 1.0: 250 VA, 480 V to 120 V, against the row's 150 VA class, its Assumption (B); the control load on file is g1's 60 VA input) on the mounting plate, fed from q1's load side L1 and L2 through q4 (mcb-2p 1.1: two poles, one handle, one trip; request panel-1 items 1 and 2); its secondary to q2 (mcb-1p-c6 1.5 since v0.9, 6 A C) and g1 (psu-24v-2a4 1.4 since v0.10: 60 W, 2.5 A), the grounded end bonded at PE:5 (NFPA 79 9.1.3 as the row cites it). q4's rated current and q2 as the secondary's protection are NOT ON FILE (B) (section 5): not claimed |
| m1 | load | **no** | The row's sizing figure is 11 A. Since v0.8 k1 is contactor-18a-1no (1.1 since v0.11; AC-3 18 A at 400 V, its ratings.csv ie_ac3, ETIM EF001392; elec-r35, request panel-6 item 1a). **Its rating at this circuit's 480 V is NOT ON FILE (A)** (a rating, the element's): v0.8 and v0.9 wrote "above the motor's 11 A" without the voltage; above 11 A is said at 400 V only. Request panel-15's answer (the core, 2026-11-13) judges a 480 V controller by NEC 430.83(A)(1): its horsepower (kW) rating at the application voltage, not less than the motor's, so no AC-3 current at 480 V is asked for. Of the two rows it named, contactor-18a-1no 1.1 has the first: its main poles' operating voltage up to 480 V AC (ratings.csv `ue_max`, ETIM EF008206 / EF008207, "generic design", elec-r46), so the 480 V supply is within K1's Ue. The second, Rated operation power NEMA (EF011960), is "not stated" in its Class values (item 15), so K1's power against m1's at 480 V stays NOT ON FILE (A) until elec states it (the core's note lib/requests/core/elec-contactor-480v-2026-11-13.md asks for it). With f1 (overload-9a-1no1nc 1.1) mounted under it; q3 is still a planned row with a placeholder id: mcb-3p-c10 (10 A) is below the row's current and no larger 3-pole breaker is on file (request panel-6 item 1, request elec-13), so wires 1 to 6 wait on it. f1's range is open: NOT ON FILE (A): the motor's nameplate FLA (NEC 430.32(A)(1) sets the overload from the nameplate current, 430.6(A)(2), and the spec's row says the generic motor's FLA is not on file). D125 (8.0 to 12.5 A) is the shop's provisional choice in bom.csv until that figure comes; v0.1 to v0.3 wrote it as holding the row's 11 A table figure (lib/reviews/panel/r5.md finding 2). The cable leaves at gl-m1; no power terminals: the motor's leads land on f1 |
| pump_run | DO | **no** | k1's coil A1-A2 (v0.8: A2 to the 0 V bus, wire 64; A1 from f1 96, wire 65) and io-1's DO2 (v0.8). Not written: the chain's head from DO2 through a safety output to f1 95 (section 3: k-safe's two N.O. outputs both stand in the solenoid paths) and io-1's output supply (24VO, 0VO: section 8) |
| k1_aux | DI | **yes** (v0.9) | k1 13-14 into io-1 DI0 (wire 46, v0.8); the common 13 from the +24 V bus at X1:7 (wire 70, v0.9; to v0.8 not written: no bus block left) |
| ol_trip | DI | **yes** (v0.9) | f1 97-98 (N.O., closes on a trip) into io-1 DI1 (wire 47, v0.8), its common 97 from the +24 V bus at X1:8 (wire 71, v0.9); 95-96 stays hardwired in K1's coil chain (wire 65; the core's answer to request panel-1, 3.d: the point was ol_ok on 95-96 until 2026-11-11) |
| sol_a | DO | **no** | io-1 DO0 (v0.8) to the down-stroke path's head k-safe 13 (wire 36), through the safety relays' outputs to X1:19 (X1:14 to v0.8; k-2h planned), to the valve's solenoid a. The coil's power is NOT ON FILE in the row itself (the valve is not built) |
| sol_b | DO | in form (v0.8) | io-1 DO1 to k-safe 23 (wire 39), k-safe 23-24, k-lc 23-24 to X1:20 (X1:15 to v0.8; wire 40), solenoid b. io-1's outputs have no supply yet (section 8), so the solver's `run` stand-in stays |
| press_ok | DI | in form (v0.8) | X1:21 (X1:16 to v0.8) into io-1 DI5 (wire 51); the switch's common on X1:4 side 2 |
| pressure | AI | **yes** (v0.9) | X1:22 (X1:17 to v0.8) into io-2 AI0+ (plc-aio 1.0: 4-20 mA input; wire 52); the loop's 24 V from X1:3 side 2; AI0-'s return to the 0 V bus at X1:18 (wire 55, v0.9; kept to v0.8: no 0 V block left) |
| ram_top | DI | in form (v0.8) | X1:23 (X1:18 to v0.8) into io-1 DI6 (wire 53) |
| ram_bottom | DI | in form (v0.8) | X1:24 (X1:19 to v0.8) into io-1 DI7 (wire 54) |
| two_hand | safety | **no** | k-2h is a planned row: a two-hand control relay (ISO 13851 type IIIC, both buttons within 0.5 s) is not an element and not an inventory row. relay-safety-2ch-2no1nc's record has no two-hand function, as the spec's note says (request panel-6 item 3). PL d / category 3 is the row's Assumption (A): EM's |
| curtain | safety | in form | k-lc (relay-safety-2ch-2no1nc 1.2), the curtain's OSSD1 and OSSD2 on its two input channels. Open: whether that input takes a curtain's solid-state outputs is not in relay-safety-2ch-2no1nc's record (request panel-6 item 4); until it is, k-lc is the shop's proposal, not a claim |
| estop | safety | in form; the claim is EM's | k-safe (relay-safety-2ch-2no1nc 1.2): its two channels out through estop-door (op-estop-22-2nc 1.1, two N.C. blocks; the id op-estop-22 until the library's rename of 2026-11-11) and the two-hand station's e-stop in series, and back (wires 29 to 34, v0.3). Stop category 0, PL d / category 3 is the row's Assumption (A): EM's, with his safety sign-off |
| safety_ok | DI | **no** | a safety relay's N.O. output into io-1 DI4 (the shop's channel, kept: wire 50). With two relays (three with k-2h) which output is "the" safety_ok is section 3's open point |
| safety_fb | DI | in form (v0.8) | k-safe 41-42 into io-1 DI2 (wire 48) and k-lc's into DI3 (wire 49); the commons 41 from the +24 V bus at X1:9 and X1:10 (wires 72, 73, v0.9); whether the row means both is request panel-6 item 3 |
| hmi | comm | in form (v0.9) | hmi1 (hmi-7in 1.0: generic, ETIM EC011541, elec-r38, at station 6) on the door at the place kept for it since v0.1 (x 300, z 420), fed 24 V DC from X1:7 side 2, 0 V from X1:18 side 2 and its FE to PE:7 (wires 74 to 76, across the hinge; 10 W, 0.42 A). Open: the Ethernet link to plc-1: hmi-7in 1.0 has no socket (port-rj45 is not built: its spec.md), so no cordset can be placed; plc-1's port-eth (plc0 1.2, on rail-3 since v0.8) stands over a slot of duct-145's top wall for it (v0.1 to v0.8: a planned row, a folder without an element) |
| h1_run | DO | in form | h1 (op-pilot-22 1.0, white) on the door, fed from io-1 DO3 (v0.8, wire 43) |
| h2_fault | DO | in form | h2 (op-pilot-22 1.0, red) on the door, from io-1 DO4 (wire 44) |
| bonding | safety | yes, as blocks | PE:1 to PE:8 on the bottom rail for the supply's PE, the motor's, the frame's and the HPU skid's, the door's and the plate's; the conductors are the wire list's. Since v0.7 the enclosure is bonded: wires 61 to 63 from PE:1 to 3 to enc-wm's earth studs PE1 (body), PE2 (door), PE3 (plate). The frame's and the skid's bonding cables have no entry into the enclosure yet (request panel-6 item 5) |

Count (v0.9): 6 served (supply, control_power, bonding; since v0.9 k1_aux, ol_trip and pressure: their commons and AI0-'s
return written), 10 in form (curtain, estop, h1_run, h2_fault, sol_b, press_ok, ram_top, ram_bottom, safety_fb; since v0.9
hmi), 5 not yet (m1: q3; pump_run: its coil chain's head; sol_a: k-2h; two_hand; safety_ok). "In form" for the I/O rows: the
device and the signal wire are there, and what is open is the field side or section 3's (v0.8: 3, 12, 6; v0.7: 3, 4, 14;
v0.5: 2, 4, 15; v0.4: 1, 4, 16).

## 2. Rows in the BOM that are not placed (2 since v0.9; 3 in v0.8; 7 in v0.6 and v0.7)

v0.9 places hmi1 (hmi-7in 1.0, elec-r38, at station 6) and adds the two combs jmp-1 and jmp-2 (term-jumper 2.0) and five X1
blocks (x1-37 to x1-41): 88 rows, 86 placed.

v0.8 places k1 (contactor-18a-1no 1.0), f1 (held in assembly.py's `HOLD` 0.1 to 0.7, now empty), io-1 (plc-dio 1.0) and io-2
(plc-aio 1.0), each at station 6 when placed, and adds the cordset row w-pwr (placed): 81 rows, 78 placed.

t1 (xfmr-control 1.0; 1.1 since v0.8) and q4 (mcb-2p 1.1 since v0.7; 1.0 in v0.6) are placed since v0.6 (planned rows v0.1 to v0.5: request panel-1 items 1 and 2).

q1 (disc-3p-30a 1.4) is placed since v0.5: held v0.1 to v0.4 because, placed on the door, it would be swung whole by the
motion check until lib/motion.csv (the core's) carried this panel's three rows (request panel-2's answer scoped the first
rows to p*-motor-starter; request panel-10 asked for this panel's; answered 2026-11-11: scope pnl-press-hydraulic, leader
enc-1.door, q1 excluded, q1.door-unit and q1.handle follow). One row set a panel type is still the core's end state.

| tag | element | why |
|---|---|---|
| q3 | placeholder `mcb-3p` | no 3-pole breaker for an 11 A motor on file (request panel-6 item 1, request elec-13) |
| k-2h | placeholder `relay-twohand` | request panel-6 item 3 |

The places of the planned rows are reserved by eye from sizes not on file; each moves when its element says its size.

## 3. The safety functions (the shop's call, asked for by the spec's two_hand row)

The spec has three safety inputs (two e-stops in one chain, a light curtain, a two-hand station) and two safety outputs
(solenoid a through 13-14, solenoid b through 23-24), and K1's coil drops with the e-stop. relay-safety-2ch-2no1nc is a single-function
relay (the spec's own note). The shop's arrangement, with what is on file:

- **k-safe**: the e-stop chain. Its outputs open everything: both solenoids and K1's coil.
- **k-lc**: the light curtain. Its outputs open both solenoids (the row: "no down command without ... a clear curtain"; the
  spec's sol_b row stops the return stroke too). K1 stays in: a broken curtain stops the ram, not the pump.
- **k-2h** (planned): the two-hand relay. Its output is in solenoid a's path only (the down stroke).
- So solenoid a's path is k-safe 13-14, k-lc 13-14, k-2h's output in series; solenoid b's is k-safe 23-24, k-lc 23-24.

Open, and not the shop's to settle: (1) the category and PL of every row (Assumption (A), EM's; ISO 13849-1 is not on file);
(2) whether contacts of separate relays in series keep the category the spec claims; (3) which relay's output and feedback
the spec's safety_ok and safety_fb rows mean, with more than one relay (request panel-6 item 3 asks the core to say, or to
give each its row); (4) the monitoring of K1 and of the valve (no feedback loop is drawn in the spec).
An alternative on the inventory: safety-controller (a folder without an element) would take all three functions in one
device. The shop places what is on file and asks.

## 4. Arrangement (design choices of the shop, read against the hosts' solids before placing)

- Mounting plate (enc-1.back-panel): x 50 to 550, z 50 to 750, face y 230.5; its studs at x 75 and 525, z 75 and 725.
  Everything on the plate stands in x 100 to 500, clear of the studs.
- **The rows since v0.8 (panel-r20), from the top:** duct-705 (z 705 to 745, kept); rail-1 at z 635 (630 before) with
  k-safe 125 to 147.5, k-lc 155 to 177.5, k-2h's place 185 to 207.5 (planned), io-1 215 to 275 (plc-dio 1.0, 60 wide), io-2
  285 to 330 (plc-aio 1.0, 45 wide), x 330 to 383 spare; duct-525 (525 to 565; duct-515 at 515 before); rail-2 at z 465 (440)
  with q2, g1, q4 as before (x 360 to 500 now spare: t1 left it); duct-365 (365 to 405; duct-325 at 325 before); rail-3 at
  z 307 (250), length 270 (x 100 to 370, 400 before), fix_pitch 150 (screw heads 108 to 117 and 258 to 267), with q3's place
  117 to 195 (planned), k1 200 to 245 (contactor-18a-1no 1.0) and f1 under it, plc-1 267.5 to 357.5 (plc0 1.2), its end clamp
  360 to 368, then t1 on the plate at x 376 to 492; duct-145 (kept) and rail-4 (kept). The risers are kept (z 145 to 715):
  every row still meets them.
  The figures that set it (design choices of the shop, each read from the element's own build): (1) plc0 1.2's sockets open
  downward at z rail - 65.1 (its element.py: body z -52.5 to 52.5, the receptacle 12.6 below), and an L-coded male plug
  (plug-m12 1.6) is 53.8 from its foremost face to the cable exit, its face 0.1 short of the mouth: the plug ends 53.9 under the
  mouth and the cordset's straight 12 more (cordset-m12 1.8). The plug's overmould (r 7.5 about y 193) cannot pass a duct's
  wall even with a finger out (the fingers stand in y 172.8 to 197.8: panel-r19), so the plug must end above a duct: about 120
  under the rail. (2) The overload hangs from k1's bottom face (z rail - 42.5) 72 down (overload-9a-1no1nc's envelope): 114.5
  under the rail. (3) The safety relays are 119.1 high about their rail (relay-safety-2ch-2no1nc: 119.14), the I/O modules 100,
  the breakers and the PSU 105; t1 130. With four duct rows of 40 on a plate whose rows must stay in z 145 to 745 (the risers
  stop under the top studs), the controller and the overload share one deep row: rail-3 at 307 puts the plug's end at 188
  (3.0 over duct-145's top, 185) and f1's bottom at 192.5 (7.5 over). Above: plc-1's top 359.5, 5.5 under duct-365; rail-2's
  devices 412.5 to 517.5, 7.5 from each duct; rail-1's relays 575.4 to 694.6, 10.4 from each.
  (4) plc-1 at x 267.5 puts port-pwr (x + 58.5) at 326, the middle of duct-145's top-wall finger x 320 to 332 (duct-40x60:
  slots 8.0 wide at a 20 pitch from x 112; the finger broken out: section 9), and port-eth (x + 31.5) at 299. **Corrected in
  v0.10 (lib/reviews/panel/r20.md finding 3):** 299 is not over a slot a D cable can use. The cable is 6.6 across (cordset-m12
  CABLE_D), so at 299 it spans 295.7 to 302.3, 2.3 into the finger at 300 to 312; the slot 292 to 300 would take a centre
  between 295.3 and 296.7. v0.8 said "as on the first panel", which is not so (the first panel's 278 is its slot's middle).
  Nothing stands there yet (the Ethernet cordset waits on hmi-7in's socket): when it comes, the finger beside the slot is
  broken out as for w-pwr (duct-40x60 `breakout` b200, local 200 to 212, x 300 to 312: a gap 292 to 320 that holds 299 ± 3.3). (5) The I/O modules' link to the controller (backplane, side bus or fieldbus) is not
  stated in plc-dio 1.0 or plc-aio 1.0 and not modelled, so the modules need not stand beside the controller: they keep
  rail-1, where the controller's place was. Whether a controller and a motor contactor share a rail is the reviewer's to read
  against UL 508A and NFPA 79 (neither read into a table here). **Corrected in v0.10 (lib/reviews/panel/r20.md finding 1):**
  v0.8 said the 24 V and 480 V conductors leave them by different ducts; wires.csv does not bear it out. t1's 480 V primary
  (13, 14) runs in duct-365 with the 24 V wires (46, 47, 64, 65 among them), duct-525 carries 480 V 11 and 12 with 24 V wires,
  and duct-145 and riser-l carry the 120 V 15 and 16 with 24 V ones. Conductors of different voltages may share a duct when
  each is insulated for the highest voltage in it (NFPA 79 13.1.3, as the reviewer reads it; not on file): the conductors'
  insulation is NOT ON FILE (B): NFPA 79 13.1.3 (section 8), and the panel claims no separation by duct.
  The build's overlap check (GEO-020: 1396 solids, no interference) and the door's swing (MOT-010: 113 nodes) pass on it.
- Rails to v0.7 (din-rail-35 1.1, length 400, x 100 to 500) at z 630, 440, 250, 105. fix_pitch 375: two panel screws a rail, heads
  at x 108 to 117 and 483 to 492, so that every device stands between them (pnl-motor-starter r2: a strip's end sat on a
  screw head). Devices use x 120 to 482. **Rail-1 since v0.5: length 340, x 100 to 440, fix_pitch 275 (heads at x 108 to
  117 and 383 to 392, between plc-1's end at 305 and io-2's reserved place at 395), its right end clamp at x 430 to 438.**
- **The disconnect's body (v0.5):** disc-3p-30a's body is 44.6 wide and 69.1 high and sits on the shaft's axis behind the
  door handle; no gap between a rail's edge and the duct above it is 69.1 high (57.5 at rail-1 and rail-2, 47.5 at rail-3)
  and the plate has no bare area right or left of the rails (x 100 to 500; the risers and the studs outside), so the body
  cannot seat on the plate anywhere the v0.1 layout left free. The shop's choice: rail-1 ends at x 440 and the body seats
  on the plate at x 442.7 to 487.3, z 605.5 to 674.5 (q1 at x 465 on the door; its handle plate 430.5 to 499.5), 4.7 clear
  of the rail's end clamp, 14.7 clear of riser-r, below duct-705. The shaft (198.4) puts the body's back face on the plate
  (y 230.5): bom.csv's row shows the sum from the element's own stack (disc-3p-30a element.py: 86.3 handle face to body
  back as supplied, 22 in front of the door face, 30.2 as supplied). The body is drawn seated, not fixed: disc-3p-30a 1.4
  has no mounting feature for the body (its brief), so how it holds to the plate is not modelled. (pm-motor-starter's and
  pnl-motor-starter's q1 stand about 26 in front of their plate with shaft 243.1, the core's figure, kept there.)
- Ducts (duct-40x60 1.3 since v0.7, 1.2 before: the same part with no breakout, length 400, x 100 to 500), bottoms at z 705, 515, 325, 145: one above each rail. From a rail's
  centreline to the duct above it: 75 (rail-1 to rail-3), 40 (rail-4, whose blocks reach 23.5).
- **Risers (v0.2):** the same duct stood on end (bom.csv `roll` -90, as pnl-motor-starter's) at each end of the rows:
  riser-l at x 58 to 98 and riser-r at x 502 to 542, both z 145 to 715, length 570, 2 clear of the rows' ends (100 and
  500). They cover the three lower rows whole and reach 10 into the top row (705 to 745): a riser the rows' full height
  (to 745) would stand on the plate's top studs (M8, Ø8, x 75 and 525, z 725, 12 proud of the plate: enc-wm element.py
  STUD_INSET), which sit 2 outside the rows' ends at the top row's height; the risers stop 6 below the studs. Read first:
  the plate spans x 50 to 550 and nothing else stands left of x 100 or right of 500 (the rails and the rows start at
  100; the rails' end clamps at 102 to 110). A design choice; the top row's wires enter the risers through the rows' open
  ends and the risers' top 10 mm. No riser could stand inside the rows' ends: the rails run x 100 to 500 under every
  such place.
- To v0.7: rail-1: k-safe 125 to 147.5, k-lc 155 to 177.5, plc-1 215 to 305. Rail-2: q2 125 to 143, g1 155 to 187, q4 200
  to 235.4 (v0.6; kept).
- **The transformer since v0.8:** t1 at `enc-1.back-panel` x 384, y 230.5, z 200: body x 376 to 492, z 190 to 320, in the motor
  row right of rail-3's end (370; its end clamp to 368), 10 clear of riser-r, 5 over duct-145 and 45 under duct-365. Its
  primary's entries (the top block) now open toward duct-365, the plug's and the PE clamp's toward duct-145: wires 13 to 18
  keep their routes by the rows' new tags (wires.csv) and their lengths are the new build's. The HMI's planned place on the
  door (x 300, z 420) no longer faces t1.
- **The transformer (v0.6 to v0.7):** xfmr-control 1.0 is a surface-mount device, not a rail device (its element.py ORIGIN: the
  brackets' flanges on the panel, origin the lower-left of four M5 clearance holes; body x -8 to 108, z -10 to 120, 108 deep),
  and 130 high: no gap between a rail and the duct above it is that high (57.5 at rail-2), and the gap between duct-325's top
  (365) and duct-515's bottom (515) is 150. So t1 stands on the plate in rail-2's band at its right: `enc-1.back-panel`
  x 380, y 230.5 (the plate's face), z 385: body x 372 to 488, z 375 to 505, y 122.5 to 230.5; 10 clear of duct-325 below
  and duct-515 above, 14 clear of riser-r (502). **Rail-2 since v0.6: length 260, x 100 to 360, fix_pitch 200 (heads at
  x 108 to 117 and 308 to 317), its right end clamp at x 350 to 358**, 12 clear of t1's body. The primary's entries (the
  top block's top face) open toward duct-515, the plug's and the PE clamp's toward duct-325. The door in front of t1 carries
  nothing placed; the HMI's planned place (door, x 300, z 420) faces t1's left part, and t1's front is 122.5 behind the
  door's front face: whether the HMI's depth clears it is read when hmi-7in is an element (v0.9: it is; hmi-7in 1.0 reaches 66.0
  behind its seating face, the plug included, so to y 64 with the door closed: 58.5 clear of t1's front at 122.5, wherever t1 stands). Design choices of the shop; the build's overlap check (1147 solids) and the door's swing (MOT-010) pass
  on it. The four panel screws are the installer's (xfmr-control's own spec: not built).
- Rail-4: end cover 120 to 122, X1:1 to X1:41 from 122 at 6 pitch (to 368; X1:36 to 338 until v0.8), PE:1 to PE:8 at 5 pitch
  (to 408), end cover to 410; rail-4's right panel screw head at x 483 to 492 is 73 beyond it.
- **X1's 41 blocks** (36 to v0.8) carry the plan of section 7: the 30 field conductors of the spec's 24 V rows, two a contact or
  coil (sol_a 2, sol_b 2, press_ok 2, pressure 2, ram_top 2, ram_bottom 2, the two-hand station's four contacts 8, its
  e-stop's two channels 4, the curtain 6: receiver +24 V, 0 V, OSSD1, OSSD2; sender +24 V, 0 V), the door's two lamp
  returns and the 0 V bond (3), since v0.9 the four contacts' commons, AI0-'s return and the HMI's supply, and 3 spare. The
  curtain's and the station's own pin lists are not on file (neither is an element): the conductors are named by function.
- **The combs (v0.9):** term-jumper 2.0 jmp-1 (10 poles) on the +24 V group X1:1 to 10 at x 125 (cap 122.25 to 181.75) and
  jmp-2 (8 poles) on the 0 V group X1:11 to 18 at x 185 (cap 182.25 to 229.75, 0.5 from jmp-1's: term-jumper spec.md), z 114.2
  (rail + 9.2: the comb's design channel), each blade on its block's centre (block x + 3.0). **Pushed home since v0.10:** the
  seating face on the blocks' front face (y 223.0 - 44.5 = 178.5), each blade in its block's body, declared `seated` in
  lib/contacts.csv (`pnl-*, jmp-*.p-*|M-CU, x1-*.body`; request panel-13's answer item 1: term-4mm has no jumper channel on
  file, and the core refused one of our own; a modelling simplification GEO-030 lists in every report). v0.9 drew them offered
  up (seating face at 166.9), as pnl-motor-starter 0.12. w-pwr's leads crossed jmp-1's
  cap with v0.8's last leg (GEO-020, 25.5 mm3 at x 162 to 170): v0.9 turns the jacket's end 2 forward for 1 down (section 9).
- Door (enc-1.door, front face y -2): h1 at x 240 and h2 at x 360, z 640; estop-door at x 300, z 200; nameplate at x 60 to
  180, z 720 to 780; the middle (around x 300, z 420) kept for the HMI, where hmi1 (hmi-7in 1.0) stands since v0.9: its bezel
  x 200 to 400, z 345 to 495, its clamps behind the door to z 346 and 494, the door's cut-out 187 x 133 (hmi-7in CUTOUT_RECT,
  cut by the mount; the door 2.0 thick against the clamps' 1.0 to 6.0 range); q1's handle at x 465, z 640 (v0.5; the plan had
  reserved x 480, where the body would have stood on rail-1 and 0.3 into riser-r).
- Entries: gl-supply and gl-m1 in the enclosure's two M20 holes (x 200 and 400, y 100, in the bottom).
- **Fill.** The plate is full in height with four rails at these spacings; the reserved places on rail-1 (io-1, io-2) and
  the motor branch on rail-3 are sized by eye. Whether the finished panel fits a 600 x 800 wall-mount is not known until
  those elements exist; "by fill" has no figure on file (request panel-2 item 3). The spec's header asks for an enc-wm
  and the shop built to it.

## 5. Figures

- **24 V load, what is placed:** k-safe and k-lc 0.17 A each (4 W, relay-safety-2ch-2no1nc's record), plc-1 0.15 A (plc0's assumption), h1
  and h2 0.02 A each (op-pilot-22's assumption): 0.53 A of g1's 2.5 A; since v0.8 io-1 and io-2 0.083 A each (2.0 W: plc-dio
  and plc-aio ratings.csv load_i, derived): 0.70 A, and K1's coil 0.20 A (contactor-18a-1no ratings.csv load_i: 4.8 W, a design
  figure) once its chain's head is written: 0.90 A; since v0.9 the HMI 0.42 A (hmi-7in ratings.csv load_i: 10 W, a design
  figure): 1.12 A placed, 1.32 A with K1's coil, of g1's 2.5 A. Not in the sum because not on file: the two solenoids (the
  spec: coil power NOT ON FILE), the I/O's outputs' loads beyond the lamps, the curtain, the transmitter's loop, k-2h.
- **Motor branch design current:** 1.25 x the motor's Table 430.250 current, NOT ON FILE (B): NEC 2023 Table 430.250
  (view-only; lib/reviews/panel/r5.md finding 1 and r7.md finding 1). NEC 430.22 with 430.6(A)(1) takes the table's figure
  for the motor's horsepower and voltage, not the nameplate's; v0.1 to v0.4 wrote 1.25 x 11 A = 13.75 A from the spec's
  row (11 A): this spec from v0.1, wires.csv's header from its first version, v0.3 (both files give this range since v0.7).
  The reviewer reads 11 A as the 7½ hp line; 7.5 kW is 10 hp, 14 A at 460 V (lib/reviews/panel/r5.md finding 1; v0.5 and
  v0.6 had it the other way round, r14's finding 1). Neither figure is on file; no gauge is chosen from either (none is filled), and the attended reading settles it. For the core: the
  controls.csv m1 row's 11 A is the same finding (lib/reviews/panel/r5.md finding 1). The gauge is NOT ON FILE (B): the
  ampacity table is not read (request panel-1 item 4).
- **The control transformer (v0.6):** g1's input 60 VA against t1's 250 VA (the spec's row asks a 150 VA class, its
  Assumption (B)); the solver draws 0.521 A on the primary at 480 V (section 8). q4's rated current and the primary's
  protection: NOT ON FILE (B): NEC 2023 430.72(C) and 450.3(B) (mcb-2p's own record says the same); q2's 6 A as the 120 V
  secondary's protection (t1 2.08 A rated): NOT ON FILE (B), the same tables. The panel claims neither.
- **f1's range:** NOT ON FILE (A): the motor's nameplate full-load current (NEC 430.32(A)(1), 430.6(A)(2)); the spec's row says
  "FLA NOT ON FILE (generic design)". bom.csv's range=D125 is the shop's provisional choice, not a figure met (v0.4; lib/reviews/panel/r5.md
  finding 2). If the table figure is 14 A, the nameplate current likelier lies above D125's 12.5 A.
- **NOT ON FILE (B):** NEC 430.52's largest branch protection for this motor (a table's figure); the short-circuit current
  rating, spacings and wire bending space (UL 508A, to buy): the panel claims no SCCR; the cables' diameters (gland-m20
  takes one cord of 6.1 to 13 mm).
- **Heat load:** not summed; most of the devices that make it are not on file.
- The rated voltages missing from the breakers' and the disconnect's ratings.csv (pnl-motor-starter spec.md section 5)
  hold here too.

## 6. What the next versions add
Each planned row placed when its element is on file (q3, k-2h), and its wires (the kept numbers of section 8) with it;
io-1's output supply (section 8) and the head of K1's coil chain when the safety arrangement is settled (section 3); K1's
480 V power line when contactor-18a-1no states its NEMA power (section 1, m1); the entries for the field cables when the enclosure has them; the gauges when the ampacity table is read; the
Ethernet cordset to the HMI when hmi-7in has its socket (port-rj45) and plc0 its receptacle minor (port-eth over its slot
since v0.8); the twin (a scene of the core's, as request panel-8's). (v0.9 did: hmi1 placed and fed, the four contacts'
commons and AI0-'s return on longer bridged groups, the combs; v0.10 pushed them home; v0.11 joined every blade by its own
pin.)

## 7. The terminal plan (terminals.csv; role card r2; arrangement: NFPA 79 13.1 as the card cites it)

NFPA 79 is view-only and not read into a table (lib/standards/sources.csv), so the plan quotes none of its wording; the rules
below are the shop's design rules, written as such (pnl-motor-starter's, section 7 of its spec), and the reviewer reads them
against the clause.

- **Two strips on rail-4**: X1 (control, 24 V DC; 41 feed-through blocks since v0.9, 36 before) and PE (8 ground blocks). Side 1 of a block (clamp 1,
  the top entry) takes the panel's devices; side 2 (clamp 2, the bottom entry, toward the enclosure's bottom and its cable
  entries) takes what leaves the panel, and the door's two lamp returns (the door is off the plate).
- **One conductor a clamp** (design: the shop's rule; how many conductors a clamp of term-4mm may take is not in its brief:
  request panel-3 item 4). A potential with more than two ends is a bridged group: +24 V on X1:1 to 10 since v0.9 (seventeen
  ends: the PSU, the two safety relays, the controller, the two I/O rows and, since v0.9, the four contacts' commons k1 13,
  f1 97, k-safe 41, k-lc 41 inside; the curtain's two supplies, the transmitter's loop, three switch commons and, since v0.9,
  the HMI's +24 V outside), 0 V on X1:11 to 18 since v0.9 (sixteen ends: the PSU, the relays, the controller, the I/O rows,
  K1's coil and, since v0.9, AI0-'s return inside; the curtain's two returns, the two solenoids' returns, the two lamps, the
  one bond to PE:8 and, since v0.9, the HMI's 0 V outside). To v0.8: X1:1 to 6 and X1:7 to 13. The bridges are term-jumper
  2.0 combs since v0.9 (jmp-1, 10 poles; jmp-2, 8 poles; section 4; request panel-3 item 1); to v0.8 block-to-block rows
  stood in. The 0 V group's first block is the controller's return (X1:11, X1:10 to v0.8), the one nearest w-pwr's jacket end
  (x 166); the other blocks keep their pairs of sides.
- **What lands on X1** (38 of 41 named, 3 spare; v0.9's numbers, v0.8's in brackets): the two buses (1 to 18; 1 to 13); the
  solenoids' feeds, each the end of its safety path (19: down stroke through k-2h, reserved; 20: up stroke from k-lc 24,
  planned; 14 and 15); the four field inputs into the I/O (21 to 24, planned; 16 to 19); the e-stop chain's four conductors
  to the two-hand station's e-stop (25 to 28, planned: the same form as pnl-motor-starter's X1:9 to 12; 20 to 23); the
  two-hand station's eight (29 to 36, reserved on k-2h; 24 to 31); the curtain's two OSSDs into k-lc's input (37, 38,
  reserved on request panel-6 item 4; 32, 33).
- **What lands on PE**: the supply's protective conductor (PE:1, from gl-supply), the frame's and the HPU skid's bonding
  cables (PE:2 and 3; no entry for them yet, request panel-6 item 5), the motor cable's PE (PE:4, with g1's PE on side 1),
  the transformer's grounded secondary end 2V (PE:5, planned since v0.6) and its frame (PE:6 side 1, v0.6), the HMI's functional earth (PE:7 side 1, v0.9: the shop's choice, no FE bar in the BOM), the 0 V bond (X1:17 to PE:8, X1:13 to v0.8; NFPA 79 8.2.1 as pm-motor-starter's wire 20
  cites it). Side 1 of PE:1 to 3 takes the body's, the door's and the mounting plate's earth studs (enc-wm's pins PE1 to
  PE3, wires 61 to 63, since v0.7; enc-wm 1.1 had none: request panel-7). PE:1 is planned (side 2 is the supply cable's
  own PE); PE:2 and PE:3 stay reserved for their side 2, the frame's and the skid's bonding cables (no entry yet).
- **What has no terminal**: the supply's phases (on q1 L1 L2 L3); the motor leads (f1 T1 T2 T3 through gl-m1: X1 is the
  control strip and the BOM has no power strip, a design choice); the Ethernet link hmi1 to plc-1 (a data pair is not
  broken at a screw terminal, a design choice); the panel's own circuits device to device: k-safe S11 and S21 to the door
  e-stop, the series links of the two solenoid paths (section 3), K1's coil and auxiliaries, f1 95-96, both relays' 41-42
  and their outputs to the I/O, the I/O's outputs to the door lamps, the transformer, q2 and g1's input.
- **v0.8:** X1:4 and X1:10 side 1 take the cordset w-pwr's leads 1 and 3 (wires 23 and 27 retired; terminals.csv writes
  "(w-pwr.B1)" and "(w-pwr.B3)": a lead, not a wire); X1:5 and 6, 11 and 12 take the I/O modules' supplies (wires 66 to 69),
  X1:13 K1's coil return (64), X1:16 to 19 the four field signals into io-1 DI5 to DI7 and io-2 AI0+ (51 to 54): those nine
  blocks go from reserved to planned. The plan's buses have no block left for the four contacts' commons (k1 13, f1 97,
  k-safe 41, k-lc 41), io-1's output supply 24VO and 0VO, or io-2's AI0- return: open, for a version that lengthens the bridged
  groups (X1:34 to 36 are spare but not next to them; a group is one run of bridged blocks).
- **v0.9:** the bridged groups lengthened (X1 36 to 41 blocks; the numbers above): X1:7 to 10 side 1 take the four contacts'
  commons k1 13, f1 97, k-safe 41, k-lc 41 (wires 70 to 73), X1:18 side 1 AI0-'s return (wire 55, kept since v0.3); side 2 of
  X1:7 and X1:18 the HMI's +24 V and 0 V across the hinge (74, 75); PE:7 side 1 its FE (76). io-1's output supply 24VO and 0VO
  stays open: whether it is fed through a safety output is section 3's (EM's); the +24 V group has side 2 of X1:8 to 10 free,
  so a feed from the bus needs no further block when it is settled.
- Count (v0.9): 41 X1 blocks: 27 planned, 11 reserved, 3 spare. 8 PE blocks: 6 planned, 2 reserved, 0 spare (PE:7 planned
  with the HMI's FE). v0.8: 36 X1 blocks: 22 planned, 11 reserved, 3 spare (v0.7: 13, 20, 3; v0.2 and v0.3 wrote 11 and 22; terminals.csv and the
  table above gave 13 and 20: lib/reviews/panel/r6.md's note); 8 PE blocks: 5 planned, 2 reserved, 1 spare (v0.7: PE:1 planned with
  wire 61; v0.6: 4, 3, 1; v0.5: 2, 4, 2; PE:5 and PE:6 planned with t1 in v0.6).

Open lines of the plan:
- The PE blocks are joined only through their bonding feet and rail-4; the rail's rating as that protective conductor is
  NOT ON FILE (B): IEC 60947-7-2 (request panel-3 item 2).
- No field device of the machine is an element on file, so no field pin mark is on file: side 2 names each conductor by its
  function. The station's e-stop channels are written 11-12 and 21-22 as op-estop-22-2nc's marks are (the shop's naming).
- Which relay's output the spec's safety_ok means, with two relays and a third planned, is request panel-6 item 3; the plan
  gives it no terminal (device to device).
- X1 is 24 V DC throughout, so the plan separates no voltages on it.

## 8. The wire list (wires.csv, sources.csv; role card r3; v0.3, counts v0.5)

The form, the rules and the colours are pnl-motor-starter's (its spec.md section 8). What this panel has on file is less: the
motor branch, the transformer, the controller's I/O, the two-hand relay and the lamps' feeds all end on planned rows, so
their wires are kept numbers, not wires.

**v0.11:** 57 numbered wires, 30 with a length, as v0.10. The ten stand-in rows for blades 5 and up (section `bridge
(term-jumper 2.0 · no pin)`) become joins of each blade to its own block, jmp-1.5 to .10 on X1:5 to 10 and jmp-2.5 to .8 on
X1:15 to 18 (term-jumper behaviour.csv on main: pin k `count poles>=k`, the bar's contact rows k to k+1 `always`), so all 18
blades are rows of section `bridge (term-jumper 2.0)`. `python lib/build.py nets pnl-press-hydraulic q1.on=1 q2.on=1 q4.on=1
field=1 curtain=1 run=1` (2026-11-13, this round): 202 elements with a spec, 94 rows, 4 sources, 9 passes, stable; +24 V on
jmp-1.1 to .10 (X1:1 to 10), 0 V on jmp-2.1 to .8 (X1:11 to 18); io-1's DI0 to DI7 off; loads hmi1 0.417 A, io-1 and io-2
0.083 A, k-lc and k-safe 0.167 A, plc-1 0.15 A, g1 0.5 A at 120 V, t1's primary 0.521 A at 480 V, h1, h2 and k1's coil 0 A
(io-1's outputs off, K1's coil chain not written: section 3): as v0.10.

**v0.9:** 57 numbered wires, 30 with a length. Written: 55 (AI0-'s return to X1:18, kept since v0.3: 982). Added: 70 to 73
(the four contacts' commons from the +24 V group: k1 13 to X1:7, 614; f1 97 to X1:8, 681; k-safe 41 to X1:9 and k-lc 41 to
X1:10, no length: the relays' pins have no node, request panel-4 item 1), 74 to 76 (the HMI's +24 V from X1:7 side 2, 0 V to
X1:18 side 2, FE to PE:7 side 1, across the hinge: no length). Every row on X1:7 and up names its new block (terminals.csv);
the moved blocks change the lengths of 17 228, 18 227, 24 833, 28 331, 41 949, 51 965, 52 1001, 53 982, 54 993, 61 576,
63 242, 64 711, 67 894, 69 909. The bridges: the eleven block-to-block rows of v0.8 became the combs' joins, blade k of
jmp-1 / jmp-2 in the k-th block of its group for k 1 to 4 (term-jumper behaviour.csv) and, for blades 5 and up, ten stand-in
rows block to block (section `bridge (term-jumper 2.0 · no pin)`: the comb's behaviour.csv has pins 1 to 4 only, request
panel-13 item 2). Not written and not numbered: the head of K1's coil chain and io-1's output supply (section 3). Kept: 1 to
9, 37, 50.

**v0.8:** 49 numbered wires, 27 with a length. Written: 36 and 39 (io-1 DO0 and DO1 to the heads of the two solenoid paths,
k-safe 13 and 23), 43 and 44 (io-1 DO3 and DO4 to the door lamps, across the hinge), 46 to 49 (k1 13-14, f1 97-98, k-safe's and
k-lc's 41-42 into io-1 DI0 to DI3), 51 to 54 (X1:16, 18, 19 into io-1 DI5 to DI7; X1:17 into io-2 AI0+); added: 64 (K1's coil
A2 to X1:13), 65 (f1 96 to K1's A1: the chain's end), 66 to 69 (X1:5 and 11 to io-1's 24V and 0V; X1:6 and 12 to io-2's).
Retired: 23 and 27 (plc-1's supply), now the cordset w-pwr's two plug-in rows and two landed rows, as pnl-motor-starter 0.10's
22 and 29. Three plug-in rows join f1's pins to k1's clamps 2, 4, 6 (no wire). The channels are the shop's: DI0 k1_aux, DI1
ol_trip, DI2 and DI3 safety_fb, DI4 safety_ok (kept), DI5 press_ok, DI6 ram_top, DI7 ram_bottom; DO0 sol_a, DO1 sol_b, DO2
pump_run (not written: its chain's head), DO3 h1_run, DO4 h2_fault, DO5 to DO7 spare; io-2 AI0 pressure. Kept: 1 to 9 (q3
planned; 7 to 9 are f1's T1 to T3 out through gl-m1), 37 (k-2h), 50 (safety_ok), 55 (AI0-'s return). Not written and not
numbered: the head of K1's coil chain, the four contacts' commons, io-1's output supply (sections 3 and 7). The `run`
stand-in stays: io-1's DO1 sources only from its output supply (plc-dio behaviour.csv), which is not wired.
Lengths: t1's six wires (13 to 18) have new routes with t1 in the motor row (13 and 14 by duct-365 alone, 442 and 441; 15 952;
16 997; 17 258; 18 257), and every row moved, so the lengths of 10 to 12, 20, 24 and 41 changed too (wires.csv has them all);
the 12 new ones: 46 819, 47 823, 51 935, 52 971, 53 952, 54 963, 64 687, 65 293, 66 829, 67 870, 68 844, 69 885. 36, 39, 43,
44, 48 and 49 end on a relay or a lamp, whose pins have no node (request panel-4 item 1).

**What the solver sees, v0.9** (`python lib/build.py nets pnl-press-hydraulic q1.on=1 q2.on=1 q4.on=1 field=1 curtain=1
run=1`): 202 elements with a spec, 94 wires, 4 sources, 7 passes, stable. t1 energised, g1 on (120.0 V, 0.5 A); k-safe and k-lc
powered, inputs made, outputs on (0.167 A each); plc-1 run; io-1 and io-2 powered (0.083 A each); hmi1 powered (24.0 V,
0.417 A); K1's coil dead (its chain's head is not written). Two readings are the solver's, not the panel's (request panel-14):
the combs' bar resistance (term-jumper behaviour.csv, 2.07e-5 ohm a pitch) puts the 0 V blocks some µV apart, and the solver
counts a floating side as 0 V, so io-1 reads every floating input as signal 1 (DI0 with K1 released, DI4 with no wire) and the
lamps h1 and h2, whose feeds from io-1 DO3 / DO4 are off, report 0.0 V and 13913 A (0.5 W over about 3.6e-5 V).

**What the solver saw, v0.8** (`python lib/build.py nets pnl-press-hydraulic q1.on=1 q2.on=1 q4.on=1 field=1 curtain=1
run=1`): 179 elements with a spec, 79 wires, 4 sources, 6 passes, stable; plc-1 powered through w-pwr (24.0 V, 0.15 A); io-1
and io-2 powered (24.0 V, 0.083 A each); K1's coil dead (its chain's head is not written: 0 V); the rest as v0.6.

**What was there to v0.7.** 33 numbered wires between devices on file (v0.7: 61 to 63, the enclosure's bonding; v0.6: 11 to 18 added, the transformer's), and 23 rows that are
not wires (eleven bridges, seven rail joints between the PE blocks, five stand-ins; v0.3 and v0.4 wrote 29 and eleven for the
file's 27 and nine, lib/reviews/panel/r7.md's note; v0.5 dropped the three stand-ins for q1's poles with q1 placed, v0.6 the
`t1` one with t1 placed). Kept: 1 to 9 (the motor branch), 36, 37,
39 (the solenoid paths' heads at io-1 and the two-hand relay), 43 and 44 (the lamps' feeds from io-1), 46 to 55 (the signals
into io-1 and io-2); 61 to 63 were kept to v0.6 (no bonding point on enc-wm 1.1: request panel-7) and are written in v0.7.

| section | wires | colour (the card's list, NFPA 79 13.2.4 as it cites it) |
|---|---|---|
| control (mains) | 7 (10: q2 to the PSU; v0.6: 11 and 12 q1's load side L1 and L2 to q4; 13 and 14 q4 to t1's primary 1U 1V; 15 t1's 2U to q2; 16 t1's 2V to g1's N) | black for the 480 V primary (11 to 14: a power circuit), red for the ungrounded 120 V (10, 15); 16, the grounded 120 V conductor: NOT ON FILE (B): NFPA 79 13.2.4 (the card's list has a line for the grounded DC conductor only; as pnl-motor-starter's wire 16) |
| control & 24 VDC | 19 (20 to 27 the two buses' panel ends; 29 to 34 the e-stop chain; 35, 38 the two solenoid paths' series links between the relays; 40 solenoid b's feed to X1:15; 42, 45 the door lamps' returns) | blue; the 0 V conductors (24 to 27, 42, 45) white/blue |
| ground | 7 (28 the 0 V bond to PE:8; 41 the PSU's PE; v0.6: 17 t1's 2V bonded to PE:5 at the source, NFPA 79 9.1.3 as the spec's row cites it; 18 t1's frame to PE:6; v0.7: 61 to 63 PE:1 to 3 to the body's, the door's and the plate's earth studs, NFPA 79 8.2 and NEC 250 as the spec's bonding row cites them; 61 546 and 63 212 long, 62 across the hinge with no length) | green/yellow |

- **Gauge: NOT ON FILE (B) on every wire** (request panel-1 item 4: the core's answer leaves the ampacity table to an
  attended reading, EM's). Design currents on file: the 24 V feed 2.5 A at most (g1); the relays 0.17 A each; the lamps
  0.02 A; the motor branch's for the kept wires 1 to 9 is NOT ON FILE (B) (1.25 x the Table 430.250 current, section 5;
  v0.1 to v0.4 wrote 13.75 A from the spec's row: section 5).
- **Insulation (v0.10; lib/reviews/panel/r20.md finding 1): NOT ON FILE (B): NFPA 79 13.1.3.** The ducts carry 480 V (11 to
  14, in duct-525 and duct-365), 120 V (15, 16, in duct-145, riser-l, duct-525 and duct-365) and 24 V wires together. They may
  share a duct when each conductor is insulated for the highest voltage in it, as the reviewer reads NFPA 79 13.1.3; the clause
  is not read into lib/standards/, and the wire element (lib/elements/wire 1.0) states no rated voltage. So no insulation voltage
  and no separation by duct is claimed; the wires' rated voltage is the same attended reading as their gauge.
- **Colour:** complete but wire 16's (above); wire 28 (the 0 V bond) is green/yellow by the shop's choice, as the first panel's wire 31, for the
  reviewer.
- **Route:** duct-705, 525, 365, 145 are the rows above rail-1 to rail-4 (since v0.8; 515 and 325 to v0.7); riser-l joins them for every wire between two rows
  (the devices stand at the left); `door` is the loom across the door's hinge (not an element on file): six wires cross it
  (the e-stop chain's four at estop-door, the two lamp returns).
- **Length: on 17 of the 33** (v0.7: 61 546, 63 212; v0.6: 10 306, 11 399, 12 396, 13 808, 14 775, 15 778, 16 607, 17 1004, 18 1013, 20 765, 24
  808, 41 924; as before 23 1042, 27 1078, 28 325), from assembly.py `lengths()`, pnl-motor-starter's method copied with
  `door` as this enclosure's loom token; written to out/wire-lengths.csv at every build. g1's and q2's lengths come with the
  pins at their minors with port nodes (psu-24v-2a4 1.3, mcb-1p-c6 1.4). The other 15 end on k-safe, k-lc or the door,
  whose pins have no node (relay-safety-2ch-2no1nc 1.2, op-estop-22-2nc 1.1, op-pilot-22 1.0: request panel-4 item 1) or
  cross the loom; v0.7's 62 crosses the loom too (16 without a length). Wires 13 and 14 go by riser-r (t1 stands at the plate's right; q4's load side is its bottom).
- **Not placed:** no wire element, as the first panel (the gauge is the wire's size).

**What the solver sees, v0.6** (`python lib/build.py nets pnl-press-hydraulic q1.on=1 q2.on=1 q4.on=1 field=1 curtain=1
run=1`): 162 elements with a spec, 53 wires, 4 sources, 6 passes, stable. t1 energised: its primary 480.0 V, 0.521 A across
L1 and L2 (q4's load side); its secondary 120.0 V on q2 and g1.L; 2V and t1.PE on the 0 V / PE net; g1 on (120.0 V, 0.5 A);
the bus at 24.0 V; k-safe and k-lc powered, inputs made, outputs on (0.167 A each); plc-1 run (0.15 A); X1:15 at 24 V; no load
over its limit. Without q4.on (or q1.on): 1 pass, every load at 0 V, t1 dead: the control circuit drops with the supply, as the
built panel will. v0.3 to v0.5 (below) had the transformer as a stand-in.

**What the solver saw, v0.3 to v0.5**: with q1.on, q2.on, t1 (the transformer's
stand-in), field (the station's e-stop jumpered at X1:20 to 23), curtain (k-lc's two channels jumpered from its own pulse
outputs, as a clear curtain would make them: its OSSD inputs are request panel-6 item 4) and run (the controller's up-stroke
output stood in from the bus block kept for io-1, X1:6, to k-safe 23): g1 on (120 V, 0.5 A); the bus at 24.0 V; k-safe and
k-lc powered, inputs made, outputs on; plc-1 run; X1:15 (solenoid b's feed) at 24 V; 5 passes, stable. The lamps stay dark
(their feeds are io-1's, planned). Without `curtain` k-lc's outputs are off and X1:15 is dead; without `t1` nothing in the
control circuit lives.

**The stand-ins** (each a `when` row named in the file with what it stands for; none is a wire): `q1.on` the disconnect's
three poles, gone in v0.5 (the placed switch's own contact rows carry the state, "q1: handle=on"; the solver's figures above
are unchanged: 159 elements with a spec, 46 wires, 5 passes); `t1` the transformer's secondary (sources.csv: 120 V on q2.1) and its grounded end to g1.N and PE:5, gone in v0.6 (t1 placed: its own source row; q4's own contact rows carry q4.on; this panel has no twin scene, so no key needs a stand-in, unlike pnl-motor-starter's q4 rows); `field` the
station's e-stop; `curtain` k-lc's inputs; `run` the up-stroke output. The bridges and the rail are joints with no number.

## 9. The controller's supply cordset w-pwr (v0.8; pnl-motor-starter's section 9, the same method)

- **The part:** cordset-m12 1.8, coding L, genders male-open, length 600 (the catalogue's shortest, cordset-m12 LENGTHS; the
  run is about 270 and the surplus lies in the duct). Its plug in plc-1's port-pwr; its five bare leads (16 AWG, 50 beyond the
  jacket, fanned 6 from the axis: cordset-m12's design) at end B; leads 1 and 3 are wires.csv's landed rows on X1:4 and X1:10.
- **The placement:** bom.csv row w-pwr, parent plc-1.port-pwr, at x 326, y 193.0, z 232.7, pitch 90 (the plugging direction
  up into the socket that looks down). The socket's mouth is at z 307 - 65.1 = 241.9; the plug is drawn offered up, its mating
  face 9.2 below the mouth, as on the first panel (plc0 1.2 models the socket as a solid cylinder: a mated plug overlaps it;
  the receptacle minor is request panel-11 item 2). The plug ends at z 188, 3.0 over duct-145's top (185).
- **The route** (assembly.py PATHS, world points after the plug's own straight 12; build() turns them into the row's frame):
  down into duct-145 at x 326 through its top wall where the finger x 320 to 332 is broken out (bom.csv `breakout=b226`, gap
  312 to 340), stepping forward from y 193.0 to y 184.4 (the first panel's 229.5 on a plate at 275.6; this plate is at 230.5):
  behind the cover's skirts (to y 179.2) and inside the fingers' zone (y 172.8 to 197.8); a 45 degree turn onto the row's run at
  z 166 (the cavity z 146.5 to 183.5); left along the row to x 172; a 45 degree turn down to x 166, through the bottom wall where
  the finger x 160 to 172 is out (`a66`, gap 152 to 180); 3 under the duct (z 142); the jacket's end at (166, 179.4, 137), the last
  leg turned 45 degrees toward the front so that the leads run on down and forward, in front of the blocks (their front faces
  y 178.5; the markers' to 176.5) and over X1:4 to X1:10 (x 140 to 182). **v0.9:** the jacket's end at (166, 176.4, 138), the
  last leg 2 forward for 1 down: at 45 degrees the leads crossed jmp-1's cap (z 110.2 to 118.2, y 158.9 to 166.9; GEO-020
  25.5 mm3); now they pass over it (z about 129 at its front face) and over X1:4 and X1:11, where leads 1 and 3 land: the 16.5 between the duct's bottom (145) and the
  blocks' tops (128.5) holds no 9.8 cable with its leads straight down. The leads' tips stand about 47 in front of the blocks
  since v0.9 (about 25 to v0.8),
  not in the clamps (a lead is straight in the element: wires.csv says "landed").
- **Checks:** GEO-020 1396 solids, no interference (`python lib/build.py assembly pnl-press-hydraulic`: the route iterated in
  seconds, first try); the solver reads the cordset's own contact rows (plc-1 powered, section 8).

## 10. Placed elements not yet at station 6 (v0.10, checked again in v0.11 and v0.12; lib/reviews/panel/r18.md finding 1, r20 finding 4)

OPERATING.md 12 (quality at the source) and lib/panel-shop.md "The line": a panel moves through the stations as an element does,
and a host places common parts that have passed station 6. `python lib/build.py station <id>` on 2026-11-13 (main 0c07f83b; the
four v0.11 pins again at main 29ddebeb, panel-r28; plc-aio 1.1 at main 72c8146b, panel-r29) for
every element this BOM places: these are below station 6 at the pinned version, so **the panel's own station 6 waits on them**.
None is the shop's to fix (each is its lane's element); they are placed because the panel's points need them and no element at
station 6 serves those points.

| tag(s) | element · pin | station reached | what holds it |
|---|---|---|---|
| rail-1 to rail-4 | din-rail-35 1.1 | 1 open | DOC-004: no Stage 0 brief; GEO-070 (its end clamps touch nothing of the body) |
| estop-door | op-estop-22-2nc 1.1 | 1 open | DOC-004: no Stage 0 brief |
| h1, h2 | op-pilot-22 1.0 | 1 open | DOC-004: no Stage 0 brief |
| np-1 | tag-plate 1.0 | 1 open | DOC-008 (a spec figure against the brief's NOT ON FILE) |
| f1 | overload-9a-1no1nc 1.1 | 2 open | GEO-070. Placed since v0.8 under k1, as that element's spec gives (held v0.1 to v0.7); v0.8's report did not name its station (review r20 finding 4) |
| k-safe, k-lc | relay-safety-2ch-2no1nc 1.2 | 5 open | BEH-020: no port node for the probe (wires 48 and 49 have no length for it) |
| w-pwr | cordset-m12 1.8, variant `coding=L;genders=male-open` | 6 open | that variant's AutoCAD gate failed (2026-11-11, core round 29) |

At station 6 or past it (checked the same day): enc-wm 1.4, contactor-18a-1no 1.1, plc0 1.2, plc-dio 1.0, plc-aio 1.1, hmi-7in
1.1, psu-24v-2a4 1.4, mcb-1p-c6 1.5, mcb-2p 1.1, disc-3p-30a 1.7, xfmr-control 1.1, term-4mm 1.6, term-jumper 2.0, gland-m20 1.3
(station 7 open); duct-40x60 1.3, marker-terminal 1.0, term-endplate 1.0 (released). q3 and k-2h are planned rows, not placed
(section 2). A pin moved to a version below station 6 is said so in the round's report (review r21 finding 1).

## History
| version | date | what |
|---|---|---|
| 0.12 | 2026-11-13 | panel-r29 (unattended): pin plc-aio 1.0 to 1.1 (elec-r46's text minor, at station 6; the build already drew 1.1). 57 wires, 30 lengths; 88 BOM rows, 86 placed. A minor: the pin only; no geometry moves. The panel's first AutoCAD gate since 0.9 (AutoCAD hung 03:42 to 10:01) |
| 0.11 | 2026-11-13 | panel-r28 (unattended): every comb blade joined by its own pin: term-jumper's behaviour.csv on main gives pin k `count poles>=k` (elec-r50, request panel-13 item 2), so wires.csv's ten stand-in rows for blades 5 and up (jmp-1.5 to .10, jmp-2.5 to .8) become joins blade to block; the solver reads both groups on every blade, loads as 0.10. Pins (text minors, at station 6): contactor-18a-1no 1.1 (Ue up to 480 V AC, `ue_max`: section 1, m1, K1's 480 V line now waits only on its NEMA power, EF011960, not stated), disc-3p-30a 1.7, hmi-7in 1.1, term-4mm 1.6. 57 wires, 30 lengths; 88 BOM rows, 86 placed. A minor: wires.csv's bridge rows and the pins; no geometry moves |
| 0.10 | 2026-11-13 | panel-r26 (unattended): the combs pushed home (request panel-13's answer item 1): jmp-1 and jmp-2 at y 178.5 (166.9 in 0.9), declared `seated` by lib/contacts.csv (GEO-030: 18 pairs; GEO-020 1492 solids, no interference). Pins psu-24v-2a4 1.4, disc-3p-30a 1.6 (elec-r39 to r41's minors, at station 6). Text (review r20 findings 1 to 4, r18 finding 1): k1's AC-3 18 A said at 400 V and its 480 V rating NOT ON FILE (A), request panel-15; the duct sentence corrected and the insulation NOT ON FILE (B): NFPA 79 13.1.3; port-eth's slot corrected (the Ethernet cordset will break out b200); section 10, the placed elements below station 6. 57 wires, 30 lengths; 88 BOM rows, 86 placed. A minor: the combs move 11.6 toward the blocks, nothing else moves |
| 0.9 | 2026-11-12 | panel-r24 (unattended): X1 laid out again, 36 to 41 blocks (x1-37 to x1-41 added; PE:1 to 8 and the right end cover 30 to the right): the +24 V group X1:1 to 10 and the 0 V group X1:11 to 18 (section 7), the field blocks 14 to 36 renumbered 19 to 41; the bridges placed, term-jumper 2.0 jmp-1 (10 poles) and jmp-2 (8 poles), drawn offered up (section 4; request panel-13); hmi1 placed (hmi-7in 1.0, elec-r38) on the door at x 300, z 420; wires.csv: 55 written, 70 to 76 added (the four contacts' commons, the HMI's supply), every X1 row renumbered, the combs' joins with stand-ins for blades 5 and up; 57 wires, 30 lengths; w-pwr's last leg turned 2 forward for 1 down (it crossed jmp-1's cap: section 9); pins term-4mm, mcb-1p-c6, disc-3p-30a 1.5 (elec's text minors, each at station 6). 88 BOM rows, 86 placed. Strip, PE blocks and the door's cut-out moved or added: not a minor in the elements' sense |
| 0.8 | 2026-11-12 | panel-r20 (unattended): the plate laid out again (section 4): rail-3 to z 307 (length 270, fix_pitch 150) carrying k1 (contactor-18a-1no 1.0, placed), f1 under it (overload-9a-1no1nc 1.1, placed: `HOLD` empty) and the controller plc-1 (from rail-1: its L plug needs ~120 under its rail); duct-365, rail-2 465, duct-525, rail-1 635 (tags duct-325 and duct-515 before); t1 (xfmr-control 1.1, the pin from 1.0) in the motor row at x 384, z 200; io-1 (plc-dio 1.0) and io-2 (plc-aio 1.0) placed on rail-1. The supply cordset w-pwr placed through duct-145's breakouts b226 and a66 (section 9). wires.csv: 36, 39, 43, 44, 46 to 49, 51 to 54 written, 64 to 69 added, 23 and 27 retired for the cordset's rows, three plug-in rows f1 to k1, t1's six wires routed anew; 49 wires, 27 lengths; terminals.csv: nine X1 blocks planned (22 planned, 11 reserved, 3 spare). 81 BOM rows, 78 placed. Rails, ducts, the controller and the transformer moved: not a minor in the elements' sense |
| 0.7 | 2026-11-12 | panel-r18 (unattended): the enclosure bonded: wires.csv 61 to 63 written, PE:1 to 3 side 1 to enc-wm's earth studs PE1 (pe-body), PE2 (pe-door), PE3 (pe-plate) (mech-r95, request panel-7's answer; 61 546, 63 212, 62 across the hinge); terminals.csv PE:1 planned, PE:2 and 3 name their side 1; pins enc-wm 1.4 (1.1), duct-40x60 1.3, mcb-2p 1.1. Text: the motor branch current's wording and one version range in spec.md and wires.csv (lib/reviews/panel/r14.md finding 1), disc-3p-30a 1.4 in the q1 lines (r16.md finding 1). 33 wires, 17 lengths; 80 BOM rows, 73 placed. A minor: no position changed |
| 0.6 | 2026-11-12 | panel-r16 (unattended): t1 (xfmr-control 1.0) placed on the mounting plate right of rail-2 (x 380, z 385; rail-2 length 260, fix_pitch 200: section 4) and q4 (mcb-2p 1.0) on rail-2 at x 200; wires.csv 11 to 17 written and 18 added (t1's frame to PE:6), the `t1` stand-in rows gone (wires.csv and sources.csv), phases 277.128 V; terminals.csv PE:5 and PE:6 planned; pins disc-3p-30a 1.4, mcb-1p-c6 1.4, psu-24v-2a4 1.3 (their port nodes: 15 wire lengths); f1's nameplate FLA written NOT ON FILE (A) (lib/reviews/panel/r11.md note 2). 80 BOM rows, 73 placed; control_power served. A minor: the origin, every duct, device and cut-out kept; rail-2 shorter, t1 at its own place |
| 0.5 | 2026-11-11 | panel-r14 (unattended): the main disconnect q1 placed (request panel-10's answer: lib/motion.csv's three rows for this panel), its body on the mounting plate at the right end of rail-1 (q1 x 465, shaft 198.4; rail-1 length 340, fix_pitch 275: section 4); assembly.py `HOLD` keeps f1 only; wires.csv: the three q1 stand-ins dropped, the motor branch's design current as NOT ON FILE (B), NEC Table 430.250 (lib/reviews/panel/r7.md finding 1), the count of rows that are not wires corrected (24: r7.md's note). 80 BOM rows, 71 placed. A minor: the origin, the rails' positions, every duct, device and cut-out kept; rail-1 shorter, q1 adds its handle cut-out on the door. Gated at this version (panel-r14): status above |
| 0.4 | 2026-11-11 | panel-r11 (unattended): text only, the geometry is v0.2's: f1's range written as open (NOT ON FILE: the motor's nameplate FLA, NEC 430.32; D125 the shop's provisional choice; lib/reviews/panel/r5.md finding 2), the terminal plan's count corrected (13 planned, 20 reserved; r6.md's note), the renamed ids relay-safety-2ch-2no1nc and overload-9a-1no1nc (the library's, core round 29), request panel-10 for the door disconnect's motion rows (request panel-2's answer covers p*-motor-starter only) |
| 0.3 | 2026-11-11 | panel-r7 (unattended): the wire list between the devices on file, wires.csv (22 wires, 3 lengths; the kept numbers for the planned rows) and sources.csv; assembly.py `lengths()`; terminals.csv's wire column; the door e-stop's id op-estop-22-2nc (the library's rename) and the ol_trip point (the core's rename of ol_ok). No BOM row and no position changed: the geometry is 0.2's. Gated in panel-r9 (2026-11-11), no file of the panel changed: AutoCAD PASS (1077 solids, audit clean), Blender PASS (284 meshes clean), Godot QA FAIL (772 draw calls > 400, the core's budget rule; request panel-9) |
| 0.1 | 2026-11-11 | panel-r5 (unattended): the BOM (78 rows: 68 placed), assembly.py and this spec |
| 0.2 | 2026-11-11 | panel-r6 (unattended): the terminal plan, terminals.csv (36 X1 blocks and 8 PE named); two riser ducts (riser-l, riser-r: 80 rows, 70 placed); a minor: the origin and every position of v0.1 kept |
