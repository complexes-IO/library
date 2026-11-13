"""The operable twin of one machine in Godot (lib/toolkit/twin/twin.gd; EM 2026-11-08: test one system through the three tools).

    python lib/build.py twin <assembly-id>            builds the assembly, exports its glb, imports it into the twin's Godot
                                                      project (lib/toolkit/twin) and opens the twin in a window (press E: the
                                                      e-stop; the HUD lists every input and its key)
    python lib/build.py twin <assembly-id> --smoke    no window: works every input in turn, prints the STATE lines, writes
                                                      lib/assemblies/<id>/qa/twin.json (the core's headless check)

The scene is lib/toolkit/twin/scenes/<id>.json: which of the solver's inputs the operator can work (`solver`: a manual state
<tag>.<state> of an element, or a sources.csv / wires.csv `when` name), each with a key and a short label; `show` flags; `report`
nodes; the `smoke` sequence. Nothing else: the parts are driven by the solver (toolkit/nets.py; lib/behaviour.md, EM 2026-11-09:
behaviour emerges from the elements), which solved() runs for every combination of those inputs and writes to
res://out/<id>-solved.json: poses, flags, each net's potential and the probe points. The twin reads the table; the meter (press P,
click two terminals) reads two nets. The table is memoryless: a machine whose behaviour depends on history (a seal-in) needs the
solver live, which is the next step. The glb is the assembly's own export, every placed element its own node, moving parts with the
writer's motion extras (toolkit/cadout.py). Godot: $GODOT, or the PC's godot_console.exe. The project is core-owned."""
import os, sys, json, shutil, subprocess, hashlib, struct, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__)); LIB = os.path.dirname(HERE); TWIN = os.path.join(HERE, "twin")
GODOT = os.environ.get("GODOT") or os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "WinGet", "Links", "godot_console.exe")

IMPORT = """[remap]

importer="scene"
importer_version=1
type="PackedScene"
path="res://.godot/imported/{id}.glb-{h}.scn"

[deps]

source_file="res://assets/{id}.glb"
dest_files=["res://.godot/imported/{id}.glb-{h}.scn"]

[params]

nodes/root_type=""
nodes/root_name=""
nodes/root_script=null
mesh_library/use_node_names_as_mesh_names=false
array_mesh/deduplicate_surfaces=true
nodes/apply_root_scale=true
nodes/root_scale=1.0
nodes/import_as_skeleton_bones=false
nodes/use_name_suffixes=true
nodes/use_node_type_suffixes=true
meshes/ensure_tangents=true
meshes/generate_lods=true
meshes/create_shadow_meshes=true
meshes/light_baking=1
meshes/lightmap_texel_size=0.2
meshes/force_disable_compression=false
skins/use_named_skins=true
animation/import=true
animation/fps=30
animation/trimming=false
animation/remove_immutable_tracks=true
animation/import_rest_as_RESET=false
import_script/path=""
materials/extract=0
materials/extract_format=0
materials/extract_path=""
_subresources={{
"materials": {{
{mats}
}}
}}
gltf/naming_version=2
gltf/embedded_image_handling=1
gltf/texture_map_mode=1
"""


def tres(name):
    from .cadout import MATERIALS, EMISSIVE
    (r, g, b, a), metallic, rough = MATERIALS.get(name, ((0.6, 0.6, 0.6, 1), 0, 0.5)); em = EMISSIVE.get(name)
    body = ['[gd_resource type="StandardMaterial3D" format=3]', "", "[resource]", f'resource_name = "{name}"', f"albedo_color = Color({r}, {g}, {b}, {a})",
            f"metallic = {metallic}", f"roughness = {rough}"]
    if a < 1: body.append("transparency = 1")
    if em: body += ["emission_enabled = true", f"emission = Color({em[0]}, {em[1]}, {em[2]}, 1)", "emission_energy_multiplier = 0.0"]
    return "\n".join(body) + "\n"


def glb_materials(path):
    with open(path, "rb") as f:
        f.read(12); jl, jt = struct.unpack("<II", f.read(8)); js = json.loads(f.read(jl))
    return [m["name"] for m in js.get("materials", [])]


