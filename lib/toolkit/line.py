"""The element line (lib/OPERATING.md section 13): eight stations every element passes, in order, at its current version.

    1 identity     Identity and sources        DOC-001..004: version, history row, baseline, the Stage 0 brief
    2 static       Static checks               holes, fastener patterns, sheet holes, shared figures, stack-ups, pins, faces, cuts
    3 mechanism    Mechanism                   moving parts at rest and through their travel, declared contacts, contacts, M12 fits
    4 performance  Performance                 the gate's fillet pre-flight (FIL-010); the build's own QA (budgets) is the precondition
    5 safety       Ratings and safety marks    the electrical rule and rating checks (ERC, ELR) wherever the element is used
    6 tools        The real tools              AutoCAD gate (at this version), Blender gate, Godot QA; in assemblies: no overlap, cables mate;
                                               every brief envelope figure on the gate's STEP extents (toolkit/figcompare.py, ISO 2768-1 m)
    7 signoff      Independent sign-off        every Assumption accepted by its class (DOC-005) and the reviewer's "<id> <version>: PASS";
                                               a safety-function element (inventory.csv safety=yes) also EM's "Safety sign-off: <version> · EM <date>"
    8 released     Released                    the tag <id>/<version>

Nothing here is recorded by hand: each station is computed from what is on file (lib/out/validation.json, the gate and QA files,
lib/reviews/, the tags), so it can't go stale. `python lib/build.py line [lane]` is the board; `python lib/build.py station <id>`
shows one element, station by station, with what holds it. Every station assumes `python lib/build.py` printed ALL PASS (the
element's check.py and its QA, budgets included) and that `validate` ran on this tree.
"""
import csv, json, os, re, subprocess

from . import library, figcompare, approvals

LIB = os.path.dirname(library.ELEMENTS)
STATIONS = [(1, "identity", "Identity and sources"), (2, "static", "Static checks"), (3, "mechanism", "Mechanism"),
            (4, "performance", "Performance"), (5, "safety", "Ratings and safety marks"), (6, "tools", "The real tools"),
            (7, "signoff", "Independent sign-off"), (8, "released", "Released")]
RULE_STATION = {"DOC-001": 1, "DOC-002": 1, "DOC-003": 1, "DOC-004": 1, "GEN-010": 1, "DOC-008": 1, "DOC-009": 1, "DOC-005": 7, "DOC-006": 5, "DOC-007": 5, "PIN-002": 2,
                "HOLE-010": 2, "HOLE-020": 2, "GDT-010": 2, "DFM-010": 2, "MATE-010": 2, "STK-010": 2, "PIN-001": 2, "PIN-010": 2,
                "PIN-020": 2, "GEO-050": 2, "GEO-060": 2, "GEO-070": 2,
                "GEO-010": 3, "GEO-030": 3, "MOT-010": 3, "MOT-020": 3, "MOT-030": 3, "CORE-010": 3, "M12-010": 3,
                "FIL-010": 4,
                "GEO-020": 6, "PIN-030": 6, "BEH-010": 5, "BEH-020": 5, "BEH-030": 5, "BEH-040": 5,
                "PNE-001": 6, "PNE-002": 6, "PNE-004": 6, "PNE-005": 6,
                "HYD-001": 6, "HYD-002": 6}         # ERC-*, ELR-*, the other PNE-* and HYD-* (request pneu-8): 5; any rule not named here: 2


def station_of(rule):
    if rule in RULE_STATION: return RULE_STATION[rule]
    if rule.startswith(("ERC-", "ELR-", "PNE-", "HYD-")): return 5
    return 2


def _findings(lib=None, elements=None):
    try: fs = json.load(open(os.path.join(lib or LIB, "out", "validation.json"), encoding="utf-8"))["findings"]
    except (OSError, ValueError, KeyError): return None
    return own_findings(fs, elements)


def own_findings(fs, elements=None):
    """request elec-11 item 2 (core watch 2026-11-12, a flow change): a lane's merge of main takes lib/out/validation.json from main
    (a generated file: conflicts take main's copy), while the element's own out/validate.json, which only the lane's build writes,
    merges clean. disc-3p-30a 1.4 was fixed and built on elec's branch and still read at station 2 from main's record of 1.3 (GEO-070
    x7), so the board counted it and elec-r32 built nothing at 3 of 3. The findings an element's own build judged (scope = the element)
    are read from its own file wherever the two disagree; findings an assembly gives it (scope = the assembly) stay the merged
    record's. On main every element's file and the merged record agree (checked 2026-11-12), so the board on main is unchanged."""
    root = elements or library.ELEMENTS
    by = {}
    for f in fs: by.setdefault(f.get("scope"), []).append(f)
    key = lambda f: (f.get("rule"), f.get("status"), f.get("where"), f.get("message"))
    swap = {}
    for eid in by:
        own = _json(os.path.join(root, str(eid), "out", "validate.json"))
        if not isinstance(own, dict) or not isinstance(own.get("findings"), list): continue
        mine = [f for f in own["findings"] if isinstance(f, dict) and f.get("scope") == eid]
        if mine and sorted(map(key, mine), key=str) != sorted(map(key, by[eid]), key=str): swap[eid] = mine
    if not swap: return fs
    return [f for f in fs if f.get("scope") not in swap] + [f for e in swap for f in swap[e]]


def _catalogue():
    return {r["id"]: r for r in csv.DictReader(open(os.path.join(LIB, "catalogue.csv"), encoding="utf-8"))}


def _tags():
    return set(subprocess.run(["git", "tag", "-l", "*/*"], capture_output=True, text=True, cwd=LIB).stdout.split())


def _reviews():
    out = []
    for d, _, fs in os.walk(os.path.join(LIB, "reviews")):
        for f in fs:
            if f.endswith(".md"): out.append(open(os.path.join(d, f), encoding="utf-8", errors="replace").read())
    return "\n".join(out)


