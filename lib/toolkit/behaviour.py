"""The behaviour spec of an element, lib/elements/<id>/behaviour.csv (lib/behaviour.md; EM 2026-11-09: "every electrical and
mechanical element gets a behaviour spec"). This module reads it, checks it (BEH-010/020/030) and evaluates its `when`
expressions for the solver (toolkit/nets.py). An element knows only itself: its expressions name its own states, parts and pins.
    python lib/build.py behaviour <id>    -> the spec as the solver reads it
    python lib/build.py behaviour         -> the elements without a file, by lane
"""
import ast, csv, os, re

from . import library

KINDS = ("pin", "contact", "load", "source", "state", "pose", "link", "limit")
MANUAL = re.compile(r"^manual(?:\s+(toggle|latch|momentary))?(?:\s+cleared\s+by\s+([\w\-]+))?$", re.I)
MOVING = ("rotate", "translate", "compress", "emissive")
NUM = re.compile(r"^-?\d+(\.\d+)?$")

PROPOSED = os.path.join(os.path.dirname(library.ELEMENTS), "requests", "core", "behaviour")   # the core's proposals, lane by lane

def path(eid): return os.path.join(library.ELEMENTS, eid, "behaviour.csv")

def proposed(eid):
    """the core's proposed spec for an element whose lane hasn't taken it in yet (lib/requests/core/behaviour/<id>.csv), or None"""
    p = os.path.join(PROPOSED, eid + ".csv"); return p if os.path.isfile(p) and not os.path.isfile(path(eid)) else None

def rows(eid, proposals=True):
    p = path(eid)
    if not os.path.isfile(p): p = proposed(eid) if proposals else None
    if not p: return None
    out = []
    for r in csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#")):
        extra = r.pop(None, None)                                                   # more fields than the header: BEH-010
        if r and any((v or "").strip() for v in r.values()):
            d = {k: (v or "").strip() for k, v in r.items()}
            if extra: d["_extra"] = ",".join(extra)
            out.append(d)
    return out

def manual(when):
    """(kind, cleared_by) for a manual state row, else None"""
    m = MANUAL.match(when or "")
    return ((m.group(1) or "toggle").lower(), m.group(2) or "") if m else None

class When:
    """a parsed `when`: names it uses, and eval(env) over env = dict(states={name: bool}, V=fn(part)->float, I=fn(part)->float,
    Vab=fn(a, b)->float)"""
    OPS = {ast.Eq: lambda a, b: a == b, ast.NotEq: lambda a, b: a != b, ast.Lt: lambda a, b: a < b, ast.LtE: lambda a, b: a <= b,
           ast.Gt: lambda a, b: a > b, ast.GtE: lambda a, b: a >= b}
    def __init__(self, text):
        self.text = (text or "").strip(); self.states = set(); self.parts = set(); self.pins = set(); self.error = ""
        src = self.text.replace("-", "__D__") if self.text else "False"               # node and state names carry hyphens
        try: self.tree = ast.parse(src, mode="eval").body; self._walk(self.tree)
        except SyntaxError as e: self.tree = None; self.error = f"does not parse: {e.msg}"
    def _nm(self, s): return s.replace("__D__", "-")
    def _walk(self, n):
        if isinstance(n, ast.BoolOp): [self._walk(v) for v in n.values]
        elif isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.Not, ast.USub)): self._walk(n.operand)
        elif isinstance(n, ast.Compare): self._walk(n.left); [self._walk(c) for c in n.comparators]
        elif isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)): self._walk(n.left); self._walk(n.right)
        elif isinstance(n, ast.Constant) and isinstance(n.value, (int, float, bool)): pass
        elif isinstance(n, ast.Name): self.states.add(self._nm(n.id))
        elif isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.attr in ("V", "I"): self.parts.add(self._nm(n.value.id))
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "V" and len(n.args) == 2 and all(isinstance(a, (ast.Name, ast.Constant)) for a in n.args):
            self.pins.update(self._nm(a.id) if isinstance(a, ast.Name) else str(a.value) for a in n.args)
        else: self.error = f"not allowed in a when: {ast.dump(n)[:40]}"
    def eval(self, env):
        return bool(self._ev(self.tree, env)) if self.tree is not None else False
    def _ev(self, n, env):
        if isinstance(n, ast.BoolOp):
            vals = [self._ev(v, env) for v in n.values]; return all(vals) if isinstance(n.op, ast.And) else any(vals)
        if isinstance(n, ast.UnaryOp): v = self._ev(n.operand, env); return (not v) if isinstance(n.op, ast.Not) else -v
        if isinstance(n, ast.Compare):
            a = self._ev(n.left, env)
            for op, c in zip(n.ops, n.comparators):
                b = self._ev(c, env)
                if not self.OPS[type(op)](a, b): return False
                a = b
            return True
        if isinstance(n, ast.BinOp):
            a, b = self._ev(n.left, env), self._ev(n.right, env)
            return a + b if isinstance(n.op, ast.Add) else a - b if isinstance(n.op, ast.Sub) else a * b if isinstance(n.op, ast.Mult) else (a / b if b else float("inf"))
        if isinstance(n, ast.Constant): return n.value
        if isinstance(n, ast.Name): return bool(env.get("states", {}).get(self._nm(n.id), False))
        if isinstance(n, ast.Attribute): return float((env.get("V") if n.attr == "V" else env.get("I"))(self._nm(n.value.id)))
        if isinstance(n, ast.Call):
            a, b = (self._nm(x.id) if isinstance(x, ast.Name) else str(x.value) for x in n.args); return float(env["Vab"](a, b))
        return False

