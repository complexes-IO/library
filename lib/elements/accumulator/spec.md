# accumulator · v1.0 · hydraulic accumulator, generic, bladder type, 1 l nominal gas volume, 160 bar, upright, fluid port down

**What** a hydraulic bladder accumulator (lib/inventory.csv row `accumulator`, "hydraulic accumulator (bladder)", own_design
generic, 1 system: hpu-assembly-station). A steel shell holds a gas-filled bladder; oil from the pressure line enters through
`port-oil` under the shell and squeezes the gas, and the gas pushes the oil back out when the line's pressure falls. In a
circuit it stores energy, covers a short peak of flow and smooths the pump's pulsation. It stands upright, the fluid port down
and the gas charging valve, under its cap, on top.
**Class** device · **Baseline** our own design: generic hydraulic bladder accumulator (no ETIM class; ISO 4413 values), as
OPERATING.md 12 (generic elements, EM 2026-11-07; a product class ETIM has no class for is generic by the standard whose rating
data its Class values follow, EM 2026-11-08) and the inventory row (own_design generic) say. No vendor file was opened or
measured. The class values below are its design inputs; its sizes are design choices. Its fluid port's standard is not in
lib/standards/sources.csv (Open figures). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: the centre of the fluid port's face (the joint plane z = 0); the shell's axis along +z.
**Built with** toolkit 1.3 · AutoLISP command `ACCUMULATOR` · no parameters.

The class chosen: none. The inventory row names no class. lib/standards/etim/classes.csv (ETIM 10.0's subset on file) has the
word only as a synonym of batteries (EC011878, EC000356, EC000357) and of a battery charger (EC011960); EC012187 "Pressured
air vessel" (receiver-air's class) is an air receiver, with no gas charge and no bladder, and its features (a compressed air
vessel's connections and a safety valve) do not describe this part. So none is claimed. The standard named, ISO 4413 (hydraulic
fluid power: general rules and safety requirements for systems and their components), is not in lib/standards/sources.csv: it
is named as the standard against which the accumulator's rating quantities are stated, as hpu-7.5kw 1.1, valve-counterbalance
1.1, hyd-filter-return 1.0 and hyd-cooler 1.0 name it, and no figure or clause is taken from it.

The id: the inventory's, kept (OPERATING.md 12). Under OPERATING.md 6's id convention (class, form, size, function) it would
read `accumulator-bladder-1l`; request pneu-10 already asks the core how the lane's hydraulic ids are to be renamed, and this
one rides with its answer (lib/needs-em/pneu.md).

## Class values (no ETIM class; ISO 4413 values)
Design inputs (OPERATING.md 12): the quantities an accumulator is chosen by, with the value this one is designed to.