def _safety():
    """the elements lib/inventory.csv marks safety=yes (round 10 f: machine safety and life safety)"""
    try: rows = csv.DictReader(open(os.path.join(LIB, "inventory.csv"), encoding="utf-8"))
    except OSError: return set()
    return {r["id"] for r in rows if r.get("id") and not r["id"].startswith("#") and (r.get("safety") or "").strip().lower() == "yes"}


def _spec(eid):
    try: return open(os.path.join(library.ELEMENTS, eid, "spec.md"), encoding="utf-8", errors="replace").read()
    except OSError: return ""


def safety_signed(spec, version):
    """EM's own line for a safety-function element: 'Safety sign-off: <version> · EM <date>'"""
    return bool(re.search(rf"Safety sign-off:\s*v?{re.escape(version)}\s*·\s*EM\s+\d{{4}}-\d{{2}}-\d{{2}}", spec))


def _json(path):
    try: return json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError): return None


ACAD_NO_RESULT = "AutoCAD gate: no result for the gate file on file: "


def acad_unanswered(d, name, acad, head):
    """request elec-17, ESCAPE elec-r52 (core watch 2026-11-13): acad-gate.py writes gate/<name>.lsp, whose first line gives the version
    station 6 reads, and its run log before AutoCAD runs anything, and gate/<name>-acad.json only at the end. mcb-3p 1.1's one try in
    AutoCAD's outage failed at its first COM call: the lsp said v1.1, the JSON was 1.0's pass, and station 6 read PASS at 1.1. The lsp
    belongs to the passing result only when its gate-build date is the result's date and the run's own log (round 12's, which starts
    "acad-gate "), where on file, ends that run with "gate <name>: PASS -> ". Older logs redirected by hand (no "acad-gate " line) are
    not read. True when the lsp on file is a run that wrote no result."""
    m = re.search(r"\(gate build ([\d-]+)", head or "")
    if m and acad.get("date") and m.group(1) != str(acad.get("date")): return True
    try: log = open(os.path.join(d, "gate", f"{name}-acad-run.txt"), encoding="utf-8", errors="replace").read()
    except OSError: return False
    if not log.startswith("acad-gate "): return False
    return not re.search(rf"^gate {re.escape(name)}: PASS -> ", log, re.M)


def tools_check(eid, version):
    """station 6, the element's own part: the AutoCAD gate passed at this version, the Blender gate and Godot QA passed"""
    d = os.path.join(library.ELEMENTS, eid); why = []
    acad = _json(os.path.join(d, "gate", f"{eid}-acad.json"))
    lsp = os.path.join(d, "gate", f"{eid}.lsp")
    try: head = open(lsp, encoding="utf-8", errors="replace").readline()
    except OSError: head = ""
    m = re.search(rf"{re.escape(eid)} v([\d.]+)", head); gated = m.group(1) if m else None
    if not acad: why.append("no AutoCAD gate on file")
    elif not acad.get("pass"): why.append(f"AutoCAD gate failed ({acad.get('date', '?')})")
    elif acad_unanswered(d, eid, acad, head): why.append(f"{ACAD_NO_RESULT}gate/{eid}.lsp (v{gated}) is from a run that wrote none; the pass on file is an earlier run's, not v{version}")
    elif gated != version: why.append(f"AutoCAD gate passed at v{gated}, not v{version}")
    else: why += [f"AutoCAD gate: {figcompare.say(r)}" for r in figcompare.misses(acad)]     # escape group 6 (core watch 2026-11-06)
    bl = _json(os.path.join(d, "gate", f"{eid}.json"))
    if not bl: why.append("no Blender gate on file")
    elif not bl.get("pass"): why.append("Blender gate failed")
    why += decal_holds(eid)                                                     # escape group 18 (core watch 2026-11-06)
    qa = _json(os.path.join(d, "qa", f"{eid}.json"))
    if not qa: why.append("no Godot QA on file")
    elif not qa.get("pass"): why.append("Godot QA failed")
    else: why += qa_source_miss(qa, bl, f"qa/{eid}.json") + qa_read_miss(qa, eid, eid, f"qa/{eid}.json")   # ESCAPE mech/r140 1; round 37
    # every variant gated on file is the element too (EM, 2026-11-05: a failed D or L gate held nothing): its AutoCAD gate passed at
    # this version, and its Blender gate and Godot QA, where on file, passed
    for v in variants(eid):
        n = f"{eid}-{v}"; a = _json(os.path.join(d, "gate", f"{n}-acad.json")) or {}
        try: h = open(os.path.join(d, "gate", f"{n}.lsp"), encoding="utf-8", errors="replace").readline()
        except OSError: h = ""
        m = re.search(rf"{re.escape(eid)} v([\d.]+)", h); gv = m.group(1) if m else None
        if not a.get("pass"): why.append(f"variant {v}: AutoCAD gate failed ({a.get('date', '?')})")
        elif acad_unanswered(d, n, a, h): why.append(f"variant {v}: {ACAD_NO_RESULT}gate/{n}.lsp (v{gv}) is from a run that wrote none; the pass on file is an earlier run's, not v{version}")
        elif gv != version: why.append(f"variant {v}: AutoCAD gate passed at v{gv}, not v{version}")
        else: why += [f"variant {v}: AutoCAD gate: {figcompare.say(r)}" for r in figcompare.misses(a)]
        for f, tool in ((os.path.join(d, "gate", f"{n}.json"), "Blender gate"), (os.path.join(d, "qa", f"{n}.json"), "Godot QA")):
            r = _json(f)
            if r is not None and not r.get("pass"): why.append(f"variant {v}: {tool} failed")
        q, b = _json(os.path.join(d, "qa", f"{n}.json")), _json(os.path.join(d, "gate", f"{n}.json"))
        if q and q.get("pass"): why += [f"variant {v}: {w}" for w in qa_source_miss(q, b, f"qa/{n}.json") + qa_read_miss(q, eid, n, f"qa/{n}.json")]
    why += result_holds(eid)                                                    # escape group 17 (core watch 2026-11-07)
    return why


