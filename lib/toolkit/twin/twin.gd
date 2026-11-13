# The operable twin of one machine (EM 2026-11-08: "test one system ... to see how this process quality"): loads
# res://assets/<id>.glb (the assembly's export, every element its own node, moving parts with the writer's motion extras),
# res://scenes/<id>.json (which of the solver's inputs the operator can work, keys, labels) and res://out/<id>-solved.json (the
# solver's table, toolkit/nets.py: for every combination of those inputs the poses, the flags, each net's potential and the probe
# points; EM 2026-11-09: behaviour emerges from the elements, nothing is scripted here). Click a part that is an input, or press
# its key; the table says what every part does. P: the meter; click two terminals and read it.
#   python lib/build.py twin <id>   (godot --path lib/toolkit/twin --scene res://twin.tscn -- <id>)   the window: orbit with the left mouse, wheel zooms,
#                                                                           right mouse pans, click an input, keys as listed
#   python lib/build.py twin <id> --smoke   (godot --headless ... -- <id> --smoke)
#                                                                           no window: works every input in turn, prints STATE
#                                                                           lines (the driven parts' values), writes out/<id>-twin.json
extends Node3D

var scene := {}
var solved := {}                    # the solver's table (res://out/<id>-solved.json)
var part: Node3D
var probe_mode := false
var probes := []                    # the two pins the meter's leads touch
var layer_on := {}                  # layer name -> bool (lib/flows.md: CAD layers; from the table's "layers")
var tag_meshes := {}                # placed element tag -> [MeshInstance3D] of its own meshes (not a nested element's)
var rest := {}                      # node name -> rest transform
var inputs := {}                    # input name -> bool
var nodes := {}                     # node name as the scene names it -> Node3D (the importer swaps '.' for '_')
var hud: Label
var cam: Camera3D
var orbit_yaw := 0.0; var orbit_pitch := 0.3; var orbit_dist := 3.0; var orbit_target := Vector3.ZERO
var momentary := []                 # inputs to release after one evaluation
var rep := {"states": []}

func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var id: String = args[0]
	scene = JSON.parse_string(FileAccess.get_file_as_string("res://scenes/%s.json" % id))
	solved = JSON.parse_string(FileAccess.get_file_as_string("res://out/%s-solved.json" % id))
	var packed: PackedScene = load("res://assets/%s.glb" % id)
	part = packed.instantiate(); add_child(part)
	for n in part.find_children("*", "Node3D", true, false):
		rest[n.name] = n.transform
		nodes[n.name] = n
	for name in solved["order"]:
		inputs[name] = false
		var nd := _node(String(solved["inputs"][name].get("node", "")))
		if nd: _make_clickable(nd, name)
	for name in solved.get("layers", {}).keys(): layer_on[name] = true
	_index_tags()
	_rig()
	var box := _bounds(part); orbit_target = box.get_center()
	orbit_dist = max(box.size.x, max(box.size.y, box.size.z)) * float(scene.get("distance", 1.6))
	var v: Array = scene.get("view", [-0.7, 0.35, 0.65]); orbit_yaw = atan2(v[0], v[2]); orbit_pitch = asin(clamp(v[1], -0.99, 0.99))
	_place_camera()
	_evaluate()
	if "--smoke" in args: await _smoke(id)

# ---------------------------------------------------------------- the solver's table
func _key() -> String:
	var k := ""
	for name in solved["order"]: k += "1" if inputs[name] else "0"
	return k

func _state() -> Dictionary:
	return solved["states"].get(_key(), {})

func _evaluate() -> void:
	for n in part.find_children("*", "Node3D", true, false): if rest.has(n.name): n.transform = rest[n.name]
	var st := _state(); var driven: Dictionary = st.get("poses", {})
	var lit := {}
	for k in driven.keys():
		_drive(k, float(driven[k])); var nd := _node(k)
		if nd: lit[nd.name] = true
	for n in part.find_children("*", "MeshInstance3D", true, false):   # every lamp not driven is dark
		var m = _motion(n)
		if m is Dictionary and String(m.get("kind", "")) == "emissive" and not lit.has(n.name): _glow(n, 0.0)
	_hud(driven)
	for name in momentary: inputs[name] = false
	momentary.clear()

# ---------------------------------------------------------------- layers (as CAD layers: a visibility per group; the solver is untouched)
func _index_tags() -> void:
	# the glb names every node "<tag>.<node>" (the importer writes '_' for '.'): a mesh belongs to the longest tag that prefixes its name
	var tags := []
	for L in solved.get("layers", {}).values(): for t in L["tags"]: if not tags.has(t): tags.append(t)
	var san := {}
	for t in tags: san[t] = t.replace(".", "_").replace(":", "_").replace("/", "_")
	for m in part.find_children("*", "MeshInstance3D", true, false):
		var best := ""
		for t in tags:
			var s_: String = san[t]
			if (m.name == s_ or m.name.begins_with(s_ + "_")) and s_.length() > best.length(): best = t
		if best != "":
			if not tag_meshes.has(best): tag_meshes[best] = []
			tag_meshes[best].append(m)