def spec(eid, R=None, params=None):
    """the spec as the solver reads it: dict(pins={mark: port}, torque={mark: value}, contacts=[(a, b, part, When, R)],
    loads=[(a, b, part, When|None, value, unit)], sources=[(a, b, part, When|None, value, unit, source)],
    states={part: [(name, When|None, manual|None, 'default'|'')]}, poses=[(nodes, When|state, amount)], links=[(a, b)],
    limits=[(a, value, unit)], inputs={state: dict(kind, cleared_by, part)}, forms={(param, values): {mark: node}},
    counts={mark: (node, param, k)}).
    A pin row whose `when` names a form (form()) moves its mark to node b in that form: params (the build's) that match it apply it;
    without params the default form's nodes stand. A pin row whose `when` names a count (count(): "count poles>=5") is a pin only in
    a build whose param is at least k (request panel-13 2: term-jumper's blades follow `poles`); with params it is in pins where the
    build has it, without params it is in counts only (nets.elements adds it where the placed build has its node). A pin row whose
    `when` names values (only(): "only kind=signal", request elec-15) is the same for a word: a pin only in a build whose param has
    one of them, stored in counts with k the tuple of values."""
    R = rows(eid) if R is None else R
    S = dict(pins={}, torque={}, contacts=[], loads=[], sources=[], states={}, poses=[], links=[], limits=[], inputs={}, forms={}, counts={})
    if R is None: return None
    later = []
    for r in R:
        k = r.get("kind", ""); a, b, part, when, val, unit = (r.get(x, "") for x in ("a", "b", "part", "when", "value", "unit"))
        if k == "pin" and form(when): S["forms"].setdefault(form(when), {})[a] = b; later.append((form(when), a, b)); continue
        if k == "pin" and (count(when) or only(when)):
            prm, kk = count(when) or only(when); S["counts"][a] = (b, prm, kk); S["torque"][a] = val
            if params is not None and has(params.get(prm), kk): S["pins"][a] = b
            continue
        if k == "pin": S["pins"][a] = b; S["torque"][a] = val
        elif k == "contact": S["contacts"].append((a, b, part, When("True" if when.lower() == "always" else when), val))
        elif k == "load": S["loads"].append((a, b, part, When(when) if when else None, val, unit))
        elif k == "source": S["sources"].append((a, b, part, When(when) if when else None, val, unit, r.get("source", "")))
        elif k == "state":
            m = manual(when); dflt = when.lower() == "default"; hold = when.lower() == "hold"
            S["states"].setdefault(part, []).append((a, None if (m or dflt or hold) else When(when), m, "default" if dflt else ("hold" if hold else "")))
            if m: S["inputs"][a] = dict(kind=m[0], cleared_by=m[1], part=part)
        elif k == "pose": S["poses"].append((a.split(), when, val))
        elif k == "link": S["links"].append((a, b))
        elif k == "limit": S["limits"].append((a, val, unit))
    for (prm, vals), a, b in later:
        if params is not None and str(params.get(prm, "")) in vals: S["pins"][a] = b
    return S

