"""Swept and lofted shapes as `mesh` primitives: a 2D profile carried along a 3D path (frames by parallel transport), rounded
outlines, and extruded plates. Used for anything a box and a cylinder cannot say: glasses frames, cables, handles, hoses."""
import math
import numpy as np

def rounded_outline(corners, radii, per_arc=10):
    """closed 2D outline through `corners` with each corner rounded to its radius; returns an (N,2) array, counter-clockwise"""
    pts = []; n = len(corners); C = [np.array(c, float) for c in corners]
    for i in range(n):
        p0, p1, p2 = C[i - 1], C[i], C[(i + 1) % n]; r = radii[i]
        d0 = p0 - p1; d0 /= np.linalg.norm(d0); d2 = p2 - p1; d2 /= np.linalg.norm(d2)
        ang = math.acos(np.clip(d0 @ d2, -1, 1)); t = r / math.tan(ang / 2)
        a, b = p1 + d0 * t, p1 + d2 * t
        bis = d0 + d2; bis /= np.linalg.norm(bis); centre = p1 + bis * (r / math.sin(ang / 2))
        a0 = math.atan2(*(a - centre)[::-1]); a1 = math.atan2(*(b - centre)[::-1])
        da = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        pts += [centre + r * np.array([math.cos(a0 + da * k / per_arc), math.sin(a0 + da * k / per_arc)]) for k in range(per_arc + 1)]
    return np.array(pts)

def resample(path, step):
    """resample a polyline (closed if its first and last points coincide) to roughly equal `step`"""
    P = np.array(path, float); seg = np.linalg.norm(np.diff(P, axis=0), axis=1); L = seg.sum(); n = max(4, int(round(L / step)))
    s = np.concatenate([[0], np.cumsum(seg)]); u = np.linspace(0, L, n + 1)
    return np.array([np.array([np.interp(x, s, P[:, k]) for k in range(3)]) for x in u])

def sweep(path, profile, closed=False, up=(0, 0, 1.0)):
    """carry a 2D profile [(a, b), ...] along a 3D path; the profile's a axis follows the transported normal, b the binormal.
    A planar path (every closed one we draw) uses the plane normal as a constant frame, so a closed loop meets itself exactly.
    Returns outward-facing triangles for a counter-clockwise profile."""
    P = np.array(path, float)
    if closed and np.linalg.norm(P[0] - P[-1]) < 1e-9: P = P[:-1]
    n = len(P); T = np.zeros((n, 3))
    for i in range(n):
        a = P[(i - 1) % n] if closed else P[max(i - 1, 0)]; b = P[(i + 1) % n] if closed else P[min(i + 1, n - 1)]
        T[i] = b - a; T[i] /= np.linalg.norm(T[i])
    # planar?  the mean binormal of successive tangents
    cr = np.array([np.cross(T[i], T[(i + 1) % n]) for i in range(n - (0 if closed else 1))]); nrm = cr.sum(axis=0)
    planar = np.linalg.norm(nrm) > 1e-6 and all(abs(np.dot(T[i], nrm / np.linalg.norm(nrm))) < 1e-3 for i in range(n))
    N = np.zeros((n, 3))
    if planar:
        pn = nrm / np.linalg.norm(nrm)
        for i in range(n): N[i] = pn
    else:
        u0 = np.array(up, float); N[0] = np.cross(T[0], u0) if abs(T[0] @ u0) < 0.98 else np.cross(T[0], [1.0, 0, 0])
        N[0] -= T[0] * (N[0] @ T[0]); N[0] /= np.linalg.norm(N[0])
        for i in range(1, n):
            v = N[i - 1] - T[i] * (N[i - 1] @ T[i]); N[i] = v / np.linalg.norm(v)
    B = np.cross(T, N)
    rings = [[P[i] + N[i] * a + B[i] * b for a, b in profile] for i in range(n)]
    m = len(profile); tris = []
    segs = n if closed else n - 1
    for i in range(segs):
        r0, r1 = rings[i], rings[(i + 1) % n]
        for j in range(m):
            k = (j + 1) % m
            tris.append((tuple(r0[j]), tuple(r1[j]), tuple(r1[k]))); tris.append((tuple(r0[j]), tuple(r1[k]), tuple(r0[k])))
    if not closed:
        c0, c1 = rings[0], rings[-1]; m0 = np.mean(c0, axis=0); m1 = np.mean(c1, axis=0)
        for j in range(m):
            k = (j + 1) % m; tris.append((tuple(m0), tuple(c0[j]), tuple(c0[k]))); tris.append((tuple(m1), tuple(c1[k]), tuple(c1[j])))
    # orientation: make the signed volume positive (profile handedness vs frame handedness)
    vol = sum(np.dot(a, np.cross(b, c)) for a, b, c in ((np.array(t[0]), np.array(t[1]), np.array(t[2])) for t in tris)) / 6.0
    if vol < 0: tris = [(t[0], t[2], t[1]) for t in tris]
    return tris

def rounded_rect_profile(w, h, r, per_arc=4):
    """2D profile of a w × h rounded rectangle centred on the origin"""
    return [tuple(p) for p in rounded_outline([(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)], [r] * 4, per_arc)]

def circle_profile(r, n=16):
    return [(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n)) for i in range(n)]

def plate(outline, to3d, thickness, normal):
    """extrude a closed 2D outline into a plate: to3d maps (a, b) -> 3D point on the front face; `normal` is the unit extrusion direction.
    Triangulated as a fan from the centroid (fine for convex and gently concave outlines like a lens)."""
    O = np.array(outline, float); c = O.mean(axis=0); nrm = np.array(normal, float) * thickness
    F = [np.array(to3d(*p)) for p in O]; fc = np.array(to3d(*c)); Bk = [p + nrm for p in F]; bc = fc + nrm
    tris = []; m = len(F)
    for j in range(m):
        k = (j + 1) % m
        tris.append((tuple(fc), tuple(F[j]), tuple(F[k]))); tris.append((tuple(bc), tuple(Bk[k]), tuple(Bk[j])))
        tris.append((tuple(F[j]), tuple(Bk[j]), tuple(Bk[k]))); tris.append((tuple(F[j]), tuple(Bk[k]), tuple(F[k])))
    return tris
