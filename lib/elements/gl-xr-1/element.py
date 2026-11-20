#!/usr/bin/env python3
"""gl-xr-1: the institute's own display glasses, a prop for the site and the virtual campus. A full-rim frame sized by the boxing
system (ISO 8624), clear 2 mm meniscus lenses seated in a rim groove with a display window inside each, a slim brow module with a
knurled dial behind each rim, three-knuckle screw hinges, temples that taper to the tip and curve down behind the ear, nose pads
on wire arms, and the institute's mark inlaid in the outer face of each temple (toolkit/mark.py: the one outline every element
carries, from the site's own mark). Every outer edge is rounded in the geometry here (no box primitive is visible). Our design; not a
vendor's shape."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
from toolkit import library, mark as MK, sweep as SW
from toolkit.prims import Prims

ID, VERSION, CLASS = "gl-xr-1", "2.0", "prop"
TITLE = "display glasses, full-rim frame, clear lenses with a display window, screw hinges, tapered temples"
TOOLKIT = "1.3"
BASELINE = "ISO 8624 boxing system: lens 52 x 40, bridge 18, temple 145, overall width 143 (adult ranges, EM's brief 2026-11-20); the shape is our own"
ORIGIN = "bridge centre on the front face; lenses in the xz plane, temples toward +y (the wearer's side)"
COMMAND = "GLXR"
PARAMS = dict(fold=0.0)                                   # temple fold angle, degrees (0 open, 90 folded)
FOLD = dict(r=90.0, l=84.0)                               # the right temple folds flat first, the left comes to rest over it (MOT-010: both at 90 would share space)
TRIANGLES = 60000                                         # EM's brief 2026-11-20: web-light, under 60 000 (the rounded edges are geometry, not a bevel)

# ---- boxing system (ISO 8624), mm
LENS_A, LENS_B, DBL, TEMPLE_L = 52.0, 40.0, 18.0, 145.0   # horizontal and vertical boxed lens size, distance between lenses, overall length of side
CX = DBL / 2 + LENS_A / 2                                 # boxed lens centre x (35: centre distance 70)
# ---- lens: a meniscus, two concentric spheres, 2 mm thick, front vertex 0.2 behind the frame's front plane
LENS_T, LENS_R, LENS_Y = 2.0, 350.0, 0.2
EYE_DX, EYE_DZ, DISP_W, DISP_H, DISP_T = -3.0, 1.5, 22.0, 13.0, 0.3    # the display window: centre from the boxed centre (3 nasal: PD 64), size, thickness
# ---- frame sections
RIM_D, RIM_OUT, RIM_IN, GROOVE = 4.6, 2.7, 0.8, 0.15      # rim depth; rim outside the lens edge; lip over the lens edge; groove floor clearance
LUG = dict(w=4.4, h=9.0, r=1.3)                           # end piece and temple butt section: thickness x height, edge radius
LUG_X, HINGE_Z = 68.2, 13.0                               # end piece and temple centre line x; hinge height
HINGE_X, HINGE_Y, HINGE_R = 64.35, 9.6, 1.5               # hinge axis (vertical), proud of the inner faces; knuckle radius
JOINT = 0.15                                              # half the butt joint between end piece and temple
MARK = dict(d=6.0, line=0.4, behind=12.0, proud=0.03, depth=0.3)   # the mark: ring outer diameter and line; its centre behind the hinge axis; inlay proud of the face (GEO-050: never coplanar) and deep


def _orient(tris):
    """a closed shell, outward: flip every triangle when the signed volume is negative"""
    A = np.array(tris, float); vol = np.einsum("ij,ij->i", A[:, 0], np.cross(A[:, 1], A[:, 2])).sum()
    return [(t[0], t[2], t[1]) for t in tris] if vol < 0 else list(tris)


def _loft(rings, closed=False, c0=None, c1=None):
    """triangles through a row of rings (same point count each); an open row is capped by a fan from c0 / c1 (default: the ring's mean)"""
    R = [[tuple(float(v) for v in p) for p in r] for r in rings]; n = len(R); m = len(R[0]); tris = []
    for i in range(n if closed else n - 1):
        r0, r1 = R[i], R[(i + 1) % n]
        for j in range(m):
            k = (j + 1) % m; tris.append((r0[j], r1[j], r1[k])); tris.append((r0[j], r1[k], r0[k]))
    if not closed:
        m0 = tuple(np.mean(R[0], axis=0)) if c0 is None else tuple(float(v) for v in c0)
        m1 = tuple(np.mean(R[-1], axis=0)) if c1 is None else tuple(float(v) for v in c1)
        for j in range(m):
            k = (j + 1) % m; tris.append((m0, R[0][j], R[0][k])); tris.append((m1, R[-1][k], R[-1][j]))
    return _orient(tris)


def _round_poly(corners, radii, arcs):
    """a closed 2D outline through `corners`, each rounded to its own radius with its own number of arc segments"""
    pts = []; n = len(corners); C = [np.array(c, float) for c in corners]
    for i in range(n):
        p0, p1, p2 = C[i - 1], C[i], C[(i + 1) % n]; r = radii[i]
        if r <= 0: pts.append(p1); continue
        d0 = p0 - p1; d0 /= np.linalg.norm(d0); d2 = p2 - p1; d2 /= np.linalg.norm(d2)
        ang = math.acos(np.clip(d0 @ d2, -1, 1)); t = r / math.tan(ang / 2)
        a, b = p1 + d0 * t, p1 + d2 * t; bis = d0 + d2; bis /= np.linalg.norm(bis); c = p1 + bis * (r / math.sin(ang / 2))
        a0 = math.atan2(*(a - c)[::-1]); a1 = math.atan2(*(b - c)[::-1]); da = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        pts += [c + r * np.array([math.cos(a0 + da * k / arcs[i]), math.sin(a0 + da * k / arcs[i])]) for k in range(arcs[i] + 1)]
    return np.array(pts)


def _spline(ctrl, per=24):
    """a Catmull-Rom curve through the control points, as a dense polyline"""
    C = [np.array(c, float) for c in ctrl]; C = [2 * C[0] - C[1]] + C + [2 * C[-1] - C[-2]]; out = []
    for i in range(1, len(C) - 2):
        p0, p1, p2, p3 = C[i - 1], C[i], C[i + 1], C[i + 2]
        for t in np.linspace(0, 1, per, endpoint=False):
            out.append(0.5 * (2 * p1 + (p2 - p0) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (3 * p1 - p0 - 3 * p2 + p3) * t ** 3))
    return np.array(out + [C[-2]])


class _Path:
    """a polyline read by arc length"""
    def __init__(self, pts):
        self.P = np.array(pts, float); self.S = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(self.P, axis=0), axis=1))]); self.L = float(self.S[-1])
    def at(self, s): return np.array([np.interp(s, self.S, self.P[:, k]) for k in range(3)])
    def tan(self, s):
        d = self.at(min(s + 0.05, self.L)) - self.at(max(s - 0.05, 0.0)); return d / np.linalg.norm(d)
    def cut(self, length): return _Path([self.at(s) for s in np.linspace(0, length, max(8, int(length)))])


