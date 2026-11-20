#!/usr/bin/env python3
"""pnl-motor-starter: the panel shop's motor-starter panel, built to mc-motor-1's controls spec (lib/assemblies/mc-motor-1/controls.csv;
lib/panel-shop.md "First job"; type motor-starter, lib/panel-types.csv). Built from bom.csv through the toolkit, as pm-motor-starter
is: no geometry of its own. spec.md says which row of the spec each device serves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, cadout, preview
from toolkit.prims import Prims, nodes
ID = "pnl-motor-starter"; VERSION = "0.16"; HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
# A BOM row on file that is not placed yet, with what it waits on. bom.csv keeps its version pin; the row is reported as planned.
# q1 (the door-coupled disconnect) was held 0.1 to 0.5 while lib/motion.csv's three rows that keep its body on the back panel
# named pm-motor-starter only; since the core's answer to request panel-2 (2026-11-11) their scope is p*-motor-starter.
# 0.7: w-pwr, the controller's L-coded supply cordset (cordset-m12 1.8 male-open, request panel-4's answer item 2), is held: its
# cable is 9.8 across (cordset-m12 CABLE_D L) and duct-40x60's slots are 8.0 wide (its SLOT), so no path from plc-1's port-pwr
# into the duct rows or the risers passes the fingers without GEO-020 (every entry to the duct system is a slot or a riser's top
# end); the shop would break a finger out, and the element has no parameter for that (request panel-11 item 1).
# 0.10: duct-40x60 1.3's `breakout` parameter (mech's, the answer to request panel-11 item 1) leaves the finger out where the L
# cable passes a wall (bom.csv: duct-1680 b143, riser-l a906 and a306, duct-1085 a66), so w-pwr is placed; nothing is held.
HOLD = {}
# A placed cordset's route, in the panel's frame (mm): the points of its `path` parameter after the plug's own straight exit
# (cordset-m12: the cable leaves the overmould straight for 12, then follows `path`). bom.csv's params column cannot carry a list
# (library.parse_params reads scalars), so the path lives here and build() turns it into the element's own frame (the inverse of
# the row's placement rotation) before placing the row. Each point's reason is in spec.md section 9.
PATHS = {
    "w-eth": [(278.0, 238.1, 1712.0),      # straight down from port-eth (x 278, over the slot of duct-1680's top wall at x 274 to 282; the wall is z 1718.5 to 1720) into the row
              (284.0, 238.1, 1706.0),      # a 45 degree turn onto the row's run, at the z of riser-r's slot 1702 to 1710
              (1384.0, 238.1, 1706.0),     # along duct-1680 (open right end at x 1362), through riser-r's left-wall slot, to the riser's centre
              (1384.0, 238.1, 1618.0),     # down riser-r
              (1394.0, 238.1, 1606.0),     # a 45 degree turn to the riser's right-wall slot at z 1602 to 1610
              (1416.0, 238.1, 1606.0),     # out through that slot (the wall is x 1402.5 to 1404) toward the right wall
              (1416.0, 200.0, 1590.0),     # toward the front and down, to where p-x1's pigtail ends (x 1381, y 150, z 1570)
              (1416.0, 170.0, 1578.0)],    # the jacket's end; the four leads run 50 on from here (lead-1 to lead-4: wires.csv)
    # 0.10: the L-coded supply lead, at y 229.5 all the way (in front of w-eth's run at y 238.1: 4.9 + 3.3 = 8.2 apart, 8.6 here;
    # behind the cover's skirts, whose y ends at 224.3: 0.3 clear), through four breakouts (spec.md section 9)
    "w-pwr": [(305.0, 229.5, 1714.0),      # down through duct-1680's top wall where finger x 302 to 314 is out (gap 294 to 322), stepping forward to y 229.5
              (305.0, 229.5, 1698.0),      # on down past w-eth's run (z 1706): beside it, 8.6 apart in y
              (299.0, 229.5, 1692.0),      # a 45 degree turn onto the row's run at z 1692 (below w-eth's drop at x 278, whose foot is z 1702.7)
              (140.0, 229.5, 1692.0),      # left along duct-1680, out of its open end (x 162), through riser-l's right wall where finger z 1690 to 1702 is out (gap 1682 to 1710), to the riser's centre
              (140.0, 229.5, 1106.0),      # down riser-l's cavity (x 121.5 to 158.5)
              (146.0, 229.5, 1100.0),      # a 45 degree turn to riser-l's right wall where finger z 1090 to 1102 is out (gap 1082 to 1110)
              (222.0, 229.5, 1100.0),      # right along duct-1085 (cavity z 1086.5 to 1123.5)
              (228.0, 229.5, 1094.0),      # a 45 degree turn down to its bottom wall, where finger x 222 to 234 is out (gap 214 to 242)
              (228.0, 229.5, 1060.0)],     # the jacket's end, 25 under the duct, over X1:7 (x 228); the leads run 50 on (tips about z 1010, 36 over the blocks' top 973.5)
}
def _local(row, pts):
    """world points -> the element's own frame for a row placed at (x, y, z) with its yaw, pitch and roll (prims.rotation_yp)"""
    import numpy as np
    from toolkit.prims import rotation_yp
    R = rotation_yp(row["yaw"], row.get("pitch", 0.0), row.get("roll", 0.0)); at = np.array([row["x"], row["y"], row["z"]], float)
    return [tuple(round(float(c), 3) for c in R.T @ (np.array(p, float) - at)) for p in pts]
