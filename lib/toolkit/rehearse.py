"""The library's next merge run, rehearsed in the cloud (core watch 2026-11-16, the improvement run; a flow change, a merge check).

The PC was silent 40 h with origin/core (round 37) and 14 queued lane rounds waiting for main, and round 36's core merge had been
refused twice on the PC (340/341 under COMPLEXES_UNATTENDED) before anyone in the cloud saw the cause. A refusal found when the PC
comes back costs the restart its first hours. This merges what waits, in the library's order (autopilot.merge_order: core first,
then the rest oldest first), into a scratch worktree of main; runs the owners check of each branch the way the library does
(`owners <lane> main <branch>`); takes main's copy of a generated file that conflicts (owner `*`, OPERATING.md 5) and reports any
other conflict; then runs selftest on the merged tree attended and with COMPLEXES_UNATTENDED=1. Nothing is pushed or kept.
"""
import contextlib, csv, fnmatch, io, os, re, shutil, subprocess, sys, tempfile


def _hit(f, p):                                                            # build.owners' match: * in one name, trailing /* a subtree
    fs, ps = f.split("/"), p.split("/")
    if ps[-1] == "*" and len(fs) >= len(ps): fs = fs[:len(ps) - 1]; ps = ps[:-1]
    return len(fs) == len(ps) and all(fnmatch.fnmatchcase(x, y) for x, y in zip(fs, ps))


def generated(path, owners_csv):
    """True when the most specific OWNERS.csv row for path is owner `*` (generated: take main's copy and rebuild)"""
    rows = [r for r in csv.DictReader(io.StringIO(owners_csv)) if r.get("path") and not r["path"].startswith("#")]
    rows.sort(key=lambda r: (r["owner"] != "*", -len(r["path"].rstrip("*"))))
    own = next((r["owner"] for r in rows if _hit(path, r["path"])), None)
    return own == "*"


def lane_of(ref):
    """the lane whose owners check a branch takes: origin/core -> core, origin/cloud-pneu -> pneu, origin/review -> review"""
    b = ref.split("/", 1)[-1]
    return b[len("cloud-"):] if b.startswith("cloud-") else b


