#!/usr/bin/env python3
"""reactor-line-3p-4a: three-phase line reactor (a net reactance coil on a drive's supply side), 4 A a line, 480 V, 50 / 60 Hz,
7.35 mH a phase (uk 4 %), open construction, screwed to the back panel by two mounting brackets. A generic element
(OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002563 "Coil for low-voltage", built to
the class values in spec.md "## Class values"; no maker's datasheet. What it meets comes from the standards on file: the four
panel-screw holes are ISO 273 medium clearance for M5 (lib/standards/holes.csv); their pattern, and every other size, is a design
choice, said so in spec.md. Modelled as built, in xfmr-control-3ph 1.2's form: a three-limb laminated core in the plane of the
panel, one coil on each limb, clamp bars on the yokes, the two brackets, the line-side terminal block on the upper clamp bar and
the load-side block (with PE) on the lower one.
1.0 (elec-r60): first build."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "reactor-line-3p-4a", "1.0", "device"
TITLE = "three-phase line reactor 4 A, 480 V, 50/60 Hz, 7.35 mH (uk 4 %), open, bracket mounted, screw terminals (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Coil for low-voltage (ETIM 10.0 EC002563); class values in spec.md; panel-screw "
            "holes ISO 273 medium for M5 (lib/standards/holes.csv); sizes and the hole pattern are design choices; the terminals' "
            "conductor range is open (spec.md)")
ORIGIN = "surface-mount device: back face (the brackets' flanges) y = 0, lower-left mounting hole x = 0, z = 0, body toward -y"
COMMAND = "REACTOR3"
PARAMS = {}

# ---- core: three limbs and two yokes of laminations in the x-z plane, stacked along y (design choices)
LIMB, WINDOW, WIN_H, YOKE = 20.0, 16.0, 44.0, 20.0     # limb width, window width, window height, yoke height
STACK = (-51.0, -21.0)                                 # stack front and back faces (30 deep), 21 clear of the panel
X0, Z0 = 2.0, 15.0                                     # the core's lower-left corner from the origin (the lower-left hole)
CORE_W = 3 * LIMB + 2 * WINDOW                         # 92
CORE_H = WIN_H + 2 * YOKE                              # 84
# ---- coils (design choices): a rectangular tube on each limb
GAP, BUILD, END = 1.0, 6.0, 2.0                        # bobbin gap to the limb, winding build, clearance to each yoke
# ---- clamp bars, brackets and panel holes
BAR_T, BAR_IN = 3.0, 2.0                               # clamp bar thickness (y) and inset from the core's sides and yoke edges
BR_T, BR_X, FLANGE = 2.5, 10.0, 25.0                   # bracket sheet, its overhang past the core in x, flange height
HOLE_D, HOLE_IN, HOLE_Z = 5.5, 8.0, 15.0               # Ø5.5 = ISO 273 medium for M5; 8.0 in from the flange ends; 15.0 from the yoke face
# ---- terminal blocks (design choices) on the front clamp bars; the conductor range is open (spec.md)
PITCH, BLOCK_D, BLOCK_M = 16.0, 18.0, 4.0              # terminal pitch, block depth (y), margin at each end
HEAD = dict(r=2.8, t=1.2, dz=7.0, entry=(5.0, 10.0, 0.5))
LINE = ("1U1", "1V1", "1W1")                           # from the supply
LOAD = ("1U2", "1V2", "1W2")                           # to the drive

def terminals(P, x0, marks, y_face, z_edge, up, target, r, t, dz, entry, mat="M-ZINC"):
    """screw clamps along x from x0 on a block's front face y_face: the head is the port node t-<mark>; the wire entry is a slot cut
    into the block's end face z_edge (xfmr-control-3ph 1.2's function: the shape of the toolkit's din.terminal_row, with a named
    node per terminal)"""
    s = 1 if up else -1
    for i, mk in enumerate(marks):
        cx = x0 + PITCH * (i + 0.5); cz = z_edge - s * dz; n = f"t-{mk}"
        P.cyl(f"node:{n}|{mat}", (cx, y_face, cz), (cx, y_face - t, cz), r)
        P.pivot(n, "port", (cx, y_face - t, cz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")   # PIN-002: a screw clamp
        w, d, sl = entry; z0 = z_edge - (sl if up else 0.0)
        P.cutbox("M-GASKET", cx - w / 2, y_face + 2.0, z0 - (0.0 if up else 1.0), w, d, sl + 1.0, target)       # out past the end face
        P.box("M-GASKET", cx - w / 2, y_face + 2.0, z0, w, d, sl)                                               # the dark slot in its cut

def build():
    P = Prims(); yf, yb = STACK; T = yb - yf
    zb, zt = Z0, Z0 + CORE_H                                                                # core bottom and top
    # ---------------- core (one material, the laminations)
    C = "M-STEEL-7035"
    P.box(C, X0, yf, zb, CORE_W, T, YOKE)                                                   # bottom yoke
    P.box(C, X0, yf, zt - YOKE, CORE_W, T, YOKE)                                            # top yoke
    limbs = [X0 + i * (LIMB + WINDOW) for i in range(3)]
    for lx in limbs: P.box(C, lx, yf, zb + YOKE, LIMB, T, WIN_H)                            # three limbs
    # ---------------- coils: a tube round each limb, through the window height less END at each yoke
    for lx in limbs:
        ox, oy = LIMB + 2 * (GAP + BUILD), T + 2 * (GAP + BUILD)
        cx0, cy0, cz0, ch = lx - GAP - BUILD, yf - GAP - BUILD, zb + YOKE + END, WIN_H - 2 * END
        k = P.box("M-CU", cx0, cy0, cz0, ox, oy, ch)
        P.cutbox("M-CU", lx - GAP, yf - GAP, cz0 - 1.0, LIMB + 2 * GAP, T + 2 * GAP, ch + 2.0, k)   # the bore round the limb
    # ---------------- clamp bars on the yokes, front and back (steel flats)
    G = "M-GALV"; bx0, bw = X0 + BAR_IN, CORE_W - 2 * BAR_IN; bzh = YOKE - 2 * BAR_IN
    for z in (zb + BAR_IN, zt - YOKE + BAR_IN):
        P.box(G, bx0, yf - BAR_T, z, bw, BAR_T, bzh)                                         # front
        P.box(G, bx0, yb, z, bw, BAR_T, bzh)                                                 # back
    # ---------------- mounting brackets: a web on each yoke's end face, a flange on the panel with two holes
    xl, xr = X0 - BR_X, X0 + CORE_W + BR_X
    web_y0 = yf + 2.0                                                                       # the web stops 2.0 short of the core's front
    P.box(G, xl, web_y0, zb - BR_T, xr - xl, -BR_T - web_y0, BR_T)                          # lower web, under the bottom yoke
    P.box(G, xl, web_y0, zt, xr - xl, -BR_T - web_y0, BR_T)                                 # upper web, on the top yoke
    lo = P.box(G, xl, -BR_T, zb - FLANGE, xr - xl, BR_T, FLANGE)                            # lower flange (on the panel)
    hi = P.box(G, xl, -BR_T, zt, xr - xl, BR_T, FLANGE)                                     # upper flange
    for f, z in ((lo, zb - HOLE_Z), (hi, zt + HOLE_Z)):
        for x in (xl + HOLE_IN, xr - HOLE_IN):
            P.hole("M-GASKET", (x, 0.5, z), (x, -BR_T - 0.5, z), HOLE_D / 2, f)              # M5 panel screw, ISO 273 medium
    # ---------------- terminal blocks on the front clamp bars: line side on top, load side below with PE beside it
    B = "M-GREY-PA"; yb_face = yf - BAR_T - BLOCK_D; cx = X0 + CORE_W / 2
    top_z0, top_z1 = zt - YOKE + BAR_IN, zt - BAR_IN
    w1 = len(LINE) * PITCH + 2 * BLOCK_M
    tb = P.box(B, cx - w1 / 2, yb_face, top_z0, w1, BLOCK_D, top_z1 - top_z0)
    terminals(P, cx - w1 / 2 + BLOCK_M, LINE, yb_face, top_z1, True, tb, **HEAD)
    bot_z0, bot_z1 = zb + BAR_IN, zb + YOKE - BAR_IN
    w2 = len(LOAD) * PITCH + 2 * BLOCK_M; wpe = PITCH + 2 * BLOCK_M
    x2 = cx - (w2 + wpe) / 2
    sb = P.box(B, x2, yb_face, bot_z0, w2, BLOCK_D, bot_z1 - bot_z0)
    terminals(P, x2 + BLOCK_M, LOAD, yb_face, bot_z0, False, sb, **HEAD)
    pb = P.box("M-GREEN-YELLOW", x2 + w2, yb_face, bot_z0, wpe, BLOCK_D, bot_z1 - bot_z0)  # PE block (green-yellow)
    terminals(P, x2 + w2 + BLOCK_M, ("PE",), yb_face, bot_z0, False, pb, **HEAD)
    # ---------------- rating plate on the middle coil's front
    mid = limbs[1] + LIMB / 2; yc = yf - GAP - BUILD
    P.box("M-WHITE-PA", mid - 12.0, yc - 0.1, zb + YOKE + 9.0, 24.0, 0.1, 26.0)
    lo_x = min(xl, X0 - GAP - BUILD)
    P.collider("env", lo_x, yb_face - HEAD["t"], zb - FLANGE, xr - lo_x, -(yb_face - HEAD["t"]), CORE_H + 2 * FLANGE)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear brackets and panel holes", az=60, el=20),
            dict(name="elevation core coils and terminal blocks", az=270, el=0),
            dict(name="side stack coils brackets and clamp bars", az=180, el=5),
            dict(name="line terminals", az=230, el=40, center=(48, -70, 90), height=30),
            dict(name="load terminals and PE", az=230, el=-30, center=(48, -70, 25), height=30)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
