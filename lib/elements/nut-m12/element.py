#!/usr/bin/env python3
"""nut-m12: the knurled coupling nut of an M12 cable end. Captive on the plug: turning it pulls the plug home by one pitch per turn, so
its node is a rotate pivot with the lead in its extras; how far it is turned is the joint's state (toolkit/contact.py). The thread
follows the gender (toolkit/m12.py 1.3): a male plug's nut is the threaded SLEEVE (one solid: the external thread envelope from the
sleeve's front to the knurl) that screws into the female's bore; a female plug's nut is the threaded BORE, its front face behind the
insert face. 1.4: the A male nut as measured (the A cordset, round 5): front face 0.9 behind the carrier face, knurl Ø15 1.4 to 3.9, a
13 mm hex 3.9 to 6.4. 1.5 (round 6): the D male nut is the A nut; the L male nut's front face at 1.2, Ø17.9 to 5.2, a 16.9 hex
to its back face at 8.7 (the D and L cordsets). Built in the M12 mating frame: mating plane y = 0, the counterpart toward -y. Brief: references/measure.md."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "nut-m12", "1.5", "connector-part"
TITLE = "M12 x 1 knurled coupling nut, male (threaded sleeve, nickel-plated brass) or female (threaded bore, nickel-plated zinc)"
TOOLKIT = "1.3"
BASELINE = "cordset ends read with Open CASCADE (rounds 4 and 5): male sleeve Ø8.3 / Ø8.8 bore reaching 8.9 / 8.8, thread 0.9 (L 1.2) behind the carrier face to 5.95 (L 6.44) ahead, knurl Ø15 / Ø17.9; A male nut: collar 0.9, knurl 1.4-3.9, hex 13 AF 3.9-6.4 (the A cordset); D / L male nut length an Assumption; female nut face 1.5 (L 1.3) behind the insert face, thread Ø11.0 from 2.1 (L 1.59) behind it; torque 0.5-0.6 N m"
ORIGIN = "the mating plane on the nut axis (the male carrier face / the female insert face); the counterpart toward -y"
COMMAND = "M12NUT"
PARAMS = dict(gender="male", coding="A")

def tail_f(coding):
    """a female nut's back behind the mating plane: past the insert's base (Assumption)"""
    return m12.insert_l("female", coding, "cordset") + 0.5

def build(gender="male", coding="A"):
    P = Prims(); rk = m12.KNURL[coding]
    if gender == "male":
        ri, reach = m12.male("cordset", coding, "bore"), m12.male("cordset", coding, "reach"); k0 = m12.male("cordset", coding, "face")
        y_front, y_back = -reach, m12.nut_back(coding); parts = []
        if coding in m12.MALE_NUT:                                                                  # the measured nut
            nu = m12.MALE_NUT[coding]; k1 = nu["knurl"][1]; h0, h1, af, hr = nu["hex"]; c0 = nu["collar"][0] if nu["collar"] else k0
            parts.append((P.cyl("node:self|M-ZINC", (0, -reach, 0), (0, c0, 0), m12.THREAD_R), -reach, c0))   # sleeve: lip, chamfer, thread
            if nu["collar"]:
                c0, c1, cr = nu["collar"]; parts.append((P.cyl("node:self|M-ZINC", (0, c0, 0), (0, k0, 0), cr), c0, k0))   # the front face's collar
            parts.append((P.cyl("node:self|M-ZINC", (0, k0, 0), (0, k1, 0), rk), k0, k1))                     # the knurl
            hx = P.cyl("node:self|M-ZINC", (0, h0, 0), (0, h1, 0), hr); parts.append((hx, h0, h1))           # the hex, corners turned
            for k in range(6):                                                                                 # its six flats
                t = math.radians(30 + 60 * k); n = (math.sin(t), 0.0, math.cos(t)); tg = (math.cos(t), 0.0, -math.sin(t))
                o = (n[0] * af + tg[0] * 8.0, h0 - 1.0, n[2] * af + tg[2] * 8.0)
                P.cut("M-GASKET", o, n, (0, 1, 0), (-tg[0], 0.0, -tg[2]), 2.0, h1 - h0 + 2.0, 20.0, hx)
        else:
            parts.append((P.cyl("node:self|M-ZINC", (0, -reach, 0), (0, k0, 0), m12.THREAD_R), -reach, k0))  # the threaded sleeve: lip, chamfer
            parts.append((P.cyl("node:self|M-ZINC", (0, k0, 0), (0, y_back, 0), rk), k0, y_back))             # and thread in one envelope; knurl
        for c, y0, y1 in parts: P.hole("M-GASKET", (0, y0 - 1.0, 0), (0, y1 + 1.0, 0), ri, c)
    else:
        y_front, y_back = m12.female("cordset", coding, "face"), tail_f(coding)
        c = P.cyl("node:self|M-ZINC", (0, y_front, 0), (0, y_back, 0), rk)
        P.hole("M-GASKET", (0, y_front - 1.0, 0), (0, y_back + 1.0, 0), m12.THREAD_R, c)          # the threaded bore (plain at the minor r)
    catch, _ = m12.engagement(m12.thread_span("male", coding), m12.thread_span("female", coding))
    P.pivot("self", "rotate", (0, 0, 0), axis=(0, -1, 0), range=(0, round(360.0 * catch / m12.PITCH, 1)), unit="deg", lead=m12.PITCH, drives="mate", torque=m12.TORQUE)
    P.collider("env", -rk, y_front, -rk, 2 * rk, y_back - y_front, 2 * rk)
    return P

PREVIEWS = [dict(name="male nut (threaded sleeve)", az=250, el=25), dict(name="female nut (threaded bore)", az=250, el=25, params=dict(gender="female")),
            dict(name="male L-coded", az=250, el=25, params=dict(coding="L"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
