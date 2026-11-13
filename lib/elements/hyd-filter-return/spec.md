# hyd-filter-return · v1.2 · hydraulic return-line filter, generic, inline head with spin-on canister, 16 bar, bypass 3 bar, clogging indicator

**What** an inline hydraulic return-line filter (lib/inventory.csv row `hyd-filter-return`, "hydraulic filter (return line)", own_design
generic, 2 systems: hpu-assembly-station, test-bench-hydraulic). It sits in the T line between the directional valve and the tank
and takes out the dirt the circuit made before the oil reaches the tank again. Oil enters `port-in`, passes through the element
in the spin-on canister under the head from its outside to its core, and leaves through `port-out`. When the element is clogged
its pressure drop rises: first the clogging indicator on the head (`indicator`, a red button) rises, then a bypass valve in the
head opens, so the return line is never blocked. The canister is changed by hand or with a wrench on the boss under it.
**Class** device · **Baseline** our own design: generic hydraulic return-line filter (no ETIM class; ISO 4413 values), as
OPERATING.md 12 (generic elements, EM 2026-11-07; a product class ETIM has no class for is generic by the standard whose rating
data its Class values follow, EM 2026-11-08) and the inventory row (own_design generic) say. No vendor file was opened or
measured. The class values below are its design inputs; its sizes are design choices. No standard on file shapes it: its ports'
standard is not in lib/standards/sources.csv (Open figures). No vendor names; "generic" in its title.
**Units / frame** mm, Z up. Origin: port-in's face, the inlet spot face's outer face on the flow axis (x = 0); the flow axis along
+x to port-out, the canister down (−z), the clogging indicator up (+z).
**Built with** toolkit 1.3 · AutoLISP command `HYD-FILTER` · no parameters.

