#!/usr/bin/env python3
"""pbs-6h-22: six-hole 22.5 mm pushbutton station, horizontal, IP66, die-cast body and lid, RAL 7035. The operators it carries are
BOM rows (bom.csv): each row is a cut-out on the lid face, so changing the station's fit-out is editing the BOM, not this file."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, drawing as D
from toolkit.prims import Prims

ID, VERSION, CLASS = "pbs-6h-22", "1.7", "station"
TRIANGLES = 20000                      # five male M12 receptacles: threaded sleeves and contacts (port-m12-a 1.4); the class budget is 9000
TITLE = "six-hole 22.5 mm pushbutton station, horizontal, IP66, die-cast, RAL 7035"
TOOLKIT = "1.3"
BASELINE = "six-hole die-cast station class (AutomationDirect / Rockwell 800F-6H, measured, not shipped); operators per the 22.5 mm standard"
ORIGIN = "back face, lower-left mounting hole; body extends toward -y (toward the student)"
COMMAND = "PBS"
PARAMS = {}

N, PITCH, CUT = 6, 50.0, 22.5                  # holes, pitch, cut-out
BOX = dict(w=340.0, h=90.0, d=50.0, t=3.0)     # back box, wall
LID = dict(d=22.0, t=3.0)                       # lid depth, wall; 1.5 larger than the box all round, its skirt sits on the rim gasket
MOUNT = dict(inset=10.0, hole=5.5)              # four mounting holes through the back
GLAND = dict(r=14.0, h=10.0)                    # M20 on the bottom face, 40 from the left end
SCREW = dict(r=3.0, h=1.5)                      # four captive lid screws
W, H, D0, T = BOX["w"], BOX["h"], BOX["d"], BOX["t"]; DL = LID["d"]; FACE = -(D0 + DL); OV = 1.5
X0, Z0 = -MOUNT["inset"], -MOUNT["inset"]       # the box's lower-left corner
CZ = Z0 + H / 2                                 # operator centre line

def build():
    P = Prims()
    body = P.box("M-ALU-7035", X0, -D0, Z0, W, D0, H)                                           # 1.6: the die-cast box is one solid,
    P.cutbox("M-GASKET", X0 + T, -D0 - 1.0, Z0 + T, W - 2 * T, D0 - T + 1.0, H - 2 * T, body)      # hollowed (back and walls T thick)
    for mx in (0.0, W - 2 * MOUNT["inset"]):
        for mz in (0.0, H - 2 * MOUNT["inset"]): P.hole("M-GASKET", (mx, 1.0, mz), (mx, -T - 1.0, mz), MOUNT["hole"] / 2, body)
    end_l = end_r = body                                                                            # the M12 ports go through its end walls
    gw, gy = 2.0, -D0 - 1.5                                                                         # rim gasket: a ring on the wall tops (1.2: was a solid plate)
    P.box("M-GASKET", X0 + 0.5, gy, Z0 + 0.5, gw, 1.5, H - 1); P.box("M-GASKET", X0 + W - 0.5 - gw, gy, Z0 + 0.5, gw, 1.5, H - 1)
    P.box("M-GASKET", X0 + 0.5 + gw, gy, Z0 + 0.5, W - 1 - 2 * gw, 1.5, gw); P.box("M-GASKET", X0 + 0.5 + gw, gy, Z0 + H - 0.5 - gw, W - 1 - 2 * gw, 1.5, gw)
    L = "node:lid-1|M-ALU-7035"
    SK = DL - LID["t"] - 1.5                                                                        # skirt ends on the gasket (1.2: ran 4 into the walls)
    lidface = P.box(L, X0 - OV, FACE, Z0 - OV, W + 2 * OV, LID["t"] + SK, H + 2 * OV)              # 1.6: the lid is one solid, face and skirt,
    P.cutbox("M-GASKET", X0 - OV + LID["t"], FACE + LID["t"], Z0 - OV + LID["t"], W + 2 * OV - 2 * LID["t"], SK + 1.0, H + 2 * OV - 2 * LID["t"], lidface)   # hollowed
    for sx in (X0 + 8, X0 + W - 8):
        for sz in (Z0 + 8, Z0 + H - 8): P.cyl("node:lid-1|M-ZINC", (sx, FACE, sz), (sx, FACE - SCREW["h"], sz), SCREW["r"])
    P.cyl("M-ZINC", (X0 + 40, -D0 / 2, Z0), (X0 + 40, -D0 / 2, Z0 - GLAND["h"]), GLAND["r"]); P.cyl("M-BLACK-PA", (X0 + 40, -D0 / 2, Z0 - GLAND["h"]), (X0 + 40, -D0 / 2, Z0 - GLAND["h"] - 6), 9.0)
    P.pivot("lid-1", "translate", (X0, FACE, Z0), axis=(0, -1, 0), range=(0, 30))
    P.collider("env", X0 - OV, FACE - 32, Z0 - OV - 16, W + 2 * OV, D0 + DL + 32, H + 2 * OV + 16)
    walls = {"lid-1": (lidface, LID["t"]), "end-r": (end_r, T), "end-l": (end_l, T)}
    for row in library.own_bom(sys.modules[__name__]):                      # operators on the lid, M12 ports through the end walls: one cut-out per BOM row
        if row["parent"] == "lid-1": assert abs(row["y"] - FACE) < 1e-6 and abs(row["z"] - CZ) < 1e-6, row
        panel, t = walls[row["parent"]]
        library.mount(P, row, panel, t)
    return P

def drawing(path):
    s = 1.6; g = []; fx, fy = 70, 90; rows = library.own_bom(sys.modules[__name__])
    g.append(D.R(fx, fy, W * s, H * s)); g.append(D.R(fx + 3 * s, fy + 3 * s, (W - 6) * s, (H - 6) * s, "o2"))
    for r in rows:
        cx = fx + (r["x"] - X0) * s; cy = fy + H / 2 * s; es = r["element"] == "op-estop-22-2nc"
        g.append(D.C(cx, cy, CUT / 2 * s, "h")); g.append(D.C(cx, cy, (20.0 if es else 14.85) * s))
        g.append(D.R(cx - 30 * s, cy - 30 * s, 60 * s, 60 * s, "o2") if es else D.R(cx - 15 * s, cy - 50 * 0.65 * s, 30 * s, 50 * s, "o2"))
        g.append(D.T(cx, fy + H * s + 14, r["tag"], extra='style="font-size:7px"'))
    for mx in (10, W - 10):
        for mz in (10, H - 10): g.append(D.C(fx + mx * s, fy + mz * s, 2.75 * s, "h"))
    g.append(D.dim_h(fx, fx + W * s, fy - 22, f"{W:.0f}", fy)); g.append(D.dim_v(fy, fy + H * s, fx - 22, f"{H:.0f}", fx))
    g.append(D.dim_h(fx + 45 * s, fx + 95 * s, fy + H * s + 34, f"{PITCH:.0f} pitch", fy + H / 2 * s))
    g.append(D.dim_h(fx + 10 * s, fx + (W - 10) * s, fy + H * s + 56, f"{W - 20:.0f} mounting centres", fy + (H - 10) * s))
    g.append(D.T(fx + W * s / 2, fy + H * s + 80, "FRONT · cut-outs Ø22.5 at 50 pitch · mounting holes 4 × Ø5.5, position Ø0.5 (MMC) to A, the back face"))
    sx0 = fx + W * s + 70; depth = D0 + DL
    g.append(D.R(sx0, fy, depth * s, H * s)); g.append(D.Ln(sx0 + D0 * s, fy, sx0 + D0 * s, fy + H * s, "o2"))
    g.append(D.R(sx0 - 3 * s, fy + (H / 2 - 14.85) * s, 3 * s, 29.7 * s, "o2")); g.append(D.R(sx0 - 30 * s, fy + (H / 2 - 20) * s, 30 * s, 40 * s, "o2"))
    g.append(D.R(sx0 + (D0 - 40 - GLAND["r"]) * s, fy + H * s, 2 * GLAND["r"] * s, GLAND["h"] * s, "o2"))
    g.append(D.dim_h(sx0, sx0 + depth * s, fy - 22, f"{depth:.0f}", fy)); g.append(D.dim_h(sx0 - 30 * s, sx0, fy + H * s + 34, "30", fy + H / 2 * s))
    g.append(D.T(sx0 + depth * s / 2, fy + H * s + 80, "SIDE"))
    D.page(path, sx0 + depth * s + 60, fy + H * s + 100, f"{ID} v{VERSION} · {TITLE} · mm",
           [" · ".join(f"{r['tag']} = {r['element']} {r['version']}" for r in rows), "legend plates 30 x 50 · E-stop on a 60 x 60 yellow plate · M20 gland"], g)

PREVIEWS = [dict(name="front three-quarter", az=250, el=20), dict(name="back box, mounting holes, gland", az=60, el=25),
            dict(name="estop E-stop head and plate, pilot lights", az=255, el=12, center=(X0 + 45 + 3.5 * PITCH, FACE - 10, CZ), height=110),
            dict(name="caps start, stop, reset: bezels, flush caps, legend plates", az=255, el=12, center=(X0 + 45 + PITCH, FACE - 10, CZ), height=110)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
