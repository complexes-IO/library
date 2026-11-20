"""The institute's mark on an element (EM 2026-11-20: "I want complexes logo on them 0{1} with a circle"): the ring with 0{1}
inside it, one outline for every element, so the mark is the same wherever it stands.

The outline is lib/standards/cit-mark.json: the site's own mark (the inline svg.site-mark of the site's nav: a circle and the text
0{1}, centred), the characters' contours those of the font that mark names, taken once and not redrawn. It is given for a ring
of BASE_D mm outside diameter; regions(d) scales it.

  regions(d, line)     the mark as flat regions [(points, triangles, loops)], mm about the ring's centre, u to the right and v up
                       as it is read: the ring, then each character island with its holes (the zero's counter; the dot inside
                       the counter is an island of its own). d: the ring's outside diameter (MIN_D or more: under it the
                       characters' strokes go under 0.3 mm). line: the ring's line (default LINE_PER_D x d: the site's ring is
                       thinner than a part can carry).
  inlay(region, to3)   one region as a closed solid mesh: to3(u, v, top) gives the point on the face (top) and at the inlay's
                       floor. For a face that is not flat (a temple that bows): the element gives the mapping.
  flat(P, layer, centre, u, v, d, ...)   the mark on a flat face: centre a point on the face, u the reading direction, v up
                       (unit vectors in the face; the outward normal is u x v). One mesh per region on `layer`, PROUD of the
                       face (GEO-050: never coplanar) and DEPTH into it. The layer is the element's choice: a metal on a dark
                       housing, a dark plastic on a light one.

The mark is a mesh: the glTF, the previews, Blender and Godot carry it; AutoCAD does not build meshes (toolkit/cadout.py), so the
drawing has no mark yet. No other logo, vendor name or product name goes on an element (lib/OPERATING.md 6)."""
import json, math, os
import numpy as np

BASE_D = 6.0                 # the outline file's ring, outside diameter, mm
MIN_D = 6.0                  # EM's brief 2026-11-20 (gl-xr-1): no stroke in the characters thinner than 0.3 mm
LINE_PER_D = 0.4 / 6.0       # the ring's line: 0.4 at 6.0 (the same brief)
PROUD, DEPTH = 0.03, 0.3
FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "standards", "cit-mark.json")
_CACHE = {}


def _orient(tris):
    """a closed shell, outward: flip every triangle when the signed volume is negative"""
    A = np.array(tris, float); vol = np.einsum("ij,ij->i", A[:, 0], np.cross(A[:, 1], A[:, 2])).sum()
    return [(t[0], t[2], t[1]) for t in tris] if vol < 0 else list(tris)


def _area(p): return 0.5 * float(np.sum(p[:, 0] * np.roll(p[:, 1], -1) - np.roll(p[:, 0], -1) * p[:, 1]))


def _inside(q, p):
    """is point q inside the closed outline p (crossing number)"""
    a, b = p, np.roll(p, -1, axis=0); m = (a[:, 1] > q[1]) != (b[:, 1] > q[1])
    return bool(np.sum(q[0] < a[m, 0] + (q[1] - a[m, 1]) * (b[m, 0] - a[m, 0]) / (b[m, 1] - a[m, 1])) % 2)


