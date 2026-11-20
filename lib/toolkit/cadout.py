"""Shared AutoCAD writer for the component library: primitives -> AutoLISP with true solids. Millimetres (INSUNITS 4).
Primitive kinds: box (x, y, z, dx, dy, dz) · cyl (p1, p2, r) · obox (origin, ex, ey, ez, l, w, h) · hole and cut (subtracted from their
target). Each primitive carries a layer;
layers named M-<material> so Blender maps materials by layer. A 'node' prefix in the layer name (node:<name>|M-...) marks a named part."""
import numpy as np
from . import outfile
def layer_name(lay):
    """node:<name>|M-<mat> -> node-<name>_M-<mat>: a colon is not a layer character in AutoCAD; this is the form on disk"""
    return lay.replace("|", "_").replace(":", "-")
def f(v): return f"{v:.4f}".rstrip("0").rstrip(".") if abs(v) > 1e-9 else "0"
def pt(p): return f"(list {f(p[0])} {f(p[1])} {f(p[2])})"
HEAD = ["(defun BX (lay p1 p2 h) (command \"_.-LAYER\" \"_M\" lay \"\") (command \"_.BOX\" p1 p2 h) (entlast))",
        "(defun CY (lay p1 p2 r / h) (setq h (distance p1 p2)) (command \"_.-LAYER\" \"_M\" lay \"\")",
        "  (command \"_.UCS\" \"_ZA\" p1 p2) (command \"_.CYLINDER\" (list 0 0 0) r h) (command \"_.UCS\" \"_W\") (entlast))",
        "(defun UB (lay o xp yp l w h) (command \"_.-LAYER\" \"_M\" lay \"\")",
        "  (command \"_.UCS\" \"3\" o xp yp) (command \"_.BOX\" (list 0 0 0) (list l w 0) h) (command \"_.UCS\" \"_W\") (entlast))"]
def write_lsp(path, cmd, prims, title):
    L = [f";; {title}. Generated. Millimetres. APPLOAD, then {cmd}."] + HEAD + [f"(defun c:{cmd} (/ os hole {" ".join(f"e{i}" for i in range(len(prims)))})",
         "  (setq os (getvar \"OSMODE\")) (setvar \"OSMODE\" 0) (setvar \"CMDECHO\" 0) (setvar \"INSUNITS\" 4) (setvar \"ISOLINES\" 8)"]
    targets = {q[-1] for _, k, q in prims if k in ("hole", "cut")}
    for i, (lay, kind, p) in enumerate(prims):
        if lay.startswith("collider:"): continue                      # Godot only
        lay = layer_name(lay)
        if kind == "box":
            x, y, z, dx, dy, dz = p; L.append(f"  (setq e{i} (BX \"{lay}\" {pt((x, y, z))} {pt((x + dx, y + dy, z))} {f(dz)}))" if i in targets else f"  (BX \"{lay}\" {pt((x, y, z))} {pt((x + dx, y + dy, z))} {f(dz)})")
        elif kind == "cyl":
            p1, p2, r = p; call = f"(CY \"{lay}\" {pt(p1)} {pt(p2)} {f(r)})"; L.append(f"  (setq e{i} {call})" if i in targets else f"  {call}")
        elif kind == "obox":
            o, ex, ey, ez, l, w, h = p; o = np.array(o, float); ex = np.array(ex, float); ey = np.array(ey, float); ez = np.array(ez, float)
            if np.cross(ex, ey) @ ez < 0: o = o + ex * l; ex = -ex      # UCS 3 is right-handed: span a left-handed frame from its far x corner
            call = f"(UB \"{lay}\" {pt(o)} {pt(o + ex)} {pt(o + ey)} {f(l)} {f(w)} {f(h)})"; L.append(f"  (setq e{i} {call})" if i in targets else f"  {call}")
        elif kind == "mesh": L.append(f"  ;; {lay}: swept mesh, {len(p[0])} triangles: not built in AutoCAD (glTF only)")
        elif kind == "hole":   # (p1, p2, r, target index): a cylinder subtracted from the primitive it is listed against
            p1, p2, r, t = p; L.append(f"  (setq hole (CY \"{lay}\" {pt(p1)} {pt(p2)} {f(r)})) (command \"_.SUBTRACT\" e{t} \"\" hole \"\")")
        elif kind == "cut":    # (o, ex, ey, ez, l, w, h, target): a box subtracted from the primitive it is listed against
            o, ex, ey, ez, l, w, h, t = p; o = np.array(o, float); ex = np.array(ex, float); ey = np.array(ey, float); ez = np.array(ez, float)
            if np.cross(ex, ey) @ ez < 0: o = o + ex * l; ex = -ex
            L.append(f"  (setq hole (UB \"{lay}\" {pt(o)} {pt(o + ex)} {pt(o + ey)} {f(l)} {f(w)} {f(h)})) (command \"_.SUBTRACT\" e{t} \"\" hole \"\")")
    L += ["  (command \"_.-LAYER\" \"_S\" \"0\" \"\") (setvar \"OSMODE\" os) (command \"_.ZOOM\" \"_E\") (princ \"\\nBuilt.\") (princ))", f"(princ \"\\nType {cmd}.\") (princ)"]
    outfile.write(path, "\n".join(L) + "\n")


