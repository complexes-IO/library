"""Which edges of an element the AutoCAD gate fillets: one definition shared by the gate (acad-gate.py) and the validation suite.
An edge is picked when it is a convex outer edge of a box / oriented box / cylinder primitive, longer than MIN_EDGE, on a part at least
2.5 r thick, and NOT buried: its pick point is not inside, or within 0.05 mm of, another solid of the same element (holes respected).
Round 4 (2026-11-04): an edge another solid shares (two solids flush on one outline) is skipped as `shared`; a pick is made at a point
whose view, the outward bisector, no other solid blocks, else the edge is `hidden`; a circle is picked off its axis-aligned points, and
each edge carries alternates (point, view) for the gate to try when a pick selects nothing.
Round 5 (2026-11-04): the gate looks in 2D wireframe, where every edge shows whatever stands in front, and a pick takes the nearest
edge AutoCAD draws. So each try is scored by its clearance: how close any other edge, of any solid at any depth, passes to it in its
view (the A pins 0.015 from a male sleeve's diagonal points, the lid's edge exactly on the box rim's bisector). A circle is tried at
twelve points (the four diagonals, then the eight 22.5° points between them, never an axis-aligned seam point) and every edge from
three views (its faces' bisector, then leaning 2:1 toward each face). The first try with CLEAR is the pick and the next clear ones its
alternates; with none that clear, the clearest ones above MIN_CLEAR; with none above that, the edge is `crowded`.
A buried edge cannot be seen, needs no fillet, and a point pick on it can select the neighbouring solid instead: on the 2026-11-03 gate
run buried edges were 53 of 89 rejects on pbs-6h-22 and 137 of 177 on contactor-9a-1no1nc."""
import math
import numpy as np
from .solid import Scene, inside

MIN_EDGE = 3.0
EPS = 0.05
CLEAR = 0.25                   # mm in the view between a pick and the nearest other edge: clear (the gate zooms to a 10 mm window)
MIN_CLEAR = 0.02               # below this the other edge is on the pick (AutoCAD takes the nearest edge it draws): crowded
STEP = 0.1                     # mm between the points that stand for an edge
STRETCH = 0.5                  # mm: a single run this much shorter than its edge is a stretch a hole or cut left (round 10 c)
BATCH_VIEW = np.array([1.0, -1.0, 1.0]) / math.sqrt(3.0)
RADIUS = {"enclosure": 1.0, "rail": 1.0, "furniture": 1.0, "contact": 0.1, "wire": 0.1}   # mm by element class; default 0.5
# round 3 (2026-11-04): R 0.5 on 1 to 2 mm contacts and wire ends cannot work; a pin gets an edge break, not a die-cast round

def radius(cls=None, mod=None):
    """the fillet radius of an element: its own FILLET_R, else by class"""
    if mod is not None and getattr(mod, "FILLET_R", None): return float(mod.FILLET_R)
    return RADIUS.get(cls or getattr(mod, "CLASS", ""), 0.5)

def _radii(P, cls):
    """per primitive: the radius of the innermost element that owns it (a contact inside an I/O block keeps a contact's radius)"""
    n = len(P); r = [radius(cls)] * n; span = [math.inf] * n; cache = {}
    for s0, e0, tag, eid in getattr(P, "owners", []):
        if eid not in cache:
            try:
                from . import library
                cache[eid] = radius(mod=library.load(eid))
            except Exception: cache[eid] = radius(cls)
        for i in range(s0, min(e0, n)):
            if e0 - s0 < span[i]: span[i] = e0 - s0; r[i] = cache[eid]
    for i, rr in getattr(P, "radii", {}).items():                      # a primitive's own radius wins (round 30 2.d: cordset-m12's bare
        if 0 <= i < n: r[i] = float(rr)                                # leads are wire ends inside a cable, RADIUS["wire"], not r 0.5)
    return r

