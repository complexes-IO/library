#!/usr/bin/env python3
"""One command for the library: build every element, run every check, regenerate catalogue.csv, build every assembly.
    python lib/build.py              everything
    python lib/build.py check        checks + validation (fast, no previews)
    python lib/build.py validate     the validation suite only (add -v to list every REVIEW, --fast to skip geometry and motion)
    python lib/build.py assembly <id>  one assembly: built, and the assembly rules run on it (no report written; -v lists every PASS)
    python lib/build.py <element-id> one element and its check
    python lib/build.py expect <element-id>   rewrite check.py's expected numbers from the current build (after a deliberate change)
    python lib/build.py [changed] -v --part=<k>/<n>   the full build in n commands: part k builds the k-th slice of the elements;
                                     the last checks the others passed on this tree, then validates and stamps (incremental.part_slice)
    python lib/build.py selftest     the validation suite's seeded-fault tests (every checker must catch its planted fault)
    python lib/build.py twin <assembly-id> [--smoke]   the operable twin of a machine in Godot (lib/toolkit/twin; --smoke: headless)
    python lib/build.py line [lane]             the element line: every element at the station it has reached, and what holds it
    python lib/build.py station <id>            one element, station by station (OPERATING.md 13)
    python lib/build.py inventory [lane]        what the 40 systems need, what is built, and each lane's next elements (lib/inventory.csv)
    python lib/build.py owners <lane> [base] [branch]   files changed since base (default main) that the lane does not own (OWNERS.csv);
                                     no branch: this worktree, uncommitted files included
Exit code 1 if any check fails."""
import csv, io, os, subprocess, sys
for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8", errors="replace")       # Windows consoles default to cp1252
    except Exception: pass
os.environ.setdefault("PYTHONUTF8", "1")                                   # child checks read UTF-8 specs on every platform
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from toolkit import VERSION as TOOLKIT_VERSION, library, qa, validate
from toolkit import fillet as FIL
from toolkit.prims import extents, nodes

