#!/usr/bin/env python3
"""enc-fs-1524x1829x305: floor-standing two-door control cabinet, NEMA 12 / IP55, powder-coated steel, key lock, floor stand.
Every visible feature a product manual's CAD image shows; nothing internal (interior devices are their own elements, placed on
back-panel by an assembly BOM). The door-mounted operators are this element's own BOM rows (bom.csv), parent door-r.
The three M8 earth studs are port nodes since 1.9 (lib/requests/core/mech-earth-studs-2026-11-11.md, from the panel shop's request
panel-3 item 3): `pe-body` on the back wall's inner face, `pe-door-l` and `pe-door-r` on the doors' inner faces, children of their
doors (P.parents) so they swing with them; gender none (PIN-002); their torque NOT ON FILE (B) in behaviour.csv. Studs unchanged
in place and size, so 1.9 is a minor (nodes added, none moved)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, drawing as DR
from toolkit.prims import Prims

ID, VERSION, CLASS = "enc-fs-1524x1829x305", "1.9", "enclosure"
TITLE = "floor-standing two-door control cabinet 1524 x 1829 x 305, NEMA 12 / IP55, RAL 7035"
TOOLKIT = "1.3"
BASELINE = "60 x 72 x 12 in dust-tight floor-stand class (maker's catalogue drawing and STEP, references/source.txt; measured, not shipped)"
ORIGIN = "floor plane, front-left anchor hole of the left leg; doors face -y"
COMMAND = "ENC"
PARAMS = dict(swing_l=0.0, swing_r=0.0)

W, H, D = 1524.0, 1829.0, 305.0        # body outside, excluding legs and door returns
T = 1.9                                 # 14 ga sheet
LEG_H, LEG_W = 305.0, 206.0             # two full-depth channel legs, flush with the body sides
LEG_T, FOOT_FL = 3.0, 60.0              # leg sheet; anchor flange turned out at the floor
ANCHOR = 11.1                           # anchor hole, two per leg: 7/16 in (11.13, STEP read-back 2026-11-03; was 14)
DOOR_RET, DOOR_GAP, DOOR_T = 25.0, 3.0, 1.9
HINGE_T = 6.0
HANDLE = dict(w=25.0, h=210.0, d=28.0, z=1180.0, from_meeting=50.0)   # 3-point latch handle, right door
BACK_PANEL = (1372.0, 1676.0, 2.5)      # galvanised sub-panel on 25 mm studs
GLAND = (1050.0, 200.0, 2.0)            # removable gland plate in the floor of the body: opening and plate flange clear of the leg channels (1.5)
EYE_R = 22.0                            # lifting eye ring; bar centre 42 above the top
DOOR_MARGIN = 13.0                      # door inset from the body edge, top and bottom
LEG_X = [0.0, W - LEG_W]; Z0 = LEG_H
DW = (W - 3 * DOOR_GAP) / 2; DH = H - 2 * DOOR_MARGIN
FL = 30.0                               # door-frame flange

def body(P):
    for lx in LEG_X:
        P.box("M-STEEL-7035", lx, 0, 0, LEG_T, D, LEG_H); P.box("M-STEEL-7035", lx + LEG_W - LEG_T, 0, 0, LEG_T, D, LEG_H)
        P.box("M-STEEL-7035", lx, 0, 0, LEG_W, LEG_T, LEG_H); P.box("M-STEEL-7035", lx, D - LEG_T, 0, LEG_W, LEG_T, LEG_H)
        foot = P.box("M-STEEL-7035", lx, -FOOT_FL, 0, LEG_W, D + 2 * FOOT_FL, 6.0)
        for ay in (-FOOT_FL / 2, D + FOOT_FL / 2): P.hole("M-GASKET", (lx + LEG_W / 2, ay, -1.0), (lx + LEG_W / 2, ay, 7.0), ANCHOR / 2, foot)
    P.box("M-STEEL-7035", 0, D - T, Z0, W, T, H)                                                   # back
    P.host("wall-l", P.box("M-STEEL-7035", 0, 0, Z0, T, D, H), T); P.host("wall-r", P.box("M-STEEL-7035", W - T, 0, Z0, T, D, H), T)   # sides: ports mount through them
    P.box("M-STEEL-7035", 0, 0, Z0 + H - T, W, D, T)                                               # top
    gx, gy = (W - GLAND[0]) / 2, (D - GLAND[1]) / 2                                                # bottom around the gland opening
    P.box("M-STEEL-7035", 0, 0, Z0, gx, D, T); P.box("M-STEEL-7035", W - gx, 0, Z0, gx, D, T)
    P.box("M-STEEL-7035", gx, 0, Z0, GLAND[0], gy, T); P.box("M-STEEL-7035", gx, D - gy, Z0, GLAND[0], gy, T)
    P.host("gland-plate", P.box("node:gland-plate|M-GALV", gx - 15, gy - 15, Z0 - GLAND[2], GLAND[0] + 30, GLAND[1] + 30, GLAND[2]), GLAND[2])
    for i in range(4):
        for sy in (gy - 7, D - gy + 7):
            sx = gx - 7 + (GLAND[0] + 14) * (i / 3); P.cyl("M-ZINC", (sx, sy, Z0 - GLAND[2] - 3), (sx, sy, Z0 - GLAND[2]), 4.5)
    P.box("M-STEEL-7035", 0, 0, Z0, W, T, FL); P.box("M-STEEL-7035", 0, 0, Z0 + H - FL, W, T, FL)   # door frame flange and gasket
    P.box("M-STEEL-7035", 0, 0, Z0, FL, T, H); P.box("M-STEEL-7035", W - FL, 0, Z0, FL, T, H)
    P.box("M-GASKET", FL - 8, -2, Z0 + FL - 8, W - 2 * FL + 16, 2, 8); P.box("M-GASKET", FL - 8, -2, Z0 + H - FL, W - 2 * FL + 16, 2, 8)
    P.box("M-GASKET", FL - 8, -2, Z0 + FL, 8, 2, H - 2 * FL); P.box("M-GASKET", W - FL, -2, Z0 + FL, 8, 2, H - 2 * FL)
    bpx, bpz = (W - BACK_PANEL[0]) / 2, Z0 + (H - BACK_PANEL[1]) / 2                               # back panel on four studs
    bp = P.host("back-panel", P.box("node:back-panel|M-GALV", bpx, D - T - 25 - BACK_PANEL[2], bpz, BACK_PANEL[0], BACK_PANEL[2], BACK_PANEL[1]), BACK_PANEL[2])
    for sx in (bpx + 40, bpx + BACK_PANEL[0] - 40):
        for sz in (bpz + 40, bpz + BACK_PANEL[1] - 40):
            P.hole("M-GASKET", (sx, D - T - 24, sz), (sx, D - T - 25 - BACK_PANEL[2] - 1, sz), 5.5, bp)               # Ø11 stud hole (M10 clearance, ISO 273 medium) in the sub-panel (1.5)
            P.cyl("M-ZINC", (sx, D - T, sz), (sx, D - T - 25 - BACK_PANEL[2] - 6, sz), 5.0)
            P.cyl("M-ZINC", (sx, D - T - 25 - BACK_PANEL[2], sz), (sx, D - T - 25 - BACK_PANEL[2] - 8, sz), 8.5)
    for ex in (W * 0.25, W * 0.75):                                                                 # lifting eyes
        P.cyl("M-ZINC", (ex, D / 2, Z0 + H), (ex, D / 2, Z0 + H + 42), 9.0)                           # the eye's stem, up to the ring bar's centre (1.9: it stopped at +24, 12 short of the bar, GEO-070)
        P.cyl("M-ZINC", (ex, D / 2 - EYE_R, Z0 + H + 42), (ex, D / 2 + EYE_R, Z0 + H + 42), 6.0)
    P.cyl("node:pe-body|M-BRASS", (60, D - T, Z0 + 60), (60, D - T - 20, Z0 + 60), 4.0)             # earth stud, a port node (1.9): the body's bonding point
    P.pivot("pe-body", "port", (60, D - T - 20, Z0 + 60), axis=(0, -1, 0), range=(0, 0), unit="PE", gender="none")
    P.pivot("gland-plate", "translate", (gx - 15, gy - 15, Z0 - GLAND[2]), axis=(0, 0, -1), range=(0, 60))
    P.pivot("back-panel", "fixed", (bpx, D - T - 25 - BACK_PANEL[2], bpz))
    P.collider("body", 0, 0, Z0, W, D, H); P.collider("leg-l", LEG_X[0], -FOOT_FL, 0, LEG_W, D + 2 * FOOT_FL, LEG_H); P.collider("leg-r", LEG_X[1], -FOOT_FL, 0, LEG_W, D + 2 * FOOT_FL, LEG_H)

def door(P, name, hinge_x, swing_deg, handle, ops):
    """a door as oriented boxes about its hinge axis at (hinge_x, 0); swing_deg = 0 closed; the leaf opens outward (toward -y)"""
    s = 1 if name == "door-l" else -1
    th = -math.radians(swing_deg) * s; c, sn = math.cos(th), math.sin(th)                       # outward: the free edge moves toward -y (1.5: was inward)
    ex = (s * c, s * sn, 0); ey = (-sn, c, 0); ez = (0, 0, 1)
    o = (hinge_x, -DOOR_RET, Z0 + DOOR_MARGIN); L = f"node:{name}|M-STEEL-7035"
    skin = P.host(name, P.obox(L, o, ex, ey, ez, DW, DOOR_T, DH), DOOR_T)                       # door-mounted devices cut through the skin
    P.pivot(name, "rotate", (hinge_x, -DOOR_RET - 2, Z0 + DOOR_MARGIN), axis=(0, 0, 1), range=(0, -110 * s))  # +z axis: door-l opens clockwise (-), door-r anticlockwise (+), both outward (1.5)
    P.collider(name, min(hinge_x, hinge_x + s * DW), -DOOR_RET, Z0 + DOOR_MARGIN, DW, DOOR_RET + DOOR_T, DH)
    def off(dx, dy, dz): return (o[0] + ex[0] * dx + ey[0] * dy, o[1] + ex[1] * dx + ey[1] * dy, o[2] + dz)
    meet = DOOR_RET - 2.5 if handle else DOOR_RET                                                   # the active door's meeting return stops in front of the astragal (1.5)
    P.obox(L, off(0, 0, 0), ex, ey, ez, DOOR_T, DOOR_RET, DH); P.obox(L, off(DW - DOOR_T, 0, 0), ex, ey, ez, DOOR_T, meet, DH)
    P.obox(L, off(0, 0, 0), ex, ey, ez, DW, DOOR_RET, DOOR_T); P.obox(L, off(0, 0, DH - DOOR_T), ex, ey, ez, DW, DOOR_RET, DOOR_T)
    hn = "hinge-l" if s > 0 else "hinge-r"                                                          # the hinge pin is its own part (1.5)
    P.cyl(f"node:{hn}|M-ZINC", (hinge_x, -DOOR_RET - 2, Z0 + DOOR_MARGIN + 20), (hinge_x, -DOOR_RET - 2, Z0 + DOOR_MARGIN + DH - 20), HINGE_T / 2 + 1)
    P.pivot(hn, "fixed", (hinge_x, -DOOR_RET - 2, Z0 + DOOR_MARGIN + 20))
    if handle:
        hx = DW - HANDLE["from_meeting"] - HANDLE["w"] / 2
        hb = off(hx - HANDLE["w"] / 2, -HANDLE["d"], HANDLE["z"] - Z0 - DOOR_MARGIN - HANDLE["h"] / 2)
        P.obox("node:handle-1|M-ZINC", hb, ex, ey, ez, HANDLE["w"], HANDLE["d"], HANDLE["h"])
        P.pivot("handle-1", "rotate", off(hx, -HANDLE["d"], HANDLE["z"] - Z0 - DOOR_MARGIN + 60), axis=(ey[0], ey[1], 0), range=(0, 90))   # lever swings out about its top pin
        P.obox("node:handle-1|M-BLACK-PA", off(hx - 10, -HANDLE["d"] - 14, HANDLE["z"] - Z0 - DOOR_MARGIN - 70), ex, ey, ez, 20, 14, 140)
        ck = off(hx, -HANDLE["d"] - 1, HANDLE["z"] - Z0 - DOOR_MARGIN + 80); P.cyl("node:handle-1|M-BLACK-PA", ck, (ck[0] - ey[0] * 6, ck[1] - ey[1] * 6, ck[2]), 9.0)
        for zz in (DH - 60, 60): P.obox(f"node:{name}|M-ZINC", off(hx - 15, DOOR_RET - 8, zz - 6), ex, ey, ez, 30, 6, 12)   # door hardware swings with the door (1.5)
    else:
        P.obox(L, off(DW - DOOR_T, DOOR_RET - 2, DOOR_T + 0.5), ex, ey, ez, DOOR_T + DOOR_GAP + 15, 2, DH - 2 * DOOR_T - 1.0)   # astragal, clear of the active door's top / bottom returns (1.5)
        for zz in (DH - 60, 60): P.obox(f"node:{name}|M-ZINC", off(DW - 45, DOOR_RET - 8, zz - 6), ex, ey, ez, 30, 6, 12)
    P.obox(f"node:{name}|M-ZINC", off(80, DOOR_RET - 4, DH - 40), ex, ey, ez, 200, 4, 8)            # door stay
    pe = "pe-door-l" if s > 0 else "pe-door-r"                                                      # door earth stud, a port node (1.9), a child of the door
    P.cyl(f"node:{pe}|M-BRASS", off(50, DOOR_T, 60), off(50, DOOR_T + 18, 60), 4.0)
    P.pivot(pe, "port", off(50, DOOR_T + 18, 60), axis=(ey[0], ey[1], 0), range=(0, 0), unit="PE", gender="none")
    P.parents[pe] = name                                                                            # swings with its door, keeps its own pivot
    if ops and swing_deg == 0:                                                                      # BOM operators cut through the skin (closed-door frame)
        for row in ops: library.mount(P, row, skin, DOOR_T)

def build(swing_l=0.0, swing_r=0.0):
    P = Prims(); body(P)
    rows = library.own_bom(sys.modules[__name__])
    door(P, "door-l", DOOR_GAP, swing_l, False, [r for r in rows if r["parent"] == "door-l"])
    door(P, "door-r", W - DOOR_GAP, swing_r, True, [r for r in rows if r["parent"] == "door-r"])
    return P

def drawing(path):
    s = 0.12; g = []; fx, fy = 60, 92; floor = fy + (LEG_H + H) * s
    g.append(DR.R(fx, fy, W * s, H * s))
    for lx in LEG_X: g.append(DR.R(fx + lx * s, fy + H * s, LEG_W * s, LEG_H * s)); g.append(DR.R(fx + lx * s, floor - 18 * s, LEG_W * s, 18 * s))
    for dx0 in (DOOR_GAP, 2 * DOOR_GAP + DW): g.append(DR.R(fx + dx0 * s, fy + DOOR_MARGIN * s, DW * s, DH * s, "o2"))
    hx = W / 2 + DOOR_GAP / 2 + HANDLE["from_meeting"] + HANDLE["w"] / 2; hz = LEG_H + H - HANDLE["z"]
    g.append(DR.R(fx + (hx - HANDLE["w"] / 2) * s, fy + (hz - HANDLE["h"] / 2) * s, HANDLE["w"] * s, HANDLE["h"] * s, "o2"))
    for r in library.own_bom(sys.modules[__name__]): g.append(DR.C(fx + r["x"] * s, fy + (LEG_H + H - r["z"]) * s, 15 * s, "o2"))
    for ex in (W * 0.25, W * 0.75): g.append(DR.C(fx + ex * s, fy - EYE_R * s - 2, EYE_R * s))
    g.append(DR.dim_h(fx, fx + W * s, fy - 22, f"{W:.0f}", fy)); g.append(DR.dim_v(fy, fy + H * s, fx - 26, f"{H:.0f}", fx))
    g.append(DR.dim_v(fy + H * s, floor, fx - 26, f"{LEG_H:.0f}", fx)); g.append(DR.dim_h(fx + DOOR_GAP * s, fx + (DOOR_GAP + DW) * s, floor + 22, f"{DW:.0f}", fy + H * s))
    g.append(DR.T(fx + W * s / 2, floor + 44, "FRONT"))
    sx0 = fx + W * s + 90
    g.append(DR.R(sx0, fy, D * s, H * s)); g.append(DR.R(sx0 - DOOR_RET * s, fy + DOOR_MARGIN * s, DOOR_RET * s, DH * s, "o2"))
    g.append(DR.R(sx0 - (DOOR_RET + HANDLE["d"]) * s, fy + (LEG_H + H - HANDLE["z"] - HANDLE["h"] / 2) * s, HANDLE["d"] * s, HANDLE["h"] * s, "o2"))
    g.append(DR.R(sx0, fy + H * s, D * s, LEG_H * s)); g.append(DR.R(sx0 - FOOT_FL * s, floor - 18 * s, (D + 2 * FOOT_FL) * s, 18 * s))
    g.append(DR.dim_h(sx0, sx0 + D * s, fy - 22, f"{D:.0f}", fy)); g.append(DR.dim_h(sx0 - DOOR_RET * s, sx0, floor + 22, f"{DOOR_RET:.0f}", fy + H * s))
    g.append(DR.T(sx0 + D * s / 2, floor + 44, "SIDE"))
    tx, ty = fx, floor + 80
    g.append(DR.R(tx, ty, W * s, D * s))
    for lx in LEG_X: g.append(DR.R(tx + lx * s, ty - FOOT_FL * s, LEG_W * s, (D + 2 * FOOT_FL) * s, "h"))
    for ex in (W * 0.25, W * 0.75): g.append(DR.C(tx + ex * s, ty + D * s / 2, 9 * s))
    g.append(DR.dim_h(tx + LEG_W * s / 2, tx + (LEG_X[1] + LEG_W / 2) * s, ty + (D + 2 * FOOT_FL) * s + 22, f"{LEG_X[1] - LEG_X[0]:.0f} anchor centres", ty + D * s))
    g.append(DR.T(tx + W * s / 2, ty + D * s + 46, "TOP"))
    DR.page(path, max(sx0 + D * s + 60, 470), ty + D * s + 70, f"{ID} v{VERSION} · {TITLE} · mm",
           ["14 ga body and doors · 25 mm door returns · 13 mm door margins · continuous hinges · 3-point key-lock handle 50 from the meeting edge, 1180 above the floor",
            f"back panel {BACK_PANEL[0]:.0f} x {BACK_PANEL[1]:.0f} x {BACK_PANEL[2]:.1f} galv · gland plate {GLAND[0]:.0f} x {GLAND[1]:.0f} · two {LEG_W:.0f} wide channel legs, {LEG_H:.0f} high · door operators per bom.csv"], g)

PREVIEWS = [dict(name="closed front three-quarter", az=250, el=22), dict(name="rear three-quarter", az=60, el=22),
            dict(name="open doors 110 deg: back panel, gland plate, door hardware", az=262, el=18, params=dict(swing_l=110, swing_r=110)),
            dict(name="handle 3-point key-lock handle, right door", az=262, el=10, center=(W / 2 + HANDLE["from_meeting"] + 20, -40, HANDLE["z"]), height=420),
            dict(name="doorops door operators: E-stop, reset, power light at 1500", az=262, el=10, center=(W / 2 + 170, -40, 1500), height=420),
            dict(name="leg floor stand: channel leg, floor flange, anchor holes", az=240, el=25, center=(LEG_X[0] + LEG_W / 2, D / 2, 120), height=520)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
