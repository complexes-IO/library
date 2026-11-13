"""The build of what changed (core chat 2026-11-11, a flow change: a full build is 65 minutes on the PC and every merge ran one, so
a queue of 14 lane rounds was 15 hours of building elements nobody had touched).

`python lib/build.py changed [base]` (base: a commit, default HEAD) builds, checks and validates the elements whose own files
differ from <base>, every element and assembly that carries or loads one of them, and the library-wide rules; every other
finding is taken from <base>'s lib/out/validation.json, which a full build wrote. The printed summary and the files written are
the full build's. It falls back to the full build, saying why, whenever the part is not safely knowable:

  - a changed file outside an element's or an assembly's folder that a build reads (toolkit, standards, build.py, lib/*.csv,
    lib/*.py other than the gate scripts, the Rust core), or a path this module does not know
  - an element or assembly folder that came or went under another name (a rename), or <base> has no validation.json, or it was
    written by another toolkit, validation version or rule count

  - this worktree's last full build is more than FULL_EVERY_H hours old, or there is no record of one
  - an element or assembly folder that last full build built is gone (renamed or removed since; the stamp lists them), so a
    rename committed before `changed` runs is seen though HEAD already holds it (round 32 return 4.2)

What it cannot see, and a full build does: a rule that reads another element's files (DOC-006 reads every element's part
numbers). That is what the last line above bounds: a full build that ends ALL PASS writes its time in this worktree's git folder
(no tracked file: a stamp in the tree would conflict across four worktrees), and `changed` builds in full once it is 12 hours old.
"""
import os, re, csv, json, subprocess, datetime as dt
from . import library

ROOT = library.ROOT
GENERATED = ("out", "gate", "thumbs", "qa", "__pycache__", "blend", "gltf", "dwg", "step")     # written by builds and gates, read by none
DOCS = ("reviews/", "rounds/", "needs-em/", "requests/", "metrics/", "out/", "roles/", "godot/", "milestone-1/")
DOC_FILES = ("catalogue.csv", "line-history.csv", "OWNERS.csv")
GATE_SCRIPTS = ("acad-gate.py", "acad_filedialog.py", "gate-report.py", "element-index.py", "iges2step.py", "step-measure-occ.py",
                "acad-import-check.py", "autopilot.py", "lock.py")


FULL_EVERY_H = 12


def _stamp(cwd=None):
    r = subprocess.run(["git", "rev-parse", "--absolute-git-dir"], cwd=cwd or os.path.dirname(ROOT), capture_output=True, text=True)
    return os.path.join(r.stdout.strip(), "complexes-last-full-build") if r.returncode == 0 and r.stdout.strip() else None


def mark_full(now=None, cwd=None, ids=None):
    """a full build ended ALL PASS: note when (this worktree's git folder), and the element and assembly folders it built (core watch
    2026-11-12, round 32 return 4.2: a rename committed before `changed` is invisible against HEAD; against this list it is not)"""
    p = _stamp(cwd)
    if p: open(p, "w", encoding="utf-8").write((now or dt.datetime.now()).isoformat(timespec="seconds") + "\n"
                                                + ("ids: " + ",".join(sorted(ids)) + "\n" if ids else ""))


def _stamp_text(cwd=None, text=None):
    if text is not None: return text
    p = _stamp(cwd)
    try: return open(p, encoding="utf-8").read() if p else ""
    except OSError: return ""


def gone_since_full(element_ids, assembly_ids, cwd=None, text=None):
    """why a full build is due because a folder the last full build built is gone (renamed or removed) since ('' when none, or when
    the stamp lists no folders: a stamp written before this rule). text: the stamp file's content, for the planted cases."""
    line = next((l for l in _stamp_text(cwd, text).splitlines() if l.startswith("ids: ")), "")
    if not line: return ""
    gone = sorted({i for i in line[5:].strip().split(",") if i} - set(element_ids) - set(assembly_ids))
    return f"{', '.join(gone[:4])}: gone or renamed since this worktree's last full build" if gone else ""


def full_due(now=None, cwd=None, text=None):
    """why a full build is due ('' when the last one is recent enough). text: the stamp file's content, for the planted cases."""
    text = _stamp_text(cwd, text)
    try: last = dt.datetime.fromisoformat((text.strip().splitlines() or [""])[0].strip())
    except ValueError: return "no full build on record in this worktree"
    age = ((now or dt.datetime.now()) - last).total_seconds() / 3600
    return f"this worktree's last full build is {age:.0f} h old (one every {FULL_EVERY_H} h)" if age > FULL_EVERY_H else ""