# ------------------------------------------------------------------ glTF 2.0 (.glb) straight from the primitives
# One node per named part (layer prefix "node:<name>|"), everything else under "body". One mesh primitive per material layer.
# Our frame is mm, Z up; glTF is metres, Y up: (x, y, z) mm -> (x, z, -y) / 1000. Vertices are shared (indexed) and normals omitted.
import json, struct, math
import numpy as np
MATERIALS = {   # base colour, metallic, roughness per material layer (Blender refines these; the names are what matter)
    "M-STEEL-7035": ((0.85, 0.85, 0.83, 1), 0.0, 0.45), "M-GALV": ((0.72, 0.74, 0.76, 1), 1.0, 0.5), "M-GASKET": ((0.08, 0.08, 0.08, 1), 0.0, 0.9),
    "M-ZINC": ((0.66, 0.68, 0.70, 1), 1.0, 0.4), "M-BLACK-PA": ((0.08, 0.09, 0.1, 1), 0.0, 0.6), "M-BRASS": ((0.72, 0.6, 0.29, 1), 1.0, 0.35), "M-CU": ((0.72, 0.45, 0.2, 1), 1.0, 0.4),
    "M-ALU-7035": ((0.83, 0.83, 0.81, 1), 0.0, 0.5), "M-GREEN": ((0.07, 0.5, 0.2, 1), 0.0, 0.45), "M-RED": ((0.7, 0.05, 0.05, 1), 0.0, 0.45), "M-BLUE": ((0.05, 0.25, 0.75, 1), 0.0, 0.45),
    "M-YELLOW": ((0.95, 0.75, 0.0, 1), 0.0, 0.55), "M-LENS-GREEN": ((0.25, 0.85, 0.4, 1), 0.0, 0.2), "M-LENS-RED": ((0.95, 0.3, 0.25, 1), 0.0, 0.2), "M-LENS-WHITE": ((0.95, 0.95, 0.92, 1), 0.0, 0.2),
    "M-LENS-DARK": ((0.08, 0.09, 0.11, 0.6), 0.0, 0.08), "M-TITANIUM": ((0.6, 0.62, 0.65, 1), 1.0, 0.35),
    "M-WHITE-PA": ((0.92, 0.92, 0.9, 1), 0.0, 0.5), "M-GREY-PA": ((0.55, 0.57, 0.6, 1), 0.0, 0.55), "M-WHITE-PVC": ((0.92, 0.92, 0.9, 1), 0.0, 0.5), "M-GREY-PVC": ((0.55, 0.57, 0.6, 1), 0.0, 0.55), "M-GREEN-YELLOW": ((0.15, 0.6, 0.2, 1), 0.0, 0.5), "M-YELLOW-PA": ((0.95, 0.8, 0.05, 1), 0.0, 0.5),
    "M-ALU-ANOD": ((0.78, 0.79, 0.8, 1), 1.0, 0.4), "M-ZINC-CAST": ((0.62, 0.63, 0.65, 1), 1.0, 0.45), "M-LENS-YELLOW": ((0.95, 0.85, 0.3, 1), 0.0, 0.2), "M-RED-PA": ((0.75, 0.08, 0.06, 1), 0.0, 0.5),
    "M-BLACK-PC": ((0.05, 0.05, 0.06, 1), 0.0, 0.3), "M-CABLE-PUR": ((0.1, 0.1, 0.12, 1), 0.0, 0.7), "M-CABLE-GREY": ((0.5, 0.52, 0.54, 1), 0.0, 0.7), "M-COLLIDER": ((0.2, 0.8, 0.9, 0.3), 0.0, 1.0), "M-CAST-BLUE": ((0.17, 0.29, 0.54, 1), 0.3, 0.5),
    "M-CONCRETE": ((0.74, 0.73, 0.70, 1), 0.0, 0.9), "M-WALL": ((0.85, 0.80, 0.72, 1), 0.0, 0.85),   # lab rooms (toolkit/rooms.py)
    "M-SILVER": ((0.86, 0.86, 0.88, 1), 1.0, 0.25), "M-GOLD": ((0.83, 0.69, 0.22, 1), 1.0, 0.25), "M-BROWN": ((0.4, 0.24, 0.12, 1), 0.0, 0.6), "M-CU-CORRODED": ((0.36, 0.55, 0.45, 1), 0.3, 0.8), "M-ORANGE-PA": ((0.95, 0.45, 0.08, 1), 0.0, 0.5), "M-CASE-CLEAR": ((0.85, 0.9, 0.95, 0.25), 0.0, 0.05),
    # gl-xr-1 2.0 (EM 2026-11-20): three finishes that read apart, a clear lens and the display window inside it
    "M-BLACK-MATTE": ((0.03, 0.032, 0.036, 1), 0.0, 0.85), "M-TI-BRUSHED": ((0.62, 0.62, 0.64, 1), 1.0, 0.3),
    "M-LENS-CLEAR": ((0.97, 0.98, 0.99, 1), 0.0, 0.0), "M-WAVEGUIDE": ((0.8, 0.8, 0.8, 0.02), 0.0, 0.1)}