The class chosen: none. The inventory row names no class. lib/standards/etim/classes.csv (ETIM 10.0's subset on file) has no
hydraulic filter class. Its nearest, EC010080 "Bucket filter, single" (tier 2, group EG015140 "Filters/separators", synonym "Oil
filter"), is a basket strainer for a pipeline: a coarse screen in a flanged or threaded pot, with no bypass valve, no clogging
indicator and no fine element, and lib/standards/etim/class-features.csv holds none of its features. EC010151 "Pipeline
strainer" is the same kind. Neither describes a return-line filter of a hydraulic circuit, so none is claimed (hx-shell-tube's case, pneu-r67:
a class that doesn't fit the row's systems is not built to). The standard named, ISO 4413 (hydraulic fluid power: general rules
and safety requirements for systems and their components), is not in lib/standards/sources.csv: it is named as the standard
against which the filter's rating quantities are stated, as hpu-7.5kw 1.1 and valve-counterbalance 1.0 name it, and no figure or
clause is taken from it.

## Class values (no ETIM class; ISO 4413 values)
Design inputs (OPERATING.md 12): the quantities a return-line filter is chosen by, with the value this one is designed to.

| # | quantity | value |
|---|---|---|
| 1 | max. operating pressure | design: 16 bar (≥ the tank line's 10 bar, toolkit/hyd.py P_TANK and H5: a part whose every port sits on the tank line is judged at the tank line's pressure; element.py asserts); in ratings.csv as p_max, status "generic design", its source the same design rule (1.1: "design: 16 bar ≥ the tank line's 10 bar (toolkit/hyd.py P_TANK and H5); ISO 4413 named and not on file", as valve-counterbalance 1.1's and hyd-cooler 1.0's; hyd-filter-1.0.md finding 1) |
| 2 | filtration rating | 10 µm nominal: design choice. No beta ratio is claimed (its test standard, ISO 16889, is not in lib/standards/sources.csv) |
| 3 | bypass valve opening pressure drop | 3 bar: design choice, below the max. operating pressure (asserted) |
| 4 | clogging indicator | visual, a button that rises 5 mm at a pressure drop of 2 bar: design choice, below the bypass (asserted), so the indicator shows before unfiltered oil passes |
| 5 | flow | not stated: no flow or pressure drop at a flow is claimed. The head is sized for a return line of the press's kind (hydraulic.csv T), a design choice |
| 6 | fluid | mineral hydraulic oil ISO VG 46 (ISO 11158 HM; toolkit/hyd.py H7) |
| 7 | element | spin-on canister, changed whole; its medium not stated |
| 8 | ports | `port-in`, `port-out`, their thread open (Open figures) |

These are generic design values (OPERATING.md 12), not tested ratings. HYD-003 (toolkit/v_hyd.py) reads p_max in an assembly
whose hyd.csv places the filter: on the tank line it is judged at that line's pressure, on a pressure line at the relief setting,
where 16 bar fails, as it should: this is a return-line filter, never a pressure-line one.

**No safety claim.** The bypass valve protects the element and keeps the return line open; it is no pressure relief of the
circuit, and this element claims no safety function (OPERATING.md 12; the inventory row's `safety` column is empty).

## Dimensions (design choices, our own)
| item | value | why |
|---|---|---|
| head | 100 long (x 1 to 101) × 80 × 40, the flow axis through its centre (y = 0, z = 0); anodised aluminium (`M-ALU-ANOD`) | holds the two ports, the bypass valve and the indicator, and the canister's seat on its underside |
| port spot faces | Ø32 × 1 proud on each end face, on the flow axis (x 0 to 1.5 and 100.5 to 102, 0.5 into the head) | the joint plane a port fitting meets (hyd-flow-control 1.0's pattern); 4 of end face above and below each (asserted); no bore cut (Open figures) |
| canister | Ø76 × 130 under the head's centre (x = 51), z −150 to −19.5 (0.5 into the head); painted steel (`M-STEEL-7035`) | the spin-on element; 2 inside the head's underside across y, 12 along x (asserted ≥ 2) |
| wrench boss | Ø30 × 8 under the canister's end, z −158 to −149.5 (0.5 into the canister) | where a wrench turns the canister off; drawn round (its flats are appearance) |
| indicator housing | Ø20 × 10 on the head's top face at x = 26, z 19.5 to 30 (0.5 into the head); black (`M-BLACK-PA`) | over the inlet side, where the dirty oil's pressure acts; 15 from the head's inlet end face (asserted ≥ 5) |
| indicator button | Ø10 × 4 on the housing, face to face (z 30 to 34 at rest); red (`M-RED-PA`) | rises 5 when the element is clogged |
| element, bypass valve, indicator piston and spring | not modelled | inside the canister and head |
| overall | envelope 102 × 80 × 192 (x 0 to 102, y −40 to 40, z −158 to 34) at rest; 197 high with the button risen | |

## Ports (toolkit/hyd.py)
| node | unit | gender | role | at | basis |
|---|---|---|---|---|---|
| `port-in` | hyd-port | female | none | the inlet spot face, x = 0, axis −x | design: named by its function (as control-valve 1.0's liquid ports); the hydraulic port marking standard (ISO 9461) is not on file, so no letter or number is claimed |
| `port-out` | hyd-port | female | none | the outlet spot face, x = 102, axis +x | as `port-in`; to the tank |

"hyd-port" is toolkit/hyd.py's unit for a hydraulic port whose dash size is open (H1); HYD-001 reads a joint on it as REVIEW until
the size is stated, and HYD-002 wants both ports joined in an assembly. No role: toolkit/pneu.py's roles are air roles, and no
HYD check reads one but `plug`.

## Open figures
- NOT ON FILE (B): SAE J1926-1 table 1, the two ports' dash size, thread, spot face and depth (toolkit/hyd.py H1 and H4: every
  cell of DASH is open; the standard is not in lib/standards/sources.csv). The ports are plain spot faces with their pivots; the
  bores are cut once the table is on file (a major).
- NOT ON FILE (B): ISO 9461, the two oil ports' marks (toolkit/hyd.py H11, request pneu-10's answer item 2: hydraulic port
  identification; lib/standards/sources.csv iso-9461, wanted), as hpu-0.37kw 1.0's, hyd-flow-control 1.2's and valve-counterbalance
  1.2's lines. The ports are named by their function (`port-in`, `port-out`) and claim no letter or number; when the standard is on
  file, hyd.PORT_MARKS takes the marks with their clause and a text minor marks these ports from it.

## Named nodes
`indicator` (the clogging indicator's button): kind translate along +z at x = 26, 0 to 5 mm, at rest 0 (seated: the element
clear). The twin reads no pressure from it in 1.0: its two states are set by hand until a hydraulic model drives them
(behaviour.csv). `port-in`, `port-out` (the spot faces): kind port, fixed (range 0).

## Materials by layer
`M-ALU-ANOD` head · `M-SILVER` port spot faces · `M-STEEL-7035` canister, wrench boss · `M-BLACK-PA` indicator housing ·
`M-RED-PA` indicator button

## Decals (Blender)
None (the flow arrow, the port names and the "generic" label are a later version). No vendor names, no approval marks.

## Notes
- No mounting holes: the head is carried by its port fittings here; tapped holes on the head's top face, with their thread
  derived (toolkit/derive.py thread), are a later version.
- The canister is one fixed solid with the head in this version; a replaceable `element` node (the engineer changes a clogged
  canister) is a later major, with the twin's hydraulic model.

## Outputs (out/)
`hyd-filter-return.lsp` · `.glb` (indicator and port pivots, `-colonly` colliders) · `preview-*.png`. Terminal: dwg/, step/, gltf/ per
the QA checklist.

## History
| version | change |
|---|---|
| 1.0 | first build, generic (no ETIM class; ISO 4413 values), pneu-r79 (unattended): inline return-line filter, head 100 × 80 × 40 with spot faces `port-in` / `port-out` (hyd-port, the thread left open, class B), spin-on canister Ø76 × 130 with a wrench boss, clogging indicator `indicator` (translate, 5 mm); 16 bar, bypass 3 bar, indicator 2 bar; element, bypass valve and indicator internals not modelled; nothing placed |
| 1.1 | text only, pneu-r86 (unattended; review hyd-filter-1.0.md finding 1, pneu/r79.md finding 1): ratings.csv p_max's source in the "design: ..." form naming the rule (≥ hyd.P_TANK, H5) with ISO 4413 named and not on file, as valve-counterbalance 1.1's; element.py's canister comment gives the canister's outside volume (note 1). No geometry, node, origin or cut-out changed |
| 1.2 | text only, pneu-r89 (unattended; review hyd-filter-1.1.md note 1, pneu/r86.md note 3): Open figures carries the ISO 9461 line for the two ports' marks (a class B line, the document wanted in lib/standards/wanted.md; request pneu-10's answer item 2), which the Ports table already named as not on file; built under the id core round 29 gave the element (hyd-filter). No geometry, node, origin or cut-out changed |
