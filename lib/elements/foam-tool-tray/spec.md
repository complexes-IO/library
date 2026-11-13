# foam-tool-tray · v1.0 · shadow-foam insert 865 × 555 × 50 for a cabinet-tool 1.1 drawer, blank, two finger notches

**What** A shadow-foam tool insert for one drawer of the tool cabinet (lib/machines-factory.txt line 80: the cabinet-tool system
places cabinet-tool, tb-rollcab, hardware-cabinet and foam-tool-tray). One foam block that lies on the drawer tray's bottom and
fills its plan, with two finger notches at the front edge to lift it out. The block is blank: the tools' pockets are not cut.
**Class** furniture · **Baseline** our own design (OPERATING.md 12, own designs; lib/inventory.csv marks foam-tool-tray own_design
"yes", "shadow-foam tool tray for a drawer"). No product was matched and no vendor file was opened. The plan is sized to
cabinet-tool's drawer tray; every other size is a design choice.
**Units / frame** mm, Z up. Origin: the block's underside z = 0 at its front-left corner, x = 0, y = 0; the front face toward −y,
as cabinet-tool's drawers open. In a cabinet-tool drawer node the origin sits at (17.5, 0, the tray bottom's top face).
**Built with** toolkit 1.3 · AutoLISP command `FOAMTRAY` · no parameters.

## Mechanism
None: one fixed body, no node. It moves with the drawer it lies in (cabinet-tool's `drawer-1` .. `drawer-5`), which is the
drawer's node, not this element's. behaviour.csv is header only.

## What it meets (figures from files on hand)
| what | figure | from |
|---|---|---|
| cabinet-tool 1.1 (the drawer tray it lies in) | the tray's inside 869 wide (x 15.5 to 884.5 in the drawer) and 558.5 deep (y 0, the drawer front's back face, to 558.5); the lowest inside height 118.5 (the two 150 fronts: sides 20 below the front's top, bottom 10 above its lower edge, 1.5 sheet) | cabinet-tool/element.py (W, T, SIDE_CLR, TRAY_D, TRAY_T, FRONTS), read by library.load, so the two cannot drift apart |

Nothing else on file. tb-rollcab's drawer trays are smaller (649 × 418.5 inside): this block doesn't fit them; a tb-rollcab size
is a later variant. Which tools a drawer holds is the system's choice and is not on file; no hand-tool element (wrenches,
screwdrivers, pliers) is built, and the one tool element on file, tool-dmm, is not placed by this block. So no tool's outline is
cut: a host doesn't model a cut-out for a part it doesn't place (OPERATING.md 12). Each tool's pocket is cut in a later version
once the tools a drawer holds are on file, or by the user in the blank foam.

## Its own sizes (design choices)
| item | value | why |
|---|---|---|
| block | 865 × 555 (x 0 to 865, y 0 to 555) | the tray's inside less 2 each side and 3.5 at the back: a design choice, so the block drops in and lifts out |
| thickness | 50 (z 0 to 50) | a design choice, under the lowest tray's 118.5 inside height, so one block suits every drawer of cabinet-tool |
| finger notches | 2, each 100 wide (x), 40 into the block from the front face (y 0 to 40), 30 deep from the top (z 20 to 50), centred at x 216.25 and 648.75 (the front edge's quarter points) | a design choice: two fingers' room to lift the block out of the tray |
| tool pockets | none | the tools a drawer holds are not on file (above) |

## Named nodes
None. Collider `foam`: the block's envelope.

## Materials by layer
`M-BLACK-PA` the foam block (the library's black layer; the layer name only: the foam is not polyamide, and lib/materials.csv has
no foam layer).

## Notes
No load rating, no material grade and no safety claim. The volume is 23 763 750 mm³ (the block 24 003 750 less the two notches
2 × 120 000; written as volume only: no foam density is on file, so no mass is stated). No vendor names, no label.

## Outputs (out/)
`foam-tool-tray.lsp` · `.glb` · `preview-*.png`. Terminal: dwg/, step/, gltf/ from the gates.

## History
| version | change |
|---|---|
| 1.0 | first build, our own design (mech-r73, unattended) |