def solved(aid, P, scene, out_path):
    """the solver's table for the scene's inputs: poses, flags, nets and probes per combination; written to out_path. Returns the table."""
    from . import nets as NT, behaviour as BH
    E = NT.elements(P); SRC = NT.sources(aid); W = NT.wires(aid); known = NT.input_names(E, SRC, W)
    order = list(scene["inputs"].keys()); solver = {k: scene["inputs"][k].get("solver", k) for k in order}
    missing = [f"{k} -> {solver[k]}" for k in order if solver[k] not in known]
    if missing: print(f"{aid}: scene inputs the solver doesn't know: {', '.join(missing)} (of {', '.join(sorted(known))})")
    inputs = {}
    for k in order:
        d = dict(known.get(solver[k], dict(kind="toggle", cleared_by="", tag="", state=solver[k])))
        node = scene["inputs"][k].get("node", "")
        if not node and d.get("tag"):                                                 # the node its pose rows move, for clicking
            e = E[d["tag"]]
            for nodes, when, amt in e.S["poses"]:
                if when == d["state"] and nodes and nodes[0] != "*": node = e.tag if nodes[0] == "self" else f"{e.tag}.{nodes[0]}"; break
        cleared = next((kk for kk in order if d.get("cleared_by") and solver[kk] == f"{d['tag']}.{d['cleared_by']}"), "")
        inputs[k] = dict(kind=d.get("kind", "toggle"), cleared_by=cleared, node=node, key=scene["inputs"][k].get("key", ""), short=scene["inputs"][k].get("short", k), solver=solver[k])
    g = lambda v: [round(float(v[0]) / 1000.0, 5), round(float(v[2]) / 1000.0, 5), round(-float(v[1]) / 1000.0, 5)]   # as cadout.write_glb
    probes = {}
    for e in E.values():
        for mark, node in e.S["pins"].items():
            pv = P.pivots.get(f"{e.tag}.{node}") if node else None
            for marks in e.S.get("forms", {}).values():                              # a form's node, where the placed build is that form
                if not pv and marks.get(mark) and P.pivots.get(f"{e.tag}.{marks[mark]}"): pv = P.pivots[f"{e.tag}.{marks[mark]}"]
            if pv and pv.get("origin") is not None: probes[e.pin(mark)] = g(pv["origin"])
    states = {}; pins_all = sorted({e.pin(m) for e in E.values() for m in e.S["pins"]}); netmaps = []; netkey = {}
    import itertools
    for bits in itertools.product((0, 1), repeat=len(order)):
        inp = {solver[k]: bool(b) for k, b in zip(order, bits)}
        for e in E.values(): e.__init__(e.tag, e.eid, e.S)
        r = NT.solve(aid, inp, P=P, E=E, W=W, SRC=SRC)
        net_of = {}; pots = {}; ids = {}
        for pin in pins_all:
            root = r.nets.find(pin); i = ids.setdefault(root, len(ids)); net_of[pin] = i
            if i not in pots:
                pot = r.pots.get(root); pots[i] = None if pot is None or (pot.ac is None and pot.dc is None) else [round(pot.ac.real, 2) if pot.ac is not None else 0.0, round(pot.ac.imag, 2) if pot.ac is not None else 0.0, round(pot.dc, 2) if pot.dc is not None else 0.0]
        key = json.dumps(net_of, sort_keys=True)
        if key not in netkey: netkey[key] = len(netmaps); netmaps.append(net_of)        # most combinations share a connectivity
        poses = {k: v for k, v in r.poses(P).items() if v}
        for e in E.values():                                                              # a placed element's `self` is the tag's own node
            if f"{e.tag}.self" in poses: poses[e.tag] = poses.pop(f"{e.tag}.self")
        states["".join(str(b) for b in bits)] = dict(poses=poses, flags=sorted(k for k, v in r.flags().items() if v), nets=netkey[key], pots={str(k): v for k, v in pots.items()}, over=r.over(), stable=r.stable)
    table = dict(asset=aid, order=order, inputs=inputs, probes=probes, pins=pins_all, netmaps=netmaps, states=states, layers=layers(aid, P, E, W))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    json.dump(table, open(out_path, "w", encoding="utf-8"), separators=(",", ":"))
    rest = states["0" * len(order)]
    print(f"{aid}: solved {len(states)} combinations of {len(order)} inputs; {len(probes)} probe points; at rest {len(rest['flags'])} flags" + (f"; OVER: {rest['over']}" if rest["over"] else ""))
    return table

# layer colours: the real wire and line colours (NFPA 79 13.2.4; ISO 1219 for fluid lines); structure grey, safety yellow
LAYER_COLOUR = {"480 VAC power": "#202020", "480 VAC & 120 VAC power": "#202020", "control (mains)": "#c0392b", "control & 24 VDC": "#1f5fbf", "control & 24 VDC supply": "#1f5fbf",
                "Ethernet & communication": "#2a9d8f", "ground": "#2e8b3a", "hydraulic": "#b02020", "pneumatic": "#3a7fc1", "safety": "#e0b000", "structure": "#8a8a8a", "mechanism": "#7a5c99", "field": "#777777", "field (bench test)": "#777777"}