def rehearse(repo, base, refs, owners=None, selftest=True, build=False, log=print):
    """merge refs, in order, into a scratch worktree of base in repo. owners(lane, base, head, here) -> bool, printing its lines
    (build.owners). Returns [{ref, lane, owners, owners_line, merge: merged|conflict|error, generated: [...], conflicts: [...]}]
    and, with selftest, a dict {attended: "n of m", unattended: "n of m", ok}; with build, the changed -v summary."""
    G = lambda *a, cwd=None: subprocess.run(["git", "-c", "user.email=core-watch@users.noreply.github.com", "-c", "user.name=core watch", *a],
                                            cwd=cwd or repo, capture_output=True, text=True, encoding="utf-8", errors="replace")
    wt = tempfile.mkdtemp(prefix="rehearse-"); os.rmdir(wt)
    r = G("worktree", "add", "-q", "--detach", wt, base)
    if r.returncode: return [{"ref": base, "lane": "", "owners": False, "owners_line": "", "merge": "error",
                              "generated": [], "conflicts": [r.stderr.strip()]}], None
    out, st = [], None
    try:
        for ref in refs:
            lane = lane_of(ref); row = {"ref": ref, "lane": lane, "owners": True, "owners_line": "", "merge": "merged",
                                        "generated": [], "conflicts": []}
            if owners is not None:
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf): row["owners"] = bool(owners(lane, base, ref, os.path.join(wt, "lib")))
                row["owners_line"] = (buf.getvalue().strip().splitlines() or [""])[-1]
                row["owners_out"] = [ln.strip() for ln in buf.getvalue().splitlines() if ln.strip().startswith("NOT ")]
            m = G("merge", "--no-ff", "--no-commit", ref, cwd=wt)
            un = [f for f in G("diff", "--name-only", "--diff-filter=U", cwd=wt).stdout.split("\n") if f]
            if m.returncode and not un:                                     # nothing to commit, or git refused before merging
                if "Already up to date" in (m.stdout + m.stderr): row["merge"] = "merged"; out.append(row); continue
                row["merge"] = "error"; row["conflicts"] = (m.stderr or m.stdout).strip().splitlines()[-1:] or ["?"]
                G("merge", "--abort", cwd=wt); out.append(row); continue
            try: oc = open(os.path.join(wt, "lib", "OWNERS.csv"), encoding="utf-8").read()
            except OSError: oc = ""
            gen = [f for f in un if f.startswith("lib/") and generated(f, oc)]
            real = [f for f in un if f not in gen]
            if real:
                row["merge"] = "conflict"; row["conflicts"] = real; row["generated"] = gen
                G("merge", "--abort", cwd=wt); out.append(row); continue
            for f in gen: G("checkout", "HEAD", "--", f, cwd=wt)               # main's copy (autopilot.md, the library terminal, step 1)
            row["generated"] = gen
            G("commit", "-q", "--no-verify", "-m", f"rehearse {ref}", cwd=wt)
            out.append(row)
        if selftest:
            st = {}
            for key, extra in (("attended", {}), ("unattended", {"COMPLEXES_UNATTENDED": "1"})):
                env = {k: v for k, v in os.environ.items() if k != "COMPLEXES_UNATTENDED"}; env.update(extra)
                p = subprocess.run([sys.executable, os.path.join("lib", "build.py"), "selftest"], cwd=wt, env=env,
                                   capture_output=True, text=True, encoding="utf-8", errors="replace")
                mm = re.search(r"selftest: (\d+) of (\d+)", p.stdout)
                st[key] = f"{mm.group(1)} of {mm.group(2)}" if mm else f"no summary (exit {p.returncode})"
                st[key + "_wrong"] = [ln.strip() for ln in p.stdout.splitlines() if ln.strip().startswith(("WRONG", "FAIL", "!!"))][:5]
            st["ok"] = all(re.fullmatch(r"(\d+) of \1", st[k]) for k in ("attended", "unattended"))
        if build:
            p = subprocess.run([sys.executable, os.path.join("lib", "build.py"), "changed", "-v"], cwd=wt, capture_output=True,
                               text=True, encoding="utf-8", errors="replace")
            st = st or {}
            st["build"] = [ln for ln in p.stdout.splitlines() if re.search(r"ALL PASS|findings from|\bFAIL\b", ln)][-5:]
            st["build_exit"] = p.returncode
    finally:
        G("worktree", "remove", "--force", wt)
        shutil.rmtree(wt, ignore_errors=True)
    return out, st


def lines(rows, st):
    """what to print: one line per branch, then selftest; the first a REHEARSAL verdict"""
    bad = [r for r in rows if r["merge"] != "merged" or not r["owners"]]
    if st and not st.get("ok", True): bad.append({"ref": "selftest"})
    head = ("REHEARSAL CLEAN: " if not bad else "REHEARSAL REFUSED: ") + (", then ".join(r["ref"] for r in rows) or "nothing waits for main")
    out = [head]
    for r in rows:
        s = f"  {r['ref']} (owners {r['lane']}): {r['merge']}"
        if r["generated"]: s += f"; main's copy of {len(r['generated'])} generated file(s): " + ", ".join(r["generated"][:4])
        if r["conflicts"]: s += "; CONFLICT: " + ", ".join(r["conflicts"][:6])
        if not r["owners"]: s += "; " + r["owners_line"] + (" (" + "; ".join(r.get("owners_out", [])[:4]) + ")" if r.get("owners_out") else "")
        out.append(s)
    if st:
        if "attended" in st:
            out.append(f"  selftest on the merged tree: {st['attended']} attended, {st['unattended']} with COMPLEXES_UNATTENDED=1"
                       + ("" if st["ok"] else "; " + "; ".join(st["attended_wrong"] + st["unattended_wrong"])))
        if "build" in st: out.append("  changed -v: " + " | ".join(st["build"]) + f" (exit {st['build_exit']})")
    return out