QA_SOURCE = "Godot QA did not read the Blender gate's export"


def qa_source_miss(qa, bl, name):
    """station 6 (ESCAPE mech/r140 1, core watch 2026-11-13): Godot QA counts what it rendered, and lib/godot-qa.py fell back without a
    word to the writer's out/<id>.glb when gltf/<id>.glb was not there yet, so profile-t-alu-30x30x3's first QA passed on 28 triangles
    (no bevel) while the file shipped, the Blender gate's export, has 220 in its body; station 6 read only "pass". The QA's rendered
    triangles must equal the export's visible ones (the Blender result's export.triangles_per_node, collider nodes "-colonly" left
    out): a QA of another file, or of an older export, holds the element. A Blender result with no per-node count holds nothing here.
    Probed on main before the push: 273 elements and 5 variants agree; nut-m12, plug-m12 (its QA = the writer's 2288) and port-m12-a
    differ, each already held at station 6 by a gate at an older version."""
    tpn = ((bl or {}).get("export") or {}).get("triangles_per_node")
    if not isinstance(tpn, dict) or not tpn or not isinstance(qa, dict) or not isinstance(qa.get("triangles"), int): return []
    vis = sum(v for k, v in tpn.items() if "colonly" not in k and isinstance(v, (int, float)))
    if qa["triangles"] == vis: return []
    gen = qa.get("triangles_generator")
    said = " (the writer's out/ glb)" if gen == qa["triangles"] else ""
    return [f"{QA_SOURCE}: {name} rendered {qa['triangles']} triangles{said}, the export's visible nodes have {vis}; rerun the QA on gltf/"]


QA_READ = "Godot QA read another file than the Blender gate's export"


def qa_read_miss(qa, eid, name, rel):
    """station 6 (core round 37, the core's half of round 36 A1; ESCAPE mech/r140 1): from round 36 lib/godot-qa.py writes into each
    qa/<name>.json the file it read ("source", relative to lib/, with "/"). An element's QA must have read its Blender export,
    elements/<id>/gltf/<id>.glb; a variant's, its gltf/<variant>.glb or, as godot-qa.py allows, the AutoCAD gate's gate/<variant>.glb.
    A QA that read anything else (the writer's out/ glb, another element's file) holds the element. A QA written before round 36
    carries no "source" and holds nothing here (qa_source_miss still compares its triangles). The sha256 is not compared: gltf/ is
    git-ignored and each worktree's copy is its own, so a file on this checkout is not the one the QA read."""
    src = (qa or {}).get("source") if isinstance(qa, dict) else None
    if not isinstance(src, str) or not src: return []
    want = [f"elements/{eid}/gltf/{name}.glb"] + ([f"elements/{eid}/gate/{name}.glb"] if name != eid else [])
    if src.replace("\\", "/") in want: return []
    return [f"{QA_READ}: {rel} read {src}, not {want[0]}; rerun the QA after the Blender gate"]


def result_holds(eid):
    """station 6 (escape group 17, core watch 2026-11-07; reviewer relay-ice-cube-1.1:2): every other verdict of the element on file.
    The pose check (lib/pose-check.py: gate/<id>-poses.json; Godot's qa/<id>-*-poses.json) and the results of a variant that has no
    AutoCAD gate of its own (relay-ice-cube-2co's cutaway: gate/<id>-cutaway.json, qa/<id>-cutaway.json) were read by nothing, so
    relay-ice-cube-2co passed station 6 with its own pose check reading "pass": false (3 of 22 checks, at 1.0 and again at 1.1). A result
    that says it failed holds the element; one that carries no verdict (no "pass" key) holds nothing."""
    d = os.path.join(library.ELEMENTS, eid); done = set(variants(eid)); out = []
    for sub in ("gate", "qa"):
        try: fs = sorted(os.listdir(os.path.join(d, sub)))
        except OSError: continue
        for f in fs:
            if not f.endswith(".json") or f.endswith("-acad.json") or not f.startswith(eid + "-"): continue
            stem = f[len(eid) + 1:-len(".json")]
            if not stem.endswith("poses") and stem in done: continue           # a gated variant: tools_check read it above
            r = _json(os.path.join(d, sub, f))
            if not isinstance(r, dict) or r.get("pass") is not False: continue
            if stem.endswith("poses"):
                cs = r.get("checks") or []; bad = [c.get("check", "?") for c in cs if isinstance(c, dict) and not c.get("ok")]
                out.append(f"pose check failed on file: {sub}/{f} ({len(cs) - len(bad)} of {len(cs)} agree; first: {bad[0][:60] if bad else '?'})")
            else:
                out.append(f"{'Blender gate' if sub == 'gate' else 'Godot QA'} failed on file: {sub}/{f}")
    return out


DECAL_STALE = "Blender gate before the decal check"


def decal_stale(bl):
    """the meshes of a Blender result whose decal island carries no 'check': written by the gate before toolkit/decal.py (EM 2026-11-05,
    plc0-1.1 finding 1), which projected a printed box from above and passed (reviewer marker-terminal-1.0:1, tool-dmm-1.0:1,
    teach-pendant-1.0:1, thermostat-enc-1.0:1: a 2.0 mm island for the only print the element carries). Such a pass never ran the check."""
    ms = (bl or {}).get("meshes") or {}
    return sorted(k for k, v in ms.items() if isinstance(v, dict) and isinstance(v.get("decal_island"), dict) and "check" not in v["decal_island"])


