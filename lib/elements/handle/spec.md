# handle · v1.0 · pull handle 136 x 42, own design, two Ø12 legs 120 apart under a 12 x 12 grip bar, 2 x M6 tapped ends (thread derived, ISO 965-1)

**What** A pull handle: the bar a hand takes to open a guard door, a cabinet door, a drawer or a hinged cover, screwed to it from
behind. Two round legs stand on the mounting face and a square grip bar joins their ends; each leg's foot is tapped M6 for a
socket head cap screw driven through the door's clearance hole. The inventory row lists it as "handle" (made of two socket head
cap screws, screw-iso4762) for the doors, drawers and covers of the machine rows (lib/machines-factory.txt); no system row names
it on its own. One fixed body: no moving node (the door it moves is the host's node) and no terminal.
**Class** device · **Baseline** our own design, OPERATING.md 12 "Own designs" (EM, 2026-11-05): handles are in its list and
lib/inventory.csv marks the row own_design "yes". No ETIM 10.0 class on file is a plain pull handle and no handle standard is in
lib/standards/sources.csv, so there are no class values and no standard's figures to follow: the thread it carries is derived
from the standards on file (ISO 68-1, ISO 965-1) and every other size is a design choice. No product was matched and no vendor
file was opened.
**Units / frame** mm, Z up: the grip runs along x, the legs along y. Origin: the mounting face plane (y = 0, the door's outer face)
at the handle's centre, x = 0 midway between the legs, z = 0 on the legs' axes; +y away from the door. The legs' axes are the
lines x = ±60, z = 0 along y (y 0 to 30); the grip lies at x ±68, y 30 to 42, z ±6. Extents x ±68, y 0 to 42, z ±6.
**Built with** toolkit 1.3 · AutoLISP command `HANDLEPULL` · no parameters.

## What it meets
| figure | value | source |
|---|---|---|
| the screws | 2 × M6 tapped holes, one in each leg's foot on its axis (x ±60, z 0), 12 deep from the mounting face; drawn at the thread's minor diameter Ø4.9175 | derived: `python lib/build.py derive thread M6` (ISO 68-1 basic profile; ISO 965-1 clause 10, internal 6H: D1 4.9175 to 5.1475, D2 5.3505 to 5.4926; ISO 261 pitch 1; tap drill 5.0). M6 is this design's choice (a handle's usual fixing; the inventory's made_of is screw-iso4762 x2, a common part not built yet: the holes are modelled, the part placed later). The thread's helix is not drawn: the hole shows the minor diameter, the figure a tapped bore reads as |
| the door | the legs' feet, two Ø12 discs in the plane y = 0, 120 apart | design: a flat face of the door, drawer front or cover, with two Ø6.6 clearance holes at 120 pitch (ISO 273 medium, lib/standards/holes.csv) that are the host's. Position: with the host's Ø6.6 holes and M6 screws the two parts share T ≤ H − F = 0.6 (ASME Y14.5 fixed fastener: the host's clearance pattern and this tapped pattern together); this design takes Ø0.3 at MMC for its tapped pattern and leaves Ø0.3 to the host, a design choice written here, not a declared feature (features.csv kind `own`: no clearance hole of its own) |
| the hand | the grip bar, 12 × 12 in section, 30 clear of the mounting face, 120 between the legs | by hand; no pull force or load figure |

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| legs | Ø12 bright steel, 30 long (y 0 to 30), their axes at x ±60 | round bar a hand clears; 120 between the legs takes a gloved hand (about 100 across the knuckles) with room; 30 from the door leaves the fingers' room behind the grip; Ø12 leaves a 3.5 wall round the Ø4.9175 tapped bore |
| grip | 12 × 12 in section (y 30 to 42, z ±6), 136 long (x ±68) | the legs' diameter, so the grip's sides lie flush with the legs' extremes (one clean outline); 8 past each leg's axis, so the bar's end stands 2 past the leg's outer side and the leg's end face sits wholly on the grip's underside |
| tapped holes | M6, 12 deep (2 × the nominal diameter) from the foot, on the leg's axis | a thread engagement of 2 d in steel; the screw's length is the host's choice (its door thickness plus 12 or less) |
| load, pull force, finish | not claimed | no figure is on file for them and the element is not sized against a load; the layer M-SILVER shows bright steel, no grade or finish is claimed |

## Mechanism
None: the two legs and the grip are one fixed body, and the door, drawer or cover it moves is the host's node. behaviour.csv is
the header only (no terminal, no state, no pose). MOT-010 has nothing to sweep.

## Named nodes
None. Collider, an axis-aligned box: `pull` (the whole handle, x ±68, y 0 to 42, z ±6).

## Materials by layer
`M-SILVER` the legs and the grip (bright steel, one body).

## Decals (Blender)
"complexes.org" on the grip's front face (+y, y = 42), between the legs.

## Notes
No vendor names, part numbers or marks. No load or pull-force claim: no figure is on file for them and the element is not sized
against a load. Not drawn: the screws (placed later from screw-iso4762), the thread's helix (the tapped holes show their minor
diameter), the door and its clearance holes (the host's). No open figure: the thread's figures are derived from ISO 68-1 and
ISO 965-1 (on file, toolkit/derive.py), the host's holes are ISO 273's, and the rest are design choices. A handle is in
OPERATING.md 12's list of own designs and no dimensional standard for one is on file, so it is built as our own design with no
class values; a bow handle with through holes and nuts, a recessed (flush) pull, a folding handle or a machine-tool ball handle is
another version or another element.
The gate's fillet rule (fillet r 0.5 for a device, lib/toolkit/fillet.py): every free edge is 12 or longer (the grip's edges 12
and 136, the legs' circular edges Ø12), so no edge falls in the 1.5 to 2.5 range that reads under 90 % of its fillet volume
(mech-r4, r98); the legs' upper circular edges lie buried against the grip's underside and the tapped bores are inside the legs.
Gate note (mech-r92's lesson): the bounding box's extremes lie on the grip (x ±68, y 42, z ±6: an axis-aligned uncut box) and on
the legs' feet (y 0); no node is nested and nothing is tilted.

## Outputs (out/)
`handle.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r100, unattended, 2026-11-11) |