# A full build in parts (core watch 2026-11-13, round 33 return, a flow change: the PC's full build took 108 of the agent's 120 minutes
# for one command, and the tree grows by a dozen elements a run). `--part=k/n` builds the k-th of n slices of the elements; the
# last part checks that every earlier one passed on this same tree (HEAD and the index), then validates everything, writes the
# catalogue and assemblies and stamps the full build, as one full build would. A build that is not the full one (`changed` went
# incremental) does its work in the last part; the earlier parts have nothing to do.
PARTS = "complexes-full-parts"


def part_slice(ids, k, n):
    """the k-th of n contiguous slices of the sorted ids; the n slices hold every id once"""
    ids = sorted(ids); return ids[len(ids) * (k - 1) // n: len(ids) * k // n]


def tree_key(cwd=None):
    """HEAD and the index, so a part recorded on one tree is not counted on another ('' outside git)"""
    import hashlib
    c = cwd or os.path.dirname(ROOT)
    h = subprocess.run(["git", "rev-parse", "HEAD"], cwd=c, capture_output=True, text=True)
    i = subprocess.run(["git", "ls-files", "-s"], cwd=c, capture_output=True)
    if h.returncode or i.returncode: return ""
    return h.stdout.strip()[:12] + "-" + hashlib.sha256(i.stdout).hexdigest()[:12]


def _parts_path(cwd=None):
    p = _stamp(cwd); return os.path.join(os.path.dirname(p), PARTS) if p else None


def parts_text(cwd=None):
    p = _parts_path(cwd)
    try: return open(p, encoding="utf-8").read() if p else ""
    except OSError: return ""


def part_record(k, n, ok, key, text=""):
    """the parts file's text with part k/n's result on tree <key> added (an earlier result of the same part replaced)"""
    keep = [l for l in text.splitlines() if l.split()[:3] != [key, str(n), str(k)]]
    return "\n".join(keep + [f"{key} {n} {k} {'ok' if ok else 'fail'}"]) + "\n"


def parts_missing(n, key, text):
    """the earlier parts (1 .. n-1) not recorded as passed on tree <key> in an n-part build"""
    done = {int(l.split()[2]) for l in text.splitlines() if len(l.split()) == 4 and l.split()[:2] == [key, str(n)] and l.split()[3] == "ok"}
    return [j for j in range(1, n) if j not in done] if key else list(range(1, n))


def parts_write(text, cwd=None):
    p = _parts_path(cwd)
    if p: open(p, "w", encoding="utf-8").write(text)                       # empty once the last part has run


def files(base="HEAD", cwd=None):
    """paths (repo-relative, '/') that differ from <base> in the index or the working tree, and untracked ones"""
    cwd = cwd or os.path.dirname(ROOT)
    g = lambda *a: subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    return sorted({f.strip() for f in (g("diff", "--name-only", base) + g("ls-files", "--others", "--exclude-standard")).splitlines() if f.strip()})


def classify(path):
    """('element', id) | ('assembly', id) | ('none', why) | ('full', why) for one changed path"""
    p = path.replace("\\", "/")
    if not p.startswith("lib/"): return ("none", "outside lib/") if not p.startswith(".github/") else ("none", "ci")
    r = p[4:]; parts = r.split("/")
    if parts[0] == "elements":
        if len(parts) == 2: return ("none", "the elements' index and reports")
        if parts[1].startswith("_") or parts[2] in GENERATED: return ("none", "generated or a gate's output")
        return ("element", parts[1])
    if parts[0] == "assemblies":
        if len(parts) == 2: return ("none", "a note beside the assemblies")
        if parts[2] in GENERATED: return ("none", "generated")
        return ("assembly", parts[1])
    if r.startswith("requests/core/behaviour/") and r.endswith(".csv"): return ("element", parts[-1][:-4])     # a proposal the build reads (behaviour.rows)
    if any(r.startswith(d) for d in DOCS): return ("none", "reports, reviews, requests, role cards: no build reads them")
    if len(parts) == 1:
        if r in DOC_FILES or r in GATE_SCRIPTS: return ("none", "generated, or a gate script")
        if r.endswith((".md", ".txt")): return ("none", "text")
        return ("full", f"{r}: a build reads it")
    return ("full", f"{r}: a build reads it" if parts[0] in ("toolkit", "standards", "core") else f"{r}: a path the changed build does not know")


def dependents(element_ids=None, elements_dir=None, assemblies_dir=None):
    """{id: set of elements and assemblies that carry or load it} from each element's bom.csv and library.load("<id>") in its
    .py files, and each assembly's bom.csv"""
    ed = elements_dir or library.ELEMENTS; ad = assemblies_dir or os.path.join(ROOT, "assemblies")
    ids = list(element_ids) if element_ids is not None else library.element_ids()
    dep = {}
    def bom(path):
        try: return {(r.get("element") or "").strip() for r in csv.DictReader(open(path, encoding="utf-8")) if (r.get("element") or "").strip() and not r["element"].startswith("#")}
        except OSError: return set()
    for e in ids:
        d = os.path.join(ed, e); uses = bom(os.path.join(d, "bom.csv"))
        for f in (os.listdir(d) if os.path.isdir(d) else []):
            if f.endswith(".py"):
                try: uses |= set(re.findall(r"""\bload\(\s*["']([a-z0-9][a-z0-9.\-]*)["']""", open(os.path.join(d, f), encoding="utf-8", errors="replace").read()))
                except OSError: pass
        for u in uses - {e}: dep.setdefault(u, set()).add(e)
    for a in (sorted(os.listdir(ad)) if os.path.isdir(ad) else []):
        for u in bom(os.path.join(ad, a, "bom.csv")) - {a}: dep.setdefault(u, set()).add(a)
    return dep


def closure(seed, dep):
    out = set(seed); todo = list(seed)
    while todo:
        for d in dep.get(todo.pop(), ()):
            if d not in out: out.add(d); todo.append(d)
    return out


def scope(paths, element_ids, assembly_ids, dep, base_elements=None, base_assemblies=None):
    """('full', why) or ('part', elements, assemblies, why) for a list of changed paths. element_ids / assembly_ids: what the tree
    holds now; base_*: what <base> held (None: unknown, not compared)."""
    E, A = set(), set()
    for p in paths:
        k, v = classify(p)
        if k == "full": return ("full", v)
        if k == "element": E.add(v)
        if k == "assembly": A.add(v)
    if base_elements is not None:
        gone = sorted((set(base_elements) - set(element_ids)) | (set(base_assemblies or ()) - set(assembly_ids)))
        if gone: return ("full", f"{', '.join(gone[:4])}: gone or renamed since the base")
    lost = sorted((E - set(element_ids)) | (A - set(assembly_ids)))                 # files changed in a folder that is no element now
    if lost: return ("full", f"{', '.join(lost[:4])}: changed files in a folder that holds no element.py / assembly.py")
    seed = (E & set(element_ids)) | (A & set(assembly_ids))
    cl = closure(seed, dep)
    Es = sorted(cl & set(element_ids)); As = sorted(cl & set(assembly_ids))
    carried = sorted(cl - seed)
    return ("part", Es, As, f"{len(seed)} changed" + (f", {len(carried)} that carry or load them ({', '.join(carried[:5])}{'…' if len(carried) > 5 else ''})" if carried else ""))


def base_findings(base="HEAD", cwd=None):
    """<base>'s lib/out/validation.json (None when it has none or it does not parse)"""
    r = subprocess.run(["git", "show", f"{base}:lib/out/validation.json"], cwd=cwd or os.path.dirname(ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode: return None
    try: return json.loads(r.stdout)
    except ValueError: return None


def base_ids(base="HEAD", cwd=None):
    """(elements, assemblies) <base> held: folders with an element.py / assembly.py"""
    r = subprocess.run(["git", "ls-tree", "-r", "--name-only", base, "lib/elements", "lib/assemblies"], cwd=cwd or os.path.dirname(ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")
    E = {p.split("/")[2] for p in r.stdout.splitlines() if p.count("/") == 3 and p.endswith("/element.py")}
    A = {p.split("/")[2] for p in r.stdout.splitlines() if p.count("/") == 3 and p.endswith("/assembly.py")}
    return E, A


def merge(old, new, redone, element_ids, assembly_ids):
    """the full list of findings: <old>'s for every scope not redone and still in the tree, then the new ones. redone: the scopes
    run again (elements, assemblies and 'library')."""
    live = set(element_ids) | set(assembly_ids)
    keep = [f for f in old if f.get("scope") not in redone and f.get("scope") in live]
    order = {s: i for i, s in enumerate(sorted(element_ids) + ["library"] + sorted(assembly_ids))}     # a full run's order: no churn in validation.json
    return sorted(keep + list(new), key=lambda f: order.get(f.get("scope"), len(order)))