FORM = re.compile(r"^form\s+([A-Za-z_]\w*)\s*=\s*([\w.\-]+(?:\s*\|\s*[\w.\-]+)*)$")

COUNT = re.compile(r"^count\s+([A-Za-z_]\w*)\s*>=\s*(\d+)$")

def count(when):
    """(param, k) for a pin row's `when` that names a count ("count poles>=5": the pin is there only in a build whose param is at
    least k; request panel-13 2, core watch 2026-11-13), else None. A form moves a pin; a count adds one, and only a count does."""
    m = COUNT.match((when or "").strip())
    return (m.group(1), int(m.group(2))) if m else None

ONLY = re.compile(r"^only\s+([A-Za-z_]\w*)\s*=\s*([\w.\-]+(?:\s*\|\s*[\w.\-]+)*)$")

def only(when):
    """(param, (values...)) for a pin row's `when` that names the values its pin is in ("only kind=signal": the mark is a pin only
    in a build whose param has one of the values; request elec-15, core watch 2026-11-13: receptacle-m23's signal kind has contacts 4
    to 6 and no PE), else None. Stored with the counts (spec()["counts"], k a tuple of values): a count adds a pin for a number, an
    `only` for a word; a form moves one. The mark has no other row."""
    m = ONLY.match((when or "").strip())
    return (m.group(1), tuple(v.strip() for v in m.group(2).split("|"))) if m else None

def has(v, k):
    """a build whose param is v has a counts pin at k: v >= k for a count (k an int), v one of k for an `only` (k a tuple)"""
    if isinstance(k, tuple): return v is not None and str(v).strip() in k
    return _int(v) is not None and _int(v) >= k

def at(k):
    """the param value of a build that has a counts pin at k: k itself for a count, the first value for an `only`"""
    return k[0] if isinstance(k, tuple) else k

def _int(x):
    try: return int(str(x).strip())
    except (TypeError, ValueError): return None

def form(when):
    """(param, (values...)) for a pin row's `when` that names a form of the element ("form genders=male-open|female-open": the
    pin is at node b only in a build with that param; cordset-m12 1.8, core round 29), else None"""
    m = FORM.match((when or "").strip())
    return (m.group(1), tuple(v.strip() for v in m.group(2).split("|"))) if m else None

def state_names(S): return {n for part in S["states"].values() for n, w, m, d in part if d != "hold"}

