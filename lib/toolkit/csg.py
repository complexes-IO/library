"""Holes and cut-outs in the mesh: the glTF and the previews get the same openings AutoCAD makes with SUBTRACT.
  cut_solid(kind, q, subs)   faces of one solid minus its holes / cuts: (faces, method)
      method "extrude"  the target is rebuilt as an extrusion of its section along one of its axes, every opening parallel to that axis
                        as a stepped bore (through, blind from either face, counterbored, internal undercut). End faces are triangulated
                        with their openings (ear clipping with hole bridging): a closed shell, every edge used twice.
      method "bsp"      anything else (openings across two axes, overlapping openings, notches through an edge): a BSP boolean
                        (the csg.js algorithm). Closed in volume, but split faces meet in T-junctions.
      method "plain"    nothing to see: every opening is internal or misses the solid; the primitive's own faces are right.
      method None       not cut (a swept mesh: AutoCAD does not build meshes either). The validation suite reports it (GEO-060).
Hole polygons start at the same angle, with the same facet count (segments(r)), as the preview prism of a cylinder on the same axis,
so a pin in its bore matches facet for facet."""
import math, sys
import numpy as np

N = 20                       # sides of a cylinder or hole above 2.5 mm radius (the preview prism uses segments() too)
EPS = 1e-6

FACETS = None                # the facet count of the Prims being meshed, when it states its own (Prims.facets; toolkit/preview.py sets it for the
                             # length of one mesh() and puts it back). None: the library's counts below. EM 2026-11-20: round holes on the parts the home
                             # page shows close; the Blender gate's count of non-manifold edges is checked at the build for such an element (qa.py)

def segments(r):
    """facets of a cylinder or hole of radius r in the mesh: small contacts and pins stay light, holes match the pins in them"""
    if FACETS: return 8 if r <= 0.5 else FACETS
    return 8 if r <= 1.0 else 12 if r <= 2.5 else N

def _ring_phase(d):
    """the direction of the preview prism's first vertex for a cylinder along d"""
    d = np.asarray(d, float); d = d / np.linalg.norm(d)
    up = np.array([0, 0, 1.0]) if abs(d[2]) < 0.99 else np.array([1.0, 0, 0]); u = np.cross(d, up); return u / np.linalg.norm(u)

# ------------------------------------------------------------------ 2-D: polygon with holes -> triangles (ear clipping, hole bridging)
def _area(P): return 0.5 * sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P)))

def _ccw(P): return P if _area(P) > 0 else P[::-1]

def _seg_cross(a, b, c, d):
    """proper intersection of segments ab and cd (touching at an endpoint does not count)"""
    def o(p, q, r): return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    d1, d2, d3, d4 = o(c, d, a), o(c, d, b), o(a, b, c), o(a, b, d)
    return ((d1 > EPS and d2 < -EPS) or (d1 < -EPS and d2 > EPS)) and ((d3 > EPS and d4 < -EPS) or (d3 < -EPS and d4 > EPS))

def _bridge(poly, hole, others):
    """join a clockwise hole into the counter-clockwise outline through its rightmost vertex and the nearest vertex it can see"""
    m = max(range(len(hole)), key=lambda i: (hole[i][0], -hole[i][1])); M = hole[m]
    edges = [(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly))] + [(h[i], h[(i + 1) % len(h)]) for h in [hole] + others for i in range(len(h))]
    for j in sorted(range(len(poly)), key=lambda j: (poly[j][0] - M[0]) ** 2 + (poly[j][1] - M[1]) ** 2):
        P = poly[j]
        if any(_seg_cross(M, P, a, b) for a, b in edges): continue
        return poly[:j + 1] + hole[m:] + hole[:m + 1] + [poly[j]] + poly[j + 1:]
    return None

def _in_tri(p, a, b, c):
    def s(p1, p2, p3): return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    d1, d2, d3 = s(p, a, b), s(p, b, c), s(p, c, a)
    return not (((d1 < -EPS) or (d2 < -EPS) or (d3 < -EPS)) and ((d1 > EPS) or (d2 > EPS) or (d3 > EPS)))

