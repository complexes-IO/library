#!/usr/bin/env python3
"""cordset-m12: M12 cordset, A- / D- / L-coded, each end a plug-m12 (male pins or female sockets, coupling nut, seal), swept cable along
a path. Own element (2026-11-03 ruling): the cable is the first routed geometry in the library; a connections.csv row supplies the path
and the params (genders="male-female" | "male-male" | ..., conditions_a / conditions_b for a damaged pin). The open-ended form (1.8,
request panel-4 item 2): genders "male-open" / "female-open", end B no plug, the jacket ends and the conductors fan out as bare
leads, each lead's tip a contact node lead-<pin> (behaviour.csv's form rows give end B's pins those nodes)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
from toolkit import fillet, library, m12, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "cordset-m12", "1.8", "cable"
TITLE = "M12 cordset, A / D / L coded, male or female ends (plug-m12) or open-ended, PUR, routed"
TOOLKIT = "1.3"
BASELINE = "cordset cut sheets and drawings (round-4 reference set): cable Ø A 5.0 (22 AWG), D 6.6, L 9.8 (16 AWG); lengths 0.6 / 1 / 2 / 3 / 5 / 7.5 / 10 / 15 m; bend radius 5 x Ø fixed, 10 x Ø flexing; ends are plug-m12 1.3; the A cable Ø5.0 is the catalogue's PVC figure (the TPE cable's Ø is NOT ON FILE)"
ORIGIN = "end A mating face at the origin, plugging along +y into a port whose face is at y = 0 and looks toward -y; the cable leaves toward -y and follows `path`"
COMMAND = "CORD"
PARAMS = dict(coding="A", length=1000.0, ends="straight", path=None, genders="male-female", conditions_a="", conditions_b="")
CABLE_D = {"A": 5.0, "D": 6.6, "L": 9.8}           # catalogues: A 5.0 (PVC; TPE NOT ON FILE), D 6.6, L 9.8 (16 AWG; 14 AWG is 10.5)
BEND = (5.0, 10.0)                                 # minimum bend radius x Ø: fixed, flexing (cut sheets)
LENGTHS = (600, 1000, 2000, 3000, 5000, 7500, 10000, 15000)   # catalogue lengths, mm
OPEN = "open"                                      # end B's gender in the open-ended form: no plug, bare leads (1.8)
LEAD_AWG = {"A": 22, "D": None, "L": 16}           # conductor size: A 22 AWG, L 16 AWG (lib/standards/cables.csv); D NOT ON FILE (B)
LEAD_L, LEAD_SPREAD = 50.0, 6.0                    # design: each lead 50 beyond the jacket, its tip 6 out from the cable's axis (own choice; no standard fixes a strip length)

def awg_d(n):
    """derived: the AWG definition, d = 0.127 mm x 92^((36 - n) / 39) (lib/standards/sources.csv awg; ASTM B258 tabulates it)"""
    return 0.127 * 92 ** ((36 - n) / 39.0)

def lead_d(coding):
    """a bare lead's diameter: the coding's conductor (solid equivalent, derived). D: the conductor size is NOT ON FILE (B); its leads
    are drawn at A's 22 AWG until the cut sheet's figure is on file (Assumption (B), spec.md)"""
    return awg_d(LEAD_AWG[coding] or LEAD_AWG["A"])

def _frame(v):
    """two unit vectors square to v and each other: e1 the one nearest +z (the female face's 'up', where the key's angle is counted)"""
    v = np.asarray(v, float) / np.linalg.norm(v); up = np.array([0.0, 0.0, 1.0]) if abs(v[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    e1 = up - v * (up @ v); e1 /= np.linalg.norm(e1); return e1, np.cross(v, e1)

def _leads(P, coding, end, v):
    """end B of the open form: one bare lead per pole of the coding from the jacket's end along v, fanned out on the poles' angles;
    each tip a contact node lead-<pole>, axis along its lead"""
    e1, e2 = _frame(v); r_in = CABLE_D[coding] / 4; dl = lead_d(coding); tips = []
    for pole, ang in m12.LAYOUT[coding].items():
        radial = np.zeros(3) if ang is None else e1 * math.cos(math.radians(ang)) + e2 * math.sin(math.radians(ang))
        a = np.asarray(end, float) + radial * (0 if ang is None else r_in)
        b = np.asarray(end, float) + v * LEAD_L + radial * (0 if ang is None else LEAD_SPREAD)
        i = P.cyl("M-CU", tuple(a - v * 2.0), tuple(b), dl / 2)                   # 2 into the jacket, so the lead leaves it
        P.radii[i] = fillet.RADIUS["wire"]                                        # a conductor's end takes a wire's edge break, not r 0.5
        ax = (b - a) / np.linalg.norm(b - a)
        P.pivot(f"lead-{pole}", "contact", tuple(b), axis=tuple(ax), range=(0, 0), unit="mm", pole=pole, gender="lead", d=round(dl, 3))
        tips.append(b)
    return tips

def _yaw_pitch(v):
    """yaw and pitch (degrees, toolkit placement order) that turn a plug's -y (toward its receptacle) onto the unit vector v"""
    v = np.asarray(v, float) / np.linalg.norm(v)
    return math.degrees(math.atan2(v[0], -v[1])), -math.degrees(math.asin(max(-1.0, min(1.0, v[2]))))

