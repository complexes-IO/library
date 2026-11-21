"""Seeded-fault tests of the validation suite: every checker is shown a known fault and a known good case, and must call both right.
Run: python lib/build.py selftest  (exit 1 on any miss). A checker that cannot find a planted fault is not allowed to pass a real one."""
import json, math, re
import numpy as np
from .prims import Prims
from .solid import Scene, inside
from . import v_geometry as G, v_electrical as E, v_features as V

def _owned(P, s, e, tag): P.owners.append((s, e, tag, "test"))

def cases():
    out = []
    def t(name, ok, got=""): out.append((name, bool(ok), got))
    # geometry kernel: mesh parity agrees with the exact box test
    V8 = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
    F12 = [(0, 2, 1), (0, 3, 2), (4, 5, 6), (4, 6, 7), (0, 1, 5), (0, 5, 4), (1, 2, 6), (1, 6, 5), (2, 3, 7), (2, 7, 6), (3, 0, 4), (3, 4, 7)]
    q = ([tuple(tuple(c * 10.0 for c in V8[i]) for i in f) for f in F12],)
    X = np.random.default_rng(1).random((20000, 3)) * 14 - 2
    agree = (inside("mesh", q, X) == np.all((X >= 0) & (X <= 10), axis=1)).mean(); t("mesh inside test = box inside test", agree == 1.0, f"{agree:.4f}")
    # the institute's mark (toolkit/mark.py, EM 2026-11-20): one outline for every element; the triangles cover the regions, an inlay is a closed shell, a ring too small to carry the characters is refused
    from . import mark as MK
    R6 = MK.regions(6.0); tri_area = lambda r: sum(0.5 * ((r[0][b][0] - r[0][a][0]) * (r[0][c][1] - r[0][a][1]) - (r[0][b][1] - r[0][a][1]) * (r[0][c][0] - r[0][a][0])) for a, b, c in r[1])
    ring = 0.5 * 72 * math.sin(2 * math.pi / 72) * (3.0 ** 2 - 2.6 ** 2)
    t("mark: the ring is 6.0 outside with a 0.4 line, and 0{1} is five islands inside it", abs(tri_area(R6[0]) - ring) < 1e-6 and len(R6) == 6 and all(float(np.hypot(*q)) < 2.6 for r in R6[1:] for q in r[0]), f"ring {tri_area(R6[0]):.4f} of {ring:.4f}, {len(R6)} regions")
    t("mark: a ring twice the size has four times the area in every region", all(abs(tri_area(b) - 4 * tri_area(a)) < 1e-6 for a, b in zip(R6, MK.regions(12.0))), f"{sum(map(tri_area, MK.regions(12.0))):.4f} of {4 * sum(map(tri_area, R6)):.4f}")
    edges = {}
    for r in R6:
        for tri in MK.inlay(r, lambda u, v, top: (u, v, 0.03 if top else -0.3)):
            for a, b in zip(tri, tri[1:] + tri[:1]): edges[(a, b)] = edges.get((a, b), 0) + 1
    t("mark: every inlay is a closed shell (each edge once in each direction)", all(n == 1 and edges.get((b, a)) == 1 for (a, b), n in edges.items()), f"{len(edges)} directed edges")
    try: MK.regions(5.0); small = False
    except ValueError: small = True
    t("mark: a 5 mm ring is refused (the characters' strokes would go under 0.3 mm)", small)
    # an element's own facet count (Prims.facets, EM 2026-11-20: round holes): only its mesh changes, the library's count comes back, and the build counts what the Blender gate would
    from . import csg as _csg, preview as _pv, cadout as _co, qa as _qa
    P = Prims(); b_ = P.box("M-STEEL", 0, 0, 0, 40, 6, 30); P.hole("M-GASKET", (20, -1, 15), (20, 7, 15), 2.25, b_); n12 = len(_pv.mesh(P))
    P.facets = 32; n32 = len(_pv.mesh(P)); P.facets = None; again = len(_pv.mesh(P))
    t("facets: a 2.25 mm hole has 12 sides by default and 32 when its Prims says so; the default comes back after", n32 > n12 == again and _csg.FACETS is None, f"{n12}, {n32}, {again} faces; csg.FACETS {_csg.FACETS}")
    P.facets = 32; t("facets: a closed cut box has no non-manifold edge in the glb", _co.non_manifold(P) == {}, str(_co.non_manifold(P)))
    Q = Prims(); Q.mesh("M-STEEL", [((0, 0, 0), (10, 0, 0), (0, 10, 0)), ((0, 0, 0), (0, 0, 10), (10, 0, 0)), ((0, 0, 0), (0, 10, 0), (0, 0, 10))])
    t("facets: an open shell's edges are counted as the Blender gate counts them (3 of a tetrahedron less one face)", _co.non_manifold(Q) == {("body", "M-STEEL"): 3}, str(_co.non_manifold(Q)))
    class _M: CLASS = "device"; TRIANGLES = 100000
    P.facets = 64; r_ = _qa.run(_M, P); t("facets: a count outside 24 to 48 is refused at the build", any("outside 24 to 48" in x for x in r_), str(r_[:1]))
    # interference: overlapping instances FAIL, touching instances PASS, a hole clears its plug
    P = Prims(); P.box("M-STEEL", 0, 0, 0, 10, 10, 10); _owned(P, 0, 1, "a"); P.box("M-STEEL", 8, 0, 0, 10, 10, 10); _owned(P, 1, 2, "b")
    r = G.interference(P, "test-overlap"); t("GEO-020 finds a 2 mm overlap", any(s == "FAIL" and x == "GEO-020" for s, x, *_ in r), r[0][3])
    P = Prims(); P.box("M-STEEL", 0, 0, 0, 10, 10, 10); _owned(P, 0, 1, "a"); P.box("M-STEEL", 10, 0, 0, 10, 10, 10); _owned(P, 1, 2, "b")
    r = G.interference(P, "test-touch"); t("GEO-020 passes touching faces", not any(s == "FAIL" for s, *_ in r))
    P = Prims(); pl = P.box("M-STEEL", -20, 0, -20, 40, 2, 40); P.hole("M-GASKET", (0, -1, 0), (0, 3, 0), 5.0, pl); _owned(P, 0, 2, "a")
    P.cyl("M-ZINC", (0, -5, 0), (0, 8, 0), 4.9); _owned(P, 2, 3, "b")
    r = G.interference(P, "test-hole"); t("GEO-020 passes a plug through its clearance hole", not any(s == "FAIL" for s, *_ in r))
    P = Prims(); pl = P.box("M-STEEL", -20, 0, -20, 40, 2, 40); _owned(P, 0, 1, "a"); P.cyl("M-ZINC", (0, -5, 0), (0, 8, 0), 4.9); _owned(P, 1, 2, "b")
    r = G.interference(P, "test-nohole"); t("GEO-020 fails a plug with no hole", any(s == "FAIL" for s, *_ in r))
    # motion: a 100 mm leaf turning about z hits a post at 45 degrees
    P = Prims(); P.box("node:leaf|M-STEEL", 0, -1, 0, 100, 2, 20); P.pivot("leaf", "rotate", (0, 0, 0), axis=(0, 0, 1), range=(0, 90))
    c45 = (70 * math.cos(math.radians(45)), 70 * math.sin(math.radians(45))); P.cyl("M-STEEL", (c45[0], c45[1], -5), (c45[0], c45[1], 25), 3.0)
    r = G.motion(P, "test-leaf"); hit = [x for x in r if x[0] == "FAIL"]
    ang = float(hit[0][3].split("blocked at ")[1].split(" ")[0]) if hit else None
    t("MOT-010 stops the leaf at the post (≈ 40–45°)", ang is not None and 38 <= ang <= 46, f"{ang}")
    P = Prims(); P.box("node:leaf|M-STEEL", 0, -1, 0, 100, 2, 20); P.pivot("leaf", "rotate", (0, 0, 0), axis=(0, 0, 1), range=(0, 90)); P.cyl("M-STEEL", (-40, 40, -5), (-40, 40, 25), 3.0)
    r = G.motion(P, "test-leaf-clear"); t("MOT-010 passes a clear swing", not any(x[0] == "FAIL" for x in r))
    # a follower moves with its leader: the carried block must not be reported against the leaf
    P = Prims(); P.box("node:leaf|M-STEEL", 0, -1, 0, 100, 2, 20); P.pivot("leaf", "rotate", (0, 0, 0), axis=(0, 0, 1), range=(0, 90))
    s0 = len(P); P.box("M-BLACK-PA", 50, 1, 5, 10, 10, 10); _owned(P, s0, s0 + 1, "op"); P.parents["op"] = "leaf"
    r = G.motion(P, "test-carry"); t("MOT-010 carries a BOM child with its parent", not any(x[0] == "FAIL" for x in r), r[0][3])
    # request mech-6 (2026-11-09): an own part with its own pivot, declared on a moving part (tensioner-belt's roll on its arm,
    # P.parents["roll"] = "arm"), rides the arm's swing rigidly and still spins on its own; before, MOT-010 looked it up by owner
    # tag only, so the roll stayed behind and a post in its path at 45 degrees was never met
    def _arm(post):
        P = Prims(); P.box("node:arm|M-STEEL", 0, -2, 0, 60, 4, 6); P.pivot("arm", "rotate", (0, 0, 0), axis=(0, 0, 1), range=(0, 90))
        P.cyl("node:roll|M-BLACK-PA", (70, 0, 0), (70, 0, 6), 10.0); P.pivot("roll", "rotate", (70, 0, 0), axis=(0, 0, 1), range=(0, 360))
        P.parents["roll"] = "arm"
        if post: c = (70 * math.cos(math.radians(45)), 70 * math.sin(math.radians(45))); P.cyl("M-STEEL", (c[0], c[1], -5), (c[0], c[1], 25), 3.0)
        return G.motion(P, "test-roll")
    r = _arm(True); t("MOT-010 carries an own part declared on its moving part (tensioner-belt's roll, P.parents): the roll meets the post in the arm's swing",
                      any(x[0] == "FAIL" and x[2] == "arm" and "roll" in x[3] for x in r), r[0][3] if r else "")
    r = _arm(False); t("MOT-010 still sweeps the carried roll's own spin (2 nodes swept, clear)", r and not any(x[0] == "FAIL" for x in r) and "2 moving node" in r[-1][3], r[-1][3] if r else "")
    # rotated parts that only touch are not an overlap (SKIN), and a follower moving less than its leader is checked against it
    from .solid import rotation
    P = Prims(); P.box("M-STEEL", 0, -1, 0, 100, 2, 20); P.box("M-BLACK-PA", 50, 1, 5, 10, 10, 10); S = Scene(P); R = rotation((0, 0, 1), 45)
    S.move([0, 1], R, np.zeros(3)); t("touching faces stay apart after a rotation", S.overlap(0, 1) is None)
    P = Prims(); P.box("node:card|M-WHITE-PA", 0, 0, 0, 10, 2, 10); P.pivot("card", "translate", (0, 0, 0), axis=(0, 1, 0), range=(0, 3))
    P.box("node:finger|M-BRASS", 0, 2.5, 0, 10, 1, 10); P.pivot("finger", "translate", (0, 2.5, 0), axis=(0, 1, 0), range=(0, 1))
    import tempfile, os, csv as _csv
    from . import library as _lib
    mp = os.path.join(_lib.ROOT, "motion.csv"); orig = open(mp, "rb").read()          # bytes: the file's own line endings come back
    try:
        open(mp, "a", encoding="utf-8").write("selftest-card,card,finger,follow,,planted\n")
        r = G.motion(P, "selftest-card"); t("MOT-010 finds a leader overrunning a follower that stopped", any(x[0] == "FAIL" for x in r), r[0][3])
    finally: open(mp, "wb").write(orig)
    # ESCAPE clamp-angle-1.0 1 (review mech/r124): two independent slides, each clear alone, meet when both are out; MOT-010 swept each
    # with the other at rest and passed. Posed together at their ends they are a REVIEW; with shorter strokes they pass as a pair
    def _pads(stroke):
        P = Prims(); P.box("node:pad-a|M-STEEL", 32, 1, 0, 36, 10, 10); P.pivot("pad-a", "translate", (50, 1, 0), axis=(0, 1, 0), range=(0, stroke))
        P.box("node:pad-b|M-STEEL", 1, 32, 0, 10, 36, 10); P.pivot("pad-b", "translate", (1, 50, 0), axis=(1, 0, 0), range=(0, stroke))
        return G.motion(P, "test-pads")
    r = _pads(29); t("ESCAPE clamp-angle-1.0 1: MOT-010 poses two independent slides together at their ends; each clear alone, they meet (REVIEW, both named)",
                     not any(x[0] == "FAIL" for x in r) and any(x[0] == "REVIEW" and x[2] == "pad-a+pad-b" and "posed together" in x[3] for x in r),
                     "; ".join(x[3] for x in r))
    r = _pads(20); t("ESCAPE clamp-angle-1.0 1: two slides whose strokes keep apart pass, the pair counted", r and r[-1][0] == "PASS" and "1 pair(s)" in r[-1][3], r[-1][3] if r else "")
    # MOT-020 (escape overload-9a-1no1nc 1.1:1): a follow leader must reach its follower within its own travel; MOT-010 alone moved it anyway
    def _fc(gap, axis=(0, 1, 0), mode="follow", note=""):
        P = Prims(); P.box("node:card|M-WHITE-PA", 0, 0, 0, 10, 2, 10); P.pivot("card", "translate", (0, 0, 0), axis=axis, range=(0, 3))
        P.box("node:finger|M-BRASS", 0, 2 + gap, 0, 10, 1, 10); P.pivot("finger", "translate", (0, 2 + gap, 0), axis=(0, 1, 0), range=(0, 1))
        return G.follow_contact(P, "selftest-fc", [dict(scope="selftest-fc", leader="card", follower="finger", mode=mode, stop="", note=note)])
    r = _fc(0.5); t("MOT-020 passes a leader that meets its follower within its travel (gap 0.5, travel 3)", r and all(x[0] == "PASS" for x in r), r[0][3] if r else "")
    r = _fc(4.0); t("MOT-020 flags a leader whose travel ends short of its follower (gap 4, travel 3)", any(x[0] == "REVIEW" for x in r), r[0][3] if r else "")
    r = _fc(0.5, axis=(0, -1, 0)); t("MOT-020 flags a leader that moves away from its follower (overload-9a-1no1nc's bimetal)", any(x[0] == "REVIEW" for x in r), r[0][3] if r else "")
    r = _fc(4.0, mode="linked", note="a pin the model doesn't draw"); t("MOT-020 accepts a pair declared linked with its reason", not any(x[0] == "REVIEW" for x in r))
    r = _fc(4.0, mode="linked"); t("MOT-020 flags a pair declared linked with no reason", any(x[0] == "REVIEW" for x in r))
    P = Prims(); b = P.box("M-STEEL", 0, 0, 0, 10, 10, 10); P.hole("M-GASKET", (0, -1, 5), (0, 11, 5), 2, b)
    r = V.breakout("test", P); t("HOLE-020 fails a hole that breaks out of its part", r and r[0][0] == "FAIL", r[0][3] if r else "")
    P = Prims(); P.box("M-GREY-PA", 0, 0, 0, 20, 10, 20); P.cyl("node:cap|M-RED-PA", (10, 2, 10), (10, 0, 10), 3.0); P.pivot("cap", "fixed", (10, 0, 10))
    r = G.zfight(P, "test"); t("GEO-050 flags a cap flush with its face", any(x[0] == "REVIEW" for x in r), r[0][3])
    P = Prims(); P.box("M-GREY-PA", 0, 0, 0, 20, 10, 20); P.cyl("node:cap|M-RED-PA", (10, 2, 10), (10, -0.5, 10), 3.0); P.pivot("cap", "fixed", (10, 0, 10))
    r = G.zfight(P, "test"); t("GEO-050 passes a cap 0.5 proud", all(x[0] == "PASS" for x in r))
    # the mesh writer cuts what AutoCAD subtracts: exact volumes, closed shells
    from . import csg
    def _open_edges(Fc):
        Ed = {}
        for ps in Fc:
            for i in range(len(ps)):
                k = (tuple(np.round(ps[i], 4)), tuple(np.round(ps[(i + 1) % len(ps)], 4))); Ed[k] = Ed.get(k, 0) + 1
        return sum(1 for (a, b), c in Ed.items() if Ed.get((b, a), 0) != c)
    def _ngon(r): n = csg.segments(r); return 0.5 * n * r * r * math.sin(2 * math.pi / n)
    Fc, how = csg.cut_solid("box", (0, 0, 0, 40, 6, 30), [("hole", ((20, -1, 15), (20, 7, 15), 2.25, 0)), ("hole", ((20, -1, 15), (20, 2, 15), 4.0, 0)),
                                                          ("cut", ((4, -1, 4), (1, 0, 0), (0, 1, 0), (0, 0, 1), 8, 8, 20, 0))])
    want = 40 * 6 * 30 - _ngon(2.25) * 4 - _ngon(4.0) * 2 - 8 * 6 * 20
    t("glTF cuts a counterbore and a rectangular cut-out: closed, exact volume", how == "extrude" and _open_edges(Fc) == 0 and abs(csg.volume(Fc) - want) < 1e-6 * want,
      f"{how}, open {_open_edges(Fc) if Fc else '-'}, {csg.volume(Fc) if Fc else 0:.2f} vs {want:.2f}")
    Fc, how = csg.cut_solid("box", (0, 0, 0, 40, 8, 30), [("hole", ((10, -1, 15), (10, 9, 15), 2.0, 0)), ("hole", ((30, 4, -1), (30, 4, 31), 2.0, 0))])
    want = 40 * 8 * 30 - _ngon(2.0) * 8 - _ngon(2.0) * 30
    t("glTF cuts holes on two axes by boolean: watertight, exact volume", how == "bsp" and _open_edges(Fc) == 0 and abs(csg.volume(Fc) - want) < 1e-4 * want,
      f"{how}, open {_open_edges(Fc) if Fc else '-'}, {csg.volume(Fc) if Fc else 0:.2f} vs {want:.2f}")
    Fc, how = csg.cut_solid("box", (0, 0, 0, 20, 10, 20), [("cut", ((5, 3, 10), (1, 0, 0), (0, 1, 0), (0, 0, 1), 10, 4, 11, 0))])
    t("glTF cuts a channel that opens through a side only (no end face of the first axis)", how in ("extrude", "bsp") and _open_edges(Fc) == 0 and abs(csg.volume(Fc) - 3600) < 1e-3,
      f"{how}, {csg.volume(Fc) if Fc else 0:.2f} vs 3600")
    P = Prims(); pl = P.box("M-STEEL", -20, 0, -20, 40, 2, 40); P.hole("M-GASKET", (0, -1, 0), (0, 3, 0), 2.25, pl); P.cyl("node:pin|M-BRASS", (0, 0, 0), (0, 6, 0), 2.0); P.pivot("pin", "fixed", (0, 0, 0))
    r = G.zfight(P, "test"); t("GEO-050 passes a pin flush in its cut bore", all(x[0] == "PASS" for x in r), r[0][3])
    # request elec-2: din.terminal_row's wire entries stood 0.5 proud of the end face (thermostat-enc 1.0: 60.5 for a 60 housing)
    from . import din as DIN
    from .prims import extents as _ext
    def _rail(up):
        P = Prims(); hb = P.box("M-GREY-PA", 0.0, -40.0, -30.0, 35.0, 40.0, 60.0)
        try: DIN.terminal_row(P, 5.5, -40.0, 30.0 if up else -30.0, 2, 12.0, up=up, target=hb)
        except TypeError as e: return P, hb, str(e)
        return P, hb, ""
    for up in (False, True):
        P, hb, err = _rail(up); lo, hi = _ext(P) if not err else ((0, 0, 0), (0, 0, 0))
        cuts = [q for L, k, q in P if k == "cut" and q[-1] == hb]; zf = G.zfight(P, "test") if not err else [("ERR",)]
        t(f"din.terminal_row with its housing ({'top' if up else 'bottom'} row): the wire entries are cut into the end face, the envelope is the housing's 60 and nothing flickers",
          not err and abs(lo[2] + 30.0) < 1e-9 and abs(hi[2] - 30.0) < 1e-9 and len(cuts) == 2 and all(x[0] == "PASS" for x in zf), err or f"z {lo[2]}…{hi[2]}, cuts {len(cuts)}, {zf[0]}")
    P = Prims(); m_ = P.mesh("M-STEEL", [((0, 0, 0), (10, 0, 0), (0, 10, 0)), ((0, 0, 0), (0, 0, 10), (10, 0, 0)), ((0, 0, 0), (0, 10, 0), (0, 0, 10)), ((10, 0, 0), (0, 0, 10), (0, 10, 0))])
    P.hole("M-GASKET", (2, 2, -1), (2, 2, 11), 0.5, m_)
    r = G.openings(P, "test"); t("GEO-060 flags a hole the glTF cannot show (swept mesh)", any(x[0] == "REVIEW" for x in r), r[0][3])
    P = Prims(); pl = P.box("M-STEEL", 0, 0, 0, 40, 2, 40); P.cutbox("M-GASKET", 10, -1, 10, 20, 4, 20, pl); _owned(P, 0, 2, "a")
    P.box("M-BLACK-PA", 12, -5, 12, 16, 12, 16); _owned(P, 2, 3, "b")
    r = G.interference(P, "test-window"); t("GEO-020 passes a part through a rectangular cut-out", not any(s == "FAIL" for s, *_ in r), r[0][3])
    # the gate's fillet pre-flight: a wall a bore leaves behind an edge is thin; a contact keeps its own radius inside a host
    from . import fillet as FI
    P = Prims(); sl = P.cyl("M-ZINC", (0, 0, 0), (0, 8, 0), 6.0); P.hole("M-GASKET", (0, -1, 0), (0, 9, 0), 5.46, sl)
    st = [e["status"] for rec in FI.outer_edges(P, 0.5) for e in rec["edges"]]; t("FIL-010 skips the rim of a 0.54 wall left by a bore (thin)", st and all(x == "thin" for x in st), str(st))
    from . import library as LB
    P = Prims(); LB.place(P, dict(element="contact-m12-pin", version="1.2", tag="c1", parent="", x=0, y=0, z=0, yaw=0.0, params={}))
    rr = {rec["r"] for rec in FI.outer_edges(P, None, cls="device")}; t("FIL-010 gives a placed contact its own radius (0.1), not its host's", rr == {0.1}, str(rr))
    st = {e["status"] for rec in FI.outer_edges(P, None, cls="device") for e in rec["edges"]}
    t("FIL-010 leaves a placed element's edges to that element's own gate (child)", st == {"child"}, str(st))
    # the element line (OPERATING.md 13): a station holds on its own findings; the stations after it wait
    from . import line as LN
    cat_ = {"gl-xr-1": {"version": "1.2"}}
    rows = LN.element("gl-xr-1", findings=[dict(status="REVIEW", rule="DOC-004", scope="gl-xr-1", elements=[], message="no brief")], cat=cat_, tags=set(), reviews="")
    t("LINE holds an element at station 1 on a missing brief, and every station after it", LN.reached(rows) == 0 and not rows[1][3], str([(n, ok) for n, _, _, ok, _ in rows]))
    rows = LN.element("gl-xr-1", findings=[], cat=cat_, tags={"gl-xr-1/1.2"}, reviews="gl-xr-1 1.2: PASS")
    t("LINE passes an element to station 8 only with its gates, the reviewer's PASS and its tag", LN.reached(rows) in (5, 8) and (LN.reached(rows) == 8) == (not LN.tools_check("gl-xr-1", "1.2")), str(LN.reached(rows)))
    vp = os.path.join(_lib.ELEMENTS, "gl-xr-1", "gate", "gl-xr-1-planted-acad.json")
    try:
        open(vp, "w", encoding="utf-8").write('{"pass": false, "date": "planted"}')
        why = LN.tools_check("gl-xr-1", "1.2")
        t("LINE holds an element at station 6 when one of its variants failed its AutoCAD gate", any(w.startswith("variant planted") for w in why), str(why))
    finally:
        if os.path.exists(vp): os.remove(vp)
    # ESCAPE mech/r140 1 (core watch 2026-11-13): lib/godot-qa.py fell back to the writer's out/ glb before the Blender gate's export
    # existed, and station 6 read only the QA's "pass": profile-t-alu-30x30x3's first QA passed on 28 triangles, the export's body has 220
    _bl = {"pass": True, "export": {"triangles_per_node": {"base-colonly": 12, "body": 220, "post-colonly": 12}, "triangles": 244}}
    _m = LN.qa_source_miss({"pass": True, "triangles": 28, "triangles_generator": 28}, _bl, "qa/x.json")
    t("ESCAPE mech/r140 1: LINE holds a Godot QA that rendered 28 triangles (the writer's glb) where the Blender export's visible nodes have 220; 220 passes, and a Blender result with no per-node count holds nothing",
      len(_m) == 1 and _m[0].startswith(LN.QA_SOURCE) and "28" in _m[0] and "220" in _m[0] and "writer's" in _m[0]
      and LN.qa_source_miss({"pass": True, "triangles": 220, "triangles_generator": 28}, _bl, "qa/x.json") == []
      and LN.qa_source_miss({"pass": True, "triangles": 28}, {"pass": True}, "qa/x.json") == [], str(_m))
    # core round 37 (the core's half of round 36 A1): qa/<id>.json names the file Godot QA read; station 6 reads it
    _r = LN.qa_read_miss({"pass": True, "source": "elements/x/out/x.glb"}, "x", "x", "qa/x.json")
    t("round 37: LINE holds an element whose Godot QA read elements/x/out/x.glb, not its Blender export; gltf/x.glb, a variant's gate/<variant>.glb and a QA with no source hold nothing",
      len(_r) == 1 and _r[0].startswith(LN.QA_READ) and "out/x.glb" in _r[0]
      and LN.qa_read_miss({"pass": True, "source": "elements/x/gltf/x.glb"}, "x", "x", "qa/x.json") == []
      and LN.qa_read_miss({"pass": True, "source": "elements/x/gate/x-D.glb"}, "x", "x-D", "qa/x-D.json") == []
      and LN.qa_read_miss({"pass": True, "source": "elements/x/gate/x.glb"}, "x", "x", "qa/x.json") != []
      and LN.qa_read_miss({"pass": True, "triangles": 28}, "x", "x", "qa/x.json") == [], str(_r))
    vp, lp, bp = (os.path.join(_lib.ELEMENTS, "gl-xr-1", "gate", "gl-xr-1-planted" + x) for x in ("-acad.json", ".lsp", ".json"))
    _qd = os.path.join(_lib.ELEMENTS, "gl-xr-1", "qa"); qp = os.path.join(_qd, "gl-xr-1-planted.json"); _mkq = not os.path.isdir(_qd)
    try:
        if _mkq: os.makedirs(_qd)
        open(lp, "w", encoding="utf-8").write(";; gl-xr-1 v1.2  (planted)\n")
        open(vp, "w", encoding="utf-8").write(json.dumps({"pass": True, "date": "planted", "measure_compare": []}))
        open(bp, "w", encoding="utf-8").write(json.dumps(_bl))
        open(qp, "w", encoding="utf-8").write(json.dumps({"pass": True, "triangles": 28, "triangles_generator": 28}))
        why = LN.tools_check("gl-xr-1", "1.2")
        ok1 = any(w.startswith("variant planted: " + LN.QA_SOURCE) for w in why)
        open(qp, "w", encoding="utf-8").write(json.dumps({"pass": True, "triangles": 220, "triangles_generator": 28}))
        why2 = LN.tools_check("gl-xr-1", "1.2")
        t("ESCAPE mech/r140 1: LINE holds an element at station 6 on a variant's Godot QA of another file than its export, and lets the export's own count through",
          ok1 and not any(LN.QA_SOURCE in w for w in why2), f"{why} | {why2}")
    finally:
        for f in (vp, lp, bp, qp):
            if os.path.exists(f): os.remove(f)
        if _mkq and os.path.isdir(_qd) and not os.listdir(_qd): os.rmdir(_qd)
    # request elec-17, ESCAPE elec-r52 (core watch 2026-11-13): mcb-3p 1.1's AutoCAD try failed at its first COM call after writing
    # gate/mcb-3p.lsp (v1.1) and its run log; the 1.0 pass stayed in the JSON, and station 6 read PASS at 1.1
    vp, lp, rp = (os.path.join(_lib.ELEMENTS, "gl-xr-1", "gate", "gl-xr-1-planted" + x) for x in ("-acad.json", ".lsp", "-acad-run.txt"))
    try:
        open(vp, "w", encoding="utf-8").write(json.dumps({"pass": True, "date": "2026-11-12", "measure_compare": []}))
        open(lp, "w", encoding="utf-8").write(";; gl-xr-1 v1.2 {'kind': 'planted'} (gate build 2026-11-13). Generated.\n")
        open(rp, "w", encoding="utf-8").write("acad-gate gl-xr-1 · started 2026-11-13 09:28:01 · log x\nTraceback ...\nAttributeError: Documents.Count\n")
        w_day = [w for w in LN.tools_check("gl-xr-1", "1.2") if w.startswith("variant planted")]
        open(lp, "w", encoding="utf-8").write(";; gl-xr-1 v1.2 {'kind': 'planted'} (gate build 2026-11-12). Generated.\n")
        open(vp, "w", encoding="utf-8").write(json.dumps({"pass": True, "date": "2026-11-12", "measure_compare": []}))
        open(rp, "w", encoding="utf-8").write("acad-gate gl-xr-1 · started 2026-11-12 09:28:01 · log x\nAttributeError: Documents.Count\n")
        w_log = [w for w in LN.tools_check("gl-xr-1", "1.2") if w.startswith("variant planted")]
        open(rp, "a", encoding="utf-8").write("gate gl-xr-1-planted: PASS -> x\n")
        w_ok = [w for w in LN.tools_check("gl-xr-1", "1.2") if w.startswith("variant planted") and "AutoCAD" in w]
        t("ESCAPE elec-r52 (request elec-17): LINE holds a variant whose gate lsp is a run that wrote no result (a later build date, or its own "
          "run log ends without the verdict) though the JSON on file passed; the same run's log with its PASS line passes",
          len(w_day) == 1 and LN.ACAD_NO_RESULT in w_day[0] and len(w_log) == 1 and LN.ACAD_NO_RESULT in w_log[0] and w_ok == [],
          f"{w_day} | {w_log} | {w_ok}")
    finally:
        for f in (vp, lp, rp):
            if os.path.exists(f): os.remove(f)
    # escape group 6 (core watch 2026-11-06; reviewer bench-1800-1.0:1, disc-3p-30a-1.3:4, overload-9a-1.1:2): a brief figure is matched only
    # to the feature it names; an envelope figure the build misses on its own axis beyond ISO 2768-1 m holds the element at station 6
    from . import figcompare as FC
    def _fc1(feat, vals, ext, **k): return FC.compare([dict(feature=feat, values=vals, **k)], ext)[0]
    r = _fc1("depth overall (pins to front)", [83.7], [45.0, 84.9, 71.7]); t("FIG misses overload-9a-1no1nc's 83.7 depth against a build 84.9 deep (the old 2 mm passed it)", r["status"] == "miss", str(r))
    r = _fc1("shaft length", [30.2], [69.1, 86.3, 83.55]); t("FIG never calls a 30.2 shaft found beside a 32.0 hub: a part's figure is 'not located'", r["status"] == "not located", str(r))
    r = _fc1("trip current range", [7.0], [45.0, 84.9, 71.7]); t("FIG skips a current (7.0 A matched a 7.0 mm solid before)", r["status"] == "not a length", str(r))
    r = _fc1("depth", [45.0], [45.0, 84.9, 71.7]); t("FIG matches a named axis only: a 45.0 depth does not pass on the 45.0 width", r["status"] == "miss" and r["axis"] == "y", str(r))
    r = _fc1("width, 1 pole", [17.7], [17.763, 73.001, 105.202]); t("FIG finds mcb-1p-c6's 17.7 width on a 17.763 build (ISO 2768-1 m 0.2)", r["status"] == "found", str(r))
    r = _fc1("height above the shaft centre (terminal box top)", [104.5], [138.0, 250.5, 175.5]); t("FIG takes a height measured from a part as local, not the envelope", r["status"] == "not located", str(r))
    r = _fc1("depth alone (rail back to coil face)", [98.5], [45.0, 148.0, 78.4], source="drawing p. 1; not built (the front block is fitted)"); t("FIG leaves a row the lane marks 'not built' to the reviewer", r["status"] == "not built", str(r))
    vp, lp = (os.path.join(_lib.ELEMENTS, "gl-xr-1", "gate", "gl-xr-1-planted" + x) for x in ("-acad.json", ".lsp"))
    try:
        open(lp, "w", encoding="utf-8").write(";; gl-xr-1 v1.2  (planted)\n")
        open(vp, "w", encoding="utf-8").write(json.dumps({"pass": True, "date": "planted", "step": {"extents": [140.0, 13.1, 33.0]},
                                                          "measure_compare": [{"feature": "width", "values": [138.0], "not_on_file": False}]}))
        why = LN.tools_check("gl-xr-1", "1.2")
        t("LINE holds an element at station 6 when its AutoCAD gate passed with a brief figure off the build (138.0 wide, built 140.0)", any("138" in w and "x extent 140" in w for w in why), str(why))
    finally:
        for f in (vp, lp):
            if os.path.exists(f): os.remove(f)
    # electrical rule check on single conductors
    for roles, rule, want in ((["supply+:24V:US", "supply0"], "ERC-001", "FAIL"), (["in", "lamp+"], "ERC-005", "FAIL"), (["out", "lamp+"], None, None),
                              (["out", "out"], "ERC-003", "FAIL"), (["load+:24V:US", "supply0"], "ERC-004", "FAIL"), (["sw-com", "supply0"], "ERC-006", "FAIL"),
                              (["data:TD+", "data:TD-"], "ERC-008", "FAIL"), (["safe-src:1", "safe-contact:2"], "ERC-009", "FAIL"),
                              (["phase-src:L1", "phase-load:L2"], "ERC-010", "REVIEW"), (["PE", "phase-src:L1"], "ERC-001", "FAIL"), (["sw-no", "in"], None, None)):
        bad, _ = E.net_rules(roles)
        got = {(s, r_) for s, r_, _ in bad}
        t(f"ERC {' + '.join(roles)} → {want or 'clean'}", ((want, rule) in got) if rule else not bad, str(sorted(got)))
    # holes, GD&T, stacks
    P = Prims(); pl = P.box("M-STEEL-7035", 0, 0, 0, 100, 1.5, 100)
    for x in (10, 90): P.hole("M-GASKET", (x, -1, 50), (x, 3, 50), 2.25, pl)
    h, g = V.holes("test-none", P); t("HOLE-010 knows Ø4.5 as M4 clearance", any(s == "PASS" and "M4 clearance medium" in m for s, _, _, m in h), h[0][3])
    gd = V.gdt("test-none", P, g); t("GDT-010 flags a long M4 pattern on general tolerance", any(s == "REVIEW" for s, *_ in gd), gd[0][3])
    P2 = Prims(); pl = P2.box("M-STEEL-7035", 0, 0, 0, 100, 1.5, 100); P2.hole("M-GASKET", (50, -1, 50), (50, 3, 50), 2.0, pl)
    h, _ = V.holes("test-none", P2); t("HOLE-010 flags a Ø4.0 hole as non-standard", any(s == "REVIEW" for s, *_ in h), h[0][3])
    P3 = Prims(); pl = P3.box("M-STEEL-7035", 0, 0, 0, 100, 1.5, 100); P3.hole("M-GASKET", (2.5, -1, 50), (2.5, 3, 50), 2.25, pl)
    d = V.dfm("test-none", P3); t("DFM-010 flags a hole 0.25 from the edge", any(s == "REVIEW" for s, *_ in d), d[0][3] if d else "")
    import tempfile, os
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False)
    f.write("stack,term,element,attr,value,sign,tol,min,max,note\nx,requirement,,,,,,0,,\nx,gap,,,10,+,0.5,,,\nx,part,,,10.2,-,0.5,,,\n"); f.close()
    s = V.stacks(f.name); os.unlink(f.name); t("STK-010 fails a stack that closes to −0.2", s and s[0][0] == "FAIL", s[0][3] if s else "")
    # contacts: the joint's state comes from where the parts are (toolkit/contact.py)
    from . import contact as C, library as L_
    rcp, plg = L_.load("receptacle-m12"), L_.load("plug-m12")
    port, plug = rcp.build(gender="female", coding="A"), plg.build(gender="male", coding="A")
    r = C.mate(port, "self", plug, "self", turns=4); t("contact: nut home, every pole made and sealed", r["seated"] and r["sealed"] and len(r["made"]) == 5, str(r["poles"]))
    r = C.mate(port, "self", plug, "self", gap=4.7); t("contact: 4.7 mm off the seat, the pins only touch (marginal)", all(s["state"] == "marginal" for s in r["poles"].values()), str({p: s["state"] for p, s in r["poles"].items()}))
    r = C.mate(port, "self", plug, "self", turns=0)
    t("contact: pushed on by hand to the thread: made, but not seated or sealed (friction only)", len(r["made"]) == 5 and not r["seated"] and not r["sealed"] and any("friction" in n for n in r["notes"]), "; ".join(r["notes"]))
    r = C.mate(port, "self", plg.build(gender="male", coding="D"), "self", turns=5); t("contact: a D plug's key stops it 8.4 short of an A port", not r["key"] and not r["made"] and abs(r["gap"] - 8.4) < 0.01, "; ".join(r["notes"]))
    r = C.mate(port, "self", plg.build(gender="male", coding="A", conditions="2:bent"), "self", turns=5)
    t("contact: a bent pin rests on the insert face, the plug stops short, nothing made", not r["seated"] and not r["made"] and r["gap"] > 6.0, f"gap {r['gap']}; " + "; ".join(r["notes"]))
    r = C.mate(port, "self", plg.build(gender="male", coding="A", conditions="4:pushed-back"), "self", turns=5)
    t("contact: a pushed-back pin is marginal at the seat, the rest made", r["poles"]["4"]["state"] == "marginal" and len(r["made"]) == 4, str({p: s["state"] for p, s in r["poles"].items()}))
    r = C.mate(port, "self", plug, "self", turns=5, torque=0.2); t("contact: home but under-torqued is not sealed", r["seated"] and not r["sealed"], "; ".join(r["notes"]))
    r = C.mate(port, "self", plug, "self", turns=5, torque=0.9); t("contact: over the 0.6 N m window is flagged (thread damage)", r["sealed"] and any("over 0.6" in n for n in r["notes"]), "; ".join(r["notes"]))
    pL, qL = rcp.build(gender="male", coding="L"), plg.build(gender="female", coding="L")
    r = C.mate(pL, "self", qL, "self", turns=7); t("contact: L-coded, FE a pin in the female half, every pole made", r["seated"] and len(r["made"]) == 5 and r["poles"]["5"]["state"] == "made", str({p: s["state"] for p, s in r["poles"].items()}))
    r = C.mate(pL, "self", qL, "self", gap=4.0)
    t("contact: L-coded FE makes first (4 mm off the seat: FE made, the power pins not yet)", r["poles"]["5"]["state"] == "made" and all(r["poles"][p]["state"] == "open" for p in "1234"), str({p: s["state"] for p, s in r["poles"].items()}))
    r = C.mate(port, "self", plug, "self", turns=4, key_err=1.0)
    t("contact: a key 1° off (past the keyway's 0.81°) stops the plug, nothing made", not r["key"] and not r["made"] and not r["seated"], "; ".join(r["notes"]))
    r = C.mate(port, "self", plug, "self", turns=4, key_err=0.8)
    t("contact: a key 0.8° off (inside the keyway) still seats and makes every pole", r["seated"] and len(r["made"]) == 5, str({p: s["state"] for p, s in r["poles"].items()}))
    r = C.mate(port, "self", plug, "self", turns=4)
    t("contact: the thread catch and length come from both halves (a device female, a cordset male: 1.45 mm)", abs(r["thread_catch"] - 1.45) < 1e-6 and abs(r["thread_engaged"] - 1.45) < 1e-6, f"{r['thread_catch']} / {r['thread_engaged']}")
    # CORE-010: a contact outside what the Rust core's proofs assume is caught
    from . import validate as VA0
    P = L_.load("contact-m12-pin").build(); P.pivots["self"]["range"] = (3.0, 1.0)
    r = VA0.core_assumptions("selftest", P); t("CORE-010 fails a contact whose zone runs backward", any(x[0] == "FAIL" for x in r), str(r))
    # the gate's picks: a circle off its axis-aligned points, alternates, an enclosed edge hidden
    P = Prims(); P.cyl("M-ZINC", (0, 0, 0), (0, 10, 0), 6.0)
    e0 = [e for rec in FI.outer_edges(P, 0.5) for e in rec["edges"]]
    t("FIL-010 picks a circle at a diagonal point, with alternates for the gate", all(abs(e["point"][0]) > 1 and abs(e["point"][2]) > 1 and len(e["alts"]) >= 1 for e in e0), str([(e["point"], len(e["alts"])) for e in e0]))
    P = Prims(); bx = P.box("M-ALU-7035", 0, 0, 0, 60, 60, 60); P.cutbox("M-GASKET", 3, 3, 3, 54, 54, 54, bx); P.cyl("M-ZINC", (30, 20, 30), (30, 40, 30), 8.0)
    st = [e["status"] for rec in FI.outer_edges(P, 0.5) if rec["layer"] == "M-ZINC" for e in rec["edges"]]
    t("FIL-010 skips an edge every view of which another solid blocks (hidden)", st and all(x == "hidden" for x in st), str(st))
    # round 5: a pick is scored by how close another edge passes in its view, at any depth (the gate looks in 2D wireframe)
    P = Prims(); sl = P.cyl("M-ZINC", (0, -8.9, 0), (0, 1.4, 0), 5.46); P.hole("M-GASKET", (0, -9.9, 0), (0, 2.4, 0), 4.15, sl)
    for a_ in (45, 135, 225, 315):
        x_, z_ = 2.5 * math.sin(math.radians(a_)), 2.5 * math.cos(math.radians(a_)); P.cyl("M-GOLD", (x_, 0, z_), (x_, -6.45, z_), 0.5)
    fr = [e for rec in FI.outer_edges(P, 0.5) if rec["index"] == sl for e in rec["edges"] if abs(e["point"][1] + 8.9) < 1e-6][0]
    ang = math.degrees(math.atan2(fr["point"][0], fr["point"][2])) % 90
    t("FIL-010 moves a sleeve's front pick off the diagonals the pins sit behind (clear in its view)", fr["status"] == "pick" and fr["clearance"] >= FI.CLEAR and abs(ang - 45) > 10, f"{fr['point']} {fr['clearance']}")
    P = Prims(); bx = P.box("M-ALU-7035", 0, -50, 0, 100, 50, 30); P.box("M-ALU-7035", -1.5, -72, -1.5, 103, 20.5, 33)
    S_ = __import__("toolkit.solid", fromlist=["Scene"]).Scene(P); e_ = ("line", ((0.0, -50.0, 0.0), (100.0, -50.0, 0.0)))
    d_, _ = FI.clearance(S_, bx, (50.0, -50.0, 0.0), (0.0, -0.7071, -0.7071), e_)
    rim = [e for rec in FI.outer_edges(P, 0.5) if rec["index"] == bx for e in rec["edges"] if abs(e["point"][1] + 50) < 1e-6 and abs(e["point"][2]) < 1e-6][0]
    t("FIL-010 sees a lid edge lying on a rim edge's bisector, and picks the rim from a leaning view", d_ < FI.MIN_CLEAR and rim["status"] == "pick" and abs(rim["view"][1] - rim["view"][2]) > 0.1 and rim["clearance"] >= FI.MIN_CLEAR, f"{d_} {rim['view']} {rim['clearance']}")
    # round 6: a circle a cut interrupts is the arcs it leaves, each with its own length (the gate expects each arc's own volume)
    P = Prims(); kn = P.cyl("M-GREY-PA", (0, 0, 0), (0, 4.0, 0), 3.05); P.cutbox("M-GASKET", -0.3, -1.0, -3.6, 0.6, 2.2, 7.2, kn)
    top = [e for rec in FI.outer_edges(P, 0.5) for e in rec["edges"] if abs(e["point"][1]) < 1e-6 and e["status"] == "pick"]
    t("FIL-010 splits a knob's top circle at its pointer slot into two arcs, each with its own length", len(top) == 2 and all(abs(e["length"] - 3.05 * (math.pi - 2 * math.asin(0.3 / 3.05))) < 0.1 for e in top), str([round(e["length"], 2) for e in top]))
    P = Prims(); fr = P.cyl("M-GREY-PA", (0, 0, 0), (0, 9.0, 0), 4.35); P.cutbox("M-GASKET", -1.7, -1.0, 1.4, 3.4, 9.2, 4.0, fr)
    arc = [e for rec in FI.outer_edges(P, 0.5) for e in rec["edges"] if abs(e["point"][1]) < 1e-6 and e["status"] == "pick"]
    want = 4.35 * (2 * math.pi - 2 * math.asin(1.7 / 4.35))
    t("FIL-010 takes a front circle a recess interrupts as the one arc left (its length, not the circle's)", len(arc) == 1 and abs(arc[0]["length"] - want) < 0.1, f"{[round(e['length'], 2) for e in arc]} want {want:.2f}")
    # round 7: M12-010 mates every insert pair on file; the cordset L female's keyway as first read (its own STEP) must fail it
    from . import m12 as M12, validate as VA1
    keep_ = dict(M12.L_KEY["pocket"]["cordset"]); M12.L_KEY["pocket"]["cordset"] = dict(chord=1.4, feet=(-0.99, 0.99), tops=((-1.7, 3.352), (1.7, 3.352)))
    try: r = VA1.m12_fits(pairs=[("L", "cordset", "cordset")])
    finally: M12.L_KEY["pocket"]["cordset"] = keep_
    t("M12-010 fails a female L keyway its male's block stands 0.30 inside (7700-P4241 as read)", r and r[0][0] == "FAIL", str(r))
    r = VA1.m12_fits(pairs=[("L", "cordset", "device")]); t("M12-010 passes the cordset L female on X03 with X04's outline", r and r[0][0] == "PASS", str(r))
    # a wire end in a screw clamp (toolkit/contact.py terminate)
    cl = L_.load("clamp-screw").build().pivots["self"]; Wm = L_.load("wire")
    def wend(**k): return Wm.build(**{**Wm.PARAMS, **k}).pivots["end-a"]
    r = C.terminate(cl, wend(), depth=9.0); t("clamp: stripped 10, in 9, at torque: made", r["state"] == "made", str(r))
    r = C.terminate(cl, wend(conditions="a:under-stripped"), depth=7.5); t("clamp: under-stripped, insulation under the clamp: marginal", r["state"] == "marginal" and r["insulation"] > 0, str(r))
    r = C.terminate(cl, wend(), depth=9.0, torque=0.0); t("clamp: screw never tightened: open", r["state"] == "open", str(r))
    r = C.terminate(cl, wend(), depth=9.0, torque=0.2); t("clamp: under-torqued: marginal (works loose)", r["state"] == "marginal", str(r))
    r = C.terminate(cl, wend(size=10.0), depth=9.0); t("clamp: a 10 mm² wire in a 4 mm² clamp: blocked", r["state"] == "blocked", str(r))
    r = C.terminate(cl, wend(conditions="a:over-stripped"), depth=7.5); t("clamp: over-stripped: made, bare conductor touchable", r["state"] == "made" and any("touchable" in n for n in r["notes"]), str(r))
    # PIN-030 on a two-port assembly: a male-female cordset between two female ports cannot go on
    from . import validate as VA
    P = Prims()
    for tag, x in (("a", 0.0), ("b", 100.0)): L_.place(P, dict(element="receptacle-m12", version="1.6", tag=tag, parent="", x=x, y=0, z=0, yaw=0.0, params=dict(gender="female", coding="A")))
    for genders, want in (("male-female", "FAIL"), ("male-male", "PASS")):
        f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
        f.write(f"from,to,cable,version,section,length,route,params,note\na,b,cordset-m12,1.4,control & 24 VDC supply,1000,bench,genders={genders},planted\n"); f.close()
        j = VA.joints("selftest", P, path=f.name); os.unlink(f.name)
        got = [x[0] for x in j]
        t(f"PIN-030 {genders} cordset between two female ports → {want}", (want in got) if want == "FAIL" else (got and all(g == "PASS" for g in got)), " | ".join(x[3] for x in j))
    # request elec-1 (ESCAPE, elec r0): DOC-005 missed relay-safety-2ch-2no1nc's open figure written '**assumption**' in lower case
    spec = "# x v1.0\n\n## Nodes\n`sw-mode` (rotate, 0–300°, **{a}**)\n\n## Notes and assumptions\nnone\n\n## History\n| v | what |\n|---|---|\n| 1.0 | {h} |\n"
    r = VA.doc005(spec.format(a="assumption", h="first")); t("DOC-005 counts an open figure marked '**assumption**' in lower case", r and r[0] == "REVIEW", str(r))
    r = VA.doc005(spec.format(a="measured", h="then an assumption: the drawing p. 1 gives it")); t("DOC-005 passes a closed history note and a 'Notes and assumptions' heading", r is None, str(r))
    # round 10 c: the batch rule from round 9's trials (io-block-m12-8di8do's housing hung only with the whole edges and two edges' stretches together)
    P = Prims(); bx = P.box("M-ALU-7035", 0, 0, 0, 40, 10, 20); P.cutbox("M-GASKET", 10, -1, 17, 4, 4, 4, bx); P.cutbox("M-GASKET", 25, 7, 17, 4, 4, 4, bx)
    rec = [r_ for r_ in FI.outer_edges(P, 0.5) if r_["index"] == bx][0]; B = FI.batches(rec); E_ = rec["edges"]
    srcs = [{E_[j]["src"] for j in b_ if E_[j]["stretch"]} for b_ in B]
    t("FIL-010 batches a solid's whole edges together, longest first, and each interrupted edge's stretches alone after them",
      len(B) == 3 and not srcs[0] and all(len(x) == 1 and all(E_[j]["stretch"] for j in b_) for x, b_ in zip(srcs[1:], B[1:]))
      and [E_[j]["length"] for j in B[0]] == sorted((E_[j]["length"] for j in B[0]), reverse=True) and sum(map(len, B)) == sum(e["status"] == "pick" for e in E_), str(B))
    P = Prims(); P.box("M-ALU-7035", 0, 0, 0, 40, 10, 20); B = FI.batches(FI.outer_edges(P, 0.5)[0])
    t("FIL-010 keeps a solid with no interrupted edge in one batch", len(B) == 1 and len(B[0]) == 12, str(B))
    # round 10 d: an assembly finding holds the elements it judged (station 5: ERC / ELR; station 6: PIN-030, GEO-020)
    P = Prims(); P.box("M-STEEL", 0, 0, 0, 10, 10, 10); P.owners.append((0, 1, "panel-1", "pm-motor-starter")); P.box("M-STEEL", 20, 0, 0, 10, 10, 10); P.owners.append((1, 2, "panel-1.k1", "contactor-9a-1no1nc"))
    F_ = VA.assembly_findings("selftest", P, [("FAIL", "ELR-011", "motor-m1 panel-1.k1", "AC-3 6 A < motor current 9.10 A (planted)")])
    rows = LN.element("contactor-9a-1no1nc", findings=F_, cat={"contactor-9a-1no1nc": {"version": "9.9"}}, tags=set(), reviews="", safety=set())
    t("ELR-011 below the motor current holds the contactor at station 5 (the finding names it)", F_[0]["elements"] == ["contactor-9a-1no1nc"] and LN.reached(rows) == 4 and any("ELR-011" in w for w in rows[4][4]), f"{F_[0]['elements']} reached {LN.reached(rows)}")
    P = Prims(); P.box("M-STEEL", 0, 0, 0, 10, 10, 10); P.owners.append((0, 1, "a", "plc0")); P.box("M-STEEL", 8, 0, 0, 10, 10, 10); P.owners.append((1, 2, "b", "psu-24v-2a4"))
    F_ = VA.assembly_findings("selftest", P, G.interference(P, "selftest"))
    t("GEO-020 in an assembly holds both elements that overlap", any(f_["status"] == "FAIL" and sorted(f_["elements"]) == ["plc0", "psu-24v-2a4"] for f_ in F_), str([f_["elements"] for f_ in F_]))
    P = Prims()
    for tag, x in (("a", 0.0), ("b", 100.0)): L_.place(P, dict(element="receptacle-m12", version="1.6", tag=tag, parent="", x=x, y=0, z=0, yaw=0.0, params=dict(gender="female", coding="A")))
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
    f.write("from,to,cable,version,section,length,route,params,note\na,b,cordset-m12,1.4,control & 24 VDC supply,1000,bench,genders=male-female,planted\n"); f.close()
    F_ = VA.assembly_findings("selftest", P, VA.joints("selftest", P, path=f.name)); os.unlink(f.name)
    bad_ = [f_ for f_ in F_ if f_["status"] == "FAIL"]
    t("PIN-030 a cable end that cannot mate holds the cable and the element whose port it meets", bad_ and all(sorted(f_["elements"]) == ["cordset-m12", "receptacle-m12"] for f_ in bad_), str([f_["elements"] for f_ in F_]))
    # round 10 b, e: Assumptions by class; EM's approval is '· EM <date>', one line per figure
    sp = "# x v1.0\n\nwidth 40 (**Assumption (B)**: no drawing)\ncolour grey (**Assumption (C)**)\ncurrent 2 A NOT ON FILE\n{s}\n## History\n| 1.0 | first |\n"
    r = VA.doc005(sp.format(s="REVIEW accepted: width 40, the panel cut-out fits · mech 2026-11-05"))
    t("DOC-005 holds an element whose 'REVIEW accepted:' has no '· EM <date>' (a proposal)", r and r[0] == "REVIEW" and "proposal" in r[2], str(r))
    r = VA.doc005(sp.format(s="REVIEW accepted: width 40 · EM 2026-11-05"))
    t("DOC-005 holds an element with one EM approval, an open NOT ON FILE figure and a class B figure (a source wanted, not EM's)", r and r[0] == "REVIEW" and "source" in r[2], str(r))
    r = VA.doc005(sp.format(s="REVIEW accepted: width 40 · EM 2026-11-05\nREVIEW accepted: current 2 A, the datasheet's · EM 2026-11-05"))
    t("DOC-005 passes one EM approval per open figure; the class C colour needs none", r and r[0] == "PASS", str(r))
    # EM 2026-11-09: a class B figure is a document wanted, not a line of EM's per figure
    r = VA.doc005("# x v1.0\n\nflange to ISO 5211 NOT ON FILE (B): the standard is not on file\n## History\n| 1.0 | first |\n")
    t("DOC-005 holds a class B figure alone as 'source wanted' (the document, asked for once), which the board reads as src, not EM",
      r and r[0] == "REVIEW" and r[2].startswith("source wanted") and not LN.waits_on_em((7, "signoff", "x", False, [f"{r[1]} {r[0]}: {r[2]}"]))
      and LN.waits_on_source((7, "signoff", "x", False, [f"{r[1]} {r[0]}: {r[2]}"])) and not LN.waits_on_source((7, "signoff", "x", False, [f"{r[1]} {r[0]}: {r[2]}", "DOC-006 REVIEW: vendor name"])), str(r))
    r = VA.doc005("# x v1.0\n\nflange to ISO 5211 NOT ON FILE (B): the standard is not on file\nREVIEW accepted: flange to ISO 5211 · EM 2026-11-09\n## History\n| 1.0 | first |\n")
    t("DOC-005 passes a class B figure EM chose to accept anyway", r and r[0] == "PASS", str(r))
    from . import derive as DV
    _t8 = DV.thread(8); _t6 = DV.thread(6)
    t("derive: ISO 68-1 / ISO 965-1 give M8 6g / 6H within 0.01 mm of the published limits (d 7.760–7.972, d2 7.042–7.160, D1 6.647–6.912, D2 7.188–7.348) and M6 likewise",
      all(abs(a - b) <= 0.01 for a, b in ((_t8["ext"]["d_max"], 7.972), (_t8["ext"]["d_min"], 7.760), (_t8["ext"]["d2_max"], 7.160), (_t8["ext"]["d2_min"], 7.042),
                                        (_t8["int"]["D1_min"], 6.647), (_t8["int"]["D1_max"], 6.912), (_t8["int"]["D2_min"], 7.188), (_t8["int"]["D2_max"], 7.348),
                                        (_t6["ext"]["d_min"], 5.794), (_t6["int"]["D1_max"], 5.153), (_t6["int"]["D2_max"], 5.500))), str(_t8))
    t("derive: a 7.5 kW 460 V motor draws about 12 A at IE3 efficiency; a bore-40 cylinder at 160 bar presses 20.1 kN and runs 0.29 m/s on 22 l/min; a 23.4 mm copper bar of 8.84 mm² is 46 µΩ",
      DV.motor_current(7.5, 460)["I"] == 12.08 and DV.cylinder(40, 22, 160, 22)["F_kN"] == 20.11 and DV.cylinder(40, 22, 160, 22)["v_out_m_s"] == 0.292 and DV.resistance("copper", 23.4, 8.84)["R_uohm"] == 45.64)
    # request mech-7 (2026-11-10): derive.torque, the torque-tension relation (ISO 16047 / VDI 2230 Part 1) on ISO 898-1's stress area
    _as = {6: 20.1, 8: 36.6, 10: 58.0, 12: 84.3}
    _q = DV.torque(8, prop_class="8.8", mu_G=0.12, mu_K=0.12, nu=0.7, d_w=13)
    _F = 0.7 * 640 * math.pi / 4 * ((7.188 + 6.4665) / 2) ** 2; _M = _F * (0.16 * 1.25 + 0.58 * 0.12 * 7.188 + 0.12 * (13 + 9.0) / 2 / 2) / 1000
    t("derive: ISO 898-1's stress area formula gives the published A_s of M6, M8, M10, M12 (20.1, 36.6, 58.0, 84.3 mm²) within 0.1",
      all(abs(DV.stress_area(dd)[0] - a) <= 0.1 for dd, a in _as.items()), str({dd: round(DV.stress_area(dd)[0], 2) for dd in _as}))
    t("derive: torque M8 8.8 (ν 0.7, μ 0.12, d_w 13, ISO 273 medium hole 9.0) is F_M = ν·640·A_s and M_A = F_M (0.16P + 0.58 μ d2 + μ D_Km/2), its design inputs in its source",
      _q["d_h"] == 9.0 and _q["ReL_nom"] == 640 and abs(_q["F_kN"] - _F / 1000) < 0.01 and abs(_q["M_Nm"] - _M) < 0.1 and "nu 0.7" in _q["source"] and "d_w 13" in _q["source"], str(_q))
    _bad = []
    for _kw in (dict(prop_class="A2-70", d_w=13), dict(prop_class="8.8"), dict(prop_class="8.8", d_w=8)):
        try: DV.torque(8, **_kw); _bad.append(_kw)
        except ValueError: pass
    t("derive: torque refuses a class its designation doesn't give by formula (A2-70), a missing bearing face d_w, and a face inside the hole", not _bad, str(_bad))
    _w = DV.wanted_md()
    t("wanted: the documents class B figures wait for are listed once each with their elements", _w.startswith("# Documents wanted") and "## " in _w)
    r = VA.doc005("# x v1.0\n\nlabel 3 mm from the edge (**Assumption (C)**)\n## History\n| 1.0 | first |\n")
    t("DOC-005 passes a class C (cosmetic) Assumption alone: the reviewer's PASS at station 7 accepts it", r and r[0] == "PASS", str(r))
    r = VA.doc005("# x v1.0\n\nrated 6 A (**Assumption**)\nREVIEW accepted: · EM 2026-11-05\n## History\n| 1.0 | first |\n")
    t("DOC-005 counts an Assumption with no class as A and an approval that names no figure as nothing", r and r[0] == "REVIEW" and "no class" in r[2], str(r))
    import importlib.util as _iu
    sp_ = _iu.spec_from_file_location("autopilot_selftest", os.path.join(_lib.ROOT, "autopilot.py")); AP = _iu.module_from_spec(sp_); sp_.loader.exec_module(AP)
    _ev = []
    class _FakeP:                                                    # core watch 2026-11-11: the library's prompt came after claude's 3 s stdin wait
        pid = 1; returncode = 0
        def __init__(self, *a, **k): _ev.append("start")
        def communicate(self, text, timeout=None): _ev.append(("stdin", text))
    _op = AP.subprocess.Popen
    try:
        AP.subprocess.Popen = _FakeP
        _lr = AP.launch(["claude", "-p"], ".", None, {}, lambda: (_ev.append("built"), "the prompt")[1], 60)
    finally: AP.subprocess.Popen = _op
    t("an unattended run builds its prompt before the session starts and writes it at once (autopilot.launch; the library's merge_list fetch outlasted claude -p's 3 s stdin wait)",
      _ev == ["built", "start", ("stdin", "the prompt")] and _lr == "exit 0", str(_ev))
    _og = AP.git                                                     # core watch 2026-11-11: elec's 16 starts in 18 minutes
    def _fake_git(subj, files):
        def g(*a, **k):
            return {"rev-parse": "b2", "log": subj, "diff": "\n".join(files)}.get(a[0], "")
        return g
    try:
        AP.git = _fake_git("elec needs-em (unattended, 2026-11-10 21:44 start): no round; fifteenth start", ["lib/needs-em/elec.md"]); _c1 = AP.chain_next({}, "elec", ".", "a1", "exit 0")
        AP.git = _fake_git("elec needs-em (unattended): the merge refused", ["lib/needs-em/elec.md", "lib/rounds/elec/next.md"]); _c2 = AP.chain_next({}, "elec", ".", "a1", "exit 0")
        AP.git = _fake_git("elec-r27 (unattended): xfmr-control 1.0", ["lib/elements/xfmr-control/element.py", "lib/rounds/elec/r27.md"]); _c3 = AP.chain_next({}, "elec", ".", "a1", "exit 0")
    finally: AP.git = _og
    t("a lane run whose commits touch only its notes (needs-em, its round report, a request) does not chain into the next start; one that built does (autopilot.chain_next)",
      (_c1, _c2, _c3) == (False, False, True), str((_c1, _c2, _c3)))
    d_ = "+++ b/lib/elements/x/spec.md\n@@ -3 +3,2 @@\n-REVIEW accepted: width 40 · EM 2026-11-01\n+REVIEW accepted: width 40 · EM 2026-11-05\n+width 40 (Assumption (B))\n"
    t("an unattended push that adds a line carrying '· EM <date>' is refused (autopilot pre-push)", AP.em_lines(d_) == ["REVIEW accepted: width 40 · EM 2026-11-05"] and AP.em_lines("-x · EM 2026-11-05\n x · EM 2026-11-05\n") == [], str(AP.em_lines(d_)))
    # elec-r27, 2026-11-11: the push refused for main's own EM-marked lines, carried in by a repair commit; and the orphaned tails that began it
    _dm = "+++ b/lib/reviews/elements/x-1.0.md\n@@ -0,0 +1,2 @@\n+REVIEW accepted: width 40 · EM 2026-11-05\n+REVIEW accepted: depth 9 · EM 2026-11-11\n"
    _on = AP.em_not_on(AP.em_lines_by_file(_dm), lambda p_: "# x\nREVIEW accepted: width 40 · EM 2026-11-05\n" if p_ == "lib/reviews/elements/x-1.0.md" else "")
    t("an unattended push that carries a line with EM's mark which main already holds in that file is not refused for it; a marked line main does not hold still is",
      _on == [("lib/reviews/elements/x-1.0.md", "REVIEW accepted: depth 9 · EM 2026-11-11")], str(_on))
    _sw = AP.stale_watchers(["92088|1|2700|tail.exe", "89880|1|2690|tail.exe", "100|0|2700|tail.exe", "101|1|30|grep.exe", "102|1|500|python.exe", "x|1|500|tail.exe", "103|1|121|grep.exe"])
    t("autopilot ends a tail or grep whose shell is gone and that is older than two hours, and leaves one whose shell lives, a young one, and every other program",
      _sw == [92088, 89880, 103], str(_sw))
    # core watch 2026-11-06: publish_status piped text to git, and on Windows branch line-status got "status.md\r" with a mangled "·"
    import subprocess as _sp, tempfile as _tf
    _seen = []; _run = AP.subprocess.run
    def _spy(*a, **k): _seen.append((type(k.get("input")).__name__, bool(k.get("text")))); return _run(*a, **k)
    with _tf.TemporaryDirectory() as _d:
        _run(["git", "init", "-q", _d], capture_output=True)
        AP.subprocess.run = _spy
        try: _tr = AP.status_tree("# Line status · 02:13\n", _d)
        finally: AP.subprocess.run = _run
        _ls = _run(["git", "ls-tree", "-z", _tr], capture_output=True, cwd=_d).stdout
        _name = _ls.split(b"\t", 1)[-1].rstrip(b"\0") if _ls else b""
        _body = _run(["git", "cat-file", "blob", f"{_tr}:status.md"], capture_output=True, cwd=_d).stdout if _name == b"status.md" else b""
    t("the line status goes to git as UTF-8 bytes and the file is named exactly status.md (autopilot.status_tree)",
      _name == b"status.md" and _body == "# Line status · 02:13\n".encode("utf-8") and _seen and all(i in ("bytes", "NoneType") and not tx for i, tx in _seen),
      f"{_name!r} {_seen}")
    _pt = AP.parse_task('"TaskName","Scheduled Task State","Status","Last Run Time","Last Result","Next Run Time"\n'
                        '"\\complexes\\elec","Enabled","Running","11/6/2026 1:27:00 AM","-2147020576","11/6/2026 2:27:00 AM"\n')
    t("a Windows task's Last Result is read out: -2147020576 is 0x800710E0, Windows refused to start it; 0 is ok (autopilot.task_result)",
      "Last Result: -2147020576 (0x800710E0: Windows refused" in _pt and AP.task_result("0") == "ok" and AP.task_result("267009") == "running now", _pt)
    # EM 2026-11-06: elec's task stood "Running" with no run alive from 13:58 the day before, and Windows refused every start
    with _tf.TemporaryDirectory() as _d:
        _st, _al, _tr_, _sl = AP.state, AP.alive, AP.task_record, AP.time.sleep
        AP.state = lambda *p: AP.os.path.join(_d, *p); AP.alive = lambda pid: pid == 4242
        try:
            _R = {"Status": "Running"}
            _never = AP.stuck("elec", _R)
            _ready = AP.stuck("elec", {"Status": "Ready"})
            open(AP.os.path.join(_d, "elec.pid"), "w").write("4242"); _going = AP.stuck("elec", _R); AP.os.remove(AP.os.path.join(_d, "elec.pid"))
            open(AP.os.path.join(_d, "elec.start"), "w").write("x"); _fresh = AP.stuck("elec", _R)
            _old = AP.time.time() - 3 * 3600; AP.os.utime(AP.os.path.join(_d, "elec.start"), (_old, _old))
            with open(AP.os.path.join(_d, "runs.csv"), "w", encoding="utf-8") as _f:
                _f.write("shift,lane,started,ended,result,log\n")
                _f.write(f"s,elec,x,{AP.dt.datetime.fromtimestamp(AP.time.time() - 2 * 3600):%Y-%m-%d %H:%M},exit 0,l\n")
            _hung = AP.stuck("elec", _R)
            _cmds = []
            AP.task_record = lambda ln: _R if ln == "elec" else {"Status": "Ready"}
            AP.time.sleep = lambda n: None
            AP.subprocess.run = lambda c, **k: (_cmds.append(" ".join(c)), _sp.CompletedProcess(c, 0, "", ""))[1]
            import contextlib as _cl, io as _io
            try:
                with _cl.redirect_stdout(_io.StringIO()):                  # round 15's return: the planted restart's message read like a real one
                    AP.unstick("elec"); _self = list(_cmds)
                    AP.unstick("mech")
            finally: AP.subprocess.run = _run
            _log = open(AP.os.path.join(_d, "unstuck.log"), encoding="utf-8").read()
        finally: AP.state, AP.alive, AP.task_record, AP.time.sleep = _st, _al, _tr_, _sl
    t("a lane's Windows task held Running with no run alive and nothing for an hour is stuck; Ready, a live round or a start within the hour is not (autopilot.stuck)",
      _never == "never" and _ready is None and _going is None and _fresh is None and _hung and _hung != "never", f"{_never} {_ready} {_going} {_fresh} {_hung}")
    # EM 2026-11-07: "I see cad is not working": every run exited 1 within a minute, and the reason sat only in the PC's logs
    with _tf.TemporaryDirectory() as _d:
        _st = AP.state; AP.state = lambda *p: os.path.join(_d, *p); os.makedirs(os.path.join(_d, "logs"))
        try:
            _fut, _past = int(AP.time.time()) + 3600, int(AP.time.time()) - 60
            open(os.path.join(_d, "logs", "a.log"), "w").write(f"working\nClaude AI usage limit reached|{_fut}\n")
            open(os.path.join(_d, "logs", "b.log"), "w").write(f"Claude AI usage limit reached|{_past}\n")
            open(os.path.join(_d, "logs", "c.log"), "w").write("Invalid API key · Please run /login\n")
            _lu = AP.limit_until([{"result": "exit 1", "log": "a.log"}]); _lp = AP.limit_until([{"result": "exit 1", "log": "b.log"}])
            _lo = AP.limit_until([{"result": "exit 0", "log": "a.log"}]); _tc = AP.log_tail("c.log"); _ta = AP.log_tail("a.log")
            # core watch 2026-11-08: the weekly limit's refusal names a clock time, not an epoch, and was not read: the library
            # started into it 04:52 to 08:52 and the lanes lost their starts with it
            open(os.path.join(_d, "logs", "d.log"), "w").write("You've hit your weekly limit · resets 9am (America/Chicago)\n")
            _n0 = AP.dt.datetime(2026, 11, 8, 8, 52)
            _row = {"result": "exit 1", "log": "d.log", "ended": "2026-11-08 08:52"}
            _ld = AP.limit_until([_row], now=_n0)                                                   # read in this machine's zone
            _ld_after = AP.limit_until([_row], now=_ld + AP.dt.timedelta(minutes=7)) if _ld else "unread"   # past its reset: not held
        finally: AP.state = _st
    t("a run refused for the usage limit holds the next starts until its reset time, and a failed run's reason reads in the status (autopilot.limit_until, log_tail)",
      _lu is not None and _lp is None and _lo is None and "Please run /login" in _tc and str(_fut) not in _ta and "limit reached|20" in _ta, f"{_lu} {_lp} {_lo} {_tc} {_ta}")
    # core watch 2026-11-11: from 02:07 CST every start exited 1 at once, "You're out of usage credits": no reset time, so nothing
    # headed the status, and each refused start still spent a slot of the shift's budget (core's 2 among them)
    with _tf.TemporaryDirectory() as _d:
        _st = AP.state; AP.state = lambda *p: os.path.join(_d, *p); os.makedirs(os.path.join(_d, "logs"))
        try:
            _cr = "You're out of usage credits. Switch to another model, or manage usage credits at https://claude.ai/settings/usage\n"
            open(os.path.join(_d, "logs", "ok.log"), "w").write("round done\n")
            open(os.path.join(_d, "logs", "cr1.log"), "w").write(_cr)
            open(os.path.join(_d, "logs", "cr2.log"), "w").write("built two parts\n" + _cr)
            open(os.path.join(_d, "logs", "err.log"), "w").write("Traceback: KeyError\n")
            _ok = {"lane": "mech", "started": "2026-11-11 01:00", "ended": "2026-11-11 01:40", "result": "exit 0", "log": "ok.log"}
            _long = {"lane": "mech", "started": "2026-11-11 02:48", "ended": "2026-11-11 03:48", "result": "exit 1", "log": "cr2.log"}
            _now1 = {"lane": "elec", "started": "2026-11-11 03:27", "ended": "2026-11-11 03:27", "result": "exit 1", "log": "cr1.log"}
            _err = {"lane": "elec", "started": "2026-11-11 03:27", "ended": "2026-11-11 03:27", "result": "exit 1", "log": "err.log"}
            _rf = (AP.refused(_now1), AP.refused(_long), AP.refused(_err), AP.refused(_ok))
            _co = AP.credits_out([_ok, _long, _now1]); _co0 = AP.credits_out([_long, _now1, _ok]); _co1 = AP.credits_out([_now1, _err])
            _cl = AP.credit_lines([_ok, _long, _now1], AP.dt.datetime(2026, 11, 11, 4, 18))
        finally: AP.state = _st
    t("a start refused at once for the account's credits or limit spends no budget, and a line out of credits says so in one STALLED line with since when (autopilot.refused, credits_out, credit_lines)",
      _rf == (True, False, False, False) and _co and _co[1] == 2 and str(_co[0]) == "2026-11-11 02:48:00" and _co0 is None
      and _co1 is None and _cl and _cl[0].startswith("STALLED: the account is out of usage credits since 2026-11-11 02:48 (1.5 h); 2 run(s)"),
      f"{_rf} {_co} {_co0} {_co1} {_cl}")
    _T = "You've hit your weekly limit · resets 9am (America/Chicago)"
    _r1 = AP.reset_at(_T, _n0, local_offset=-6)                               # the PC in Chicago: 09:00 today
    _r2 = AP.reset_at(_T, AP.dt.datetime(2026, 11, 8, 9, 7), local_offset=-6) # already past: the next 09:00
    _r3 = AP.reset_at(_T, AP.dt.datetime(2026, 11, 8, 14, 52), local_offset=0) # a PC on UTC: Chicago's 09:00 is 15:00
    _r4 = AP.reset_at("You've hit your limit · resets 3:30pm", _n0, local_offset=-6)
    _r5 = AP.reset_at("You've hit your weekly limit · resets Nov 10 at 9am (America/Chicago)", _n0, local_offset=-6)
    _r6 = AP.reset_at("You've hit your weekly limit · resets 9am (Mars/Olympus)", _n0, local_offset=-6)
    _r7 = AP.reset_at("Invalid API key · Please run /login", _n0)
    import inspect as _insp
    from . import approvals as _apv
    _oz = _apv._zone
    try: _apv._zone = lambda tz, zoneinfo=True: _oz(tz, False); _r1b = AP.reset_at(_T, _n0, local_offset=-6)   # the PC without tzdata
    finally: _apv._zone = _oz
    t("a refusal that says 'resets 9am (America/Chicago)' is read as the PC's local time, with or without zone data, a date or another zone; an unknown zone or no reset is None (autopilot.reset_at)",
      _r1 == AP.dt.datetime(2026, 11, 8, 9) and _r1b == _r1 and _r2 == AP.dt.datetime(2026, 11, 9, 9) and _r3 == AP.dt.datetime(2026, 11, 8, 15)
      and _r4 == AP.dt.datetime(2026, 11, 8, 15, 30) and _r5 == AP.dt.datetime(2026, 11, 10, 9) and _r6 is None and _r7 is None
      and _ld is not None and _ld != "unread" and _ld > _n0 and _ld_after is None, f"{_r1} {_r1b} {_r2} {_r3} {_r4} {_r5} {_r6} {_r7} {_ld} {_ld_after}")
    # EM 2026-11-07: pneu ran 38 idle rounds in a row, mech four; each spent the allowance the building lanes needed
    with _tf.TemporaryDirectory() as _d, _tf.TemporaryDirectory() as _g:
        _st = AP.state; AP.state = lambda *p: os.path.join(_d, *p)
        try:
            _run(["git", "init", "-q", _g], capture_output=True)
            _cm = lambda m: _run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "--allow-empty", "-m", m], cwd=_g, capture_output=True)
            _cm("pneu-r45 (unattended): idle (38th in a row, waiting on EM: pneu-2)")
            open(os.path.join(_d, "pneu.inputs"), "w").write("fp1")
            _iw_same, _iw_new = AP.idle_wait("pneu", _g, "fp1"), AP.idle_wait("pneu", _g, "fp2")
            # core watch 2026-11-08: mech's 19:07 start, refused within a minute, recorded the inputs the core merge had just changed,
            # and every start after the limit's reset skipped as "nothing changed"
            _ri_fail = AP.record_inputs("pneu", "fp2", "exit 1; left uncommitted changes"); _iw_fail = AP.idle_wait("pneu", _g, "fp2")
            _ri_stop = AP.record_inputs("pneu", "fp2", "stopped at the 150 min limit"); _iw_stop = AP.idle_wait("pneu", _g, "fp2")
            _ri_done = AP.record_inputs("pneu", "fp2", "exit 0"); _iw_done = AP.idle_wait("pneu", _g, "fp2")
            _cm("pneu-r46 (unattended): fitting-npt 1.0, standard part, station 6")
            _iw_built = AP.idle_wait("pneu", _g, "fp1")
        finally: AP.state = _st
    t("an idle lane waits until main changes something it could use, starts when it does, and a building lane never waits (autopilot.idle_wait)",
      _iw_same and _iw_new is None and _iw_built is None, f"{_iw_same} | {_iw_new} | {_iw_built}")
    # core watch 2026-11-14, the improvement run: lib/reviews as one tree woke the idle panel shop on every review of another lane's
    # rounds (8 of its 36 wakes 11-11 to 11-13; panel-r19, r30, r31 idle), and the line then stood 41 h on the weekly limit
    with _tf.TemporaryDirectory() as _g:
        def _w(p, s):
            os.makedirs(os.path.dirname(os.path.join(_g, p)), exist_ok=True); open(os.path.join(_g, p), "w", encoding="utf-8").write(s)
        def _cm(m):
            _run(["git", "add", "-A"], cwd=_g, capture_output=True)
            _run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", m], cwd=_g, capture_output=True)
            return {ln: AP.inputs_fp("HEAD", ln, cwd=_g) for ln in ("panel", "mech")} | {None: AP.inputs_fp("HEAD", cwd=_g)}
        _run(["git", "init", "-q", _g], capture_output=True)
        _w("lib/OWNERS.csv", "path,owner,note\nlib/elements/bench-1800/*,mech,\nlib/elements/mcb-2p/*,elec,\n")
        for _p in ("lib/reviews/mech/r1.md", "lib/reviews/panel/r1.md", "lib/toolkit/x.py", "lib/elements/bench-1800/element.py",
                   "lib/elements/mcb-2p/element.py", "lib/assemblies/mc-1/controls.csv"): _w(_p, "1\n")
        _w("lib/assemblies/pnl-a/bom.csv", "element,version\nmcb-2p,1.0\n")
        _f0 = _cm("base")
        _w("lib/reviews/mech/r2.md", "PASS\n"); _f1 = _cm("review mech-r2")                     # another lane's round review
        _w("lib/reviews/elements/mcb-2p-1.0.md", "PASS\n"); _f2 = _cm("review mcb-2p")           # elec's element
        _w("lib/reviews/elements/bench-1800-1.0.md", "FINDINGS\n"); _f3 = _cm("review bench")    # mech's own element
        _w("lib/elements/mcb-2p/element.py", "2\n"); _f4 = _cm("mcb-2p 1.1")                     # a version the panel can pin
        _w("lib/assemblies/mc-1/controls.csv", "2\n"); _f5 = _cm("a controls spec")
        _w("lib/reviews/panel/r2.md", "PASS\n"); _f6 = _cm("review panel-r2")
    _lw = [(a["panel"] == b["panel"], a["mech"] == b["mech"], a[None] == b[None]) for a, b in zip((_f0, _f1, _f2, _f3, _f4, _f5), (_f1, _f2, _f3, _f4, _f5, _f6))]
    t("an idle lane wakes on its own reviews, its own elements' reviews and, for the panel shop, a new version it places or a controls spec; not on another lane's (autopilot.lane_inputs)",
      _lw == [(True, False, False), (True, True, False), (True, False, False), (False, True, True), (False, True, True), (False, True, False)], _lw)
    # core watch 2026-11-10, the improvement run: elec-9's answer and round 26 sat on core 14 h, the queue 9 h, library budget 0
    import datetime as _dts
    _nw = _dts.datetime(2026, 11, 10, 8, 7)
    _sl0 = AP.stall_lines(_nw, 0, True, _dts.datetime(2026, 11, 9, 18, 42), ["elec-9", "pneu-7"], _dts.datetime(2026, 11, 9, 22, 57), 3) if hasattr(AP, "stall_lines") else []
    _sl1 = AP.stall_lines(_nw, 8, False, None, [], _dts.datetime(2026, 11, 9, 22, 57), 1) if hasattr(AP, "stall_lines") else []
    _sl2 = AP.stall_lines(_nw, 8, True) if hasattr(AP, "stall_lines") else ["missing"]
    t("the status says when nothing reaches main, why, and how long the core's answers and the queue have waited (autopilot.stall_lines, stalls)",
      len(_sl0) == 3 and _sl0[0].startswith("STALLED") and "library's budget is 0" in _sl0[0] and "elec-9, pneu-7" in _sl0[1] and "(13.4 h)" in _sl0[1]
      and "3 queued lane round(s)" in _sl0[2] and "(9.2 h)" in _sl0[2]
      and len(_sl1) == 2 and "no shift is open" in _sl1[0] and "budget" not in _sl1[0].split(";")[0]
      and _sl2 == [] and "stalls(c)" in _insp.getsource(AP.status), f"{_sl0} | {_sl1} | {_sl2}")
    # core watch 2026-11-15, the improvement run: line-status last written 16:08 CST 11-14, the PC silent 16 h, and no reader said so
    _st = ("# Line status · 2026-11-14 16:08\n\n```\nshift: 2026-11-14 10:48 to 2026-11-14 18:48 (open)\n"
           "usage limit: the account's limit was reached; runs wait until 2026-11-15 09:00\n```\n")
    _hs = getattr(AP, "silence_lines", None)
    _si0 = _hs(_st, _dts.datetime(2026, 11, 15, 9, 30)) if _hs else []
    _si1 = _hs(_st, _dts.datetime(2026, 11, 14, 17, 30)) if _hs else ["missing"]
    _si2 = _hs("", _dts.datetime(2026, 11, 15, 9, 30)) if _hs else []
    t("a session in the cloud reads the PC's silence from line-status: its age, a usage limit already reset, a shift already closed (autopilot.silence_lines; build.py silent)",
      len(_si0) == 3 and _si0[0].startswith("PC SILENT") and "(17.4 h)" in _si0[0] and "reset at 2026-11-15 09:00" in _si0[1]
      and "closed at 2026-11-14 18:48" in _si0[2] and _si1 == [] and len(_si2) == 1 and _si2[0].startswith("PC SILENT"), f"{_si0} | {_si1} | {_si2}")
    # core watch 2026-11-17, the improvement run: the PC silent 64 h, 0 elements for 88 h, and no reader named the generic elements the
    # cloud could build meanwhile (EM 2026-11-07: the cloud builders), or that starting them is EM's
    _sa, _cl = getattr(AP, "silence_age", None), getattr(AP, "cloud_lines", None)
    _ca = _sa(_st, _dts.datetime(2026, 11, 15, 9, 30)) if _sa else None
    _cl0 = _cl(30.0, {"mech": [("EC012003", "Ball joint")], "elec": []}, {"mech": "2026-11-07"}) if _cl else []
    _cl1 = _cl(_ca, {"mech": [("EC012003", "Ball joint")]}) if _cl and _ca is not None else ["missing"]
    _cl2 = _cl(None, {"mech": [("EC012003", "Ball joint")]}) if _cl else ["missing"]
    t("a PC silent 24 h or more names the generic elements the cloud could build to station 5, and that starting them is EM's (autopilot.cloud_lines; build.py silent)",
      _ca is not None and abs(_ca - 17.367) < 0.01 and len(_cl0) == 2 and _cl0[0].startswith("CLOUD CAN BUILD") and "30.0 h" in _cl0[0]
      and "EM's" in _cl0[0] and _cl0[1] == "  mech: EC012003 Ball joint (cloud-mech last built 2026-11-07)" and _cl1 == [] and _cl2 == [],
      f"{_ca} | {_cl0} | {_cl1} | {_cl2}")
    # core watch 2026-11-18, the improvement run: the summary reads main, and every needs-em.md entry core watch wrote while the PC
    # was silent (PC SILENT, the cloud builders' decision) stood on origin/core alone for four days
    _un, _ul = getattr(AP, "unmerged_needs", None), getattr(AP, "unmerged_lines", None)
    _nm = "# Needs EM\n\n## 2026-11-13 14:30 CST · round 37 ready\n\n- **Yours: the next whole machine.** more\n"
    _nc = ("# Needs EM\n\n## 2026-11-17 08:50 CST · the cloud could build\n\n- **Yours, a decision: start the cloud builders again?** On"
           " 11-07 ...\n- **Nothing to decide, done.** x\n\n## 2026-11-15 08:35 CST · PC SILENT\n\n- **Yours, the line's cost: PC SILENT:"
           " line-status last written 2026-11-14 16:08 CST (16.2 h). Every start.** y\n\n" + _nm.split("\n\n", 1)[1])
    _u0 = _un(_nm, _nc) if _un else []
    _u1 = _un(_nc, _nc) if _un else ["missing"]
    _ul0 = _ul(_u0) if _ul else []
    t("the core's needs-em entries that main lacks are named for the summary, which reads main (autopilot.unmerged_needs; build.py needs-em)",
      [h for h, _ in _u0] == ["2026-11-17 08:50 CST · the cloud could build", "2026-11-15 08:35 CST · PC SILENT"]
      and _u0[0][1] == ["Yours, a decision: start the cloud builders again?", "Nothing to decide, done"]
      and _u0[1][1] == ["Yours, the line's cost: PC SILENT: line-status last written 2026-11-14 16:08 CST (16.2 h)"]
      and _u1 == [] and _ul0 and _ul0[0].startswith("NEEDS EM, NOT ON MAIN: 2 entries") and _ul([]) == [],
      f"{_u0} | {_u1} | {_ul0}")
    # core watch 2026-11-19, the improvement run: a new entry a day restated the same silence and the same open decision; `needs-em`
    # printed 7 entries, 28 lines, for what EM is asked. Each open item is printed once, with the entry it was first written in.
    _oi = getattr(AP, "open_items", None)
    _oe = [("2026-11-18 08:40 CST (14:40 UTC) · still", ["Yours, the line's cost: PC SILENT: line-status last written 2026-11-14 16:08 CST (88.2 h at 08:18 CST)",
                                                        "Yours, a decision, still open: start the cloud builders again?", "Nothing to decide, done"]),
           ("2026-11-17 08:50 CST (14:50 UTC) · could", ["Yours, the line's cost: PC SILENT: line-status last written 2026-11-14 16:08 CST (64.3 h at 08:21 CST)",
                                                        "Yours, a decision: start the cloud builders again?"]),
           ("2026-11-15 08:35 CST (14:35 UTC) · silent", ["Yours, the line's cost: PC SILENT: line-status last written 2026-11-14 16:08 CST (16.2 h)"])]
    _oi0 = _oi(_oe) if _oi else []
    _ol0 = _ul(_oe) if _ul else []
    t("each open item of the core's needs-em entries is named once, with the entry it was first written in, however many entries restate it (autopilot.open_items; build.py needs-em)",
      [(n, h[:16]) for _, h, n in _oi0] == [(3, "2026-11-15 08:35"), (2, "2026-11-17 08:50")] and _oi0[0][0].endswith("(88.2 h at 08:18 CST)")
      and _ol0[1] == "OPEN FOR EM: 2 items, each once" and _ol0[2].endswith("(first written 2026-11-15 08:35 CST; restated in 3 entries)")
      and "Nothing to decide, done" not in "\n".join(_ol0) and "    - Nothing to decide, done" in _ul(_oe, full=True),
      f"{_oi0} | {_ol0}")
    # core watch 2026-11-16, the improvement run: the PC silent 40 h with round 37 and 14 lane rounds waiting for main; round 36's
    # core merge had been refused twice on the PC before the cloud saw why. The next merge run is rehearsed in the cloud first.
    import importlib as _il, tempfile as _tfr, subprocess as _spr, os
    try: _RH = _il.import_module("toolkit.rehearse")
    except ImportError: _RH = None
    _rh = None
    if _RH is not None:
        with _tfr.TemporaryDirectory() as _gr:
            _Gr = lambda *a: _spr.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *a], cwd=_gr, capture_output=True, text=True)
            _wr = lambda p, s: (os.makedirs(os.path.dirname(os.path.join(_gr, p)), exist_ok=True), open(os.path.join(_gr, p), "w").write(s))
            _Gr("init", "-q", "-b", "main")
            _wr("lib/OWNERS.csv", "path,owner,note\nlib/out/*,*,generated\nlib/core.txt,core,\nlib/x.txt,elec,\nlib/m.txt,mech,\nlib/y.txt,core,\n")
            for _p in ("lib/out/v.json", "lib/core.txt", "lib/x.txt", "lib/m.txt", "lib/y.txt"): _wr(_p, "0\n")
            _Gr("add", "."); _Gr("commit", "-qm", "base")
            _Gr("checkout", "-qb", "core"); _wr("lib/core.txt", "core\n"); _Gr("commit", "-qam", "c")
            _Gr("checkout", "-q", "main"); _Gr("checkout", "-qb", "mech"); _wr("lib/out/v.json", "mech\n"); _wr("lib/m.txt", "m\n"); _Gr("commit", "-qam", "m")
            _Gr("checkout", "-q", "main"); _Gr("checkout", "-qb", "elec"); _wr("lib/x.txt", "elec\n"); _wr("lib/y.txt", "elec\n"); _Gr("commit", "-qam", "e")
            _Gr("checkout", "-q", "main"); _wr("lib/out/v.json", "main\n"); _wr("lib/x.txt", "main\n"); _Gr("commit", "-qam", "main moved")
            _ow = lambda ln, b, h, here: not [f for f in _spr.run(["git", "diff", "--name-only", f"{b}...{h}"], cwd=here, capture_output=True, text=True).stdout.split()
                                              if f in ("lib/core.txt", "lib/y.txt") and ln != "core"]
            _rows, _st = _RH.rehearse(_gr, "main", ["core", "mech", "elec"], owners=_ow, selftest=False)
            _rh = [(r["ref"], r["merge"], r["generated"], r["conflicts"], r["owners"]) for r in _rows]
            _rl = _RH.lines(_rows, _st)
            _left = _spr.run(["git", "worktree", "list"], cwd=_gr, capture_output=True, text=True).stdout.strip().count("\n")
    t("the library's next merges are rehearsed in a scratch worktree: core merged, a lane's generated conflict takes main's copy, a real conflict and a file outside the lane refuse it, and the worktree is gone after (toolkit/rehearse; build.py rehearse)",
      _rh == [("core", "merged", [], [], True), ("mech", "merged", ["lib/out/v.json"], [], True), ("elec", "conflict", [], ["lib/x.txt"], False)]
      and _rl[0].startswith("REHEARSAL REFUSED") and "CONFLICT: lib/x.txt" in _rl[3] and _left == 0
      and _RH.generated("lib/out/v.json", "path,owner,note\nlib/out/*,*,g\n") and not _RH.generated("lib/x.txt", "path,owner,note\nlib/out/*,*,g\n"),
      f"{_rh} | {_rl if _RH else 'no toolkit.rehearse'}")
    _src_run = _insp.getsource(AP.run)
    t("a start that failed or was stopped records nothing of what it saw on main, so the next start still finds the change; only a round that ran to its end does (autopilot.record_inputs)",
      not _ri_fail and _iw_fail is None and not _ri_stop and _iw_stop is None and _ri_done and _iw_done
      and "record_inputs(lane, fp, result)" in _src_run and '.inputs"' not in _src_run, f"{_ri_fail} {_iw_fail} | {_ri_stop} {_iw_stop} | {_ri_done} {_iw_done}")
    t("another lane's start ends the stuck task and starts it again, and never touches its own (autopilot.unstick)",
      _self == [] and _cmds == ["schtasks /End /TN complexes\\elec", "schtasks /Run /TN complexes\\elec"] and "started it again" in _log, f"{_self} {_cmds}")
    # core watch 2026-11-08 (round 19 return, section 3): cloud-pneu's nine elements waited 29 h behind lanes queued after them
    import datetime as _dtm
    _ts = lambda d, hm: _dtm.datetime(2026, 11, d, int(hm[:2]), int(hm[3:])).timestamp()
    _mo = AP.merge_order([("origin/core (merge core)", None), ("mech at r45's head", _ts(8, "13:48")), ("elec at r17's head", _ts(8, "14:14")),
                          ("pneu at r49's head", _ts(8, "13:31")), ("origin/cloud-pneu as lane pneu", _ts(7, "14:26")), ("origin/review", _ts(8, "11:48"))])
    _mo2 = AP.merge_order([("mech at r1's head", None), ("elec at r1's head", _ts(8, "10:00")), ("pneu at r1's head", _ts(8, "10:00"))])
    t("the library's run list: core first, then the longest waiting, so a cloud builder cut by queued lanes comes in next run; review, doc-only, takes none of the four places (autopilot.merge_order; round 22 return 4.4)",
      _mo == ["origin/core (merge core)", "origin/cloud-pneu as lane pneu", "origin/review", "pneu at r49's head", "mech at r45's head"]
      and _mo2 == ["elec at r1's head", "pneu at r1's head", "mech at r1's head"] and "merge_order(" in _insp.getsource(AP.merge_list), f"{_mo} | {_mo2}")
    # round 20 return, difference 2: a stopped run's merge, a staged file its build then rewrote; `merge --abort` refused ("not
    # uptodate"), the stash cleaned the tree, MERGE_HEAD stayed, and the next run's first merge refused
    with _tf.TemporaryDirectory() as _d, _tf.TemporaryDirectory() as _g:
        _st, _rn = AP.state, AP.runs
        AP.state = lambda *p: os.path.join(_d, *p)
        AP.runs = lambda: [{"lane": "library", "started": "2026-11-08 12:52", "result": "stopped at the 150 min limit; left uncommitted changes"}]
        try:
            _G = lambda *a: _run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *a], cwd=_g, capture_output=True)
            _G("init", "-q", "-b", "main"); os.makedirs(os.path.join(_g, "lib"))
            _f = os.path.join(_g, "lib", "catalogue.csv")
            open(_f, "w").write("a\n"); _G("add", "."); _G("commit", "-qm", "a")
            _G("checkout", "-qb", "cloud-elec"); open(_f, "w").write("b\n"); _G("commit", "-qam", "b")
            _G("checkout", "-q", "main"); open(os.path.join(_g, "lib", "g"), "w").write("c\n"); _G("add", "."); _G("commit", "-qm", "c")
            _G("merge", "--no-ff", "--no-commit", "cloud-elec"); open(_f, "w").write("rebuilt\n")    # the build rewrote it
            _old = AP.time.time() - 7200
            for _p in (_f, os.path.join(_g, "lib", "g")): os.utime(_p, (_old, _old))
            import io as _io, contextlib as _cl
            with _cl.redirect_stdout(_io.StringIO()) as _hout:      # round 22 return 4.3: the planted put-aside prints nothing in a real log
                _hl = AP.heal("library", _g)
            _mh = os.path.exists(os.path.join(_g, ".git", "MERGE_HEAD"))
            _mr = _G("merge", "--no-ff", "--no-commit", "cloud-elec").returncode                   # the next run's first merge
        finally: AP.state, AP.runs = _st, _rn
    t("a stopped run's half-done merge is put aside whole: no MERGE_HEAD left behind, so the next run's merge starts (autopilot.heal)",
      _hl is True and not _mh and _mr == 0 and "put aside the leftovers" in _hout.getvalue(), f"{_hl} {_mh} {_mr}")
    # core watch 2026-11-11 (elec's 19:27 run of 2026-11-10): `git merge main`, a fast-forward over the renormalize, wrote every
    # file but a gate log a stale process held open; HEAD and the index stayed behind, and every later run would skip or stash
    def _ffcase(lane_work):
        with _tf.TemporaryDirectory() as _d, _tf.TemporaryDirectory() as _g:
            _st, _rn = AP.state, AP.runs
            AP.state = lambda *p: os.path.join(_d, *p)
            AP.runs = lambda: [{"lane": "elec", "started": "2026-11-10 19:27", "result": "exit 0; left uncommitted changes"}]
            try:
                _G = lambda *a: _run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "-c", "core.autocrlf=false", *a], cwd=_g, capture_output=True)
                _G("init", "-q", "-b", "main"); os.makedirs(os.path.join(_g, "lib", "gate"))
                _held, _sp = os.path.join(_g, "lib", "gate", "run.txt"), os.path.join(_g, "lib", "spec.md")
                open(_held, "wb").write(b"gate\r\nlog\r\n"); open(_sp, "w").write("v1\n"); _G("add", "."); _G("commit", "-qm", "a")
                _G("branch", "elec")
                open(os.path.join(_g, "lib", ".gitattributes"), "w").write("* text=auto eol=lf\n")
                open(_sp, "w").write("v2\n"); open(os.path.join(_g, "lib", "new.md"), "w").write("n\n")
                _G("add", "--renormalize", "lib"); _G("add", "."); _G("commit", "-qm", "renormalize")
                _mainsha = _G("rev-parse", "HEAD").stdout.strip()
                _G("checkout", "-q", "elec"); _G("checkout", "-q", "main", "--", "lib/spec.md", "lib/new.md", "lib/.gitattributes")
                _G("reset", "-q")                                     # the tree is main's, HEAD and the index are not
                open(_held, "wb").write(b"gate\r\nlog\r\n")           # the one file the merge could not write: still the old bytes
                if lane_work: open(_sp, "w").write("the lane's own change\n")
                _old = AP.time.time() - 7200
                for _r, _ds, _fs in os.walk(os.path.join(_g, "lib")):
                    for _x in _fs: os.utime(os.path.join(_r, _x), (_old, _old))
                _mt = os.path.getmtime(_held)
                import io as _io2, contextlib as _cl2
                with _cl2.redirect_stdout(_io2.StringIO()) as _o: _h = AP.heal("elec", _g)
                _at = _G("rev-parse", "HEAD").stdout.strip() == _mainsha
                _sl = _G("stash", "list").stdout.decode().strip()
                return _h, _at, os.path.getmtime(_held) == _mt, _sl, _o.getvalue()
            finally: AP.state, AP.runs = _st, _rn
    _ff1, _ff2 = _ffcase(False), _ffcase(True)
    t("a fast-forward merge that wrote every file but one held open is finished in git's records, no file written, nothing stashed; a folder holding the lane's own change is put aside as before (autopilot.finish_ff, heal)",
      _ff1[0] is True and _ff1[1] and _ff1[2] and _ff1[3] == "" and "finished the fast-forward" in _ff1[4]
      and not _ff2[1] and "finished the fast-forward" not in _ff2[4] and _ff2[3] != "", f"{_ff1} | {_ff2}")
    # round 10 f: a safety-function element holds at station 7 until EM's own line
    cs = {"relay-safety-2ch-2no1nc": {"version": "1.0"}}
    rows = LN.element("relay-safety-2ch-2no1nc", findings=[], cat=cs, tags=set(), reviews="relay-safety-2ch-2no1nc 1.0: PASS", safety={"relay-safety-2ch-2no1nc"}, spec="# relay-safety-2ch-2no1nc v1.0\n")
    ok1 = any("Safety sign-off" in w for w in rows[6][4])
    rows = LN.element("relay-safety-2ch-2no1nc", findings=[], cat=cs, tags=set(), reviews="relay-safety-2ch-2no1nc 1.0: PASS", safety={"relay-safety-2ch-2no1nc"}, spec="# relay-safety-2ch-2no1nc v1.0\nSafety sign-off: 1.0 · EM 2026-11-05\n")
    t("LINE holds a safety relay with the reviewer's PASS and no EM 'Safety sign-off' at station 7", ok1 and not any("Safety sign-off" in w for w in rows[6][4]) and "relay-safety-2ch-2no1nc" in LN._safety(), str(rows[6][4]))
    # request pneu-1: the pneumatic contract (toolkit/pneu.py) and the PNE checks (toolkit/v_pneu.py), one PASS and one fault per rule
    from . import pneu as PN, v_pneu as PV
    tb = lambda od: dict(unit=f"tube-{od}", gender="male", role="work"); pi = lambda od: dict(unit=f"tube-{od}", gender="female", role="work")
    th = lambda u, g, role="work", **k: dict(unit=u, gender=g, role=role, **k)
    t("PNE-001 passes a 1/4 in tube in a 1/4 in push-in port", PN.pne001(tb("1/4"), pi("1/4"))[0] == "PASS")
    t("PNE-001 fails a 6 mm tube in a 1/4 in port, and a 1/4 in tube in a 6 mm port (look-alikes)", PN.pne001(tb("6mm"), pi("1/4"))[0] == "FAIL" and PN.pne001(tb("1/4"), pi("6mm"))[0] == "FAIL" and "look-alikes" in PN.pne001(tb("6mm"), pi("1/4"))[1])
    t("PNE-002 passes an NPT 1/8 male in an NPT 1/8 port", PN.pne002(th("NPT1/8", "male"), th("NPT1/8", "female"))[0] == "PASS")
    r = [PN.pne002(th(a, "male"), th(b, "female"))[0] for a, b in (("NPT1/8", "G1/8"), ("NPT1/4", "NPT1/8"), ("NPT1/4", "G1/8"))]
    t("PNE-002 fails NPT 1/8 in G1/8, NPT 1/4 in NPT 1/8, and the gauge's NPT 1/4 in the FRL's G1/8 gauge port as on file", r == ["FAIL"] * 3, str(r))
    t("PNE-002 fails two male threads", PN.pne002(th("NPT1/8", "male"), th("NPT1/8", "male"))[0] == "FAIL")
    st = [PN.mate(th("NPT1/8", "male"), None)["state"], PN.mate(th("NPT1/8", "male"), th("NPT1/8", "female"), sealant=True)["state"],
          PN.mate(th("NPT1/8", "male"), th("NPT1/8", "female"))["state"], PN.mate(th("G1/8", "male"), th("G1/8", "female"), face_seal=True)["state"],
          PN.mate(th("NPT1/8", "male", role="plug"), th("NPT1/8", "female"), sealant=True)["state"], PN.mate(dict(tb("1/4"), condition="collet-open"), pi("1/4"))["state"],
          PN.mate(dict(tb("1/4"), condition="angled-cut"), pi("1/4"))["state"], PN.mate(tb("1/4"), th("NPT1/4", "female"))["state"]]
    t("pneu.mate: open, sealed, leaking (NPT, no sealant), sealed (G, face seal), blocked (plug), pulled-out, leaking (angled cut), mismatch (tube to thread)",
      st == ["open", "sealed", "leaking", "sealed", "blocked", "pulled-out", "leaking", "mismatch"], str(st))
    def circ(**k):
        C = dict(ports={}, joints=[], rating={}, supply=None, p_set=None, limit={}, dump=None, source=None); C.update(k); return C
    C = circ(ports={"v.port-1": th("NPT1/8", "female", "supply"), "f.port-b": th("NPT1/8", "male")}, joints=[dict(a="f.port-b", b="v.port-1", row=1)])
    r = PV.joints(C); t("PNE-002 fails an NPT joint made without sealant (nothing declared)", r and r[0][0] == "FAIL" and "leaking" in r[0][3], str(r))
    C["joints"][0]["condition"] = "no-sealant"; r = PV.joints(C)
    t("PNE-002 REVIEWs the same joint when its leak is a declared fault (a training fault)", r and r[0][0] == "REVIEW", str(r))
    p100 = PN.psig(100.0)
    r = PV.pressures(circ(rating={"cyl": dict(p_max=PN.psig(145.0)), "part": dict(p_max=PN.psig(90.0)), "unk": dict(p_max=None)}))
    got = {w: s_ for s_, _, w, _ in r}
    t("PNE-003 passes a 145 psi cylinder, fails a 90 psi part on the 100 psig supply, REVIEWs a rating NOT ON FILE", got == {"cyl": "PASS", "part": "FAIL", "unk": "REVIEW"}, str(got))
    r = PV.pressures(circ(rating={"part": dict(p_max=PN.psig(90.0))}, limit={"part": PN.psig(85.0)}))
    t("PNE-003 passes the 90 psi part behind an 85 psig relief valve", r and r[0][0] == "PASS", str(r))
    C = circ(ports={"vb.port-3": th("NPT1/8", "female", "exhaust"), "vb.port-5": th("NPT1/8", "female", "exhaust"), "s1.port-1": th("NPT1/8", "male", "silencer")},
             joints=[dict(a="s1.port-1", b="vb.port-3", row=1, sealant=True)])
    r = PV.open_ports(C); got = sorted((s_, x, w) for s_, x, w, _ in r)
    t("PNE-004 / PNE-005: the bank's port 3 silenced passes, port 5 left open fails both", got == [("FAIL", "PNE-004", "vb.port-5"), ("FAIL", "PNE-005", "vb.port-5"), ("PASS", "PNE-005", "vb.port-3")], str(got))
    r = [E.coil_voltage(24.0, 24.0, "x")[0], E.coil_voltage(110.0, 24.0, "x")[0]]
    t("PNE-006 (ELR-021): a 24 V coil on psu-24v-2a4 passes, a 110 V coil on it fails", r == ["PASS", "FAIL"], str(r))
    R7 = {"v": dict(p_max=PN.psig(145.0), p_min=PN.psig(30.0))}
    r = [[x[0] for x in PV.pressures(circ(rating=R7, p_set=PN.psig(s_))) if x[1] == "PNE-007"] for s_ in (80.0, 20.0, 90.0)]
    t("PNE-007: set 80 psig with a 30 psig minimum passes; 20 psig fails; 90 psig (above P_WORK_MAX) is EM's (REVIEW)", r == [["PASS"], ["FAIL"], ["PASS", "REVIEW"]], str(r))
    base = dict(ports={"drop.out": th("NPT1/4", "male", "supply"), "dv.port-1": th("NPT1/4", "female", "supply")}, joints=[dict(a="drop.out", b="dv.port-1", row=1)], source="drop.out")
    r = [PV.isolation(circ(**base, dump="dv", rating={"dv": dict(lockable="yes")}))[0][0], PV.isolation(circ(**base))[0][0], PV.isolation(circ(**base, dump="dv", rating={"dv": dict(lockable="no")}))[0][0]]
    t("PNE-008: a lockable dump valve first after the drop passes; none fails; one that takes no padlock fails", r == ["PASS", "FAIL", "FAIL"], str(r))
    r = [[x[0] for x in PV.pressures(circ(rating={"g": dict(span=PN.psig(s_))})) if x[1] == "PNE-009"][0] for s_ in (160.0, 100.0, 60.0)]
    t("PNE-009 on the 100 psig supply: a 0-160 psig gauge passes, 0-100 REVIEW (at full scale), 0-60 fails (pegs)", r == ["PASS", "REVIEW", "FAIL"], str(r))
    d_ = tempfile.mkdtemp()
    try:
        open(os.path.join(d_, "air.csv"), "w", encoding="utf-8").write("from,to,params,note\nfrl.port-2,vb.port-1,sealant=yes,planted\n")
        open(os.path.join(d_, "air-circuit.csv"), "w", encoding="utf-8").write("key,tag,value,unit,note\nset,,80,psig,planted\n")
        P = Prims(); P.pivot("frl.port-2", "port", (0, 0, 0), unit="NPT1/8", gender="male", role="work"); P.pivot("vb.port-1", "port", (0, 0, 0), unit="NPT1/8", gender="female", role="supply")
        P.pivot("vb.port-3", "port", (0, 0, 0), unit="NPT1/8", gender="female", role="exhaust"); P.pivot("vb.coil-14", "fixed", (0, 0, 0))
        R_ = {"frl": {"p_max": dict(value="150", unit="psig")}, "vb": {"p_max": dict(value="10", unit="bar"), "p_min": dict(value="2", unit="bar")}}
        C = PV.circuit(d_, P, lambda P_, tag: (tag, R_.get(tag, {}))); r = PV.check(C); got = {(s_, x, w.split()[-1]) for s_, x, w, _ in r}
        t("v_pneu reads air.csv and air-circuit.csv: the joint passes, the unsilenced port 3 fails, the units convert (10 bar, 80 psig)",
          C and set(C["ports"]) == {"frl.port-2", "vb.port-1", "vb.port-3"} and abs(C["p_set"] - PN.psig(80.0)) < 1e-9 and abs(C["rating"]["vb"]["p_max"] - 1000.0) < 1e-9
          and ("PASS", "PNE-002", "vb.port-1") in got and ("FAIL", "PNE-005", "vb.port-3") in got and ("FAIL", "PNE-008", "circuit") in got, str(sorted(got)))
    finally:
        import shutil; shutil.rmtree(d_, ignore_errors=True)
    t("PNE-* findings name the elements they judged (station 5 / 6 hold them)", "PNE-" in VA.JUDGED and LN.station_of("PNE-003") == 5 and LN.station_of("PNE-001") == 6)
    # request pneu-8: the hydraulic contract (toolkit/hyd.py) and the HYD checks (toolkit/v_hyd.py), the lane's planted cases
    from . import hyd as HY, v_hyd as HV
    hp = lambda u, g, role="work": dict(unit=u, gender=g, role=role)
    r = [HY.hyd001(hp("hyd-port-8", "male"), hp("hyd-port-6", "female"))[0], HY.hyd001(hp("hyd-port-8", "male"), hp("hyd-port-8", "female"))[0],
         HY.hyd001(hp("hyd-port", "male"), hp("hyd-port-8", "female"))[0], HY.hyd001(hp("hyd-port-8", "female"), hp("hyd-port-8", "female"))[0]]
    t("HYD-001: a -8 port joined to a -6 fails, to a -8 passes, an open size is REVIEW, two females fail", r == ["FAIL", "PASS", "REVIEW", "FAIL"], str(r))
    def hc(**k):
        C = dict(ports={}, joints=[], rating={}, flow=None, source=None, reliefs=[("hpu", 160.0)], tank=None, cylinders={}, hold={}); C.update(k); return C
    C = hc(ports={"cyl.port-cap": hp("hyd-port-8", "female"), "cyl.port-rod": hp("hyd-port-8", "female"), "h1.end-1": hp("hyd-port-8", "male")},
           joints=[dict(a="h1.end-1", b="cyl.port-cap", row=1, line="A")])
    r = sorted((x[0], x[2]) for x in HV.open_ports(C))
    t("HYD-002: hyd-cylinder-da-40's port-rod left open fails; the joined cap port and a declared tank return pass", r == [("FAIL", "cyl.port-rod")]
      and not HV.open_ports(dict(C, joints=C["joints"] + [dict(a="cyl.port-rod", b=None, tank=True, row=2)])), str(r))
    r = {w: s_ for s_, x, w, _ in HV.pressures(hc(rating={"weak": dict(p_max=100.0), "hold-down": dict(p_max=160.0), "unk": dict(p_max=None)})) if x == "HYD-003"}
    t("HYD-003 on the press's 160 bar circuit: p_max 100 fails, hold-down at 160 passes (≥), NOT ON FILE is REVIEW", r == {"weak": "FAIL", "hold-down": "PASS", "unk": "REVIEW"}, str(r))
    C = hc(ports={"flt.port-1": hp("hyd-port-12", "female")}, joints=[dict(a="v.T", b="flt.port-1", row=1, line="T")], rating={"flt": dict(p_max=16.0)})
    r = [x[0] for x in HV.pressures(C) if x[1] == "HYD-003"]
    t("HYD-003 judges an element whose every port is on the tank line at the T line's pressure (a 16 bar return filter passes at 10 bar)", r == ["PASS"], str(r))
    r = [x[0] for x in HV.hoses(hc(joints=[dict(a="hpu.P", b="v.P", row=1, line="P", hose="h1")], rating={"h1": dict(p_max=140.0)})) if x[1] == "HYD-004"]
    r2 = [x[0] for x in HV.hoses(hc(joints=[dict(a="hpu.P", b="v.P", row=1, line="P", hose="h1")], rating={"h1": dict(p_max=210.0)})) if x[1] == "HYD-004"]
    t("HYD-004: a hose rated 140 bar on the 160 bar P line fails; 210 passes", r == ["FAIL"] and r2 == ["PASS"], f"{r} {r2}")
    r = [(x[0], x[3].split(" is ")[1][:8]) for b in (6.4, 12.7) for x in HV.hoses(hc(flow=22.0, joints=[dict(a="hpu.P", b="v.P", row=1, line="P", bore=b)])) if x[1] == "HYD-005"]
    t("HYD-005: 22 l/min through a 6.4 mm bore is 11.4 m/s (REVIEW above 6), through 12.7 mm 2.9 m/s (PASS)", r == [("REVIEW", "11.4 m/s"), ("PASS", "2.9 m/s,")], str(r))
    r = [[x[0] for x in HV.pressures(hc(rating={"g": dict(span=s_)})) if x[1] == "HYD-006"][0] for s_ in (250.0, 160.0, 100.0)]
    t("HYD-006 at 160 bar: a 0-250 bar gauge passes (64 %), 0-160 REVIEW (100 %), 0-100 fails (pegs)", r == ["PASS", "REVIEW", "FAIL"], str(r))
    r = [HV.reliefs(hc(source="hpu", reliefs=R_, rating={"hpu": dict(p_max=200.0)}))[0][0] for R_ in ([("hpu", 160.0)], [("hpu", 160.0), ("rv2", 140.0)], [], [("hpu", 250.0)])]
    t("HYD-007: one relief at 160 under a 200 bar source passes; two reliefs on one source, none, and one set above the source's rating fail", r == ["PASS", "FAIL", "FAIL", "FAIL"], str(r))
    r = [HV.holding(hc(cylinders={"cyl": True}, hold=h_))[0][0] for h_ in ({}, {"cyl": ("cbv", False)}, {"cyl": ("cbv", True)})] + [len(HV.holding(hc(cylinders={"cyl": False})))]
    t("HYD-008: the press's vertical cylinder with no hold is REVIEW, a counterbalance named without EM's sign-off REVIEW, signed PASS; a horizontal one is not judged",
      r == ["REVIEW", "REVIEW", "PASS", 0], str(r))
    d_ = tempfile.mkdtemp()
    try:
        open(os.path.join(d_, "hyd.csv"), "w", encoding="utf-8").write("from,to,params,note\nhpu.port-p,cyl.port-cap,line=A;hose=h1;bore=12.7,planted\n")
        open(os.path.join(d_, "hyd-circuit.csv"), "w", encoding="utf-8").write(
            "key,tag,value,unit,note\nsource,hpu,22,l/min,planted\nrelief,hpu,16,MPa,planted\nhold,cbv,,,for cyl; planted, no sign-off\n")
        P = Prims(); P.pivot("hpu.port-p", "port", (0, 0, 0), unit="hyd-port-8", gender="male", role="supply")
        P.pivot("cyl.port-cap", "port", (0, 0, 0), unit="hyd-port-8", gender="female", role="work"); P.pivot("cyl.port-rod", "port", (0, 0, 0), unit="hyd-port", gender="female", role="work")
        P.pivot("cyl.rod", "translate", (0, 0, 0), axis=(0, 0, -1), range=(0, 300)); P.pivot("x.port-1", "port", (0, 0, 0), unit="NPT1/8", gender="female")
        R_ = {"hpu": {"p_max": dict(value="200", unit="bar")}, "cyl": {"p_max": dict(value="160", unit="bar")}, "h1": {"p_max": dict(value="2900", unit="psi")}}
        C = HV.circuit(d_, P, lambda P_, tag: (tag, R_.get(tag, {}))); got = {(s_, x, w.split()[-1]) for s_, x, w, _ in HV.check(C)}
        t("v_hyd reads hyd.csv and hyd-circuit.csv: 16 MPa is 160 bar, 2900 psi converts, the -8 joint passes, the rod port left open fails, "
          "the rod axis -z makes the cylinder vertical and its counterbalance waits on EM; an air port is not a hydraulic one",
          C and set(C["ports"]) == {"hpu.port-p", "cyl.port-cap", "cyl.port-rod"} and C["reliefs"] == [("hpu", 160.0)] and abs(C["rating"]["h1"]["p_max"] - 199.948) < 0.01
          and C["cylinders"] == {"cyl": True} and ("PASS", "HYD-001", "cyl.port-cap") in got and ("FAIL", "HYD-002", "cyl.port-rod") in got
          and ("PASS", "HYD-003", "cyl") in got and ("PASS", "HYD-005", "cyl.port-cap") in got and ("REVIEW", "HYD-008", "cyl") in got and ("PASS", "HYD-007", "hpu") in got, str(sorted(got)))
        t("HYD-* on an assembly with no hyd.csv: nothing", HV.circuit(tempfile.gettempdir() + "/no-such-assembly-x", P) is None)
    finally:
        import shutil; shutil.rmtree(d_, ignore_errors=True)
    t("HYD-* findings name the elements they judged; joints hold at station 6, ratings and the hold at 5", "HYD-" in VA.JUDGED and LN.station_of("HYD-001") == 6
      and LN.station_of("HYD-002") == 6 and LN.station_of("HYD-003") == 5 and LN.station_of("HYD-008") == 5 and all(f"HYD-00{i}" in VA.rules.RULES for i in range(1, 9)))
    # EM 2026-11-05 rulings (the Electrical CAD assets chat)
    r = VA.vendor_hits(dict(spec="cage 5.1 x 10.4 (AutomationDirect page); rated 1.5 A (UL 1.5 A)"), "Part number: 7641K21 (page verified)\n")
    t("DOC-006 finds a vendor name and an approval mark in a spec", r and "AutomationDirect" in r[0] and "UL" in r[0], str(r))
    r = VA.vendor_hits(dict(BASELINE="per the 7641K21 drawing"), "Part number: 7641K21 (page verified)\n")
    t("DOC-006 finds the element's own part number in its BASELINE", r and "7641K21" in r[0], str(r))
    r = VA.vendor_hits(dict(spec="cage 5.1 x 10.4 (maker's datasheet, references/measure.md p. 1); built to UL 508A and CSA C22.2 No. 14; PVC UL 94 V-0"), "Part number: 7641K21\n")
    t("DOC-006 passes \"maker's datasheet\" and standards cited by number (UL 508A, UL 94 V-0, CSA C22.2)", r == [], str(r))
    # ESCAPE panel/r15 2 (core watch 2026-11-12): pnl-press-hydraulic's first AutoCAD gate ran out/<id>.lsp as a merge had left it (v0.4's,
    # no q1 solids) while assembly.py said 0.5, and lock.py recorded "0.5 autocad PASS": nothing tied an assembly's gate to the LISP it ran
    import tempfile, shutil as _sh
    _ag = getattr(VA, "assembly_gate", lambda a, r=None: [])                       # before the fix: no rule, the stale PASS stood
    _cen = lambda src: {k: re.findall(r'\((?:BX|CY|UB) "([^"]+)"', src).count(k) for k in set(re.findall(r'\((?:BX|CY|UB) "([^"]+)"', src))}   # acad-gate.py's census
    _r = tempfile.mkdtemp(); _a = os.path.join(_r, "assemblies", "zq-asm")
    for _s in ("out", "gate"): os.makedirs(os.path.join(_a, _s))
    with open(os.path.join(_a, "assembly.py"), "w") as _f: _f.write('ID = "zq-asm"; VERSION = "0.5"\n')
    _l04 = ';; zq-asm. Generated. Millimetres. APPLOAD, then ZQ.\n  (BX "node-k1_M-ZINC" (list 0 0 0) (list 1 1 0) 1)\n'
    _l05 = _l04 + '  (setq e1 (BX "node-q1_M-ZINC" (list 0 0 0) (list 1 1 0) 1))\n  (CY "node-q1_M-CU" (list 0 0 0) (list 0 0 1) 1)\n'
    def _gate(lisp, extra=None):
        with open(os.path.join(_a, "gate", "zq-asm-acad.json"), "w") as _f: json.dump({"id": "zq-asm", "date": "2026-11-12", "pass": True, "lisp_per_layer": _cen(lisp), **(extra or {})}, _f)
    open(os.path.join(_a, "out", "zq-asm.lsp"), "w").write(_l05); _gate(_l04); _stale = _ag("zq-asm", _r)
    _gate(_l05); _same = _ag("zq-asm", _r)
    _gate(_l05, dict(version="0.4")); _older = _ag("zq-asm", _r)
    open(os.path.join(_a, "out", "zq-asm.lsp"), "w").write(_l05.replace("zq-asm.", "zq-asm v0.4.", 1)); _gate(_l05); _head = _ag("zq-asm", _r)
    _sh.rmtree(_r, ignore_errors=True)
    t("ESCAPE panel/r15 2: GATE-010 holds an assembly whose AutoCAD PASS ran another LISP than out/<id>.lsp (census v0.4's, or a version that is not assembly.py's) and passes one that ran it",
      _stale and _stale[0][0] == "REVIEW" and "node-q1" in _stale[0][3] and _same and _same[0][0] == "PASS" and _older and _older[0][0] == "REVIEW" and "v0.4" in _older[0][3]
      and _head and _head[0][0] == "REVIEW" and "says v0.4" in _head[0][3] and "GATE-010" in VA.rules.RULES, str((_stale, _same, _older, _head)))
    # ESCAPE io-block-m12-8di8do-1.8 1 (review elec-r31; core watch 2026-11-12): vendors.csv's LioN-X pattern was case-sensitive and DOC-006
    # never read element.py's COMMAND, so `COMMAND = "LIONX"` shipped in the LISP and "AutoLISP command `LIONX`" passed in the spec
    r = VA.vendor_hits(dict(COMMAND="LIONX", spec="AutoLISP command `LIONX` draws the block"))
    _ok = VA.vendor_hits(dict(COMMAND="IOBLOCK8", spec="a million x 2 (millionx); AutoLISP command `IOBLOCK8`"))
    t("ESCAPE io-block-m12-8di8do-1.8 1: DOC-006 finds a product family in capitals in the LISP command and the spec (LIONX), and not in a word",
      len(r) == 2 and all("LioN-X" in x for x in r) and r[0].startswith("COMMAND") and _ok == [], str((r, _ok)))
    # escape 21 (mech r15:1): DOC-006 read only the element's own part numbers; '440R' (relay-safety-2ch-2no1nc's 440R-S13R2) passed in a host's spec and bom notes
    def _v6(texts, src="", others=None):
        try: return VA.vendor_hits(texts, src, others=others)
        except TypeError as e: return [f"no others: {e}"]
    sib = {"440R-S13R2": "relay-safety-2ch-2no1nc", "440R": "relay-safety-2ch-2no1nc", "CWB9-11-30C03": "contactor-9a-1no1nc", "CWB9": "contactor-9a-1no1nc"}
    r = _v6(dict(spec="estop-1 feeds the 440R (its monitored output is X2 A)"), "Part number: OWN-PLANNED\n", sib)
    t("DOC-006 finds a carried element's part-number prefix in a host's spec (440R, relay-safety-2ch-2no1nc's)", r and "440R (relay-safety-2ch-2no1nc's)" in r[0], str(r))
    r = _v6(dict(bom="E-stop dual channel to the panel's p-x3 (440R S12 / S22)\nin series into the safety relay (relay-safety-2ch-2no1nc)"), "", sib)
    t("DOC-006 reads bom.csv notes as text that leaves the brief", len(r) == 1 and r[0].startswith("bom:") and "440R" in r[0], str(r))
    r = _v6(dict(spec="the station's E-stop wires to relay-safety-2ch-2no1nc; worktop 1200 high; IRB 1200-7 class"), "Part number: RW27-2D3-U010\n", sib)
    t("DOC-006 passes an element id (relay-safety-2ch-2no1nc: the match is case-sensitive) and an all-digit head ('1200' is no prefix)",
      r == [] and VA.pn_prefix("1200-7") == "" and VA.pn_prefix("440R-S13R2") == "440R" and VA.pn_prefix("OWN-PLANNED") == "", str(r))
    r = _v6(dict(spec="trips the RW27 (maker's datasheet)"), "Part number: RW27-2D3-U010 (page verified)\n", sib)
    t("DOC-006 finds the element's own family prefix (RW27 of RW27-2D3-U010)", r and "RW27" in r[0], str(r))
    sp6 = "# x v1.0\n\nhandle swing 90° (**Assumption (C)**)\ndecal position NOT ON FILE (C)\n## History\n| 1.0 | first |\n"
    r = VA.doc005(sp6); t("DOC-005 passes a class C Assumption and a class C NOT ON FILE alone (the reviewer's)", r and r[0] == "PASS", str(r))
    r = VA.doc005("# x v1.0\n\n## History\n| 1.0 | first |\n", ratings=[dict(property="load_i", value="0.15", status="assumption", source="own design")])
    t("DOC-005 counts a ratings.csv row whose status is 'assumption' (class A: plc0's load_i)", r and r[0] == "REVIEW" and "ratings.csv" in r[2], str(r))
    r = VA.doc005("# x v1.0\n\n## History\n| 1.0 | first |\n", brief="| LED window / M12 socket | NOT ON FILE |\nNOT ON FILE in prose is not a row\n")
    t("DOC-005 counts the brief's NOT ON FILE table rows", r and r[0] == "REVIEW" and "1 NOT ON FILE" in r[2] and "brief" in r[2], str(r))
    # escape group 4 (tag-plate-1.0:1, core watch 2026-11-08): a brief's NOT ON FILE figure built unmarked in the spec is DOC-008, station 1
    _bt = "| feature | mm | source |\n|---|---|---|\n| legend plate W x H x T | 30 x 50 x 1 | pbs spec |\n| institute tag plate W x H x T | NOT ON FILE | position only |\n| pin row offset from the body centre line | 3.2 | NOT ON FILE |\n"
    _st = "# tag-plate v1.0\n\n## Dimensions\n| item | value |\n|---|---|\n| tag | 120 × 60 × 1.5 aluminium |\n| legend | 30 × 50 × 1 |\n| body | 44.8 × 78.4 |\n\n## History\n| 1.0 | first |\n"
    _u = VA.unmarked_nof(_st, _bt)
    t("DOC-008 holds the spec's unmarked figure for the brief's NOT ON FILE feature (tag-plate 1.0: '| tag | 120 × 60 × 1.5 |'), only that row",
      [r_[1][:7] for r_ in _u] == ["| tag |"], str(_u))
    _um = [VA.unmarked_nof(_st.replace("aluminium", "aluminium, Assumption (B): our own size"), _bt), VA.unmarked_nof(_st.replace("aluminium", "aluminium (EM 2026-11-03)"), _bt),
           VA.unmarked_nof(_st, _bt.replace("| NOT ON FILE | position only", "| 120 x 60 x 1.5 | EM 2026-11-03"))]
    t("DOC-008 clears the row once it is marked Assumption, cites EM's dated ruling, or the brief gives the figure", _um == [[], [], []], str(_um))
    t("DOC-008 reads a brief row as NOT ON FILE only when its figure cell says so (a measured figure with 'NOT ON FILE' as its source is not)",
      not any("body" in r_[1] for r_ in _u), str(_u))
    _ul = VA.unmarked_nof("# r v1.0\n| item | value |\n|---|---|\n| coil | 24 V DC, 640 Ω |\n| bobbin size | 12 × 8 |\n## History\n| 1.0 | x |\n",
                          "| coil turns, wire gauge, inductance, bobbin size | NOT ON FILE | none |\n")
    t("DOC-008 matches a brief row that lists parts only by a spec row naming one part fully (relay-ice-cube-2co's coil 24 V DC is on file; its bobbin size is not)",
      [r_[1][:14] for r_ in _ul] == ["| bobbin size "], str(_ul))
    t("DOC-008 is a station 1 hold (identity and sources), the lane's to fix, not EM's", LN.RULE_STATION.get("DOC-008") == 1
      and not LN.waits_on_em((1, "x", "x", False, ["DOC-008 REVIEW: spec.md gives '| tag | 120' for the brief's NOT ON FILE"])), str(LN.RULE_STATION.get("DOC-008")))
    P = Prims(); P.pivot("port-pwr", "port", (0, 0, 0), unit="L"); P.pivot("t-1", "port", (0, 0, 0), unit="screw", gender="none")
    r = VA.port_genders("selftest", P); t("PIN-002 holds a port with no gender (plc0's port-pwr), not a screw clamp declared 'none'", r and r[0][0] == "REVIEW" and "port-pwr" in r[0][2] and "t-1" not in r[0][2], str(r))
    P.pivots["port-pwr"]["gender"] = "male"; r = VA.port_genders("selftest", P); t("PIN-002 passes when every port declares its gender", r and r[0][0] == "PASS", str(r))
    # the behaviour spec (EM 2026-11-09: every electrical and mechanical element gets one; lib/behaviour.md)
    from . import behaviour as BH
    _bp = Prims(); _bp.pivot("t-a1", "port", (0, 0, 0), unit="screw", gender="none"); _bp.pivot("t-a2", "port", (0, 0, 0), unit="screw", gender="none")
    _bp.pivot("t-13", "port", (0, 0, 0), unit="screw", gender="none"); _bp.pivot("t-14", "port", (0, 0, 0), unit="screw", gender="none")
    _bp.pivot("carrier", "translate", (0, 0, 0), axis=(0, 1, 0), range=(0, 3.5)); _bp.pivot("coil", "emissive", (0, 0, 0), range=(0, 1))
    _good = [dict(kind="pin", a="A1", b="t-a1", part="term", when="", value="1.0", unit="N·m", source="spec p. 9", note=""),
             dict(kind="pin", a="A2", b="t-a2", part="term", when="", value="1.0", unit="N·m", source="spec p. 9", note=""),
             dict(kind="pin", a="13", b="t-13", part="term", when="", value="1.0", unit="N·m", source="spec p. 9", note=""),
             dict(kind="pin", a="14", b="t-14", part="term", when="", value="1.0", unit="N·m", source="spec p. 9", note=""),
             dict(kind="load", a="A1", b="A2", part="coil", when="", value="99", unit="ohm", source="spec p. 6", note=""),
             dict(kind="state", a="released", b="", part="magnet", when="default", value="", unit="", source="spec p. 6", note=""),
             dict(kind="state", a="operated", b="", part="magnet", when="coil.V >= 19.2", value="", unit="", source="spec p. 6", note=""),
             dict(kind="state", a="released", b="", part="magnet", when="coil.V <= 9.6", value="", unit="", source="spec p. 6", note=""),
             dict(kind="contact", a="13", b="14", part="aux", when="operated", value="", unit="", source="spec p. 8", note=""),
             dict(kind="pose", a="*", b="", part="", when="operated", value="end", unit="", source="", note="")]
    _r = BH.check("selftest", _bp, _good); t("BEH-010 passes a well-formed spec with every pin on a port node", _r and _r[-1][0] == "PASS" and not any(x[0] != "PASS" for x in _r), str(_r))
    t("BEH-010 is REVIEW while the file is missing (the lanes add them as backlog), at station 5", BH.check("selftest", _bp, None)[0][0] == "REVIEW" and LN.RULE_STATION.get("BEH-010") == 5)
    _bad = [dict(r_) for r_ in _good]; _bad[8]["when"] = "energised"
    t("BEH-010 fails a contact whose when names a state the element doesn't define", any(x[0] == "FAIL" and "energised" in x[3] for x in BH.check("selftest", _bp, _bad)))
    _bad = [dict(r_) for r_ in _good]; _bad[6]["when"] = "lamp.V >= 19.2"
    t("BEH-010 fails a when that measures a part the element has no load or contact for", any(x[0] == "FAIL" and "lamp" in x[3] for x in BH.check("selftest", _bp, _bad)))
    _bad = [dict(r_) for r_ in _good]; _bad[5]["when"] = "coil.V < 9.6"
    t("BEH-010 fails a state machine with no default row", any(x[0] == "FAIL" and "default" in x[3] for x in BH.check("selftest", _bp, _bad)))
    _bad = [dict(r_) for r_ in _good]; _bad[4]["source"] = ""
    t("BEH-010 fails a row with no source", any(x[0] == "FAIL" and "source" in x[3] for x in BH.check("selftest", _bp, _bad)))
    _bad = [dict(r_) for r_ in _good]; _bad[6]["when"] = "__import__('os').system('x')"
    t("BEH-010 refuses anything but states, measurements and comparisons in a when", any(x[0] == "FAIL" and "not allowed" in x[3] for x in BH.check("selftest", _bp, _bad)))
    _bad = [dict(r_) for r_ in _good]; _bad[0]["b"] = "t-99"
    t("BEH-020 holds a pin whose port node the element doesn't build", any(x[1] == "BEH-020" and "A1" in x[2] for x in BH.check("selftest", _bp, _bad)))
    # core round 29 (request panel-4 item 2): a pin row's when may name a form of the element ("form genders=male-open|female-open"):
    # the mark moves to node b in a build of that form; BEH-020 reads each form's nodes in a build of that form
    class _FormEl:
        PARAMS = dict(genders="male-female")
        @staticmethod
        def build(genders="male-female"):
            P_ = Prims(); P_.pivot("t-a1", "port", (0, 0, 0), unit="screw", gender="none"); P_.pivot("t-a2", "port", (0, 0, 0), unit="screw", gender="none")
            for n_ in ("t-13", "t-14"): P_.pivot(n_, "port", (0, 0, 0), unit="screw", gender="none")
            if genders.endswith("-open"): P_.pivot("lead-1", "contact", (0, 0, 0), unit="mm")
            return P_
    _fm = [dict(r_) for r_ in _good] + [dict(kind="pin", a="A1", b="lead-1", part="term", when="form genders=male-open|female-open", value="", unit="", source="x", note="")]
    _fS0, _fS1 = BH.spec("selftest", _fm), BH.spec("selftest", _fm, params=dict(genders="female-open"))
    _fr = BH.check("selftest", _bp, _fm, build_of=_FormEl)
    t("behaviour: a form's pin row moves its mark to the form's node only in a build of that form, and BEH-020 finds the node there",
      _fS0["pins"]["A1"] == "t-a1" and _fS1["pins"]["A1"] == "lead-1" and not any(x[1] == "BEH-020" for x in _fr), f"{_fS0['pins']} {_fS1['pins']} {_fr}")
    _fm2 = [dict(r_) for r_ in _fm]; _fm2[-1]["b"] = "lead-9"
    _fm3 = [dict(r_) for r_ in _fm]; _fm3[-1]["when"] = "genders"
    _fm4 = [dict(r_) for r_ in _fm]; _fm4[-1]["a"] = "B7"
    t("behaviour: BEH-020 holds a form's pin whose node a build of that form lacks; BEH-010 fails a pin row's when that names no form, and a form row for a mark with no default row",
      any(x[1] == "BEH-020" and "form genders=male-open" in x[2] for x in BH.check("selftest", _bp, _fm2, build_of=_FormEl))
      and any(x[0] == "FAIL" and "names a form only" in x[3] for x in BH.check("selftest", _bp, _fm3, build_of=_FormEl))
      and any(x[0] == "FAIL" and "adds none" in x[3] for x in BH.check("selftest", _bp, _fm4, build_of=_FormEl)))
    # request panel-13 2 (core watch 2026-11-13): term-jumper's blades follow `poles` (2 to 12) but its behaviour.csv had pins 1 to 4, so
    # a 2-pole comb showed blades 3 and 4 live and joined to nothing, and a 7-pole comb had no blade 5 to 7. A count adds a pin
    class _CountEl:
        PARAMS = dict(poles=4)
        @staticmethod
        def build(poles=4):
            P_ = Prims()
            for k_ in range(1, int(poles) + 1): P_.pivot(f"p-{k_}", "port", (k_ * 6.0, 0, 0), unit="pin", gender="male")
            return P_
    _cr = [dict(kind="pin", a=str(k_), b=f"p-{k_}", part=f"blade-{k_}", when="" if k_ <= 2 else f"count poles>={k_}", value="not claimed", unit="N·m", source="x", note="")
           for k_ in range(1, 13)] + [dict(kind="contact", a=str(k_), b=str(k_ + 1), part="bar", when="always", value="0.0000207", unit="ohm", source="x", note="") for k_ in range(1, 12)]
    _crc = BH.check("selftest", _CountEl.build(), _cr, build_of=_CountEl)
    _crb = [dict(r_) for r_ in _cr] + [dict(kind="pin", a="5", b="p-5", part="blade-5", when="", value="not claimed", unit="N·m", source="x", note="")]
    _crm = [dict(r_) for r_ in _cr]; _crm[11]["b"] = "p-99"
    class _PP:
        def __init__(self, n_): self.owners = [(0, 0, "jmp-1", "selftest")]; self.pivots = {f"jmp-1.p-{k_}": {} for k_ in range(1, n_ + 1)}
    from . import nets as _NTc
    _cS = BH.spec("selftest", _cr)
    _c2, _c7 = _NTc._counted(_cS, "jmp-1", _PP(2)), _NTc._counted(_cS, "jmp-1", _PP(7))
    t("behaviour: a count pin (`count poles>=k`, request panel-13 2) is a pin only where the build has it: BEH-010/020/040 pass a comb whose"
      " pins 3 to 12 follow poles; the solver gives a 2-pole comb pins 1, 2 and contact 1-2 only, a 7-pole comb pins 1 to 7 and contacts"
      " 1-2 to 6-7; a count row for a mark with a default row FAILs; a count pin a build at its k lacks is BEH-020",
      all(x[0] == "PASS" for x in _crc) and sorted(_c2["pins"]) == ["1", "2"] and [(c_[0], c_[1]) for c_ in _c2["contacts"]] == [("1", "2")]
      and sorted(_c7["pins"], key=int) == [str(k_) for k_ in range(1, 8)] and len(_c7["contacts"]) == 6
      and any(x[0] == "FAIL" and "count row" in x[3] for x in BH.check("selftest", _CountEl.build(), _crb, build_of=_CountEl))
      and any(x[1] == "BEH-020" and "pin 12" in x[2] for x in BH.check("selftest", _CountEl.build(), _crm, build_of=_CountEl)),
      f"{_crc} {sorted(_c2['pins'])} {_c2['contacts'][:3]} {sorted(_c7['pins'])}")
    # request elec-15 and ESCAPE receptacle-m23-1.0 2 (core watch 2026-11-13): receptacle-m23's `kind` (power: 1, 2, 3, PE; signal: 1 to 6)
    # is a word, so neither a form (moves) nor a count (a number) could add marks 4 to 6 in the signal kind or drop PE there; BEH-020
    # read the default kind only and the signal kind's contacts had no rows. `only <param>=<value>[|<value>]`: a pin only in those builds
    class _KindEl:
        PARAMS = dict(kind="power")
        @staticmethod
        def build(kind="power"):
            P_ = Prims()
            for m_ in (["1", "2", "3", "pe"] if kind == "power" else ["1", "2", "3", "4", "5", "6"]): P_.pivot(f"c-{m_}", "contact", (0, 0, 0), unit="m23")
            return P_
    _kr = [dict(kind="pin", a=m_.upper(), b=f"c-{m_}", part=f"contact-{m_}", when="" if m_ in "123" else ("only kind=power" if m_ == "pe" else "only kind=signal"),
                value="not claimed", unit="N·m", source="x", note="") for m_ in ("1", "2", "3", "4", "5", "6", "pe")]
    _krc = BH.check("selftest", _KindEl.build(), _kr, build_of=_KindEl)
    _kS = BH.spec("selftest", _kr); _kSs = BH.spec("selftest", _kr, params=dict(kind="signal")); _kSp = BH.spec("selftest", _kr, params=dict(kind="power"))
    class _KP:
        def __init__(self, k_): self.owners = [(0, 0, "x1", "selftest")]; self.pivots = {f"x1.{n_}": {} for n_ in _KindEl.build(k_).pivots}
    _kns, _knp = _NTc._counted(_kS, "x1", _KP("signal")), _NTc._counted(_kS, "x1", _KP("power"))
    _krb = [dict(r_) for r_ in _kr] + [dict(kind="pin", a="4", b="c-4", part="contact-4", when="", value="not claimed", unit="N·m", source="x", note="")]
    _krm = [dict(r_) for r_ in _kr]; _krm[3]["b"] = "c-9"
    t("behaviour: an `only kind=<value>` pin (request elec-15, ESCAPE receptacle-m23-1.0 2) is a pin only in builds of that value: BEH-010/020/040"
      " pass a two-kind receptacle (4 to 6 signal, PE power); the power build has 1, 2, 3, PE and the signal build 1 to 6, in spec(params) and in the"
      " solver; an only row for a mark with a default row FAILs; an only pin a build of its value lacks is BEH-020",
      all(x[0] == "PASS" for x in _krc) and sorted(_kSp["pins"]) == ["1", "2", "3", "PE"] and sorted(_kSs["pins"]) == ["1", "2", "3", "4", "5", "6"]
      and sorted(_knp["pins"]) == ["1", "2", "3", "PE"] and sorted(_kns["pins"]) == ["1", "2", "3", "4", "5", "6"]
      and any(x[0] == "FAIL" and "only row" in x[3] for x in BH.check("selftest", _KindEl.build(), _krb, build_of=_KindEl))
      and any(x[1] == "BEH-020" and "only kind=signal pin 4" in x[2] for x in BH.check("selftest", _KindEl.build(), _krm, build_of=_KindEl)),
      f"{_krc} {sorted(_kSp['pins'])} {sorted(_kSs['pins'])} {sorted(_kns['pins'])}")
    from toolkit import library as LBc_, m12 as M12c_
    _cm = LBc_.load("cordset-m12"); _co = {c_: _cm.build(coding=c_, genders="male-open") for c_ in ("A", "D", "L")}
    _cd = _cm.build(**_cm.PARAMS)
    t("cordset-m12's open end has one contact node per pole of its coding and no plug-m12 at end B; the default form keeps port-b",
      all(sorted(n_ for n_, pv_ in P_.pivots.items() if n_.startswith("lead-") and pv_["kind"] == "contact") == sorted(f"lead-{k_}" for k_ in M12c_.LAYOUT[c_])
          and not any(n_ == "port-b" or n_.startswith("port-b.") for n_ in P_.pivots) for c_, P_ in _co.items())
      and "port-b" in _cd.pivots and not any(n_.startswith("lead-") for n_ in _cd.pivots), str({c_: sorted(n_ for n_ in P_.pivots if not n_.startswith("port-a")) for c_, P_ in _co.items()}))
    # round 30's 2.d (core watch 2026-11-12): the open form's AutoCAD FAIL was its five L leads' end circles picked at the device's
    # r 0.5 (Ø1.29, just over 2.5 r); a conductor's end takes the wire's edge break. Prims.radii gives one primitive its own radius,
    # carried by transform and library.place, and fillet._radii takes it over the owner's
    from toolkit import fillet as FLc_, prims as PRc_
    _lp = [(rec_["r"], e_["status"]) for rec_ in FLc_.outer_edges(_co["L"], cls=_cm.CLASS) if rec_["layer"] == "M-CU" for e_ in rec_["edges"] if e_["status"] == "pick"]
    _tp = PRc_.Prims(); _tp.box("M-X", 0, 0, 0, 1, 1, 1); _tp.radii[0] = 0.1; _tq = PRc_.transform(_tp, (5, 0, 0), base=3)
    t("cordset-m12's open L leads are picked at the wire's radius (0.1), not the device's 0.5; a primitive's own radius survives placing",
      len(_lp) == 5 and all(r_ == FLc_.RADIUS["wire"] for r_, _ in _lp) and _tq.radii == {3: 0.1}, str(_lp))
    _bad = [dict(r_) for r_ in _good]; _bad[9]["a"] = "housing"
    t("BEH-030 fails a pose on a node that doesn't move", any(x[1] == "BEH-030" and x[0] == "FAIL" for x in BH.check("selftest", _bp, _bad)))
    _S = BH.spec("selftest", _good); _w = _S["states"]["magnet"][1][1]
    t("a when evaluates on what the element's loads see (coil at 24 V operates, 15 V holds the previous state, 5 V releases)",
      _w.eval(dict(states={}, V=lambda p: 24.0, I=lambda p: 0, Vab=None)) and not _w.eval(dict(states={}, V=lambda p: 15.0, I=lambda p: 0, Vab=None))
      and _S["states"]["magnet"][2][1].eval(dict(states={}, V=lambda p: 5.0, I=lambda p: 0, Vab=None)))
    t("pose '*' = end puts every moving node at its range end in that state, nothing at rest", BH.poses(_S, _bp, {"operated": True}) == {"carrier": 3.5, "coil": 1.0} and BH.poses(_S, _bp, {"operated": False}) == {})
    _bp.pivot("t-21", "port", (0, 0, 0), unit="screw", gender="none"); _bp.pivot("flag", "translate", (0, 0, 0), axis=(0, 1, 0), range=(0, 3))
    _bp.pivot("estop-door", "translate", (0, 0, 0), axis=(0, 1, 0), range=(0, 6)); _bp.owners.append((0, 0, "estop-door", "op-estop-22-2nc"))
    _c = [dict(r_) for r_ in _good]; _c[9]["a"] = "carrier coil"
    _r = BH.check("selftest", _bp, _c)
    t("BEH-040 holds a port node with no pin row and a moving node with no pose row, and leaves a placed element's nodes to its own spec",
      any(x[1] == "BEH-040" and "t-21" in x[2] for x in _r) and any(x[1] == "BEH-040" and "flag" in x[2] and "estop-door" not in x[2] for x in _r), str(_r))
    # core watch 2026-11-09, the improvement run: the core drafts the spec an element's own nodes settle (BH.draft), and only that
    def _dr(P, rows=()):
        txt, why = BH.draft("selftest-draft", P, motion_rows=list(rows))
        R = [dict(zip(BH.HEADER.split(","), l.split(","))) for l in (txt or "").splitlines() if l and not l.startswith("#") and l != BH.HEADER]
        return txt, why, (BH.check("selftest-draft", P, R) if txt else [])
    _s = Prims(); _txt, _, _r = _dr(_s)
    _m = Prims(); _m.pivot("door", "rotate", (0, 0, 0), axis=(0, 0, 1), range=(0, 110)); _m.pivot("drawer", "translate", (0, 0, 0), axis=(0, 1, 0), range=(0, 300))
    _mt, _, _mr = _dr(_m)
    t("behaviour draft: a structural part is the header alone, and a moving part a manual toggle and a pose per node; BEH-010/030/040 pass both",
      _txt and _txt.strip().splitlines()[-1] == BH.HEADER and [x[0] for x in _r] == ["PASS"]
      and _mt and _mt.count(",manual toggle,") == 2 and _mt.count("\npose,") == 2 and all(x[0] == "PASS" for x in _mr), f"{_r} {_mr}")
    _p = Prims(); _p.pivot("t-1", "port", (0, 0, 0), unit="screw", gender="none")
    _e = Prims(); _e.pivot("lamp", "emissive", (0, 0, 0), range=(0, 1))
    _k = Prims(); _k.pivot("lever", "rotate", (0, 0, 0), axis=(0, 0, 1), range=(0, 30))
    t("behaviour draft leaves to the lane what the part's nodes don't settle: a port's mark, what lights a lamp, a motion.csv follower",
      _dr(_p)[0] is None and "port" in _dr(_p)[1] and _dr(_e)[0] is None and "emissive" in _dr(_e)[1]
      and _dr(_k, [dict(scope="selftest-*", leader="lever", follower="cam", mode="follow", stop="")])[0] is None)
    # the solver (toolkit/nets.py): a three-wire motor starter wired from the proposed specs, nothing scripted
    from . import nets as NT
    class _FP:
        def __init__(self): self.owners = []; self.pivots = {}
    _fp = _FP()
    for _tg, _ed in [("x1-1", "term-4mm"), ("x1-2", "term-4mm"), ("x1-3", "term-4mm"), ("x1-4", "term-4mm"), ("x1-5", "term-4mm"), ("q1", "disc-3p-30a"),
                     ("k1", "contactor-9a-1no1nc"), ("f1", "overload-9a-1no1nc"), ("stop", "op-estop-22-2nc"), ("start", "op-pb-22-1no"), ("h1", "op-pilot-22")]:
        _fp.owners.append((0, 0, _tg, _ed))
    _fp.pivots["k1.carrier"] = dict(kind="translate", range=(0, 3.5)); _fp.pivots["h1.self"] = dict(kind="emissive", range=(0, 1))
    _W = [dict(zip(("from", "to"), x)) for x in [("x1-1.2", "stop.11"), ("stop.12", "f1.95"), ("f1.96", "start.13"), ("start.14", "k1.A1"), ("k1.A2", "x1-2.2"),
          ("k1.13", "start.13"), ("k1.14", "start.14"), ("h1.X1", "k1.54"), ("k1.53", "f1.96"), ("h1.X2", "x1-2.2"),
          ("x1-3.2", "q1.L1"), ("x1-4.2", "q1.L2"), ("x1-5.2", "q1.L3"), ("q1.T1", "k1.1"), ("q1.T2", "k1.3"), ("q1.T3", "k1.5"), ("k1.2", "f1.L1"), ("k1.4", "f1.L2"), ("k1.6", "f1.L3")]]
    _SRC = [dict(pin="x1-1.1", kind="VDC", value="24", phase=""), dict(pin="x1-2.1", kind="VDC", value="0", phase=""),
            dict(pin="x1-3.1", kind="VAC", value="277.13", phase="0"), dict(pin="x1-4.1", kind="VAC", value="277.13", phase="-120"), dict(pin="x1-5.1", kind="VAC", value="277.13", phase="120")]
    _E = NT.elements(_fp)
    if len(_E) == 11:
        def _run(inp, fresh=True):
            if fresh:
                for e_ in _E.values(): e_.__init__(e_.tag, e_.eid, e_.S)
            return NT.solve("selftest", inp, P=_fp, W=_W, SRC=_SRC, E=_E)
        _r = _run({"q1.on": True})
        t("nets: the disconnect on puts 277 V to ground and 480 V between phases on K1's line side; the load side floats (the meter says so)",
          _r.meter("k1.1", "x1-2.1")["vac"] == 277.1 and _r.meter("k1.1", "k1.3")["vac"] == 480.0 and _r.meter("k1.1", "k1.2").get("floating") == ["k1.2"], str(_r.meter("k1.1", "k1.3")))
        _r = _run({"q1.on": True, "start.pressed": True})
        t("nets: start pressed: 24 V reaches the coil through the e-stop and the overload, K1 operates, 480 V reaches the motor terminals, the coil draws 0.24 A",
          _r.states()["k1"]["magnet-system"] == "operated" and _r.meter("k1.A1", "k1.A2")["vdc"] == 24.0 and _r.meter("f1.T1", "f1.T2")["vac"] == 480.0 and round(_r.loads()["k1.coil"]["I"], 2) == 0.24, str(_r.loads()))
        _r = _run({"q1.on": True}, fresh=False)
        t("nets: seal-in emerges: the button released, K1 stays in through its own 13-14 (nothing scripted); the run lamp is lit through 53-54",
          _r.states()["k1"]["magnet-system"] == "operated" and _r.flags()["h1.lit"] and _r.poses(_fp) == {"k1.carrier": 3.5, "h1.self": 1.0}, str(_r.states()) + str(_r.poses(_fp)))
        _r = _run({"q1.on": True, "stop.pressed": True}, fresh=False)
        t("nets: the e-stop pressed opens the coil circuit: K1 drops out, 0 V on the motor terminals, 0 V across the coil", _r.states()["k1"]["magnet-system"] == "released" and _r.meter("f1.T1", "f1.T2")["vac"] == 0.0 and _r.meter("k1.A1", "k1.A2")["vdc"] == 0.0)
        _r = _run({"q1.on": True, "start.pressed": True, "f1.tripped": True})
        t("nets: the overload tripped: 95-96 open, K1 cannot pull in with start held; 97-98 closed signals the trip", _r.states()["k1"]["magnet-system"] == "released" and _r.meter("k1.A1", "k1.A2")["vdc"] == 0.0 and _r.nets.find("f1.97") == _r.nets.find("f1.98"))
        _r = _run({"start.pressed": True})
        t("nets: with the disconnect off the control circuit still runs (24 V is its own source) but the motor terminals read 0", _r.states()["k1"]["magnet-system"] == "operated" and _r.meter("f1.T1", "f1.T2")["vac"] == 0.0)
        _Wbad = [w_ for w_ in _W if w_ != dict(zip(("from", "to"), ("k1.14", "start.14")))]
        for e_ in _E.values(): e_.__init__(e_.tag, e_.eid, e_.S)
        NT.solve("selftest", {"q1.on": True, "start.pressed": True}, P=_fp, W=_Wbad, SRC=_SRC, E=_E); _r = NT.solve("selftest", {"q1.on": True}, P=_fp, W=_Wbad, SRC=_SRC, E=_E)
        t("nets: a miswire misbehaves as the real one would: the seal-in wire left off, K1 drops when the button is released", _r.states()["k1"]["magnet-system"] == "released")
        _r = _run({"q1.on": True, "q2.on": True, "field": True, "run": True})
        t("nets: the solver runs the core's hand-laid panel (pm-motor-starter wires.csv) and finds what the rules block hid: the PSU sees 480 V on a 264 V input, so nothing in the control circuit lives",
          (lambda R: R.over() == [("g1.input", 480.0, 264.0, "VAC")] and R.states()["g1"]["converter"] == "off" and R.states()["k1"]["magnet-system"] == "released")(NT.solve("pm-motor-starter", {"q1.on": True, "q2.on": True, "q3.on": True, "field": True, "run": True})), "")
        _motor = [dict(wire="m12", **{"from": "f1.T1", "to": "f1.T2"}, r_ohm="600"), dict(wire="m23", **{"from": "f1.T2", "to": "f1.T3"}, r_ohm="600"), dict(wire="m31", **{"from": "f1.T3", "to": "f1.T1"}, r_ohm="600")]
        _loose = [dict(w_, r_ohm="5") if w_["from"] == "k1.2" else w_ for w_ in _W]
        for e_ in _E.values(): e_.__init__(e_.tag, e_.eid, e_.S)
        _r = NT.solve("selftest", {"q1.on": True, "start.pressed": True}, P=_fp, W=_W + _motor, SRC=_SRC, E=_E)
        for e_ in _E.values(): e_.__init__(e_.tag, e_.eid, e_.S)
        _rl = NT.solve("selftest", {"q1.on": True, "start.pressed": True}, P=_fp, W=_loose + _motor, SRC=_SRC, E=_E)
        t("flows 1.5: with a 600 Ω delta load the motor terminals read 480 V and the line carries √3 × 0.8 A; a 5 Ω loose joint on K1's T1 drops 6.8 V across itself, T1–T2 reads 474 V and T2–T3 still 480 (Kirchhoff, nothing scripted)",
          _r.meter("f1.T1", "f1.T2")["vac"] == 480.0 and round(abs(_r.currents["k1.pole-1"][2]), 2) == 1.39 and _rl.meter("k1.2", "f1.L1")["vac"] == 6.8 and _rl.meter("f1.T1", "f1.T2")["vac"] == 474.1 and _rl.meter("f1.T2", "f1.T3")["vac"] == 480.0,
          f"{_r.meter('f1.T1', 'f1.T2')} {_rl.meter('k1.2', 'f1.L1')} {_rl.meter('f1.T1', 'f1.T2')} {dict((k, round(abs(v[2]), 2)) for k, v in _rl.currents.items())}")
        t("nets: every solution reaches a fixpoint", _r.stable and _r.passes <= 5, str(_r.passes))
        # request panel-14 (core watch 2026-11-13): a comb's milliohm bar put the 0 V blocks some µV apart, and the solver read that
        # offset across a load or an input whose other side floats (io-1's floating DIs read on; a 0.5 W lamp drew 13 912 A)
        _W14 = [w_ for w_ in _W if w_ != dict(zip(("from", "to"), ("h1.X1", "k1.54")))]
        _S14 = [dict(s_, value="0.000036") if s_["pin"] == "x1-2.1" else s_ for s_ in _SRC]
        for e_ in _E.values(): e_.__init__(e_.tag, e_.eid, e_.S)
        _rf = NT.solve("selftest", {"q1.on": True}, P=_fp, W=_W, SRC=_S14, E=_E)
        for e_ in _E.values(): e_.__init__(e_.tag, e_.eid, e_.S)
        _rd = NT.solve("selftest", {"q1.on": True}, P=_fp, W=_W14, SRC=_S14 + [dict(pin="h1.X1", kind="VDC", value="0", phase="")], E=_E)
        t("nets: a load with a floating side sees nothing across it, whatever µV its other side sits at (request panel-14: K1 out, the run lamp's +"
          " floats and its 0 V is 36 µV off: 0 V, 0 A, not 13 333 A); a power-rated load a few µV across draws nothing (P / V only past 1 V,"
          " as load_edges); a floating side still counts as 0 V for nothing else (the meter reports it)",
          _rf.loads()["h1.lamp-block"] == dict(V=0.0, I=0.0) and _rd.loads()["h1.lamp-block"]["I"] == 0.0 and not _rf.flags()["h1.lit"]
          and NT._mag(None, NT.Pot(dc=3.6e-5)) == 0.0 and NT._mag(NT.Pot(dc=24.0), NT.Pot(dc=0.0)) == 24.0, f"{_rf.loads()['h1.lamp-block']} {_rd.loads()['h1.lamp-block']}")
    else: t("nets: the eleven proposed specs of the starter are readable (lib/requests/core/behaviour/)", False, str(sorted(_E)))
    # the twin reads the solver's table, not rules (toolkit/twin.solved)
    import tempfile as _tf, os
    from . import twin as TWN
    _P = NT._assembly("pm-motor-starter"); _sc = json.load(open(os.path.join(_lib.ROOT, "toolkit", "twin", "scenes", "pm-motor-starter.json"), encoding="utf-8"))
    _sc2 = dict(_sc, inputs={k: _sc["inputs"][k] for k in ("power", "q2", "q3", "estop")})
    with _tf.TemporaryDirectory() as _d:
        _T = TWN.solved("pm-motor-starter", _P, _sc2, os.path.join(_d, "t.json"))
    _on = _T["states"]["1110"]; _nm = _T["netmaps"][_on["nets"]]
    _pot = lambda pin: _on["pots"].get(str(_nm[pin]))
    t("twin table: 2^n combinations of the scene's inputs, each with poses, flags, a net map and potentials; the e-stop input carries its latch, its clearing input and the node to click",
      len(_T["states"]) == 16 and _T["inputs"]["estop"]["kind"] == "latch" and _T["inputs"]["estop"]["node"] == "enc-1.estop-door" and "k1.1" in _T["probes"], str(_T["inputs"]["estop"]))
    t("twin table: with Q1, Q2 and Q3 on the table reads 480 V across the PSU's input and marks it OVER its 264 V rating; its output floats, so K1's coil has nothing",
      _on["over"] == [["g1.input", 480.0, 264.0, "VAC"]] or _on["over"] == [("g1.input", 480.0, 264.0, "VAC")], str(_on["over"]))
    t("twin table: the PSU's +V floats (None) and its L–N potentials differ by 480 V",
      _pot("g1.+V") is None and _pot("g1.L") is not None and _pot("g1.N") is not None and round(((_pot("g1.L")[0] - _pot("g1.N")[0]) ** 2 + (_pot("g1.L")[1] - _pot("g1.N")[1]) ** 2) ** 0.5) == 480, str(_pot("g1.L")))
    # request panel-12 (core watch 2026-11-12): the scene's key 4 named the transformer's stand-in `t1`, gone with t1 placed at v0.9;
    # the input is now q4's handle (q4.on), and "power on" works it: Q1, Q4, Q2, Q3 on give 120 V on t1's secondary and the PSU on
    try:
        _sp = json.load(open(os.path.join(_lib.ROOT, "toolkit", "twin", "scenes", "pnl-motor-starter.json"), encoding="utf-8"))
        _pon = next(s_["work"] for s_ in _sp["smoke"] if s_.get("name") == "power on")
        _sp2 = dict(_sp, inputs={k: _sp["inputs"][k] for k in ("power", "q4", "q2", "q3")})
        with _tf.TemporaryDirectory() as _d:
            _Tp = TWN.solved("pnl-motor-starter", NT._assembly("pnl-motor-starter"), _sp2, os.path.join(_d, "t.json"))
        _a, _b = _Tp["states"]["1111"], _Tp["states"]["1011"]
        _p2u = lambda st: st["pots"].get(str(_Tp["netmaps"][st["nets"]].get("t1.2U")))
        ok = _sp["inputs"]["q4"]["solver"] == "q4.on" and "t1" not in _sp["inputs"] and "q4" in _pon and "g1.on" in _a["flags"] \
            and (_p2u(_a) or [0])[0] == 120.0 and "g1.on" not in _b["flags"] and _p2u(_b) is None
        got = f"power on {_pon} 1111 {_p2u(_a)} {'g1.on' in _a['flags']} 1011 {_p2u(_b)}"
    except Exception as e: ok, got = False, repr(e)
    t("twin scene pnl-motor-starter: key 4 is Q4's handle (q4.on, request panel-12); 'power on' works it, so t1's secondary reads 120 V and the PSU"
      " is on, and with Q4 off the secondary floats and the PSU is off", ok, got)
    t("a manual state becomes a twin input with its kind and what clears it", BH.spec("selftest", [dict(kind="state", a="tripped", b="", part="latch", when="manual latch cleared by reset", value="", unit="", source="x", note=""),
      dict(kind="state", a="reset", b="", part="btn", when="manual momentary", value="", unit="", source="x", note="")])["inputs"] == {"tripped": dict(kind="latch", cleared_by="reset", part="latch"), "reset": dict(kind="momentary", cleared_by="", part="btn")})
    from . import decal as DC
    L_, W_, H_ = 70.0, 0.2, 30.0                                                    # plc0's label: a closed printed box 70 x 0.2 x 30
    box = [((0, -1, 0), L_ * H_), ((0, 1, 0), L_ * H_), ((1, 0, 0), W_ * H_), ((-1, 0, 0), W_ * H_), ((0, 0, 1), L_ * W_), ((0, 0, -1), L_ * W_)]
    vx = [(x, y, z) for x in (0, L_) for y in (0, W_) for z in (0, H_)]
    old_n = tuple(sum(n[i] for n, _ in box) for i in range(3)); old_n = old_n if any(old_n) else (0, 0, 1)
    old = DC.check([round(x, 2) for x in DC.island(vx, old_n)])
    n_ = DC.axis(box); new = DC.check([round(x, 2) for x in DC.island(vx, n_)])
    t("decal: a closed printed box projects along its front (-y) as 70 x 30 and passes; the old sum-of-normals fallback fails it as a strip",
      n_ == (0.0, -1.0, 0.0) and new[0] == "PASS" and old[0] == "FAIL", f"{n_} {new} | old {old}")
    # escape, request elec-3: thermostat-enc's dial island faced +y (its hidden back) because float32 noise broke a 1e-9 tie
    n_ = DC.axis([((0, 1, 0), 314.1593), ((0, -1, 0), 314.159)])
    t("decal: a disc's back and front a float32 noise apart (314.1593 vs 314.159) are a tie and go to the front (-y)", n_ == (0.0, -1.0, 0.0), str(n_))
    n_ = DC.axis([((0, 1, 0), 314.16), ((0, -1, 0), 300.0)])
    t("decal: a back really larger than the front (314 vs 300) still wins (the tie is noise, not any difference)", n_ == (0.0, 1.0, 0.0), str(n_))
    # ESCAPE valve-gauge-double-1.0 2 (core watch 2026-11-13): an x-axis tie went to the first face's side, so port-4's field on +x faced -x
    _xt = [((-1, 0, 0), 40.0), ((1, 0, 0), 40.0)]
    _xn = (DC.axis(_xt, away=(12.0, 1.0, -3.0)), DC.axis(_xt, away=(-12.0, 1.0, -3.0)), DC.axis([((0, 1, 0), 40.0), ((0, -1, 0), 40.0)], away=(0.0, 9.0, 0.0)),
           DC.axis(_xt, away=(0.0, 0.0, 0.0)))
    t("ESCAPE valve-gauge-double-1.0 2: a print on +x whose front and back tie faces +x, one on -x faces -x (away from the centre); "
      "a y tie away +y faces +y (valve-ball-32-1.1); an island at the centre keeps the old rule", _xn[:3] == ((1.0, 0.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
      and _xn[3] in ((1.0, 0.0, 0.0), (-1.0, 0.0, 0.0)), str(_xn))
    # ESCAPE valve-ball-32-1.1 (core watch 2026-11-14; group 35 again): a field that is its own mesh, and a y tie, faced their hidden sides
    _yt = [((0, 1, 0), 30.0), ((0, -1, 0), 30.0)]
    _fx = DC.away_from((40.0, 0.0, 5.0), ((39.0, -6.0, 0.0), (41.0, 6.0, 10.0)), ((-40.0, -30.0, -20.0), (41.0, 30.0, 30.0)))   # port-3's field, its own mesh
    _fy = DC.away_from((0.0, 30.0, 5.0), ((-6.0, 29.0, 0.0), (6.0, 31.0, 10.0)), ((-40.0, -30.0, -20.0), (41.0, 31.0, 30.0)))   # port-2's, on +y
    _vb = (DC.axis(_xt, away=_fx), DC.axis(_yt, away=_fy), DC.axis(_yt, away=DC.away_from((0.0, -30.0, 5.0), ((-6.0, -31.0, 0.0), (6.0, -29.0, 10.0)), ((-40.0, -31.0, -20.0), (41.0, 30.0, 30.0)))),
           DC.axis(_yt), DC.axis([((0, 0, 1), 30.0), ((0, 0, -1), 30.0)], away=(0.0, 0.0, -9.0)))
    t("ESCAPE valve-ball-32-1.1 (group 35 again): a field that is its own mesh on +x faces +x (away from the element's centre, the mesh's "
      "being its own), one on +y faces +y, one on -y faces -y; a y tie with no centre keeps -y; a z tie keeps +z (decal.away_from, axis)",
      _vb == ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 0.0, 1.0)), str(_vb))
    t("LINE counts an element waiting at station 7 in its lane's work in progress, not one past it (finish before start)", LN.in_progress(6) and not LN.in_progress(7))
    # request mech-3 (core watch 2026-11-06): the board counted every element not past 7, those waiting on EM included; mech idled 4 rounds
    _h = lambda n, *holds: (n, "x", "x", False, list(holds))
    _em = _h(7, "DOC-005 REVIEW: open figures in spec.md: 3 Assumption (B), 7 Assumption (C), 1 NOT ON FILE, 1 NOT ON FILE (C); 4 need EM, 0 ap",
             'no reviewer line "motor-iec71-370w 1.3: PASS" in lib/reviews/')
    t("LINE: an element whose hold at 7 includes DOC-005 REVIEW (EM's lines short, text cut at 110) waits on EM and is out of the WIP count",
      LN.waits_on_em(_em) and not LN.wip(6, _em))
    t("LINE: an element at 1 with no Stage 0 brief (a vendor file read attended) waits on EM",
      LN.waits_on_em(_h(1, "DOC-004 REVIEW: no Stage 0 brief (references/measure.md) on file")))
    t("LINE: a safety-function element held only for EM's 'Safety sign-off' waits on EM",
      LN.waits_on_em(_h(7, 'a safety-function element (inventory.csv safety=yes): no "Safety sign-off: 1.1 · EM <date>" in spec.md')))
    import tempfile as _tfw
    with _tfw.TemporaryDirectory() as _rv:
        os.makedirs(os.path.join(_rv, "elements"))
        _hp = _h(7, 'no reviewer line "pallet 1.0: PASS" in lib/reviews/')
        _w_none = LN.wip(6, _hp, _rv)
        open(os.path.join(_rv, "elements", "pallet-1.0.md"), "w").write("pallet 1.0: FINDINGS\n1. x\n")
        _w_first = LN.wip(6, _hp, _rv)
        open(os.path.join(_rv, "elements", "pallet-1.0-reread.md"), "w").write("pallet 1.0: FINDINGS\n1. still open\n")
        _w_reread = LN.wip(6, _hp, _rv)
        _m_reread = LN.count_mark(6, _hp, _rv)
        os.remove(os.path.join(_rv, "elements", "pallet-1.0-reread.md")); _m_first = LN.count_mark(6, _hp, _rv)
        os.remove(os.path.join(_rv, "elements", "pallet-1.0.md")); _m_none = LN.count_mark(6, _hp, _rv)
    # core watch 2026-11-07 (improvement run): the board marked mech's 6 reviewer-held elements 'WIP' under a header that counted 0
    t("LINE: the board's mark says 'WIP' exactly when the WIP count counts it: waiting on the reviewer 'rev', its re-read still finding something 'WIP'",
      _m_none == "rev" and _m_first == "rev" and _m_reread == "WIP", f"{_m_none} {_m_first} {_m_reread}")
    t("LINE: an element waiting only on the reviewer (no review at its version, or the re-read owed) is out of the WIP; one whose re-read "
      "still finds something, or held by its own gate's miss, counts (EM 2026-11-07: elements first; finish before start)",
      not _w_none and not _w_first and _w_reread
      and LN.wip(5, _h(6, "AutoCAD gate: brief figure 'height' 850.9 not on the build's z extent 1250.9 (diff 400 > 0.8, ISO 2768-1 m)"))
      and not LN.wip(7, None), f"{_w_none} {_w_first} {_w_reread}")
    # core watch 2026-11-09 (2.d, elec idle r17, r18): the cloud builder's elements waiting only for their first gates filled elec's limit
    _g_new = _h(6, "no AutoCAD gate on file", "no Blender gate on file", "no Godot QA on file")
    _g_fail = _h(6, "no Blender gate on file", "AutoCAD gate failed (2026-11-08)")
    _g_old = _h(6, "AutoCAD gate passed at v1.0, not v1.1")
    t("LINE: an element held at station 6 only by gates not yet run is the lane's gate queue ('gate'), out of the WIP; a failed "
      "gate beside it, or alone, counts (core watch 2026-11-09: elec idled two rounds with 9 such counted)",
      not LN.wip(5, _g_new) and LN.count_mark(5, _g_new) == "gate" and LN.wip(5, _g_fail)
      and LN.count_mark(5, _g_fail) == "WIP" and not LN.waits_on_gates(_h(5, "no AutoCAD gate on file")),
      f"{LN.wip(5, _g_new)} {LN.count_mark(5, _g_new)} {LN.wip(5, _g_fail)}")
    # request elec-16 (core watch 2026-11-13): AutoCAD answered nothing from 03:42; elec's minors held only by an AutoCAD pass at the old
    # version counted 5 of 3, and r51, r52 built nothing
    _g_oldf = _h(6, "AutoCAD gate passed at v1.0, not v1.1", "AutoCAD gate failed (2026-11-13)")
    _g_oldv = _h(6, "variant d: AutoCAD gate passed at v1.0, not v1.1", "no Godot QA on file")
    _g_nores = _h(6, LN.ACAD_NO_RESULT + "gate/x.lsp (v1.1) is from a run that wrote none; the pass on file is an earlier run's, not v1.1")
    _g_oldb = _h(6, "AutoCAD gate passed at v1.0, not v1.1", "Blender gate failed")
    t("LINE: request elec-16: an element held at station 6 only by an AutoCAD pass at an older version (its own or a variant's), or by a "
      "gate file whose run wrote no result, waits for a run ('gate', out of the WIP); with a failed AutoCAD or Blender gate beside it, it counts",
      not LN.wip(5, _g_old) and LN.count_mark(5, _g_old) == "gate" and not LN.wip(5, _g_oldv) and not LN.wip(5, _g_nores)
      and LN.wip(5, _g_oldf) and LN.wip(5, _g_oldb) and LN.count_mark(5, _g_oldb) == "WIP",
      f"{LN.wip(5, _g_old)} {LN.count_mark(5, _g_old)} {LN.wip(5, _g_oldv)} {LN.wip(5, _g_nores)} {LN.wip(5, _g_oldf)} {LN.wip(5, _g_oldb)}")
    # request elec-7 (core watch 2026-11-09): relay-safety-2ch-2no1nc 1.2's depth 113.6 (manual p. 11) against 114.6, a vendor file's reading, filled elec's limit
    import json as _jr
    with _tfw.TemporaryDirectory() as _er:
        _el, _ne = os.path.join(_er, "elements"), os.path.join(_er, "needs-em"); os.makedirs(os.path.join(_el, "sr-x", "gate")); os.makedirs(_ne)
        def _gj(src):
            _jr.dump({"pass": True, "step": {"extents": [22.563, 114.601, 119.203]}, "measure_compare": [
                {"feature": "height", "values": [119.14], "source": "manual p. 11 Figure 2"},
                {"feature": "depth", "values": [113.6], "source": src}]}, open(os.path.join(_el, "sr-x", "gate", "sr-x-acad.json"), "w"))
        _hr = _h(6, "AutoCAD gate: brief figure 'depth' 113.6 not on the build's y extent 114.601 (diff 1.001 > 0.3, ISO 2768-1 m)")
        _ln = {"sr-x": "elec"}
        _gj("manual p. 11, p. 73")
        _r_before = LN.waits_on_reading(_hr, "sr-x", _el, _ne, _ln)
        open(os.path.join(_ne, "elec.md"), "w").write("1. sr-x 1.2 holds at station 6 on its brief depth: the manual p. 11 read, attended\n")
        _r_after = LN.waits_on_reading(_hr, "sr-x", _el, _ne, _ln)
        import shutil as _shr; _shr.copytree(os.path.join(_el, "sr-x", "gate"), os.path.join(_el, "sr", "gate"))
        os.rename(os.path.join(_el, "sr", "gate", "sr-x-acad.json"), os.path.join(_el, "sr", "gate", "sr-acad.json"))
        _r_other = LN.waits_on_reading(_hr, "sr", _el, _ne, {"sr": "elec"})              # "sr-x" in the file doesn't name "sr"
        _r_beside = LN.waits_on_reading(_h(6, _hr[4][0], "Blender gate failed"), "sr-x", _el, _ne, _ln)
        _gj("references/model-measure.json solid 3, p. 11"); _r_data = LN.waits_on_reading(_hr, "sr-x", _el, _ne, _ln)
        _gj("own: design choice"); _r_own = LN.waits_on_reading(_hr, "sr-x", _el, _ne, _ln)
    t("LINE: a station-6 hold that is only the gate's brief-figure miss on a vendor document's page, with the element in its lane's "
      "needs-em file, waits on EM (attended reading) and leaves the WIP; not named there, beside another hold, a figure from a measure "
      "JSON or the lane's own choice, it counts (request elec-7: relay-safety-2ch-2no1nc 1.2 took elec to 4 of 3, two idle rounds)",
      not _r_before and _r_after and not _r_other and not _r_beside and not _r_data and not _r_own and not LN.waits_on_reading(_hr, None),
      f"{_r_before} {_r_after} {_r_other} {_r_beside} {_r_data} {_r_own}")
    # request elec-8 (core watch 2026-11-09): relay-safety-2ch-2no1nc 1.2 held at station 5 by BEH-020 only, its marks' positions on the manual's Figure 6
    with _tfw.TemporaryDirectory() as _er:
        _el, _ne = os.path.join(_er, "elements"), os.path.join(_er, "needs-em"); os.makedirs(os.path.join(_el, "sr-x", "references")); os.makedirs(_ne)
        def _mm(ports): open(os.path.join(_el, "sr-x", "references", "measure.md"), "w").write(f"# brief\n\n## Ports\n{ports}\n\n## Decals\n- front (p. 14)\n")
        _p5 = _h(5, "BEH-020 REVIEW: no port (or contact) node on the element for the probe to touch (P.pivot(<node>, 'port', ...))")
        _ln = {"sr-x": "elec"}
        _mm("Screw terminal blocks A1 / A2, S11 / S21, 13/14 (manual p. 14 Table 2).")
        _p_before = LN.waits_on_reading(_p5, "sr-x", _el, _ne, _ln)
        open(os.path.join(_ne, "elec.md"), "w").write("1. sr-x 1.2 holds at station 5 on BEH-020: the marks' positions are on Figure 6, attended\n")
        _p_after = LN.waits_on_reading(_p5, "sr-x", _el, _ne, _ln)
        _p_beside = LN.waits_on_reading(_h(5, _p5[4][0], "BEH-040 REVIEW: moving node with no pose row"), "sr-x", _el, _ne, _ln)
        _p_st6 = LN.waits_on_reading(_h(6, _p5[4][0]), "sr-x", _el, _ne, _ln)
        _mm("A1 / A2 at x 3.2, 8.2 (references/model-measure.json solid 4, p. 14)"); _p_data = LN.waits_on_reading(_p5, "sr-x", _el, _ne, _ln)
        _mm("Two screw clamps, our own design."); _p_own = LN.waits_on_reading(_p5, "sr-x", _el, _ne, _ln)
        # elec idle r31 (core watch 2026-11-12): renamed, the element's needs-em line still names its old id (an alias)
        _mm("Screw terminal blocks A1 / A2, S11 / S21, 13/14 (manual p. 14 Table 2).")
        os.makedirs(os.path.join(_el, "relay-x-2ch", "references"))
        open(os.path.join(_el, "relay-x-2ch", "references", "measure.md"), "w").write(open(os.path.join(_el, "sr-x", "references", "measure.md")).read())
        _lnr = {"relay-x-2ch": "elec"}
        _p_noalias = LN.waits_on_reading(_p5, "relay-x-2ch", _el, _ne, _lnr)
        open(os.path.join(_el, "relay-x-2ch", "metadata.json"), "w").write('{"element_id": "relay-x-2ch", "aliases": ["sr-x"]}')
        _p_alias = LN.waits_on_reading(_p5, "relay-x-2ch", _el, _ne, _lnr)
        open(os.path.join(_el, "relay-x-2ch", "metadata.json"), "w").write('{"element_id": "relay-x-2ch", "aliases": ["sr-y"]}')
        _p_other = LN.waits_on_reading(_p5, "relay-x-2ch", _el, _ne, _lnr)
        os.remove(os.path.join(_el, "sr-x", "references", "measure.md")); _p_none = LN.waits_on_reading(_p5, "sr-x", _el, _ne, _ln)
    t("LINE: a renamed element whose lane's needs-em line names it by its old id (an alias in metadata.json) waits on EM as under its "
      "own id; with no alias, or another alias, it counts (elec idle r31: sr-440r's line, relay-safety-2ch-2no1nc counted, 4 of 3)",
      _p_alias and not _p_noalias and not _p_other, f"{_p_alias} {_p_noalias} {_p_other}")
    t("LINE: a station-5 hold that is only BEH-020, with the brief's Ports placing the marks from a vendor document's page and the "
      "element in its lane's needs-em file, waits on EM (attended reading) and leaves the WIP; not named there, beside another hold, "
      "at another station, ports from a measure JSON, the lane's own design, or no brief, it counts (request elec-8: relay-safety-2ch-2no1nc 1.2, "
      "Figure 6, elec at 3 of 3 in r23)",
      not _p_before and _p_after and not _p_beside and not _p_st6 and not _p_data and not _p_own and not _p_none,
      f"{_p_before} {_p_after} {_p_beside} {_p_st6} {_p_data} {_p_own} {_p_none}")
    # request elec-11 item 2 (core watch 2026-11-12): main's validation.json, taken whole at a lane's merge, read an element the lane
    # had fixed and built (its own out/validate.json, merged clean) at its old findings: disc-3p-30a 1.4 counted, elec-r32 built nothing
    with _tfw.TemporaryDirectory() as _vd:
        _vl, _ve = os.path.join(_vd, "lib"), os.path.join(_vd, "lib", "elements")
        os.makedirs(os.path.join(_vl, "out")); os.makedirs(os.path.join(_ve, "disc-x", "out")); os.makedirs(os.path.join(_ve, "asm-x"))
        _g70 = {"status": "REVIEW", "rule": "GEO-070", "scope": "disc-x", "where": "disc-x", "message": "3 solids 1.9 mm from the main body", "elements": []}
        _ok70 = dict(_g70, status="PASS", message="every solid touches the main body")
        _erc = {"status": "REVIEW", "rule": "ERC-010", "scope": "asm-x", "where": "asm-x", "message": "Q1 below its load", "elements": ["disc-x"]}
        json.dump({"findings": [_g70, _erc]}, open(os.path.join(_vl, "out", "validation.json"), "w"))
        _vcat = {"disc-x": {"version": "1.4"}}
        _vst = lambda: {n: h for n, _, _, _, h in LN.element("disc-x", LN._findings(_vl, _ve), _vcat, set(), "", set(), "")}
        _v_none = _vst()                                                           # no own file: the merged record
        json.dump({"findings": [_ok70]}, open(os.path.join(_ve, "disc-x", "out", "validate.json"), "w"))
        _v_own = _vst()                                                            # its own build PASS: read from its own file
        json.dump({"findings": [_g70]}, open(os.path.join(_ve, "disc-x", "out", "validate.json"), "w"))
        _v_same = _vst()
    t("LINE: an element whose own out/validate.json (its lane's build, merged clean) passes a rule the merged lib/out/validation.json "
      "still holds it on reads at its own findings; the assembly's finding that names it stays; with no own file, or one that agrees, "
      "the merged record (request elec-11 item 2: disc-3p-30a 1.4 at main's GEO-070 of 1.3, elec-r32 idle at 3 of 3)",
      any("GEO-070" in h for h in _v_none[2]) and not _v_own[2] and any("ERC-010" in h for h in _v_own[5])
      and any("GEO-070" in h for h in _v_same[2]), f"{_v_none[2]} | {_v_own[2]} {_v_own[5]} | {_v_same[2]}")
    # request elec-5 (core watch 2026-11-07): the board gave totals only, and the lane counted three EM-held elements as its own
    _rv = 'no reviewer line "relay-ice-cube-2co 1.3: PASS" in lib/reviews/'
    t("LINE: the board marks each element: EM's DOC-005 beside the reviewer's line 'EM', a gate's own miss 'WIP', past 7 ''",
      LN.count_mark(6, _h(7, _em[4][0], _rv)) == "EM"
      and LN.count_mark(5, _h(6, "AutoCAD gate: brief figure 'height' 850.9 not on the build's z extent 1250.9 (diff 400 > 0.8, ISO 2768-1 m)")) == "WIP"
      and LN.count_mark(7, None) == "")
    # core watch 2026-11-08 (improvement run): elec counted 13 against its limit of 3, 11 of them taken back at versions it had already
    # brought to station 5 or 6 by checks added later (GEO-070, MOT-030, DOC-006 ...), and would start no new element for over a shift
    _hist = {("plc0", "1.1"): 6, ("mcb-1p-c6", "1.2"): 4}
    _gen = _h(2, "PIN-002 REVIEW: 2 port(s) without a gender (port-eth, port-pwr): declare gender=male, female or none on the pivot")
    t("LINE the backlog: an element held at 2 at a version that had reached 6 (a later rule took it back) is out of the WIP count and marked 'back'",
      not LN.wip(1, _gen, eid="plc0", ver="1.1", hist=_hist) and LN.count_mark(1, _gen, eid="plc0", ver="1.1", hist=_hist) == "back")
    t("LINE the backlog: the same hold at a new version (no history: the lane's own work), at a version never past where it stands, or "
      "with no id given, still counts 'WIP'",
      LN.wip(1, _gen, eid="plc0", ver="1.2", hist=_hist) and LN.wip(4, _gen, eid="mcb-1p-c6", ver="1.2", hist=_hist)
      and LN.wip(1, _gen, hist=_hist) and LN.count_mark(1, _gen, eid="plc0", ver="1.2", hist=_hist) == "WIP")
    t("LINE the backlog: EM's hold still reads 'EM' and an element past 7 '' though its history is higher",
      LN.count_mark(6, _h(7, _em[4][0]), eid="plc0", ver="1.1", hist=_hist) == "EM" and LN.count_mark(7, None, eid="plc0", ver="1.1", hist={("plc0", "1.1"): 8}) == "")
    with _tfw.TemporaryDirectory() as _hd:
        _hf = os.path.join(_hd, "line-history.csv")
        open(_hf, "w", encoding="utf-8").write("at,element,lane,version,reached\n2026-11-05 16:46,plc0,elec,1.1,6\n2026-11-08 16:19,plc0,elec,1.1,1\nbad,row\n")
        _hb = LN.history_best(_hf)
    t("LINE the backlog: lib/line-history.csv gives each version's highest station, a broken row skipped", _hb == {("plc0", "1.1"): 6}, str(_hb))
    # escape group 13, station 7 (core watch 2026-11-09; reviewer mech-r67 finding 1): duct-40x60 1.2 took a behaviour.csv after its
    # review at the same version (fingerprint f1adca2a42a0a2f9 reviewed, b306824a6a813e12 on main) and station 7 still passed
    import hashlib as _hlf
    with _tfw.TemporaryDirectory() as _fd:
        _fe, _fr = os.path.join(_fd, "elements"), os.path.join(_fd, "reviews")
        for _p, _c in (("spec.md", b"spec\r\n"), ("element.py", b"x = 1\n"), ("out/x.lsp", b"gen"), ("gate/x.json", b"{}"), ("qa/q.json", b"{}")):
            os.makedirs(os.path.dirname(os.path.join(_fe, "duct-x", _p)), exist_ok=True); open(os.path.join(_fe, "duct-x", _p), "wb").write(_c)
        _hx = _hlf.sha256(b"lib/elements/duct-x/element.py\0x = 1\nlib/elements/duct-x/spec.md\0spec\n").hexdigest()[:16]
        _fp0 = LN.source_fingerprint("duct-x", _fe)
        os.makedirs(os.path.join(_fr, "elements"))
        _rvf = os.path.join(_fr, "elements", "duct-x-1.2.md")
        open(_rvf, "w").write(f"duct-x 1.2: PASS\n\nSource fingerprint for the record: sha256\n{_fp0} (method as in cabinet-tool-1.1.md)\n")
        _s_same = LN.review_stale("duct-x", "1.2", _fr, _fe)
        open(os.path.join(_fe, "duct-x", "out", "x.lsp"), "wb").write(b"regenerated")       # a generated file: not the reviewed files
        _s_gen = LN.review_stale("duct-x", "1.2", _fr, _fe)
        open(os.path.join(_fe, "duct-x", "behaviour.csv"), "wb").write(b"node,state\n")      # the lane's file at the same version
        _s_new = LN.review_stale("duct-x", "1.2", _fr, _fe); _hs = (7, "x", "x", False, _s_new)
        _fp1 = LN.source_fingerprint("duct-x", _fe)
        open(os.path.join(_fr, "elements", "duct-x-1.2-reread.md"), "w").write(f"duct-x 1.2: PASS\nSource fingerprint: sha256 {_fp1}\n")
        _s_reread = LN.review_stale("duct-x", "1.2", _fr, _fe)
        os.remove(os.path.join(_fr, "elements", "duct-x-1.2-reread.md"))
        open(_rvf, "w").write("duct-x 1.2: PASS\n")
        _s_old = LN.review_stale("duct-x", "1.2", _fr, _fe)
    t("LINE the source fingerprint is the reviewer's: tracked files but out/, gate/, thumbs/, qa/, by path, path NUL content, CRLF made LF, 16 hex",
      _fp0 == _hx, f"{_fp0} {_hx}")
    t("LINE holds at station 7 a reviewer's PASS whose recorded fingerprint is not the files' now (a behaviour.csv added at the same version), "
      "as waiting on the reviewer's re-read, out of the WIP count; the same files, a regenerated out/ file, a re-read at the new fingerprint, "
      "or a PASS written before fingerprints pass (escape group 13)",
      not _s_same and not _s_gen and _s_new and _s_new[0].startswith(LN.STALE_REVIEW) and LN.waits_on_reviewer(_hs) and LN.rereview_due("duct-x", "1.2", _hs)
      and not LN.wip(6, _hs) and LN.count_mark(6, _hs) == "rev" and not _s_reread and not _s_old and _fp1 != _fp0,
      f"{_s_same} {_s_gen} {_s_new} {_s_reread} {_s_old}")
    # round 25's return 4.2 (core watch 2026-11-10): gland-m20 1.3's re-read found FINDINGS at its current files ("Files now: sha256 ..."),
    # and rereview still read the older PASS, recorded on other files, as the element's verdict
    with _tfw.TemporaryDirectory() as _gd:
        _ge, _gr = os.path.join(_gd, "elements"), os.path.join(_gd, "reviews")
        os.makedirs(os.path.join(_ge, "gland-x")); os.makedirs(os.path.join(_gr, "elements"))
        open(os.path.join(_ge, "gland-x", "spec.md"), "wb").write(b"spec\n")
        _gf0 = LN.source_fingerprint("gland-x", _ge)
        open(os.path.join(_gr, "elements", "gland-x-1.3-reread.md"), "w").write(f"gland-x 1.3: PASS\nSource fingerprint: sha256 {_gf0}\n")
        open(os.path.join(_ge, "gland-x", "behaviour.csv"), "wb").write(b"node,state\n")
        _gf1 = LN.source_fingerprint("gland-x", _ge)
        _g_due = LN.review_stale("gland-x", "1.3", _gr, _ge)
        open(os.path.join(_gr, "elements", "gland-x-1.3-reread2.md"), "w").write(f"gland-x 1.3: FINDINGS\nFiles now: sha256 {_gf1}\n")
        _g_fnd = LN.review_stale("gland-x", "1.3", _gr, _ge); _gh = (7, "x", "x", False, _g_fnd)
        _g_v = LN.review_verdict("gland-x", "1.3", _gr, _ge); _g_v0 = LN.review_verdict("gland-x", "1.3", _gr)
        _g_w = LN.waits_on_reviewer(_gh, _gr, _ge); _g_r = LN.rereview_due("gland-x", "1.3", _gh, _gr, _ge)
    t("LINE a review at the files now outranks a PASS read on other files: a later FINDINGS that records the current fingerprint "
      "(any wording) is the verdict, the element is the lane's (counted) and rereview lists it as FINDINGS; with no such review the "
      "stale PASS still waits on the re-read (round 25's return 4.2)",
      _g_due and _g_due[0].startswith(LN.STALE_REVIEW) and _g_fnd and _g_fnd[0].startswith(LN.NO_REVIEWER_LINE) and "reread2" in _g_fnd[0]
      and _g_v == "FINDINGS" and _g_v0 == "PASS" and not _g_w and _g_r,
      f"{_g_due} {_g_fnd} {_g_v} {_g_v0} {_g_w} {_g_r}")
    # request pneu-7 item 3 (core watch 2026-11-10): gauge-p 1.0's last re-read put both open findings under "## Still open (waits on
    # the core, and through it on EM)", and the board still counted it in pneu's three places
    with _tfw.TemporaryDirectory() as _wd:
        _wr = os.path.join(_wd, "reviews"); os.makedirs(os.path.join(_wr, "elements"))
        _wf = lambda n, x: open(os.path.join(_wr, "elements", n), "w").write(x)
        _wf("gauge-x-1.0.md", "gauge-x 1.0: FINDINGS\n\n## Findings\n1. the lane's\n")
        _wf("gauge-x-1.0-reread.md", "gauge-x 1.0: FINDINGS\n\n## Still open\n1. the lane's\n")
        _wh = (7, "x", "x", False, ['no reviewer line "gauge-x 1.0: PASS" in lib/reviews/'])
        _w0 = LN.waits_on_review_owner(_wh, _wr); _wc0 = LN.count_mark(6, _wh, _wr, "gauge-x", "1.0", {})
        _wf("gauge-x-1.0-reread2.md", "gauge-x 1.0: FINDINGS\n\n## Still open (waits on the core, and through it on EM)\n1. features\n")
        _w1 = LN.waits_on_review_owner(_wh, _wr); _wc1 = LN.count_mark(6, _wh, _wr, "gauge-x", "1.0", {}); _ww1 = LN.wip(6, _wh, _wr, "gauge-x", "1.0", {})
        _wf("gauge-x-1.0-reread3.md", "gauge-x 1.0: FINDINGS\n\n## Still open (waits on the core)\n1. features\n\n## Still open (the lane's)\n2. text\n")
        _w2 = LN.waits_on_review_owner(_wh, _wr); _ww2 = LN.wip(6, _wh, _wr, "gauge-x", "1.0", {})
        _wf("gauge-x-1.0-reread4.md", "gauge-x 1.0: FINDINGS\n\n## Still open (waits on EM: the ETIM download)\n1. features\n")
        _w3 = LN.waits_on_review_owner(_wh, _wr)
    t("LINE an element whose newest review puts every open finding under a heading that waits on the core or EM is the core's or "
      "EM's, not counted; the review before it, or one finding of the lane's beside them, and it counts (request pneu-7 item 3)",
      _w0 is None and _wc0 == "WIP" and _w1 == "core" and _wc1 == "core" and not _ww1 and _w2 is None and _ww2 and _w3 == "EM",
      f"{_w0} {_wc0} {_w1} {_wc1} {_ww1} {_w2} {_ww2} {_w3}")
    # EM 2026-11-06 (reviewer wire-1.0 finding 1): "this info should be from the National Electrical Code. how are we guessing?"
    _src = ("INSUL = {1.5: 0.7}\n"
            "def dims(size):\n    t = INSUL.get(float(size), 0.8); return t\n"
            "    fl = FERRULE_L.get(size, 10)  # and a second\n"
            "    ok = INSUL[float(size)]; c = PARAMS.get('colour'); n = OPTS.get(k, None); w = d.get(k, 3)\n"
            "# INSUL.get(size, 0.8) in a comment\n")
    _sd = VA.silent_defaults("", _src)
    t("SRC-010 flags a figure table looked up with a number to fall back on, and not a plain lookup, a None default or a comment",
      len(_sd) == 2 and _sd[0].startswith("element.py:3 INSUL.get(float(size), 0.8)") and "FERRULE_L" in _sd[1], str(_sd))
    # EM 2026-11-07: generic elements, our own vendor-neutral design of an ETIM class, built unattended
    from . import generic as GN7
    _kn = {"EC000066"}
    _ok = GN7.check("our own design: generic power contactor, AC switching (ETIM 10.0 EC000066)", "# x v1.0\n## Class values\n| Rated current | 9 A |\n", _kn)
    _nc = GN7.check("our own design: generic contactor", "# x\n## Class values\n", _kn)
    _bad = GN7.check("our own design: generic contactor (ETIM 10.0 EC999999)", "# x\n", _kn)
    _not = GN7.check("our own design: a bracket", "# x\n", _kn) + GN7.check("from the maker's datasheet (EC000066)", "# x\n", _kn)
    _std = GN7.check("our own design: generic servo drive, 400 W (no ETIM class; IEC 61800-2 values)", "# x\n## Class values\n| Rated output | 400 W |\n", _kn)
    _stdbad = GN7.check("our own design: generic servo drive (no ETIM class)", "# x\n## Class values\n", _kn)
    t("GEN-010: a product class ETIM has no class for is generic by the standard it names ('no ETIM class; IEC 61800-2 values'); 'no ETIM class' alone fails",
      not _std and _stdbad, f"{_std} {_stdbad}")
    t("GEN-010: a generic element names an ETIM class on file and states its Class values; an own design or a product isn't generic",
      _ok == [] and len(_nc) == 1 and "names no ETIM class" in _nc[0] and len(_bad) == 2 and _not == [], f"{_ok} {_nc} {_bad} {_not}")
    # request pneu-5: an inventory row's class outside classes.csv's groups, its features on file (motor-iec's EC001851), was "not on file"
    _feat = GN7.check("our own design: generic three-phase motor (ETIM 10.0 EC001851)", "# x\n## Class values\n", None)
    _none = GN7.check("our own design: generic motor (ETIM 10.0 EC999999)", "# x\n## Class values\n", None)
    t("GEN-010 (request pneu-5): a class whose features are on file (class-features.csv) is on file though classes.csv's groups leave it out; "
      "a class in neither is not", _feat == [] and len(_none) == 1 and "not an ETIM class on file" in _none[0], f"{_feat} {_none}")
    # escape, pneu-r52 (chiller 1.0 finding 1): a "generic design" rating with no feature of its class behind it passed DOC-005 and GEN-010
    _ft = {"EC002516": [("EF008207", "Operating voltage AC 60 Hz")], "EC010722": [("EF000353", "Max. tensile force")],
           "EC010413": [("EF000008", "Width")]}
    _nm7 = {"EC010413": ["Storage tank", "Pressureless storage tank"]}
    _rr = lambda p, s: [dict(property=p, value="4", unit="bar", status="generic design", source=s)]
    _ch = "our own design: generic chiller (ETIM 10.0 EC002516)"
    _r_bad = GN7.rating_rows(_ch, _rr("p_max", "generic design input of the water circuit (EC002516 has no pressure feature)"), _ft, _nm7)
    _r_ef = GN7.rating_rows(_ch, _rr("voltage", "ETIM 10.0 EC002516 class value (EF008207 Operating voltage AC 60 Hz)"), _ft, _nm7)
    _r_nm = GN7.rating_rows("our own design: generic belt tensioner (ETIM 10.0 EC010722)", _rr("max_tensile_force", "ETIM 10.0 EC010722 class value"), _ft, _nm7)
    _r_syn = GN7.rating_rows("our own design: generic storage tank (ETIM 10.0 EC010413)", _rr("p_max", "EC010413 class value (its synonym 'Pressureless storage tank')"), _ft, _nm7)
    _r_asm = GN7.rating_rows(_ch, [dict(property="p_max", value="4", unit="bar", status="assumption", source="none")], _ft, _nm7)
    _r_off = GN7.rating_rows("our own design: generic tube (ETIM 10.0 EC011348)", _rr("p_max", "EC011348 class value"), _ft, _nm7)
    _r_std = GN7.rating_rows("our own design: generic servo drive (no ETIM class; IEC 61800-2 values)", _rr("power", "IEC 61800-2 value"), _ft, _nm7) + \
             GN7.rating_rows("our own design: generic servo drive (no ETIM class; IEC 61800-2 values)", _rr("inrush", "a design input"), _ft, _nm7)
    t("GEN-010 ratings (escape pneu-r52): a 'generic design' rating whose source names no feature of its class is held (chiller's p_max); "
      "an EF code, the feature's name as the property, a quoted class synonym, an 'assumption' row and a class with no features on file pass; "
      "a no-ETIM-class row names its standard",
      len(_r_bad) == 1 and "p_max" in _r_bad[0] and not _r_ef and not _r_nm and not _r_syn and not _r_asm and not _r_off
      and len(_r_std) == 1 and "inrush" in _r_std[0], f"{_r_bad} {_r_ef} {_r_nm} {_r_syn} {_r_asm} {_r_off} {_r_std}")
    _rows = [dict(**{"class": "EC1", "description": "Gear wheel", "group": "EG020017", "domain": "mechanical", "tier": "1", "inventory": ""}),
             dict(**{"class": "EC2", "description": "Hammer-in plug", "group": "EG020045", "domain": "mechanical", "tier": "1", "inventory": ""}),
             dict(**{"class": "EC3", "description": "Bearing", "group": "EG020017", "domain": "mechanical", "tier": "1", "inventory": "bearing-ball"}),
             dict(**{"class": "EC4", "description": "Ball joint", "group": "EG020017", "domain": "mechanical", "tier": "1", "inventory": ""}),
             dict(**{"class": "EC5", "description": "Steam injector", "group": "EG015640", "domain": "fluid", "tier": "1", "inventory": ""}),
             dict(**{"class": "EC6", "description": "Compressed air filter", "group": "EG020014", "domain": "fluid", "tier": "1", "inventory": ""})]
    for r_ in _rows: r_["lane"] = GN7.LANE[r_["domain"]]; r_["trade"] = bool(GN7.TRADE.search(r_["description"])) or (r_["lane"] == "pneu" and not GN7.FLUID_POWER.search(r_["description"]))
    _nm = [r_["class"] for r_ in GN7.next_classes("mech", 0, _rows, {"EC4": ["x"]})]; _np = [r_["class"] for r_ in GN7.next_classes("pneu", 0, _rows, {})]
    t("generic work list: an ETIM class no inventory row or element covers, not a building-trade class, fluid power only for pneu",
      _nm == ["EC1"] and _np == ["EC6"], f"{_nm} {_np}")
    _es = (GN7.etim_shown(17, 6), GN7.etim_shown(2, 6), GN7.etim_shown(0, 6))
    _tr = [bool(GN7.TRADE.search(d_)) for d_ in ("Manifold for hydronic circuits", "Screw for compressed air screwdriver",
                                                 "Connecting hose for compressed air tool", "Three-way ball valve")]
    t("idle pneu r87 to r89 (core watch 2026-11-12): `inventory <lane>` lists ETIM classes even when the lane has more rows left than it "
      "shows (every row may wait on a document), the rest of n when fewer; hydronic and compressed-air-tool classes are trade classes",
      _es == (3, 4, 6) and _tr == [True, True, True, False], f"{_es} {_tr}")
    import tempfile as _tfg
    with _tfg.TemporaryDirectory() as _dg:
        _pg = os.path.join(_dg, "inventory.csv"); open(_pg, "w").write("id,lane,own_design\nrelay-x,elec,generic\nscrew-x,mech,\n")
        _g1, _g2 = VA.inventory_own("relay-x", _pg), VA.inventory_own("screw-x", _pg)
    t("DOC-004 exempts an inventory row marked generic (no maker's brief needed) and still holds an unmarked product row", _g1 is True and _g2 is False, f"{_g1} {_g2}")
    # EM 2026-11-06: his approvals come from the station 7 sign-off page through lib/approvals.csv (toolkit/approvals.py)
    from . import approvals as AP7
    _sp = "# x v1.0\n\n- **Assumption (B)**: width 40, a fit to the rail\n| strip | 10 | Assumption: the clamp's maker states it (NOT ON FILE) |\n## History\n| 1.0 | first |\n"
    _ol = AP7.open_lines(_sp, [("measure.md", "| depth | NOT ON FILE |\n| tint | NOT ON FILE (C) |\n")])
    _need = VA.doc005(_sp, brief="| depth | NOT ON FILE |\n| tint | NOT ON FILE (C) |\n")
    t("approvals: the sign-off page lists exactly the figures DOC-005 counts as EM's (2 lines, 3 figures; class C left out, class B a document wanted since 2026-11-09)",
      len(_ol) == 2 and sum(len(x["hits"]) for x in _ol) == 3 and _need and "3 need EM" in _need[2] and "1 class B want a source" in _need[2], f"{[(x['file'], x['hits']) for x in _ol]} {_need}")
    _row = lambda fig, n, d="yes", sg="· EM 2026-11-06": dict(element="x", version="1.0", kind="figure", figure=fig, figures=str(n), decision=d, signed=sg)
    _all = [_row(x["text"], len(x["hits"])) for x in _ol]
    _br = "| depth | NOT ON FILE |\n| tint | NOT ON FILE (C) |\n"
    r_all = VA.doc005(_sp, brief=_br, em=AP7.counts("x", _sp, _br, rows=_all))
    r_chg = VA.doc005(_sp.replace("width 40", "width 42"), brief=_br, em=AP7.counts("x", _sp.replace("width 40", "width 42"), _br, rows=_all))
    r_uns = VA.doc005(_sp, brief=_br, em=AP7.counts("x", _sp, _br, rows=[dict(r_, signed="") for r_ in _all]))
    _allB = _all + [_row("- **Assumption (B)**: width 40, a fit to the rail", 1)]                 # EM accepting the class B figure himself
    r_allB = VA.doc005(_sp, brief=_br, em=AP7.counts("x", _sp, _br, rows=_allB))
    t("approvals: with every line on the page accepted the element still waits for the class B figure's document ('source wanted'); EM accepting that figure too passes it; a changed figure, or a row without EM's mark, counts nothing",
      r_all and r_all[0] == "REVIEW" and r_all[2].startswith("source wanted") and r_allB and r_allB[0] == "PASS" and r_chg and r_chg[0] == "REVIEW" and r_uns and r_uns[0] == "REVIEW", f"{r_all} | {r_allB} | {r_chg} | {r_uns}")
    r_no = VA.doc005(_sp, brief=_br, em=AP7.counts("x", _sp, _br, rows=[_row(_ol[0]["text"], 1, "no")]))
    _hold = _h(7, f"DOC-005 REVIEW: {r_no[2][:110]}") if r_no else None
    t("approvals: a figure EM refused is named first and is the lane's to change, so the element counts in its WIP again",
      r_no and r_no[2].startswith("1 refused by EM") and not LN.waits_on_em(_hold) and LN.wip(6, _hold), str(r_no))
    # escape mech-r68:4, the DOC-005 half (core watch 2026-11-09): gland-m20 1.3 took a behaviour.csv whose torque reads NOT ON FILE,
    # unclassed (counted as A), and DOC-005 read only spec.md, ratings.csv and the brief: station 7 passed with a figure no page of EM's listed
    _bh = ("# behaviour.csv · x · NOT ON FILE in the header is prose\nkind,a,b,part,when,value,unit,source,note\n"
           "pin,cable,self,body,,NOT ON FILE,N·m,the gland's own tightening torque is NOT ON FILE (maker's sheet),\n"
           "pin,1,t-1,body,,0.5,N·m,drawing p. 1,the stem (thread NOT ON FILE; spec.md Open figures)\n"
           "state,run,,,,,,Assumption (C): the lamp's tint,\n")
    _sp0 = "# x v1.0\n\n## History\n| 1.0 | first |\n"
    r_b = VA.doc005(_sp0, behaviour=_bh)
    _olb = AP7.open_lines(_sp0, (), (), behaviour=_bh)
    t("DOC-005 counts behaviour.csv's open figures: an unclassed NOT ON FILE torque as A, a class C one the reviewer's, a note's pointer and the header not at all (escape mech-r68:4)",
      r_b and r_b[0] == "REVIEW" and "behaviour.csv" in r_b[2] and "1 need EM" in r_b[2] and len(_olb) == 1 and _olb[0]["file"] == "behaviour.csv"
      and _olb[0]["hits"] == [("NOT ON FILE", None)], f"{r_b} {_olb}")
    r_ba = VA.doc005(_sp0, behaviour=_bh, em=AP7.counts("x", _sp0, behaviour=_bh, rows=[_row(_olb[0]["text"], 1)]))
    r_bc = VA.doc005(_sp0, behaviour=_bh.replace("NOT ON FILE,N·m", "NOT ON FILE (B),N·m"), em=AP7.counts("x", _sp0, behaviour=_bh.replace("NOT ON FILE,N·m", "NOT ON FILE (B),N·m"), rows=[_row(_olb[0]["text"], 1)]))
    t("approvals: EM's line on a behaviour.csv row clears it, and a row changed since (a class written) comes back to the page",
      r_ba and r_ba[0] == "PASS" and r_bc and r_bc[0] == "REVIEW" and "class B wants a source" not in r_bc[2], f"{r_ba} | {r_bc}")
    _sr = [dict(element="sr", version="1.1", kind="safety", decision="yes", signed="· EM 2026-11-06")]
    t("approvals: a safety sign-off on the page counts for its own version only, and only with EM's mark",
      AP7.safety_signed("sr", "1.1", _sr) and not AP7.safety_signed("sr", "1.2", _sr) and not AP7.safety_signed("sr", "1.1", [dict(_sr[0], signed="")]))
    import tempfile as _tf7
    with _tf7.TemporaryDirectory() as _d6:
        _p6 = os.path.join(_d6, "approvals.csv"); _old6 = AP7.PATH; AP7.PATH = _p6
        try:
            open(_p6, "w", encoding="utf-8").write("element,version,kind,decision,signed\nfixture-relay,1.0,safety,yes,· EM 2026-11-06\n")
            _cs6 = {"fixture-relay": {"version": "1.0"}}
            _r6 = LN.element("fixture-relay", findings=[], cat=_cs6, tags=set(), reviews="fixture-relay 1.0: PASS", safety={"fixture-relay"}, spec="# fixture-relay v1.0\n")
            _r6b = LN.element("fixture-relay", findings=[], cat={"fixture-relay": {"version": "1.1"}}, tags=set(), reviews="fixture-relay 1.1: PASS", safety={"fixture-relay"}, spec="# fixture-relay v1.1\n")
        finally: AP7.PATH = _old6
    t("LINE passes station 7's safety sign-off from EM's page row at that version, and holds the next version for a new one",
      not any("Safety sign-off" in w for w in _r6[6][4]) and any("Safety sign-off" in w for w in _r6b[6][4]), f"{_r6[6][4]} | {_r6b[6][4]}")
    with _tf7.TemporaryDirectory() as _d7:
        _p7 = os.path.join(_d7, "approvals.csv")
        _dec = [dict(id="x--a1", kind="figure", decision="yes", note="", element="x", version="1.0", file="spec.md", line=3,
                     figure=_ol[0]["text"], figures=1, cls="B", at="2026-11-07T03:30:00Z")]
        a1 = AP7.merge(_dec, _p7); a2 = AP7.merge(_dec, _p7); a3 = AP7.merge([dict(_dec[0], decision="no", note="find the rail's\nsource")], _p7)
        _rows7 = AP7.read(_p7); _txt7 = open(_p7, encoding="utf-8").read()
    t("approvals: merge writes one signed row per page record (dated in Chicago), keeps it once, and takes EM's changed decision",
      a1 == (1, 0) and a2 == (0, 0) and a3 == (0, 1) and len(_rows7) == 1 and _rows7[0]["decision"] == "no" and _rows7[0]["signed"] == "· EM 2026-11-06"
      and "\n" not in _rows7[0]["note"], f"{a1} {a2} {a3} {_rows7}")
    # library run 2026-11-06 13:52 (refused core 3496d48): the PC's Python has no tzdata, ZoneInfo raised, and merge dated in UTC
    with _tf7.TemporaryDirectory() as _d8:
        _p8 = os.path.join(_d8, "approvals.csv")
        AP7.merge(_dec, _p8, zoneinfo=False); AP7.merge([dict(_dec[0], id="x--a2", at="2026-07-01T05:30:00Z")], _p8, zoneinfo=False)
        _r8 = {r["record"]: r["signed"] for r in AP7.read(_p8)}
    try: AP7._zone("Europe/Nowhere", zoneinfo=False); _nz = False
    except ValueError: _nz = True
    t("approvals: with no time-zone data on the PC, merge still dates EM's decisions in Chicago (CST in November, CDT in July), and a zone with no rule is refused, never dated in UTC",
      _r8.get("x--a1") == "· EM 2026-11-06" and _r8.get("x--a2") == "· EM 2026-07-01" and _nz, f"{_r8} refused={_nz}")
    import importlib.util as _iu7
    _s7 = _iu7.spec_from_file_location("autopilot_selftest7", os.path.join(_lib.ROOT, "autopilot.py")); _A7 = _iu7.module_from_spec(_s7); _s7.loader.exec_module(_A7)
    t("approvals: an unattended push that adds a row to lib/approvals.csv is refused like any line with EM's mark (autopilot pre-push)",
      _A7.em_lines("+++ b/lib/approvals.csv\n@@ -1 +1,2 @@\n+x,1.0,figure,spec.md,3,B,1,yes,width 40,,· EM 2026-11-06,x--a1\n") != [], _txt7[:200])
    # escape group 18 (core watch 2026-11-06; reviewer marker-terminal-1.0:1, tool-dmm-1.0:1, teach-pendant-1.0:1, thermostat-enc-1.0:1):
    # station 6 counted a Blender pass written before toolkit/decal.py, whose decal islands were never checked (a 2.0 mm tag edge for the print)
    _old = {"pass": True, "meshes": {"body": {"decal_island": {"faces": 2, "size_mm": [2.0, 5.7], "normal": [0, 0, 1]}}, "pin": {"tris": 12}}}
    _new = {"pass": True, "meshes": {"body": {"decal_island": {"faces": 2, "front_faces": 1, "size_mm": [5.7, 10.0], "normal": [0, -1, 0], "check": "PASS"}}}}
    t("LINE finds marker-terminal's decal island with no check (a Blender pass from before the decal check) and none in a checked one",
      LN.decal_stale(_old) == ["body"] and LN.decal_stale(_new) == [] and LN.decal_stale({"pass": True}) == [], f"{LN.decal_stale(_old)} {LN.decal_stale(_new)}")
    vp, lp, bp = (os.path.join(_lib.ELEMENTS, "gl-xr-1", "gate", "gl-xr-1-planted" + x) for x in ("-acad.json", ".lsp", ".json"))
    try:
        open(lp, "w", encoding="utf-8").write(";; gl-xr-1 v1.2  (planted)\n")
        open(vp, "w", encoding="utf-8").write(json.dumps({"pass": True, "date": "planted", "step": {"extents": [140.0, 13.1, 33.0]}, "measure_compare": []}))
        open(bp, "w", encoding="utf-8").write(json.dumps(_old))
        why = LN.tools_check("gl-xr-1", "1.2")
        t("LINE holds an element at station 6 on a Blender result (a variant's too) whose decal islands were never checked",
          any(w.startswith(LN.DECAL_STALE) and "gl-xr-1-planted.json" in w for w in why), str(why))
        open(bp, "w", encoding="utf-8").write(json.dumps(_new))
        why = LN.tools_check("gl-xr-1", "1.2")
        t("LINE lets a variant's checked decal island through station 6", not any("gl-xr-1-planted.json" in w for w in why), str(why))
    finally:
        for f in (vp, lp, bp):
            if os.path.exists(f): os.remove(f)
    # escape group 17 (core watch 2026-11-07; reviewer relay-ice-cube-1.1:2): station 6 passed with the element's own pose check
    # failing on file, and read no result of a variant without an AutoCAD gate (the cutaway)
    _g = os.path.join(_lib.ELEMENTS, "gl-xr-1", "gate"); _q = os.path.join(_lib.ELEMENTS, "gl-xr-1", "qa")
    pp, cp, qp = (os.path.join(_g, "gl-xr-1-poses.json"), os.path.join(_g, "gl-xr-1-plantcut.json"), os.path.join(_q, "gl-xr-1-plantcut-poses.json"))
    _mk = [p for p in (_g, _q) if not os.path.isdir(p)]
    try:
        for p in _mk: os.makedirs(p)
        open(pp, "w", encoding="utf-8").write(json.dumps({"id": "gl-xr-1", "pass": False, "checks": [
            {"check": "released: arm on the stop", "ok": True}, {"check": "manual: the button faces the card", "ok": False}]}))
        open(cp, "w", encoding="utf-8").write(json.dumps({"id": "gl-xr-1-plantcut", "pass": False, "meshes": {}}))
        open(qp, "w", encoding="utf-8").write(json.dumps({"poses": []}))
        why = LN.result_holds("gl-xr-1")
        t("LINE holds an element at station 6 on its own pose check failing on file, and on a failed result of a variant with no AutoCAD gate (a cutaway); a pose file with no verdict holds nothing",
          any(w.startswith("pose check failed on file: gate/gl-xr-1-poses.json (1 of 2") for w in why)
          and any(w == "Blender gate failed on file: gate/gl-xr-1-plantcut.json" for w in why) and len(why) == 2
          and any(w.startswith("pose check failed") for w in LN.tools_check("gl-xr-1", "1.2")), str(why))
        open(pp, "w", encoding="utf-8").write(json.dumps({"id": "gl-xr-1", "pass": True, "checks": [{"check": "x", "ok": True}]}))
        open(cp, "w", encoding="utf-8").write(json.dumps({"id": "gl-xr-1-plantcut", "pass": True, "meshes": {}}))
        t("LINE lets a passed pose check and a passed cutaway result through station 6", LN.result_holds("gl-xr-1") == [], str(LN.result_holds("gl-xr-1")))
    finally:
        for f in (pp, cp, qp):
            if os.path.exists(f): os.remove(f)
        for p in reversed(_mk):
            try: os.rmdir(p)
            except OSError: pass
    _co = _h(6, LN.DECAL_STALE + " (toolkit/decal.py): gate/marker-terminal.json decal islands body carry no check; the core re-gates it in Blender")
    t("LINE: an element held at 6 only for the core's Blender re-gate is out of its lane's WIP count; with a hold of the lane's own beside it, it counts",
      LN.waits_on_core(_co) and not LN.wip(5, _co)
      and LN.wip(5, _h(6, _co[4][0], "Godot QA failed")) and not LN.waits_on_core(_h(6, "Blender gate failed")))
    # request mech-4 (core watch 2026-11-07): an element reviewed at its version (FINDINGS) whose other holds at 7 have cleared waits on
    # the reviewer coming back, which reviewer.md 4b never does: the board lists it (line.rereview_due), and only it
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, "elements"))
        for f, body in (("bench-x-1.3.md", "bench-x 1.3: FINDINGS\n\n1. Held for EM only."), ("bench-x-1.30.md", "bench-x 1.30: PASS"),
                        ("relay-s-1.0.md", "relay-s 1.0: REVIEWED, EM to sign"), ("done-x-1.1.md", "done-x 1.1: FINDINGS"),
                        ("done-x-1.1-signed.md", "done-x 1.1: PASS"), ("old-x-1.0.md", "old-x 1.0: FINDINGS")):
            open(os.path.join(td, "elements", f), "w", encoding="utf-8").write(body)
        _rv = lambda e, v: _h(7, f'no reviewer line "{e} {v}: PASS" in lib/reviews/')
        _rr = lambda e, v, nxt: LN.rereview_due(e, v, nxt, root=td)
        t("LINE (request mech-4): an element reviewed at its version with FINDINGS (or a safety element's REVIEWED, EM to sign), held at 7 only"
          " by the reviewer's line, is listed for a re-read; one with EM's figures still open, one with no review at its version, one with a"
          " PASS on file (a later -signed review), and 1.30's PASS read as 1.3's are not",
          _rr("bench-x", "1.3", _rv("bench-x", "1.3")) and _rr("relay-s", "1.0", _rv("relay-s", "1.0"))
          and not _rr("bench-x", "1.3", _h(7, "DOC-005 REVIEW: open figures", _rv("bench-x", "1.3")[4][0]))
          and not _rr("new-x", "1.0", _rv("new-x", "1.0")) and not _rr("old-x", "1.1", _rv("old-x", "1.1"))
          and LN.review_verdict("done-x", "1.1", td) == "PASS" and LN.review_verdict("bench-x", "1.3", td) == "FINDINGS"
          and not _rr("bench-x", "1.3", _h(6, "Blender gate failed")),
          f'{LN.review_verdict("bench-x", "1.3", td)} {LN.review_verdict("done-x", "1.1", td)}')
    # ESCAPE (reviews of gl-xr-1 1.2 and cable-pwr-480 1.1): DOC-004 skipped any baseline with 'our own' or 'own design' anywhere in it
    t("DOC-004 exempts only a baseline that starts 'own' / 'our own' (gl-xr-1's 'envelope from a published spec sheet ... the shape is our own' needs a brief)",
      not VA.own_design("display-glasses envelope from a published spec sheet (155 x 50.1 x 56.5 mm folded); the shape is our own")
      and not VA.own_design("cord: 14/4 SOOW class (cord datasheet); plug envelope own design to mate port-pwr-480")
      and VA.own_design("own design: cage 5.1 x 10.4 x 7.5") and VA.own_design("Our own design: a stand") and VA.own_design("own (EM 2026-11-03): 90 x 105 x 60"))
    # ESCAPE group 19 (elec r6:1, thermostat-enc 1.0): DOC-004 took the baseline's words for an element the inventory lists as a product
    # class (own_design not yes); an element with no inventory row is still judged by its words
    with tempfile.TemporaryDirectory() as td:
        ip = os.path.join(td, "inventory.csv")
        open(ip, "w", encoding="utf-8").write("id,lane,own_design\n# a comment,,\nthermo-x,elec,\nbracket-x,mech,yes\n")
        _io19 = (VA.inventory_own("thermo-x", ip), VA.inventory_own("bracket-x", ip), VA.inventory_own("seal-x", ip))
    t("DOC-004 (escape group 19): 'our own design' exempts no element whose lib/inventory.csv row isn't own_design=yes; a row marked yes,"
      " or no row (a common part), is judged by its baseline",
      _io19 == (False, True, None) and not VA.own_design("our own design: a thermostat housing", _io19[0])
      and VA.own_design("our own design: a bracket", _io19[1]) and VA.own_design("own design: a seal", _io19[2])
      and not VA.own_design("from the maker's datasheet", True), str(_io19))
    # round 10 return: the build wrote out/preview-male,.png for plug-m12 and insert-m12 (a first word with its comma)
    from . import library as LB
    pv = ["male A-coded (threaded sleeve)", "female A-coded (threaded nut)", "male, pin 2 bent"]
    r = LB.preview_names(pv)
    t("preview names: plug-m12's 'male, pin 2 bent' writes no comma, and two names that share 'male' take their whole names",
      r == ["male-a-coded-threaded-sleeve", "female", "male-pin-2-bent"] and LB.preview_names(["D-coded x", "1.5 mm²"]) == ["D-coded", "1.5"]
      and all(re.fullmatch(r"[a-z0-9-]+", x) for x in r), str(r))
    # request mech-1 (2026-11-06): a run's CLASS and the PVC layers change no number the gates read; the PVC layers have a colour everywhere
    from . import fillet as FL, qa as QA, cadout as CO, preview as PV
    class _Run: CLASS = "run"
    class _Dev: CLASS = "device"
    bl = open(__import__("os").path.join(__import__("os").path.dirname(__file__), "blender", "gate.py")).read()
    one = re.search(r"ONE_SEGMENT = \{([^}]*)\}", bl); one = one and re.findall(r'"([^"]+)"', one.group(1))
    t("CLASS run: a duct moved from device keeps its fillet radius, budgets and Blender bevel segments; M-*-PVC render as M-*-PA",
      FL.radius(None, _Run) == FL.radius(None, _Dev) and QA.budgets(_Run)[0] == QA.budgets(_Dev)[0] and one and ("run" in one) == ("device" in one)
      and all(CO.MATERIALS.get(f"M-{c}-PVC") == CO.MATERIALS.get(f"M-{c}-PA") and PV.colour(f"M-{c}-PVC") == PV.colour(f"M-{c}-PA") != "#999" for c in ("WHITE", "GREY")),
      f"r {FL.radius(None, _Run)} budget {QA.budgets(_Run)} one {one}")
    # round 13 return (A.b): acad-gate.py could key duct-40x60's finger exclusion only on the id and a height, the layer being the only
    # name a primitive carried; a part name rides beside the layer (Prims.parts), through transform and placing, and reaches no output
    from .prims import transform as _tf
    try:
        P = Prims(); P.box("M-WHITE-PA", 0, 0, 0, 100, 2, 40); f_ = P.box("M-WHITE-PA", 0, 2, 0, 10, 25, 2, part="duct-finger")
        T = _tf(P, (5, 0, 0), 90.0, lambda n: f"d1.{n}", base=7)
        ok = (P.parts == {f_: "duct-finger"} and all(isinstance(q[0], str) and "finger" not in q[0] for q in P)
              and T.parts == {f_ + 7: "d1.duct-finger"} and _tf(P).parts == {f_: "duct-finger"})
        got = f"{P.parts} {T.parts}"
    except TypeError as e: ok, got = False, str(e)
    t("PRIMS: a part name (part=\"duct-finger\") is kept beside the layer, never in it, and follows its primitive through transform and a host's base",
      ok, got)
    # round 14 return (B a): relay-ice-cube-2co's cutaway Blender result came from a scratch glb, so no run could redo it; a gated variant's
    # glb is made by a command on file (build.py glb <id> <suffix> k=v ...), named for the result it feeds, its parameters checked
    import tempfile, struct as _st
    with tempfile.TemporaryDirectory() as td:
        try:
            pth = LB.variant_glb("relay-ice-cube-2co", "cutaway", {"view": "cutaway", "socket": False}, folder=td)
            with open(pth, "rb") as f: f.read(12); jl, _ = _st.unpack("<II", f.read(8)); js = json.loads(f.read(jl))
            cut = {n["name"] for n in js["nodes"]}
            pp = LB.variant_glb("relay-ice-cube-2co", "planted", {}, folder=td)
            with open(pp, "rb") as f: f.read(12); jl, _ = _st.unpack("<II", f.read(8)); prod = {n["name"] for n in json.loads(f.read(jl))["nodes"]}
            refused = []
            for sfx, kv in (("cutaway", {"veiw": "cutaway"}), ("Cut away", {})):
                try: LB.variant_glb("relay-ice-cube-2co", sfx, kv, folder=td)
                except ValueError: refused.append(sfx)
            ok = (os.path.basename(pth) == "relay-ice-cube-2co-cutaway.glb" and cut != prod and len(cut) < len(prod) and refused == ["cutaway", "Cut away"])
            got = f"{os.path.basename(pth)} nodes {len(cut)} vs {len(prod)} refused {refused}"
        except Exception as e: ok, got = False, repr(e)
    t("GLB: build.py glb writes relay-ice-cube-2co's cutaway as gate/relay-ice-cube-2co-cutaway.glb (the Blender result's name), fewer walls than the product;"
      " a misspelt parameter or a bad suffix is refused", ok, got)
    # round 15's return, 1: main and core had two merge bases (main merged core, then core merged an older main), and owners
    # diffed from one of them, so main's own library files counted as the core's (17 outside)
    import tempfile, os, subprocess as _sp, importlib.util as _iu, contextlib as _cl, io as _io
    try:
        _bs = _iu.spec_from_file_location("build_selftest", os.path.join(_lib.ROOT, "build.py")); BU = _iu.module_from_spec(_bs); _bs.loader.exec_module(BU)
        with tempfile.TemporaryDirectory() as td:
            g = lambda *a: _sp.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "init.defaultBranch=main", *a], cwd=td, capture_output=True, text=True, check=True).stdout
            def w(f, x): os.makedirs(os.path.dirname(os.path.join(td, f)), exist_ok=True); open(os.path.join(td, f), "w", encoding="utf-8").write(x)
            g("init", "-q"); w("lib/OWNERS.csv", "path,owner,note\nlib/core.txt,core,\nlib/lib.txt,library,\n"); w("lib/core.txt", "0"); w("lib/lib.txt", "0")
            g("add", "-A"); g("commit", "-qm", "c0"); g("branch", "core")
            g("checkout", "-q", "core"); w("lib/core.txt", "1"); g("commit", "-qam", "k1")
            g("checkout", "-q", "main"); w("lib/lib.txt", "1"); g("commit", "-qam", "m1"); m1 = g("rev-parse", "HEAD").strip()
            g("merge", "-q", "--no-ff", "-m", "merge core", "core")
            g("checkout", "-q", "core"); g("merge", "-q", "--no-ff", "-m", "merge main", m1); w("lib/core.txt", "2"); g("commit", "-qam", "k3")
            nb = len(g("merge-base", "--all", "main", "core").split())
            buf = _io.StringIO()
            with _cl.redirect_stdout(buf): clean = BU.owners("core", "main", "core", here=os.path.join(td, "lib"))
            w("lib/lib.txt", "core wrote this"); w("lib/elements/new-x/metadata.json", "{}"); g("add", "-A"); g("commit", "-qm", "k4")
            with _cl.redirect_stdout(buf): dirty = BU.owners("core", "main", "core", here=os.path.join(td, "lib"))
        named = "no row: lib/elements/new-x/ (1 file(s)" in buf.getvalue()
        ok, got = nb == 2 and clean and not dirty and named, f"bases {nb} clean {clean} dirty {dirty} named {named}: {buf.getvalue()[-300:]}"
    except Exception as e: ok, got = False, repr(e)
    t("OWNERS: with two merge bases (main merged core, core merged an older main) main's own files are not counted as the branch's;"
      " a file the branch itself changed outside its lane still is (build.branch_files); an element folder no row covers is named"
      " (round 23's return 4.3: frl's and vacuum's stubs)", ok, got)
    # round 15's return, 2: a variant's gate run named after its element wrote no metrics row (lock.py looked for <element>.json)
    try:
        _ls = _iu.spec_from_file_location("lock_selftest", os.path.join(_lib.ROOT, "lock.py")); LK = _iu.module_from_spec(_ls); _ls.loader.exec_module(LK)
        import time as _ti
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, "elements", "relay-x", "gate")); os.makedirs(os.path.join(td, "metrics"))
            open(os.path.join(td, "metrics", "core.csv"), "w", encoding="utf-8").write("date,round,element,version,gate,result,first_pass\n")
            old = os.path.join(td, "elements", "relay-x", "gate", "relay-x.json"); open(old, "w").write('{"pass": true}'); os.utime(old, (1, 1))
            t0 = _ti.time()
            open(os.path.join(td, "elements", "relay-x", "gate", "relay-x-cutaway.json"), "w").write('{"pass": true}')
            _h = LK.HERE; LK.HERE = td
            try:
                row = LK.metrics_row("blender", "library", "relay-x", t0, "15")
                open(os.path.join(td, "elements", "relay-x", "gate", "relay-x-side.json"), "w").write('{"pass": true}')
                two = LK.metrics_row("blender", "library", "relay-x", t0, "15")
            finally: LK.HERE = _h
            body = open(os.path.join(td, "metrics", "core.csv"), encoding="utf-8").read()
        ok, got = bool(row) and row["element"] == "relay-x-cutaway" and row["result"] == "PASS" and two is None and body.count("relay-x-cutaway") == 1, f"{row} {two}"
    except Exception as e: ok, got = False, repr(e)
    t("LOCK: a variant's run named after its element still writes its row, named after the one variant result it wrote; two fresh variants: no guess (lock.metrics_row)", ok, got)
    # round 35's return (core watch 2026-11-13): from 03:53 every AutoCAD run in every lane held the lock its full five minutes on a COM
    # call AutoCAD rejected and wrote no result (22 runs, about 112 minutes); nothing told the next lane not to try
    try:
        import io, contextlib
        n0 = 1_000_000.0
        r1 = LK.down_next(None, 1, 305, False, n0); r2 = LK.down_next(r1, 1, 312, False, n0 + 400)
        alone = LK.down_refuse(r1, n0 + 60); refused = LK.down_refuse(r2, n0 + 460); probe = LK.down_refuse(r2, n0 + 400 + LK.DOWN_WAIT_S + 1)
        cleared = [LK.down_next(r2, 0, 305, True, n0 + 3000), LK.down_next(r2, 1, 320, True, n0 + 3000), LK.down_next(r2, 75, 3, False, n0 + 3000)]
        with tempfile.TemporaryDirectory() as td:
            json.dump(r2, open(os.path.join(td, "autocad-down.json"), "w")); _ld = LK.lock_dir; LK.lock_dir = lambda: td
            _now = LK.time.time; LK.time.time = lambda: n0 + 460
            # the case is measured the same with and without COMPLEXES_UNATTENDED (core watch 2026-11-13: round 36's core merge read
            # 340/341 under autopilot, where lock.py refuses a `python -c` as "not a gate" (126) before the down check; core watch's
            # clone, without the variable, read 341/341): attended with any command, unattended with a gate gate_ok accepts
            _ev = os.environ.get("COMPLEXES_UNATTENDED")
            codes = {}
            try:
                for mode, cmd in (("attended", ["python", "-c", "raise SystemExit(9)"]),
                                  ("unattended", ["python", "lib/acad-gate.py", "x"])):
                    if mode == "unattended": os.environ["COMPLEXES_UNATTENDED"] = "1"
                    else: os.environ.pop("COMPLEXES_UNATTENDED", None)
                    buf = io.StringIO()
                    with contextlib.redirect_stdout(buf): codes[mode] = LK.main(["run", "autocad", "mech", "x", "--"] + cmd)
            finally:
                LK.lock_dir = _ld; LK.time.time = _now
                if _ev is None: os.environ.pop("COMPLEXES_UNATTENDED", None)
                else: os.environ["COMPLEXES_UNATTENDED"] = _ev
            ran = os.path.exists(os.path.join(td, "usage.csv"))
        code = codes.get("attended")
        ok = (r2["streak"] == 2 and not alone and "last 2 runs" in refused and probe == "" and cleared == [None, None, None]
              and codes == {"attended": LK.BUSY, "unattended": LK.BUSY} and not ran)
        got = f"{r2} alone={alone!r} probe={probe!r} cleared={cleared} codes={codes} ran={ran}"
    except Exception as e: ok, got = False, repr(e)
    t("LOCK: two AutoCAD runs in a row that held the lock 240 s or more and wrote no result make the next run busy at once (exit 75, the"
      " command not started) for 30 minutes, then one try goes through; one alone, a run that wrote a result (pass or fail), or a quick"
      " exit clears it (round 35's return; lock.down_next, down_refuse)", ok, got)
    # request panel-8 (core watch 2026-11-11): an assembly's twin started Godot outside the lock, and the lock refused it unattended;
    # and an assembly's gate (a panel's) wrote no metrics row: metrics_row looked under lib/elements/ alone, and the lane had no file
    try:
        _tw = ["python", "lib/build.py", "twin", "pnl-motor-starter", "--smoke"]
        ok_tw = LK.gate_ok(_tw) and not LK.gate_ok(_tw[:4]) and not LK.gate_ok(["python", "lib/build.py", "twin", "x;rm", "--smoke"]) \
            and not LK.gate_ok(["python", "lib/build.py", "selftest", "x", "--smoke"]) and LK.gate_ok(["python", "lib/godot-qa.py", "x"])
        with tempfile.TemporaryDirectory() as td:
            ad = os.path.join(td, "assemblies", "pnl-x"); os.makedirs(os.path.join(ad, "gate")); os.makedirs(os.path.join(td, "metrics")); os.makedirs(os.path.join(td, "elements"))
            open(os.path.join(ad, "assembly.py"), "w").write('ID = "pnl-x"; VERSION = "0.5"; HERE = "."\n')
            t0 = _ti.time(); open(os.path.join(ad, "gate", "pnl-x.json"), "w").write('{"pass": false}')
            _h = LK.HERE; LK.HERE = td
            try: arow = LK.metrics_row("blender", "panel", "pnl-x", t0, "8")
            finally: LK.HERE = _h
            body = open(os.path.join(td, "metrics", "panel.csv"), encoding="utf-8").read().splitlines()
        ok = ok_tw and bool(arow) and arow["version"] == "0.5" and arow["result"] == "FAIL" and body[0].startswith("date,round,element,version,gate") and len(body) == 2
        got = f"twin {ok_tw} row {arow} file {body}"
    except Exception as e: ok, got = False, repr(e)
    t("LOCK: an assembly's twin smoke run is a gate the lock starts unattended (python lib/build.py twin <id> --smoke, nothing else); an"
      " assembly's gate writes its metrics row, version from assembly.py, into the lane's file, made with its header (request panel-8)", ok, got)
    # request panel-9 1, an ESCAPE (core watch 2026-11-11): port-m12-a's L key gated clean at the element's origin, and placed at 1.5 m
    # in a panel its CSG needle (2.7e-5 mm thick) collapsed in the glb's float32 metres: Blender counted a degenerate triangle. The
    # writer now flips or merges every needle thinner than cadout.NEEDLE_MM, inside one solid, the shell kept closed
    try:
        from . import cadout as _co
        import struct as _st, collections as _cc
        def _deg(path, node):
            b = open(path, "rb").read(); jl = _st.unpack("<I", b[12:16])[0]; js = json.loads(b[20:20 + jl]); bn = b[28 + jl:]; n = 0
            for nd in js["nodes"]:
                if nd["name"] != node: continue
                for pr in js["meshes"][nd["mesh"]]["primitives"]:
                    a, i_ = js["accessors"][pr["attributes"]["POSITION"]], js["accessors"][pr["indices"]]
                    V = np.frombuffer(bn, np.float32, a["count"] * 3, js["bufferViews"][a["bufferView"]]["byteOffset"]).reshape(-1, 3).astype(float)
                    I = np.frombuffer(bn, np.uint32, i_["count"], js["bufferViews"][i_["bufferView"]]["byteOffset"]).reshape(-1, 3)
                    n += int((0.5 * np.linalg.norm(np.cross(V[I[:, 1]] - V[I[:, 0]], V[I[:, 2]] - V[I[:, 0]]), axis=1) < 1e-12).sum())   # Blender's gate: area < 1e-12 m2
            return n
        def _panel():
            P = Prims(); P.assembly = True
            _lib.place(P, dict(element="port-m12-a", version="1.4", tag="p-x2", parent="", x=1524.0, y=150.0, z=1550.0, yaw=90.0, params={"coding": "L"}))
            return P
        with tempfile.TemporaryDirectory() as td:
            g = os.path.join(td, "p.glb"); _un = _co.unneedle
            _co.unneedle = lambda x, **k: x
            try: _co.write_glb(g, _panel(), "p"); before = _deg(g, "p-x2.body")
            finally: _co.unneedle = _un
            _co.write_glb(g, _panel(), "p"); after = _deg(g, "p-x2.body")
        thin, open_ = {}, {}
        for cod in ("D", "L"):
            gr = _co._tris(_lib.load("port-m12-a").build(coding=cod), {})
            thin[cod] = sum(_co._height(*q[1:]) < _co.NEEDLE_MM for v in gr.values() for q in v)
            _E2 = _cc.Counter((q[0],) + tuple(np.round(q[1 + j], 4)) + tuple(np.round(q[1 + (j + 1) % 3], 4)) for v in gr.values() for q in v for j in range(3))
            open_[cod] = sum(1 for e, c in _E2.items() if c != 1 or _E2.get(e[:1] + e[4:7] + e[1:4], 0) != 1)
        ok, got = before >= 1 and after == 0 and thin == {"D": 0, "L": 0} and open_ == {"D": 0, "L": 0}, f"placed L: {before} -> {after} degenerate; needles {thin}; open edges {open_}"
    except Exception as e: ok, got = False, repr(e)
    t("ESCAPE panel-9 1: port-m12-a's L key placed at 1.5 m (pnl-motor-starter's p-x2) writes no triangle Blender reads as degenerate; without"
      " cadout.unneedle it writes one; the D and L builds keep no needle thinner than NEEDLE_MM and every shell closed", ok, got)
    # request mech-12 (core watch 2026-11-11): the gate's glb extents took each node's own translation, so a nested node (turntable's
    # rollers on its deck, P.parents) was read where its parent stands; cadout.glb_extents walks the node tree
    try:
        P = Prims(); P.box("node:deck|M-STEEL", -50, -50, 0, 100, 100, 10)
        P.cyl("node:roller|M-BLACK-PA", (-20, 0, 15), (20, 0, 15), 10.0); P.pivot("roller", "rotate", (0, 0, 15), axis=(1, 0, 0), range=(0, 360)); P.parents["roller"] = "deck"
        P.pivot("deck", "rotate", (0, 0, 5), axis=(0, 0, 1), range=(0, 360))
        with tempfile.TemporaryDirectory() as td:
            g = os.path.join(td, "n.glb"); _co.write_glb(g, P, "n"); b = open(g, "rb").read(); jl = _st.unpack("<I", b[12:16])[0]; js = json.loads(b[20:20 + jl])
        lo, hi = _co.glb_extents(js); flat = max(nd.get("translation", [0, 0, 0])[1] + js["accessors"][js["meshes"][nd["mesh"]]["primitives"][0]["attributes"]["POSITION"]]["max"][1] for nd in js["nodes"]) * 1000
        nested = any("children" in nd for nd in js["nodes"])
        ok, got = nested and abs(hi[2] - 25.0) < 0.01 and abs(lo[2]) < 0.01 and flat < 24.0, f"nested {nested} tree z {lo[2]:.3f}..{hi[2]:.3f}, flat reading's top {flat:.3f}"
    except Exception as e: ok, got = False, repr(e)
    t("glb extents: a nested node counts with its parents' transforms (cadout.glb_extents: a roller on a deck reaches z 25; the flat reading,"
      " each node's own translation, stops short) (request mech-12)", ok, got)
    # request elec-4 (core watch 2026-11-07): lib/pose-check.py posed the flag by the card's 1.2 (its pivot runs 0..3.6) and the door-lock
    # 180 mm (a 0..4 slider since 1.1), and read the armature's bounding box, whose tip reached the core's plane while its face over the
    # core stayed 0.68 open; and the lanes could not run it unattended. The core's toolkit/poses.py, run as `build.py poses <id>`
    from . import poses as PO
    pv = {"flag": {"kind": "translate", "range": (0, 3.6)}, "door-lock": {"kind": "translate", "range": (0, 4.0)},
          "armature": {"kind": "rotate", "range": (0, 4.06)}, "coil": {"kind": "emissive", "range": (0, 1)}, "case": {"kind": "fixed", "range": (0, 0)}}
    a_ = PO.amounts(pv)
    t("POSES: every moving node is posed by its own pivot's range end (flag 3.6, door-lock 4.0), never a fixed number; lamps and fixed nodes not at all",
      a_ == {"flag": 3.6, "door-lock": 4.0, "armature": 4.06}, a_)
    hinge = {"kind": "rotate", "origin": (10.54, -36.6, 11.9), "axis": (1, 0, 0), "range": (0, 4.06)}
    plate = PO.move(PO.pts_of(((6.04, -37.6, -5.0), (1, 0, 0), (0, 1, 0), (0, 0, 1), 9.0, 1.0, 17.9), "obox", 21), hinge, 4.06)
    A_ = np.array(plate); clo, chi = np.array((8.54, -35.4, 4.5)), np.array((12.54, -16.0, 8.5))
    box_g = PO.gap((None, "", "obox", A_.min(axis=0), A_.max(axis=0)), (None, "", "cyl", clo, chi), 1); face_g = PO.face_gap(A_, clo, chi, 1)
    t("POSES: a plate turned about its top hinge until its tip reaches the core's plane: the bounding box reads closed, the face over the core"
      " reads the 0.68 left open (face_gap)", box_g is not None and abs(box_g) < 0.1 and face_g is not None and 0.6 < face_g < 0.8, f"box {box_g} face {face_g}")
    flat = PO.move(PO.pts_of(((6.04, -37.6, -5.0), (1, 0, 0), (0, 1, 0), (0, 0, 1), 9.0, 1.0, 17.9), "obox", 21), {**hinge, "kind": "translate", "axis": (0, 1, 0)}, 1.2)
    t("POSES: the same plate moved square onto the core reads closed over the core (face_gap 0)", abs(PO.face_gap(np.array(flat), clo, chi, 1)) < 0.01, PO.face_gap(np.array(flat), clo, chi, 1))
    # escape group 24 (core watch 2026-11-07, review relay-ice-cube-1.3:1): "the door holds the button in" passed with the door 1.76 in
    # front of the pressed button (door_back_y -39.12, button -37.36): one-sided. And the manual push was bounded only from below
    t("POSES: the door 1.76 in front of the pressed button does not hold it (relay-ice-cube-2co 1.3: back -39.12, button front -37.36; holds)",
      not PO.holds(-39.12, -37.36), PO.holds(-39.12, -37.36))
    t("POSES: the door at the button face, 0.3 in front, or 0.03 into it holds it; 0.2 into it is an overlap (holds, both sides)",
      PO.holds(-37.36, -37.36) and PO.holds(-37.66, -37.36) and PO.holds(-37.33, -37.36) and not PO.holds(-37.16, -37.36))
    t("POSES: a push 0.3 past the card's 1.2 travel overtravels it; 1.24 is within 0.05; 1.1 falls short (push_ok, both sides)",
      not PO.push_ok(1.5, 1.2) and PO.push_ok(1.24, 1.2) and not PO.push_ok(1.1, 1.2), (PO.push_ok(1.5, 1.2), PO.push_ok(1.24, 1.2), PO.push_ok(1.1, 1.2)))
    # escape group 9 (core watch 2026-11-07, review port-m12-a-1.4:1): the port's nut and its flange stood 1.9 apart with nothing in the
    # wall between them (the M16 panel-thread body not modelled), and every check passed. GEO-070: the fixed solids form one body
    def port_(body):
        P = Prims(); P.cyl("M-ZINC", (0, 0, 0), (0, -3.0, 0), 9.0); P.cyl("M-ZINC", (0, 1.9, 0), (0, 4.9, 0), 9.0)
        if body: P.cyl("M-ZINC", (0, -3.0, 0), (0, 1.9, 0), 8.0)
        return P
    r = G.bodies(port_(False), "test")
    t("GEO-070 flags a port whose nut and flange stand 1.9 apart with no body through the wall (port-m12-a 1.4)",
      any(x[0] == "REVIEW" and "1.90 mm" in x[3] for x in r), r[0][3] if r else "")
    r = G.bodies(port_(True), "test"); t("GEO-070 passes the same port with its M16 body through the wall", r and all(x[0] == "PASS" for x in r), r[0][3] if r else "")
    P = port_(True); P.box("node:btn|M-RED-PA", -2, -12, -2, 4, 4, 4); P.pivot("btn", "translate", (0, -8, 0), (0, 1, 0), (0, 3))
    r = G.bodies(P, "test"); t("GEO-070 leaves a moving part to its pivot (a button 5 in front of the face, MOT-010 / MOT-020 judge it)", r and all(x[0] == "PASS" for x in r), r[0][3] if r else "")
    P = port_(True); s0 = len(P); P.box("M-STEEL", 20, 0, 0, 2, 2, 2); P.box("M-STEEL", 30, 0, 0, 2, 2, 2); _owned(P, s0, len(P), "kid")
    P.box("M-STEEL", 9, 0, -1, 11, 1, 1)
    r = G.bodies(P, "test"); t("GEO-070 judges a host on how it joins a placed element, not on the element's own parts", r and all(x[0] == "PASS" for x in r), r[0][3] if r else "")
    P = Prims(); P.box("M-STEEL", 0, 0, 0, 100, 50, 100); P.box("node:door|M-STEEL", 0, -2, 0, 100, 2, 100); P.pivot("door", "rotate", (0, -1, 0), (0, 0, 1), (0, 110))
    P.cyl("node:hinge|M-ZINC", (-3, -3, 10), (-3, -3, 90), 3.0); P.pivot("hinge", "fixed", (-3, -3, 10))
    r = G.bodies(P, "test"); t("GEO-070 joins a hinge to its cabinet through the door it carries, at rest (enc-fs)", r and all(x[0] == "PASS" for x in r), r[0][3] if r else "")
    # escape group 8 (core watch 2026-11-07, review clamp-screw-1.1:4): the clamp's screw turned 720 degrees at lead 0.5, 1.0 mm into a
    # 5.0 window, and MOT-010 passed it: no conductor of its range was ever clamped. MOT-030: the stroke closes the window
    def clamp_(rng, placed=False):
        P = Prims(); P.box("node:self|M-ZINC", -2.5, 0, -6.4, 5, 7.5, 10.4)
        P.cyl("node:screw|M-ZINC", (0, 3.75, -5.8), (0, 3.75, -2.5), 1.5)
        P.pivot("screw", "rotate", (0, 3.75, 0), axis=(0, 0, 1), range=rng, unit="deg", lead=0.5)
        P.pivot("self", "contact", (0, 0, 0), axis=(0, 1, 0), range=(0.5, 7.5), unit="mm", gender="clamp", size_min=0.33, size_max=5.26, window=(4.0, 5.0))
        if not placed: return P
        H = Prims(); H.parents = {}; H.box("M-PA", -10, -10, -10, 20, 20, 3)
        from .prims import transform as _tf8; tp = _tf8(P, (0, 0, 0), 0.0, lambda n: "clamp-1" if n == "self" else f"clamp-1.{n}"); H.extend(tp); H.pivots.update(tp.pivots); H.parents["clamp-1"] = ""
        return H
    r = G.screw_stroke(clamp_((0, 720)), "test")
    t("MOT-030 flags a clamp screw whose 2 turns at lead 0.5 close 1.0 of a 5.0 window (clamp-screw 1.1)", any(x[0] == "REVIEW" and "needs 4.35" in x[3] for x in r), r[0][3] if r else "")
    r = G.screw_stroke(clamp_((0, 3240)), "test"); t("MOT-030 passes the same screw at 9 turns (4.5 closes the window onto a 0.33 mm2 conductor)", r and all(x[0] == "PASS" for x in r), r[0][3] if r else "")
    r = G.screw_stroke(clamp_((0, 720), placed=True), "test"); t("MOT-030 leaves a placed clamp to its own check, not its host's (term-4mm)", not r, str(r))
    from toolkit import library as LB_; r = G.screw_stroke(LB_.load("clamp-screw").build(), "clamp-screw")
    t("MOT-030 on the element on file: clamp-screw's screw does not close its window (the escape itself)", any(x[0] == "REVIEW" for x in r) or "1.1" != LB_.load("clamp-screw").VERSION, r[0][3] if r else "")
    try: PO.run("no-such-element", write=False); ok_ = False
    except ValueError: ok_ = True
    t("POSES: build.py poses refuses an element with no pose check of its own (toolkit/poses.CHECKS)", ok_)
    # request elec-6 (2026-11-08): an interlock, motion.csv mode "requires": the slider closes only over the pressed button
    Pq = Prims(); Pq.box("node:btn|M-RED", 4, -40, 0, 4, 4, 4); Pq.pivot("btn", "translate", (6, -40, 2), axis=(0, 1, 0), range=(0, 1.5))
    Pq.box("node:slider|M-BLACK-PA", 0, -40, 0, 2, 1, 2); Pq.pivot("slider", "translate", (1, -40, 1), axis=(1, 0, 0), range=(0, 4.0))
    Pq.box("M-GREY-PA", -10, -30, -10, 30, 10, 30)                                                  # the body behind both
    _free = G.motion(Pq, "test-interlock", rows=[])
    _req = G.motion(Pq, "test-interlock", rows=[dict(scope="test-interlock", leader="btn", follower="slider", mode="requires", stop="1.5", note="")])
    t("MOT-010 'requires': the slider hits the button at rest and is blocked; with the button held pressed (the interlock) it closes over it clear",
      any(x[0] == "FAIL" and x[2] == "slider" for x in _free) and not any(x[0] == "FAIL" for x in _req),
      f"{[x[3][:60] for x in _free if x[0] == 'FAIL']} {[x for x in _req if x[0] == 'FAIL']}")
    # EM 2026-11-07: inch parts beside metric; UNC/UNF figures from FED-STD-H28/2B Table II.A.3, held to the thread form's arithmetic
    from toolkit import unthreads as UT_
    _ut = UT_.load(); _bad = {k: dict(v) for k, v in _ut.items()}
    _bad["No. 10-32"].update(minor_min_in=0.158, minor_min_in_text="0.158"); _bad["1/4-20"].update(pct_max=62.2, pct_max_text="62.2")
    _hits = {s for s, _ in UT_.check(_bad)}
    t("UN threads: the table on file holds (basic minor D - 1.082532P, percent of 0.75H); a misread minor diameter or percent fails",
      len(_ut) >= 39 and not UT_.check(_ut) and _hits == {"No. 10-32", "1/4-20"}, f"{len(_ut)} {UT_.check(_ut)[:2]} {sorted(_hits)}")
    # EM 2026-11-07: NPT as calculated values (ASME B1.20.1 formulas); the first figures he sent had their columns shifted by one
    from toolkit import pneu as PN_
    _np = [PN_.npt_check(PN_.NPT[s]["table"]) for s in PN_.THREADS]
    _sent = PN_.npt_check(dict(D=0.540, n=18, E0=0.49163, L1=0.2278, E1=0.50858, L2=0.4018, E2=0.51451, L3=0.4000, E3=0.51443, h=0.04444))
    t("NPT: the calculated sizes hold to B1.20.1's formulas and 1:16 taper; the shifted figures first sent for 1/4 fail (E0, E1, E2, E3)",
      not any(_np) and abs(PN_.NPT["NPT1/4"]["table"]["E1"] - 0.49163) < 5e-6 and {p.split()[0] for p in _sent} >= {"E0", "E1", "E2", "E3"},
      f"{_np} {_sent[:3]}")
    # EM 2026-11-10: every element is the Institute's (toolkit/owner.py, DOC-007): ids name the class; metadata.json is the owner's record
    from toolkit import owner as OW
    # the two product ids are built from halves, so a rename's token replace cannot reach the case (round 27's return 2: it would
    # have made them class names and the case would miss)
    _h = (OW.id_hits("sr-" + "440r", "Part number: 440R-S13R2\n"), OW.id_hits("lionx" + "-8io"), OW.id_hits("relay-safety", "Part number: 440R-S13R2\n"), OW.id_hits("io-block-m12"))
    t("DOC-007 finds a product in an id (440R's family prefix, case-blind; LioN-X) and none in a class name",
      _h[0] == ["part-number family 440R"] and _h[1] == ["LioN-X"] and _h[2] == [] and _h[3] == [], str(_h))
    # round 27's return 1 (core watch 2026-11-11): rename's token replace let "-" follow the old id, so it matched the old id inside
    # the new one and would have written contactor-9a-1no1nc-1no1nc in OPERATING.md 6; it also rewrote the lines that record a rename
    _o, _n = "ka-9a", "ka-9a-1no1nc"
    _t0 = f"see {_o}, {_o}-acad.json and ka-9ab\nthe examples: {_n}, kb-2\n{_o} -> {_n} (renamed)\nhost places {_o}-coil and {_o}\n"
    _t1, _d1 = OW.retoken(_t0, _o, _n, others={"ka-9a-coil"}); _t2, _d2 = OW.retoken(_t1, _o, _n, others={"ka-9a-coil"})
    t("rename: the old id and its files take the new id; the new id, a sibling id that starts with the old one, a line that names the new id and a rename record are left; a second run changes nothing",
      _t1 == f"see {_n}, {_n}-acad.json and ka-9ab\nthe examples: {_n}, kb-2\n{_o} -> {_n} (renamed)\nhost places {_o}-coil and {_n}\n"
      and [i for i, _, _ in _d1] == [1, 4] and _d2 == [] and _n + "-1no1nc" not in _t1, f"{_t1!r} {_d1} {_d2}")
    _t3, _d3 = OW.retoken("valve-a3 in valve-a3-acad.json; valve-a3x\n", "valve-a3", "valve-32nc-sr")
    _op = "x\nThe id convention (written down)\n  form: relay-safety / ka-9a, enc-fs\nBuilt elements whose id lacks the function: ka-9a\nka-9a in the lane table\n"
    _t4, _ = OW.retoken(_op, _o, _n, keep=OW.keep_lines("OPERATING.md", _op))
    t("rename: OPERATING.md 6's id convention is left as written (a form's example is not the element); the rest of the file is renamed",
      _t4 == _op.replace("ka-9a in the lane", _n + " in the lane") and OW.keep_lines("README.md", _op) == set(), f"{_t4!r}")
    t("rename: a new id that does not start with the old one replaces every whole token, the files named after it too",
      _t3 == "valve-32nc-sr in valve-32nc-sr-acad.json; valve-a3x\n" and len(_d3) == 1, f"{_t3!r}")
    # round 28's return 1 and 3 (core watch 2026-11-11): the tool rewrote a review's name written under the old id (sr-440r-1.1.md,
    # relay-ice-cube-1.3:1) and a path to a record; requests/ and needs-em/ are records; and an id after a string's \n was missed
    _q = "review ka-9a-1.1 finding 3; ka-9a-1.3:1; lib/reviews/elements/ka-9a-1.2.md; taken in from lib/requests/core/behaviour/ka-9a.csv; ka-9a 1.2 is held\n"
    _t5, _d5 = OW.retoken(_q, _o, _n, others={"ka-9a-coil"})
    t("rename: a review's name under the old id (<old>-<version>) and a path to a record keep the old id; the element at a version is renamed",
      _t5 == _q.replace("ka-9a 1.2 is held", _n + " 1.2 is held") and len(_d5) == 1, f"{_t5!r}")
    _t6, _ = OW.retoken('write("element,version\\nka-9a,1.0")\n', _o, _n)
    t("rename: an id that follows a string's \\n escape in code is a token and is renamed",
      _t6 == f'write("element,version\\n{_n},1.0")\n', f"{_t6!r}")
    # round 29's return 2.a.8 (core watch 2026-11-11): a token may start after "-", so a pneumatic id matched as its hydraulic
    # twin's tail (hyd-<old>) and the dry run would have renamed that element too (its folder, OWNERS row, catalogue row, element.py ID)
    _q7 = "x-fc and z-x-fc-y in x-fc-acad.json\nfc placed; fc-acad.json; hyd-fc,1.0; lib/elements/hyd-fc/element.py; ID = 'hyd-fc'\n"
    _t7, _d7 = OW.retoken(_q7, "fc", "fc-inline", others={"hyd-fc", "x-fc", "z-x-fc-y"})
    t("rename: another id that holds the old id after a '-' (hyd-fc when fc is renamed) is left whole, in text, paths and code; the old id alone is renamed",
      _t7 == "x-fc and z-x-fc-y in x-fc-acad.json\nfc-inline placed; fc-inline-acad.json; hyd-fc,1.0; lib/elements/hyd-fc/element.py; ID = 'hyd-fc'\n"
      and [i for i, _, _ in _d7] == [2], f"{_t7!r} {_d7}")
    # request pneu-13 2 (core watch 2026-11-12): `hx` is the heat exchanger's id (the case writes zq, so the rename leaves it) and a half-width name in 20 elements' code
    _q8 = 'ID = "zq"\nzq = w / 2\nbox(-zq, zq)\nload("elements/zq/spec.md"); f"{zq}"; place("zq-acad.json")\n'
    _t8, _ = OW.retoken(_q8, "zq", "zq-shell-tube", code=True); _t8t, _ = OW.retoken("zq is placed\n", "zq", "zq-shell-tube", code=False)
    _t8d, _ = OW.retoken("w = a.ka-9a + 1\n", "ka-9a", "ka-9a-x", code=True)
    t("rename: in code, an id with no '-' is renamed only where it opens a string or a path; a bare name ('zq = w / 2', f\"{zq}\") is "
      "code and stays; text and an id with a '-' as before (request pneu-13 2: 49 lines of other elements' element.py)",
      _t8 == 'ID = "zq-shell-tube"\nzq = w / 2\nbox(-zq, zq)\nload("elements/zq-shell-tube/spec.md"); f"{zq}"; place("zq-shell-tube-acad.json")\n'
      and _t8t == "zq-shell-tube is placed\n" and _t8d == "w = a.ka-9a-x + 1\n", f"{_t8!r} {_t8t!r} {_t8d!r}")
    t("rename: lib/requests/ and lib/needs-em/ are records a rename leaves (OW.HISTORY); the dry run counts the changed lines outside the element by kind",
      all(any(h in r_ for h in OW.HISTORY) for r_ in ("requests/elec/7.md", "requests/core/escapes.md", "needs-em/library.md"))
      and OW.risky([("elements/ka-9a/spec.md", 1, "", ""), ("elements/kb/spec.md", 2, "", ""), ("elements/kc/spec.md", 3, "", ""), ("toolkit/line.py", 4, "", "")], "ka-9a") == [("spec.md", 2), ("toolkit/line.py", 1)])
    # round 30's return 2.c (core watch 2026-11-12): after --write the element's folder is elements/<new>/ and the new id holds the old
    # one, so the write's count took the element's own gate and qa files as outside and "other ids" listed the element itself
    # round 30's return 4.3 (core watch 2026-11-12): build.py index stopped on a generic design's brief written as one string; the
    # owner's record may hold the brief as a record ({"stage0": ...}) or, for an own or generic design with no Stage 0 brief, as its line
    import importlib.util as _ilu
    _sp = _ilu.spec_from_file_location("element_index_t", os.path.join(os.path.dirname(OW.library.ELEMENTS), "element-index.py"))
    _ei = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_ei)
    t("index: an owner's record's brief reads as a record's 'stage0' or as one string (mcb-2p, xfmr-control); none is empty",
      _ei._brief({"stage0": "references/measure.md"}) == "references/measure.md" and _ei._brief("our own design: generic x") == "our own design: generic x"
      and not _ei._brief(None), f"{_ei._brief({'stage0': 'references/measure.md'})!r} {_ei._brief('our own design: generic x')!r} {_ei._brief(None)!r}")
    _el1 = OW.library.element_ids
    try:
        OW.library.element_ids = lambda: ["fc-inline", "hyd-fc", "kb"]
        _h8 = OW.holders("fc", "fc-inline"); _h8a = OW.holders("fc")
    finally: OW.library.element_ids = _el1
    # request pneu-14 item 3 (core watch 2026-11-12): hpu-large -> hpu-7.5kw had no metadata.json, so its old id was in no aliases
    _elk = OW.library.ELEMENTS
    with _tfw.TemporaryDirectory() as _ad:
        try:
            OW.library.ELEMENTS = _ad
            os.makedirs(os.path.join(_ad, "hpu-x")); os.makedirs(os.path.join(_ad, "hpu-y"))
            open(os.path.join(_ad, "hpu-y", "metadata.json"), "w").write('{"element_id": "hpu-y", "domain": "fluid", "aliases": ["hpu-w"]}')
            OW.keep_alias("hpu-x", "hpu-large"); OW.keep_alias("hpu-y", "hpu-big")
            _ka = json.load(open(os.path.join(_ad, "hpu-x", "metadata.json"))); _kb = json.load(open(os.path.join(_ad, "hpu-y", "metadata.json")))
            _kc = OW.check("hpu-x")
        finally: OW.library.ELEMENTS = _elk
    t("rename --write: an element with no metadata.json gets one with its old id in aliases, the owner and the licence (DOC-007 finds "
      "nothing in it); one with a record keeps it and adds the old id (request pneu-14 3: hpu-large in no aliases after its rename)",
      _ka.get("aliases") == ["hpu-large"] and _ka.get("owner") == OW.OWNER and _ka.get("element_id") == "hpu-x" and not _kc
      and _kb.get("aliases") == ["hpu-w", "hpu-big"] and _kb.get("domain") == "fluid", f"{_ka} {_kb} {_kc}")
    t("rename --write: the element under its new id is neither 'outside' nor 'another id that holds the old id' (holders, risky take <new>)",
      _h8 == ["hyd-fc"] and _h8a == ["fc-inline", "hyd-fc"]
      and OW.risky([("elements/fc-inline/gate/x.json", 1, "", ""), ("elements/kb/spec.md", 2, "", "")], "fc", "fc-inline") == [("spec.md", 1)]
      and OW.risky([("elements/fc-inline/gate/x.json", 1, "", "")], "fc") == [("x.json", 1)], f"{_h8} {_h8a}")
    _td = tempfile.mkdtemp(); _el0 = OW.library.ELEMENTS
    try:
        OW.library.ELEMENTS = _td; os.makedirs(os.path.join(_td, "x-relay", "references"))
        open(os.path.join(_td, "x-relay", "element.py"), "w").write("ID='x-relay'\n")
        json.dump({"element_id": "x-relay", "manufacturer": "Rockwell", "part_number": "440R-S13R2", "status": {"brief": "ok"}, "width": 22.5, "domain": "electrical"},
                  open(os.path.join(_td, "x-relay", "metadata.json"), "w"))
        _c0 = OW.check("x-relay"); _mv, _ = OW.own("x-relay", write=True); _c1 = OW.check("x-relay")
        _m = json.load(open(os.path.join(_td, "x-relay", "metadata.json"))); _a = open(os.path.join(_td, "x-relay", "references", "source.txt")).read()
        t("DOC-007 holds a metadata.json that carries the maker; build.py own moves the record verbatim to a block in references/source.txt, names the owner and MIT, and the hold clears",
          len(_c0) == 1 and "manufacturer" in _c0[0] and _mv == ["manufacturer", "part_number", "status"] and _c1 == [] and _m["owner"] == OW.OWNER
          and _m["licence"] == "MIT" and _m["width"] == 22.5 and "manufacturer" not in _m and "part_number: 440R-S13R2" in _a and 'status: {"brief": "ok"}' in _a, f"{_c0} {_mv} {_c1} {_m} {_a}")
    finally:
        OW.library.ELEMENTS = _el0; import shutil as _sh; _sh.rmtree(_td, ignore_errors=True)
    # request mech-10 3 (review mech-r86 finding 3; core watch 2026-11-11): own kept a catalogue part's envelope in an own design's
    # record (hardware-cabinet 152.4 x 1.27 x 50.8, its build 600 x 347 x 700), and nothing compared the record with the build
    _b = dict(width=600.0, height=700.0, depth=347.0)
    _dr = (OW.envelope_drift({"width": 152.4, "height": 1.27, "depth": 50.8, "datasheet_dims": [152.4, 50.8]}, _b),
           OW.envelope_drift({"width": 600.0, "height": 700.2, "depth": 347.0, "datasheet_dims": None}, _b), OW.envelope_drift({"width": None}, _b))
    t("DOC-007 envelope: an own design's record that keeps another part's width, height, depth or datasheet_dims drifts; its own build's (within 0.5 mm) and an empty record do not",
      [k for k, _ in _dr[0]] == ["width", "height", "depth", "datasheet_dims"] and _dr[1] == [] and _dr[2] == [], str(_dr))
    _td = tempfile.mkdtemp(); _el0 = OW.library.ELEMENTS
    try:
        OW.library.ELEMENTS = _td; os.makedirs(os.path.join(_td, "x-cab", "references"))
        open(os.path.join(_td, "x-cab", "element.py"), "w").write("ID='x-cab'\n")
        json.dump({"element_id": "x-cab", "domain": "mechanical", "owner": OW.OWNER, "licence": "MIT", "width": 152.4, "height": 1.27, "depth": 50.8,
                   "units": "mm", "datasheet_dims": [152.4, 50.8]}, open(os.path.join(_td, "x-cab", "metadata.json"), "w"))
        _c0 = OW.check("x-cab", built=_b); _mv, _ = OW.own("x-cab", write=True, built=_b); _c1 = OW.check("x-cab", built=_b)
        _m = json.load(open(os.path.join(_td, "x-cab", "metadata.json"))); _a = open(os.path.join(_td, "x-cab", "references", "source.txt")).read()
        t("DOC-007 holds an own design whose metadata.json keeps a catalogue envelope; build.py own writes the build's (width x, depth y, height z, datasheet_dims null), moves the old figures verbatim to source.txt, and the hold clears",
          len(_c0) == 1 and "envelope" in _c0[0] and _c1 == [] and (_m["width"], _m["height"], _m["depth"], _m["datasheet_dims"]) == (600.0, 700.0, 347.0, None)
          and "catalogue height: 1.27" in _a and "catalogue datasheet_dims: [152.4, 50.8]" in _a and len(_mv) == 4, f"{_c0} {_mv} {_c1} {_m} {_a}")
    finally:
        OW.library.ELEMENTS = _el0; _sh.rmtree(_td, ignore_errors=True)
    # request mech-10 2 (lib/behaviour.md, pin): a pin the element claims no torque for is written 'not claimed' and is no open figure
    from .validate import behaviour_open as _bo
    _bh = "kind,a,b,part,when,value,unit,source,note\npin,1,stud,stud,,not claimed,N·m,not claimed: the host's lock nut sets it (lib/behaviour.md),\npin,2,slot,slot,,NOT ON FILE (B),N·m,ISO 2380,\n"
    _bo1 = _bo(_bh)
    t("behaviour.csv: a pin's 'not claimed' torque is no open figure for DOC-005; a NOT ON FILE (B) torque is one, class B",
      [(i, k, c) for i, _, k, c in _bo1] == [(3, "NOT ON FILE", "B")], str(_bo1))
    # core watch 2026-11-11 (request panel-4 3 and 4): pm-motor-starter's wires ended on plc-1.L+, a mark plc0 does not have, and passed
    from . import v_panel as PLV
    _tags = ["plc-1", "x1-1", "x1-2", "enc-1", "enc-1.lamp-power"]; _el = {"plc-1": "plc0", "x1-1": "term-4mm", "x1-2": "term-4mm", "enc-1": "enc", "enc-1.lamp-power": "op-pilot-22"}
    _pins = {"plc0": {"24V-1", "24V-3"}, "term-4mm": {"1", "2"}, "op-pilot-22": {"X1", "X2"}, "enc": None}
    _W = lambda *r: [dict(wire=w, **{"from": a, "to": b}) for w, a, b in r]
    _e1 = PLV.ends(_W(("24", "x1-1.2", "plc-1.L+")), _tags, _el.get, _pins.get)
    _e2 = PLV.ends(_W(("24", "x1-1.2", "plc-9.24V-1")), _tags, _el.get, _pins.get)
    _e3 = PLV.ends(_W(("24", "x1-1.2", "plc-1.24V-1"), ("46", "x1-1.1", "enc-1.lamp-power.X1"), ("", "x1-2.9", "nowhere.1")), _tags, _el.get, _pins.get)
    t("PNL-010 fails a wire end on a mark its element's behaviour.csv has no pin for (plc-1.L+ on plc0)", [s for s, *_ in _e1] == ["FAIL"] and "no pin 'L+'" in _e1[0][3], str(_e1))
    t("PNL-010 fails a wire end on a tag the assembly does not have", [s for s, *_ in _e2] == ["FAIL"] and "no element" in _e2[0][3], str(_e2))
    t("PNL-010 passes ends on real pins, a nested tag by its longest match (enc-1.lamp-power, not enc-1), and leaves an unnumbered join alone",
      [s for s, *_ in _e3] == ["PASS"] and PLV.split_end("enc-1.lamp-power.X1", _tags) == ("enc-1.lamp-power", "X1"), str(_e3))
    _T = [dict(strip="X1", terminal="1", tag="x1-1", wire="46/24")]
    _p1 = PLV.plan(_T, _W(("24", "x1-1.2", "plc-1.24V-1"), ("46", "x1-1.1", "enc-1.lamp-power.X1")))
    _p2 = PLV.plan(_T, _W(("24", "x1-1.1", "plc-1.24V-1"), ("46", "x1-1.1", "enc-1.lamp-power.X1")))
    _p3 = PLV.plan([dict(strip="X1", terminal="1", tag="x1-1", wire="46/(31)")], _W(("46", "x1-1.1", "a.1"), ("47", "x1-1.2", "b.1")))
    t("PNL-030 passes a terminal plan that names each wire on the side it ends", [s for s, *_ in _p1] == ["PASS"], str(_p1))
    t("PNL-030 fails a plan whose side names a wire that ends on the other side, and the wire the plan does not name there",
      sum(s == "FAIL" for s, *_ in _p2) == 2, str(_p2))
    t("PNL-030 fails a wire on a block the plan does not name (a bracketed number is kept, not checked)", [s for s, *_ in _p3] == ["FAIL"] and "47" in _p3[0][2], str(_p3))
    # ESCAPE, lib/reviews/panel/r6.md finding 1 (core watch 2026-11-11): a merge brought contactor-9a and op-estop-22 back into the panels'
    # BOMs after their rename; the assembly dropped both rows as planned (no folder) and every check passed
    _bm = [dict(element="ka-9a", version="1.2", tag="k1"), dict(element="ka-9a-1no1nc", version="1.2", tag="k2"), dict(element="relay-new", version="-", tag="k3"),
           dict(element="kb-planned", version="", tag="k4"), dict(element="kc-typo", version="1.0", tag="k5"), dict(element="relay-row", version="1.0", tag="k6")]
    _b1 = PLV.bom_ids(_bm, {"ka-9a-1no1nc"}, {"relay-row"}, {"ka-9a": "ka-9a-1no1nc"})
    t("ESCAPE panel/r6 1: BOM-010 fails a bom.csv row that names a renamed element's old id (an alias), reviews a versioned row naming no element and no inventory row, and passes a placeholder with no version, an element on file and an inventory row",
      [(s, w) for s, _, w, _ in _b1] == [("FAIL", "k1"), ("REVIEW", "k5")] and "ka-9a-1no1nc" in _b1[0][3], str(_b1))
    # ESCAPE, lib/reviews/panel/r18.md finding 1 (core watch 2026-11-14): pnl-motor-starter's gate of record passed with k1 drawn at
    # contactor-9a-1no1nc 1.3 (no AutoCAD gate at 1.3; the row pins 1.2) and w-pwr's L variant (its gate failed); nothing read the
    # station of what a panel places, and the round queued as all-pass
    import json as _js
    from . import line as _LN, library as _lb
    _gd, _qd = (os.path.join(_lb.ELEMENTS, "gl-xr-1", x) for x in ("gate", "qa"))
    _mkq = not os.path.isdir(_qd)
    _pf = [os.path.join(_gd, "gl-xr-1-bomx" + x) for x in ("-acad.json", ".lsp", ".json")] + [os.path.join(_qd, "gl-xr-1-bomx.json")]
    try:
        os.makedirs(_qd, exist_ok=True)
        _ver = _LN._catalogue()["gl-xr-1"]["version"]
        open(_pf[0], "w", encoding="utf-8").write(_js.dumps({"pass": False, "date": "2026-11-11", "params": {"kind": "bomx", "coding": "L"}, "measure_compare": []}))
        open(_pf[1], "w", encoding="utf-8").write(f";; gl-xr-1 v{_ver} {{'kind': 'bomx', 'coding': 'L'}} (gate build 2026-11-11). Generated.\n")
        open(_pf[2], "w", encoding="utf-8").write(_js.dumps({"pass": True})); open(_pf[3], "w", encoding="utf-8").write(_js.dumps({"pass": True}))
        _v1 = _LN.placed_variant("gl-xr-1", _lb.parse_params("coding=L;kind=bomx;length=2000"))
        _v0 = _LN.placed_variant("gl-xr-1", _lb.parse_params("coding=L;length=2000"))
        _h1 = _LN.build_holds("gl-xr-1", _ver, _v1)
        open(_pf[0], "w", encoding="utf-8").write(_js.dumps({"pass": True, "date": "2026-11-11", "params": {"kind": "bomx", "coding": "L"}, "measure_compare": []}))
        _h2 = _LN.build_holds("gl-xr-1", _ver, "bomx"); _h3 = _LN.build_holds("gl-xr-1", "9.9", "bomx")
        t("ESCAPE panel/r18 1: a BOM row's params pick the gated variant whose gate params they all carry (none: the default build); that "
          "build holds on its failed AutoCAD gate and on a pass at another version than the one drawn, and passes when gated at it",
          _v1 == "bomx" and _v0 is None and any("AutoCAD gate failed" in w for w in _h1) and _h2 == [] and any("not v9.9" in w for w in _h3),
          f"{_v1} {_v0} | {_h1} | {_h2} | {_h3}")
    finally:
        for f in _pf:
            if os.path.exists(f): os.remove(f)
        if _mkq and os.path.isdir(_qd) and not os.listdir(_qd): os.rmdir(_qd)
    _bs = [dict(element="kx", version="1.2", tag="k1"), dict(element="kx", version="1.2", tag="k2"), dict(element="wx", version="1.8", tag="w-pwr", params="coding=L"),
           dict(element="ok-x", version="1.0", tag="ok1"), dict(element="a-cell", version="0.1", tag="c1"), dict(element="#kx", version="1.3", tag="k9")]
    _hf = lambda e, v, p: ((None, ["AutoCAD gate failed (2026-11-03)"]) if e == "kx" else ("L", ["AutoCAD gate failed (2026-11-11)"]) if p.get("coding") == "L" else (None, []))
    _b2 = PLV.bom_stations(_bs, {"kx": "1.3", "wx": "1.8", "ok-x": "1.0"}, _hf)
    _b3 = PLV.bom_stations(_bs[3:], {"ok-x": "1.0"}, _hf)
    t("ESCAPE panel/r18 1: BOM-020 reviews each placed element and variant below station 6 once, naming its tags and the pin the build does "
      "not draw, skips an assembly or comment row, and passes a BOM whose every placed element passed",
      [(s, w) for s, _, w, _ in _b2] == [("REVIEW", "k1, k2"), ("REVIEW", "w-pwr")] and "pins 1.2, the build draws 1.3" in _b2[0][3]
      and "variant L" in _b2[1][3] and "pins" not in _b2[1][3] and [s for s, *_ in _b3] == ["PASS"], f"{_b2} | {_b3}")
    # ESCAPES 28 to 30 (core watch 2026-11-11): DOC-009, a figure that leans on another is sourced as well as it
    _d9 = ("| earth stud torque | 22.3 N·m | derived: derive.torque(8, 1.25, '8.8') (ISO 16047); design: property class 8.8 (the stud's steel, "
           "this design's choice). design: d_w 13 (the bearing face: this design's figure, the nut's standard ISO 4032 not on file) |\n")
    _9a = [VA.unruled_design(_d9), VA.unruled_design(_d9.replace("this design's choice", "ISO 898-1 clause 4: a machined stud of this design")),
           VA.unruled_design(_d9.replace("derived:", "on file:")), VA.unruled_design("", "pin,PE1,pe,stud,,22.3,N·m,derived: x; design: class 8.8 (this design's choice),\n"),
           VA.unruled_design("| f | 1 | derived: derive.torque(10) design: d_w 40 (the element's bearing face: the plate's underside) |\n")]
    t("ESCAPE mech/r95 1: DOC-009 holds a derived figure whose 'design:' input calls itself this design's choice and names no rule (enc-wm 1.3's "
      "8.8 stud), in spec.md or behaviour.csv; passes it once the rule is named, a figure that is not derived, and an input that is the element's own face",
      [len(x) for x in _9a] == [1, 0, 0, 1, 0] and "8.8" in _9a[0][0], str(_9a))
    _mt = ("# x v1.0\n## What it meets\n| figure | value | source |\n|---|---|---|\n| the work | the base | a flat steel face |\n"
           "| the dial indicator | the bore Ø8 | this design's figure (features.csv, kind own): the indicator's Ø8 stem |\n## Its own sizes\n| a | 8 | this design's figure |\n")
    _9b = [VA.meets_unruled(_mt), VA.meets_unruled(_mt.replace("this design's figure (features", "**NOT ON FILE (B)**: ISO 463, the stem (features")),
           VA.meets_unruled(_mt.replace("indicator's Ø8 stem", "indicator's Ø8 stem; ISO 3611 leaves it free"))]
    t("ESCAPE mech/r94 1: DOC-009 holds a 'What it meets' row sourced \"this design's figure\" that names no standard (stand-magnetic's Ø8 stem bore), "
      "only in that table; passes it with 'NOT ON FILE (B): <standard>' or the standard that leaves it free",
      [len(x) for x in _9b] == [1, 0, 0] and "dial indicator" in _9b[0][0], str(_9b))
    _ed, _el = tempfile.mkdtemp(), _lib.ELEMENTS
    try:
        for _e, _s in (("cyl-t", "# cyl-t v1.1\n## Open figures\n- NOT ON FILE (B): the mounting interface (ISO 6020-2); a host can't place the cylinder until it is on file.\n"),
                       ("plate-t", "# plate-t v1.0\n## Open figures\n- NOT ON FILE (B): the plate's finish.\n"),
                       ("head-t", "# head-t v1.0\n## Open figures\nNone of this element's own.\n")):
            os.makedirs(os.path.join(_ed, _e)); open(os.path.join(_ed, _e, "spec.md"), "w", encoding="utf-8").write(_s)
        open(os.path.join(_ed, "head-t", "bom.csv"), "w", encoding="utf-8").write("element,version,tag,parent,x,y,z,yaw,params,note\ncyl-t,1.1,cyl,,0,0,0,0,,\nplate-t,1.0,p,,0,0,0,0,,\n")
        _lib.ELEMENTS = _ed; _9c = [VA.leans_on_open("head-t")]
        open(os.path.join(_ed, "head-t", "spec.md"), "a", encoding="utf-8").write("- **NOT ON FILE (B)**: the cylinder's mounting to the arm (ISO 6020-2; cyl-t's open figure).\n")
        _9c.append(VA.leans_on_open("head-t"))
    finally: _lib.ELEMENTS = _el; import shutil as _sh9; _sh9.rmtree(_ed, ignore_errors=True)
    t("ESCAPE pneu/r87 1: DOC-009 holds a host that places a part whose spec has its mounting NOT ON FILE (head-rivet-c-hyd on hyd-cylinder-da-40), "
      "not for the part's other open figures; passes once the host's own NOT ON FILE line names the part (DOC-005 then counts it: source wanted)",
      [len(x) for x in _9c] == [1, 0] and "cyl-t" in _9c[0][0] and "plate-t" not in _9c[0][0], str(_9c))
    # ESCAPE reviews/elements/mcb-2p-1.0.md 1 (core watch 2026-11-12): a behaviour row sourced "design choice" with no rule passed DOC-005
    _bh = ("kind,a,b,part,when,value,unit,source,note\nstate,on,,mechanism,manual toggle,,,spec.md Named nodes (one common handle),\n"
           "state,reset,,mechanism,manual momentary,,,design choice: trip-free; reset by moving the toggle to off (spec.md Named nodes),\n"
           "state,shut,,throttle,default,,,spec.md Named nodes (knob 0°: the throttle shut; a design choice),\n")
    _bf = "kind,a,b,part,when,value,unit,source,note\nstate,reset,,mechanism,manual momentary,,,\"Assumption (A): trip-free, reset by moving the toggle to off\",\n"
    _9d = [VA.behaviour_unruled(_bh, _bf), VA.behaviour_unruled(_bh.replace("design choice: trip-free;", "Assumption (A): trip-free;")),
           VA.behaviour_unruled(_bh.replace("design choice: trip-free;", "design: trip-free (IEC 60898-1 9.x);"))]
    t("ESCAPE mcb-2p-1.0 1: DOC-009 holds a behaviour.csv state row sourced 'design choice' with no rule (mcb-2p's trip-free reset), naming the family's "
      "Assumption on the same row; passes it as 'Assumption (A)' or with its rule, and a knob angle called a design choice after its spec line",
      [len(x) for x in _9d] == [1, 0, 0] and "reset" in _9d[0][0] and "family" in _9d[0][0], str(_9d))
    _9r = [dict(property="voltage", value="460", unit="V", status="derived", source="campus supply"), dict(property="phases", value="3", unit="", status="derived", source=""),
           dict(property="power", value="7.5", unit="kW", status="generic design", source="ISO 4413 value")]
    _9s = ("## Open figures\n- NOT ON FILE (A): the drive motor's full-load current at 460 V (a rating the ELR checks read through `pwr`; NFPA 70\n"
           "  Table 430.250, read attended into a standards table, closes it).\n")
    _9e = [getattr(VA, "current_derivable", lambda s, r: [])(_9s, _9r),
           getattr(VA, "current_derivable", lambda s, r: [])(_9s.replace("NOT ON FILE (A): the drive motor's full-load current at 460 V", "NOT ON FILE (B): NFPA 70 Table 430.250, the motor's table current"), _9r),
           getattr(VA, "current_derivable", lambda s, r: [])(_9s, [dict(r_, value="0.37") if r_["property"] == "power" else r_ for r_ in _9r]),
           getattr(VA, "current_derivable", lambda s, r: [])("", _9r + [dict(property="fla", value="12", unit="A", status="assumption", source="class A")])]
    t("ESCAPE hpu-large-1.2 1 (hpu-7.5kw-1.2 1): DOC-009 holds a motor's full-load current written NOT ON FILE (A) (or a ratings.csv 'assumption') "
      "when derive.motor_current gives it from the power and voltage on file (7.5 kW, 460 V: 12.08 A); a class B table-current line passes, and 0.37 kW (no IE3 figure on file) is not derivable",
      [len(x) for x in _9e] == [1, 0, 0, 1] and "12.08" in _9e[0][0] and "derive motor 7.5 460" in _9e[0][0], str(_9e))
    t("DOC-009 is a station 1 hold, the lane's to fix, not EM's", LN.RULE_STATION.get("DOC-009") == 1
      and not LN.waits_on_em((1, "x", "x", False, ["DOC-009 REVIEW: places cyl-t, whose spec has its mounting NOT ON FILE"])), str(LN.RULE_STATION.get("DOC-009")))
    _bd = tempfile.mkdtemp()
    try:
        open(os.path.join(_bd, "bom.csv"), "w", encoding="utf-8").write("element,version,tag,parent,x,y,z,yaw,params,note,pitch,roll\nduct-40x60,1.0,riser-l,floor,0,0,0,0,,,,-90\ndin-rail-35,1.1,rail-1,floor,0,0,0,0,,,,\n")
        _br = _lib.read_bom(os.path.join(_bd, "bom.csv"))
    finally: import shutil as _sh2; _sh2.rmtree(_bd, ignore_errors=True)
    t("library.read_bom makes a number of roll as of pitch (request panel-5 1: a riser duct stood on end failed in place)", [r["roll"] for r in _br] == [-90.0, 0.0], str([r.get("roll") for r in _br]))
    # core chat 2026-11-11, a flow change: the build of what changed (toolkit/incremental.py; `build.py changed [base]`)
    from toolkit import incremental as INC
    _k = [INC.classify(p_)[0] for p_ in ("lib/elements/contactor-9a/spec.md", "lib/elements/contactor-9a/out/validate.json", "lib/elements/contactor-9a/gate/x.json",
          "lib/assemblies/pm-motor-starter/wires.csv", "lib/toolkit/nets.py", "lib/inventory.csv", "lib/operators.py", "lib/standards/vendors.csv", "lib/reviews/mech/r1.md",
          "lib/OPERATING.md", "lib/acad-gate.py", "lib/newthing/x.bin", "lib/requests/core/behaviour/term-4mm.csv", "lib/requests/mech/9.md")]
    t("changed build: an element's own file names the element, its out/ and gate/ nothing; a toolkit, standards, lib/*.csv or unknown path the full build; reviews and role text nothing; a behaviour proposal its element",
      _k == ["element", "none", "none", "assembly", "full", "full", "full", "full", "none", "none", "none", "full", "element", "none"], str(_k))
    _dep = {"contactor-9a": {"pm-motor-starter"}, "pm-motor-starter": {"dm-cell"}, "column": {"arm-radial"}}
    _ei, _ai = ["contactor-9a", "column", "arm-radial", "tag-plate"], ["pm-motor-starter", "dm-cell"]
    _s1 = INC.scope(["lib/elements/contactor-9a/spec.md", "lib/reviews/x.md"], _ei, _ai, _dep, set(_ei), set(_ai))
    _s2 = INC.scope(["lib/elements/column/element.py"], _ei, _ai, _dep, set(_ei), set(_ai))
    _s3 = INC.scope(["lib/elements/io-block-m12/spec.md"], ["io-block-m12"], [], {}, {"lionx-8io"}, set())
    _s4 = INC.scope(["lib/elements/column/element.py", "lib/toolkit/x.py"], _ei, _ai, _dep)
    t("changed build: a changed element takes every assembly that carries it, and the assembly that carries that one; an element another loads takes the loader; a renamed folder or a toolkit file is the full build",
      _s1[:3] == ("part", ["contactor-9a"], ["dm-cell", "pm-motor-starter"]) and _s2[:3] == ("part", ["arm-radial", "column"], []) and _s3[0] == "full" and _s4[0] == "full", f"{_s1} {_s2} {_s3} {_s4}")
    _mg = INC.merge([dict(scope="a", rule="1"), dict(scope="b", rule="2"), dict(scope="library", rule="3"), dict(scope="gone", rule="4")],
                    [dict(scope="a", rule="9"), dict(scope="library", rule="8")], {"a", "library"}, ["a", "b"], [])
    t("changed build: the merged findings are the base's for what was not run again and is still in the tree, the new ones for the rest (the library-wide rules always run again), in a full run's order",
      [(f_["scope"], f_["rule"]) for f_ in _mg] == [("a", "9"), ("b", "2"), ("library", "8")], str(_mg))
    import datetime as _dtm
    _n0 = _dtm.datetime(2026, 11, 11, 12, 0)
    _fd = (INC.full_due(_n0, text=""), INC.full_due(_n0, text="2026-11-11T03:00:00\n"), INC.full_due(_n0, text="2026-11-10T23:00:00\n"))
    t("changed build: with no full build on record, or one more than 12 h old, the full build is due; 9 h old, it is not",
      _fd[0].startswith("no full build") and _fd[1] == "" and "13 h old" in _fd[2], str(_fd))
    # core watch 2026-11-12, round 32 return 4.2: hx -> hx-shell-tube was committed before `changed -v`, which saw nothing renamed against HEAD
    _st = "2026-11-12T10:43:00\nids: column,hx,pm-motor-starter\n"
    _gs = (INC.gone_since_full(["column", "hx-shell-tube"], ["pm-motor-starter"], text=_st), INC.gone_since_full(["column", "hx"], ["pm-motor-starter"], text=_st),
           INC.gone_since_full(["column"], [], text="2026-11-12T10:43:00\n"), INC.full_due(_dtm.datetime(2026, 11, 12, 12, 0), text=_st))
    t("changed build: a folder the last full build built and the tree no longer holds (a rename committed before `changed`) is the full build; none gone, or a stamp "
      "that lists no folders, is not; the stamp's folder line leaves its time readable",
      _gs[0].startswith("hx: gone or renamed") and _gs[1] == "" and _gs[2] == "" and _gs[3] == "", str(_gs))
    # core watch 2026-11-13, round 33 return: the PC's full build took 108 of the agent's 120 minutes for one command; --part=k/n splits it
    _ids = [f"e{i:02d}" for i in range(23, 0, -1)]
    _sl = [INC.part_slice(_ids, k_, n_) for n_ in (2, 3) for k_ in range(1, n_ + 1)]
    _cover = sorted(_sl[0] + _sl[1]) == sorted(_ids) == sorted(_sl[2] + _sl[3] + _sl[4]) and not set(_sl[0]) & set(_sl[1])
    _r1 = INC.part_record(1, 2, True, "kA", ""); _rf = INC.part_record(1, 2, False, "kA", _r1)
    _pm = (INC.parts_missing(2, "kA", ""), INC.parts_missing(2, "kA", _r1), INC.parts_missing(2, "kB", _r1), INC.parts_missing(2, "kA", _rf),
           INC.parts_missing(3, "kA", INC.part_record(2, 3, True, "kA", _r1)), INC.parts_missing(2, "", _r1))
    t("full build in parts: the slices hold every element once; the last part is refused while an earlier part has not passed on this same tree "
      "(none run, run on another tree, its rerun failed, or run for another n), and runs once it has",
      _cover and _pm == ([1], [], [1], [1], [1], [1]), f"{_cover} {_pm}")
    # request elec-12 (core watch 2026-11-12): a mates.csv row whose element is not in the library yet holds neither side
    import tempfile as _tf, os
    from toolkit import validate as _VM
    with _tf.TemporaryDirectory() as _td:
        _mp = os.path.join(_td, "mates.csv")
        with open(_mp, "w", encoding="utf-8", newline="") as _fh:
            _fh.write("feature,a_element,a_attr,b_element,b_attr,tol,required,source,note,kind\n"
                      "zq pitch,zq-not-built,PITCH,overload-9a-1no1nc,PIN_PITCH,0.2,yes,planted,planted,equal\n"
                      "zq width,contactor-9a-1no1nc,W,overload-9a-1no1nc,W,0.5,yes,planted,planted,equal\n")
        _mr = _VM.mates(_mp)
    _mh = [(_s, _VM.mate_elements(_r)) for _s, _r, _ in _mr]
    t("MATE-010: a row naming an element not in the library yet is REVIEW and holds neither element (overload-9a-1no1nc is not taken back); "
      "a row between two elements on file still names both", len(_mh) == 2 and _mh[0] == ("REVIEW", ()) and _mh[1][1] == ("contactor-9a-1no1nc", "overload-9a-1no1nc"), str(_mh))
    # request elec-13 (core watch 2026-11-13): a row the core adds from a request states its route (own_design), or no lane builds it
    with _tf.TemporaryDirectory() as _td:
        _ip = os.path.join(_td, "inventory.csv")
        with open(_ip, "w", encoding="utf-8", newline="") as _fh:
            _fh.write("id,lane,systems,domains,used_by,own_design,type,made_of,etim,note,safety,pin\n"
                      "zq-3p,elec,1,1,x,,zq,,EC000042,request zq-1 (planted),,6\n"
                      "zq-2p,elec,1,1,x,generic,zq,,EC000042,request zq-2 (planted),,6\n"
                      "zq-1p,elec,1,1,x,,zq,,EC000042,,,\n")
        _iu = _VM.inventory_unmarked(_ip)
    _live = _VM.inventory_unmarked()
    t("inventory: a row added from a request with an empty own_design is named (zq-3p), a marked one and a product row are not; "
      "lib/inventory.csv has none (mcb-3p, request elec-13)", _iu == ["zq-3p"] and _live == [], f"{_iu} {_live}")
    # EM 2026-11-12: lab rooms inside the campus Labs building (toolkit/rooms.py, ROOM-010 / 020 / 030)
    from toolkit import rooms as RM
    _b = RM.bay(2)
    t("rooms: bay 2 of the Labs building is 15770 x 25770 mm clear and 8000 mm to the eaves, its door 1000 x 2100 at x 7885, its origin at (117.115, 166.615) m on the campus",
      (_b["dx"], _b["dy"], _b["h"], _b["door_w"], _b["door_h"], _b["door_x"]) == (15770.0, 25770.0, 8000.0, 1000.0, 2100.0, 7885.0) and _b["campus_origin"][:2] == (117.115, 166.615), str(_b))
    def _room(enc_y, extra=()):
        Pr = RM.shell(Prims(), _b); a = len(Pr); Pr.box("M-STEEL-7035", 1000, enc_y, 0, 1524, 305, 1829); Pr.owners = [(a, a + 1, "enc-1", "enc-fs-1524x1829x305")]
        for bx in extra: Pr.box("node:bench-x|M-WOOD", *bx)
        return {(r[0], r[1], r[2][:14]) for r in RM.check("lab-x", Pr, _b, 277)}
    _ok, _blk, _wall, _out, _door = _room(20000), _room(20000, [(1500, 19500, 0, 600, 300, 900)]), _room(1000), _room(25600), _room(20000, [(7600, 500, 0, 600, 600, 900)])
    t("rooms: a panel with nothing in front passes; a bench 500 mm in front of its door fails ROOM-020; a panel 1000 mm from the brick wall opposite fails condition 2's 1067 mm; one through the north wall fails ROOM-010; a bench inside the door fails ROOM-030",
      all(s_ == "PASS" for s_, _, _ in _ok) and ("FAIL", "ROOM-020", "enc-1") in _blk and ("FAIL", "ROOM-020", "enc-1") in _wall
      and ("FAIL", "ROOM-010", "lab-x") in _out and ("FAIL", "ROOM-030", "lab-x") in _door, f"{sorted(_ok)} {sorted(_blk)} {sorted(_wall)} {sorted(_out)} {sorted(_door)}")
    # EM 2026-11-12, before the library goes public: what a contribution may bring in (toolkit/guard.py)
    from toolkit import guard as GD
    _ok = "import os, sys, math\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom toolkit import library\nrows = library.own_bom(sys.modules[__name__])\nif __name__ == '__main__': print(library.emit(sys.modules[__name__]))\n"
    _bad = ["import subprocess\n", "import os\nos.system('x')\n", "eval('1')\n", "x = ().__class__.__bases__\n", "open('/x', 'w')\n", "import os\ngetattr(os, 'system')\n", "from os import system\n", "import sys\nsys.modules['os']\n"]
    _r = [bool(GD.code_findings("lib/elements/x/element.py", b_)) for b_ in _bad]
    t("GRD-020: element code that imports subprocess, calls os.system, eval or getattr, reaches a dunder, writes a file, imports a name from os or reads another module fails; the library's own boilerplate passes",
      all(_r) and not GD.code_findings("lib/elements/x/element.py", _ok), f"{_r} {GD.code_findings('lib/elements/x/element.py', _ok)}")
    _f = [bool(GD.file_findings(p_, d_, ext_)) for p_, d_, ext_ in (("lib/elements/x/a.exe", b"MZ", False), ("lib/elements/x/out/x.glb", b"MZ", False),
          ("lib/elements/x/out/x.glb", b"glTF", True), ("lib/elements/x/spec.md", b"a\x00b", False), ("lib/elements/x/out/d.svg", b"<svg onload='x'>", False),
          ("lib/toolkit/x.py", b"x = 1", True), ("lib/elements/x/x.lsp", b"(defun c:x ())", False))]
    _g = [bool(GD.file_findings(p_, d_, ext_)) for p_, d_, ext_ in (("lib/elements/x/spec.md", b"# x\n", True), ("lib/elements/x/out/x.glb", b"glTF....", False))]
    t("GRD-010: an .exe, a .glb that is not glTF, a built file from outside, a NUL in a text file, an svg that runs script, a toolkit file from outside and a .lsp outside out/ fail; a spec from outside and a lane's glb pass",
      all(_f) and not any(_g), f"{_f} {_g}")
    # EM 2026-11-12: the catalogue of what is not in store (toolkit/wanted.py): one issue per wanted element; claims keep lanes off it
    from toolkit import wanted as WT
    _iss = [dict(number=7, state="open", body="<!-- wanted:led -->\nx", assignees=[dict(login="ada")], updated_at="2026-11-12T10:00:00Z"),
            dict(number=8, state="open", body="<!-- wanted:fan-cooling -->", assignees=[], updated_at="2026-11-12T10:00:00Z"),
            dict(number=9, state="closed", body="<!-- wanted:port-rj45 -->", assignees=[dict(login="bob")], updated_at="2026-11-12T10:00:00Z")]
    _cl = WT.claimed(WT.claims_csv(_iss)); _sp = WT.specs(); _ids = {x["id"] for x in _sp}
    t("wanted: an open, assigned issue is a claim the lanes skip (an unassigned or closed one is not); every wanted issue names an element with no folder, carries its marker and the claim steps",
      _cl == {"led": "ada"} and not (_ids & set(OW.library.element_ids())) and all(x["body"].startswith(f"<!-- wanted:{x['id']} -->") and "/claim" in x["body"] for x in _sp), f"{_cl} {len(_sp)}")
    # EM 2026-11-13: the sync between the workshop and the public library (toolkit/public_sync.py)
    from toolkit import public_sync as PS
    import subprocess as _sp9, tempfile as _tf9
    with _tf9.TemporaryDirectory() as _d9:
        _g = lambda *a, **k: _sp9.run(["git", *a], cwd=_d9, capture_output=True, text=True, env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}, **k).stdout.strip()
        _g("init", "-q", "-b", "main"); open(os.path.join(_d9, "a"), "w").write("0"); _g("add", "a"); _g("commit", "-qm", "first: the export")
        open(os.path.join(_d9, "a"), "w").write("1"); _g("commit", "-qam", "a contribution"); _c1 = _g("rev-parse", "HEAD")
        open(os.path.join(_d9, "a"), "w").write("2"); _g("commit", "-qam", "From the workshop: x\n\nWorkshop-Sha: " + "f" * 40)
        open(os.path.join(_d9, "a"), "w").write("3"); _g("commit", "-qam", "a second contribution"); _c3 = _g("rev-parse", "HEAD")
        _all = PS.contributions("HEAD", None, cwd=_d9); _after = PS.contributions("HEAD", _c1, cwd=_d9)
    t("public sync: the contributions to bring in are the public commits after the last imported one, never the first commit (the export) nor a workshop sync",
      _all == [_c1, _c3] and _after == [_c3], f"{_all} {_after}")
    # ESCAPE lib/reviews/pneu/r100.md finding 2 (core watch 2026-11-14): valve-gauge-double 1.1's retry found the hung run's gate folder in
    # TRUSTEDPATHS, recorded it as found and put it back (trustedpaths_restored_ok true); 50 of its 55 entries were such leftovers.
    # Entries verbatim from gate/valve-gauge-double-acad.json (its shapes: backslashes, one forward-slash out/, an assembly out/,
    # lane worktrees, EM's Downloads folders and lib\out, which stay)
    from toolkit import acadset as AS
    _tp = ("<PC>;"
           "<PC>;"
           "<PC>;"
           "<PC>;"
           "F:/Foundation/Research/Complexes.org/CAD/lib/elements/term-4mm/out;"
           "<PC>;"
           "<PC>;"
           "<PC>")
    _kp, _dp = AS.split(_tp); _rv = AS.restore_value(_tp)
    t("ESCAPE pneu/r100 2: what a gate puts back in TRUSTEDPATHS drops every element or assembly gate/ or out/ folder of a library worktree "
      "(either slash, a lane's worktree included) that earlier stopped runs left, keeps EM's folders and lib\\out in their order, and a "
      "clean list comes back unchanged",
      len(_dp) == 5 and _kp == _tp.split(";")[:2] + [_tp.split(";")[5]] and _rv == ";".join(_kp) and AS.restore_value(_rv) == _rv
      and AS.leftovers({"trustedpaths_before": _tp}) == _dp and AS.leftovers({}) == [], f"{_kp} | {_dp}")
    return out

def main():
    res = cases(); bad = [r for r in res if not r[1]]
    for name, ok, got in res: print(f"  {'ok  ' if ok else 'MISS'} {name}" + ("" if ok else f"   got: {got}"))
    print(f"selftest: {len(res) - len(bad)} of {len(res)} planted cases called right")
    return not bad
