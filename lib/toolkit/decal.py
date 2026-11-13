"""The decal projection of the Blender gate (toolkit/blender/gate.py), in plain Python so the selftest can plant it (EM 2026-11-05;
reviewer plc0-1.1 finding 1). The printed faces of an element are projected along the outward normal of the face cluster that
carries the print, never along the sum of all their normals: for a closed printed box that sum is zero, and the old fallback,
straight down, squashed plc0's 70 x 30 label to a 70 x 0.2 strip and passed.

  axis(faces)          faces: [(normal (x, y, z), area)]. Clusters the faces by axis (|n·m| > 0.95, opposite faces together, as a
                       label's front and back), takes the cluster of largest area, and returns its outward normal: the side with the
                       larger area, on a tie the element's front (-y), then the top (+z). A tie is within TIE_REL of the larger
                       side: Blender's mesh data is float32 and a disc's two caps, wound opposite ways, sum to areas a few 1e-7 apart,
                       so a 1e-9 tie let noise pick the hidden back (request elec-3, thermostat-enc's dial island facing +y).
                       An x axis has neither (a tie there went to whichever face came first, so a print on +x or -x
                       could face inwards: ESCAPE valve-gauge-double-1.0 2, port-4's field on +x recorded -x): with away, the
                       vector from the mesh's centre to the island's, the tie goes to the side away from the centre; y and z ties
                       keep -y / +z, so no result on file for them changes.
  island(verts, n)     the island's two sides (in the faces' units) when verts are projected along n
  check(size_mm)       FAIL when either side is under DECAL_MIN_MM (a decal drawn there is squashed to nothing)
DECAL_MIN_MM is the library's design choice: 3 mm, 6 px at the gate's 2 px per mm."""
import math

DECAL_MIN_MM = 3.0
AWAY_MIN = 0.05                                     # the island's centre lies along the axis by at least 5 % of its offset from the mesh's centre
TIE_REL = 1e-4                                      # 0.01 %: float32 noise is ~1e-7; a real front/back difference is far larger

def _dot(a, b): return sum(x * y for x, y in zip(a, b))
def _unit(a):
    l = math.sqrt(_dot(a, a)); return tuple(x / l for x in a) if l > 0 else None

def axis(faces, away=None):
    clusters = []                                   # [axis, {+1: area, -1: area}]
    for n, area in faces:
        n = _unit(n)
        if n is None or area <= 0: continue
        for c in clusters:
            d = _dot(n, c[0])
            if abs(d) > 0.95: c[1][1 if d > 0 else -1] += area; break
        else: clusters.append([n, {1: area, -1: 0.0}])
    if not clusters: return (0.0, -1.0, 0.0)
    c = max(clusters, key=lambda c: c[1][1] + c[1][-1])
    a, (p, m) = c[0], (c[1][1], c[1][-1])
    if abs(p - m) > TIE_REL * max(p, m): return a if p > m else tuple(-x for x in a)
    front = (0.0, -1.0, 0.0) if abs(a[1]) > 0.5 else (0.0, 0.0, 1.0)
    if abs(_dot(a, front)) < 0.5 and away is not None:                     # an x axis: front and top are both across it (ESCAPE
        w = _unit(away); d = _dot(a, w) if w else 0.0                       # valve-gauge-double-1.0 2): the side away from the centre
        if abs(d) > AWAY_MIN: return a if d > 0 else tuple(-x for x in a)
    return a if _dot(a, front) >= 0 else tuple(-x for x in a)

def basis(n):
    """two unit vectors u, v across the projection normal n"""
    a = (1.0, 0.0, 0.0) if abs(n[0]) < 0.9 else (0.0, 1.0, 0.0)
    cr = lambda p, q: (p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2], p[0] * q[1] - p[1] * q[0])
    u = _unit(cr(n, a)); v = _unit(cr(n, u)); return u, v

def island(verts, n):
    u, v = basis(n); us = [_dot(p, u) for p in verts]; vs = [_dot(p, v) for p in verts]
    return max(us) - min(us), max(vs) - min(vs)

def check(size_mm):
    small = min(size_mm)
    if small < DECAL_MIN_MM: return "FAIL", f"decal island {size_mm[0]:.2f} x {size_mm[1]:.2f} mm: a side under {DECAL_MIN_MM:g} mm squashes the decal"
    return "PASS", f"decal island {size_mm[0]:.2f} x {size_mm[1]:.2f} mm"