EXTENSIONS = {   # glTF material extensions per material layer; written only for a material that has a row here
    "M-LENS-CLEAR": {"KHR_materials_transmission": {"transmissionFactor": 0.95}, "KHR_materials_ior": {"ior": 1.5}}}
EMISSIVE = {"M-LENS-GREEN": (0.25, 0.85, 0.4), "M-LENS-RED": (0.95, 0.3, 0.25), "M-LENS-WHITE": (0.95, 0.95, 0.92), "M-LENS-YELLOW": (0.95, 0.85, 0.3)}   # emissiveFactor; Godot's twin scales it with the output bit
def _tris(prims, report=None):
    """triangulate: {(node, material): [(oid, p0, p1, p2), ...]}, mm, outward. Holes and cuts are cut (toolkit/csg.py, as AutoCAD's
    SUBTRACT); report gets {object id: (primitive index, method)}. Colliders become <name>-colonly nodes.
    The object id travels with each triangle so vertices are shared within one solid only (abutting solids stay separate shells)."""
    from . import preview
    cols = [(q[0].replace("collider:", "node:") + "-colonly|M-COLLIDER", q[1], q[2]) for q in prims if q[0].startswith("collider:")]
    out = {}
    for base, group, rep in ((0, prims, report), (10 ** 6, cols, None)):
        for L, oid, ps in preview.mesh(group, report=rep):
            node, mat = ("body", L)
            if L.startswith("node:"): node, mat = L[5:].split("|", 1)
            P = [np.array(p, float) for p in ps]
            for i in range(1, len(P) - 1): out.setdefault((node, mat), []).append((base + oid, P[0], P[i], P[i + 1]))
    return {k: unneedle(v) for k, v in out.items()}


NEEDLE_MM = 1e-3    # a triangle thinner than this (twice its area over its longest edge) collapses in float32 metres a machine away from
                    # the origin: 1 m's float32 step is 1.2e-4 mm, 8 m's 9.5e-4 mm (request panel-9 1, an escape: port-m12-a's D and L
                    # keys gated clean at the element's origin and failed Blender's degenerate count placed at 1.5 m in a panel)
SHORT_MM = 0.1      # a needle whose shortest edge is under this has its edge merged (the glb only: STEP and AutoCAD keep every vertex)


def _height(a, b, c):
    e = max(np.linalg.norm(b - a), np.linalg.norm(c - b), np.linalg.norm(a - c))
    return 0.0 if e <= 0 else float(np.linalg.norm(np.cross(b - a, c - a))) / e


