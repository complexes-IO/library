#!/usr/bin/env python3
"""insert-m12: the coded insert of an M12 joint half and the contacts it carries (toolkit/m12.py 1.3). Female: the insert front, the
half's foremost face, with its keying (A one keyway, D three notches, L a recess at FE) and a socket in each cavity, and a base behind
the bore floor. Male: the pin carrier, a pin in each bore, and the keying ahead of it (A one peg, D three ribs, L the key block that
carries the FE socket); the sleeve itself is the nut's or the receptacle's. 1.4 (toolkit/m12.py 1.4, round 5 figures): D poles and
notches in the module's own sense; the L key block and recess cut to their measured outlines. 1.5 (m12.py 1.5, round 6): D keyed as
it is (the female's tooth, notches and slot; the male's channel blocks and rib); the I/O block's X03 block and X04's recess outlines.
1.6 (round 7): the cordset L female's recess takes X04's outline: its own STEP's does not fit its male (toolkit/m12.py, M12-010). `kind` cordset | device picks the figures of a cable end or
a housing. Every contact is a placed element (tag c<pole>), so its condition is a BOM parameter: conditions="2:bent/4:pushed-back".
Built in the M12 mating frame: mating plane y = 0, counterpart toward -y, key toward +z. Brief: references/measure.md."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "insert-m12", "1.6", "connector-part"
TITLE = "M12 coded insert, female (sockets, keying) or male (pin carrier, keying), A / D / L coding, cable end or device, with its contacts"
TOOLKIT = "1.3"
BASELINE = "toolkit/m12.py 1.4: the cordset ends (the A, D and L cordsets) and the I/O block's ports read with Open CASCADE (rounds 4 and 5): insert fronts Ø8.2 / Ø8.7, keyways, D notches and ribs, the L key block and recess outlines, FE; carrier and base lengths an Assumption"
ORIGIN = "the mating plane on the insert axis: female insert face / male carrier face at y = 0, counterpart toward -y, key toward +z"
COMMAND = "M12INS"
PARAMS = dict(gender="female", coding="A", kind="cordset", conditions="", tail=1.0)

def _socket_seat(P, targets, x, z, coding, y_face=0.0):
    """chamfer, entry and the socket's cavity at (x, z) below a face at y_face, through every target the column crosses"""
    mouth = y_face + m12.SOCKET["mouth"]
    for tg, y0, y1 in targets:
        if y0 <= y_face: P.hole("M-GASKET", (x, y0 - 1.0, z), (x, min(y_face + 0.3, y1), z), m12.CHAMFER[coding] / 2, tg)
        if y0 < mouth: P.hole("M-GASKET", (x, y0 - 1.0, z), (x, min(mouth, y1), z), m12.GUIDE[coding] / 2, tg)
        P.hole("M-GASKET", (x, max(mouth, y0), z), (x, y1 + 1.0, z), m12.CAVITY[coding] / 2, tg)

def _pin_seat(P, targets, x, z, r, y_root=0.0, y_end=None):
    """the pin's stepped bore (shank, retention collar, tail) at (x, z), the pin's root at y_root"""
    for tg, y0, y1 in targets:
        for a_, b_, rr in ((y_root - 1.0, y_root + 2.0, r), (y_root + 2.0, y_root + 2.6, r + 0.25), (y_root + 2.6, (y_end or y1) + 1.0, r + 0.15)):
            lo, hi = max(a_, y0 - 1.0 if a_ <= y_root - 1.0 else y0), min(b_, y1 + 1.0)
            if hi > lo: P.hole("M-GASKET", (x, lo, z), (x, hi, z), rr, tg)

def _cut_beside(P, a, b, depth, y0, y1, target):
    """cut away the strip `depth` wide on the right-hand side of the line a -> b (points (x, z); right-hand looking down +y onto
    the xz plane: the normal (dz, -dx)), from y0 to y1"""
    dx, dz = b[0] - a[0], b[1] - a[1]; L_ = math.hypot(dx, dz); n = (dz / L_, 0.0, -dx / L_); ez = (dx / L_, 0.0, dz / L_)   # n x y = ez
    P.cut("M-GASKET", (a[0], y0, a[1]), n, (0, 1, 0), ez, depth, y1 - y0, L_, target)

def _l_block(P, blk, kind, y0, y1):
    """cut the male L key block out of a full disc `blk`: what is left is the measured outline (toolkit/m12.key_outline): the chord,
    two flanks, the ledge on +x and the wall on -x"""
    c, (fl, fr), ((xl, zl), (xr, zr)), s = m12.key_outline("L", "male", kind)
    P.cutbox("M-GASKET", -6.0, y0, -6.0, 12.0, y1 - y0, 6.0 + c, blk)                            # below the chord
    P.cutbox("M-GASKET", -6.0, y0, -6.0, 6.0 + xl, y1 - y0, 12.0, blk)                           # beyond the wall (-x)
    P.cutbox("M-GASKET", xr, y0, -6.0, 6.0 - xr, y1 - y0, 6.0 + zr, blk)                         # under the ledge (+x)
    _cut_beside(P, (fr, c), (xr, zr), 1.5, y0, y1, blk)                                         # outside the +x flank
    _cut_beside(P, (xl, zl), (fl, c), 1.5, y0, y1, blk)                                         # outside the -x flank

