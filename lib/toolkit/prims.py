"""Primitive list every element builds. Each entry is (layer, kind, params):
  box  (x, y, z, dx, dy, dz)             axis-aligned
  cyl  (p1, p2, r)                       between two points
  obox (o, ex, ey, ez, l, w, h)          oriented box: origin, unit axes, sizes
  hole (p1, p2, r, target)               cylinder subtracted from the primitive at index `target`
  cut  (o, ex, ey, ez, l, w, h, target)  oriented box subtracted from the primitive at index `target` (rectangular cut-outs, windows, notches)
  mesh (tris,)                           raw triangles [((x,y,z),(x,y,z),(x,y,z)), ...] for swept and lofted shapes (glTF and preview only)
Each method returns the index of what it appended (holes and cuts need it). box, cyl, obox and mesh take an optional part="<name>":
a part name kept beside the list in Prims.parts {index: name}, never in the layer, so no output (layers, census, glTF materials) reads
it; a tool keys on it where a layer can't tell one part from another (round 13 return: acad-gate.py's duct-finger exclusion). Holes and cuts are SUBTRACT: AutoCAD subtracts them, the glTF
writer and the previews cut them (toolkit/csg.py), the validation kernel tests against them."""
import math
import numpy as np

SUBTRACT = ("hole", "cut")      # kinds that remove material from the primitive whose index is their last parameter

class Prims(list):
    """pivots: {node: dict(kind="rotate"|"translate"|"emissive"|"port", origin=(x,y,z), axis=(x,y,z), range=(a,b), unit="deg"|"mm")}
    A node with a pivot is exported with its origin at `origin`, so Godot rotates / slides it in place.
    Colliders: a box on layer "collider:<name>" is exported as node <name>-colonly (Godot makes a convex collider, no mesh)."""
    def __init__(self, *a):
        super().__init__(*a); self.pivots = {}; self.owners = []     # owners: (start, end, tag, element id) per placed instance
        self.hosts = {}                                                 # surfaces other elements mount on and cut through: name -> (primitive index, thickness)
        self.parents = {}                                               # placed instance tag -> its BOM parent (what it rides on)
        self.params = {}                                                # placed instance tag -> the params it was built with (ratings follow them)
        self.parts = {}                                                 # primitive index -> part name (part="..."; carried by transform and library.place)
        self.radii = {}                                                 # primitive index -> its own fillet radius (fillet._radii; a bare lead's edge break)
    def _part(self, part):
        i = len(self) - 1
        if part: self.parts[i] = str(part)
        return i
    def host(self, name, index, thickness): self.hosts[name] = (index, float(thickness)); return index
    def pivot(self, node, kind, origin, axis=(0, 0, 1), range=(0, 0), unit=None, **extra):
        """extra: data the node carries for the twin (exported in the glTF extras): a contact's pole, gender, zone and condition, a port's
        mating data (gender, key, thread, seal), a nut's lead. Vectors in extra named keyref are rotated with the element when placed."""
        self.pivots[node] = dict(kind=kind, origin=tuple(float(v) for v in origin), axis=tuple(float(v) for v in axis), range=tuple(range), unit=unit or ("deg" if kind == "rotate" else "mm"), **extra)
    def collider(self, name, x, y, z, dx, dy, dz): self.append((f"collider:{name}", "box", (x, y, z, dx, dy, dz))); return len(self) - 1
    def box(self, L, x, y, z, dx, dy, dz, part=None): self.append((L, "box", (x, y, z, dx, dy, dz))); return self._part(part)
    def cyl(self, L, p1, p2, r, part=None): self.append((L, "cyl", (tuple(p1), tuple(p2), r))); return self._part(part)
    def obox(self, L, o, ex, ey, ez, l, w, h, part=None): self.append((L, "obox", (tuple(o), tuple(ex), tuple(ey), tuple(ez), l, w, h))); return self._part(part)
    def hole(self, L, p1, p2, r, target): self.append((L, "hole", (tuple(p1), tuple(p2), r, target))); return len(self) - 1
    def cut(self, L, o, ex, ey, ez, l, w, h, target): self.append((L, "cut", (tuple(o), tuple(ex), tuple(ey), tuple(ez), l, w, h, target))); return len(self) - 1
    def cutbox(self, L, x, y, z, dx, dy, dz, target):
        """an axis-aligned rectangular cut-out (x, y, z, dx, dy, dz as for box) through the primitive at index `target`"""
        return self.cut(L, (x, y, z), (1, 0, 0), (0, 1, 0), (0, 0, 1), dx, dy, dz, target)
    def mesh(self, L, tris, part=None): self.append((L, "mesh", (list(tris),))); return self._part(part)

def rotation_yp(yaw=0.0, pitch=0.0, roll=0.0):
    """the placement rotation: roll about the element's own y first, then pitch about its x, then yaw about Z (degrees). Roll turns
    +z toward +x: clockwise looking along +y, the way toolkit/m12.py measures a port's clocking (round 5: the LioN-X ports)"""
    a = math.radians(yaw); c, s = math.cos(a), math.sin(a); b = math.radians(pitch); cb, sb = math.cos(b), math.sin(b)
    g = math.radians(roll); cg, sg = math.cos(g), math.sin(g)
    return (np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]]) @ np.array([[1.0, 0, 0], [0, cb, -sb], [0, sb, cb]])
            @ np.array([[cg, 0, sg], [0, 1.0, 0], [-sg, 0, cg]]))