def edge_frames(prim):
    """[(pick points [(point, n1, n2)], length, curve)] for the outer edges of a primitive: n1, n2 the outward normals of the two faces
    meeting there (for a circle, n2 is the radial normal at each point). The first point is the default pick."""
    lay, kind, q = prim; out = []
    if kind == "box":
        x, y, z, dx, dy, dz = q; kind, q = "obox", ((x, y, z), (1, 0, 0), (0, 1, 0), (0, 0, 1), dx, dy, dz)
    if kind == "obox":
        o, ex, ey, ez, l, w, h = q; o = np.array(o, float); E = [np.array(e, float) for e in (ex, ey, ez)]; S_ = [float(l), float(w), float(h)]
        for i in range(3):
            if S_[i] < 0: o = o + E[i] * S_[i]; S_[i] = -S_[i]
        for i in range(3):
            o1, o2 = [j for j in range(3) if j != i]
            for a in (0, 1):
                for b in (0, 1):
                    n1, n2 = E[o1] * (1 if a else -1), E[o2] * (1 if b else -1)
                    base = o + E[o1] * S_[o1] * a + E[o2] * S_[o2] * b
                    pts = [tuple(float(v) for v in base + E[i] * S_[i] * f) for f in (0.5, 0.3, 0.7)]
                    out.append(([(p, n1, n2) for p in pts], S_[i], ("line", (base, base + E[i] * S_[i]))))
        return out
    if kind == "cyl":
        p1, p2, r = q; p1, p2 = np.array(p1, float), np.array(p2, float); d = p2 - p1; L = float(np.linalg.norm(d)); d /= L
        a = np.array([1.0, 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1.0, 0]); u = np.cross(d, a); u /= np.linalg.norm(u); w = np.cross(d, u)
        for c, nd in ((p1, -d), (p2, d)):
            diag, mid = [], []
            for k in range(4):                                                  # the four diagonals first: never the axis-aligned points
                t = math.radians(45 + 90 * k); rad = u * math.cos(t) + w * math.sin(t); diag.append((tuple(float(v) for v in (c + rad * r)), nd, rad))
            for k in range(8):                                                  # then the 22.5° points between them
                t = math.radians(22.5 + 45 * k); rad = u * math.cos(t) + w * math.sin(t); mid.append((tuple(float(v) for v in (c + rad * r)), nd, rad))
            up = np.array([1.0, -1.0, 1.0]) / math.sqrt(3)                       # prefer the point the gate's default view sees best
            for pts in (diag, mid): pts.sort(key=lambda e: -float((np.asarray(e[1]) + np.asarray(e[2])) @ up))
            out.append((diag + mid, 2 * math.pi * r, ("circle", (c, d, r))))
    return out

def shared(S, i, p, n1, n2, eps=EPS):
    """the index of another solid that shares the edge: flush on one of its faces (just across face 1, inside face 2's plane, or the
    other way round) or overlapping it right at the edge, while the space outside the edge is free (else it is buried). AutoCAD sees
    two solids there and cannot fillet one: 'Cannot fillet multiple bodies', or the pick lands on the neighbour."""
    p = np.asarray(p, float); n1 = np.asarray(n1, float); n2 = np.asarray(n2, float)
    probes = np.array([p + n1 * eps - n2 * eps, p + n2 * eps - n1 * eps, p - (n1 + n2) * eps])
    for j in S.idx:
        if j == i: continue
        lo, hi = S.bounds(j)
        if np.any(np.all(probes < lo - eps, axis=0)) or np.any(np.all(probes > hi + eps, axis=0)): continue        # no overlap on some axis
        k, q, H = S.geom(j); m = inside(k, q, probes)
        for hk, hq in H: m &= ~inside(hk, hq, probes)
        if m.any(): return j
    return None

