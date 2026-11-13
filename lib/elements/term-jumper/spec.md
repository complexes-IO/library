# term-jumper · v2.0 · plug-in jumper for term-4mm feed-through blocks, 4 poles (complexes.org generic)

**What** A plug-in jumper (cross-connector) for term-4mm feed-through blocks: a comb of copper blades on one bar under an insulating cap, one blade per block at the block's pitch, pushed into the blocks' centre channel from the front. It joins neighbouring blocks into one potential without taking a clamp, so a panel's +24 V or 0 V group lands one conductor a clamp (pnl-motor-starter's X1:1 to 4, X1:5 to 8 and X1:15 to 16; request panel-3 item 1, lib/requests/core/elec-term-jumper-2026-11-11.md). 2 to 12 poles by parameter (built with 4), 32 A, 500 V. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC000489, built to the class values below; no maker's datasheet and no product is matched.
**Class** device · **Baseline** our own design: generic Cross-connector for terminal block (ETIM 10.0 EC000489). The class values are this element's definition (design inputs); the pitch and the reach come from term-4mm 1.4 on file; the block's channel is open (class B, Dimensions) and the blades are built to a design channel; every other size is a design choice, said so below. Class and feature names: ETIM International, ETIM 10.0, ODC-BY 1.0 (lib/standards/etim/README.md).
**Units / frame** mm, Z up. Origin: the cap's seating face on the block's front y = 0, blades toward +y (into the block, toward the rail); pole 1's blade on x = 0, poles along +x at the pitch; z = 0 on the blades' axis. In term-4mm's frame the jumper sits at (3.0 + 6.0 (k − 1), −44.5, 9.2): the first bridged block's centre, the block's front face, the design channel's z (9.5 in 1.0).
**Built with** toolkit 1.3 · AutoLISP command `TERMJMP` · parameter `poles` (2 … 12; 4 as built and gated).

## Class values
ETIM 10.0 EC000489 "Cross-connector for terminal block", every feature in ETIM's order (lib/standards/etim/class-features.csv), with the value this element is designed to.

