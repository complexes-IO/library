"""Solid geometry kernel for the validation suite (numpy only; no CAD kernel needed). It reads a Prims list exactly as AutoCAD will
build it: every box / obox / cyl is a solid, every hole and cut is subtracted from its target, every mesh is a closed triangle shell.
  Scene(P)                  solids with their owner instance, node, axis-aligned bounds and holes
  scene.overlap(i, j)       sampled overlap of two solids: volume (mm3), thickness (mm), where (bounds) or None when they only touch
  scene.moved(idx, R, t)    a rigid copy of some solids (rotation R about the origin, then translation t) for the motion sweep
Inside tests are exact for the analytic kinds; meshes use the generalised winding number. Overlap is sampled on a cell-centred grid,
so an overlap thinner than the grid step can be missed: the step is reported with every finding."""
import math
import numpy as np

EPS = 0.05            # bounds closer than this only touch
CELLS = 60000         # sample budget per pair
CELLS_MESH = 12000    # sample budget when a mesh (winding number) is involved
H_MIN = 0.2           # finest grid step (mm)

def node_of(L):
    return L[5:].split("|", 1)[0] if L.startswith("node:") else None

def aabb(k, q):
    if k == "box":
        x, y, z, dx, dy, dz = q; a = np.array([x, y, z], float); b = a + np.array([dx, dy, dz], float)
        return np.minimum(a, b), np.maximum(a, b)
    if k in ("cyl", "hole"):
        p1, p2, r = np.array(q[0], float), np.array(q[1], float), float(q[2]); d = p2 - p1; n = np.linalg.norm(d)
        e = r * np.sqrt(np.clip(1 - (d / n) ** 2, 0, 1)) if n > 0 else np.full(3, r)
        return np.minimum(p1, p2) - e, np.maximum(p1, p2) + e
    if k == "obox":
        o, ex, ey, ez, l, w, h = q; o, ex, ey, ez = (np.array(v, float) for v in (o, ex, ey, ez))
        C = np.array([o + ex * l * a + ey * w * b + ez * h * c for a in (0, 1) for b in (0, 1) for c in (0, 1)])
        return C.min(axis=0), C.max(axis=0)
    if k == "mesh":
        V = np.array([v for t in q[0] for v in t], float); return V.min(axis=0), V.max(axis=0)
    if k == "cut": return aabb("obox", q[:7])
    raise ValueError(k)

SKIN = 1e-3          # a point closer than this to a surface is not inside: faces that only touch never count as overlap

def inside(k, q, X):
    """bool mask of the points X (n, 3) strictly inside one primitive (SKIN from its surface)"""
    e = SKIN
    if k == "box":
        lo, hi = aabb(k, q); return np.all((X > lo + e) & (X < hi - e), axis=1)
    if k in ("cyl", "hole"):
        p1, p2, r = np.array(q[0], float), np.array(q[1], float), float(q[2]); d = p2 - p1; n2 = d @ d
        if n2 == 0: return np.zeros(len(X), bool)
        t = (X - p1) @ d / n2; rad = np.linalg.norm((X - p1) - np.outer(t, d), axis=1); et = e / math.sqrt(n2)
        return (t > et) & (t < 1 - et) & (rad < r - e)
    if k == "obox":
        o, ex, ey, ez, l, w, h = q; D = X - np.array(o, float); m = np.ones(len(X), bool)
        for e_, s in ((ex, l), (ey, w), (ez, h)):
            a = D @ np.array(e_, float); m &= (a > min(0, s) + e) & (a < max(0, s) - e)
        return m
    if k == "cut": return inside("obox", q[:7], X)
    if k == "mesh":
        T = _mesh_array(q)
        lo, hi = T.reshape(-1, 3).min(axis=0), T.reshape(-1, 3).max(axis=0)
        m = np.all((X >= lo) & (X <= hi), axis=1); out = np.zeros(len(X), bool)
        if m.any(): out[m] = parity(q, X[m])
        return out
    raise ValueError(k)

