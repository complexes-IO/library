"""The solver (lib/behaviour.md; EM 2026-11-09: "the behaviors should emerge from the complete set"). Nothing here knows what a
motor starter is. It takes the elements placed in an assembly, each with its behaviour spec (toolkit/behaviour.py), the wires between
their pins (wires.csv: from, to as <tag>.<mark>) and the sources that feed the assembly (sources.csv), and runs the set:
    pins joined by wires and by closed contacts are one net; sources give nets their potential (AC as a phasor, DC as a number);
    a load between two nets sees their difference; every element's state rows are evaluated on what its own loads see; contacts
    follow the states; the nets are rebuilt; until nothing changes (a fixpoint, bounded).
Phase 1 is ideal: a closed contact drops nothing, a load draws its rated current, a wire has no length. The meter reads two nets.
    solve(aid, inputs)             -> Result for one set of operator inputs ({"<tag>.<state>": bool})
    Result.meter(pin_a, pin_b)     -> dict(vac=..., vdc=...) what a meter between two pins reads
    table(aid, P)                  -> every combination of the twin's inputs solved: what the twin reads (toolkit/twin.py)
    python lib/build.py nets <aid> [state=1 ...]   -> prints the nets, the states and the poses
"""
import cmath, csv, itertools, math, os

from . import library, behaviour as BH

ROOT = library.ROOT
MAX_PASSES = 40