def decal_holds(eid):
    """station 6 (escape group 18, core watch 2026-11-06): every Blender result of the element on file (its own, its variants', a
    cutaway's: gate/<id>*.json but the AutoCAD and pose results) whose decal islands were never checked. The decal fix was a toolkit
    change, so the re-gate is the core's (lib/roles/core.md: a toolkit change is the core's to re-gate in its own round)"""
    try: fs = sorted(os.listdir(os.path.join(library.ELEMENTS, eid, "gate")))
    except OSError: return []
    out = []
    for f in fs:
        if not (f.startswith(eid) and f.endswith(".json")) or f.endswith(("-acad.json", "-poses.json")): continue
        if f != f"{eid}.json" and not f.startswith(eid + "-"): continue
        st = decal_stale(_json(os.path.join(library.ELEMENTS, eid, "gate", f)))
        if st: out.append(f"{DECAL_STALE} (toolkit/decal.py): gate/{f} decal islands {', '.join(st[:4])}{' ...' if len(st) > 4 else ''} "
                          f"carry no check; the core re-gates it in Blender")
    return out


def variants(eid):
    """the variants gated on file: gate/<id>-<variant>-acad.json"""
    try: fs = os.listdir(os.path.join(library.ELEMENTS, eid, "gate"))
    except OSError: return []
    return sorted(f[len(eid) + 1:-len("-acad.json")] for f in fs
                  if f.startswith(eid + "-") and f.endswith("-acad.json") and f != f"{eid}-acad.json")


FP_SKIP = ("out", "gate", "thumbs", "qa")
STALE_REVIEW = "reviewed on other files: "
FP_RECORDED = re.compile(r"source\s+fingerprint\b.{0,80}?sha256\s+([0-9a-f]{16})", re.S | re.I)


def source_fingerprint(eid, elements=None):
    """the element's source fingerprint, the reviewer's method (cabinet-tool-1.1.md, 2026-11-08; OPERATING.md 13, round 11): every
    tracked file under lib/elements/<id>/ but out/, gate/, thumbs/ and qa/, sorted by its repo path, each fed to one sha256 as that path,
    a NUL byte, then its content with CRLF made LF; the first 16 hex. Read from the working tree, so the PC and a Linux clone agree.
    Outside a git work tree (a planted case) every file under the folder counts. None when the folder doesn't exist."""
    import hashlib
    d = os.path.join(elements or library.ELEMENTS, eid)
    if not os.path.isdir(d): return None
    r = subprocess.run(["git", "ls-files", "--full-name", "-z", "--", "."], capture_output=True, cwd=d)
    if r.returncode == 0 and elements is None:
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=d).stdout.strip()
        names = [(p, os.path.join(top, p)) for p in r.stdout.decode("utf-8").split("\0") if p]
    else:
        names = []
        for w, _, fs in os.walk(d):
            for f in fs:
                rel = os.path.relpath(os.path.join(w, f), d).replace(os.sep, "/")
                names.append((f"lib/elements/{eid}/{rel}", os.path.join(w, f)))
    h = hashlib.sha256(); pre = f"lib/elements/{eid}/"
    for p, full in sorted(names):
        if p[len(pre):].split("/")[0] in FP_SKIP: continue
        try: c = open(full, "rb").read()
        except OSError: continue
        h.update(p.encode("utf-8") + b"\0" + c.replace(b"\r\n", b"\n"))
    return h.hexdigest()[:16]


FP_ANY = re.compile(r"sha256\s+([0-9a-f]{16})\b", re.I)


def review_at_files(eid, ver, cur, root=None):
    """(file, verdict) of a review at <id> <version> that is not a PASS and records the files' fingerprint now, cur, in any wording
    ("Source fingerprint: sha256 <16 hex>", or "Files now: sha256 <16 hex>" as gland-m20-1.3-reread2.md wrote it); None when there is
    none. Round 25's return 4.2 (core watch 2026-11-10): gland-m20 1.3's re-read found FINDINGS at its current files, and rereview still
    read the older PASS, recorded on other files, as the verdict: the newest reading of the files is the one that stands."""
    d = os.path.join(root or os.path.join(LIB, "reviews"), "elements")
    try: names = sorted(os.listdir(d))
    except OSError: return None
    for f in names:
        if not (f.startswith(f"{eid}-{ver}") and f.endswith(".md")): continue
        rest = f[len(f"{eid}-{ver}"):-3]
        if rest and not rest.startswith("-"): continue
        txt = open(os.path.join(d, f), encoding="utf-8", errors="replace").read()
        m = VERDICT.search(txt)
        if not (m and m.group("id") == eid and m.group("ver") == ver) or m.group("verdict") == "PASS": continue
        if cur and cur.lower() in {x.lower() for x in FP_ANY.findall(txt)}: return f, m.group("verdict")
    return None


def review_stale(eid, ver, root=None, elements=None):
    """station 7, escape group 13's sign-off half (core watch 2026-11-09; reviewer mech-r67 finding 1, gl-xr-1-1.2:1): a reviewer's PASS
    counts only for the files it read. duct-40x60 1.2 took a behaviour.csv after its review, at the same version, and station 7 still
    passed on a review of other files (fingerprint f1adca2a42a0a2f9 reviewed, b306824a6a813e12 on main); the behaviour backlog does the
    same to every released element. Each element review at this version whose verdict is PASS (its -reread.md too) records "Source
    fingerprint ... sha256 <16 hex>"; when every one of them records one and none is the files' fingerprint now, the PASS was for other
    files: held, waiting on the reviewer's re-read (rereview_due; out of the lane's count). A PASS file with no fingerprint (written
    before the reviewer recorded them) still counts as it did."""
    d = os.path.join(root or os.path.join(LIB, "reviews"), "elements"); fps = []
    try: names = sorted(os.listdir(d))
    except OSError: return []
    for f in names:
        if not (f.startswith(f"{eid}-{ver}") and f.endswith(".md")): continue
        rest = f[len(f"{eid}-{ver}"):-3]
        if rest and not rest.startswith("-"): continue
        txt = open(os.path.join(d, f), encoding="utf-8", errors="replace").read()
        m = VERDICT.search(txt)
        if not (m and m.group("id") == eid and m.group("ver") == ver and m.group("verdict") == "PASS"): continue
        fp = FP_RECORDED.search(txt)
        if not fp: return []                                                # a PASS on file before fingerprints: counts as before
        fps.append(fp.group(1).lower())
    if not fps: return []
    cur = source_fingerprint(eid, elements)
    if cur is None or cur in fps: return []
    later = review_at_files(eid, ver, cur, root)
    if later:                                                           # round 25's return 4.2: the re-read already read these files
        f, v = later
        return [f"{NO_REVIEWER_LINE}\"{eid} {ver}: PASS\" at the files now ({cur}): {f} read them and says {v}; the PASS before it read "
                f"fingerprint {fps[-1]}: the lane's fix, then the reviewer's re-read"]
    return [f"{STALE_REVIEW}\"{eid} {ver}: PASS\" read fingerprint {fps[-1]}, the files are now {cur} (a file changed at the same "
            f"version): the reviewer's re-read, build.py rereview; `build.py fingerprint {eid}`"]