def lengths(P, rows):
    """each numbered wire's length from its route (role card r3: "length from the route"), written to out/wire-lengths.csv.
    The method, the shop's: the wire runs square (every leg summed along x, y and z) from end A's node into its first duct at the
    x it stands at, along the duct's centreline to the end the next riser is at, along the riser's centreline to the next row,
    and so on to end B's node. No allowance is added (service loop, strip length: none on file). A wire with an end whose pin has
    no node on file, or one through `door-r` (the hinge loom: no element on file), gets its reason instead of a figure."""
    import csv
    from toolkit import nets, behaviour as BH
    tags = nets.placed(P); duct = library.load("duct-40x60"); D = {}
    for r in rows:
        if r["element"] != "duct-40x60": continue
        n = float(r["params"]["length"]); yc = r["y"] - duct.H / 2
        D[r["tag"]] = dict(v=True, yc=yc, xc=r["x"] - duct.W / 2, lo=r["z"], hi=r["z"] + n) if r["roll"] == -90 else dict(v=False, yc=yc, zc=r["z"] + duct.W / 2, lo=r["x"], hi=r["x"] + n)
    def node(pin):
        tag, mark = pin.rsplit(".", 1)
        if tag not in tags: return None, f"{tag} is not placed"
        n = (BH.spec(tags[tag]) or {"pins": {}})["pins"].get(mark)
        if not n: return None, f"{pin} has no node (request panel-4 item 1)"
        pv = P.pivots.get(tag if n == "self" else f"{tag}.{n}")
        return (tuple(float(c) for c in pv["origin"]), "") if pv else (None, f"{pin}: node {n} is not in the build")
    clamp = lambda v, d: min(max(v, d["lo"]), d["hi"])
    out = []
    for w in nets.wires(ID):
        if not w.get("wire"): continue
        toks = [t.strip() for t in w.get("route", "").split(">") if t.strip()]; ends = [w["from"], w["to"]]
        if toks and toks[0] == "wall-r": toks.reverse(); ends.reverse()
        (a, why_a), (b, why_b) = node(ends[0]), node(ends[1]); why = why_a or why_b
        door = next((t for t in toks if t in ("door-r", "door-l")), None)          # 0.11: door-l too (wire 63 to the left door's stud)
        if not why and door: why = f"{door}: the hinge loom is not an element on file"
        if not why and (not toks or any(t != "wall-r" and t not in D for t in toks)): why = f"route '{w.get('route', '')}' names a duct that is not placed"
        if why: out.append((w["wire"], "", why)); continue
        pts = [a]
        for i, t in enumerate(toks):
            nxt = toks[i + 1] if i + 1 < len(toks) else None; cur = pts[-1]
            if t == "wall-r": continue                                         # from the last duct's point straight (square) to the port
            d = D[t]
            if d["v"]:                                                         # a riser: in at the height it is reached, out at the next row's centreline or the port's height
                pts.append((d["xc"], d["yc"], clamp(cur[2], d)))
                pts.append((d["xc"], d["yc"], D[nxt]["zc"] if nxt in D and not D[nxt]["v"] else clamp(b[2], d)))
            else:                                                              # a row: in at the x it is reached, out at the end the riser is at, the right end for the wall, or end B's x
                pts.append((clamp(cur[0], d), d["yc"], d["zc"]))
                x = clamp(D[nxt]["xc"], d) if nxt in D else d["hi"] if nxt == "wall-r" else clamp(b[0], d)
                pts.append((x, d["yc"], d["zc"]))
        pts.append(b)
        out.append((w["wire"], str(round(sum(abs(q[k] - p[k]) for p, q in zip(pts, pts[1:]) for k in range(3)))), ""))
    with open(os.path.join(OUT, "wire-lengths.csv"), "w", newline="\n", encoding="utf-8") as f:
        csv.writer(f).writerows([("wire", "length_mm", "why_not")] + out)
    return out
def build(report=True, override=None):
    P = Prims(); P.assembly = True; placed, planned = [], []
    for row in library.read_bom(os.path.join(HERE, "bom.csv")):             # reads the risers' `roll` column too (request panel-5's answer, 2026-11-11)
        if override and row["tag"] in override: row = {**row, "params": {**row["params"], **override[row["tag"]]}}
        if row["tag"] in PATHS: row = {**row, "params": {**row["params"], "path": _local(row, PATHS[row["tag"]])}}
        if row["tag"] in HOLD or row["version"].strip() in ("", "-") or not os.path.isdir(os.path.join(library.ELEMENTS, row["element"])): planned.append(row); continue
        library.place_on_hosts(P, row); placed.append(row)                 # a row on enc-1.door-r / wall-r / gland-plate is mounted: the host gets its cut-out
    if not override:
        try: lengths(P, placed)                                             # a report beside the build, never a reason for it to fail
        except Exception as e: print(f"{ID}: wire lengths not written: {type(e).__name__}: {e}")
    if report: print(f"{ID}: placed {len(placed)}; planned {len(planned)}: " + ", ".join(f"{r['tag']}={r['element']}" for r in planned))
    return P
if __name__ == "__main__":
    P = build(); cadout.write_lsp(os.path.join(OUT, ID + ".lsp"), "PNLMS", P, ID); print(" ", cadout.write_glb(os.path.join(OUT, ID + ".glb"), P, ID)["nodes"][:6], "...")
    Fo = preview.mesh(build(report=False, override={"enc-1": dict(swing_l=110, swing_r=110)}))
    preview.render(Fo, f"{ID} doors open", az=265, el=12, center=(762, 240, 1400), height=1500, fname="preview-open.png", out=OUT)