def triangulate(outer, holes):
    """outer and holes as point lists in any orientation; counter-clockwise triangles, or None"""
    poly = _ccw([tuple(p) for p in outer])
    H = [_ccw([tuple(p) for p in h])[::-1] for h in holes]
    H.sort(key=lambda h: -max(p[0] for p in h))
    for k, h in enumerate(H):
        poly = _bridge(poly, h, H[k + 1:])
        if poly is None: return None
    V = list(range(len(poly))); tris = []; guard = 0
    while len(V) > 3 and guard < 4 * len(poly) * len(poly):
        guard += 1; n = len(V); found = False
        for i in range(n):
            ia, ib, ic = V[i - 1], V[i], V[(i + 1) % n]; a, b, c = poly[ia], poly[ib], poly[ic]
            if (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) <= EPS: continue        # reflex or flat
            if any(poly[jj] not in (a, b, c) and _in_tri(poly[jj], a, b, c) for jj in V if jj not in (ia, ib, ic)): continue
            tris.append((a, b, c)); V.pop(i); found = True; break
        if not found:                                                      # a flat vertex blocks progress: drop it, else give up
            for i in range(len(V)):
                a, b, c = poly[V[i - 1]], poly[V[i]], poly[V[(i + 1) % len(V)]]
                if abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) <= EPS: V.pop(i); found = True; break
            if not found: return None
    if len(V) == 3: tris.append(tuple(poly[v] for v in V))
    return tris

def _convex_disjoint(A, B):
    """separating-axis test for two convex polygons (2-D)"""
    for P in (A, B):
        for i in range(len(P)):
            e = (P[(i + 1) % len(P)][0] - P[i][0], P[(i + 1) % len(P)][1] - P[i][1]); n = (-e[1], e[0])
            pa = [n[0] * p[0] + n[1] * p[1] for p in A]; pb = [n[0] * p[0] + n[1] * p[1] for p in B]
            if max(pa) < min(pb) + EPS or max(pb) < min(pa) + EPS: return True
    return False

def _inside_convex(P, C):
    """every vertex of P strictly inside convex polygon C (counter-clockwise)"""
    for i in range(len(C)):
        a, b = C[i], C[(i + 1) % len(C)]
        for p in P:
            if (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) <= 1e-4: return False
    return True

def _pt_in_poly(p, P):
    c = False
    for i in range(len(P)):
        (x1, y1), (x2, y2) = P[i], P[(i + 1) % len(P)]
        if (y1 > p[1]) != (y2 > p[1]) and p[0] < x1 + (p[1] - y1) * (x2 - x1) / (y2 - y1): c = not c
    return c

def _inside_poly(Q, P):
    """polygon Q strictly inside polygon P (any shape): every vertex inside, no edges crossing"""
    if not all(_pt_in_poly(q, P) for q in Q): return False
    for i in range(len(Q)):
        a, b = Q[i], Q[(i + 1) % len(Q)]
        for j in range(len(P)):
            if _seg_cross(a, b, P[j], P[(j + 1) % len(P)]): return False
    return True

def _diff(A, B):
    """A minus B for two counter-clockwise polygons where B bites one stretch of A's boundary (a keyway, a notch): one polygon, or None"""
    A, B = _ccw(list(A)), _ccw(list(B)); ev = []
    for i in range(len(A)):
        a0, a1 = A[i], A[(i + 1) % len(A)]
        for j in range(len(B)):
            b0, b1 = B[j], B[(j + 1) % len(B)]
            d = (a1[0] - a0[0]) * (b1[1] - b0[1]) - (a1[1] - a0[1]) * (b1[0] - b0[0])
            if abs(d) < 1e-12: continue
            t = ((b0[0] - a0[0]) * (b1[1] - b0[1]) - (b0[1] - a0[1]) * (b1[0] - b0[0])) / d
            u = ((b0[0] - a0[0]) * (a1[1] - a0[1]) - (b0[1] - a0[1]) * (a1[0] - a0[0])) / d
            if 1e-9 < t < 1 - 1e-9 and 1e-9 < u < 1 - 1e-9: ev.append((i, t, j, (a0[0] + (a1[0] - a0[0]) * t, a0[1] + (a1[1] - a0[1]) * t)))
    if len(ev) != 2: return None
    ev.sort(key=lambda e: (e[0], e[1]))
    def mid(e1, e2):                                                       # a point on A's boundary between two events
        i = e1[0]; a0, a1 = A[i], A[(i + 1) % len(A)]; t = (e1[1] + (e2[1] if e2[0] == i else 1.0)) / 2
        return (a0[0] + (a1[0] - a0[0]) * t, a0[1] + (a1[1] - a0[1]) * t)
    e_in, e_out = (ev[0], ev[1]) if _pt_in_poly(mid(ev[0], ev[1]), B) else (ev[1], ev[0])
    out = [e_out[3]]; n = len(A); k = (e_out[0] + 1) % n
    while True:                                                            # along A from the exit to the entry
        if _pt_in_poly(A[k], B): return None                               # B swallows a vertex outside the bite: not a simple bite
        out.append(A[k])
        if k == e_in[0]: break
        k = (k + 1) % n
    out.append(e_in[3])
    j = e_in[2]; m = len(B)                                                # along B backwards, from the entry to the exit, inside A
    while True:
        out.append(B[j])
        if j == (e_out[2] + 1) % m: break
        j = (j - 1) % m
        if len(out) > len(A) + len(B) + 4: return None
    return out if _area(out) > 0 else None

