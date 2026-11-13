"""Lab rooms: the level between a machine and the campus (EM 2026-11-12: the labs and machines become labs inside the campus Labs
building; the campus becomes a virtual school). element -> machine -> lab room -> Labs building -> campus.

A room is one bay of the Labs building, sized from lib/standards/labs-building.csv (copied from the campus model, which lives
outside this repository: its Labs row, its wall thickness and its D2 door; walls centred on the grid lines, partitions between bays,
each bay's door on the south wall at the middle of its run). Windows and the clerestory are the campus model's, not drawn here.
Room frame: millimetres, Z up, origin at the bay's inner south-west corner (the wall faces), +y north. The campus places the room
at world (metres) campus_origin(bay), x 1000 smaller: the one scale boundary of the virtual school manifest (2026-11-01).

The room's shell (floor slab, the four walls with the door) is built here for the library's own checks and a standalone walk; the
campus brings its own shell, so a room exports its contents alone for the campus (build(shell=False)).

Checks (scope assembly, toolkit/validate.assembly_run, on any assembly that has room.csv):
ROOM-010 every machine placed in the room lies inside the clear floor and below the eaves.
ROOM-020 NFPA 70 110.26(A): in front of every enclosure's door face, a working space the equipment's width (at least 762 mm) by
         1981 mm high, free of every solid for the depth Table 110.26(A)(1) gives; the depth to the nearest wall face (a grounded
         surface, brick) is at least condition 2's. lib/standards/clearances.csv carries the figures.
ROOM-030 the door's opening (D2, from the campus rules) and 1000 mm in front of it inside the room are clear.
"""
import csv, json, math, os
from . import library
from .prims import Prims, extents

LIB = library.ROOT


def _csv(path):
    return [r for r in csv.DictReader(l for l in open(path, encoding="utf-8") if not l.startswith("#"))] if os.path.isfile(path) else []


def labs():
    """lib/labs.csv rows by bay number"""
    return {int(r["bay"]): r for r in _csv(os.path.join(LIB, "labs.csv"))}


def clearances():
    """lib/standards/clearances.csv: {key: (value, unit, source)}"""
    return {r["key"]: (float(r["value"]), r["unit"], r["source"]) for r in _csv(os.path.join(LIB, "standards", "clearances.csv"))}


def building():
    """the Labs building (metres): lib/standards/labs-building.csv, copied from the campus model"""
    v = {r["key"]: float(r["value"]) for r in _csv(os.path.join(LIB, "standards", "labs-building.csv"))}
    return dict(x=v["x"], y=v["y"], dx=v["dx"], dy=v["dy"], h=v["eaves"], bays=int(v["bays"]), t=v["wall"], door_w=v["door_w"],
                door_h=v["door_h"], wall_bay=v["wall_bay"])


