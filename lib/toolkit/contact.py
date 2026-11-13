"""Contacts: where two conductors meet, and whether they do. A cable's wiring map says which pin should meet which; whether it does
depends on how the parts sit: the key, how far the coupling nut is turned, the state of each pin. This module reads that from the
elements themselves, so a half-turned nut, a bent pin or a wrong coding gives the twin the same symptom it gives a technician.

Element data (pivots, exported to the glTF extras for the binder):
  contact  a contact element's node. origin: a pin's tip, a socket's mouth. axis: the way the pin travels to engage (a pin: root to
           tip; a socket: mouth to bottom). range (s0, s1): the contact zone, mm from the origin into the part (a pin: its plain shank
           from the end of the lead-in to the carrier face; a socket: from where the springs first touch to the bottom of the bore).
           extras: pole, gender (pin | socket), d (mm), wipe (mm of overlap for a reliable contact), r (mΩ when made), condition;
           a socket's face (mm: how far the insert face stands in front of its mouth, where an off-axis pin stops).
  port     a connector's mating face. origin on the axis in the mating plane, axis out of the face; extras: gender (male: pins,
           female: sockets), coding, keyref (the key's direction), key_tol (deg), key_gap (mm: the gap at which a key that does not fit
           stops the plug), thread_span (mm: this half's thread, measured ahead of its mating plane; the catch and the length
           engaged come from both halves), thread_gap (the catch against a standard counterpart), pitch (mm per turn), seal (mm of
           squeeze at the seat), torque (N m, min and max).

States of a pin and its socket: made (overlap ≥ wipe), marginal (0 < overlap < wipe: works on the bench, drops out under vibration or
heat), open, high-r (made, but corroded or a spread spring), blocked (a bent pin: it meets the insert face and the plug cannot seat)."""
import math
import numpy as np
from .solid import rotation

CONDITIONS = {"pin": ("ok", "bent", "pushed-back", "broken", "corroded"), "socket": ("ok", "spread", "corroded", "missing")}
LATERAL = 0.15          # mm: a pin further than this off its socket's axis does not enter it (Assumption: about the bore clearance)

def contacts(P):
    """{node: pivot} of every contact in a Prims list"""
    return {n: pv for n, pv in P.pivots.items() if pv["kind"] == "contact"}

def ports(P):
    return {n: pv for n, pv in P.pivots.items() if pv["kind"] == "port" and "gender" in pv}

def _under(P, port_node):
    """the contacts that belong to a port: nodes under the same placed instance as the port node (tag.*)"""
    if port_node == "self": return contacts(P)
    return {n: pv for n, pv in contacts(P).items() if n.startswith(port_node + ".")}

def pair(pin, sock, T=None, M=None, a_p=None, a_s=None):
    """state of one pin in one socket (pivot dicts, world frame unless T, M, a_p, a_s override tip, mouth and axes):
    dict(state, overlap, depth, lateral, r)"""
    T = np.array(T if T is not None else pin["origin"], float); M = np.array(M if M is not None else sock["origin"], float)
    ap = np.array(a_p if a_p is not None else pin["axis"], float); ap /= np.linalg.norm(ap)
    asx = np.array(a_s if a_s is not None else sock["axis"], float); asx /= np.linalg.norm(asx)
    d = float((T - M) @ asx); lat = float(np.linalg.norm((T - M) - asx * d)); par = float(ap @ asx)
    pc, sc = pin.get("condition", "ok"), sock.get("condition", "ok")
    res = dict(depth=round(d, 3), lateral=round(lat, 3), overlap=0.0, r=None)
    if sc == "missing" or pc == "broken": return dict(res, state="open")
    face = float(sock.get("face", 0.0))                                         # the insert face stands this far in front of the mouth
    if par < math.cos(math.radians(3)) or lat > LATERAL:                        # off its socket: it meets the insert face around it
        return dict(res, state="blocked", stop=d + face) if d >= -face - 0.05 - 1e-9 else dict(res, state="open")   # resting on the face: blocked
    s0p, s1p = (float(v) for v in pin["range"]); s0s, s1s = (float(v) for v in sock["range"])
    ov = min(d - s0p, s1s) - max(d - s1p, s0s); res["overlap"] = round(max(0.0, ov), 3)
    wipe = max(float(pin.get("wipe", 0.5)), float(sock.get("wipe", 0.5)))
    if d > s1s + 1e-6: return dict(res, state="blocked", stop=d - s1s)            # the tip is on the bottom of the bore: over-driven
    if ov <= 0: return dict(res, state="open")
    if sc == "spread" or ov < wipe: return dict(res, state="marginal")
    r = float(pin.get("r", 5.0)) + float(sock.get("r", 5.0))
    if "corroded" in (pc, sc): return dict(res, state="high-r", r=r * 100)
    return dict(res, state="made", r=r)