func _apply_layers() -> void:
	var show := {}
	for name in layer_on.keys():
		for t in solved["layers"][name]["tags"]: show[t] = show.get(t, false) or layer_on[name]
	for t in tag_meshes.keys():                                                  # the render layer mask, not `visible`: a hidden parent must not hide the devices mounted on it
		for m in tag_meshes[t]: m.layers = 1 if show.get(t, true) else 0

func _toggle_layer(name: String) -> void:
	layer_on[name] = not layer_on[name]; _apply_layers(); _hud({})

func _reading(a: String, b: String) -> Dictionary:
	# what a meter between two pins reads in the current state: vac (rms), vdc, and whether a side floats
	var st := _state(); var nm: Dictionary = solved["netmaps"][int(st.get("nets", 0))]; var pots: Dictionary = st.get("pots", {})
	if not nm.has(a) or not nm.has(b): return {"vac": 0.0, "vdc": 0.0, "floating": [a, b]}
	var pa = pots.get(str(int(nm[a]))); var pb = pots.get(str(int(nm[b])))
	var fl := []
	if pa == null: fl.append(a)
	if pb == null: fl.append(b)
	if fl.size() > 0: return {"vac": 0.0, "vdc": 0.0, "floating": fl}
	var dre: float = pa[0] - pb[0]; var dim: float = pa[1] - pb[1]
	return {"vac": snapped(sqrt(dre * dre + dim * dim), 0.1), "vdc": snapped(pa[2] - pb[2], 0.01), "floating": []}

func _drive(key: String, v: float) -> void:
	var nd := _node(key)
	if nd == null: push_warning("%s: no such node" % key); return
	var m = _motion(nd)
	if not (m is Dictionary): push_warning("%s: no motion extra" % key); return
	var a: Array = m.get("axis", [0, 1, 0]); var axis := Vector3(a[0], a[1], a[2]).normalized()
	match String(m.get("kind", "")):
		"rotate": nd.rotate(axis, deg_to_rad(v))
		"translate": nd.position += axis * v / 1000.0
		"compress":
			var L := _extent_along(nd, axis)
			var f: float = (L - v / 1000.0) / L if L > 0 else 1.0
			var B := Basis()
			B.x = Vector3(1, 0, 0) + axis * axis.x * (f - 1); B.y = Vector3(0, 1, 0) + axis * axis.y * (f - 1); B.z = Vector3(0, 0, 1) + axis * axis.z * (f - 1)
			nd.basis = B * nd.basis
		"emissive": _glow(nd, v)

func _motion(nd: Node):
	if nd.has_meta("extras") and nd.get_meta("extras") is Dictionary: return nd.get_meta("extras").get("motion")
	return null

func _node(key: String) -> Node3D:
	if key == "": return null
	if nodes.has(key): return nodes[key]
	var alt := key.replace(".", "_").replace(":", "_").replace("/", "_")
	if nodes.has(alt): return nodes[alt]
	return part.find_child(alt, true, false)

# ---------------------------------------------------------------- the operator
func _make_clickable(nd: Node3D, input_name: String) -> void:
	for m in nd.find_children("*", "MeshInstance3D", true, false) + ([nd] if nd is MeshInstance3D else []):
		var mi: MeshInstance3D = m
		var body := StaticBody3D.new(); var shape := CollisionShape3D.new()
		shape.shape = mi.mesh.create_trimesh_shape(); body.add_child(shape); mi.add_child(body)
		body.set_meta("input", input_name)

func _work(name: String) -> void:
	var kind := String(solved["inputs"][name].get("kind", "toggle"))
	match kind:
		"toggle": inputs[name] = not inputs[name]
		"latch": inputs[name] = true                           # a latch stays until the input that clears it is worked
		"momentary": inputs[name] = true; momentary.append(name)
	for other in solved["order"]:                              # a momentary that clears a latch (the e-stop's twist, the overload's reset)
		if String(solved["inputs"][other].get("cleared_by", "")) == name and inputs[name]: inputs[other] = false
	_evaluate()

func _probe_at(hit_pos: Vector3) -> String:
	# the probe point (a pin) nearest the click, within 15 mm
	var best := ""; var bd := 0.015
	for pin in solved["probes"].keys():
		var p: Array = solved["probes"][pin]; var d := hit_pos.distance_to(Vector3(p[0], p[1], p[2]))
		if d < bd: bd = d; best = pin
	return best