def blocked(S, i, p, v, span):
    """the index of a solid (this one included) that stands in the view from p along v within `span`, else None: each solid's box is
    crossed by the ray (slab test), and the stretch inside it is sampled finely"""
    o = np.asarray(p, float); v = np.asarray(v, float); lo, hi = S.lo - 1e-6, S.hi + 1e-6
    with np.errstate(divide="ignore", invalid="ignore"):
        inv = np.where(np.abs(v) > 1e-12, 1.0 / v, np.inf)
        t1 = (lo - o) * inv; t2 = (hi - o) * inv
    t1 = np.where(np.abs(v) > 1e-12, t1, np.where((o >= lo) & (o <= hi), -np.inf, np.inf))
    t2 = np.where(np.abs(v) > 1e-12, t2, np.where((o >= lo) & (o <= hi), np.inf, -np.inf))
    tn = np.max(np.minimum(t1, t2), axis=1); tf = np.min(np.maximum(t1, t2), axis=1)
    tn = np.maximum(tn, 0.3); ok = (tf >= tn) & (tn <= span)
    for jj in np.argsort(tn):
        if not ok[jj]: continue
        a_, b_ = tn[jj], min(tf[jj], span); n = int(min(400, max(8, (b_ - a_) / 0.25)))
        X = o[None, :] + np.outer(np.linspace(a_, b_, n), v)
        j = S.idx[jj]
        if S.P[j][1] == "mesh": continue                                          # a swept mesh: not in the drawing (AutoCAD builds no meshes)
        k, q, H = S.geom(j); m = inside(k, q, X)
        for hk, hq in H: m &= ~inside(hk, hq, X)
        if m.any(): return j
    return None

def _line_pts(a, b, step=STEP):
    a, b = np.asarray(a, float), np.asarray(b, float); n = max(2, int(np.linalg.norm(b - a) / step) + 1)
    return a[None, :] + np.outer(np.linspace(0.0, 1.0, n), b - a)

