"""lib/core/src/generated.rs from the elements: the M12 halves the Rust core and its Kani proofs work on, in whole micrometres.
Run by `python lib/build.py core`. Every figure comes from the element as built (its pivots: the same data the glTF extras carry), so
the proofs check the rules against the parts, and a changed element changes the proofs' data on the next build.
Also writes the golden cases: what toolkit/contact.py says for a set of poses, for the Rust tests to agree with (differential test)."""
import math, os
import numpy as np
from . import library, contact as C, m12

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "core", "src", "generated.rs")
HALVES = [  # (rust name, element, gender, coding): the halves the cell uses
    ("DEV_F_A", "receptacle-m12", "female", "A"), ("DEV_M_A", "receptacle-m12", "male", "A"),
    ("CORD_M_A", "plug-m12", "male", "A"), ("CORD_F_A", "plug-m12", "female", "A"),
    ("DEV_F_D", "receptacle-m12", "female", "D"), ("CORD_M_D", "plug-m12", "male", "D"),
    ("DEV_F_L", "receptacle-m12", "female", "L"), ("DEV_M_L", "receptacle-m12", "male", "L"),
    ("CORD_M_L", "plug-m12", "male", "L"), ("CORD_F_L", "plug-m12", "female", "L")]
JOINTS = [("DEV_F_A", "CORD_M_A"), ("DEV_M_A", "CORD_F_A"), ("DEV_F_D", "CORD_M_D"), ("DEV_F_L", "CORD_M_L"), ("DEV_M_L", "CORD_F_L")]
GAPS = [0.0, 1.0, 1.45, 2.5, 3.0, 4.4, 4.7, 5.0, 6.5, 9.0]
COND = {"pin": ("ok", "bent", "pushed-back", "broken", "corroded"), "socket": ("ok", "spread", "corroded", "missing")}
RUST_COND = {"ok": "Ok", "bent": "Bent", "pushed-back": "PushedBack", "broken": "Broken", "corroded": "Corroded", "spread": "Spread", "missing": "Missing"}

def um(v): return int(round(float(v) * 1000.0))

def _contact(pv, cond, missing_pole=None):
    o = [um(v) for v in pv["origin"]]; a = np.array(pv["axis"], float); a /= np.linalg.norm(a)
    par = abs(a[1]) >= math.cos(math.radians(3)); d_ = 1 if a[1] > 0 else -1
    s0, s1 = (um(v) for v in pv["range"])
    return (f'ContactDef {{ pole: {int(pv["pole"])}, kind: Kind::{"Pin" if pv["gender"] == "pin" else "Socket"}, cond: Cond::{RUST_COND[cond]}, '
            f'origin: [{o[0]}, {o[1]}, {o[2]}], dir: {d_}, parallel: {"true" if par else "false"}, range: ({s0}, {s1}), '
            f'wipe: {um(pv.get("wipe", 0.5))}, face: {um(pv.get("face", 0.0))}, r_mohm: {int(round(float(pv.get("r", 5.0))))} }}')

def _half(name, eid, gender, coding):
    mod = library.load(eid); P = mod.build(**{**mod.PARAMS, "gender": gender, "coding": coding}); pp = P.pivots["self"]
    ok = C._under(P, "self"); poles = sorted(ok.items(), key=lambda kv: int(kv[1]["pole"]))
    base = [_contact(pv, "ok") for _, pv in poles]
    variants = []
    for _, pv in poles:
        pole = str(pv["pole"])
        for c in COND[pv["gender"]][1:]:
            if c == "missing": variants.append(_contact(pv, "missing")); continue
            Q = mod.build(**{**mod.PARAMS, "gender": gender, "coding": coding, "conditions": f"{pole}:{c}"})
            qv = next(v for v in C._under(Q, "self").values() if str(v["pole"]) == pole); variants.append(_contact(qv, c))
    lo, hi = (um(v) for v in pp["thread_span"]); t0, t1 = (int(round(float(v) * 1000)) for v in pp["torque"])
    head = (f'pub static {name}: HalfDef = HalfDef {{ name: "{eid} {gender} {coding} ({pp.get("half", "")})", gender: Gender::{gender.capitalize()}, '
            f'coding: Coding::{coding}, key_gap: {um(pp["key_gap"])}, key_tol_mdeg: {int(round(float(pp["key_tol"]) * 1000))}, '
            f'thread_span: ({lo}, {hi}), pitch: {um(pp["pitch"])}, torque_mnm: ({t0}, {t1}), contacts: &[\n        ' + ",\n        ".join(base) +
            "],\n    variants: &[\n        " + ",\n        ".join(variants) + "] };")
    return head, (mod, P, gender, coding, eid)

def _golden(halves):
    """(port, plug, gap µm, conditions on the plug, expected seated, gap after, per-pole states) from toolkit/contact.py"""
    rows = []
    for a, b in JOINTS:
        (ma, Pa, ga, ca, ea), (mb, Pb, gb, cb, eb) = halves[a], halves[b]
        plug_conds = [""] + [f"{p}:{c}" for p, c in (("2", "bent"), ("4", "pushed-back"), ("3", "corroded"), ("1", "broken"))]
        for cond in plug_conds:
            Q = mb.build(**{**mb.PARAMS, "gender": gb, "coding": cb, "conditions": cond}) if cond else Pb
            for g in GAPS:
                r = C.mate(Pa, "self", Q, "self", gap=g)
                st = ", ".join(f'({int(p)}, State::{ {"made": "Made", "marginal": "Marginal", "open": "Open", "high-r": "HighR", "blocked": "Blocked"}[s["state"]] })' for p, s in sorted(r["poles"].items()))
                cp, cc = (cond.split(":") + ["", ""])[:2] if cond else ("0", "ok")
                rows.append(f'Golden {{ port: &{a}, plug: &{b}, plug_pole: {int(cp or 0)}, plug_cond: Cond::{RUST_COND[cc or "ok"]}, gap: {um(g)}, '
                            f'seated: {"true" if r["seated"] else "false"}, gap_after: {um(r["gap"])}, poles: &[{st}] }}')
    return rows

def write():
    halves, src = {}, []
    for name, eid, g, c in HALVES:
        s, info = _half(name, eid, g, c); src.append(s); halves[name] = info
    gold = _golden(halves)
    txt = ("// GENERATED by `python lib/build.py core` (toolkit/coregen.py) from the elements as built. Do not edit: change the element.\n"
           f"// toolkit/m12.py: key tolerance {m12.KEY_TOL} deg, torque {m12.TORQUE} N m. Lengths in whole micrometres.\n"
           "use crate::joint::{ContactDef, HalfDef, Kind, Cond, Gender, Coding, Golden, State};\n\n" + "\n\n".join(src) +
           "\n\npub static HALVES: [&HalfDef; %d] = [%s];\n" % (len(HALVES), ", ".join(f"&{n}" for n, *_ in HALVES)) +
           "pub static JOINTS: [(&HalfDef, &HalfDef); %d] = [%s];\n" % (len(JOINTS), ", ".join(f"(&{a}, &{b})" for a, b in JOINTS)) +
           "\n/// what toolkit/contact.py says for these poses: the Rust rules must agree (tests/golden)\npub static GOLDEN: &[Golden] = &[\n    " + ",\n    ".join(gold) + "];\n")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    from . import outfile; outfile.write(OUT, txt, newline="\n")
    return OUT, len(HALVES), len(gold)
