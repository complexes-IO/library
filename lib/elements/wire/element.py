#!/usr/bin/env python3
"""wire: one insulated conductor with its two prepared ends (stripped, or crimped in a ferrule), as its own element: an end stripped too
short, a nicked conductor or stray strands are properties of this part, and toolkit/contact.py terminate() decides what a clamp makes of
them. Frame: end A's tip at the origin, inserted along +y (into a clamp whose mouth faces -y); the wire runs toward -y and follows `path`.
Brief: references/measure.md."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
from toolkit import library, sweep as SW
from toolkit.prims import Prims, rotation_yp

ID, VERSION, CLASS = "wire", "1.0", "wire"
TITLE = "single insulated conductor, stranded copper, PVC, stripped or ferruled ends, routed"
TOOLKIT = "1.3"
BASELINE = "own design: conductor Ø from the cross-section; insulation thickness IEC 60227-3 class (Assumption: not on file); ferrules DIN 46228-4 class (Assumption)"
ORIGIN = "end A's conductor tip on the wire axis, inserted along +y; the wire leaves toward -y and follows `path`"
COMMAND = "WIRE"
PARAMS = dict(size=1.5, colour="M-BLUE", length=150.0, path=None, strip=10.0, ferrule=False, conditions="")
INSUL = {0.5: 0.6, 0.75: 0.6, 1.0: 0.6, 1.5: 0.7, 2.5: 0.8, 4.0: 0.8, 6.0: 0.8, 10.0: 1.0}      # mm insulation: Assumption (IEC 60227-3 class)
FERRULE_L = {0.5: 8.0, 0.75: 8.0, 1.0: 8.0, 1.5: 8.0, 2.5: 8.0, 4.0: 10.0, 6.0: 12.0, 10.0: 12.0}   # sleeve length: Assumption (DIN 46228-4 class)
STRAY = 4                                                                                         # strands drawn when an end has them out

def dims(size):
    """conductor Ø (area-equivalent, mm), insulation OD"""
    d = 2 * math.sqrt(float(size) / math.pi); t = INSUL.get(float(size), 0.8); return d, d + 2 * t + 0.2   # + 0.2: stranding lay

def _end(P, node, tip, a, size, strip, ferrule, cond, colour):
    """one prepared end: tip point, unit axis a (the way it goes into a clamp); returns the point where the insulation starts"""
    d, od = dims(size); r = d / 2; tip = np.asarray(tip, float); a = np.asarray(a, float) / np.linalg.norm(a)
    s = strip * (0.4 if cond == "under-stripped" else 1.8 if cond == "over-stripped" else 1.0)
    if ferrule:
        fl = FERRULE_L.get(float(size), 10.0)
        P.cyl(f"node:{node}|M-SILVER", tuple(tip - a * fl), tuple(tip), r + 0.15)                   # tinned copper sleeve
        P.cyl(f"node:{node}|{colour}", tuple(tip - a * (fl + 2.0)), tuple(tip - a * fl), od / 2 + 0.3)   # plastic collar
        zone = fl; ins = tip - a * (fl + 2.0)
    else:
        rc = r * (0.6 if cond == "nicked" else 1.0)
        P.cyl(f"node:{node}|M-CU", tuple(tip - a * s), tuple(tip - a * (s * 0.5)), r)
        P.cyl(f"node:{node}|M-CU", tuple(tip - a * (s * 0.5)), tuple(tip - a * (s * 0.4)), rc)      # a nick halfway down
        P.cyl(f"node:{node}|M-CU", tuple(tip - a * (s * 0.4)), tuple(tip), r)
        if cond == "strands-out":
            up = np.array([0, 0, 1.0]) if abs(a[2]) < 0.9 else np.array([1.0, 0, 0]); u = np.cross(a, up); u /= np.linalg.norm(u); v = np.cross(a, u)
            for k in range(STRAY):
                th = 2 * math.pi * k / STRAY; out = u * math.cos(th) + v * math.sin(th)
                P.cyl(f"node:{node}|M-CU", tuple(tip - a * (s * 0.7) + out * (r * 0.6)), tuple(tip - a * (s * 0.1) + out * (r + 1.6)), 0.12)
        zone = s; ins = tip - a * s
    P.pivot(node, "contact", tuple(tip), axis=tuple(a), range=(0.0, zone), unit="mm", gender="wire", size=float(size), d=d, ferrule=bool(ferrule), strip=s, condition=cond)
    return ins

def build(size=1.5, colour="M-BLUE", length=150.0, path=None, strip=10.0, ferrule=False, conditions=""):
    P = Prims(); d, od = dims(size)
    cond = {k.strip(): v.strip() for k, v in (p.split(":", 1) for p in str(conditions or "").replace(";", "/").split("/") if ":" in p)}
    a_ins = _end(P, "end-a", (0, 0, 0), (0, 1, 0), size, strip, ferrule, cond.get("a", "ok"), colour)
    cb = cond.get("b", "ok")
    reach = (FERRULE_L.get(float(size), 10.0) + 2.0) if ferrule else strip * (0.4 if cb == "under-stripped" else 1.8 if cb == "over-stripped" else 1.0)
    if path is None:                                                   # a straight run with a little sag; end B looks on along -y
        run = max(10.0, float(length) - abs(a_ins[1]) - reach)
        pts = [a_ins, a_ins + (0, -run * 0.5, -min(4.0, run * 0.05)), a_ins + (0, -run, 0)]
    else:
        pts = [a_ins, a_ins + (0, -5.0, 0)] + [np.array(p, float) for p in path]
    v = pts[-1] - pts[-2]; v /= np.linalg.norm(v)
    tip_b = pts[-1] + v * reach
    _end(P, "end-b", tip_b, v, size, strip, ferrule, cb, colour)
    run = sum(float(np.linalg.norm(np.array(b) - np.array(a))) for a, b in zip(pts, pts[1:]))
    route = SW.resample([tuple(p) for p in pts], max(3.0, run / 80.0))
    P.mesh(colour, SW.sweep(route, SW.circle_profile(od / 2, 10)))
    allp = np.vstack([route, [tip_b], [[0, 0, 0]]]); lo = allp.min(axis=0) - od; hi = allp.max(axis=0) + od
    P.collider("env", *lo, *(hi - lo))
    return P

PREVIEWS = [dict(name="1.5 mm2 blue, stripped", az=250, el=20, center=(0, -10, 0), height=30), dict(name="ferruled", az=250, el=20, center=(0, -10, 0), height=30, params=dict(ferrule=True)),
            dict(name="end A under-stripped, strands out at B", az=250, el=20, params=dict(conditions="a:under-stripped/b:strands-out"))]
if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
