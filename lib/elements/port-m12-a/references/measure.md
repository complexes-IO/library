# port-m12-a · measure brief

Element `port-m12-a`: M12 panel receptacle (bulkhead), female, with pigtail, coding A / D / L as a parameter. The panel wall carries these ports (README discipline 0): p-x1 (D, Ethernet), p-x2 (L, 24 V power), p-x3 (A, E-stop chain) on the right wall of pm-motor-starter. EM's list asks for a REAR-mount receptacle; the AutomationDirect file on disk is the FRONT-mount Murrelektronik 7231-13561-9720100 (A-coded 5-pin, 1 m pigtail): it is the size-and-look baseline only, the mounting style is our own.

## Documents on file
- `references/dimensional-drawing.pdf`: AutomationDirect 2-D drawing 7231-13561-9720100, one page (p. 1), title 'RECEPTACLE, M12 FEMALE, 5-POLE, 1.0m (3.3ft) WIRES, 22 AWG, FRONT MOUNT'; figures (mm [in], read from the drawing 2026-11-02): dia 18.0 [0.71] flange / nut, SW17 hex (17.0 across flats), dia 13.5 [0.53] front body, 22.6 [0.89] behind the panel face, M12 x 1 front thread, M16 x 1.5 panel thread.
- `references/7231-13561-9720100-2d.dwg`: the same drawing as DWG.
- `references/datasheet.pdf`: AutomationDirect cutsheet, one page (p. 1): 'Bulkhead', 'M12 female with female threads 5-wire/5-pin', pigtail 1 m 22 AWG, nylon 12, nickel-plated die-cast zinc, IP67, 'Includes Mounting nut(s)', UL E224242.
- `references/source.txt`: page verification; the mounting-style difference recorded.
- `model.step`: AutomationDirect STEP (mm), 1 solid.

## Figures (mm)
| feature | mm | source |
|---|---|---|
| flange / nut diameter | 18.0 | 2-D drawing p. 1 |
| hex across flats | 17.0 | 2-D drawing p. 1 (SW17) |
| front body diameter | 13.5 | 2-D drawing p. 1 |
| panel thread | M16 x 1.5 | 2-D drawing p. 1 (panel hole Ø16.5 class, NOT ON FILE as a figure) |
| mating thread | M12 x 1 | 2-D drawing p. 1; IEC 61076-2-101 |

## Spacings (not size-checked)
Distances between features, not the size of any one solid, so the gate's size check (STEP overall / per-solid sizes) cannot find them. The element holds them in its constants; figures.md checks them against the vendor STEP each round (decision, round 7 prompt).
- length behind the panel face: 22.6 (2-D drawing p. 1)
- overall length: 42.6 (STEP read-back (the drawing gives the rear length only))
- pigtail: 1000, 22 AWG, 5 wires (cutsheet p. 1)

## STEP read-back (Open CASCADE)
- model.step: 1 solid, 156 faces, extents 18.0 x 18.0 x 42.6 mm (mm); datasheet check 17.0 exact (hex), 18.0 exact (flange).
- Single solid 18.0 x 18.0 x 42.6 with its axis along z in the vendor pose (-30.0 to +12.6: 12.6 in front of the flange, 30.0 behind including the pigtail stub); the pigtail wires are not in the model.
- AutoCAD 2026 import VERIFIED, extents match.

## Mounting
Vendor part: front mount through an M16 x 1.5 panel hole, nut behind (drawing title; cutsheet 'Includes Mounting nut(s)'). Our element: REAR mount (EM's list): the body sits behind the wall, the M16 thread passes through the hole, the nut tightens on the front face; the flange then lies inside the panel. Same hole, reversed stack; the dimensions above hold either way.

## Build notes (own model)
- Parametric: `coding` = A / D / L (the keyway and pin count differ inside the socket only; the envelope is the same M12 x 1 / M16 x 1.5 body), `pigtail` length, `mount` = rear (default) / front.
- Body: Ø13.5 front socket 12.6 long with the M12 x 1 thread modelled as a plain cylinder; Ø18.0 flange; SW17 hex nut 17.0 across flats; rear body 22.6 behind the panel; pigtail as a `cordset-m12` style sweep or a stub.
- Socket face: 5 pin holes on the A-coded pattern (IEC 61076-2-101) as a decal, not holes; D- and L-coded faces by the same rule.
- Datum: the panel hole centre on the wall face; the socket looks outward (-y of the wall).

## Origin
Cut-out centre class (README Conventions): the panel hole centre on the wall's front face y = 0, socket toward -y; the rear body extends to +y behind the wall. The host (enc-fs wall) cuts the Ø16.5 hole through `library.mount`.

## Named nodes
- `node:self` = the socket (the thing a cordset plugs into), kind port: extras `kind=port, coding=<A|D|L>, unit=<A|D|L>` so the twin matches a cable end to the port; no motion.
- No lamp, nothing moves.

## Ports
- The element is a port: M12 female, pins by coding: A-coded 1 = +24 V, 2 = Ch. B, 3 = GND, 4 = Ch. A, 5 = FE (as the LioN-X I/O ports, io-block-m12-8di8do brief); D-coded 1 TD+, 2 RD+, 3 TD-, 4 RD-; L-coded 1 US +24 V, 2 GND_UL, 3 GND_US, 4 UL +24 V, 5 FE (io-block-m12-8di8do brief, manual p. 32 / 33 / 35).
- Mates `cordset-m12` (male end) on the outside, pigtail to the terminal strip inside.

## Decals
- Port label beside the hole (p-x1 / p-x2 / p-x3) on the wall, from the assembly BOM tags; coding colour ring: A black, D green, L grey (the LioN-X manual's colour coding p. 32 / 33 / 34).

## Status
Figures VERIFIED (2 of 2 on the drawing exact; rear length 22.6 and front 12.6 read from the drawing and the STEP); rear-mount stack is our own ruling, not a vendor figure; licence AutomationDirect REVIEW. Stage 0 COMPLETE 2026-11-03.

---
2026-11-03. Stage 0 of lib/element-qa-checklist.txt: identity, documents on file with page numbers, figure table (mm, document and page per figure), Open CASCADE per-solid read-back of the vendor STEP, mounting, build notes, origin per the README convention, named nodes (kind and range), ports (pinout), decals, status. 'NOT ON FILE' marks a figure no document on disk gives; nothing is guessed.