func _unhandled_input(ev: InputEvent) -> void:
	if ev is InputEventKey and ev.pressed and not ev.echo:
		if OS.get_keycode_string(ev.keycode).to_upper() == "P": probe_mode = not probe_mode; probes.clear(); _hud({}); return
		for name in solved.get("layers", {}).keys():                          # F1..F12 toggle the layers
			if String(solved["layers"][name].get("key", "")).to_upper() == OS.get_keycode_string(ev.keycode).to_upper(): _toggle_layer(name); return
		for name in solved["order"]:
			if String(solved["inputs"][name].get("key", "")).to_upper() == OS.get_keycode_string(ev.keycode).to_upper(): _work(name); return
	if ev is InputEventMouseButton and ev.pressed and ev.button_index == MOUSE_BUTTON_LEFT:
		var from := cam.project_ray_origin(ev.position); var to := from + cam.project_ray_normal(ev.position) * 100.0
		var q := PhysicsRayQueryParameters3D.create(from, to); var hit := get_world_3d().direct_space_state.intersect_ray(q)
		if probe_mode:
			var pin := _probe_at(hit["position"]) if hit else ""
			if pin != "":
				if probes.size() >= 2: probes.clear()
				probes.append(pin); _hud({}); return
		if hit and hit["collider"].has_meta("input"): _work(hit["collider"].get_meta("input")); return
	if ev is InputEventMouseButton and ev.pressed:
		if ev.button_index == MOUSE_BUTTON_WHEEL_UP: orbit_dist *= 0.9; _place_camera()
		if ev.button_index == MOUSE_BUTTON_WHEEL_DOWN: orbit_dist *= 1.1; _place_camera()
	if ev is InputEventMouseMotion:
		if ev.button_mask & MOUSE_BUTTON_MASK_LEFT: orbit_yaw -= ev.relative.x * 0.01; orbit_pitch = clamp(orbit_pitch + ev.relative.y * 0.01, -1.4, 1.4); _place_camera()
		if ev.button_mask & MOUSE_BUTTON_MASK_RIGHT:
			orbit_target += cam.global_transform.basis * Vector3(-ev.relative.x, ev.relative.y, 0) * orbit_dist * 0.001; _place_camera()

func _place_camera() -> void:
	var dir := Vector3(sin(orbit_yaw) * cos(orbit_pitch), sin(orbit_pitch), cos(orbit_yaw) * cos(orbit_pitch))
	cam.position = orbit_target + dir * orbit_dist; cam.look_at(orbit_target, Vector3.UP)

func _hud(_driven: Dictionary) -> void:
	# one short line per input, bottom-left, out of the model's way; the title is the window's
	if hud == null: return
	var lines := []
	for name in solved["order"]:
		var inp: Dictionary = solved["inputs"][name]
		lines.append("%s  %s %s" % [inp.get("key", " "), inp.get("short", name), "●" if inputs[name] else "○"])
	var st := _state(); var flags: Array = st.get("flags", [])
	for s in scene.get("show", []): lines.append("    %s %s" % [s["label"], "●" if flags.has(s["flag"]) else "○"])
	for o in st.get("over", []): lines.append("    OVER %s sees %s V, rated %s %s" % [o[0], o[1], o[2], o[3]])
	if probe_mode:
		var txt := "P  meter: click two terminals"
		if probes.size() == 1: txt = "P  meter: %s – ?" % probes[0]
		if probes.size() == 2:
			var r := _reading(probes[0], probes[1])
			txt = "P  meter %s – %s: %s VAC  %s VDC%s" % [probes[0], probes[1], r["vac"], r["vdc"], ("  (floating: %s)" % ", ".join(r["floating"])) if r["floating"].size() > 0 else ""]
		lines.append(txt)
	else: lines.append("P  meter")
	var ls := []
	for name in solved.get("layers", {}).keys(): ls.append("%s %s %s" % [solved["layers"][name].get("key", ""), name, "●" if layer_on[name] else "○"])
	if ls.size() > 0: lines.append("layers: " + "   ".join(ls))
	hud.text = "\n".join(lines)
	hud.position = Vector2(16, get_viewport().get_visible_rect().size.y - hud.get_minimum_size().y - 14)

# ---------------------------------------------------------------- headless smoke test
func _smoke(id: String) -> void:
	var seq: Array = scene.get("smoke", [])
	await _record("rest")
	for step in seq:
		for name in step.get("work", []): _work(name)
		for name in step.get("layers", []): _toggle_layer(name)        # a layer toggled in the sequence (lib/flows.md)
		await _record(step["name"])
	var f := FileAccess.open("res://out/%s-twin.json" % id, FileAccess.WRITE); f.store_string(JSON.stringify(rep, "  ")); f.close()
	get_tree().quit()

