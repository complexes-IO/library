"""The library: find, load, place and emit elements. An element is lib/elements/<id>/element.py exposing
  ID, VERSION ("major.minor"), CLASS, TITLE, TOOLKIT (toolkit version it was last built with), BASELINE, ORIGIN (text), COMMAND (AutoLISP),
  PARAMS (dict of defaults), build(**params) -> Prims, PREVIEWS (list of dicts: name, az, el[, center, height, params]),
  optionally CUTOUT (mm, for panel operators the host cuts a hole for), drawing(path), and a bom.csv beside it for the elements it carries.
A BOM row: element, version, tag, parent, x, y, z, yaw, params, note; optional pitch (about the element's own x) and roll (its own y). Placing an element renames its node `self` to the tag and every
other node to `tag.node`, so a twin reads one flat namespace per assembly."""
import csv, importlib.util, math, os, re, sys, warnings
import numpy as np
from . import VERSION as TOOLKIT_VERSION, cadout, preview
from .prims import Prims, transform, solids, rotation_yp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELEMENTS = os.path.join(ROOT, "elements")
_loaded = {}


def preview_names(names):
    """file stems for preview-<stem>.png: the first word, the whole name when two share it. The first word keeps only
    [A-Za-z0-9._-] (so "D-coded" and "1.5" keep their names), the whole name is made [a-z0-9-]
    (round 10 return: "male, pin 2 bent" wrote preview-male,.png beside preview-male.png)."""
    slug = lambda x: re.sub(r"[^a-z0-9]+", "-", x.lower()).strip("-")
    first = [re.sub(r"[^A-Za-z0-9._-]+", "", n.split()[0]).strip("._-") if n.split() else "" for n in names]
    return [f if f and first.count(f) == 1 else slug(n) for f, n in zip(first, names)]

def element_ids():
    return sorted(d for d in os.listdir(ELEMENTS) if os.path.isfile(os.path.join(ELEMENTS, d, "element.py")))

def load(eid, version=None):
    """import elements/<eid>/element.py; a pinned version must match on the major and be <= the library's minor"""
    if eid not in _loaded:
        path = os.path.join(ELEMENTS, eid, "element.py")
        if not os.path.isfile(path): raise FileNotFoundError(f"{eid}: not in the library yet ({path})")
        spec = importlib.util.spec_from_file_location(f"element_{eid.replace('-', '_')}", path); mod = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = mod; spec.loader.exec_module(mod)
        if mod.ID != eid: raise ValueError(f"{eid}: element.py says ID = {mod.ID}")
        _loaded[eid] = mod
    mod = _loaded[eid]
    if version:
        want = tuple(int(v) for v in str(version).split(".")); have = tuple(int(v) for v in mod.VERSION.split("."))
        if want[0] != have[0] or want[1] > have[1]: raise ValueError(f"{eid}: BOM pins {version}, library has {mod.VERSION} (incompatible)")
        if want != have: warnings.warn(f"{eid}: BOM pins {version}, building with {mod.VERSION} (minor change, same nodes and origin)")
    return mod

def parse_params(s):
    out = {}
    for kv in (s or "").split(";"):
        if "=" not in kv: continue
        k, v = (x.strip() for x in kv.split("=", 1))
        if v.lower() in ("true", "false"): out[k] = v.lower() == "true"
        else:
            try: out[k] = float(v) if "." in v else int(v)
            except ValueError: out[k] = v
    return out

def read_bom(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r.get("element") and not r["element"].startswith("#")]
    for r in rows:
        for k in ("x", "y", "z", "yaw", "pitch", "roll"): r[k] = float(r.get(k) or 0)  # pitch, roll: optional columns, about the element's own x, y (roll: request panel-5 1)
        r["params"] = parse_params(r.get("params", ""))
    return rows

def _moving_host(P, parent):
    """a child placed on a part that moves (a door, a lid) puts its unnamed solids into that part's node, so it rides along in the
    export (the enclosure's door e-stop: its housing was fused into the cabinet and stayed behind when the door opened, EM
    2026-11-08); the element's node list is unchanged"""
    pv = getattr(P, "pivots", {}).get(parent)
    return bool(pv) and pv.get("kind") in ("rotate", "translate")


def place(P, row, prims=None):
    """append an element instance to P per a BOM row; returns (module, first index). prims may be passed when already built.
    In an assembly (P.assembly set by assembly.py) the element's unnamed solids become its own part, <tag>.body, so every placed
    element can be taken out of the machine whole (EM 2026-11-08: the engineer learns to replace parts); inside an element,
    children stay in the element's body."""
    mod = load(row["element"], row.get("version"))
    body = prims if prims is not None else mod.build(**{**getattr(mod, "PARAMS", {}), **row["params"]})
    tag = row["tag"]
    def rename(n):                       # tag "self": the child IS this element's node self (a port-m12-a is its receptacle), names kept
        return n if tag == "self" else (tag if n == "self" else f"{tag}.{n}")
    base = len(P); tp = transform(body, (row["x"], row["y"], row["z"]), row["yaw"], rename, base, row.get("pitch", 0.0), row.get("roll", 0.0),
                                  own_body=True if getattr(P, "assembly", False) else (row.get("parent", "") if _moving_host(P, row.get("parent", "")) else False)); P.extend(tp); P.pivots.update(tp.pivots)
    if hasattr(P, "owners"): P.owners.extend(tp.owners); P.owners.append((base, len(P), tag, mod.ID))   # who owns which primitives (validation)
    if hasattr(P, "hosts"): P.hosts.update(tp.hosts)                                                   # surfaces it offers (tag.name)
    if hasattr(P, "parents"): P.parents.update(tp.parents); P.parents[tag] = row.get("parent", "")
    if hasattr(P, "params"): P.params.update(tp.params); P.params[tag] = {**getattr(mod, "PARAMS", {}), **row["params"]}
    if hasattr(P, "parts"): P.parts.update(tp.parts)                                                    # part names, the instance's tag before them
    if hasattr(P, "radii"): P.radii.update(tp.radii)                                                    # a primitive's own fillet radius
    return mod, base