def _frame(pv):
    a = np.array(pv["axis"], float); a /= np.linalg.norm(a); k = np.array(pv.get("keyref", (0, 0, 1)), float); k = k - a * (k @ a); k /= np.linalg.norm(k)
    return np.array(pv["origin"], float), a, k

def seat(port, plug, key_err=0.0, gap=0.0):
    """the rigid move (R, t) that brings a plug's mating face onto a port's: axes opposed, keys aligned (plus key_err degrees about the
    port axis), the plug `gap` mm short of the seat"""
    O1, a1, k1 = _frame(port); O2, a2, k2 = _frame(plug)
    A = np.column_stack([-a2, k2, np.cross(-a2, k2)]); B = np.column_stack([a1, k1, np.cross(a1, k1)])
    R = rotation(a1, key_err) @ B @ A.T
    t = O1 + a1 * gap - R @ O2
    return R, t

def mate(port_P, port_node, plug_P, plug_node, turns=None, gap=None, key_err=0.0, torque=None):
    """what a technician gets when plug (plug_P, its port node) meets port (port_P, its port node).
    gap: mm short of the seat, or turns: coupling-nut turns after the thread caught (pushed home by hand to the thread first).
    Returns dict(gap, seated, sealed, key, gender, coding, poles={pole: pair state}, made=[poles], notes=[...])."""
    pp, qp = port_P.pivots[port_node], plug_P.pivots[plug_node]; notes = []
    gender_ok = pp.get("gender") != qp.get("gender"); coding_ok = pp.get("unit") == qp.get("unit")
    key_ok = coding_ok and abs(key_err) <= float(pp.get("key_tol", 5.0))
    g_thr, engaged = threads(pp, qp); pitch = float(pp.get("pitch", 1.0))
    if gap is None: gap = g_thr if turns is None else max(0.0, g_thr - pitch * float(turns))
    gap = float(gap)
    if not gender_ok: notes.append(f"both halves are {pp.get('gender')}: they do not mate"); gap = max(gap, float(pp.get("key_gap", 5.0)) + 5.0)
    elif not key_ok:
        g_key = float(pp.get("key_gap", 5.0)); notes.append(("coding " + str(qp.get("unit")) + " into " + str(pp.get("unit")) if not coding_ok else f"key {key_err:+.0f}° off") + f": the key stops the plug {g_key:g} mm short")
        gap = max(gap, g_key)
    R, t = seat(pp, qp, key_err if key_ok else 0.0, gap)
    def world(pv, moved):
        o, a = np.array(pv["origin"], float), np.array(pv["axis"], float)
        return (R @ o + t, R @ a) if moved else (o, a)
    by_pole = {}                                    # pins and sockets from both halves: an L-coded FE pin sits in the female half
    for moved, side in ((False, _under(port_P, port_node)), (True, _under(plug_P, plug_node))):
        for n, pv in side.items():
            g = pv.get("gender")
            if g in ("pin", "socket"): by_pole.setdefault(str(pv.get("pole")), {})[g] = (n, pv, moved)
    poles = {}
    for pole, d in sorted(by_pole.items()):
        if "pin" not in d or "socket" not in d: poles[pole] = dict(state="open", note="no counterpart"); continue
        (_, pin, mp), (_, so, ms) = d["pin"], d["socket"]
        T, ap = world(pin, mp); M, as_ = world(so, ms)
        poles[pole] = pair(pin, so, T, M, ap, as_)
    blocked = [p for p, s in poles.items() if s["state"] == "blocked"]
    if blocked and gender_ok and key_ok:
        notes.append(f"pin {', '.join(blocked)} meets the face around its socket: the plug cannot seat")
        # the plug stops where the first blocking pin meets the insert face (or the bottom of its bore): everything is re-evaluated there
        g2 = gap + max(0.0, max(poles[p].get("stop", poles[p]["depth"]) for p in blocked) + 0.05)
        if g2 > gap + 1e-6:
            res = mate(port_P, port_node, plug_P, plug_node, gap=g2, key_err=key_err, torque=torque)
            res["notes"] = notes + [n for n in res["notes"] if n not in notes]; return res
    seated = gap <= 0.05 and gender_ok and key_ok
    tq = float(torque) if torque is not None else (float(pp["torque"][0]) if seated and "torque" in pp else 0.0)
    sealed = seated and "torque" in pp and tq >= float(pp["torque"][0])
    if seated and not sealed: notes.append(f"seated but torque {tq:g} N m < {pp['torque'][0]} N m: not sealed, and it can work loose")
    made_now = [p for p, s in poles.items() if s["state"] in ("made", "high-r", "marginal")]
    if made_now and not seated and gender_ok and key_ok:
        notes.append(f"{len(made_now)} pole(s) touching {gap:g} mm short of the seat" + (", before the nut has caught the thread" if gap >= g_thr - 1e-6 else ", the nut not home")
                     + ": held by the contacts' friction only, not sealed; it works loose under vibration (intermittent)")
    if "torque" in pp and torque is not None and float(torque) > float(pp["torque"][1]) + 1e-9:
        notes.append(f"torque {float(torque):g} N m over {pp['torque'][1]} N m: the nut or the receptacle's thread can be damaged")
    return dict(gap=round(gap, 3), seated=seated, sealed=sealed, gender=gender_ok, coding=coding_ok, key=key_ok, poles=poles,
                made=[p for p, s in poles.items() if s["state"] in ("made", "high-r")], notes=notes, thread_catch=g_thr, thread_engaged=engaged)