def _section(w, h, r): return w, h, min(r, w / 2 - 0.1, h / 2 - 0.1)


def bar(pts, sec, up=(0, 0, 1.0), dome=(True, True), step=2.0, arc=6):
    """a rounded bar along a path: section sec(s) -> (width, height, edge radius), height along `up`. A domed end is the same edge
    radius carried round the end face (a filleted end), so the bar has no sharp edge anywhere; `arc` segments per quarter circle."""
    pa = pts if isinstance(pts, _Path) else _Path(pts); sec_ = sec if callable(sec) else (lambda s: sec)
    r0 = _section(*sec_(0.0))[2]; r1 = _section(*sec_(pa.L))[2]; st = []; q = [math.radians(90.0 * i / arc) for i in range(1, arc + 1)]
    if dome[0]: st += [(r0 * (1 - math.sin(a)), r0 * (1 - math.cos(a))) for a in reversed(q)]
    a_, b_ = (r0 if dome[0] else 0.0), pa.L - (r1 if dome[1] else 0.0); n = max(1, int(math.ceil((b_ - a_) / step)))
    st += [(a_ + (b_ - a_) * i / n, 0.0) for i in range(n + 1)]
    if dome[1]: st += [(pa.L - r1 * (1 - math.sin(a)), r1 * (1 - math.cos(a))) for a in q]
    U0 = np.array(up, float); rings = []
    for s, e in st:
        w, h, r = _section(*sec_(s)); prof = SW.rounded_rect_profile(w - 2 * e, h - 2 * e, max(r - e, 0.05), arc)
        p = pa.at(s); T = pa.tan(s); V = U0 - T * (U0 @ T); V /= np.linalg.norm(V); U = np.cross(T, V)
        rings.append([p + U * a + V * b for a, b in prof])
    return _loft(rings)