def _rows(path):
    if not os.path.isfile(path): return []
    return [{k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(l for l in open(path, encoding="utf-8") if not l.startswith("#")) if r and any((v or "").strip() for v in r.values())]

def wires(aid): return _rows(os.path.join(ROOT, "assemblies", aid, "wires.csv"))
def sources(aid): return _rows(os.path.join(ROOT, "assemblies", aid, "sources.csv"))

def placed(P):
    """{tag: element id} for every placed element of the assembly, nested ones by their full tag"""
    return {t: e for _, _, t, e in getattr(P, "owners", [])}

class Element:
    """one placed element in the solver: its spec, its current states, what its loads see"""
    def __init__(self, tag, eid, S):
        self.tag, self.eid, self.S = tag, eid, S
        self.state = {part: next((n for n, w, m, d in lst if d == "default"), None) for part, lst in S["states"].items()}   # None: no rest state declared
        self.V = {}; self.I = {}                                                      # per load / contact part
    def pin(self, mark): return f"{self.tag}.{mark}"
    def flags(self): return {n: (self.state.get(part) == n) for part, lst in self.S["states"].items() for n, *_ in lst}
    def env(self, pot):
        """pot: pin -> Pot (or None) through the current nets"""
        f = self.flags()
        def vab(a, b): return _mag(pot(self.pin(a)), pot(self.pin(b)))
        return dict(states=f, V=lambda p: self.V.get(p, 0.0), I=lambda p: self.I.get(p, 0.0), Vab=vab)
    def closed(self, pot):
        """[(pin a, pin b, R, part)] of the contacts closed in the current states; R None for an ideal joint (no figure on file)"""
        env = self.env(pot); return [(self.pin(a), self.pin(b), _num(R), part) for a, b, part, w, R in self.S["contacts"] if w.eval(env)]
    def load_edges(self, pot):
        """[(pin a, pin b, R, part)] of the loads with a resistance on file (R, or P at the voltage they saw last pass)"""
        env = self.env(pot); out = []
        for a, b, part, w, val, unit in self.S["loads"]:
            if w and not w.eval(env): continue
            R = _num(val) if unit.lower() in ("ohm", "ω") else None
            if R is None and unit.upper() == "W" and _num(val) and self.V.get(part, 0) > 1: R = self.V[part] ** 2 / _num(val)
            if R: out.append((self.pin(a), self.pin(b), R, part))
        return out
    def step(self, pot, inputs):
        """re-evaluate every state machine on what the loads see and the operator's inputs; True when something changed.
        Rows in order, the first true wins (so a fault row above a command row takes precedence); a manual row is true while its
        input is set; none true: a `hold` row keeps the previous state (hysteresis, declared), otherwise the machine rests at its default."""
        env = self.env(pot); changed = False
        for part, lst in self.S["states"].items():
            new = None; hold = False
            for name, w, m, d in lst:
                if d == "default": continue
                if d == "hold": hold = True; continue
                if (m and inputs.get(f"{self.tag}.{name}", inputs.get(name, False))) or (w and w.eval(env)): new = name; break
            if new is None and not hold: new = next((n for n, w, m, d in lst if d == "default"), None)
            if new is not None and new != self.state.get(part): self.state[part] = new; changed = True
        return changed

def _num(x):
    try: return float(x)
    except (TypeError, ValueError): return None

def nodal(nets, pots, edges, loads):
    """phase 1.5 (lib/flows.md): the node equations over the nets. Ideal joints are already one net; every edge and load with a
    resistance connects two nets by a conductance; nets with a source hold their potential (Dirichlet); the rest are solved
    (G_uu V_u = -G_uf V_f), AC and DC by superposition since G is linear. Nets reachable from no source stay floating (None).
    Returns ({net root: Pot}, {label: (a, b, I complex or float)} the edge currents)."""
    import numpy as np
    all_edges = [(a, b, R, lab) for a, b, R, lab in edges] + [(a, b, R, f"load {lab}") for a, b, R, lab in loads]
    if not all_edges: return pots, {}
    roots = {}
    for a, b, R, lab in all_edges: roots.setdefault(nets.find(a), len(roots)); roots.setdefault(nets.find(b), len(roots))
    for r in pots: roots.setdefault(r, len(roots))
    n = len(roots); G = np.zeros((n, n))
    for a, b, R, lab in all_edges:
        i, j = roots[nets.find(a)], roots[nets.find(b)]; g = 1.0 / R
        G[i, i] += g; G[j, j] += g; G[i, j] -= g; G[j, i] -= g
    # connected components over the edges: a component with no fixed node floats
    comp = list(range(n))
    def find(x):
        while comp[x] != x: comp[x] = comp[comp[x]]; x = comp[x]
        return x
    for a, b, R, lab in all_edges: comp[find(roots[nets.find(a)])] = find(roots[nets.find(b)])
    out = {r: Pot(p.ac, p.dc) for r, p in pots.items()}
    for kind in ("ac", "dc"):
        fixed = {roots[r]: getattr(p, kind) for r, p in pots.items() if getattr(p, kind) is not None}
        if not fixed: continue
        live = {find(i) for i in fixed}                                                 # components that have a source of this kind
        unknown = [i for i in range(n) if i not in fixed and find(i) in live]
        if unknown:
            U = np.array(unknown); Fi = np.array(list(fixed)); Vf = np.array([fixed[i] for i in Fi], dtype=complex if kind == "ac" else float)
            Guu = G[np.ix_(U, U)]; Guf = G[np.ix_(U, Fi)]
            try: Vu = np.linalg.solve(Guu, -Guf @ Vf)
            except np.linalg.LinAlgError: Vu = np.linalg.lstsq(Guu, -Guf @ Vf, rcond=None)[0]
            inv = {i: r for r, i in roots.items()}
            for i, v in zip(U, Vu):
                p = out.setdefault(inv[i], Pot()); setattr(p, kind, complex(v) if kind == "ac" else float(v.real if isinstance(v, complex) else v))
    currents = {}
    for a, b, R, lab in all_edges:
        pa, pb = out.get(nets.find(a)), out.get(nets.find(b))
        if pa is None or pb is None: continue
        iac = ((pa.ac or 0j) - (pb.ac or 0j)) / R if (pa.ac is not None or pb.ac is not None) else 0j
        idc = ((pa.dc or 0.0) - (pb.dc or 0.0)) / R if (pa.dc is not None or pb.dc is not None) else 0.0
        currents[lab] = (a, b, iac, idc)
    return out, currents

def _mag(a, b):
    """what a load between two potentials sees: the AC difference and the DC difference combined (rms). A floating side (nothing
    drives its net) carries no current, so it sits at the other side's potential and the load sees 0, whatever the driven side's
    potential (request panel-14: a comb's milliohm bar put the 0 V blocks µV apart, and a floating side counted as 0 V read that
    offset as a signal). The meter reports a floating side as such (Result.meter)."""
    if a is None or b is None or (a.ac is None and a.dc is None) or (b.ac is None and b.dc is None): return 0.0
    dac = abs((a.ac or 0j) - (b.ac or 0j)); ddc = (a.dc or 0.0) - (b.dc or 0.0)
    return math.hypot(dac, ddc)

class Pot:
    """a net's potential: ac phasor (complex, V rms) and / or dc (V), None where nothing drives it"""
    __slots__ = ("ac", "dc")
    def __init__(self, ac=None, dc=None): self.ac, self.dc = ac, dc
    def __repr__(self): return (f"{abs(self.ac):.1f}∠{math.degrees(cmath.phase(self.ac)):.0f}° VAC" if self.ac is not None else "") + (f" {self.dc:+.1f} VDC" if self.dc is not None else "") or "floating"

class Nets:
    """union-find over pins"""
    def __init__(self): self.p = {}
    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x: self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def join(self, a, b): ra, rb = self.find(a), self.find(b); self.p[ra] = rb if ra != rb else ra
    def groups(self):
        g = {}
        for x in list(self.p): g.setdefault(self.find(x), []).append(x)
        return g

class Result:
    def __init__(self, aid, elements, nets, pots, inputs, passes, stable):
        self.aid, self.elements, self.nets, self.pots, self.inputs, self.passes, self.stable = aid, elements, nets, pots, inputs, passes, stable
    def meter(self, a, b):
        """what a meter reads between two pins (<tag>.<mark>): vac (rms) and vdc; a floating side (nothing drives its net) reads 0
        and is reported (a real meter shows a ghost voltage there: the student learns to doubt a reading on a floating conductor)"""
        pa, pb = self.pots.get(self.nets.find(a)), self.pots.get(self.nets.find(b))
        floating = [p for p, pot in ((a, pa), (b, pb)) if pot is None or (pot.ac is None and pot.dc is None)]
        if floating: return dict(vac=0.0, vdc=0.0, floating=floating)
        vac = abs((pa.ac or 0j) - (pb.ac or 0j)) if (pa.ac is not None or pb.ac is not None) else 0.0
        vdc = (pa.dc or 0.0) - (pb.dc or 0.0) if (pa.dc is not None or pb.dc is not None) else 0.0
        return dict(vac=round(vac, 1), vdc=round(vdc, 2))
    def states(self): return {e.tag: dict(e.state) for e in self.elements.values()}
    def flags(self): return {f"{e.tag}.{n}": v for e in self.elements.values() for n, v in e.flags().items()}
    def over(self):
        """[(<tag>.<part>, V seen, limit, unit)] every load that sees more than its limit row allows (a design error the wiring made)"""
        out = []
        for e in self.elements.values():
            for a, val, unit in e.S["limits"]:
                try: lim = float(val)
                except ValueError: continue
                if unit.upper() in ("VAC", "VDC", "V") and a in e.V and e.V[a] > lim + 1e-6: out.append((f"{e.tag}.{a}", round(e.V[a], 1), lim, unit))
        return out
    def loads(self): return {f"{e.tag}.{p}": dict(V=round(v, 2), I=round(e.I.get(p, 0.0), 3)) for e in self.elements.values() for p, v in e.V.items()}
    def poses(self, P):
        """{<tag>.<node>: amount} for the assembly's pivots in the solved states"""
        out = {}
        for e in self.elements.values():
            sub = _SubPivots(P, e.tag)
            for node, amt in BH.poses(e.S, sub, e.flags()).items(): out[f"{e.tag}.{node}"] = amt
        return out
    def pins_at(self, node):
        """the pins (<tag>.<mark>) whose port node is <tag>.<node> (what a probe on that node touches)"""
        out = []
        for e in self.elements.values():
            if node.startswith(e.tag + "."):
                local = node[len(e.tag) + 1:]
                out += [e.pin(m) for m, n in e.S["pins"].items() if n == local or (n == "" and m == local)]
                out += [e.pin(m) for marks in e.S.get("forms", {}).values() for m, n in marks.items() if n == local and e.pin(m) not in out]   # a form's node (cordset-m12 open end)
        return out

class _SubPivots:
    """the assembly's pivots seen from one placed element (its tag stripped), for behaviour.poses"""
    def __init__(self, P, tag):
        pre = tag + "."; self.pivots = {n[len(pre):]: pv for n, pv in P.pivots.items() if n.startswith(pre)}
        if tag in P.pivots: self.pivots["self"] = P.pivots[tag]                          # a placed element's own node carries its tag
        self.owners = [(a, b, t[len(pre):], e) for a, b, t, e in getattr(P, "owners", []) if t.startswith(pre)]

def _assembly(aid):
    import importlib.util
    p = os.path.join(ROOT, "assemblies", aid, "assembly.py")
    sp = importlib.util.spec_from_file_location(f"asmN_{aid.replace('-', '_')}", p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m.build(report=False)

def _counted(S, tag, P):
    """an element whose pins follow a parameter (behaviour.md `count <param>>=<k>`: term-jumper's blades, request panel-13 2): its
    count pins are the solver's where the placed build has their node, and a contact, load or source naming a count pin the build
    lacks is not in the solver (a 2-pole comb has blades 1 and 2 only; a 7-pole comb 1 to 7). Elements with no count stand as read."""
    C = S.get("counts") or {}
    if not C: return S
    pre = tag + "."; have = {n[len(pre):] for n in getattr(P, "pivots", {}) if n.startswith(pre)}
    pins = dict(S["pins"]); pins.update({m: n for m, (n, prm, k) in C.items() if n in have})
    gone = set(C) - set(pins)
    keep = lambda a, b: a not in gone and b not in gone
    return dict(S, pins=pins, contacts=[c for c in S["contacts"] if keep(c[0], c[1])], loads=[x for x in S["loads"] if keep(x[0], x[1])],
                sources=[x for x in S["sources"] if keep(x[0], x[1])])

def elements(P, specs=None):
    """{tag: Element} for every placed element with a behaviour spec (specs: {eid: spec} to override, for tests)"""
    out = {}
    for tag, eid in placed(P).items():
        S = (specs or {}).get(eid) or BH.spec(eid)
        if S: out[tag] = Element(tag, eid, _counted(S, tag, P))
    return out

def solve(aid, inputs=None, P=None, W=None, SRC=None, specs=None, E=None):
    """one solution: inputs {"<tag>.<state>": True} for the operator's manual states (a bare state name applies to every element
    that has it). W / SRC / specs / E override the files (tests)."""
    inputs = inputs or {}
    P = P if P is not None else _assembly(aid)
    E = E if E is not None else elements(P, specs)
    W = wires(aid) if W is None else W; SRC = sources(aid) if SRC is None else SRC
    nets = Nets(); pots = {}; passes = 0; stable = False; currents = {}; edges = []
    pot = lambda pin: pots.get(nets.find(pin)) if nets is not None else None
    for e in E.values(): e.step(lambda pin: None, inputs)                            # the operator's inputs first
    while passes < MAX_PASSES:
        passes += 1
        nets = Nets(); edges = []                                                    # edges: (pin a, pin b, R ohm, label) with a resistance (phase 1.5, lib/flows.md)
        for i, w in enumerate(W, 1):
            if w.get("when") and not inputs.get(w["when"], False): continue           # an outside contact an operator's input stands for
            R = _num(w.get("r_ohm"))
            if R: edges.append((w["from"], w["to"], R, f"wire {w.get('wire') or i}"))
            else: nets.join(w["from"], w["to"])
        for e in E.values():
            for a, b, R, part in e.closed(pot):
                if R: edges.append((a, b, R, f"{e.tag}.{part}"))
                else: nets.join(a, b)
        for e in E.values():
            for mark in e.S["pins"]: nets.find(e.pin(mark))
        pots = {}
        for s in SRC:                                                                   # the assembly's own sources: absolute potentials
            if s.get("when") and not inputs.get(s["when"], False): continue             # a source from outside that an operator's input stands for
            r = nets.find(s["pin"]); v = float(s["value"]); p = pots.setdefault(r, Pot())
            if s["kind"].upper() == "VAC": p.ac = cmath.rect(v, math.radians(float(s.get("phase") or 0)))
            else: p.dc = v
        for _ in range(3):                                                              # element sources (a PSU): relative to what they see
            for e in E.values():
                env = e.env(pot)
                for a, b, part, w, val, unit, _src in e.S["sources"]:
                    if w and not w.eval(env): continue
                    try: v = float(val)
                    except ValueError: continue
                    ra, rb = nets.find(e.pin(a)), nets.find(e.pin(b)); pa, pb = pots.get(ra), pots.get(rb)
                    if unit.upper() == "VAC":
                        if pb is not None and pb.ac is not None: pots.setdefault(ra, Pot()).ac = pb.ac + v
                        elif pa is not None and pa.ac is not None: pots.setdefault(rb, Pot()).ac = pa.ac - v
                        else: pots.setdefault(rb, Pot()).ac = 0j; pots.setdefault(ra, Pot()).ac = complex(v, 0)
                    else:
                        if pb is not None and pb.dc is not None: pots.setdefault(ra, Pot()).dc = pb.dc + v
                        elif pa is not None and pa.dc is not None: pots.setdefault(rb, Pot()).dc = pa.dc - v
                        else: pots.setdefault(rb, Pot()).dc = 0.0; pots.setdefault(ra, Pot()).dc = v
        loads = [x for e in E.values() for x in e.load_edges(pot)]
        pots, currents = nodal(nets, pots, edges, loads)                                 # phase 1.5: drops along resistive edges
        for e in E.values():                                                            # what every load sees
            for a, b, part, w, val, unit in e.S["loads"]:
                env = e.env(pot)
                if w and not w.eval(env): e.V[part] = 0.0; e.I[part] = 0.0; continue
                v = _mag(pot(e.pin(a)), pot(e.pin(b))); e.V[part] = v
                try: R = float(val) if unit.lower() in ("ohm", "ω") else None; Pw = float(val) if unit.upper() == "W" else None
                except ValueError: R = Pw = None
                e.I[part] = (v / R if R else (Pw / v if (Pw and v > 1) else 0.0))     # a power-rated load is a resistance past 1 V only (load_edges)
        changed = any([e.step(pot, inputs) for e in E.values()])                    # every element steps (no short-circuit)
        if not changed: stable = True; break
    R_ = Result(aid, E, nets, pots, inputs, passes, stable); R_.currents = currents; R_.edges = edges
    return R_

def input_names(E, SRC=(), W=()):
    """the operator's inputs of the assembly: {"<tag>.<state>": dict(kind, cleared_by, part, tag, state)}, plus the sources.csv rows
    an input stands for ({"<when>": dict(kind="toggle", source=True)})"""
    out = {}
    for e in E.values():
        for name, d in e.S["inputs"].items(): out[f"{e.tag}.{name}"] = dict(d, tag=e.tag, state=name)
    for s in list(SRC) + list(W or []):
        if s.get("when"): out.setdefault(s["when"], dict(kind="toggle", cleared_by="", part="", tag="", state=s["when"], source=True))
    return out

def table(aid, P=None, E=None, W=None, SRC=None, names=None, specs=None):
    """every combination of the assembly's manual inputs (or `names`, a subset) solved: [(inputs, Result)]"""
    P = P if P is not None else _assembly(aid); E = E if E is not None else elements(P, specs)
    SRC = sources(aid) if SRC is None else SRC
    W = wires(aid) if W is None else W
    names = names or sorted(input_names(E, SRC, W))
    out = []
    for bits in itertools.product((False, True), repeat=len(names)):
        inp = dict(zip(names, bits)); out.append((inp, solve(aid, inp, P=P, W=W, SRC=SRC, E=E)))
        for e in E.values(): e.__init__(e.tag, e.eid, e.S)                              # fresh states per combination
    return out

def describe(aid, inputs=None):
    P = _assembly(aid); E = elements(P); r = solve(aid, inputs or {}, P=P, E=E); SRC = sources(aid)
    L = [f"{aid} · {len(E)} elements with a spec, {len(wires(aid))} wires, {len(sources(aid))} sources; {r.passes} passes, {'stable' if r.stable else 'NOT STABLE'}",
         "inputs: " + (", ".join(f"{k}={'1' if v else '0'}" for k, v in sorted(r.inputs.items())) if r.inputs else "none set") + " (of " + ", ".join(sorted(input_names(E, SRC, wires(aid)))) + ")"]
    for root, pins in sorted(r.nets.groups().items(), key=lambda kv: -len(kv[1])):
        if len(pins) < 2 and root not in r.pots: continue
        L.append(f"  net {r.pots.get(root, Pot())!r:>24}: " + " ".join(sorted(pins)))
    for tag, st in sorted(r.states().items()): L.append(f"  {tag}: " + ", ".join(f"{p}={s}" for p, s in st.items()))
    for k, v in sorted(r.loads().items()): L.append(f"  load {k}: {v['V']} V, {v['I']} A")
    for part, v, lim, unit in r.over(): L.append(f"  OVER {part}: sees {v} V, rated {lim} {unit}")
    return "\n".join(L)