func _record(label: String) -> void:
	if DisplayServer.get_name() != "headless":
		await RenderingServer.frame_post_draw; await get_tree().process_frame; await RenderingServer.frame_post_draw
		var img := get_viewport().get_texture().get_image()
		img.save_png(ProjectSettings.globalize_path("res://out/%s-twin-%s.png" % [OS.get_cmdline_user_args()[0], label.replace(" ", "-")]))
	var state := {}
	for key in scene.get("report", []):
		var nd := _node(key)
		if nd == null: state[key] = "NOT FOUND"; continue
		var r: Transform3D = rest[nd.name]
		var dpos := (nd.position - r.origin) * 1000.0
		var m = _motion(nd); var kind := String(m.get("kind", "")) if m is Dictionary else ""
		if kind == "emissive": state[key] = _glow_level(nd)
		elif kind == "rotate": state[key] = snapped(rad_to_deg((r.basis.inverse() * nd.basis).get_euler().length()), 0.01)
		else: state[key] = snapped(dpos.length(), 0.01)
	var meter := {}
	for pair in scene.get("meter", []):
		var r := _reading(String(pair[0]), String(pair[1]))
		meter["%s-%s" % [pair[0], pair[1]]] = ("floating" if r["floating"].size() > 0 else "%s VAC %s VDC" % [r["vac"], r["vdc"]])
	var st := _state()
	var shown := 0
	for t in tag_meshes.keys(): for m in tag_meshes[t]: if m.layers != 0: shown += 1
	rep["states"].append({"name": label, "inputs": inputs.duplicate(), "nodes": state, "flags": st.get("flags", []), "meter": meter, "over": st.get("over", []), "layers": layer_on.duplicate(), "meshes_shown": shown})
	var parts := []
	for k in state.keys(): parts.append("%s=%s" % [k, state[k]])
	for k in meter.keys(): parts.append("%s: %s" % [k, meter[k]])
	print("STATE %s: %s" % [label, ", ".join(parts)])

func _rig() -> void:
	var sun := DirectionalLight3D.new(); sun.rotation_degrees = Vector3(-45, -35, 0); sun.light_energy = 1.1; add_child(sun)
	var fill := DirectionalLight3D.new(); fill.rotation_degrees = Vector3(-15, 140, 0); fill.light_energy = 0.5; add_child(fill)
	var env := WorldEnvironment.new(); var e := Environment.new(); e.background_mode = Environment.BG_COLOR; e.background_color = Color(0.96, 0.96, 0.95)
	e.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR; e.ambient_light_color = Color(0.8, 0.8, 0.8); e.ambient_light_energy = 0.6; env.environment = e; add_child(env)
	cam = Camera3D.new(); cam.name = "cam"; cam.near = 0.01; cam.far = 100.0; add_child(cam)
	var layer := CanvasLayer.new(); add_child(layer)
	hud = Label.new(); hud.add_theme_color_override("font_color", Color(0.25, 0.25, 0.25)); hud.add_theme_font_size_override("font_size", 13); layer.add_child(hud)
	DisplayServer.window_set_title(String(scene.get("title", "twin")))

# ---------------------------------------------------------------- helpers (as pose.gd)
func _extent_along(nd: Node3D, axis: Vector3) -> float:
	var lo := INF; var hi := -INF
	for m in nd.find_children("*", "MeshInstance3D", true, false) + ([nd] if nd is MeshInstance3D else []):
		var mi: MeshInstance3D = m
		for s in mi.mesh.get_surface_count():
			for v in mi.mesh.surface_get_arrays(s)[Mesh.ARRAY_VERTEX]:
				var d: float = (nd.transform.basis.inverse() * (mi.global_transform * v - nd.global_transform.origin)).dot(axis) if mi != nd else v.dot(axis)
				lo = min(lo, d); hi = max(hi, d)
	return hi - lo

func _glow(nd: Node, energy: float) -> void:
	for m in nd.find_children("*", "MeshInstance3D", true, false) + ([nd] if nd is MeshInstance3D else []):
		var mi: MeshInstance3D = m
		for s in mi.mesh.get_surface_count():
			var mat: Material = mi.mesh.surface_get_material(s)
			if mat is StandardMaterial3D:
				var sm: StandardMaterial3D = mat.duplicate(); sm.emission_enabled = energy > 0; sm.emission_energy_multiplier = energy * 4.0
				mi.set_surface_override_material(s, sm)
	nd.set_meta("glow", energy)

func _glow_level(nd: Node) -> float:
	return float(nd.get_meta("glow")) if nd.has_meta("glow") else 0.0

func _bounds(n: Node3D) -> AABB:
	var box := AABB(); var first := true
	for m in n.find_children("*", "MeshInstance3D", true, false) + ([n] if n is MeshInstance3D else []):
		var mi: MeshInstance3D = m
		if mi.name.ends_with("-colonly"): continue
		var b := mi.global_transform * mi.get_aabb()
		box = b if first else box.merge(b); first = false
	return box