def bay(n, B=None):
    """bay n (1 = west): its clear size and door in the room frame (mm), and where its origin sits on the campus (m)"""
    B = B or building()
    if not 1 <= n <= B["bays"]: raise ValueError(f"bay {n}: the Labs building has bays 1 to {B['bays']}")
    bw = B["dx"] / B["bays"]; t = B["t"]
    x0 = B["x"] + (n - 1) * bw                                            # the bay's west grid line (a wall centre line)
    run_nb = max(1, math.ceil(bw / B["wall_bay"] - 1e-9)); seg = bw / run_nb      # the campus model's wall runs split into bays of wall_bay
    door_c = (run_nb // 2 + 0.5) * seg - t / 2                            # Run.door_bay, measured from the inner face of the west wall
    return dict(n=n, dx=round((bw - t) * 1000, 1), dy=round((B["dy"] - t) * 1000, 1), h=round(B["h"] * 1000, 1), wall=round(t * 1000, 1),
                door_x=round(door_c * 1000, 1), door_w=B["door_w"] * 1000, door_h=B["door_h"] * 1000,
                campus_origin=(round(x0 + t / 2, 4), round(B["y"] + t / 2, 4), 0.0))


def shell(P, b):
    """the room's floor and walls into P (room frame, mm): named nodes room.floor, room.wall-s / -n / -w / -e"""
    t, dx, dy, h = b["wall"], b["dx"], b["dy"], b["h"]
    P.box("node:room.floor|M-CONCRETE", -t, -t, -200, dx + 2 * t, dy + 2 * t, 200)
    d0, d1 = b["door_x"] - b["door_w"] / 2, b["door_x"] + b["door_w"] / 2
    P.box("node:room.wall-s|M-WALL", -t, -t, 0, d0 + t, t, h)                       # south wall, west of the door
    P.box("node:room.wall-s|M-WALL", d1, -t, 0, dx + t - d1, t, h)                  # east of the door
    P.box("node:room.wall-s|M-WALL", d0, -t, b["door_h"], d1 - d0, t, h - b["door_h"])   # over the door
    P.box("node:room.wall-n|M-WALL", -t, dy, 0, dx + 2 * t, t, h)
    P.box("node:room.wall-w|M-WALL", -t, 0, 0, t, dy, h)
    P.box("node:room.wall-e|M-WALL", dx, 0, 0, t, dy, h)
    P.pivot("room.door", "fixed", (b["door_x"], 0, 0), axis=(0, 1, 0), w=b["door_w"], h=b["door_h"])
    return P


# ---------------------------------------------------------------- checks
def _boxes(P, skip=("room.",)):
    """[(name, lo, hi)] of every solid but the shell's, as boxes"""
    out = []
    for i, (L, k, q) in enumerate(P):
        if L.startswith("collider:") or k in ("hole", "cut"): continue
        name = L[5:].split("|")[0] if L.startswith("node:") else "body"
        if any(name.startswith(s) for s in skip): continue
        lo, hi = extents([(L, k, q)]); out.append((name, lo, hi))
    return out


def _hit(lo, hi, blo, bhi, eps=1.0):
    return all(lo[i] < bhi[i] - eps and hi[i] > blo[i] + eps for i in range(3))


def enclosures(P):
    """[(tag, lo, hi)] of every placed enclosure (element CLASS 'enclosure') in P, from P.owners"""
    out = []
    for a, z, tag, eid in getattr(P, "owners", []):
        try: cls = library.load(eid).CLASS
        except Exception: continue
        if cls == "enclosure" and z > a:
            lo, hi = extents(P[a:z]); out.append((tag, lo, hi))
    return out


def check(aid, P, b, volts_to_ground=None):
    """ROOM-010 / 020 / 030 findings [(status, rule, where, message)] for room assembly aid built in P (shell included)"""
    F, C = [], clearances()
    body = _boxes(P)
    if not body: return [("REVIEW", "ROOM-010", aid, "no machine placed in the room yet")]
    lo, hi = extents([(L, k, q) for L, k, q in P if not (L.startswith("node:room.") or L.startswith("collider:")) and k not in ("hole", "cut")])
    lo, hi = tuple(float(v) for v in lo), tuple(float(v) for v in hi)
    inside = lo[0] >= -0.5 and lo[1] >= -0.5 and lo[2] >= -0.5 and hi[0] <= b["dx"] + 0.5 and hi[1] <= b["dy"] + 0.5 and hi[2] <= b["h"] + 0.5
    F.append(("PASS" if inside else "FAIL", "ROOM-010", aid, f"the machines span ({lo[0]:.0f}, {lo[1]:.0f}, {lo[2]:.0f}) to ({hi[0]:.0f}, {hi[1]:.0f}, {hi[2]:.0f}) mm; the clear room is {b['dx']} x {b['dy']} mm, {b['h']} mm to the eaves"))
    v = volts_to_ground
    cond = "151-600" if v is None or v > 150 else "0-150"
    d1 = C[f"depth-{cond}-c1"][0]; d2 = C[f"depth-{cond}-c2"][0]; wmin = C["width-min"][0]; hmin = C["height-min"][0]
    src = C[f"depth-{cond}-c1"][2]
    for tag, elo, ehi in enclosures(P):
        front = elo[1]                                                     # rooms place machines facing -y (south, the door)
        w0, w1 = elo[0], max(ehi[0], elo[0] + wmin)
        space = ((w0, front - d1, 0.0), (w1, front - 0.5, max(hmin, ehi[2])))
        hits = sorted({n for n, blo, bhi in body if _hit(space[0], space[1], blo, bhi) and not n.startswith(tag)})
        F.append(("FAIL" if hits else "PASS", "ROOM-020", tag,
                  (f"working space {w1 - w0:.0f} x {d1:.0f} x {space[1][2]:.0f} mm in front of the door face at y {front:.0f}: "
                   + (f"obstructed by {', '.join(hits[:6])}" if hits else "clear") + f" ({src}; {cond} V to ground, condition 1)")))
        wall = front - 0.0                                                 # the south wall's inner face is y 0
        F.append(("PASS" if wall >= d2 - 0.5 else "FAIL", "ROOM-020", tag,
                  f"{wall:.0f} mm from the door face to the wall opposite (a grounded surface: condition 2 needs {d2:.0f} mm)"))
    dlo = (b["door_x"] - b["door_w"] / 2, 0.0, 0.0); dhi = (b["door_x"] + b["door_w"] / 2, C["door-approach"][0], b["door_h"])
    hits = sorted({n for n, blo, bhi in body if _hit(dlo, dhi, blo, bhi)})
    F.append(("FAIL" if hits else "PASS", "ROOM-030", aid, f"the door ({b['door_w']:.0f} x {b['door_h']:.0f} mm at x {b['door_x']:.0f}) and "
              f"{C['door-approach'][0]:.0f} mm inside it: " + (f"obstructed by {', '.join(hits[:6])}" if hits else "clear") + f" ({C['door-approach'][2]})"))
    return F


def run(aid, P, root=None):
    """validate.assembly_run's hook: the ROOM findings of an assembly that has room.csv (its bay), [] for any other"""
    rc = os.path.join(LIB, "assemblies", aid, "room.csv")
    if not os.path.isfile(rc): return []
    r = {x["key"]: x["value"] for x in _csv(rc)}
    v = float(r["volts_to_ground"]) if r.get("volts_to_ground") else None
    return check(aid, P, bay(int(r["bay"])), v)