def wire(pts, r, n=14, step=1.0):
    """a round wire along a path, flat ends (both are buried in what it joins)"""
    pa = _Path(pts); rings = []
    for s in np.linspace(0, pa.L, max(2, int(math.ceil(pa.L / step)) + 1)):
        p = pa.at(s); T = pa.tan(s); V = np.array([0, 0, 1.0]); V = V - T * (V @ T); V /= np.linalg.norm(V); U = np.cross(T, V)
        rings.append([p + r * (math.cos(2 * math.pi * j / n) * U + math.sin(2 * math.pi * j / n) * V) for j in range(n)])
    return _loft(rings)


def lathe(base, profile, n=28, amp=None):
    """a turned part about a vertical axis through `base`: profile [(radius, z)], first and last on the axis; amp[k] adds a
    straight knurl of that depth to profile point k (radius alternates up and down round the part)"""
    b = np.array(base, float); amp = amp or [0.0] * len(profile); rings = []
    for (r, z), a in zip(profile[1:-1], amp[1:-1]):
        rings.append([b + np.array([(r + (a / 2 if j % 2 == 0 else -a / 2)) * math.cos(2 * math.pi * j / n), (r + (a / 2 if j % 2 == 0 else -a / 2)) * math.sin(2 * math.pi * j / n), z]) for j in range(n)])
    return _loft(rings, c0=b + np.array([0, 0, profile[0][1]]), c1=b + np.array([0, 0, profile[-1][1]]))


def _turned(r, z0, z1, rho, arcs=5):
    """profile of a cylinder r between z0 and z1 with both rims rounded to rho"""
    lo = [(r - rho + rho * math.sin(a), z0 + rho - rho * math.cos(a)) for a in np.linspace(0, math.pi / 2, arcs + 1)]
    hi = [(r - rho + rho * math.cos(a), z1 - rho + rho * math.sin(a)) for a in np.linspace(0, math.pi / 2, arcs + 1)]
    return [(0.0, z0)] + lo + hi + [(0.0, z1)]


def lens_outline():
    """the lens shape, (N, 2) points (x outward, z up) about the boxed centre, counter-clockwise seen from the front, exactly
    LENS_A x LENS_B by the boxing system: a soft rectangle, the top edge rising a little outward, the nasal lower corner the roundest.
    Corners in 5 degree steps (the rim that follows them shows no facet), straight runs in pieces of 6 at most (the meniscus edge)."""
    c = _round_poly([(-24.5, -20.0), (25.0, -20.0), (26.0, 19.2), (-26.0, 17.6)], [12.0, 10.0, 7.5, 6.5], [18, 18, 18, 18]); o = []
    for a, b in zip(c, np.roll(c, -1, axis=0)):
        k = max(1, int(math.ceil(np.linalg.norm(b - a) / 6.0))); o += [a + (b - a) * j / k for j in range(k)]
    o = np.array(o); lo, hi = o.min(axis=0), o.max(axis=0)
    return (o - (lo + hi) / 2) * np.array([LENS_A / (hi[0] - lo[0]), LENS_B / (hi[1] - lo[1])])


def _normals(o):
    """outward unit normals of a counter-clockwise outline"""
    t = np.roll(o, -1, axis=0) - np.roll(o, 1, axis=0); n = np.stack([t[:, 1], -t[:, 0]], axis=1)
    return n / np.linalg.norm(n, axis=1)[:, None]


def _sph(x, z, rad):
    """y of the sphere of radius rad about the lens's centre of curvature, at (x, z) from the boxed centre"""
    return LENS_Y + LENS_R - math.sqrt(rad * rad - x * x - z * z)


def shell(o, rf, rb, ts=(0.5, 1.0)):
    """a curved plate over outline o between the spheres rf (front) and rb (back): the lens, and the display window inside it"""
    c = o.mean(axis=0); m = len(o); tris = []
    def face(rad): return (CX + c[0], _sph(c[0], c[1], rad), c[1]), [[(CX + c[0] + t * (x - c[0]), _sph(c[0] + t * (x - c[0]), c[1] + t * (z - c[1]), rad), c[1] + t * (z - c[1])) for x, z in o] for t in ts]
    (f0, F), (b0, B) = face(rf), face(rb)
    for j in range(m):
        k = (j + 1) % m; tris.append((f0, F[0][j], F[0][k])); tris.append((b0, B[0][k], B[0][j]))
        for a in range(len(ts) - 1):
            tris += [(F[a][j], F[a + 1][j], F[a + 1][k]), (F[a][j], F[a + 1][k], F[a][k]), (B[a][j], B[a + 1][k], B[a + 1][j]), (B[a][j], B[a][k], B[a + 1][k])]
        tris += [(F[-1][j], B[-1][j], B[-1][k]), (F[-1][j], B[-1][k], F[-1][k])]
    return _orient(tris)