def _l_pocket(P, front, kind, y0, y1):
    """cut the female L recess into the insert front: the measured outline (toolkit/m12.key_outline), as four overlapping pieces:
    the ledge on -x and the wall on +x"""
    c, (fl, fr), ((xl, zl), (xr, zr)), s = m12.key_outline("L", "female", kind); zt = min(zl, zr)
    P.cutbox("M-GASKET", -6.0, y0, zt, 6.0 + xr, y1 - y0, 6.0 - zt, front)                        # above the flank tops, to the wall
    P.cutbox("M-GASKET", fl, y0, c, fr - fl, y1 - y0, zt - c + 0.01, front)                       # between the flank feet
    _cut_beside(P, (xr, zr), (fr, c), 2.0, y0, y1, front)                                       # inside the +x flank
    _cut_beside(P, (fl, c), (xl, zl), 2.0, y0, y1, front)                                       # inside the -x flank

def _d_female(P, front, D):
    """D keying in the female front (toolkit/m12.D_KEY): flat notches either side of the tooth on the 0° line, the slot on 106.5°"""
    k = m12.D_KEY; t, fl, deep = k["tooth"], k["floor"], k["deep"]; a, w, sf = k["slot"]
    P.cutbox("M-GASKET", -6.0, -1.0, fl, 6.0 - t, deep + 1.0, 6.0 - fl, front)
    P.cutbox("M-GASKET", t, -1.0, fl, 6.0 - t, deep + 1.0, 6.0 - fl, front)
    th = math.radians(a); rad = (math.sin(th), 0.0, math.cos(th)); tan = (math.cos(th), 0.0, -math.sin(th))   # tan x y = rad
    P.cut("M-GASKET", (rad[0] * sf - tan[0] * w, -1.0, rad[2] * sf - tan[2] * w), tan, (0, 1, 0), rad, 2 * w, deep + 1.0, 6.0 - sf, front)

def _d_male(P, col, bore, reach):
    """D keying ahead of the male carrier (toolkit/m12.D_KEY): the two blocks the channel leaves above the chord, and the flat rib
    on the 106.5° line (mirrored: a male face is the female's mirror image)"""
    k = m12.D_KEY; ch, cw = k["chord"], k["channel"]; hw, top = k["rib"]; a = k["slot"][0]; R_ = bore - 0.05
    for side in (-1, 1):
        b = P.cyl(col, (0, -reach, 0), (0, 0, 0), R_)
        P.cutbox("M-GASKET", -6.0, -reach - 1.0, -6.0, 12.0, reach + 2.0, 6.0 + ch, b)             # below the chord
        P.cutbox("M-GASKET", -6.0 if side > 0 else -cw, -reach - 1.0, -6.0, 6.0 + cw, reach + 2.0, 12.0, b)   # the channel and the other side
    th = math.radians(a); rad = (-math.sin(th), 0.0, math.cos(th)); ex = (math.cos(th), 0.0, math.sin(th))      # ex x y = rad (male: x mirrored)
    P.obox(col, (rad[0] * top - ex[0] * hw, -reach, rad[2] * top - ex[2] * hw), ex, (0, 1, 0), rad, 2 * hw, reach, R_ - top)