def catalogue(status=None):
    status = status or {}
    rows = []
    for eid in library.element_ids():
        m = library.load(eid); P = m.build(**getattr(m, "PARAMS", {})); lo, hi = extents(P)
        own = library.own_bom(m)
        rows.append(dict(id=eid, **{"class": m.CLASS}, version=m.VERSION, status=("rebuild" if m.TOOLKIT != TOOLKIT_VERSION else {"PASS": "releasable", "REVIEW": "review", "FAIL": "fail"}.get(status.get(eid), "built")), title=m.TITLE,
                         size_mm=f"{hi[0] - lo[0]:.0f} x {hi[1] - lo[1]:.0f} x {hi[2] - lo[2]:.0f}", origin=m.ORIGIN, nodes=" ".join(nodes(P)),
                         params=";".join(f"{k}={v}" for k, v in getattr(m, "PARAMS", {}).items()), carries=" ".join(f"{r['tag']}={r['element']}@{r['version']}" for r in own),
                         toolkit=m.TOOLKIT, command=m.COMMAND, baseline=m.BASELINE,
                         budget_tris=qa.budgets(m)[0], budget_mats=qa.budgets(m)[1], fillet_r=FIL.radius(m.CLASS, m)))   # one source for Godot QA and the gate
    b = io.StringIO(newline=""); w = csv.DictWriter(b, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    from toolkit import outfile; outfile.write(os.path.join(HERE, "catalogue.csv"), b.getvalue(), newline="")    # unchanged: untouched
    print(f"catalogue.csv: {len(rows)} elements")

def branch_files(git, base, head):
    """the files a branch changed against base. Round 15's return: with more than one merge base (main merged core, then core
    merged an older main), `base...head` diffs from one of them and counts main's own commits as the branch's. A file counts only
    when it differs from every merge base: what equals one of them came in from main, not from the branch."""
    mbs = [m for m in git("merge-base", "--all", base, head).split() if m]
    if len(mbs) < 2: return set(git("diff", "--name-only", f"{base}...{head}").split("\n"))
    sets = [set(git("diff", "--name-only", m, head).split("\n")) for m in mbs]
    return set.intersection(*sets)

def owners(lane, base="main", head=None, here=None):
    """every file changed since base (lib/ and .github/) that `lane` does not own: the ownership check (lib/OPERATING.md, lib/OWNERS.csv).
    No head: this worktree's HEAD plus its uncommitted and untracked files. A head (a branch): that branch's commits only.
    here: the lib folder (a planted case's repository); default this library's."""
    import fnmatch
    HERE_ = here or HERE
    git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True, cwd=HERE_).stdout
    rows = [r for r in csv.DictReader(open(os.path.join(HERE_, "OWNERS.csv"), encoding="utf-8")) if r["path"] and not r["path"].startswith("#")]
    rows.sort(key=lambda r: (r["owner"] != "*", -len(r["path"].rstrip("*"))))   # generated files first, then the most specific
    def hit(f, p):                                                            # * stays inside one folder name; a trailing /* takes the subtree
        fs, ps = f.split("/"), p.split("/")
        if ps[-1] == "*" and len(fs) >= len(ps): fs = fs[:len(ps) - 1]; ps = ps[:-1]
        return len(fs) == len(ps) and all(fnmatch.fnmatchcase(x, y) for x, y in zip(fs, ps))
    root = git("rev-parse", "--show-toplevel").strip()
    for ref in (base, head or "HEAD"):                                        # round 8: a missing base made the diff silently empty
        if subprocess.run(["git", "rev-parse", "--verify", "--quiet", ref + "^{commit}"], capture_output=True, cwd=HERE_).returncode:
            print(f"owners: {ref!r} is not a commit here (no such branch?): nothing checked"); return False
    files = branch_files(git, base, head or "HEAD")
    if head is None:
        for line in git("status", "--porcelain", "--untracked-files=all").split("\n"):
            if len(line) > 3: files.add(line[3:].split(" -> ")[-1].strip('"'))
    lib = os.path.relpath(os.path.realpath(HERE_), os.path.realpath(root)).replace("\\", "/")                      # "lib" in the repo
    bad, seen, norow = [], 0, {}
    for f in sorted(x.strip() for x in files if x.strip()):
        if "__pycache__" in f: continue
        if f.startswith(lib + "/"): f = "lib/" + f[len(lib) + 1:]
        elif not f.startswith(".github/"): continue                          # the rest of the repo is outside the library
        seen += 1
        own = next((r["owner"] for r in rows if hit(f, r["path"])), None)
        if own == "*" or own == lane: continue
        if lane == "public" and f.startswith(("lib/elements/", "lib/assemblies/")) and "/" in f[len("lib/elements/"):]: continue   # the public library's contributions (toolkit/public_sync.py)
        if own is None and f.startswith("lib/elements/"):                    # a new element folder: the lane that makes it owns it
            d = "/".join(f.split("/")[:3]); norow[d] = norow.get(d, 0) + 1; continue
        bad.append((f, own))
    for f, o in bad: print(f"  NOT {lane}'s: {f} (owner {o})")
    for d, n in sorted(norow.items()):                                       # round 23's return 4.3: a stub folder on main with no row
        print(f"  no row: {d}/ ({n} file(s); counted as {lane}'s new element: the merge adds its OWNERS row)")
    print(f"owners: {seen} changed file(s) checked for lane {lane} against {base}, {len(bad)} outside it")
    return not bad