def element(eid, findings=None, cat=None, tags=None, reviews=None, safety=None, spec=None, reviews_root=None):
    """[(station number, name, title, passed, [what holds it])] for one element at its current version. A station passes only when
    every station before it passed."""
    findings = _findings() if findings is None else findings
    cat = _catalogue() if cat is None else cat
    tags = _tags() if tags is None else tags
    reviews = _reviews() if reviews is None else reviews
    safety = _safety() if safety is None else safety
    if eid not in cat: return []
    ver = cat[eid]["version"]
    hold = {n: [] for n, _, _ in STATIONS}
    if findings is None: hold[1].append("no lib/out/validation.json: run python lib/build.py validate")
    for f in findings or []:
        if f["status"] == "PASS": continue
        if f["scope"] == eid or eid in (f.get("elements") or []):
            hold[station_of(f["rule"])].append(f"{f['rule']} {f['status']}: {f['message'][:110]}")
    hold[6] += tools_check(eid, ver)
    if not re.search(rf"^[\s\-*`]*{re.escape(eid)}`?\s+v?{re.escape(ver)}\s*:\s*PASS", reviews, re.M):
        hold[7].append(f"no reviewer line \"{eid} {ver}: PASS\" in lib/reviews/")
    else: hold[7] += review_stale(eid, ver, reviews_root)                     # escape group 13, station 7 (core watch 2026-11-09)
    # (a stale PASS is not "no reviewer line": waits_on_reviewer and rereview_due read it as the reviewer's re-read owed)
    if eid in safety and not safety_signed(_spec(eid) if spec is None else spec, ver) and not approvals.safety_signed(eid, ver):
        hold[7].append(f"a safety-function element (inventory.csv safety=yes): no \"Safety sign-off: {ver} · EM <date>\" in spec.md or lib/approvals.csv")
    if f"{eid}/{ver}" not in tags: hold[8].append(f"no tag {eid}/{ver}")
    out, ok = [], True
    for n, name, title in STATIONS:
        ok = ok and not hold[n]; out.append((n, name, title, ok, hold[n]))
    return out


def in_progress(r):
    """EM 2026-11-05, finish before start (OPERATING.md 13): an element counts in its lane's work in progress until it has passed station 7;
    one at station 6 waiting for its sign-off counts"""
    return r < 7


EM_HOLD = re.compile(r"^DOC-005 REVIEW(?!: \d+ refused by EM)(?!: source wanted)|^DOC-004 REVIEW: no Stage 0 brief|no \"Safety sign-off: ")
SOURCE_HOLD = "DOC-005 REVIEW: source wanted"                                    # EM 2026-11-09: a class B figure waits for its document, not for EM


def waits_on_em(nxt):
    """OPERATING.md 13 and the lanes' cards: the work-in-progress limit counts a lane's elements 'not counting those that wait on EM'
    (request mech-3, core watch 2026-11-06: the board counted all 15 of mech's, 5 of them waiting on EM's figures and 2 on a Stage 0
    brief, and mech built nothing for four rounds). An element waits on EM when a hold at the first station it hasn't passed is one only
    EM can clear: DOC-005 REVIEW (it is REVIEW only while open figures need more of EM's lines than he has written; the hold's text is
    cut at 110 characters, so the status is read, not the counts), a Stage 0 brief (a vendor file is read attended), or a
    safety-function element's sign-off. A reviewer's line or a finding the lane can fix is not EM's: those still count."""
    if not nxt: return False                                                    # nxt: the board's (n, name, title, ok, holds) it is held at
    for h in nxt[4]:
        if EM_HOLD.search(h): return True
    return False


def waits_on_source(nxt):
    """EM 2026-11-09 ("not stopping for data that is derived from known formulas or based in standards"): held at station 7 only by
    class B figures whose standard is not on file (DOC-005 "source wanted"). The document is asked for once (lib/standards/wanted.md);
    neither EM's line per figure nor the lane's work clears it, so it leaves the WIP count and is not EM's."""
    return bool(nxt and nxt[0] == 7 and nxt[4]) and all(h.startswith(SOURCE_HOLD) or h.startswith(NO_REVIEWER_LINE) for h in nxt[4]) and any(h.startswith(SOURCE_HOLD) for h in nxt[4])


def waits_on_core(nxt):
    """held only by the core's re-gate (escape group 18): every hold at the station it is held at is a Blender result from before the
    decal check. The lane can't clear it, so it doesn't count in the lane's limit; one hold of the lane's own beside it, and it counts"""
    return bool(nxt and nxt[4]) and all(h.startswith(DECAL_STALE) for h in nxt[4])