# ------------------------------------------------------------------ 3-D: a target as an extrusion with stepped bores
def _frames(k, q):
    """(origin, u, v, a, section polygon in (u, v), length along a) per axis of the target, right-handed (u x v = a)"""
    if k == "box":
        x, y, z, dx, dy, dz = q; lo = np.minimum([x, y, z], [x + dx, y + dy, z + dz]); hi = np.maximum([x, y, z], [x + dx, y + dy, z + dz])
        o, E, S = lo, list(np.eye(3)), list(hi - lo)
    elif k == "obox":
        o, ex, ey, ez, l, w, h = q; o = np.array(o, float); E = [np.array(e, float) for e in (ex, ey, ez)]; S = [float(l), float(w), float(h)]
        for i in range(3):
            if S[i] < 0: o = o + E[i] * S[i]; S[i] = -S[i]
        if np.cross(E[0], E[1]) @ E[2] < 0: o = o + E[0] * S[0]; E[0] = -E[0]
    elif k == "cyl":
        p1, p2, R = np.array(q[0], float), np.array(q[1], float), float(q[2]); d = p2 - p1; T = float(np.linalg.norm(d)); a = d / T
        u = _ring_phase(a); v = np.cross(a, u); n = segments(R)
        return [(p1, u, v, a, [(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n)) for i in range(n)], T)]
    else: return []
    out = []
    for ax in range(3):
        U, V = S[(ax + 1) % 3], S[(ax + 2) % 3]
        out.append((o, E[(ax + 1) % 3], E[(ax + 2) % 3], E[ax], [(0.0, 0.0), (U, 0.0), (U, V), (0.0, V)], S[ax]))
    return out

def _opening(o, u, v, a, hk, hq):
    """one hole or cut seen along a: (shape, depth from, depth to) with shape ("c", centre, r, phase) or ("r", polygon); False if not parallel"""
    if hk in ("hole", "cyl"):
        q1, q2, r = np.array(hq[0], float), np.array(hq[1], float), float(hq[2]); dd = q2 - q1; L = np.linalg.norm(dd)
        if L < EPS or abs(abs(dd @ a) / L - 1) > 1e-6: return False
        uh = _ring_phase(dd); ph = math.atan2(uh @ v, uh @ u) % (2 * math.pi / segments(r))
        s0, s1 = sorted(((q1 - o) @ a, (q2 - o) @ a))
        return ("c", (round(float((q1 - o) @ u), 6), round(float((q1 - o) @ v), 6)), r, ph), s0, s1
    co, cx, cy, cz, l, w, h = hq[:7]; co = np.array(co, float); E = [np.array(e, float) for e in (cx, cy, cz)]; S = [l, w, h]
    ax = [i for i in range(3) if abs(abs(E[i] @ a) - 1) < 1e-6]
    if len(ax) != 1: return False
    i = ax[0]; o1, o2 = [j for j in range(3) if j != i]
    pts = [co + E[o1] * S[o1] * sa + E[o2] * S[o2] * sb for sa, sb in ((0, 0), (1, 0), (1, 1), (0, 1))]
    s0, s1 = sorted(((co - o) @ a, (co + E[i] * S[i] - o) @ a))
    return ("r", tuple(_ccw([(float((p - o) @ u), float((p - o) @ v)) for p in pts]))), s0, s1

