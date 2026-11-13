#!/usr/bin/env python3
"""port-m12-a: M12 bulkhead port, A / D / L coded, rear mount by default, pigtail stub. Brief: references/measure.md
(18.0 flange, SW17 nut, Ø13.5 front, 22.6 rear body, M16 x 1.5 panel thread). 1.1: the front is a receptacle-m12 (sleeve, coded insert,
contacts, seal) placed as this element's own port node; `gender` female (sockets, the default: a supply side stays touch-safe) or male.
1.4: receptacle-m12 1.3: the female insert is the foremost face (Open CASCADE, round 4), so it stands 12.6 in front of the flange
(drawing p. 1) and is the mating plane; the receptacle's body runs back to the nut. A male uses the same mating plane, its threaded
sleeve standing 8.9 further out (Assumption)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "port-m12-a", "1.4", "connector"
TITLE = "M12 bulkhead socket A / D / L coded, M16 x 1.5 panel thread, rear mount, pigtail"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet: a panel-mount M12 receptacle (references/measure.md; 2-D drawing p. 1: 18.0 flange, SW17, Ø13.5, 22.6 behind the panel); IEC 61076-2-101"
ORIGIN = "cut-out centre class: panel hole centre on the wall's front face y = 0, socket toward -y, rear body toward +y"
COMMAND = "PM12"
CUTOUT = 16.5
PARAMS = dict(coding="A", mount="rear", panel_t=1.9, pigtail=150.0, gender="female", conditions="")
FACE = -15.6                                       # the mating plane: the foremost face, 12.6 in front of the flange (drawing p. 1)

def build(coding="A", mount="rear", panel_t=1.9, pigtail=150.0, gender="female", conditions=""):
    P = Prims()
    def hexa(L, y0, y1, af):
        r = af / math.sqrt(3); pts = [(r * math.cos(math.pi / 3 * i + math.pi / 6), r * math.sin(math.pi / 3 * i + math.pi / 6)) for i in range(6)]
        P.mesh(L, SW.sweep([(0, y0, 0), (0, y1, 0)], pts))
    if mount == "rear":
        hexa("M-ZINC", 0, -3.0, 17.0)                                                      # nut on the front face
        P.cyl("M-ZINC", (0, panel_t, 0), (0, panel_t + 3.0, 0), 9.0)                         # flange inside
    else:
        P.cyl("M-ZINC", (0, 0, 0), (0, -3.0, 0), 9.0); hexa("M-ZINC", panel_t, panel_t + 3.0, 17.0)
    rcp = library.load("receptacle-m12")
    library.place(P, dict(element="receptacle-m12", version="1.6", tag="self", parent="", x=0, y=FACE, z=0, yaw=0.0,
                          params=dict(gender=gender, coding=coding, conditions=conditions, length=-3.0 - FACE)))   # IS this port's node self; its Ø13.5 body runs to the nut
    P.cyl("M-BLACK-PC", (0, panel_t + 3.0, 0), (0, 22.6, 0), 7.0)                           # rear body
    P.mesh("M-CABLE-PUR", SW.sweep(SW.resample([(0, 22.6, 0), (0, 22.6 + pigtail * 0.6, 0), (0, 22.6 + pigtail * 0.8, -pigtail * 0.2)], 6.0), SW.circle_profile(2.5, 10)))
    ahead = rcp.front(gender, coding)                                                        # the female front face, or the male sleeve
    P.collider("env", -9, FACE - ahead, -9, 18, 22.6 - FACE + ahead, 18)
    return P

PREVIEWS = [dict(name="front three-quarter A-coded", az=250, el=20), dict(name="rear body and pigtail", az=60, el=20), dict(name="D-coded", az=250, el=20, params=dict(coding="D")),
            dict(name="male A-coded", az=250, el=20, params=dict(gender="male"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