def rim(o, nrm):
    """the rim: a closed section carried round the lens outline, its groove following the lens edge (the lens is a meniscus, so its
    edge is not in one plane). Section in (depth y, radial b): b < 0 over the lens, the lens edge at b = 0."""
    rings = []
    for (x, z), (nx, nz) in zip(o, nrm):
        g0 = _sph(x, z, LENS_R) - 0.1; g1 = _sph(x, z, LENS_R - LENS_T) + 0.1
        prof = _round_poly([(0.0, -RIM_IN), (0.0, RIM_OUT), (RIM_D, RIM_OUT), (RIM_D, -RIM_IN), (g1, -RIM_IN), (g1, GROOVE), (g0, GROOVE), (g0, -RIM_IN)],
                           [0.3, 1.0, 1.0, 0.3, 0.2, 0.12, 0.12, 0.2], [5, 7, 7, 5, 3, 2, 2, 3])
        rings.append([(CX + x + nx * b, a, z + nz * b) for a, b in prof])
    return _loft(rings, closed=True)


def screw_head(c, r=1.05, h=0.6, slot=0.2, depth=0.3):
    """a slotted pan head on top of the hinge: sections across the slot, the slot a lower section between two short ramps"""
    xs = [-r * math.cos(math.radians(a)) for a in (6, 16, 30, 45, 60, 74)]; st = [(x, h) for x in xs] + [(-slot - 0.02, h), (-slot + 0.06, h - depth)]
    st += [(-x, hh) for x, hh in reversed(st)]; rings = []
    for x, hh in st:
        w = 2 * math.sqrt(r * r - x * x); rc = min(0.25, w / 2 - 0.03, hh / 2 - 0.03)
        rings.append([(c[0] + x, c[1] + a, c[2] + hh / 2 + b) for a, b in SW.rounded_rect_profile(w, hh, rc)])
    return _loft(rings)


def _rim_point(o, nrm, nasal, z, b, y):
    """the point at radial offset b on the rim section nearest height z, on the nasal or the temporal side"""
    i = min((i for i in range(len(o)) if (o[i][0] < 0) == nasal), key=lambda i: abs(o[i][1] - z))
    return np.array([CX + o[i][0] + nrm[i][0] * b, y, o[i][1] + nrm[i][1] * b])