def build(gender="female", coding="A", kind="cordset", conditions="", tail=1.0):
    P = Prims(); d = m12.CONTACT_D[coding]; r = d / 2; cond = m12.parse_conditions(conditions)
    col = m12.COLOUR[coding]; kr = m12.key_r(coding); prot, lead = m12.PIN[coding]; bottom = m12.SOCKET["bottom"][coding]
    fe = m12.REVERSED.get(coding, ()); fe_xz = m12.pole_xz(coding, fe[0], gender) if fe else None
    if gender == "female":
        D = m12.female(kind, coding, "depth"); L = m12.insert_l("female", coding, kind)
        front = P.cyl(col, (0, 0, 0), (0, D, 0), m12.INSERT_R[coding])                          # the foremost face; the male sleeve slides over it
        if coding == "A":                                                                        # the keyway along its edge
            for a in m12.KEYS["A"]:
                x, z = m12.ang_xz(a, kr, "female"); P.hole("M-GASKET", (x, -1.0, z), (x, D + 1.0, z), m12.KEYWAY["d"] / 2, front)
        if coding == "D": _d_female(P, front, D)                                                  # the tooth between its notches, the slot
        if coding == "L":                                                                        # the recess the male's key block enters, at FE (+z)
            _l_pocket(P, front, kind, -1.0, m12.L_KEY["recess"][kind])
        back = P.cyl(col, (0, D, 0), (0, L, 0), m12.THREAD_R)                                    # base behind the bore floor
        targets = [(front, 0.0, D), (back, D, L)]; rx = m12.THREAD_R
    else:
        L = m12.insert_l("male", coding, kind); bore = m12.male(kind, coding, "bore")
        back = P.cyl(col, (0, 0, 0), (0, L, 0), bore - 0.05)                                     # pin carrier inside the sleeve
        if coding == "A":                                                                        # the key peg along the sleeve wall
            for a in m12.KEYS["A"]:
                x, z = m12.ang_xz(a, kr, "male"); P.cyl(col, (x, -m12.KEY["reach"], z), (x, 0, z), m12.KEY["d"] / 2)
        if coding == "D": _d_male(P, col, bore, m12.KEY["reach"])                                 # the blocks either side of the channel, the rib
        targets = [(back, 0.0, L)]; rx = bore
        if coding == "L":                                                                        # the key block at FE, the FE socket in it
            yb = -(m12.male(kind, coding, "reach") - m12.L_KEY["back"])
            blk = P.cyl(col, (0, yb, 0), (0, 0, 0), bore - 0.05)
            _l_block(P, blk, kind, yb - 1.0, 1.0)
            x, z = fe_xz; P.hole("M-GASKET", (x, yb - 1.0, z), (x, 1.0, z), m12.FE_L["bore"] / 2, blk)
            P.hole("M-GASKET", (x, -1.0, z), (x, L + 1.0, z), m12.FE_L["bore"] / 2, back)
    for pole in m12.LAYOUT[coding]:
        x, z = m12.pole_xz(coding, pole, gender); kind_c = m12.gender_of(coding, pole, gender); c = cond.get(pole, "ok")
        if pole in fe and gender == "male":                                                      # L FE socket: mouth at the key block's face
            yb = -(m12.male(kind, coding, "reach") - m12.L_KEY["back"])
            if c != "missing":
                library.place(P, dict(element="contact-m12-socket", version="1.3", tag=f"c{pole}", parent="", x=x, y=yb, z=z, yaw=0.0,
                                      params=dict(d=d, pole=pole, condition=c, tail=max(0.1, min(tail, L - (yb + m12.FE_L["deep"]) - 1.1)),
                                                  outer=m12.FE_L["bore"], bottom=m12.FE_L["deep"], face=0.0)))
        elif pole in fe:                                                                         # L FE pin: standing in the recess, its tip below the face
            below = m12.FE_L["below"]; root = m12.L_KEY["recess"][kind]; pl = root - below
            _pin_seat(P, targets, x, z, m12.CONTACT_D[coding] / 2, y_root=root, y_end=L)
            if c != "missing":
                library.place(P, dict(element="contact-m12-pin", version="1.2", tag=f"c{pole}", parent="", x=x, y=below, z=z, yaw=0.0,
                                      params=dict(d=d, pole=pole, condition=c, protrude=pl, lead=m12.FE_L["pin"][1], tail=max(0.1, min(tail, L - root - 2.6 - 0.1)))))
        elif kind_c == "socket":
            _socket_seat(P, targets, x, z, coding)
            if c != "missing":
                library.place(P, dict(element="contact-m12-socket", version="1.3", tag=f"c{pole}", parent="", x=x, y=m12.SOCKET["mouth"], z=z, yaw=0.0,
                                      params=dict(d=d, pole=pole, condition=c, tail=max(0.1, min(tail, L - m12.SOCKET["mouth"] - bottom - 1.1)),
                                                  outer=m12.CAVITY[coding], bottom=bottom)))
        else:
            _pin_seat(P, targets, x, z, r)
            if c != "missing":
                library.place(P, dict(element="contact-m12-pin", version="1.2", tag=f"c{pole}", parent="", x=x, y=-prot, z=z, yaw=0.0,
                                      params=dict(d=d, pole=pole, condition=c, protrude=prot, lead=lead, tail=min(tail, L - 2.6 - 0.1) if tail else 0.1)))
    ahead = max(m12.KEY["reach"], prot, m12.male(kind, coding, "reach") - m12.L_KEY["back"] if coding == "L" else 0) if gender == "male" else 0.0
    P.collider("env", -rx, -ahead, -rx, 2 * rx, L + ahead, 2 * rx)
    return P

PREVIEWS = [dict(name="female A-coded", az=250, el=25), dict(name="male A-coded (pins, key peg)", az=250, el=25, params=dict(gender="male")),
            dict(name="female D-coded (three notches)", az=250, el=25, params=dict(coding="D")),
            dict(name="female L-coded (FE in the recess)", az=250, el=25, params=dict(coding="L")),
            dict(name="male L-coded (key block, FE socket)", az=250, el=25, params=dict(gender="male", coding="L")),
            dict(name="male, pin 2 bent, pin 4 pushed back", az=250, el=25, params=dict(gender="male", conditions="2:bent/4:pushed-back"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
