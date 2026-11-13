#!/usr/bin/env python3
"""cable-pwr-480: the motor branch cable, panel receptacle to motor terminal box: a 3P+E pin-and-sleeve plug (end A), a four-core jacket
along `path`, and at end B the cores out of the jacket as wire elements (L1 L2 L3 PE) with their prepared ends for the motor terminals.
1.1: the conductor is chosen by the standards, not by taste: 14 AWG (2.08 mm²) four-conductor SOOW 600 V cord. The 10 A branch breaker must
protect the cord (NEC 240.4 / IEC 60364-4-43: 15 A, NEC Table 400.5(A)(1) column A, three current-carrying); the conductors carry 125 % of
the motor's 1.1 A table current (NEC 430.22, 430.6(A)(1)); 14 AWG is the NFPA 79 minimum for power circuits. Brief: references/measure.md."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
from toolkit import library, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "cable-pwr-480", "1.4", "cable"
TITLE = "motor branch cable 3P+E 480 V: pin-and-sleeve plug, 14/4 SOOW 600 V cord, cores prepared for the motor terminals"
TOOLKIT = "1.3"
BASELINE = "cord: 14/4 SOOW 600 V 90 °C class (the cord maker's datasheet, references/source.txt: nominal OD 0.570 in = 14.48 mm, cores black / white / red / green); ampacity 15 A from NEC Table 400.5(A)(1) column A; plug envelope own design to mate port-pwr-480 1.1 (IEC 60309-2 class), Assumption (B), spec.md"
ORIGIN = "end A (plug) mating face at the origin, plugging along +y into a receptacle that looks toward -y; the jacket leaves toward -y and follows `path`"
COMMAND = "C480"
PARAMS = dict(length=4000.0, path=None, size=2.08, cores="M-BLACK-PA/M-WHITE-PA/M-RED/M-GREEN", strip=10.0, ferrule=True, conditions="")
JACKET_OD = {2.08: 14.48}                       # four-core OD by core size, mm²: 2.08 (14/4 SOOW), the cord maker's datasheet (1.2: the
                                                # unsourced 1.5 / 2.5 / 4 / 6 rows are gone; another size is NOT ON FILE and stops the build)

def jacket_od(size):
    """the cord's OD for a core size in mm² (SRC-010: no figure for a size the table lacks)"""
    try: return JACKET_OD[float(size)]
    except KeyError: raise ValueError(f"cable-pwr-480: jacket OD for {size} mm² cores is NOT ON FILE (JACKET_OD holds {sorted(JACKET_OD)}: the cord maker's datasheet)") from None
PLUG_R, PLUG_L, GRIP_R, GRIP_L = 24.0, 60.0, 19.0, 45.0           # plug body and grip (Assumption (B): fits and envelope, to mate the receptacle's Ø44 socket face; spec.md Dimensions, plug)
POLES = ("L1", "L2", "L3", "PE")
TAIL = 90.0                                                       # cores out of the jacket at end B

def _yp_into(v):
    """yaw and pitch that turn +y onto unit vector v (toolkit placement: pitch about x first, then yaw about z)"""
    v = np.asarray(v, float) / np.linalg.norm(v)
    return math.degrees(math.atan2(-v[0], v[1])), math.degrees(math.asin(max(-1.0, min(1.0, v[2]))))

def build(length=4000.0, path=None, size=2.08, cores="M-BLACK-PA/M-WHITE-PA/M-RED/M-GREEN", strip=10.0, ferrule=True, conditions=""):
    """size: mm² per core (2.08 = 14 AWG). cores: L1 / L2 / L3 / PE colours, as the cord comes: black, white, red, green (green the
    equipment ground; a white core in a flexible cord may be a phase, NEC 200.7(C))"""
    P = Prims(); od = jacket_od(size); cols = cores.split("/")
    cond = {}                                                                                             # 'L1:a:under-stripped': pole, wire end, condition
    for part in str(conditions or "").split("/"):
        if part.count(":") == 2: pole, end, c = part.split(":"); cond.setdefault(pole, []).append(f"{end}:{c}")
    P.cyl("node:port-a|M-RED-PA", (0, 0, 0), (0, -PLUG_L, 0), PLUG_R)                                  # plug body (its face meets the socket face)
    P.cyl("M-BLACK-PA", (0, -PLUG_L, 0), (0, -PLUG_L - GRIP_L, 0), GRIP_R)                                # grip and cable entry
    P.pivot("port-a", "port", (0, 0, 0), axis=(0, 1, 0), range=(0, 0), unit="480V-3P+E", gender="male")   # 7 h earth keying (IEC 60309-2, port-pwr-480 brief)
    start = np.array([0.0, -PLUG_L - GRIP_L, 0.0])
    if path is None:
        L = max(100.0, float(length) - PLUG_L - GRIP_L - TAIL * 0.3)
        pts = [start, start + (0, -15.0, 0), start + (0, -L * 0.3, -L * 0.04), start + (0, -L * 0.7, -L * 0.04), start + (0, -L + 20.0, 0), start + (0, -L, 0)]
    else:
        pts = [start, start + (0, -15.0, 0)] + [np.array(p, float) for p in path]
    v = pts[-1] - pts[-2]; v /= np.linalg.norm(v)
    run = sum(float(np.linalg.norm(b - a)) for a, b in zip(pts, pts[1:]))
    mid = SW.resample([tuple(p) for p in pts[1:]], max(8.0, run / 150.0)); route = np.vstack([[pts[0]], mid])
    P.mesh("M-CABLE-GREY", SW.sweep(route, SW.circle_profile(od / 2, 12)))
    E = pts[-1]
    P.cyl("node:port-b|M-CABLE-GREY", tuple(E - v * 0.0), tuple(E + v * 3.0), od / 2)                    # the jacket's cut end (it lands in the motor's gland)
    P.pivot("port-b", "port", tuple(E), axis=tuple(v), range=(0, 0), unit="480V-3P+E", gender="none")   # PIN-002: a jacket end in a gland (OPERATING.md 6)
    up = np.array([0, 0, 1.0]) if abs(v[2]) < 0.9 else np.array([1.0, 0, 0]); u = np.cross(v, up); u /= np.linalg.norm(u); w = np.cross(v, u)
    yaw, pitch = _yp_into(v); off = od / 4
    for k, (pole, col) in enumerate(zip(POLES, cols)):
        o = u * off * math.cos(math.pi / 4 + k * math.pi / 2) + w * off * math.sin(math.pi / 4 + k * math.pi / 2)
        tip = E + v * TAIL + o * 3.0
        library.place(P, dict(element="wire", version="1.0", tag=f"core-{pole.lower()}", parent="", x=tip[0], y=tip[1], z=tip[2], yaw=yaw, pitch=pitch,
                              params=dict(size=size, colour=col, length=TAIL + 2.0, strip=strip, ferrule=ferrule, conditions="/".join(cond.get(pole, [])))))
    allp = np.vstack([route, [E + v * (TAIL + 5)], [[0, 0, 0]]]); lo = allp.min(axis=0) - PLUG_R; hi = allp.max(axis=0) + PLUG_R
    P.collider("env", *lo, *(hi - lo))
    return P

PREVIEWS = [dict(name="4 m, plug end", az=250, el=20, center=(0, -60, 0), height=160), dict(name="core ends at the motor", az=250, el=25, center=(0, -3880, 0), height=160)]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
