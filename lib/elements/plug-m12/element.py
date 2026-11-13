#!/usr/bin/env python3
"""plug-m12: the cable side of an M12 joint (toolkit/m12.py 1.3, kind cordset): the coded insert with its contacts (insert-m12), the
coupling nut (nut-m12) that carries the thread for its gender, on a female plug the face seal (seal-m12) on the bore floor, and the
overmould the cable leaves. A male plug's sleeve is its foremost part; a female plug's insert face is, the nut's face 1.5 (L 1.3)
behind it. 1.4: the A male body as measured behind its nut (the A cordset, round 5). 1.5: the D and L male bodies as measured
(the D and L cordsets, round 6). Its node `self` is the cable end that lands on a
port, with the mating data in its extras (port_data). Built in the M12
mating frame: mating plane y = 0, the receptacle toward -y, the plug body and cable toward +y. Brief: references/measure.md."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, m12
from toolkit.prims import Prims

ID, VERSION, CLASS = "plug-m12", "1.6", "connector"
TITLE = "M12 cable plug, male (pins, threaded sleeve nut) or female (sockets, threaded nut, seal), A / D / L coded, straight overmould"
TOOLKIT = "1.3"
BASELINE = "cordset ends read with Open CASCADE (round 4): overall A male 40.7, D male 47.5, L male 53.8, L female 53.0 (drawings and OCC); A female 38 (catalogue m12patchcbl p. 1: the axial female, no model on file); overmould Ø an Assumption"
ORIGIN = "the mating plane on the axis (male: carrier face; female: insert face, the foremost face); the receptacle toward -y; the cable leaves toward +y"
COMMAND = "M12PLG"
PARAMS = dict(gender="male", coding="A", conditions="", overall=0.0)
OVERALL = {("male", "A"): 40.7, ("male", "D"): 47.5, ("male", "L"): 53.8,          # foremost face to cable exit; D female as A female:
           ("female", "A"): 38.0, ("female", "D"): 38.0, ("female", "L"): 53.0}    # Assumption
BODY_R = {"A": 6.5, "D": 6.5, "L": 7.5}                                             # overmould: D / L Assumption (under the knurl)
BODY_MALE = {"A": [(4.2, 7.5), (6.0, 15.35), (5.1, 19.8), (4.4, 28.8), (5.25, 29.3), (4.4, 31.8)],
             "D": [(4.2, 8.6), (7.1, 13.6), (7.5, 14.4), (7.1, 15.1), (7.5, 15.9), (7.1, 16.6), (7.5, 17.4), (7.1, 31.0), (5.8, 34.5), (4.5, 38.6)],
             "L": [(5.55, 10.0), (7.6, 12.1), (8.45, 16.0), (7.9, 22.3), (7.25, 28.6), (6.6, 34.8), (6.1, 41.0), (6.5, 41.4), (5.8, 45.0)]}
                                  # male bodies behind the nut's back face, as (r, to), tapers and cones modelled as steps at their mid-points:
                                  # A (the A cordset, OCC, round 5): neck Ø8.4 to 7.5; Ø12 and the taper to Ø10.2 to 15.35; Ø10.2 and the taper
                                  # to Ø8.8 to 19.8; Ø8.8 to 28.8; the ring Ø10.5 to 29.3; the boot to 31.8.
                                  # D (the D cordset, round 6): neck Ø8.4 to 8.6; Ø14.2 with three Ø15.0 grip beads (13.6-14.4, 15.1-15.9,
                                  # 16.6-17.4) to 31.0; the 20.4° taper to Ø9.0 by 38.0 (two steps); the boot end at 38.6.
                                  # L (the L cordset, round 6): neck Ø11.1 to 10.0; the overmould Ø15.2 rising to Ø16.9 at 14.2-16.0, tapering
                                  # to Ø12.3 at 34.8 and Ø12.05 at 41.0 (four steps); the ring Ø13.0 at 41.2; the R20 boot to the end at 45.0

def cable_exit(gender="male", coding="A", overall=0.0):
    """where the cable leaves the overmould, in the plug frame (the overall length runs from the half's foremost point)"""
    o = float(overall) or OVERALL[(gender, coding)]
    return (0.0, o - m12.front(gender, coding), 0.0)

def build(gender="male", coding="A", conditions="", overall=0.0):
    P = Prims(); nut = library.load("nut-m12"); exit_y = cable_exit(gender, coding, overall)[1]
    library.place(P, dict(element="insert-m12", version="1.6", tag="insert", parent="", x=0, y=0, z=0, yaw=0.0,
                          params=dict(gender=gender, coding=coding, kind="cordset", conditions=conditions, tail=1.0)))
    library.place(P, dict(element="nut-m12", version="1.5", tag="nut", parent="", x=0, y=0, z=0, yaw=0.0, params=dict(gender=gender, coding=coding)))
    if gender == "male":
        back = m12.nut_back(coding); L = m12.insert_l("male", coding)
        if coding in BODY_MALE and abs(exit_y - BODY_MALE[coding][-1][1]) < 1e-6:                  # the measured body, solid by solid
            y0 = back
            for k, (r_, y1) in enumerate(BODY_MALE[coding]):
                c_ = P.cyl("node:self|M-BLACK-PC" if k == 0 else "M-BLACK-PC", (0, y0, 0), (0, y1, 0), r_); y0 = y1
        else:
            mould = P.cyl("node:self|M-BLACK-PC", (0, back, 0), (0, exit_y, 0), BODY_R[coding])
            if L > back: P.hole("M-GASKET", (0, back - 1.0, 0), (0, L, 0), m12.male("cordset", coding, "bore"), mould)   # the carrier's seat
    else:
        D = m12.female("cordset", coding, "depth"); L = m12.insert_l("female", coding); back = nut.tail_f(coding); t = m12.seal_thick(coding)
        library.place(P, dict(element="seal-m12", version="1.2", tag="seal", parent="", x=0, y=D - t, z=0, yaw=0.0,
                              params=dict(r_in=m12.INSERT_R[coding] + 0.05, r_out=m12.THREAD_R - 0.01, thick=t)))   # on the bore floor
        P.cyl("M-BLACK-PC", (0, L, 0), (0, back, 0), m12.THREAD_R - 0.06)                         # neck inside the nut, behind the insert base
        mould = P.cyl("node:self|M-BLACK-PC", (0, back, 0), (0, exit_y, 0), BODY_R[coding])
    P.pivot("self", "port", (0, 0, 0), axis=(0, -1, 0), range=(0, 0), unit=coding, **m12.port_data(coding, gender, "cordset"))
    ahead = m12.front(gender, coding); rk = m12.KNURL[coding]
    P.collider("env", -rk, -ahead, -rk, 2 * rk, exit_y + ahead, 2 * rk)
    return P

PREVIEWS = [dict(name="male A-coded (threaded sleeve)", az=250, el=20), dict(name="female A-coded (threaded nut)", az=250, el=20, params=dict(gender="female")),
            dict(name="male, pin 2 bent", az=250, el=20, params=dict(conditions="2:bent"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
