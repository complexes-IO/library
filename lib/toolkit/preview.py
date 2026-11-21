"""Shared preview renderer for the component library: orthographic z-buffer, millimetres, Z up. Flat shading on purpose:
it checks shapes and sizes; materials and light belong to Blender and Godot."""
import math, os
import numpy as np
from . import outfile
COL = {}
def mesh(prims, colliders=False, report=None):
    """outward faces (layer, object id, points) of every solid, with its holes and cuts cut (toolkit/csg.py); report, a dict, gets
    {object id: (primitive index, method)} for every solid that had openings. A Prims that states its own facet count (prims.facets)
    is meshed with it: every round face above 0.5 mm radius, holes and the pins in them alike."""
    from . import csg
    old = csg.FACETS; csg.FACETS = getattr(prims, "facets", None) or old
    try: return _mesh(prims, colliders, report)
    finally: csg.FACETS = old


def _mesh(prims, colliders=False, report=None):
    from . import csg
    faces = []; oid = 0
    subs = {}
    for L, k, q in prims:
        if k in ("hole", "cut"): subs.setdefault(q[-1], []).append((k, q))
    def quad(L, pts): faces.append((L, oid, pts))
    def bx(L, x, y, z, dx, dy, dz):
        p = [(x, y, z), (x + dx, y, z), (x + dx, y + dy, z), (x, y + dy, z), (x, y, z + dz), (x + dx, y, z + dz), (x + dx, y + dy, z + dz), (x, y + dy, z + dz)]
        for q in [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]: quad(L, [p[i] for i in q])
    def obox(L, o, ex, ey, ez, l, w, h):
        o = np.array(o, float); ex = np.array(ex, float); ey = np.array(ey, float); ez = np.array(ez, float)
        if np.cross(ex, ey) @ ez < 0: o = o + ex * l; ex = -ex        # left-handed frame: span it from the far x corner so faces point outward
        cs = [tuple(o + ex * l * sx + ey * w * sy + ez * h * sz) for sz in (0, 1) for (sx, sy) in ((0, 0), (1, 0), (1, 1), (0, 1))]
        for q in [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]: quad(L, [cs[i] for i in q])
    def prism(L, c1, c2, r, n=None):
        n = n or csg.segments(r)
        c1, c2 = np.array(c1, float), np.array(c2, float); d = c2 - c1; h = np.linalg.norm(d); d /= h
        up = np.array([0, 0, 1.0]) if abs(d[2]) < 0.99 else np.array([1.0, 0, 0]); u = np.cross(d, up); u /= np.linalg.norm(u); v = np.cross(d, u)
        ring = [c1 + (u * math.cos(2 * math.pi * i / n) + v * math.sin(2 * math.pi * i / n)) * r for i in range(n)]   # counter-clockwise about d
        for i in range(n):
            j = (i + 1) % n; quad(L, [tuple(ring[i]), tuple(ring[j]), tuple(ring[j] + d * h), tuple(ring[i] + d * h)])   # outward
        quad(L, [tuple(q) for q in reversed(ring)]); quad(L, [tuple(q + d * h) for q in ring])                           # caps outward
    for i, (L, k, p) in enumerate(prims):
        if L.startswith("collider:") and not colliders: continue
        oid = i + 1                                                    # object id = primitive index + 1: stable, names the primitive
        if i in subs and k in ("box", "obox", "cyl", "mesh"):
            F, how = csg.cut_solid(k, p, subs[i])
            if report is not None: report[oid] = (i, how)
            if F is not None:
                for ps in F: quad(L, [tuple(v) for v in ps])
                continue
        if k == "box": bx(L, *p)
        elif k == "obox": obox(L, *p)
        elif k == "cyl": prism(L, *p)
        elif k == "mesh":
            for t in p[0]: quad(L, [tuple(v) for v in t])
    return faces
DEFAULT_COL = {"M-STEEL-7035": "#d9d9d6", "M-GALV": "#b7bcc2", "M-GASKET": "#2a2a2a", "M-ZINC": "#a8adb3", "M-BLACK-PA": "#1f2124", "M-BRASS": "#b89a4a", "M-CU": "#b87333",
               "M-ALU-7035": "#d4d4d0", "M-GREEN": "#2fa84f", "M-RED": "#d9342b", "M-BLUE": "#2d6ae0", "M-YELLOW": "#f2c200", "M-LENS-GREEN": "#5ee08a", "M-LENS-RED": "#ff6a5c", "M-LENS-WHITE": "#f4f4ee",
               "M-DIN": "#c9ccd0", "M-GREY-PA": "#8d9196", "M-CAST-BLUE": "#2b4a8a", "M-CONCRETE": "#bdbbb4", "M-WALL": "#d9cbb8", "M-WOOD": "#b08a57", "M-LENS-DARK": "#2a2e36", "M-TITANIUM": "#9a9ea5",
               "M-WHITE-PA": "#e8e8e4", "M-WHITE-PVC": "#e8e8e4", "M-GREY-PVC": "#8d9196", "M-GREEN-YELLOW": "#3a9a3a", "M-YELLOW-PA": "#f2c200", "M-ALU-ANOD": "#c9cbcd", "M-ZINC-CAST": "#a0a2a5", "M-RED-PA": "#c0211b",
               "M-BLACK-PC": "#141416", "M-CABLE-PUR": "#1c1c20", "M-CABLE-GREY": "#808386", "M-LENS-YELLOW": "#f4d35e", "M-SILVER": "#d8d8dc", "M-GOLD": "#d4b03a", "M-BROWN": "#6b3e1f", "M-CU-CORRODED": "#5c8c72", "M-ORANGE-PA": "#f07a1a", "M-CASE-CLEAR": "#e4ecf2", "M-CAST-BLUE": "#2b4a8a"}
