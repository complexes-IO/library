"""Stage 3 of lib/element-qa-checklist.txt: the Blender gate, headless only (asset-pipeline-prompt.txt section A).

    blender --background --python lib/toolkit/blender/gate.py -- <in.glb> <out dir> [--class <class>] [--step <filleted.step>] [--printed M-WHITE-PA,M-BLACK-PA] [--no-thumb]

1. Imports the glb; per mesh: non-manifold edges, inside-out faces (faces a normal recalculation would flip, and the signed volume),
   degenerate triangles, duplicate vertices beyond the shared ones. Any of the first three > 0 fails the gate.
2. Smoothing: smooth by angle 30 deg on every mesh (cylinders smooth, box edges sharp); custom normals and tangents are exported.
3. Fillets by class: operator-22 / device / connector / plate / rail / cable / station keep a Bevel modifier (0.5 mm, 2 segments, 30 deg);
   enclosure / furniture / machine bake a normal map from the filleted STEP (tessellated through Open CASCADE to STL, imported,
   selected-to-active bake at 2048) onto the low-poly glb when --step is given, else fall back to the Bevel and say so.
4. UVs: smart project (66 deg, 0.3 % margin) on every mesh; meshes of the printed materials get a second UV map 'decal' with their
   printed faces projected flat along the printed side's outward normal (toolkit/decal.py); island bounds in the report; an island
   with a side under decal.DECAL_MIN_MM fails the gate (EM 2026-11-05).
5. Materials untouched (names, count). 6. Export <out dir>/gltf/<id>.glb: metres, Y-up, node names and transforms as imported,
   custom normals, tangents, modifiers applied, no cameras or lights, extras kept. 7. Report <out dir>/gate/<id>.json and the
   thumbnail <out dir>/thumbs/<id>.png (800 px, three-quarter, Cycles CPU: Workbench / EEVEE crash headless on this host)."""
import bpy, bmesh, os, sys, json, math, time, subprocess
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))   # lib/, for toolkit.decal
from toolkit import decal as DC
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
if len(argv) < 2: raise SystemExit(__doc__)
GLB = os.path.abspath(argv[0]); OUTDIR = os.path.abspath(argv[1]); ID = os.path.splitext(os.path.basename(GLB))[0]
def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else default
CLASS = opt("--class", "device"); STEP = opt("--step"); BEVEL_ONLY = set(m for m in (opt("--bevel-only", "") or "").split(",") if m); PRINTED = set((opt("--printed", "M-WHITE-PA,M-BLACK-PA") or "").split(",")); THUMB = "--no-thumb" not in argv
BAKE_CLASSES = {"enclosure", "furniture", "machine"}
ONE_SEGMENT = {"operator-22", "operator", "device", "connector", "assembly", "run"}   # EM 2026-11-03: bevel 1 segment for operator, device, connector (assemblies are mostly devices); run (mech-1, 2026-11-06) as device
SEGMENTS = 1 if CLASS in ONE_SEGMENT else 2
for d in ("gltf", "gate", "thumbs"): os.makedirs(os.path.join(OUTDIR, d), exist_ok=True)
OUT = os.path.join(OUTDIR, "gltf", ID + ".glb"); REPORT = os.path.join(OUTDIR, "gate", ID + ".json"); PNG = os.path.join(OUTDIR, "thumbs", ID + ".png")
rep = {"id": ID, "source": GLB, "class": CLASS, "date": time.strftime("%Y-%m-%d"), "meshes": {}, "fail": []}

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB)
objs = sorted([o for o in bpy.data.objects if o.type == "MESH"], key=lambda o: o.name)
mats_in = sorted(m.name for m in bpy.data.materials); rep["materials"] = mats_in
print(f"imported {GLB}: {len(objs)} meshes, materials {mats_in}", flush=True)