def check(eid, P=None, R=None, build_of=None):
    """[(status, rule, where, message)] for one element: BEH-010 file and form, BEH-020 pins have port nodes (each form's in a build of
    that form; build_of: the element module, for tests), BEH-030 poses move real nodes"""
    R = rows(eid) if R is None else R
    if R is None: return [("REVIEW", "BEH-010", eid, "no behaviour.csv: what the element does at its terminals and joints (lib/behaviour.md; EM 2026-11-09)")]
    out = []; S = spec(eid, R); names = state_names(S); pins = set(S["pins"]); parts = set()
    if proposed(eid): out.append(("REVIEW", "BEH-010", eid, f"behaviour.csv proposed by the core (lib/requests/core/behaviour/{eid}.csv): the lane takes it into the element (copy it in, check each figure against its brief, commit) or writes its own"))
    for r in R:
        if r.get("_extra") is not None: out.append(("FAIL", "BEH-010", f"{eid} {r.get('kind')} {r.get('a')}", f"more fields than the header (spilled: '{r['_extra']}')"))
        if r.get("kind") not in KINDS: out.append(("FAIL", "BEH-010", f"{eid} {r.get('kind') or '(blank)'}", f"unknown kind; one of {', '.join(KINDS)}"))
        if not r.get("source") and r.get("kind") not in ("pose", "link"): out.append(("FAIL", "BEH-010", f"{eid} {r.get('kind')} {r.get('a')}", "no source: cite the document or write NOT ON FILE"))
        if r.get("kind") in ("contact", "load", "source", "pin") and r.get("part"): parts.add(r["part"])
        if r.get("kind") == "pin" and r.get("when"):
            fm = form(r["when"]); cn = count(r["when"]) or only(r["when"])
            if not fm and not cn: out.append(("FAIL", "BEH-010", f"{eid} pin {r.get('a')}", f"when '{r['when']}': a pin row's when names a form only ('form <param>=<value>[|<value>]'), a count ('count <param>>=<k>') or the values its pin is in ('only <param>=<value>[|<value>]')"))
            elif fm and r.get("a") not in pins: out.append(("FAIL", "BEH-010", f"{eid} pin {r.get('a')}", f"form row for a mark with no default pin row: the form moves a pin, it adds none (a pin that follows a parameter is a count: 'count <param>>=<k>')"))
            elif cn and r.get("a") in pins: out.append(("FAIL", "BEH-010", f"{eid} pin {r.get('a')}", f"{'count' if count(r['when']) else 'only'} row for a mark that has a default pin row: a {'count' if count(r['when']) else 'only'} row adds the pin, so the mark has no other row"))
    for part, lst in S["states"].items():
        if sum(1 for n, w, m, d in lst if d == "default") > 1: out.append(("FAIL", "BEH-010", f"{eid} state {part}", "two default rows"))
        if not any(d == "default" for n, w, m, d in lst): out.append(("FAIL", "BEH-010", f"{eid} state {part}", "no default row: which state is rest (a button's rest is a state too: 'released')"))
    for n, w, m, d in [x for lst in S["states"].values() for x in lst]:
        if m and m[1] and m[1] not in names: out.append(("FAIL", "BEH-010", f"{eid} state {n}", f"cleared by {m[1]}: no such state"))
    pins |= set(S["counts"])                                                            # a count's pin: in the builds that have it
    whens = [(f"contact {a}-{b}", w) for a, b, _, w, _ in S["contacts"]] + [(f"load {a}-{b}", w) for a, b, _, w, *_ in S["loads"] if w] + \
            [(f"source {a}-{b}", w) for a, b, _, w, *_ in S["sources"] if w] + [(f"state {n}", w) for lst in S["states"].values() for n, w, *_ in lst if w] + \
            [(f"pose {' '.join(nd)}", When(wh)) for nd, wh, _ in S["poses"] if wh not in names]
    for where, w in whens:
        if w.error: out.append(("FAIL", "BEH-010", f"{eid} {where}", f"when '{w.text}' {w.error}"))
        for s in w.states - names: out.append(("FAIL", "BEH-010", f"{eid} {where}", f"when names '{s}': not a state of this element"))
        for p in w.parts - parts: out.append(("FAIL", "BEH-010", f"{eid} {where}", f"when measures '{p}': not a load or contact part of this element"))
        for p in w.pins - pins: out.append(("FAIL", "BEH-010", f"{eid} {where}", f"when probes pin '{p}': no pin row"))
    for a, b, part, *_ in S["contacts"] + [x[:3] for x in S["loads"]] + [x[:3] for x in S["sources"]]:
        for p in (a, b):
            if p not in pins: out.append(("FAIL", "BEH-010", f"{eid} {part or a + '-' + b}", f"pin '{p}' has no pin row (mark, port node, torque)"))
    for a, b in S["links"]:
        if a not in names: out.append(("FAIL", "BEH-010", f"{eid} link {a}", "not a state of this element"))
    if P is not None:
        ports = {n for n, pv in P.pivots.items() if pv.get("kind") in ("port", "contact")}      # a clamp's contact zone is touchable too
        missing = [m for m, node in S["pins"].items() if node not in ports]
        dflt = {}
        if S["counts"]:                                                                  # a count's pins: in the default build up to its param, and each in a build at its k
            try: m_ = build_of if build_of is not None else library.load(eid); dflt = dict(getattr(m_, "PARAMS", {}))
            except Exception: m_ = None
            for mk, (node, prm, kk) in S["counts"].items():
                wd = "count" if not isinstance(kk, tuple) else "only"                     # an `only` pin (request elec-15): in a build at its first value
                if has(dflt.get(prm), kk): S["pins"][mk] = node; missing += [mk] if node not in ports else []
                try: Pk = m_.build(**dict(dflt, **{prm: at(kk)})); kports = {n for n, pv in Pk.pivots.items() if pv.get("kind") in ("port", "contact")}
                except Exception as e: out.append(("FAIL", "BEH-020", f"{eid} {wd} {prm}={at(kk)}", f"the build does not run: {e}")); continue
                if node not in kports: out.append(("REVIEW", "BEH-020", f"{eid} {wd} {prm}={at(kk)} pin {mk}", f"no port (or contact) node in a build of that {'count' if wd == 'count' else 'value'} for the probe to touch"))
        if missing: out.append(("REVIEW", "BEH-020", f"{eid} pins {' '.join(missing)}", "no port (or contact) node on the element for the probe to touch (P.pivot(<node>, 'port', ...))"))
        for (prm, vals), marks in S["forms"].items():                                    # each form's nodes, in a build of that form
            try:
                m = build_of if build_of is not None else library.load(eid)
                Pf = m.build(**dict(getattr(m, "PARAMS", {}), **{prm: vals[0]}))
                fports = {n for n, pv in Pf.pivots.items() if pv.get("kind") in ("port", "contact")}
            except Exception as e:
                out.append(("FAIL", "BEH-020", f"{eid} form {prm}={vals[0]}", f"the form does not build: {e}")); continue
            fmiss = [mk for mk, node in marks.items() if node not in fports]
            if fmiss: out.append(("REVIEW", "BEH-020", f"{eid} form {prm}={vals[0]} pins {' '.join(fmiss)}", "no port (or contact) node in a build of that form for the probe to touch"))
        tags = [t for _, _, t, _ in getattr(P, "owners", [])]                            # placed elements carry their own specs
        own_ports = {n for n in ports if n not in tags and not any(n.startswith(t + ".") for t in tags)}
        unpinned = sorted(own_ports - set(S["pins"].values()) - {"self"})
        if unpinned: out.append(("REVIEW", "BEH-040", f"{eid} ports {' '.join(unpinned)}", "port node with no pin row: what mark is printed there, what does it carry"))
        moving = {n for n, pv in P.pivots.items() if pv.get("kind") in MOVING and n not in tags and not any(n.startswith(t + ".") for t in tags)}
        posed = {n for nodes, _, _ in S["poses"] for n in nodes}
        unposed = sorted(moving - posed) if "*" not in posed else []
        if unposed: out.append(("REVIEW", "BEH-040", f"{eid} nodes {' '.join(unposed)}", "moving node with no pose row: which state moves it (or a manual state the operator sets)"))
        for nodes, when, amt in S["poses"]:
            for nd in nodes:
                if nd != "*" and nd not in moving: out.append(("FAIL", "BEH-030", f"{eid} pose {nd}", "not a moving node of the element (no rotate / translate / compress / emissive pivot)"))
            if amt != "end" and not NUM.match(amt): out.append(("FAIL", "BEH-030", f"{eid} pose {' '.join(nodes)}", f"amount '{amt}': a number or 'end'"))
    if not any(st == "FAIL" for st, *_ in out):
        out.append(("PASS", "BEH-010", eid, f"{len(S['pins'])} pins, {len(S['contacts'])} contacts, {len(S['loads'])} loads, {len(S['sources'])} sources, {sum(len(v) for v in S['states'].values())} states ({len(S['inputs'])} manual), {len(S['poses'])} pose rows"))
    return out

