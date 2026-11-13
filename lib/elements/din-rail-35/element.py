#!/usr/bin/env python3
"""din-rail-35: 35 x 7.5 top-hat mounting rail to EN 60715 (TH35-7.5), slotted, zinc-plated steel, cut to length, with end clamps
and panel screws. The slots are real openings in the mesh (the crown is built as two strips and bridges), so the glTF shows them
without booleans; AutoCAD gets the same solids."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, drawing as DR
from toolkit.prims import Prims

ID, VERSION, CLASS = "din-rail-35", "1.1", "rail"
TITLE = "35 x 7.5 top-hat DIN rail, EN 60715 TH35-7.5, slotted, zinc-plated steel, cut to length"
TOOLKIT = "1.3"
BASELINE = "EN 60715 TH35-7.5 section; slot pattern 6.2 x 18 at 25 pitch (the common perforated rail)"
ORIGIN = "back face (on the panel), centre of the first slot: rail runs +x, its 35 mm height is along z, crown toward -y"
COMMAND = "RAIL"
PARAMS = dict(length=1000.0, clamps=True, fix_pitch=200.0)

RW, RH, T = 35.0, 7.5, 1.0            # overall height (along z), depth (crown off the panel), sheet
CROWN = 27.0                           # crown width (outer); flanges (RW - CROWN) / 2 = 4 each side
SLOT = dict(w=6.2, l=18.0, pitch=25.0, first=12.5)   # slot: 6.2 across (z), 18 along (x), 25 pitch, first centre 12.5 from the end
CLAMP = dict(w=8.0, h=35.0, d=14.0)    # screw-type end clamp, grey PA, M4 screw on top
SCREW = dict(r=4.5, h=3.0)             # M5 pan head through a slot into the panel

def build(length=1000.0, clamps=True, fix_pitch=200.0):
    P = Prims(); L = float(length); x0 = -SLOT["first"]; zc = 0.0
    n = int((L - 2 * SLOT["first"]) // SLOT["pitch"]) + 1             # slots that fit
    ends = [x0 + SLOT["first"] + i * SLOT["pitch"] for i in range(n)]   # slot centres
    # flanges on the panel (y in [-T, 0]) and webs up to the crown
    P.box("M-GALV", x0, -T, -RW / 2, L, T, (RW - CROWN) / 2); P.box("M-GALV", x0, -T, CROWN / 2, L, T, (RW - CROWN) / 2)      # flanges z = ±(13.5..17.5)
    P.box("M-GALV", x0, -RH, -CROWN / 2, L, RH, T); P.box("M-GALV", x0, -RH, CROWN / 2 - T, L, RH, T)                           # webs at z = ±13.5
    # crown at y in [-RH, -RH + T]: two strips either side of the slot row, bridges between slots, and the two end pieces
    sw = SLOT["w"] / 2
    P.box("M-GALV", x0, -RH, -CROWN / 2, L, T, CROWN / 2 - sw); P.box("M-GALV", x0, -RH, sw, L, T, CROWN / 2 - sw)
    xs = x0
    for c in ends:
        P.box("M-GALV", xs, -RH, -sw, c - SLOT["l"] / 2 - xs, T, 2 * sw); xs = c + SLOT["l"] / 2
    P.box("M-GALV", xs, -RH, -sw, x0 + L - xs, T, 2 * sw)
    # panel screws through slots at fix_pitch (nearest slot), head on the crown
    k = max(1, int(round(fix_pitch / SLOT["pitch"])))
    for c in ends[::k]: P.cyl("M-ZINC", (c, -RH, zc), (c, -RH - SCREW["h"], zc), SCREW["r"])
    P.collider("env", x0, -CLAMP["d"], -RW / 2, L, CLAMP["d"], RW)
    if clamps:
        for cx in (x0 + 2.0, x0 + L - 2.0 - CLAMP["w"]):
            P.box("M-GREY-PA", cx, -CLAMP["d"], -CLAMP["h"] / 2 + 0.1, CLAMP["w"], CLAMP["d"] - 0.1, CLAMP["h"] - 0.2)   # 0.1 inside the rail's edges and off the mounting plane (GEO-050)
            P.cyl("M-ZINC", (cx + CLAMP["w"] / 2, -CLAMP["d"] + 4, CLAMP["h"] / 2), (cx + CLAMP["w"] / 2, -CLAMP["d"] + 4, CLAMP["h"] / 2 + 2.5), 3.0)
    return P

def drawing(path):
    s = 0.5; g = []; fx, fy = 70, 90; L = 300.0                     # front: a 300 mm sample
    g.append(DR.R(fx, fy, L * s, RW * s)); g.append(DR.Ln(fx, fy + 4 * s, fx + L * s, fy + 4 * s, "o2")); g.append(DR.Ln(fx, fy + 31 * s, fx + L * s, fy + 31 * s, "o2"))
    n = int((L - 25) // 25) + 1
    for i in range(n):
        c = fx + (12.5 + 25 * i) * s; g.append(DR.R(c - 9 * s, fy + (17.5 - 3.1) * s, 18 * s, 6.2 * s, "o2"))
    g.append(DR.dim_h(fx + 12.5 * s, fx + 37.5 * s, fy - 22, "25 pitch", fy)); g.append(DR.dim_v(fy, fy + RW * s, fx - 22, "35", fx))
    g.append(DR.dim_h(fx, fx + 12.5 * s, fy + RW * s + 24, "12.5", fy + RW * s)); g.append(DR.T(fx + L * s / 2, fy + RW * s + 48, "FRONT · slots 6.2 x 18 at 25 pitch · cut to length"))
    sx0 = fx + L * s + 80; S = 4.0                                    # section, 4x
    pts = [(-17.5, 0), (-13.5, 0), (-13.5, 7.5), (13.5, 7.5), (13.5, 0), (17.5, 0)]
    g.append('<polyline points="' + " ".join(f"{sx0 + (x + 17.5) * S:.1f},{fy + 60 - y * S:.1f}" for x, y in pts) + '" class="o"/>')
    g.append(DR.dim_h(sx0, sx0 + 35 * S, fy - 22, "35", fy + 60)); g.append(DR.dim_h(sx0 + 4 * S, sx0 + 31 * S, fy + 60 + 24, "27", fy + 60))
    g.append(DR.dim_v(fy + 60 - 7.5 * S, fy + 60, sx0 + 35 * S + 26, "7.5", sx0 + 35 * S)); g.append(DR.T(sx0 + 17.5 * S, fy + 60 + 48, "SECTION · EN 60715 TH35-7.5 · 1.0 sheet"))
    DR.page(path, sx0 + 35 * S + 80, fy + 60 + 70, f"{ID} v{VERSION} · {TITLE} · mm", ["zinc-plated steel · end clamps 8 wide, grey PA, M4 screw · M5 pan-head panel screws through slots at fix_pitch"], g)

PREVIEWS = [dict(name="front three-quarter, 1000 mm", az=250, el=20), dict(name="section end clamp and slots", az=240, el=25, center=(0, -4, 0), height=90),
            dict(name="short 300 mm cut", az=250, el=20, params=dict(length=300))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
