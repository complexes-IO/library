#!/usr/bin/env python3
"""xfmr-control: single-phase control transformer, 250 VA, 480 V primary to 120 V secondary, open construction (core and coil),
screwed to the back panel by two mounting brackets. A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design
of the ETIM 10.0 class EC002486 "One-phase control transformer", built to the class values in spec.md "## Class values"; no maker's
datasheet (the vendor stub in the folder's references/ is reference only and was not opened; nothing of it is used).
What it meets comes from the standards and elements on file: the four panel-screw holes are ISO 273 medium clearance for M5
(lib/standards/holes.csv); the secondary terminals are a placed terminal-plug 2.0 (lib/inventory.csv made_of "terminal-plug"),
version pinned, on a header built to the plug's spec (pins 1.0 x 1.0, 5.0 past the mating face); every other size, the hole pattern
included, is a design choice, said so in spec.md. Not placed in 1.0 (OPERATING.md 12, quality at the source): screw-iso4762 x4 of
the inventory's made_of is not built, so the panel screws are the installer's and only their clearance holes are modelled.
Modelled as built: an E-I laminated core in the plane of the panel (two outer limbs, a centre limb twice their width, two yokes), one
coil on the centre limb (primary and secondary windings on one bobbin, not told apart), clamp bars on the yokes, the two brackets,
the primary terminal block (1U 1V screw clamps) on the upper clamp bar, the secondary header with its plug and the PE clamp block
(green-yellow) on the lower one.
1.1 (elec-r35): text only, geometry as 1.0. pins.csv t-PE's source says the bonding rule's standard is not on file (review elec-r27
finding 1)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "xfmr-control", "1.1", "device"
TITLE = "control transformer 250 VA, 1~ 480 V / 120 V, open, bracket mounted, screw-clamp primary, plug-in secondary (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic One-phase control transformer (ETIM 10.0 EC002486); class values in spec.md; panel-screw holes "
            "ISO 273 medium for M5 (lib/standards/holes.csv); the secondary terminals are a placed terminal-plug 2.0 element on a "
            "header built to its spec; sizes and the hole pattern are design choices; the primary and PE clamps' conductor range is "
            "open (spec.md)")
ORIGIN = "surface-mount device: back face (the brackets' flanges) y = 0, lower-left mounting hole x = 0, z = 0, body toward -y"
COMMAND = "XFMR1"
PARAMS = {}

# ---- core: an E-I stack of laminations in the x-z plane, stacked along y (design choices)
LIMB_O, LIMB_C, WINDOW, WIN_H, YOKE = 16.0, 32.0, 16.0, 48.0, 16.0   # outer limb, centre limb, window width and height, yoke height
STACK = (-71.0, -21.0)                                 # stack front and back faces (50 deep), 21 clear of the panel
X0, Z0 = 2.0, 15.0                                     # the core's lower-left corner from the origin (the lower-left hole)
CORE_W = 2 * LIMB_O + 2 * WINDOW + LIMB_C              # 96
CORE_H = WIN_H + 2 * YOKE                              # 80
# ---- the coil (design choice): a rectangular tube on the centre limb; both windings on one bobbin
GAP, BUILD, END = 1.0, 12.0, 5.0                       # bobbin gap to the limb, winding build, clearance to each yoke (the blocks sit 1.0 past it)
# ---- clamp bars, brackets and panel holes
BAR_T, BAR_IN = 3.0, 2.0                               # clamp bar thickness (y) and inset from the core's sides and yoke edges
BR_T, BR_X, FLANGE = 2.5, 10.0, 25.0                   # bracket sheet, its overhang past the core in x, flange height
HOLE_D, HOLE_IN, HOLE_Z = 5.5, 8.0, 15.0               # Ø5.5 = ISO 273 medium for M5; 8.0 in from the flange ends; 15.0 from the yoke face
# ---- terminal blocks (design choices) on the front clamp bars; the clamps' conductor range is open (spec.md)
PITCH, BLOCK_D, BLOCK_H, BLOCK_M = 16.0, 18.0, 18.0, 4.0   # screw-clamp pitch, block depth (y), block height (z), margin at each end
HEAD = dict(r=2.8, t=1.2, dz=7.0, entry=(5.0, 10.0, 0.5))
PRIMARY = ("1U", "1V")
# ---- the secondary: a header for terminal-plug 2.0 (2 poles) on the lower block; the plug placed on it, version pinned
PLUG = "2.0"
X2 = dict(poles=2, w=24.0)                             # the plug's tag; its block 24 wide
PIN_W, PIN_L = 1.0, 5.0                                # header pin 1.0 x 1.0, 5.0 past the mating face (terminal-plug 2.0 spec.md Dimensions)

def terminals(P, x0, marks, y_face, z_edge, up, target, r, t, dz, entry, mat="M-ZINC"):
    """screw clamps along x from x0 on a block's front face y_face: the head is the port node t-<mark>; the wire entry is a slot cut
    into the block's end face z_edge (the shape of the toolkit's din.terminal_row, with a named node per terminal; as xfmr-control-3ph)"""
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
    # ---------------- core (one material, the laminations): two yokes, two outer limbs, the centre limb
    C = "M-STEEL-7035"
    P.box(C, X0, yf, zb, CORE_W, T, YOKE)                                                   # bottom yoke
    P.box(C, X0, yf, zt - YOKE, CORE_W, T, YOKE)                                            # top yoke
    P.box(C, X0, yf, zb + YOKE, LIMB_O, T, WIN_H)                                           # left outer limb
    P.box(C, X0 + CORE_W - LIMB_O, yf, zb + YOKE, LIMB_O, T, WIN_H)                         # right outer limb
    lc = X0 + LIMB_O + WINDOW                                                               # the centre limb's left face (x 34)
    P.box(C, lc, yf, zb + YOKE, LIMB_C, T, WIN_H)                                           # centre limb
    # ---------------- the coil: a tube round the centre limb, through the window height less END at each yoke
    ox, oy = LIMB_C + 2 * (GAP + BUILD), T + 2 * (GAP + BUILD)
    cx0, cy0, cz0, ch = lc - GAP - BUILD, yf - GAP - BUILD, zb + YOKE + END, WIN_H - 2 * END
    k = P.box("M-CU", cx0, cy0, cz0, ox, oy, ch)
    P.cutbox("M-CU", lc - GAP, yf - GAP, cz0 - 1.0, LIMB_C + 2 * GAP, T + 2 * GAP, ch + 2.0, k)   # the bore round the limb
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
    # ---------------- terminal blocks on the front clamp bars: primary on top, the secondary header and PE below
    B = "M-GREY-PA"; yb_face = yf - BAR_T - BLOCK_D; cx = X0 + CORE_W / 2
    top_z1 = zt - BAR_IN; top_z0 = top_z1 - BLOCK_H                                         # z 75 ... 93, 1.0 above the coil
    w1 = len(PRIMARY) * PITCH + 2 * BLOCK_M
    tb = P.box(B, cx - w1 / 2, yb_face, top_z0, w1, BLOCK_D, BLOCK_H)
    terminals(P, cx - w1 / 2 + BLOCK_M, PRIMARY, yb_face, top_z1, True, tb, **HEAD)
    bot_z0 = zb + BAR_IN; bot_z1 = bot_z0 + BLOCK_H                                         # z 17 ... 35, 1.0 below the coil
    w2 = X2["w"]; wpe = PITCH + 2 * BLOCK_M
    x2 = cx - w2                                                                            # the secondary block x 26 ... 50, PE 50 ... 74
    P.box(B, x2, yb_face, bot_z0, w2, BLOCK_D, BLOCK_H)                                     # the header block (the plug's seat)
    plug_w = X2["poles"] * 5.0; px = x2 + (w2 - plug_w) / 2; pz = (bot_z0 + bot_z1) / 2     # the plug centred on the block, sockets' axis z 25
    for i in range(X2["poles"]):                                                            # header pins into the plug's sockets (its spec: 1.0 x 1.0, <= 5.0)
        hx = px + 5.0 * i + 2.5
        P.box("M-ZINC", hx - PIN_W / 2, yb_face - PIN_L, pz - PIN_W / 2, PIN_W, PIN_L, PIN_W)
    library.place(P, dict(element="terminal-plug", version=PLUG, tag="x2", parent="", x=px, y=yb_face, z=pz, yaw=0.0,
                          params=dict(poles=X2["poles"])))                                  # the secondary plug (placed element, pinned)
    pb = P.box("M-GREEN-YELLOW", x2 + w2, yb_face, bot_z0, wpe, BLOCK_D, BLOCK_H)           # PE block (green-yellow)
    terminals(P, x2 + w2 + BLOCK_M, ("PE",), yb_face, bot_z0, False, pb, **HEAD)
    # ---------------- rating plate on the coil's front
    yc = yf - GAP - BUILD
    P.box("M-WHITE-PA", cx - 18.0, yc - 0.1, cz0 + 5.0, 36.0, 0.1, ch - 10.0)
    P.collider("env", xl, yb_face - 16.0, zb - FLANGE, xr - xl, -(yb_face - 16.0), CORE_H + 2 * FLANGE)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="rear brackets and panel holes", az=60, el=20),
            dict(name="elevation core coil and terminal blocks", az=270, el=0),
            dict(name="side stack coil brackets and clamp bars", az=180, el=5),
            dict(name="primary terminals", az=230, el=40, center=(50, -90, 86), height=36),
            dict(name="secondary plug header and PE", az=230, el=-30, center=(50, -98, 26), height=40)]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
