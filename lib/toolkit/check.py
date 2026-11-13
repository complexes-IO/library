"""The contract every element's check.py runs. `run(mod, expect)` builds the element and verifies:
  metadata present and well formed · version in element.py matches the spec.md header · toolkit version recorded ·
  primitive count, extents (mm, tolerance 0.5), node names, hole count against `expect` · every hole targets an existing solid ·
  every BOM row it carries resolves to a library element at a compatible version.
Exit code 1 on the first failure; prints one line per check."""
import os, re, sys
from . import VERSION as TOOLKIT_VERSION, library
from .prims import extents, nodes

def run(mod, expect):
    here = os.path.dirname(os.path.abspath(mod.__file__)); fails = 0
    def ok(cond, what, got=""):
        nonlocal fails
        print(f"  {'ok  ' if cond else 'FAIL'} {what}" + (f": {got}" if got != "" and not cond else "")); fails += 0 if cond else 1
    print(f"{mod.ID} v{mod.VERSION}")
    for k in ("ID", "VERSION", "CLASS", "TITLE", "TOOLKIT", "BASELINE", "ORIGIN", "COMMAND", "build", "PREVIEWS"): ok(hasattr(mod, k), f"has {k}")
    ok(re.fullmatch(r"\d+\.\d+", mod.VERSION) is not None, "version is major.minor", mod.VERSION)
    spec = open(os.path.join(here, "spec.md"), encoding="utf-8").read().splitlines()[0] if os.path.isfile(os.path.join(here, "spec.md")) else ""
    ok(f"v{mod.VERSION}" in spec, "spec.md header carries the same version", spec)
    ok(mod.TOOLKIT == TOOLKIT_VERSION, f"built with toolkit {TOOLKIT_VERSION}", mod.TOOLKIT)
    P = mod.build(**getattr(mod, "PARAMS", {}))
    ok(len(P) == expect["primitives"], f"{expect['primitives']} primitives", len(P))
    lo, hi = extents(P); elo, ehi = expect["extents"]
    ok(all(abs(a - b) <= 0.5 for a, b in zip(lo, elo)) and all(abs(a - b) <= 0.5 for a, b in zip(hi, ehi)), f"extents {elo} .. {ehi}", f"{lo} .. {hi}")
    ok(nodes(P) == sorted(expect["nodes"]), "nodes " + ", ".join(sorted(expect["nodes"])), nodes(P))
    holes = [(i, q) for i, (L, k, q) in enumerate(P) if k == "hole"]
    ok(len(holes) == expect["holes"], f"{expect['holes']} holes", len(holes))
    subs = [(i, q) for i, (L, k, q) in enumerate(P) if k in ("hole", "cut")]
    ok(all(0 <= q[-1] < i and P[q[-1]][1] not in ("hole", "cut") for i, q in subs), "every hole and cut targets an earlier solid")
    for row in library.own_bom(mod):
        try: library.load(row["element"], row["version"]); ok(True, f"bom: {row['tag']} = {row['element']} {row['version']}")
        except Exception as e: ok(False, f"bom: {row['tag']} = {row['element']} {row['version']}", e)
    print(f"  {'PASS' if not fails else f'{fails} FAILED'}")
    if fails: sys.exit(1)
    return P