def inventory(lane=None, n=6):
    """the inventory (lib/inventory.csv) against what is built: per lane, the elements built and their status, then the next to
    build. Rank: the systems an element unlocks, or for a common part the systems of the devices made of it (made_of), whichever
    is more. Status from catalogue.csv and the release tags, never from the inventory."""
    import re
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, "inventory.csv"), encoding="utf-8")) if not r["id"].startswith("#")]
    cat = {r["id"]: r for r in csv.DictReader(open(os.path.join(HERE, "catalogue.csv"), encoding="utf-8"))}
    tags = set(subprocess.run(["git", "tag", "-l", "*/*"], capture_output=True, text=True, cwd=HERE).stdout.split())
    parts = lambda r: [m.group(1) for m in re.finditer(r"([a-z0-9][a-z0-9.\-]*)(?:\s*x\d+)?", r.get("made_of") or "")]
    demand, users = {}, {}
    for r in rows:
        for c in set(parts(r)):
            demand[c] = demand.get(c, 0) + int(r["systems"] or 0); users.setdefault(c, []).append(r["id"])
    rank = lambda r: max(int(r["systems"] or 0), demand.get(r["id"], 0))
    pin = lambda r: int(r["pin"]) if (r.get("pin") or "").strip().isdigit() else 10 ** 6   # EM's order first (inventory.csv pin; 2026-11-08: led, terminal-plug, vfd-0.75kw)
    total = len(rows); done = 0
    from toolkit import wanted as WT                                     # a person's claim (the wanted issues; branch wanted-claims): never built by a lane
    cl = subprocess.run(["git", "show", "origin/wanted-claims:claims.csv"], capture_output=True, text=True, cwd=HERE)
    claims = WT.claimed(cl.stdout) if cl.returncode == 0 else {}
    for ln in ([lane] if lane else sorted({r["lane"] for r in rows})):
        mine = [r for r in rows if r["lane"] == ln]
        built = [r for r in mine if r["id"] in cat]; todo = sorted((r for r in mine if r["id"] not in cat and r["id"] not in claims), key=lambda r: (pin(r), -rank(r), r["id"]))
        for r in mine:
            if r["id"] not in cat and r["id"] in claims: print(f"   claimed {r['id']:22s} by @{claims[r['id']]} (a contributor's: skip it; the wanted issue)")
        rel = [r for r in built if f"{r['id']}/{cat[r['id']]['version']}" in tags]; done += len(built)
        print(f"{ln}: {len(mine)} in the inventory · {len(built)} built ({len(rel)} released at their current version) · {len(todo)} to build")
        for r in built: print(f"   built   {r['id']:22s} {cat[r['id']]['version']:5s} {cat[r['id']]['status']:10s} unlocks {r['systems']} systems")
        for r in todo[:n]:
            why = f"unlocks {r['systems']} systems" if int(r["systems"] or 0) >= demand.get(r["id"], 0) else f"part of {len(users[r['id']])} devices ({demand[r['id']]} systems)"
            if pin(r) < 10 ** 6: why = f"pinned {pin(r)} (EM); " + why
            print(f"   next    {r['id']:22s} {why:34s} {r.get('type', '')}")
        from toolkit import generic as GN                                 # then ETIM classes, built generic (EM 2026-11-07; toolkit/generic.py),
        nx = GN.next_classes(ln, 0)                                       # always some: a lane whose rows all wait builds these (core watch 2026-11-12)
        for r in nx[:GN.etim_shown(len(todo), n)]: print(f"   etim    {r['class']:22s} {'generic, ' + r['group_description'][:24]:34s} {r['description']}")
        print(f"   ETIM classes left for {ln} to build generic: {len(nx)} ({sum(1 for r in nx if r.get('tier') == '1')} machine core)"
              + (": when no row above builds unattended, the next element is the first class here" if nx and todo else ""))
    if not lane: print(f"inventory: {done} of {total} built")
    return True