def unneedle(tris, hmin=NEEDLE_MM, passes=200):
    """flip the long edge of every needle (a CSG triangle whose third vertex lies all but on its longest edge) with the triangle across
    it, when that keeps both new triangles facing the neighbour's way and thicker than the needle. Within one solid (vertices are shared
    by their glb key, 0.1 µm), so the shell stays closed: no vertex moves, no triangle is added or dropped, the surface moves by less
    than the needle's height. A needle that no flip thickens and whose shortest edge is under SHORT_MM has that edge merged, when the
    two ends share no neighbour but the two triangles' far corners and no triangle turns over: two triangles fewer, the shell still
    closed, a vertex moved by under 0.1 mm. A needle neither helps stays (request panel-9 1)."""
    if all(_height(*t[1:]) >= hmin for t in tris): return tris                    # nothing thin: the list as it came, byte for byte
    by = {}
    for t in tris: by.setdefault(t[0], []).append(t)
    out = []
    for oid, ts in by.items():
        key = lambda p: tuple(np.round(p, 4)); V = {}; idx = []
        for t in ts:
            row = []
            for p in t[1:]:
                k = key(p)
                if k not in V: V[k] = (len(V), p)
                row.append(V[k][0])
            idx.append(row)
        pts = [None] * len(V)
        for k, (i, p) in V.items(): pts[i] = np.array(p, float)
        H = lambda r: _height(pts[r[0]], pts[r[1]], pts[r[2]])
        N = lambda r: np.cross(pts[r[1]] - pts[r[0]], pts[r[2]] - pts[r[0]])
        if min(H(r) for r in idx) < hmin:
            for _ in range(passes):
                edges = {}
                for n, r in enumerate(idx):
                    for j in range(3): edges.setdefault((r[j], r[(j + 1) % 3]), n)
                flipped = 0
                for n, r in enumerate(idx):
                    h = H(r)
                    if h >= hmin: continue
                    j = max(range(3), key=lambda j: np.linalg.norm(pts[r[(j + 1) % 3]] - pts[r[j]]))
                    u, v, b = r[j], r[(j + 1) % 3], r[(j + 2) % 3]
                    m = edges.get((v, u))
                    if m is None or m == n: continue
                    s = idx[m]; d = next((x for x in s if x not in (u, v)), None)
                    if d is None or d == b: continue
                    n2 = N(s); t1, t2 = [u, d, b], [d, v, b]
                    if min(H(t1), H(t2)) <= h or N(t1) @ n2 <= 0 or N(t2) @ n2 <= 0: continue
                    if any(e in edges and edges[e] not in (n, m) for e in ((b, d), (d, b))): continue     # the diagonal exists already
                    idx[n], idx[m] = t1, t2; flipped += 1
                    for e in ((u, v), (v, u)): edges.pop(e, None)
                    for k_, rr in ((n, t1), (m, t2)):
                        for jj in range(3): edges[(rr[jj], rr[(jj + 1) % 3])] = k_
                collapsed = 0                                                     # a needle with a short edge (no flip makes it thicker):
                for n, r in enumerate(idx):                                        # merge that edge's ends, when the shell stays closed
                    if r is None or H(r) >= hmin: continue
                    j = min(range(3), key=lambda j: np.linalg.norm(pts[r[(j + 1) % 3]] - pts[r[j]]))
                    b, c = r[j], r[(j + 1) % 3]
                    if np.linalg.norm(pts[c] - pts[b]) >= SHORT_MM: continue
                    m = edges.get((c, b)); live = [q for q in idx if q is not None]
                    if m is None or idx[m] is None: continue
                    nb = lambda v: {x for q in live if v in q for x in q} - {v}
                    opp = {x for x in r + idx[m] if x not in (b, c)}
                    if nb(b) & nb(c) != opp: continue                              # the link condition: no fold, no pinched edge
                    moved = [(k_, [b if x == c else x for x in q]) for k_, q in enumerate(idx) if q is not None and c in q and k_ not in (n, m)]
                    if any(N(q2) @ N(idx[k_]) <= 0 for k_, q2 in moved): continue  # no triangle turns over
                    for k_, q2 in moved: idx[k_] = q2
                    idx[n] = idx[m] = None; collapsed += 1; break                  # the edge map is stale: rebuild it on the next pass
                idx = [q for q in idx if q is not None]
                if not flipped and not collapsed: break
        out += [(oid, pts[r[0]], pts[r[1]], pts[r[2]]) for r in idx]
    return out