def waits_on_reviewer(nxt, root=None, elements=None):
    """held at station 7 only by the reviewer's line, with nothing for the lane to do (EM 2026-11-07: "we need more elements, this
    should be our #1 priority"; mech idled four rounds with 8 elements counted, every one waiting on the reviewer): the reviewer has
    not reviewed this version, or reviewed it before EM's approvals and owes it the re-read (reviewer.md 4c). After a re-read that
    still finds something, the element is the lane's again and counts. A PASS read on other files (review_stale, escape group 13)
    waits on the reviewer's re-read the same way."""
    if nxt and nxt[0] == 7 and nxt[4] and all(h.startswith(STALE_REVIEW) for h in nxt[4]): return True
    if not nxt or nxt[0] != 7 or not nxt[4] or not all(h.startswith(NO_REVIEWER_LINE) for h in nxt[4]): return False
    m = re.search(r'"([a-z0-9][a-z0-9.\-]*) v?(\d+\.\d+): PASS"', nxt[4][0])
    if not m: return False
    eid, ver = m.groups(); v = review_verdict(eid, ver, root, elements)
    if v is None: return True
    d = os.path.join(root or os.path.join(LIB, "reviews"), "elements")
    return v == "FINDINGS" and not os.path.exists(os.path.join(d, f"{eid}-{ver}-reread.md"))


FINDING_HEAD = re.compile(r"^##\s+(?:Findings?|Still open)\b(.*)$", re.M)
WAITS_HEAD = re.compile(r"waits on (the core|EM)\b", re.I)


def _review_order(rest):
    """the order of an element's review files at one version: the review (''), -reread, -reread2, -reread3 ..."""
    if not rest: return 0
    m = re.fullmatch(r"-reread(\d*)", rest)
    return (int(m.group(1)) if m.group(1) else 1) if m else 0.5


def waits_on_review_owner(nxt, root=None):
    """request pneu-7 item 3 (core watch 2026-11-10; flow, OPERATING.md 8.d and 13: what waits on the core or EM is not counted): held at
    station 7 only by the reviewer's line, and the newest review of this version (the last re-read) says FINDINGS with every one of
    its findings headings marked as waiting on the core or EM ("## Still open (waits on the core, and through it on EM)", gauge-p
    1.0's re-read2: its class features wait on EM's ETIM download, pneu-5). The lane has nothing to do on it, yet it filled one of
    pneu's three places. Returns 'core' or 'EM' (the heading's first owner), or None. A heading with no such mark, or one finding of
    the lane's beside them, and the element counts as before."""
    if not nxt or nxt[0] != 7 or not nxt[4] or not all(h.startswith(NO_REVIEWER_LINE) for h in nxt[4]): return None
    m = re.search(r'"([a-z0-9][a-z0-9.\-]*) v?(\d+\.\d+): PASS"', nxt[4][0])
    if not m: return None
    eid, ver = m.groups(); d = os.path.join(root or os.path.join(LIB, "reviews"), "elements"); got = []
    try: names = os.listdir(d)
    except OSError: return None
    for f in names:
        if not (f.startswith(f"{eid}-{ver}") and f.endswith(".md")): continue
        rest = f[len(f"{eid}-{ver}"):-3]
        if rest and not rest.startswith("-"): continue
        got.append((_review_order(rest), f))
    if not got: return None
    txt = open(os.path.join(d, max(got)[1]), encoding="utf-8", errors="replace").read()
    v = VERDICT.search(txt)
    if not (v and v.group("id") == eid and v.group("ver") == ver and v.group("verdict") == "FINDINGS"): return None
    heads = FINDING_HEAD.findall(txt)
    owners_ = [WAITS_HEAD.search(h) for h in heads]
    if not heads or not all(owners_): return None
    return "core" if owners_[0].group(1).lower() == "the core" else "EM"


HISTORY = os.path.join(LIB, "line-history.csv")
_HIST = {}


def history_best(path=None):
    """the highest station each (element, version) has reached in lib/line-history.csv (core watch writes a row per element every run)"""
    p = path or HISTORY
    if p not in _HIST:
        best = {}
        try:
            with open(p, encoding="utf-8", newline="") as f:
                for row in csv.DictReader(f):
                    try: k = (row["element"], row["version"]); best[k] = max(best.get(k, 0), int(row["reached"]))
                    except (KeyError, ValueError, TypeError): continue
        except OSError: pass
        _HIST[p] = best
    return _HIST[p]


def taken_back(eid, ver, r, hist=None):
    """the backlog (core watch 2026-11-08, improvement run; flow, OPERATING.md 8.d): the element stands below a station it had already
    passed at this same version, so nothing the lane wrote moved it back: a rule or a tool added since did (GEO-070, MOT-030, DOC-006 on
    a host's notes ...). elec counted 13 in progress against a limit of 3, 11 of them taken back this way at versions it had brought
    to station 5 or 6, and at one finding (or three text fixes) a round it would start no new element for more than a shift. The lane
    still fixes them first (autopilot.md 2a); they no longer stop the round's new element. A new version has no history, so the lane's
    own unfinished work always counts."""
    if not eid or not ver: return False
    best = history_best() if hist is None else hist
    return best.get((eid, ver), 0) > r


UNGATED = ("no AutoCAD gate on file", "no Blender gate on file", "no Godot QA on file")
# request elec-16 (core watch 2026-11-13; flow, OPERATING.md 8.d): an AutoCAD pass at an older version, or a gate file whose run wrote no
# result, with nothing else held at station 6 (the Blender gate and Godot QA passed, stations 1 to 5 pass), waits for one AutoCAD run as a
# missing gate does. AutoCAD answered no gate from 03:42 on 11-13, and elec's three text minors and two fixed holds, each held only so,
# counted 5 of 3: r51 and r52 built nothing. A failed AutoCAD gate still counts (the lane's fix)
ACAD_OLD = re.compile(r"^(?:variant [^:]+: )?(?:AutoCAD gate passed at v[\d.]+, not v[\d.]+$|" + re.escape(ACAD_NO_RESULT) + ")")