def line_board(lane=None):
    """the element line (OPERATING.md 13): per lane, each element at the station it has reached, and what holds it next"""
    from toolkit import line as LN
    per = LN.board(lane); names = {n: t for n, _, t in LN.STATIONS}
    for ln, items in sorted(per.items()):
        wip = sum(1 for e, v, r, nxt in items if LN.wip(r, nxt, eid=e, ver=v))            # finish before start (EM 2026-11-05); waiting on EM, the core or the reviewer doesn't count (EM 2026-11-07)
        bk = sum(1 for e, v, r, nxt in items if LN.count_mark(r, nxt, eid=e, ver=v) == "back")   # core watch 2026-11-08: the backlog, fixed first, not counted
        em = sum(1 for e, v, r, nxt in items if LN.count_mark(r, nxt, eid=e, ver=v) == "EM")   # request elec-7: a vendor document's reading too
        co = sum(1 for _, _, r, nxt in items if LN.in_progress(r) and LN.waits_on_core(nxt) and not LN.waits_on_em(nxt))   # escape group 18
        rv = sum(1 for e, v, r, nxt in items if LN.count_mark(r, nxt, eid=e, ver=v) == "rev")   # core watch 2026-11-07: the marks add up to the header
        gq = sum(1 for e, v, r, nxt in items if LN.count_mark(r, nxt, eid=e, ver=v) == "gate")  # core watch 2026-11-09: first gates not yet run
        sw = sum(1 for e, v, r, nxt in items if LN.count_mark(r, nxt, eid=e, ver=v) == "src")   # EM 2026-11-09: a standard's document wanted
        print(f"{ln}: {len(items)} elements · {wip} in progress (not yet past station 7; limit 3) · {em} waiting on EM (not counted) · "
              + (f"{co} waiting on the core's Blender re-gate (not counted) · " if co else "")
              + (f"{rv} waiting on the reviewer (not counted) · " if rv else "")
              + (f"{gq} waiting for a gate run, first or out of date (the lane's gate queue: gate up to three a round, first; not counted) · " if gq else "")
              + (f"{sw} waiting for a standard's document (lib/standards/wanted.md; not counted) · " if sw else "")
              + (f"{bk} taken back by a later rule or tool (the backlog: fix first; not counted) · " if bk else "") + " · ".join(f"{n}:{sum(1 for x in items if x[2] == n)}" for n in range(9)))
        for eid, ver, r, nxt in sorted(items, key=lambda x: (-x[2], x[0])):
            held = f"held at {nxt[0]} {names[nxt[0]]}: {nxt[4][0]}" + (f" (+{len(nxt[4]) - 1})" if len(nxt[4]) > 1 else "") if nxt else "released"
            if LN.rereview_due(eid, ver, nxt): held += f" [reviewed at {ver}: {LN.review_verdict(eid, ver)}; only the reviewer's line holds it: re-read due, build.py rereview]"
            print(f"   {r} {LN.count_mark(r, nxt, eid=eid, ver=ver):4s} {eid:22s} {ver:5s} {held}")   # request elec-5: which elements the limit counts
    return True

def rereview():
    """request mech-4: every element held at station 7 only by the reviewer's line though the reviewer has reviewed its version
    (toolkit/line.rereview_due), one per line, '<id> <version> <verdict>'; the reviewer's re-read works from this list"""
    from toolkit import line as LN
    n = 0
    for ln, items in sorted(LN.board().items()):
        for eid, ver, r, nxt in sorted(items):
            if LN.rereview_due(eid, ver, nxt):
                stale = nxt[4][0].startswith(LN.STALE_REVIEW)                 # escape group 13: a PASS read on other files
                print(f"{eid} {ver} {LN.review_verdict(eid, ver)}{', files changed since: now ' + LN.source_fingerprint(eid) if stale else ''} ({ln})"); n += 1
    print(f"rereview: {n} element(s) reviewed at their version, now held only by the reviewer's line"); return True

