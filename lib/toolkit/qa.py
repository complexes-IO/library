"""Mesh-level QA on an element's primitives, run by build.py after check.py. Catches what the glTF writer (with its cut openings) can get wrong
before Blender sees it: open or inside-out meshes, degenerate triangles, class triangle budgets, pivots that point at nothing,
colliders missing. Returns a list of problems (empty = pass)."""
import numpy as np
from . import preview
from .prims import nodes, solids

BUDGET = {"operator-22": 3000, "connector": 3000, "cable": 8000, "device": 12000, "rail": 3000, "station": 9000, "enclosure": 25000,
          "furniture": 15000, "prop": 20000, "machine": 100000, "plate": 600, "contact": 400, "connector-part": 1500, "wire": 2000,
          "tube": 8000, "actuator": 12000,
          "run": 12000}                                      # mech-1 (2026-11-06): a run (duct, tray) takes a device's budget, so a CLASS change alone moves no number                   # pneu-1: tube as cable, actuator (cylinders, rotary actuators, grippers) as device
# toolkit 1.3 cuts holes into the mesh: station 8000 -> 9000 and plate 500 -> 600 carry the openings (pbs-6h-22 8376, tag-plate 536);
# connector 2000 -> 3000 and cable 6000 -> 8000 carry the contacts as elements (a receptacle-m12 with five contacts is about 1500)
MATERIALS = {"device": 12, "actuator": 12, "station": 14, "enclosure": 10, "machine": 16}   # materials per element (draw calls); default 8.
# round 3 (2026-11-04): a mechanism-first device shows its interior (relay-ice-cube-2co 12) and a station carries its operators and ports
# (pbs-6h-22 13). One source for every budget: build.py writes them to catalogue.csv (budget_tris, budget_mats) for Godot QA.

def budgets(mod):
    """(triangles, materials) an element may use: its own TRIANGLES / MATERIALS_MAX, else its class's"""
    cls = getattr(mod, "CLASS", "device")
    return getattr(mod, "TRIANGLES", None) or BUDGET.get(cls, 12000), getattr(mod, "MATERIALS_MAX", None) or MATERIALS.get(cls, 8)

def _tris_by_node(prims):
    faces = preview.mesh(prims); out = {}
    for L, oid, ps in faces:
        node = L[5:].split("|", 1)[0] if L.startswith("node:") else "body"
        P = [np.array(p, float) for p in ps]
        for i in range(1, len(P) - 1): out.setdefault(node, []).append((P[0], P[i], P[i + 1]))
    return out

def _per_object_faces(prims):
    """faces grouped per primitive (object id) so closedness is checked per solid, not per node"""
    faces = preview.mesh(prims); out = {}
    for L, oid, ps in faces: out.setdefault(oid, []).append([np.array(p, float) for p in ps])
    return out

def run(mod, P):
    problems = []
    cls = getattr(mod, "CLASS", "device"); budget, mat_budget = budgets(mod)              # an element may state its own, with its reason
    by_node = _tris_by_node(P); total = sum(len(t) for t in by_node.values())
    if total > budget: problems.append(f"triangle budget: {total} > {budget} for {'this element (TRIANGLES)' if getattr(mod, 'TRIANGLES', None) else 'class ' + cls}")
    mats = {L.split("|")[-1] for L, k, q in P if k not in ("hole", "cut") and not L.startswith("collider:")}
    if len(mats) > mat_budget: problems.append(f"materials: {len(mats)} > {mat_budget} for class {cls} ({', '.join(sorted(mats))})")
    # per solid: closed (each edge used twice, opposite directions), outward (signed volume > 0), no degenerate triangles
    sol = P
    for oid, faces in _per_object_faces(P).items():
        edges = {}; vol = 0.0; degenerate = 0
        for ps in faces:
            for i in range(1, len(ps) - 1):
                a, b, c = ps[0], ps[i], ps[i + 1]
                area2 = np.linalg.norm(np.cross(b - a, c - a))
                if area2 < 1e-6: degenerate += 1
                vol += np.dot(a, np.cross(b, c)) / 6.0
            n = len(ps)
            for i in range(n):
                k = (tuple(np.round(ps[i], 4)), tuple(np.round(ps[(i + 1) % n], 4))); edges[k] = edges.get(k, 0) + 1
        open_edges = sum(1 for (a, b), c in edges.items() if edges.get((b, a), 0) != c)
        if open_edges: problems.append(f"solid {oid} ({sol[oid - 1][0]}): {open_edges} unmatched edges (not closed / inconsistent winding)")
        if vol <= 0: problems.append(f"solid {oid} ({sol[oid - 1][0]}): signed volume {vol:.1f} <= 0 (inside out)")
        if degenerate: problems.append(f"solid {oid} ({sol[oid - 1][0]}): {degenerate} degenerate triangles")
    # pivots name real nodes; moving nodes have a pivot; every element has at least one collider
    nd = set(nodes(P))
    for n, pv in P.pivots.items():
        if n not in nd: problems.append(f"pivot {n} names no node")
    for n in nd:
        if n not in P.pivots: problems.append(f"node {n} has no pivot (declare kind: rotate / translate / emissive / port / fixed)")
    if not any(L.startswith("collider:") for L, _, _ in P): problems.append("no collider box")
    return problems