# ------------------------------------------------------------------ 1. mesh checks
for o in objs:
    bm = bmesh.new(); bm.from_mesh(o.data); bm.faces.ensure_lookup_table()
    nonman = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    degenerate = sum(1 for f in bm.faces if f.calc_area() < 1e-12)
    doubles = len(bmesh.ops.find_doubles(bm, verts=bm.verts, dist=1e-7)["targetmap"])
    before = [f.normal.copy() for f in bm.faces]
    bm2 = bm.copy(); bm2.faces.ensure_lookup_table(); bmesh.ops.recalc_face_normals(bm2, faces=bm2.faces)
    flipped = sum(1 for f, n in zip(bm2.faces, before) if f.normal.dot(n) < -0.5); bm2.free()
    vol = bm.calc_volume(signed=True)
    tris = sum(len(f.verts) - 2 for f in bm.faces)
    rep["meshes"][o.name] = {"vertices": len(bm.verts), "triangles": tris, "non_manifold_edges": nonman, "inside_out_faces": flipped, "signed_volume_mm3": round(vol * 1e9, 3), "degenerate_triangles": degenerate, "duplicate_vertices": doubles,
                            "materials": [s.material.name for s in o.material_slots if s.material], "location_m": [round(v, 6) for v in o.location], "extras": {k: (list(v) if hasattr(v, "__len__") and not isinstance(v, str) else v) for k, v in o.items() if not k.startswith("_")}}
    if o.name.endswith("-colonly"): rep["meshes"][o.name]["collider"] = True
    else:
        if nonman: rep["fail"].append(f"{o.name}: {nonman} non-manifold edges")
        if flipped: rep["fail"].append(f"{o.name}: {flipped} inside-out faces")
        if degenerate: rep["fail"].append(f"{o.name}: {degenerate} degenerate triangles")
        if vol < 0: rep["fail"].append(f"{o.name}: signed volume {vol * 1e9:.1f} mm3 < 0")
    bm.free()
    print(f"  {o.name:28s} tris {tris:6d}  non-manifold {nonman:4d}  flipped {flipped:3d}  degenerate {degenerate:3d}  doubles {doubles:4d}  volume {vol * 1e9:10.1f} mm3", flush=True)

# ------------------------------------------------------------------ 2. smoothing, 3. fillets, 4. UVs
bake_used = False; bake_note = ""
def select_only(o):
    bpy.ops.object.select_all(action="DESELECT"); o.select_set(True); bpy.context.view_layer.objects.active = o
for o in objs:
    select_only(o)
    try: bpy.ops.object.shade_smooth_by_angle(angle=math.radians(30))
    except Exception:
        try: bpy.ops.object.shade_auto_smooth(angle=math.radians(30))
        except Exception as e: rep.setdefault("notes", []).append(f"{o.name}: smoothing operator missing ({e})"); bpy.ops.object.shade_smooth()
    if o.name.endswith("-colonly"): continue
    if BEVEL_ONLY:
        # EM 2026-11-03 (relay): bevel only the listed materials' faces (case, socket); blades, rivets, springs and leads stay sharp
        slots = {i for i, sl in enumerate(o.material_slots) if sl.material and sl.material.name in BEVEL_ONLY}
        if slots:
            bm = bmesh.new(); bm.from_mesh(o.data); bm.edges.ensure_lookup_table(); n_w = 0
            wl = bm.edges.layers.float.get("bevel_weight_edge") or bm.edges.layers.float.new("bevel_weight_edge")
            for e in bm.edges:
                fs = e.link_faces
                if len(fs) == 2 and all(f.material_index in slots for f in fs) and fs[0].normal.angle(fs[1].normal, 0) > math.radians(30): e[wl] = 1.0; n_w += 1
            bm.to_mesh(o.data); bm.free(); o.data.update()
            m = o.modifiers.new("Bevel", "BEVEL"); m.width = 0.0005; m.segments = SEGMENTS; m.limit_method = "WEIGHT"
            rep["meshes"][o.name]["bevel_edges"] = n_w
    elif CLASS not in BAKE_CLASSES or not STEP:
        m = o.modifiers.new("Bevel", "BEVEL"); m.width = 0.0005; m.segments = SEGMENTS; m.limit_method = "ANGLE"; m.angle_limit = math.radians(30)
    # UVs: smart project on every mesh
    bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.003); bpy.ops.object.mode_set(mode="OBJECT")
    # decal islands: a second UV map for the printed faces
    printed_slots = [i for i, s in enumerate(o.material_slots) if s.material and s.material.name in PRINTED]
    if printed_slots:
        uv = o.data.uv_layers.new(name="decal"); o.data.uv_layers.active = uv
        bm = bmesh.new(); bm.from_mesh(o.data); bm.faces.ensure_lookup_table(); lay = bm.loops.layers.uv["decal"]
        faces = [f for f in bm.faces if f.material_index in printed_slots]
        if faces:
            # EM 2026-11-05 (plc0-1.1 finding 1): along the outward normal of the face cluster that carries the print (toolkit/decal.py),
            # not the sum of every normal (zero for a closed box, which fell back to straight down and squashed the label to a strip)
            # an x-axis tie goes to the side away from the mesh's centre (ESCAPE valve-gauge-double-1.0 2; toolkit/decal.axis)
            pts = [l.vert.co for f in faces for l in f.loops]; ic = sum(pts, Vector()) / len(pts)
            xs = [v.co for v in bm.verts]; mc = Vector([(min(c[i] for c in xs) + max(c[i] for c in xs)) / 2 for i in range(3)])
            n = Vector(DC.axis([(tuple(f.normal), f.calc_area()) for f in faces], away=tuple(ic - mc)))
            u, v = (Vector(x) for x in DC.basis(tuple(n)))
            front = [f for f in faces if abs(f.normal.dot(n)) > 0.95] or faces          # the island's bounds: the printed side only
            us = [l.vert.co.dot(u) for f in front for l in f.loops]; vs = [l.vert.co.dot(v) for f in front for l in f.loops]
            u0, u1, v0, v1 = min(us), max(us), min(vs), max(vs); du = (u1 - u0) or 1e-9; dv = (v1 - v0) or 1e-9
            for f in faces:
                for l in f.loops:
                    uu, vv = l.vert.co.dot(u), l.vert.co.dot(v)
                    l[lay].uv = (min(max((uu - u0) / du, 0.0), 1.0) * 0.98 + 0.01, min(max((vv - v0) / dv, 0.0), 1.0) * 0.98 + 0.01)
            size = [round(du * 1000, 2), round(dv * 1000, 2)]; st, msg = DC.check(size)
            bm.to_mesh(o.data); rep["meshes"][o.name]["decal_island"] = {"faces": len(faces), "front_faces": len(front), "size_mm": size, "px_at_2px_per_mm": [int(du * 2000), int(dv * 2000)], "normal": [round(c, 3) for c in n], "check": st}
            if st == "FAIL": rep["fail"].append(f"{o.name}: {msg}")
        bm.free(); o.data.uv_layers.active = o.data.uv_layers[0]
    dim = [round(v * 1000, 2) for v in o.dimensions]; rep["meshes"][o.name]["dimensions_mm"] = dim
    area = sum(p.area for p in o.data.polygons); rep["meshes"][o.name]["uv_texture_px_at_2px_per_mm"] = int(math.sqrt(area * 1e6) * 2)