def threads(pp, qp):
    """(the gap at which the threads catch, the length engaged at the seat) from the two mating faces' thread spans (toolkit/m12.py
    engagement); a face without a span falls back on the port's thread_gap"""
    a, b = pp.get("thread_span"), qp.get("thread_span")
    if a is not None and b is not None and pp.get("gender") != qp.get("gender"):
        ms, fs = (a, b) if pp.get("gender") == "male" else (b, a)
        m_lo, m_hi = (float(v) for v in ms); f_lo, f_hi = (float(v) for v in fs)
        return round(f_hi + m_hi, 3), round(min(-m_lo, f_hi) - max(-m_hi, f_lo), 3)
    g = float(pp.get("thread_gap", 4.0)); return g, g

def window(port_P, port_node, plug_P, plug_node, step=0.05, top=6.0):
    """gap ranges per pole: {pole: (made below, marginal below, open above)} as the plug comes home: the pins' engagement window"""
    out = {}
    g = top
    while g >= -1e-9:
        r = mate(port_P, port_node, plug_P, plug_node, gap=g)
        for p, s in r["poles"].items():
            w = out.setdefault(p, dict(first_touch=None, made_at=None))
            if s["state"] != "open" and w["first_touch"] is None: w["first_touch"] = round(g, 3)
            if s["state"] in ("made", "high-r") and w["made_at"] is None: w["made_at"] = round(g, 3)
        g -= step
    return out

