#!/usr/bin/env python3
"""terminal-plug: pluggable terminal block (the plug half), screw clamps, 5.0 mm pitch, poles by parameter (2 ... 12, built with 4).
A generic element (OPERATING.md 12, EM 2026-11-07): our own vendor-neutral design of the ETIM 10.0 class EC002021 "Terminal block
connector", built to the class values in spec.md "## Class values"; no maker's datasheet. A common part (lib/inventory.csv: part of 22
devices): a host carries the header the plug's sockets take and places this element on it, version pinned.
Every size is a design choice, said so in spec.md: no standard on file fixes a plug's pitch or body (IEC 60999, the clamps' standard, is
not on file); the clamps' conductor range is open (spec.md, NOT ON FILE (B)); the header's pin size is the host's and open too.
Modelled from the outside in: one housing; per pole a screw well on the front face with the clamp screw (port node t-<n>), a wire entry
in the bottom face, a socket in the mating face (port node s-<n>), and a pull grip along the top; the clamp cages and the
contact springs inside are not modelled.
2.0 (elec-r26, review elec-r22 finding 1 / terminal-plug-1.0 finding 1): the joint gets a depth. Each socket is open 6.0 deep from
the mating face (the engagement depth, a design choice) with its 0.5 dark floor at the bottom (open 5.5), so a host's 1.0 x 1.0 header
pin can enter up to 5.0 (0.5 short of the floor) without touching the plug. A cut-out change, so a major (OPERATING.md 7)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library
from toolkit.prims import Prims

ID, VERSION, CLASS = "terminal-plug", "2.0", "device"
TITLE = "pluggable terminal block, plug with screw clamps, 5.0 mm pitch, 4 poles (2 to 12 by parameter), 12 A 250 V (complexes.org generic)"
TOOLKIT = "1.3"
BASELINE = ("our own design: generic Terminal block connector (ETIM 10.0 EC002021); class values in spec.md; sizes are design choices; "
            "the clamps' conductor range and the header's pin are open (spec.md)")
ORIGIN = ("mating face on the host's header y = 0, body toward -y (away from the host), left face x = 0, poles along +x, "
          "z = 0 on the sockets' axis")
COMMAND = "TERMPLUG"
PARAMS = dict(poles=4)
POLES = (2, 12)                      # the poles a host may ask for (design choice; class value 9 / 13)

# ---- housing (design choices; spec.md Dimensions)
PITCH = 5.0                          # pole pitch along x (class value 11: width = poles x pitch)
D = 16.0                             # depth: mating face y = 0 to front face y = -16
Z0, Z1 = -6.0, 8.0                   # bottom (wire entries) and top (grip) faces of the housing
# ---- per pole (design choices)
WELL = (3.6, 3.0, 3.6, 3.5)          # screw well in the front face: width (x), depth (y), height (z), centre z
SCREW_R, SCREW_T = 1.5, 0.6          # clamp screw head Ø3.0 x 0.6, at the well's floor
ENTRY = (3.2, 3.2, -10.5, 0.5)       # wire entry in the bottom face: width (x), length (y), centre y, depth of the dark slot
SOCKET = (2.0, 2.0, 6.0, 0.5)        # socket in the mating face: width (x), height (z), engagement depth (y), dark floor at its bottom; centred on z = 0
HEADER_PIN = (1.0, 5.0)              # the host's header pin this socket takes: square side, longest free length past the mating face (the socket is open 5.5
                                     # above its 0.5 floor; the pin ends 0.5 short of the floor, so it touches nothing of the plug)
GRIP = (4.0, 1.5)                    # pull grip along the top at the front: depth (y), height above the top face

def build(poles=4):
    n = int(poles)
    if not POLES[0] <= n <= POLES[1]: raise ValueError(f"terminal-plug: poles {n} outside {POLES[0]} ... {POLES[1]} (spec.md Class values 9)")
    P = Prims(); G = "M-GREEN"; W = n * PITCH
    body = P.box(G, 0, -D, Z0, W, D, Z1 - Z0)                                                  # housing
    gd, gh = GRIP
    P.box(G, 0, -D, Z1, W, gd, gh)                                                             # pull grip along the top front edge
    ww, wd, wh, wz = WELL; ew, el, ey, et = ENTRY; sw, sh, sd, sf = SOCKET
    for k in range(1, n + 1):
        cx = PITCH * (k - 0.5)
        # screw well and the clamp screw at its floor: the port node t-<k> (a screw clamp, PIN-002 gender none)
        P.cutbox("M-GREEN", cx - ww / 2, -D - 1.0, wz - wh / 2, ww, wd + 1.0, wh, body)      # well, open to the front face
        yf = -D + wd                                                                           # the well's floor
        P.cyl(f"node:t-{k}|M-ZINC", (cx, yf, wz), (cx, yf - SCREW_T, wz), SCREW_R)
        P.pivot(f"t-{k}", "port", (cx, yf - SCREW_T, wz), axis=(0, -1, 0), range=(0, 0), unit="screw", gender="none")
        # wire entry in the bottom face: the dark slot in its cut (the toolkit's terminal_row shape, din.py)
        P.cutbox("M-GASKET", cx - ew / 2, ey - el / 2, Z0 - 1.0, ew, el, et + 1.0, body)
        P.box("M-GASKET", cx - ew / 2, ey - el / 2, Z0, ew, el, et)
        # socket in the mating face, open sd deep, its dark floor at the bottom: the port node s-<k> (it takes the header's pin: gender female, PIN-002)
        P.cutbox("M-GASKET", cx - sw / 2, -sd, -sh / 2, sw, sd + 1.0, sh, body)
        P.box(f"node:s-{k}|M-GASKET", cx - sw / 2, -sd, -sh / 2, sw, sf, sh)
        P.pivot(f"s-{k}", "port", (cx, 0.0, 0.0), axis=(0, 1, 0), range=(0, 0), unit="pin", gender="female")
    P.collider("env", 0, -D, Z0, W, D, Z1 + gh - Z0)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=20),
            dict(name="mating face and sockets", az=60, el=15),
            dict(name="wire entries from below", az=230, el=-40),
            dict(name="two poles", az=250, el=20, params=dict(poles=2)),
            dict(name="twelve poles", az=250, el=20, params=dict(poles=12))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