| # | quantity | value |
|---|---|---|
| 1 | max. operating pressure | design: 160 bar (rated for the relief pressure of the hydraulic circuits on file: hpu-7.5kw 1.1's p_max and relief setting, the press's hydraulic.csv; toolkit/hyd.py H5: every element on the pressure side has p_max at or above the relief setting); in ratings.csv as p_max, status "generic design". An accumulator makes no pressure of its own: its gas is at the oil's pressure |
| 2 | nominal gas volume | design: 1 l (the shell's inside, Ø98 × 134 at an 8 wall: 1.01 l, the ends not counted; `volume_l()`, asserted within 5 %) |
| 3 | gas | design: dry nitrogen, an inert gas (never air or oxygen over oil) |
| 4 | gas pre-charge pressure | not stated: a setting, made at commissioning from the circuit's minimum working pressure; the circuit's figure, and none is claimed here |
| 5 | useful oil volume, max. flow | not stated: they follow from the pre-charge and the circuit's pressures (the gas law); no figure is claimed |
| 6 | fluid | mineral hydraulic oil ISO VG 46 (ISO 11158 HM; toolkit/hyd.py H7) |
| 7 | construction | bladder type: a steel shell, a gas-filled elastomer bladder, a poppet in the fluid port that closes when the bladder is full out; bladder and poppet not modelled |
| 8 | mounting position | upright, the fluid port down |
| 9 | ports | `port-oil` (its thread open, Open figures); the gas charging valve under its cap is no port of the circuit |

These are generic design values (OPERATING.md 12), not tested ratings, and not a pressure vessel's code rating: no
pressure-vessel design code (ASME BPVC Section VIII, EN 13445; receiver-air 2.0 names the same two) is on file, the shell is modelled
solid, its 8 wall serves the volume figure only, and no stamp, listing or approval mark is shown or claimed (receiver-air 2.0's
case). HYD-003 (toolkit/v_hyd.py) reads p_max in an assembly whose hyd.csv places the accumulator on a pressure line.

**No safety claim.** An accumulator holds stored energy after the pump stops. What makes a circuit with one safe to work on
(a shut-off valve, a discharge valve to the tank, a relief valve on the accumulator's side of the shut-off, a warning sign) are
the circuit's parts, separate elements, the assembly's to place; none is modelled or claimed here, and this element is not a
protective device (the inventory row's `safety` column is empty; lib/needs-em/pneu.md asks EM whether he wants a line on it).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| shell | Ø114 × 150 along z (z 46 to 196); painted steel (`M-STEEL-7035`) | holds the bladder; 1 l inside at an 8 wall (class value 2) |
| ends | Ø90 × 15 below and above the shell (z 31 to 46.5 and 195.5 to 211, 0.5 into it) | show the rounded ends without modelling their curve (compressor-air's way) |
| fluid port block | Ø50 × 30 under the lower end (z 1 to 31.5, 0.5 into it); `M-ZINC` | carries the fluid port; the poppet inside it not modelled |
| fluid port spot face | Ø32 × 1 proud under the block (z 0 to 1.5, 0.5 into it); `M-SILVER` | the joint plane a port fitting meets (hyd-filter-return 1.0's pattern); 9 of block face round it (asserted ≥ 6); no bore cut (Open figures) |
| gas valve stem | Ø16 × 12 on the upper end (z 210.5 to 223, 0.5 into it); brass | the gas charging valve; its core and thread not modelled, nothing claimed |
| gas valve cap | Ø28 × 28 over the stem's end (z 222.5 to 251); black (`M-BLACK-PA`) | protects the charging valve; fixed in the model |
| bladder, poppet | not modelled | inside the shell |
| overall | envelope 114 × 114 × 251 (x and y −57 to 57, z 0 to 251) | |

## Ports (toolkit/hyd.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-oil` | hyd-port | female | none | the spot face under the port block, the origin, axis −z | design: named by its function (as hyd-filter-return 1.0's and hyd-cooler 1.0's ports); the hydraulic port marking standard (ISO 9461) is not on file, so no letter or number is claimed |

"hyd-port" is toolkit/hyd.py's unit for a hydraulic port whose dash size is open (H1); HYD-001 reads a joint on it as REVIEW
until the size is stated. No role: toolkit/pneu.py's roles are air roles, and no HYD check reads one but `plug`. The gas valve
has no node: no element of the library joins it, and a charging set is a tool.

## Open figures
- NOT ON FILE (B): SAE J1926-1 table 1, the fluid port's dash size, thread, spot face and depth (toolkit/hyd.py H1 and H4:
  every cell of DASH is open; the standard is not in lib/standards/sources.csv). The fluid port is a plain spot face with its
  pivot; the bore is cut once the table is on file (a major).

## Named nodes
`port-oil` (the spot face): kind port, fixed (range 0). Nothing moves.

## Materials by layer
`M-STEEL-7035` shell and ends · `M-ZINC` fluid port block · `M-SILVER` fluid port spot face · `M-BRASS` gas valve stem ·
`M-BLACK-PA` gas valve cap

## Decals (Blender)
None (the "generic" label, the pressure and volume figures and a stored-energy warning are a later version; signs are their
own elements). No vendor names, no approval marks.

## Notes
- No clamp or bracket: an accumulator is held round its shell by clamps on a bracket, the assembly's parts (not built). The
  shell's Ø114 is the figure a clamp element would take from this one.
- The twin reads no pressure or oil volume from it: the gas law's state comes with a hydraulic model (behaviour.csv).
- Not placed: the shut-off and discharge block and the relief valve an accumulator stands on in a circuit (no such element is
  built; "No safety claim" above).

## Outputs (out/)
`accumulator.lsp` · `.glb` (port pivot, `-colonly` collider) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per the QA
checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (no ETIM class; ISO 4413 values), pneu-r82 (unattended): upright bladder accumulator, shell Ø114 × 150 with stepped ends, 1 l nominal gas volume, 160 bar by design; fluid port `port-oil` as a spot face under the port block (hyd-port, the thread left open, class B); gas charging valve stem and cap on top, no node; bladder and poppet not modelled; nothing placed, nothing moves |