# ------------------------------------------------------------------ a wire end in a clamp
def terminate(clamp, wire, depth=None, torque=None, T=None, M=None, a_w=None, a_c=None):
    """state of a prepared wire end in a screw clamp (pivot dicts: clamp kind contact gender clamp; wire end kind contact gender wire).
    depth: how far the tip went past the clamp's mouth (default: from where the parts are); torque on the clamp screw, N m (default the
    window's minimum). Returns dict(state, depth, bare, insulation, notes): state made | marginal | open | high-r | blocked."""
    notes = []
    T = np.array(T if T is not None else wire["origin"], float); M = np.array(M if M is not None else clamp["origin"], float)
    aw = np.array(a_w if a_w is not None else wire["axis"], float); aw /= np.linalg.norm(aw)
    ac = np.array(a_c if a_c is not None else clamp["axis"], float); ac /= np.linalg.norm(ac)
    if depth is None:
        depth = float((T - M) @ ac); lat = float(np.linalg.norm((T - M) - ac * depth))
        if aw @ ac < math.cos(math.radians(10)) or lat > min(clamp.get("window", (4.0, 5.0))) / 2 - float(wire.get("d", 1.4)) / 2:
            return dict(state="blocked" if depth > -0.5 else "open", depth=round(depth, 2), bare=0.0, insulation=0.0, notes=["the wire is not on the clamp's axis"])
    depth = float(depth); size = float(wire.get("size", 1.5))
    tq = float(torque) if torque is not None else float(clamp["torque"][0])
    res = dict(depth=round(depth, 2), bare=0.0, insulation=0.0)
    if size > float(clamp.get("size_max", 1e9)) + 1e-9: return dict(res, state="blocked", notes=[f"{size:g} mm² is over the clamp's {clamp['size_max']:g} mm²: it does not go in"])
    z0, z1 = (float(v) for v in clamp["range"]); zone = float(wire["range"][1])
    bare = min(depth, z1) - max(depth - zone, z0); res["bare"] = round(max(0.0, bare), 2)
    ins = min(depth - zone, z1) - z0; res["insulation"] = round(max(0.0, ins), 2)                          # insulation reaching under the clamp
    if depth - zone < -1.0: notes.append(f"{-(depth - zone):.1f} mm of bare conductor outside the clamp: touchable")
    if wire.get("condition") == "strands-out": notes.append("stray strands outside the clamp: a short to the neighbour is waiting")
    if size < float(clamp.get("size_min", 0)) - 1e-9: notes.append(f"{size:g} mm² is under the clamp's {clamp['size_min']:g} mm²: it is not gripped"); return dict(res, state="marginal", notes=notes)
    if tq <= 0: notes.append("the screw is not tightened"); return dict(res, state="open", notes=notes)
    if bare <= 0: notes.append("the clamp grips insulation only" if ins > 0 else "the conductor does not reach the clamp"); return dict(res, state="open", notes=notes)
    grip = float(clamp.get("grip", 5.0))
    if ins > 0.3: notes.append(f"insulation {ins:.1f} mm under the clamp")
    if tq < float(clamp["torque"][0]) - 1e-9: notes.append(f"torque {tq:g} N m under {clamp['torque'][0]} N m: it works loose and heats under load"); return dict(res, state="marginal", notes=notes)
    if bare < grip: notes.append(f"only {bare:.1f} mm of conductor under the clamp (needs {grip:g})"); return dict(res, state="marginal", notes=notes)
    if tq > float(clamp["torque"][1]) + 1e-9: notes.append(f"torque {tq:g} N m over {clamp['torque'][1]} N m: strands crushed"); return dict(res, state="high-r", notes=notes)
    if "corroded" in (wire.get("condition"), clamp.get("condition")) or wire.get("condition") == "nicked":
        notes.append("corroded or nicked: made, but with resistance that heats"); return dict(res, state="high-r", notes=notes)
    return dict(res, state="made", notes=notes)