def write_glb(path, prims, name):
    rep = {}; groups = _tris(prims, rep); pivots = getattr(prims, "pivots", {})
    def g(v): return [v[0] / 1000.0, v[2] / 1000.0, -v[1] / 1000.0]          # mm Z-up -> glTF metres Y-up
    mats = sorted({m for _, m in groups}); mat_index = {m: i for i, m in enumerate(mats)}
    nodes = sorted({n for n, _ in groups}, key=lambda n: (n != "body", n))
    bufs = []; views = []; accessors = []; meshes = []; gnodes = []; offset = 0
    def add_view(data, target):
        nonlocal offset
        b = data.tobytes(); pad = (-len(b)) % 4; views.append(dict(buffer=0, byteOffset=offset, byteLength=len(b), target=target)); bufs.append(b + b"\0" * pad); offset += len(b) + pad; return len(views) - 1
    for n in nodes:
        prims_json = []
        for m in mats:
            tris = groups.get((n, m))
            if not tris: continue
            o = np.array(pivots[n]["origin"], float) if n in pivots else np.zeros(3)     # mesh relative to its pivot
            raw = [(t[0],) + tuple(np.round([p[0] - o[0], p[2] - o[2], -(p[1] - o[1])], 4)) for t in tris for p in t[1:]]      # (solid id, mm glTF axes)
            uniq = {}; idx = []                                                                        # shared within a solid, never across touching solids
            for v in raw:
                if v not in uniq: uniq[v] = len(uniq)
                idx.append(uniq[v])
            pos = np.array([k[1:] for k in uniq.keys()], dtype=np.float32) / 1000.0; idx = np.array(idx, dtype=np.uint32)
            vp = add_view(pos, 34962); vi = add_view(idx, 34963)
            accessors.append(dict(bufferView=vp, componentType=5126, count=len(pos), type="VEC3", min=pos.min(axis=0).tolist(), max=pos.max(axis=0).tolist())); ap = len(accessors) - 1
            accessors.append(dict(bufferView=vi, componentType=5125, count=len(idx), type="SCALAR")); ai = len(accessors) - 1
            prims_json.append(dict(attributes=dict(POSITION=ap), indices=ai, material=mat_index[m]))   # no normals on purpose: flat normals are computed by the client, and the mesh stays connected for Blender's bevel
        meshes.append(dict(name=n, primitives=prims_json)); node = dict(name=n, mesh=len(meshes) - 1)
        if n in pivots:
            pv = pivots[n]; node["translation"] = g(pv["origin"])
            node["extras"] = dict(motion=dict(kind=pv["kind"], axis=g(np.array(pv["axis"]) * 1000.0), range=list(pv["range"]), unit=pv["unit"]))
            more = {k: v for k, v in pv.items() if k not in ("kind", "origin", "axis", "range", "unit")}
            if "keyref" in more: more["keyref"] = g(np.array(more["keyref"], float) * 1000.0)      # a direction: glTF axes like `axis`
            if more: node["extras"][pv["kind"] if pv["kind"] in ("contact", "port") else "data"] = more
        gnodes.append(node)
    # the hierarchy (EM 2026-11-08, the twin: the disconnect handle, the e-stop and the nameplate stayed in the air when the door
    # opened): a node whose tag declares a parent (prims.parents: a BOM row's `parent`, an element's own door-mounted parts) is
    # a child of that parent's node, its translation relative to the parent's origin, so it moves with the door. A parent that
    # is a tag with no node of its own (the enclosure itself) is climbed through to the next one up. An element declares a part
    # of its own that must NOT follow its BOM parent with P.parents["<part>"] = "fixed" (a disconnect's body on the back panel
    # while its handle and door unit ride the door).
    parents = getattr(prims, "parents", {}) or {}; index = {n["name"]: i for i, n in enumerate(gnodes)}
    def parent_of(n):
        tag = n; seen = set()
        while tag and tag not in seen:
            seen.add(tag); hop = None
            for c in [tag] + [tag.rsplit(".", k)[0] for k in range(1, tag.count(".") + 1)]:    # the node, then its tag prefixes
                if parents.get(c): hop = parents[c]; break
            if not hop or hop == "fixed": return None            # "fixed": the element says this part stays on its mounting plane
            if hop in index and hop != n: return hop
            tag = hop
        return None
    roots = []
    for i, node in enumerate(gnodes):
        pa = parent_of(node["name"])
        if pa is None: roots.append(i); continue
        node["extras"] = dict(node.get("extras", {}), parent=pa)
        po = np.array(gnodes[index[pa]].get("translation", [0, 0, 0]), float); co = np.array(node.get("translation", [0, 0, 0]), float)
        node["translation"] = (co - po).tolist()
        gnodes[index[pa]].setdefault("children", []).append(i)
    gltf = dict(asset=dict(version="2.0", generator="complexes component library"), scene=0, scenes=[dict(name=name, nodes=roots)], nodes=gnodes, meshes=meshes,
                materials=[dict(name=m, pbrMetallicRoughness=dict(baseColorFactor=list(MATERIALS.get(m, ((0.6, 0.6, 0.6, 1), 0, 0.5))[0]), metallicFactor=MATERIALS.get(m, (0, 0, 0.5))[1], roughnessFactor=MATERIALS.get(m, (0, 0, 0.5))[2]), **({"emissiveFactor": list(EMISSIVE[m])} if m in EMISSIVE else {}), **({"alphaMode": "BLEND"} if MATERIALS.get(m, ((0, 0, 0, 1),))[0][3] < 1 else {}), **({"extensions": EXTENSIONS[m]} if m in EXTENSIONS else {})) for m in mats],
                **({"extensionsUsed": sorted({e for m in mats for e in EXTENSIONS.get(m, {})})} if any(m in EXTENSIONS for m in mats) else {}),
                bufferViews=views, accessors=accessors, buffers=[dict(byteLength=offset)])
    js = json.dumps(gltf, separators=(",", ":")).encode(); js += b" " * ((-len(js)) % 4); bin_ = b"".join(bufs)
    outfile.write(path, struct.pack("<III", 0x46546C67, 2, 12 + 8 + len(js) + 8 + len(bin_)) + struct.pack("<II", len(js), 0x4E4F534A) + js + struct.pack("<II", len(bin_), 0x004E4942) + bin_)
    how = [m for _, m in rep.values()]
    return dict(nodes=[n["name"] for n in gnodes], materials=mats, triangles=sum(len(v) for k, v in groups.items() if not k[0].endswith('-colonly')),
                openings=dict(extrude=how.count("extrude"), bsp=how.count("bsp"), plain=how.count("plain"), uncut=[prims[i][0] for i, m in rep.values() if m is None]))