def waits_on_gates(nxt):
    """held at station 6 only by gates not yet run (core watch 2026-11-09, 2.d; flow, OPERATING.md 8.d): every hold there is a
    missing AutoCAD, Blender or Godot result, nothing failed and nothing to redesign. elec idled r17 and r18 with 6 to 9 of the cloud
    builder's generic elements counted, each waiting only for its first gates. Gate runs are the lane's queue at station 6, worked
    first each round (autopilot.md 2a, up to three elements), not designs in progress: they don't stop the round's new element. A
    failed gate is the lane's fix and still counts; an out-of-date AutoCAD pass is a run owed, as a missing one (request elec-16, ACAD_OLD)"""
    return bool(nxt and nxt[0] == 6 and nxt[4]) and all(h in UNGATED or ACAD_OLD.match(h) for h in nxt[4])


BRIEF_MISS = "AutoCAD gate: brief figure "
PORT_HOLD = "BEH-020 REVIEW"
DOC_PAGE = re.compile(r"\b(?:p|pp|page)\.?\s*\d+|\b(?:Figure|Fig\.|Table|Appendix)\s*[A-Z\d]", re.I)
DATA_ON_FILE = re.compile(r"measure[\w\-]*\.json|\bSTEP\b|read-back|\bOCC\b", re.I)
_LANES = {}


def brief_ports(eid, elements=None):
    """the text of the '## Ports' section of the element's Stage 0 brief (references/measure.md), or '' when there is none"""
    try: txt = open(os.path.join(elements or library.ELEMENTS, eid, "references", "measure.md"), encoding="utf-8", errors="replace").read()
    except OSError: return ""
    m = re.search(r"^##\s+Ports\s*$(.*?)(?=^##\s|\Z)", txt, re.M | re.S)
    return m.group(1).strip() if m else ""


def waits_on_reading(nxt, eid, elements=None, needs=None, lanes=None):
    """request elec-7 (core watch 2026-11-09; flow, OPERATING.md 8.d and 12: what waits on EM or a source never stops a lane building):
    held at station 6 only by the AutoCAD gate's brief-figure misses, each missed row's source a page of a vendor document (the brief's
    measure.md: "manual p. 11"), none a figure read from data on file (a measure JSON, the STEP read-back), and the element named in
    its lane's lib/needs-em/<lane>.md, so EM has the question. Opening a vendor file is attended only (autopilot.md 3): whether the
    build or the reading is wrong can't be settled unattended, as DOC-004's missing brief can't. relay-safety-2ch-2no1nc 1.2 (depth 113.6 read
    against 114.6) took elec to 4 against its limit of 3 and a second idle round. Still held at station 6: only the count changes.
    request elec-8 (core watch 2026-11-09, the same flow rule): held at station 5 only by BEH-020 (pins with no port node), when the
    brief's Ports section gives the marks from a vendor document's page and from no data on file, and the element is named in its
    lane's needs-em file: which mark sits at which position is that document's to say (relay-safety-2ch-2no1nc: manual p. 14 Figure 6, an image),
    read attended; placing the nodes before it is a guess (OPERATING.md 6). relay-safety-2ch-2no1nc 1.2 held elec at 3 of 3 for r23"""
    if not eid or not nxt or not nxt[4]: return False
    if nxt[0] == 6 and all(h.startswith(BRIEF_MISS) for h in nxt[4]):
        rep = _json(os.path.join(elements or library.ELEMENTS, eid, "gate", f"{eid}-acad.json"))
        ms = figcompare.misses(rep)
        if not ms or not all(DOC_PAGE.search(m.get("source", "")) and not DATA_ON_FILE.search(m.get("source", "")) for m in ms): return False
    elif nxt[0] == 5 and all(h.startswith(PORT_HOLD) for h in nxt[4]):
        # request elec-8 (core watch 2026-11-09): BEH-020 only, and the brief's Ports section places the marks from a vendor page alone
        # (relay-safety-2ch-2no1nc: "manual p. 14 Table 2"; their positions on Figure 6, an image): a port node put on a position no file gives is a guess
        ports = brief_ports(eid, elements)
        if not ports or not DOC_PAGE.search(ports) or DATA_ON_FILE.search(ports): return False
    else: return False
    if lanes is None:
        if "o" not in _LANES: _LANES["o"] = owners()
        lanes = _LANES["o"]
    ln = lanes.get(eid)
    if not ln: return False
    try: txt = open(os.path.join(needs or os.path.join(LIB, "needs-em"), f"{ln}.md"), encoding="utf-8").read()
    except OSError: return False
    # elec idle r31 (core watch 2026-11-12): a rename keeps the lane's needs-em file as written (history), so the question EM has
    # names the element by its old id: sr-440r's lines held relay-safety-2ch-2no1nc in elec's count after its rename (elec-r31
    # built nothing at 4 of 3). The element is named by its id or any alias in its metadata.json
    meta = _json(os.path.join(elements or library.ELEMENTS, eid, "metadata.json"))
    names = [eid] + [a for a in ((meta.get("aliases") if isinstance(meta, dict) else None) or []) if isinstance(a, str) and a]
    return any(re.search(rf"(?<![\w\-]){re.escape(n)}(?![\w\-])", txt) for n in names)


def wip(r, nxt, root=None, eid=None, ver=None, hist=None):
    """counts in its lane's work-in-progress limit (OPERATING.md 13): not yet past station 7 (r, the last station passed), and not
    waiting on EM (his lines, or a vendor file's reading: waits_on_reading), on the core's re-gate, or on the reviewer, at the station it
    is held at (nxt, as the board gives it), and not taken back by a later rule or tool (taken_back: needs the element's id and version)"""
    return (in_progress(r) and not waits_on_em(nxt) and not waits_on_reading(nxt, eid) and not waits_on_core(nxt) and not waits_on_source(nxt)
            and not waits_on_reviewer(nxt, root) and not waits_on_review_owner(nxt, root) and not waits_on_gates(nxt) and not taken_back(eid, ver, r, hist))


