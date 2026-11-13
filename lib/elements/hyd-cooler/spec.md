# hyd-cooler · v1.0 · hydraulic oil cooler, generic, water cooled, shell and tube, two water passes, oil side 16 bar, NPT 3/8 water ports

**What** a water-cooled hydraulic oil cooler (lib/inventory.csv row `hyd-cooler`, "hydraulic oil cooler", own_design generic,
2 systems: hpu-assembly-station, test-bench-hydraulic). It sits in the return line, between the return-line filter and the tank,
and takes out the heat the circuit's losses put into the oil. The oil enters `port-oil-in`, passes through the shell round the
tubes and leaves through `port-oil-out`; the cooling water enters `port-water-in` (the lower port on the water bonnet), runs
through the tubes to the far bonnet and back, and leaves through `port-water-out` (the upper port), so the tubes stay full.
**Class** device · **Baseline** our own design: generic hydraulic oil cooler (no ETIM class; ISO 4413 values), as
OPERATING.md 12 (generic elements, EM 2026-11-07; a product class ETIM has no class for is generic by the standard whose rating
data its Class values follow, EM 2026-11-08) and the inventory row (own_design generic) say. No vendor file was opened or
measured. The class values below are its design inputs; its sizes are design choices. Its water ports take their figures from
the standard on file (ASME B1.20.1, through toolkit/pneu.py); its oil ports' standard is not in lib/standards/sources.csv (Open
figures). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the two feet's underside (the mounting plane z = 0); the shell's axis along x
at z = 90; the water ports on the −x bonnet's end face, the oil ports on the shell's top.
**Built with** toolkit 1.3 · AutoLISP command `HYD-COOLER` · no parameters.