def pose_amount(P, node, amt):
    pv = P.pivots.get(node, {})
    if amt == "end": return float(pv.get("range", (0, 0))[1])
    return float(amt)

def poses(S, P, states):
    """{node: amount} for the element's current states (dict state name -> bool); a pose row's when is a state name or an expression"""
    names = state_names(S); out = {}
    moving = [n for n, pv in P.pivots.items() if pv.get("kind") in MOVING]
    for nodes, when, amt in S["poses"]:
        on = states.get(when, False) if when in names else When(when).eval(dict(states=states, V=lambda p: 0.0, I=lambda p: 0.0, Vab=lambda a, b: 0.0))
        if not on: continue
        for nd in nodes:
            for n in (moving if nd == "*" else [nd]):
                if n in P.pivots: out[n] = pose_amount(P, n, amt)
    return out

def missing(lane=None):
    """elements without a behaviour.csv of their own, [(lane, id, note)] (the lane from lib/OWNERS.csv as the board reads it; the note says
    when the core has proposed one)"""
    from . import line as LN
    lanes = LN.owners(); out = []
    for eid in library.element_ids():
        if rows(eid, proposals=False) is None and (lane is None or lanes.get(eid, "?") == lane):
            out.append((lanes.get(eid, "?"), eid, "proposed by the core: lib/requests/core/behaviour/" + eid + ".csv" if proposed(eid) else ""))
    return sorted(out)

HEADER = "kind,a,b,part,when,value,unit,source,note"

