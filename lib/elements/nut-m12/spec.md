# nut-m12 · v1.5 · M12 x 1 coupling nut

**What** M12 x 1 coupling nut: one part of the M12 joint family (contact-m12-pin, contact-m12-socket, insert-m12, nut-m12, seal-m12, receptacle-m12, plug-m12), so a pin can bend, a socket spring can spread, a nut can be left two turns short, and the twin gets the same symptom a technician gets (`toolkit/contact.py`).
**Class** connector-part · **Baseline** the M12 interface (`toolkit/m12.py` 1.6; IEC 61076-2-101 A / D, IEC 61076-2-111 L class), its figures from the cordset ends and the I/O block's ports read with Open CASCADE (round 4). Nothing of a vendor file ships.
**Units / frame** mm, Z up. Origin: the mating plane on the nut axis (the male carrier face / the female insert face); the counterpart toward −y.
**Built with** toolkit 1.3 · AutoLISP command `M12NUT` · `gender` (male | female), `coding` (A | D | L).

Built in the M12 mating frame of `toolkit/m12.py`: the mating plane at y = 0, the counterpart toward −y, the part's body toward +y, the key toward +z. Every figure of the M12 interface lives in `toolkit/m12.py`, so the two halves of a joint, built by different elements, still meet.

## Dimensions
| item | value |
|---|---|
| male (threaded sleeve) | one solid at the thread envelope r 5.46, bored Ø8.3 (L Ø8.8), from 8.9 (L 8.8) ahead of the mating plane to 1.4 behind it (the lip and chamfer lie inside the envelope); knurl Ø15 (L Ø17.9) from 1.4 to 6.2 behind |
| female (threaded bore) | Ø15 (L Ø17.9) from its front face 1.5 (L 1.3) behind the insert face to past the insert's base, bored Ø10.92 (on the cordset the thread Ø11.0 starts 2.1 behind the insert face, L 1.59) |