def build(coding="A", length=1000.0, ends="straight", path=None, genders="male-female", conditions_a="", conditions_b=""):
    P = Prims(); r = CABLE_D[coding] / 2; ga, gb = (genders.split("-") + ["female"])[:2]
    plug = library.load("plug-m12")
    def exit_len(g): return 0.0 if g == OPEN else plug.cable_exit(g, coding)[1]
    # end A: plugging along +y into its port, so the plug turns 180° (its receptacle side, -y, onto +y); the cable leaves toward -y
    library.place(P, dict(element="plug-m12", version="1.6", tag="port-a", parent="", x=0, y=0, z=0, yaw=180.0,
                          params=dict(gender=ga, coding=coding, conditions=conditions_a)))
    a_tail = np.array([0.0, -exit_len(ga), 0.0])
    if path is None:                                                                                      # straight run along -y with a gentle hang; end B looks on along -y
        L = float(length) - exit_len(ga) - exit_len(gb)
        pts = [a_tail, a_tail + (0, -12.0, 0), a_tail + (0, -L * 0.25, -L * 0.03), a_tail + (0, -L * 0.75, -L * 0.03), a_tail + (0, -L + 12.0, 0), a_tail + (0, -L, 0)]
    else:
        pts = [a_tail, a_tail + (0, -12.0, 0)] + [np.array(p, float) for p in path]                       # leaves the overmould straight
    v = pts[-1] - pts[-2]; v /= np.linalg.norm(v)
    b_face = pts[-1] + v * exit_len(gb); yaw, pitch = _yaw_pitch(v)
    if gb == OPEN: b_face = _leads(P, coding, pts[-1], v)                                                  # bare leads; the jacket ends at pts[-1]
    else: library.place(P, dict(element="plug-m12", version="1.6", tag="port-b", parent="", x=b_face[0], y=b_face[1], z=b_face[2], yaw=yaw, pitch=pitch,
                                params=dict(gender=gb, coding=coding, conditions=conditions_b)))
    run = sum(float(np.linalg.norm(np.array(b) - np.array(a))) for a, b in zip(pts, pts[1:]))
    mid = SW.resample([tuple(p) for p in pts[1:-1]], max(8.0, run / 150.0))                               # about 150 rings whatever the length
    route = np.vstack([[pts[0]], mid, [pts[-1]]])                                                          # the straight leads stay straight
    P.mesh("M-CABLE-PUR", SW.sweep(route, SW.circle_profile(r, 12)))
    rk = m12.KNURL[coding]; ahead = [[0, m12.front(ga, coding), 0]]                                         # end A's front reaches toward +y
    ends = np.atleast_2d(np.asarray(b_face, float))
    lo = np.min(np.vstack([route, ends, ahead]), axis=0) - rk; hi = np.max(np.vstack([route, ends, ahead]), axis=0) + rk
    P.collider("env", *lo, *(hi - lo))
    return P

PREVIEWS = [dict(name="A-coded 1 m straight", az=250, el=20), dict(name="connector end A", az=250, el=20, center=(0, -20, 0), height=50),
            dict(name="end A, pin 2 bent", az=120, el=10, center=(0, -10, 0), height=30, params=dict(conditions_a="2:bent")),
            dict(name="D-coded 2 m", az=250, el=20, params=dict(coding="D", length=2000)), dict(name="routed with two bends", az=240, el=25, params=dict(path=[(0, -200, 0), (0, -250, -150), (300, -250, -150), (300, -200, -300)])),
            dict(name="L-coded open end B", az=200, el=20, center=(0, -1000, -30), height=90, params=dict(coding="L", genders="male-open"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