def draft(eid, P, motion_rows=None, today=""):
    """(text, reason): the core's proposal for an element whose spec its own nodes settle, or (None, why not) (core watch
    2026-11-09, the improvement run: 103 elements held at station 5 by BEH-010 alone, 38 of them structural parts whose file is
    the header and a pose per moving node, at a lane's three a round). Drafted only when the element has no own port or contact
    node (a pin's mark is printed on the part: the lane reads it), no emissive node (what lights it is behaviour), no compress
    node (a spring follows a load), and no own node in lib/motion.csv (a follower or an interlock is the lane's to state). Each
    moving node gets its own manual toggle, rest by default, and a pose at its range end: no figure but the pivot's own."""
    if os.path.isfile(path(eid)): return None, "has its own behaviour.csv"
    tags = [t for _, _, t, _ in getattr(P, "owners", [])]
    own = lambda n: n not in tags and not any(n.startswith(t + ".") for t in tags)
    ports = sorted(n for n, pv in P.pivots.items() if pv.get("kind") in ("port", "contact") and own(n) and n != "self")
    if ports: return None, "port nodes " + " ".join(ports[:4]) + ": a pin row each, its mark read from the part"
    moving = [(n, pv) for n, pv in P.pivots.items() if pv.get("kind") in MOVING and own(n)]
    if any(pv.get("kind") == "emissive" for _, pv in moving): return None, "an emissive node: what lights it is the device's behaviour"
    if any(pv.get("kind") == "compress" for _, pv in moving): return None, "a compress node: a spring follows a load"
    if any(not pv.get("range") for _, pv in moving): return None, "a moving node with no range: 'end' has nothing to read"
    if motion_rows is None:
        mp = os.path.join(os.path.dirname(library.ELEMENTS), "motion.csv")
        motion_rows = list(csv.DictReader(l for l in open(mp, encoding="utf-8") if not l.startswith("#"))) if os.path.isfile(mp) else []
    import fnmatch
    named = {r.get(k) for r in motion_rows if fnmatch.fnmatch(eid, r.get("scope") or "") for k in ("leader", "follower")}
    tied = sorted(n for n, _ in moving if n in named)
    if tied: return None, "motion.csv ties " + " ".join(tied) + ": a follower or an interlock is the lane's to state"
    L = [f"# PROPOSED by the core {today} for the lane that owns the element: copy to lib/elements/<id>/behaviour.csv, check each row against element.py and the spec, commit. Until then BEH-010 is REVIEW.",
         f"# behaviour.csv · {eid} (lib/behaviour.md). Drafted from the element's own nodes (toolkit/behaviour.draft): " +
         ("a structural part, no terminals, no moving nodes, no states. The file says so." if not moving else
          "no terminals; each moving node a manual toggle, rest by default, posed at its range end. Name the states by what they mean (open, closed) when you take it in."),
         HEADER]
    for n, pv in moving:
        lo, hi = (pv.get("range") or (0, 0))[:2]
        src = f"element.py (node {n}: {pv.get('kind')} {lo:g} to {hi:g})"
        L += [f"state,{n}-rest,,{n},default,,,{src},", f"state,{n}-end,,{n},manual toggle,,,{src},", f"pose,{n},,,{n}-end,end,,{src},"]
    return "\n".join(L) + "\n", ""

def describe(eid):
    S = spec(eid)
    if S is None: return f"{eid}: no behaviour.csv"
    L = [f"{eid} · behaviour.csv", f"  pins: " + " ".join(f"{m}@{n or '-'}" for m, n in S["pins"].items())]
    for part, lst in S["states"].items():
        L.append(f"  states of {part}: " + "; ".join(("(hold the previous state)" if d == "hold" else f"{n} [{'default' if d else ('manual ' + m[0] + (' cleared by ' + m[1] if m[1] else '')) if m else w.text}]") for n, w, m, d in lst))
    for a, b, part, w, R in S["contacts"]: L.append(f"  contact {a}-{b} ({part}) closed when {w.text}" + (f", {R} ohm" if R else ""))
    for a, b, part, w, v, u in S["loads"]: L.append(f"  load {a}-{b} ({part}) {v} {u}" + (f" when {w.text}" if w else ""))
    for a, b, part, w, v, u, _ in S["sources"]: L.append(f"  source {a}-{b} ({part}) {v} {u}" + (f" when {w.text}" if w else ""))
    for nodes, when, amt in S["poses"]: L.append(f"  pose {' '.join(nodes)} = {amt} when {when}")
    for a, b in S["links"]: L.append(f"  link {a} follows {b}")
    return "\n".join(L)