def _poly(sh):
    if sh[0] == "r": return list(sh[1])
    (cx, cy), r, ph = sh[1], sh[2], sh[3]; n = segments(r)
    return [(cx + r * math.cos(ph + 2 * math.pi * i / n), cy + r * math.sin(ph + 2 * math.pi * i / n)) for i in range(n)]

def _size(sh): return 0.0 if sh is None else (sh[2] if sh[0] == "c" else 1e9)

def _extrude(o, u, v, a, outer, T, subs):
    """the extrusion of `outer` 0..T along a minus subs; None when an opening is not parallel to a, overlaps another or crosses the edge;
    "plain" when nothing shows"""
    outer = _ccw(outer); groups = []                                       # [key, [(shape, d0, d1)]]: coaxial circles share a key
    for hk, hq in subs:
        r = _opening(o, u, v, a, hk, hq)
        if r is False: return None
        sh, s0, s1 = r; d0, d1 = max(0.0, s0), min(T, s1)
        if d1 - d0 <= EPS: continue
        if _convex_disjoint(_poly(sh), outer): continue                     # misses the solid
        key = ("c", sh[1]) if sh[0] == "c" else ("r", len(groups))
        for g in groups:
            if g[0] == key: g[1].append((sh, d0, d1)); break
        else: groups.append([key, [(sh, d0, d1)]])
    notch = [g for g in groups if len(g[1]) == 1 and g[1][0][1] <= EPS and g[1][0][2] >= T - EPS and not _inside_convex(_poly(g[1][0][0]), outer)]
    for g in notch:                                                        # a through-opening across the edge: the section itself changes
        outer = _diff(outer, _poly(g[1][0][0]))
        if outer is None: return None
    groups = [g for g in groups if g not in notch]
    inner = [g for g in groups if not any(d0 <= EPS or d1 >= T - EPS for _, d0, d1 in g[1])]
    for g in inner:                                                        # a cavity that reaches no end face shows only if it breaks a side
        if not _inside_poly(_poly(max((s_ for s_, _, _ in g[1]), key=_size)), outer): return None
    groups = [g for g in groups if g not in inner]                          # true internal cavities do not show
    if not groups and not notch: return "plain"
    env = [_poly(max((s for s, _, _ in g[1]), key=_size)) for g in groups]              # each group's largest opening
    for i in range(len(env)):
        if not _inside_poly(env[i], outer): return None                                    # a partial notch through an edge: BSP
        for j in range(i + 1, len(env)):
            if not _convex_disjoint(env[i], env[j]): return None                           # openings that run into each other
    def at(g, depth):
        act = [s for s, d0, d1 in g[1] if d0 - EPS <= depth <= d1 + EPS]
        return max(act, key=_size) if act else None
    def to3(p2, depth): return tuple(o + u * p2[0] + v * p2[1] + a * depth)
    faces = []
    n = len(outer)
    for i in range(n):                                                     # outer walls, outward
        p, q2 = outer[i], outer[(i + 1) % n]; faces.append([to3(p, 0), to3(q2, 0), to3(q2, T), to3(p, T)])
    for depth, flip in ((0.0, True), (T, False)):                           # end faces with their openings
        tr = triangulate(outer, [_poly(at(g, depth)) for g in groups if at(g, depth) is not None])
        if tr is None: return None
        for t in tr: faces.append([to3(p, depth) for p in (t[::-1] if flip else t)])
    for g in groups:                                                       # bores: an inward wall per layer, a step between layers
        bps = sorted({0.0, T} | {d for _, d0, d1 in g[1] for d in (d0, d1)})
        for z0, z1 in zip(bps, bps[1:]):
            sh = at(g, (z0 + z1) / 2)
            if sh is None: continue
            P = _poly(sh); m = len(P)
            for i in range(m): p, q2 = P[i], P[(i + 1) % m]; faces.append([to3(q2, z0), to3(p, z0), to3(p, z1), to3(q2, z1)])
        for z in bps:
            if z <= EPS or z >= T - EPS: continue
            lo_, hi_ = at(g, z - 1e-4), at(g, z + 1e-4)
            if lo_ == hi_: continue
            big, small, up = (lo_, hi_, False) if _size(lo_) > _size(hi_) else (hi_, lo_, True)   # the step faces the larger opening
            Pb = _poly(big)
            if small is None: tr = triangulate(Pb, [])
            elif big[0] == small[0] == "c" and segments(big[2]) == segments(small[2]) and abs(big[3] - small[3]) < 1e-9:
                Ps = _poly(small); tr = []; nb = len(Pb)
                for i in range(nb): j = (i + 1) % nb; tr += [(Pb[i], Pb[j], Ps[j]), (Pb[i], Ps[j], Ps[i])]
            else: tr = triangulate(Pb, [_poly(small)]) if _inside_convex(_poly(small), _ccw(Pb)) else None
            if tr is None: return None
            for t in tr: faces.append([to3(p, z) for p in (t if up else t[::-1])])
    return faces