def transform(prims, at=(0, 0, 0), yaw=0.0, rename=None, base=0, pitch=0.0, roll=0.0, own_body=False):
    """copy prims translated by `at` after a roll about the element's y, a pitch about its x and a yaw about Z (degrees).
    `rename(node) -> node` renames node layers; `base` offsets hole targets (the index the first copied primitive will have in the
    receiving list). `own_body`: True, the copy's unnamed solids become their own part, rename("body") (an element placed in an
    assembly stays removable as a whole, EM 2026-11-08); a node name, they join that node (a child on a moving host rides with
    it); False, an element composing its children keeps them in its body."""
    t = np.array(at, float); R = rotation_yp(yaw, pitch, roll); axis_aligned = abs(yaw) < 1e-9 and abs(pitch) < 1e-9 and abs(roll) < 1e-9
    def p_(p): return tuple(R @ np.array(p, float) + t)
    def v_(v): return tuple(R @ np.array(v, float))
    def lay_(L):
        if rename and L.startswith("node:"):
            node, mat = L[5:].split("|", 1); return f"node:{rename(node)}|{mat}"
        if own_body and rename and not L.startswith("collider:") and rename("body") != "body":
            return f"node:{own_body if isinstance(own_body, str) else rename('body')}|{L}"   # <tag>.body (True): never fused into the
        return L                                      # assembly's body, the machine comes apart; a node name: joins that node (a door's e-stop)
    out = Prims()
    for s0, e0, tg, eid in getattr(prims, "owners", []):
        out.owners.append((s0 + base, e0 + base, rename(tg) if rename else tg, eid))
    for hn, (hi, ht) in getattr(prims, "hosts", {}).items():
        out.hosts[rename(hn) if rename else hn] = (hi + base, ht)
    for tg, pa in getattr(prims, "parents", {}).items():
        out.parents[rename(tg) if rename else tg] = (rename(pa) if rename and pa and pa != "fixed" else pa)   # "fixed" stays a word (cadout)
    for tg, pr in getattr(prims, "params", {}).items():
        out.params[rename(tg) if rename else tg] = pr
    for i, nm in getattr(prims, "parts", {}).items():
        out.parts[i + base] = rename(nm) if rename else nm
    for i, rr in getattr(prims, "radii", {}).items():
        out.radii[i + base] = rr
    for node, pv in getattr(prims, "pivots", {}).items():
        out.pivots[rename(node) if rename else node] = dict(pv, origin=p_(pv["origin"]), axis=v_(pv["axis"]), **({"keyref": v_(pv["keyref"])} if "keyref" in pv else {}))
    for L, k, q in prims:
        L = lay_(L)
        if k == "box":
            x, y, z, dx, dy, dz = q
            if axis_aligned: out.append((L, "box", (x + t[0], y + t[1], z + t[2], dx, dy, dz)))
            else: out.append((L, "obox", (p_((x, y, z)), v_((1, 0, 0)), v_((0, 1, 0)), v_((0, 0, 1)), dx, dy, dz)))
        elif k == "cyl": p1, p2, r = q; out.append((L, "cyl", (p_(p1), p_(p2), r)))
        elif k == "obox": o, ex, ey, ez, l, w, h = q; out.append((L, "obox", (p_(o), v_(ex), v_(ey), v_(ez), l, w, h)))
        elif k == "hole": p1, p2, r, tg = q; out.append((L, "hole", (p_(p1), p_(p2), r, tg + base)))
        elif k == "cut": o, ex, ey, ez, l, w, h, tg = q; out.append((L, "cut", (p_(o), v_(ex), v_(ey), v_(ez), l, w, h, tg + base)))
        elif k == "mesh": out.append((L, "mesh", ([tuple(p_(v) for v in t) for t in q[0]],)))
    return out

def extents(prims):
    """axis-aligned bounding box of the solids (holes ignored): (min xyz, max xyz) in mm"""
    pts = []
    for L, k, q in prims:
        if L.startswith("collider:"): continue
        if k == "box": x, y, z, dx, dy, dz = q; pts += [(x, y, z), (x + dx, y + dy, z + dz)]
        elif k == "cyl":
            p1, p2, r = q; p1, p2 = np.array(p1, float), np.array(p2, float); d = p2 - p1; d /= np.linalg.norm(d)
            e = r * np.sqrt(np.clip(1 - d * d, 0, 1)); pts += [tuple(p1 - e), tuple(p1 + e), tuple(p2 - e), tuple(p2 + e)]
        elif k == "obox":
            o, ex, ey, ez, l, w, h = q; o, ex, ey, ez = (np.array(v, float) for v in (o, ex, ey, ez))
            pts += [tuple(o + ex * l * a + ey * w * b + ez * h * c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
        elif k == "mesh": pts += [v for t in q[0] for v in t]
    A = np.array(pts); return tuple(np.round(A.min(axis=0), 2)), tuple(np.round(A.max(axis=0), 2))

def nodes(prims):
    return sorted({L[5:].split("|", 1)[0] for L, _, _ in prims if L.startswith("node:")})

def solids(prims):
    """the primitives that are solids: no holes or cuts, no colliders (indices change: use it for counting, not for hole targets)"""
    return Prims([q for q in prims if q[1] not in SUBTRACT and not q[0].startswith("collider:")])