The class chosen: none. The inventory row names no class. lib/standards/etim/classes.csv (ETIM 10.0's subset on file) has three
cooler or exchanger classes and none is an oil cooler: EC002514 and EC002515 are a switchgear cabinet's air/air and air/water
heat exchangers (their features are a cabinet's cut-out and cooling output; hx-shell-tube's case, pneu-r67: a class that doesn't fit the
row's systems is not built to), and EC004896 is a portable evaporative room cooler. So none is claimed. The standard named,
ISO 4413 (hydraulic fluid power: general rules and safety requirements for systems and their components), is not in
lib/standards/sources.csv: it is named as the standard against which the cooler's rating quantities are stated, as hpu-7.5kw 1.1,
valve-counterbalance and hyd-filter-return 1.0 name it, and no figure or clause is taken from it.

Water cooled, not air blast: a design choice. Both kinds are oil coolers; the water-cooled one joins the chiller on file
(chiller 2.1, `port-supply` / `port-return`, female NPT 3/8) through ports of the same size, and it has no fan motor, so it
carries no electrical rating that would have to be stated without a source. An air-blast cooler would be its sibling, a later
element with its own id (OPERATING.md 6: the form in the id), if a machine asks for one.

## Class values (no ETIM class; ISO 4413 values)
Design inputs (OPERATING.md 12): the quantities an oil cooler is chosen by, with the value this one is designed to.

| # | quantity | value |
|---|---|---|
| 1 | max. operating pressure, oil side | design: 16 bar (≥ the tank line's 10 bar, toolkit/hyd.py P_TANK and H5: a part whose every oil port sits on the tank line is judged at the tank line's pressure; element.py asserts); in ratings.csv as p_max, status "generic design" |
| 2 | max. operating pressure, water side | not stated: no water circuit's pressure is on file to rate it for (chiller 2.1's own is one of EM's open lines), and nothing is claimed |
| 3 | cooling capacity | not stated: no heat load is on file (the circuit's losses are its machine's figure), and none is claimed |
| 4 | oil flow, water flow | not stated: no flow or pressure drop at a flow is claimed. The shell is sized for a return line of the press's kind (hydraulic.csv T), a design choice |
| 5 | fluid, oil side | mineral hydraulic oil ISO VG 46 (ISO 11158 HM; toolkit/hyd.py H7) |
| 6 | coolant, water side | water or a water-glycol mix, as a chiller supplies it |
| 7 | construction | shell and tube: the oil in the shell, the water in the tubes, two water passes (both water ports on one bonnet); tubes, tube sheets and baffles not modelled |
| 8 | ports | `port-oil-in`, `port-oil-out` (their thread open, Open figures); `port-water-in`, `port-water-out` female NPT 3/8 |

These are generic design values (OPERATING.md 12), not tested ratings. HYD-003 (toolkit/v_hyd.py) reads p_max in an assembly
whose hyd.csv places the cooler: on the tank line it is judged at that line's pressure, on a pressure line at the relief setting,
where 16 bar fails, as it should: this is a return-line cooler, never a pressure-line one.

**No safety claim.** A cooler holds the oil's temperature; it is no protective device, and this element claims no safety
function (OPERATING.md 12; the inventory row's `safety` column is empty). It has no over-temperature switch: that is the
circuit's, a separate element.

## Dimensions (design choices, our own, but the water bores)
| item | value | why |
|---|---|---|
| shell | Ø100 × 400 along x (x −200 to 200), its axis at z = 90; painted steel (`M-STEEL-7035`) | holds the tube bundle; the oil passes round the tubes |
| bonnets | Ø110 × 40 on each end (x −240 to −199.5 and 199.5 to 240, 0.5 into the shell); cast (`M-ZINC-CAST`) | the −x one takes the water in and out (divided inside for the two passes), the +x one turns it round; 35 above the mounting plane (asserted ≥ 30) |
| oil port blocks | 44 × 44, z 130 to 152, on the shell's top at x = +130 (`port-oil-in`) and −130 (`port-oil-out`); painted steel | a flat face for each oil port; their feet inside the shell across their whole width (the shell's surface is at z 134.9 under a block's edge; asserted); 48 in from the shell's ends |
| oil port spot faces | Ø32 × 1 proud on each block's top (z 151.5 to 153, 0.5 into the block); `M-SILVER` | the joint plane a port fitting meets (hyd-filter-return 1.0's pattern); 6 of block face round each (asserted); no bore cut (Open figures) |
| water port bosses | Ø28 × 16 along −x on the −x bonnet's end face (x −256 to −239.5, 0.5 into the bonnet), at z = 65 (`port-water-in`) and 115 (`port-water-out`), y = 0; `M-GALV` | 22 apart and 16 in from the bonnet's edge (asserted ≥ 20 and ≥ 10); the inlet below so the water rises through the tubes |
| water port bores | Ø17.055 × 12.358 deep, blind, one in each boss from its face | Ø = E1 + h of NPT 3/8 from pneu.NPT (values calculated from ASME B1.20.1's formulas, EM 2026-11-07), the diameter fitting-pushin 2.0 draws its male stub at, so stub and bore touch and never overlap (tank 2.0's rule); depth L2 + 2 (the 2 a run-out), asserted ≥ the make-up and 3 short of the boss's 16; 5.47 of boss wall (asserted ≥ 5). Role in features.csv (HOLE-010) |
| feet | two saddles 30 × 120 × 45 high under the shell at x = −150 and +150; black (`M-BLACK-PA`) | carry the shell 40 above the mounting plane; each holds the shell over 40 of its width (asserted); wider than the bonnets |
| tubes, tube sheets, baffles | not modelled | inside the shell |
| overall | envelope 496 × 120 × 153 (x −256 to 240, y −60 to 60, z 0 to 153) | |

## Ports (toolkit/hyd.py, toolkit/pneu.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-oil-in` | hyd-port | female | none | the spot face on the +x block, x = 130, z = 153, axis +z | design: named by its function (as hyd-filter-return 1.0's ports); the hydraulic port marking standard (ISO 9461) is not on file, so no letter or number is claimed |
| `port-oil-out` | hyd-port | female | none | the spot face on the −x block, x = −130, z = 153, axis +z | as `port-oil-in`; to the tank. The oil runs toward −x, against the water's first pass |
| `port-water-in` | NPT3/8 | female | none (a liquid port) | the lower boss's face, x = −256, z = 65, axis −x | pneu.py D1 (NPT, ASME B1.20.1); NPT 3/8 as coolant-pump's and chiller's liquid ports; named by its function, no ISO 11727 number (that numbering is for pneumatic ports) |
| `port-water-out` | NPT3/8 | female | none (a liquid port) | the upper boss's face, x = −256, z = 115, axis −x | as `port-water-in` |

"hyd-port" is toolkit/hyd.py's unit for a hydraulic port whose dash size is open (H1); HYD-001 reads a joint on it as REVIEW until
the size is stated, and HYD-002 wants both oil ports joined in an assembly. No role: toolkit/pneu.py's roles are air roles, and no
HYD check reads one but `plug`. A fitting-pushin 2.0 with an NPT 3/8 stub screws into either water port face to face.

## Open figures
- NOT ON FILE (B): SAE J1926-1 table 1, the two oil ports' dash size, thread, spot face and depth (toolkit/hyd.py H1 and H4:
  every cell of DASH is open; the standard is not in lib/standards/sources.csv). The oil ports are plain spot faces with their
  pivots; the bores are cut once the table is on file (a major).

## Named nodes
`port-oil-in`, `port-oil-out` (the spot faces), `port-water-in`, `port-water-out` (the bosses): kind port, fixed (range 0).
Nothing moves.

## Materials by layer
`M-STEEL-7035` shell, oil port blocks · `M-ZINC-CAST` bonnets · `M-SILVER` oil port spot faces · `M-GALV` water port bosses ·
`M-BLACK-PA` feet

## Decals (Blender)
None (the flow arrows, the port names and the "generic" label are a later version). No vendor names, no approval marks.

## Notes
- No mounting holes: the feet are plain in this version; their holes, with a clearance from lib/standards/holes.csv and a
  features.csv row, are a later version (a new cut-out, so a major).
- No drain or vent plug on the bonnets in this version.
- The twin reads no temperature from it: the oil's temperature comes with a hydraulic and thermal model (behaviour.csv).

## Outputs (out/)
`hyd-cooler.lsp` · `.glb` (port pivots, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (no ETIM class; ISO 4413 values), pneu-r80 (unattended): water-cooled shell-and-tube oil cooler, shell Ø100 × 400 on two saddle feet, two bonnets; oil ports `port-oil-in` / `port-oil-out` as spot faces on two blocks on the shell's top (hyd-port, the thread left open, class B); water ports `port-water-in` / `port-water-out` female NPT 3/8 on the −x bonnet, bored Ø (E1 + h) × (L2 + 2) deep, blind in their bosses; oil side 16 bar; tubes, tube sheets and baffles not modelled; nothing placed |