def _side(fold, sd):
    """every part of one side, built on +x, as (layer, triangles, moves with the temple); the -x side is the mirror image, but for
    the mark, which reads left to right on both: toward the back on +x (side r), toward the front on -x (side l)"""
    o = lens_outline(); nrm = _normals(o); out = []; BLK, TI, GREY = "M-BLACK-MATTE", "M-TI-BRUSHED", "M-GREY-PA"
    F = "node:frame|"; T = "node:temple-{sd}|"
    out.append((F + BLK, rim(o, nrm), False))
    out.append(("node:lens-{sd}|M-LENS-CLEAR", shell(o, LENS_R, LENS_R - LENS_T), False))
    d = SW.rounded_outline([(EYE_DX - DISP_W / 2, EYE_DZ - DISP_H / 2), (EYE_DX + DISP_W / 2, EYE_DZ - DISP_H / 2), (EYE_DX + DISP_W / 2, EYE_DZ + DISP_H / 2), (EYE_DX - DISP_W / 2, EYE_DZ + DISP_H / 2)], [1.5] * 4, 3)
    out.append(("node:display-{sd}|M-WAVEGUIDE", shell(d, LENS_R - LENS_T / 2 + DISP_T / 2, LENS_R - LENS_T / 2 - DISP_T / 2, ts=(1.0,)), False))
    # brow module: a slim bar behind the top of the rim, flush with its top, no lower than the rim's own band
    top = sorted((p for p in o if p[1] > 0), key=lambda p: p[0]); zt = lambda x: float(np.interp(x, [p[0] for p in top], [p[1] for p in top]))
    out.append((F + BLK, bar([(CX + x, 6.8, zt(x) + RIM_OUT - 1.7) for x in np.linspace(-16, 18, 18)], (6.0, 3.4, 1.2), step=2.5), False))
    dz = zt(4.0) + RIM_OUT                                                                    # the module's top under the dial
    pr = [(0.0, dz - 0.4), (2.7, dz - 0.4), (2.7, dz + 1.3)] + [(2.1 + 0.6 * math.cos(a), dz + 1.4 + 0.6 * math.sin(a)) for a in np.linspace(0, math.pi / 2, 7)] + [(0.0, dz + 2.0)]
    out.append(("node:dial-{sd}|" + GREY, lathe((CX + 4.0, 6.8, 0.0), pr, n=80, amp=[0, 0.22, 0.22] + [0] * 8), False))
    # end piece: out of the rim's temporal side, round the corner, back to the butt joint
    e0 = _rim_point(o, nrm, False, HINGE_Z, 0.2, RIM_D / 2); arc = [(64.5 + 3.7 * math.sin(a), 6.0 - 3.7 * math.cos(a), HINGE_Z) for a in np.linspace(0, math.pi / 2, 19)]
    out.append((F + BLK, bar([tuple(e0)] + arc + [(LUG_X, HINGE_Y - JOINT, HINGE_Z)], (LUG["w"], LUG["h"], LUG["r"]), step=0.5), False))
    # hinge: two knuckles and a leaf on the frame, one knuckle and a leaf on the temple, a slotted screw down the axis
    ax = (HINGE_X, HINGE_Y, 0.0); k = 2.3; z0 = HINGE_Z - 1.5 * k - 0.1
    for a, moves in ((z0, False), (z0 + k + 0.1, True), (z0 + 2 * k + 0.2, False)):
        out.append(((T if moves else F) + TI, lathe(ax, _turned(HINGE_R, a, a + k, 0.5)), moves))
        y0, y1 = (HINGE_Y, 12.2) if moves else (7.0, HINGE_Y)
        out.append(((T if moves else F) + TI, bar([(65.5, y0, a + k / 2), (65.5, y1, a + k / 2)], (1.2, k, 0.5), dome=(not moves, moves), step=1.0, arc=4), moves))   # the knuckle's tab
    out.append((F + TI, bar([(65.5, 3.6, HINGE_Z), (65.5, 7.9, HINGE_Z)], (1.2, 3 * k + 0.2, 0.5), step=1.5, arc=4), False))                 # frame leaf, on the end piece's inner face
    out.append((T + TI, bar([(65.5, 11.4, HINGE_Z), (65.5, 17.0, HINGE_Z)], (1.2, 3 * k + 0.2, 0.5), step=1.5, arc=4), True))                  # temple leaf
    out.append((F + TI, screw_head((HINGE_X, HINGE_Y, z0 + 3 * k + 0.1)), False))
    out.append((F + TI, lathe(ax, [(0.0, z0 - 0.35)] + [(0.6 * math.sin(a), z0 - 0.35 * math.cos(a)) for a in np.linspace(math.pi / 8, math.pi / 2, 4)] + [(0.0, z0 + 0.1)], n=12), False))   # the screw's end
    # temple: a butt the end piece's section, tapering all the way, bowing a little out then in, curving down behind the ear;
    # its length by ISO 8624 is from the hinge axis to the tip along the centre line
    cl = _spline([(LUG_X, HINGE_Y + JOINT, HINGE_Z), (LUG_X, 22.0, HINGE_Z), (LUG_X + 0.8, 45.0, HINGE_Z + 0.1), (LUG_X + 1.2, 68.0, HINGE_Z - 0.2), (LUG_X + 0.7, 88.0, HINGE_Z - 1.4),
                  (LUG_X - 0.2, 103.0, HINGE_Z - 4.4), (LUG_X - 1.3, 115.0, HINGE_Z - 9.6), (LUG_X - 2.4, 124.5, HINGE_Z - 16.5), (LUG_X - 3.5, 132.0, HINGE_Z - 24.5), (LUG_X - 4.6, 138.5, HINGE_Z - 33.0)])
    pa = _Path(cl).cut(TEMPLE_L - JOINT); tab = [(0.0, 4.4, 9.0, 1.3), (40.0, 4.2, 8.6, 1.3), (95.0, 3.2, 6.4, 1.2), (pa.L, 2.7, 5.0, 1.1)]
    sec = lambda s: tuple(float(np.interp(s, [r[0] for r in tab], [r[i] for r in tab])) for i in (1, 2, 3))
    out.append((T + BLK, bar(pa, sec, step=3.0), True))
    # the mark: a titanium inlay following the temple's outer face, centred on its height, MARK behind the hinge axis
    grid = np.linspace(0.0, 40.0, 161); ys = [pa.at(s)[1] for s in grid]; d = 1.0 if sd == "r" else -1.0
    def face(y): s = float(np.interp(y, ys, grid)); q = pa.at(s); return q[0] + sec(s)[0] / 2, q[2]
    yc = HINGE_Y + MARK["behind"]; zc = face(yc)[1]
    for region in MK.regions(MARK["d"], MARK["line"]):
        out.append((T + TI, MK.inlay(region, lambda u, v, top: (face(yc + d * u)[0] + (MARK["proud"] if top else -MARK["depth"]), yc + d * u, zc + v)), True))
    # nose pad on a wire arm (the body: neither frame nor temple)
    a0 = _rim_point(o, nrm, True, -5.0, 1.0, 4.0); pc = np.array([a0[0] - 1.0, 11.9, -8.6])
    out.append((TI, wire(_spline([tuple(a0), (a0[0] - 0.6, 7.0, -5.3), (a0[0] - 1.3, 9.8, -6.4), tuple(pc + np.array([0.5, -0.4, 1.0]))], 8).tolist(), 0.6), False))
    pd = np.array([0.3, 0.1, -1.0]); pd /= np.linalg.norm(pd)
    out.append((GREY, bar([tuple(pc - 5.5 * pd), tuple(pc + 5.5 * pd)], (2.2, 5.6, 1.0), up=(0.35, 1.0, 0.0), step=1.5), False))
    if fold:                                                    # the temple and its half of the hinge turn about the hinge axis, inward
        a = math.radians(fold); c, s = math.cos(a), math.sin(a)
        rot = lambda p: (HINGE_X + (p[0] - HINGE_X) * c - (p[1] - HINGE_Y) * s, HINGE_Y + (p[0] - HINGE_X) * s + (p[1] - HINGE_Y) * c, p[2])
        out = [(L, [tuple(rot(p) for p in t) for t in tris] if moves else tris, moves) for L, tris, moves in out]
    return out, dz