# ------------------------------------------------------------------ BSP boolean (csg.js), for whatever the extrusion cannot do
EPS_B = 1e-5

class _Poly:
    __slots__ = ("v", "n", "w")
    def __init__(self, v, n=None, w=None):
        self.v = np.asarray(v, float)
        if n is None:
            c = self.v; nx = np.roll(c, -1, axis=0)
            n = np.array([((c[:, 1] - nx[:, 1]) * (c[:, 2] + nx[:, 2])).sum(), ((c[:, 2] - nx[:, 2]) * (c[:, 0] + nx[:, 0])).sum(), ((c[:, 0] - nx[:, 0]) * (c[:, 1] + nx[:, 1])).sum()])
            n = n / np.linalg.norm(n); w = float(n @ c[0])
        self.n, self.w = n, w
    def flip(self): return _Poly(self.v[::-1], -self.n, -self.w)

def _split(n, w, p, cf, cb, f, b):
    t = p.v @ n - w; ty = np.where(t < -EPS_B, 2, np.where(t > EPS_B, 1, 0)); kind = int(np.bitwise_or.reduce(ty))
    if kind == 0: (cf if n @ p.n > 0 else cb).append(p)
    elif kind == 1: f.append(p)
    elif kind == 2: b.append(p)
    else:
        F, B = [], []; m = len(p.v)
        for i in range(m):
            j = (i + 1) % m; ti, tj = ty[i], ty[j]; vi, vj = p.v[i], p.v[j]
            if ti != 2: F.append(vi)
            if ti != 1: B.append(vi)
            if (ti | tj) == 3: s = (w - n @ vi) / (n @ (vj - vi)); x = vi + (vj - vi) * s; F.append(x); B.append(x)
        if len(F) >= 3: f.append(_Poly(F, p.n, p.w))
        if len(B) >= 3: b.append(_Poly(B, p.n, p.w))

class _Node:
    def __init__(self, polys=None):
        self.n = None; self.w = None; self.front = None; self.back = None; self.polys = []
        if polys: self.build(polys)
    def _all_nodes(self):
        st = [self]; out = []
        while st:
            x = st.pop(); out.append(x); st += [c for c in (x.front, x.back) if c]
        return out
    def invert(self):
        for x in self._all_nodes():
            x.polys = [p.flip() for p in x.polys]
            if x.n is not None: x.n, x.w = -x.n, -x.w
            x.front, x.back = x.back, x.front
    def clip_polys(self, polys):
        if self.n is None: return list(polys)
        f, b = [], []
        for p in polys: _split(self.n, self.w, p, f, b, f, b)
        if self.front: f = self.front.clip_polys(f)
        b = self.back.clip_polys(b) if self.back else []
        return f + b
    def clip_to(self, bsp):
        for x in self._all_nodes(): x.polys = bsp.clip_polys(x.polys)
    def all_polys(self): return [p for x in self._all_nodes() for p in x.polys]
    def build(self, polys):
        if not polys: return
        if self.n is None: self.n, self.w = polys[0].n, polys[0].w
        f, b = [], []
        for p in polys: _split(self.n, self.w, p, self.polys, self.polys, f, b)
        if f:
            if not self.front: self.front = _Node()
            self.front.build(f)
        if b:
            if not self.back: self.back = _Node()
            self.back.build(b)