def layers(aid, P, E, W):
    """the machine's layers, from its elements (lib/flows.md: a layer exists because an element carries it): one per wires.csv section
    (the elements whose pins the section's wires land on), hydraulic and pneumatic from hydraulic.csv / air.csv, safety from the
    inventory's safety column, mechanism from the moving nodes, structure for everything left. {name: dict(tags, colour, key)}"""
    import csv as _c
    from . import nets as NT
    adir = os.path.join(LIB, "assemblies", aid); tags = NT.placed(P); out = {}
    def tag_of(pin): return pin.rsplit(".", 1)[0] if "." in pin else pin
    for w in W:
        sec = (w.get("section") or "").strip() or "wiring"
        if sec.startswith("field"): continue                                           # a stand-in for an outside contact, not a circuit of the machine
        for pin in (w["from"], w["to"]):
            t = tag_of(pin)
            if t in tags: out.setdefault(sec, set()).add(t)
    for fn, name in (("hydraulic.csv", "hydraulic"), ("air.csv", "pneumatic")):
        f = os.path.join(adir, fn)
        if os.path.isfile(f):
            for r in _c.DictReader(l for l in open(f, encoding="utf-8") if not l.startswith("#")):
                for pin in (r.get("from", ""), r.get("to", "")):
                    t = tag_of(pin)
                    if t in tags: out.setdefault(name, set()).add(t)
    inv = os.path.join(LIB, "inventory.csv"); safe = set()
    if os.path.isfile(inv):
        safe = {r["id"].strip() for r in _c.DictReader(l for l in open(inv, encoding="utf-8") if not l.startswith("#")) if (r.get("safety") or "").strip().lower() == "yes"}
    for t, eid in tags.items():
        if eid in safe: out.setdefault("safety", set()).add(t)
    moving = {n.split(".")[0] for n, pv in P.pivots.items() if pv.get("kind") in ("rotate", "translate", "compress")}
    for t in tags:
        if t in moving or any(n.startswith(t + ".") and pv.get("kind") in ("rotate", "translate", "compress") for n, pv in P.pivots.items()): out.setdefault("mechanism", set()).add(t)
    in_flow = {t for name, ts in out.items() if name not in ("mechanism", "safety") for t in ts}
    out["structure"] = {t for t in tags if t not in in_flow and "." not in t}
    keys = [f"F{i}" for i in range(1, 13)]
    order = ["structure", "mechanism"] + sorted(n for n in out if n not in ("structure", "mechanism", "safety")) + (["safety"] if "safety" in out else [])
    return {name: dict(tags=sorted(out[name]), colour=LAYER_COLOUR.get(name, "#555555"), key=keys[i] if i < len(keys) else "") for i, name in enumerate(order) if out.get(name)}


def run(aid, smoke=False):
    """build the assembly, export, import into the twin project, run the twin (a window) or its smoke test; returns the exit code"""
    from . import cadout
    from .cadout import MATERIALS
    adir = os.path.join(LIB, "assemblies", aid); scene_path = os.path.join(TWIN, "scenes", aid + ".json")
    if not os.path.isfile(scene_path): print(f"{aid}: no twin scene at lib/toolkit/twin/scenes/{aid}.json"); return 2
    spec = importlib.util.spec_from_file_location("asm", os.path.join(adir, "assembly.py")); asm = importlib.util.module_from_spec(spec); spec.loader.exec_module(asm)
    P = asm.build(report=False) if "report" in asm.build.__code__.co_varnames else asm.build()
    os.makedirs(os.path.join(adir, "out"), exist_ok=True); glb = os.path.join(adir, "out", aid + ".glb"); cadout.write_glb(glb, P, aid)
    for d in ("assets", "materials", "out"): os.makedirs(os.path.join(TWIN, d), exist_ok=True)
    scene = json.load(open(scene_path, encoding="utf-8"))
    solved(aid, P, scene, os.path.join(TWIN, "out", aid + "-solved.json"))
    for name in MATERIALS: open(os.path.join(TWIN, "materials", name + ".tres"), "w", encoding="utf-8", newline="\n").write(tres(name))
    dst = os.path.join(TWIN, "assets", aid + ".glb"); shutil.copy2(glb, dst)
    mats = ",\n".join(f'"{m}": {{\n"use_external/enabled": true,\n"use_external/path": "res://materials/{m}.tres"\n}}' for m in glb_materials(dst))
    open(dst + ".import", "w", encoding="utf-8", newline="\n").write(IMPORT.format(id=aid, h=hashlib.md5(aid.encode()).hexdigest(), mats=mats))
    r = subprocess.run([GODOT, "--headless", "--path", TWIN, "--import", "--quit"], capture_output=True, text=True, timeout=900); print("import exit", r.returncode)
    cmd = [GODOT] + (["--headless"] if smoke else []) + ["--path", TWIN, "--scene", "res://twin.tscn", "--", aid] + (["--smoke"] if smoke else [])
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    lines = [l for l in r.stdout.splitlines() if l.startswith("STATE")]
    print("\n".join(lines) or (r.stdout[-1500:] + r.stderr[-1500:]))
    if smoke:
        out = os.path.join(TWIN, "out", aid + "-twin.json")
        if os.path.isfile(out): os.makedirs(os.path.join(adir, "qa"), exist_ok=True); shutil.copy2(out, os.path.join(adir, "qa", "twin.json")); print("->", os.path.relpath(os.path.join(adir, "qa", "twin.json"), LIB))
        bad = [l for l in r.stdout.splitlines() + r.stderr.splitlines() if "SCRIPT ERROR" in l or "NOT FOUND" in l]
        if bad: print("\n".join(bad[:20])); return 1
    return 0