def build(fold=0.0):
    P = Prims()
    for s, sd in ((1, "r"), (-1, "l")):
        side, dz = _side(min(fold, FOLD[sd]), sd)
        for L, tris, _ in side:
            P.mesh(L.format(sd=sd), tris if s > 0 else _orient([tuple((-p[0], p[1], p[2]) for p in t) for t in tris]))
    o = lens_outline(); e = _rim_point(o, _normals(o), True, 12.5, 0.2, RIM_D / 2)             # bridge: rim to rim, a low arch, 4.4 deep x 4.6 high
    P.mesh("node:frame|M-BLACK-MATTE", bar(_spline([(-e[0], e[1], e[2]), (-4.0, e[1], e[2] + 1.5), (0.0, e[1], e[2] + 2.0), (4.0, e[1], e[2] + 1.5), tuple(e)], 10), (4.4, 4.6, 1.3), step=1.0))
    P.pivot("frame", "fixed", (0, 0, 0))
    for s, sd in ((1, "r"), (-1, "l")):
        P.pivot(f"lens-{sd}", "emissive", (s * CX, LENS_Y, 0), axis=(0, -1, 0), range=(0, 1))
        P.pivot(f"display-{sd}", "emissive", (s * (CX + EYE_DX), LENS_Y + LENS_T / 2, EYE_DZ), axis=(0, -1, 0), range=(0, 1))   # the display window: where the image leaves the lens
        P.pivot(f"temple-{sd}", "rotate", (s * HINGE_X, HINGE_Y, HINGE_Z), axis=(0, 0, 1), range=(0, FOLD[sd] * s))             # about the hinge screw
        P.pivot(f"dial-{sd}", "rotate", (s * (CX + 4.0), 6.8, dz + 1.0), axis=(0, 0, 1), range=(0, 300))
    P.collider("front", -72, -0.5, -24, 144, 13, 50); P.collider("temple-l", -73, 9, -22, 10, 128, 42); P.collider("temple-r", 63, 9, -22, 10, 128, 42)
    return P


PREVIEWS = [dict(name="front", az=270, el=4), dict(name="three-quarter", az=238, el=14), dict(name="side temples and hinge", az=180, el=8),
            dict(name="folded temples", az=238, el=14, params=dict(fold=90))]

if __name__ == "__main__": print(library.emit(sys.modules[__name__]))