_GRID = {}
def parity(q, X):
    """inside a closed shell by ray parity along +x; triangles binned on a y-z grid so each point meets only its column's triangles"""
    T = _mesh_array(q); key = id(q[0])
    if key not in _GRID or _GRID[key][0] is not q[0]:
        lo = T[:, :, 1:].reshape(-1, 2).min(axis=0); hi = T[:, :, 1:].reshape(-1, 2).max(axis=0)
        n = int(min(96, max(4, np.sqrt(len(T)) * 1.5))); cs = np.maximum((hi - lo) / n, 1e-6)
        tl = np.floor((T[:, :, 1:].min(axis=1) - lo) / cs).astype(int).clip(0, n - 1); th = np.floor((T[:, :, 1:].max(axis=1) - lo) / cs).astype(int).clip(0, n - 1)
        bins = {}
        for t in range(len(T)):
            for a in range(tl[t, 0], th[t, 0] + 1):
                for b in range(tl[t, 1], th[t, 1] + 1): bins.setdefault((a, b), []).append(t)
        _GRID[key] = (q[0], lo, cs, n, {k: np.array(v) for k, v in bins.items()})
    _, lo, cs, n, bins = _GRID[key]
    Y = X[:, 1:] + np.array([1.13e-7, 2.71e-7]); c = np.floor((Y - lo) / cs).astype(int)
    out = np.zeros(len(X), bool); ok = np.all((c >= 0) & (c < n), axis=1)
    keys = c[:, 0] * n + c[:, 1]
    for kk in np.unique(keys[ok]):
        sel = np.nonzero(ok & (keys == kk))[0]; tri = bins.get((int(kk // n), int(kk % n)))
        if tri is None: continue
        A, B, C = T[tri, 0], T[tri, 1], T[tri, 2]                                   # (t, 3)
        p = Y[sel][:, None, :]                                                     # (s, 1, 2)
        v0, v1 = (B - A)[None, :, 1:], (C - A)[None, :, 1:]; v2 = p - A[None, :, 1:]
        d = v0[..., 0] * v1[..., 1] - v0[..., 1] * v1[..., 0]
        with np.errstate(divide="ignore", invalid="ignore"):
            u = (v2[..., 0] * v1[..., 1] - v2[..., 1] * v1[..., 0]) / d; w = (v0[..., 0] * v2[..., 1] - v0[..., 1] * v2[..., 0]) / d
            hitm = (d != 0) & (u >= 0) & (w >= 0) & (u + w <= 1)
            xs = A[None, :, 0] + u * (B - A)[None, :, 0] + w * (C - A)[None, :, 0]
        out[sel] = ((hitm & (xs > X[sel][:, None, 0])).sum(axis=1) % 2) == 1
    return out

_MESH = {}
def _mesh_array(q):
    key = id(q[0])
    if key not in _MESH or _MESH[key][0] is not q[0]: _MESH[key] = (q[0], np.array(q[0], float))
    return _MESH[key][1]

def winding(T, X, chunk=4000):
    """generalised winding number of a closed triangle shell T (m, 3, 3) at points X (n, 3)"""
    out = np.zeros(len(X))
    for s in range(0, len(X), chunk):
        P = X[s:s + chunk, None, :]
        a, b, c = T[None, :, 0] - P, T[None, :, 1] - P, T[None, :, 2] - P
        la, lb, lc = (np.linalg.norm(v, axis=2) for v in (a, b, c))
        det = np.einsum("ijk,ijk->ij", a, np.cross(b, c))
        den = la * lb * lc + np.einsum("ijk,ijk->ij", a, b) * lc + np.einsum("ijk,ijk->ij", b, c) * la + np.einsum("ijk,ijk->ij", c, a) * lb
        out[s:s + chunk] = np.abs(np.arctan2(det, den).sum(axis=1) / (2 * math.pi))
    return out

def rigid(k, q, R, t):
    """a primitive moved by x' = R x + t"""
    R = np.asarray(R, float); t = np.asarray(t, float)
    def p_(p): return tuple(R @ np.array(p, float) + t)
    def v_(v): return tuple(R @ np.array(v, float))
    if k == "box":
        x, y, z, dx, dy, dz = q; return "obox", (p_((x, y, z)), v_((1, 0, 0)), v_((0, 1, 0)), v_((0, 0, 1)), dx, dy, dz)
    if k == "obox": o, ex, ey, ez, l, w, h = q; return "obox", (p_(o), v_(ex), v_(ey), v_(ez), l, w, h)
    if k == "cyl": return "cyl", (p_(q[0]), p_(q[1]), q[2])
    if k == "hole": return "hole", (p_(q[0]), p_(q[1]), q[2], q[3])
    if k == "cut": o, ex, ey, ez, l, w, h, tg = q; return "cut", (p_(o), v_(ex), v_(ey), v_(ez), l, w, h, tg)
    if k == "mesh": return "mesh", ([tuple(p_(v) for v in tri) for tri in q[0]],)
    raise ValueError(k)

def rotation(axis, deg):
    a = np.array(axis, float); a /= np.linalg.norm(a); th = math.radians(deg); c, s = math.cos(th), math.sin(th)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + s * K + (1 - c) * (K @ K)

class Scene:
    """solids of a Prims list: kind, params, layer, node, owner tag, owner path, holes, bounds"""
    def __init__(self, P):
        self.P = P; n = len(P)
        own = [""] * n; span = [math.inf] * n
        for s0, e0, tag, eid in getattr(P, "owners", []):
            for i in range(s0, min(e0, n)):
                if e0 - s0 < span[i]: span[i] = e0 - s0; own[i] = tag
        self.owner_of = own
        holes = {}
        for i, (L, k, q) in enumerate(P):
            if k in ("hole", "cut"): holes.setdefault(q[-1], []).append(i)
        self.idx = [i for i, (L, k, q) in enumerate(P) if k not in ("hole", "cut") and not L.startswith("collider:")]
        self.holes = holes
        B = [aabb(P[i][1], P[i][2]) for i in self.idx]
        self.lo = np.array([b[0] for b in B]) if B else np.zeros((0, 3)); self.hi = np.array([b[1] for b in B]) if B else np.zeros((0, 3))
        self.pos = {i: j for j, i in enumerate(self.idx)}
        self.alt = {}                                   # solid index -> moved (kind, q, holes [(kind, q)]) during a sweep

    def node(self, i): return node_of(self.P[i][0])
    def name(self, i):
        n = self.node(i); o = self.owner_of[i]
        if n: return n
        return f"{o}.body" if o else "body"
    def material(self, i): L = self.P[i][0]; return L.split("|", 1)[1] if "|" in L else L

    def geom(self, i):
        if i in self.alt: return self.alt[i]
        k, q = self.P[i][1], self.P[i][2]
        return k, q, [(self.P[h][1], self.P[h][2]) for h in self.holes.get(i, [])]

    def bounds(self, i):
        if i in self.alt: return aabb(self.alt[i][0], self.alt[i][1])
        j = self.pos[i]; return self.lo[j], self.hi[j]

    def candidates(self, I, J=None):
        """index pairs (i, j) from I x J (or I x I, i < j) whose bounds overlap by more than EPS on every axis"""
        I = list(I); J = list(J) if J is not None else None; out = []
        if not I: return out
        li = np.array([self.bounds(i)[0] for i in I]); hi_ = np.array([self.bounds(i)[1] for i in I])
        Jl = J if J is not None else I
        if not Jl: return out
        lj = np.array([self.bounds(j)[0] for j in Jl]); hj = np.array([self.bounds(j)[1] for j in Jl])
        for a in range(0, len(I), 512):
            ov = np.minimum(hi_[a:a + 512, None, :], hj[None, :, :]) - np.maximum(li[a:a + 512, None, :], lj[None, :, :])
            m = np.all(ov > EPS, axis=2)
            for x, y in zip(*np.nonzero(m)):
                i, j = I[a + x], Jl[y]
                if J is None and not i < j: continue
                if i != j: out.append((i, j))
        return out

    def overlap(self, i, j):
        """None when i and j only touch; else dict(volume, thickness, lo, hi, step)"""
        (ki, qi, hi_), (kj, qj, hj) = self.geom(i), self.geom(j)
        la, ha = aabb(ki, qi); lb, hb = aabb(kj, qj)
        lo, hi = np.maximum(la, lb), np.minimum(ha, hb); ext = hi - lo
        if np.any(ext <= EPS): return None
        if ki == kj == "box" and not hi_ and not hj:                                  # exact
            return dict(volume=float(np.prod(ext)), thickness=float(ext.min()), lo=lo, hi=hi, step=0.0)
        if ki == "mesh" and kj != "mesh": (ki, qi, hi_), (kj, qj, hj) = (kj, qj, hj), (ki, qi, hi_)    # analytic solid first, mesh last
        budget = CELLS_MESH if "mesh" in (ki, kj) else CELLS
        vol = float(np.prod(ext)); h = max(H_MIN, (vol / budget) ** (1 / 3))
        n = np.maximum(1, np.ceil(ext / h)).astype(int); st = ext / n
        g = [lo[a] + st[a] * (np.arange(n[a]) + 0.5) for a in range(3)]
        X = np.stack(np.meshgrid(*g, indexing="ij"), axis=-1).reshape(-1, 3)
        m = inside(ki, qi, X)
        for k, q in hi_: m &= ~inside(k, q, X)
        if not m.any(): return None
        X = X[m]; m = inside(kj, qj, X)
        for k, q in hj: m &= ~inside(k, q, X)
        if not m.any(): return None
        X = X[m]; cell = float(np.prod(st)); a, b = X.min(axis=0) - st / 2, X.max(axis=0) + st / 2
        return dict(volume=len(X) * cell, thickness=float((b - a).min()), lo=a, hi=b, step=float(st.max()))

    def move(self, idx, R, t):
        """move solids idx (and their holes) rigidly for the next overlap calls; reset() puts them back"""
        for i in idx:
            k, q = self.P[i][1], self.P[i][2]
            self.alt[i] = (*rigid(k, q, R, t), [rigid(self.P[h][1], self.P[h][2], R, t) for h in self.holes.get(i, [])])
    def reset(self): self.alt = {}