| # | feature (ETIM) | value |
|---|---|---|
| 1 | Model (EF000010) | plug-in bridge (a comb of blades on one bar, pushed into the blocks' centre channel) |
| 2 | Number of bridged clamps (EF002550) | 4 as built; 2 to 12 by the parameter `poles` (2 and 4 for pnl-motor-starter's X1 groups) |
| 3 | Explosion-tested version 'Ex e' (EF008498) | no |
| 4 | Rated current In (EF008250) | 32 A: the rating of the block it bridges (term-4mm's brief, references/measure.md of term-4mm: 1000 V / 32 A, the 4 mm² class). The rule the sections meet: each blade is at least the block's own rated section, 4.05 mm² (1.5 × 2.7) against 4 mm², and the bar 5.0 mm² carries the group's current between blades; the standard that ties a block's rated current to its section (IEC 60947-7-1) is not in lib/standards/sources.csv, so the claim rests on the block's rated section, not on that standard |
| 5 | Rated voltage (EF000228) | 500 V: covers the library's 480 V panels (mc-motor-1's supply, lib/assemblies/mc-motor-1/controls.csv); the insulation between bridged groups is the blocks' walls round each blade (term-4mm's brief: 1000 V), which hold once term-4mm has the channel (Dimensions); the caps add none |
| 6 | Insulated (EF000019) | yes (the cap covers the bar; only the blades are bare, inside the blocks) |
| 7 | With contact protection (EF008186) | yes (plugged in, no live part is outside the blocks) |
| 8 | Mounting method (EF000003) | plug-in |
| 9 | Modular spacing (EF000394) | 6 mm (term-4mm 1.4 SIZES, the feed-through pitch, read at build time) |
| 10 | Colour (EF000007) | red |

These values are what the element claims: ratings are the class definition, not a certification, and no approval mark is shown. `ratings.csv` carries the electrical ones for the ratings checks (status "generic design"); `pins.csv` gives each blade its role; `behaviour.csv` what the solver reads (the comb is one conductor).

## Dimensions
| item | value | source |
|---|---|---|
| pitch | 6.0 between blade axes (x 0, 6, 12, 18 at 4 poles) | term-4mm 1.4 SIZES["feed"] (the block's pitch on file), read at build time |
| reach | 11.5 from the seating face to the blade tips (y 0 … 11.5): the block's front face to the face of its current bar | term-4mm 1.4 element.py (the wire axis 9.0 off the front, the current bar 2.5 behind it) |
| cap | ((poles − 1) × 6.0 + 5.5) × 8.0 × 8.0 (x −2.75 … 20.75 at 4 poles, y −8 … 0, z −4 … 4): 23.5 wide at 4 poles; the ends 2.75 past the end blades' axes, so two combs on neighbouring groups stand 0.5 apart | design choice; the 8 × 8 section is the AutoCAD gate's: its fillet pre-flight rejects 4 and 5 mm end-face edges on the envelope (run 1 of elec-r29; pneu-r70's 4 mm tab passed at 8) |
| bar | (poles − 1) × 6.0 + 1.5 long × 2.0 × 2.5 (y −3.0 … −1.0, z −1.25 … 1.25), in a pocket of the cap 1.0 under the seating face | design choice (5.0 mm²) |
| blades | one per pole: 1.5 (x) × 2.7 (z), from the bar's face (y −1.0) through a slot in the cap's floor to y 11.5; 0.1 past the bar's 2.5 on each side in z | 4.05 mm²: at least the bridged block's own rated section (term-4mm's brief, references/measure.md of term-4mm line 3: the 4 mm² class), so each blade carries the block's 32 A on the block's own basis (2.0, review term-jumper-1.0 finding 2; 1.0's 1.5 × 2.5 = 3.75 mm² was below it). Kept 1.5 thick, as 1.0: a 1.6 blade had its 12.5 long edges rejected by the AutoCAD gate's fillet pre-flight (2.0's first run, elec-r36), so the section grew in z |
| design channel | the slot in the block the blade needs: 1.5 × 2.7 at the block's centre x, at z = 9.2 of term-4mm's frame, 11.5 deep from the front face to the current bar (z 7.85 … 10.55, on the bar's z −11.75 … 11.75); z = 9.2 keeps the cap (z 5.2 … 13.2) 0.2 clear of the marker tag (marker-terminal 1.0: z −5 … 5) and 0.2 clear of clamp 1's screwdriver hole (term-4mm 1.4: Ø4.2 at z 15.5, `P.hole`'s radius 2.1, so z 13.4 … 17.6) | design choice of this joint: term-4mm has no channel on file (NOT ON FILE (B): the maker's drawing of term-4mm's bar jumper, the document wanted; term-4mm's brief lists that jumper, references/measure.md of term-4mm line 9, not downloaded, and no standard tabulates a terminal maker's jumper channel: an attended download, lib/needs-em/elec.md r36). Whether term-4mm, a measured element, takes this design channel is the core's to rule (review term-jumper-1.0 finding 3) |
| overall | 23.5 × 19.5 × 8.0 at 4 poles (x −2.75 … 20.75, y −8 … 11.5, z −4 … 4) | from the parts above |

Pole marks 1 … n from pole 1 (x = 0), a design choice; no print on the part (the cap's top face, 8.0 × 23.5, carries "complexes.org" as a decal only).

## Named nodes
Ports `p-1` … `p-n` (the blades; kind port, unit pin, gender male: each plugs into a block's channel, PIN-002; the pivot at the blade's tip on the block's current bar). No moving node.

## Materials by layer
`M-RED-PA` cap · `M-CU` bar and blades

## Decals (Blender)
On the cap's top face: "complexes.org generic", "term-jumper", "32 A 500 V". No maker's name, logo or approval mark.

## Notes and open figures
- One fit is open: the block's jumper channel (class B, above: the maker's drawing is the document wanted). The blades are built to this element's design channel; until term-4mm has a channel (the core's ruling), an assembly that places both shows the blades inside the block's body. Everything else is a design choice of this element; nothing is guessed and shown as sourced.
- A comb bridges feed-through blocks only (the ground blocks bond through the rail and are 5.0 pitch). It takes no clamp: the blocks' clamps stay free for one conductor each (pnl-motor-starter's terminals.csv rule).
- behaviour.csv is written for the 4-pole build: pins 1 … 4 on p-1 … p-4, joined `always` through the bar. A 2-pole build has p-1 and p-2 only.
- Not a safety-function device. No rating beyond the class values is claimed.

## Outputs (out/)
`term-jumper.lsp` · `.glb` (pivots on the ports, `env-colonly` collider) · `preview-*.png`. Gates (AutoCAD, Blender, Godot) at 2.0 in elec-r36 (lib/rounds/elec/r36.md); 1.0's in elec-r29.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (ETIM 10.0 EC000489), our own design; elec-r29 (unattended, 2026-11-11) |
| 2.0 | a major (review term-jumper-1.0 findings 1 to 3; elec-r36, unattended, 2026-11-12): the design channel at z 9.2 of the block's frame (was 9.5), so the 8.0 cap clears clamp 1's screwdriver hole, which 1.0 read with its radius as a diameter (z 13.4 … 17.6, not 14.45 … 16.55), and the marker tag, 0.2 each; each blade 1.5 × 2.7 = 4.05 mm², at least the block's rated section (was 1.5 × 2.5 = 3.75; a first 1.6 × 2.5 failed the AutoCAD gate's fillet pre-flight on the blades' long edges, so the blade kept 1.0's 1.5 thickness and grew in z); the open line names its document, the maker's drawing of the bar jumper; the 500 V row no longer leans on the caps' spacing. The origin moves 0.3 in the block's frame, so a major; nodes p-1 … p-4 and the overall size are unchanged |