if CLASS in BAKE_CLASSES and STEP and os.path.exists(STEP):
    # tessellate the filleted STEP to STL through Open CASCADE (the system python has OCP; Blender's does not), import, bake normals
    stl = os.path.join(OUTDIR, "gate", ID + "-hi.stl"); py = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "step2stl.py")
    # the system python that has OCP (cadquery-ocp): LIBPY from the driver, else the Python 3.12 install, else whatever 'python' is on PATH
    cands = [os.environ.get("LIBPY", ""), os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Python", "Python312", "python.exe"), "python"]
    pyexe = next(c for c in cands if c and (os.path.exists(c) or c == "python"))
    r = subprocess.run([pyexe, py, STEP, stl], capture_output=True, text=True)
    if os.path.exists(stl):
        bpy.ops.wm.stl_import(filepath=stl, global_scale=0.001); hi = [o for o in bpy.context.selected_objects if o.type == "MESH"]
        bpy.context.scene.render.engine = "CYCLES"; bpy.context.scene.cycles.device = "CPU"; bpy.context.scene.cycles.samples = 8
        for o in objs:
            if o.name.endswith("-colonly"): continue
            img = bpy.data.images.new(f"{o.name}-normal", 2048, 2048, float_buffer=False); img.colorspace_settings.name = "Non-Color"
            for s in o.material_slots:
                if not s.material: continue
                s.material.use_nodes = True; nt = s.material.node_tree; tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; nt.nodes.active = tex
            bpy.ops.object.select_all(action="DESELECT")
            for h in hi: h.select_set(True)
            o.select_set(True); bpy.context.view_layer.objects.active = o
            try:
                bpy.ops.object.bake(type="NORMAL", use_selected_to_active=True, cage_extrusion=0.003, margin=4); p = os.path.join(OUTDIR, "gate", f"{ID}-{o.name}-normal.png"); img.filepath_raw = p; img.file_format = "PNG"; img.save(); bake_used = True
                rep["meshes"][o.name]["normal_map"] = p
            except Exception as e: bake_note = f"bake failed on {o.name}: {e}"; break
        for h in hi: bpy.data.objects.remove(h, do_unlink=True)
    else: bake_note = "STEP tessellation failed: " + r.stderr[-300:]
    if not bake_used:
        for o in objs:
            if o.name.endswith("-colonly") or o.modifiers: continue
            m = o.modifiers.new("Bevel", "BEVEL"); m.width = 0.001; m.segments = SEGMENTS; m.limit_method = "ANGLE"; m.angle_limit = math.radians(30)
        bake_note = (bake_note or "no STEP given") + "; Bevel 1.0 mm used instead"
rep["fillet"] = {"bake_used": bake_used, "note": bake_note, "bevel_mm": None if bake_used else (1.0 if CLASS in BAKE_CLASSES else 0.5), "segments": None if bake_used else SEGMENTS}
mats_out = sorted(m.name for m in bpy.data.materials)
if mats_out != mats_in: rep["fail"].append(f"materials changed: {mats_in} -> {mats_out}")

# ------------------------------------------------------------------ 6. export
# transparent materials (base colour alpha < 1, e.g. M-CASE-CLEAR 0.25) stay BLEND: the exporter reads the render method
rep["transparent"] = []
for mt in bpy.data.materials:
    a = 1.0
    if mt.use_nodes:
        for nd in mt.node_tree.nodes:
            if nd.type == "BSDF_PRINCIPLED": a = min(a, nd.inputs["Base Color"].default_value[3], nd.inputs["Alpha"].default_value)
    if a < 1.0:
        try: mt.surface_render_method = "BLENDED"
        except Exception: pass
        try: mt.blend_method = "BLEND"
        except Exception: pass
        rep["transparent"].append({"material": mt.name, "alpha": round(a, 3)})
bpy.ops.object.select_all(action="SELECT")
bpy.ops.export_scene.gltf(filepath=OUT, export_format="GLB", export_apply=True, export_normals=True, export_tangents=True, export_texcoords=True, export_yup=True,
                          export_cameras=False, export_lights=False, export_extras=True, export_materials="EXPORT", use_selection=False, export_animations=False)
rep["export"] = {"path": OUT, "bytes": os.path.getsize(OUT)}
# read-back: node names, triangles per node after the bevel
bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.gltf(filepath=OUT)
back = {o.name: len(o.data.polygons) for o in bpy.data.objects if o.type == "MESH"}; rep["export"]["triangles_per_node"] = back; rep["export"]["triangles"] = sum(back.values())
rep["export"]["nodes"] = sorted(back); rep["export"]["materials"] = sorted(m.name for m in bpy.data.materials)
import struct as _st
with open(OUT, "rb") as _f:
    _f.read(12); _jl, _jt = _st.unpack("<II", _f.read(8)); _js = json.loads(_f.read(_jl))
rep["export"]["alpha_modes"] = {m_["name"]: m_.get("alphaMode", "OPAQUE") for m_ in _js.get("materials", []) if m_.get("alphaMode")}
for t_ in rep["transparent"]:
    if rep["export"]["alpha_modes"].get(t_["material"]) != "BLEND": rep["fail"].append(f"{t_['material']} lost its transparency on export (alphaMode {rep['export']['alpha_modes'].get(t_['material'], 'OPAQUE')})")
missing = sorted(set(rep["meshes"]) - set(back)); extra = sorted(set(back) - set(rep["meshes"]))
if missing or extra: rep["fail"].append(f"node names changed on export: missing {missing}, extra {extra}")

# ------------------------------------------------------------------ 7. thumbnail (Cycles CPU)
if THUMB:
    sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 24; sc.cycles.use_denoising = False
    sc.render.resolution_x = 800; sc.render.resolution_y = 600; sc.render.film_transparent = False
    objs2 = [o for o in bpy.data.objects if o.type == "MESH" and not o.name.endswith("-colonly")]
    for o in bpy.data.objects:
        if o.name.endswith("-colonly"): o.hide_render = True
    pts = [o.matrix_world @ Vector(c) for o in objs2 for c in o.bound_box]; lo = Vector([min(p[i] for p in pts) for i in range(3)]); hi = Vector([max(p[i] for p in pts) for i in range(3)])
    ctr = (lo + hi) / 2; size = max((hi - lo).length, 1e-3)
    cam = bpy.data.cameras.new("cam"); co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co; cam.lens = 50
    co.location = ctr + Vector((0.9, -1.1, 0.7)).normalized() * size * 1.6; d = ctr - co.location; co.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; bg = w.node_tree.nodes["Background"]; bg.inputs[0].default_value = (0.93, 0.93, 0.92, 1); bg.inputs[1].default_value = 0.8
    sun = bpy.data.lights.new("sun", "SUN"); sun.energy = 3.0; so = bpy.data.objects.new("sun", sun); sc.collection.objects.link(so); so.rotation_euler = (math.radians(50), math.radians(10), math.radians(35))
    key = bpy.data.lights.new("key", "AREA"); key.energy = 40 * size * size; key.size = size; ko = bpy.data.objects.new("key", key); sc.collection.objects.link(ko); ko.location = ctr + Vector((-0.6, -0.8, 1.2)) * size; ko.rotation_euler = (ctr - ko.location).to_track_quat("-Z", "Y").to_euler()
    sc.render.filepath = PNG; bpy.ops.render.render(write_still=True); rep["thumbnail"] = PNG
rep["pass"] = not rep["fail"]
json.dump(rep, open(REPORT, "w"), indent=1)
print(f"blender gate {ID}: {'PASS' if rep['pass'] else 'FAIL ' + '; '.join(rep['fail'])}; export {rep['export']['triangles']} triangles -> {OUT}; report {REPORT}", flush=True)