## M12 interface figures used (toolkit/m12.py 1.6)
| figure | value | source |
|---|---|---|
| thread | M12 x 1, pitch 1.0. A male half carries the external thread on a sleeve (a cable's coupling nut, a device's fixed sleeve); a female half the threaded bore round its insert. Both are modelled plain at r 5.46, so the halves touch and never overlap | the designation (ISO 261); cordset ends and the I/O block read with Open CASCADE (round 4) |
| two kinds of half | `cordset` (a cable end: the cordset STEP files) and `device` (a housing: the I/O block's STEP); each keeps its own figures | round 4 |
| tightening torque | 0.5 to 0.6 N m | maker's datasheet: the I/O block's technical data p. 2 (0.5); cordset catalogues p. 2 (max. 0.6) |
| genders | X03 Power In male; X04, X1-X8, X01 / X02 female | maker's datasheet: the I/O block's manual p. 32-34 |
| male sleeve | bore Ø8.3, front 8.9 ahead of the carrier face (A / D cordset); Ø8.8 x 8.8 (L cordset); Ø8.9 x 8.9 (X03). Lip Ø10.5 x 2.2 and its 45° chamfer lie inside the modelled thread envelope (one solid) | OCC (the A, D and L cordsets, the I/O block's X03) |
| male thread | from 0.9 behind to 5.95 ahead of the carrier face (A / D); 1.2 behind to 6.44 ahead (L cordset); 3.7 behind to 7.94 ahead (X03) | OCC |
| male nuts | behind the carrier face. A and D (the same nut): front face 0.9 with its 45° chamfer Ø14 → Ø15 to 1.4 (a Ø14 collar), knurl Ø15 1.4 to 3.7 (round to 3.9), hex 13.0 across flats with its corners turned to Ø14.4 from 3.9 to 6.2, back face 6.4. L: front face at 1.2 out to Ø17.9, Ø17.9 to 5.2, hex 16.9 across flats with its corners turned to Ø17.9 to 8.15, back face 8.7. Bodies: A neck Ø8.4 to 7.5, Ø12, tapers to Ø10.2 and Ø8.8, ring Ø10.5 at 28.8, boot end 31.8; D neck Ø8.4 to 8.6, Ø14.2 with three Ø15.0 grip beads, a 20.4° taper to Ø9.0, boot end 38.6; L neck Ø11.1 to 10.0, the overmould to Ø16.9 tapering to Ø12.05, ring Ø13.0 at 41.2, boot end 45.0 (tapers modelled as steps) | OCC (the A cordset round 5; the D and L cordsets round 6) |
| female | the insert face is the half's foremost face. Cordset: nut face 1.5 behind it (L 1.3); thread Ø11.0 from 2.1 (L 1.59) behind it; insert Ø8.2 (L Ø8.7) 9.0 (L 10.5) from the bore floor. Device (the I/O block's ports): housing face 3.4 behind it; Ø12.3 entry to 1.1 behind the housing face, then the Ø10.917 bore to 6.0; floor 9.5 below the insert face | OCC (the A cordset, the L cordset, the I/O block's X1-X8 / X04) |
| where the threads catch | from both halves: a cordset pair 3.85 (L 4.85); a cordset male on an I/O block's female 1.45 (L 1.94), the length engaged at the seat the same | computed (toolkit/m12.py engagement) from the figures above |
| keying | A: a Ø1.2 peg on r 3.55, 8.4 ahead, in a Ø1.3 keyway. D (female-face angles, clockwise from +z): the female a tooth 1.80 wide on the 0° line standing to the insert's edge, flat notches either side with their floors on one chord 3.127 from the axis, and a slot 1.00 wide on the 106.5° line, its floor 3.292 from the axis, both 8.7 deep; the male a chord 3.250 from the axis across the 0° line cut by a 2.00 channel (two blocks out to the sleeve bore) and a flat rib 0.90 wide on the 106.5° line, its top 3.400 from the axis, both 8.4 ahead. L (FE up, u across, + clockwise): the male key block a flat chord (cordset 1.5, X03 1.448), flanks leaning 20° out to the flank tops (cordset ±1.6 at 3.05; X03 −1.648 / +1.651 at 2.998), a ledge on +u and a wall on −u, its face 0.8 behind the sleeve front, the FE socket in it; the female recess (X04 as read: chord 1.369 with feet −1.167 / +1.205, tops −1.731 at 2.919 / +1.770 at 2.922, 8.5 deep; the cordset female takes X04's outline, 8.2 deep: Assumption, see below), its ledge on −u, its wall on +u | OCC face wires (rounds 5 and 6: the I/O block's X01 / X03 / X04, the D and L cordsets); the cordset female's radial grooves not modelled. The cordset female's own STEP keyway (chord 1.4, tops ±1.7 at 3.352) does not fit its own male: an exact boolean of the L cordset's halves as they mate leaves 3.375 mm³ in common (the male's foot 0.302 inside the female's ledge), and the drawing dimensions neither (round 7). M12-010 mates every pair on file |
| contact entries | A / D: Ø1.05, chamfer to Ø2.0, counterbore Ø1.65 from 1.0 in; L: Ø1.6, counterbore Ø2.1 | the I/O block's STEP read-back (maker's file; references/measure.md) |
| pole layout | A female face, clockwise from the key: 2 at 45°, 3 at 135°, 4 at 225°, 1 at 315°, 5 centre, on Ø5.00. D (from the key reference): 2 at 45°, 3 at 135°, 4 at 225°, 1 at 315°, on Ø5.0: the notch pair between 1 and 2, the single notch between 2 and 3. L: on Ø5.88 at 72°, FE at the key | the A cordset drawing, Detail A; maker's datasheet: the I/O block's manual p. 32 Fig. 5 and the D cordset drawing (D, round 5); the I/O block's X04; OCC |
| contacts | A / D pins Ø1.0, 6.45 + 0.45 tip = 6.9 ahead; L Ø1.5, 4.8 + 0.6 tip = 5.4. L FE: the female's pin 7.3 + 0.7 tip, its tip 0.2 below the insert face; the male's socket a Ø1.85 bore 8.0 deep in the key block, so FE makes first (made 6.2 off the seat, the power pins 2.75) | OCC; the make order computed (toolkit/contact.py window) |
| socket bore | mouth 1.0 below the face; bottom 7.0 below the face (A / D holes 7.0 deep); L 8.0; springs from 0.5 into the mouth | read-back (mouth); OCC (depth); springs Assumption |
| engagement | A / D pins touch 4.9 off the seat and are made by 4.4, before any thread catches: a plug pushed on by hand makes contact held by friction only | computed |
| seal | NOT ON FILE: no file on hand shows one. Modelled as a flat ring on the female's bore floor, as thick as the gap the male sleeve leaves plus a 0.2 squeeze | Assumption |
| wipe; contact resistance | 0.5 mm; 5 mΩ | Assumption |
| key tolerance | per coding, from each keyway's own side clearance over the outermost radius the halves share: A 0.807° (the Ø1.2 peg in the Ø1.3 keyway on r 3.55); D 0.704° (the 0.90 rib in the 1.00 slot to r 4.07); L, block wall to recess wall: X03 in a cordset female 1.759°, a cordset male in X04 or in a cordset female 2.452°. The old 5° (an Assumption) let pins stop on the face (found writing the Kani proof) | derived from the figures above (toolkit/m12.py key_tol) |
| ratings (not geometry) | A 4 A, 250 V (cable Ø5.0 for PVC; the TPE cable's Ø NOT ON FILE); D 4 A (1.5 A under the North American listing, maker's datasheet), 60 V DC (Ø6.6); L 12 A (16 AWG, Ø9.8) / 16 A (14 AWG, Ø10.5), 63 V DC | cordset catalogues p. 2; lib/standards |
## Named nodes
`self` (kind rotate about −y, range 0 to 1386° (3.85 turns; L 1746°), extras lead 1.0 mm per turn, drives mate, torque 0.5-0.6 N m): captive on the plug, so turning it pulls the plug home

## Materials by layer
`M-ZINC` (the finish; the cut sheets give nickel-plated brass for the male nut, nickel-plated zinc for the female)

## Decals (Blender)
none

## Notes and assumptions
The joint's state is computed, not drawn: `toolkit/contact.py` `mate()` brings a plug onto a port (key, gender, nut turns, torque) and reports each pole made, marginal, open, high-r or blocked; PIN-030 runs it on every cable end of an assembly. 1.2 turned the thread round (the male half carries the external thread); 1.3 put the terminal's Open CASCADE read-back of the cordset ends and the I/O block's ports on file: the female insert is the foremost face, the thread catch comes from both halves, D keys with three ribs, L with a block that carries FE. Figures marked Assumption are NOT ON FILE: the seal, the contact springs, the D angle sense, the L block's inner edge, the bodies behind the faces. Nothing of a vendor file ships: the files are measured in references/ and stay there.

## Outputs (out/)
`nut-m12.lsp` · `.glb` (contact and port data in the node extras, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, gltf/ per the QA checklist.

## History
| version | change |
|---|---|
| 1.5 | round 6 back (2026-11-04): the D male nut is the A nut (the D cordset); the L male nut as measured (the L cordset): front face 1.2, Ø17.9 to 5.2, a 16.9 hex to its back face at 8.7 |
| 1.4 | round 5 back (2026-11-04): the A male nut as measured (the A cordset): sleeve to its front face 0.9, a Ø14 collar to 1.4, knurl Ø15 to 3.9, a 13 mm hex with turned corners to 6.4 |
| 1.3 | round 4 back (2026-11-04): the male sleeve is one solid (the 1.2 lip and runout put two solids' faces in one plane and the gate's picks failed there); the female nut's face 1.5 (L 1.3) behind the insert face; 3.85 turns (L 4.85) |
| 1.2 | round 4 (2026-11-04): the thread follows the gender (male: the external thread on the sleeve; female: the threaded bore), figures from the cordset drawings; 4.35 turns to the seat; torque 0.5-0.6 N m; params `gender`, `coding` (`back`, `bore_back` gone) |
| 1.1 | round 3 (2026-11-04): torque 0.5 N m on file (maker's datasheet: the I/O block's technical data p. 2); `bore_back` (a female plug's thread runs on for the receptacle's sleeve) |
| 1.0 | first build: the element layer reaches the contacts (2026-11-03), toolkit 1.3 |