def colour(L):
    """a layer's preview colour: an explicit COL entry, else the material part of the layer (after the bar)"""
    return COL.get(L) or COL.get(L.split("|")[-1]) or DEFAULT_COL.get(L.split("|")[-1], "#999")
def render(faces, name, az=35, el=28, w=1600, h=1000, center=None, height=None, fname=None, out=None):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, matplotlib.colors as mc
    a, b = math.radians(az), math.radians(el)
    e = np.array([math.cos(b) * math.cos(a), math.cos(b) * math.sin(a), math.sin(b)])      # toward the camera
    right = np.cross(-e, [0, 0, 1.0]); right /= np.linalg.norm(right); up = np.cross(right, -e)   # camera at +e looking along -e, Z up, right-handed image
    def proj(P): P = np.asarray(P, float); return (P @ right, -(P @ up), P @ e)
    if center is None:
        pts = np.array([q for _, _, ps in faces for q in ps]); pr = np.array([proj(q)[:2] for q in pts])
        x0, x1, y0, y1 = pr[:, 0].min(), pr[:, 0].max(), pr[:, 1].min(), pr[:, 1].max(); sc = min(w * 0.92 / (x1 - x0), h * 0.92 / (y1 - y0))
    else:
        cx, cy = proj(center)[:2]; sc = h / height; x0 = x1 = cx; y0 = y1 = cy
    ox, oy = w / 2 - sc * (x0 + x1) / 2, h / 2 - sc * (y0 + y1) / 2
    zbuf = np.full((h, w), -np.inf); idb = np.full((h, w), -1); img = np.zeros((h, w, 3)); img[:] = (0.96, 0.96, 0.95)
    light = np.array([-0.3, -0.5, 0.8]); light /= np.linalg.norm(light); tris = []
    for L, oid, ps in faces:
        P = np.array(ps, float); n = np.cross(P[1] - P[0], P[2] - P[0]); nn = np.linalg.norm(n)
        if nn == 0: continue
        n /= nn
        if n @ e <= 0: continue
        sh = 0.55 + 0.45 * max(0, n @ light); col = tuple(np.clip(np.array(mc.to_rgb(colour(L))) * sh, 0, 1))
        q = [(ox + sc * a_, oy + sc * b_, d) for a_, b_, d in (proj(p) for p in ps)]
        for i in range(1, len(q) - 1): tris.append((oid, (q[0], q[i], q[i + 1]), col))
    for tid, ((xa, ya, za), (xb, yb, zb), (xc, yc, zc)), col in tris:
        xmin, xmax = int(max(0, math.floor(min(xa, xb, xc)))), int(min(w - 1, math.ceil(max(xa, xb, xc)))); ymin, ymax = int(max(0, math.floor(min(ya, yb, yc)))), int(min(h - 1, math.ceil(max(ya, yb, yc))))
        if xmin > xmax or ymin > ymax: continue
        det = (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)
        if abs(det) < 1e-9: continue
        X, Y = np.meshgrid(np.arange(xmin, xmax + 1) + 0.5, np.arange(ymin, ymax + 1) + 0.5)
        l1 = ((xb - xa) * (Y - ya) - (X - xa) * (yb - ya)) / det; l2 = ((X - xa) * (yc - ya) - (xc - xa) * (Y - ya)) / det; l0 = 1 - l1 - l2
        inside = (l0 >= -1e-6) & (l1 >= -1e-6) & (l2 >= -1e-6)
        if not inside.any(): continue
        z = l0 * za + l2 * zb + l1 * zc; sub = zbuf[ymin:ymax + 1, xmin:xmax + 1]; upd = inside & (z > sub)
        sub[upd] = z[upd]; idb[ymin:ymax + 1, xmin:xmax + 1][upd] = tid; img[ymin:ymax + 1, xmin:xmax + 1][upd] = col
    edge = np.zeros((h, w), bool); edge[:, 1:] |= idb[:, 1:] != idb[:, :-1]; edge[1:, :] |= idb[1:, :] != idb[:-1, :]; img[edge] *= 0.6
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=100); ax = fig.add_axes([0, 0, 1, 1]); ax.imshow(img); ax.set_axis_off()
    ax.text(14, h - 16, name, color="#555", fontsize=11, family="DejaVu Sans Mono"); outfile.savefig(fig, os.path.join(out or os.getcwd(), fname or f"preview-{name.split()[0]}.png"), dpi=100); plt.close(fig)

