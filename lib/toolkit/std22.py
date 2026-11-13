"""The 22.5 mm operator standard (IEC 60947-5-1 cut-out) shared by the op-*-22 elements: dimensions, the parts every operator has.
An operator's local frame: origin at the cut-out centre ON the panel's front face; the panel lies in the plane y = 0 and extends toward
+y (its thickness); the operator's bezel and cap are at y < 0 (toward the person), the latch and contact blocks at y > panel_t.
The host cuts the Ø22.5 hole through its own panel (library.mount does it); the operator cuts holes only through its own parts."""
CUTOUT = 22.5
BEZEL = dict(r=14.85, proud=3.0)                 # Ø29.7 ring, 3 proud of the face it sits on
CAP = dict(r=10.75, travel=4.0)                  # Ø21.5 flush cap
LENS = dict(r=11.0, dome=6.0)                    # Ø22 domed lens
LEGEND = dict(w=30.0, h=50.0, t=1.0)             # legend plate under the operator (text is a decal)
LATCH = dict(r=15.0, h=8.0)                      # Ø30 mounting latch behind the panel
BLOCK = dict(w=22.0, d=30.0, h=25.0)             # contact / lamp block, two terminal screws
PANEL_RANGE = (1.0, 6.0)                         # panel thickness the operators clamp: NOT ON FILE (Assumption: 800F / 3SU1 class 1 to 6)
ESTOP = dict(r=20.0, h=24.0, collar_r=16.0, collar_h=6.0, plate=(60.0, 60.0, 1.5))   # Ø40 mushroom on a Ø32 × 6 collar, 60 × 60 yellow plate

def behind(P, panel_t, blocks, bore=None):
    """latch and contact blocks behind the panel (+y side); bore: the latch's plunger bore radius (pushbuttons)"""
    y0 = panel_t
    lt = P.cyl("M-BLACK-PA", (0, y0, 0), (0, y0 + LATCH["h"], 0), LATCH["r"])
    if bore: P.hole("M-GASKET", (0, y0 - 1, 0), (0, y0 + LATCH["h"] + 1, 0), bore, lt)
    for b in range(blocks):
        z0 = -BLOCK["h"] / 2 - b * (BLOCK["h"] + 1)
        P.box("M-BLACK-PA", -BLOCK["w"] / 2, y0 + LATCH["h"], z0, BLOCK["w"], BLOCK["d"], BLOCK["h"])
        for tx in (-6, 6): P.cyl("M-ZINC", (tx, y0 + LATCH["h"] + BLOCK["d"], z0 + BLOCK["h"] / 2 + 4), (tx, y0 + LATCH["h"] + BLOCK["d"] + 1.5, z0 + BLOCK["h"] / 2 + 4), 2.2)

def legend(P):
    """legend plate on the panel face, with its own Ø22.5 hole; returns the y of its front face"""
    lp = P.box("M-BLACK-PA", -LEGEND["w"] / 2, -LEGEND["t"], -LEGEND["h"] * 0.65, LEGEND["w"], LEGEND["t"], LEGEND["h"])
    P.hole("M-GASKET", (0, -LEGEND["t"] - 1, 0), (0, 1, 0), CUTOUT / 2, lp)
    return -LEGEND["t"]

def bezel(P, yf, inner_r):
    """Ø29.7 bezel ring standing `proud` off the face at yf, bored to inner_r"""
    bz = P.cyl("M-ZINC", (0, yf, 0), (0, yf - BEZEL["proud"], 0), BEZEL["r"])
    P.hole("M-GASKET", (0, yf + 1, 0), (0, yf - BEZEL["proud"] - 1, 0), inner_r, bz)
    return bz