def count_mark(r, nxt, root=None, eid=None, ver=None, hist=None):
    """what the board prints beside each element (request elec-5, core watch 2026-11-07: the lane read three elements held by EM's
    DOC-005 lines beside the reviewer's line as counted, though wip() already left them out; the board gave only the totals): 'WIP'
    counted in the lane's limit, 'EM', 'core' or 'rev' (the reviewer) waiting and not counted, '' past station 7. 'WIP' exactly when
    wip() counts it (core watch 2026-11-07, improvement run: after waits_on_reviewer the board marked mech's 6 reviewer-held elements
    'WIP' under a header that counted 0, and a lane that reads the marks idles at its limit)"""
    if not in_progress(r): return ""
    if waits_on_em(nxt) or waits_on_reading(nxt, eid): return "EM"      # request elec-7: a vendor document's reading, attended
    if waits_on_source(nxt): return "src"                                 # EM 2026-11-09: a standard's document wanted (lib/standards/wanted.md)
    if waits_on_core(nxt): return "core"
    if waits_on_reviewer(nxt, root): return "rev"
    o = waits_on_review_owner(nxt, root)
    if o: return o                                                      # request pneu-7 item 3: the review's open findings are the core's or EM's
    if waits_on_gates(nxt): return "gate"                               # first gates not yet run: the lane's gate queue, not counted
    return "back" if taken_back(eid, ver, r, hist) else "WIP"           # the backlog: the lane's to fix first, not counted


NO_REVIEWER_LINE = "no reviewer line "
VERDICT = re.compile(r"^[\s\-*`#]*(?P<id>[a-z0-9][a-z0-9.\-]*)`?\s+v?(?P<ver>\d+\.\d+)\s*:\s*(?P<verdict>PASS|FINDINGS|REVIEWED, EM to sign)", re.M)


def review_verdict(eid, ver, root=None, elements=None):
    """the reviewer's verdict on file for <id> <version> (lib/reviews/elements/<id>-<version>*.md, first verdict line in each): 'PASS',
    'FINDINGS', 'REVIEWED, EM to sign', or None when there is no element review at this version. PASS wins over the others, except a
    PASS read on other files (review_stale) when a later review records the files now and says otherwise (round 25's return 4.2)."""
    if root is None or elements is not None:
        st = review_stale(eid, ver, root, elements)
        if st and st[0].startswith(NO_REVIEWER_LINE):
            m = re.search(r"read them and says (FINDINGS|REVIEWED, EM to sign);", st[0])
            if m: return m.group(1)
    d = os.path.join(root or os.path.join(LIB, "reviews"), "elements"); got = set()
    try: names = os.listdir(d)
    except OSError: return None
    for f in names:
        if not (f.startswith(f"{eid}-{ver}") and f.endswith(".md")): continue
        rest = f[len(f"{eid}-{ver}"):-3]
        if rest and not rest.startswith("-"): continue                      # bench-1800-1.3 is not bench-1800-1.30
        m = VERDICT.search(open(os.path.join(d, f), encoding="utf-8", errors="replace").read())
        if m and m.group("id") == eid and m.group("ver") == ver: got.add(m.group("verdict"))
    return "PASS" if "PASS" in got else ("REVIEWED, EM to sign" if "REVIEWED, EM to sign" in got else ("FINDINGS" if got else None))


def rereview_due(eid, ver, nxt, root=None, elements=None):
    """request mech-4 (core watch, 2026-11-07): held at station 7 only by the reviewer's line, while the reviewer has already reviewed
    this version (FINDINGS, or a safety element's "REVIEWED, EM to sign") and wrote no PASS. Every other hold at 7 cleared (EM's figures
    approved, DOC-005 PASS; a safety element's sign-off on file), so the element waits on the reviewer coming back to it, which
    reviewer.md 4b ("no review at its version") never does (proposal in lib/requests/core/needs-em.md, 2026-11-07 04:30 UTC). The
    board lists these, so the reviewer's re-read has a list to work from. A PASS whose recorded fingerprint is not the files' now
    (review_stale, escape group 13) is due too: the re-read reads what changed since and records the new fingerprint."""
    if nxt and nxt[0] == 7 and nxt[4] and all(h.startswith(STALE_REVIEW) for h in nxt[4]): return True
    if not nxt or nxt[0] != 7 or not nxt[4] or not all(h.startswith(NO_REVIEWER_LINE) for h in nxt[4]): return False
    return review_verdict(eid, ver, root, elements) in ("FINDINGS", "REVIEWED, EM to sign")


def reached(rows):
    """the last station passed (0: none)"""
    return max([n for n, _, _, ok, _ in rows if ok] or [0])


def owners():
    lanes = {}
    for r in csv.DictReader(open(os.path.join(LIB, "OWNERS.csv"), encoding="utf-8")):
        m = re.match(r"^lib/elements/([^/*]+)/\*$", r["path"] or "")
        if m: lanes[m.group(1)] = r["owner"]
    return lanes


def board(lane=None):
    """per lane: every element, the station it has reached, and what holds it at the next one"""
    findings, cat, tags, reviews, lanes, safety = _findings(), _catalogue(), _tags(), _reviews(), owners(), _safety()
    per = {}
    for eid in sorted(cat):
        ln = lanes.get(eid, "?")
        if lane and ln != lane: continue
        rows = element(eid, findings, cat, tags, reviews, safety); r = reached(rows)
        nxt = next((x for x in rows if not x[3]), None)
        per.setdefault(ln, []).append((eid, cat[eid]["version"], r, nxt))
    return per