def _ring(c, d, r):
    d = np.asarray(d, float); d = d / np.linalg.norm(d); a = np.array([1.0, 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(d, a); u /= np.linalg.norm(u); return d, u, np.cross(d, u)

def _circle_pts(c, d, r, step=STEP):
    c = np.asarray(c, float); d, u, w = _ring(c, d, r); n = max(24, int(2 * math.pi * r / step))
    t = np.linspace(0.0, 2 * math.pi, n, endpoint=False)
    return c[None, :] + (np.outer(np.cos(t), u) + np.outer(np.sin(t), w)) * r

def _curves(k, q):
    """a primitive's edges as curves: ('line', (a, b)) or ('circle', (centre, axis, r))"""
    out = []
    if k == "box": x, y, z, dx, dy, dz = q; k, q = "obox", ((x, y, z), (1, 0, 0), (0, 1, 0), (0, 0, 1), dx, dy, dz)
    if k == "obox":
        o, ex, ey, ez, l, w, h = q; o = np.array(o, float); E = [np.array(e, float) for e in (ex, ey, ez)]; S_ = [float(l), float(w), float(h)]
        for i in range(3):
            o1, o2 = [j for j in range(3) if j != i]
            for a in (0, 1):
                for b in (0, 1):
                    base = o + E[o1] * S_[o1] * a + E[o2] * S_[o2] * b; out.append(("line", (base, base + E[i] * S_[i])))
    elif k == "cyl":
        p1, p2, r = q; p1, p2 = np.array(p1, float), np.array(p2, float); out += [("circle", (p1, p2 - p1, r)), ("circle", (p2, p2 - p1, r))]
    return out

def _curve_dist(X, curve):
    """distance of points X from a curve"""
    kind, g = curve
    if kind == "line":
        a, b = (np.asarray(v, float) for v in g); ab = b - a; t = np.clip(((X - a) @ ab) / max(ab @ ab, 1e-12), 0.0, 1.0)
        return np.linalg.norm(X - (a[None, :] + np.outer(t, ab)), axis=1)
    c, d, r = g; c = np.asarray(c, float); d = np.asarray(d, float); d = d / np.linalg.norm(d); v = X - c; ax = v @ d
    rad = np.linalg.norm(v - np.outer(ax, d), axis=1); return np.hypot(rad - r, ax)

def _material(S, j, X, skip=None):
    """X inside solid j (its openings removed; `skip` an opening to leave out)"""
    k, q, H = S.geom(j); m = inside(k, q, X)
    for n_, (hk, hq) in enumerate(H):
        if n_ != skip: m &= ~inside(hk, hq, X)
    return m

def edge_points(S, j):
    """points every STEP along every edge solid j has: its primitive's edges where no opening removed them, the rims where its holes
    and cuts leave its faces, and a cut's corners inside the material. Sampled, not exact: what `crowded` compares a pick against"""
    cache = S.__dict__.setdefault("_edge_pts", {})
    if j in cache: return cache[j]
    k, q, H = S.geom(j); pts = []
    for kind, g in _curves(k, q):
        X = _line_pts(*g) if kind == "line" else _circle_pts(*g)
        keep = np.ones(len(X), bool)
        for hk, hq in H: keep &= ~inside(hk, hq, X)
        pts.append(X[keep])
    for n_, (hk, hq) in enumerate(H):
        if hk == "hole":
            p1, p2, r = np.asarray(hq[0], float), np.asarray(hq[1], float), float(hq[2]); L = float(np.linalg.norm(p2 - p1))
            if L < 1e-9: continue
            d, u, w = _ring(p1, p2 - p1, r); na = max(16, int(2 * math.pi * r / STEP)); nt = max(2, int(L / STEP) + 1)
            th = np.linspace(0.0, 2 * math.pi, na, endpoint=False); t = np.linspace(0.0, L, nt)
            R = np.outer(np.cos(th), u) + np.outer(np.sin(th), w)                                   # na x 3
            X = p1[None, None, :] + t[None, :, None] * d[None, None, :] + R[:, None, :] * (r + 0.03)
            m = _material(S, j, X.reshape(-1, 3), skip=n_).reshape(na, nt)                          # material just outside the bore
            ia, it = np.nonzero(m[:, 1:] != m[:, :-1])                                              # where the bore leaves a face
            if len(ia): pts.append(p1[None, :] + np.outer((t[it] + t[it + 1]) / 2, d) + R[ia] * r)
            for e, sgn in ((p1, -1.0), (p2, 1.0)):                                                  # a blind end: its circle is an edge
                Xe = e[None, :] + R * (r - 0.03) + d[None, :] * 0.03 * sgn
                me = _material(S, j, Xe, skip=n_)
                if me.any(): pts.append(e[None, :] + R[me] * r)
        elif hk == "cut":
            o, ex, ey, ez, l, w, h = hq[:7]; o = np.array(o, float); E = [np.array(v, float) for v in (ex, ey, ez)]; S_ = [float(l), float(w), float(h)]
            for i in range(3):
                if S_[i] < 0: o = o + E[i] * S_[i]; S_[i] = -S_[i]
            for i in range(3):                                                                      # its corners inside the material
                o1, o2 = [jj for jj in range(3) if jj != i]
                for a in (0, 1):
                    for b in (0, 1):
                        base = o + E[o1] * S_[o1] * a + E[o2] * S_[o2] * b; X = _line_pts(base, base + E[i] * S_[i])
                        off = (E[o1] * (1 if a else -1) + E[o2] * (1 if b else -1)) * 0.03
                        m = _material(S, j, X + off, skip=n_)
                        if m.any(): pts.append(X[m])
            for i in range(3):                                                                      # where its faces leave the solid's faces
                o1, o2 = [jj for jj in range(3) if jj != i]
                for side in (0, 1):
                    f0 = o + E[i] * S_[i] * side; nrm = E[i] * (1 if side else -1) * 0.03
                    for a_, b_ in ((o1, o2), (o2, o1)):                                             # lines along a_, spaced along b_
                        sp = max(0.25, S_[b_] / 300.0); nb = max(2, int(S_[b_] / sp) + 1); na_ = max(2, int(S_[a_] / STEP) + 1)
                        sa = np.linspace(0.0, S_[a_], na_); sb = np.linspace(0.0, S_[b_], nb)
                        X = f0[None, None, :] + sb[:, None, None] * E[b_][None, None, :] + sa[None, :, None] * E[a_][None, None, :]
                        m = _material(S, j, (X + nrm).reshape(-1, 3), skip=n_).reshape(nb, na_)
                        ib, ia = np.nonzero(m[:, 1:] != m[:, :-1])
                        if len(ib): pts.append(f0[None, :] + np.outer(sb[ib], E[b_]) + np.outer((sa[ia] + sa[ia + 1]) / 2, E[a_]))
    cache[j] = np.vstack(pts) if pts else np.zeros((0, 3))
    return cache[j]

def clearance(S, i, p, v, curve, rho=CLEAR):
    """(how close the nearest other edge passes to p in the view along v, at any depth, capped at rho; the solid it belongs to, or
    None): in 2D wireframe the gate's pick takes the nearest edge drawn. The edge being picked (curve) does not count."""
    o = np.asarray(p, float); v = np.asarray(v, float); v = v / np.linalg.norm(v); lo, hi = S.lo - rho, S.hi + rho
    with np.errstate(divide="ignore", invalid="ignore"):
        inv = np.where(np.abs(v) > 1e-12, 1.0 / v, np.inf); t1 = (lo - o) * inv; t2 = (hi - o) * inv
    inside_ax = (o >= lo) & (o <= hi)
    t1 = np.where(np.abs(v) > 1e-12, t1, np.where(inside_ax, -np.inf, np.inf)); t2 = np.where(np.abs(v) > 1e-12, t2, np.where(inside_ax, np.inf, -np.inf))
    tn = np.max(np.minimum(t1, t2), axis=1); tf = np.min(np.maximum(t1, t2), axis=1)
    best, who = rho, None
    for jj in np.nonzero(tf >= tn)[0]:
        j = S.idx[jj]
        if S.P[j][1] == "mesh": continue
        X = edge_points(S, j)
        if not len(X): continue
        c = np.cross(X - o, v); d2 = (c * c).sum(axis=1); m = d2 < best * best
        if j == i and m.any(): m[m] = _curve_dist(X[m], curve) > 0.06
        if m.any():
            d = float(np.sqrt(d2[m].min()))
            if d < best: best, who = d, j
    return best, who

def wall(S, i, p, n1, n2, reach):
    """True when the material behind the edge is thinner than `reach` along either face normal (a wall left by a hole or a cut)"""
    k, q, H = S.geom(i); p = np.asarray(p, float); q0 = p - (n1 + n2) * 0.01
    t = np.linspace(0.03, reach, 12)
    for n in (n1, n2):
        X = q0[None, :] - np.outer(t, n); m = inside(k, q, X)
        for hk, hq in H: m &= ~inside(hk, hq, X)
        if not m.all(): return True
    return False

def edges_of(prim):
    """(pick point, edge length) for the outer edges of a primitive, and its thinnest size (the gate's own rule)"""
    lay, kind, q = prim; out = []
    if kind == "box":
        x, y, z, dx, dy, dz = q; c = [(x, x + dx), (y, y + dy), (z, z + dz)]
        for ax in range(3):
            o = [a for a in range(3) if a != ax]
            for u in c[o[0]]:
                for v in c[o[1]]:
                    p = [0.0, 0.0, 0.0]; p[ax] = (c[ax][0] + c[ax][1]) / 2; p[o[0]] = u; p[o[1]] = v; out.append((tuple(p), abs(c[ax][1] - c[ax][0])))
        return out, min(abs(dx), abs(dy), abs(dz))
    if kind == "cyl":
        p1, p2, r = q; p1, p2 = np.array(p1, float), np.array(p2, float); d = p2 - p1; L = float(np.linalg.norm(d)); d /= L
        a = np.array([1.0, 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1.0, 0]); u = np.cross(d, a); u /= np.linalg.norm(u)
        for c in (p1, p2): out.append((tuple(float(v) for v in (c + u * r)), 2 * math.pi * r))
        return out, min(L, 2 * r)
    if kind == "obox":
        o, ex, ey, ez, l, w, h = q; o, ex, ey, ez = (np.array(v, float) for v in (o, ex, ey, ez)); ax = [(ex, l), (ey, w), (ez, h)]
        for i in range(3):
            o1, o2 = [j for j in range(3) if j != i]
            for a in (0, 1):
                for b in (0, 1):
                    p = o + ax[i][0] * ax[i][1] / 2 + ax[o1][0] * ax[o1][1] * a + ax[o2][0] * ax[o2][1] * b; out.append((tuple(float(v) for v in p), abs(ax[i][1])))
        return out, min(abs(l), abs(w), abs(h))
    return out, 0.0

def buried(S, i, p, eps=EPS):
    """the index of another solid the point p lies in or within eps of, else None"""
    p = np.asarray(p, float)
    d = np.array([[a, b, c] for a in (-eps, 0, eps) for b in (-eps, 0, eps) for c in (-eps, 0, eps)]) + p
    for j in S.idx:
        if j == i: continue
        lo, hi = S.bounds(j)
        if np.any(p < lo - eps) or np.any(p > hi + eps): continue
        k, q, H = S.geom(j)
        m = inside(k, q, d)
        for hk, hq in H: m &= ~inside(hk, hq, d)
        if m.any(): return j
    return None

def _runs(S, i, curve, pts, L):
    """the stretches of an edge that a hole or cut leaves, each [(candidate points [(point, n1, n2)], length)]: a circle the L
    recess interrupts is one arc of 283°; a knob top the pointer slot crosses, two arcs (round 6). Candidates are the edge's own
    picks that fall inside the stretch (clear of its ends), then the stretch's middle and quarter points. [] when nothing is left."""
    kind, g = curve
    if kind == "circle":
        c, d, r = g; c = np.asarray(c, float); _, u, w = _ring(c, d, r); nd = np.asarray(pts[0][1], float)
        n = max(360, int(2 * math.pi * r / 0.05)); t = np.arange(n) * 2 * math.pi / n
        Rr = np.outer(np.cos(t), u) + np.outer(np.sin(t), w); X = c + Rr * r; wrap = True
        m = _material(S, i, X - (nd[None, :] + Rr) * 0.02)
        def at(f): th = 2 * math.pi * f; rad = u * math.cos(th) + w * math.sin(th); return (tuple(float(v) for v in c + rad * r), tuple(nd), rad)
        def param(q): v = np.asarray(q, float) - c; return (math.atan2(v @ w, v @ u) / (2 * math.pi)) % 1.0
        total = 2 * math.pi * r; margin = max(2.0 / 360.0, 0.3 / total)
    else:
        a_, b_ = (np.asarray(v, float) for v in g); n1, n2 = (np.asarray(v, float) for v in pts[0][1:])
        n = max(60, int(L / 0.05)); t = np.linspace(0.0, 1.0, n); X = a_ + np.outer(t, b_ - a_); wrap = False
        m = _material(S, i, X - (n1 + n2)[None, :] * 0.02)
        def at(f): return (tuple(float(v) for v in a_ + (b_ - a_) * f), tuple(n1), tuple(n2))
        def param(q): ab = b_ - a_; return float((np.asarray(q, float) - a_) @ ab / (ab @ ab))
        total = L; margin = max(0.02, 0.3 / max(L, 1e-9))
    if m.all(): return [(pts, L)]
    if not m.any(): return []
    lab = -np.ones(n, int); run = -1
    order = np.roll(np.arange(n), -int(np.argmin(m))) if wrap else np.arange(n)                # start on a gap: no run wraps
    prev = False
    for k in order:
        if m[k] and not prev: run += 1
        if m[k]: lab[k] = run
        prev = bool(m[k])
    out = []; step = 1.0 / n if wrap else 1.0 / (n - 1)
    for rid in range(run + 1):
        ks = [k for k in order if lab[k] == rid]; f0 = ks[0] * step; span = len(ks) * step
        def inside(f):
            if wrap: g_ = (f - f0) % 1.0
            else: g_ = f - f0
            return margin <= g_ <= span - margin
        cand = [e for e in pts if inside(param(e[0]))] + [at((f0 + span * q) % 1.0 if wrap else f0 + span * q) for q in (0.5, 0.25, 0.75)]
        out.append((cand, span * total))
    return out

def _views(n1, n2):
    """the views an edge is tried from: its faces' bisector, then leaning 2:1 toward each face"""
    out = []
    for a, b in ((1.0, 1.0), (2.0, 1.0), (1.0, 2.0)):
        v = a * np.asarray(n1, float) + b * np.asarray(n2, float); out.append(v / np.linalg.norm(v))
    return out

def outer_edges(P, R=None, min_edge=MIN_EDGE, cls=None):
    """for every geometric primitive (box / cyl / obox, colliders excluded), in Prims order: dict(index, layer, r, thin,
    edges=[dict(point, length, status in pick / short / thin / buried / shared / crowded / hidden / cut / child, by, view, clearance,
    batch_ok, alts)]). child (round 9): the primitive belongs to an element placed inside this one (a port, an insert, a contact);
    that element is gated as itself, so the host's gate leaves its edges alone. An edge a hole or cut interrupts is split into the stretches left, each with its own length and picks (round 6); `cut`:
    nothing of it is left. r: the radius for that primitive (R if given, else its own element's, see radius()); thin: the part is thinner than 2.5 r,
    or the wall a hole or cut leaves behind the edge is; view: the direction to look from (the faces' bisector, or a 2:1 lean); clearance:
    mm to the nearest other edge in that view (capped at CLEAR); batch_ok: as clear from the batch view 1,-1,1; alts: further
    [(point, view, clearance)] on the same edge for the gate to try in turn when a pick selects nothing. crowded: some view of the edge is
    unblocked, but another edge sits on every one of them (under MIN_CLEAR)."""
    S = Scene(P); out = []; RR = [R] * len(P) if R is not None else _radii(P, cls)
    child = set()
    for s0, e0, *_ in getattr(P, "owners", []): child.update(range(s0, min(e0, len(P))))
    span = float(np.linalg.norm(S.hi.max(axis=0) - S.lo.min(axis=0))) if len(S.idx) else 10.0
    for i, prim in enumerate(P):
        if prim[1] not in ("box", "cyl", "obox") or prim[0].startswith("collider:"): continue
        r = float(RR[i]); _, thin = edges_of(prim); rec = dict(index=i, layer=prim[0], r=r, thin=thin, edges=[])
        if i in child:
            rec["edges"] = [dict(point=tuple(pts[0][0]), length=L, status="child", by=None, view=None, clearance=0.0, batch_ok=False, alts=[],
                                 src=k, stretch=False) for k, (pts, L, curve) in enumerate(edge_frames(prim))]
            out.append(rec); continue
        holed = bool(S.holes.get(i))
        frames = []
        for k, (pts, L, curve) in enumerate(edge_frames(prim)):
            runs = _runs(S, i, curve, pts, L) if holed and thin >= 2.5 * r else [(pts, L)]
            if not runs: rec["edges"].append(dict(point=tuple(pts[0][0]), length=L, status="cut", by=None, view=None, clearance=0.0, batch_ok=False, alts=[], src=k, stretch=False))
            split = len(runs) > 1 or bool(runs) and runs[0][1] < L - STRETCH        # interrupted: more than its ends' sampling lost
            frames += [(p_, L_, curve, k, split) for p_, L_ in runs]
        for pts, L, curve, src, split in frames:
            p, n1, n2 = pts[0]; n1, n2 = np.asarray(n1, float), np.asarray(n2, float)
            v = n1 + n2; v = v / np.linalg.norm(v); by = None; alts = []; batch_ok = False; cl = 0.0
            if thin < 2.5 * r: st = "thin"
            elif L <= min_edge: st = "short"
            elif holed and wall(S, i, p, n1, n2, 2.5 * r): st = "thin"
            else:
                j = buried(S, i, p); st, by = ("buried", j) if j is not None else ("pick", None)
                if st == "pick":
                    j = shared(S, i, p, n1, n2)
                    if j is not None: st, by = "shared", j
                if st == "pick":
                    clear, tried = [], []; seen = None; ok_pt = {}
                    for k_ in range(3):                                                  # bisector at every point, then the two leans
                        for q_, a_, b_ in pts:
                            if len(clear) >= 6: break
                            if q_ not in ok_pt:
                                qa = np.asarray(q_, float); inner = qa - (np.asarray(a_, float) + np.asarray(b_, float)) * 0.02
                                ok_pt[q_] = buried(S, i, q_) is None and bool(_material(S, i, inner[None, :])[0])
                            if not ok_pt[q_]: continue
                            vv = _views(a_, b_)[k_]
                            if blocked(S, i, q_, vv, span) is not None: continue
                            d, j = clearance(S, i, q_, vv, curve)
                            rec_ = (q_, tuple(float(c) for c in vv), round(d, 3))
                            if d >= CLEAR: clear.append(rec_)
                            elif d >= MIN_CLEAR: tried.append(rec_)
                            else: seen = j if seen is None else seen
                    good = clear + sorted(tried, key=lambda e: -e[2])[:max(0, 6 - len(clear))]
                    if good:
                        (p, v, cl), alts = good[0], good[1:]; batch_ok = clearance(S, i, p, BATCH_VIEW, curve)[0] >= CLEAR
                    elif seen is not None: st, by = "crowded", seen
                    else: st, by = "hidden", blocked(S, i, p, v, span)
            rec["edges"].append(dict(point=tuple(p), length=L, status=st, by=by, view=tuple(float(c) for c in v), clearance=cl, batch_ok=batch_ok,
                                     alts=[dict(point=q_, view=vv, clearance=d_) for q_, vv, d_ in alts], src=src, stretch=split))
        out.append(rec)
    return out

def batches(rec):
    """the FILLETEDGE batches for one solid (round 10 c, from round 9's trials on io-block-m12-8di8do's housing): [[edge index into rec["edges"]]],
    picks only, in the order the gate sends them. Batch 1 holds the solid's whole edges, longest first (trial E: the long edges take
    their full fillet when they go before the corner edges). The stretches a hole or cut leaves of one edge go in a batch of their own,
    one batch per interrupted edge, after it (trials A, B and C batched; only the whole edges with the stretches of more than one edge
    together, trial D and every gate of rounds 8 and 9, hung). A solid with no interrupted edge keeps its one batch."""
    pick = [(j, e) for j, e in enumerate(rec["edges"]) if e["status"] == "pick"]
    whole = [j for j, e in sorted(pick, key=lambda x: -x[1]["length"]) if not e.get("stretch")]
    out = [whole] if whole else []
    for s in sorted({e.get("src") for _, e in pick if e.get("stretch")}, key=lambda s: -max(e["length"] for _, e in pick if e.get("stretch") and e.get("src") == s)):
        out.append([j for j, e in sorted(pick, key=lambda x: -x[1]["length"]) if e.get("stretch") and e.get("src") == s])
    return out

def summary(P, R=None, cls=None):
    """counts per status: what the gate will try to fillet"""
    c = {"batches": 0}
    for rec in outer_edges(P, R, cls=cls):
        for e in rec["edges"]: c[e["status"]] = c.get(e["status"], 0) + 1
        c["batches"] += len(batches(rec))
    return c
