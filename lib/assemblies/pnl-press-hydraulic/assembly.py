#!/usr/bin/env python3
"""pnl-press-hydraulic: the panel shop's control panel for the hydraulic press, built to press-hydraulic's controls spec
(lib/assemblies/press-hydraulic/controls.csv; lib/panel-shop.md "Second job"; a wall-mount enc-wm). Built from bom.csv through the
toolkit, as pnl-motor-starter is: no geometry of its own. spec.md says which row of the spec each device serves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import library, cadout, preview
from toolkit.prims import Prims
ID = "pnl-press-hydraulic"; VERSION = "0.12"; HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
# A BOM row on file that is not placed yet, with what it waits on. bom.csv keeps its version pin; the row is reported as planned.
# q1 (the door-coupled disconnect) was held 0.1 to 0.4: its parent is enc-1.door (the door gets the handle's cut-out), so MOT-010
#     swung the whole switch with the door until lib/motion.csv (the core's) carried this panel's three rows (body excluded from
#     enc-1.door, door-unit and handle follow it: request panel-10's answer, 2026-11-11). Placed since 0.5, the body on the plate.
# f1 was held 0.1 to 0.7: overload-9a-1no1nc mounts on its contactor's lower terminals, and no contactor at the motor's current was
#     an element (request panel-6 item 1). Since 0.8 k1 is contactor-18a-1no 1.0 (elec-r35) and f1 is placed under it; nothing is held.
HOLD = {}
# A placed cordset's route, in the panel's frame (mm): the points of its `path` parameter after the plug's own straight exit
# (cordset-m12: the cable leaves the overmould straight for 12, then follows `path`). bom.csv's params column cannot carry a list
# (library.parse_params reads scalars), so the path lives here and build() turns it into the element's own frame (the inverse of
# the row's placement rotation) before placing the row: pnl-motor-starter's PATHS and _local, the same method. spec.md section 9.
# 0.8: the L-coded supply lead at y 184.4 (pnl-motor-starter's 229.5 on a plate at 275.6: this plate is at 230.5), behind the
# cover's skirts (y to 179.2) and inside the fingers' zone (y 172.8 to 197.8), through duct-145's two breakouts (bom.csv b226 / a66).
PATHS = {
    "w-pwr": [(326.0, 184.4, 172.0),      # down through duct-145's top wall where finger x 320 to 332 is out (gap 312 to 340), stepping forward to y 184.4
              (320.0, 184.4, 166.0),      # a 45 degree turn onto the row's run at z 166 (cavity z 146.5 to 183.5)
              (172.0, 184.4, 166.0),      # left along duct-145
              (166.0, 184.4, 160.0),      # a 45 degree turn down to its bottom wall, where finger x 160 to 172 is out (gap 152 to 180)
              (166.0, 184.4, 142.0),      # down through the gap (the wall is z 145 to 146.5), 3 under the duct
              (166.0, 176.4, 138.0)],     # the jacket's end, turned toward the front (0.9: 2 forward for 1 down; 0.8's 45 degrees put the leads through jmp-1's cap, z 110.2 to 118.2 at y 158.9 to 166.9): the leads run 50 on along it, over the comb (z 129 at its front face) and in front of the blocks (front y 178.5), over X1:4 and X1:11
}
def _local(row, pts):
    """world points -> the element's own frame for a row placed at (x, y, z) with its yaw, pitch and roll (prims.rotation_yp)"""
    import numpy as np
    from toolkit.prims import rotation_yp
    R = rotation_yp(row["yaw"], row.get("pitch", 0.0), row.get("roll", 0.0)); at = np.array([row["x"], row["y"], row["z"]], float)
    return [tuple(round(float(c), 3) for c in R.T @ (np.array(p, float) - at)) for p in pts]
def lengths(P, rows):
    """each numbered wire's length from its route (role card r3), written to out/wire-lengths.csv: pnl-motor-starter's lengths()
    (its assembly.py), the same method, with `door` as this enclosure's hinge loom token (enc-wm has one door). Square legs
    from end A's node into its first duct, along the ducts' centrelines, to end B's node; no allowance (none on file)."""
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
        (a, why_a), (b, why_b) = node(ends[0]), node(ends[1]); why = why_a or why_b
        if not why and "door" in toks: why = "door: the hinge loom is not an element on file"
        if not why and (not toks or any(t not in D for t in toks)): why = f"route '{w.get('route', '')}' names a duct that is not placed"
        if why: out.append((w["wire"], "", why)); continue
        pts = [a]
        for i, t in enumerate(toks):
            nxt = toks[i + 1] if i + 1 < len(toks) else None; cur = pts[-1]; d = D[t]
            if d["v"]:                                                         # a riser: in at the height it is reached, out at the next row's centreline or end B's height
                pts.append((d["xc"], d["yc"], clamp(cur[2], d)))
                pts.append((d["xc"], d["yc"], D[nxt]["zc"] if nxt in D and not D[nxt]["v"] else clamp(b[2], d)))
            else:                                                              # a row: in at the x it is reached, out at the end the riser is at, or end B's x
                pts.append((clamp(cur[0], d), d["yc"], d["zc"]))
                pts.append((clamp(D[nxt]["xc"], d) if nxt in D else clamp(b[0], d), d["yc"], d["zc"]))
        pts.append(b)
        out.append((w["wire"], str(round(sum(abs(q[k] - p[k]) for p, q in zip(pts, pts[1:]) for k in range(3)))), ""))
    with open(os.path.join(OUT, "wire-lengths.csv"), "w", newline="\n", encoding="utf-8") as f:
        csv.writer(f).writerows([("wire", "length_mm", "why_not")] + out)
    return out
def build(report=True, override=None):
    P = Prims(); P.assembly = True; placed, planned = [], []
    for row in library.read_bom(os.path.join(HERE, "bom.csv")):
        if override and row["tag"] in override: row = {**row, "params": {**row["params"], **override[row["tag"]]}}
        row["roll"] = float(row.get("roll") or 0)                           # bom.csv's roll column (the risers: a duct on end). library.read_bom reads pitch only: request panel-5
        if row["tag"] in PATHS: row = {**row, "params": {**row["params"], "path": _local(row, PATHS[row["tag"]])}}
        if row["tag"] in HOLD or row["version"].strip() in ("", "-") or not os.path.isdir(os.path.join(library.ELEMENTS, row["element"])): planned.append(row); continue
        library.place_on_hosts(P, row); placed.append(row)                 # a row on enc-1.door is mounted: the door gets its cut-out
    if not override:
        try: lengths(P, placed)                                             # a report beside the build, never a reason for it to fail
        except Exception as e: print(f"{ID}: wire lengths not written: {type(e).__name__}: {e}")
    if report: print(f"{ID}: placed {len(placed)}; planned {len(planned)}: " + ", ".join(f"{r['tag']}={r['element']}" for r in planned))
    return P
if __name__ == "__main__":
    P = build(); cadout.write_lsp(os.path.join(OUT, ID + ".lsp"), "PNLPH", P, ID); print(" ", cadout.write_glb(os.path.join(OUT, ID + ".glb"), P, ID)["nodes"][:6], "...")
    # the door closed: enc-wm 1.1 has no parameter that opens its door, so the inside is not in a preview yet (request panel-6 item 5)
    preview.render(preview.mesh(P), f"{ID} door closed", az=250, el=20, fname="preview-front.png", out=OUT)