def mount(P, row, panel, panel_t):
    """place a panel operator and cut its cut-out through the host's panel primitive (index `panel`, thickness panel_t along the
    operator's local +y). The row's x, y, z is the cut-out centre on the panel's front face."""
    mod = load(row["element"], row.get("version"))
    if "panel_t" in getattr(mod, "PARAMS", {}): row = {**row, "params": {**row["params"], "panel_t": panel_t}}   # the operator's parts behind the panel start past it
    mod, base = place(P, row)
    r = getattr(mod, "CUTOUT", None); rect = getattr(mod, "CUTOUT_RECT", None)
    R = rotation_yp(row["yaw"], row.get("pitch", 0.0), row.get("roll", 0.0)); d = R @ np.array([0.0, 1.0, 0.0])   # local +y after roll, pitch and yaw
    c = np.array([row["x"], row["y"], row["z"]])
    if r: P.hole("M-GASKET", tuple(c - d * 1.0), tuple(c + d * (panel_t + 1.0)), r / 2, panel)
    if rect:                                                                                   # (w along local x, h along local z), centred
        w, h = rect; ex, ez = R @ np.array([1.0, 0, 0]), R @ np.array([0, 0, 1.0])
        P.cut("M-GASKET", tuple(c - ex * w / 2 - ez * h / 2 - d * 1.0), tuple(ex), tuple(d), tuple(ez), w, panel_t + 2.0, h, panel)
    return mod, base

def place_on_hosts(P, row):
    """place a BOM row; when its parent is a host surface of something already placed (enc-1.door-r, enc-1.wall-r), mount it there
    so the host gets the element's cut-out"""
    if row.get("parent") in getattr(P, "hosts", {}):
        idx, t = P.hosts[row["parent"]]; return mount(P, row, idx, t)
    return place(P, row)

def own_bom(mod):
    path = os.path.join(os.path.dirname(os.path.abspath(mod.__file__)), "bom.csv")
    return read_bom(path) if os.path.isfile(path) else []

def variant_glb(eid, suffix, params, folder=None):
    """a gated variant's glb, made by a command on file (lessons 2026-11-06, round 13 back: relay-ice-cube-2co's cutaway Blender result came
    from a scratch glb, so no run could redo it): `python lib/build.py glb <id> <suffix> k=v ...` writes gate/<id>-<suffix>.glb (git-
    ignored), the element built with its PARAMS and the given ones, the glb named for the Blender gate's result gate/<id>-<suffix>.json.
    A suffix is [a-z0-9-]; a parameter the element doesn't take is refused, never passed through. Returns the path."""
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", suffix or ""): raise ValueError(f"variant suffix {suffix!r}: [a-z0-9-] only")
    mod = load(eid); defaults = getattr(mod, "PARAMS", {})
    unknown = sorted(set(params) - set(defaults))
    if unknown: raise ValueError(f"{eid} takes no parameter {', '.join(unknown)} (PARAMS: {', '.join(sorted(defaults)) or 'none'})")
    name = f"{eid}-{suffix}"; folder = folder or os.path.join(ELEMENTS, eid, "gate"); os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, name + ".glb")
    cadout.write_glb(path, mod.build(**{**defaults, **params}), name)
    return path

def emit(mod, out=None, previews=True):
    """write an element's outputs into its out/: <id>.lsp, <id>.glb, <id>-drawing.svg, preview-*.png. Returns a summary dict."""
    here = os.path.dirname(os.path.abspath(mod.__file__)); out = out or os.path.join(here, "out"); os.makedirs(out, exist_ok=True)
    P = mod.build(**getattr(mod, "PARAMS", {}))
    cadout.write_lsp(os.path.join(out, mod.ID + ".lsp"), mod.COMMAND, P, f"{mod.ID} v{mod.VERSION}")
    info = cadout.write_glb(os.path.join(out, mod.ID + ".glb"), P, mod.ID)
    if hasattr(mod, "drawing"): mod.drawing(os.path.join(out, mod.ID + "-drawing.svg"))
    if previews:
        F = preview.mesh(P); pv = getattr(mod, "PREVIEWS", [])
        for v, nm in zip(pv, preview_names([v["name"] for v in pv])):
            Fv = preview.mesh(mod.build(**{**getattr(mod, "PARAMS", {}), **v["params"]})) if v.get("params") else F
            preview.render(Fv, f"{mod.ID} {v['name']}", az=v.get("az", 250), el=v.get("el", 20), center=v.get("center"), height=v.get("height"),
                           fname=f"preview-{nm}.png", out=out)
    return dict(id=mod.ID, version=mod.VERSION, primitives=len(P), **info)