def _subtract(A, B):
    a, b = _Node(A), _Node(B)
    a.invert(); a.clip_to(b); b.clip_to(a); b.invert(); b.clip_to(a); b.invert(); a.build(b.all_polys()); a.invert()
    return a.all_polys()

def polygons(k, q):
    """outward convex faces of one analytic primitive (box, obox, cyl, hole, cut) as point lists"""
    if k == "box":
        x, y, z, dx, dy, dz = q; k, q = "obox", ((x, y, z), (1, 0, 0), (0, 1, 0), (0, 0, 1), dx, dy, dz)
    if k in ("obox", "cut"):
        (o, ex, ey, ez, l, w, h) = q[:7]; o = np.array(o, float); ex, ey, ez = (np.array(e, float) for e in (ex, ey, ez))
        o = o + ex * min(l, 0) + ey * min(w, 0) + ez * min(h, 0); l, w, h = abs(l), abs(w), abs(h)
        if np.cross(ex, ey) @ ez < 0: o = o + ex * l; ex = -ex
        cs = [o + ex * l * sx + ey * w * sy + ez * h * sz for sz in (0, 1) for (sx, sy) in ((0, 0), (1, 0), (1, 1), (0, 1))]
        return [[tuple(cs[i]) for i in f] for f in [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]]
    if k in ("cyl", "hole"):
        c1, c2, r = np.array(q[0], float), np.array(q[1], float), float(q[2]); d = c2 - c1; h = np.linalg.norm(d)
        if h < EPS: return None
        d = d / h; u = _ring_phase(d); v = np.cross(d, u); n = segments(r)
        ring = [c1 + (u * math.cos(2 * math.pi * i / n) + v * math.sin(2 * math.pi * i / n)) * r for i in range(n)]
        F = [[tuple(ring[i]), tuple(ring[(i + 1) % n]), tuple(ring[(i + 1) % n] + d * h), tuple(ring[i] + d * h)] for i in range(n)]
        return F + [[tuple(p) for p in reversed(ring)], [tuple(p + d * h) for p in ring]]
    return None

def _bsp(k, q, subs):
    A = polygons(k, q)
    if A is None: return None
    old = sys.getrecursionlimit(); sys.setrecursionlimit(max(old, 20000))
    try:
        R = [_Poly(f) for f in A]
        for hk, hq in subs:
            B = polygons(hk, hq)
            if B and all(np.isfinite(np.array(f, float)).all() for f in B): R = _subtract(R, [_Poly(f) for f in B])
    finally: sys.setrecursionlimit(old)
    out = []
    for p in R:
        V = np.round(p.v, 6); ar = np.linalg.norm(sum(np.cross(V[i] - V[0], V[i + 1] - V[0]) for i in range(1, len(V) - 1)))
        if ar > 1e-8: out.append(V)
    return _close_t(_merge(_weld(out, fan=False)))