def _tri_poly(outer, holes):
    """triangles of a flat region with holes: each hole joined to the outline by a bridge, then ears cut, the best-shaped first.
    Returns (points, triangles as index triples, loops as index lists: the outline counter-clockwise, the holes clockwise)."""
    O = outer if _area(outer) > 0 else outer[::-1]; H = [h if _area(h) < 0 else h[::-1] for h in holes]
    P = np.array([tuple(q) for q in O] + [tuple(q) for h in H for q in h]); loops = [list(range(len(O)))]
    for h in H: loops.append(list(range(sum(len(l) for l in loops), sum(len(l) for l in loops) + len(h))))
    def cr(o, a, b): return (P[a][0] - P[o][0]) * (P[b][1] - P[o][1]) - (P[a][1] - P[o][1]) * (P[b][0] - P[o][0])
    E = [(l[i], l[(i + 1) % len(l)]) for l in loops for i in range(len(l))]
    def blocked(a, b): return any(len({a, b, c, d}) == 4 and cr(c, d, a) * cr(c, d, b) < 0 and cr(a, b, c) * cr(a, b, d) < 0 for c, d in E)
    V = list(loops[0])
    for hl in sorted(loops[1:], key=lambda l: -max(P[i][0] for i in l)):
        m = max(hl, key=lambda i: P[i][0]); c = next(k for k in sorted(range(len(V)), key=lambda k: float(np.hypot(*(P[V[k]] - P[m])))) if not blocked(m, V[k]))
        j = hl.index(m); E += [(m, V[c])]; V = V[:c + 1] + hl[j:] + hl[:j + 1] + V[c:]
    tris = []
    while len(V) > 3:
        n = len(V); A = P[[V[i - 1] for i in range(n)]]; B = P[V]; C = P[[V[(i + 1) % n] for i in range(n)]]; W = P[V]; best = None
        ar = (B[:, 0] - A[:, 0]) * (C[:, 1] - A[:, 1]) - (B[:, 1] - A[:, 1]) * (C[:, 0] - A[:, 0])
        for i in np.argsort(-ar / np.maximum.reduce([np.sum((B - A) ** 2, axis=1), np.sum((C - B) ** 2, axis=1), np.sum((A - C) ** 2, axis=1)])):
            if ar[i] <= 1e-5: break
            a, b, c = A[i], B[i], C[i]; ids = (V[i - 1], V[i], V[(i + 1) % n])
            s1 = (b[0] - a[0]) * (W[:, 1] - a[1]) - (b[1] - a[1]) * (W[:, 0] - a[0]); s2 = (c[0] - b[0]) * (W[:, 1] - b[1]) - (c[1] - b[1]) * (W[:, 0] - b[0])
            s3 = (a[0] - c[0]) * (W[:, 1] - c[1]) - (a[1] - c[1]) * (W[:, 0] - c[0]); own = np.isin(V, ids)
            if not np.any((s1 > -1e-9) & (s2 > -1e-9) & (s3 > -1e-9) & ~own): best = int(i); break
        if best is None: raise ValueError("mark outline: no ear left to cut")
        tris.append((V[best - 1], V[best], V[(best + 1) % n])); V.pop(best)
    tris.append(tuple(V))
    got = sum(0.5 * cr(a, b, c) for a, b, c in tris); want = _area(O) + sum(_area(h) for h in H)
    if abs(got - want) > 1e-6 or min(cr(a, b, c) for a, b, c in tris) <= 0: raise ValueError(f"mark outline: triangles cover {got:.6f}, the region is {want:.6f}")
    return P, tris, loops


def regions(d=BASE_D, line=None):
    if d < MIN_D - 1e-9: raise ValueError(f"the mark's ring is {d} mm: under {MIN_D} the characters' strokes go under 0.3 mm")
    line = LINE_PER_D * d if line is None else line; key = (round(d, 6), round(line, 6))
    if key in _CACHE: return _CACHE[key]
    data = json.load(open(FILE, encoding="utf-8")); k = d / BASE_D
    C = [np.array(c["points"], float) * k for c in data["contours"]]; depth = [sum(_inside(c[0], o) for o in C if o is not c) for c in C]
    circle = lambda r: np.array([(r * math.cos(2 * math.pi * i / 72), r * math.sin(2 * math.pi * i / 72)) for i in range(72)])
    out = [_tri_poly(circle(d / 2), [circle(d / 2 - line)])]
    for c, n in zip(C, depth):
        if n % 2 == 0: out.append(_tri_poly(c, [h for h, nh in zip(C, depth) if nh == n + 1 and _inside(h[0], c)]))
    _CACHE[key] = out; return out


def inlay(region, to3):
    P, tris, loops = region; top = [to3(u, v, True) for u, v in P]; bot = [to3(u, v, False) for u, v in P]
    T = [(top[a], top[b], top[c]) for a, b, c in tris] + [(bot[a], bot[c], bot[b]) for a, b, c in tris]
    for l in loops:
        for a, b in zip(l, l[1:] + l[:1]): T += [(bot[a], bot[b], top[b]), (bot[a], top[b], top[a])]
    return _orient(T)


def flat(P, layer, centre, u, v, d=BASE_D, line=None, proud=PROUD, depth=DEPTH, part=None):
    c, u, v = np.array(centre, float), np.array(u, float), np.array(v, float); n = np.cross(u, v)
    if abs(np.linalg.norm(u) - 1) > 1e-6 or abs(np.linalg.norm(v) - 1) > 1e-6 or abs(u @ v) > 1e-6: raise ValueError("the mark's u and v are unit vectors at right angles")
    for r in regions(d, line): P.mesh(layer, inlay(r, lambda a, b, top: tuple(c + u * a + v * b + n * (proud if top else -depth))), part=part)