def glb_extents(js):
    """a glb's extents in mm, the library's axes (x, y, z up): (min, max). Every node of the scene with its parents' transforms
    applied (translation, rotation, scale, matrix), from each mesh accessor's bounds; collider nodes (-colonly) left out. A nested
    node (P.parents: a roll on its arm, rollers on a turning deck) counts like a top-level one (request mech-12: the AutoCAD gate's
    reader took each node's own translation alone and read turntable 1.0's rollers 10 mm low)."""
    def mat(nd):
        if "matrix" in nd: return np.array(nd["matrix"], float).reshape(4, 4).T
        x, y, z, w = nd.get("rotation", [0, 0, 0, 1]); sx, sy, sz = nd.get("scale", [1, 1, 1])
        R = np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)], [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                      [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]]) @ np.diag([sx, sy, sz])
        M = np.eye(4); M[:3, :3] = R; M[:3, 3] = nd.get("translation", [0, 0, 0]); return M
    nodes = js.get("nodes", []); lo = np.full(3, np.inf); hi = np.full(3, -np.inf)
    sc = js.get("scenes", [{}])[js.get("scene", 0)] if js.get("scenes") else {}
    kids = {c for nd in nodes for c in nd.get("children", [])}
    roots = sc.get("nodes", [i for i in range(len(nodes)) if i not in kids])
    stack = [(i, np.eye(4)) for i in roots]
    while stack:
        i, W = stack.pop(); nd = nodes[i]; M = W @ mat(nd)
        if "mesh" in nd and not nd.get("name", "").endswith("-colonly"):
            for pr in js["meshes"][nd["mesh"]]["primitives"]:
                a = js["accessors"][pr["attributes"]["POSITION"]]; b0, b1 = a["min"], a["max"]
                C = np.array([[x, y, z, 1.0] for x in (b0[0], b1[0]) for y in (b0[1], b1[1]) for z in (b0[2], b1[2])]) @ M.T
                lo = np.minimum(lo, C[:, :3].min(axis=0)); hi = np.maximum(hi, C[:, :3].max(axis=0))
        stack += [(c, M) for c in nd.get("children", [])]
    if not np.isfinite(lo).all(): return None
    return [lo[0] * 1000, -hi[2] * 1000, lo[1] * 1000], [hi[0] * 1000, -lo[2] * 1000, hi[1] * 1000]     # glTF metres Y-up -> mm Z-up
