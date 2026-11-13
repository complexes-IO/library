#!/usr/bin/env python3
"""plc0: the institute's controller as a physical box: DIN rail, RUN / FAULT lenses, one M12 D-coded Ethernet and one M12 L-coded
power socket on the bottom face. Our own design (manifest open question, 2026-11-03 proposal); no vendor shape.
1.2: PIN-002 (EM 2026-11-05; IEC 60204-1 13.4.5): both port pivots declare their gender as built, female (sockets). Review plc0-1.1
finding 3 (port-pwr male L, as io-block-m12-8di8do X03) is a node and geometry change, a 2.0, still open. DOC-006: no vendor name in BASELINE."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "plc0", "1.2", "device"
TITLE = "plc0 controller: DIN-rail box 90 x 105 x 60, RUN / FAULT, M12 Ethernet and power"
TOOLKIT = "1.3"
BASELINE = "own (EM 2026-11-03): 90 x 105 x 60, 35 mm rail; port pinouts as io-block-m12-8di8do X01 / X03; a reference controller on file (references/measure.md) sized only as a reference"
ORIGIN = "rail device: back face on the rail crown y = 0, rail centreline z = 0, left face x = 0, body toward -y"
COMMAND = "PLC0"
PARAMS = {}
W, H, D = 90.0, 105.0, 60.0

def build():
    P = Prims()
    P.box("M-GREY-PA", 0, -D + 3, -H / 2, W, D - 3, H)                                                 # housing
    P.box("M-BLACK-PC", 3, -D, -H / 2 + 3, W - 6, 3, H - 6)                                             # front plate
    din.rail_clip(P, W / 2 - 11.25, 22.5)
    din.led(P, "led-run", "M-LENS-GREEN", 12.0, -D, 38.0); din.led(P, "led-fault", "M-LENS-RED", 22.0, -D, 38.0)
    P.box("M-WHITE-PA", 10, -D - 0.2, -10, W - 20, 0.2, 30)                                             # label field: plc0, tag, RUN / FAULT (decal)
    for name, cx, unit, ring in (("port-eth", W / 2 - 13.5, "D", "M-GREEN"), ("port-pwr", W / 2 + 13.5, "L", "M-GREY-PA")):
        P.cyl("M-ZINC", (cx, -D / 2, -H / 2), (cx, -D / 2, -H / 2 - 12.6), 6.75)                         # M12 socket on the bottom face
        P.cyl(f"node:{name}|{ring}", (cx, -D / 2, -H / 2 - 12.8), (cx, -D / 2, -H / 2 - 12.0), 5.0)      # coding insert 0.2 proud of the socket rim (GEO-050)
        P.pivot(name, "port", (cx, -D / 2, -H / 2 - 12.6), axis=(0, 0, -1), range=(0, 0), unit=unit, gender="female")   # PIN-002: sockets, as built
    P.collider("env", 0, -D, -H / 2 - 12.6, W, D + 7.5, H + 12.6)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="bottom M12 sockets", az=250, el=-30)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