def line_history():
    """append the board to lib/line-history.csv: one row per element, its station now (core watch, every run; the improvement run
    reads lead time per station from it)"""
    import datetime as _dt
    from toolkit import line as LN
    p = os.path.join(HERE, "line-history.csv"); new = not os.path.exists(p); at = _dt.datetime.now().strftime("%Y-%m-%d %H:%M"); n = 0
    with open(p, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        if new: w.writerow(["at", "element", "lane", "version", "reached"])
        for ln, items in sorted(LN.board().items()):
            for eid, ver, r, _ in sorted(items): w.writerow([at, eid, ln, ver, r]); n += 1
    print(f"line-history.csv: {n} elements at {at}"); return True

def line_station(eid):
    from toolkit import line as LN
    rows = LN.element(eid)
    if not rows: print(f"station: {eid} is not in catalogue.csv"); return False
    for n, name, title, ok, hold in rows:
        print(f"  {n} {title:26s} {'PASS' if ok else ('open' if hold else 'waits for the station before')}")
        for h in hold: print(f"       {h}")
    return True

def run(path):
    r = subprocess.run([sys.executable, path], capture_output=True, text=True, encoding="utf-8", errors="replace", env={**os.environ, "PYTHONUTF8": "1"}); print(r.stdout.rstrip()); 
    if r.returncode: print(r.stderr.rstrip())
    return r.returncode == 0

def expect(eid):
    m = library.load(eid); P = m.build(**getattr(m, "PARAMS", {})); lo, hi = extents(P)
    lo = tuple(float(v) for v in lo); hi = tuple(float(v) for v in hi)
    open(os.path.join(library.ELEMENTS, eid, "check.py"), "w", encoding="utf-8").write(f'''#!/usr/bin/env python3
"""{eid}: the contract. Regenerate with `python lib/build.py expect {eid}` after a deliberate change; never to hide one."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from toolkit import check, library
check.run(library.load("{eid}"), dict(primitives={len(P)}, extents=({lo}, {hi}), nodes={nodes(P)}, holes={sum(1 for q in P if q[1] == "hole")}))
'''); print(f"check.py rewritten for {eid}: {len(P)} primitives, {lo} .. {hi}")

if __name__ == "__main__":
    flags = {a for a in sys.argv[1:] if a.startswith("-")}; sys.argv = [a for a in sys.argv if not a.startswith("-")]
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"; ok = True
    if arg == "expect": [expect(e) for e in (sys.argv[2:] or library.element_ids())]; sys.exit(0)
    if arg == "core":                                                     # lib/core/src/generated.rs for the Rust core and its Kani proofs
        from toolkit import coregen; path, nh, ng = coregen.write(); print(f"{os.path.relpath(path, HERE)}: {nh} M12 halves, {ng} golden cases"); sys.exit(0)
    if arg == "owners": sys.exit(0 if owners(sys.argv[2], *sys.argv[3:5]) else 1)
    if arg == "inventory": sys.exit(0 if inventory(sys.argv[2] if len(sys.argv) > 2 else None) else 1)
    if arg == "line": sys.exit(0 if line_board(sys.argv[2] if len(sys.argv) > 2 else None) else 1)
    if arg == "station": sys.exit(0 if line_station(sys.argv[2]) else 1)
    if arg == "history": sys.exit(0 if line_history() else 1)
    if arg == "rereview": sys.exit(0 if rereview() else 1)
    if arg == "fingerprint":                                              # an element's source fingerprint, the reviewer's method (escape group 13)
        if len(sys.argv) < 3: sys.exit("usage: python lib/build.py fingerprint <id> [<id> ...]")
        from toolkit import line as LN
        for e in sys.argv[2:]: print(f"{e} {LN.source_fingerprint(e) or 'no such element'}")
        sys.exit(0)
    if arg == "approvals":                                                # EM's station 7 sign-off page (toolkit/approvals.py)
        from toolkit import approvals; import json
        if sys.argv[2:3] == ["merge"] and len(sys.argv) == 4:
            a_, c_ = approvals.merge(json.load(open(sys.argv[3], encoding="utf-8"))); print(f"lib/approvals.csv: {a_} added, {c_} changed"); sys.exit(0)
        sys.exit("usage: python lib/build.py approvals merge <decisions.json>")
    if arg == "glb":                                                      # a gated variant's glb: glb <id> <suffix> k=v ... -> gate/<id>-<suffix>.glb
        if len(sys.argv) < 4: sys.exit("usage: python lib/build.py glb <id> <suffix> [k=v ...]")
        pr = library.parse_params(";".join(sys.argv[4:]))
        try: print(os.path.relpath(library.variant_glb(sys.argv[2], sys.argv[3], pr), HERE)); sys.exit(0)
        except ValueError as e: sys.exit(f"refused: {e}")
    if arg == "poses":                                                    # an element's pose check -> gate/<id>-poses.json (toolkit/poses.py)
        if len(sys.argv) != 3: sys.exit("usage: python lib/build.py poses <id>")
        from toolkit import poses
        try: sys.exit(0 if poses.run(sys.argv[2])["pass"] else 1)
        except ValueError as e: sys.exit(f"refused: {e}")
    if arg == "dashboard":                                               # the control room, read-only (toolkit/dashboard.py)
        from toolkit import dashboard
        sys.exit(0 if dashboard.serve(next((int(a) for a in sys.argv[2:] if a.isdigit()), 8765), "--lan" in flags) else 1)
    if arg == "behaviour":                                                            # the behaviour spec (EM 2026-11-09; lib/behaviour.md)
        from toolkit import behaviour as BH
        if len(sys.argv) > 2 and sys.argv[2] == "draft":                             # the core's proposals its nodes settle (BH.draft)
            import datetime; lane = next((a for a in sys.argv[3:] if not a.startswith("-")), None); n = 0
            for ln, eid, note in BH.missing(lane):
                if note: continue
                m = library.load(eid); txt, why = BH.draft(eid, m.build(**getattr(m, "PARAMS", {})), today=datetime.date.today().isoformat())
                print(f"  {ln:5} {eid:28} {'drafted' if txt else 'left to the lane: ' + why}")
                if txt and "--write" in flags:
                    os.makedirs(BH.PROPOSED, exist_ok=True); open(os.path.join(BH.PROPOSED, eid + ".csv"), "w", encoding="utf-8", newline="\n").write(txt); n += 1
            print(f"{n} proposals written to lib/requests/core/behaviour/" if "--write" in flags else "(--write writes them; the core's only)"); sys.exit(0)
        if len(sys.argv) > 2 and not sys.argv[2].startswith("-"): print(BH.describe(sys.argv[2])); sys.exit(0)
        miss = BH.missing(); print(f"{len(miss)} elements without a behaviour.csv of their own ({sum(1 for m in miss if m[2])} proposed by the core):")
        for lane, eid, note in miss: print(f"  {lane:5} {eid:28} {note}")
        sys.exit(0)
    if arg == "derive":                                                               # derived figures (EM 2026-11-09; toolkit/derive.py)
        from toolkit import derive as DV; print(DV.describe(sys.argv[2:])); sys.exit(0)
    if arg == "wanted":                                                               # the documents class B figures wait for
        from toolkit import derive as DV
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "standards", "wanted.md"); txt = DV.wanted_md()
        open(out, "w", encoding="utf-8", newline="\n").write(txt); print(txt.splitlines()[4]); print("->", os.path.relpath(out)); sys.exit(0)
    if arg == "drawio":                                                               # draw.io diagrams of the work (EM 2026-11-09)
        from toolkit import drawio as DW
        path, msg = DW.write(sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("-") else None)
        print(msg if path is None else f"{msg} -> {os.path.relpath(path, os.path.dirname(os.path.abspath(__file__)))}"); sys.exit(0 if path else 1)
    if arg == "index":                                                                # round 27's return 4.3: the unattended tool list holds build.py, not the script
        r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "element-index.py")] + sys.argv[2:]); sys.exit(r.returncode)
    if arg == "publish":                                                              # the public library's tree (toolkit/publish.py)
        from toolkit import publish as PB
        if len(sys.argv) < 3: sys.exit("usage: python lib/build.py publish <out dir>")
        src = os.path.dirname(HERE); n, masked, fatal = PB.export(src, sys.argv[2], PB.public_docs(src))
        for x in fatal: print(f"  REFUSED {x[0]}:{x[2]}: {x[1]} ({x[3]})")
        print(f"publish: {n} files to {sys.argv[2]}; {len(masked)} PC path(s) masked; {len(fatal)} refused"); sys.exit(1 if fatal else 0)
    if arg == "store":                                                                # the catalogue of what is not in store (toolkit/wanted.py)
        from toolkit import wanted as WT; import json
        S = WT.specs(); print(json.dumps(S, indent=1, ensure_ascii=False) if "-v" in flags else
                             "\n".join(f"  {s['id']:28} {', '.join(s['labels'][1:])}" for s in S) + f"\n{len(S)} wanted"); sys.exit(0)
    if arg == "guard":                                                                # what a contribution may bring in (toolkit/guard.py)
        from toolkit import guard as GD
        base = sys.argv[2] if len(sys.argv) > 2 else "HEAD"; paths, F = GD.check(base, external="--external" in flags)
        for st, rule, where, msg in F: print(f"  {st:6} {rule} {where}: {msg}")
        print(f"guard: {len(paths)} changed file(s) against {base}{' (external)' if '--external' in flags else ''}; {len(F)} refused")
        sys.exit(1 if F else 0)
    if arg == "audit":                                                                # EM's audit card (toolkit/audit.py; EM 2026-11-12)
        from toolkit import audit as AU; import json
        ids = [a for a in sys.argv[2:] if not a.startswith("-") and a in library.element_ids()]
        print(json.dumps(AU.cards(ids), indent=1, ensure_ascii=False)); sys.exit(0)
    if arg in ("own", "rename"):                                                      # every element is the Institute's (EM 2026-11-10; toolkit/owner.py)
        from toolkit import owner as OW; print(OW.describe(([arg] if arg == "rename" else []) + sys.argv[2:] + sorted(flags))); sys.exit(0)
    if arg == "assembly":                                                             # one assembly: build it, run the assembly rules (request panel-5 2a)
        if len(sys.argv) != 3: sys.exit("usage: python lib/build.py assembly <id> [-v] [--fast]")
        F = validate.assembly_run(sys.argv[2], geometry="--fast" not in flags)
        for f in sorted(F, key=lambda f: ({"FAIL": 0, "REVIEW": 1, "PASS": 2}[f["status"]], f["rule"])):
            if f["status"] != "PASS" or "-v" in flags: print(f"  {f['status']:6} {f['rule']:8} {f['where']}: {f['message']}")
        n = {s_: sum(f["status"] == s_ for f in F) for s_ in ("PASS", "REVIEW", "FAIL")}
        print(f"{sys.argv[2]}: {len(F)} findings, {n['PASS']} pass, {n['REVIEW']} review, {n['FAIL']} fail (no report written: the full build writes them)")
        sys.exit(1 if n["FAIL"] else 0)
    if arg == "nets":                                                                 # the solver (lib/behaviour.md; toolkit/nets.py)
        from toolkit import nets as NT
        inp = {a.split("=")[0]: a.split("=")[1] not in ("0", "false", "off") for a in sys.argv[3:] if "=" in a}
        print(NT.describe(sys.argv[2], inp)); sys.exit(0)
    if arg == "twin":
        from toolkit import twin as TW; sys.exit(TW.run(sys.argv[2], smoke="--smoke" in flags))
    if arg == "selftest":
        from toolkit import selftest; sys.exit(0 if selftest.main() else 1)
    part = None
    if arg == "changed":                                                             # the build of what changed (toolkit/incremental.py)
        from toolkit import incremental as INC, rules as RL
        base = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
        asm_now = sorted(a for a in os.listdir(os.path.join(HERE, "assemblies")) if os.path.isfile(os.path.join(HERE, "assemblies", a, "assembly.py")))
        old = INC.base_findings(base); be, ba = INC.base_ids(base)
        sc = INC.scope(INC.files(base), library.element_ids(), asm_now, INC.dependents(), be, ba)
        if INC.full_due(): sc = ("full", INC.full_due())
        elif INC.gone_since_full(library.element_ids(), asm_now): sc = ("full", INC.gone_since_full(library.element_ids(), asm_now))
        elif old is None: sc = ("full", f"{base} has no lib/out/validation.json")
        elif (old.get("toolkit"), old.get("validation"), old.get("rules")) != (validate.TOOLKIT, validate.VALIDATION, len(RL.RULES)):
            sc = ("full", f"{base}'s validation.json was written by another toolkit, validation version or rule count")
        if sc[0] == "full": print(f"changed: the full build ({sc[1]})"); arg = "all"
        else:
            new_e = sorted(set(library.element_ids()) - set(old.get("status", {})) - set(sc[1]))          # no findings at the base: they join the run
            new_a = sorted(set(asm_now) - set(old.get("status", {})) - set(sc[2]))
            if new_e or new_a: sc = ("part", sorted(set(sc[1]) | set(new_e)), sorted(set(sc[2]) | set(new_a)), sc[3] + f", {len(new_e) + len(new_a)} with no findings at {base}")
            part = (sc[1], sc[2], old["findings"])
            print(f"changed against {base}: {len(sc[1])} element(s), {len(sc[2])} assembly(ies): {sc[3]}; every other finding is {base}'s")
            if not sc[1] and not sc[2]: print("  nothing a build reads changed")
    ids = part[0] if part else library.element_ids() if arg in ("all", "check") else ([] if arg == "validate" else [arg])
    pk = next((f[len("--part="):] for f in flags if f.startswith("--part=")), None); pkn = None   # a full build in parts (incremental.part_slice)
    if pk:
        from toolkit import incremental as INC
        try: pkn = tuple(int(x) for x in pk.split("/")); assert len(pkn) == 2 and 1 <= pkn[0] <= pkn[1]
        except (ValueError, AssertionError): sys.exit("usage: --part=<k>/<n>, 1 <= k <= n (python lib/build.py [changed] -v --part=1/2, then --part=2/2)")
        if arg != "all" or part:
            if pkn[0] < pkn[1]: print(f"part {pk}: not the full build; nothing to do until the last part ({pkn[1]}/{pkn[1]})"); sys.exit(0)
            pkn = None
        else:
            key = INC.tree_key(); miss = INC.parts_missing(pkn[1], key, INC.parts_text()) if pkn[0] == pkn[1] else []
            if miss: print(f"part {pk}: part(s) {', '.join(f'{j}/{pkn[1]}' for j in miss)} not passed on this tree (HEAD and index); run them first"); print("FAILURES"); sys.exit(1)
            ids = INC.part_slice(ids, *pkn); print(f"part {pk} of the full build: {len(ids)} of {len(library.element_ids())} elements" + (", then validation, catalogue and assemblies" if pkn[0] == pkn[1] else ""))
    for eid in ids:
        d = os.path.join(library.ELEMENTS, eid)
        if arg != "check": print(f"build {eid}"); ok &= run(os.path.join(d, "element.py"))
        ok &= run(os.path.join(d, "check.py"))
        m = library.load(eid); probs = qa.run(m, m.build(**getattr(m, "PARAMS", {})))
        print(f"  qa   {eid}: " + ("PASS" if not probs else "FAIL\n    " + "\n    ".join(probs))); ok &= not probs
    if pkn and pkn[0] < pkn[1]:
        INC.parts_write(INC.part_record(pkn[0], pkn[1], ok, key, INC.parts_text()))
        print(f"PART {pk} {'PASS' if ok else 'FAILURES'}" + (f": run --part={pkn[0] + 1}/{pkn[1]} next" if ok else "")); sys.exit(0 if ok else 1)
    status = {}
    if arg in ("all", "check", "validate", "changed"):
        asm = sorted(a for a in os.listdir(os.path.join(HERE, "assemblies")) if os.path.isfile(os.path.join(HERE, "assemblies", a, "assembly.py")))
        status = validate.report(library.element_ids(), asm, geometry="--fast" not in flags, verbose="-v" in flags, part=part)
        print("(check / qa decide ALL PASS; the validation suite decides release)")
    if arg in ("all", "changed"):
        catalogue(status)
        from toolkit import coregen; cp, nh, ng = coregen.write(); print(f"{os.path.relpath(cp, HERE)}: {nh} M12 halves, {ng} golden cases (the Rust core's data)")
        for a in sorted(os.listdir(os.path.join(HERE, "assemblies"))):
            p = os.path.join(HERE, "assemblies", a, "assembly.py")
            if os.path.isfile(p) and (part is None or a in part[1]): print(f"assemble {a}"); ok &= run(p)
    if ok and arg == "all" and "--fast" not in flags:
        from toolkit import incremental as INC                                         # `changed` builds in full again 12 h from now,
        INC.mark_full(ids=list(library.element_ids()) + [a for a in os.listdir(os.path.join(HERE, "assemblies"))      # or once a folder built here is gone
                                                         if os.path.isfile(os.path.join(HERE, "assemblies", a, "assembly.py"))])
    if pkn: INC.parts_write("")                                                       # the last part ran: the parts are spent
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