def _close_t(polys, tol=1e-5, rounds=4):
    """the T-junctions a triangulation can leave where a straight run of one face meets a vertex of the next (a collinear point it
    clipped away): every edge used once is split at the mesh's vertices lying on it, its triangle split with it (round 5: two LioN-X
    inserts came out open). Zero-area slivers are dropped first, so the neighbour across them is split instead. A face whose edge has
    no vertex on it is left as it is."""
    def k(p): return tuple(round(float(c), 5) for c in p)
    tris = []
    for ps in polys:
        P = [tuple(float(c) for c in p) for p in ps]
        tris += [[P[0], P[i], P[i + 1]] for i in range(1, len(P) - 1)]
    def flat(t): A = np.array(t, float); return np.linalg.norm(np.cross(A[1] - A[0], A[2] - A[0])) < 1e-6
    for _ in range(rounds):
        tris = [t for t in tris if not flat(t)]                              # a zero-area sliver closes nothing: split its neighbour instead
        cnt = {}
        for t in tris:
            for i in range(3): cnt[(k(t[i]), k(t[(i + 1) % 3]))] = cnt.get((k(t[i]), k(t[(i + 1) % 3])), 0) + 1
        open_ = {e for e, c in cnt.items() if cnt.get((e[1], e[0]), 0) != c}
        if not open_: break
        allv = np.array(sorted({v for t in tris for v in map(k, t)}), float); changed = False; out = []
        for t in tris:
            done = False
            for i in range(3):
                a_, b_ = np.array(t[i]), np.array(t[(i + 1) % 3]); c_ = t[(i + 2) % 3]
                if (k(a_), k(b_)) not in open_: continue
                d = b_ - a_; L2 = d @ d
                if L2 < 1e-12: continue
                lo, hi = np.minimum(a_, b_) - tol, np.maximum(a_, b_) + tol
                C = allv[np.all((allv >= lo) & (allv <= hi), axis=1)]
                tt = (C - a_) @ d / L2; off = np.linalg.norm(C - a_ - np.outer(tt, d), axis=1)
                m = (tt > 1e-6) & (tt < 1 - 1e-6) & (off < tol)
                if not m.any(): continue
                pts = [tuple(a_)] + [tuple(C[m][j]) for j in np.argsort(tt[m])] + [tuple(b_)]
                out += [[pts[j], pts[j + 1], c_] for j in range(len(pts) - 1)]; done = changed = True; break
            if not done: out.append(t)
        tris = out
        if not changed: break
    return [t for t in tris if not flat(t)]

def _weld(polys, fan=True):
    """close the T-junctions a BSP boolean leaves: every vertex lying on another face's edge is inserted into that edge, and a face that
    gained vertices is fanned from its centroid (no sliver triangles; fan=False keeps it one polygon). The result is watertight."""
    if not polys: return []
    allv = np.unique(np.concatenate(polys), axis=0); out = []
    for V in polys:
        new = []; grew = False
        for i in range(len(V)):
            a, b = V[i], V[(i + 1) % len(V)]; d = b - a; L2 = d @ d; new.append(a)
            if L2 < 1e-12: continue
            lo, hi = np.minimum(a, b) - 1e-5, np.maximum(a, b) + 1e-5
            C = allv[np.all((allv >= lo) & (allv <= hi), axis=1)]
            if len(C) <= 2: continue
            t = (C - a) @ d / L2; off = np.linalg.norm(C - a - np.outer(t, d), axis=1)
            m = (t > 1e-7) & (t < 1 - 1e-7) & (off < 1e-5)
            if m.any():
                for j in np.argsort(t[m]): new.append(C[m][j])
                grew = True
        if not grew or not fan: out.append([tuple(x) for x in (new if grew else V)]); continue
        c = tuple(np.mean(V, axis=0))
        for i in range(len(new)): out.append([c, tuple(new[i]), tuple(new[(i + 1) % len(new)])])
    return out

