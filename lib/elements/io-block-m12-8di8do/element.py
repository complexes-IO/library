#!/usr/bin/env python3
"""io-block-m12-8di8do: 8DI/8DO multiprotocol I/O block, 8 M12 A-coded ports, 2 D-coded Ethernet, 2 L-coded power, die-cast IP67.
1.1: every port is a receptacle-m12 in a pocket of the body (real sleeve, insert, socket or pin contacts, seal): a cable's pins meet
these contacts, and a contact's condition is a parameter (conditions="x1:2:spread").
1.5 (the maker's STEP read with Open CASCADE, round 5): the housing face 17.6 off the back (1.4 built 30.7, every port 13.1 too far
out); the face as measured: the ports at x ±15, power X03 / X04 at the FE end, Ethernet X01 / X02 next, X1 to X4 / X5 to X8 numbered
from the far end; each port clocked as on the part; 16 channel LEDs and a row of 7 status LEDs; the three rotary switches with no
cover, a round cap beside them; FE an M4 threaded hole in the power-end lug; the mounting slots; 13 clip-in label plates.
1.6 (round 6): no lug face: the housing face runs to both ends, cut by three pockets at the power end (the first slot's seat and the
FE's seat at 10.0 off the back, the label plate's pocket at 13.4) and one at the far end, each as measured; X04 clocked -45.0°.
Not modelled: the R5 roll-over of the face into the end faces (the gate's rounds stand for it) and the back face's 1.0 recess (against
the mounting surface).
1.7: receptacle-m12 1.6 (X03's key tolerance against the cordset female's new recess: 1.759°).
1.8 (elec-r25): text only, geometry as 1.7. The maker's and product names out of BASELINE (DOC-006: they live in references/);
the mounting pattern's position tolerance declared in features.csv (GDT-010; Assumption (B), spec.md); behaviour.csv.
1.9 (elec-r32): text only, geometry as 1.8. COMMAND IOBLOCK8 (the old command named the maker's product family: review
io-block-m12-8di8do-1.8 finding 1, an ESCAPE of DOC-006); the input ON level class B in spec.md as in behaviour.csv; every bare
NOT ON FILE in spec.md, the brief and behaviour.csv classed.
1.10 (elec-r33): text only, geometry as 1.9. spec.md's Behaviour list names the sensor supply's short-circuit protection as a
class A open figure, as behaviour.csv's us-bus row does, so DOC-005 counts it (review io-block-m12-8di8do-1.9 finding 1).
Brief: references/measure.md; the face layout: the round-5 figures (figures.md 4.1)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, din, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "io-block-m12-8di8do", "1.10", "device"
TITLE = "8DI/8DO IP67 I/O block, 8 x M12 A-coded, 2 x M12 D-coded Ethernet, 2 x M12 L-coded power"
TOOLKIT = "1.3"
BASELINE = "maker's datasheet (references/measure.md: techdata p. 1-4: 60 x 31 x 200, 2-hole M4 mount; manual p. 12 / 20 / 26 / 32 / 33 / 35 / 39 / 159 pinouts, FE, switches, LEDs; the STEP read with Open CASCADE, rounds 4 and 5)"
ORIGIN = "frame device: back face on the mounting surface y = 0, first mounting hole x = 0, z = 0; body toward -y, length along +z"
COMMAND = "IOBLOCK8"                                # 1.9: a neutral name (the old one named the maker's product family, DOC-006)
PARAMS = dict(conditions="")
X0, X1_, Z0, Z1, T = -29.79, 29.79, -4.5, 195.3, 17.6   # body (OCC): x ±29.79, z -4.50 to 195.30, housing face 17.6 off the back
HOLES = 190.5                                      # the mounting pattern (drawing): the screws; the far slot's centre is 191.05 (OCC)
SLOT = dict(w=4.5, l=6.0, far=191.05)              # mounting slots 4.5 x 6.0: across x at the first hole, along z at the far one
SEAT = 10.0                                        # the screw and FE seats 10.0 off the back (OCC, round 6: 9.7 was the slots' chamfer start)
SEATS = [(0.0, 0.504, 5.0, 4.92, 5.92), (20.0, 0.504, 4.5, 4.43, 5.42)]
                                                   # power-end seats, open at the end (OCC face wires, round 6): (x, arc centre z, arc R,
                                                   # half-width where the side meets the arc, half-width at z -4.30); the sides lean 10°
FAR_SEAT = (0.0, 190.303, 4.5)                     # far seat: an R4.5 arc, its sides leaning 10° out toward the far end
LABEL_POCKET = dict(x=(-25.70, -2.56), z=4.80, floor=13.4)   # the power-end label plate's pocket, its floor 13.4 off the back
M12_R = 6.75                                       # the bore each receptacle's body sits in, flush with the housing face (Assumption: hidden)
GENDER = {"x03": "male"}                           # power IN a male L-coded connector, power OUT and the rest sockets (manual p. 32-34; STEP agrees)
TRIANGLES = 30000                                  # 12 receptacles with their bodies and contacts, 23 LEDs, 13 label plates (class budget 12000)
# (name, coding, x, z, clocking): clocking is the key's angle looking at the housing face, clockwise from the far end (+z) (OCC)
PORTS = [("x1", "A", -15.0, 174.0, 0.0), ("x2", "A", -15.0, 147.0, 0.0), ("x3", "A", -15.0, 120.0, 0.0), ("x4", "A", -15.0, 93.0, 0.0),
         ("x5", "A", 15.0, 174.0, -90.0), ("x6", "A", 15.0, 147.0, -90.0), ("x7", "A", 15.0, 120.0, -90.0), ("x8", "A", 15.0, 93.0, -90.0),
         ("x01", "D", -15.0, 39.0, 0.0), ("x02", "D", 15.0, 39.0, -89.6), ("x03", "L", -15.0, 12.0, 45.0), ("x04", "L", 15.0, 12.0, -45.0)]
LED = dict(r=1.8, proud=0.1, dz=3.0, x=5.0)        # Ø3.6 lenses 0.1 proud; channel A at port z + 3 (yellow), B at z - 3 (white), x ±5
STATUS = [("led-p1", "M-LENS-GREEN"), ("led-p2", "M-LENS-GREEN"), ("led-dia", "M-LENS-RED"), ("led-bf", "M-LENS-RED"),
          ("led-s5", "M-LENS-WHITE"), ("led-ul", "M-LENS-GREEN"), ("led-us", "M-LENS-GREEN")]
                                                   # z 77.8, x -17.4 to 17.4 at 5.8: P1 / P2 Lnk/Act, MS/DIA, NS/BF, the 5th (name and
                                                   # colour NOT ON FILE: a clear lens), U_L, U_S (techdata p. 1 drawing read by eye; manual p. 159 / 160)
SWITCH = dict(z=66.2, x=(("x100", -20.7), ("x10", -6.9), ("x1", 6.9)), r=3.05, bore=3.15, pocket=(3.6, 1.3, 4.0), slot=(0.6, 1.2))
CAP = dict(x=20.7, z=66.2, r=6.15, gap=0.2, deep=1.5)   # a round cap Ø12.3 flush with the face: what it covers is NOT ON FILE; the
                                                   # 0.2 ring round it stands for its edge groove (Assumption)
FE = dict(x=20.0, z=0.5)                           # M4 threaded hole through the power-end lug (manual p. 26; drawing), modelled plain
PLATES = [(12.7, 24.2), (-12.7, 24.2), (12.7, 51.2), (-12.7, 51.2), (12.7, 105.2), (-12.7, 105.2), (12.7, 132.2), (-12.7, 132.2),
          (12.7, 159.2), (-12.7, 159.2), (15.0, 185.2), (-15.0, 185.2), (-15.6, 0.7)]   # 13 clip-in label plates (OCC; techdata: 15x)
PLATE = dict(base=(19.9, 7.95), top=(19.24, 7.29), seat=1.0)

def _port(P, body, name, coding, cx, cz, clock, conditions):
    """a receptacle-m12 flush in the housing face, clocked as on the part: the port node port-<name> with its insert and contacts"""
    rcp = library.load("receptacle-m12"); g = GENDER.get(name, "female"); f = rcp.face(g, coding)
    P.hole("M-GASKET", (cx, -T - 1.0, cz), (cx, -T + 9.0, cz), M12_R, body)
    library.place(P, dict(element="receptacle-m12", version="1.6", tag=f"port-{name}", parent="", x=cx, y=-T - f, z=cz, yaw=0.0, roll=clock,
                          params=dict(gender=g, coding=coding, conditions=conditions.get(name, ""), length=f + 9.0)))

def _beside(P, a, b, depth, y0, y1, target):
    """cut the strip `depth` wide on the right-hand side of the line a -> b (points (x, z); normal (dz, -dx)), from y0 to y1"""
    dx, dz = b[0] - a[0], b[1] - a[1]; L_ = math.hypot(dx, dz); n = (dz / L_, 0.0, -dx / L_); ez = (dx / L_, 0.0, dz / L_)
    P.cut("M-GASKET", (a[0], y0, a[1]), n, (0, 1, 0), ez, depth, y1 - y0, L_, target)

def _seat(P, body, x, zc, R, w_top, w_end, toward):
    """a screw seat open at the body's end (toward -1: the power end, +1: the far end): an arc of R about (x, zc) and two sides
    leaning 10°, down to SEAT"""
    y0, y1 = -T - 1.0, -SEAT; z_end = (Z0 - 1.0) if toward < 0 else (Z1 + 1.0)
    P.hole("M-GASKET", (x, y0, zc), (x, y1, zc), R, body)
    zt = zc + math.sqrt(max(R * R - w_top * w_top, 0.0)) * (1 if toward < 0 else -1)          # where the sides meet the arc
    lean = (w_end - w_top) / abs(-4.30 - zt) if toward < 0 else math.tan(math.radians(10.0)); w_far = w_top + lean * abs(z_end - zt)
    P.cutbox("M-GASKET", x - w_top, y0, min(zt, z_end), 2 * w_top, y1 - y0, abs(z_end - zt), body)
    for sg in (-1, 1):                                                                        # the wedges outside the straight part
        a, b = (x + sg * w_top, zt), (x + sg * w_far, z_end)
        if (sg > 0) == (toward > 0): a, b = b, a                                              # keep the strip on the pocket's side
        _beside(P, a, b, w_far - w_top + 0.5, y0, y1, body)

def _slot(P, body, x, z, along_z):
    """a 4.5 wide, 6.0 long mounting slot through the lug, from the back to past the seat"""
    h = (SLOT["l"] - SLOT["w"]) / 2; r = SLOT["w"] / 2
    for s in (-h, h):
        P.hole("M-GASKET", (x + (0 if along_z else s), 1.0, z + (s if along_z else 0)), (x + (0 if along_z else s), -SEAT - 1.0, z + (s if along_z else 0)), r, body)
    if along_z: P.cutbox("M-GASKET", x - r, -SEAT - 1.0, z - h, 2 * r, SEAT + 2.0, 2 * h, body)
    else: P.cutbox("M-GASKET", x - h, -SEAT - 1.0, z - r, 2 * h, SEAT + 2.0, 2 * r, body)

def build(conditions=""):
    """conditions: per port and pole, 'x1:2:spread/x5:4:corroded' (port:pole:condition) for fault scenarios"""
    P = Prims(); cond = {}
    for part in str(conditions or "").split("/"):
        if part.count(":") == 2: port, pole, c = part.split(":"); cond.setdefault(port, []).append(f"{pole}:{c}")
    cond = {k: "/".join(v) for k, v in cond.items()}
    body = P.box("M-ZINC-CAST", X0, -T, Z0, X1_ - X0, T, Z1 - Z0)                                     # die-cast body
    for x, zc, R, wt, we in SEATS: _seat(P, body, x, zc, R, wt, we, -1)                               # the power end's two seats
    _seat(P, body, FAR_SEAT[0], FAR_SEAT[1], FAR_SEAT[2], FAR_SEAT[2], None, +1)                       # the far end's
    lp = LABEL_POCKET; P.cutbox("M-GASKET", lp["x"][0], -T - 1.0, Z0 - 1.0, lp["x"][1] - lp["x"][0], T - lp["floor"] + 1.0, lp["z"] - Z0 + 1.0, body)
    _slot(P, body, 0.0, 0.0, False); _slot(P, body, 0.0, SLOT["far"], True)
    for z in (0.0, HOLES):                                                                            # M4 pan-head screws on the seats (Ø7 x 2.8: Assumption (C), appearance)
        P.cyl("M-ZINC", (0, -SEAT, z), (0, -SEAT - 2.8, z), 3.5)
    P.hole("M-GASKET", (FE["x"], 1.0, FE["z"]), (FE["x"], -7.2, FE["z"]), 2.0, body)                    # FE: M4 (Ø4.0 plain), Ø4.5 to the seat,
    P.hole("M-GASKET", (FE["x"], -7.2, FE["z"]), (FE["x"], -SEAT - 1.0, FE["z"]), 2.25, body)            # a Ø6.4 x 1.0 counterbore at the back
    P.hole("M-GASKET", (FE["x"], 1.0, FE["z"]), (FE["x"], -1.0, FE["z"]), 3.2, body)
    for name, coding, cx, cz, clock in PORTS:
        _port(P, body, name, coding, cx, cz, clock, cond)
        if coding == "A":                                                                             # channel LEDs: A (pin 4) yellow, B (pin 2) white
            lx = LED["x"] if cx > 0 else -LED["x"]
            din.led(P, f"led-{name}a", "M-LENS-YELLOW", lx, -T, cz + LED["dz"], r=LED["r"], proud=LED["proud"])
            din.led(P, f"led-{name}b", "M-LENS-WHITE", lx, -T, cz - LED["dz"], r=LED["r"], proud=LED["proud"])
    for k, (node, mat) in enumerate(STATUS):
        din.led(P, node, mat, -17.4 + 5.8 * k, -T, 77.8, r=LED["r"], proud=LED["proud"])
    sw = SWITCH; pr, p0, p1 = sw["pocket"]; sw_w, sw_d = sw["slot"]
    for n, x in sw["x"]:                                                                              # rotary switches: no cover (OCC, techdata photo)
        P.hole("M-GASKET", (x, -T - 1.0, sw["z"]), (x, -T + p0, sw["z"]), sw["bore"], body)
        P.hole("M-GASKET", (x, -T + p0, sw["z"]), (x, -T + p1, sw["z"]), pr, body)
        k_ = P.cyl(f"node:sw-{n}|M-GREY-PA", (x, -T - 0.1, sw["z"]), (x, -T + p1 - 0.05, sw["z"]), sw["r"])
        P.cutbox("M-GASKET", x - sw_w / 2, -T - 1.0, sw["z"] - sw["r"] - 0.5, sw_w, 0.9 + sw_d, 2 * sw["r"] + 1.0, k_)   # the pointer slot
        P.pivot(f"sw-{n}", "rotate", (x, -T, sw["z"]), axis=(0, -1, 0), range=(0, 324))
    P.hole("M-GASKET", (CAP["x"], -T - 1.0, CAP["z"]), (CAP["x"], -T + CAP["deep"], CAP["z"]), CAP["r"] + CAP["gap"], body)
    P.cyl("node:cap|M-BLACK-PC", (CAP["x"], -T, CAP["z"]), (CAP["x"], -T + CAP["deep"], CAP["z"]), CAP["r"])
    P.pivot("cap", "fixed", (CAP["x"], -T, CAP["z"]), axis=(0, -1, 0))
    (bw, bh), (tw, th) = PLATE["base"], PLATE["top"]; s = PLATE["seat"]
    for px, pz in PLATES:                                                                             # label plates, tops flush with their surface
        if pz < LABEL_POCKET["z"]:                                                                    # the power end's plate sits on its pocket floor
            P.box("M-WHITE-PA", px - tw / 2, -LABEL_POCKET["floor"] - s, pz - th / 2, tw, s, th); continue
        P.cutbox("M-GASKET", px - bw / 2, -T - 1.0, pz - bh / 2, bw, s + 1.0, bh, body)
        P.box("M-WHITE-PA", px - tw / 2, -T, pz - th / 2, tw, s, th)
    out = max(m12.face(g, c, "device") + m12.front(g, c, "device") for g, c in (("male", "L"), ("female", "A")))   # X03's sleeve: 13.1
    P.collider("env", X0, -T - out, Z0, X1_ - X0, T + out, Z1 - Z0)
    return P

PREVIEWS = [dict(name="front three-quarter", az=250, el=25), dict(name="ports close-up", az=262, el=15, center=(0, -20, 130), height=100),
            dict(name="power end: power, Ethernet, status LEDs and switches", az=262, el=15, center=(0, -20, 45), height=90)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
