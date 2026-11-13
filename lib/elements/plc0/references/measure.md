# plc0 · measure brief

Element `plc0`: the cell controller, OUR OWN element (EM 2026-11-03): a DIN-rail controller box, proposed 90 wide x 105 high x 60 deep with `led-run`, `led-fault`, one M12 D-coded Ethernet port, one M12 L-coded 24 V power port and a 22.5 mm rail clip. The manifest's open question (which controller) is answered by making plc0 our own: the Rockwell CompactLogix 5380 5069-L306ER file on disk (RESTRICTED licence) is a size-and-look reference only and nothing of it ships. plc-1 on rail-1 of pm-motor-starter (BOM, planned).

## Documents on file
- `references/datasheet.pdf`: Rockwell 5069-TD002O-EN-P (November 2023), 30 pages: features p. 4 ('Dimensions (HxWxD), approx 143.97 x 98.10 x 136.81 mm'), installation p. 5 ('DIN rail mount (horizontal mount only)', EN 50022 35 x 7.5 rail, RTB torque 0.4 N m, strip 12 mm), dimensions figure p. 7 and p. 11 (137.84, 123.00, 143.97, 136.81, 130.31, 101.66 / 101.7, 98.10 mm), minimum space p. 16 (50.8 mm above and below at 50 C).
- `references/5069-td001-compact-5000-io-specifications.pdf`: Compact 5000 I/O, 56 pages: spacing p. 3 (25.0 mm to the sides, 50.0 top / bottom), I/O module envelope p. 5 ('144.6 x 22 x 105.4 mm' per slot).
- `references/5069-L306ER-cutsheet.html`, `references/5069-L306ER-2d-10002334625.dwg`, `references/L3z_assem080116.zip`: the Rockwell page copy, 2-D and the family STEP as served.
- `model.step`: the L3z family STEP, 107 solids (reference only).

## Figures (mm)
| feature | mm | source |
|---|---|---|
| our box W x H x D (proposal) | 90 x 105 x 60 | EM 2026-11-03 ruling (the manifest's open question) |
| rail clip | 22.5 wide, EN 50022 35 x 7.5 | EM ruling; rail per TD002 p. 5 |
| reference controller H x W x D | 143.97 x 98.10 x 136.81 | TD002 p. 4, p. 7 |
| reference I/O module per slot | 144.6 x 22 x 105.4 | TD001 p. 5 |
| clearance around the box | 50.8 above / below, 25.0 sides | TD002 p. 16; TD001 p. 3 |
| LED window / M12 socket | NOT ON FILE (ours: Ø3 lens, M12 x 1 sockets 18 across the flange) | din.led() default r 1.6; port-m12-a brief |

## STEP read-back (Open CASCADE)
- model.step (reference only): 107 solids, 26323 faces, extents 101.655 x 149.94 x 137.113 mm (mm); against TD002: 98.10 vs 101.66 (3.6: the family model carries the RTB plugs), 143.97 vs 149.94 (6.0: the DIN latch tab), 136.81 vs 137.11 (0.3).
- Largest solids: the controller body 82.9 x 123.6 x 81.4 plus a 85.6 x 134.2 x 63.2 front, the 31.6 x 132.5 x 132.3 power section, a 21.2 x 124.3 x 127.0 end cap, the 98.2 x 123.0 x 26.7 top; two 18.8 x 99.7 x 15.9 RTBs.
- Used for the look (front face split into a status LED strip, a display window, the port block) and the rail-device proportions, not for any figure of our box.

## Mounting
35 mm rail (EN 50022, TD002 p. 5) by the 22.5 mm clip (din.rail_clip), rail-1 of the panel, between the 440R and the LioN-X-side ports; clearance 50.8 above and below (TD002 p. 16) is a layout rule for the BOM, not geometry.

## Build notes (own model)
- Box 90 x 105 x 60 (W x H x D) in M-GREY-PA with a darker front plate; rail clip 22.5 wide at the back (din.rail_clip); front face: `led-run` (green) and `led-fault` (red) lenses top-left (din.led), a label field (decal) below; bottom face: one M12 D-coded socket (Ethernet) and one M12 L-coded socket (24 V) at 27 pitch (the LioN-X pitch), each an 18 mm flange with the M12 x 1 socket; USB and SD slots as decals only.
- Carried ports: the two sockets are this element's own ports (not port-m12-a instances), declared with pivots kind port so the cables of connections.csv (panel-1.p-x1 -> ..., p-x2) can be routed to the panel wall ports from here in a later BOM.
- Datum: rail device.

## Origin
Rail device (README Conventions): back face on the rail crown y = 0, rail centreline z = 0, left edge x = 0, body toward -y.

## Named nodes
- `node:led-run`: green lens, kind emissive, 0 to 1 (controller RUN).
- `node:led-fault`: red lens, kind emissive, 0 to 1 (controller FAULT).
- `node:port-eth`: M12 D-coded socket, kind port, unit D.
- `node:port-pwr`: M12 L-coded socket, kind port, unit L.

## Ports
- `port-eth`: M12 D-coded 4-pin, 1 TD+, 2 RD+, 3 TD-, 4 RD- (as the LioN-X X01 / X02, io-block-m12-8di8do brief).
- `port-pwr`: M12 L-coded 5-pin, 1 US +24 V, 2 GND_UL, 3 GND_US, 4 UL +24 V, 5 FE (as the LioN-X X03 / X04).

## Decals
- Front label field: 'plc0' and the institute's tag (tag-plate kind=device, 30 x 12); 'RUN' / 'FAULT' beside the lenses; port labels 'ETH' / '24 V' at the sockets. No vendor name or logo (standing rule; the Rockwell reference is RESTRICTED).

## Status
Own element: the box figures are EM's ruling of 2026-11-03, not vendor figures; the reference STEP is on file and read back for proportion only; lens and socket figures from din.py and the port-m12-a brief. Stage 0 COMPLETE 2026-11-03 as a proposal; EM to confirm the 90 x 105 x 60 envelope before Stage 1.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