def _merge(polys):
    """the fragments a BSP boolean leaves on one plane, joined again: per plane the boundary edges (welded, so shared edges cancel) are
    chained into loops; a vertex that is a corner of no loop (a split point on a straight edge) is dropped from every loop, so faces
    still meet edge to edge; holes go to the loop around them and each face is triangulated once. A plane it cannot join keeps its fan."""
    def k4(p): return tuple(round(float(c), 4) for c in p)
    groups = {}
    for ps in polys:
        P = np.array(ps, float); n = np.zeros(3)
        for i in range(len(P)): n += np.cross(P[i], P[(i + 1) % len(P)])
        nn = np.linalg.norm(n)
        if nn < 1e-12: continue
        n /= nn; key = (tuple(np.round(n, 4)), round(float(n @ P[0]), 4)); groups.setdefault(key, []).append(ps)
    rep = {}; planes = []; corner = set(); out = []
    for (nk, w), G in groups.items():
        cnt = {}
        for ps in G:
            for i in range(len(ps)):
                a, b = k4(ps[i]), k4(ps[(i + 1) % len(ps)]); rep.setdefault(a, ps[i]); rep.setdefault(b, ps[(i + 1) % len(ps)])
                cnt[(a, b)] = cnt.get((a, b), 0) + 1
        bnd = {}; ok = True
        for (a, b), c in cnt.items():
            d = c - cnt.get((b, a), 0)
            if d == 1:
                if a in bnd: ok = False; break
                bnd[a] = b
            elif d not in (0, -1): ok = False; break
        loops = []
        while ok and bnd:
            a0 = next(iter(bnd)); loop = [a0]; a = bnd.pop(a0)
            while a != a0:
                if a not in bnd or len(loop) > 100000: ok = False; break
                loop.append(a); a = bnd.pop(a)
            loops.append(loop)
        if not ok or not loops:
            for ps in G:
                corner.update(k4(p) for p in ps)
                c = tuple(np.mean(np.array(ps, float), axis=0))
                out += [[c, tuple(ps[i]), tuple(ps[(i + 1) % len(ps)])] for i in range(len(ps))] if len(ps) > 3 else [list(ps)]
            continue
        for loop in loops:
            m = len(loop)
            for i in range(m):
                A, B, C = (np.array(rep[loop[j]], float) for j in (i - 1, i, (i + 1) % m))
                e1, e2 = B - A, C - B
                if np.linalg.norm(np.cross(e1, e2)) > 1e-7 * max(np.linalg.norm(e1) * np.linalg.norm(e2), 1e-12): corner.add(loop[i])
        planes.append((np.array(nk, float), G, loops))
    def contains(P, pt):
        c = False
        for i in range(len(P)):
            (x1, y1), (x2, y2) = P[i], P[(i + 1) % len(P)]
            if (y1 > pt[1]) != (y2 > pt[1]) and pt[0] < x1 + (pt[1] - y1) * (x2 - x1) / (y2 - y1): c = not c
        return c
    for n, G, loops in planes:
        n = n / np.linalg.norm(n)
        up = np.array([0, 0, 1.0]) if abs(n[2]) < 0.9 else np.array([1.0, 0, 0]); u = np.cross(up, n); u /= np.linalg.norm(u); v = np.cross(n, u)
        to3 = {}; L2 = []
        for loop in loops:
            keep = [a for a in loop if a in corner]
            if len(keep) < 3: continue
            q = [(float(np.array(rep[a]) @ u), float(np.array(rep[a]) @ v)) for a in keep]
            for a, p2 in zip(keep, q): to3[p2] = rep[a]
            L2.append(q)
        outers = [q for q in L2 if _area(q) > 0]; holes = [q for q in L2 if _area(q) <= 0]
        own = {id(o): [] for o in outers}
        for h in holes:
            cand = [o for o in outers if contains(o, h[0])]
            if cand: own[id(min(cand, key=lambda o: abs(_area(o))))].append(h)
        tris = []
        for o in outers:
            tr = triangulate(o, own[id(o)])
            if tr is None: tris = None; break
            tris += [[tuple(to3[p]) for p in t] for t in tr]
        if tris is not None: out += tris; continue
        for ps in G:                                                       # triangulation failed on this plane: keep its fragments
            c = tuple(np.mean(np.array(ps, float), axis=0))
            out += [[c, tuple(ps[i]), tuple(ps[(i + 1) % len(ps)])] for i in range(len(ps))]
    return out

# ------------------------------------------------------------------ the one entry point
_CACHE = {}

def cut_solid(k, q, subs):
    """(faces, method) for target (k, q) minus subs [(kind, q), ...]; faces point outward. See the module docstring for the methods."""
    if not subs: return None, "plain"
    key = (k, repr(q), repr(subs), FACETS)
    if key in _CACHE: return _CACHE[key]
    res = (None, None)
    if k in ("box", "obox", "cyl"):
        for fr in _frames(k, q):
            r = _extrude(*fr, subs)
            if r == "plain": res = (None, "plain"); break
            if r is not None: res = (r, "extrude"); break
        else:
            try:
                f = _bsp(k, q, subs); res = (f, "bsp") if f else (None, None)
            except (RecursionError, ZeroDivisionError, FloatingPointError, ValueError): res = (None, None)
    if len(_CACHE) > 4000: _CACHE.clear()
    _CACHE[key] = res
    return res

def volume(faces):
    """signed volume of a closed outward shell (mm³): the self-test's measure"""
    v = 0.0
    for ps in faces:
        P = [np.array(p, float) for p in ps]
        for i in range(1, len(P) - 1): v += P[0] @ np.cross(P[i], P[i + 1]) / 6.0
    return v
